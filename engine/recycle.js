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

// Every teaches-tagged exercise from lessons before `lesson`, in the same
// level, that the learner has already completed. Reading exercises are
// never tagged and so never appear here — they only make sense right after
// their own story.
async function collectRecyclePool(lesson) {
    const data = window._curriculumData;
    if (!data) return [];

    const levelKey = (lesson.level || '').toUpperCase();
    const levelData = data.levels && data.levels[levelKey];
    if (!levelData) return [];

    const lessons = (levelData.units || []).flatMap(u => u.lessons || []);
    const index = lessons.findIndex(l => l.id === lesson.id);
    if (index <= 0) return [];

    const progress = (typeof getProgress === 'function') ? getProgress() : {};
    const earlier = lessons.slice(0, index).filter(l => progress[l.id]);

    const pool = [];
    for (const entry of earlier) {
        const earlierLesson = await loadLesson(entry.id);
        if (!earlierLesson) continue;

        for (const section of earlierLesson.sections || []) {
            if (section.type !== 'exercise-group') continue;
            const file = await loadContent(section.ref);
            const byId = {};
            (file.exercises || []).forEach(ex => { byId[ex.id] = ex; });

            for (const id of section.exerciseRefs || []) {
                const ex = byId[id];
                if (ex && ex.teaches && ex.teaches.length) pool.push(ex);
            }
        }
    }
    return pool;
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
