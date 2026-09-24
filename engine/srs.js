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
        try {
            srsDeck = JSON.parse(saved);
        } catch (error) {
            console.warn('Corrupted srsDeck storage, resetting to empty:', error);
            srsDeck = [];
        }
        if (!Array.isArray(srsDeck)) srsDeck = [];
        // Enrich cards that were added before dictionary loaded
        for (const card of srsDeck) {
            if (card.english === 'unknown' || !card.english) {
                const entry = (typeof Lexicon !== 'undefined' && typeof Lexicon.define === 'function') ? Lexicon.define(card.spanish) : null;
                if (entry) {
                    card.english = entry.en;
                    card.type = entry.type;
                }
            }
            normalizeCard(card);
        }
        updateSRSCounter();
    } else {
        srsDeck = [];
        updateSRSCounter();
    }
}

function saveDeck() {
    localStorage.setItem(Lang.key('srsDeck'), JSON.stringify(srsDeck));
    updateSRSCounter();
    if (typeof Sync !== 'undefined' && Sync.scheduleAutoSave) {
        Sync.scheduleAutoSave();
    }
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
    if (typeof Sync !== 'undefined' && Sync.scheduleAutoSave) {
        Sync.scheduleAutoSave();
    }
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

// A learner who tests out of a level (placement or level test) never met its
// lessons, so none of their words reached the deck — and the Reader, "% familiar"
// and "Within reach" then treat every A1 word as unknown to someone placed into
// A2. Credit the words those lessons teach as known instead — read from each
// lesson's own vocabulary, the same list its "Add to Review" step offers, so
// the forms and translations match what finishing it would have stored
// (source 'level-test', so they can be told apart; My Dictionary can send any
// back to review). Words already in the deck or known are left alone.
async function creditTestedOutWords(lessonIds) {
    if (!(lessonIds && lessonIds.length) || typeof loadLesson !== 'function') return 0;
    const course = Lang.code();
    const vocab = await Promise.all(lessonIds.map(async id => {
        const lesson = await loadLesson(id).catch(() => null);
        return lesson ? collectLessonVocabulary(lesson).catch(() => []) : [];
    }));
    if (Lang.code() !== course) return 0; // course switched mid-fetch

    const inDeck = new Set(srsDeck.map(card => card.spanish));
    const added = new Date().toISOString();
    let count = 0;
    vocab.flat().forEach(word => {
        if (!word.lemma || inDeck.has(word.lemma) || isKnown(word.lemma)) return;
        knownWords.push({
            spanish: word.lemma,
            english: word.translation || 'unknown',
            type: word.pos || 'unknown',
            source: 'level-test',
            added
        });
        count++;
    });
    if (count) saveKnownWords();
    return count;
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
    const course = (typeof Lang !== 'undefined' && Lang.name) ? Lang.name() : 'course';
    if (!confirm(`Are you sure you want to reset your ${course} flashcards and known words? Your global XP and streak will be preserved.`)) {
        return;
    }
    localStorage.removeItem(Lang.key('srsDeck'));
    localStorage.removeItem(Lang.key('knownWords'));
    srsDeck = [];
    knownWords = [];
    sessionRelearningQueue = [];
    updateSRSCounter();
    updateReviewStats();
    if (typeof UI !== 'undefined' && UI.toast) {
        UI.toast('Flashcard deck reset.', 'info');
    }
    endReviewSession();
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
    MAX_INTERVAL: 365,
    // A card that has been rated "again" this many times total (not in a
    // row — SM-2 has no concept of "in a row" here) is flagged a leech: it
    // keeps failing regardless of how the schedule adjusts, which is a
    // different problem than "not due enough yet" and worth surfacing
    // rather than silently cycling forever. Same default Anki uses.
    LEECH_THRESHOLD: 8,
    // Spreads reviews that would otherwise land on the exact same future
    // date (e.g. a batch reviewed together today, all rated "good") across
    // a few days either side, so a backlog doesn't re-clump every time it
    // recurs. Only applied to the ease-driven growth phase (reviews >= 2)
    // — the fixed FIRST_INTERVAL/SECOND_INTERVAL ramp stays exact, and an
    // interval this short fuzzing to 0 (or flipping order with its
    // neighbour) isn't worth it anyway.
    FUZZ_MIN_INTERVAL_DAYS: 3,
    FUZZ_RANGE: 0.15
};

const DAY_MS = 24 * 60 * 60 * 1000;

// Deterministic 0..1 pseudo-random from a string (FNV-1a-ish hash) — used
// only for interval fuzz. Must be deterministic: the interval preview a
// learner sees on the rating buttons (updateRatingLabels(), a
// previewSchedule() call) and the interval actually saved when they click
// (rateCard() -> scheduleCard() -> another previewSchedule() call) need to
// agree, and they're two separate calls with no shared state to fuzz from
// other than the card/rating/interval themselves.
function fuzzSeed(str) {
    let h = 2166136261;
    for (let i = 0; i < str.length; i++) {
        h ^= str.charCodeAt(i);
        h = Math.imul(h, 16777619);
    }
    return ((h >>> 0) % 10000) / 10000;
}

function fuzzInterval(interval, card, rating) {
    if (interval < SRS_CONFIG.FUZZ_MIN_INTERVAL_DAYS) return interval;
    const seed = fuzzSeed(`${card.spanish || ''}|${rating}|${interval}`);
    const delta = interval * SRS_CONFIG.FUZZ_RANGE * (seed * 2 - 1);
    return Math.min(SRS_CONFIG.MAX_INTERVAL, Math.max(1, Math.round(interval + delta)));
}

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

    if (typeof card.lapses !== 'number' || !(card.lapses >= 0)) card.lapses = 0;
    card.leech = card.lapses >= SRS_CONFIG.LEECH_THRESHOLD;

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
    let fuzzable = false;
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
        fuzzable = true;
    }

    // Round up: at a short interval "hard" (1.2x) would otherwise round back
    // down to where it started and the card could never work its way out.
    interval = Math.min(SRS_CONFIG.MAX_INTERVAL, Math.max(1, Math.ceil(interval)));
    if (fuzzable) interval = fuzzInterval(interval, card, rating);

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

    if (rating === 'again') card.lapses = (card.lapses || 0) + 1;
    card.leech = (card.lapses || 0) >= SRS_CONFIG.LEECH_THRESHOLD;

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

    // Known and reviewing are mutually exclusive (see the file header
    // comment on knownWords above) — without this check, tapping an
    // already-known word in the Reader and hitting "Add to SRS Deck"
    // would push a second, independent card for the same lemma, since
    // this only ever checked srsDeck, never knownWords.
    if (srsDeck.find(w => w.spanish === cleanWord) || isKnown(cleanWord)) {
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
    if (btn) {
        btn.textContent = '✓ Added to deck!';
        btn.disabled = true;
        btn.style.background = 'var(--primary)';
    }
    
    updateSRSCounter();
    saveDeck();
    updateReaderWordColors();
    setTimeout(closePopup, 600);
}

