// ========================================
// DECKS REVIEW ISOLATION TEST SUITE
// ========================================
const assert = require('assert');

global.window = global;
global.document = {
    addEventListener: () => {},
    querySelector: () => null,
    querySelectorAll: () => [],
    getElementById: (id) => ({
        style: {},
        classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
        querySelectorAll: () => [],
        querySelector: () => null,
        setAttribute: () => {},
        getAttribute: () => null,
        addEventListener: () => {}
    })
};

global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`,
    content: (p) => p
};

global.Lexicon = {
    isLoaded: () => true,
    load: async () => {},
    define: (word) => {
        const dict = {
            perro: { en: 'dog', type: 'noun' },
            gato: { en: 'cat', type: 'noun' },
            casa: { en: 'house', type: 'noun' }
        };
        return dict[word.toLowerCase()] || null;
    },
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
const Decks = require('../../engine/decks.js');

(async function runTests() {
    console.log('--- Test 1: Reviewing a deck does not auto-dump words into srsDeck ---');
    const mockDeck = {
        id: 'test-deck-1',
        name: 'Animals Deck',
        words: [
            { lemma: 'perro', translation: 'dog', pos: 'noun' },
            { lemma: 'gato', translation: 'cat', pos: 'noun' }
        ]
    };

    assert.strictEqual(srsDeck.length, 0, 'srsDeck should start empty');
    
    // Start review session with the deck's words
    SRS.startReviewSession(mockDeck.words.map(w => w.lemma), mockDeck.name, { words: mockDeck.words });
    
    assert.strictEqual(srsDeck.length, 0, 'srsDeck should still be empty after starting review');
    const card1 = SRS.getCurrentReviewCard();
    assert.strictEqual(card1 !== null, true, 'currentReviewCard should be active');
    assert.strictEqual(card1.isEphemeral, true, 'Candidate card should be ephemeral');
    console.log('[PASS] startReviewSession initializes ephemeral deck cards without mutating srsDeck.');

    console.log('\n--- Test 2: Rating an ephemeral card does not insert it into srsDeck ---');
    const firstWord = card1.spanish;
    SRS.rateCard('good');
    assert.strictEqual(srsDeck.length, 0, 'Rating an ephemeral card must not add it to srsDeck');
    const card2 = SRS.getCurrentReviewCard();
    assert.strictEqual(card2.spanish !== firstWord, true, 'Next card should be presented');
    console.log('[PASS] Ephemeral card rating progresses session without srsDeck insertion.');

    console.log('\n--- Test 3: Existing srsDeck card in a deck session is preserved and updated ---');
    const existingCards = [{
        spanish: 'casa',
        english: 'house',
        type: 'noun',
        source: 'lesson',
        reviews: 1,
        ease: 2.5,
        interval: 1
    }];
    SRS.setDeck(existingCards);
    global.srsDeck = existingCards;

    const mockDeck2 = {
        id: 'test-deck-2',
        name: 'House Deck',
        words: [
            { lemma: 'casa', translation: 'house', pos: 'noun' }
        ]
    };

    SRS.startReviewSession(mockDeck2.words.map(w => w.lemma), mockDeck2.name, { words: mockDeck2.words });
    const cardCasa = SRS.getCurrentReviewCard();
    assert.strictEqual(cardCasa.spanish, 'casa');
    assert.strictEqual(Boolean(cardCasa._original), true, 'Should link to original srsDeck card');
    SRS.rateCard('good');
    assert.strictEqual(SRS.getDeck()[0].reviews, 2, 'Existing srsDeck card reviews count should be incremented');
    console.log('[PASS] Existing srsDeck card updated properly.');

    console.log('\n--- Test 4: statusOf calculation ---');
    const status = Decks.statusOf(mockDeck);
    assert.strictEqual(status.total, 2);
    assert.strictEqual(status.inDeck, 0, '0 in user deck because neither perro nor gato is in srsDeck');
    assert.strictEqual(status.due, 0, '0 due in user deck');
    assert.strictEqual(status.ready, 2, '2 ready to practice in this deck');
    console.log('[PASS] statusOf correctly reflects deck standing.');

    console.log('\n[ALL PASS] Deck review isolation tests passed successfully.');
})();
