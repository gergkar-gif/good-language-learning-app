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
            normalizeCard(card);
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
// SCHEDULING (SM-2)
// ============================================
const SRS_CONFIG = {
    START_EASE: 2.5,
    MIN_EASE: 1.3,
    MAX_EASE: 3.0,
    // How each rating moves the card's ease factor.
    EASE_DELTA: { again: -0.20, hard: -0.15, good: 0, easy: 0.15 },
    AGAIN_MINUTES: 1,
    // Fixed ramp for the first two successful reviews; after that the
    // interval is driven by the ease factor.
    FIRST_INTERVAL: { hard: 1, good: 1, easy: 4 },
    SECOND_INTERVAL: { hard: 3, good: 6, easy: 8 },
    HARD_MULTIPLIER: 1.2,
    EASY_BONUS: 1.3,
    MAX_INTERVAL: 365
};

const DAY_MS = 24 * 60 * 60 * 1000;

function newCardSchedule() {
    return {
        reviews: 0,
        ease: SRS_CONFIG.START_EASE,
        interval: 0,
        lastReviewed: null,
        nextReview: new Date().toISOString()
    };
}

function clampEase(ease) {
    return Math.min(SRS_CONFIG.MAX_EASE, Math.max(SRS_CONFIG.MIN_EASE, ease));
}

function daysBetween(from, to) {
    return (new Date(to) - new Date(from)) / DAY_MS;
}

// Cards saved before SM-2 have no `ease` or `interval`. Rebuild both from
// what the card does have so its review history isn't thrown away.
function normalizeCard(card) {
    if (typeof card.reviews !== 'number' || !(card.reviews >= 0)) card.reviews = 0;

    card.ease = (typeof card.ease === 'number' && isFinite(card.ease))
        ? clampEase(card.ease)
        : SRS_CONFIG.START_EASE;

    if (typeof card.interval !== 'number' || !isFinite(card.interval) || card.interval < 0) {
        card.interval = inferInterval(card);
    }
    return card;
}

// The old scheduler wrote a fixed gap between lastReviewed and nextReview.
// That gap is the closest thing a legacy card has to an interval.
function inferInterval(card) {
    if (!card.reviews) return 0;
    if (card.lastReviewed && card.nextReview) {
        const days = Math.round(daysBetween(card.lastReviewed, card.nextReview));
        if (days >= 1) return Math.min(SRS_CONFIG.MAX_INTERVAL, days);
    }
    return 1;
}

// What a rating would do to a card, without touching it. Used both to apply
// the rating and to label the rating buttons.
function previewSchedule(card, rating, now) {
    now = now || new Date();
    const reviews = (typeof card.reviews === 'number' && card.reviews >= 0) ? card.reviews : 0;
    const currentInterval = (typeof card.interval === 'number' && isFinite(card.interval) && card.interval >= 0)
        ? card.interval
        : inferInterval(card);
    const currentEase = (typeof card.ease === 'number' && isFinite(card.ease))
        ? card.ease
        : SRS_CONFIG.START_EASE;

    const ease = clampEase(currentEase + (SRS_CONFIG.EASE_DELTA[rating] || 0));

    if (rating === 'again') {
        return { ease: ease, interval: 0, dueInMinutes: SRS_CONFIG.AGAIN_MINUTES, reviews: 0 };
    }

    let interval;
    if (reviews === 0) {
        interval = SRS_CONFIG.FIRST_INTERVAL[rating];
    } else if (reviews === 1) {
        interval = SRS_CONFIG.SECOND_INTERVAL[rating];
    } else {
        // Growth is driven by how long the card actually survived, so a card
        // reviewed early earns a smaller step than one left until it is due.
        // The floor stops an early rating from ever shortening the schedule.
        const elapsed = card.lastReviewed ? daysBetween(card.lastReviewed, now) : currentInterval;
        const base = Math.max(0, Math.min(currentInterval, elapsed));
        const multiplier = rating === 'hard' ? SRS_CONFIG.HARD_MULTIPLIER
                         : rating === 'easy' ? ease * SRS_CONFIG.EASY_BONUS
                         : ease;
        interval = Math.max(currentInterval, base * multiplier);
    }

    // Round up: at a short interval "hard" (1.2x) would otherwise round back
    // down to where it started and the card could never work its way out.
    interval = Math.min(SRS_CONFIG.MAX_INTERVAL, Math.max(1, Math.ceil(interval)));

    return { ease: ease, interval: interval, dueInMinutes: interval * 24 * 60, reviews: reviews + 1 };
}

function scheduleCard(card, rating, now) {
    now = now || new Date();
    normalizeCard(card);

    const next = previewSchedule(card, rating, now);

    card.ease = next.ease;
    card.interval = next.interval;
    card.reviews = next.reviews;
    card.lastReviewed = now.toISOString();
    card.nextReview = new Date(now.getTime() + next.dueInMinutes * 60 * 1000).toISOString();

    return card;
}

function formatInterval(minutes) {
    if (minutes < 60) return Math.round(minutes) + 'm';
    if (minutes < 60 * 24) return Math.round(minutes / 60) + 'h';

    // Stay in days a good while: at the point where intervals get long, "50d"
    // and "65d" both collapsing to "2mo" would make Good and Easy look alike.
    const days = minutes / (60 * 24);
    if (days < 90) return Math.round(days) + 'd';
    if (days < 365) return trimZero((days / 30.4).toFixed(1)) + 'mo';
    return trimZero((days / 365).toFixed(1)) + 'y';
}

function trimZero(value) {
    return String(value).replace(/\.0$/, '');
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
    
    srsDeck.push(Object.assign({
        spanish: cleanWord,
        english: data.en,
        type: data.type,
        added: new Date().toISOString()
    }, newCardSchedule()));
    
    recordNewWord();
    
    const btn = document.getElementById('popup-add-btn');
    btn.textContent = '✓ Added!';
    btn.style.background = 'var(--primary)';
    
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

// Fisher-Yates on a copy — the deck itself keeps its order.
function shuffled(cards) {
    const out = cards.slice();
    for (let i = out.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [out[i], out[j]] = [out[j], out[i]];
    }
    return out;
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

    // Random pick, so the deck isn't drilled in the same order every session
    // (which trains recall by position rather than by meaning).
    currentReviewCard = shuffled(dueCards)[0];
    normalizeCard(currentReviewCard);

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

    updateRatingLabels();
    updateReviewStats();
}

// The intervals are per-card now, so the buttons can't carry fixed labels.
function updateRatingLabels() {
    if (!currentReviewCard) return;
    const now = new Date();

    ['again', 'hard', 'good', 'easy'].forEach(rating => {
        const label = document.querySelector('.review-rate-' + rating + ' .review-rate-time');
        if (!label) return;
        label.textContent = formatInterval(previewSchedule(currentReviewCard, rating, now).dueInMinutes);
    });
}

function showAnswer() {
    document.getElementById('review-answer').style.display = 'block';
    document.getElementById('show-answer-btn').style.display = 'none';
    document.getElementById('rating-buttons').style.display = 'flex';
}

function rateCard(rating) {
    if (!currentReviewCard) return;

    const now = new Date();

    // Runs before scheduleCard, which is what makes "is this card new?"
    // answerable — rescheduling increments the review count.
    recordReview(currentReviewCard, rating);

    scheduleCard(currentReviewCard, rating, now);

    saveDeck();
    updateReaderWordColors();
    showNextCard();
}