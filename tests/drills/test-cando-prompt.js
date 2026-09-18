// ============================================
// CAN-DO PROMPT & SCAFFOLDING UNIT TESTS
// ============================================
const assert = require('assert');

// Mock browser globals for testing
global.window = global;
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
    createElement: (tag) => ({
        innerHTML: '',
        textContent: '',
        appendChild: () => {},
        setAttribute: () => {},
        querySelectorAll: () => [],
        querySelector: () => null
    })
};
global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};
global.Lang = {
    code: () => 'hu',
    name: () => 'Hungarian',
    content: (p) => p,
    set: () => {}
};
global.Content = {
    json: async () => ({ pairs: [], prompts: [] })
};

// 1. Load CanDoPrompt module
require('../../engine/canDoPrompt.js');
assert(typeof CanDoPrompt !== 'undefined', 'CanDoPrompt must be defined');
assert(typeof CanDoPrompt.formatPrompt === 'function', 'CanDoPrompt.formatPrompt must be exported');
assert(typeof CanDoPrompt.extractCleanTitle === 'function', 'CanDoPrompt.extractCleanTitle must be exported');

console.log('--- Test 1: Clean Title Extraction ---');
const t1 = CanDoPrompt.extractCleanTitle('I can name all twelve months and say which month something is in.');
assert.strictEqual(t1, 'Months of the Year', `Expected "Months of the Year", got "${t1}"`);

const t2 = CanDoPrompt.extractCleanTitle('I can complete a short at the café interaction.');
assert.strictEqual(t2, 'At the Café', `Expected "At the Café", got "${t2}"`);

const t3 = CanDoPrompt.extractCleanTitle('I can describe my daily routine.');
assert.strictEqual(t3, 'Daily Routine', `Expected "Daily Routine", got "${t3}"`);

const t4 = CanDoPrompt.extractCleanTitle('I can ask for and understand simple directions in town.');
assert.strictEqual(t4, 'Asking for Directions', `Expected "Asking for Directions", got "${t4}"`);

const t5 = CanDoPrompt.extractCleanTitle('I can greet someone and introduce myself.');
assert.strictEqual(t5, 'Greetings & Introductions', `Expected "Greetings & Introductions", got "${t5}"`);
console.log('[PASS] Title extraction creates clean, readable titles without truncation.');

console.log('--- Test 2: Months of the Year (Hungarian & Spanish) ---');
const huMonths = CanDoPrompt.formatPrompt('I can name all twelve months and say which month something is in.', {
    language: 'Hungarian',
    langCode: 'hu',
    modality: 'oral'
});
assert.strictEqual(huMonths.type, 'enumeration');
assert.strictEqual(huMonths.title, 'Months of the Year');
assert(huMonths.prompt.includes('Say the months of the year in Hungarian'), 'Prompt should mention months of the year');
assert(huMonths.prompt.includes('birthday'), 'Prompt should mention birthday/event');
assert(huMonths.cues.length >= 2, 'Should have at least 2 scaffolding cues');
assert(huMonths.cues[0].includes('január'), 'Hungarian cues should include Hungarian month examples');
assert(huMonths.cues[1].includes('-ban / -ben'), 'Hungarian cues should mention -ban / -ben suffix');

const esMonths = CanDoPrompt.formatPrompt('I can name all twelve months and say which month something is in.', {
    language: 'Spanish',
    langCode: 'es',
    modality: 'oral'
});
assert.strictEqual(esMonths.type, 'enumeration');
assert(esMonths.cues[0].includes('enero'), 'Spanish cues should include Spanish month examples');
assert(esMonths.cues[1].includes('"en"'), 'Spanish cues should mention "en" preposition');
console.log('[PASS] Months enumeration formatting correctly scaffolded.');

console.log('--- Test 3: Café Interaction ---');
const huCafe = CanDoPrompt.formatPrompt('I can complete a short at the café interaction.', {
    language: 'Hungarian',
    langCode: 'hu',
    modality: 'oral'
});
assert.strictEqual(huCafe.type, 'transaction');
assert.strictEqual(huCafe.title, 'At the Café');
assert(huCafe.scenario.includes('café'), 'Scenario should mention café');
assert(huCafe.prompt.includes('Order at the café'), 'Prompt should be active ordering task');
assert(huCafe.cues.length >= 3, 'Café transaction should provide 3-part dialogue cues');
assert(huCafe.cues[1].includes('Kérek'), 'Hungarian cue should suggest Kérek');
console.log('[PASS] Café interaction correctly scaffolded.');

console.log('--- Test 4: Personal Monologue (Daily Routine) ---');
const routine = CanDoPrompt.formatPrompt('I can describe my daily routine.', {
    language: 'Spanish',
    langCode: 'es',
    modality: 'oral'
});
assert.strictEqual(routine.type, 'monologue');
assert.strictEqual(routine.title, 'Daily Routine');
assert(routine.prompt.includes('daily routine'), 'Prompt should instruct describing daily routine');
assert(routine.cues.length >= 2, 'Monologue should provide guidance cues');
console.log('[PASS] Monologue prompt correctly scaffolded.');

console.log('--- Test 5: SpeakingDriller Integration with CanDoPrompt ---');
require('../../engine/drills/speaking.js');
const mockContainer = { innerHTML: '', querySelector: () => null, querySelectorAll: () => [] };

SpeakingDriller.render(mockContainer, {
    targetCompetency: 'I can complete a short at the café interaction.',
    level: 'A1',
    maxSeconds: 40
}).then(() => {
    SpeakingDriller.stop();
    console.log('[PASS] SpeakingDriller correctly initializes with CanDoPrompt formatted prompt.');
    console.log('\n[ALL PASS] Can-Do Prompt & Scaffolding Test Suite passed.');
}).catch((e) => {
    console.error('SpeakingDriller render error:', e);
    process.exit(1);
});
