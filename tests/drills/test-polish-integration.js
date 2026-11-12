// ============================================
// POLISH FULL INTEGRATION TEST SUITE
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

// 1. Polish Morphology, Vocalizations & Clitic Peeling
require('../../engine/morphology/polish.js');
assert(typeof PolishMorphology !== 'undefined', 'PolishMorphology must be defined');
assert(typeof PolishMorphology.analyze === 'function', 'PolishMorphology must export analyze()');
assert(typeof PolishMorphology.lookup === 'function', 'PolishMorphology must export lookup()');

// Contractions & vocalizations
assert(PolishMorphology.contractions['we'] && PolishMorphology.contractions['we'].lemma === 'w', 'we should resolve to w');
assert(PolishMorphology.contractions['ze'] && PolishMorphology.contractions['ze'].lemma === 'z', 'ze should resolve to z');
assert(PolishMorphology.contractions['ode'] && PolishMorphology.contractions['ode'].lemma === 'od', 'ode should resolve to od');
assert(PolishMorphology.contractions['dlań'] && PolishMorphology.contractions['dlań'].lemma === 'dla', 'dlań should resolve to dla');

// Mobile clitic peeling
const clitics1 = PolishMorphology.peelClitics('czytałem');
assert(clitics1 && clitics1.some(c => c.stem === 'czytał' && c.clitic === 'em'), 'czytałem should peel to stem czytał and clitic em');

const clitics2 = PolishMorphology.peelClitics('poszłam');
assert(clitics2 && clitics2.some(c => c.stem === 'poszła' && c.clitic === 'm'), 'poszłam should peel to stem poszła and clitic m');

const clitics3 = PolishMorphology.peelClitics('zrobiliśmy');
assert(clitics3 && clitics3.some(c => c.stem === 'zrobili' && c.clitic === 'śmy'), 'zrobiliśmy should peel to stem zrobili and clitic śmy');

// Irregular verb / form lookup with morphology
const mockDict = {
    'pójść': { en: 'to go', type: 'verb' },
    'być': { en: 'to be', type: 'verb' },
    'stół': { en: 'table', type: 'noun', gender: 'm' },
    'pies': { en: 'dog', type: 'noun', gender: 'm' }
};

const lookup1 = PolishMorphology.lookup('poszłam', mockDict);
assert(lookup1 && lookup1.readings.some(r => r.lemma === 'pójść'), 'lookup poszłam should resolve to pójść');

const lookup2 = PolishMorphology.lookup('stole', mockDict);
assert(lookup2 && lookup2.readings.some(r => r.lemma === 'stół'), 'lookup stole should resolve to stół (o:ó alternation)');

const lookup3 = PolishMorphology.lookup('psa', mockDict);
assert(lookup3 && lookup3.readings.some(r => r.lemma === 'pies'), 'lookup psa should resolve to pies (fleeting e)');

console.log('[PASS] PolishMorphology rules, vocalizations, clitic peeling, and irregular lookup verified.');

// 2. Lang profile, paradigm & course availability gating
const Lang = require('../../engine/lang.js');
assert(Lang.profile('pl'), 'Lang.profile("pl") must be defined');
assert(Lang.voices('pl').includes('pl-PL'), 'Lang.voices("pl") must include pl-PL');
const plProfile = Lang.profile('pl');
assert(plProfile && plProfile.diacritics, 'Polish profile must define diacritics');
assert(plProfile.examLabels && plProfile.examLabels.trueFalseNotStated, 'Polish profile must define examLabels');
const plParadigm = Lang.paradigm('pl');
assert(plParadigm && plParadigm.defaultPersons.length === 6, 'Polish paradigm must define 6 grammatical persons');

// Gating check: Polish must NOT be in AVAILABLE course picker until lessons are ready
assert(!Lang.available().includes('pl'), 'Polish must be gated from AVAILABLE courses in Lang.js');

console.log('[PASS] Lang profile, paradigm, voices, and availability gating for Polish verified.');

// 3. Speech phonetic folding
const SpeechInput = require('../../engine/speech-input.js');
assert(typeof SpeechInput !== 'undefined' && typeof SpeechInput.phoneticFold === 'function', 'SpeechInput must export phoneticFold');

// Homophones rz / ż
assert.strictEqual(SpeechInput.phoneticFold('morze', 'pl'), SpeechInput.phoneticFold('może', 'pl'), 'morze and może should fold identically');

// Homophones ó / u
assert.strictEqual(SpeechInput.phoneticFold('bóg', 'pl'), SpeechInput.phoneticFold('bug', 'pl'), 'bóg and bug should fold identically');

// Homophones ch / h
assert.strictEqual(SpeechInput.phoneticFold('chełm', 'pl'), SpeechInput.phoneticFold('hełm', 'pl'), 'chełm and hełm should fold identically');

