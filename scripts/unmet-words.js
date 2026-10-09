#!/usr/bin/env node
// Words an exercise uses before the course has taught them (ROADMAP 153).
//
// Runs every target-language word of a unit's exercises through the Reader's
// own Lexicon.lookup() and checks its lemma against what the learner has met
// by that lesson ("met" as in docs/unit-finish-brief.md step 4):
//   - a vocabulary list at or before the lesson (word-lesson-index.json, the
//     first lesson that lists the lemma; phrase entries count word by word),
//   - an earlier lesson's grammar screen: its tables and the single words it
//     italicises (*ez*, *az*), not the example sentences,
//   - the lesson's own grammar screens, in full (its examples are allowed),
//   - every lesson of an earlier level.
// A word is met if its surface form or any reading's lemma is. Forms are not
// checked: *címem* passes once *cím* is met, though the -m possessive may not
// be taught yet. That stays a reader's job, as do names (capitalised words
// with no dictionary reading are skipped).
//
//   node scripts/unmet-words.js <course> [level] [--stems a1-21,a1-22]
//
// Prints JSON: [{stem, id, word, first}] with `first` the stem that first
// teaches the word, or null if no lesson does. scripts/check-content.py runs
// it for the `unmet-word` check; run it alone to see a unit's list.

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const args = process.argv.slice(2);
const flag = name => { const i = args.indexOf(name); return i === -1 ? null : args[i + 1]; };
const positional = args.filter((a, i) => !a.startsWith('--') && !(args[i - 1] || '').startsWith('--'));
const course = positional[0];
const onlyLevel = positional[1] || null;
const onlyStems = flag('--stems') ? new Set(flag('--stems').split(',')) : null;
if (!course) { console.error('usage: unmet-words.js <course> [level] [--stems a,b]'); process.exit(2); }

const root = path.resolve(__dirname, '..');
process.chdir(root);

