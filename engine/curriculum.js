// ============================================
// CURRICULUM RENDERER
// ============================================
// Two views in the Learn tab: a list of levels, and one level's lessons.
// Levels are entered rather than expanded in place — five accordions open at
// once buried the lesson you actually wanted.

// Line icons rather than emoji: they take the level's colour, so the icon,
// the spine and the progress bar all read as one object.
const LEVEL_ICONS = {
    A1: '<path d="M12 20v-7m0 0c0-3-2-5-5-5H4c0 3 2 5 5 5h3Zm0 0c0-3.3 2.7-6 6-6h2c0 3.3-2.7 6-6 6h-2Z"/>',
    A2: '<path d="M4 6.5A2.5 2.5 0 0 1 6.5 4h11A2.5 2.5 0 0 1 20 6.5v7a2.5 2.5 0 0 1-2.5 2.5H9l-5 4V6.5Z"/>',
    B1: '<circle cx="12" cy="12" r="8.5"/><path d="m15 9-2 4.5L8.5 15l2-4.5L15 9Z"/>',
    B2: '<path d="M3 18.5 9 8l4 6.5M11 18.5 15.5 10l5.5 8.5H3"/>',
    C1: '<path d="m12 3.5 2.6 5.6 6 .8-4.4 4.2 1.1 6.1L12 17.3l-5.3 2.9 1.1-6.1L3.4 9.9l6-.8L12 3.5Z"/>'
};

const LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1'];

// Which level's lessons are on screen; null means the level list.
let openLevel = null;

function levelIcon(level) {
    return '<svg class="level-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
        (LEVEL_ICONS[level] || LEVEL_ICONS.A1) + '</svg>';
}

function levelStats(lessons, progress) {
    const done = lessons.filter(l => progress[l.id]).length;
    return {
        done: done,
        total: lessons.length,
        percent: lessons.length ? Math.round((done / lessons.length) * 100) : 0
    };
}

// The chosen course may have no content yet — content/hu exists as an empty
// folder — and a 404 here used to reject with a JSON parse error that killed
// startup before anything rendered, leaving a blank page that a reload could
// not fix, because the choice is saved. Fall back to the default course and
// say so instead.
async function loadCurriculumData() {
    try {
        const res = await fetch(Lang.content('curriculum/curriculum.json'));
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return await res.json();
    } catch (error) {
        if (Lang.code() === Lang.defaultCode()) throw error;

        // By the time this runs, other modules have already read the wrong
        // course — the reader has failed to load its manifest, the SRS deck
        // has been read from an empty key. Re-fetching the curriculum alone
        // would leave those stale for the rest of the session, so start over
        // with the corrected language. This can only happen once: after the
        // reload the language is the default, and this branch is not reached.
        console.warn(`No ${Lang.name()} course content yet — restarting on the default course.`, error);
        Lang.set(Lang.defaultCode());
        location.reload();
        return new Promise(() => {});   // halt startup; the reload takes over
    }
}

async function renderCurriculum() {
    if (!window._curriculumData) {
        window._curriculumData = await loadCurriculumData();
    }

    const root = document.getElementById('learn-content');
    if (!root) return;

    root.innerHTML = openLevel ? levelDetailHtml(openLevel) : levelListHtml();
    attachCurriculumEvents(root);
}

function levelListHtml() {
    const progress = getProgress();
    const levels = window._curriculumData.levels;

    const cards = LEVEL_ORDER.filter(l => levels[l]).map(level => {
        const data = levels[level];
        const stats = levelStats(data.lessons || [], progress);

        return `
            <button class="level-card" data-open-level="${level}" data-level="${level}">
                <span class="level-card-spine"></span>
                ${levelIcon(level)}
                <span class="level-card-body">
                    <span class="level-card-title">${UI.escape(data.title || level)}</span>
                    <span class="level-card-sub">${level} · ${UI.escape(data.description || '')}</span>
                    <span class="level-card-meter">
                        <span class="level-card-track">
                            <span class="level-card-fill" style="width:${stats.percent}%"></span>
                        </span>
                        <span class="level-card-count">${stats.done} / ${stats.total} lessons</span>
                    </span>
                </span>
                <span class="level-card-chevron" aria-hidden="true">›</span>
            </button>
        `;
    }).join('');

    // No heading here — the page header already says "Lessons".
    return `<div class="level-list">${cards}</div>`;
}

function levelDetailHtml(level) {
    const progress = getProgress();
    const data = window._curriculumData.levels[level];
    const lessons = data.lessons || [];
    const stats = levelStats(lessons, progress);

    // The first unfinished lesson is the one to pick up next.
    const currentIndex = lessons.findIndex(l => !progress[l.id]);

    const rows = lessons.map((lesson, i) => {
        const done = !!progress[lesson.id];
        const current = i === currentIndex;
        const minutes = lesson.estimatedMinutes ? lesson.estimatedMinutes + ' min' : '';
        const state = done ? 'done' : current ? 'current' : 'todo';

        return `
            <li>
                <button class="lesson-row is-${state}" data-start-lesson="${UI.escape(lesson.id)}">
                    <span class="lesson-row-num">${UI.escape(lesson.label || String(i + 1).padStart(2, '0'))}</span>
                    <span class="lesson-row-title">${UI.escape(lesson.title)}</span>
                    <span class="lesson-row-time">${minutes}</span>
                    <span class="lesson-row-state" aria-label="${state}">${
                        done ? '✓' : current ? '▶' : ''
                    }</span>
                </button>
            </li>
        `;
    }).join('');

    // The test closes the level, so it sits after the lessons rather than
    // beside them — and it reports its own state, because a passed level is
    // the one thing on this screen that is not simply "lessons finished".
    const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(level) : null;
    const testRow = `
        <button class="level-test-row${result && result.passed ? ' is-passed' : ''}"
                data-open-test="${level}">
            <span class="level-test-title">${level} level test</span>
            <span class="level-test-meta">${
                result
                    ? `${result.correct} / ${result.total}${result.passed ? ' · passed' : ''}`
                    : '20 questions · 80% to move on'
            }</span>
        </button>
    `;

    return `
        <div class="level-detail" data-level="${level}">
            <button class="level-back" data-close-level="1">← All levels</button>

            <header class="level-detail-head">
                ${levelIcon(level)}
                <span class="level-detail-titles">
                    <span class="level-card-title">${UI.escape(data.title || level)}</span>
                    <span class="level-card-sub">${level} · ${UI.escape(data.description || '')}</span>
                </span>
                <span class="level-detail-progress">
                    <span class="level-card-count">${stats.done} / ${stats.total} lessons</span>
                    <span class="progress-ring" style="--pct:${stats.percent}">
                        <span class="progress-ring-label">${stats.percent}%</span>
                    </span>
                </span>
            </header>

            ${lessons.length
                ? `<ol class="lesson-rows">${rows}</ol>${testRow}`
                : '<p class="text-muted level-empty">No lessons at this level yet.</p>'}
        </div>
    `;
}

function attachCurriculumEvents(root) {
    root.addEventListener('click', e => {
        const open = e.target.closest('[data-open-level]');
        if (open) {
            openLevel = open.getAttribute('data-open-level');
            renderCurriculum();
            return;
        }

        if (e.target.closest('[data-close-level]')) {
            openLevel = null;
            renderCurriculum();
            return;
        }

        const start = e.target.closest('[data-start-lesson]');
        if (start) startLesson(start.getAttribute('data-start-lesson'));

        const test = e.target.closest('[data-open-test]');
        if (test && typeof LevelTest !== 'undefined') {
            LevelTest.open(test.getAttribute('data-open-test'));
        }
    });
}
