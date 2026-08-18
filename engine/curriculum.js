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
// mountain, no star. Five levels as one fixed set, reused everywhere a
// level appears (level list, lesson header). Rebuilt 2026-08-14 onto the
// same disc formula as the path/driller art (PATH_SHAPES in this file,
// DRILLER_ICONS in engine/workshop.js) at the user's request, so level
// identity, path nodes and driller marks all read as one visual family:
// a --wash circle base, one --ink structural shape, exactly one --accent
// element. See [[preferred-disc-art-language]].
const LEVEL_ICONS = {
    // A1 — a solid semicircle with a mast rising from its centre.
    A1: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M14 62a36 36 0 0 1 72 0Z" class="ps-ink"/><line class="ps-line" x1="50" y1="62" x2="50" y2="14"/><circle cx="50" cy="14" r="7" class="ps-accent"/>',
    // A2 — a disc with a wedge cut from its centre.
    A2: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 50 8A42 42 0 0 1 89 71Z" class="ps-ink"/><circle cx="89" cy="71" r="7" class="ps-accent"/>',
    // B1 — a disc bisected diagonally, a dot at the chord's end.
    B1: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M79.7 20.3A42 42 0 0 1 20.3 79.7Z" class="ps-ink"/><circle cx="79.7" cy="20.3" r="7" class="ps-accent"/>',
    // B2 — an outline angle with a smaller filled triangle nested in it.
    B2: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path class="ps-line" d="M18 78 50 20 82 78"/><path d="M34 78 50 50 66 78Z" class="ps-ink"/><circle cx="50" cy="20" r="6" class="ps-accent"/>',
    // C1 — a diagonal line rising to a dot.
    C1: '<circle cx="50" cy="50" r="42" class="ps-wash"/><line class="ps-line" x1="18" y1="82" x2="76" y2="24"/><circle cx="76" cy="24" r="7" class="ps-accent"/>'
};

const LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1'];

// Which level and unit are on screen; null means "one level up".
let openLevel = null;
let openUnit = null;

function levelIcon(level, extraClass) {
    return '<svg class="level-icon' + (extraClass ? ' ' + extraClass : '') + '" viewBox="0 0 100 100" aria-hidden="true">' +
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

    // The unit path and the unit's lesson list both mark the learner's next
    // stop with .is-current — on a level with dozens of units, or a unit
    // split into many lessons, that can sit well below the fold. Land there
    // directly instead of leaving the learner to scroll and hunt for it.
    const current = root.querySelector('.is-current');
    if (current) current.scrollIntoView({ block: 'center' });
}

function levelListHtml() {
    const progress = getProgress();
    const levels = window._curriculumData.levels;

    const cards = LEVEL_ORDER.filter(l => levels[l]).map(level => {
        const data = levels[level];
        const stats = progressStats(levelLessons(data), progress);

        // The code is the row's heading and the name its gloss — this is a
        // list of levels, so the code is what identifies one. No ordinal
        // number: LEVEL_ORDER's position was never meaningful to a learner.
        return `
            <button class="level-card" data-open-level="${level}" data-level="${level}">
                ${levelIcon(level, 'level-icon--lg')}
                <span class="level-card-body">
                    <span class="level-card-code">${level}</span>
                    <span class="level-card-title">${UI.escape(data.title || level)}</span>
                    <span class="level-card-sub">${UI.escape(data.description || '')}</span>
                    <span class="level-card-meter">
                        <span class="level-card-track">
                            <span class="level-card-fill" style="width:${stats.percent}%"></span>
                        </span>
                        <span class="level-card-count">${stats.done} / ${stats.total}</span>
                    </span>
                </span>
                <span class="level-card-arrow" aria-hidden="true"></span>
            </button>
        `;
    }).join('');

    // No heading here — the page header already says "Lessons".
    return `<div class="level-list">${cards}</div>`;
}


