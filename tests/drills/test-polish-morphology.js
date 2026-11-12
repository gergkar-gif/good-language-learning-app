const assert = require('assert');

// Mock browser globals for node testing
global.window = global;
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: () => null
};

// 1. Polish Morphology & Vocalized Prepositions
require('../../engine/morphology/polish.js');
assert(typeof PolishMorphology !== 'undefined', 'PolishMorphology must be defined');
assert(typeof PolishMorphology.analyze === 'function', 'PolishMorphology must export analyze()');
assert(typeof PolishMorphology.withPreposition === 'function', 'PolishMorphology must export withPreposition()');

// Test vocalized prepositions
assert.strictEqual(PolishMorphology.withPreposition('w', 'Wrocławiu'), 'we Wrocławiu', 'w should vocalize to we before w+cons');
assert.strictEqual(PolishMorphology.withPreposition('w', 'Warszawie'), 'w Warszawie', 'w before single w+vowel remains w');
assert.strictEqual(PolishMorphology.withPreposition('z', 'szkoły'), 'ze szkoły', 'z should vocalize to ze before sz+cons');
assert.strictEqual(PolishMorphology.withPreposition('z', 'mną'), 'ze mną', 'z should vocalize to ze before mną');
assert.strictEqual(PolishMorphology.withPreposition('z', 'bratem'), 'z bratem', 'z before single b+cons remains z');
assert.strictEqual(PolishMorphology.withPreposition('od', 'mnie'), 'ode mnie', 'od should vocalize to ode before mnie');

// Test contractions
assert.strictEqual(PolishMorphology.contractions['we'].lemma, 'w');
assert.strictEqual(PolishMorphology.contractions['ze'].lemma, 'z');
assert.strictEqual(PolishMorphology.contractions['dlań'].lemma, 'dla');
assert.strictEqual(PolishMorphology.contractions['doń'].lemma, 'do');
assert.strictEqual(PolishMorphology.contractions['nań'].lemma, 'na');

// Test mobile clitic peeling
const p1 = PolishMorphology.peelClitics('czytałem');
assert(p1.some(c => c.stem === 'czytał' && c.clitic === 'em'), 'czytałem should peel to czytał + em');

const p2 = PolishMorphology.peelClitics('poszłam');
assert(p2.some(c => c.stem === 'poszła' && c.clitic === 'm'), 'poszłam should peel to poszła + m');

const p3 = PolishMorphology.peelClitics('zrobilibyśmy');
assert(p3.some(c => c.type === 'conditional'), 'zrobilibyśmy should resolve conditional clitic');

const p4 = PolishMorphology.peelClitics('coście');
assert(p4.some(c => c.stem === 'co' && c.clitic === 'ście'), 'coście should peel to co + ście');

// Test nominal/adjectival alternations & lookup
const mockDict = {
    'pójść': { en: 'to go', type: 'verb' },
    'być': { en: 'to be', type: 'verb' },
    'stół': { en: 'table', type: 'noun', gender: 'm' },
    'pies': { en: 'dog', type: 'noun', gender: 'm' },
    'polska': { en: 'Poland', type: 'proper noun', gender: 'f' }
};

const res1 = PolishMorphology.lookup('poszłam', mockDict);
assert(res1.readings.some(r => r.lemma === 'pójść'), 'lookup poszłam should resolve to pójść');

const res2 = PolishMorphology.lookup('stole', mockDict);
assert(res2.readings.some(r => r.lemma === 'stół'), 'lookup stole should resolve to stół (o:ó alternation)');

const res3 = PolishMorphology.lookup('psa', mockDict);
assert(res3.readings.some(r => r.lemma === 'pies'), 'lookup psa should resolve to pies (fleeting e)');

const res4 = PolishMorphology.lookup('Polsce', mockDict);
assert(res4.readings.some(r => r.lemma.toLowerCase() === 'polska'), 'lookup Polsce should resolve to polska (k:c palatalization)');

console.log('[PASS] PolishMorphology rules, vocalizations, clitics, and stem alternations verified.');

// 2. Lexicon integration
const Lexicon = require('../../engine/lexicon.js');
assert.strictEqual(Lexicon.getMorphology('pl'), PolishMorphology, 'Lexicon must register PolishMorphology for pl');

console.log('[PASS] Lexicon registration for Polish verified.');
console.log('\n[ALL PASS] Polish morphology integration tests passed cleanly.');
