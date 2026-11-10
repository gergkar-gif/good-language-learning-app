// Placement diagnostic: tests that load engine/diagnostic.js itself (the
// older test-diagnostic.js checks a copy of the scoring), and that hold
// every course's items to the placement rules.
const fs = require('fs');
const path = require('path');
const assert = require('assert');

global.window = { _curriculumData: null };
const Diag = require('../engine/diagnostic.js');

const tier = (level, correct, extra) => {
    const ratio = correct / 12;
    return Object.assign({ level, correct, total: 12, passed: ratio >= 0.83, borderline: ratio < 0.83 && ratio >= 0.7 }, extra || {});
};

// 1. The pass mark shown to the learner is a count the tier can reach.
assert.strictEqual(Diag._needed(0.83, 12), 10, 'the pass mark is 10 of 12');
assert.strictEqual(Diag._needed(0.7, 12), 9, '70% of 12 items is 9');
assert.strictEqual(Diag._needed(0.83, 10), 9);
console.log('[PASS] pass mark: 10 of 12, nearly there at 9 of 12');

// 2. Placement ladder, including the middle band.
assert.strictEqual(Diag._determinePlacement([tier('A1', 8)]), 'A1', 'a failed A1 stays in A1');
assert.strictEqual(Diag._determinePlacement([tier('A1', 9)]), 'A2', 'nearly there on A1 moves up');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 8)]), 'A2');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 9)]), 'B1');
assert.strictEqual(Diag._determinePlacement([tier('A1', 10), tier('A2', 10), tier('B1', 8)]), 'B1', '10 of 12 clears a tier');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 12)]), 'B2');
console.log('[PASS] placement ladder with the nearly-there band');

// 3. Never place into a level the course has no units for (es-es B2).
window._curriculumData = { levels: { A1: { units: [{}] }, A2: { units: [{}] }, B1: { units: [{}] }, B2: { units: [] }, C1: { units: [] } } };
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 12)]), 'B1', 'cleared B1 stays in B1 when B2 is empty');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 12), tier('B1', 9)]), 'B1', 'nearly there on B1 stays in B1 when B2 is empty');
assert.strictEqual(Diag._determinePlacement([tier('A1', 12), tier('A2', 9)]), 'B1', 'levels with units are unaffected');
window._curriculumData = null;
console.log('[PASS] no placement into an empty level');

// 4. The review list: the nearly-there tier's missed skills, at most three.
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12), tier('A2', 9, { missedSkills: ['a', 'b', 'c', 'd'] })]), ['a', 'b', 'c']);
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12), tier('A2', 8, { missedSkills: ['a'] })]), [], 'a failed tier gives no review list');
assert.deepStrictEqual(Diag._reviewSkills([tier('A1', 12, { missedSkills: [] })]), []);
console.log('[PASS] review list comes from the nearly-there tier only');

// 5. Every course that has a diagnostic (found on disk, so a new language
//    is held to this from its first commit): what the review list needs
//    (one registered skill per core item, with a learner-facing title,
//    unique ids) and the item rules in AGENTS.md § "Placement diagnostic".
//
//    KNOWN_OPEN lists, by exact id, the items written before the rules that
//    still break them (ROADMAP 155). They are reported, not failed; any
//    item NOT listed fails, and a listed item that has been fixed fails
//    too, so the list can only shrink.
const KNOWN_OPEN = {
    hu: {
        offLevel: ['hu-diag-a2-01', 'hu-diag-a2-04', 'hu-diag-a2-06', 'hu-diag-a2-07', 'hu-diag-a2-08',
            'hu-diag-b1-01', 'hu-diag-b1-03', 'hu-diag-b1-05', 'hu-diag-b1-06', 'hu-diag-b1-08', 'hu-diag-b1-09'],
        noNotStated: true
    }
};
const contentDir = path.join(__dirname, '..', 'content');
const courses = fs.readdirSync(contentDir).filter(c => fs.existsSync(path.join(contentDir, c, 'tests', 'diagnostic-test.json'))).sort();
assert(courses.includes('es-es') && courses.includes('es-latam') && courses.includes('hu'), 'the three shipped diagnostics are found');
const norm = v => v.trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

courses.forEach(course => {
    const lang = course.split('-')[0];
    const skills = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'skills', lang + '.json'), 'utf8')).skills;
    const titles = JSON.parse(fs.readFileSync(path.join(contentDir, course, 'indexes', 'grammar-titles.json'), 'utf8'));
    const data = JSON.parse(fs.readFileSync(path.join(contentDir, course, 'tests', 'diagnostic-test.json'), 'utf8'));
    const open = KNOWN_OPEN[course] || {};
    const allowedOffLevel = new Set(open.offLevel || []);
    const ids = new Set();
    const offLevel = [];
    let notStated = 0;
    data.tiers.forEach(t => {
        t.questions.forEach(q => {
            assert(!ids.has(q.id), `${course} ${q.id}: duplicate id`);
            ids.add(q.id);
            assert(Array.isArray(q.teaches) && q.teaches.length === 1, `${course} ${q.id}: exactly one skill`);
            const slug = q.teaches[0];
            const skill = skills[slug];
            assert(skill, `${course} ${q.id}: unknown skill ${slug}`);
            assert.strictEqual(skill.kind, 'grammar', `${course} ${q.id}: ${slug} is not a grammar skill`);
            assert(typeof titles[slug] === 'string' && titles[slug], `${course} ${q.id}: ${slug} has no title for the review list`);
            if (skill.level !== t.level) {
                assert(allowedOffLevel.has(q.id), `${course} ${q.id}: ${slug} is a ${skill.level} skill in the ${t.level} tier`);
                offLevel.push(q.id);
            } else {
                assert(!allowedOffLevel.has(q.id), `${course} ${q.id}: now on level, remove it from KNOWN_OPEN`);
            }
            if (q.type === 'text-input') {
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
    if (open.noNotStated) assert.strictEqual(notStated, 0, `${course}: has a "not stated" answer now, remove noNotStated from KNOWN_OPEN`);
    else assert(notStated >= 1, `${course}: "not stated" must be the right answer at least once`);
    if (offLevel.length || open.noNotStated) {
        console.log(`[PASS] ${course}: review list has what it needs. KNOWN OPEN: ${offLevel.length} items below their tier's level${open.noNotStated ? ', no "not stated" answer' : ''}`);
    } else {
        console.log(`[PASS] ${course}: review list has what it needs; every item tests one skill of its own tier`);
    }
});

console.log('\n[ALL PASS] Diagnostic engine tests.');
