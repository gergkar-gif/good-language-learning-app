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
    const saved = localStorage.getItem(Lang.key('srsDeck'));
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
    localStorage.setItem(Lang.key('srsDeck'), JSON.stringify(srsDeck));
    updateSRSCounter();
}

// ============================================
// KNOWN WORDS ("My Dictionary")
// ============================================
// A word here is retired from review entirely — distinct from a "mastered"
// SRS card (3+ successful reviews, engine/decks.js), which still comes back
// on its schedule. A word gets here three ways: the learner says so at the
// end of a lesson, they add it directly in My Dictionary, or a long-lived
// SRS card graduates on its own (see maybeGraduate() below). Known and
// reviewing are mutually exclusive on purpose — marking a word known always
// retires any active card for it, so the same word never sits in both.
let knownWords = [];

function loadKnownWords() {
    try {
        const saved = localStorage.getItem(Lang.key('knownWords'));
        knownWords = saved ? JSON.parse(saved) : [];
    } catch (error) {
        knownWords = [];
    }
}

function saveKnownWords() {
    localStorage.setItem(Lang.key('knownWords'), JSON.stringify(knownWords));
}

function isKnown(lemma) {
    return knownWords.some(w => w.spanish === lemma);
}

function addKnownWord(spanish, english, type, source) {
    if (!spanish || isKnown(spanish)) return false;
    srsDeck = srsDeck.filter(card => card.spanish !== spanish);
    knownWords.push({
        spanish: spanish,
        english: english || 'unknown',
        type: type || 'unknown',
        source: source || 'manual',
        added: new Date().toISOString()
    });
    saveDeck();
    saveKnownWords();
    return true;
}

// The undo, from My Dictionary: back into review as a fresh card rather than
// restoring whatever schedule it had before — a word retired long enough ago
// to need pulling back deserves to start over, not resume mid-interval.
function moveKnownToReview(spanish) {
    const word = knownWords.find(w => w.spanish === spanish);
    if (!word) return;
    knownWords = knownWords.filter(w => w.spanish !== spanish);
    srsDeck.push(Object.assign({
        spanish: word.spanish,
        english: word.english,
        type: word.type,
        source: word.source
    }, newCardSchedule()));
    saveKnownWords();
    saveDeck();
}

// A card that has held up for months across several successful reviews has
// earned its way out of the queue — SRS keeps testing what's still fragile,
// and by this point this word isn't. Checked right after every rating
// (rateCard(), below) rather than on a timer, so graduation only ever
// follows a review that just confirmed the word is solid.
const GRADUATION_MIN_REVIEWS = 5;
const GRADUATION_MIN_INTERVAL_DAYS = 180;

function maybeGraduate(card) {
    if (!card || card.reviews < GRADUATION_MIN_REVIEWS) return false;
    if (card.interval < GRADUATION_MIN_INTERVAL_DAYS) return false;
    if (isKnown(card.spanish)) return false;

    srsDeck = srsDeck.filter(c => c.spanish !== card.spanish);
    knownWords.push({
        spanish: card.spanish,
        english: card.english,
        type: card.type,
        source: card.source,
        added: new Date().toISOString(),
        graduated: true
    });
    saveKnownWords();
    return true;
}

