// ============================================
// RECOMMEND — "what should this learner practice right now"
// ============================================
// One shared signal, consumed by Home's post-unit nudge, Home's per-lesson
// mini-game nudge, and Workshop's "Recommended for you" card, rather than
// several heuristics that could drift apart. Two independent halves —
// grammar and vocabulary — each ranking the same two signals:
//
//   1. Weak — engine/learnerModel.js's weakSkills()/weakWords(), the
//      Kwiziq-style "you're shaky here" signal for either half (grammar:
//      recycle-schedule ease folded with level-test misses; vocabulary:
//      srsDeck ease). Recommend no longer computes this itself — it only
//      picks the single top candidate from LearnerModel's ranked list.
//   2. Recent — no weak signal exists yet for grammar (a new learner, or
//      one who hasn't hit enough recycle blocks for any skill to carry
//      real history), so fall back to whatever grammar concept the most
//      recently completed lesson's unit leaned on most — "practice what
//      you just learned" instead of recommending nothing. Vocabulary has
//      no equivalent "recent" fallback here — a caller that also knows
//      which lesson just finished (Home, the lesson-complete screen) can
//      fall back to that lesson's own new words itself; Recommend only
//      owns the weak-word signal, the one every caller would otherwise
//      duplicate.
//
// The grammar half resolves to a grammar-index.json skill id — the same
// id GrammarDriller's `{ skill }` option already understands — so it's
// always directly launchable via Workshop.open('grammar', { skill }).
// The vocabulary half resolves to a list of words in the exact
// { lemma, translation, pos } shape VocabularyDriller's `{ words }`
// option already understands.

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

    // The single best thing to suggest right now, for grammar and
    // vocabulary independently — either half can be present, absent, or
    // both, so a caller (Workshop's card, Home's nudges) can offer
    // whichever exist rather than forcing one combined pick. `reason` on
    // each half says why, so a caller can word its card differently
    // ("you've been shaky on..." vs "practice what you just learned...").
    // Returns null only when NEITHER half has anything to suggest (no
    // progress yet, no curriculum loaded) — a caller checking `if (!rec)`
    // still works exactly as before this had a vocabulary half.
    async function recommend() {
        const topSkill = (await LearnerModel.weakSkills(1))[0];
        let skill = topSkill ? topSkill.skillId : null;
        let skillReason = skill ? 'weak' : null;
        let unit = null, levelKey = null;

        if (!skill) {
            const lessonId = LearnerPath.lastCompletedLessonId();
            const found = lessonId ? LearnerPath.unitFor(lessonId) : null;
            if (found) {
                skill = await unitSkillFor(found.unit);
                if (skill) {
                    skillReason = 'recent';
                    unit = found.unit;
                    levelKey = found.levelKey;
                }
            }
        }

        const words = LearnerModel.weakWords().map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos }));
        const wordsReason = words.length ? 'weak' : null;

        if (!skill && !words.length) return null;
        return { skill, skillReason, words, wordsReason, unit, levelKey };
    }

    return {
        recommend: recommend,
        unitSkillFor: unitSkillFor,
        lessonSkillFor: lessonSkillFor,
        exerciseRefFor: exerciseRefFor
    };
})();
