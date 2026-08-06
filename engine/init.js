// ============================================
// APP INITIALISATION
// ============================================

var LEVELS = ['a1','a2','b1','b2','c1'];

function showTab(tabName, button) {
    document.querySelectorAll('.tab').forEach(function (tab) {
        tab.classList.add('hidden');
    });

    var tab = document.getElementById(tabName);
    if (tab) tab.classList.remove('hidden');

    document.querySelectorAll('.nav button').forEach(function (btn) {
        btn.classList.remove('active');
    });

    if (!button && window.event) button = window.event.target;
    if (button) button.classList.add('active');

    if (tabName === 'reader' && typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }

    if (tabName === 'drills') {
        if (typeof Verbs !== 'undefined') Verbs.render();
    }

    if (tabName === 'review' && typeof showNextCard === 'function') {
        showNextCard();
    }
}

// --------------------------------------------
// Learn page
// --------------------------------------------

function toggleLevel(level) {
    var body = document.getElementById(level + '-lessons');
    var arrow = document.getElementById(level + '-arrow');

    if (!body || !arrow) return;

    var open = body.style.display !== 'none';
    body.style.display = open ? 'none' : 'block';
    arrow.textContent = open ? '\u25B6' : '\u25BC';
}

function renderLearnPage(curriculum) {
    var root = document.getElementById('learn-content');
    if (!root) return;

    var html = '<h2 class="section-title">Your Path</h2>';
    html += '<p class="section-subtitle">All levels are open. Jump in anywhere.</p>';

    Object.entries(curriculum.levels).forEach(function (entry) {
        var level = entry[0];
        var data  = entry[1];

        html += ''
            + '<div class="level-section">'
            +   '<div class="level-header" data-level="' + level.toLowerCase() + '">'
            +     '<div>'
            +       '<h3>' + data.title + '</h3>'
            +       '<p>' + (data.description || '') + '</p>'
            +     '</div>'
            +     '<span class="level-arrow" id="' + level.toLowerCase() + '-arrow">\u25BC</span>'
            +   '</div>'
            +   '<div id="' + level.toLowerCase() + '-lessons"></div>'
            + '</div>';
    });

    root.innerHTML = html;

    // Attach level toggle events (event delegation)
    root.addEventListener('click', function (e) {
        var header = e.target.closest('.level-header');
        if (header) {
            toggleLevel(header.dataset.level);
        }
    });

    // Render A1 lessons (others empty for now)
    if (typeof renderA1Lessons === 'function') {
        renderA1Lessons(curriculum.levels.A1.lessons);
    }
}

// --------------------------------------------
// Lesson close button (replaces inline onclick)
// --------------------------------------------

function _attachLessonClose() {
    var btn = document.getElementById('lesson-close-btn');
    if (btn) btn.addEventListener('click', closeLesson);

    var nextBtn = document.getElementById('lesson-next-btn');
    if (nextBtn) nextBtn.addEventListener('click', nextLessonStep);
}

// --------------------------------------------
// Nav delegation (replaces inline onclick)
// --------------------------------------------

function _attachNavEvents() {
    document.querySelector('.nav').addEventListener('click', function (e) {
        var btn = e.target.closest('button[data-tab]');
        if (btn) showTab(btn.dataset.tab, btn);
    });
}

// --------------------------------------------
// Startup
// --------------------------------------------

async function initialiseApp() {

    await loadDictionary();

    loadDeck();
    loadXP();
    updateXPHeader();

    var response = await fetch('content/curriculum/curriculum.json');
    var curriculum = await response.json();

    window._curriculumData = curriculum;

    // Nav
    _attachNavEvents();

    // Learn page
    renderLearnPage(curriculum);

    if (typeof renderCurriculum === 'function') {
        renderCurriculum();
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
