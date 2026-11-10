// Placement diagnostic: tests that load engine/diagnostic.js itself (the
// older test-diagnostic.js checks a copy of the scoring), and that hold the
// Spanish items to the level of their tier.
const fs = require('fs');
const path = require('path');
const assert = require('assert');

global.window = { _curriculumData: null };
const Diag = require('../engine/diagnostic.js');

const tier = (level, correct, extra) => {
    const ratio = correct / 12;
    return Object.assign({ level, correct, total: 12, passed: ratio >= 0.85, borderline: ratio < 0.85 && ratio >= 0.7 }, extra || {});
};

// 1. The pass mark shown to the learner is a count the tier can reach.
assert.strictEqual(Diag._needed(0.85, 12), 11, '85% of 12 items is 11');
assert.strictEqual(Diag._needed(0.7, 12), 9, '70% of 12 items is 9');
assert.strictEqual(Diag._needed(0.85, 10), 9);
console.log('[PASS] pass mark: 11 of 12, nearly there from 9 of 12');

// 2. Placement ladder, including the middle band.
assert.strictEqual(Diag._determinePlacement([tier('A1', 8)]), 'A1', 'a failed A1 stays in A1');
assert.strictEqual(Diag._determinePlacement([tier('A1', 9)]), 'A2', 'nearly there on A1 moves up');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 8)]), 'A2');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 10)]), 'B1');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 12)]), 'B2');
console.log('[PASS] placement ladder with the nearly-there band');

// 3. Never place into a level the course has no units for (es-es B2).
window._curriculumData = { levels: { A1: { units: [{}] }, A2: { units: [{}] }, B1: { units: [{}] }, B2: { units: [] }, C1: { units: [] } } };
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 12)]), 'B1', 'cleared B1 stays in B1 when B2 is empty');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 9)]), 'B1', 'nearly there on B1 stays in B1 when B2 is empty');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 10)]), 'B1', 'levels with units are unaffected');
window._curriculumData = null;
console.log('[PASS] no placement into an empty level');

// 4. The review list: the nearly-there tier's missed skills, at most three.
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12), tier('A2', 9, { missedSkills: ['a', 'b', 'c', 'd'] })]), ['a', 'b', 'c']);
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12), tier('A2', 8, { missedSkills: ['a'] })]), [], 'a failed tier gives no review list');
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12, { missedSkills: [] })]), []);
console.log('[PASS] review list comes from the nearly-there tier only');

// 5. Spanish items: one skill each, a grammar skill of the tier's own
//    level, known to the registry; no vosotros answers in es-latam; typed
//    items never list an alternative that only repeats the answer.
const skills = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'skills', 'es.json'), 'utf8')).skills;
['es-es', 'es-latam'].forEach(course => {
    const data = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'content', course, 'tests', 'diagnostic-test.json'), 'utf8'));
    const ids = new Set();
    let notStated = 0;
    data.tiers.forEach(t => {
        t.questions.forEach(q => {
            assert(!ids.has(q.id), `${course} ${q.id}: duplicate id`);
            ids.add(q.id);
            assert(Array.isArray(q.teaches) && q.teaches.length === 1, `${course} ${q.id}: exactly one skill`);
            const skill = skills[q.teaches[0]];
            assert(skill, `${course} ${q.id}: unknown skill ${q.teaches[0]}`);
            assert.strictEqual(skill.level, t.level, `${course} ${q.id}: ${q.teaches[0]} is a ${skill.level} skill in the ${t.level} tier`);
            if (q.type === 'text-input') {
                const norm = v => v.trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
                (q.altAnswers || []).forEach(a => assert.notStrictEqual(norm(a), norm(q.answer), `${course} ${q.id}: altAnswer repeats the answer`));
                if (course === 'es-latam') {
                    [q.answer].concat(q.altAnswers || []).forEach(a => assert(!/[áée]is$/.test(a.trim()), `${course} ${q.id}: vosotros form "${a}"`));
                }
            }
        });
        t.readingSection.questions.forEach(rq => {
            assert(!ids.has(rq.id), `${course} ${rq.id}: duplicate id`);
            ids.add(rq.id);
            if (rq.type === 'true-false-not-stated' && rq.correct === 2) notStated++;
        });
    });
    assert(notStated >= 1, `${course}: "not stated" must be the right answer at least once`);
    console.log(`[PASS] ${course}: every item tests one skill of its own tier`);
});

console.log('\n[ALL PASS] Diagnostic engine tests.');