// A hand-drawn-feeling line connecting one node per unit — added 2026-08-14
// (visual identity v2), replacing the card list for the unit-list screen
// specifically (the level list one step up stays cards; see design
// principles.md). The wave is generated, not hand-placed, so it holds up
// for any unit count without per-level tuning.
// Units sit strictly at alternating extremes of the swing rather than at
// samples of a sine wave. Two reasons, and the second is the load-bearing
// one: it gives the bold serpentine of the reference, and it means every
// node has the *whole* opposite half of the column free for its shape and
// its label — a node sampled near the centre line has the least room of
// any, which is what forced the artwork small before.
//
// x is emitted as a bare -1/+1 multiplier, not pixels, so the swing width
// can be a CSS variable and widen with the viewport (see --path-amp).
function unitPathPoints(count, spacing) {
    const points = [];
    for (let i = 0; i < count; i++) {
        points.push({ sx: i % 2 === 0 ? -1 : 1, y: 56 + i * spacing });
    }
    return points;
}

// One cubic per gap, with both control points held on their own point's
// vertical. That leaves the curve vertical where it meets each node and
// fully horizontal halfway between, which is the wide sweep in the
// reference — and it keeps the line inside the band its points span, so it
// never runs under the labels sitting outside that band.
function curveThrough(points) {
    if (points.length < 2) return '';
    let d = `M ${points[0].x} ${points[0].y}`;
    for (let i = 0; i < points.length - 1; i++) {
        const dy = (points[i + 1].y - points[i].y) * 0.5;
        d += ` C ${points[i].x} ${points[i].y + dy},` +
             ` ${points[i + 1].x} ${points[i + 1].y - dy},` +
             ` ${points[i + 1].x} ${points[i + 1].y}`;
    }
    return d;
}

function serpentineD(points, norm, capY) {
    const pts = points.map(p => ({ x: p.sx * norm, y: p.y }));
    return `M ${pts[0].x} ${capY} L ${pts[0].x} ${pts[0].y}` +
        curveThrough(pts).replace(/^M [^C]*/, ' ');
}

// Two-tone discs for both path types — single-track and dual-track alike —
// distinct from LEVEL_ICONS, which stay reserved for level *identity* (nav,
// the level list, hero art) where repetition is the point. Every entry is a
// circle (--wash base) with an ink shape and one accent element, so the
// path reads as a gallery of related compositions rather than one icon
// stamped down the page. Fourteen of them, each also used mirrored (see
// pathArt), so nothing repeats inside 28 units.
//
// Was two separate sets — square-boxed shapes for the single-track path,
// discs for the dual-track one — until the user said they preferred the
// disc look and asked for it everywhere (2026-08-14). Unified rather than
// kept in sync by hand.
const PATH_SHAPES = [
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 8A42 42 0 0 1 50 92Z" class="ps-ink"/><circle cx="34" cy="62" r="7" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 50 8A42 42 0 0 1 86 71Z" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M79.7 20.3A42 42 0 0 1 20.3 79.7Z" class="ps-ink"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="50" y="50" width="34" height="34" class="ps-accent"/><line class="ps-line" x1="50" y1="6" x2="50" y2="94"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M8 50A42 42 0 0 1 92 50Z" class="ps-ink"/><circle cx="50" cy="50" r="8" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 50 8A42 42 0 0 0 14 71Z" class="ps-ink"/><rect x="62" y="62" width="22" height="22" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M20.3 20.3A42 42 0 0 1 79.7 79.7Z" class="ps-ink"/><circle cx="70" cy="28" r="7" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 8A42 42 0 0 1 92 50L50 50Z" class="ps-ink"/><line class="ps-line" x1="6" y1="72" x2="94" y2="72"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M8 58A42 42 0 0 0 92 58Z" class="ps-ink"/><circle cx="8" cy="58" r="6" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><circle cx="50" cy="50" r="24" class="ps-line"/><circle cx="50" cy="50" r="8" class="ps-accent"/>',
    '<circle cx="42" cy="54" r="34" class="ps-wash"/><circle cx="74" cy="30" r="18" class="ps-ink"/><circle cx="74" cy="30" r="5" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 20 20 80 20Z" class="ps-ink"/><rect x="70" y="12" width="12" height="12" class="ps-accent"/>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 8A42 42 0 0 1 84 30L50 50Z" class="ps-ink"/><g class="ps-rules"><line x1="12" y1="70" x2="88" y2="70"/><line x1="18" y1="80" x2="82" y2="80"/></g>',
    '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 92 50A42 42 0 0 1 50 92Z" class="ps-ink"/><rect x="42" y="10" width="16" height="16" class="ps-accent"/>'
];

