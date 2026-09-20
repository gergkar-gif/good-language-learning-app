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

    // A curated title map exists for Hungarian skill ids
    // (content/hu/indexes/grammar-titles.json, e.g. "ban-ben-in" ->
    // "-ban / -ben — In") specifically because the blind hyphen-to-space
    // regex below can't know a suffix should keep its leading dash or that
    // "in"/"to" etc. are prepositions, not words to title-case ("Ban Ben
    // In"). Spanish has no equivalent file, so that fetch fails (404) and
    // resolves to {}. Keyed by the resolved path (not a single flat
    // variable) so switching course language at runtime — no reload —
    // can't keep serving whichever language's map happened to load first;
    // humanizeSkill() re-resolves the current path on every call, cheap
    // since it's just a string join, not a fetch.
    const _grammarTitlesCache = {};
    const _scenariosCache = {};

    async function _loadScenariosForLang() {
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') return [];
        const path = Lang.content('conversation-scenarios.json');
        if (!_scenariosCache[path]) {
            const data = await Content.json(path).catch(() => null);
            _scenariosCache[path] = (data && data.scenarios) ? data.scenarios : [];
        }
        return _scenariosCache[path];
    }

    async function _scenarioForUnit(unitId) {
        if (!unitId) return null;
        try {
            const scenarios = await _loadScenariosForLang();
            return scenarios.find(s => (s.unitIds || []).includes(unitId)) || null;
        } catch (e) {
            return null;
        }
    }

    async function _ensureGrammarTitles() {
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') return {};
        const path = Lang.content('indexes/grammar-titles.json');
        if (!_grammarTitlesCache[path]) {
            _grammarTitlesCache[path] = await Content.json(path).catch(() => ({}));
        }
        return _grammarTitlesCache[path];
    }

    function humanizeSkill(id) {
        const key = String(id || '');
        const path = (typeof Lang !== 'undefined') ? Lang.content('indexes/grammar-titles.json') : null;
        const titles = path ? _grammarTitlesCache[path] : null;
        if (titles && titles[key]) return titles[key];
        return key.replace(/[-_]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    }

    // A `secondary` candidate's button label — shared by Home's own
    // secondary tier and Workshop's "Recommended for you" card, so the two
    // surfaces can't drift on how a candidate reads.
    function secondaryLabel(candidate) {
        if (candidate.kind === 'grammar') return `Grammar: ${humanizeSkill(candidate.skill)}`;
        if (candidate.kind === 'vocabulary') return `Vocabulary (${candidate.words.length})`;
        if (candidate.kind === 'speaking') return candidate.skill ? `Speaking: ${humanizeSkill(candidate.skill)}` : 'Speaking Practice';
        if (candidate.kind === 'writing') return candidate.title || 'Writing Studio';
        if (candidate.kind === 'driller') return candidate.title;
        return '';
    }

    // Launches a `secondary` candidate — same shared surface as above, so
    // both callers route identically.
    function openSecondary(candidate) {
        if (!candidate || typeof Workshop === 'undefined') return;
        if (candidate.kind === 'grammar') Workshop.open('grammar', { skill: candidate.skill });
        else if (candidate.kind === 'vocabulary') Workshop.open('vocabulary', { words: candidate.words });
        else if (candidate.kind === 'speaking') Workshop.open('speaking', { skill: candidate.skill, autoStart: true });
        else if (candidate.kind === 'writing') Workshop.open('writing', candidate.options);
        else if (candidate.kind === 'driller') Workshop.open(candidate.drillerId, candidate.options);
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
    // there's an actual grammar skill or scenario to point at.
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

        const scenario = await _scenarioForUnit(unit.id);
        if (scenario) {
            return { levelKey, unit, scenario, kind: 'scenario' };
        }

        const skill = await Recommend.unitSkillFor(unit);
        if (!skill) return null;

        return { levelKey, unit, skill, kind: 'grammar' };
    }

    // Home's per-lesson counterpart: a quick mini-game challenge offered
    // after a lesson. Varied dynamically across all 9 Workshop drillers
    // depending on the learner's previous knowledge (weaknesses first, then
    // curriculum-unlocked variety).
    async function _miniGameNudge() {
        const lessonId = LearnerPath.lastCompletedLessonId();
        if (!lessonId || miniGameDismissed(lessonId)) return null;

        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        const completedCount = (typeof LearnerPath !== 'undefined' && LearnerPath.completedCount)
            ? LearnerPath.completedCount() : 0;
        const currentLevel = (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel)
            ? LearnerPath.currentLevel() : 'A1';

        // 1. Weakness signals from LearnerModel
        const weakSkillsList = (typeof LearnerModel !== 'undefined') ? await LearnerModel.weakSkills(1) : [];
        const topWeakSkill = weakSkillsList[0] ? weakSkillsList[0].skillId : null;

        const weakWordsList = (typeof LearnerModel !== 'undefined') ? LearnerModel.weakWords() : [];
        const weakDrillersList = (typeof LearnerModel !== 'undefined') ? LearnerModel.weakDrillers() : [];
        const weakDrillerIds = new Set(weakDrillersList.map(d => d.drillerId));

        const weakProductionList = (typeof LearnerModel !== 'undefined' && LearnerModel.weakProductionSkills)
            ? LearnerModel.weakProductionSkills(1) : [];
        const topWeakProduction = weakProductionList[0] ? weakProductionList[0].skillId : null;

        // 2. Recent lesson content
        let recentSkill = null;
        let recentWords = [];
        const found = LearnerPath.unitFor(lessonId);
        if (found) {
            recentSkill = await Recommend.unitSkillFor(found.unit);
        }
        if (typeof loadLesson === 'function' && typeof collectLessonVocabulary === 'function') {
            try {
                const lesson = await loadLesson(lessonId);
                if (lesson) recentWords = await collectLessonVocabulary(lesson);
            } catch (err) {}
        }

        const candidates = [];

        // Candidate 0: Conversation Roleplay (if the lesson's unit matches a scenario)
        const unitId = found ? found.unit.id : null;
        const matchingScenario = await _scenarioForUnit(unitId);
        if (matchingScenario) {
            candidates.push({
                drillerId: 'speaking',
                title: 'Oral Roleplay',
                buttonLabel: `Roleplay: ${matchingScenario.title}`,
                blurb: `Put what you just learned into practice in a real-life dialogue: "${matchingScenario.title}".`,
                reason: 'communicative_practice',
                priority: 96,
                options: { scenarioId: matchingScenario.id, returnTab: 'home' }
            });
        }

        // Candidate 1: Targeted Grammar
        const effectiveSkill = topWeakSkill || recentSkill;
        if (effectiveSkill) {
            const isWeak = !!topWeakSkill;
            candidates.push({
                drillerId: 'grammar',
                title: 'Targeted Grammar',
                buttonLabel: `Grammar: ${humanizeSkill(effectiveSkill)} (5 questions)`,
                blurb: isWeak
                    ? "You've been shaky on this grammar concept — a quick pass will lock it in."
                    : "Reinforce the grammar you just learned, while it's fresh.",
                reason: isWeak ? 'weak' : 'fresh',
                priority: isWeak ? 100 : 50,
                options: { skill: effectiveSkill, count: 5, autoStart: true }
            });
        }

        // Candidate 2: Vocabulary Recall
        const effectiveWords = (weakWordsList.length >= 3)
            ? weakWordsList.map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos }))
            : recentWords;
        if (effectiveWords && effectiveWords.length > 0) {
            const isWeak = weakWordsList.length >= 3;
            const chosenWords = effectiveWords.slice(0, 6);
            candidates.push({
                drillerId: 'vocabulary',
                title: isWeak ? 'Tricky Words' : 'Vocabulary Recall',
                buttonLabel: `Vocabulary (${chosenWords.length} words)`,
                blurb: isWeak
                    ? "A few words need a quick refresh before they fade."
                    : "Test your recall of newly introduced words.",
                reason: isWeak ? 'weak' : 'fresh',
                priority: isWeak ? 95 : 45,
                options: { words: chosenWords, autoStart: true }
            });
        }

        // Candidate 3: Spanish Verb Speed Sprint (60s)
        if (lang.startsWith('es') && completedCount >= 3) {
            const isWeak = weakDrillerIds.has('verbs');
            candidates.push({
                drillerId: 'verbs',
                title: 'Verb Speed Sprint',
                buttonLabel: 'Verb Speed Sprint (60s)',
                blurb: "A fast-paced 60-second sprint to sharpen your conjugation reflex.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 90 : 42,
                options: { mode: 'speed', autoStart: true, duration: 60 }
            });
        }

        // Candidate 4: Hungarian Suffix Sprint
        if (lang === 'hu' && (completedCount >= 15 || LearnerPath.isComplete('lesson.a1.22'))) {
            const isWeak = weakDrillerIds.has('hu-suffix');
            candidates.push({
                drillerId: 'hu-suffix',
                title: 'Suffix Sprint',
                buttonLabel: 'Suffix Sprint (5 questions)',
                blurb: "Practice plurals, possession, and case endings with quick feedback.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 90 : 42,
                options: { autoStart: true, count: 5 }
            });
        }

        // Candidate 5: Hungarian Prefix Sprint
        if (lang === 'hu' && (currentLevel !== 'A1' || LearnerPath.isComplete('lesson.a2.01'))) {
            const isWeak = weakDrillerIds.has('hu-prefix');
            candidates.push({
                drillerId: 'hu-prefix',
                title: 'Prefix Sprint',
                buttonLabel: 'Prefix Sprint (5 questions)',
                blurb: "Master verbal prefixes and directional shifts in 5 quick questions.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 90 : 40,
                options: { autoStart: true, count: 5 }
            });
        }

        // Candidate 6: Hungarian Verb Driller
        if (lang === 'hu' && completedCount >= 8) {
            const isWeak = weakDrillerIds.has('hu-verb');
            candidates.push({
                drillerId: 'hu-verb',
                title: 'Hungarian Verbs',
                buttonLabel: 'Verb Forms (5 questions)',
                blurb: "Test definite and indefinite conjugations across Hungarian stems.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 90 : 38,
                options: { autoStart: true, count: 5 }
            });
        }

        // Candidate 7: Hungarian Morphology Driller
        if (lang === 'hu' && (completedCount >= 25 || LearnerPath.isComplete('lesson.a1.51'))) {
            const isWeak = weakDrillerIds.has('hu-morphology');
            candidates.push({
                drillerId: 'hu-morphology',
                title: 'Morphology Puzzle',
                buttonLabel: 'Morphology (5 questions)',
                blurb: "Deconstruct complex agglutinative words into root and affixes.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 90 : 36,
                options: { autoStart: true, count: 5 }
            });
        }

        // Candidate 8: Fast Translation (intermediate or >= 10 lessons)
        if (completedCount >= 10 || currentLevel !== 'A1') {
            const isWeak = weakDrillerIds.has('translation');
            const targetLang = (typeof Lang !== 'undefined') ? Lang.name() : 'the target language';
            candidates.push({
                drillerId: 'translation',
                title: 'Fast Translation',
                buttonLabel: 'Fast Translation (5 sentences)',
                blurb: `Translate 5 rapid sentences, alternating between English and ${targetLang}.`,
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 88 : 35,
                options: { autoStart: true, count: 5, level: currentLevel.toLowerCase(), direction: 'alternate' }
            });
        }

        // Candidate 9: Listening / Audio Decode
        if (completedCount >= 5) {
            const isWeak = weakDrillerIds.has('listening');
            candidates.push({
                drillerId: 'listening',
                title: 'Audio Decode',
                buttonLabel: 'Audio Decode (5 questions)',
                blurb: "Tune your ear to native speech with 5 rapid audio clips.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 88 : 35,
                options: { autoStart: true, count: 5, level: currentLevel.toLowerCase() }
            });
        }

        // Candidate 10: Speaking Driller (Oral production)
        const canSpeak = (typeof SpeechInput !== 'undefined' && SpeechInput.isSupported()) || (typeof ParlourTTS !== 'undefined' && ParlourTTS.available());
        if (canSpeak && completedCount >= 2) {
            const isWeak = !!topWeakProduction || weakDrillerIds.has('speaking');
            const targetSkill = topWeakProduction || (isWeak ? null : effectiveSkill);
            candidates.push({
                drillerId: 'speaking',
                title: isWeak ? 'Oral Recall Challenge' : 'Speak Out Loud',
                buttonLabel: targetSkill
                    ? `Speaking: ${humanizeSkill(targetSkill)} (5 sentences)`
                    : 'Speaking Sprint (5 sentences)',
                blurb: isWeak
                    ? "Turn written recall into active oral fluency with quick spoken production."
                    : "Speak sentences aloud to build real-time speech reflexes.",
                reason: isWeak ? 'weak' : 'variety',
                priority: isWeak ? 92 : 44,
                options: { autoStart: true, count: 5, level: currentLevel.toLowerCase(), skill: targetSkill || undefined }
            });
        }

        if (!candidates.length) return null;

        // Selection:
        // If there are weak candidates (priority >= 80), pick the highest priority weak candidate.
        // If all are non-weak, rotate through candidates using lessonId hash for variety.
        const weakCandidates = candidates.filter(c => c.priority >= 80);
        let primaryCandidate, altCandidate;

        if (weakCandidates.length > 0) {
            weakCandidates.sort((a, b) => b.priority - a.priority);
            primaryCandidate = weakCandidates[0];
            const others = candidates.filter(c => c.drillerId !== primaryCandidate.drillerId);
            altCandidate = others.length ? others[0] : null;
        } else {
            let hash = 0;
            for (let i = 0; i < lessonId.length; i++) {
                hash = (hash * 31 + lessonId.charCodeAt(i)) >>> 0;
            }
            const idx = hash % candidates.length;
            primaryCandidate = candidates[idx];
            altCandidate = candidates[(idx + 1) % candidates.length];
        }

        return {
            lessonId,
            challengeTitle: primaryCandidate.title,
            drillerId: primaryCandidate.drillerId,
            buttonLabel: primaryCandidate.buttonLabel,
            blurb: primaryCandidate.blurb,
            reason: primaryCandidate.reason,
            options: primaryCandidate.options,
            skill: primaryCandidate.drillerId === 'grammar' ? primaryCandidate.options.skill : null,
            skillReason: primaryCandidate.drillerId === 'grammar' ? primaryCandidate.reason : null,
            words: primaryCandidate.drillerId === 'vocabulary' ? primaryCandidate.options.words : [],
            wordsReason: primaryCandidate.drillerId === 'vocabulary' ? primaryCandidate.reason : null,
            alt: altCandidate ? {
                drillerId: altCandidate.drillerId,
                title: altCandidate.title,
                buttonLabel: altCandidate.buttonLabel,
                options: altCandidate.options
            } : null
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
        // Warmed up here so it's ready by the time any caller downstream
        // computes a label via secondaryLabel()/humanizeSkill() -- every
        // real recommendation is produced through this function first.
        await _ensureGrammarTitles();

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
        if (typeof LearnerModel !== 'undefined' && LearnerModel.weakProductionSkills) {
            const weakProd = await LearnerModel.weakProductionSkills(1);
            if (weakProd && weakProd.length > 0) {
                const p = weakProd[0];
                if (p.modality === 'written') {
                    secondary.push({ kind: 'writing', title: `Writing: ${humanizeSkill(p.skillId)}`, reason: 'weak' });
                } else {
                    secondary.push({ kind: 'speaking', skill: p.skillId, reason: 'weak' });
                }
            }
        }
        _drillerCandidates().forEach(c => {
            if (c.drillerId === 'speaking' && secondary.some(s => s.kind === 'speaking')) return;
            if (c.drillerId === 'writing' && secondary.some(s => s.kind === 'writing')) return;
            secondary.push(c);
        });

        return { primary, secondary: secondary.slice(0, 3) };
    }

    // ----------------------------------------
    // PIECE C: SHARED "WHAT'S NEXT" RESULTS-SCREEN ACTION
    // ----------------------------------------

    function _nextActionInfo(primary) {
        let title, sub, cta;
        if (primary.kind === 'continue') {
            if (!primary.step) return null; // course finished
            if (primary.step.kind === 'test') {
                title = `${primary.step.level} level test`;
                cta = `Take ${primary.step.level} test`;
                sub = 'Course checkpoint · 80% to move on';
            } else {
                title = primary.step.lesson.title;
                cta = `Next: ${primary.step.lesson.title}`;
                sub = 'Continue your course';
            }
        } else if (primary.kind === 'unit-nudge') {
            if (primary.scenario) {
                title = `Oral Roleplay: ${primary.scenario.title}`;
                cta = `Start roleplay: ${primary.scenario.title}`;
                sub = `Put "${primary.unit.title || 'that unit'}" into conversation`;
            } else {
                title = `Practise: ${humanizeSkill(primary.skill)}`;
                cta = title;
                sub = `A quick round on what "${primary.unit.title || 'that unit'}" just taught`;
            }
        } else if (primary.kind === 'mini-game') {
            title = primary.challengeTitle || (primary.skill ? `Grammar: ${humanizeSkill(primary.skill)}` : 'Quick Challenge');
            cta = primary.buttonLabel || title;
            sub = primary.blurb || "Reinforce what you just learned";
        } else {
            return null;
        }

        return { title, cta, sub };
    }

    function _nextActionHtml(primary) {
        const info = _nextActionInfo(primary);
        if (!info) return '';

        return `
            <div class="wk-next-action">
                <span class="wk-next-eyebrow">What's next?</span>
                <button class="vbtn vbtn-primary wk-next-primary-btn" data-next-action="1">${esc(info.cta)} →</button>
                <span class="wk-next-sub">${esc(info.sub)}</span>
            </div>
        `;
    }

    function _routeTo(primary) {
        if (typeof Workshop !== 'undefined') Workshop.close();
        if (primary.kind === 'continue') {
            if (!primary.step) return;
            if (primary.step.kind === 'test') {
                if (typeof LevelTest !== 'undefined') LevelTest.open(primary.step.level);
            } else if (typeof startLesson === 'function') {
                startLesson(primary.step.lesson.id);
            }
        } else if (primary.kind === 'unit-nudge') {
            dismissUnit(primary.unit.id);
            if (typeof Workshop !== 'undefined') {
                if (primary.scenario) {
                    Workshop.open('speaking', { scenarioId: primary.scenario.id, returnTab: 'home' });
                } else {
                    Workshop.open('grammar', { skill: primary.skill, autoStart: true });
                }
            }
        } else if (primary.kind === 'mini-game') {
            dismissMiniGame(primary.lessonId);
            if (typeof Workshop !== 'undefined') {
                Workshop.open(primary.drillerId, primary.options);
            }
        }
    }

    // Mounted on results screens. When a results actions container (.vspeed-results-actions)
    // is present, the Next Activity is mounted at the TOP as the primary forward action,
    // and "Practice Again" is demoted to secondary.
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

        const info = _nextActionInfo(rec.primary);
        if (!info) return;

        const actionsEl = container.querySelector('.vspeed-results-actions');
        if (actionsEl) {
            const playAgainBtn = actionsEl.querySelector('[data-action="play-again"]');
            if (playAgainBtn) {
                playAgainBtn.classList.remove('vbtn-primary');
                playAgainBtn.classList.add('vbtn-secondary');
            }

            const slot = document.createElement('div');
            slot.className = 'wk-next-action-slot';
            slot.innerHTML = `
                <button class="vbtn vbtn-primary wk-next-primary-btn" data-next-action="1">${esc(info.cta)} →</button>
                <span class="wk-next-sub">${esc(info.sub)}</span>
            `;
            actionsEl.insertAdjacentElement('afterbegin', slot);

            const btn = slot.querySelector('[data-next-action]');
            if (btn) btn.addEventListener('click', () => _routeTo(rec.primary));
            return;
        }

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
        grammarVocabCandidate: _grammarVocabCandidate,
        _scenarioForUnit,
        _practiceNudge,
        _miniGameNudge
    };
})();

if (typeof window !== 'undefined') {
    window.RecommendationEngine = RecommendationEngine;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RecommendationEngine;
}
