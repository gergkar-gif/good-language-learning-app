// Unit Test: Progressive Two-Tier Hint Mechanism for Fill-Blank Exercises
// Verifies:
// 1. Level 1 hint reveals first letter of canonical target word
// 2. Level 2 hint reveals English sentence gloss
// 3. Zero emojis in hint UI (clean Parlour typography)
// 4. Soft signal on Learner Path / Stats: usedHint prevents correctFirstTry and schedules 'hard' in SM-2 Recycle

const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock browser / DOM globals
class MockClassList {
    constructor() {
        this.classes = new Set();
    }
    add(...names) { names.forEach(n => this.classes.add(n)); }
    remove(...names) { names.forEach(n => this.classes.delete(n)); }
    contains(n) { return this.classes.has(n); }
    toggle(n, force) {
        if (force !== undefined) {
            if (force) this.add(n); else this.remove(n);
        } else {
            if (this.contains(n)) this.remove(n); else this.add(n);
        }
    }
}

class MockElement {
    constructor(tagName = 'div', id = '') {
        this.tagName = tagName.toUpperCase();
        this.id = id;
        this.classList = new MockClassList();
        this._textContent = '';
        this._innerHTML = '';
        this.style = {};
        this.disabled = false;
        this.value = '';
        this.listeners = {};
    }

    get textContent() { return this._textContent; }
    set textContent(val) {
        this._textContent = String(val);
    }

    get innerHTML() { return this._innerHTML; }
    set innerHTML(val) {
        this._innerHTML = String(val);
    }

    addEventListener(event, fn) {
        if (!this.listeners[event]) this.listeners[event] = [];
        this.listeners[event].push(fn);
    }

    dispatchEvent(evt) {
        const type = typeof evt === 'string' ? evt : evt.type;
        (this.listeners[type] || []).forEach(fn => fn(evt));
    }

    querySelector(sel) {
        if (sel === '.gd-hint-btn') return this._hintBtn;
        if (sel === '.gd-hint-area') return this._hintArea;
        if (sel === '.gd-input') return this._input;
        return null;
    }

    querySelectorAll() { return []; }
    focus() {}
    blur() {}
}

const elements = {};
global.document = {
    getElementById: (id) => elements[id] || null,
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener: () => {}
};

