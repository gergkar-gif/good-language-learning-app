// ========================================
// SKILL REACH GATING
// ========================================
// Skills are tagged across levels, so a learner in HU A1 unit 3 must not
// be drilled on (or recommended) a skill through B2 exercises. Runs on the
// real Hungarian curriculum and grammar index.
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '../..');
const hu = p => JSON.parse(fs.readFileSync(path.join(root, 'content/hu', p), 'utf8'));
const curriculum = hu('curriculum/curriculum.json');
const index = hu('indexes/grammar-index.json');

const store = {};
let appOpen = 10;
let progress = {};
const ctx = {
    console, Date, Math, JSON, Map, Set, Promise, Object, Array,
    localStorage: {
        getItem: k => (k in store ? store[k] : null),
        setItem: (k, v) => { store[k] = String(v); },
        removeItem: k => { delete store[k]; }
    },
    Lang: { key: k => 'hu_' + k, name: () => 'Hungarian', code: () => 'hu', content: p => p },
    Content: { json: async p => { if (p === 'indexes/grammar-index.json') return index; throw new Error('404'); } },
    AppOpens: { current: () => appOpen },
    LEVEL_ORDER: ['A1', 'A2', 'B1', 'B2', 'C1'],
    getProgress: () => progress,
    document: { getElementById: () => null, querySelectorAll: () => [], addEventListener: () => {} },
    CustomEvent: function () {}
};
ctx.window = ctx;
ctx.window.addEventListener = () => {};
ctx.window.dispatchEvent = () => {};
ctx.window._curriculumData = curriculum;
vm.createContext(ctx);
for (const f of ['srs.js', 'recycle.js', 'learnerPath.js', 'learnerModel.js']) {
    vm.runInContext(fs.readFileSync(path.join(root, 'engine', f), 'utf8'), ctx);
}
const run = code => vm.runInContext(code, ctx);

(async () => {
    // A learner through A1 unit 3.
    curriculum.levels.A1.units.slice(0, 3).forEach(u =>
        u.lessons.forEach(l => { progress[l.id] = { completedAt: '2026-09-27T10:00:00Z' }; }));

    const reached = run('LearnerPath.reachedExerciseRefs()');
    assert.ok(reached.has('exercises/a1/a1-13-ex.json'), 'a unit-3 lesson is reached');
    assert.ok(!reached.has('exercises/a1/a1-16-ex.json'), 'unit 4 is not reached yet');
    assert.ok(![...reached].some(r => r.includes('/b2/')), 'no B2 file is reached');
    console.log('✓ reachedExerciseRefs() stops at the furthest completed lesson');

    // A skill taught in unit 1 is also tagged on B1 exercises — only the
    // reached ones should feed a drill.
    const all = index.bySkill['vagyok-vagy-and-where-van-goes'];
    const kept = all.filter(e => reached.has(e.ref));
    assert.ok(kept.length > 0 && kept.length < all.length && kept.every(e => e.ref.includes('/a1/')),
        `pool narrows to reached A1 files (${kept.length}/${all.length})`);
    console.log('✓ a cross-level skill narrows to the reached exercises');

    // Misses on B2 exercises (e.g. from an ungated drill before this fix)
    // must not make a B2 skill the learner's top recommendation.
    const b2 = index.bySkill['b2-nehogy-subjunctive'].slice(0, 3).map(e => e.id);
    for (let i = 0; i < 4; i++) {
        appOpen++;
        ctx.__r = b2.map(id => ({ id, rating: 'again' }));
        run('Recycle.credit(__r)');
    }
    let weak = await run('LearnerModel.weakSkills()');
    assert.ok(!weak.some(s => s.skillId === 'b2-nehogy-subjunctive'), 'unreached B2 skill is not weak: ' + JSON.stringify(weak.map(s => s.skillId)));
    console.log('✓ weakSkills() ignores evidence from unreached lessons');

    // Once the learner actually gets there, the same evidence counts.
    Object.values(curriculum.levels).forEach(lv => (lv.units || []).forEach(u =>
        u.lessons.forEach(l => { progress[l.id] = { completedAt: '2026-09-27T10:00:00Z' }; })));
    weak = await run('LearnerModel.weakSkills()');
    assert.ok(weak.some(s => s.skillId === 'b2-nehogy-subjunctive'), 'reached B2 skill with misses is weak');
    console.log('✓ the same evidence counts once the lessons are reached');

    console.log('\nAll skill reach gating tests passed!');
})().catch(e => { console.error(e); process.exit(1); });
