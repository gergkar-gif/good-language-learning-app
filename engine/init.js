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

    // Home is entirely counted from data other modules own, so it is redrawn
    // on entry rather than kept up to date. Walking back onto it after a
    // lesson is exactly when every number on it has just changed.
    if (tabName === 'home' && typeof Home !== 'undefined') {
        Home.render();
    }

    // Re-render on entry rather than trusting what was drawn last time. The
    // level list carries state the rest of the app changes — a finished
    // lesson, a passed level test — and coming back to a stale list is how a
    // pass appears not to have registered.
    if (tabName === 'learn' && typeof renderCurriculum === 'function') {
        renderCurriculum();
    }

    if (tabName === 'reader' && typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }

    if (tabName === 'drills' && typeof Workshop !== 'undefined') {
        Workshop.render();
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

// Icons are put in from the registry rather than written into the markup, so
// there is one place a shape is defined and index.html stays readable.
function _drawNavIcons() {
    if (typeof Art === 'undefined') return;
    document.querySelectorAll('.nav button[data-icon]').forEach(btn => {
        const label = btn.textContent.trim();
        btn.innerHTML = Art.icon(btn.dataset.icon) +
            '<span class="nav-label">' + label + '</span>';
    });
}

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
    loadKnownWords();
    loadXP();
    updateXPHeader();

    // Home is the landing section, so its header is the first one drawn.
    if (typeof PageHeader !== 'undefined') PageHeader.show('home');

    // Falls back to the default course when the chosen one has no content.
    window._curriculumData = await loadCurriculumData();

    // Nav
    _drawNavIcons();
    _attachNavEvents();

    // Learn page. Drawn at startup even though Home is what is on screen —
    // the Lessons tab is one tap away and should not arrive empty.
    if (typeof renderCurriculum === 'function') {
        try {
            await renderCurriculum();
        } catch (e) {
            console.error('Failed to render curriculum:', e);
        }
    }

    // Home page. After the curriculum, which it reads to name the next lesson.
    if (typeof Home !== 'undefined') {
        try {
            await Home.render();
        } catch (e) {
            console.error('Failed to render home:', e);
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