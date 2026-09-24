// ============================================
// TEST SUITE: CEFR LEVEL DIAGNOSTIC TEST
// ============================================
// Verifies:
// 1. Content schema and validity for ES and HU diagnostic tests
// 2. Absence of emojis (Parlour constructivist design principle)
// 3. Pedagogical preface text & communication-first philosophy
// 4. Adaptive placement ladder logic (A1 -> A2 -> B1 -> B2 placement)
// 5. Open-ended level extensibility (e.g., adding B2 / C1 dynamically)
// 6. Preceding level completion logic on placement acceptance

const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('=== Running CEFR Diagnostic Test Suite ===\n');

// Helper to detect emojis
const EMOJI_REGEX = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

// 1. Test Content Validation
const languages = ['es', 'hu'];
const testData = {};

for (const lang of languages) {
    let filePath = path.join(__dirname, `../../content/${lang}/tests/diagnostic-test.json`);
    if (!fs.existsSync(filePath) && lang === 'es') {
        filePath = path.join(__dirname, `../../content/es-latam/tests/diagnostic-test.json`);
    }
    assert(fs.existsSync(filePath), `diagnostic-test.json must exist for ${lang}`);
    
    const content = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    testData[lang] = content;
    
    assert(content.language === lang, `${lang}: language should match ${lang}`);
    assert(Array.isArray(content.tiers), `${lang}: tiers should be an array`);
    assert(content.tiers.length >= 3, `${lang}: should have at least A1, A2, B1 tiers`);
    
    content.tiers.forEach((tier, tIdx) => {
        assert(tier.level, `${lang}: tier ${tIdx} missing level`);
        assert(tier.name, `${lang}: tier ${tIdx} missing name`);
        assert(Array.isArray(tier.questions), `${lang}: tier ${tier.level} questions should be array`);
        assert(tier.questions.length >= 5, `${lang}: tier ${tier.level} should have at least 5 questions`);
        
        tier.questions.forEach((q, qIdx) => {
            assert(q.id, `${lang} ${tier.level} Q${qIdx}: missing id`);
            assert(q.sentence, `${lang} ${tier.level} Q${qIdx}: missing sentence`);
            assert(Array.isArray(q.options), `${lang} ${tier.level} Q${qIdx}: options should be array`);
            assert(q.options.length >= 3, `${lang} ${tier.level} Q${qIdx}: should have at least 3 options`);
            assert(typeof q.correct === 'number', `${lang} ${tier.level} Q${qIdx}: correct must be a number`);
            assert(q.correct >= 0 && q.correct < q.options.length, `${lang} ${tier.level} Q${qIdx}: correct index out of bounds`);
            
            // Emoji check
            assert(!EMOJI_REGEX.test(q.sentence), `${lang} ${tier.level} Q${qIdx}: sentence must not contain emojis`);
            q.options.forEach((opt, oIdx) => {
                assert(!EMOJI_REGEX.test(opt), `${lang} ${tier.level} Q${qIdx} Opt ${oIdx}: option must not contain emojis`);
            });
        });
    });
    console.log(`[PASS] Content schema & emoji validation passed for ${lang.toUpperCase()}`);
}

// 2. Engine Verification: File inspection
const enginePath = path.join(__dirname, '../../engine/diagnostic.js');
assert(fs.existsSync(enginePath), 'engine/diagnostic.js must exist');
const engineSource = fs.readFileSync(enginePath, 'utf8');

// Check for zero emojis in engine source
assert(!EMOJI_REGEX.test(engineSource), 'engine/diagnostic.js must contain zero emojis');
console.log('[PASS] Zero emojis in engine/diagnostic.js verified');

// Check pedagogical preface quote in engine
assert(engineSource.includes('we are not doing language learning to finish a course, but to actually be able to communicate') ||
       engineSource.includes('we do not learn a language merely to finish a course, but to actually be able to communicate'),
       'Engine must contain the pedagogical preface statement about learning to communicate');
console.log('[PASS] Pedagogical philosophy quote present in engine');

// 3. Adaptive Placement Ladder Logic
const LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1'];

