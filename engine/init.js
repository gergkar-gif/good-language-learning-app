// ============================================
// APP INITIALISATION
// ============================================

const LEVELS = ['a1', 'a2', 'b1', 'b2', 'c1'];

function showTab(tabName, button) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
    const tab = document.getElementById(tabName);
    if (tab) tab.classList.remove('hidden');

    document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
    if (!button && window.event) button = window.event.target;
    if (button) button.classList.add('active');

    // The header is contextual — it names the room you just walked into.
    if (typeof PageHeader !== 'undefined') PageHeader.show(tabName);

    if (tabName === 'reader' && typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }

    if (tabName === 'drills' && typeof Verbs !== 'undefined') {
        Verbs.render();
    }

    // Decks opens on the browser, not mid-session: arriving at a flashcard
    // you did not ask for is disorienting, and the point of the tab now is
    // choosing what to study.
    if (tabName === 'review' && typeof Decks !== 'undefined') {
        if (typeof endReviewSession === 'function') endReviewSession();
        else Decks.render();
    }

    // Rendered on entry rather than kept up to date: everything on it is
    // counted from data the rest of the app owns, so the only moment it can
    // be wrong is the moment you walk in.
    if (tabName === 'journey' && typeof Journey !== 'undefined') {
        Journey.render();
    }
}

// The Learn page is rendered by engine/curriculum.js. An earlier accordion
// version lived here (renderLearnPage/toggleLevel); nothing called it once
// renderCurriculum took over, and the level list replaced it entirely.

// --------------------------------------------
// Lesson close button (replaces inline onclick)
// --------------------------------------------

function _attachLessonClose() {
    const btn = document.getElementById('lesson-close-btn');
    if (btn) btn.addEventListener('click', closeLesson);

    // The Continue button is not bound here: renderStep() sets its onclick
    // every step, because the last step has to call finishLesson instead. A
    // listener here as well fired alongside that onclick, so one press
    // advanced two steps and the learner never saw every other screen.
}

// --------------------------------------------
// Nav delegation (replaces inline onclick)
// --------------------------------------------

function _attachNavEvents() {
    document.querySelector('.nav').addEventListener('click', e => {
        const btn = e.target.closest('button[data-tab]');
        if (btn) showTab(btn.dataset.tab, btn);
    });
}

// --------------------------------------------
// Startup
// --------------------------------------------

async function initialiseApp() {
    loadDeck();
    loadXP();
    updateXPHeader();

    // Learn is the landing section, so its header is the first one drawn.
    if (typeof PageHeader !== 'undefined') PageHeader.show('learn');

    // Falls back to the default course when the chosen one has no content.
    window._curriculumData = await loadCurriculumData();

    // Nav
    _attachNavEvents();

    // Learn page
    if (typeof renderCurriculum === 'function') {
        try {
            await renderCurriculum();
        } catch (e) {
            console.error('Failed to render curriculum:', e);
        }
    }

    // Lesson screen events
    _attachLessonClose();

    // Verbs module
    if (typeof Verbs !== 'undefined') {
        Verbs.init();
    }

    if (typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }
}

document.addEventListener('DOMContentLoaded', initialiseApp);