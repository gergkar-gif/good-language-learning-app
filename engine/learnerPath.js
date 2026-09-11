// ============================================
// LEARNER PATH — "where is the learner?"
// ============================================
// Step 1 of the Learner model & personalized path roadmap initiative (see
// ROADMAP.md). One reliable source of truth for current level/unit/lesson
// position, the next curriculum step, and a last-activity timestamp — kept
// separate from curriculum position, since touching the app isn't the same
// as finishing something in it.
//
// engine/progress.js remains the low-level completion-record store
// (getProgress/markLessonComplete/isLessonComplete) — this module sits one
// layer above it and owns position computation, which used to be scattered
// across engine/recommend.js (unitFor, lastCompletedLessonId) and
// engine/home.js (nextStep and its private helpers). Consolidating fixes a
// real bug along the way: engine/curriculum.js's unit/lesson-path screens
// used to compute "current" with a simpler, independent algorithm (first
// incomplete item in curriculum order) that could disagree with Home's
// Continue card (which follows the learner forward from their last
// completed lesson) whenever someone skipped ahead or tested out of a
// level. Both now read from nextStep() here.

const LearnerPath = (function () {
    'use strict';

    // ----------------------------------------
    // COMPLETION (thin delegate — progress.js stays the store)
    // ----------------------------------------

    function isComplete(lessonId) {
        return (typeof isLessonComplete === 'function') ? isLessonComplete(lessonId) : false;
    }

    // ----------------------------------------
    // POSITION PRIMITIVES (moved verbatim from engine/recommend.js)
    // ----------------------------------------

    // Which unit (and level) a lesson id belongs to, or null if the
    // curriculum isn't loaded or the id isn't in it.
    function unitFor(lessonId) {
        const data = window._curriculumData;
        if (!data || !data.levels || !lessonId) return null;

        for (const levelKey of Object.keys(data.levels)) {
            const units = data.levels[levelKey].units || [];
            const unit = units.find(u => (u.lessons || []).some(l => l.id === lessonId));
            if (unit) return { levelKey, unit };
        }
        return null;
    }

    // The lesson most recently marked complete, by timestamp.
    function lastCompletedLessonId() {
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        let bestId = null, bestTime = -1;
        Object.keys(progress).forEach(id => {
            const t = Date.parse((progress[id] || {}).completedAt || '') || 0;
            if (t > bestTime) { bestTime = t; bestId = id; }
        });
        return bestId;
    }

    // ----------------------------------------
    // NEXT STEP (moved verbatim from engine/home.js)
    // ----------------------------------------

    // The whole course, flattened into one ordered walk — every lesson, and
    // a level-test placeholder right after each level's last lesson, in the
    // same level→unit→lesson order the app has always used. nextStep()
    // below walks this twice: once forward from wherever the learner
    // actually left off, once from the very start as a fallback.
    function courseWalk() {
        const data = window._curriculumData;
        if (!data || !data.levels) return [];
        const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1'];

        const steps = [];
        order.forEach(level => {
            const entry = data.levels[level];
            const units = (entry && entry.units) || [];
            const lessons = units.flatMap(u => u.lessons || []);
            if (!lessons.length) return;

            lessons.forEach(lesson => {
                // The unit's own title is more useful here than the level's —
                // "Greetings & Introductions" says more than "Fundamentals".
                const unit = units.find(u => (u.lessons || []).some(l => l.id === lesson.id));
                steps.push({ kind: 'lesson', level, title: (unit && unit.title) || entry.title || '', lesson });
            });
            steps.push({ kind: 'test', level, title: entry.title || '' });
        });
        return steps;
    }

    function stepIsDone(step, progress) {
        if (step.kind === 'lesson') return !!progress[step.lesson.id];
        const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(step.level) : null;
        return !!(result && result.passed);
    }

    function levelStats(level, progress) {
        const data = window._curriculumData;
        const entry = data && data.levels && data.levels[level];
        const lessons = ((entry && entry.units) || []).flatMap(u => u.lessons || []);
        return { done: lessons.filter(l => progress[l.id]).length, total: lessons.length };
    }

    function stepToResult(step, progress) {
        const stats = levelStats(step.level, progress);
        if (step.kind === 'test') {
            const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(step.level) : null;
            return { kind: 'test', level: step.level, title: step.title, result, done: stats.done, total: stats.total };
        }
        return { kind: 'lesson', level: step.level, title: step.title, lesson: step.lesson, done: stats.done, total: stats.total };
    }

    // The next thing to continue with. Follows the learner rather than the
    // course's own order: it continues forward from wherever their most
    // recently completed lesson actually sits, so clearing Unit 10 out of
    // order recommends Unit 11 next, not a snap back to Unit 1 just because
    // it's still the earliest unfinished thing overall. Only falls back to
    // sweeping from the very start of the course — the old, order-only
    // behaviour — once there's genuinely nothing left ahead, which is what
    // keeps a real gap left behind (an earlier unit never finished) from
    // being lost track of forever rather than just not being the default.
    //
    // This is the ONE canonical "current position" algorithm — every screen
    // that needs to mark something "current" (Home's Continue card,
    // curriculum.js's unit-path and lesson-path screens) should read from
    // here rather than keeping its own, simpler notion of "current".
    function nextStep() {
        const data = window._curriculumData;
        if (!data || !data.levels) return null;

        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const steps = courseWalk();
        if (!steps.length) return null;

        const lastId = lastCompletedLessonId();
        const lastIndex = lastId ? steps.findIndex(s => s.kind === 'lesson' && s.lesson.id === lastId) : -1;

        if (lastIndex !== -1) {
            for (let i = lastIndex + 1; i < steps.length; i++) {
                const step = steps[i];
                if (stepIsDone(step, progress)) continue;

                // A level test only belongs here once the whole level is
                // actually done — reaching it mid-forward-scan while an
                // earlier lesson in the SAME level is still incomplete
                // (behind the scan's start point, so never visited above)
                // means there's a real gap to go back to first. Stop
                // scanning forward and fall through to the sweep below,
                // which will find that gap rather than offering the test
                // prematurely.
                if (step.kind === 'test') {
                    const stats = levelStats(step.level, progress);
                    if (stats.done < stats.total) break;
                }

                return stepToResult(step, progress);
            }
        }

        for (let i = 0; i < steps.length; i++) {
            if (!stepIsDone(steps[i], progress)) return stepToResult(steps[i], progress);
        }

        return null;    // every lesson finished and every test passed
    }

    // ----------------------------------------
    // LAST ACTIVITY (new)
    // ----------------------------------------

    // Scoped per course, same reasoning as progress.js's progressKey() — a
    // learner studying both Spanish and Hungarian has two meaningfully
    // different "last touched" answers, unlike XP/streak (engine/xp.js),
    // which is deliberately global across courses.
    const lastActivityKey = () => Lang.key('lastActivity');

    // Called on real engagement (a lesson actually opening with content),
    // not on tab navigation or app open — see the call site in
    // engine/lessons.js's startLesson() for why that's the right spot.
    function touchActivity() {
        try {
            localStorage.setItem(lastActivityKey(), new Date().toISOString());
        } catch (error) {
            // Private browsing with storage disabled — activity just won't
            // be remembered this session, same tolerance as other
            // localStorage writes elsewhere in the app.
        }
    }

    function lastActivityAt() {
        const raw = localStorage.getItem(lastActivityKey());
        if (!raw) return null;
        const t = Date.parse(raw);
        return Number.isNaN(t) ? null : raw;
    }

    return {
        isComplete,
        unitFor,
        lastCompletedLessonId,
        nextStep,
        touchActivity,
        lastActivityAt
    };
})();
