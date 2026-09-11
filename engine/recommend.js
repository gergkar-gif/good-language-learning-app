// ============================================
// RECOMMEND — grammar-skill lookup primitives
// ============================================
// Low-level "given a unit/lesson, which grammar-index skill does it teach"
// helpers, reused independently by engine/home.js's post-unit practice
// nudge and engine/lessons.js's lesson-complete labeling — a different
// purpose (labeling a specific unit/lesson) than ranking a recommendation.
// The actual "what should this learner practice right now" decision (weak/
// recent grammar skill, weak vocabulary words) moved to
// engine/recommendationEngine.js as part of the Learner model &
// personalized path roadmap initiative's step 3 — see that file's header
// comment.

const Recommend = (function () {
    'use strict';

    // The exact exercises-file path a lesson id resolves to — same
    // level/rest split loadLesson() uses in engine/lessons.js.
    function exerciseRefFor(lessonId) {
        const parts = lessonId.replace(/^lesson\./, '').split('.');
        const level = parts[0];
        const rest = parts.slice(1).join('-');
        return `exercises/${level}/${level}-${rest}-ex.json`;
    }

    async function _grammarIndex() {
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') return null;
        try {
            return await Content.json(Lang.content('indexes/grammar-index.json'));
        } catch (error) {
            return null;
        }
    }

    // The grammar concept a unit leans on most, read from the same
    // teaches-tag index Workshop's Grammar Driller already builds its
    // skill list from — no new content or index needed. Ties a unit to
    // a skill by matching that skill's exercise refs against the unit's
    // own lesson ids; the most frequent match wins. Returns null (not
    // "mixed") when nothing matches.
    async function unitSkillFor(unit) {
        const index = await _grammarIndex();
        if (!index) return null;

        const refs = new Set((unit.lessons || []).map(l => exerciseRefFor(l.id)));
        const counts = {};
        Object.keys(index.bySkill || {}).forEach(skill => {
            index.bySkill[skill].forEach(entry => {
                if (refs.has(entry.ref)) counts[skill] = (counts[skill] || 0) + 1;
            });
        });

        const ranked = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
        return ranked[0] || null;
    }

    // The grammar concept ONE lesson teaches, not a whole unit — for the
    // lesson-complete screen's "Quick Reinforce" mini-game, which should
    // scope to exactly what was just taught, not the other lessons in the
    // same unit unitSkillFor() would also pull in. Same ref-matching idea,
    // narrowed to a single lesson's own exercise file.
    async function lessonSkillFor(lessonId) {
        const index = await _grammarIndex();
        if (!index) return null;

        const ref = exerciseRefFor(lessonId);
        const counts = {};
        Object.keys(index.bySkill || {}).forEach(skill => {
            index.bySkill[skill].forEach(entry => {
                if (entry.ref === ref) counts[skill] = (counts[skill] || 0) + 1;
            });
        });

        const ranked = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
        return ranked[0] || null;
    }

    return {
        unitSkillFor: unitSkillFor,
        lessonSkillFor: lessonSkillFor,
        exerciseRefFor: exerciseRefFor
    };
})();