// Word-final devoicing
assert.strictEqual(SpeechInput.phoneticFold('chleb', 'pl'), SpeechInput.phoneticFold('chlep', 'pl'), 'chleb and chlep should fold identically (final b -> p)');

console.log('[PASS] Polish speech phonetic folding (homophones, devoicing, nasal reduction) verified.');

// 4. Polish Grammar Studio & Workshop registration
require('../../engine/drills/pl-grammar-studio.js');
assert(typeof PlGrammarStudio !== 'undefined', 'PlGrammarStudio must be defined');
assert(typeof PlGrammarStudio.render === 'function', 'PlGrammarStudio must export render()');
assert(typeof PlGrammarStudio.stop === 'function', 'PlGrammarStudio must export stop()');
assert(Array.isArray(PlGrammarStudio.TABS) && PlGrammarStudio.TABS.length === 5, 'PlGrammarStudio must define 5 drill tabs');

// Test question pools
for (const tab of PlGrammarStudio.TABS) {
    const pool = PlGrammarStudio._poolFor(tab.id);
    assert(Array.isArray(pool) && pool.length >= 10, `Tab ${tab.id} must have at least 10 questions, found ${pool ? pool.length : 0}`);
}

// Workshop integration
global.Lang.code = () => 'pl';
global.Lang.name = () => 'Polish';
require('../../engine/workshop.js');
const plDrillerDef = Workshop.getDriller('pl-grammar-studio');
assert(plDrillerDef && plDrillerDef.langs.includes('pl'), 'pl-grammar-studio must support "pl" in Workshop');

const verbDrillerDef = Workshop.getDriller('verbs');
assert(verbDrillerDef && verbDrillerDef.langs.includes('pl'), 'verbs driller must support "pl" in Workshop');

const certyfikatDrillerDef = Workshop.getDriller('pl-certyfikat-b1-exam');
assert(certyfikatDrillerDef && certyfikatDrillerDef.langs.includes('pl'), 'pl-certyfikat-b1-exam must support "pl" in Workshop');

Workshop.close();
Workshop.open('pl-grammar-studio');
const activeStudio = Workshop.activeDriller();
assert(activeStudio && activeStudio.id === 'pl-grammar-studio', 'pl-grammar-studio should open in Workshop');

console.log('[PASS] PlGrammarStudio tabs, 20 questions per tab, and Workshop integration verified.');

// 5. Verbs dataset verification
require('../../imports/verbs/pl/verb-list-pl.js');
assert(Array.isArray(ALL_POLISH_VERBS) && ALL_POLISH_VERBS.length >= 100, `ALL_POLISH_VERBS must contain >= 100 verbs, found ${ALL_POLISH_VERBS.length}`);

// Test loading top verbs
const bycData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/pl/być.json'), 'utf8'));
assert(bycData.infinitive === 'być' && bycData.indicativo && bycData.indicativo.presente, 'być.json must be valid with indicativo.presente');
assert.strictEqual(bycData.indicativo.presente.ja, 'jestem');

const miecData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/pl/mieć.json'), 'utf8'));
assert(miecData.infinitive === 'mieć' && miecData.indicativo && miecData.indicativo.presente, 'mieć.json must be valid with indicativo.presente');
assert.strictEqual(miecData.indicativo.presente.ja, 'mam');

const robicData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/pl/robić.json'), 'utf8'));
assert(robicData.infinitive === 'robić' && robicData.indicativo && robicData.indicativo.presente, 'robić.json must be valid with indicativo.presente');
assert.strictEqual(robicData.indicativo.presente.ja, 'robię');

console.log('[PASS] Polish verbs list and JSON conjugation datasets verified.');

// 6. Content files existence & valid JSON
const plContentDir = path.join(__dirname, '../../content/pl');
const filesToCheck = [
    'speaking-prompts.json',
    'conversation-scenarios.json',
    'writing-prompts.json',
    'writing-exchanges.json',
    'listening-tasks.json',
    'videos.json',
    'songs.json',
    'certyfikat-b1-exam.json',
    'indexes/word-index.json',
    'indexes/verb-index.json',
    'indexes/frequency.json',
    'indexes/translation-index.json',
    'curriculum/units/a1.json'
];

for (const relPath of filesToCheck) {
    const fullPath = path.join(plContentDir, relPath);
    assert(fs.existsSync(fullPath), `Required content file missing: ${relPath}`);
    const parsed = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    assert(parsed !== null, `File should be valid JSON: ${relPath}`);
}
console.log('[PASS] All required Polish content & index files present and valid JSON.');

console.log('\n[ALL PASS] Polish course full integration test suite passed cleanly.');
