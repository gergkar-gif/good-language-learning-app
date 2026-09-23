// ============================================
// RECYCLE BLOCK
// ============================================
// Grammar and skills are reviewed by resurfacing exercises from lessons the
// learner has already completed, on an SM-2-shaped curve (ease grows/shrinks
// the same way engine/srs.js's vocabulary deck does) but keyed by exercise
// id instead of a lemma, and scheduled in app OPENS rather than wall-clock
// time — see below. See content/es/guides/a1-srs-srategy.md.
//
// The vocabulary deck's "again" reschedules a card a fixed number of
// minutes out (SRS_CONFIG.AGAIN_MINUTES), which works when hundreds of
// other due cards dilute it. A recycle pool for one grammar point can be a
// handful of exercises, so a real-time "due in 1 minute" never stops being
// due — the same miss would keep winning that concept's one recycle slot in
// every lesson taken afterward, no matter how many days passed. Counting in
// app opens instead fixes that at the source: a miss comes back next time
// the learner opens the app (never mid-session), and opening the app five
// times counts as five spaced attempts, not one instant that time forgot.
const recycleKey = () => Lang.key('recycleSchedule');

function loadRecycleSchedule() {
    try {
        return JSON.parse(localStorage.getItem(recycleKey()) || '{}');
    } catch (e) {
        return {};
    }
}

function saveRecycleSchedule(schedule) {
    localStorage.setItem(recycleKey(), JSON.stringify(schedule));
}

function currentAppOpen() {
    return (typeof AppOpens !== 'undefined') ? AppOpens.current() : 0;
}

function newRecycleCardSchedule() {
    return { reviews: 0, ease: SRS_CONFIG.START_EASE, interval: 0, lastOpen: 0, dueAtOpen: 0, lapses: 0, leech: false };
}

// Cards saved by an older, date-based version of this schedule (or missing
// fields entirely) just come up due immediately, same as a brand-new card —
// there is nothing else meaningful to infer an "opens" count from.
function normalizeRecycleCard(card) {
    if (typeof card.reviews !== 'number' || !(card.reviews >= 0)) card.reviews = 0;
    card.ease = (typeof card.ease === 'number' && isFinite(card.ease))
        ? Math.min(SRS_CONFIG.MAX_EASE, Math.max(SRS_CONFIG.MIN_EASE, card.ease))
        : SRS_CONFIG.START_EASE;
    if (typeof card.interval !== 'number' || !isFinite(card.interval) || card.interval < 0) card.interval = 0;
    if (typeof card.dueAtOpen !== 'number' || !isFinite(card.dueAtOpen)) card.dueAtOpen = 0;
    if (typeof card.lastOpen !== 'number' || !isFinite(card.lastOpen)) card.lastOpen = 0;
    if (typeof card.lapses !== 'number' || !(card.lapses >= 0)) card.lapses = 0;
    card.leech = card.lapses >= SRS_CONFIG.LEECH_THRESHOLD;
    return card;
}

function recycleCard(schedule, id) {
    if (!schedule[id]) schedule[id] = newRecycleCardSchedule();
    return normalizeRecycleCard(schedule[id]);
}

// Same growth shape as srs.js's previewSchedule, but every unit is an app
// open instead of a day, and "again" always resolves to "next open" — never
// due again inside the same sitting the learner just missed it in.
function scheduleRecycleCard(card, rating, currentOpen) {
    normalizeRecycleCard(card);
    const ease = Math.min(SRS_CONFIG.MAX_EASE, Math.max(SRS_CONFIG.MIN_EASE, card.ease + (SRS_CONFIG.EASE_DELTA[rating] || 0)));

    if (rating === 'again') {
        card.ease = ease;
        card.interval = 0;
        card.reviews = 0;
        card.lastOpen = currentOpen;
        card.dueAtOpen = currentOpen + 1;
        card.lapses = (card.lapses || 0) + 1;
        card.leech = card.lapses >= SRS_CONFIG.LEECH_THRESHOLD;
        return card;
    }

    let interval;
    if (card.reviews === 0) {
        interval = SRS_CONFIG.FIRST_INTERVAL[rating];
    } else if (card.reviews === 1) {
        interval = SRS_CONFIG.SECOND_INTERVAL[rating];
    } else {
        const elapsed = Math.max(0, currentOpen - card.lastOpen) || card.interval;
        const base = Math.max(0, Math.min(card.interval, elapsed));
        const multiplier = rating === 'hard' ? SRS_CONFIG.HARD_MULTIPLIER
                         : rating === 'easy' ? ease * SRS_CONFIG.EASY_BONUS
                         : ease;
        interval = Math.max(card.interval, base * multiplier);
    }

    card.ease = ease;
    card.interval = Math.max(1, Math.round(interval));
    card.reviews += 1;
    card.lastOpen = currentOpen;
    card.dueAtOpen = currentOpen + card.interval;
    return card;
}

// Same order curriculum.js draws the level list in — duplicated rather than
// shared because these are separate classic scripts with no module system,
// and this list changes about as often as CEFR itself does.
const RECYCLE_LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1'];

