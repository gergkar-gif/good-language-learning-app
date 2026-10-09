// Print a lesson as the learner gets it, generated screens included (ROADMAP 153).
//
//   node scripts/render_lesson.js <course> <lesson stem> [<lesson stem> ...]
//   node scripts/render_lesson.js hu a1-01 a1-02
//
// Runs the real buildSteps() from engine/lessons.js with file-reading stubs, so
// the speaking steps and the communicative challenge the engine generates are
// shown exactly as the app builds them. Quick Review is left out: it depends on
// the learner's history and replays exercises from earlier lessons.
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..');
const [course, ...stems] = process.argv.slice(2);
if (!course || !stems.length) { console.error('usage: node scripts/render_lesson.js <course> <stem> ...'); process.exit(2); }

const NAMES = { hu: 'Hungarian', 'es-es': 'Spanish', 'es-latam': 'Spanish' };
const missing = [];
const ctx = {
    console: { log() {}, warn: (...a) => missing.push('warn: ' + a.join(' ')), error: (...a) => missing.push('error: ' + a.join(' ')) },
    setTimeout, clearTimeout, Promise, JSON, Math, Date, Object, Array, String, Set, Map, RegExp,
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    Lang: { content: p => `content/${course}/${p}`, name: () => NAMES[course] || course, code: () => course.split('-')[0] },
    Reader: { assignCharacterVoices: () => ({}) },
    fetch: async p => {
        const f = path.join(ROOT, p);
        if (!fs.existsSync(f)) { missing.push('404: ' + p); return { ok: false, status: 404, json: async () => null }; }
        const text = fs.readFileSync(f, 'utf8');
        return { ok: true, status: 200, json: async () => JSON.parse(text), text: async () => text };
    },
};
ctx.window = ctx; ctx.globalThis = ctx;
vm.createContext(ctx);
for (const f of ['engine/canDoPrompt.js', 'engine/exercise-audio.js', 'engine/lessons.js']) {
    vm.runInContext(fs.readFileSync(path.join(ROOT, f), 'utf8'), ctx, { filename: f });
}

const opts = (e) => (e.options || []).map((o, i) => `      ${i === e.correct ? '*' : '-'} ${o}`).join('\n');
function show(s, n) {
    const head = `[${n}] ${s.type}${s.title ? ' · ' + s.title : ''}`;
    const out = [head];
    const add = (k, v) => { if (v !== undefined && v !== null && v !== '' && !(Array.isArray(v) && !v.length)) out.push(`    ${k}: ${typeof v === 'string' ? v : JSON.stringify(v)}`); };
    switch (s.type) {
        case 'goal': case 'checklist': add('items', s.items); break;
        case 'grammar': (s.parts || []).forEach(p => add(p.type, p.content || p.text || p.items || p.rows || p.title)); break;
        case 'vocabulary': add('words', (s.words || []).map(w => `${w.lemma} = ${w.translation}`).join(' · ')); break;
        case 'story': (s.lines || []).forEach(p => out.push(`    ${p.lang && p.lang !== course.split('-')[0] ? '(' + p.lang + ') ' : ''}${p.speaker ? p.speaker + ': ' : ''}${p.text || ''}`)); break;
        case 'speaking': add('mode', s.mode); add('prompt', s.prompt); add('say', s.spanish); add('english', s.english); break;
        case 'challenge': ['scenario', 'prompt', 'cues', 'target', 'english', 'canDo'].forEach(k => add(k, s[k])); break;
        case 'srs': add('cards', (s.cards || []).map(w => w.lemma).join(', ')); break;
        default:
            add('id', s.id);
            add('question', s.question || s.instruction);
            if (s.prompt && Array.isArray(s.prompt)) add('prompt', s.prompt.map(t => `${t.speaker}: ${t.text}`).join(' / '));
            add('sentence', s.sentence); add('hint', s.hint);
            add('answer', s.answer || s.answers || s.solution);
            add('english', s.english);
            add('pairs', s.pairs);
            if (s.options) out.push(opts(s));
    }
    return out.join('\n');
}

(async () => {
    for (const stem of stems) {
        const level = stem.split('-')[0];
        const lessonPath = `content/${course}/lessons/${level}/${stem}.json`;
        const lesson = JSON.parse(fs.readFileSync(path.join(ROOT, lessonPath), 'utf8'));
        missing.length = 0;
        const steps = await vm.runInContext('buildSteps', ctx)(lesson);
        console.log(`\n========== ${course} ${stem}: ${lesson.title} (${steps.length} screens) ==========`);
        steps.forEach((s, i) => console.log(show(s, i + 1)));
        if (missing.length) console.log('\n  !! ' + [...new Set(missing)].join('\n  !! '));
    }
})().catch(e => { console.error(e); process.exit(1); });