function updateSRSCounter() {
    const counter = document.getElementById('srs-counter');
    if (counter) counter.textContent = srsDeck.length;
    if (typeof window !== 'undefined' && typeof window.dispatchEvent === 'function') {
        window.dispatchEvent(new CustomEvent('srs-updated', { detail: { count: srsDeck.length } }));
    }
}

// ============================================
// SRS REVIEW SYSTEM
// ============================================
let currentReviewCard = null;
let sessionRelearningQueue = [];

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
let reviewLimit = null;

// Which side of the card shows first: 'es-en' is recognition (see Spanish,
// recall the meaning), 'en-es' is production (see English, recall the
// word). A study-style preference like XP and the streak (see the header
// comment in engine/lang.js), not a property of one course, so it is a
// plain key rather than one scoped through Lang.key() — a learner who
// prefers production-first wants that whichever course they are reviewing.
const REVIEW_DIRECTION_KEY = 'app_reviewDirection';
let reviewDirection = 'en-es';
try {
    const saved = localStorage.getItem(REVIEW_DIRECTION_KEY);
    reviewDirection = saved === 'es-en' ? 'es-en' : 'en-es';
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
    // Drop the flipped-height hold (see revealAnswer()) — Type mode's card
    // is laid out differently.
    const cardEl = document.getElementById('review-card');
    if (cardEl) cardEl.style.minHeight = '';
    // Same reasoning as toggleReviewDirection(): redraw the same card in the
    // new mode rather than skipping to a fresh one.
    if (currentReviewCard) renderCard();
}

function updateDirectionToggle() {
    const btn = document.getElementById('dk-direction-toggle');
    const esLabel = document.getElementById('dk-direction-es');
    const enLabel = document.getElementById('dk-direction-en');
    const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'Spanish';

    if (btn) {
        btn.setAttribute('data-direction', reviewDirection);
        btn.setAttribute('aria-checked', reviewDirection !== 'es-en' ? 'true' : 'false');
        btn.setAttribute('aria-label', `Toggle review direction (${langName}, English)`);
    }
    if (esLabel) {
        esLabel.textContent = langName;
        esLabel.title = `${langName} to English`;
        esLabel.classList.toggle('dk-direction-active', reviewDirection === 'es-en');
    }
    if (enLabel) {
        enLabel.title = `English to ${langName}`;
        enLabel.classList.toggle('dk-direction-active', reviewDirection === 'en-es');
    }
}

