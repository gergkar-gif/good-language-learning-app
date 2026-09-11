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

    // A review plan item is the one kind launched via goTab() — the normal
    // showTab()-driven tab switch, which tears down whatever tab it's
    // leaving (see engine/init.js's teardownTab()). Without this flag,
    // launching a review item would look identical to the learner
    // navigating away to abandon the plan, and get its own plan discarded
    // out from under it before the review even starts. Set immediately
    // before that one goTab() call, cleared as soon as teardown() reads it.
    let _leavingForReview = false;

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

    function renderChecklist() {
        const host = activityHost();
        if (!host) return;
        _embeddedDriller = null;

        if (!StudyPlan.isActive()) {
            renderCompletion();
            return;
        }

        const items = StudyPlan.items();
        const index = StudyPlan.currentIndex();
        const skip = StudyPlan.skipped();
        const current = items[index];

        const rows = items.map((item, i) => `
            <li class="sp-item ${i < index ? 'sp-item-done' : ''} ${i === index ? 'sp-item-current' : ''}">
                <span class="sp-item-check">${i < index ? '✓' : i + 1}</span>
                <span class="sp-item-label">${esc(itemLine(item))}</span>
            </li>
        `).join('');

        host.innerHTML = `
            <div class="sp-checklist">
                <p class="sp-checklist-eyebrow">${esc(StudyPlan.minutes())}-minute session</p>
                <ul class="sp-item-list">${rows}</ul>
                ${skip ? `<p class="sp-skipped">${esc(skipText(skip))}</p>` : ''}
                <button class="btn-primary" data-sp-go="1">${esc(itemLine(current))} →</button>
                <button class="dk-secondary" data-sp-leave="1">Leave session</button>
            </div>
        `;

        const goBtn = host.querySelector('[data-sp-go]');
        if (goBtn) goBtn.addEventListener('click', () => launchItem(current));
        const leaveBtn = host.querySelector('[data-sp-leave]');
        if (leaveBtn) leaveBtn.addEventListener('click', leave);
    }

    // ----------------------------------------
    // LAUNCHING AN ITEM
    // ----------------------------------------

    function launchItem(item) {
        _embeddedDriller = null;
        if (item.kind === 'grammar' && typeof GrammarDriller !== 'undefined') {
            const host = activityHost();
            host.innerHTML = '<div id="study-plan-driller"></div>';
            GrammarDriller.render(document.getElementById('study-plan-driller'), { skill: item.skill, count: item.count });
            _embeddedDriller = GrammarDriller;
        } else if (item.kind === 'vocabulary' && typeof VocabularyDriller !== 'undefined') {
            const host = activityHost();
            host.innerHTML = '<div id="study-plan-driller"></div>';
            VocabularyDriller.render(document.getElementById('study-plan-driller'), { words: item.words });
            _embeddedDriller = VocabularyDriller;
        } else if (item.kind === 'lesson' && typeof startLesson === 'function') {
            startLesson(item.lessonId);
        } else if (item.kind === 'test' && typeof LevelTest !== 'undefined') {
            // Known v1 limitation: LevelTest.open() always returns to the
            // Lessons tab on its own exit, not back to this screen — a
            // plan containing a test item ends here if the learner takes
            // it. Rare in practice (only ever appears right at a level
            // gate) and not something this module can fix without also
            // changing engine/leveltest.js's own hardcoded return.
            LevelTest.open(item.level);
        } else if (item.kind === 'review') {
            // Reviews are not truncated to the estimated count — once
            // started, the existing whole-due-deck review flow runs to its
            // own natural end, same as a lesson does. Consistent with the
            // roadmap's own "no countdown, time is a planning constraint"
            // framing: the budget only sizes what gets queued up front.
            _leavingForReview = true;
            goTab('review');
            if (typeof Decks !== 'undefined') Decks.reviewDeck('all');
        }
    }

    // Called by RecommendationEngine.mountNextAction() whenever StudyPlan
    // is active, instead of it computing a fresh generic recommendation.
    // The one thing every item kind needs on its own results/summary
    // screen: a way back into this one. Embedded items (grammar/vocabulary)
    // never actually left #study-plan-screen, so this just re-renders in
    // place; review's own summary lives on the #review tab and genuinely
    // navigates back.
    function mountNextAction(container) {
        if (!container) return;
        container.insertAdjacentHTML('beforeend', `
            <div class="wk-next-action">
                <span class="wk-next-eyebrow">Your time-based session</span>
                <button class="wk-next-btn" data-sp-next="1">Back to your plan →</button>
            </div>
        `);
        const btn = container.querySelector('[data-sp-next]');
        if (btn) {
            btn.addEventListener('click', () => {
                StudyPlan.advance();
                goTab('study-plan-screen');
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
        renderChecklist();
    }

    // ----------------------------------------
    // COMPLETION / LEAVING
    // ----------------------------------------

    function renderCompletion() {
        const host = activityHost();
        if (!host) return;

        const doneCount = StudyPlan.items().length;
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
        if (_embeddedDriller && typeof _embeddedDriller.stop === 'function') _embeddedDriller.stop();
        _embeddedDriller = null;
        if (_leavingForReview) {
            _leavingForReview = false;
        } else {
            StudyPlan.discard();
        }
    }

    return { open, openBudgetPicker, mountNextAction, onEnter, teardown };
})();
