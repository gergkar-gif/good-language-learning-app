// ========================================
// HOME RECOMMENDATION — LEARNER PROFILES
// ========================================
// Home shows exactly one recommendation. Each profile below is a learner
// state and the card that state should produce, run through the real
// engine files (srs, recycle, learnerPath, learnerModel, drillHistory,
// recommend, recommendationEngine) against the real es-latam curriculum
// and grammar index. When a change to the engine moves a card, this is
// where it shows up.
//
// The rule every profile checks, one way or another: a card other than
// Continue must have a reason the learner would agree with. "You made a
// few mistakes with X lately" must mean recent mistakes with X that
// haven't since been put right.
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '../..');
const COURSE = 'es-latam';
const read = p => JSON.parse(fs.readFileSync(path.join(root, 'content', COURSE, p), 'utf8'));
const curriculum = read('curriculum/curriculum.json');
const grammarIndex = read('indexes/grammar-index.json');

const ENGINE_FILES = ['srs.js', 'recycle.js', 'learnerPath.js', 'learnerModel.js',
    'drillHistory.js', 'recommend.js', 'recommendationEngine.js'];

const DAY = 24 * 60 * 60 * 1000;
const NOW = Date.parse('2026-09-28T12:00:00Z');

// A fresh app per profile: its own localStorage, progress and app-open
// counter, with the engine files evaluated inside it.
function world({ progress = {}, appOpen = 50, store = {} } = {}) {
    const ctx = {
        console, Math, JSON, Map, Set, Promise, Object, Array, Number, String, isFinite,
        Date: class extends Date {
            constructor(...a) { super(...(a.length ? a : [NOW])); }
            static now() { return NOW; }
        },
        localStorage: {
            getItem: k => (k in store ? store[k] : null),
            setItem: (k, v) => { store[k] = String(v); },
            removeItem: k => { delete store[k]; }
        },
        Lang: { key: k => COURSE + ':' + k, name: () => 'Spanish', code: () => COURSE, content: p => p },
        Content: {
            json: async p => {
                const file = path.join(root, 'content', COURSE, p);
                if (!fs.existsSync(file)) throw new Error('404 ' + p);
                return JSON.parse(fs.readFileSync(file, 'utf8'));
            }
        },
        AppOpens: { current: () => appOpen },
        LEVEL_ORDER: ['A1', 'A2', 'B1', 'B2', 'C1'],
        getProgress: () => progress,
        LevelTest: { resultFor: () => null },
        document: { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [], addEventListener: () => {} },
        CustomEvent: function () {}
    };
    ctx.window = ctx;
    ctx.window.addEventListener = () => {};
    ctx.window.dispatchEvent = () => {};
    ctx.window._curriculumData = curriculum;
    vm.createContext(ctx);
    ENGINE_FILES.forEach(f => vm.runInContext(fs.readFileSync(path.join(root, 'engine', f), 'utf8'), ctx));
    ctx.run = code => vm.runInContext(code, ctx);
    ctx.setOpen = n => { appOpen = n; };
    return ctx;
}

// ---- curriculum helpers ----
const coreUnits = level => (curriculum.levels[level].units || []).filter(u => !u.track || u.track === 'core');
const allCoreLessons = level => coreUnits(level).flatMap(u => u.lessons || []);

// Progress through (and including) `lessonId`, in course order, core
// lessons only, one minute apart so the last one is the most recent.
function progressThrough(lessonId) {
    const progress = {};
    let t = NOW - 30 * DAY;
    for (const level of ['A1', 'A2', 'B1']) {
        for (const lesson of allCoreLessons(level)) {
            progress[lesson.id] = { completedAt: new Date(t += 60000).toISOString() };
            if (lesson.id === lessonId) return progress;
        }
    }
    return progress;
}

const refFor = id => {
    const parts = id.replace(/^lesson\./, '').split('.');
    return `exercises/${parts[0]}/${parts[0]}-${parts.slice(1).join('-')}-ex.json`;
};

// Recycle cards for `ids`: 'good' = answered right twice (starting ease),
// 'missed' = most recent answer wrong, `open` = the app open it happened at.
function cards(ids, kind, open) {
    const out = {};
    ids.forEach(id => {
        out[id] = kind === 'missed'
            ? { reviews: 0, ease: 1.9, interval: 0, lastOpen: open, dueAtOpen: open + 1, lapses: 2, leech: false }
            : { reviews: 2, ease: 2.5, interval: 6, lastOpen: open, dueAtOpen: open + 6, lapses: 0, leech: false };
    });
    return out;
}

