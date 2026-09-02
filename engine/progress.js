// ============================================
// PROGRESS ENGINE
// ============================================

// Scoped per course: a Hungarian lesson carries the same id as its Spanish
// counterpart, so one shared map would mark both complete at once.
const progressKey = () => Lang.key('progress');

function getProgress() {
    try {
        return JSON.parse(localStorage.getItem(progressKey()) || "{}");
    } catch (e) {
        console.warn("Failed to parse progress from localStorage:", e);
        return {};
    }
}

function saveProgress(progress) {
    localStorage.setItem(progressKey(), JSON.stringify(progress));
}

// Returns true only on the first completion. XP is awarded by the caller
// (finishLesson) so that completion and reward live in one place.
function markLessonComplete(lessonId) {
    const progress = getProgress();

    if (progress[lessonId]) return false;

    progress[lessonId] = {
        completedAt: new Date().toISOString()
    };

    saveProgress(progress);

    if (typeof renderCurriculum === "function") {
        renderCurriculum();
    }

    return true;
}

function isLessonComplete(lessonId) {
    return !!getProgress()[lessonId];
}

// Bulk-completes every lesson in a level at once — used when a learner
// tests out of a level via LevelTest's jump-ahead threshold rather than
// working through each lesson individually. Batches the localStorage
// write and the curriculum re-render into one each, unlike calling
// markLessonComplete() lesson-by-lesson, since this can touch dozens of
// lessons in a single call. Awards no XP: level tests have never carried
// an XP reward (see engine/leveltest.js), and paying out a whole level's
// worth of per-lesson XP for one test would reward the test itself
// rather than the work XP is meant to measure. Returns the ids newly
// marked complete, so the caller can report how many that actually was.
function markLevelComplete(levelKey) {
    const data = window._curriculumData;
    if (!data || !data.levels || !data.levels[levelKey]) return [];

    const lessons = (data.levels[levelKey].units || []).flatMap(u => u.lessons || []);
    const progress = getProgress();
    const newlyCompleted = [];

    // Each entry gets its own millisecond rather than one shared
    // new Date().toISOString() call — a tight loop over dozens/hundreds
    // of lessons can otherwise stamp many of them with the exact same
    // millisecond, and lastCompletedLessonId() (engine/home.js) breaks a
    // tie by picking whichever was inserted FIRST, i.e. the earliest
    // lesson in the level — the opposite of "most recently completed."
    // Spacing them out (curriculum order, so the level's last lesson
    // reads as the latest) keeps that resolvable to a real answer instead
    // of an accidental tie (found via bug sweep, 2026-09-02).
    const baseTime = Date.now();
    lessons.forEach((l, i) => {
        if (!progress[l.id]) {
            progress[l.id] = { completedAt: new Date(baseTime + i).toISOString(), viaLevelTest: true };
            newlyCompleted.push(l.id);
        }
    });

    if (newlyCompleted.length) {
        saveProgress(progress);
        if (typeof renderCurriculum === 'function') renderCurriculum();
    }

    return newlyCompleted;
}

function getLevelProgress(levelKey) {
    const data = window._curriculumData;

    if (!data || !data.levels || !data.levels[levelKey]) {
        return {
            completed: 0,
            total: 0
        };
    }

    const lessons = (data.levels[levelKey].units || []).flatMap(u => u.lessons || []);
    const progress = getProgress();

    return {
        completed: lessons.filter(l => progress[l.id]).length,
        total: lessons.length
    };
}

window.SpanishMastery = window.SpanishMastery || {};

window.SpanishMastery.progress = {
    getProgress,
    saveProgress,
    markLessonComplete,
    markLevelComplete,
    isLessonComplete,
    getLevelProgress
};