#!/usr/bin/env node
// Reader dictionary-coverage audit.
//
// Runs every word of every story through the same Lexicon.lookup() pipeline the
// Reader uses when a learner taps a word, and reports the ones that would show
// "Not in the dictionary yet" (or only a literal compound-split guess). It
// loads the real engine files headless, so the verdicts match the app exactly.
//
//   node scripts/audit-reader-coverage.js [course|all] [--out report.json]
//                                          [--top N] [--min-count N]
//
// course: hu | es-es | es-latam | all (default all)
//
// Exit code is 0 either way: this is a report, not a gate. Feed the JSON report
// to scripts/fill-dictionary-gaps.py to draft entries for the misses.

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const args = process.argv.slice(2);
const flag = (name, dflt) => {
    const i = args.indexOf(name);
    return i === -1 ? dflt : args[i + 1];
};
const positional = args.filter((a, i) => !a.startsWith('--') && !(args[i - 1] || '').startsWith('--'));
const courseArg = positional[0] || 'all';
const outFile = flag('--out', null);
const topN = parseInt(flag('--top', '40'), 10);
const minCount = parseInt(flag('--min-count', '1'), 10);

const root = path.resolve(__dirname, '..');
process.chdir(root);

// ---- headless browser shims (same approach as tests/drills) ----
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

// The Reader's own tokenizer (engine/reader.js WORD_CHARS): letters incl.
// Spanish and Hungarian diacritics; digits are never looked up.
const WORD_CHARS = 'a-zA-ZáéíóúÁÉÍÓÚ' +
    'ñÑüÜöÖőŐűŰ';
const WORD_RE = new RegExp('[' + WORD_CHARS + ']+', 'g');

function storyFiles(course) {
    const out = [];
    (function walk(dir) {
        for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
            const p = path.join(dir, e.name);
            if (e.isDirectory()) walk(p);
            else if (e.name.endsWith('.json') && e.name !== 'manifest.json') out.push(p);
        }
    })(path.join('content', course, 'stories'));
    return out.sort();
}

function sentenceAround(text, start, end) {
    let a = start, b = end;
    while (a > 0 && !'.!?\n'.includes(text[a - 1])) a--;
    while (b < text.length && !'.!?\n'.includes(text[b])) b++;
    const s = text.slice(a, Math.min(b + 1, text.length)).trim();
    return s.length > 160 ? s.slice(Math.max(0, start - a - 70), start - a + 90).trim() : s;
}

async function auditCourse(course) {
    Lang.set(course);
    await Lexicon.load();
    const lang = Lang.code() === 'hu' ? 'hu' : 'es';

    const words = new Map();   // lower-cased token -> {count, stories:Set, capitalised, lower, sample}
    let tokenTotal = 0;
    const files = storyFiles(course);
    for (const file of files) {
        let story;
        try { story = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (e) { continue; }
        const storyId = story.id || path.basename(file, '.json');
        for (const p of story.paragraphs || []) {
            // paragraphs in another language (English narration) aren't tappable
            if (p.lang && p.lang !== lang) continue;
            const text = p.text || '';
            let m;
            WORD_RE.lastIndex = 0;
            while ((m = WORD_RE.exec(text))) {
                const token = m[0];
                tokenTotal++;
                const key = token.toLowerCase();
                let w = words.get(key);
                if (!w) {
                    w = { count: 0, stories: new Set(), capMid: 0, lowerMid: 0, sample: null };
                    words.set(key, w);
                }
                w.count++;
                w.stories.add(storyId);
                // capitalised somewhere other than sentence start suggests a name
                const before = text.slice(0, m.index).replace(/\s+$/, '');
                const atStart = before === '' || /[.!?—–:„"“]$/.test(before);
                if (!atStart) {
                    if (token[0] !== token[0].toLowerCase()) w.capMid++; else w.lowerMid++;
                }
                if (!w.sample) w.sample = sentenceAround(text, m.index, m.index + token.length);
            }
        }
    }

    const misses = [];
    const literalOnly = [];
    const crashes = [];
    for (const [key, w] of words) {
        if (key.length < 2) continue;   // single letters aren't meaningful lookups
        let res;
        try {
            res = Lexicon.lookup(key);
        } catch (err) {
            // a tap on this word would throw in the app, which is worse than a miss
            crashes.push({ word: key, w, error: String(err && err.message || err).slice(0, 120) });
            continue;
        }
        const readings = res.readings || [];
        if (readings.length === 0) {
            misses.push({ word: key, w });
        } else if (readings.every(r => r.compoundParts)) {
            literalOnly.push({ word: key, w, parts: readings[0].compoundParts });
        }
    }
    const shape = ({ word, w, parts, error }) => ({
        word,
        count: w.count,
        stories: w.stories.size,
        likelyName: w.capMid > 0 && w.lowerMid === 0,
        sample: w.sample,
        ...(parts ? { parts } : {}),
        ...(error ? { error } : {})
    });
    const byCount = (a, b) => b.count - a.count || a.word.localeCompare(b.word);
    return {
        course,
        stories: files.length,
        tokens: tokenTotal,
        uniqueWords: words.size,
        misses: misses.map(shape).filter(x => x.count >= minCount).sort(byCount),
        literalOnly: literalOnly.map(shape).filter(x => x.count >= minCount).sort(byCount),
        crashes: crashes.map(shape).sort(byCount)
    };
}

(async () => {
    const courses = courseArg === 'all' ? Lang.available() : [courseArg];
    const report = [];
    for (const c of courses) {
        if (!Lang.available().includes(c)) { console.error('Unknown course: ' + c); process.exit(2); }
        const r = await auditCourse(c);
        report.push(r);
        const names = r.misses.filter(x => x.likelyName).length;
        console.log(`\n=== ${c}: ${r.stories} stories, ${r.tokens} tokens, ${r.uniqueWords} unique words`);
        console.log(`    not in the dictionary: ${r.misses.length} (${names} look like names)`);
        console.log(`    literal compound guess only: ${r.literalOnly.length}`);
        console.log(`    lookup throws (tap would fail): ${r.crashes.length}`);
        r.crashes.slice(0, 10).forEach(x => console.log(`      ${x.word}: ${x.error}`));
        r.misses.slice(0, topN).forEach(x =>
            console.log(`    ${String(x.count).padStart(4)}x ${x.likelyName ? '[name] ' : '       '}${x.word}   ${x.sample ? '| ' + x.sample.slice(0, 90) : ''}`));
    }
    if (outFile) {
        fs.writeFileSync(outFile, JSON.stringify(report, null, 1));
        console.log('\nWrote ' + outFile);
    }
})();
