// ========================================
// LEARNER SIGNALS TEST SUITE
// ========================================
// Grammar Driller -> recycle schedule -> LearnerModel skill state;
// Reader lookups -> SRS 'again' + LearnerModel.weakWords();
// Vocabulary Driller -> SRS (source check).
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const store = {};
let appOpen = 10;
const files = {
    'indexes/grammar-index.json': { bySkill: { 'ser-estar': [{ id: 'ex-1', ref: 'x' }, { id: 'ex-2', ref: 'x' }] } },
    'drills/grammar/a1-bank.json': { items: [
        { id: 'B-1', module: 'ser_estar' },
        { id: 'B-2', module: 'ser_estar' },
        { id: 'B-3', module: 'articles' }
    ] }
};
const ctx = {
    console, Date, Math, JSON, Map, Set, Promise, Object, Array,
    localStorage: {
        getItem: k => (k in store ? store[k] : null),
        setItem: (k, v) => { store[k] = String(v); },
        removeItem: k => { delete store[k]; }
    },
    Lang: { key: k => 'es_' + k, name: () => 'Spanish', code: () => 'es', content: p => p },
    Content: { json: async p => { if (!files[p]) throw new Error('404'); return files[p]; } },
    AppOpens: { current: () => appOpen },
    document: { getElementById: () => null, querySelectorAll: () => [], addEventListener: () => {} },
    CustomEvent: function () {}
};
ctx.window = ctx;
ctx.window.addEventListener = () => {};
ctx.window.dispatchEvent = () => {};
vm.createContext(ctx);
for (const f of ['srs.js', 'recycle.js', 'learnerModel.js']) {
    vm.runInContext(fs.readFileSync(path.join(__dirname, '../../engine', f), 'utf8'), ctx);
}
const run = code => vm.runInContext(code, ctx);
const schedule = () => JSON.parse(store['es_recycleSchedule'] || '{}');

(async () => {
    // ---- 1. Grammar Driller -> recycle -> skill state ----
    ctx.__r = [{ id: 'ex-1', rating: 'again' }, { id: 'bank:B-1', rating: 'again' }, { id: 'bank:B-2', rating: 'good' }];
    run('Recycle.credit(__r)');
    assert.strictEqual(schedule()['ex-1'].lapses, 1, 'a miss on a lesson exercise is recorded');
    assert.strictEqual(schedule()['bank:B-2'].reviews, 1, 'a correct bank item on a new card is recorded');

    // not due any more -> a correct answer in the same sitting is ignored, a miss is not
    const dueBefore = schedule()['bank:B-2'].dueAtOpen;
    ctx.__r = [{ id: 'bank:B-2', rating: 'good' }];
    run('Recycle.credit(__r)');
    assert.strictEqual(schedule()['bank:B-2'].dueAtOpen, dueBefore, 'correct on a not-due item is ignored');
    ctx.__r = [{ id: 'bank:B-2', rating: 'again' }];
    run('Recycle.credit(__r)');
    assert.strictEqual(schedule()['bank:B-2'].lapses, 1, 'a miss always counts');
    console.log('✓ Recycle.credit: misses always, correct answers only when due');

    const state = await run('LearnerModel.skillState("ser-estar")');
    assert.strictEqual(state.recycle && state.recycle.seen, 3, 'skill joins lesson exercise ex-1 and bank items B-1/B-2, misses included');
    assert.strictEqual(state.state, 'developing', 'misses at ease 2.3 -> developing, got ' + state.state);
    console.log('✓ bank items are joined to their skill by module (ser_estar -> ser-estar)');

    // push the skill into weak: repeated misses across opens
    for (let i = 0; i < 3; i++) {
        appOpen++;
        ctx.__r = [{ id: 'ex-1', rating: 'again' }, { id: 'bank:B-1', rating: 'again' }];
        run('Recycle.credit(__r)');
    }
    const weak = await run('LearnerModel.weakSkills()');
    assert.ok(weak.some(s => s.skillId === 'ser-estar' && s.state === 'weak'), 'drilled misses make the skill weak: ' + JSON.stringify(weak));
    console.log('✓ Grammar Driller misses show up in LearnerModel.weakSkills()');

    // ---- 2. Reader lookups ----
    const future = new Date(Date.now() + 5 * 864e5).toISOString();
    run(`srsDeck = [{ spanish: 'perro', english: 'dog', reviews: 3, ease: 2.5, interval: 10, lapses: 0, nextReview: '${future}' }]; knownWords = [{ spanish: 'casa' }];`);
    run('LearnerModel.recordLookup("perro", "dog", "noun")');
    assert.strictEqual(run('srsDeck[0].lapses'), 1, 'looking up a carded word is a missed review');
    run('LearnerModel.recordLookup("perro", "dog", "noun")');
    assert.strictEqual(run('srsDeck[0].lapses'), 1, 'only once per word per day');
    console.log('✓ looking up a word with a card counts as AGAIN, once a day');

    run('LearnerModel.recordLookup("casa", "house", "noun")');
    assert.ok(!JSON.parse(store['es_wordLookups']).casa, 'known words are not logged');
    console.log('✓ known words are ignored');

    // an uncarded word looked up on two separate days surfaces in weakWords
    run('LearnerModel.recordLookup("gato", "cat", "noun")');
    assert.strictEqual(run('LearnerModel.lookedUpWords().length'), 0, 'one day is not enough');
    const l = JSON.parse(store['es_wordLookups']);
    l.gato.days = ['2026-09-01'].concat(l.gato.days);
    store['es_wordLookups'] = JSON.stringify(l);
    const ww = run('LearnerModel.weakWords()');
    assert.strictEqual(ww.map(w => w.lemma).join(','), 'gato', 'gato surfaces; carded perro is below the SRS floor: ' + JSON.stringify(ww));
    assert.strictEqual(ww[0].translation, 'cat');
    console.log('✓ words looked up on 2+ days without a card surface in weakWords()');

    // ---- 3. Vocabulary Driller wiring (source) ----
    const vocab = fs.readFileSync(path.join(__dirname, '../../engine/drills/vocabulary.js'), 'utf8');
    assert.ok(/_finishSession\(\) \{[\s\S]{0,120}_creditSrs\(\)/.test(vocab), 'finish sends SRS outcomes');
    assert.ok(/_abortSession\(\) \{[\s\S]{0,120}_creditSrs\(\)/.test(vocab), 'leaving partway sends SRS outcomes');
    const grammar = fs.readFileSync(path.join(__dirname, '../../engine/drills/grammar.js'), 'utf8');
    assert.ok(/_finishSession\(\) \{[\s\S]{0,120}_creditRecycle\(\)/.test(grammar));
    assert.ok(/_abortSession\(\) \{[\s\S]{0,120}_creditRecycle\(\)/.test(grammar));
    console.log('✓ both drillers flush outcomes on finish and on leaving');

    console.log('\nAll learner signal tests passed!');
})().catch(e => { console.error(e); process.exit(1); });