// Each shape is used twice — once as drawn, once mirrored — before the set
// comes round again, so a 20- or 36-unit level never shows the same
// composition twice anywhere near itself.
function pathArt(index, artClass) {
    const shape = PATH_SHAPES[index % PATH_SHAPES.length];
    const flipped = Math.floor(index / PATH_SHAPES.length) % 2 === 1;
    return `<svg class="${artClass}${flipped ? ' is-flip' : ''}" viewBox="0 0 100 100" aria-hidden="true">${shape}</svg>`;
}

function unitPathHtml(level, units, progress) {
    if (!units.length) return '';

    // The horizontal swing is a CSS length (--path-amp); NORM is only the
    // viewBox's own half-width, which the SVG then stretches to that
    // length. Keeping it normalised is what lets the swing be responsive.
    const NORM = 100;
    const spacing = 200;
    const points = unitPathPoints(units.length, spacing);
    const height = points[points.length - 1].y + 56;

    // The line runs on above the first unit and is capped with a dot, so it
    // reads as a route already under way rather than something that starts
    // abruptly at unit one.
    const capY = 14;
    const pathD = serpentineD(points, NORM, capY);

    // "Current" is the first unit not yet finished — the one the path is
    // visibly leading to. Everything before it is done; everything after is
    // upcoming. Clicking any of them still works the same as before.
    const firstOpenIndex = units.findIndex(u => progressStats(u.lessons || [], progress).percent < 100);
    const currentIndex = firstOpenIndex === -1 ? units.length - 1 : firstOpenIndex;

    const nodes = units.map((unit, i) => {
        const stats = progressStats(unit.lessons || [], progress);
        const status = stats.percent === 100 ? 'done' : i === currentIndex ? 'current' : 'upcoming';
        // Content hangs off the side the path is *not* swinging towards, so
        // it always runs into the open half of the column rather than off
        // the edge — and it alternates on its own, because the wave does.
        const side = points[i].sx < 0 ? 'right' : 'left';
        return `
            <button class="unit-path-node is-${status} is-${side}"
                    style="--sx:${points[i].sx}; --y:${points[i].y}px"
                    data-open-unit="${UI.escape(unit.id)}">
                ${pathArt(i, 'unit-path-art')}
                <span class="unit-path-text">
                    <span class="unit-path-num">${UI.escape(String(unit.label).padStart(2, '0'))}</span>
                    <span class="unit-path-title">${UI.escape(unit.title)}</span>
                    <span class="unit-path-count">${stats.total} ${stats.total === 1 ? 'lesson' : 'lessons'}</span>
                </span>
            </button>
        `;
    }).join('');

    // The cap is a DOM element, not an SVG circle: the swing is stretched
    // horizontally by preserveAspectRatio="none", which would draw any
    // circle inside the viewBox as an ellipse.
    return `
        <div class="unit-path" style="--path-h:${height}px">
            <svg class="unit-path-line" viewBox="${-NORM} 0 ${NORM * 2} ${height}"
                 preserveAspectRatio="none" aria-hidden="true">
                <path d="${pathD}"/>
            </svg>
            <span class="unit-path-cap" style="--sx:${points[0].sx}; --y:${capY}px" aria-hidden="true"></span>
            ${nodes}
        </div>
    `;
}

