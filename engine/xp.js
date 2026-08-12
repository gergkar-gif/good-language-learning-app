// ============================================
// XP SYSTEM
// ============================================
// XP is deliberately small. A normal day lands around 30-100 and a heavy
// day around 150 — see the calibration note above DAILY_GOALS. Nothing is
// paid for time spent, and nothing is paid for adding a word: a new word
// earns its keep only when it is successfully reviewed.
let xpData = {
    total: 0,
    // date -> { total, review, reading, grammar, reviewsDone, newWords,
    //           storiesDone, lessonsDone }
    history: {},
    // date -> words added that day, which is what the cap below limits
    dailyNewWords: {}
};

const NEW_WORDS_DAILY_CAP = 20;

const REVIEW_XP = { again: 0, hard: 1, good: 2, easy: 3 };
const READING_XP = 15;
const GRAMMAR_XP = 20;

// Doing exactly the three daily activities is 20 reviews (~40 XP at a
// typical mix of ratings) + one story (15) + one lesson (20) = ~75 XP.
// Reviews only, or a lighter day, sits near 30-40; a heavy day of 40
// reviews plus a story and two lessons reaches ~150.
const DAILY_GOALS = { reviews: 20, stories: 1, lessons: 1 };
const STREAK_ACTIVITIES_REQUIRED = 2;

const RATING_LABELS = { hard: 'Hard review', good: 'Good review', easy: 'Easy review' };

function dateString(date) {
    return date.toISOString().split('T')[0];
}

function getTodayString() {
    return dateString(new Date());
}

function emptyDay() {
    return {
        total: 0,
        review: 0,
        reading: 0,
        grammar: 0,
        reviewsDone: 0,
        newWords: 0,
        storiesDone: 0,
        lessonsDone: 0
    };
}

// Read-write: creates the day if it doesn't exist yet.
function dayEntry(dateStr) {
    if (!xpData.history[dateStr]) xpData.history[dateStr] = emptyDay();
    return xpData.history[dateStr];
}

// Read-only: never writes an empty day into history.
function getDay(dateStr) {
    return xpData.history[dateStr] || emptyDay();
}

function loadXP() {
    const saved = localStorage.getItem('spanishApp_xp');
    if (!saved) return;

    const parsed = JSON.parse(saved);
    xpData = {
        total: parsed.total || 0,
        history: {},
        dailyNewWords: parsed.dailyNewWords || {}
    };

    // The first version stored a bare XP number per day. Keep the total and
    // leave the breakdown at zero — it was never recorded, so inventing a
    // split would be worse than admitting we don't have one.
    Object.keys(parsed.history || {}).forEach(date => {
        const value = parsed.history[date];
        xpData.history[date] = typeof value === 'number'
            ? Object.assign(emptyDay(), { total: value })
            : Object.assign(emptyDay(), value);
    });
}

function saveXP() {
    localStorage.setItem('spanishApp_xp', JSON.stringify(xpData));
    updateXPHeader();
}

// ============================================
// NEW WORD CAP
// ============================================
function getDailyNewWords(dateStr) {
    return xpData.dailyNewWords[dateStr] || 0;
}

function canAddNewWord() {
    return getDailyNewWords(getTodayString()) < NEW_WORDS_DAILY_CAP;
}

// Adding a word is worth no XP — it only counts against the daily cap.
function recordNewWord() {
    const today = getTodayString();
    if (!xpData.dailyNewWords[today]) {
        xpData.dailyNewWords[today] = 0;
    }
    xpData.dailyNewWords[today]++;
    saveXP();
}

// ============================================
// AWARDING
// ============================================
function awardXP(amount, source, reason) {
    if (!amount) return;

    const day = dayEntry(getTodayString());
    day.total += amount;
    if (typeof day[source] === 'number') day[source] += amount;
    xpData.total += amount;

    saveXP();
    showXPNotification(amount, reason);
}

// Call before the card is rescheduled — "new" means it has no reviews yet.
function recordReview(card, rating) {
    const day = dayEntry(getTodayString());
    day.reviewsDone++;

    // A word counts as learned on its first successful review, not when it
    // was added to the deck.
    if (!card.reviews && rating !== 'again') day.newWords++;

    const amount = REVIEW_XP[rating] || 0;
    if (amount) {
        awardXP(amount, 'review', RATING_LABELS[rating]);
    } else {
        saveXP();
    }
}

// isFirstTime is false when the learner is re-reading or replaying: the
// activity still counts towards the streak, but the XP is not paid twice.
function recordStoryCompleted(isFirstTime) {
    dayEntry(getTodayString()).storiesDone++;
    if (isFirstTime) {
        awardXP(READING_XP, 'reading', 'Story complete');
    } else {
        saveXP();
    }
}

function recordLessonCompleted(isFirstTime) {
    dayEntry(getTodayString()).lessonsDone++;
    if (isFirstTime) {
        awardXP(GRAMMAR_XP, 'grammar', 'Lesson complete');
    } else {
        saveXP();
    }
}

function showXPNotification(amount, reason) {
    const notif = document.createElement('div');
    notif.textContent = (amount > 0 ? '+' : '') + amount + ' XP — ' + reason;
    notif.style.cssText = `
        position: fixed;
        top: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: var(--primary);
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        z-index: 1000;
        animation: fadeUp 2s ease-out forwards;
    `;
    document.body.appendChild(notif);
    setTimeout(() => notif.remove(), 2000);
}

