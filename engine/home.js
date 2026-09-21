// ============================================
// HOME
// ============================================
// The screen that answers one question: what should I do now?
//
// Nothing is studied here. Every object on it is a door into the section that
// owns the work, and the screen is deliberately short — one dominant thing to
// continue, three other ways in, where today stands, and how far the course
// has come. Detail about progress belongs on My Journey; anything that needs
// choosing between belongs in the section that owns it.
//
// Home keeps no state of its own. Every figure is counted at render time from
// data another module owns, and the tab is redrawn on every entry (see
// showTab in engine/init.js), so it cannot go stale.

const Home = (function () {
    'use strict';

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    function plural(n, one, many) {
        return n === 1 ? one : (many || one + 's');
    }

    // The page title. Time of day, not progress: the header is editorial and
    // carries no running state, so the one thing on it that changes is the
    // one thing that has nothing to do with how the learner is doing.
    function greeting() {
        const hour = new Date().getHours();
        let timeStr = 'Good morning';
        if (hour >= 12 && hour < 18) timeStr = 'Good afternoon';
        else if (hour >= 18) timeStr = 'Good evening';

        const name = (typeof Sync !== 'undefined' && typeof Sync.getUserName === 'function')
            ? Sync.getUserName()
            : (typeof localStorage !== 'undefined' ? localStorage.getItem('parlour_user_name') || '' : '');

        if (name) {
            return `${timeStr}, ${name}`;
        }
        return timeStr;
    }

    // ----------------------------------------
    // GATHERING
    // ----------------------------------------

    // Counted here rather than taken from getDueCards(), which answers within
    // whatever deck the last review session was scoped to. Home is asking
    // about the whole deck.
    function deckStanding() {
        const deck = (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) ? srsDeck : [];
        const now = Date.now();
        let due = 0;
        let soonest = null;

        deck.forEach(card => {
            // No schedule means the card has never been reviewed. The deck
            // browser counts those as due; so does this.
            if (!card.nextReview) { due++; return; }
            const at = new Date(card.nextReview).getTime();
            if (at <= now) { due++; return; }
            if (soonest === null || at < soonest) soonest = at;
        });

        return {
            size: deck.length,
            due: due,
            waitMinutes: soonest === null ? null : Math.max(1, Math.round((soonest - now) / 60000))
        };
    }

    // The post-unit practice nudge and the per-lesson mini-game offer are
    // both computed by engine/recommendationEngine.js now, alongside the
    // plain continue card — one RecommendationEngine.recommend() call in
    // render() below replaces what used to be three separate calls here.
    // dismissUnit()/dismissMiniGame() stay as thin delegates since Home's
    // own click handlers below still need to call them directly.
    const dismissUnit = RecommendationEngine.dismissUnit;
    const dismissMiniGame = RecommendationEngine.dismissMiniGame;
    let _currentPrimaryRec = null;

    // ----------------------------------------
    // PIECES
    // ----------------------------------------

    function meter(percent) {
        const width = Math.max(0, Math.min(100, percent));
        return `<span class="hm-track"><span class="hm-fill" style="width:${width}%"></span></span>`;
    }

    // The dominant object on the screen, and the only thing wearing the
    // accent: the course is the spine of the app, so what comes next in it
    // leads whatever else is waiting.
    function continueCard(step) {
        if (!step) {
            return `
                <section class="hm-continue is-done">
                    <span class="hm-eyebrow">The course</span>
                    <span class="hm-continue-title">Every lesson is finished</span>
                    <span class="hm-continue-sub">Nothing is left to unlock. Keep the
                        words alive in Decks, and read.</span>
                </section>
            `;
        }

        const level = step.level;
        const levelTitle = step.title;
        const percent = step.total ? Math.round((step.done / step.total) * 100) : 0;
        const count = `${step.done} of ${step.total} ${plural(step.total, 'lesson')}`;

        if (step.kind === 'test') {
            const best = step.result
                ? `Best so far ${step.result.correct} / ${step.result.total} · 80% to move on`
                : '20 questions · 80% to move on';

            return `
                <button class="hm-continue" data-open-test="${esc(level)}">
                    <span class="hm-eyebrow">${esc(level)}${levelTitle ? ' · ' + esc(levelTitle) : ''}</span>
                    <span class="hm-continue-title">${esc(level)} level test</span>
                    <span class="hm-continue-sub">${esc(best)}</span>
                    ${meter(percent)}
                    <span class="hm-continue-foot">
                        <span class="hm-count">${count}</span>
                        <span class="hm-cta">Take the test →</span>
                    </span>
                </button>
            `;
        }

        const lesson = step.lesson;
        const sub = [
            lesson.label ? 'Lesson ' + lesson.label : '',
            lesson.grammar || ''
        ].filter(Boolean).join(' · ');

        return `
            <button class="hm-continue" data-start-lesson="${esc(lesson.id)}">
                <span class="hm-eyebrow">${esc(level)}${levelTitle ? ' · ' + esc(levelTitle) : ''}</span>
                <span class="hm-continue-title">${esc(lesson.title)}</span>
                <span class="hm-continue-sub">${esc(sub)}</span>
                ${meter(percent)}
                <span class="hm-continue-foot">
                    <span class="hm-count">${count}</span>
                    <span class="hm-cta">${step.done ? 'Continue' : 'Begin'} →</span>
                </span>
            </button>
        `;
    }

    // Stands in the continue card's slot for exactly one visit after a unit
    // ends — same dominant position, because this is the one moment a
    // detour here is worth more than the default "keep going." Two real
    // actions rather than one whole-row click (unlike continueCard's
    // button), since "practise" and "not now" aren't the same weight.
    function practiceNudgeCard(nudge) {
        const title = nudge.unit.title || 'that unit';
        if (nudge.scenario) {
            return `
                <section class="hm-continue hm-nudge">
                    <span class="hm-eyebrow">${esc(nudge.levelKey)} · Unit Milestone</span>
                    <span class="hm-continue-title">Put it into conversation</span>
                    <span class="hm-continue-sub">Complete the oral roleplay "${esc(nudge.scenario.title)}" to put what "${esc(title)}" taught into active practice.</span>
                    <span class="hm-continue-foot">
                        <button class="hm-cta-btn" data-practice-scenario="${esc(nudge.scenario.id)}"
                            data-unit-id="${esc(nudge.unit.id)}">Start roleplay →</button>
                        <button class="dk-link-btn" data-skip-unit="${esc(nudge.unit.id)}">Not now</button>
                    </span>
                </section>
            `;
        }
        return `
            <section class="hm-continue hm-nudge">
                <span class="hm-eyebrow">${esc(nudge.levelKey)} · Unit complete</span>
                <span class="hm-continue-title">Practise before moving on?</span>
                <span class="hm-continue-sub">A quick round on what "${esc(title)}" just taught,
                    while it's still fresh.</span>
                <span class="hm-continue-foot">
                    <button class="hm-cta-btn" data-practice-unit="${esc(nudge.unit.id)}"
                        data-skill="${esc(nudge.skill)}">Practise now →</button>
                    <button class="dk-link-btn" data-skip-unit="${esc(nudge.unit.id)}">Not now</button>
                </span>
            </section>
        `;
    }

    function miniGameCard(mini) {
        const blurb = mini.blurb || "Reinforce what you just learned, while it's still fresh.";
        const title = mini.challengeTitle || 'Play a mini-game?';
        const primaryLabel = mini.buttonLabel || (mini.skill ? `Grammar (${QUICK_REINFORCE_COUNT} questions)` : 'Quick challenge');

        return `
            <section class="hm-continue hm-nudge">
                <span class="hm-eyebrow">Quick challenge</span>
                <span class="hm-continue-title">${esc(title)}</span>
                <span class="hm-continue-sub">${esc(blurb)}</span>
                <span class="hm-continue-foot">
                    <button class="hm-cta-btn" data-mini-game-primary="1"
                        data-mini-game-lesson="${esc(mini.lessonId)}">${esc(primaryLabel)} →</button>
                    ${mini.alt ? `
                        <button class="hm-cta-btn" data-mini-game-alt="1"
                            data-mini-game-lesson="${esc(mini.lessonId)}">${esc(mini.alt.buttonLabel)} →</button>
                    ` : ''}
                    <button class="dk-link-btn" data-skip-mini-game="${esc(mini.lessonId)}">Not now</button>
                </span>
            </section>
        `;
    }

    function onboardingWelcomeCard() {
        const currentCode = Lang.code();
        const chips = Lang.available().map(code => {
            const isSelected = code === currentCode;
            return `
                <button type="button" class="hm-lang-choice-btn ${isSelected ? 'is-active' : ''}" data-switch-lang="${esc(code)}" ${isSelected ? 'aria-pressed="true"' : 'aria-pressed="false"'}>
                    ${esc(Lang.nameFor(code))}
                </button>
            `;
        }).join('');

        return `
            <section class="hm-continue hm-onboarding-card">
                <div class="hm-onboarding-head">
                    <span class="hm-eyebrow">Welcome to Parlour</span>
                    <button class="hm-onboarding-dismiss-btn" data-dismiss-onboarding="1" title="Dismiss" aria-label="Dismiss">&times;</button>
                </div>
                <span class="hm-continue-title">Find your starting point</span>
                <p class="hm-onboarding-blurb">Parlour is for people who actually want to learn languages and cultures. A non-commercial project, we want to provide a place where you can learn, read, review, and practice — welcome!</p>
                
                <div class="hm-onboarding-lang-picker">
                    <span class="hm-onboarding-picker-label">I want to learn:</span>
                    <div class="hm-onboarding-lang-chips">
                        ${chips}
                    </div>
                </div>

                <div class="hm-onboarding-actions">
                    <button class="hm-onboarding-cta" data-open-diagnostic="1" type="button">Take placement test →</button>
                    <button class="hm-onboarding-btn-secondary" data-start-unit-1="1" type="button">Start at Unit 1</button>
                    <button class="hm-onboarding-btn-guide" data-open-guide-modal="1" type="button">How Parlour works</button>
                </div>
            </section>
        `;
    }

    // A one-tap Quick Budget bar directly under the hero card — lets the
    // learner size and launch a finite study session (5, 10, 15, or 30 min)
    // without navigating away or opening extra modal sheets.
    function quickBudgetBar() {
        return `
            <div class="hm-budget-bar">
                <span class="hm-budget-label">Short on time?</span>
                <div class="hm-budget-pills">
                    <button class="hm-budget-pill" data-sp-budget="5" type="button">5 min</button>
                    <button class="hm-budget-pill" data-sp-budget="10" type="button">10 min</button>
                    <button class="hm-budget-pill" data-sp-budget="15" type="button">15 min</button>
                    <button class="hm-budget-pill" data-sp-budget="30" type="button">30 min</button>
                </div>
            </div>
        `;
    }

    // Dynamic Memory / Review alert — renders ONLY when cards are actually due.
    // When 0 cards are due, it renders nothing (zero visual clutter).
    function reviewAlert(deck) {
        if (!deck || !deck.due) return '';
        return `
            <div class="hm-review-alert">
                <div class="hm-review-alert-body">
                    <span class="hm-review-alert-badge">${deck.due}</span>
                    <div class="hm-review-alert-text">
                        <strong>${deck.due} ${plural(deck.due, 'word')} ready for review</strong>
                        <span class="hm-review-alert-sub">Scheduled memory review</span>
                    </div>
                </div>
                <button class="vbtn vbtn-primary hm-review-alert-cta" data-review-all="1" type="button">Review now →</button>
            </div>
        `;
    }

    // Today's three activities and the streak they keep. Streamlined to keep
    // Home calm and focused: daily trio status and interactive activity chips.
    function todayStrip() {
        return `
            <div class="today">
                <div class="today-head">
                    <span id="daily-trio-status" class="daily-trio-status">Daily Trio: 0 of 3</span>
                    <span id="header-streak" class="today-streak"></span>
                    <span id="header-xp" style="display:none;"></span>
                </div>
                <div id="daily-activities" class="daily-activities"></div>
            </div>
        `;
    }

    // ----------------------------------------
    // ACTIONS
    // ----------------------------------------

    function goTab(id, options) {
        const button = document.querySelector('.nav button[data-tab="' + id + '"]');
        if (typeof showTab === 'function') showTab(id, button, options);
    }

    function attach(host) {
        host.addEventListener('click', e => {
            const start = e.target.closest('[data-start-lesson]');
            if (start && typeof startLesson === 'function') {
                start.classList.add('is-loading');
                startLesson(start.getAttribute('data-start-lesson'));
                return;
            }

            const test = e.target.closest('[data-open-test]');
            if (test && typeof LevelTest !== 'undefined') {
                test.classList.add('is-loading');
                LevelTest.open(test.getAttribute('data-open-test'));
                return;
            }

            const diag = e.target.closest('[data-open-diagnostic]');
            if (diag && typeof DiagnosticTest !== 'undefined') {
                DiagnosticTest.open({
                    onExit: () => render()
                });
                return;
            }

            const startUnit1 = e.target.closest('[data-start-unit-1]');
            if (startUnit1) {
                if (typeof DiagnosticTest !== 'undefined') DiagnosticTest.dismissOnboarding();
                const next = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
                if (next && next.kind === 'lesson' && typeof startLesson === 'function') {
                    startUnit1.classList.add('is-loading');
                    startLesson(next.lesson.id);
                } else {
                    render();
                }
                return;
            }

            const dismissOnboarding = e.target.closest('[data-dismiss-onboarding]');
            if (dismissOnboarding) {
                if (typeof DiagnosticTest !== 'undefined') DiagnosticTest.dismissOnboarding();
                render();
                return;
            }

            const openGuideModal = e.target.closest('[data-open-guide-modal]');
            if (openGuideModal) {
                if (typeof Guide !== 'undefined' && Guide.openOverviewModal) {
                    Guide.openOverviewModal();
                }
                return;
            }

            const switchLang = e.target.closest('[data-switch-lang]');
            if (switchLang) {
                const code = switchLang.getAttribute('data-switch-lang');
                if (code && code !== Lang.code()) {
                    Lang.set(code);
                    location.reload();
                }
                return;
            }

            // Straight into a session over the whole deck — the door already
            // said how many were waiting, so the deck browser in between would
            // only ask the question a second time.
            const reviewAll = e.target.closest('[data-review-all]');
            if (reviewAll) {
                reviewAll.classList.add('is-loading');
                goTab('review', { skipReviewReset: true });
                if (typeof Decks !== 'undefined') Decks.reviewDeck('all');
                return;
            }

            const story = e.target.closest('[data-open-story]');
            if (story) {
                story.classList.add('is-loading');
                goTab('reader');
                if (typeof Reader !== 'undefined') Reader.loadStory(story.getAttribute('data-open-story'));
                return;
            }

            const go = e.target.closest('[data-go]');
            if (go) goTab(go.getAttribute('data-go'));

            const trio = e.target.closest('[data-trio-activity]');
            if (trio) {
                const act = trio.getAttribute('data-trio-activity');
                if (act === 'review') {
                    goTab('review');
                } else if (act === 'reading') {
                    goTab('reader');
                } else if (act === 'learn') {
                    const next = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
                    if (next && next.kind === 'lesson' && typeof startLesson === 'function') {
                        trio.classList.add('is-loading');
                        startLesson(next.lesson.id);
                    } else {
                        goTab('lessons');
                    }
                }
                return;
            }

            const practise = e.target.closest('[data-practice-unit]');
            if (practise) {
                dismissUnit(practise.getAttribute('data-practice-unit'));
                goTab('drills');
                if (typeof Workshop !== 'undefined') {
                    Workshop.open('grammar', { skill: practise.getAttribute('data-skill') });
                }
                return;
            }

            const practiseScenario = e.target.closest('[data-practice-scenario]');
            if (practiseScenario) {
                const unitId = practiseScenario.getAttribute('data-unit-id');
                if (unitId) dismissUnit(unitId);
                const scenarioId = practiseScenario.getAttribute('data-practice-scenario');
                goTab('drills');
                if (typeof Workshop !== 'undefined') {
                    Workshop.open('speaking', { scenarioId: scenarioId, returnTab: 'home' });
                }
                return;
            }

            const skip = e.target.closest('[data-skip-unit]');
            if (skip) {
                dismissUnit(skip.getAttribute('data-skip-unit'));
                render();
                return;
            }

            const miniPrimary = e.target.closest('[data-mini-game-primary]');
            if (miniPrimary) {
                const lessonId = miniPrimary.getAttribute('data-mini-game-lesson');
                dismissMiniGame(lessonId);
                goTab('drills');
                if (_currentPrimaryRec && _currentPrimaryRec.kind === 'mini-game' && typeof Workshop !== 'undefined') {
                    Workshop.open(_currentPrimaryRec.drillerId, _currentPrimaryRec.options);
                }
                return;
            }

            const miniAlt = e.target.closest('[data-mini-game-alt]');
            if (miniAlt) {
                const lessonId = miniAlt.getAttribute('data-mini-game-lesson');
                dismissMiniGame(lessonId);
                goTab('drills');
                if (_currentPrimaryRec && _currentPrimaryRec.kind === 'mini-game' && _currentPrimaryRec.alt && typeof Workshop !== 'undefined') {
                    Workshop.open(_currentPrimaryRec.alt.drillerId, _currentPrimaryRec.alt.options);
                }
                return;
            }

            const miniGrammar = e.target.closest('[data-mini-game-grammar]');
            if (miniGrammar) {
                dismissMiniGame(miniGrammar.getAttribute('data-mini-game-lesson'));
                goTab('drills');
                if (typeof Workshop !== 'undefined') {
                    Workshop.open('grammar', {
                        skill: miniGrammar.getAttribute('data-mini-game-grammar'),
                        count: (typeof QUICK_REINFORCE_COUNT === 'number') ? QUICK_REINFORCE_COUNT : 5
                    });
                }
                return;
            }

            const miniVocab = e.target.closest('[data-mini-game-vocab]');
            if (miniVocab) {
                const lessonId = miniVocab.getAttribute('data-mini-game-lesson');
                dismissMiniGame(lessonId);
                (async () => {
                    const lesson = (typeof loadLesson === 'function') ? await loadLesson(lessonId) : null;
                    const words = (lesson && typeof collectLessonVocabulary === 'function')
                        ? await collectLessonVocabulary(lesson) : [];
                    goTab('drills');
                    if (typeof Workshop !== 'undefined') Workshop.open('vocabulary', { words: words });
                })();
                return;
            }

            const skipMini = e.target.closest('[data-skip-mini-game]');
            if (skipMini) {
                dismissMiniGame(skipMini.getAttribute('data-skip-mini-game'));
                render();
                return;
            }

            const secGrammar = e.target.closest('[data-secondary-grammar]');
            if (secGrammar) {
                goTab('drills');
                RecommendationEngine.openSecondary({ kind: 'grammar', skill: secGrammar.getAttribute('data-secondary-grammar') });
                return;
            }

            const secDriller = e.target.closest('[data-secondary-driller]');
            if (secDriller) {
                goTab('drills');
                RecommendationEngine.openSecondary({ kind: 'driller', drillerId: secDriller.getAttribute('data-secondary-driller') });
                return;
            }

            // Vocabulary's word list doesn't serialise cleanly into a data
            // attribute — same reasoning engine/workshop.js's own secondary
            // wiring already documents — so this recomputes the
            // recommendation fresh rather than caching rec.secondary across
            // the render/click boundary, keeping this file's "no state of
            // its own" rule intact.
            if (e.target.closest('[data-secondary-vocab]')) {
                goTab('drills');
                (async () => {
                    const rec = await RecommendationEngine.recommend();
                    const candidate = rec.secondary.find(c => c.kind === 'vocabulary');
                    RecommendationEngine.openSecondary(candidate);
                })();
                return;
            }

            const budgetBtn = e.target.closest('[data-sp-budget]');
            if (budgetBtn && typeof StudyPlanRunner !== 'undefined') {
                const minutes = Number(budgetBtn.getAttribute('data-sp-budget'));
                StudyPlanRunner.start(minutes);
                return;
            }

            if (e.target.closest('[data-open-study-plan]')) {
                if (typeof StudyPlanRunner !== 'undefined') StudyPlanRunner.openBudgetPicker();
                return;
            }
        });

        host.addEventListener('change', e => {
            const select = e.target.closest('#hm-lang-select');
            if (!select || select.value === Lang.code()) return;
            Lang.set(select.value);
            location.reload();
        });
    }

    // Which course the learner is studying. Refined into a discreet topbar chip
    // rather than a bulky form group, leaving Home's primary focus on learning.
    function courseBlock() {
        const options = Lang.available()
            .map(code => `<option value="${code}"${code === Lang.code() ? ' selected' : ''}>${esc(Lang.nameFor(code))}</option>`)
            .join('');

        return `
            <div class="hm-topbar">
                <div class="hm-lang-chip">
                    <label class="hm-lang-label" for="hm-lang-select">Course:</label>
                    <select id="hm-lang-select" class="hm-lang-select" aria-label="Course">${options}</select>
                </div>
            </div>
        `;
    }

    // ----------------------------------------
    // RENDER
    // ----------------------------------------

    async function render() {
        const host = document.getElementById('home-root');
        if (!host) return;

        const step = LearnerPath.nextStep();
        const deck = deckStanding();
        const rec = await RecommendationEngine.recommend();
        _currentPrimaryRec = rec ? rec.primary : null;

        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const completedCount = Object.keys(progress).length;
        const showOnboarding = completedCount === 0
            && typeof DiagnosticTest !== 'undefined'
            && !DiagnosticTest.hasTaken()
            && !DiagnosticTest.isOnboardingDismissed();

        host.innerHTML = `
            ${courseBlock()}
            ${showOnboarding ? onboardingWelcomeCard() : ''}
            ${rec.primary.kind === 'unit-nudge' ? practiceNudgeCard(rec.primary)
                : rec.primary.kind === 'mini-game' ? miniGameCard(rec.primary)
                : continueCard(rec.primary.step)}
            ${quickBudgetBar()}
            ${reviewAlert(deck)}
            ${todayStrip()}
        `;

        // The streak, the XP and the three activity marks are written by the
        // XP module, which owns them and keeps them right everywhere.
        if (typeof updateXPHeader === 'function') updateXPHeader();

        if (!host.dataset.wired) {
            attach(host);
            host.dataset.wired = '1';
        }
    }

    return { render, greeting, nextStep: LearnerPath.nextStep };
})();