function setReviewDirection(dir) {
    if (reviewDirection === dir) return;
    reviewDirection = dir;
    try {
        localStorage.setItem(REVIEW_DIRECTION_KEY, reviewDirection);
    } catch (error) {
        // Private browsing with storage disabled: the preference just won't
        // survive a reload.
    }
    updateDirectionToggle();
    if (currentReviewCard) renderCard();
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

function updateReviewBanner() {
    const banner = document.getElementById('review-scope');
    if (!banner) return;
    if (reviewLimit) {
        const current = (reviewSessionStats ? reviewSessionStats.total : 0) + 1;
        const scopePrefix = reviewScope ? reviewScopeName + ' · ' : '';
        banner.textContent = `${scopePrefix}Card ${Math.min(current, reviewLimit)} of ${reviewLimit}`;
        banner.style.display = 'block';
    } else if (reviewScope) {
        banner.textContent = 'Reviewing: ' + reviewScopeName;
        banner.style.display = 'block';
    } else {
        banner.textContent = '';
        banner.style.display = 'none';
    }
}

function startReviewSession(lemmas, name, options) {
    sessionRelearningQueue = [];
    reviewScope = lemmas ? new Set(lemmas) : null;
    reviewScopeName = reviewScope ? (name || 'Deck') : '';
    reviewLimit = (options && typeof options.limit === 'number' && options.limit > 0) ? options.limit : null;
    reviewSessionStats = {
        total: 0, again: 0, hard: 0, good: 0, easy: 0,
        startedAt: Date.now(),
        missed: [], // {lemma, translation, pos} for each distinct card rated "again" this session
        xpBefore: (typeof xpData !== 'undefined') ? xpData.total : 0,
        rankBefore: (typeof getRank === 'function') ? getRank().rank : null,
        limit: reviewLimit
    };

    updateReviewBanner();

    const cardEl = document.getElementById('review-card');
    if (cardEl) cardEl.style.minHeight = '';

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

    // Inside a timed session the next step is the session's own "Next"
    // button — practising missed words would leave the session for
    // Workshop, and "Done" would drop the learner into Decks with the
    // session left hanging.
    const inTimedSession = typeof StudyPlan !== 'undefined' && StudyPlan.isActive();
    // Practising them opens the Vocabulary Driller, which is B1+.
    const vocabDrillerOpen = typeof Workshop === 'undefined' || !Workshop.isAvailable || Workshop.isAvailable('vocabulary');
    const missedCount = (inTimedSession || !vocabDrillerOpen) ? 0 : s.missed.length;

    summaryEl.innerHTML = `
        <p class="review-summary-eyebrow">Session complete</p>
        <h2 class="review-summary-title">Nice work.</h2>
        ${statsHtml}
        ${streakText ? `<p class="review-summary-streak">${escFn(streakText)}</p>` : ''}
        ${rankedUp ? `<p class="review-summary-milestone">Rank up! You're now Rank ${rankAfter}.</p>` : ''}
        ${milestones.map(m => `<p class="review-summary-milestone">Milestone: ${escFn(m.label)}</p>`).join('')}
        ${missedCount ? `
            <button class="dk-secondary" data-action="practice-missed">
                Practice ${missedCount} missed ${missedCount === 1 ? 'word' : 'words'}
            </button>
        ` : ''}
        ${inTimedSession ? '' : '<button class="dk-secondary" onclick="endReviewSession()">Done</button>'}
    `;
    summaryEl.style.display = 'block';

    const practiseBtn = summaryEl.querySelector('[data-action="practice-missed"]');
    if (practiseBtn) practiseBtn.addEventListener('click', () => practiceMissedFromReview(s.missed));

    if (typeof RecommendationEngine !== 'undefined') RecommendationEngine.mountNextAction(summaryEl);
    if (typeof Sync !== 'undefined' && Sync.scheduleAutoSave) Sync.scheduleAutoSave();
}

// The words rated "again" this session, straight into a Vocabulary
// Driller session scoped to just them — closes the review session first
// (same as Done would) so leaving Workshop later doesn't drop back into a
// stale review screen, then switches tabs the same way Home's own
// cross-tab links (goTab() in engine/home.js) do.
function practiceMissedFromReview(words) {
    endReviewSession();
    showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
    if (typeof Workshop !== 'undefined') Workshop.open('vocabulary', { words: words });
}

function endReviewSession() {
    sessionRelearningQueue = [];
    reviewScope = null;
    reviewScopeName = '';
    reviewLimit = null;
    reviewSessionStats = null;
    // rateCard() bails immediately when this is null (see its own guard) --
    // resetting it here is what makes a swipe-gesture's delayed rateCard()
    // setTimeout (srs.js's finishGesture, ~200ms) a safe no-op if the
    // learner backs out of the session before that timeout fires, instead
    // of mutating srsDeck / re-populating hidden review DOM after teardown.
    currentReviewCard = null;
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
    const now = Date.now();
    return srsDeck.filter(card => {
        if (!inScope(card)) return false;
        if (!card.nextReview) return true;
        return new Date(card.nextReview).getTime() <= now;
    }).sort((a, b) => {
        const aTime = a.nextReview ? new Date(a.nextReview).getTime() : 0;
        const bTime = b.nextReview ? new Date(b.nextReview).getTime() : 0;
        return aTime - bTime;
    });
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
    const remainingCount = getDueCards().length + sessionRelearningQueue.length;
    if (due) {
        due.textContent = reviewLimit
            ? Math.max(0, reviewLimit - (reviewSessionStats ? reviewSessionStats.total : 0))
            : remainingCount;
    }
    if (fresh) fresh.textContent = getNewCards().length;
    if (total) {
        total.textContent = reviewLimit
            ? reviewLimit
            : (reviewScope ? srsDeck.filter(inScope).length : srsDeck.length);
    }
}

function showNextCard() {
    updateDirectionToggle();

    const cardEl = document.getElementById('review-card');
    const emptyEl = document.getElementById('review-empty');
    const summaryEl = document.getElementById('review-summary');

    // If session has a limit (e.g. timed micro-session) and it is reached:
    if (reviewLimit && reviewSessionStats && reviewSessionStats.total >= reviewLimit) {
        if (cardEl) cardEl.style.display = 'none';
        currentReviewCard = null;
        if (emptyEl) emptyEl.style.display = 'none';
        renderReviewSessionSummary();
        return;
    }

    const dueCards = getDueCards();

    let nextCard = null;
    if (dueCards.length > 0) {
        // Pick from the most urgent cards. If reviewLimit is set, pick from the top slice
        const pool = (reviewLimit && dueCards.length > reviewLimit) ? dueCards.slice(0, reviewLimit) : dueCards;
        nextCard = shuffled(pool)[0];
    } else if (sessionRelearningQueue.length > 0) {
        // Cards that were rated "again" in this session but have not yet been recalled
        nextCard = sessionRelearningQueue[0];
    }

    if (!nextCard) {
        if (cardEl) cardEl.style.display = 'none';
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
            if (emptyEl) emptyEl.style.display = 'block';
        }
        return;
    }

    updateReviewBanner();

    if (cardEl) cardEl.style.display = 'flex';
    if (emptyEl) emptyEl.style.display = 'none';
    if (summaryEl) summaryEl.style.display = 'none';

    currentReviewCard = nextCard;
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

// Type mode's objective grade for the current card, set by
// checkTypedAnswer() and consumed by continueTypedReview() -- null means
// "not graded yet" (still typing / card just rendered).
let typedAnswerCorrect = null;
let typedAssessedBucket = null;
let cardStartTime = 0;

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

    const spanishHtml = esc(spanishDisplay) + (typeof ParlourTTS !== 'undefined' ? ParlourTTS.button(currentReviewCard.spanish, { type: 'vocabulary' }) : '');
    if (typeof ParlourTTS !== 'undefined' && ParlourTTS.preload && currentReviewCard.spanish) {
        ParlourTTS.preload({ text: currentReviewCard.spanish, type: 'vocabulary' });
    }
    // A card flagged leech (see SRS_CONFIG.LEECH_THRESHOLD) gets a quiet
    // badge here rather than any different treatment of the card itself —
    // it's information for the learner ("this one keeps not sticking"),
    // not a reason to skip or suspend it.
    const contextHtml = (displayType ? `(${esc(displayType)})` : '')
        + (currentReviewCard.leech ? ' <span class="srs-leech-badge" title="Rated Again 8+ times">Leech</span>' : '');
    if (englishFirst) {
        document.getElementById('review-front').textContent = displayEnglish;
        document.getElementById('review-back').innerHTML = spanishHtml;
        document.getElementById('review-context').innerHTML = contextHtml;
    } else {
        document.getElementById('review-front').innerHTML = spanishHtml;
        document.getElementById('review-back').textContent = displayEnglish;
        document.getElementById('review-context').innerHTML = contextHtml;
    }
    reviewExpectedSpanish = currentReviewCard.spanish;
    reviewExpectedEnglish = displayEnglish;

    const typeMode = reviewMode === 'type';

    // Type mode keeps the answer's slot (invisible) so the input below it
    // doesn't drop when Check reveals the answer and jump back up on the
    // next card.
    const answerEl = document.getElementById('review-answer');
    answerEl.style.display = typeMode ? 'block' : 'none';
    answerEl.style.visibility = typeMode ? 'hidden' : '';
    document.getElementById('rating-buttons').style.display = 'none';
    const flipActions = document.getElementById('review-flip-actions');
    if (flipActions) flipActions.style.display = typeMode ? 'none' : 'flex';
    document.getElementById('show-answer-btn').style.display = typeMode ? 'none' : 'block';

    document.getElementById('review-type-input').classList.toggle('hidden', !typeMode);
    const diacriticsEl = document.getElementById('review-type-diacritics');
    if (diacriticsEl) {
        if (typeMode && typeof UI !== 'undefined' && UI.diacriticsBarHtml) {
            diacriticsEl.innerHTML = UI.diacriticsBarHtml('#review-type-field');
        } else {
            diacriticsEl.innerHTML = '';
        }
    }

    const hintEl = document.getElementById('review-type-hint');
    if (hintEl) {
        let hasSeenHint = false;
        try {
            hasSeenHint = !!localStorage.getItem('srs_type_mode_hint_seen');
        } catch (e) {}
        hintEl.classList.toggle('hidden', !typeMode || hasSeenHint);
        if (!hintEl._wiredDismiss) {
            hintEl._wiredDismiss = true;
            hintEl.addEventListener('click', () => {
                try { localStorage.setItem('srs_type_mode_hint_seen', '1'); } catch (e) {}
                hintEl.classList.add('hidden');
            });
        }
    }
    const field = document.getElementById('review-type-field');
    if (field) {
        field.value = '';
        field.classList.remove('correct', 'almost', 'wrong');
        if (typeMode && (!window.matchMedia || !window.matchMedia('(max-width: 639px)').matches)) {
            field.focus({ preventScroll: true });
        }
    }
    // revealTypedResult() hides these while the previous card's answer is
    // shown; bring them back for the new card instead of leaving them gone.
    const micBtn = document.querySelector('#review-type-input .lsn-mic-addon');
    if (micBtn) micBtn.style.display = '';
    if (diacriticsEl) diacriticsEl.style.display = '';
    const checkBtn = document.getElementById('review-check-btn');
    if (checkBtn) checkBtn.style.display = '';
    typedAnswerCorrect = null;
    typedAssessedBucket = null;
    cardStartTime = Date.now();
    const assessEl = document.getElementById('review-type-assessment');
    if (assessEl) {
        assessEl.innerHTML = '';
        assessEl.className = 'review-type-assessment hidden';
    }
    const continueBtn = document.getElementById('review-type-continue-btn');
    if (continueBtn) {
        continueBtn.classList.add('hidden');
        continueBtn.textContent = 'Continue';
    }

    updateRatingLabels();
    updateReviewStats();
    updateDirectionToggle();
    updateModeToggle();

    const cardEl = document.getElementById('review-card');
    if (cardEl) {
        cardEl.style.transform = '';
        cardEl.style.opacity = '';
        cardEl.style.transition = '';
        cardEl.style.borderColor = '';
        initCardGestures();
    }
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
    const answerEl = document.getElementById('review-answer');
    answerEl.style.display = 'block';
    answerEl.style.visibility = '';
    const flipActions = document.getElementById('review-flip-actions');
    if (flipActions) flipActions.style.display = 'none';
    document.getElementById('show-answer-btn').style.display = 'none';
    document.getElementById('review-type-input').classList.add('hidden');
    const ratingsEl = document.getElementById('rating-buttons');
    ratingsEl.style.display = 'flex';

    // On a phone the revealed answer pushes the rating row below the fold,
    // and hiding it again for the next card shrinks the page, so the browser
    // snapped the scroll back up — the learner had to scroll down on every
    // card. Holding the card at its flipped height keeps the page (and the
    // card) still between cards; .review-flip-actions sits at the card's
    // bottom, so Show Answer lands where the rating buttons just were.
    const cardEl = document.getElementById('review-card');
    if (cardEl) cardEl.style.minHeight = cardEl.offsetHeight + 'px';
    ratingsEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
}

function showAnswer() {
    revealAnswer();
}

// Type mode keeps #review-answer laid out but invisible until Check (see
// renderCard()), so display alone doesn't say whether it's been revealed.
function isAnswerShown() {
    const answerEl = document.getElementById('review-answer');
    return answerEl.style.display === 'block' && answerEl.style.visibility !== 'hidden';
}

function initCardGestures() {
    const cardEl = document.getElementById('review-card');
    if (!cardEl || cardEl._gesturesBound) return;
    cardEl._gesturesBound = true;

    let startX = 0, startY = 0, currentX = 0, currentY = 0;
    let isTracking = false;
    let isDragging = false;

    cardEl.addEventListener('touchstart', (e) => {
        if (!currentReviewCard) return;
        if (e.target.closest('button') || e.target.closest('input')) return;
        const t = e.touches[0];
        startX = t.clientX;
        startY = t.clientY;
        currentX = startX;
        currentY = startY;
        isTracking = true;
        isDragging = false;
        cardEl.style.transition = 'none';
    }, { passive: true });

    cardEl.addEventListener('touchmove', (e) => {
        if (!isTracking) return;
        const t = e.touches[0];
        currentX = t.clientX;
        currentY = t.clientY;
        const dx = currentX - startX;
        const dy = currentY - startY;

        if (!isDragging && Math.abs(dx) > 10 && Math.abs(dx) > Math.abs(dy)) {
            isDragging = true;
        }

        if (isDragging) {
            const rotate = dx / 16;
            cardEl.style.transform = `translateX(${dx}px) rotate(${rotate}deg)`;

            if (dx < -30) {
                cardEl.style.borderColor = 'var(--danger)';
            } else if (dx > 30) {
                cardEl.style.borderColor = 'var(--success)';
            } else {
                cardEl.style.borderColor = 'var(--border)';
            }
        }
    }, { passive: true });

    const finishGesture = () => {
        if (!isTracking) return;
        const dx = currentX - startX;
        const dy = currentY - startY;
        const answerShown = isAnswerShown();

        if (isDragging) {
            const threshold = Math.min(90, window.innerWidth * 0.22);
            if (dx < -threshold && answerShown) {
                // Swipe Left -> "Again"
                cardEl.style.transition = 'transform 0.2s ease-out, opacity 0.2s ease-out';
                cardEl.style.transform = 'translateX(-120vw) rotate(-25deg)';
                cardEl.style.opacity = '0';
                setTimeout(() => {
                    rateCard('again');
                }, 200);
            } else if (dx > threshold && answerShown) {
                // Swipe Right -> "Good"
                cardEl.style.transition = 'transform 0.2s ease-out, opacity 0.2s ease-out';
                cardEl.style.transform = 'translateX(120vw) rotate(25deg)';
                cardEl.style.opacity = '0';
                setTimeout(() => {
                    rateCard('good');
                }, 200);
            } else if (Math.abs(dx) > threshold && !answerShown && reviewMode !== 'type') {
                // Dragged past threshold when answer not shown -> reveal answer and snap back
                showAnswer();
                cardEl.style.transition = 'transform 0.2s ease, border-color 0.2s ease';
                cardEl.style.transform = 'translateX(0) rotate(0deg)';
                cardEl.style.borderColor = 'var(--border)';
            } else {
                // Snap back
                cardEl.style.transition = 'transform 0.2s ease, border-color 0.2s ease';
                cardEl.style.transform = 'translateX(0) rotate(0deg)';
                cardEl.style.borderColor = 'var(--border)';
            }
        } else if (Math.abs(dx) < 10 && Math.abs(dy) < 10) {
            // Tap on card body: flip/reveal answer if not already revealed
            if (!answerShown && reviewMode !== 'type') {
                showAnswer();
            }
        }

        isTracking = false;
        isDragging = false;
    };

    cardEl.addEventListener('touchend', finishGesture);
    cardEl.addEventListener('touchcancel', finishGesture);
}

// Same normalisation lessons.js/GrammarRunner use elsewhere: case,
// whitespace and punctuation stripped, but accents checked directly
// (2026-08-27) - "dia" no longer matches "día", matching the standard the
// rest of the course now holds accents to for both languages. Also strips
// a trailing "…" — Lexicon.shortGloss() appends one when it caps a gloss
// to its first 3 synonyms (e.g. "to take, to grab, to catch…"), and
// without stripping it here a learner who types the complete, correct
// last-shown synonym ("to catch") was marked wrong because the stored
// expected answer still carried the ellipsis glued onto it.
function srsNormalise(text) {
    return String(text || '').toLowerCase()
        .replace(/["'«»“”„—–\-]/g, ' ')
        .replace(/[.,!?¡¿;:]/g, '')
        .replace(/…$/, '')
        .replace(/\s+/g, ' ')
        .trim()
        .normalize('NFC');
}

// The English side is often a list of near-synonyms ("hello / hi", "to
// remove, to take away") rather than one fixed phrase — split on both
// separators and accept a match against any alternative.
function englishAlternatives(text) {
    return String(text || '').split(/[/,]/).map(srsNormalise).filter(Boolean);
}

// Enter does double duty in type mode: first press checks the typed
// answer, second press advances — this keeps the mobile keyboard open
// the whole time instead of it dismissing (Check) then needing a tap
// on a separate Continue button, which made the viewport jump. Wired to
// the wrapping <form>'s onsubmit (not the input's onkeydown) because iOS
// Safari doesn't reliably fire a keydown event for the virtual
// keyboard's Return/Go key, but every mobile browser submits a
// single-input form when that key is pressed.
function handleTypeFieldSubmit(event) {
    if (event && event.preventDefault) event.preventDefault();
    if (typedAnswerCorrect === null) {
        checkTypedAnswer();
    } else {
        continueTypedReview();
    }
    return false;
}

function checkTypedAnswer() {
    if (!currentReviewCard || typedAnswerCorrect !== null) return;
    const field = document.getElementById('review-type-field');
    if (!field) return;

    const rawTyped = (field.value || '').trim();
    if (!rawTyped) return;

    try {
        localStorage.setItem('srs_type_mode_hint_seen', '1');
    } catch (e) {}
    const hintEl = document.getElementById('review-type-hint');
    if (hintEl) hintEl.classList.add('hidden');

    const englishFirst = reviewDirection === 'en-es';
    const typed = srsNormalise(rawTyped);

    const elapsedMs = Date.now() - (cardStartTime || Date.now());
    const elapsedSec = Math.max(0.4, elapsedMs / 1000);

    const stripAccents = (str) => String(str || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();

    let isExact = false;
    let isNearMiss = false;

    if (englishFirst) {
        const acceptableSpanish = new Set([srsNormalise(reviewExpectedSpanish)]);
        if (typeof Lexicon !== 'undefined' && typeof Lexicon.withArticle === 'function') {
            const withArt = Lexicon.withArticle(reviewExpectedSpanish);
            if (withArt) acceptableSpanish.add(srsNormalise(withArt));
        }
        const strippedTyped = typed.replace(/^(el|la|los|las|un|una|unos|unas|a|az)\s+/i, '');
        const strippedExpected = srsNormalise(reviewExpectedSpanish).replace(/^(el|la|los|las|un|una|unos|unas|a|az)\s+/i, '');
        isExact = acceptableSpanish.has(typed) || (strippedTyped.length > 0 && strippedTyped === strippedExpected);

        if (!isExact) {
            const accentLessTyped = stripAccents(strippedTyped || typed);
            for (const acc of acceptableSpanish) {
                const strippedAcc = acc.replace(/^(el|la|los|las|un|una|unos|unas|a|az)\s+/i, '');
                if (stripAccents(strippedAcc) === accentLessTyped) {
                    isNearMiss = true;
                    break;
                }
            }
        }
    } else {
        const alts = englishAlternatives(reviewExpectedEnglish);
        isExact = alts.includes(typed);
        if (!isExact) {
            const accentLessTyped = stripAccents(typed);
            isNearMiss = alts.some(alt => stripAccents(alt) === accentLessTyped);
        }
    }

    // Auto-assess into the four SM-2 buckets based on speed and accuracy:
    // 1. Exact match under 3.0s -> 'easy' (fluent, instantaneous recall)
    // 2. Exact match 3.0s to 7.5s -> 'good' (confident recall)
    // 3. Exact match over 7.5s OR near-miss (minor accent slip) -> 'hard' (hesitation or slight inaccuracy)
    // 4. Inaccurate / incorrect -> 'again' (relearning required)
    let bucket = 'again';
    if (isExact) {
        if (elapsedSec < 3.0) {
            bucket = 'easy';
        } else if (elapsedSec <= 7.5) {
            bucket = 'good';
        } else {
            bucket = 'hard';
        }
    } else if (isNearMiss) {
        bucket = 'hard';
    } else {
        bucket = 'again';
    }

    typedAssessedBucket = bucket;
    typedAnswerCorrect = (bucket !== 'again');

    field.classList.toggle('correct', bucket === 'easy' || bucket === 'good');
    field.classList.toggle('almost', bucket === 'hard');
    field.classList.toggle('wrong', bucket === 'again');
    // Deliberately left editable (not disabled, not readOnly): either one
    // can hold focus but a readOnly field never re-triggers the mobile
    // keyboard, which the Listen button needs (see the click listener
    // below) when it steals focus after the answer's been checked. Editing
    // the text here is harmless — typedAnswerCorrect already locked the
    // grade in.

    revealTypedResult(bucket, elapsedSec, isNearMiss);
}

// Type mode automatically evaluates accuracy and speed to place the card into
// one of the 4 buckets (Easy, Good, Hard, Again) and provides instant visual feedback.
function revealTypedResult(bucket, elapsedSec, isNearMiss) {
    const answerEl = document.getElementById('review-answer');
    answerEl.style.display = 'block';
    answerEl.style.visibility = '';
    document.getElementById('rating-buttons').style.display = 'none';

    // Deliberately NOT hiding #review-type-input here: it holds the field
    // itself, and hiding an ancestor forces the browser to blur it, which
    // dismisses the mobile keyboard. Instead hide just the pieces that no
    // longer apply once the answer's checked, and leave the field in place
    // (readOnly, not display:none) so focus — and the keyboard — survive
    // through to the next card's Enter press.
    const micBtn = document.querySelector('#review-type-input .lsn-mic-addon');
    if (micBtn) micBtn.style.display = 'none';
    const typeDiacriticsEl = document.getElementById('review-type-diacritics');
    if (typeDiacriticsEl) typeDiacriticsEl.style.display = 'none';
    const checkBtn = document.getElementById('review-check-btn');
    if (checkBtn) checkBtn.style.display = 'none';

    const assessEl = document.getElementById('review-type-assessment');
    if (assessEl) {
        const speedText = elapsedSec ? `${elapsedSec.toFixed(1)}s` : '';
        let badgeHtml = '';
        if (bucket === 'easy') {
            badgeHtml = `<span class="srs-bucket-badge srs-bucket-easy">Easy · ${speedText}</span> <span class="srs-bucket-desc">Quick recall</span>`;
        } else if (bucket === 'good') {
            badgeHtml = `<span class="srs-bucket-badge srs-bucket-good">Good · ${speedText}</span> <span class="srs-bucket-desc">Accurate recall</span>`;
        } else if (bucket === 'hard') {
            const desc = isNearMiss ? 'Minor accent or typo' : (speedText ? `Recalled in ${speedText}` : 'Struggled recall');
            badgeHtml = `<span class="srs-bucket-badge srs-bucket-hard">Hard · ${desc}</span>`;
        } else {
            badgeHtml = `<span class="srs-bucket-badge srs-bucket-again">Again</span> <span class="srs-bucket-desc">Needs practice</span>`;
        }
        assessEl.innerHTML = badgeHtml;
        assessEl.className = `review-type-assessment review-assess-${bucket}`;
        assessEl.classList.remove('hidden');
    }

    const continueBtn = document.getElementById('review-type-continue-btn');
    if (continueBtn) {
        continueBtn.textContent = 'Continue';
        continueBtn.classList.remove('hidden');
    }

    // Same hold as revealAnswer(): keep the card at its checked height so
    // the next card doesn't shrink the page and snap the scroll up.
    const cardEl = document.getElementById('review-card');
    if (cardEl) cardEl.style.minHeight = cardEl.offsetHeight + 'px';
    if (assessEl) assessEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
}

function continueTypedReview() {
    if (typedAssessedBucket === null && typedAnswerCorrect === null) return;
    const bucket = typedAssessedBucket || (typedAnswerCorrect ? 'good' : 'again');
    rateCard(bucket);
}

function rateCard(rating) {
    if (!currentReviewCard) return;

    const now = new Date();

    // Runs before scheduleCard, which is what makes "is this card new?"
    // answerable — rescheduling increments the review count.
    recordReview(currentReviewCard, rating);

    scheduleCard(currentReviewCard, rating, now);
    maybeGraduate(currentReviewCard);

    if (rating === 'again') {
        if (!sessionRelearningQueue.some(c => c.spanish === currentReviewCard.spanish)) {
            sessionRelearningQueue.push(currentReviewCard);
        } else {
            sessionRelearningQueue = sessionRelearningQueue.filter(c => c.spanish !== currentReviewCard.spanish);
            sessionRelearningQueue.push(currentReviewCard);
        }
    } else {
        sessionRelearningQueue = sessionRelearningQueue.filter(c => c.spanish !== currentReviewCard.spanish);
    }

    if (reviewSessionStats) {
        reviewSessionStats.total++;
        if (typeof reviewSessionStats[rating] === 'number') reviewSessionStats[rating]++;
        if (rating === 'again' && !reviewSessionStats.missed.some(w => w.lemma === currentReviewCard.spanish)) {
            reviewSessionStats.missed.push({
                lemma: currentReviewCard.spanish,
                translation: currentReviewCard.english,
                pos: currentReviewCard.type
            });
        }
    }

    saveDeck();
    updateReaderWordColors();
    showNextCard();
}

// Tapping the word's Listen button (ParlourTTS.button(), rendered inside
// #review-card) steals focus from #review-type-field, which on mobile also
// dismisses the keyboard — stranding the learner with no Continue button
// (hidden on phones, see components.css) and no keyboard to press Enter
// on. Refocusing here, synchronously inside the click handler, is still
// within the user gesture that started it, so iOS reopens the keyboard.
if (typeof document !== 'undefined') {
    document.addEventListener('click', (event) => {
        if (reviewMode !== 'type') return;
        const speakBtn = event.target.closest && event.target.closest('.speak-btn');
        if (!speakBtn) return;
        const card = document.getElementById('review-card');
        if (!card || !card.contains(speakBtn)) return;
        const field = document.getElementById('review-type-field');
        if (field) field.focus({ preventScroll: true });
    });
}

// Desktop keyboard flow for review session
if (typeof window !== 'undefined' && typeof window.addEventListener === 'function') {
window.addEventListener('keydown', (e) => {
    const session = document.getElementById('review-session');
    if (!session || session.classList.contains('hidden') || session.style.display === 'none') return;
    if (!currentReviewCard) return;

    // Don't intercept when user is typing in an input or textarea
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    const answerShown = isAnswerShown();

    if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        if (!answerShown) {
            showAnswer();
        } else if (reviewMode === 'type') {
            continueTypedReview();
        } else {
            rateCard('good');
        }
    } else if (answerShown && reviewMode !== 'type') {
        if (e.key === '1') { e.preventDefault(); rateCard('again'); }
        else if (e.key === '2') { e.preventDefault(); rateCard('hard'); }
        else if (e.key === '3') { e.preventDefault(); rateCard('good'); }
        else if (e.key === '4') { e.preventDefault(); rateCard('easy'); }
    }
});
}

if (typeof document !== 'undefined') {
    document.addEventListener('language-changed', () => {
        loadDeck();
        loadKnownWords();
        currentReviewCard = null;
        typedAnswerCorrect = null;
        if (typeof updateReaderWordColors === 'function') {
            updateReaderWordColors();
        }
    });
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        loadDeck,
        saveDeck,
        loadKnownWords,
        saveKnownWords,
        srsNormalise,
        englishAlternatives,
        getDeck: () => srsDeck,
        setDeck: (d) => { srsDeck = d; }
    };
}