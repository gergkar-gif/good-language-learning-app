// ========================================
// DECK SESSION SIZE & SMART PRIORITY TEST SUITE
// ========================================
const assert = require('assert');

global.window = global;
global.document = {
    addEventListener: () => {},
    querySelector: () => null,
    querySelectorAll: () => [],
    getElementById: () => ({
        style: {},
        dataset: {},
        classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
        querySelectorAll: () => [],
        querySelector: () => null,
        setAttribute: () => {},
        getAttribute: () => null,
        addEventListener: () => {}
    })
};

const store = {};
global.localStorage = {
    getItem(k) { return store[k] || null; },
    setItem(k, v) { store[k] = String(v); },
    removeItem(k) { delete store[k]; }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`,
    content: (p) => p,
    targetLemma: (c) => c.spanish
};

global.Lexicon = {
    isLoaded: () => true,
    load: async () => {},
    define: () => null,
    shortGloss: (en) => en ? en.split(/[,;]/)[0].trim() : '',
    withArticle: (w) => w
};
global.esc = (s) => s || '';
global.UI = {
    escape: (s) => s || '',
    toast: () => {}
};

global.srsDeck = [];
global.knownWords = [];
global.saveDeck = () => {};
global.saveKnownWords = () => {};
global.updateReaderWordColors = () => {};
global.updateSRSCounter = () => {};
global.awardXP = () => {};

const SRS = require('../../engine/srs.js');
global.startReviewSession = SRS.startReviewSession;
global.getCurrentReviewCard = SRS.getCurrentReviewCard;
global.rateCard = SRS.rateCard;
global.endReviewSession = SRS.endReviewSession;

const Decks = require('../../engine/decks.js');

(async function runTests() {
    console.log('--- Test 1: getStoredSessionLimit & setStoredSessionLimit ---');
    Decks.setStoredSessionLimit(15);
    assert.strictEqual(Decks.getStoredSessionLimit(), 15, 'Session limit should be stored as 15');

    Decks.setStoredSessionLimit(null);
    assert.strictEqual(Decks.getStoredSessionLimit(), null, 'Clearing session limit should return null');

    Decks.setStoredSessionLimit(0);
    assert.strictEqual(Decks.getStoredSessionLimit(), null, 'Zero limit should be treated as null (all)');
    console.log('[PASS] Storage helpers persist and clear session limit properly.');

    console.log('\n--- Test 2: prioritizeWords smart priority ordering ---');
    const now = Date.now();
    const DAY = 24 * 60 * 60 * 1000;

    // Set up cards in srsDeck
    global.srsDeck = [
        // Due card: due 2 days ago (most overdue)
        { spanish: 'perro', english: 'dog', reviews: 2, nextReview: new Date(now - 2 * DAY).toISOString() },
        // Due card: due 1 hour ago
        { spanish: 'gato', english: 'cat', reviews: 2, nextReview: new Date(now - 3600000).toISOString() },
        // Learning card: not due yet (due in 3 days, reviews: 1)
        { spanish: 'casa', english: 'house', reviews: 1, nextReview: new Date(now + 3 * DAY).toISOString() },
        // Mastered card: reviews >= 3, not due yet (due in 10 days)
        { spanish: 'agua', english: 'water', reviews: 4, nextReview: new Date(now + 10 * DAY).toISOString() },
        // Leech card: not due yet, but marked leech -> top urgency
        { spanish: 'libro', english: 'book', reviews: 1, leech: true, nextReview: new Date(now + 5 * DAY).toISOString() }
    ];

    // Known word
    global.knownWords = [{ spanish: 'sol', english: 'sun' }];
    global.isKnown = (lemma) => lemma === 'sol';

    const testWords = [
        { lemma: 'sol', translation: 'sun' },         // known -> priority 5
        { lemma: 'agua', translation: 'water' },      // mastered -> priority 4
        { lemma: 'nuevo', translation: 'new word' },   // new (not in srsDeck) -> priority 3
        { lemma: 'casa', translation: 'house' },      // learning -> priority 2
        { lemma: 'gato', translation: 'cat' },        // due -> priority 1
        { lemma: 'perro', translation: 'dog' },       // due (older) -> priority 1
        { lemma: 'libro', translation: 'book' }       // leech -> priority 1
    ];

    const sorted = Decks.prioritizeWords(testWords);
    const sortedLemmas = sorted.map(w => w.lemma);

    // perro is older due than gato, both are due
    // libro is leech
    assert.strictEqual(sortedLemmas.indexOf('perro') < sortedLemmas.indexOf('gato'), true, 'Older due card before newer due card');
    assert.strictEqual(sortedLemmas.indexOf('perro') < sortedLemmas.indexOf('casa'), true, 'Due card before learning card');
    assert.strictEqual(sortedLemmas.indexOf('libro') < sortedLemmas.indexOf('casa'), true, 'Leech card before learning card');
    assert.strictEqual(sortedLemmas.indexOf('casa') < sortedLemmas.indexOf('nuevo'), true, 'Learning card before new card');
    assert.strictEqual(sortedLemmas.indexOf('nuevo') < sortedLemmas.indexOf('agua'), true, 'New card before mastered card');
    assert.strictEqual(sortedLemmas.indexOf('agua') < sortedLemmas.indexOf('sol'), true, 'Mastered card before known card');
    console.log('[PASS] prioritizeWords sorts correctly: Due/Leech > Learning > New > Mastered > Known.');

    console.log('\n--- Test 3: selectSessionWords respects limit and deck bounds ---');
    const mockDeck = {
        id: 'test-priority-deck',
        name: 'Priority Test Deck',
        words: testWords
    };

    // Limit 3 should return top 3 prioritized words
    const top3 = Decks.selectSessionWords(mockDeck, 3);
    assert.strictEqual(top3.length, 3, 'Should return exactly 3 words');
    assert.strictEqual(top3.map(w => w.lemma).includes('perro'), true, 'Top 3 should include due word perro');

    // Limit null or >= total should return all words
    const allWords = Decks.selectSessionWords(mockDeck, null);
    assert.strictEqual(allWords.length, testWords.length, 'Null limit should return all words');

    const overLimit = Decks.selectSessionWords(mockDeck, 100);
    assert.strictEqual(overLimit.length, testWords.length, 'Over-limit should return all words without duplicates');
    console.log('[PASS] selectSessionWords correctly bounds and slices deck words.');

    console.log('\n--- Test 4: reviewDeck with limit bounds session size ---');
    await Decks.reviewDeck('mine', { limit: 2 });
    const currentCard = SRS.getCurrentReviewCard();
    assert.strictEqual(currentCard !== null, true, 'Review session should start');

    // Rate 2 cards
    SRS.rateCard('good');
    SRS.rateCard('good');

    // After 2 cards, limit of 2 is reached, review session should conclude
    const endedCard = SRS.getCurrentReviewCard();
    assert.strictEqual(endedCard, null, 'Review session should finish after reaching limit of 2');
    console.log('[PASS] reviewDeck with limit finishes after exact card count.');

    console.log('\n[ALL PASS] Deck session size tests passed successfully.');
})();
