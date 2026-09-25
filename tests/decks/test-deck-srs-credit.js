// ========================================
// DECK STUDY MODES -> SRS CREDIT TEST SUITE
// ========================================
// creditPractice() (engine/srs.js): what Learn/Match/Blast outcomes do to
// a word's SRS card.
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const store = {};
const ctx = {
    console,
    Date, Math, JSON, Map, Set,
    localStorage: {
        getItem: k => (k in store ? store[k] : null),
        setItem: (k, v) => { store[k] = String(v); },
        removeItem: k => { delete store[k]; }
    },
    Lang: { key: k => 'es_' + k, name: () => 'Spanish' },
    document: { getElementById: () => null, querySelectorAll: () => [], addEventListener: () => {} },
    window: { addEventListener: () => {}, dispatchEvent: () => {} },
    CustomEvent: function () {}
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, '../../engine/srs.js'), 'utf8'), ctx);

const DAY = 24 * 60 * 60 * 1000;
const now = new Date('2026-09-25T12:00:00Z');

function card(spanish, overrides) {
    return Object.assign({
        spanish, english: spanish, reviews: 3, ease: 2.5, interval: 10, lapses: 0,
        lastReviewed: new Date(now - 10 * DAY).toISOString(),
        nextReview: new Date(now - 1000).toISOString() // due
    }, overrides || {});
}

function reset(cards) {
    vm.runInContext('srsDeck = ' + JSON.stringify(cards) + '; knownWords = [];', ctx);
}
function get(lemma) {
    return vm.runInContext('srsDeck', ctx).find(c => c.spanish === lemma);
}
function credit(results) {
    ctx.__r = results; ctx.__now = now;
    vm.runInContext('creditPractice(__r, __now)', ctx);
}

// 1. 'again' applies even when the card isn't due.
reset([card('perro', { nextReview: new Date(now.getTime() + 5 * DAY).toISOString() })]);
credit([{ lemma: 'perro', rating: 'again' }]);
assert.strictEqual(get('perro').interval, 0, 'again resets the interval');
assert.strictEqual(get('perro').lapses, 1, 'again counts a lapse');
assert.strictEqual(get('perro').reviews, 0);
console.log('✓ a miss is AGAIN even on a card that is not due');

// 2. 'weak' on a due card grows at the hard pace, ease untouched.
reset([card('gato')]);
credit([{ lemma: 'gato', rating: 'weak' }]);
assert.strictEqual(get('gato').ease, 2.5, 'weak leaves ease alone');
assert.ok(get('gato').interval >= 11 && get('gato').interval <= 14, 'weak grows ~1.2x, got ' + get('gato').interval);
console.log('✓ a correct game hit is a weak good: ~1.2x interval, no ease change');

// 3. 'weak' and 'good' do nothing to a card that isn't due.
const future = new Date(now.getTime() + 5 * DAY).toISOString();
reset([card('casa', { nextReview: future }), card('mesa', { nextReview: future })]);
credit([{ lemma: 'casa', rating: 'weak' }, { lemma: 'mesa', rating: 'good' }]);
assert.strictEqual(get('casa').nextReview, future);
assert.strictEqual(get('mesa').nextReview, future);
console.log('✓ correct answers on not-yet-due cards are ignored');

// 4. 'good' on a due card is a full good (ease-driven growth).
reset([card('libro')]);
credit([{ lemma: 'libro', rating: 'good' }]);
assert.ok(get('libro').interval >= 21, 'good grows ~2.5x, got ' + get('libro').interval);
console.log('✓ Learn stage 4 counts as a full good');

// 4b. 'hard' on a due card: 1.2x growth with the ease cut; ignored if not due.
reset([card('mano'), card('pie', { nextReview: future })]);
credit([{ lemma: 'mano', rating: 'hard' }, { lemma: 'pie', rating: 'hard' }]);
assert.strictEqual(get('mano').ease, 2.35, 'hard cuts ease');
assert.ok(get('mano').interval >= 11 && get('mano').interval <= 14, 'hard grows ~1.2x, got ' + get('mano').interval);
assert.strictEqual(get('pie').nextReview, future);
console.log('✓ Learn stage 4 wrong counts as hard (due cards only)');

// 5. Words with no card are not enrolled.
reset([]);
credit([{ lemma: 'nuevo', rating: 'again' }, { lemma: 'otro', rating: 'weak' }]);
assert.strictEqual(vm.runInContext('srsDeck.length', ctx), 0);
console.log('✓ words without a card are left alone');

// 6. Who opts Match/Blast into SRS credit, and how much.
const src = f => fs.readFileSync(path.join(__dirname, '../../engine', f), 'utf8');
assert.strictEqual((src('decks.js').match(/srsCredit: true/g) || []).length, 2, 'Decks opts Match and Blast in');
assert.ok(src('studyPlanRunner.js').includes('srsCredit: true'), 'study plan Match credits fully');
assert.ok(src('recommendationEngine.js').includes('srsCredit: true'), 'weakest-words Match credits fully');
assert.ok(src('lessons.js').includes("srsCredit: 'misses'"), 'lesson Quick Reinforce credits misses only');
const matchJs = src('decks/match.js');
assert.ok(/_wrongUids\.forEach\(uid => results\.push\(\{ lemma: _wordsByUid\[uid\]\.lemma, rating: 'again' \}\)\)/.test(matchJs),
    'Match credits wrong pairs, not words left over at time-out');
console.log('✓ Match credit: full in Decks/study plan/recommendations, misses-only after a lesson');

console.log('\nAll deck SRS credit tests passed!');
