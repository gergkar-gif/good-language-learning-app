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

// --------------------------------------------
// Learn page
// --------------------------------------------

function toggleLevel(level) {
    const body = document.getElementById(`${level}-lessons`);
    const arrow = document.getElementById(`${level}-arrow`);

    if (!body || !arrow) return;

    const open = body.style.display !== 'none';
    body.style.display = open ? 'none' : 'block';
    arrow.textContent = open ? '▶' : '▼';
}

function renderLearnPage(curriculum) {
    const root = document.getElementById('learn-content');
    if (!root) return;

    let html = '<h2 class="section-title">Your Path</h2>';
    html += '<p class="section-subtitle">All levels are open. Jump in anywhere.</p>';

    Object.entries(curriculum.levels).forEach(([level, data]) => {
        html += `
            <div class="level-section">
                <div class="level-header" data-level="${level.toLowerCase()}">
                    <div>
                        <h3>${data.title}</h3>
                        <p>${data.description || ''}</p>
                    </div>
                    <span class="level-arrow" id="${level.toLowerCase()}-arrow">▼</span>
                </div>
                <div id="${level.toLowerCase()}-lessons"></div>
            </div>
        `;
    });

    root.innerHTML = html;

    // Attach level toggle events (event delegation)
    root.addEventListener('click', e => {
        const header = e.target.closest('.level-header');
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
    const btn = document.getElementById('lesson-close-btn');
    if (btn) btn.addEventListener('click', closeLesson);

    const nextBtn = document.getElementById('lesson-next-btn');
    if (nextBtn) nextBtn.addEventListener('click', nextLessonStep);
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
    await loadDictionary();

    loadDeck();
    loadXP();
    updateXPHeader();

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