// The two tracks braid down one shared path rather than sitting in separate
// columns. Columns were the earlier arrangement and they could not survive
// the wider swing: two paths side by side in the 500px shell gave 214px
// each, and the nodes overflowed. Interleaving them into a single
// composition gives each row the full column, and the crossing lines are
// what the reference actually shows.
//
// Colour carries which track a unit belongs to; side is only layout. The
// tracks are rarely the same length (B1 currently runs 36 Core against 2
// Latin America), so once the shorter one is exhausted the remaining units
// simply alternate sides as a single-track path would.
function dualTrackPathHtml(level, data, units, progress) {
    const NORM = 100;
    const spacing = 158;

    // Where each line sits when crossing a row belonging to another track,
    // as a multiple of the node swing. These have to be *asymmetric*: if
    // both lines bow by the same amount in opposite directions they stay
    // perfectly nested and never actually cross, which is a parallel weave,
    // not a braid. Measured 0 crossings before this was tuned.
    //
    // The deep -1.5 overshoot stays behind the other track's disc rather
    // than reaching its label: the disc spans amp ± art/2, which is -60px
    // to +16px at mobile, and -1.5 × 22px = -33px falls inside it.
    const BOW = [-1.5, 0.4];

    const byTrack = data.tracks.map(t => units.filter(u => u.track === t.id));
    if (!byTrack.some(a => a.length)) {
        return '<p class="text-muted level-empty">No units yet.</p>';
    }

    // Interleave one unit per track at a time, then whatever is left over.
    const rows = [];
    const longest = Math.max(...byTrack.map(a => a.length));
    for (let i = 0; i < longest; i++) {
        byTrack.forEach((arr, ti) => {
            if (arr[i]) rows.push({ unit: arr[i], ti: ti });
        });
    }

    // While more than one track is still running, each keeps its own side.
    const braidEnd = rows.reduce((last, r, i) => (r.ti !== 0 ? i : last), -1);
    rows.forEach((r, i) => {
        r.y = 60 + i * spacing;
        r.sx = i <= braidEnd ? (r.ti === 0 ? 1 : -1)
                             : ((i - braidEnd) % 2 === 1 ? -1 : 1);
    });

    const height = rows[rows.length - 1].y + 60;

    // One line per track. Through its own units it passes at full swing;
    // across a row belonging to another track it bows over the centre line,
    // which is what makes the two cross.
    const lines = data.tracks.map((track, ti) => {
        const own = rows.filter(r => r.ti === ti);
        if (!own.length) return '';
        const first = rows.indexOf(own[0]);
        const last = rows.indexOf(own[own.length - 1]);
        const pts = rows.slice(first, last + 1).map(r => ({
            x: (r.ti === ti ? r.sx : (BOW[ti] === undefined ? 0 : BOW[ti])) * NORM,
            y: r.y
        }));
        return `<path class="dtp-line dtp-line--t${ti}" d="${curveThrough(pts)}"/>`;
    }).join('');

    const firstOpen = rows.findIndex(r => progressStats(r.unit.lessons || [], progress).percent < 100);
    const currentRow = firstOpen === -1 ? rows.length - 1 : firstOpen;

    const nodes = rows.map((r, i) => {
        const stats = progressStats(r.unit.lessons || [], progress);
        const status = stats.percent === 100 ? 'done' : i === currentRow ? 'current' : 'upcoming';
        const side = r.sx < 0 ? 'left' : 'right';
        return `
            <button class="dtp-node is-t${r.ti} is-${status} is-${side}"
                    style="--sx:${r.sx}; --y:${r.y}px"
                    data-open-unit="${UI.escape(r.unit.id)}">
                ${pathArt(i, 'dtp-art')}
                <span class="dtp-text">
                    <span class="dtp-num">${UI.escape(String(r.unit.label).padStart(2, '0'))}</span>
                    <span class="dtp-title">${UI.escape(r.unit.title)}</span>
                    <span class="dtp-track">${UI.escape(data.tracks[r.ti].title)}</span>
                    <span class="dtp-count">${stats.total} ${stats.total === 1 ? 'lesson' : 'lessons'}</span>
                </span>
            </button>
        `;
    }).join('');

    const legend = data.tracks.map((t, ti) =>
        `<span class="dtp-key"><span class="dtp-key-line dtp-key-line--t${ti}"></span>${UI.escape(t.title)}</span>`
    ).join('');

    return `
        <div class="dtp">
            <div class="dtp-legend">${legend}</div>
            <div class="dtp-path" style="--dtp-h:${height}px">
                <svg class="dtp-lines" viewBox="${-NORM} 0 ${NORM * 2} ${height}"
                     preserveAspectRatio="none" aria-hidden="true">${lines}</svg>
                ${nodes}
            </div>
        </div>
    `;
}

