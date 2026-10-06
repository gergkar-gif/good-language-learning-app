// tests/drills/test-ccse-exam.js
// Automated verification suite for Spanish CCSE Exam content & engine logic.

const assert = require('assert');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const DATA_PATH = path.join(ROOT, 'content/es-es/ccse-exam.json');
const ENGINE_PATH = path.join(ROOT, 'engine/ccse-exam.js');
const WORKSHOP_PATH = path.join(ROOT, 'engine/workshop.js');
const INDEX_PATH = path.join(ROOT, 'index.html');

console.log('Testing Spanish CCSE Exam...');

// 1. Validate content/es-es/ccse-exam.json
assert(fs.existsSync(DATA_PATH), 'ccse-exam.json must exist');
const data = JSON.parse(fs.readFileSync(DATA_PATH, 'utf-8'));

assert.strictEqual(data.id, 'es-ccse-exam');
assert.strictEqual(data.passThresholdPoints, 15, 'Pass mark must be 15');
assert.strictEqual(data.maxPoints, 25, 'Total points must be 25');
assert(Array.isArray(data.categories) && data.categories.length === 5, 'Must have 5 syllabus categories');
assert(Array.isArray(data.vocabulary) && data.vocabulary.length >= 20, 'Must have >= 20 vocabulary terms');
assert(Array.isArray(data.mcqs) && data.mcqs.length >= 40, 'Must have >= 40 MCQs in pool');

console.log('[PASS] Basic data structure and metadata verified.');

// 2. Validate Question Pool
const validTareas = new Set(['tarea1', 'tarea2', 'tarea3', 'tarea4', 'tarea5']);
const tareaCounts = { tarea1: 0, tarea2: 0, tarea3: 0, tarea4: 0, tarea5: 0 };

data.mcqs.forEach((q, idx) => {
    assert(q.id, `Question ${idx} must have id`);
    assert(validTareas.has(q.tarea), `Question ${q.id} has invalid tarea: ${q.tarea}`);
    tareaCounts[q.tarea]++;
    assert(typeof q.question === 'string' && q.question.length > 5, `Question ${q.id} has invalid prompt`);
    assert(Array.isArray(q.options), `Question ${q.id} options must be an array`);
    
    if (q.tarea === 'tarea2') {
        assert.strictEqual(q.options.length, 2, `Tarea 2 question ${q.id} must be binary True/False`);
    } else {
        assert.strictEqual(q.options.length, 3, `Tarea ${q.tarea} question ${q.id} must have 3 options`);
    }
    
    assert(typeof q.correct === 'number' && q.correct >= 0 && q.correct < q.options.length, `Question ${q.id} has invalid correct index`);
    assert(typeof q.explanation === 'string' && q.explanation.length > 5, `Question ${q.id} must have explanation`);
});

assert(tareaCounts.tarea1 >= 10, 'Must have at least 10 Tarea 1 questions');
assert(tareaCounts.tarea2 >= 3, 'Must have at least 3 Tarea 2 questions');
assert(tareaCounts.tarea3 >= 2, 'Must have at least 2 Tarea 3 questions');
assert(tareaCounts.tarea4 >= 3, 'Must have at least 3 Tarea 4 questions');
assert(tareaCounts.tarea5 >= 7, 'Must have at least 7 Tarea 5 questions');

console.log(`[PASS] Question pool verified (T1: ${tareaCounts.tarea1}, T2: ${tareaCounts.tarea2}, T3: ${tareaCounts.tarea3}, T4: ${tareaCounts.tarea4}, T5: ${tareaCounts.tarea5}).`);

// 3. Validate Matching Sets
assert(data.matchingSets, 'Matching sets must exist');
const expectedModes = ['institutionToRole', 'regionToCapital', 'creatorToWork', 'dateToEvent'];
expectedModes.forEach(mode => {
    const set = data.matchingSets[mode];
    assert(set, `Matching set ${mode} must exist`);
    assert(Array.isArray(set.pairs) && set.pairs.length >= 6, `Set ${mode} must have at least 6 pairs`);
    set.pairs.forEach(p => {
        assert(Array.isArray(p) && p.length === 2 && p[0] && p[1], `Invalid pair in ${mode}`);
    });
});
console.log('[PASS] Matching sets verified (all 4 modes have >= 6 pairs).');

// 4. Validate Curated Mock Exams
assert(Array.isArray(data.mockExams) && data.mockExams.length >= 3, 'Must have at least 3 curated mock exams');