function clearDeck() {
    // Clears this course's deck. XP is not scoped by language — it records
    // that the learner studied, not which course — so clearing it here wipes
    // it for every course, which is what the button has always done. Known
    // words are cleared alongside the deck they came from for the same
    // reason — leaving them behind would be half a reset.
    localStorage.removeItem(Lang.key('srsDeck'));
    localStorage.removeItem(Lang.key('knownWords'));
    localStorage.removeItem('spanishApp_xp');
    srsDeck = [];
    knownWords = [];
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
        // Tapped while reading, rather than taken from a lesson or a deck.
        source: 'reading',
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

// A review session can be scoped to one deck. The scope is a set of lemmas
// rather than a copy of the cards, so rating a card still writes to the one
// card the whole app shares — a deck is a way of choosing what to study, not
// a second place to keep a schedule.
let reviewScope = null;      // Set of lemmas, or null for everything
let reviewScopeName = '';

// What this one session actually did — reset per session by
// startReviewSession(), read once by renderReviewSessionSummary() when the
// queue empties. xpBefore/rankBefore are snapshots taken at the start so
// the summary can say what THIS session earned/crossed, not the running
// total — the same "before" pattern engine/lessons.js's finishLesson()
// already uses for its own rank-up line.
let reviewSessionStats = null;

// Which side of the card shows first: 'es-en' is recognition (see Spanish,
// recall the meaning), 'en-es' is production (see English, recall the
// word). A study-style preference like XP and the streak (see the header
// comment in engine/lang.js), not a property of one course, so it is a
// plain key rather than one scoped through Lang.key() — a learner who
// prefers production-first wants that whichever course they are reviewing.
const REVIEW_DIRECTION_KEY = 'app_reviewDirection';
let reviewDirection = 'es-en';
try {
    reviewDirection = localStorage.getItem(REVIEW_DIRECTION_KEY) === 'en-es' ? 'en-es' : 'es-en';
} catch (error) {
    // Private browsing with storage disabled: the default is fine.
}

// 'flip' is the original self-honesty flashcard (Show Answer). 'type' asks
// for the answer first — Check reveals whether it was right, then the same
// rating buttons as flip mode, so SM-2 scheduling is identical either way;
// only how the answer gets revealed changes. Same plain-key treatment as
// reviewDirection above (a study preference, not scoped to one course).
const REVIEW_MODE_KEY = 'app_reviewMode';
let reviewMode = 'flip';
try {
    reviewMode = localStorage.getItem(REVIEW_MODE_KEY) === 'type' ? 'type' : 'flip';
} catch (error) {
    // Private browsing with storage disabled: the default is fine.
}

function updateModeToggle() {
    const btn = document.getElementById('dk-mode-toggle');
    const flipLabel = document.getElementById('dk-mode-flip');
    const typeLabel = document.getElementById('dk-mode-type');
    const typeMode = reviewMode === 'type';

    if (btn) btn.setAttribute('aria-checked', String(typeMode));
    if (flipLabel) flipLabel.classList.toggle('dk-direction-active', !typeMode);
    if (typeLabel) typeLabel.classList.toggle('dk-direction-active', typeMode);
}

function toggleReviewMode() {
    reviewMode = reviewMode === 'flip' ? 'type' : 'flip';
    try {
        localStorage.setItem(REVIEW_MODE_KEY, reviewMode);
    } catch (error) {
        // Private browsing with storage disabled: the preference just won't
        // survive a reload.
    }
    updateModeToggle();
    // Same reasoning as toggleReviewDirection(): redraw the same card in the
    // new mode rather than skipping to a fresh one.
    if (currentReviewCard) renderCard();
}

function updateDirectionToggle() {
    const btn = document.getElementById('dk-direction-toggle');
    const esLabel = document.getElementById('dk-direction-es');
    const enLabel = document.getElementById('dk-direction-en');
    const englishFirst = reviewDirection === 'en-es';

    if (btn) {
        btn.setAttribute('aria-checked', String(englishFirst));
    }
    if (esLabel) {
        esLabel.textContent = (typeof Lang !== 'undefined') ? Lang.name() : 'Spanish';
        esLabel.classList.toggle('dk-direction-active', !englishFirst);
    }
    if (enLabel) enLabel.classList.toggle('dk-direction-active', englishFirst);
}

function toggleReviewDirection() {
    reviewDirection = reviewDirection === 'es-en' ? 'en-es' : 'es-en';
    try {
        localStorage.setItem(REVIEW_DIRECTION_KEY, reviewDirection);
    } catch (error) {
        // Private browsing with storage disabled: the preference just won't
        // survive a reload.
    }
    updateDirectionToggle();
    // Re-show the same card in the new direction rather than skipping to a
    // fresh one — flipping the switch mid-review shouldn't cost a card.
    if (currentReviewCard) renderCard();
}

function startReviewSession(lemmas, name) {
    reviewScope = lemmas ? new Set(lemmas) : null;
    reviewScopeName = reviewScope ? (name || 'Deck') : '';
    reviewSessionStats = {
        total: 0, again: 0, hard: 0, good: 0, easy: 0,
        startedAt: Date.now(),
        xpBefore: (typeof xpData !== 'undefined') ? xpData.total : 0,
        rankBefore: (typeof getRank === 'function') ? getRank().rank : null
    };

    const banner = document.getElementById('review-scope');
    if (banner) {
        banner.textContent = reviewScope ? 'Reviewing: ' + reviewScopeName : '';
        banner.style.display = reviewScope ? 'block' : 'none';
    }

    const root = document.getElementById('review-session');
    if (root) root.classList.remove('hidden');
    const browser = document.getElementById('decks-root');
    if (browser) browser.classList.add('hidden');

    showNextCard();
}

// The completion moment Decks review never had — Lessons and Workshop both
// end a session on a real summary; this one just closed back to the deck
// browser with nothing said about what was just done. Deliberately reuses
// the same building blocks engine/lessons.js's renderLessonSummary()
// established for the exact same moment elsewhere: accuracy from the
// rating breakdown ("again" is the only rating that means "didn't know
// it," so hard/good/easy all count as correct — the same idea SM-2 itself
// already treats them by), XP actually earned this session (before/after
// xpData.total, not derived from the rating counts, so it can't drift out
// of sync with whatever awardXP() actually does), a streak line, a
// rank-up line, and any Journey milestone this session happened to cross
// — the same functions, same wording, so a review session and a lesson
// announce the same kind of moment the same way.
function renderReviewSessionSummary() {
    const summaryEl = document.getElementById('review-summary');
    if (!summaryEl) return;

    const s = reviewSessionStats;
    const correct = s.hard + s.good + s.easy;
    const accuracy = Math.round((correct / s.total) * 100);
    const elapsed = (typeof formatLessonElapsed === 'function')
        ? formatLessonElapsed(Date.now() - s.startedAt) : null;
    const xpEarned = (typeof xpData !== 'undefined') ? Math.max(0, xpData.total - s.xpBefore) : 0;

    const rankAfter = (typeof getRank === 'function') ? getRank().rank : null;
    const rankedUp = s.rankBefore != null && rankAfter != null && rankAfter > s.rankBefore;
    const milestones = (typeof newlyReachedMilestones === 'function') ? newlyReachedMilestones() : [];

    const escFn = (typeof esc === 'function') ? esc : (v => String(v == null ? '' : v));

    const statsHtml = `
        <div class="review-summary-stats">
            <div class="review-summary-stat">
                <div class="jr-big">${s.total}</div>
                <div class="jr-of">${s.total === 1 ? 'card' : 'cards'}</div>
            </div>
            <div class="review-summary-stat">
                <div class="jr-big">${accuracy}%</div>
                <div class="jr-of">correct</div>
            </div>
            ${elapsed ? `
                <div class="review-summary-stat">
                    <div class="jr-big">${escFn(elapsed)}</div>
                    <div class="jr-of">time</div>
                </div>
            ` : ''}
            ${xpEarned ? `
                <div class="review-summary-stat">
                    <div class="jr-big">+${xpEarned}</div>
                    <div class="jr-of">XP</div>
                </div>
            ` : ''}
        </div>
    `;

    const streakText = (typeof getStreak === 'function')
        ? (getStreak() > 0 ? `${getStreak()}-day streak` : 'No streak yet')
        : '';

    summaryEl.innerHTML = `
        <p class="review-summary-eyebrow">Session complete</p>
        <h2 class="review-summary-title">Nice work.</h2>
        ${statsHtml}
        ${streakText ? `<p class="review-summary-streak">${escFn(streakText)}</p>` : ''}
        ${rankedUp ? `<p class="review-summary-milestone">Rank up! You're now Rank ${rankAfter}.</p>` : ''}
        ${milestones.map(m => `<p class="review-summary-milestone">Milestone: ${escFn(m.label)}</p>`).join('')}
        <button class="dk-secondary" onclick="endReviewSession()">Done</button>
    `;
    summaryEl.style.display = 'block';
}

function endReviewSession() {
    reviewScope = null;
    reviewScopeName = '';
    reviewSessionStats = null;
    const summaryEl = document.getElementById('review-summary');
    if (summaryEl) summaryEl.style.display = 'none';
    const root = document.getElementById('review-session');
    if (root) root.classList.add('hidden');
    const browser = document.getElementById('decks-root');
    if (browser) browser.classList.remove('hidden');
    if (typeof Decks !== 'undefined') Decks.render();
}

function inScope(card) {
    return !reviewScope || reviewScope.has(card.spanish);
}

function getDueCards() {
    const now = new Date();
    return srsDeck.filter(card => inScope(card) && new Date(card.nextReview) <= now);
}

function getNewCards() {
    return srsDeck.filter(card => inScope(card) && card.reviews === 0);
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
    const due = document.getElementById('due-count');
    const fresh = document.getElementById('new-count');
    const total = document.getElementById('total-count');
    if (due) due.textContent = getDueCards().length;
    if (fresh) fresh.textContent = getNewCards().length;
    if (total) {
        total.textContent = reviewScope
            ? srsDeck.filter(inScope).length
            : srsDeck.length;
    }
}

function showNextCard() {
    updateDirectionToggle();

    const dueCards = getDueCards();
    const cardEl = document.getElementById('review-card');
    const emptyEl = document.getElementById('review-empty');
    const summaryEl = document.getElementById('review-summary');

    if (dueCards.length === 0) {
        cardEl.style.display = 'none';
        currentReviewCard = null;

        // A session that actually reviewed something gets the real summary;
        // opening Review with nothing due to begin with (reviewSessionStats
        // never left zero) keeps the plain "All caught up!" panel, which is
        // already the correct message for that case.
        if (reviewSessionStats && reviewSessionStats.total > 0) {
            if (emptyEl) emptyEl.style.display = 'none';
            renderReviewSessionSummary();
        } else {
            if (summaryEl) summaryEl.style.display = 'none';
            emptyEl.style.display = 'block';
        }
        return;
    }

    cardEl.style.display = 'flex';
    emptyEl.style.display = 'none';
    if (summaryEl) summaryEl.style.display = 'none';

    // Random pick, so the deck isn't drilled in the same order every session
    // (which trains recall by position rather than by meaning).
    currentReviewCard = shuffled(dueCards)[0];
    normalizeCard(currentReviewCard);

    renderCard();
}

// What renderCard() is currently asking the learner to produce, in Type
// mode — the side of the card not shown. Set by renderCard(), read by
// checkTypedAnswer(); kept separate from currentReviewCard so a live
// dictionary lookup (translations can change/improve over time) doesn't
// have to be redone at check time.
let reviewExpectedSpanish = '';
let reviewExpectedEnglish = '';

// Draws currentReviewCard in whichever direction reviewDirection currently
// asks for. Split out from showNextCard() so toggling the direction
// mid-review can redraw the same card instead of skipping to a new one.
function renderCard() {
    if (!currentReviewCard) return;

    // Live dictionary lookup — fixes cards added before dictionary loaded.
    // Shortened either way: a review card tests recall, it isn't the place
    // for the Reader popup's full dictionary gloss (see Lexicon.shortGloss).
    const liveEntry = Lexicon.define(currentReviewCard.spanish);
    const displayEnglish = Lexicon.shortGloss(liveEntry ? liveEntry.en : (currentReviewCard.english || '—'));
    const displayType = liveEntry ? liveEntry.type : (currentReviewCard.type || '');

    // el/la in front of a noun the same way Decks' own word lists already
    // show it (Lexicon.withArticle) — silently a no-op for anything that
    // isn't a noun with a known simple gender.
    const spanishDisplay = Lexicon.withArticle(currentReviewCard.spanish);
    const englishFirst = reviewDirection === 'en-es';
    document.getElementById('review-front').textContent = englishFirst ? displayEnglish : spanishDisplay;
    document.getElementById('review-back').textContent = englishFirst ? spanishDisplay : displayEnglish;
    document.getElementById('review-context').textContent = displayType ? `(${displayType})` : '';
    reviewExpectedSpanish = currentReviewCard.spanish;
    reviewExpectedEnglish = displayEnglish;

    document.getElementById('review-answer').style.display = 'none';
    document.getElementById('rating-buttons').style.display = 'none';

    const typeMode = reviewMode === 'type';
    document.getElementById('show-answer-btn').style.display = typeMode ? 'none' : 'block';
    document.getElementById('review-type-input').classList.toggle('hidden', !typeMode);
    const field = document.getElementById('review-type-field');
    if (field) {
        field.value = '';
        field.classList.remove('correct', 'wrong');
        if (typeMode) field.focus();
    }

    updateRatingLabels();
    updateReviewStats();
    updateDirectionToggle();
    updateModeToggle();
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

// Shared by both modes once the answer is settled — flip mode reaches this
// straight from a tap, type mode reaches it after grading what was typed.
function revealAnswer() {
    document.getElementById('review-answer').style.display = 'block';
    document.getElementById('show-answer-btn').style.display = 'none';
    document.getElementById('review-type-input').classList.add('hidden');
    document.getElementById('rating-buttons').style.display = 'flex';
}

function showAnswer() {
    revealAnswer();
}

// Same normalisation lessons.js/GrammarRunner use elsewhere: case,
// whitespace and punctuation stripped, but accents checked directly
// (2026-08-27) - "dia" no longer matches "día", matching the standard the
// rest of the course now holds accents to for both languages.
function srsNormalise(text) {
    return String(text || '').toLowerCase().trim()
        .replace(/[.,!?¡¿;:]/g, '')
        .normalize('NFC');
}

// The English side is often a list of near-synonyms ("hello / hi", "to
// remove, to take away") rather than one fixed phrase — split on both
// separators and accept a match against any alternative.
function englishAlternatives(text) {
    return String(text || '').split(/[/,]/).map(srsNormalise).filter(Boolean);
}

function checkTypedAnswer() {
    if (!currentReviewCard) return;
    const field = document.getElementById('review-type-field');
    if (!field) return;

    const englishFirst = reviewDirection === 'en-es';
    const typed = srsNormalise(field.value);
    const ok = englishFirst
        ? typed === srsNormalise(reviewExpectedSpanish)
        : englishAlternatives(reviewExpectedEnglish).includes(typed);

    field.classList.toggle('correct', ok);
    field.classList.toggle('wrong', !ok);
    revealAnswer();
}

function rateCard(rating) {
    if (!currentReviewCard) return;

    const now = new Date();

    // Runs before scheduleCard, which is what makes "is this card new?"
    // answerable — rescheduling increments the review count.
    recordReview(currentReviewCard, rating);

    scheduleCard(currentReviewCard, rating, now);
    maybeGraduate(currentReviewCard);

    if (reviewSessionStats) {
        reviewSessionStats.total++;
        if (typeof reviewSessionStats[rating] === 'number') reviewSessionStats[rating]++;
    }

    saveDeck();
    updateReaderWordColors();
    showNextCard();
}