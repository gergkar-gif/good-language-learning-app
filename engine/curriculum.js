// ============================================
// CURRICULUM RENDERER
// ============================================
// Three views in the Learn tab: a list of levels, a level's units, and one
// unit's lessons. Levels and units are entered rather than expanded in
// place — five accordions open at once buried the lesson you actually
// wanted. A unit with only one lesson skips its own detail screen and opens
// straight into that lesson, since there is nothing to browse first — most
// of A1 is still one lesson per unit while the rest gets split.

// Abstract, not pictograms: no sprout, no speech bubble, no compass, no
// mountain, no star. Five levels as one geometric sequence instead — point,
// line, angle, plane, and plane-with-circle — echoing Kandinsky's own
// "Point and Line to Plane". Nothing here draws a *picture* of anything;
// each level is just further along the same vocabulary the one before it
// used, which is what "the levels are a sequence" (below) already asked for.
// They take the level's colour, so the icon, the spine and the progress bar
// all read as one object.
const LEVEL_ICONS = {
    // A1 — the point. A ring around a single dot: presence, nothing moving yet.
    A1: '<circle cx="12" cy="12" r="7"/><circle cx="12" cy="12" r="2" fill="currentColor" stroke="none"/>',
    // A2 — the line. The point sets off in a direction.
    A2: '<line x1="5" y1="18" x2="17" y2="7"/><circle cx="17" cy="7" r="2.2" fill="currentColor" stroke="none"/>',
    // B1 — the angle. The line bends: a direction is chosen.
    B1: '<path d="M6 18 12 7 18 18"/><circle cx="12" cy="7" r="2" fill="currentColor" stroke="none"/>',
    // B2 — the plane. The angle closes into a shape and stands on its own.
    B2: '<path d="M12 5 19 18 5 18Z"/>',
    // C1 — synthesis. The plane overlapped by a circle: point, line and
    // plane combined into one composition.
    C1: '<path d="M9 4 17 19 3 19Z"/><circle cx="16" cy="13" r="6"/>'
};

const LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1'];

// Which level and unit are on screen; null means "one level up".
let openLevel = null;
let openUnit = null;

function levelIcon(level, extraClass) {
    return '<svg class="level-icon' + (extraClass ? ' ' + extraClass : '') + '" viewBox="0 0 24 24" ' +
        'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" ' +
        'stroke-linejoin="round" aria-hidden="true">' +
        (LEVEL_ICONS[level] || LEVEL_ICONS.A1) + '</svg>';
}

// Every lesson in a level, in teaching order, regardless of which unit it
// sits in — what "how much of this level is done" has always meant.
function levelLessons(levelData) {
    return (levelData.units || []).flatMap(u => u.lessons || []);
}

function progressStats(lessons, progress) {
    const done = lessons.filter(l => progress[l.id]).length;
    return {
        done: done,
        total: lessons.length,
        percent: lessons.length ? Math.round((done / lessons.length) * 100) : 0
    };
}

function unitById(levelData, unitId) {
    return (levelData.units || []).find(u => u.id === unitId) || null;
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

    root.innerHTML = !openLevel ? levelListHtml()
        : !openUnit ? unitListHtml(openLevel)
        : unitDetailHtml(openLevel, openUnit);

    attachCurriculumEvents(root);
}

function levelListHtml() {
    const progress = getProgress();
    const levels = window._curriculumData.levels;

    const cards = LEVEL_ORDER.filter(l => levels[l]).map(level => {
        const data = levels[level];
        const stats = progressStats(levelLessons(data), progress);

        return `
            <button class="level-card" data-open-level="${level}" data-level="${level}">
                <span class="level-card-spine"></span>
                <span class="level-card-num" aria-hidden="true">${String(LEVEL_ORDER.indexOf(level) + 1).padStart(2, '0')}</span>
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
                <span class="level-card-arrow geo-triangle" aria-hidden="true"></span>
            </button>
        `;
    }).join('');

    // No heading here — the page header already says "Lessons".
    return `<div class="level-list">${cards}</div>`;
}

