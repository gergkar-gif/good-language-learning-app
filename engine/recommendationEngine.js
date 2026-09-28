// ============================================
// RECOMMENDATION ENGINE — one recommendation, shown on Home
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
// this step's job. The post-unit practice nudge is scenario-only (a
// matching conversation roleplay) — a plain grammar recap of the unit used
// to force this same forced-primary slot too, but that gave grammar an
// outsized precedence no other driller got; it now competes as an ordinary
// _miniGameNudge() candidate like everything else (2026-09-23).
//
// There is no secondary tier (removed 2026-09-28, along with Workshop's
// "Recommended for you" card): Home shows exactly one recommendation, so
// every signal that matters — weak skills/words/drillers, the lesson just
// finished, the elective track — competes for that one slot instead.
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

    // Curated skill names live in content/<lang>/indexes/grammar-titles.json
    // (e.g. "cambio-radical-reflexivos" -> "stem-changing reflexive verbs"),
    // written lowercase-first so they sit mid-sentence in practice
    // suggestions ("You made a few mistakes with … lately."). A skill
    // missing from the file falls back to its id with spaces, which reads
    // better mid-sentence than title case. Keyed by the resolved path (not a single flat
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

    // Written Exchanges (Workshop's Writing Studio) — same shape and same
    // unitIds-matching idea as the oral scenarios above, so a unit that
    // teaches written-register content (texting a friend, a work email) can
    // earn the same forced-primary "put it into practice" slot an oral
    // scenario does, rather than being reachable only by opening Workshop
    // manually.
    const _exchangesCache = {};

    async function _loadExchangesForLang() {
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') return [];
        const path = Lang.content('writing-exchanges.json');
        if (!_exchangesCache[path]) {
            const data = await Content.json(path).catch(() => null);
            _exchangesCache[path] = (data && data.scenarios) ? data.scenarios : [];
        }
        return _exchangesCache[path];
    }

    async function _exchangeForUnit(unitId) {
        if (!unitId) return null;
        try {
            const exchanges = await _loadExchangesForLang();
            return exchanges.find(x => (x.unitIds || []).includes(unitId)) || null;
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

    // The Vocabulary Driller (engine/workshop.js) is gated to B1+ — its
    // context-inference exercises don't work with a beginner's vocabulary.
    // Mirrored here so this engine never recommends a driller its own
    // picker would refuse to show.
    function _vocabularyAvailable() {
        if (typeof LearnerPath === 'undefined' || !LearnerPath.currentLevel || typeof LEVEL_ORDER === 'undefined') return false;
        return LEVEL_ORDER.indexOf(LearnerPath.currentLevel()) >= LEVEL_ORDER.indexOf('B1');
    }

    // Where a word-review practice card lands —
    // mirrors engine/studyPlanRunner.js's own dispatch for its 'match'/
    // 'review' plan items: goTab('review') + Decks.reviewDeck() for a plain
    // review, or DeckMatch.render() straight into the deck browser's own
    // container for a match (same container Decks itself swaps content
    // into for its own match mode — see engine/decks.js's studyMode
    // branch), with onExit handing the container back to Decks.render().
    function _openSrs(candidate) {
        const isMatch = candidate.action === 'match' && typeof DeckMatch !== 'undefined';
        if (typeof showTab === 'function') {
            // skipReviewReset: for a match, we render DeckMatch into
            // #decks-root ourselves right below — without this, showTab's own
            // un-awaited Decks.render() (via endReviewSession) can resolve
            // afterwards and overwrite the match game with the plain deck
            // list, landing the learner back on the Decks browser instead.
            showTab('review', document.querySelector('.nav button[data-tab="review"]'), isMatch ? { skipReviewReset: true } : undefined);
        }
        if (isMatch) {
            const host = document.getElementById('decks-root');
            if (host) {
                DeckMatch.render(host, {
                    words: candidate.words,
                    deckId: 'weakest-words',
                    srsCredit: true,
                    exitLabel: 'Back to Decks',
                    onExit: () => { if (typeof Decks !== 'undefined') Decks.render(); }
                });
            }
        } else if (typeof Decks !== 'undefined' && Decks.reviewDeck) {
            Decks.reviewDeck('all', { limit: candidate.words.length });
        }
    }

    function humanizeSkill(id) {
        const key = String(id || '');
        const path = (typeof Lang !== 'undefined') ? Lang.content('indexes/grammar-titles.json') : null;
        const titles = path ? _grammarTitlesCache[path] : null;
        if (titles && titles[key]) return titles[key];
        return key.replace(/[-_]+/g, ' ');
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

        const words = _vocabularyAvailable()
            ? LearnerModel.weakWords().map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos }))
            : [];
        const wordsReason = words.length ? 'weak' : null;

        if (!skill && !words.length) return null;
        return { skill, skillReason, words, wordsReason, unit, levelKey };
    }

    // ----------------------------------------
    // PRIMARY CANDIDATES (moved from engine/home.js, same bodies)
    // ----------------------------------------

    // Home's post-unit practice beat: the last lesson completed was the
    // last lesson in its unit, that unit hasn't already been resolved, and
    // a matching conversation scenario exists to point at. Only a scenario
    // earns this forced-primary slot — it's a genuinely different,
    // communicative capstone a learner wouldn't otherwise be steered
    // toward. A plain grammar recap of the unit used to fall back to here
    // too, but that gave grammar special precedence no other driller got;
    // it now just competes as an ordinary _miniGameNudge() candidate
    // (Candidate 1, "Targeted Grammar") via its own "recent" fallback.
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

        // `type` distinguishes oral vs written here — deliberately not
        // `kind`, which the caller below sets to the outer 'unit-nudge' via
        // Object.assign(); reusing `kind` on this returned object would
        // silently win that merge and the card would never render (see the
        // 2026-09-23 fix that gave this its own key).
        const scenario = await _scenarioForUnit(unit.id);
        if (scenario) return { levelKey, unit, scenario, type: 'scenario' };

        const exchange = await _exchangeForUnit(unit.id);
        if (exchange) return { levelKey, unit, exchange, type: 'exchange' };

        return null;
    }

    // Home's per-lesson counterpart: a short practice session offered in
    // Continue's place after a lesson — but only when there's a real,
    // recent weakness to point at. With nothing weak this returns null and
    // Continue leads: a card that always stands in the way just teaches
    // people to tap "Not now" without reading it. Every candidate below
    // must make its blurb true.
    //
    // "Recent" is TROUBLE_RECENT_OPENS app opens for grammar (see
    // LearnerModel.troubleSkills()) and RECENT_DAYS for the signals that
    // carry dates (drill sessions, speaking attempts).
    const RECENT_DAYS = 14;
    const MIN_MISSED_WORDS = 3;

    function _isRecent(iso) {
        const t = iso ? Date.parse(iso) : NaN;
        return isFinite(t) && Date.now() - t <= RECENT_DAYS * 24 * 60 * 60 * 1000;
    }

    // Words the learner has actually got wrong: below the starting ease
    // (only 'again'/'hard' move it down), or looked up in the Reader on
    // several days (`ease: null`). weakWords() on its own returns the
    // lowest-ease cards even when none was ever missed.
    function _missedWords() {
        if (typeof LearnerModel === 'undefined' || !LearnerModel.weakWords) return [];
        const start = (typeof SRS_CONFIG !== 'undefined') ? SRS_CONFIG.START_EASE : 2.5;
        return LearnerModel.weakWords(10).filter(w => w.ease == null || w.ease < start);
    }

    // What each weak driller's card says and opens with. Speaking has its
    // own candidate below.
    const DRILLER_OFFERS = {
        verbs: { title: 'Verb conjugation', buttonLabel: 'Conjugation practice, timed', topic: 'verb conjugation', invite: 'Practice it here:', priority: 90, options: () => ({ mode: 'speed', autoStart: true, duration: 60 }) },
        'hu-verb': { title: 'Verb conjugation', buttonLabel: 'Conjugation practice', topic: 'verb conjugation', invite: 'Practice it here:', priority: 90, options: () => ({ autoStart: true, count: 5 }) },
        'hu-suffix': { title: 'Suffixes', buttonLabel: 'Suffix practice', topic: 'suffixes', invite: 'Practice them here:', priority: 90, options: () => ({ autoStart: true, count: 5 }) },
        'hu-prefix': { title: 'Verbal prefixes', buttonLabel: 'Prefix practice', topic: 'verbal prefixes', invite: 'Practice them here:', priority: 90, options: () => ({ autoStart: true, count: 5 }) },
        'hu-morphology': { title: 'Word structure', buttonLabel: 'Word structure practice', topic: 'word structure', invite: 'Practice it here:', priority: 90, options: () => ({ autoStart: true, count: 5 }) },
        translation: { title: 'Sentence translation', buttonLabel: 'Sentence translation', topic: 'sentence translation', invite: 'Practice it here:', priority: 88, options: level => ({ autoStart: true, count: 5, level, direction: 'alternate' }) },
        listening: { title: 'Listening', buttonLabel: 'Listening practice', topic: 'listening', invite: 'Practice it here:', priority: 88, options: level => ({ autoStart: true, count: 5, level }) }
    };

    // ----------------------------------------
    // OUTCOMES + COOL-DOWN
    // ----------------------------------------
    // What happened to each practice card: 'taken' or 'skipped', with the
    // app open it happened at. A skipped offer stays away for
    // SKIP_COOLDOWN_OPENS opens, so "Not now" isn't met by the same card
    // after the next lesson; a taken one isn't offered again in the same
    // sitting. Also the start of a record of how the cards are received.
    const SKIP_COOLDOWN_OPENS = 5;
    const OUTCOMES_KEPT = 50;

    function _outcomesKey() {
        return Lang.key('recommendationOutcomes');
    }

    function _outcomes() {
        try { return JSON.parse(localStorage.getItem(_outcomesKey()) || '[]'); }
        catch (error) { return []; }
    }

    function _offerKey(offer) {
        return offer.drillerId + ':' + (offer.skill || '');
    }

    function _noteOutcome(offer, outcome) {
        const list = _outcomes();
        list.push({ key: _offerKey(offer), outcome, open: _currentOpen(), at: new Date().toISOString() });
        try { localStorage.setItem(_outcomesKey(), JSON.stringify(list.slice(-OUTCOMES_KEPT))); }
        catch (error) { /* storage disabled — the cool-down just won't hold */ }
    }

    function _currentOpen() {
        return (typeof AppOpens !== 'undefined') ? AppOpens.current() : 0;
    }

    function _coolingDown(offer, outcomes, open) {
        const key = _offerKey(offer);
        return outcomes.some(o => o.key === key && (
            (o.outcome === 'skipped' && open - o.open < SKIP_COOLDOWN_OPENS) ||
            (o.outcome === 'taken' && o.open === open)));
    }

    async function _miniGameNudge() {
        const lessonId = LearnerPath.lastCompletedLessonId();
        if (!lessonId || miniGameDismissed(lessonId) || typeof LearnerModel === 'undefined') return null;

        const level = (LearnerPath.currentLevel ? LearnerPath.currentLevel() : 'A1').toLowerCase();
        const weakBlurb = topic => `You made a few mistakes with ${topic} lately.`;
        const candidates = [];

        // Grammar: every skill with recent unresolved misses, worst first,
        // so a cooled-down top skill hands over to the next one.
        const trouble = LearnerModel.troubleSkills ? await LearnerModel.troubleSkills(3) : [];
        trouble.forEach((t, i) => candidates.push({
            drillerId: 'grammar',
            skill: t.skillId,
            title: 'Grammar',
            buttonLabel: 'Grammar practice',
            blurb: weakBlurb(humanizeSkill(t.skillId)),
            invite: 'Practice it here:',
            priority: 100 - i,
            options: { skill: t.skillId, count: 5, autoStart: true }
        }));

        // Words: in context for B1+ (Vocabulary Driller), as a review
        // otherwise. Same words either way, so only one of the two.
        const words = _missedWords();
        if (words.length >= MIN_MISSED_WORDS) {
            if (_vocabularyAvailable()) {
                candidates.push({
                    drillerId: 'vocabulary',
                    title: 'Vocabulary',
                    buttonLabel: 'Vocabulary practice',
                    blurb: weakBlurb('some recent words'),
                    invite: 'Practice them here:',
                    priority: 95,
                    options: { words: words.slice(0, 6).map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos })), autoStart: true }
                });
            } else {
                const action = (words.length >= 4 && typeof DeckMatch !== 'undefined') ? 'match' : 'review';
                candidates.push({
                    drillerId: 'srs',
                    title: 'Word review',
                    buttonLabel: action === 'match' ? 'Word matching' : 'Word review',
                    blurb: 'These are the words you find hardest in review.',
                    invite: 'Practice them here:',
                    priority: 93,
                    options: { kind: 'srs', words, action }
                });
            }
        }

        // Speaking: a skill that's recently gone badly aloud, or the
        // Speaking Driller as a whole.
        const canSpeak = (typeof SpeechInput !== 'undefined' && SpeechInput.isSupported())
            || (typeof ParlourTTS !== 'undefined' && ParlourTTS.available());
        const weakDrillers = (LearnerModel.weakDrillers ? LearnerModel.weakDrillers() : []).filter(d => _isRecent(d.lastDate));
        if (canSpeak) {
            const prod = LearnerModel.weakProductionSkills
                ? (await LearnerModel.weakProductionSkills(3, 'oral')).find(p => _isRecent(p.lastSeen)) : null;
            if (prod || weakDrillers.some(d => d.drillerId === 'speaking')) {
                candidates.push({
                    drillerId: 'speaking',
                    skill: prod ? prod.skillId : null,
                    title: 'Speaking',
                    buttonLabel: 'Speaking practice',
                    blurb: prod
                        ? `You made a few mistakes with ${humanizeSkill(prod.skillId)} when speaking lately.`
                        : 'You made a few mistakes when speaking lately.',
                    invite: 'Practice it here:',
                    priority: 92,
                    options: { autoStart: true, count: 5, level, skill: prod ? prod.skillId : undefined }
                });
            }
        }

        // Any other driller whose recent sessions have gone badly.
        weakDrillers.forEach(d => {
            const offer = DRILLER_OFFERS[d.drillerId];
            if (!offer) return;
            candidates.push({
                drillerId: d.drillerId,
                title: offer.title,
                buttonLabel: offer.buttonLabel,
                blurb: weakBlurb(offer.topic),
                invite: offer.invite,
                priority: offer.priority,
                options: offer.options(level)
            });
        });

        const outcomes = _outcomes();
        const open = _currentOpen();
        const pick = candidates
            .filter(c => !_coolingDown(c, outcomes, open))
            .sort((a, b) => b.priority - a.priority)[0];
        if (!pick) return null;

        return {
            lessonId,
            challengeTitle: pick.title,
            drillerId: pick.drillerId,
            skill: pick.skill || null,
            buttonLabel: pick.buttonLabel,
            blurb: pick.blurb,
            invite: pick.invite,
            reason: 'weak',
            options: pick.options
        };
    }

    // ----------------------------------------
    // ELECTIVE-TRACK CANDIDATE
    // ----------------------------------------
    // A dual-track level's non-core track (B1 Spain's CCSE citizenship-exam
    // units, B1 Latin America's history units) is real content but not core
    // grammar progression, so engine/learnerPath.js's courseWalk() no
    // longer walks it and the level test no longer waits on it. It still
    // deserves surfacing, just occasionally, as Home's one card, after any
    // practice offer for the lesson just finished and before the plain
    // continue card: gated to roughly once every ELECTIVE_CADENCE
    // completed lessons, and skippable per-unit via the same
    // dismissedUnits() store the practice nudge already uses — skipping one
    // elective unit just moves the offer on to the next.
    const ELECTIVE_CADENCE = 5;

    function _electiveCandidate() {
        if (typeof LearnerPath === 'undefined' || !LearnerPath.currentLevel) return null;

        const completed = LearnerPath.completedCount();
        if (!completed || completed % ELECTIVE_CADENCE !== 0) return null;

        const data = window._curriculumData;
        const level = LearnerPath.currentLevel();
        const entry = data && data.levels && data.levels[level];
        if (!entry || !entry.tracks) return null;

        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const dismissed = dismissedUnits();
        const electiveUnits = (entry.units || []).filter(u => u.track && u.track !== 'core' && !dismissed.includes(u.id));

        for (const unit of electiveUnits) {
            const lesson = (unit.lessons || []).find(l => !progress[l.id]);
            if (!lesson) continue;
            const track = entry.tracks.find(t => t.id === unit.track);
            return { kind: 'elective', levelKey: level, unit, lesson, trackTitle: (track && track.title) || unit.track };
        }
        return null;
    }

    // ----------------------------------------
    // THE ENGINE
    // ----------------------------------------

    async function recommend() {
        // Warmed up here so it's ready by the time any caller downstream
        // computes a label via humanizeSkill() -- every real
        // recommendation is produced through this function first.
        await _ensureGrammarTitles();

        const nudge = await _practiceNudge();
        if (nudge) return { primary: Object.assign({ kind: 'unit-nudge' }, nudge) };

        const mini = await _miniGameNudge();
        if (mini) return { primary: Object.assign({ kind: 'mini-game' }, mini) };

        const elective = _electiveCandidate();
        if (elective) return { primary: elective };

        const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
        return { primary: { kind: 'continue', step } };
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
            if (primary.type === 'exchange') {
                title = `Written Exchange: ${primary.exchange.title}`;
                cta = `Start exchange: ${primary.exchange.title}`;
                sub = `Put "${primary.unit.title || 'that unit'}" into a written conversation`;
            } else {
                title = `Oral Roleplay: ${primary.scenario.title}`;
                cta = `Start roleplay: ${primary.scenario.title}`;
                sub = `Put "${primary.unit.title || 'that unit'}" into conversation`;
            }
        } else if (primary.kind === 'elective') {
            title = `${primary.trackTitle}: ${primary.unit.title}`;
            cta = `Start: ${primary.lesson.title}`;
            sub = `${primary.trackTitle} · optional track`;
        } else if (primary.kind === 'mini-game') {
            title = primary.challengeTitle || (primary.skill ? `Grammar: ${humanizeSkill(primary.skill)}` : 'Practice');
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

    // A Workshop driller renders into #drills-root, which only exists inside
    // the #drills tab. This card is mounted on all sorts of results screens
    // (lesson-complete, a driller's own results, Home) that aren't
    // necessarily that tab -- without switching first, Workshop.open()
    // still runs and updates Workshop's internal state, but paints into a
    // hidden container while the learner keeps looking at whatever screen
    // they clicked from, which reads as the button doing nothing at all.
    function _openWorkshopDriller(drillerId, options) {
        if (typeof showTab === 'function') {
            showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
        }
        if (typeof Workshop !== 'undefined') Workshop.open(drillerId, options);
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
            if (primary.type === 'exchange') {
                _openWorkshopDriller('writing', { scenarioId: primary.exchange.id, returnTab: 'home' });
            } else {
                _openWorkshopDriller('speaking', { scenarioId: primary.scenario.id, returnTab: 'home' });
            }
        } else if (primary.kind === 'elective') {
            if (typeof startLesson === 'function') startLesson(primary.lesson.id);
        } else if (primary.kind === 'mini-game') {
            dismissMiniGame(primary.lessonId);
            _noteOutcome(primary, 'taken');
            if (primary.drillerId === 'srs') {
                _openSrs(primary.options);
            } else {
                _openWorkshopDriller(primary.drillerId, primary.options);
            }
        }
    }

    // Home's "Not now" on a practice card.
    function skip(primary) {
        if (!primary || primary.kind !== 'mini-game') return;
        dismissMiniGame(primary.lessonId);
        _noteOutcome(primary, 'skipped');
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
        // Don't send the learner straight back into the driller they just
        // finished — point them on along the course instead.
        if (rec.primary.kind === 'mini-game' && rec.primary.drillerId === opts.excludeDrillerId) {
            const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
            rec = { primary: { kind: 'continue', step } };
        }

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
        open: _routeTo,
        skip,
        mountNextAction,
        dismissUnit,
        dismissMiniGame,
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