// The profile lesson: a mid-unit A1 lesson (not its unit's last), whose own
// grammar skill has at least two exercises in that lesson.
const mid = (() => {
    for (const unit of coreUnits('A1').slice(2)) {
        const lessons = unit.lessons || [];
        for (const lesson of lessons.slice(0, -1)) {
            const ref = refFor(lesson.id);
            for (const [skill, entries] of Object.entries(grammarIndex.bySkill)) {
                const here = entries.filter(e => e.ref === ref);
                if (here.length >= 2) return { unit, lesson, skill, ids: here.map(e => e.id) };
            }
        }
    }
    throw new Error('no suitable mid-unit lesson');
})();

const recycleStore = schedule => ({ [COURSE + ':recycleSchedule']: JSON.stringify(schedule) });

async function recommend(w) {
    return (await w.run('RecommendationEngine.recommend()')).primary;
}

const profiles = [];
const profile = (name, fn) => profiles.push({ name, fn });

// ------------------------------------------------------------------

profile('brand-new learner → Continue, first lesson', async () => {
    const p = await recommend(world());
    assert.strictEqual(p.kind, 'continue');
    assert.strictEqual(p.step.lesson.id, allCoreLessons('A1')[0].id);
});

profile('mid-unit, never got anything wrong → Continue (no "mistakes" claim)', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'good', 49)) });
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}: ${p.blurb || ''}`);
});

profile('recent misses on the lesson\'s skill → grammar practice on that skill', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 49)) });
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'mini-game', `got ${p.kind}`);
    assert.strictEqual(p.drillerId, 'grammar');
    // The missed exercises can teach more than one skill; any of them is right.
    const taught = Object.keys(grammarIndex.bySkill).filter(k => grammarIndex.bySkill[k].some(e => mid.ids.includes(e.id)));
    assert.ok(taught.includes(p.skill), `${p.skill} is not taught by the missed exercises`);
    assert.strictEqual(p.reason, 'weak');
});

profile('misses long ago, nothing since → Continue (not "lately")', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 5)) });
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}: ${p.blurb || ''}`);
});

profile('missed, then practised correctly in the same sitting → Continue', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 50)) });
    w.__r = mid.ids.map(id => ({ id, rating: 'good' }));
    w.run('Recycle.credit(__r)');
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}: ${p.blurb || ''}`);
});

profile('skipped practice on a weak skill → not offered again straight away', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 49)) });
    const first = await recommend(w);
    assert.strictEqual(first.kind, 'mini-game');
    w.__p = first;
    w.run('RecommendationEngine.skip(__p)');
    // The next lesson, same weak skill, two opens later.
    const next = allCoreLessons('A1')[allCoreLessons('A1').findIndex(l => l.id === mid.lesson.id) + 1];
    Object.assign(w.getProgress(), { [next.id]: { completedAt: new Date(NOW).toISOString() } });
    w.setOpen(52);
    const p = await recommend(w);
    assert.ok(!(p.kind === 'mini-game' && p.skill === mid.skill), 'same skill offered again right after a skip');
});

profile('skipped, then the cool-down runs out → offered again', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 49)) });
    const first = await recommend(w);
    w.__p = first;
    w.run('RecommendationEngine.skip(__p)');
    const next = allCoreLessons('A1')[allCoreLessons('A1').findIndex(l => l.id === mid.lesson.id) + 1];
    Object.assign(w.getProgress(), { [next.id]: { completedAt: new Date(NOW).toISOString() } });
    w.setOpen(56);
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'mini-game', `got ${p.kind}`);
    assert.strictEqual(p.skill, first.skill);
});

profile('practice taken → not offered again in the same sitting', async () => {
    const w = world({ progress: progressThrough(mid.lesson.id), store: recycleStore(cards(mid.ids, 'missed', 49)) });
    const first = await recommend(w);
    w.__p = first;
    // Taking it: same bookkeeping as Home's button, minus the navigation.
    w.showTab = () => {}; w.Workshop = { open() {}, close() {} }; w.document.querySelector = () => null;
    w.run('RecommendationEngine.open(__p)');
    const next = allCoreLessons('A1')[allCoreLessons('A1').findIndex(l => l.id === mid.lesson.id) + 1];
    Object.assign(w.getProgress(), { [next.id]: { completedAt: new Date(NOW).toISOString() } });
    const p = await recommend(w);
    assert.ok(!(p.kind === 'mini-game' && p.skill === first.skill), 'same skill offered again in the same sitting');
});

profile('just finished a unit with a roleplay → unit milestone', async () => {
    const unit = coreUnits('A1').find(u => u.id === 'unit.a1.11');
    const last = unit.lessons[unit.lessons.length - 1];
    const p = await recommend(world({ progress: progressThrough(last.id) }));
    assert.strictEqual(p.kind, 'unit-nudge');
    assert.strictEqual(p.unit.id, 'unit.a1.11');
});

profile('unit milestone skipped → Continue', async () => {
    const unit = coreUnits('A1').find(u => u.id === 'unit.a1.11');
    const last = unit.lessons[unit.lessons.length - 1];
    const w = world({ progress: progressThrough(last.id) });
    w.run(`RecommendationEngine.dismissUnit('unit.a1.11')`);
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}`);
});

