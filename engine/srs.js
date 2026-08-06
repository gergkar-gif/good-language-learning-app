// ============================================
// USER DATA & LOCAL STORAGE
// ============================================
let srsDeck = [];
// Set by showWord() — the resolved lemma and its dictionary entry, so
// addToSRS() saves the dictionary form rather than the tapped surface form.
let currentWord = null;
let currentWordTranslation = null;
let currentWordPos = null;

function loadDeck() {
    const saved = localStorage.getItem('spanishApp_srsDeck');
    if (saved) {
        srsDeck = JSON.parse(saved);
        // Enrich cards that were added before dictionary loaded
        for (const card of srsDeck) {
            if (card.english === 'unknown' || !card.english) {
                const entry = Lexicon.define(card.spanish);
                if (entry) {
                    card.english = entry.en;
                    card.type = entry.type;
                }
            }
        }
        updateSRSCounter();
    }
}

function saveDeck() {
    localStorage.setItem('spanishApp_srsDeck', JSON.stringify(srsDeck));
    updateSRSCounter();
}

function clearDeck() {
    localStorage.removeItem('spanishApp_srsDeck');
    localStorage.removeItem('spanishApp_xp');
    srsDeck = [];
    xpData = { total: 0, history: {}, dailyNewWords: {} };
    updateSRSCounter();
    updateXPHeader();
    alert('Deck & XP cleared!');
}

// ============================================
// ADD TO SRS
// ============================================
function addToSRS() {
    if (!currentWord) return;
    // currentWord is already the lemma resolved by showWord(), so an
    // inflected "días" tapped in a story is saved to the deck as "día".
    const cleanWord = currentWord;
    const data = {
        en: currentWordTranslation || 'unknown',
        type: currentWordPos || 'unknown'
    };

    if (srsDeck.find(w => w.spanish === cleanWord)) {
        closePopup();
        return;
    }
    
    if (!canAddNewWord()) {
        closePopup();
        return;
    }
    
    srsDeck.push({
        spanish: cleanWord,
        english: data.en,
        type: data.type,
        added: new Date().toISOString(),
        reviews: 0,
        lastReviewed: null,
        nextReview: new Date().toISOString()
    });
    
    recordNewWord();
    
    const btn = document.getElementById('popup-add-btn');
    btn.textContent = '✓ Added!';
    btn.style.background = '#8FB4BA';
    
    updateSRSCounter();
    saveDeck();
    updateReaderWordColors();
    setTimeout(closePopup, 600);
}

function updateSRSCounter() {
    const counter = document.getElementById('srs-counter');
    if (counter) counter.textContent = srsDeck.length;
}

// ============================================
// SRS REVIEW SYSTEM
// ============================================
let currentReviewCard = null;

function getDueCards() {
    const now = new Date();
    return srsDeck.filter(card => new Date(card.nextReview) <= now);
}

function getNewCards() {
    return srsDeck.filter(card => card.reviews === 0);
}

function updateReviewStats() {
    document.getElementById('due-count').textContent = getDueCards().length;
    document.getElementById('new-count').textContent = getNewCards().length;
    document.getElementById('total-count').textContent = srsDeck.length;
}

function showNextCard() {
    const dueCards = getDueCards();
    const cardEl = document.getElementById('review-card');
    const emptyEl = document.getElementById('review-empty');
    
    if (dueCards.length === 0) {
        cardEl.style.display = 'none';
        emptyEl.style.display = 'block';
        return;
    }
    
    cardEl.style.display = 'flex';
    emptyEl.style.display = 'none';
    
    currentReviewCard = dueCards[0];

    // Live dictionary lookup — fixes cards added before dictionary loaded
    const liveEntry = Lexicon.define(currentReviewCard.spanish);
    const displayEnglish = liveEntry ? liveEntry.en : (currentReviewCard.english || '—');
    const displayType = liveEntry ? liveEntry.type : (currentReviewCard.type || '');

    document.getElementById('review-front').textContent = currentReviewCard.spanish;
    document.getElementById('review-back').textContent = displayEnglish;
    document.getElementById('review-context').textContent = displayType ? `(${displayType})` : '';

    document.getElementById('review-answer').style.display = 'none';
    document.getElementById('show-answer-btn').style.display = 'block';
    document.getElementById('rating-buttons').style.display = 'none';
    
    updateReviewStats();
}

function showAnswer() {
    document.getElementById('review-answer').style.display = 'block';
    document.getElementById('show-answer-btn').style.display = 'none';
    document.getElementById('rating-buttons').style.display = 'flex';
}

function rateCard(rating) {
    if (!currentReviewCard) return;
    
    const now = new Date();
    const dueDate = new Date(currentReviewCard.nextReview);
    const isEarly = now < dueDate;
    
    const xpResult = calculateReviewXP(currentReviewCard, rating);
    if (xpResult.xp > 0) {
        awardXP(xpResult.xp, xpResult.reason);
    }
    
    if (isEarly && rating !== 'again') {
        showNextCard();
        return;
    }
    
    let intervalMinutes = 0;
    
    switch(rating) {
        case 'again':
            intervalMinutes = 1;
            currentReviewCard.reviews = 0;
            break;
        case 'hard':
            intervalMinutes = 60 * 24 * 2;
            currentReviewCard.reviews++;
            break;
        case 'good':
            intervalMinutes = 60 * 24 * 4;
            currentReviewCard.reviews++;
            break;
        case 'easy':
            intervalMinutes = 60 * 24 * 7;
            currentReviewCard.reviews++;
            break;
    }
    
    currentReviewCard.lastReviewed = now.toISOString();
    const nextReview = new Date(now.getTime() + intervalMinutes * 60 * 1000);
    currentReviewCard.nextReview = nextReview.toISOString();
    
    saveDeck();
    updateReaderWordColors();
    showNextCard();
}