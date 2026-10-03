// Hungarian Reader lookup must resolve words typed without accents
// ("kerdes" -> "kérdés"), as pasted texts and casual writing often are.
//   node tests/reader/test-hu-accentless-lookup.js
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

const root = path.resolve(__dirname, '..', '..');
process.chdir(root);
global.window = global;
const store = {};
global.localStorage = {
    getItem: k => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: k => { delete store[k]; }
};
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

const top = w => {
    const r = Lexicon.lookup(w).readings[0];
    return r && !r.compoundParts ? r.lemma : null;
};

(async () => {
    Lang.set('hu');
    await Lexicon.load();
    const cases = [
        // bare headwords
        ['kerdes', 'kérdés'], ['koszonom', 'köszönöm'], ['szep', 'szép'], ['kenyer', 'kenyér'],
        // inflected nouns
        ['hazban', 'ház'], ['kenyeret', 'kenyér'], ['varosban', 'város'],
        // verb forms
        ['kerdezte', 'kérdez'], ['tudom', 'tud'], ['irok', 'ír'],
        ['csinaltam', 'csinál'], ['olvastuk', 'olvas'],
        // irregular verbs, reached once the wrong-harmony readings are gone
        // (ROADMAP 123/124)
        ['mentunk', 'megy'], ['elmentunk', 'elmegy'],
        // an accented word that already resolves must not change
        ['kérdés', 'kérdés'], ['nagyon', 'nagyon'],
        // unaccented spelling that is itself a real word keeps its own reading
        ['kor', 'kor'],
        // a word typed with accents is never re-accented, and a stem+suffix
        // guess must be a verb form of that stem ("kés"+"ma" is not)
        ['kesma', null], ['kőr', 'kőr']
    ];
    let failed = 0;
    for (const [w, want] of cases) {
        const t0 = Date.now();
        const got = top(w);
        const ms = Date.now() - t0;
        const ok = got === want;
        if (!ok) failed++;
        console.log(`${ok ? 'ok  ' : 'FAIL'} ${w} -> ${got}${want && !ok ? ' (want ' + want + ')' : ''} [${ms}ms]`);
    }
    assert.strictEqual(failed, 0, failed + ' lookup(s) failed');
})().catch(e => { console.error(e.message); process.exit(1); });
