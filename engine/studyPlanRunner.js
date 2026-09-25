// ============================================
// STUDY PLAN RUNNER — the "#study-plan-screen" UI
// ============================================
// The screen half of Time-Based Sessions (see engine/studyPlan.js for the
// allocation/queue logic this renders). Structurally mirrors the other two
// screens that take over the whole view instead of living in a normal tab
// (#lesson-screen, #leveltest — see engine/lessons.js's startLesson() and
// engine/leveltest.js's open()): hide every .tab, show this one, no
// PageHeader involvement, own inline heading inside the dynamic content.
//
// Grammar/vocabulary plan items are rendered by embedding GrammarDriller/
// VocabularyDriller directly into #study-plan-activity (both take an
// arbitrary container — see their own render(root, options), never
// hardwired to Workshop's DOM), so those two never leave this screen.
// Lesson/test/review items DO leave (startLesson()/LevelTest.open()/the
// #review tab each own their own DOM) and come back via
// RecommendationEngine.mountNextAction()'s StudyPlan-aware branch, which
// this module answers — see mountNextAction() below.

const StudyPlanRunner = (function () {
    'use strict';

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape) ? UI.escape(value) : String(value == null ? '' : value);
    }

    function humanize(id) {
        return String(id || '').replace(/[-_]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    }

    function screenEl() {
        return document.getElementById('study-plan-screen');
    }

    function activityHost() {
        return document.getElementById('study-plan-activity');
    }

    // Which driller module (if any) is currently embedded directly in this
    // screen — GrammarDriller/VocabularyDriller.render() bypasses
    // Workshop.open() entirely, so Workshop's own _active tracking never
    // sees these, and Workshop.close() would be a no-op for them. Tracked
    // here instead so teardown() can call the right module's stop().
    let _embeddedDriller = null;

    // Hungarian drillers, looked up lazily — they're only loaded for HU.
    const HU_DRILLERS = {
        'hu-verb': () => (typeof HuVerbDriller !== 'undefined' ? HuVerbDriller : null),
        'hu-suffix': () => (typeof HuSuffixDriller !== 'undefined' ? HuSuffixDriller : null),
        'hu-prefix': () => (typeof HuPrefixDriller !== 'undefined' ? HuPrefixDriller : null),
        'hu-morphology': () => (typeof HuMorphologyDriller !== 'undefined' ? HuMorphologyDriller : null)
    };

    // Review, Verb Driller and reading items are launched via goTab() — the
    // normal showTab()-driven tab switch, which tears down whatever tab it's
    // leaving (see engine/init.js's teardownTab()). Without this flag,
    // launching one would look identical to the learner navigating away to
    // abandon the plan, and get its own plan discarded out from under it
    // before the activity even starts. Set immediately before that goTab()
    // call, cleared as soon as teardown() reads it.
    let _leavingForActivity = false;

    // Same helper shape as engine/home.js's own goTab() — looks up the real
    // nav button so the bottom nav's active state stays correct when a plan
    // item hands off to a normal tab (review). #study-plan-screen itself has
    // no nav button on purpose (an alternative entry point, not a standing
    // tab), so its own transitions pass a null button deliberately.
    function goTab(id) {
        const button = document.querySelector('.nav button[data-tab="' + id + '"]');
        if (typeof showTab === 'function') showTab(id, button);
    }

    // ----------------------------------------
    // ITEM DESCRIPTION (plain language, matching the roadmap's "clear start
    // and end" — a checklist, not a countdown)
    // ----------------------------------------

    function itemLine(item) {
        if (item.kind === 'review') return `${item.count} ${item.count === 1 ? 'word' : 'words'} due for review`;
        if (item.kind === 'lesson') return `Lesson: ${item.title}`;
        if (item.kind === 'test') return `${item.level} level test`;
        if (item.kind === 'grammar') return `Grammar: ${humanize(item.skill)} — ${item.count} ${item.count === 1 ? 'question' : 'questions'}`;
        if (item.kind === 'vocabulary') return `Vocabulary — ${item.words.length} ${item.words.length === 1 ? 'word' : 'words'}`;
        if (item.kind === 'listening') return `Listening — ${item.count} ${item.count === 1 ? 'question' : 'questions'}`;
        if (item.kind === 'speaking') return item.skill ? `Speaking: ${humanize(item.skill)} — ${item.count} ${item.count === 1 ? 'sentence' : 'sentences'}` : `Speaking — ${item.count} ${item.count === 1 ? 'sentence' : 'sentences'}`;
        if (item.kind === 'speaking-cando') return `Quick speaking — ${item.seconds}s`;
        if (item.kind === 'match') return `Match Game — ${item.words.length} pairs`;
        if (item.kind === 'translation') return `Translation — ${item.count} ${item.count === 1 ? 'sentence' : 'sentences'}`;
        if (item.kind === 'verbs') return item.tense && typeof Verbs !== 'undefined' && Verbs.tenseLabel
            ? `Verb speed drill: ${Verbs.tenseLabel(item.tense)} — ${item.seconds}s`
            : `Verb speed drill — ${item.seconds}s`;
        if (item.kind === 'driller') return `${item.title} — ${item.count} ${item.count === 1 ? 'question' : 'questions'}`;
        if (item.kind === 'reading') return `Read: ${item.title}`;
        return '';
    }

    function skipText(skip) {
        if (skip.reason === 'lesson-too-long') {
            return `Your next lesson ("${skip.title}") is about ${skip.estMinutes} min — not enough room this time. It'll be waiting next time.`;
        }
        if (skip.reason === 'test-needs-bigger-block') {
            return `Your ${skip.level} level test needs a bigger block (about ${skip.estMinutes} min) — pick a longer session when you're ready for it.`;
        }
        return '';
    }

    // ----------------------------------------
    // CHECKLIST
    // ----------------------------------------

    async function renderChecklist() {
        const host = activityHost();
        if (!host) return;
        _embeddedDriller = null;

        // Time ran out after at least one activity: end here. (If nothing
        // was started yet, the plan still shows — a late first tap.)
        if (StudyPlan.isTimeUp() && !StudyPlan.overtime() && StudyPlan.currentIndex() > 0) {
            if (StudyPlan.isActive()) renderTimeUp();
            else renderCompletion();
            return;
        }

        // Planned items all done with time to spare — add the next one.
        if (!StudyPlan.isActive() && !(await StudyPlan.extend())) {
            renderCompletion();
            return;
        }

        const items = StudyPlan.items();
        const index = StudyPlan.currentIndex();
        const skip = StudyPlan.skipped();
        const current = items[index];

        const rows = items.map((item, i) => {
            const passed = i < index && StudyPlan.wasSkipped(i);
            const state = passed ? 'sp-item-passed' : (i < index ? 'sp-item-done' : (i === index ? 'sp-item-current' : ''));
            const mark = passed ? '–' : (i < index ? '✓' : i + 1);
            return `
                <li class="sp-item ${state}">
                    <span class="sp-item-check">${mark}</span>
                    <span class="sp-item-label">${esc(itemLine(item))}</span>
                </li>
            `;
        }).join('');

        host.innerHTML = `
            <div class="sp-checklist">
                <p class="sp-checklist-eyebrow">${esc(StudyPlan.minutes())}-minute session</p>
                <ul class="sp-item-list">${rows}</ul>
                ${skip ? `<p class="sp-skipped">${esc(skipText(skip))}</p>` : ''}
                <button class="btn-primary" data-sp-go="1">${esc(itemLine(current))} →</button>
                <div class="sp-activity-bar"><button class="sp-skip-link" data-sp-skip="1">Skip this activity</button></div>
                <button class="dk-secondary" data-sp-leave="1">Leave session</button>
            </div>
        `;

        const goBtn = host.querySelector('[data-sp-go]');
        if (goBtn) goBtn.addEventListener('click', () => launchItem(current));
        const skipBtn = host.querySelector('[data-sp-skip]');
        if (skipBtn) skipBtn.addEventListener('click', skipCurrent);
        const leaveBtn = host.querySelector('[data-sp-leave]');
        if (leaveBtn) leaveBtn.addEventListener('click', leave);
    }

    // ----------------------------------------
    // SKIPPING
    // ----------------------------------------

    // Moves on without the current activity counting as done — from the
    // checklist, or from the link above an embedded driller.
    function skipCurrent() {
        if (_embeddedDriller && typeof _embeddedDriller.stop === 'function') _embeddedDriller.stop();
        _embeddedDriller = null;
        const next = StudyPlan.skip();
        if (next && !(StudyPlan.isTimeUp() && !StudyPlan.overtime())) launchItem(next);
        else renderChecklist();
    }

    // The container an embedded activity renders into, with the skip link
    // above it.
    function _activityShell(host) {
        host.innerHTML = `
            <div class="sp-activity-bar"><button class="sp-skip-link" data-sp-skip="1">Skip this activity</button></div>
            <div id="study-plan-driller"></div>
        `;
        host.querySelector('[data-sp-skip]').addEventListener('click', skipCurrent);
    }

    // ----------------------------------------
    // LAUNCHING AN ITEM
    // ----------------------------------------

    async function launchItem(item) {
        _embeddedDriller = null;
        if (item.kind === 'grammar' && typeof GrammarDriller !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = GrammarDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing grammar practice…');
            try {
                await GrammarDriller.render(document.getElementById('study-plan-driller'), { skill: item.skill, count: item.count });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'vocabulary' && typeof VocabularyDriller !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = VocabularyDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing vocabulary practice…');
            try {
                await VocabularyDriller.render(document.getElementById('study-plan-driller'), { words: item.words });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'listening' && typeof ListeningDriller !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = ListeningDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing listening practice…');
            try {
                await ListeningDriller.render(document.getElementById('study-plan-driller'), { count: item.count || 5, level: item.level, autoStart: true });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'speaking' && typeof SpeakingDriller !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = SpeakingDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing speaking practice…');
            try {
                await SpeakingDriller.render(document.getElementById('study-plan-driller'), { count: item.count || 5, level: item.level, skill: item.skill, autoStart: true });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'speaking-cando' && typeof SpeakingDriller !== 'undefined') {
            // A single CEFR can-do prompt, auto-launched straight into
            // recording (same shortcut Journey's "unverified competencies"
            // nudge uses) rather than the full Sentence-Drills session the
            // 'speaking' kind above launches — this is the guaranteed quick
            // slot, not the budget-gated longer drill block.
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = SpeakingDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing speaking prompt…');
            try {
                await SpeakingDriller.render(document.getElementById('study-plan-driller'), {
                    targetCompetency: item.text,
                    level: item.level,
                    maxSeconds: item.seconds
                });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'match' && typeof DeckMatch !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            DeckMatch.render(document.getElementById('study-plan-driller'), {
                words: item.words,
                deckId: 'timed-session',
                srsCredit: true,
                exitLabel: 'Back to plan',
                timeLimit: item.timeLimit,
                onExit: () => {
                    renderChecklist();
                }
            });
            _embeddedDriller = DeckMatch;
        } else if (item.kind === 'translation' && typeof TranslationDriller !== 'undefined') {
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = TranslationDriller;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing translation practice…');
            try {
                await TranslationDriller.render(document.getElementById('study-plan-driller'), { count: item.count, level: item.level, autoStart: true });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'driller' && HU_DRILLERS[item.drillerId] && HU_DRILLERS[item.drillerId]()) {
            const mod = HU_DRILLERS[item.drillerId]();
            const host = activityHost();
            _activityShell(host);
            _embeddedDriller = mod;
            if (typeof UI !== 'undefined') UI.showLoading('Preparing practice…');
            try {
                await mod.render(document.getElementById('study-plan-driller'), { count: item.count, autoStart: true });
            } finally {
                if (typeof UI !== 'undefined') UI.hideLoading();
            }
        } else if (item.kind === 'verbs' && typeof Workshop !== 'undefined') {
            // The Verb Driller only renders inside Workshop's own DOM, so it
            // leaves this screen the way a review does.
            _leavingForActivity = true;
            goTab('drills');
            Workshop.open('verbs', Object.assign({ mode: 'speed', duration: item.seconds, autoStart: true }, item.tense ? { tense: item.tense } : {}));
        } else if (item.kind === 'reading' && typeof Reader !== 'undefined') {
            _leavingForActivity = true;
            goTab('reader');
            Reader.loadStory(item.storyId);
        } else if (item.kind === 'lesson' && typeof startLesson === 'function') {
            startLesson(item.lessonId);
        } else if (item.kind === 'test' && typeof LevelTest !== 'undefined') {
            LevelTest.open(item.level, {
                onExit: () => {
                    showTab('study-plan-screen');
                    renderChecklist();
                }
            });
        } else if (item.kind === 'review') {
            // Respect the time-based budget: only review the budgeted count
            // of words (e.g. 9 words for 5 min) so the learner is never trapped
            // in a large backlog during a finite micro-session.
            _leavingForActivity = true;
            goTab('review');
            if (typeof Decks !== 'undefined') Decks.reviewDeck('all', { limit: item.count });
        }
    }

    // The item one past the one currently finishing — what clicking the
    // results screen's button below is about to jump straight into. Reads
    // the queue without mutating it; advancing happens on click.
    function _peekNextItem() {
        const items = StudyPlan.items();
        return items[StudyPlan.currentIndex() + 1] || null;
    }

    // Called by RecommendationEngine.mountNextAction() whenever StudyPlan
    // is active, instead of it computing a fresh generic recommendation.
    // Names the next task and jumps straight into it on click — not just
    // back to the checklist, which would cost a second tap (the checklist's
    // own "[item] →" button) on top of this one. Embedded items
    // (grammar/vocabulary/listening/speaking/match) never actually left
    // #study-plan-screen, so launchItem() just re-renders in place; a
    // lesson/test/review item's results live elsewhere, so goTab() brings
    // #study-plan-screen back first — a same-tick DOM write launchItem()
    // immediately overwrites, so there's nothing to actually see mid-swap.
    async function mountNextAction(container) {
        if (!container) return;

        // Out of planned items with time left: plan one more now, so the
        // button can name it.
        const timeUp = StudyPlan.isTimeUp() && !StudyPlan.overtime();
        let nextItem = _peekNextItem();
        if (!nextItem && !timeUp) {
            await StudyPlan.extend();
            nextItem = _peekNextItem();
        }
        const label = (nextItem && !timeUp) ? `Next: ${itemLine(nextItem)}` : 'Finish session';

        const actionsEl = container.querySelector('.vspeed-results-actions') || container.querySelector('.sp-results-actions') || container.querySelector('.dkm-done-actions');
        if (actionsEl) {
            const playAgainBtn = actionsEl.querySelector('[data-action="play-again"]') || actionsEl.querySelector('[data-action="practice-again"]') || actionsEl.querySelector('[data-match-restart]');
            if (playAgainBtn) {
                playAgainBtn.classList.remove('vbtn-primary', 'sp-start-btn', 'btn-primary');
                playAgainBtn.classList.add('vbtn-secondary', 'dk-secondary');
            }
            const slot = document.createElement('div');
            slot.className = 'wk-next-action-slot';
            slot.innerHTML = `<button class="vbtn vbtn-primary wk-next-primary-btn" data-sp-next="1">${esc(label)} →</button>`;
            actionsEl.insertAdjacentElement('afterbegin', slot);
        } else {
            container.insertAdjacentHTML('beforeend', `
                <div class="wk-next-action">
                    <span class="wk-next-eyebrow">Your time-based session</span>
                    <button class="vbtn vbtn-primary wk-next-primary-btn" data-sp-next="1">${esc(label)} →</button>
                </div>
            `);
        }

        const btn = container.querySelector('[data-sp-next]');
        if (btn) {
            btn.addEventListener('click', () => {
                const next = StudyPlan.advance();
                goTab('study-plan-screen');
                if (next && !(StudyPlan.isTimeUp() && !StudyPlan.overtime())) launchItem(next);
                else renderChecklist();
            });
        }
    }

    // Fired by showTab()'s dispatch whenever #study-plan-screen becomes
    // visible (see engine/init.js) — the one path that reaches this screen
    // WITHOUT going through mountNextAction()'s explicit advance: a lesson
    // item's own "Done" button (closeLesson()'s lessonReturnTab already
    // points here, unmodified). Checked against real curriculum state
    // (LearnerPath.isComplete), not a guessed signal.
    function onEnter() {
        const item = StudyPlan.current();
        if (item && item.kind === 'lesson' && typeof LearnerPath !== 'undefined' && LearnerPath.isComplete(item.lessonId)) {
            StudyPlan.advance();
        }
        // A reading item only counts as done when the story was finished;
        // closed early, it stays current (the learner can resume or skip).
        if (item && item.kind === 'reading' && _returningFromReading && _readingFinished) {
            StudyPlan.advance();
        }
        _returningFromReading = false;
        _readingFinished = false;
        renderChecklist();
    }

    // ----------------------------------------
    // READING HAND-BACK
    // ----------------------------------------
    // The Reader has no results screen to mount a "Next" button on, so it
    // calls these instead (engine/reader.js's finishStory()/closeStory()).
    let _returningFromReading = false;
    let _readingFinished = false;

    function isReadingItem(storyId) {
        const item = StudyPlan.current();
        return !!(item && item.kind === 'reading' && item.storyId === storyId);
    }

    // Called by finishStory() — the story was read to the end, not just
    // closed.
    function markReadingFinished(storyId) {
        if (isReadingItem(storyId)) _readingFinished = true;
    }

    // Deferred a tick: closeStory() also runs when the learner leaves the
    // Library via the main nav (teardownTab), and by then the Library tab
    // is already hidden — that's leaving the session, not finishing a step.
    function onReadingClosed(storyId) {
        if (!isReadingItem(storyId)) return;
        setTimeout(() => {
            const readerTab = document.getElementById('reader');
            if (readerTab && !readerTab.classList.contains('hidden')) {
                _returningFromReading = true;
                goTab('study-plan-screen');
            } else {
                StudyPlan.discard();
            }
        }, 0);
    }

    // ----------------------------------------
    // COMPLETION / LEAVING
    // ----------------------------------------

    // Time ran out with planned items left — end here, offer the rest.
    function renderTimeUp() {
        const host = activityHost();
        if (!host) return;
        const left = StudyPlan.items().length - StudyPlan.currentIndex();
        const next = StudyPlan.current();

        host.innerHTML = `
            <div class="sp-complete">
                <p class="sp-complete-eyebrow">Time's up</p>
                <h2 class="sp-complete-title">That's your ${esc(StudyPlan.minutes())} minutes.</h2>
                <p class="sp-complete-summary">
                    You still have ${left} planned ${left === 1 ? 'activity' : 'activities'} — keep going if you like.
                </p>
                <button class="btn-primary" data-sp-finish="1">Finish session</button>
                <button class="dk-secondary" data-sp-more="1">Keep going: ${esc(itemLine(next))} →</button>
            </div>
        `;

        host.querySelector('[data-sp-finish]').addEventListener('click', renderCompletion);
        host.querySelector('[data-sp-more]').addEventListener('click', () => {
            StudyPlan.keepGoing();
            launchItem(next);
        });
    }

    function renderCompletion() {
        const host = activityHost();
        if (!host) return;

        const doneCount = StudyPlan.doneCount();
        const startedAt = StudyPlan.startedAt();
        const elapsed = startedAt ? formatElapsed(Date.now() - startedAt) : null;
        StudyPlan.discard();

        host.innerHTML = `
            <div class="sp-complete">
                <p class="sp-complete-eyebrow">Session complete</p>
                <h2 class="sp-complete-title">Nice work.</h2>
                <p class="sp-complete-summary">
                    ${doneCount} ${doneCount === 1 ? 'thing' : 'things'} done${elapsed ? ` in ${esc(elapsed)}` : ''}.
                </p>
                <button class="btn-primary" data-sp-home="1">Back to Home</button>
            </div>
        `;

        const homeBtn = host.querySelector('[data-sp-home]');
        if (homeBtn) homeBtn.addEventListener('click', backToHome);
    }

    function formatElapsed(ms) {
        const totalMinutes = Math.max(1, Math.round(ms / 60000));
        if (totalMinutes < 60) return `${totalMinutes} min`;
        const h = Math.floor(totalMinutes / 60);
        const m = totalMinutes % 60;
        return m ? `${h} hr ${m} min` : `${h} hr`;
    }

    function backToHome() {
        goTab('home');
    }

    // "Leave session" — always available, no confirmation gate, matches
    // "a clear start and end" rather than a productivity nag. Discards
    // rather than persisting; reopening the door starts a fresh plan.
    function leave() {
        StudyPlan.discard();
        backToHome();
    }

    // ----------------------------------------
    // BUDGET PICKER — entry from Home's door
    // ----------------------------------------
    // Same body-level overlay pattern as engine/decks.js's "Add to deck"
    // picker (.wp-overlay/.wp-sheet) — a bottom sheet independent of
    // whatever tab is showing, rather than a screen of its own. No
    // countdown anywhere in it: picking a minute value only sizes the plan
    // once, up front.
    const BUDGETS = [10, 15, 20, 30, 45, 60];

    function ensureBudgetPicker() {
        let el = document.getElementById('study-plan-picker');
        if (el) return el;
        el = document.createElement('div');
        el.id = 'study-plan-picker';
        document.body.appendChild(el);
        return el;
    }

    function closeBudgetPicker() {
        const el = document.getElementById('study-plan-picker');
        if (el) el.innerHTML = '';
    }

    function openBudgetPicker() {
        const host = ensureBudgetPicker();
        host.innerHTML = `
            <div class="wp-overlay" id="study-plan-picker-overlay">
                <div class="wp-sheet sp-budget-sheet">
                    <div class="wp-header">
                        <h2 class="wp-word">How much time do you have?</h2>
                        <button class="wp-close" data-sp-picker-close="1" aria-label="Close">×</button>
                    </div>
                    <div class="sp-budget-grid">
                        ${BUDGETS.map(m => `<button class="sp-budget-btn" data-sp-budget="${m}">${m} min</button>`).join('')}
                    </div>
                </div>
            </div>
        `;

        host.querySelectorAll('[data-sp-picker-close]').forEach(el => { el.onclick = closeBudgetPicker; });
        const overlay = document.getElementById('study-plan-picker-overlay');
        if (overlay) overlay.onclick = function (e) { if (e.target === overlay) closeBudgetPicker(); };

        host.querySelectorAll('[data-sp-budget]').forEach(btn => {
            btn.onclick = async function () {
                const minutes = Number(btn.getAttribute('data-sp-budget'));
                await StudyPlan.build(minutes);
                closeBudgetPicker();
                open();
            };
        });
    }

    // ----------------------------------------
    // ENTRY
    // ----------------------------------------

    function open() {
        document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
        const scr = screenEl();
        if (scr) scr.classList.remove('hidden');
        document.body.classList.add('in-lesson');
        document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
        renderChecklist();
    }

    // Called when the learner leaves this screen via the main nav instead
    // of its own "Leave session" control (see engine/init.js's
    // teardownTab()) — treated the same as an explicit leave (discards the
    // plan; navigating away is itself the "leave" gesture here, since this
    // screen has no nav button of its own to come back to it with), plus
    // resets whichever driller is currently embedded, same cleanup
    // Workshop.close() gives its own drillers but reached directly since
    // Workshop's own _active never sees a driller embedded here.
    function teardown() {
        document.body.classList.remove('in-lesson');
        if (_embeddedDriller && typeof _embeddedDriller.stop === 'function') _embeddedDriller.stop();
        _embeddedDriller = null;
        if (_leavingForActivity) {
            _leavingForActivity = false;
        } else {
            StudyPlan.discard();
        }
    }

    async function start(minutes) {
        await StudyPlan.build(minutes);
        open();
    }

    return { open, start, openBudgetPicker, mountNextAction, onEnter, teardown, isReadingItem, markReadingFinished, onReadingClosed };
})();
