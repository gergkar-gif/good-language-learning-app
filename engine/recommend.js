// ============================================
// RECOMMEND — "what should this learner practice right now"
// ============================================
// One shared signal, consumed by Home's post-unit nudge and Workshop's
// "Recommended for you" card, rather than two heuristics that could drift
// apart. Ranks two signals:
//
//   1. Weak — a grammar skill with real review history (via the SM-2
//      schedule engine/recycle.js already keeps for in-lesson recycle
//      blocks) whose average ease is low: exercises tagged with that
//      skill keep getting marked wrong or hard. This is the
//      Kwiziq-style "you're shaky here" signal.
//   2. Recent — no weak-skill signal exists yet (a new learner, or one
//      who hasn't hit enough recycle blocks for any skill to carry real
//      history), so fall back to whatever grammar concept the most
//      recently completed lesson's unit leaned on most — "practice what
//      you just learned" instead of recommending nothing.
//
// Both resolve to a grammar-index.json skill id — the same id
// GrammarDriller's `{ skill }` option already understands (see its own
// file header), so a recommendation is always directly launchable via
// Workshop.open('grammar', { skill }).

const Recommend = (function () {
    'use strict';

    // Skills with fewer than this many reviewed exercises don't carry
    // enough signal to call "weak" rather than "barely seen yet" — one
    // wrong answer on one exercise shouldn't brand a whole skill.
    const MIN_REVIEWED = 2;

    // The exact exercises-file path a lesson id resolves to — same
    // level/rest split loadLesson() uses in engine/lessons.js.
    function exerciseRefFor(lessonId) {
        const parts = lessonId.replace(/^lesson\./, '').split('.');
        const level = parts[0];
        const rest = parts.slice(1).join('-');
        return `exercises/${level}/${level}-${rest}-ex.json`;
    }

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

    // The skill with the worst average ease among skills that actually
    // carry review history — exercises the learner has met before
    // (through a lesson's own recycle block) and struggled with, not
    // just anything untested. Returns null rather than guessing when
    // nothing has enough history yet.
    async function weakestSkill() {
        if (typeof loadRecycleSchedule !== 'function') return null;
        const index = await _grammarIndex();
        if (!index) return null;
        const schedule = loadRecycleSchedule();

        let worst = null;
        Object.keys(index.bySkill || {}).forEach(skill => {
            let totalEase = 0, seen = 0;
            (index.bySkill[skill] || []).forEach(entry => {
                const cardEntry = schedule[entry.id];
                if (cardEntry && cardEntry.reviews > 0) {
                    seen++;
                    totalEase += cardEntry.ease;
                }
            });
            if (seen >= MIN_REVIEWED) {
                const avgEase = totalEase / seen;
                if (!worst || avgEase < worst.avgEase) worst = { skill, avgEase, seen };
            }
        });
        return worst ? worst.skill : null;
    }

    // The single best thing to suggest right now, with the reason so a
    // caller can word the card differently ("you've been shaky on..."
    // vs "practice what you just learned..."). Null when there is
    // nothing to suggest at all (no progress yet, no curriculum loaded).
    async function recommend() {
        const weak = await weakestSkill();
        if (weak) return { skill: weak, reason: 'weak' };

        const lessonId = lastCompletedLessonId();
        const found = lessonId ? unitFor(lessonId) : null;
        if (!found) return null;

        const skill = await unitSkillFor(found.unit);
        if (!skill) return null;
        return { skill: skill, reason: 'recent', unit: found.unit, levelKey: found.levelKey };
    }

    return {
        recommend: recommend,
        weakestSkill: weakestSkill,
        unitSkillFor: unitSkillFor,
        unitFor: unitFor,
        lastCompletedLessonId: lastCompletedLessonId,
        exerciseRefFor: exerciseRefFor
    };
})();
