// ============================================
// RECYCLE BLOCK
// ============================================
// Grammar and skills are reviewed by resurfacing exercises from lessons the
// learner has already completed, scheduled with the same SM-2 curve as the
// vocabulary deck (engine/srs.js) but keyed by exercise id instead of a
// lemma. See content/es/guides/a1-srs-srategy.md.

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

function recycleCard(schedule, id) {
    if (!schedule[id]) schedule[id] = newCardSchedule();
    return normalizeCard(schedule[id]);
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

    const prevLevelKey = RECYCLE_LEVEL_ORDER[RECYCLE_LEVEL_ORDER.indexOf(levelKey) - 1];
    const prevLevelData = prevLevelKey && data.levels[prevLevelKey];
    if (prevLevelData) {
        const prevLessons = (prevLevelData.units || []).flatMap(u => u.lessons || []);
        await addRecycleExercises(pool, prevLessons.filter(l => progress[l.id]));
    }

    const lessons = (levelData.units || []).flatMap(u => u.lessons || []);
    const index = lessons.findIndex(l => l.id === lesson.id);
    if (index > 0) {
        await addRecycleExercises(pool, lessons.slice(0, index).filter(l => progress[l.id]));
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
    const now = new Date();

    const scored = pool.map(ex => ({ ex, card: recycleCard(schedule, ex.id) }));
    scored.sort((a, b) => {
        const aDue = new Date(a.card.nextReview) <= now;
        const bDue = new Date(b.card.nextReview) <= now;
        if (aDue !== bDue) return aDue ? -1 : 1;
        return (a.card.reviews - b.card.reviews) || (new Date(a.card.nextReview) - new Date(b.card.nextReview));
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
    scheduleCard(card, rating, new Date());
    saveRecycleSchedule(schedule);
}

window.Recycle = {
    collectPool: collectRecyclePool,
    pick: pickRecycleExercises,
    record: recordRecycleOutcome
};