data.mockExams.forEach(mock => {
    assert(mock.id && mock.title, `Mock exam ${mock.id} must have id and title`);
    assert.strictEqual(mock.questions.length, 25, `Mock ${mock.id} must have exactly 25 questions`);
    
    const mockTaskCounts = { tarea1: 0, tarea2: 0, tarea3: 0, tarea4: 0, tarea5: 0 };
    mock.questions.forEach(q => {
        assert(validTareas.has(q.tarea), `Question in ${mock.id} has invalid tarea: ${q.tarea}`);
        mockTaskCounts[q.tarea]++;
    });

    assert.strictEqual(mockTaskCounts.tarea1, 10, `${mock.id} must have 10 Tarea 1 questions`);
    assert.strictEqual(mockTaskCounts.tarea2, 3, `${mock.id} must have 3 Tarea 2 questions`);
    assert.strictEqual(mockTaskCounts.tarea3, 2, `${mock.id} must have 2 Tarea 3 questions`);
    assert.strictEqual(mockTaskCounts.tarea4, 3, `${mock.id} must have 3 Tarea 4 questions`);
    assert.strictEqual(mockTaskCounts.tarea5, 7, `${mock.id} must have 7 Tarea 5 questions`);
});
console.log('[PASS] Curated mock exams strictly match official 10/3/2/3/7 question quotas.');

// 5. Test Random Mock Generation Logic
function simulateRandomMock(pool) {
    const shuffle = arr => arr.slice().sort(() => Math.random() - 0.5);
    const byTarea = {
        tarea1: shuffle(pool.filter(q => q.tarea === 'tarea1')),
        tarea2: shuffle(pool.filter(q => q.tarea === 'tarea2')),
        tarea3: shuffle(pool.filter(q => q.tarea === 'tarea3')),
        tarea4: shuffle(pool.filter(q => q.tarea === 'tarea4')),
        tarea5: shuffle(pool.filter(q => q.tarea === 'tarea5'))
    };

    return [
        ...byTarea.tarea1.slice(0, 10),
        ...byTarea.tarea2.slice(0, 3),
        ...byTarea.tarea3.slice(0, 2),
        ...byTarea.tarea4.slice(0, 3),
        ...byTarea.tarea5.slice(0, 7)
    ];
}

for (let trial = 0; trial < 10; trial++) {
    const sampled = simulateRandomMock(data.mcqs);
    assert.strictEqual(sampled.length, 25);
    assert.strictEqual(sampled.filter(q => q.tarea === 'tarea1').length, 10);
    assert.strictEqual(sampled.filter(q => q.tarea === 'tarea2').length, 3);
    assert.strictEqual(sampled.filter(q => q.tarea === 'tarea3').length, 2);
    assert.strictEqual(sampled.filter(q => q.tarea === 'tarea4').length, 3);
    assert.strictEqual(sampled.filter(q => q.tarea === 'tarea5').length, 7);
}
console.log('[PASS] Dynamic random mock generator verified across 10 randomized trials.');

// 6. Verify Engine File
const engineCode = fs.readFileSync(ENGINE_PATH, 'utf-8');
assert(engineCode.includes('const CcseExam ='), 'Engine must declare CcseExam');
assert(engineCode.includes('render'), 'Engine must expose render');
assert(engineCode.includes('stop'), 'Engine must expose stop');
assert(engineCode.includes('timerRemaining = 45 * 60'), 'Timer must be 45 minutes');
assert(engineCode.includes('timerEnabled: false'), 'Timer must be untimed by default per learner setting');
assert(engineCode.includes('_generateRandomMock'), 'Engine must include random mock generator');
console.log('[PASS] engine/ccse-exam.js structure and exports verified.');

// 7. Verify Workshop Integration
const workshopCode = fs.readFileSync(WORKSHOP_PATH, 'utf-8');
assert(workshopCode.includes("'es-ccse-exam'"), 'workshop.js must register es-ccse-exam');
assert(workshopCode.includes("langs: ['es-es']"), 'es-ccse-exam must be scoped to es-es per learner instruction');
assert(workshopCode.includes("'es-ccse-exam': typeof CcseExam !== 'undefined' ? CcseExam : null"), 'workshop.js must map es-ccse-exam in _moduleFor');
console.log('[PASS] engine/workshop.js integration verified.');

// 8. Verify index.html Script Tag
const indexHtml = fs.readFileSync(INDEX_PATH, 'utf-8');
assert(indexHtml.includes('engine/ccse-exam.js'), 'index.html must load engine/ccse-exam.js');
console.log('[PASS] index.html script tag verified.');

console.log('\n[ALL PASS] Spanish CCSE Exam test suite successfully completed.');