profile('words reviewed but never missed → Continue (no "hardest words" claim)', async () => {
    const deck = ['casa', 'perro', 'libro', 'mesa', 'agua'].map(w => ({ spanish: w, english: w, type: 'noun', reviews: 3, ease: 2.5, lapses: 0 }));
    const w = world({ progress: progressThrough(mid.lesson.id), store: { srsDeck: JSON.stringify(deck), [COURSE + ':srsDeck']: JSON.stringify(deck) } });
    w.run('srsDeck = ' + JSON.stringify(deck));
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}: ${p.blurb || ''}`);
});

profile('several words actually missed → word review', async () => {
    const deck = ['casa', 'perro', 'libro', 'mesa', 'agua'].map((w, i) => ({ spanish: w, english: w, type: 'noun', reviews: 0, ease: i < 4 ? 1.7 : 2.5, lapses: i < 4 ? 2 : 0 }));
    const w = world({ progress: progressThrough(mid.lesson.id) });
    w.run('srsDeck = ' + JSON.stringify(deck));
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'mini-game', `got ${p.kind}`);
    assert.strictEqual(p.drillerId, 'srs');
});

profile('a drill scored badly weeks ago, not since → Continue', async () => {
    const old = new Date(NOW - 40 * DAY).toISOString();
    const hist = [1, 2, 3].map(() => ({ date: old, correct: 2, wrong: 8, accuracy: 20 }));
    const w = world({ progress: progressThrough(allCoreLessons('A1')[20].id), store: { [COURSE + ':drillHistory:listening']: JSON.stringify(hist) } });
    const key = w.run(`(function(){ let k=null; const s=localStorage.setItem; localStorage.setItem=(a,b)=>{k=a;}; DrillHistory.record('listening',{correct:1,wrong:1}); localStorage.setItem=s; return k; })()`);
    w.localStorage.setItem(key, JSON.stringify(hist));
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'continue', `got ${p.kind}: ${p.blurb || ''}`);
});

profile('a drill scored badly this week → that drill', async () => {
    const recent = new Date(NOW - 2 * DAY).toISOString();
    const hist = [1, 2, 3].map(() => ({ date: recent, correct: 2, wrong: 8, accuracy: 20 }));
    const w = world({ progress: progressThrough(allCoreLessons('A1')[20].id) });
    const key = w.run(`(function(){ let k=null; const s=localStorage.setItem; localStorage.setItem=(a,b)=>{k=a;}; DrillHistory.record('listening',{correct:1,wrong:1}); localStorage.setItem=s; return k; })()`);
    w.localStorage.setItem(key, JSON.stringify(hist));
    const p = await recommend(w);
    assert.strictEqual(p.kind, 'mini-game', `got ${p.kind}`);
    assert.strictEqual(p.drillerId, 'listening');
});

profile('B1, 5th core lesson, elective track open → elective', async () => {
    const b1 = allCoreLessons('B1');
    let progress;
    for (let i = 1; i < b1.length; i++) {
        progress = progressThrough(b1[i].id);
        if (Object.keys(progress).length % 5 === 0) break;
    }
    const p = await recommend(world({ progress }));
    assert.strictEqual(p.kind, 'elective', `got ${p.kind}`);
    assert.ok(p.lesson && p.unit.track && p.unit.track !== 'core');
});

// ------------------------------------------------------------------

(async () => {
    let failed = 0;
    for (const { name, fn } of profiles) {
        try {
            await fn();
            console.log('✓ ' + name);
        } catch (e) {
            failed++;
            console.log('✗ ' + name + '\n    ' + (e.message || e));
        }
    }
    console.log(`\n${profiles.length - failed}/${profiles.length} profiles pass`);
    if (failed) process.exit(1);
})();
