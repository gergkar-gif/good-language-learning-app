// ============================================
// RECOMMENDATION ENGINE — "one strong recommendation, occasional secondary"
// ============================================
// Step 3 of the Learner model & personalized path roadmap initiative, built
// on step 1 (engine/learnerPath.js, position) and step 2
// (engine/learnerModel.js, four-state grammar/vocab competence).
//
// `primary` is the same three candidates engine/home.js already computed
// separately (a post-unit practice nudge, a per-lesson mini-game offer, or
// the plain "keep going" continue card), now centralized behind one call
// with the SAME precedence Home always used — formalized, not re-ranked.
// Re-ranking Home's hierarchy with LearnerModel evidence is explicitly a
// later, separate roadmap step (step 4, "Simplify Home experience
// hierarchy," which the roadmap itself lists as blocked by this one) — not
// this step's job.
//
// `secondary` is a flat list of driller-launchable candidates: grammar
// (weak/recent skill), vocabulary (weak words) — both absorbed from
// engine/recommend.js's old recommend(), which owned this decision before
// this module existed — and a generic `driller` candidate for any of the
// seven drillers engine/drillHistory.js tracks (Verb Speed, Translation,
// Listening, and the four Hungarian-specific drillers). Since step 6, the
// driller-tracking metadata itself lives in engine/learnerModel.js
// (weakDrillers()) alongside weakSkills()/weakWords() — this module only
// ranks/presents it, same as the other two.
//
// Also owns the shared "what's next" action every driller's results screen
// mounts (mountNextAction()) — the roadmap's other named gap: every
// driller's results screen used to be a closed loop with no forward action.

