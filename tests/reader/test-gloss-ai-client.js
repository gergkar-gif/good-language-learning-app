// Unit Test: GlossAI client (engine/gloss-ai.js)
// Verifies the quiet-failure contract: answers are remembered per browser,
// every failure resolves to null, and the feature can be switched off.

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log('--- Testing GlossAI client ---');

const store = {};
global.window = global;
global.localStorage = {
    getItem: k => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: k => { delete store[k]; }
};
let calls = [];
let reply = () => ({ ok: true, json: async () => ({ found: true, lemma: 'elnyom', pos: 'verb', gloss: 'to oppress' }) });
global.fetch = async (url, init) => { calls.push({ url, init }); return reply(); };

vm.runInThisContext(fs.readFileSync(path.join(__dirname, '../../engine/gloss-ai.js'), 'utf8'));

(async () => {
    console.log('1. language mapping');
    assert.strictEqual(GlossAI._workerLang('hu'), 'hu');
    assert.strictEqual(GlossAI._workerLang('es-latam'), 'es');
    assert.strictEqual(GlossAI._workerLang('es-es'), 'es');

    console.log('2. a lookup posts word, sentence and language, and the answer is remembered');
    let a = await GlossAI.lookup('Elnyomta', 'A hatalom elnyomta a népet.', 'hu');
    assert.deepStrictEqual(a, { found: true, lemma: 'elnyom', pos: 'verb', gloss: 'to oppress' });
    assert.strictEqual(calls.length, 1);
    const sent = JSON.parse(calls[0].init.body);
    assert.deepStrictEqual([sent.word, sent.lang], ['elnyomta', 'hu']);
    assert.strictEqual(sent.sentence, 'A hatalom elnyomta a népet.');
    await GlossAI.lookup('elnyomta', 'x', 'hu');
    assert.strictEqual(calls.length, 1, 'the second tap is answered from memory');
    assert(store['glossAi:hu:elnyomta'], 'and persisted for the next visit');

    console.log('3. a stored answer is used with no network (fresh page load)');
    calls = [];
    store['glossAi:es:caatinga'] = JSON.stringify({ found: true, lemma: 'caatinga', pos: 'noun', gloss: 'scrubland', at: Date.now() });
    a = await GlossAI.lookup('caatinga', '', 'es-latam');
    assert.strictEqual(a.gloss, 'scrubland');
    assert.strictEqual(calls.length, 0);

    console.log('4. an old "no answer" is retried, a recent one is not');
    store['glossAi:hu:ujszo'] = JSON.stringify({ found: false, at: Date.now() - 8 * 86400000 });
    await GlossAI.lookup('ujszo', '', 'hu');
    assert.strictEqual(calls.length, 1);
    calls = [];
    store['glossAi:hu:friss'] = JSON.stringify({ found: false, at: Date.now() });
    a = await GlossAI.lookup('friss', '', 'hu');
    assert.deepStrictEqual([a.found, calls.length], [false, 0]);

    console.log('5. failures resolve to null and are not remembered');
    calls = [];
    reply = () => { throw new Error('network down'); };
    assert.strictEqual(await GlossAI.lookup('hiba', '', 'hu'), null);
    reply = () => ({ ok: false, json: async () => ({}) });
    assert.strictEqual(await GlossAI.lookup('hiba', '', 'hu'), null);
    assert(!store['glossAi:hu:hiba']);

    console.log('6. a daily-cap refusal is shown as "no suggestion" but not remembered as a real "no answer"');
    reply = () => ({ ok: true, json: async () => ({ found: false, code: 'DAILY_CAP' }) });
    a = await GlossAI.lookup('sokadik', '', 'hu');
    assert.strictEqual(a.found, false);
    assert(!store['glossAi:hu:sokadik'], 'retry later, once the cap resets');

    console.log('7. the feature can be switched off');
    store.parlour_gloss_endpoint = 'none';
    calls = [];
    assert.strictEqual(GlossAI.available(), false);
    assert.strictEqual(await GlossAI.lookup('barmi', '', 'hu'), null);
    assert.strictEqual(calls.length, 0);

    console.log('\nALL GLOSS CLIENT TESTS PASSED');
})().catch(err => { console.error('FAILED:', err); process.exit(1); });