// ============================================
// DAILY ACTIVITIES & STREAK
// ============================================
// The streak is about showing up, not about points — two of the three
// activities keeps it, all three makes the day perfect.
function getDailyActivities(dateStr) {
    const day = getDay(dateStr || getTodayString());

    // Icons name a section of the app, so they are ids in the art registry
    // rather than emoji: the three chips sit on Home now, next to the same
    // marks drawn in the nav, and a colour emoji beside them reads as a
    // different app.
    const list = [
        { key: 'review', icon: 'decks', label: 'Review', count: day.reviewsDone, goal: DAILY_GOALS.reviews },
        { key: 'reading', icon: 'reader', label: 'Read', count: day.storiesDone, goal: DAILY_GOALS.stories },
        { key: 'learn', icon: 'lessons', label: 'Learn', count: day.lessonsDone, goal: DAILY_GOALS.lessons }
    ];
    list.forEach(activity => { activity.done = activity.count >= activity.goal; });

    const completed = list.filter(activity => activity.done).length;

    return {
        list: list,
        completed: completed,
        perfect: completed === list.length,
        keepsStreak: completed >= STREAK_ACTIVITIES_REQUIRED
    };
}

function isStreakDay(dateStr) {
    return getDailyActivities(dateStr).keepsStreak;
}

function getStreak() {
    const today = new Date();
    // A day still in progress shouldn't read as a broken streak, so if today
    // hasn't qualified yet the count starts from yesterday.
    let offset = isStreakDay(dateString(today)) ? 0 : 1;
    let streak = 0;

    for (;;) {
        const day = new Date(today);
        day.setDate(day.getDate() - offset);
        if (!isStreakDay(dateString(day))) break;
        streak++;
        offset++;
    }

    return streak;
}

function getPerfectDays() {
    return Object.keys(xpData.history)
        .filter(date => getDailyActivities(date).perfect)
        .length;
}

// Deliberately separate numbers rather than one blended score.
function getStats() {
    let reviewsCompleted = 0;
    let storiesCompleted = 0;
    let lessonsCompleted = 0;
    let newWordsLearned = 0;

    Object.keys(xpData.history).forEach(date => {
        const day = xpData.history[date];
        reviewsCompleted += day.reviewsDone || 0;
        storiesCompleted += day.storiesDone || 0;
        lessonsCompleted += day.lessonsDone || 0;
        newWordsLearned += day.newWords || 0;
    });

    return {
        totalXP: xpData.total,
        reviewsCompleted: reviewsCompleted,
        storiesCompleted: storiesCompleted,
        lessonsCompleted: lessonsCompleted,
        newWordsLearned: newWordsLearned,
        perfectDays: getPerfectDays(),
        currentStreak: getStreak(),
        monthlyConsistency: getConsistency(30)
    };
}

function getConsistency(windowDays) {
    windowDays = windowDays || 30;
    const today = new Date();
    let activeDays = 0;

    for (let i = 0; i < windowDays; i++) {
        const day = new Date(today);
        day.setDate(day.getDate() - i);
        if (isStreakDay(dateString(day))) activeDays++;
    }

    return {
        activeDays: activeDays,
        windowDays: windowDays,
        percent: Math.round((activeDays / windowDays) * 100)
    };
}

// ============================================
// HEADER
// ============================================
function updateXPHeader() {
    const xpEl = document.getElementById('header-xp');
    if (xpEl) xpEl.textContent = xpData.total + ' XP';

    const activities = getDailyActivities();

    const listEl = document.getElementById('daily-activities');
    if (listEl) {
        listEl.innerHTML = activities.list.map(activity => {
            // A partial count is more use than a cross, but only where the
            // goal is big enough for progress to mean anything.
            const mark = activity.done ? '✓'
                : activity.goal > 1 ? activity.count + '/' + activity.goal
                : '✗';
            const iconHtml = (typeof Art !== 'undefined') ? Art.icon(activity.icon) : '';
            return `
                <span class="daily-activity${activity.done ? ' is-done' : ''}">
                    <span class="daily-activity-icon">${iconHtml}</span>
                    <span class="daily-activity-label">${activity.label}</span>
                    <span class="daily-activity-mark">${mark}</span>
                </span>
            `;
        }).join('');
    }

    const streakEl = document.getElementById('header-streak');
    if (streakEl) {
        const streak = getStreak();
        const perfect = getPerfectDays();
        const parts = [];

        // No flame, no star: the words already say it, and this line now sits
        // on Home among line-drawn marks where a colour emoji is the loudest
        // thing on the screen.
        parts.push(streak > 0 ? streak + '-day streak' : 'No streak yet');
        if (perfect > 0) parts.push(perfect + ' perfect');

        // Ink, not accent. On Home the accent already marks the one live
        // thing — the lesson to continue — and a second one here would make
        // the learner choose between two claims on the same signal.
        streakEl.textContent = parts.join(' · ');
        streakEl.style.color = streak > 0 ? 'var(--text)' : 'var(--muted)';
    }
}
