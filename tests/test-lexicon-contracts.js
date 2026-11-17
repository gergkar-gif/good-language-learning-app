/**
 * Verifies Lexicon + morphology lookup() contract for fr, it, pl, cs, sk.
 * Run: node tests/test-lexicon-contracts.js
 */
const assert = require('assert');
const fs = require('fs');

let currentLang = 'fr';
global.window = global;
global.document = { addEventListener: () => {}, dispatchEvent: () => {} };
global.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
global.fetch = async (url) => {
    const clean = url.replace(/^\.\//, '');
    if (!fs.existsSync(clean)) {
        return { ok: false, status: 404, async json() { throw new Error('404 ' + clean); } };
    }
    return { ok: true, status: 200, async json() { return JSON.parse(fs.readFileSync(clean, 'utf8')); } };
};

const Lang = require('../engine/lang.js');
global.Lang = Lang;
Lang.code = () => currentLang;
Lang.content = (p) => `content/${currentLang}/${p}`;

const Lexicon = require('../engine/lexicon.js');
global.Lexicon = Lexicon;
require('../engine/morphology/french.js');
require('../engine/morphology/italian.js');
require('../engine/morphology/polish.js');
require('../engine/morphology/czech.js');
require('../engine/morphology/slovak.js');

(async () => {
    // 1. Direct unit checks (all 5 morphologies loaded cleanly with Lexicon.registerMorphology)
    for (const [lang, word, mockCtx] of [
        ['it', 'parlato', { normalise: s => s.toLowerCase(), dictionary: { parlare: { en: 'to speak', type: 'verb' } }, wordIndex: {}, verbIndex: {} }],
        ['pl', 'domu.', { normalise: s => s.toLowerCase(), dictionary: { dom: { en: 'house', type: 'noun', gender: 'm' } }, wordIndex: { domu: [{ lemma: 'dom', pos: 'noun', case: 'genitive', number: 'singular' }] }, verbIndex: {} }],
        ['cs', 'dělal', { normalise: s => s.toLowerCase(), dictionary: { dělat: { en: 'to do', type: 'verb' } }, wordIndex: {}, verbIndex: {} }],
        ['sk', 'mesta.', { normalise: s => s.toLowerCase(), dictionary: { mesto: { en: 'town', type: 'noun', gender: 'n' } }, wordIndex: {}, verbIndex: {} }]
    ]) {
        const res = Lexicon; // ensure module loaded
        assert(res, 'Lexicon loaded');
        const mod = lang === 'it' ? ItalianMorphology : lang === 'pl' ? PolishMorphology : lang === 'cs' ? CzechMorphology : SlovakMorphology;
        const out = mod.lookup(word, mockCtx);
        assert(out && Array.isArray(out.readings) && out.readings.length > 0, `${lang} ctx lookup failed for ${word}`);
        assert(typeof out.readings[0].lemma === 'string' && out.readings[0].lemma, `${lang} missing lemma`);
        assert(typeof out.readings[0].pos === 'string' && out.readings[0].pos, `${lang} missing pos`);
        assert(typeof out.readings[0].translation === 'string' && out.readings[0].translation, `${lang} missing translation`);

        const miss = mod.lookup('xyznotaword', mockCtx);
        assert(miss && Array.isArray(miss.readings) && miss.readings.length === 0, `${lang} miss must return readings: []`);
    }

    // 2. Full Lexicon.load() + lookup() across fr, it, pl, cs, sk real indexes
    for (const [lang, words] of [
        ['fr', ['parler', 'parlais', 'chocolats']],
        ['it', ['parlare', 'parlato', 'a', 'ti', 'anno']],
        ['pl', ['pójść', 'gratisy', 'czytałem', 'domu.', 'mówię', 'ja', 'i']],
        ['cs', ['dělat', 'dělám', 'hrady.']],
        ['sk', ['cestovať', 'cestujem', 'mesta.', 'august', 'nie', 'áno']]
    ]) {
        currentLang = lang;
        await Lexicon.load();
        for (const w of words) {
            const res = Lexicon.lookup(w);
            assert(res && Array.isArray(res.readings) && res.readings.length > 0, `${lang} Lexicon.lookup(${w}) empty`);
            const r0 = res.readings[0];
            assert(r0.lemma && r0.pos && typeof r0.translation === 'string', `${lang} bad reading shape for ${w}`);
        }
        const miss = Lexicon.lookup('xyznotaword');
        assert(miss && Array.isArray(miss.readings) && miss.readings.length === 0, `${lang} miss must return readings: []`);
    }

    console.log('[PASS] Lexicon & morphology contracts verified for fr, it, pl, cs, sk.');
})();
