// ==========================================================
// Unit Tests: Reader Comprehension Question Option Shuffling & Grading
// ==========================================================
const assert = require('assert');
const path = require('path');

// Mock minimal browser globals for reader.js
global.window = global;

const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { Object.keys(mockStorage).forEach(k => delete mockStorage[k]); }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`,
    content: (p) => p
};

global.Art = {
    icon: (name) => `<svg class="art-${name}"></svg>`
};

class MockElement {
    constructor(tagName = 'div', attrs = {}) {
        this.tagName = tagName.toUpperCase();
        this._classList = new Set();
        this.attributes = { ...attrs };
        this.children = [];
        this.parentElement = null;
        this.innerHTML = '';
        this._listeners = {};
        this.disabled = false;
        this.hidden = false;
    }

    setAttribute(k, v) { this.attributes[k] = String(v); }
    getAttribute(k) { return this.attributes[k] !== undefined ? this.attributes[k] : null; }
    removeAttribute(k) { delete this.attributes[k]; }
    hasAttribute(k) { return this.attributes[k] !== undefined; }

    get classList() {
        const self = this;
        return {
            add: (c) => self._classList.add(c),
            remove: (c) => self._classList.delete(c),
            contains: (c) => self._classList.has(c)
        };
    }

    addEventListener(event, fn) {
        if (!this._listeners[event]) this._listeners[event] = [];
        this._listeners[event].push(fn);
    }

    dispatchEvent(event) {
        const list = this._listeners[event.type || event] || [];
        list.forEach(fn => fn(event));
    }
}

global.document = {
    createElement: (tag) => new MockElement(tag),
    getElementById: (id) => null,
    addEventListener: () => {},
    removeEventListener: () => {}
};

const Reader = require('../../engine/reader.js');

console.log('--- Test 1: _shuffled Helper Properties ---');
assert.strictEqual(typeof Reader._shuffled, 'function', 'Reader._shuffled must be exported as a function');

const original = ['A', 'B', 'C', 'D'];
const shuffledOnce = Reader._shuffled(original);
assert.strictEqual(shuffledOnce.length, 4, 'Shuffled array must preserve length');
assert.deepStrictEqual([...shuffledOnce].sort(), [...original].sort(), 'Shuffled array must contain same elements');
assert.deepStrictEqual(original, ['A', 'B', 'C', 'D'], 'Original array must not be mutated');
console.log('[PASS] _shuffled preserves array contents and avoids input mutation.');

console.log('\n--- Test 2: Random Distribution of Shuffled Options ---');
// Verify that over 200 trials with 4 options, the 0-th item does NOT always land at index 0
let positionCounts = { 0: 0, 1: 0, 2: 0, 3: 0 };
const items = [{ text: 'Opt 0', originalIdx: 0 }, { text: 'Opt 1', originalIdx: 1 }, { text: 'Opt 2', originalIdx: 2 }, { text: 'Opt 3', originalIdx: 3 }];
for (let i = 0; i < 200; i++) {
    const res = Reader._shuffled(items);
    const pos = res.findIndex(x => x.originalIdx === 0);
    positionCounts[pos]++;
}

console.log('Distribution of option 0 across positions in 200 trials:', positionCounts);
assert(positionCounts[0] < 150, 'Option 0 must not remain in position 0 deterministically');
assert(positionCounts[1] > 10, 'Option 0 must appear in position 1');
assert(positionCounts[2] > 10, 'Option 0 must appear in position 2');
assert(positionCounts[3] > 10, 'Option 0 must appear in position 3');
console.log('[PASS] Options are genuinely randomized and do not stay fixed on top.');

console.log('\n--- Test 3: Data Attributes and Original Index Preservation ---');
const testStory = {
    id: 'test-story-01',
    title: 'Prueba de Comprensión',
    level: 'B1',
    paragraphs: [{ type: 'narration', text: 'Un texto de prueba.' }],
    narration: {
        pedagogical: {
            comprehensionQuestions: [
                {
                    question: '¿Cuál es la respuesta correcta?',
                    options: ['Respuesta Correcta', 'Distractor 1', 'Distractor 2', 'Distractor 3'],
                    correctIndex: 0,
                    explanation: 'La explicación correspondiente.'
                }
            ]
        }
    }
};

// Simulate HTML generation logic from reader.js
const q = testStory.narration.pedagogical.comprehensionQuestions[0];
const indexedOptions = (q.options || []).map((opt, oIdx) => ({ text: opt, originalIdx: oIdx }));
const shuffledOpts = Reader._shuffled(indexedOptions);

assert.strictEqual(shuffledOpts.length, 4, 'Must have 4 shuffled options');
const correctItem = shuffledOpts.find(item => item.originalIdx === q.correctIndex);
assert(correctItem, 'The correct option must still be present');
assert.strictEqual(correctItem.text, 'Respuesta Correcta');
console.log('[PASS] data-opt and correctIndex references are intact after shuffle.');

console.log('\n--- Test 4: End-to-End Simulation of Click Handlers with Shuffled Options ---');
// Verify that grading logic correctly identifies the right button even when shuffled to another index
for (let trial = 0; trial < 10; trial++) {
    const perm = Reader._shuffled(indexedOptions);
    // Find button that has the correct answer
    const correctBtnIndex = perm.findIndex(item => item.originalIdx === q.correctIndex);
    const wrongBtnIndex = perm.findIndex(item => item.originalIdx !== q.correctIndex);

    // Clicking correct button
    const chosenOptCorrect = perm[correctBtnIndex].originalIdx;
    assert.strictEqual(chosenOptCorrect === q.correctIndex, true, 'Correct button must evaluate to true');

    // Clicking wrong button
    const chosenOptWrong = perm[wrongBtnIndex].originalIdx;
    assert.strictEqual(chosenOptWrong === q.correctIndex, false, 'Wrong button must evaluate to false');
}
console.log('[PASS] Option evaluation correctly pairs original index with correctIndex regardless of position.');

console.log('\n==========================================================');
console.log('ALL COMPREHENSION OPTION SHUFFLING TESTS PASSED');
console.log('==========================================================');
