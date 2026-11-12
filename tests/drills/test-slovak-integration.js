// ============================================
// SLOVAK FULL INTEGRATION TEST SUITE
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock browser globals for node testing
global.window = global;
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: () => null,
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

// 1. Slovak Morphology, Vocalizations & Clitic Peeling
require('../../engine/morphology/slovak.js');
assert(typeof SlovakMorphology !== 'undefined', 'SlovakMorphology must be defined');
assert(typeof SlovakMorphology.analyze === 'function', 'SlovakMorphology must export analyze()');
assert(typeof SlovakMorphology.lookup === 'function', 'SlovakMorphology must export lookup()');

// Contractions & vocalizations
assert(SlovakMorphology.contractions['vo'] && SlovakMorphology.contractions['vo'].lemma === 'v', 'vo should resolve to v');
assert(SlovakMorphology.contractions['so'] && SlovakMorphology.contractions['so'].lemma === 's', 'so should resolve to s');
assert(SlovakMorphology.contractions['zo'] && SlovakMorphology.contractions['zo'].lemma === 'z', 'zo should resolve to z');
assert(SlovakMorphology.contractions['ku'] && SlovakMorphology.contractions['ku'].lemma === 'k', 'ku should resolve to k');
assert(SlovakMorphology.contractions['odo'] && SlovakMorphology.contractions['odo'].lemma === 'od', 'odo should resolve to od');

// Mobile clitic & enclitic peeling
const clitics1 = SlovakMorphology.peelClitics('robilas');
assert(clitics1 && clitics1.some(c => c.stem === 'robila' && c.clitic === 's'), 'robilas should peel to stem robila and clitic s');

const clitics2 = SlovakMorphology.peelClitics('bols');
assert(clitics2 && clitics2.some(c => c.stem === 'bol' && c.clitic === 's'), 'bols should peel to stem bol and clitic s');

const clitics3 = SlovakMorphology.peelClitics('abys');
assert(clitics3 && clitics3.some(c => c.stem === 'aby' && c.clitic === 's'), 'abys should peel to stem aby and clitic s');

// Irregular verb / form lookup with morphology
const mockDict = {
    'ísť': { en: 'to go', type: 'verb' },
    'byť': { en: 'to be', type: 'verb' },
    'stôl': { en: 'table', type: 'noun', gender: 'm' },
    'pes': { en: 'dog', type: 'noun', gender: 'm' },
    'mesto': { en: 'town, city', type: 'noun', gender: 'n' }
};

const lookup1 = SlovakMorphology.lookup('šla', mockDict);
assert(lookup1 && lookup1.readings.some(r => r.lemma === 'ísť'), 'lookup šla should resolve to ísť');

const lookup2 = SlovakMorphology.lookup('stola', mockDict);
assert(lookup2 && lookup2.readings.some(r => r.lemma === 'stôl'), 'lookup stola should resolve to stôl (ô:o alternation)');

const lookup3 = SlovakMorphology.lookup('psa', mockDict);
assert(lookup3 && lookup3.readings.some(r => r.lemma === 'pes'), 'lookup psa should resolve to pes (fleeting vowel)');

const lookup4 = SlovakMorphology.lookup('miest', mockDict);
assert(lookup4 && lookup4.readings.some(r => r.lemma === 'mesto'), 'lookup miest should resolve to mesto (inserted ie in genitive plural)');

console.log('[PASS] SlovakMorphology rules, vocalizations, clitic peeling, and irregular lookup verified.');

// 2. Lang profile, paradigm & course availability gating
const Lang = require('../../engine/lang.js');
assert(Lang.profile('sk'), 'Lang.profile("sk") must be defined');
assert(Lang.voices('sk').includes('sk-SK'), 'Lang.voices("sk") must include sk-SK');
const skProfile = Lang.profile('sk');
assert(skProfile && skProfile.diacritics, 'Slovak profile must define diacritics');
assert(skProfile.examLabels && skProfile.examLabels.trueFalseNotStated, 'Slovak profile must define examLabels');
const skParadigm = Lang.paradigm('sk');
assert(skParadigm && skParadigm.defaultPersons.length === 6, 'Slovak paradigm must define 6 grammatical persons');

// Gating check: Slovak must NOT be in AVAILABLE course picker until lessons are ready
assert(!Lang.available().includes('sk'), 'Slovak must be gated from AVAILABLE courses in Lang.js');

console.log('[PASS] Lang profile, paradigm, voices, and availability gating for Slovak verified.');

// 3. Speech phonetic folding
const SpeechInput = require('../../engine/speech-input.js');
assert(typeof SpeechInput !== 'undefined' && typeof SpeechInput.phoneticFold === 'function', 'SpeechInput must export phoneticFold');

// Homophones i / y and í / ý
assert.strictEqual(SpeechInput.phoneticFold('byť', 'sk'), SpeechInput.phoneticFold('biť', 'sk'), 'byť and biť should fold identically');
assert.strictEqual(SpeechInput.phoneticFold('my', 'sk'), SpeechInput.phoneticFold('mi', 'sk'), 'my and mi should fold identically');

