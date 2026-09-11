// ============================================
// STUDY PLAN — time-budget allocation ("Time-Based Sessions")
// ============================================
// Step 5 of the Learner model & personalized path roadmap initiative,
// built on steps 1-3 (LearnerPath, LearnerModel, RecommendationEngine).
// Roadmap spec: "Learner picks a time budget... the app builds a finite
// session out of curriculum position, knowledge gaps, reviews due, and
// priorities, with a clear start and end. No countdown timer."
//
// Deliberately NOT named "session" anywhere in this module — every
// driller (engine/drills/*.js) already uses that word internally for one
// driller run start-to-finish (PHASE.SESSION, "Session Results",
// DrillHistory's own "session" = one run). This module's queue spans
// MULTIPLE activities across possibly-different screens, so it gets its
// own name, "plan," to keep call sites unambiguous. The roadmap's own
// "Time-Based Sessions" phrase stays as user-facing copy only.
//
// Pure allocation + queue-position logic — no DOM. engine/studyPlanRunner.js
// owns the screen/rendering; RecommendationEngine.mountNextAction() checks
// isActive() to hand off to the runner instead of computing a fresh
// generic recommendation whenever a plan is in progress.
//
// In-memory only, discarded on leaving early or on page reload — matches
// the roadmap's "a clear start and end," not a lingering to-do list.

const StudyPlan = (function () {
    'use strict';

    // Per-item-type pace. Grammar/vocabulary are untimed, thoughtful pace —
    // NOT the countdown-race pace of Verb Speed's/Grammar Driller's own
    // "Timed" mode, which this feature is deliberately not (the budget only
    // sizes the plan up front; nothing counts down while doing it).
    const SEC_PER_REVIEW = 20;
    const SEC_PER_GRAMMAR_Q = 30;
    const SEC_PER_VOCAB_WORD = 25;
    const DEFAULT_LESSON_MINUTES = 10; // fallback when estimatedMinutes is null (100% of HU, ~38% of ES)
    const LESSON_GRACE_MINUTES = 2;    // estimate slop tolerance, not a hard wall
    const TEST_MINUTES = 18;           // a level test is one indivisible block
    const reviewCapMinutes = minutes => Math.min(15, Math.round(minutes * 0.5));

    let _queue = null;   // array of plan items, or null when no plan is active
    let _index = 0;      // pointer into _queue — the current/next item
    let _minutes = null;
    let _skipped = null;
    let _startedAt = null;

    // ----------------------------------------
    // ALLOCATION
    // ----------------------------------------

    async function build(minutes) {
        const items = [];
        let remaining = minutes;
        let skipped = null;

        // 1. Reviews due — time-sensitive (deferring costs real SM-2 decay
        // the other three inputs don't have), so they get first claim on a
        // capped share of the budget, and get to absorb leftover time at
        // the end too (step 4 below) since a backlog is rarely fully
        // exhausted — avoids inventing busywork for long 45-60 min budgets.
        const due = (typeof getDueCards === 'function') ? getDueCards() : [];
        const cap = reviewCapMinutes(minutes);
        const firstPassMinutes = Math.min(due.length * SEC_PER_REVIEW / 60, cap);
        const firstPassCount = Math.floor(firstPassMinutes * 60 / SEC_PER_REVIEW);
        if (firstPassCount > 0) {
            items.push({ kind: 'review', count: firstPassCount });
            remaining -= firstPassMinutes;
        }

        // 2. Curriculum position — the spine of the plan.
        const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
        if (step && step.kind === 'lesson') {
            const est = step.lesson.estimatedMinutes || DEFAULT_LESSON_MINUTES;
            if (est <= remaining + LESSON_GRACE_MINUTES) {
                items.push({ kind: 'lesson', lessonId: step.lesson.id, title: step.lesson.title, estMinutes: est });
                remaining = Math.max(0, remaining - est);
            } else {
                skipped = { reason: 'lesson-too-long', title: step.lesson.title, estMinutes: est };
            }
        } else if (step && step.kind === 'test') {
            if (remaining >= TEST_MINUTES) {
                items.push({ kind: 'test', level: step.level, estMinutes: TEST_MINUTES });
                remaining -= TEST_MINUTES;
            } else {
                skipped = { reason: 'test-needs-bigger-block', level: step.level, estMinutes: TEST_MINUTES };
            }
        }

        // 3. Knowledge gaps — grammar and vocabulary split evenly over
        // what's left. Same "either, both, or neither" honesty as
        // RecommendationEngine: a slot with nothing to fill it is just
        // omitted, never padded with invented busywork.
        const half = remaining / 2;
        const grammarCount = Math.round(half * 60 / SEC_PER_GRAMMAR_Q);
        const vocabCount = Math.round(half * 60 / SEC_PER_VOCAB_WORD);

        let skill = null;
        if (grammarCount > 0 && typeof LearnerModel !== 'undefined') {
            const skills = await LearnerModel.weakSkills();
            if (skills.length) {
                skill = skills[0].skillId;
            } else if (typeof RecommendationEngine !== 'undefined' && RecommendationEngine.grammarVocabCandidate) {
                const gv = await RecommendationEngine.grammarVocabCandidate();
                skill = gv ? gv.skill : null;
            }
        }
        if (skill) {
            items.push({ kind: 'grammar', skill, count: grammarCount });
            remaining -= half;
        }

        const words = (vocabCount > 0 && typeof LearnerModel !== 'undefined') ? LearnerModel.weakWords(vocabCount) : [];
        if (words.length) {
            items.push({ kind: 'vocabulary', words });
            remaining -= half;
        }

        // 4. Leftover — top up reviews with whatever's left of the backlog.
        const dueRemaining = due.length - firstPassCount;
        if (remaining > 1 && dueRemaining > 0) {
            const topUp = Math.min(dueRemaining, Math.floor(remaining * 60 / SEC_PER_REVIEW));
            if (topUp > 0) {
                const existing = items.find(i => i.kind === 'review');
                if (existing) existing.count += topUp;
                else items.push({ kind: 'review', count: topUp });
            }
        }

        _queue = items;
        _index = 0;
        _minutes = minutes;
        _skipped = skipped;
        _startedAt = Date.now();

        return { minutes, items, skipped };
    }

    // ----------------------------------------
    // QUEUE POSITION
    // ----------------------------------------

    function isActive() {
        return Array.isArray(_queue) && _index < _queue.length;
    }

    function items() {
        return _queue || [];
    }

    function minutes() {
        return _minutes;
    }

    function skipped() {
        return _skipped;
    }

    function startedAt() {
        return _startedAt;
    }

    function currentIndex() {
        return _index;
    }

    function current() {
        return isActive() ? _queue[_index] : null;
    }

    // Marks the current item done and moves the pointer forward. Never
    // touches progress.js/xp.js/srs.js itself — those are written only by
    // whichever real activity (lesson, driller, review) the learner
    // actually completed, through its own unmodified code path. This just
    // advances the plan's own queue pointer.
    function advance() {
        if (isActive()) _index += 1;
        return current();
    }

    // Ends the plan without finishing it — "Leave session," no persistence,
    // matches "a clear start and end" rather than a lingering resumable to-do.
    function discard() {
        _queue = null;
        _index = 0;
        _minutes = null;
        _skipped = null;
        _startedAt = null;
    }

    return {
        build,
        isActive,
        items,
        minutes,
        skipped,
        startedAt,
        currentIndex,
        current,
        advance,
        discard
    };
})();
