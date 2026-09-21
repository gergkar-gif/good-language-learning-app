const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('Testing Diagnostic Test configuration and evaluation logic...\n');

// 1. Verify JSON file structures across languages
const langs = ['es-latam', 'es-es', 'hu'];

langs.forEach(lang => {
    const filePath = path.join(__dirname, '..', 'content', lang, 'tests', 'diagnostic-test.json');
    assert(fs.existsSync(filePath), `File exists: ${filePath}`);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    assert.strictEqual(data.passRatio, 0.85, `${lang}: passRatio must be 0.85`);
    assert(Array.isArray(data.tiers), `${lang}: tiers array exists`);
    assert.strictEqual(data.tiers.length, 3, `${lang}: must have 3 tiers (A1, A2, B1)`);

    const expectedLevels = ['A1', 'A2', 'B1'];
    data.tiers.forEach((tier, tIdx) => {
        assert.strictEqual(tier.level, expectedLevels[tIdx], `${lang}: tier ${tIdx} level is ${expectedLevels[tIdx]}`);
        assert.strictEqual(tier.questions.length, 10, `${lang} ${tier.level}: must have exactly 10 questions`);

        // Questions 1-5: Multiple choice
        for (let i = 0; i < 5; i++) {
            const q = tier.questions[i];
            assert(Array.isArray(q.options), `${lang} ${tier.level} Q${i+1}: options array required`);
            assert(q.options.length >= 3, `${lang} ${tier.level} Q${i+1}: at least 3 options required`);
            assert(typeof q.correct === 'number', `${lang} ${tier.level} Q${i+1}: correct index required`);
        }

        // Questions 6-7: Prompted situational
        for (let i = 5; i < 7; i++) {
            const q = tier.questions[i];
            assert(typeof q.prompt === 'string' && q.prompt.length > 0, `${lang} ${tier.level} Q${i+1}: prompt required`);
            assert(Array.isArray(q.options), `${lang} ${tier.level} Q${i+1}: options required`);
            assert(typeof q.correct === 'number', `${lang} ${tier.level} Q${i+1}: correct index required`);
        }

        // Questions 8-10: Open production text-input
        for (let i = 7; i < 10; i++) {
            const q = tier.questions[i];
            assert.strictEqual(q.type, 'text-input', `${lang} ${tier.level} Q${i+1}: type must be text-input`);
            assert(typeof q.answer === 'string' && q.answer.length > 0, `${lang} ${tier.level} Q${i+1}: answer required`);
            assert(Array.isArray(q.altAnswers), `${lang} ${tier.level} Q${i+1}: altAnswers required`);
            assert(q.sentence.includes('_____'), `${lang} ${tier.level} Q${i+1}: sentence must contain blank '_____'`);
        }
    });

    console.log(`[PASS] ${lang} diagnostic-test.json structure validated (3 tiers, 10 questions each, 85% pass mark).`);
});

// 2. Test evaluation logic
function evaluateTier(questions, answers, passRatio = 0.85) {
    let correct = 0;
    questions.forEach(q => {
        const userAns = answers[q.id];
        if (q.type === 'text-input') {
            if (typeof userAns === 'string' && userAns.trim()) {
                const cleanUser = userAns.trim().toLowerCase();
                const normUser = cleanUser.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
                const accepted = [q.answer, ...(q.altAnswers || [])].filter(Boolean).map(a => a.trim().toLowerCase());
                const normAccepted = accepted.map(a => a.normalize('NFD').replace(/[\u0300-\u036f]/g, ''));
                if (accepted.includes(cleanUser) || normAccepted.includes(normUser)) {
                    correct++;
                }
            }
        } else {
            if (userAns === q.correct) correct++;
        }
    });
    const ratio = questions.length > 0 ? (correct / questions.length) : 0;
    return {
        correct,
        total: questions.length,
        ratio,
        passed: ratio >= passRatio
    };
}

const testTierQuestions = [
    { id: 'q1', correct: 0 },
    { id: 'q2', correct: 0 },
    { id: 'q3', correct: 0 },
    { id: 'q4', correct: 0 },
    { id: 'q5', correct: 0 },
    { id: 'q6', prompt: 'Context', correct: 0 },
    { id: 'q7', prompt: 'Context', correct: 0 },
    { id: 'q8', type: 'text-input', answer: 'fuimos', altAnswers: ['fuimos'] },
    { id: 'q9', type: 'text-input', answer: 'estén', altAnswers: ['esten', 'estéis'] },
    { id: 'q10', type: 'text-input', answer: 'viajaríamos', altAnswers: ['viajariamos'] }
];

// 8 correct = 80% -> FAIL
const ans8 = {
    q1: 0, q2: 0, q3: 0, q4: 0, q5: 0,
    q6: 0, q7: 0,
    q8: 'fuimos',
    q9: 'wrong',
    q10: 'wrong'
};
const res8 = evaluateTier(testTierQuestions, ans8, 0.85);
assert.strictEqual(res8.correct, 8);
assert.strictEqual(res8.passed, false, '8/10 (80%) must fail with 85% requirement');
console.log('[PASS] 8/10 score correctly fails with 85% threshold');

// 9 correct = 90% -> PASS
const ans9 = {
    q1: 0, q2: 0, q3: 0, q4: 0, q5: 0,
    q6: 0, q7: 0,
    q8: 'fuimos',
    q9: 'esten', // tests accent tolerance
    q10: 'wrong'
};
const res9 = evaluateTier(testTierQuestions, ans9, 0.85);
assert.strictEqual(res9.correct, 9);
assert.strictEqual(res9.passed, true, '9/10 (90%) must pass with 85% requirement');
console.log('[PASS] 9/10 score with accent tolerance ("esten" for "estén") correctly passes');

// 10 correct with casing and whitespace -> PASS
const ans10 = {
    q1: 0, q2: 0, q3: 0, q4: 0, q5: 0,
    q6: 0, q7: 0,
    q8: '  FUIMOS  ',
    q9: 'estéis',
    q10: 'viajaríamos'
};
const res10 = evaluateTier(testTierQuestions, ans10, 0.85);
assert.strictEqual(res10.correct, 10);
assert.strictEqual(res10.passed, true);
console.log('[PASS] 10/10 score with casing and whitespace trimming passes');

console.log('\n[ALL PASS] Diagnostic Test suite verified successfully.');
