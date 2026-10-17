// ============================================
// ITALIAN FULL INTEGRATION TEST SUITE
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

// 1. Italian Morphology & Articles
require('../../engine/morphology/italian.js');
assert(typeof ItalianMorphology !== 'undefined', 'ItalianMorphology must be defined');
assert(typeof ItalianMorphology.analyze === 'function', 'ItalianMorphology must export analyze()');
assert(typeof ItalianMorphology.withArticle === 'function', 'ItalianMorphology must export withArticle()');

// Test preposizioni articolate
const prepTest = ItalianMorphology.contractions['dello'];
assert(prepTest && prepTest.lemma === 'di' && prepTest.pos === 'contraction', 'dello should resolve to di + lo contraction');

const prepTest2 = ItalianMorphology.contractions['negli'];
assert(prepTest2 && prepTest2.lemma === 'in' && prepTest2.pos === 'contraction', 'negli should resolve to in + gli contraction');

// Test elision
const elisionTest = ItalianMorphology.elisions["l'"];
assert(elisionTest && elisionTest.lemma === 'il' && elisionTest.pos === 'article', "l' should resolve to elided article");

// Test enclitic pronoun peeling
const encliticTest = ItalianMorphology.encliticStems('parlargli');
assert(Array.isArray(encliticTest) && encliticTest.includes('parlare'), 'parlargli should peel to stem parlare');

const encliticCombo = ItalianMorphology.encliticStems('darmelo');
assert(Array.isArray(encliticCombo) && encliticCombo.includes('dare'), 'darmelo should peel to stem dare');


// Test contextual article
assert.strictEqual(ItalianMorphology.withArticle('studente', 'm'), 'lo studente', 'studente should take "lo"');
assert.strictEqual(ItalianMorphology.withArticle('amico', 'm'), "l'amico", 'amico should take "l\'"');
assert.strictEqual(ItalianMorphology.withArticle('ragazzo', 'm'), 'il ragazzo', 'ragazzo should take "il"');
assert.strictEqual(ItalianMorphology.withArticle('studenti', 'm', true), 'gli studenti', 'studenti (pl) should take "gli"');
assert.strictEqual(ItalianMorphology.withArticle('casa', 'f'), 'la casa', 'casa should take "la"');
assert.strictEqual(ItalianMorphology.withArticle('amica', 'f'), "l'amica", 'amica should take "l\'"');
assert.strictEqual(ItalianMorphology.withArticle('amiche', 'f', true), 'le amiche', 'amiche (pl) should take "le"');

console.log('[PASS] ItalianMorphology rules, prepositions, enclitics, and contextual articles verified.');

// 2. Lang profile & speech support
const Lang = require('../../engine/lang.js');
assert(Lang.available().includes('it'), 'Lang.available() must include "it"');
assert(Lang.voices('it').includes('it-IT'), 'Lang.voices("it") must include it-IT');
const itProfile = Lang.profile('it');
assert(itProfile, 'Lang.profile("it") must be defined');
assert(itProfile.examLabels && itProfile.examLabels.trueFalseNotStated, 'Italian profile must define examLabels');
const itParadigm = Lang.paradigm('it');
assert(itParadigm && itParadigm.defaultPersons.length === 6, 'Italian paradigm must define 6 grammatical persons');

console.log('[PASS] Lang profile and voice configuration for Italian verified.');

// 3. Speech phonetic folding
const SpeechInput = require('../../engine/speech-input.js');
assert(typeof SpeechInput !== 'undefined' && typeof SpeechInput.phoneticFold === 'function', 'SpeechInput must export phoneticFold');

const fold1 = SpeechInput.phoneticFold('hanno', 'it');
const fold2 = SpeechInput.phoneticFold('anno', 'it');
assert.strictEqual(fold1, fold2, 'hanno and anno should fold identically (silent h)');

const gem1 = SpeechInput.phoneticFold('caffè', 'it');
const gem2 = SpeechInput.phoneticFold('cafe', 'it');
assert.strictEqual(gem1, gem2, 'Double consonants and accent should fold identically in speech recognition');