// Every teaches-tagged exercise the learner is eligible to see again:
// earlier completed lessons in this lesson's own level, plus — since a
// learner starting A2 has already finished A1 — every completed lesson in
// the level directly below it. One hop back, not the whole stack: B1 reaches
// into A2, not all the way to A1. Reading exercises are never tagged and so
// never appear here — they only make sense right after their own story.
async function collectRecyclePool(lesson) {
    const data = window._curriculumData;
    if (!data) return [];

    const levelKey = (lesson.level || '').toUpperCase();
    const levelData = data.levels && data.levels[levelKey];
    if (!levelData) return [];

    const progress = (typeof getProgress === 'function') ? getProgress() : {};
    const pool = [];

    // Recent completed lessons first: 3 picks don't need scanning 40+ historical lessons
    const lessons = (levelData.units || []).flatMap(u => u.lessons || []);
    const index = lessons.findIndex(l => l.id === lesson.id);
    if (index > 0) {
        const completedCurrent = lessons.slice(0, index).filter(l => progress[l.id]);
        // Focus on the most recent 8 completed lessons in the level
        await addRecycleExercises(pool, completedCurrent.slice(-8));
    }

    const prevLevelKey = RECYCLE_LEVEL_ORDER[RECYCLE_LEVEL_ORDER.indexOf(levelKey) - 1];
    const prevLevelData = prevLevelKey && data.levels[prevLevelKey];
    if (prevLevelData && pool.length < 15) {
        const prevLessons = (prevLevelData.units || []).flatMap(u => u.lessons || []);
        const completedPrev = prevLessons.filter(l => progress[l.id]);
        // Top up with up to 5 most recent completed lessons from previous level if needed
        await addRecycleExercises(pool, completedPrev.slice(-5));
    }

    return pool;
}

// loadLesson() itself is deliberately uncached — startLesson() mutates the
// object it returns (attaches a fresh `.steps` array built from that
// lesson's own current progress/recycle picks), so sharing one cached copy
// across calls would leak one screen's steps into another. This module
// never touches `.steps`, only ever reads `.sections`, so it's safe to
// cache the raw JSON here on its own — and it needs to: without this, every
// lesson load re-fetched every previously-completed lesson from scratch to
// rebuild the pool, which scales with total lessons completed and was
// measured taking 10-30s deep into a course with hundreds of lessons.
// Caches the promise itself, not just its resolved value — the lessons
// below are now fetched concurrently via Promise.all, and the "previous
// level" and "current level" batches can reference the same lesson id
// across calls. Populating the cache synchronously, before any await,
// means concurrent callers for the same id all await one real fetch
// instead of each seeing an empty cache and firing its own.
const _lessonJsonCache = {};
function _loadLessonCached(lessonId) {
    if (!(lessonId in _lessonJsonCache)) {
        _lessonJsonCache[lessonId] = loadLesson(lessonId);
    }
    return _lessonJsonCache[lessonId];
}

async function addRecycleExercises(pool, lessonEntries) {
    // One await per lesson, all in flight together, rather than one at a
    // time — loadContent()'s own contentCache already makes any exercise
    // file's second fetch free, so the only real cost left after the lesson
    // cache above is network latency, which parallelizing collapses from
    // "sum of every round trip" to "the one slowest round trip."
    const lessons = await Promise.all(lessonEntries.map(entry => _loadLessonCached(entry.id)));

    const exerciseGroupSections = [];
    for (const earlierLesson of lessons) {
        if (!earlierLesson) continue;
        for (const section of earlierLesson.sections || []) {
            if (section.type === 'exercise-group') exerciseGroupSections.push(section);
        }
    }

    // Same reasoning as the lessons above: a cold cache (first lesson of a
    // fresh page load) means every one of these is a real network fetch,
    // and there can be hundreds by the time a course is mostly complete —
    // fire them all at once rather than one at a time.
    const files = await Promise.all(exerciseGroupSections.map(section => loadContent(section.ref)));

    exerciseGroupSections.forEach((section, i) => {
        const file = files[i];
        const byId = {};
        (file.exercises || []).forEach(ex => { byId[ex.id] = ex; });

        for (const id of section.exerciseRefs || []) {
            const ex = byId[id];
            if (ex && ex.teaches && ex.teaches.length) pool.push(ex);
        }
    });
}

// Due cards first, then whichever have been seen least — so a course still
// gets a block from the first eligible lesson on, even though nothing is
// "due" yet the first time a concept becomes recyclable.
function pickRecycleExercises(pool, count) {
    if (!pool.length) return [];
    const schedule = loadRecycleSchedule();
    const currentOpen = currentAppOpen();

    const scored = pool.map(ex => ({ ex, card: recycleCard(schedule, ex.id) }));
    scored.sort((a, b) => {
        const aDue = a.card.dueAtOpen <= currentOpen;
        const bDue = b.card.dueAtOpen <= currentOpen;
        if (aDue !== bDue) return aDue ? -1 : 1;
        return (a.card.reviews - b.card.reviews) || (a.card.dueAtOpen - b.card.dueAtOpen);
    });

    // No two picks testing the same concept, so a short block still covers
    // ground rather than drilling one thing three times.
    const seenIds = new Set();
    const seenConcepts = new Set();
    const picks = [];
    for (const { ex } of scored) {
        if (seenIds.has(ex.id)) continue;
        if (picks.length && (ex.teaches || []).some(t => seenConcepts.has(t))) continue;
        picks.push(ex);
        seenIds.add(ex.id);
        (ex.teaches || []).forEach(t => seenConcepts.add(t));
        if (picks.length >= count) break;
    }
    // The concept-diversity pass can leave the block short when the pool is
    // small (early lessons); top it up rather than ship fewer than asked.
    if (picks.length < count) {
        for (const { ex } of scored) {
            if (picks.length >= count) break;
            if (seenIds.has(ex.id)) continue;
            picks.push(ex);
            seenIds.add(ex.id);
        }
    }
    return picks;
}

function recordRecycleOutcome(id, rating) {
    const schedule = loadRecycleSchedule();
    const card = recycleCard(schedule, id);
    scheduleRecycleCard(card, rating, currentAppOpen());
    saveRecycleSchedule(schedule);
}

window.Recycle = {
    collectPool: collectRecyclePool,
    pick: pickRecycleExercises,
    record: recordRecycleOutcome
};
