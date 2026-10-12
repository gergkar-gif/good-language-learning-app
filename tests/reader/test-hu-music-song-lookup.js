const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

const root = path.resolve(__dirname, '..', '..');
process.chdir(root);
global.window = global;
global.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
global.document = { addEventListener() {}, dispatchEvent() {} };
global.CustomEvent = class CustomEvent {};
global.fetch = async url => {
    const p = path.resolve(root, String(url).replace(/^\.\//, '').replace(/\?.*$/, ''));
    if (!fs.existsSync(p)) return { ok: false, status: 404, json: async () => ({}) };
    return { ok: true, status: 200, json: async () => JSON.parse(fs.readFileSync(p, 'utf8')) };
};

const load = rel => vm.runInThisContext(fs.readFileSync(path.join(root, rel), 'utf8'), { filename: rel });
load('engine/lang.js');
load('engine/morphology/hungarian.js');
load('engine/lexicon.js');

(async () => {
    Lang.set('hu');
    await Lexicon.load();

    // 1. mondjátok must resolve to verb 'mond', never noun 'monda'
    const resMond = Lexicon.lookup('mondjátok');
    assert(resMond.readings.length > 0, 'mondjátok must have readings');
    assert.strictEqual(resMond.readings[0].lemma, 'mond', `Top reading for mondjátok should be 'mond', got '${resMond.readings[0].lemma}'`);
    assert.strictEqual(resMond.readings[0].pos, 'verb', `Top reading pos should be 'verb', got '${resMond.readings[0].pos}'`);
    assert(!resMond.readings.some(r => r.lemma === 'monda'), "mondjátok must not match noun 'monda'");
    console.log('ok   mondjátok -> lemma: mond (verb), no monda');

    // 2. nyáréjszakán must resolve to nyáréjszaka with superessive case and ladder
    const resNyar = Lexicon.lookup('nyáréjszakán');
    assert(resNyar.readings.length > 0, 'nyáréjszakán must resolve in dictionary');
    assert.strictEqual(resNyar.readings[0].lemma, 'nyáréjszaka', `Top reading for nyáréjszakán should be 'nyáréjszaka', got '${resNyar.readings[0].lemma}'`);
    assert(resNyar.readings[0].analysis.includes('superessive'), `Analysis should include superessive, got '${resNyar.readings[0].analysis}'`);
    assert(resNyar.ladder && resNyar.ladder.chain && resNyar.ladder.chain.length === 2, 'nyáréjszakán should have a 2-step morphology ladder');
    assert.strictEqual(resNyar.ladder.chain[0].form, 'nyáréjszaka');
    assert.strictEqual(resNyar.ladder.chain[1].form, 'nyáréjszakán');
    assert.strictEqual(resNyar.ladder.breakdown[0].suffix, 'n');
    console.log('ok   nyáréjszakán -> lemma: nyáréjszaka (noun, superessive) with ladder slice');

    console.log('All music song Hungarian lookup tests passed!');
})();
