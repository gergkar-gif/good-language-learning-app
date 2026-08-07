// ============================================
// PROGRESS ENGINE
// ============================================

const PROGRESS_KEY = "spanishMastery_progress";

function getProgress() {
    try {
        return JSON.parse(localStorage.getItem(PROGRESS_KEY) || "{}");
    } catch (e) {
        console.warn("Failed to parse progress from localStorage:", e);
        return {};
    }
}

function saveProgress(progress) {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
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

function getLevelProgress(levelKey) {
    const data = window._curriculumData;

    if (!data || !data.levels || !data.levels[levelKey]) {
        return {
            completed: 0,
            total: 0
        };
    }

    const lessons = data.levels[levelKey].lessons || [];
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
    isLessonComplete,
    getLevelProgress
};