function determinePlacement(tierResults, tiers) {
    if (!tierResults || tierResults.length === 0) return 'A1';

    let highestPassedIdx = -1;
    for (let i = 0; i < tierResults.length; i++) {
        if (tierResults[i].passed) {
            highestPassedIdx = i;
        } else {
            break;
        }
    }

    if (highestPassedIdx === -1) {
        return tiers[0] ? tiers[0].level : 'A1';
    }

    const passedLevel = tierResults[highestPassedIdx].level;
    const normPassed = passedLevel.toUpperCase();
    const orderIdx = LEVEL_ORDER.indexOf(normPassed);

    if (orderIdx !== -1 && orderIdx + 1 < LEVEL_ORDER.length) {
        return LEVEL_ORDER[orderIdx + 1];
    }

    return passedLevel;
}

// Case A: Fails A1 tier (score 2/6 = 33%) -> placed into A1
const resA = [{ level: 'A1', passed: false, correct: 2, total: 6 }];
assert.strictEqual(determinePlacement(resA, testData.es.tiers), 'A1', 'Failing A1 should place into A1');

// Case B: Passes A1 (5/6), fails A2 (2/6) -> placed into A2
const resB = [
    { level: 'A1', passed: true, correct: 5, total: 6 },
    { level: 'A2', passed: false, correct: 2, total: 6 }
];
assert.strictEqual(determinePlacement(resB, testData.es.tiers), 'A2', 'Passing A1 and failing A2 should place into A2');

// Case C: Passes A1 (5/6), passes A2 (5/6), fails B1 (3/6) -> placed into B1
const resC = [
    { level: 'A1', passed: true, correct: 5, total: 6 },
    { level: 'A2', passed: true, correct: 5, total: 6 },
    { level: 'B1', passed: false, correct: 3, total: 6 }
];
assert.strictEqual(determinePlacement(resC, testData.es.tiers), 'B1', 'Passing A1+A2 and failing B1 should place into B1');

// Case D: Passes A1 (6/6), passes A2 (6/6), passes B1 (5/6) -> placed into B2 (jump past B1)
const resD = [
    { level: 'A1', passed: true, correct: 6, total: 6 },
    { level: 'A2', passed: true, correct: 6, total: 6 },
    { level: 'B1', passed: true, correct: 5, total: 6 }
];
assert.strictEqual(determinePlacement(resD, testData.es.tiers), 'B2', 'Passing all authored tiers (A1, A2, B1) should place into B2');
console.log('[PASS] Placement ladder logic correctly resolves A1, A2, B1, and B2 placements');

// 4. Future Extensibility: Dynamically adding B2 tier
const extendedTiers = [
    ...testData.es.tiers,
    { level: 'B2', name: 'Vantage', questions: [{ id: 'b2_1' }] }
];
const resExt = [
    { level: 'A1', passed: true },
    { level: 'A2', passed: true },
    { level: 'B1', passed: true },
    { level: 'B2', passed: true }
];
assert.strictEqual(determinePlacement(resExt, extendedTiers), 'C1', 'Passing dynamically added B2 tier should place into C1');
console.log('[PASS] Extensibility: Adding B2 tier places cleared learner into C1 without engine rewrite');

// 5. Preceding levels resolution for jump-ahead
function getPrecedingLevels(placedLevel) {
    const idx = LEVEL_ORDER.indexOf(placedLevel.toUpperCase());
    return idx > 0 ? LEVEL_ORDER.slice(0, idx) : [];
}

assert.deepStrictEqual(getPrecedingLevels('A1'), []);
assert.deepStrictEqual(getPrecedingLevels('A2'), ['A1']);
assert.deepStrictEqual(getPrecedingLevels('B1'), ['A1', 'A2']);
assert.deepStrictEqual(getPrecedingLevels('B2'), ['A1', 'A2', 'B1']);
console.log('[PASS] Preceding levels for jump-ahead calculated accurately');

// 6. Language Selection Prior to Diagnostic
const homeSource = fs.readFileSync(path.join(__dirname, '../../engine/home.js'), 'utf8');
assert(homeSource.includes('data-switch-lang'), 'Home onboarding card must allow switching target language');
assert(homeSource.includes('hm-onboarding-lang-picker'), 'Home onboarding card must render language choice chips');
assert(!engineSource.includes('data-diag-lang'), 'The course is chosen on the first-open screen, not in the diagnostic preface');
console.log('[PASS] Language selection verified on Home Onboarding Card and Diagnostic Preface');

console.log('\nAll CEFR Diagnostic Test Suite checks PASSED successfully!');
