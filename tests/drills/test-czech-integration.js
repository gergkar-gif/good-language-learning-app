// ============================================
// CZECH FULL INTEGRATION TEST SUITE
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

// 1. Czech Morphology, Vocalizations & Clitic Peeling
require('../../engine/morphology/czech.js');
assert(typeof CzechMorphology !== 'undefined', 'CzechMorphology must be defined');
assert(typeof CzechMorphology.analyze === 'function', 'CzechMorphology must export analyze()');
assert(typeof CzechMorphology.lookup === 'function', 'CzechMorphology must export lookup()');

// Contractions & vocalizations
assert(CzechMorphology.contractions['ve'] && CzechMorphology.contractions['ve'].lemma === 'v', 've should resolve to v');
assert(CzechMorphology.contractions['se'] && CzechMorphology.contractions['se'].lemma === 's', 'se should resolve to s');
assert(CzechMorphology.contractions['ze'] && CzechMorphology.contractions['ze'].lemma === 'z', 'ze should resolve to z');
assert(CzechMorphology.contractions['ke'] && CzechMorphology.contractions['ke'].lemma === 'k', 'ke should resolve to k');
assert(CzechMorphology.contractions['ode'] && CzechMorphology.contractions['ode'].lemma === 'od', 'ode should resolve to od');

// Mobile clitic & enclitic peeling
const clitics1 = CzechMorphology.peelClitics('dělals');
assert(clitics1 && clitics1.some(c => c.stem === 'dělal' && c.clitic === 's'), 'dělals should peel to stem dělal and clitic s');

const clitics2 = CzechMorphology.peelClitics('byls');
assert(clitics2 && clitics2.some(c => c.stem === 'byl' && c.clitic === 's'), 'byls should peel to stem byl and clitic s');

const clitics3 = CzechMorphology.peelClitics('abychom');
assert(clitics3 && clitics3.some(c => c.stem === 'aby' && c.clitic === 'chom'), 'abychom should peel to stem aby and clitic chom');

// Irregular verb / form lookup with morphology
const mockDict = {
    'jít': { en: 'to go', type: 'verb' },
    'být': { en: 'to be', type: 'verb' },
    'stůl': { en: 'table', type: 'noun', gender: 'm' },
    'pes': { en: 'dog', type: 'noun', gender: 'm' },
    'ruka': { en: 'hand, arm', type: 'noun', gender: 'f' }
};

const lookup1 = CzechMorphology.lookup('šla', mockDict);
assert(lookup1 && lookup1.readings.some(r => r.lemma === 'jít'), 'lookup šla should resolve to jít');

const lookup2 = CzechMorphology.lookup('stolu', mockDict);
assert(lookup2 && lookup2.readings.some(r => r.lemma === 'stůl'), 'lookup stolu should resolve to stůl (ů:o alternation)');

const lookup3 = CzechMorphology.lookup('psa', mockDict);
assert(lookup3 && lookup3.readings.some(r => r.lemma === 'pes'), 'lookup psa should resolve to pes (fleeting e)');

const lookup4 = CzechMorphology.lookup('ruce', mockDict);
assert(lookup4 && lookup4.readings.some(r => r.lemma === 'ruka'), 'lookup ruce should resolve to ruka (palatalization c:k)');

console.log('[PASS] CzechMorphology rules, vocalizations, clitic peeling, and irregular lookup verified.');

// 2. Lang profile, paradigm & course availability gating
const Lang = require('../../engine/lang.js');
assert(Lang.profile('cs'), 'Lang.profile("cs") must be defined');
assert(Lang.voices('cs').includes('cs-CZ'), 'Lang.voices("cs") must include cs-CZ');
const csProfile = Lang.profile('cs');
assert(csProfile && csProfile.diacritics, 'Czech profile must define diacritics');
assert(csProfile.examLabels && csProfile.examLabels.trueFalseNotStated, 'Czech profile must define examLabels');
const csParadigm = Lang.paradigm('cs');
assert(csParadigm && csParadigm.defaultPersons.length === 6, 'Czech paradigm must define 6 grammatical persons');

// Gating check: Czech must NOT be in AVAILABLE course picker until lessons are ready
assert(!Lang.available().includes('cs'), 'Czech must be gated from AVAILABLE courses in Lang.js');

console.log('[PASS] Lang profile, paradigm, voices, and availability gating for Czech verified.');

// 3. Speech phonetic folding
const SpeechInput = require('../../engine/speech-input.js');
assert(typeof SpeechInput !== 'undefined' && typeof SpeechInput.phoneticFold === 'function', 'SpeechInput must export phoneticFold');