// ä / e
assert.strictEqual(SpeechInput.phoneticFold('mäso', 'sk'), SpeechInput.phoneticFold('meso', 'sk'), 'mäso and meso should fold identically');

// Soft consonants before e / i
assert.strictEqual(SpeechInput.phoneticFold('deti', 'sk'), SpeechInput.phoneticFold('ďeťi', 'sk'), 'deti and ďeťi should fold identically');

// Word-final devoicing
assert.strictEqual(SpeechInput.phoneticFold('dub', 'sk'), SpeechInput.phoneticFold('dup', 'sk'), 'dub and dup should fold identically (final b -> p)');
assert.strictEqual(SpeechInput.phoneticFold('ľad', 'sk'), SpeechInput.phoneticFold('ľat', 'sk'), 'ľad and ľat should fold identically (final d -> t)');
assert.strictEqual(SpeechInput.phoneticFold('mráz', 'sk'), SpeechInput.phoneticFold('mrás', 'sk'), 'mráz and mrás should fold identically (final z -> s)');
assert.strictEqual(SpeechInput.phoneticFold('chlieb', 'sk'), SpeechInput.phoneticFold('chliep', 'sk'), 'chlieb and chliep should fold identically (final b -> p)');

console.log('[PASS] Slovak speech phonetic folding (homophones, devoicing, palatals) verified.');

// 4. Slovak Grammar Studio & Workshop registration
require('../../engine/drills/sk-grammar-studio.js');
assert(typeof SkGrammarStudio !== 'undefined', 'SkGrammarStudio must be defined');
assert(typeof SkGrammarStudio.render === 'function', 'SkGrammarStudio must export render()');
assert(typeof SkGrammarStudio.stop === 'function', 'SkGrammarStudio must export stop()');
assert(Array.isArray(SkGrammarStudio.TABS) && SkGrammarStudio.TABS.length === 5, 'SkGrammarStudio must define 5 drill tabs');

// Test question pools
for (const tab of SkGrammarStudio.TABS) {
    const pool = SkGrammarStudio._poolFor(tab.id);
    assert(Array.isArray(pool) && pool.length >= 10, `Tab ${tab.id} must have at least 10 questions, found ${pool ? pool.length : 0}`);
}

// Workshop integration
global.Lang.code = () => 'sk';
global.Lang.name = () => 'Slovak';
require('../../engine/workshop.js');
const skDrillerDef = Workshop.getDriller('sk-grammar-studio');
assert(skDrillerDef && skDrillerDef.langs.includes('sk'), 'sk-grammar-studio must support "sk" in Workshop');

const verbDrillerDef = Workshop.getDriller('verbs');
assert(verbDrillerDef && verbDrillerDef.langs.includes('sk'), 'verbs driller must support "sk" in Workshop');

const eclDrillerDef = Workshop.getDriller('sk-ecl-b1-exam');
assert(eclDrillerDef && eclDrillerDef.langs.includes('sk'), 'sk-ecl-b1-exam must support "sk" in Workshop');

Workshop.close();
Workshop.open('sk-grammar-studio');
const activeStudio = Workshop.activeDriller();
assert(activeStudio && activeStudio.id === 'sk-grammar-studio', 'sk-grammar-studio should open in Workshop');

console.log('[PASS] SkGrammarStudio tabs, 10 questions per tab, and Workshop integration verified.');

// 5. Verbs dataset verification
require('../../imports/verbs/sk/verb-list-sk.js');
assert(Array.isArray(ALL_SLOVAK_VERBS) && ALL_SLOVAK_VERBS.length >= 100, `ALL_SLOVAK_VERBS must contain >= 100 verbs, found ${ALL_SLOVAK_VERBS.length}`);

// Test loading top verbs
const bytData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/sk/byť.json'), 'utf8'));
assert(bytData.infinitive === 'byť' && bytData.indicativo && bytData.indicativo.presente, 'byť.json must be valid with indicativo.presente');
assert.strictEqual(bytData.indicativo.presente.ja, 'som');

const matData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/sk/mať.json'), 'utf8'));
assert(matData.infinitive === 'mať' && matData.indicativo && matData.indicativo.presente, 'mať.json must be valid with indicativo.presente');
assert.strictEqual(matData.indicativo.presente.ja, 'mám');

const robitData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/sk/robiť.json'), 'utf8'));
assert(robitData.infinitive === 'robiť' && robitData.indicativo && robitData.indicativo.presente, 'robiť.json must be valid with indicativo.presente');
assert.strictEqual(robitData.indicativo.presente.ja, 'robím');

console.log('[PASS] Slovak verbs library datasets and conjugation tables verified.');

console.log('\n========================================');
console.log('ALL SLOVAK INTEGRATION TESTS PASSED!');
console.log('========================================');
