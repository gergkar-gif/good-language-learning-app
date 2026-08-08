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

    if (tabName === 'review' && typeof showNextCard === 'function') {
        showNextCard();
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

    // Updated path to include language prefix
    const response = await fetch('content/es/curriculum/curriculum.json');
    const curriculum = await response.json();

    window._curriculumData = curriculum;

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