const RecommendationEngine = (function () {
    'use strict';

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    function humanizeSkill(id) {
        return String(id || '').replace(/[-_]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    }

    // A `secondary` candidate's button label — shared by Home's own
    // secondary tier and Workshop's "Recommended for you" card, so the two
    // surfaces can't drift on how a candidate reads.
    function secondaryLabel(candidate) {
        if (candidate.kind === 'grammar') return `Grammar: ${humanizeSkill(candidate.skill)}`;
        if (candidate.kind === 'vocabulary') return `Vocabulary (${candidate.words.length})`;
        if (candidate.kind === 'driller') return candidate.title;
        return '';
    }

    // Launches a `secondary` candidate — same shared surface as above, so
    // both callers route identically.
    function openSecondary(candidate) {
        if (!candidate || typeof Workshop === 'undefined') return;
        if (candidate.kind === 'grammar') Workshop.open('grammar', { skill: candidate.skill });
        else if (candidate.kind === 'vocabulary') Workshop.open('vocabulary', { words: candidate.words });
        else if (candidate.kind === 'driller') Workshop.open(candidate.drillerId);
    }

    // ----------------------------------------
    // DISMISSAL STATE (moved from engine/home.js)
    // ----------------------------------------
    // A unit's practice nudge, once resolved (practised or skipped), never
    // comes back for that unit. Persisted per course via Lang.key(), same
    // as before this moved.
    function dismissedUnitsKey() {
        return Lang.key('unitPracticeDismissed');
    }

    function dismissedUnits() {
        try {
            return JSON.parse(localStorage.getItem(dismissedUnitsKey()) || '[]');
        } catch (error) {
            return [];
        }
    }

    function dismissUnit(unitId) {
        const list = dismissedUnits();
        if (!list.includes(unitId)) {
            list.push(unitId);
            try { localStorage.setItem(dismissedUnitsKey(), JSON.stringify(list)); }
            catch (error) { /* private browsing with storage disabled — the nudge just won't stay dismissed */ }
        }
    }

    // A mini-game offer, once resolved (played or skipped), never comes
    // back for that lesson.
    function miniGameDismissedKey() {
        return Lang.key('miniGameDismissed');
    }

    function miniGameDismissed(lessonId) {
        try {
            const seen = JSON.parse(localStorage.getItem(miniGameDismissedKey()) || '{}');
            return !!seen[lessonId];
        } catch (error) {
            return false;
        }
    }

    function dismissMiniGame(lessonId) {
        try {
            const seen = JSON.parse(localStorage.getItem(miniGameDismissedKey()) || '{}');
            seen[lessonId] = true;
            localStorage.setItem(miniGameDismissedKey(), JSON.stringify(seen));
        } catch (error) {
            // Private browsing with storage disabled — same tradeoff other
            // dismissal state already accepts.
        }
    }

    // ----------------------------------------
    // GRAMMAR + VOCABULARY CANDIDATE (absorbed from engine/recommend.js)
    // ----------------------------------------
    // Weak — LearnerModel's ranked signal. Recent — no weak signal exists
    // yet for grammar, so fall back to whatever grammar concept the most
    // recently completed lesson's unit leaned on most. Vocabulary has no
    // "recent" fallback here; a caller that also knows which lesson just
    // finished can fall back to that lesson's own new words itself.
    async function _grammarVocabCandidate() {
        const topSkill = (await LearnerModel.weakSkills(1))[0];
        let skill = topSkill ? topSkill.skillId : null;
        let skillReason = skill ? 'weak' : null;
        let unit = null, levelKey = null;

        if (!skill) {
            const lessonId = LearnerPath.lastCompletedLessonId();
            const found = lessonId ? LearnerPath.unitFor(lessonId) : null;
            if (found) {
                skill = await Recommend.unitSkillFor(found.unit);
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

    // ----------------------------------------
    // PRIMARY CANDIDATES (moved from engine/home.js, same bodies)
    // ----------------------------------------

    // Home's post-unit practice beat: the last lesson completed was the
    // last lesson in its unit, that unit hasn't already been resolved, and
    // there's an actual grammar skill to point Workshop at.
    async function _practiceNudge() {
        const lessonId = LearnerPath.lastCompletedLessonId();
        if (!lessonId) return null;

        const found = LearnerPath.unitFor(lessonId);
        if (!found) return null;

        const { levelKey, unit } = found;
        const lessons = unit.lessons || [];
        const last = lessons[lessons.length - 1];
        if (!last || last.id !== lessonId) return null; // not the unit's last lesson

        if (dismissedUnits().includes(unit.id)) return null;

        const skill = await Recommend.unitSkillFor(unit);
        if (!skill) return null;

        return { levelKey, unit, skill };
    }

    // Home's per-lesson counterpart: a "Quick Reinforce" mini-game offered
    // after any lesson, not just a unit's last one. Never computed if a
    // practice nudge already applies — the caller checks that first.
    async function _miniGameNudge() {
        const lessonId = LearnerPath.lastCompletedLessonId();
        if (!lessonId || miniGameDismissed(lessonId)) return null;

        const rec = await _grammarVocabCandidate();

        let words = (rec && rec.words.length) ? rec.words : [];
        let wordsReason = words.length ? 'weak' : null;
        if (!words.length && typeof loadLesson === 'function' && typeof collectLessonVocabulary === 'function') {
            const lesson = await loadLesson(lessonId);
            if (lesson) words = await collectLessonVocabulary(lesson);
            wordsReason = words.length ? 'recent' : null;
        }

        const skill = rec ? rec.skill : null;
        if (!skill && !words.length) return null;
        return {
            lessonId,
            skill,
            skillReason: rec ? rec.skillReason : null,
            words,
            wordsReason
        };
    }

    // ----------------------------------------
    // DRILLER SIGNAL
    // ----------------------------------------
    // The driller-classification metadata (which drillers to track, their
    // curriculum-unlock gates, availability by language) moved to
    // engine/learnerModel.js in step 6, alongside grammar/vocabulary's
    // weakSkills()/weakWords() — this module only ranks/presents what
    // LearnerModel already found weak, the same way it already does for
    // grammar and vocabulary via _grammarVocabCandidate().
    function _drillerCandidates() {
        if (typeof LearnerModel === 'undefined') return [];
        return LearnerModel.weakDrillers().map(c => Object.assign({ kind: 'driller', reason: 'weak' }, c));
    }

    // ----------------------------------------
    // THE ENGINE
    // ----------------------------------------

    async function recommend() {
        const nudge = await _practiceNudge();
        const mini = nudge ? null : await _miniGameNudge();
        const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;

        let primary;
        if (nudge) primary = Object.assign({ kind: 'unit-nudge' }, nudge);
        else if (mini) primary = Object.assign({ kind: 'mini-game' }, mini);
        else primary = { kind: 'continue', step };

        const gv = await _grammarVocabCandidate();
        const secondary = [];
        if (gv && gv.skill) secondary.push({ kind: 'grammar', skill: gv.skill, reason: gv.skillReason });
        if (gv && gv.words.length) secondary.push({ kind: 'vocabulary', words: gv.words, reason: gv.wordsReason });
        _drillerCandidates().forEach(c => secondary.push(c));

        return { primary, secondary: secondary.slice(0, 3) };
    }

    // ----------------------------------------
    // PIECE C: SHARED "WHAT'S NEXT" RESULTS-SCREEN ACTION
    // ----------------------------------------

    function _nextActionHtml(primary) {
        let title, sub;
        if (primary.kind === 'continue') {
            if (!primary.step) return ''; // course finished — nothing to suggest
            title = primary.step.kind === 'test'
                ? `${primary.step.level} level test`
                : primary.step.lesson.title;
            sub = 'Keep going with your course';
        } else if (primary.kind === 'unit-nudge') {
            title = `Practise: ${humanizeSkill(primary.skill)}`;
            sub = `A quick round on what "${primary.unit.title || 'that unit'}" just taught`;
        } else if (primary.kind === 'mini-game') {
            title = primary.skill
                ? `Grammar: ${humanizeSkill(primary.skill)}`
                : `Vocabulary (${primary.words.length})`;
            sub = "Reinforce what you just learned";
        } else {
            return '';
        }

        return `
            <div class="wk-next-action">
                <span class="wk-next-eyebrow">What's next?</span>
                <button class="wk-next-btn" data-next-action="1">${esc(title)} →</button>
                <span class="wk-next-sub">${esc(sub)}</span>
            </div>
        `;
    }

    function _routeTo(primary) {
        if (primary.kind === 'continue') {
            if (!primary.step) return;
            if (primary.step.kind === 'test') {
                if (typeof LevelTest !== 'undefined') LevelTest.open(primary.step.level);
            } else if (typeof startLesson === 'function') {
                startLesson(primary.step.lesson.id);
            }
        } else if (primary.kind === 'unit-nudge') {
            dismissUnit(primary.unit.id);
            if (typeof Workshop !== 'undefined') Workshop.open('grammar', { skill: primary.skill });
        } else if (primary.kind === 'mini-game') {
            dismissMiniGame(primary.lessonId);
            if (primary.skill && typeof Workshop !== 'undefined') {
                const count = (typeof QUICK_REINFORCE_COUNT === 'number') ? QUICK_REINFORCE_COUNT : 5;
                Workshop.open('grammar', { skill: primary.skill, count });
            } else if (primary.words && primary.words.length && typeof Workshop !== 'undefined') {
                Workshop.open('vocabulary', { words: primary.words });
            }
        }
    }

    // Mounted at the end of any driller's results screen. `options.excludeDrillerId`
    // stops a driller recommending re-entry into itself — a no-op under
    // today's shape (primary never resolves to a driller candidate, only
    // secondary does) but kept as a real guard in case that ever changes,
    // rather than assumed away.
    async function mountNextAction(container, options) {
        if (!container) return;

        // Step 5 (Time-Based Sessions): while a StudyPlan is in progress,
        // every driller/lesson/review results screen's "what's next" should
        // point back into the plan's own queue, not a fresh, unrelated
        // generic recommendation.
        if (typeof StudyPlan !== 'undefined' && StudyPlan.isActive()) {
            if (typeof StudyPlanRunner !== 'undefined') StudyPlanRunner.mountNextAction(container);
            return;
        }

        const opts = options || {};
        let rec;
        try {
            rec = await recommend();
        } catch (error) {
            return;
        }
        if (!rec || !rec.primary) return;
        if (rec.primary.kind === 'driller' && rec.primary.drillerId === opts.excludeDrillerId) return;

        const html = _nextActionHtml(rec.primary);
        if (!html) return;

        container.insertAdjacentHTML('beforeend', html);
        const btn = container.querySelector('[data-next-action]');
        if (btn) btn.addEventListener('click', () => _routeTo(rec.primary));
    }

    return {
        recommend,
        mountNextAction,
        dismissUnit,
        dismissMiniGame,
        secondaryLabel,
        openSecondary,
        grammarVocabCandidate: _grammarVocabCandidate
    };
})();