// A level's units — the middle screen, new for the unit restructure. Visual
// language matches the level list on purpose: a unit is the same kind of
// object as a level, one step down.
function unitListHtml(level) {
    const progress = getProgress();
    const data = window._curriculumData.levels[level];
    const units = data.units || [];

    const cards = units.map(unit => {
        const stats = progressStats(unit.lessons || [], progress);
        return `
            <button class="level-card unit-card" data-open-unit="${UI.escape(unit.id)}">
                <span class="level-card-spine"></span>
                <span class="unit-card-num" aria-hidden="true">${UI.escape(unit.label)}</span>
                ${levelIcon(level, 'level-icon--sm')}
                <span class="level-card-body">
                    <span class="level-card-title">${UI.escape(unit.title)}</span>
                    <span class="level-card-meter">
                        <span class="level-card-track">
                            <span class="level-card-fill" style="width:${stats.percent}%"></span>
                        </span>
                        <span class="level-card-count">${stats.done} / ${stats.total}
                            ${stats.total === 1 ? 'lesson' : 'lessons'}</span>
                    </span>
                </span>
                <span class="level-card-arrow geo-triangle" aria-hidden="true"></span>
            </button>
        `;
    }).join('');

    // The test closes the level, so it sits after every unit rather than
    // inside one — and it reports its own state, because a passed level is
    // the one thing on this screen that is not simply "units finished".
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
        <div class="unit-list-view" data-level="${level}">
            <button class="level-back" data-close-level="1">← All levels</button>
            <div class="level-hero">${(typeof Art !== 'undefined') ? Art.svg('level' + level, 'level-hero-art') : ''}</div>
            ${units.length
                ? `<div class="level-list">${cards}</div>${testRow}`
                : '<p class="text-muted level-empty">No units at this level yet.</p>'}
        </div>
    `;
}

function lessonRowsHtml(lessons, progress) {
    // The first unfinished lesson is the one to pick up next.
    const currentIndex = lessons.findIndex(l => !progress[l.id]);

    return lessons.map((lesson, i) => {
        const done = !!progress[lesson.id];
        const current = i === currentIndex;
        const state = done ? 'done' : current ? 'current' : 'todo';

        return `
            <li>
                <button class="lesson-row is-${state}" data-start-lesson="${UI.escape(lesson.id)}">
                    <span class="lesson-row-num">${UI.escape(lesson.label || String(i + 1).padStart(2, '0'))}</span>
                    <span class="lesson-row-title">${UI.escape(lesson.title)}</span>
                    <span class="lesson-row-state" aria-label="${state}">${
                        done ? '✓' : current ? '▶' : ''
                    }</span>
                </button>
            </li>
        `;
    }).join('');
}

function unitDetailHtml(level, unitId) {
    const progress = getProgress();
    const data = window._curriculumData.levels[level];
    const unit = unitById(data, unitId);
    if (!unit) return unitListHtml(level);

    const lessons = unit.lessons || [];
    const stats = progressStats(lessons, progress);

    return `
        <div class="level-detail" data-level="${level}" data-unit="${UI.escape(unit.id)}">
            <button class="level-back" data-close-unit="1">← ${UI.escape(data.title || level)}</button>

            <header class="level-detail-head">
                <span class="unit-card-num unit-detail-num" aria-hidden="true">${UI.escape(unit.label)}</span>
                ${levelIcon(level)}
                <span class="level-detail-titles">
                    <span class="level-card-title">${UI.escape(unit.title)}</span>
                    <span class="level-card-sub">${level}</span>
                </span>
                <span class="level-detail-progress">
                    <span class="level-card-count">${stats.done} / ${stats.total}
                        ${stats.total === 1 ? 'lesson' : 'lessons'}</span>
                    <span class="progress-ring" style="--pct:${stats.percent}">
                        <span class="progress-ring-label">${stats.percent}%</span>
                    </span>
                </span>
            </header>

            ${lessons.length
                ? `<ol class="lesson-rows">${lessonRowsHtml(lessons, progress)}</ol>`
                : '<p class="text-muted level-empty">No lessons in this unit yet.</p>'}
        </div>
    `;
}

function attachCurriculumEvents(root) {
    // root.innerHTML is replaced on every render, but root itself is not —
    // without this guard, every renderCurriculum() call bound a fresh
    // listener on top of the ones already there. Harmless while every branch
    // just re-renders, but startLesson() has real side effects (hiding every
    // tab, showing the lesson screen), and two concurrent calls racing each
    // other could leave that in a state neither call intended on its own.
    if (root.dataset.wired) return;
    root.dataset.wired = '1';

    root.addEventListener('click', e => {
        const open = e.target.closest('[data-open-level]');
        if (open) {
            openLevel = open.getAttribute('data-open-level');
            openUnit = null;
            renderCurriculum();
            return;
        }

        if (e.target.closest('[data-close-level]')) {
            openLevel = null;
            openUnit = null;
            renderCurriculum();
            return;
        }

        const openUnitBtn = e.target.closest('[data-open-unit]');
        if (openUnitBtn) {
            const unitId = openUnitBtn.getAttribute('data-open-unit');
            const data = window._curriculumData.levels[openLevel];
            const unit = unitById(data, unitId);

            // A unit that is still one lesson has nothing to browse — go
            // straight to the lesson rather than a detail screen with one row.
            if (unit && unit.lessons && unit.lessons.length === 1) {
                startLesson(unit.lessons[0].id);
                return;
            }

            openUnit = unitId;
            renderCurriculum();
            return;
        }

        if (e.target.closest('[data-close-unit]')) {
            openUnit = null;
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