// ---- headless browser shims (same as audit-reader-coverage.js) ----
global.window = global;
const store = {};
global.localStorage = {
    getItem: k => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: k => { delete store[k]; }
};
global.document = { addEventListener() {}, dispatchEvent() {} };
global.CustomEvent = class CustomEvent {};
global.fetch = async url => {
    const p = path.resolve(root, String(url).replace(/^\.\//, '').replace(/\?.*$/, ''));
    if (!fs.existsSync(p)) return { ok: false, status: 404, json: async () => ({}) };
    return { ok: true, status: 200, json: async () => JSON.parse(fs.readFileSync(p, 'utf8')) };
};
const load = rel => vm.runInThisContext(fs.readFileSync(path.join(root, rel), 'utf8'), { filename: rel });
load('engine/lang.js');
load('engine/morphology/spanish.js');
load('engine/morphology/hungarian.js');
load('engine/lexicon.js');

const WORD_RE = /[a-zA-ZÀ-ÖØ-öø-ɏ]+/g;
const LEVELS = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2'];
const readJson = rel => { try { return JSON.parse(fs.readFileSync(path.join(root, rel), 'utf8')); } catch (e) { return null; } };
const lower = s => s.toLocaleLowerCase();
const tokens = s => (String(s || '').match(WORD_RE) || []);
const italics = s => [...String(s || '').matchAll(/\*([^*]+)\*/g)].map(m => m[1]);

// English option strings and quoted English glosses aren't target text.
const ENGLISH = new Set(('the an to are was were of and in on at for with my your his her its it i you he she we ' +
    'they do does did not this that have has what which who how why will would can could should there their from ' +
    'by or but if than then them these those our us am been being very only because one means mean word').split(' '));
// Number words are built from met parts (*tizen* + *három*): a token made only of
// met number roots counts as met.
const NUMBER_ROOTS = {
    hu: ['egy', 'kettő', 'két', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc', 'tíz', 'tizen', 'húsz', 'huszon',
         'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven', 'száz', 'ezer'],
};

// Course order: every stem with its position.
const order = new Map();
const levelOf = new Map();
for (const level of LEVELS) {
    for (const u of readJson(`content/${course}/curriculum/units/${level}.json`) || []) {
        for (const stem of u.stems || []) { order.set(stem, order.size); levelOf.set(stem, level); }
    }
}

// Words met through vocabulary lists: word -> earliest position.
const firstAt = new Map();
const meet = (word, pos) => {
    const w = lower(word);
    if (!firstAt.has(w) || firstAt.get(w) > pos) firstAt.set(w, pos);
};
const index = (readJson(`content/${course}/indexes/word-lesson-index.json`) || {}).byLemma || {};
for (const [lemma, lessonId] of Object.entries(index)) {
    const stem = lessonId.replace(/^lesson\./, '').replace(/\./g, '-');
    if (!order.has(stem)) continue;
    meet(lemma, order.get(stem));
    for (const t of tokens(lemma)) meet(t, order.get(stem));
}

// Grammar screens per stem: the subject (tables, single italic words) and everything.
function screens(stem) {
    const lesson = readJson(`content/${course}/lessons/${levelOf.get(stem)}/${stem}.json`) || {};
    return (lesson.sections || []).filter(s => s.type === 'grammar' && s.ref)
        .map(s => readJson(`content/${course}/${s.ref}`)).filter(Boolean);
}
const ownWords = new Map();   // stem -> Set of every word on its own screens
for (const stem of order.keys()) {
    const all = new Set();
    for (const g of screens(stem)) {
        const walk = x => {
            if (typeof x === 'string') tokens(x).forEach(t => all.add(lower(t)));
            else if (Array.isArray(x)) x.forEach(walk);
            else if (x && typeof x === 'object') Object.entries(x).forEach(([k, v]) => { if (k !== 'english') walk(v); });
        };
        walk(g.sections);
        for (const s of g.sections || []) {
            if (s.type === 'table') {
                for (const row of s.rows || []) for (const cell of row) {
                    tokens(String(cell).replace(/\([^)]*\)/g, '')).filter(t => !ENGLISH.has(lower(t)))
                        .forEach(t => meet(t, order.get(stem)));
                }
            } else if (s.type !== 'examples') {
                for (const it of italics(s.content)) {
                    const ts = tokens(it);
                    if (ts.length === 1) meet(ts[0], order.get(stem));
                }
            }
        }
    }
    ownWords.set(stem, all);
}

// The target-language text of an exercise. English-language fields (question,
// hint, english) are read only where they quote the target language.
function targetTexts(e) {
    // [text, may be English]: options, matching pairs and quoted question text can be
    // English; sentences, answers, tiles and dialogue lines never are.
    const out = [];
    const add = (x, maybe) => {
        if (typeof x === 'string') out.push([x, maybe]);
        else if (Array.isArray(x)) x.forEach(y => add(y, maybe));
    };
    if (Array.isArray(e.options)) out.push([e.options.filter(o => typeof o === 'string'), true]);
    add(e.sentence, false);
    add(e.answer, false);
    add(e.answers, false);
    add(e.tiles, false);
    add(e.base_sentence, false);
    for (const l of Array.isArray(e.prompt) ? e.prompt : []) add(l && l.text, false);
    for (const t of Array.isArray(e.template) ? e.template : []) add(t && t.answer, false);
    for (const p of e.pairs || []) if (Array.isArray(p)) add(p[0], true);
    const q = String(e.question || '');
    italics(q).forEach(x => add(x, true));
    for (const m of q.matchAll(/[“"„]([^”"]+)[”"]/g)) add(m[1], true);
    for (const m of q.matchAll(/(?:^|[.?!]\s+)[A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+:\s*([^:]+?)(?=\s+[A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+:|$)/g)) add(m[1], false);
    return out;
}

(async () => {
    Lang.set(course);
    await Lexicon.load();
    let ignore = new Set();
    try {
        const ig = readJson('imports/dictionary/coverage-ignore.json') || {};
        const lang = Lang.code() === 'hu' ? 'hu' : 'es';
        ignore = new Set([].concat(ig.words || [], ig.all || [], ig[lang] || []).map(lower));
    } catch (e) { /* none */ }
    const cache = new Map();
    const readingsOf = w => {
        if (!cache.has(w)) {
            let lemmas = [];
            try { lemmas = (Lexicon.lookup(w).readings || []).filter(r => !r.compoundParts).map(r => lower(r.lemma || '')); } catch (e) { /* a throw is the coverage audit's business */ }
            cache.set(w, lemmas);
        }
        return cache.get(w);
    };
    const stemAt = [...order.keys()];
    const metBy = (w, pos) => firstAt.has(w) && firstAt.get(w) <= pos;
    // English words: the course's vocabulary translations (a gloss in quotes, *"old"*).
    const glossWords = new Set();
    for (const level of LEVELS) {
        let files = [];
        try { files = fs.readdirSync(path.join(root, `content/${course}/vocabulary/${level}`)); } catch (e) { /* no level */ }
        for (const f of files) {
            for (const w of (readJson(`content/${course}/vocabulary/${level}/${f}`) || {}).words || []) {
                tokens(w.translation).forEach(t => glossWords.add(lower(t)));
            }
        }
    }
    const isEnglish = (text, pos) => {
        const ts = tokens(text).map(lower);
        if (!ts.length) return true;
        if (ts.filter(t => ENGLISH.has(t)).length * 3 >= ts.length) return true;
        // one word: English if it is a gloss and not a word met by now (*hat* is six)
        if (ts.length === 1 && glossWords.has(ts[0]) && !metBy(ts[0], pos)) return true;
        if (ts.length > 1 && ts.filter(t => glossWords.has(t) && !names.has(t)).length * 2 >= ts.length) return true;
        return !ts.some(t => readingsOf(t).length);   // no word of it is in the dictionary
    };
    // Names: words written with a capital inside a sentence somewhere in the course.
    const names = new Set();
    const lowerSeen = new Set();
    for (const [stem] of order) {
        const data = readJson(`content/${course}/exercises/${levelOf.get(stem)}/${stem}-ex.json`) || {};
        for (const e of data.exercises || []) {
            for (const [t] of targetTexts(e)) for (const text of [].concat(t)) {
                for (const m of String(text).matchAll(/(?<=[^.!?:„“"\s]\s+)[A-ZÁÉÍÓÖŐÚÜŰÑ][\wáéíóöőúüűñ]*/g)) names.add(lower(m[0]));
                for (const t of tokens(text)) if (t[0] === lower(t[0])) lowerSeen.add(t);
            }
        }
    }
    // *Meg* the name is skipped where it is capitalised; *tanár* is checked even
    // though *Tanár úr* is capitalised (a word also seen in lower case is no name).
    const capNames = new Set(names);
    for (const w of lowerSeen) names.delete(w);
    const roots = NUMBER_ROOTS[Lang.code()] || [];
    const numberMet = (w, pos) => {
        if (!w) return true;
        return roots.some(r => w.startsWith(r) && metBy(r, pos) && numberMet(w.slice(r.length), pos));
    };
    const found = [];
    for (const [stem, pos] of order) {
        const level = levelOf.get(stem);
        if (onlyLevel && level !== onlyLevel) continue;
        if (onlyStems && !onlyStems.has(stem)) continue;
        const data = readJson(`content/${course}/exercises/${level}/${stem}-ex.json`) || {};
        const own = ownWords.get(stem);
        for (const e of data.exercises || []) {
            const seen = new Set();
            const texts = [];
            for (const [t, maybe] of targetTexts(e)) {
                if (Array.isArray(t)) {   // an option list is English or not as a whole
                    if (!(maybe && t.filter(o => isEnglish(o, pos)).length * 2 > t.length)) texts.push(...t);
                } else if (!(maybe && isEnglish(t, pos))) texts.push(t);
            }
            for (const text of texts) {
                for (const tok of tokens(text)) {
                    const w = lower(tok);
                    if (w.length < 2 || seen.has(w) || ignore.has(w) || names.has(w) || (tok[0] !== w[0] && capNames.has(w))) continue;
                    seen.add(w);
                    if (own.has(w) || numberMet(w, pos)) continue;
                    const lemmas = readingsOf(w);
                    if (!lemmas.length && tok[0] !== w[0]) continue;   // a name
                    // a deliberately wrong form of a met word (*asztalek*, *könyvok*)
                    if (!lemmas.length && [...firstAt].some(([m, p]) => p <= pos && m.length >= 4 && w.startsWith(m))) continue;
                    const cands = [w, ...lemmas];
                    const at = Math.min(...cands.map(c => firstAt.has(c) ? firstAt.get(c) : Infinity));
                    if (at <= pos) continue;
                    if (lemmas.some(l => own.has(l))) continue;
                    found.push({ stem, id: e.id, word: w, first: at === Infinity ? null : stemAt[at] });
                }
            }
        }
    }
    process.stdout.write(JSON.stringify(found));
})();
