// A Hungarian ending must agree with its stem's vowel harmony:
// "mentunk" is neither "menik" + back "-tunk" (ROADMAP 123) nor
// "ment" + back "-unk" (ROADMAP 124).
//   node tests/reader/test-hu-verb-harmony.js
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

const root = path.resolve(__dirname, '..', '..');
global.window = global;
vm.runInThisContext(fs.readFileSync(path.join(root, 'engine/morphology/hungarian.js'), 'utf8'));
const read = rel => JSON.parse(fs.readFileSync(path.join(root, rel), 'utf8'));
const dictionary = read('imports/dictionary/hungarian-en.json');
const wordIndex = read('content/hu/indexes/word-index.json');

const lemmas = (word, pos) => HungarianMorphology.analyze(word, dictionary, wordIndex)
    .filter(r => pos === 'verb' ? r.pos === 'verb' : r.pos !== 'verb').map(r => r.lemma);
const verbLemmas = word => HungarianMorphology.analyze(word, dictionary, wordIndex)
    .filter(r => r.pos === 'verb').map(r => r.lemma);

const cases = [
    // wrong harmony: no verb reading
    ['mentunk', []], ['kértunk', []], ['olvastünk', []],
    // right harmony still resolves
    ['mentünk', ['megy', 'menik']], ['kértünk', ['kér']], ['olvastunk', ['olvas']],
    // compounds and í-stems are left alone: their harmony isn't in the vowels
    ['hazatértünk', ['hazatér']], ['megírtunk', ['megír']], ['bénította', ['bénít']],
    // endings shared by both harmonies
    ['gondolnék', ['gondol']], ['aggódjék', ['aggódik']]
];
let failed = 0;
for (const [word, want] of cases) {
    const got = verbLemmas(word);
    const ok = want.length ? want.every(l => got.includes(l)) : got.length === 0;
    if (!ok) failed++;
    console.log(`${ok ? 'ok  ' : 'FAIL'} ${word} -> ${JSON.stringify(got)}`);
}
// Noun/adjective endings (ROADMAP 124): "mentunk" is not "ment" + "-unk".
for (const [word, want] of [
    ['mentunk', []], ['kertunkben', []], ['hazekban', []],
    ['kertünkben', ['kert']], ['házakban', ['ház']], ['tisztje', ['tiszt']],
    // stems whose harmony the vowels don't show: é/i/í stems, loans
    ['célunk', ['cél']], ['hidak', ['híd']], ['hotelban', ['hotel']],
    // endings that never vary
    ['családé', ['család']], ['kertért', ['kert']], ['házig', ['ház']]
]) {
    const got = lemmas(word, 'nominal');
    const ok = want.length ? want.every(l => got.includes(l)) : got.length === 0;
    if (!ok) failed++;
    console.log(`${ok ? 'ok  ' : 'FAIL'} ${word} -> ${JSON.stringify(got)}`);
}
assert.strictEqual(failed, 0, failed + ' case(s) failed');