global.addEventListener = () => {};
global.removeEventListener = () => {};
global.window = global;
global.esc = (t) => String(t || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
global.escMd = global.esc;

let recordedRecycle = [];
global.Recycle = {
    record: (id, rating) => {
        recordedRecycle.push({ id, rating });
    }
};

global.Sound = {
    correct: () => {},
    wrong: () => {},
    complete: () => {}
};

// Load lessons.js functions
const lessonsCode = fs.readFileSync(path.join(__dirname, '../../engine/lessons.js'), 'utf8');
const exportsCode = `
global.stepRenderers = stepRenderers;
global.lessonRequestHint = lessonRequestHint;
global.lessonCheckBlank = lessonCheckBlank;
global.getStepState = () => stepState;
global.setStepState = (val) => { stepState = val; };
global.getCurrentLesson = () => currentLesson;
global.setCurrentLesson = (val) => { currentLesson = val; };
global.getLessonStats = () => lessonStats;
global.setLessonStats = (val) => { lessonStats = val; };
global.getGradedStepIndices = () => gradedStepIndices;
global.setGradedStepIndices = (val) => { gradedStepIndices = val; };
global.getCurrentStepIndex = () => currentStepIndex;
global.setCurrentStepIndex = (val) => { currentStepIndex = val; };
`;
eval(lessonsCode + exportsCode);

delete global.stepState;
Object.defineProperty(global, 'stepState', {
    get() { return global.getStepState(); },
    set(val) { global.setStepState(val); },
    configurable: true
});
delete global.currentLesson;
Object.defineProperty(global, 'currentLesson', {
    get() { return global.getCurrentLesson(); },
    set(val) { global.setCurrentLesson(val); },
    configurable: true
});
delete global.lessonStats;
Object.defineProperty(global, 'lessonStats', {
    get() { return global.getLessonStats(); },
    set(val) { global.setLessonStats(val); },
    configurable: true
});
delete global.gradedStepIndices;
Object.defineProperty(global, 'gradedStepIndices', {
    get() { return global.getGradedStepIndices(); },
    set(val) { global.setGradedStepIndices(val); },
    configurable: true
});
delete global.currentStepIndex;
Object.defineProperty(global, 'currentStepIndex', {
    get() { return global.getCurrentStepIndex(); },
    set(val) { global.setCurrentStepIndex(val); },
    configurable: true
});

// Minimal lesson state
currentStepIndex = 0;
currentLesson = {
    steps: [{
        id: 'ex-fb-01',
        teaches: ['hablar-presente']
    }]
};
gradedStepIndices = new Set();
lessonStats = { total: 0, correctFirstTry: 0 };

async function runTests() {
    console.log('--- Test 1: Fill-blank step initialization and zero emoji verification ---');

    elements['blank-input'] = new MockElement('input', 'blank-input');
    elements['lsn-hint-btn'] = new MockElement('button', 'lsn-hint-btn');
    elements['lsn-hint-area'] = new MockElement('div', 'lsn-hint-area');
    elements['step-feedback'] = new MockElement('p', 'step-feedback');
    elements['step-translation'] = new MockElement('p', 'step-translation');
    elements['step-diff'] = new MockElement('div', 'step-diff');
    elements['lesson-next-btn'] = new MockElement('button', 'lesson-next-btn');

    const html = stepRenderers['fill-blank']({
        sentence: 'Nosotros ___ español en casa.',
        answer: 'hablamos',
        english: 'We speak Spanish at home.'
    });

    assert.strictEqual(stepState.hintLevel, 0, 'hintLevel must start at 0');
    assert.strictEqual(stepState.usedHint, false, 'usedHint must start false');
    assert.strictEqual(stepState.answer, 'hablamos');
    assert.strictEqual(stepState.translation, 'We speak Spanish at home.');

    // Zero emojis check
    const emojiRegex = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u;
    assert.strictEqual(emojiRegex.test(html), false, 'Fill-blank render HTML must not contain emojis');

    console.log('[PASS] Fill-blank step initializes cleanly without emojis.');

    console.log('--- Test 2: Level 1 hint reveals first letter ---');
    lessonRequestHint();

    assert.strictEqual(stepState.hintLevel, 1, 'Hint level must advance to 1');
    assert.strictEqual(stepState.usedHint, true, 'usedHint must be marked true');
    assert.strictEqual(elements['lsn-hint-area'].style.display, 'block', 'Hint area must become visible');
    assert.ok(elements['lsn-hint-area'].innerHTML.includes('Starts with <strong>"h"</strong>'), 'Hint 1 must display initial letter "h"');
    assert.strictEqual(elements['lsn-hint-btn'].textContent, 'Next hint', 'Button updates to "Next hint"');
    assert.strictEqual(emojiRegex.test(elements['lsn-hint-area'].innerHTML), false, 'Hint 1 HTML must not contain emojis');

    console.log('[PASS] Level 1 hint reveals the first letter without emojis.');

    console.log('--- Test 3: Level 2 hint reveals English gloss ---');
    lessonRequestHint();

    assert.strictEqual(stepState.hintLevel, 2, 'Hint level must advance to 2');
    assert.ok(elements['lsn-hint-area'].innerHTML.includes('We speak Spanish at home.'), 'Hint 2 must display English gloss');
    assert.strictEqual(elements['lsn-hint-btn'].textContent, 'All hints shown', 'Button indicates all hints shown');
    assert.strictEqual(elements['lsn-hint-btn'].disabled, true, 'Button is disabled after all hints shown');
    assert.strictEqual(emojiRegex.test(elements['lsn-hint-area'].innerHTML), false, 'Hint 2 HTML must not contain emojis');

    console.log('[PASS] Level 2 hint reveals English gloss and locks hint button.');

    console.log('--- Test 4: Soft learner path signal & stats handling ---');
    // Learner types correct answer and checks
    elements['blank-input'].value = 'hablamos';
    recordedRecycle = [];
    lessonStats = { total: 0, correctFirstTry: 0 };
    gradedStepIndices = new Set();

    lessonCheckBlank();

    assert.strictEqual(stepState.solved, true, 'Step should be solved');
    assert.strictEqual(elements['lsn-hint-area'].style.display, 'none', 'Hint area should be hidden upon solve');
    assert.strictEqual(elements['lsn-hint-btn'].style.display, 'none', 'Hint button should be hidden upon solve');

    // Stats: because usedHint is true, correctFirstTry must NOT increment
    assert.strictEqual(lessonStats.total, 1, 'Total steps incremented');
    assert.strictEqual(lessonStats.correctFirstTry, 0, 'Step with hint must NOT count toward correctFirstTry');

    // Spaced repetition: rated 'hard' instead of 'good'
    assert.strictEqual(recordedRecycle.length, 1, 'Recycle recorded');
    assert.strictEqual(recordedRecycle[0].rating, 'hard', 'Step solved with hint must receive "hard" SM-2 rating');

    console.log('[PASS] Soft signal applied: excluded from correctFirstTry and scheduled as "hard" in SM-2.');

    console.log('--- Test 5: Clean solve without hint rates "good" and counts as correctFirstTry ---');
    stepState = {};
    stepRenderers['fill-blank']({
        sentence: 'Ellos ___ mucho.',
        answer: 'estudian',
        english: 'They study a lot.'
    });

    elements['blank-input'].value = 'estudian';
    recordedRecycle = [];
    lessonStats = { total: 0, correctFirstTry: 0 };
    gradedStepIndices = new Set();

    lessonCheckBlank();

    assert.strictEqual(stepState.solved, true);
    assert.strictEqual(lessonStats.correctFirstTry, 1, 'Clean solve without hints counts as correctFirstTry');
    assert.strictEqual(recordedRecycle[0].rating, 'good', 'Clean solve without hints receives "good" SM-2 rating');

    console.log('[PASS] Clean solve without hints gets full first-try credit and "good" rating.');

    console.log('--- Test 6: Accented initial letter preservation ---');
    stepState = {};
    stepRenderers['fill-blank']({
        sentence: '___ es mi hermano.',
        answer: 'Él',
        english: 'He is my brother.'
    });

    lessonRequestHint();
    assert.ok(elements['lsn-hint-area'].innerHTML.includes('Starts with <strong>"É"</strong>'), 'Accented initial letter preserved accurately');

    console.log('[PASS] Accented first letters handled properly.');

    console.log('--- Test 7: GrammarRunner fill-blank progressive hint parity ---');
    const grammarRunnerCode = fs.readFileSync(path.join(__dirname, '../../engine/drills/grammar-runner.js'), 'utf8');
    eval(grammarRunnerCode + '\nglobal.GrammarRunner = GrammarRunner;\n');

    const grContainer = new MockElement('div');
    const grHintBtn = new MockElement('button');
    const grHintArea = new MockElement('div');
    const grInput = new MockElement('input');
    grContainer._hintBtn = grHintBtn;
    grContainer._hintArea = grHintArea;
    grContainer._input = grInput;

    GrammarRunner.render(grContainer, {
        exercise: {
            kind: 'fill-blank',
            sentence: 'Tú ___ español.',
            answer: 'hablas',
            english: 'You speak Spanish.'
        }
    });

    assert.strictEqual(emojiRegex.test(grContainer.innerHTML), false, 'GrammarRunner fill-blank must not contain emojis');

    // Click hint button
    const hintClick = grHintBtn.listeners['click'] && grHintBtn.listeners['click'][0];
    assert.ok(hintClick, 'GrammarRunner hint button click listener registered');
    hintClick();

    assert.strictEqual(grHintArea.style.display, 'block');
    assert.ok(grHintArea.innerHTML.includes('Starts with <strong>"h"</strong>'));
    assert.strictEqual(grHintBtn.textContent, 'Next hint');

    // Second click
    hintClick();
    assert.ok(grHintArea.innerHTML.includes('You speak Spanish.'));
    assert.strictEqual(grHintBtn.textContent, 'All hints shown');

    console.log('[PASS] GrammarRunner fill-blank has matching progressive hint behavior without emojis.');

    console.log('\n[ALL PASS] All fill-blank hint mechanism tests passed successfully!');
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
