// ========================================
// DECKS IMPORT TEST SUITE
// =======================================
const assert = require('assert');

global.window = global;
localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};
global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`,
    content: (p) => p
};
global.Lexicon = {
    isLoaded: () => true,
    load: async () => {},
    define: (word) => {
        const dict = {
            perro: { en: 'dog', type: 'noun' },
            gato: { en: 'cat', type: 'noun' },
            casa: { en: 'house', type: 'noun' },
            hablar: { en: 'to speak', type: 'verb' },
            kutya: { en: 'dog', type: 'noun' }
        };
        return dict[word.toLowerCase()] || null;
    },
    shortGloss: (en) => en ? en.split(/[,;]/)[0].trim() : ''
};

const Decks = require('../../engine/decks.js');
assert(typeof Decks.parseImportLines === 'function', 'Decks.parseImportLines must be exported');

console.log('--- Test 1: Quizlet tab-separated format ---');
const quizletSample = 'perro\tdog\ngato\tcat\ncasa\thouse';
const qParsed = Decks.parseImportLines(quizletSample);
assert.strictEqual(qParsed.length, 3, 'Should parse 3 lines');
assert.strictEqual(qParsed[0].lemma, 'perro');
assert.strictEqual(qParsed[0].translation, 'dog');
assert.strictEqual(qParsed[0].inLexicon, true);
assert.strictEqual(qParsed[0].pos, 'noun');
console.log('[PASS] Quizlet tab-separated format parsed successfully.');

console.log('\n--- Test 2: Anki text export with comments and HTML tags ---');
const ankiSample = '#separator:tab\n#html:true\n#tags:A1 vocab\n<b>hablar</b>\tto speak<br><div>to talk</div>\ncoche\tcar';
const ankiParsed = Decks.parseImportLines(ankiSample);
assert.strictEqual(ankiParsed.length, 2, 'Should skip headers and parse 2 cards');
assert.strictEqual(ankiParsed[0].lemma, 'hablar', 'HTML tags should be stripped from lemma');
assert.strictEqual(ankiParsed[0].pos, 'verb');
assert.strictEqual(ankiParsed[1].lemma, 'coche');
assert.strictEqual(ankiParsed[1].translation, 'car');
assert.strictEqual(ankiParsed[1].inLexicon, false);
console.log('[PASS] Anki export with HTML tags and header comments parsed cleanly.');

console.log('\n--- Test 3: CSV format with quotes ---');
const csvSample = '"perro","dog"\n"gato","feline, cat"';
const csvParsed = Decks.parseImportLines(csvSample, { delimiter: 'comma' });
assert.strictEqual(csvParsed.length, 2);
assert.strictEqual(csvParsed[0].lemma, 'perro');
assert.strictEqual(csvParsed[1].lemma, 'gato');
assert.strictEqual(csvParsed[1].translation, 'feline, cat');
console.log('[PASS] CSV format parsed correctly.');

console.log('\n--- Test 4: Dash and Colon auto-detection ---');
const dashSample = 'perro - dog\ngato — cat\ncasa : house';
const dashParsed = Decks.parseImportLines(dashSample);
assert.strictEqual(dashParsed.length, 3);
assert.strictEqual(dashParsed[0].lemma, 'perro');
assert.strictEqual(dashParsed[1].lemma, 'gato');
assert.strictEqual(dashParsed[2].lemma, 'casa');
console.log('[PASS] Dash and colon delimiters parsed correctly.');

console.log('\n--- Test 5: Column flipping (Target <-> English reversed) ---');
const reversedSample = 'dog\tperro\ncat\tgato';
const flippedParsed = Decks.parseImportLines(reversedSample, { flipped: true });
assert.strictEqual(flippedParsed.length, 2);
assert.strictEqual(flippedParsed[0].lemma, 'perro', 'Flipped mode should assign Spanish word to lemma');
assert.strictEqual(flippedParsed[0].translation, 'dog');
assert.strictEqual(flippedParsed[0].inLexicon, true);
console.log('[PASS] Column swapping verified.');


console.log('\n[ALL PASS] Decks importer test suite passed successfully.');