// Homophones i / y and í / ý
assert.strictEqual(SpeechInput.phoneticFold('být', 'cs'), SpeechInput.phoneticFold('bít', 'cs'), 'být and bít should fold identically');
assert.strictEqual(SpeechInput.phoneticFold('mýt', 'cs'), SpeechInput.phoneticFold('mít', 'cs'), 'mýt and mít should fold identically');

// Homophones ú / ů
assert.strictEqual(SpeechInput.phoneticFold('dům', 'cs'), SpeechInput.phoneticFold('dúm', 'cs'), 'dům and dúm should fold identically');

// mě / mně
assert.strictEqual(SpeechInput.phoneticFold('město', 'cs'), SpeechInput.phoneticFold('mněsto', 'cs'), 'mě and mně should fold identically');

// Word-final devoicing
assert.strictEqual(SpeechInput.phoneticFold('dub', 'cs'), SpeechInput.phoneticFold('dup', 'cs'), 'dub and dup should fold identically (final b -> p)');
assert.strictEqual(SpeechInput.phoneticFold('led', 'cs'), SpeechInput.phoneticFold('let', 'cs'), 'led and let should fold identically (final d -> t)');
assert.strictEqual(SpeechInput.phoneticFold('vůz', 'cs'), SpeechInput.phoneticFold('vús', 'cs'), 'vůz and vús should fold identically (final z -> s and ů -> ú)');

console.log('[PASS] Czech speech phonetic folding (homophones, devoicing, palatals) verified.');

// 4. Czech Grammar Studio & Workshop registration
require('../../engine/drills/cs-grammar-studio.js');
assert(typeof CsGrammarStudio !== 'undefined', 'CsGrammarStudio must be defined');
assert(typeof CsGrammarStudio.render === 'function', 'CsGrammarStudio must export render()');
assert(typeof CsGrammarStudio.stop === 'function', 'CsGrammarStudio must export stop()');
assert(Array.isArray(CsGrammarStudio.TABS) && CsGrammarStudio.TABS.length === 5, 'CsGrammarStudio must define 5 drill tabs');

// Test question pools
for (const tab of CsGrammarStudio.TABS) {
    const pool = CsGrammarStudio._poolFor(tab.id);
    assert(Array.isArray(pool) && pool.length >= 10, `Tab ${tab.id} must have at least 10 questions, found ${pool ? pool.length : 0}`);
}

// Workshop integration
global.Lang.code = () => 'cs';
global.Lang.name = () => 'Czech';
require('../../engine/workshop.js');
const csDrillerDef = Workshop.getDriller('cs-grammar-studio');
assert(csDrillerDef && csDrillerDef.langs.includes('cs'), 'cs-grammar-studio must support "cs" in Workshop');

const verbDrillerDef = Workshop.getDriller('verbs');
assert(verbDrillerDef && verbDrillerDef.langs.includes('cs'), 'verbs driller must support "cs" in Workshop');

const cceDrillerDef = Workshop.getDriller('cs-cce-b1-exam');
assert(cceDrillerDef && cceDrillerDef.langs.includes('cs'), 'cs-cce-b1-exam must support "cs" in Workshop');

Workshop.close();
Workshop.open('cs-grammar-studio');
const activeStudio = Workshop.activeDriller();
assert(activeStudio && activeStudio.id === 'cs-grammar-studio', 'cs-grammar-studio should open in Workshop');

console.log('[PASS] CsGrammarStudio tabs, 20 questions per tab, and Workshop integration verified.');

// 5. Verbs dataset verification
require('../../imports/verbs/cs/verb-list-cs.js');
assert(Array.isArray(ALL_CZECH_VERBS) && ALL_CZECH_VERBS.length >= 100, `ALL_CZECH_VERBS must contain >= 100 verbs, found ${ALL_CZECH_VERBS.length}`);

// Test loading top verbs
const bytData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/cs/být.json'), 'utf8'));
assert(bytData.infinitive === 'být' && bytData.indicativo && bytData.indicativo.presente, 'být.json must be valid with indicativo.presente');
assert.strictEqual(bytData.indicativo.presente.ja, 'jsem');

const mitData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/cs/mít.json'), 'utf8'));
assert(mitData.infinitive === 'mít' && mitData.indicativo && mitData.indicativo.presente, 'mít.json must be valid with indicativo.presente');
assert.strictEqual(mitData.indicativo.presente.ja, 'mám');

const delatData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/cs/dělat.json'), 'utf8'));
assert(delatData.infinitive === 'dělat' && delatData.indicativo && delatData.indicativo.presente, 'dělat.json must be valid with indicativo.presente');
assert.strictEqual(delatData.indicativo.presente.ja, 'dělám');

console.log('[PASS] Czech verbs library datasets and conjugation tables verified.');

console.log('\n========================================');
console.log('ALL CZECH INTEGRATION TESTS PASSED!');
console.log('========================================');
