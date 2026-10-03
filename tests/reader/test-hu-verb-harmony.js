// A Hungarian verb ending must agree with its stem's vowel harmony
// (ROADMAP 123): "mentunk" is not "menik" + back "-tunk".
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
assert.strictEqual(failed, 0, failed + ' case(s) failed');