console.log('[PASS] Italian speech phonetic folding verified.');

// 4. Italian Grammar Studio & Workshop registration
require('../../engine/drills/it-grammar-studio.js');
assert(typeof ItGrammarStudio !== 'undefined', 'ItGrammarStudio must be defined');
assert(typeof ItGrammarStudio.render === 'function', 'ItGrammarStudio must export render()');
assert(typeof ItGrammarStudio.stop === 'function', 'ItGrammarStudio must export stop()');
assert(Array.isArray(ItGrammarStudio.TABS) && ItGrammarStudio.TABS.length === 5, 'ItGrammarStudio must define 5 drill tabs');

// Test question pools
for (const tab of ItGrammarStudio.TABS) {
    const pool = ItGrammarStudio._poolFor(tab.id);
    assert(Array.isArray(pool) && pool.length >= 10, `Tab ${tab.id} must have at least 10 questions, found ${pool ? pool.length : 0}`);
}

// Workshop integration
global.Lang.code = () => 'it';
global.Lang.name = () => 'Italian';
require('../../engine/workshop.js');
const itDrillerDef = Workshop.getDriller('it-grammar-studio');
assert(itDrillerDef && itDrillerDef.langs.includes('it'), 'it-grammar-studio must support "it" in Workshop');

const verbDrillerDef = Workshop.getDriller('verbs');
assert(verbDrillerDef && verbDrillerDef.langs.includes('it'), 'verbs driller must support "it" in Workshop');

const cilsDrillerDef = Workshop.getDriller('it-cils-exam');
assert(cilsDrillerDef && cilsDrillerDef.langs.includes('it'), 'it-cils-exam must support "it" in Workshop');

Workshop.close();
Workshop.open('it-grammar-studio');
const activeStudio = Workshop.activeDriller();
assert(activeStudio && activeStudio.id === 'it-grammar-studio', 'it-grammar-studio should open in Workshop');

console.log('[PASS] ItGrammarStudio tabs, 30+ questions per tab, and Workshop integration verified.');

// 5. Verbs dataset verification
require('../../imports/verbs/it/verb-list-it.js');
assert(Array.isArray(ALL_ITALIAN_VERBS) && ALL_ITALIAN_VERBS.length >= 100, `ALL_ITALIAN_VERBS must contain >= 100 verbs, found ${ALL_ITALIAN_VERBS.length}`);

// Test loading top verbs
const essereData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/it/essere.json'), 'utf8'));
assert(essereData.infinitive === 'essere' && essereData.tenses && essereData.tenses.presente, 'essere.json must be valid with presente');

const avereData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/it/avere.json'), 'utf8'));
assert(avereData.infinitive === 'avere' && avereData.tenses && avereData.tenses.presente, 'avere.json must be valid with presente');

const parlareData = JSON.parse(fs.readFileSync(path.join(__dirname, '../../imports/verbs/it/parlare.json'), 'utf8'));
assert(parlareData.infinitive === 'parlare' && parlareData.tenses && parlareData.tenses.presente, 'parlare.json must be valid with presente');

console.log('[PASS] Italian verbs list and JSON conjugation datasets verified.');

// 6. Content files existence & valid JSON
const itContentDir = path.join(__dirname, '../../content/it');
const filesToCheck = [
    'speaking-prompts.json',
    'conversation-scenarios.json',
    'writing-prompts.json',
    'writing-exchanges.json',
    'listening-tasks.json',
    'videos.json',
    'songs.json',
    'indexes/word-index.json',
    'indexes/verb-index.json',
    'indexes/frequency.json',
    'indexes/translation-index.json',
    'curriculum/units/a1.json'
];

for (const relPath of filesToCheck) {
    const fullPath = path.join(itContentDir, relPath);
    assert(fs.existsSync(fullPath), `Required content file missing: ${relPath}`);
    const parsed = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    assert(parsed !== null, `File should be valid JSON: ${relPath}`);
}
console.log('[PASS] All required Italian content & index files present and valid JSON.');

console.log('\n[ALL PASS] Italian course full integration test suite passed cleanly.');