function unitListHtml(level) {
    const progress = getProgress();
    const data = window._curriculumData.levels[level];
    const units = data.units || [];

    const unitsHtml = data.tracks
        ? dualTrackPathHtml(level, data, units, progress)
        : unitPathHtml(level, units, progress);

    const levelStats = progressStats(levelLessons(data), progress);

    // This screen had no title of its own — you arrived from the level list
    // and the page header still says "Lessons", so nothing named the level
    // you were actually in. The name alone: the description repeats the
    // level list you just came from, and the count is already in the
    // summary below the path.
    const headHtml = `
        <div class="unit-path-head">
            <h2 class="unit-path-head-title">${level} · ${UI.escape(data.title || '')}</h2>
        </div>
    `;

    const summaryHtml = `
        <div class="unit-path-summary">
            <span class="unit-path-summary-dot" aria-hidden="true"></span>
            <span class="unit-path-summary-text">${levelStats.done} / ${levelStats.total} lessons completed</span>
            <span class="unit-path-summary-track">
                <span class="unit-path-summary-fill" style="width:${levelStats.percent}%"></span>
            </span>
            <span class="unit-path-summary-pct">${levelStats.percent}%</span>
        </div>
    `;

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
            ${headHtml}
            ${units.length
                ? `${unitsHtml}${summaryHtml}${testRow}`
                : '<p class="text-muted level-empty">No units at this level yet.</p>'}
        </div>
    `;
}

function lessonRowsHtml(lessons, progress, unitLabel) {
    // The first unfinished lesson is the one to pick up next.
    const currentIndex = lessons.findIndex(l => !progress[l.id]);

    return lessons.map((lesson, i) => {
        const done = !!progress[lesson.id];
        const current = i === currentIndex;
        const state = done ? 'done' : current ? 'current' : 'todo';

        // Numbered within the unit — "1.4" rather than "04" — so a lesson
        // reads as a step of this unit rather than a standalone item.
        const num = unitLabel ? `${unitLabel}.${i + 1}` : (lesson.label || String(i + 1).padStart(2, '0'));

        return `
            <li>
                <button class="ud-lesson is-${state}" data-start-lesson="${UI.escape(lesson.id)}">
                    <span class="ud-lesson-node" aria-hidden="true"></span>
                    <span class="ud-lesson-num">${UI.escape(num)}</span>
                    <span class="ud-lesson-title">${UI.escape(lesson.title)}</span>
                    <span class="ud-lesson-mark" aria-label="${state}"></span>
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

    // Which track this unit belongs to, when the level runs more than one.
    const track = (data.tracks || []).find(t => t.id === unit.track);

    // One mark per lesson — the unit's shape at a glance, above the list
    // that spells it out.
    const dots = lessons.map((l, i) =>
        `<span class="ud-dot${progress[l.id] ? ' is-done' : ''}" aria-hidden="true"></span>`
    ).join('');

    return `
        <div class="level-detail" data-level="${level}" data-unit="${UI.escape(unit.id)}">
            <button class="level-back" data-close-unit="1">← ${UI.escape(data.title || level)}</button>

            <header class="ud-head">
                <span class="ud-num">${UI.escape(String(unit.label).padStart(2, '0'))}</span>
                <h2 class="ud-title">${UI.escape(unit.title)}</h2>
                ${track ? `<span class="ud-track">${UI.escape(track.title)}</span>` : ''}
                <span class="ud-count">${stats.total} ${stats.total === 1 ? 'lesson' : 'lessons'}</span>
            </header>

            ${lessons.length ? `<div class="ud-dots">${dots}</div>` : ''}

            ${lessons.length
                ? `<h3 class="ud-section">Unit path</h3>
                   <ol class="ud-lessons">${lessonRowsHtml(lessons, progress, unit.label)}</ol>`
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
