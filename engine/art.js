// ============================================
// ART
// ============================================
// Every illustration in Parlour, in one place. They are frontispieces rather
// than decoration: each is built from a handful of primitives — circles,
// rectangles, lines, arcs, triangles — and states one idea by metaphor rather
// than depiction. Roughly three quarters of each composition is deliberately
// empty, and the accent colour is rationed to a single element so it never
// competes with the page title.
//
// Vectors, not images: the whole set below is a few kilobytes, needs no
// requests, and — because every shape takes its colour from a CSS class
// rather than a literal fill — follows the palette wherever it changes.
//
// Only five classes exist, so a composition cannot quietly introduce a sixth
// colour: ink-solid, ink-line, ink-rule, ink-hair, accent-solid, accent-line.
// They are defined once, in styles/layout.css.
//
// All compositions are drawn to a 320x100 viewBox with the ground at y=86.

const Art = (function () {
    'use strict';

    const SECTIONS = {

        // Lessons — structured progression. A path opening out of a horizon,
        // perspective lines converging on a single point ahead. You stand at
        // the near edge; the accent marks where the course is going.
        path: `
            <line class="ink-hair" x1="14" y1="86" x2="306" y2="86"/>
            <g class="ink-hair">
                <line x1="30" y1="86" x2="286" y2="40"/>
                <line x1="46" y1="86" x2="286" y2="40"/>
                <line x1="66" y1="86" x2="286" y2="40"/>
                <line x1="90" y1="86" x2="286" y2="40"/>
                <line x1="118" y1="86" x2="286" y2="40"/>
                <line x1="150" y1="86" x2="286" y2="40"/>
                <line x1="186" y1="86" x2="286" y2="40"/>
                <line x1="226" y1="86" x2="286" y2="40"/>
            </g>
            <path class="ink-solid" d="M34 86a30 30 0 0 1 60 0Z"/>
            <circle class="accent-solid" cx="286" cy="40" r="6"/>
        `,

        // Library — shelves becoming a landscape. Upright volumes on a ground
        // line, a sun standing behind them. One spine is left open rather than
        // filled: the book you have not read yet.
        horizon: `
            <circle class="accent-solid" cx="214" cy="46" r="26"/>
            <line class="ink-hair" x1="40" y1="86" x2="280" y2="86"/>
            <rect class="ink-solid" x="96" y="46" width="15" height="40"/>
            <rect class="ink-solid" x="115" y="34" width="12" height="52"/>
            <rect class="ink-solid" x="131" y="52" width="17" height="34"/>
            <rect class="ink-solid" x="152" y="28" width="13" height="58"/>
            <rect class="ink-solid" x="169" y="42" width="15" height="44"/>
            <rect class="ink-line" x="188" y="56" width="14" height="30"/>
        `,

        // Workshop — building skill. A beam tilted off the level; the navy
        // circle is the balance point resting on it, the orange square the
        // weight thrown to one side. Practice is the beam finding level.
        balance: `
            <line class="ink-hair" x1="40" y1="88" x2="280" y2="88"/>
            <line class="ink-rule" x1="66" y1="70" x2="266" y2="38"/>
            <circle class="ink-solid" cx="166" cy="54" r="10"/>
            <rect class="accent-solid" x="222" y="18" width="26" height="26"/>
        `,

        // Decks — memory through repetition. The same form recurring, each
        // pass a little further back; only the nearest is fully filled in,
        // and the one at the back is the card coming round again.
        stack: `
            <line class="ink-hair" x1="40" y1="90" x2="280" y2="90"/>
            <rect class="accent-line" x="176" y="24" width="44" height="62" rx="3"/>
            <rect class="ink-line" x="152" y="24" width="44" height="62" rx="3"/>
            <rect class="ink-line" x="128" y="24" width="44" height="62" rx="3"/>
            <rect class="ink-solid" x="104" y="24" width="44" height="62" rx="3"/>
        `,

        // My Journey — distance already covered. A path that winds rather than
        // steps: every segment is a cubic with horizontal tangents at both
        // ends, so the line rises and then levels at each node instead of
        // turning a corner there. That is what learning a language is shaped
        // like, and the flat that follows a climb is as much a part of it as
        // the climb. It dips once on purpose — no honest account only goes up.
        //
        // Each node is a place the learner actually stood. The line runs in
        // from the left without one, because the beginning is not an
        // achievement. The orange square stands off the last node rather
        // than on it: a destination ahead, not a badge for what's done.
        ascent: `
            <line class="ink-hair" x1="40" y1="86" x2="280" y2="86"/>
            <path class="ink-rule" d="M44 78C76 78 76 56 108 56C128 56 128 62 148 62C170 62 170 42 192 42C214 42 214 32 236 32"/>
            <circle class="ink-solid" cx="108" cy="56" r="4"/>
            <circle class="ink-solid" cx="148" cy="62" r="4"/>
            <circle class="ink-solid" cx="192" cy="42" r="4"/>
            <circle class="ink-solid" cx="236" cy="32" r="4"/>
            <line class="ink-rule" x1="236" y1="32" x2="236" y2="14"/>
            <rect class="accent-solid" x="228" y="4" width="16" height="16"/>
        `,

        // Home — the door the whole app is named for. A threshold standing
        // open, an accent semicircle rising behind it — arrival, not
        // departure. The accent dot sits where a handle would: the point at
        // which you push it open.
        threshold: `
            <line class="ink-hair" x1="20" y1="86" x2="300" y2="86"/>
            <path class="accent-solid" d="M110 86a40 40 0 0 1 80 0Z"/>
            <rect class="ink-line" x="176" y="18" width="72" height="68"/>
            <path class="ink-solid" d="M176 18 140 30v62l36-6Z"/>
            <circle class="accent-solid" cx="168" cy="60" r="4"/>
        `,

        // Lesson complete — one climb just made, not the whole journey
        // (that's ascent, on My Journey). A single rise from the small
        // hollow-feeling point where the learner started this lesson to
        // the solid accent circle where they now stand — the arrival, not
        // the path still ahead of it.
        summit: `
            <line class="ink-hair" x1="60" y1="86" x2="260" y2="86"/>
            <path class="ink-rule" d="M84 78C124 78 124 50 174 50"/>
            <circle class="ink-solid" cx="84" cy="78" r="4"/>
            <circle class="accent-solid" cx="174" cy="50" r="7"/>
        `,

        // levelA1..levelC1 (hero-scale level identity art) removed
        // 2026-08-14 — unused since Art.svg('level'+level, ...) was dropped
        // from both curriculum.js call sites when the Lessons hero art was
        // removed at the user's request the same day. LEVEL_ICONS in
        // curriculum.js is the only level-identity art left.
    };


    // ----------------------------------------
    // ICONS
    // ----------------------------------------
    // 24x24, stroked rather than filled: at nav size a filled shape turns
    // into a blob and the hairlines that give a frontispiece its depth
    // disappear altogether. Each one is the section's illustration reduced to
    // the single gesture that survives being drawn at twenty pixels — the
    // Library's shelf of spines, the Workshop's beam over a fulcrum — so the
    // icon and the header read as the same idea at two sizes.
    //
    // No accent: an icon is a label, and a red dot in a row of five competes
    // with whichever one is actually selected.

    const ICONS = {

        // Home — a door standing open, the mark the app is named for.
        home: `
            <rect class="ink-line" x="4" y="3" width="16" height="18"/>
            <path class="ink-line" d="M4 3 12 6v15l-8-3Z"/>
            <circle class="ink-solid" cx="10" cy="12" r="1"/>
        `,

        // Lessons — the path out to a vanishing point.
        lessons: `
            <line class="ink-line" x1="2" y1="19" x2="22" y2="19"/>
            <line class="ink-line" x1="6" y1="19" x2="15" y2="6"/>
            <line class="ink-line" x1="14" y1="19" x2="16" y2="6"/>
            <circle class="ink-solid" cx="15.5" cy="5" r="1.5"/>
        `,

        // Library — spines on a shelf.
        library: `
            <line class="ink-line" x1="3" y1="20" x2="21" y2="20"/>
            <rect class="ink-line" x="5" y="8" width="3.4" height="12"/>
            <rect class="ink-line" x="10.3" y="5" width="3.4" height="15"/>
            <rect class="ink-line" x="15.6" y="10" width="3.4" height="10"/>
        `,

        // Workshop — a beam, a circle resting on it as the balance point, a
        // square weighing down one end. Line, circle, square.
        workshop: `
            <line class="ink-line" x1="3" y1="21" x2="21" y2="21"/>
            <line class="ink-line" x1="4" y1="16" x2="20" y2="8"/>
            <circle class="ink-line" cx="12" cy="12" r="2.5"/>
            <rect class="ink-line" x="15" y="4" width="5" height="5"/>
        `,

        // Decks — cards receding.
        decks: `
            <rect class="ink-line" x="3" y="6" width="12" height="15" rx="1.5"/>
            <path class="ink-line" d="M7 4h11a1.5 1.5 0 0 1 1.5 1.5v13"/>
        `,

        // My Journey — the winding climb, reduced to two bends and a square
        // destination. The dip survives at illustration size but not at this
        // one, where it would read as a wobble in the stroke rather than as
        // a setback.
        journey: `
            <path class="ink-line" d="M2.5 19.5c4 0 3.5-5.5 7-5.5s3-6 6.5-6"/>
            <line class="ink-line" x1="16" y1="8" x2="16" y2="4"/>
            <rect class="ink-line" x="13" y="1" width="6" height="6"/>
        `,

        // Reader — an open book, the Library's shelf turned to face you.
        reader: `
            <path class="ink-line" d="M12 7v14"/>
            <path class="ink-line" d="M12 7C10 5 7 4.5 3 5v13c4-.5 7 0 9 2"/>
            <path class="ink-line" d="M12 7c2-2 5-2.5 9-2v13c-4-.5-7 0-9 2"/>
        `,

        // Grammar — the paradigm, which is what a grammar screen owes you.
        grammar: `
            <rect class="ink-line" x="3" y="4" width="18" height="16" rx="1.5"/>
            <line class="ink-line" x1="3" y1="9" x2="21" y2="9"/>
            <line class="ink-line" x1="10" y1="9" x2="10" y2="20"/>
        `,

        // Listening — sound, drawn as the levels of a waveform.
        listening: `
            <line class="ink-line" x1="4" y1="10" x2="4" y2="14"/>
            <line class="ink-line" x1="8" y1="7" x2="8" y2="17"/>
            <line class="ink-line" x1="12" y1="4" x2="12" y2="20"/>
            <line class="ink-line" x1="16" y1="8" x2="16" y2="16"/>
            <line class="ink-line" x1="20" y1="11" x2="20" y2="13"/>
        `,

        // Sound effects on/off — a speaker with (or without) the two arcs
        // of sound leaving it. Reuses the same speaker cone as `listening`
        // draws for its waveform bars, kept as one glyph pair so "on" and
        // "off" read as the same control, not two different icons.
        soundOn: `
            <path class="ink-line" d="M4 9v6h4l6 5V4l-6 5Z"/>
            <path class="ink-line" d="M17 8.5a5.5 5.5 0 0 1 0 7"/>
            <path class="ink-line" d="M19.5 6a9 9 0 0 1 0 12"/>
        `,
        soundOff: `
            <path class="ink-line" d="M4 9v6h4l6 5V4l-6 5Z"/>
            <line class="ink-line" x1="16" y1="9" x2="21" y2="14"/>
            <line class="ink-line" x1="21" y1="9" x2="16" y2="14"/>
        `,

        // Settings — a dial with one mark, rather than a cog nobody can read
        // at this size.
        settings: `
            <circle class="ink-line" cx="12" cy="12" r="8"/>
            <circle class="ink-line" cx="12" cy="12" r="3"/>
            <line class="ink-line" x1="12" y1="4" x2="12" y2="1.5"/>
        `,

        // Shuffle — two strands crossing, each ending in an arrowhead: order
        // going in, a different order coming out.
        shuffle: `
            <polyline class="ink-line" points="3 17 8 17 20 6"/>
            <polyline class="ink-line" points="15 6 20 6 20 11"/>
            <polyline class="ink-line" points="3 7 8 7 20 18"/>
            <polyline class="ink-line" points="15 18 20 18 20 13"/>
        `,

        // Flag — a pennant on a pole, for reporting a problem. Filled with
        // the accent rather than left as an outline: unlike the nav row
        // (see the note above), this icon stands alone and is meant to
        // read as "something needs attention" at a glance.
        flag: `
            <line class="ink-line" x1="6" y1="21" x2="6" y2="3"/>
            <path class="accent-solid" d="M6 4 19 4 15 8 19 12 6 12Z"/>
        `
    };

    function icon(id, className) {
        const art = ICONS[id];
        if (!art) return '';
        return `
            <svg class="art icon ${className || ''}" viewBox="0 0 24 24"
                role="presentation" aria-hidden="true" focusable="false">
                ${art}
            </svg>
        `;
    }

    function iconIds() {
        return Object.keys(ICONS);
    }

    function section(id) {
        return SECTIONS[id] || '';
    }

    // A complete standalone <svg> for an illustration, for callers outside the
    // page header. Decorative by default: it carries the idea the title has
    // already stated in words, so a screen reader gains nothing by reading it.
    function svg(id, className) {
        const art = section(id);
        if (!art) return '';
        return `
            <svg class="art ${className || 'page-header-art'}" viewBox="0 0 320 100"
                preserveAspectRatio="xMidYMid meet"
                role="presentation" aria-hidden="true" focusable="false">
                ${art}
            </svg>
        `;
    }

    function ids() {
        return Object.keys(SECTIONS);
    }

    return { section, svg, ids, icon, iconIds };
})();
