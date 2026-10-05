const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('Testing LevelTest listening simulation & schema integration...\n');

// 1. Verify schema handles listeningSection
const schemaPath = path.join(__dirname, '..', 'content', 'es-es', 'schemas', 'test.schema.json');
assert(fs.existsSync(schemaPath), 'test.schema.json exists');
const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));

assert(schema.properties.listeningSection, 'listeningSection is defined in test.schema.json properties');
assert(schema.definitions.listeningQuestion, 'listeningQuestion is defined in test.schema.json definitions');

// 2. Verify content/es-es/tests/a1-test.json has valid listeningSection
const a1TestPath = path.join(__dirname, '..', 'content', 'es-es', 'tests', 'a1-test.json');
const a1Test = JSON.parse(fs.readFileSync(a1TestPath, 'utf8'));

assert(a1Test.listeningSection, 'a1-test.json has listeningSection');
assert.strictEqual(typeof a1Test.listeningSection.title, 'string', 'listeningSection has title');
assert(Array.isArray(a1Test.listeningSection.audio.turns), 'audio.turns is an array');
assert(a1Test.listeningSection.audio.turns.length >= 2, 'audio.turns has at least 2 turns for dialogue');
assert(Array.isArray(a1Test.listeningSection.questions), 'questions is an array');
assert(a1Test.listeningSection.questions.length >= 3, 'listeningSection has at least 3 questions');

a1Test.listeningSection.questions.forEach((q, idx) => {
    assert(q.id, `Question ${idx} has id`);
    assert(['listening-mc', 'true-false-not-stated'].includes(q.type), `Question ${idx} valid type`);
    assert(typeof q.correct === 'number', `Question ${idx} has correct index`);
    assert(typeof q.evidence === 'string', `Question ${idx} has evidence quote`);
});

console.log('✓ Schema and a1-test.json content validated.');

// 3. Test LevelTest module runtime behavior
// Setup DOM mocks
global.document = {
    getElementById: (id) => {
        if (id === 'leveltest-root') {
            return {
                innerHTML: '',
                querySelector: () => null,
                querySelectorAll: () => []
            };
        }
        return null;
    },
    querySelector: () => null,
    querySelectorAll: () => []
};

global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};

global.Lang = {
    current: () => 'es',
    code: () => 'es-es',
    key: (k) => 'test_' + k,
    content: (p) => p
};

global.UI = {
    escape: (s) => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'),
    toast: () => {}
};

global.ParlourTTS = {
    speak: ({ onEnded }) => { if (onEnded) setTimeout(onEnded, 10); },
    preload: () => {},
    stop: () => {}
};

const LevelTest = require('../engine/leveltest.js');
assert(LevelTest, 'LevelTest exported');
assert.strictEqual(typeof LevelTest.hasTest, 'function', 'hasTest function exported');
assert(LevelTest.hasTest('A1'), 'LevelTest hasTest A1');

console.log('✓ LevelTest runtime exports verified.');
console.log('\nAll LevelTest listening simulation checks passed successfully!');
