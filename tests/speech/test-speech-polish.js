const assert = require('assert');

// Mock localStorage for node environment
global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};

const Lang = require('../../engine/lang.js');
const SpeechInput = require('../../engine/speech-input.js');

console.log('--- Testing Polish Lang Profile & Speech Phonetic Folding ---');

// 1. Language profile and availability gating
assert(!Lang.available().includes('pl'), 'Polish must remain excluded from AVAILABLE until lessons are authored');
const plProfile = Lang.profile('pl');
assert(plProfile, 'Polish profile must be defined');
assert.strictEqual(plProfile.name, 'Polish');
assert(plProfile.voices.includes('pl-PL'), 'Polish voices must include pl-PL');
assert.strictEqual(plProfile.sttLocale, 'pl-PL');
assert(Array.isArray(plProfile.paradigm.defaultPersons) && plProfile.paradigm.defaultPersons.length === 6, 'Polish paradigm must define 6 grammatical persons');
assert(plProfile.examLabels && plProfile.examLabels.trueFalseNotStated.length === 3, 'Polish examLabels must define trueFalseNotStated');

console.log('[PASS] Polish Lang profile and gating verified.');

// 2. Homophone folding
assert.strictEqual(SpeechInput.phoneticFold('morze', 'pl'), SpeechInput.phoneticFold('może', 'pl'), 'morze and może should fold identically (rz/ż)');
assert.strictEqual(SpeechInput.phoneticFold('bóg', 'pl'), SpeechInput.phoneticFold('buk', 'pl'), 'bóg and buk should fold identically (ó/u and g/k devoicing)');
assert.strictEqual(SpeechInput.phoneticFold('herbata', 'pl'), SpeechInput.phoneticFold('cherbata', 'pl'), 'herbata and cherbata should fold identically (h/ch)');
assert.strictEqual(SpeechInput.phoneticFold('lód', 'pl'), SpeechInput.phoneticFold('lut', 'pl'), 'lód and lut should fold identically (ó/u and d/t devoicing)');

// 3. Nasal vowel reduction at word end
assert.strictEqual(SpeechInput.phoneticFold('proszę', 'pl'), SpeechInput.phoneticFold('prosze', 'pl'), 'proszę and prosze should fold identically (-ę -> -e)');
assert.strictEqual(SpeechInput.phoneticFold('idę', 'pl'), SpeechInput.phoneticFold('ide', 'pl'), 'idę and ide should fold identically');

// 4. Final obstruent devoicing
assert.strictEqual(SpeechInput.phoneticFold('chleb', 'pl'), 'hlep', 'chleb should fold to hlep (ch->h, b->p)');
assert.strictEqual(SpeechInput.phoneticFold('paw', 'pl'), 'paf', 'paw should fold to paf (w->f)');
assert.strictEqual(SpeechInput.phoneticFold('teraz', 'pl'), 'teras', 'teraz should fold to teras (z->s)');

console.log('[PASS] Polish phonetic folding verified.');
console.log('\n[ALL PASS] Polish speech and language profile test suite passed.');
