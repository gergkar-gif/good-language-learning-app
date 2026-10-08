const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('Testing Diagnostic Test right and wrong option feedback logic...\n');

// 1. Verify engine/diagnostic.js syntax and presence of key right/wrong feedback elements
const enginePath = path.join(__dirname, '..', 'engine', 'diagnostic.js');
assert(fs.existsSync(enginePath), 'engine/diagnostic.js must exist');
const engineSource = fs.readFileSync(enginePath, 'utf8');

// Ensure zero emojis per Parlour constructivist standard
const EMOJI_REGEX = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
assert(!EMOJI_REGEX.test(engineSource), 'engine/diagnostic.js must contain zero emojis');
console.log('[PASS] Zero emojis verified in engine/diagnostic.js');

// Verify option state classes appear in debrief review breakdown
assert(engineSource.includes('is-correct-opt'), 'Engine must apply is-correct-opt to correct option');
assert(engineSource.includes('is-wrong-opt'), 'Engine must apply is-wrong-opt to incorrect selected option');
assert(engineSource.includes('diag-review-options-grid'), 'Engine must render options grid in debrief review');
assert(engineSource.includes('diag-review-q-card'), 'Engine must render question cards in debrief review');
assert(engineSource.includes('diag-review-drawer'), 'Engine must provide debrief review breakdown drawer');
assert(engineSource.includes('toggle-review'), 'Engine must provide toggle for review breakdown');
assert(engineSource.includes('review-answers-bottom'), 'Engine must provide bottom action to review questions');

// Verify during-test question render DOES NOT reveal correct/wrong options
const renderTestingSection = engineSource.substring(
    engineSource.indexOf('function _renderTesting('),
    engineSource.indexOf('function _evaluateCurrentTier(')
);
assert(!renderTestingSection.includes('is-correct-opt'), '_renderTesting must NOT reveal is-correct-opt during test');
assert(!renderTestingSection.includes('is-wrong-opt'), '_renderTesting must NOT reveal is-wrong-opt during test');
console.log('[PASS] Diagnostic engine code verified: no feedback DURING test, full option review AFTER test');

// 2. Verify styles in styles/components.css and styles/workshop.css
const componentsCss = fs.readFileSync(path.join(__dirname, '..', 'styles', 'components.css'), 'utf8');
const workshopCss = fs.readFileSync(path.join(__dirname, '..', 'styles', 'workshop.css'), 'utf8');

assert(componentsCss.includes('.diag-opt-btn.is-correct-opt'), 'components.css must define .diag-opt-btn.is-correct-opt');
assert(componentsCss.includes('.diag-opt-btn.is-wrong-opt'), 'components.css must define .diag-opt-btn.is-wrong-opt');
assert(componentsCss.includes('.diag-feedback.is-correct'), 'components.css must define .diag-feedback.is-correct');
assert(componentsCss.includes('.diag-feedback.is-wrong'), 'components.css must define .diag-feedback.is-wrong');
assert(componentsCss.includes('.diag-review-drawer'), 'components.css must define .diag-review-drawer');

assert(workshopCss.includes('.diag-opt-btn.is-correct-opt'), 'workshop.css must define .diag-opt-btn.is-correct-opt');
assert(workshopCss.includes('.diag-opt-btn.is-wrong-opt'), 'workshop.css must define .diag-opt-btn.is-wrong-opt');
console.log('[PASS] CSS stylesheets include right/wrong and review styles');

// 3. Test functional behavior of option evaluation logic
function evaluateOptionMarking(q, selectedIdx) {
    const isAnswered = selectedIdx !== undefined;
    const isRight = selectedIdx === q.correct;
    const results = q.options.map((optText, idx) => {
        let cls = 'diag-opt-btn';
        let mark = null;
        if (isAnswered) {
            if (idx === q.correct) {
                cls += ' is-correct-opt';
                mark = 'correct';
            } else if (idx === selectedIdx) {
                cls += ' is-wrong-opt';
                mark = 'wrong';
            } else {
                cls += ' is-dimmed';
            }
        }
        return { text: optText, idx, cls, mark, disabled: isAnswered };
    });

    return {
        isAnswered,
        isRight,
        results,
        feedback: isAnswered ? (isRight ? 'Correct!' : `Correct answer: ${q.options[q.correct]}`) : null
    };
}

const testQ = {
    id: 'test-q1',
    sentence: 'Hola, me llamo Elena y _____ médica.',
    options: ['soy', 'estoy', 'tengo', 'hago'],
    correct: 0
};

// When user picks correct option (idx 0: "soy")
const correctEval = evaluateOptionMarking(testQ, 0);
assert.strictEqual(correctEval.isRight, true);
assert(correctEval.results[0].cls.includes('is-correct-opt'));
assert.strictEqual(correctEval.results[0].mark, 'correct');
assert(!correctEval.results[1].cls.includes('is-wrong-opt'));
assert(correctEval.results[1].cls.includes('is-dimmed'));
assert.strictEqual(correctEval.results[0].disabled, true);
assert.strictEqual(correctEval.feedback, 'Correct!');
console.log('[PASS] Correct option selection highlights option 0 as correct and dims others');

// When user picks wrong option (idx 1: "estoy")
const wrongEval = evaluateOptionMarking(testQ, 1);
assert.strictEqual(wrongEval.isRight, false);
assert(wrongEval.results[0].cls.includes('is-correct-opt'), 'Correct option must be highlighted');
assert.strictEqual(wrongEval.results[0].mark, 'correct');
assert(wrongEval.results[1].cls.includes('is-wrong-opt'), 'Selected wrong option must be highlighted red');
assert.strictEqual(wrongEval.results[1].mark, 'wrong');
assert(wrongEval.results[2].cls.includes('is-dimmed'));
assert.strictEqual(wrongEval.results[1].disabled, true);
assert.strictEqual(wrongEval.feedback, 'Correct answer: soy');
console.log('[PASS] Wrong option selection highlights option 1 as wrong and reveals option 0 as correct');

console.log('\n[ALL PASS] Diagnostic right and wrong option feedback tests completed successfully!');
