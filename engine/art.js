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
        // achievement. A small pennant flies off the last node rather than
        // sitting on it: a destination ahead, not a badge for what's done —
        // the same notched-pennant shape as the bug-report flag icon, just
        // scaled up and planted on its own pole.
        ascent: `
            <line class="ink-hair" x1="40" y1="86" x2="280" y2="86"/>
            <path class="ink-rule" d="M44 78C76 78 76 56 108 56C128 56 128 62 148 62C170 62 170 42 192 42C214 42 214 32 236 32"/>
            <circle class="ink-solid" cx="108" cy="56" r="4"/>
            <circle class="ink-solid" cx="148" cy="62" r="4"/>
            <circle class="ink-solid" cx="192" cy="42" r="4"/>
            <circle class="ink-solid" cx="236" cy="32" r="4"/>
            <line class="ink-rule" x1="236" y1="32" x2="236" y2="8"/>
            <path class="accent-solid" d="M236 8 256 8 248 13.5 256 19 236 19Z"/>
        `,

        // Home — the door the whole app is named for. Redrawn 2026-09-16 to
        // match a reference: a full accent dome, a door split into a solid
        // near leaf and an open one — unfilled rather than a seventh
        // colour, so the cream page shows through where the door stands
        // ajar — and the accent dot where a handle would be.
        threshold: `
            <line class="ink-hair" x1="14" y1="86" x2="306" y2="86"/>
            <path class="accent-solid" d="M204 86A46 46 0 0 1 296 86Z"/>
            <rect class="ink-solid" x="224" y="40" width="26" height="46"/>
            <rect class="ink-line" x="250" y="40" width="26" height="46"/>
            <circle class="accent-solid" cx="245" cy="64" r="3"/>
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

        // My Journey — the winding climb, reduced to two bends and a flagged
        // destination. The dip survives at illustration size but not at this
        // one, where it would read as a wobble in the stroke rather than as
        // a setback. The flag is one closed triangle rather than the hero's
        // notched pennant — a swallowtail notch would just blur out at this
        // size, so the plain point is what actually reads as "flag" here.
        journey: `
            <path class="ink-line" d="M2.5 19.5c4 0 3.5-5.5 7-5.5s3-6 6.5-6"/>
            <path class="ink-line" d="M16 8V2l5 2.5Z"/>
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

        // Time-based session — a clock face, the one icon in this set that
        // names a constraint rather than a place or activity.
        clock: `
            <circle class="ink-line" cx="12" cy="12" r="9"/>
            <path class="ink-line" d="M12 7v5l4 2"/>
        `,

        // Word Bank — a label tag, the mark of one word held for reference.
        wordBank: `
            <path class="ink-line" d="M3 12 12 3h7a2 2 0 0 1 2 2v7L12 21 3 12Z"/>
            <circle class="ink-solid" cx="16" cy="8" r="1.5"/>
        `,

        // Speaking — microphone capsule on a cradle with an accent voice beacon
        speaking: `
            <rect class="ink-line" x="9" y="3" width="6" height="11" rx="3"/>
            <path class="ink-line" d="M5 10a7 7 0 0 0 14 0"/>
            <line class="ink-line" x1="12" y1="17" x2="12" y2="21"/>
            <line class="ink-line" x1="8" y1="21" x2="16" y2="21"/>
            <circle class="accent-solid" cx="19" cy="5" r="1.5"/>
        `,
        mic: `
            <rect class="ink-line" x="9" y="3" width="6" height="11" rx="3"/>
            <path class="ink-line" d="M5 10a7 7 0 0 0 14 0"/>
            <line class="ink-line" x1="12" y1="17" x2="12" y2="21"/>
            <line class="ink-line" x1="8" y1="21" x2="16" y2="21"/>
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
        play: `
            <polygon class="ink-line" fill="currentColor" points="8 5, 19 12, 8 19"/>
        `,
        pause: `
            <rect class="ink-line" fill="currentColor" x="6" y="5" width="4" height="14"/>
            <rect class="ink-line" fill="currentColor" x="14" y="5" width="4" height="14"/>
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
        `,

        // Theme: Light mode (clean, minimalist radiant disc with hairlines)
        themeLight: `
            <circle class="ink-line" cx="12" cy="12" r="4"/>
            <line class="ink-line" x1="12" y1="2" x2="12" y2="4.5"/>
            <line class="ink-line" x1="12" y1="19.5" x2="12" y2="22"/>
            <line class="ink-line" x1="2" y1="12" x2="4.5" y2="12"/>
            <line class="ink-line" x1="19.5" y1="12" x2="22" y2="12"/>
            <line class="ink-line" x1="4.93" y1="4.93" x2="6.7" y2="6.7"/>
            <line class="ink-line" x1="17.3" y1="17.3" x2="19.07" y2="19.07"/>
            <line class="ink-line" x1="4.93" y1="19.07" x2="6.7" y2="17.3"/>
            <line class="ink-line" x1="17.3" y1="6.7" x2="19.07" y2="4.93"/>
        `,

        // Theme: Dark mode (clean, minimalist geometric crescent)
        themeDark: `
            <path class="ink-line" d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79Z"/>
        `,

        // Theme: System / Contrast (bisected circle: half outline, half solid ink)
        themeSystem: `
            <circle class="ink-line" cx="12" cy="12" r="9"/>
            <path class="ink-solid" d="M12 3v18a9 9 0 0 0 0-18Z"/>
        `,

        // Check — minimalist stroked checkmark
        check: `
            <polyline class="ink-line" points="4 12 9 17 20 6"/>
        `,

        // Alert / Warning — minimalist circle with hairline indicator
        alert: `
            <circle class="ink-line" cx="12" cy="12" r="9"/>
            <line class="ink-line" x1="12" y1="8" x2="12" y2="12"/>
            <circle class="ink-solid" cx="12" cy="16" r="1"/>
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

    // ----------------------------------------
    // THE COMPOSED ROOM (visual overhaul, 2026-09-29)
    // ----------------------------------------
    // Page heroes, nav icons, level marks and generated unit/story marks. All
    // drawn from sand discs, navy shapes and hairlines with ONE accent, whose
    // colour follows state (see DESIGN.md, "Colour semantics"). Classes are
    // defined in styles/overhaul.css: mk-sand, mk-navy, mk-line (its
    // stroke-width is set per shape), mk-acc, mk-accline, mk-pine, mk-pineline
    // for illustration; nv-navy, nv-line, nv-acc, nv-accline for the nav.
    // Heroes are drawn to a 252 x 184 viewBox with the ground at y=170.

    const HEROES = {
        home: `<circle class="mk-sand" cx="184" cy="72" r="64"/><path class="mk-line" stroke-width="1.2" d="M128 62A108 108 0 0 1 236 170"/><path class="mk-navy" d="M128 62V170H202z"/><path class="mk-line" stroke-width="2" d="M128 40V170M128 62H236"/><path class="mk-line" stroke-width="1.2" d="M202 170 116 46"/><g class="rise"><circle class="mk-acc" cx="149" cy="142" r="6"/></g><path class="mk-line" stroke-width="1.2" d="M20 170h232"/>`,
        lessons: `<circle class="mk-sand" cx="176" cy="52" r="70"/><path class="mk-navy" d="M44 170a72 72 0 0 1 144 0z"/><path class="mk-line" stroke-width="1.2" d="M96 118 204 44M188 170 204 44M20 170h232"/><g class="rise"><circle class="mk-acc" cx="204" cy="44" r="8"/></g>`,
        library: `<circle class="mk-sand" cx="176" cy="64" r="58"/><rect class="mk-navy" x="96" y="92" width="15" height="78"/><rect class="mk-navy" x="118" y="48" width="15" height="122"/><rect class="mk-line" stroke-width="1.5" x="141" y="106" width="13" height="64"/><rect class="mk-navy" x="161" y="76" width="15" height="94"/><path class="mk-line" d="M76 170h176"/><g class="rise"><circle class="mk-acc" cx="150" cy="60" r="9"/></g>`,
        workshop: `<circle class="mk-sand" cx="178" cy="58" r="62"/><path class="mk-line" stroke-width="2" d="M48 162 232 88"/><circle class="mk-navy" cx="132" cy="124" r="22"/><g class="rise"><rect class="mk-acc" x="188" y="56" width="20" height="20"/></g>`,
        decks: `<circle class="mk-sand" cx="182" cy="52" r="58"/><rect class="mk-line" stroke-width="1.5" x="128" y="22" width="66" height="102"/><rect class="mk-line" stroke-width="1.5" x="108" y="46" width="66" height="102"/><rect class="mk-navy" x="88" y="70" width="66" height="100"/><g class="rise"><path class="mk-accline" stroke-width="2.5" d="M194 22v102"/></g><path class="mk-line" d="M60 170h192"/>`,
        journey: `<circle class="mk-sand" cx="176" cy="64" r="64"/><circle class="mk-navy" cx="72" cy="162" r="7"/><path class="mk-line" stroke-width="2" d="M72 162C124 162 122 76 208 66"/><g class="rise"><rect class="mk-acc" x="206" y="52" width="16" height="16"/></g>`,
        complete: `<circle class="mk-sand" cx="150" cy="46" r="80"/><path class="mk-navy" d="M60 170a72 72 0 0 1 144 0z"/><path class="mk-line" d="M30 170h222"/><g class="rise"><path class="mk-pineline" stroke-width="1.5" d="M132 66v104"/><circle class="mk-pine" cx="132" cy="66" r="9"/></g>`
    };

    const NAV_ICONS = {
        home: `<path class="nv-line" style="stroke-width:1.5" d="M8 3V29"/><path class="nv-navy" d="M8 7V29H24z"/><path class="nv-line" style="stroke-width:1.2" d="M8 5A24 24 0 0 1 30 29"/><circle class="nv-acc" cx="12.5" cy="23" r="2.2"/>`,
        lessons: `<path class="nv-navy" d="M3 26a10 10 0 0 1 20 0z"/><path class="nv-line" d="M13 16 27 5M23 26 27 5M3 26.8h26"/><circle class="nv-acc" cx="27" cy="5.5" r="3.4"/>`,
        library: `<rect class="nv-navy" x="3" y="10" width="4.5" height="18"/><rect class="nv-navy" x="10" y="3" width="4.5" height="25"/><rect class="nv-line" x="17.8" y="13" width="3.9" height="15"/><rect class="nv-navy" x="24" y="8" width="4.5" height="20"/><circle class="nv-acc" cx="19.5" cy="9" r="4.2"/>`,
        workshop: `<path class="nv-line" d="M2 26 30 12" style="stroke-width:2.2"/><circle class="nv-navy" cx="15" cy="19" r="5.6"/><rect class="nv-acc" x="21" y="3" width="8" height="8"/>`,
        decks: `<rect class="nv-line" x="11" y="3" width="16" height="20"/><rect class="nv-line" x="6.5" y="7.5" width="16" height="20"/><rect class="nv-navy" x="2" y="12" width="16" height="17"/><path class="nv-accline" d="M27 3v20"/>`,
        journey: `<circle class="nv-navy" cx="5" cy="26" r="3"/><path class="nv-line" d="M5 26C14 26 13 12 24 11" style="stroke-width:2"/><rect class="nv-acc" x="22" y="6" width="7" height="7"/>`
    };

    const LEVEL_MARKS = {
        A1: `<circle class="mk-sand" cx="32" cy="30" r="24"/><path class="mk-navy" d="M12 48a20 20 0 0 1 40 0z"/><path class="mk-line" stroke-width="1.2" d="M4 48h56"/><circle class="mk-acc" cx="47" cy="15" r="5"/>`,
        A2: `<circle class="mk-sand" cx="26" cy="32" r="22"/><circle class="mk-navy" cx="40" cy="35" r="16"/><path class="mk-line" stroke-width="1.2" d="M6 58 58 8"/><circle class="mk-acc" cx="13" cy="14" r="4.5"/>`,
        B1: `<circle class="mk-sand" cx="32" cy="32" r="26"/><path class="mk-navy" d="M32 32V6A26 26 0 0 1 58 32z"/><rect class="mk-acc" x="38" y="38" width="11" height="11"/>`,
        B2: `<circle class="mk-sand" cx="32" cy="34" r="24"/><path class="mk-navy" d="M12 54V16l34 38z"/><path class="mk-line" stroke-width="1.2" d="M32 4v56"/><circle class="mk-acc" cx="47" cy="20" r="5"/>`,
        C1: `<circle class="mk-sand" cx="32" cy="32" r="26"/><path class="mk-line" stroke-width="6" d="M13 32A19 19 0 0 1 51 32"/><circle class="mk-navy" cx="32" cy="45" r="7"/><path class="mk-line" stroke-width="1.2" d="M6 58 58 6"/><circle class="mk-acc" cx="51" cy="32" r="4.5"/>`
    };

    function heroSvg(id, className) {
        const art = HEROES[id];
        if (!art) return '';
        return `
            <svg class="art art-hero ${className || 'page-header-art'}" viewBox="0 0 252 184"
                preserveAspectRatio="xMaxYMin meet"
                role="presentation" aria-hidden="true" focusable="false">
                ${art}
            </svg>
        `;
    }

    function heroIds() { return Object.keys(HEROES); }

    function navIcon(id) {
        const art = NAV_ICONS[id];
        if (!art) return icon(id);
        return `<svg class="nav-icon" viewBox="0 0 32 32" role="presentation" aria-hidden="true" focusable="false">${art}</svg>`;
    }

    // state: 'done' (accent goes green), 'now' (accent stays vermilion),
    // anything else is neutral grey. Locked units are faded by CSS (.is-locked).
    function levelMark(code, state, className) {
        const art = LEVEL_MARKS[String(code || '').toUpperCase()];
        if (!art) return '';
        return `<svg class="art art-mark is-${state || 'todo'} ${className || ''}" viewBox="0 0 64 64"
            role="presentation" aria-hidden="true" focusable="false">${art}</svg>`;
    }

    // A composition generated from an id, so the same unit or story always
    // gets the same picture. One sand disc; one navy form of eight, rotated in
    // quarter turns; optionally a hairline or a small second form opposite
    // (never beside a navy disc); exactly one accent opposite the main form.
    function _rng(seed) {
        let h = 1779033703 ^ seed.length;
        for (let i = 0; i < seed.length; i++) {
            h = Math.imul(h ^ seed.charCodeAt(i), 3432918353);
            h = (h << 13) | (h >>> 19);
        }
        return function () {
            h = Math.imul(h ^ (h >>> 16), 2246822507);
            h = Math.imul(h ^ (h >>> 13), 3266489909);
            return ((h ^= h >>> 16) >>> 0) / 4294967296;
        };
    }
    function _f(n) { return Math.round(n * 10) / 10; }
    function _form(kind, cx, cy, r) {
        const a = _f(cx - r), b = _f(cx + r);
        switch (kind) {
            case 0: return `<path class="mk-navy" d="M${a} ${cy}A${r} ${r} 0 0 1 ${b} ${cy}z"/>`;
            case 1: return `<path class="mk-navy" d="M${cx} ${cy}V${_f(cy - r)}A${r} ${r} 0 0 1 ${b} ${cy}z"/>`;
            case 2: return `<circle class="mk-navy" cx="${_f(cx + r * .32)}" cy="${_f(cy - r * .3)}" r="${_f(r * .48)}"/>`;
            case 3: return `<circle class="mk-line" stroke-width="${_f(r * .22)}" cx="${cx}" cy="${cy}" r="${_f(r * .58)}"/>`;
            case 4: return `<path class="mk-navy" d="M${_f(cx - r * .7)} ${_f(cy + r * .7)}V${_f(cy - r * .7)}L${_f(cx + r * .7)} ${_f(cy + r * .7)}z"/>`;
            case 5: return `<rect class="mk-navy" x="${a}" y="${_f(cy - r * .58)}" width="${_f(r * 2)}" height="${_f(r * .4)}"/>`;
            case 6: return `<circle class="mk-navy" cx="${_f(cx + r * .42)}" cy="${_f(cy - r * .18)}" r="${_f(r * .62)}"/>`;
            default: return `<path class="mk-navy" d="M${cx} ${cy}H${a}A${r} ${r} 0 0 1 ${cx} ${_f(cy - r)}z"/><path class="mk-navy" d="M${cx} ${cy}H${b}A${r} ${r} 0 0 1 ${cx} ${_f(cy + r)}z"/>`;
        }
    }
    function unitMark(seed, state, className) {
        const R = _rng(String(seed));
        const pick = n => Math.floor(R() * n);
        const r = 21 + pick(5), cx = 32 + pick(5) - 2, cy = 32 + pick(5) - 2;
        const rot = pick(4) * 90, kind = pick(8);
        const disc = `<circle class="mk-sand" cx="${cx}" cy="${cy}" r="${r}"/>`;
        const main = `<g transform="rotate(${rot} ${cx} ${cy})">${_form(kind, cx, cy, r)}</g>`;
        let extra = '';
        const roll = R();
        if (roll < .34) {
            const t = pick(3), lx = _f(cx + (R() - .5) * r * .8);
            extra = t === 0 ? `<path class="mk-line" stroke-width="1.2" d="M${lx} ${cy - r - 6}V${cy + r + 6}"/>`
                : t === 1 ? `<path class="mk-line" stroke-width="1.2" d="M${cx - r - 6} ${_f(cy + (R() - .5) * r * .8)}H${cx + r + 6}"/>`
                : `<path class="mk-line" stroke-width="1.2" d="M${cx - r} ${cy + r}L${cx + r} ${cy - r}"/>`;
        } else if (roll < .6 && kind !== 2 && kind !== 6) {
            extra = `<g transform="rotate(${(rot + 180) % 360} ${cx} ${cy})">${_form([0, 1, 4][pick(3)], cx, cy, _f(r * .42))}</g>`;
        }
        const ang = (rot + 180 + (R() - .5) * 70) * Math.PI / 180, d = r * (.7 + R() * .28);
        const ax = _f(cx + d * Math.sin(ang)), ay = _f(cy - d * Math.cos(ang));
        const acc = R() < .5
            ? `<circle class="mk-acc" cx="${ax}" cy="${ay}" r="${_f(4 + R() * 1.6)}"/>`
            : `<rect class="mk-acc" x="${_f(ax - 4.5)}" y="${_f(ay - 4.5)}" width="9" height="9"/>`;
        const ring = state === 'now'
            ? `<circle class="mk-accline" stroke-width="1.5" cx="${cx}" cy="${cy}" r="${r + 5}"/>` : '';
        return `<svg class="art art-mark is-${state || 'todo'} ${className || ''}" viewBox="0 0 64 64"
            role="presentation" aria-hidden="true" focusable="false">${disc}${extra}${main}${acc}${ring}</svg>`;
    }


    // Row thumbnails (72 x 56): two shapes and a grey accent. The accent turns
    // ochre only when the row has something due or new (opts.due).
    const THUMBS = {
        ochre: `<circle cx="30" cy="30" r="22" class="mk-acc"/><rect x="40" y="16" width="20" height="30" class="mk-navy"/>`,
        sand: `<circle cx="40" cy="26" r="24" class="mk-sand"/><path class="mk-navy" d="M12 52V22h26z"/>`,
        half: `<path class="mk-navy" d="M10 50A26 26 0 0 1 62 50z"/><path class="mk-accline" stroke-width="1.5" d="M36 10v40"/><circle class="mk-acc" cx="36" cy="10" r="5"/>`,
        beam: `<path class="mk-line" stroke-width="1.5" d="M6 44 66 20"/><circle class="mk-navy" cx="34" cy="32" r="8"/><rect class="mk-acc" x="50" y="8" width="10" height="10"/>`,
        cards: `<rect class="mk-line" stroke-width="1.5" x="24" y="6" width="34" height="38"/><rect class="mk-navy" x="10" y="16" width="34" height="34"/>`,
        bars: `<rect class="mk-navy" x="10" y="20" width="8" height="32"/><rect class="mk-navy" x="24" y="8" width="8" height="44"/><rect class="mk-line" stroke-width="1.5" x="39" y="24" width="8" height="28"/><circle class="mk-acc" cx="56" cy="20" r="7"/>`,
        wave: `<path class="mk-line" stroke-width="2.5" d="M10 28v0M18 18v20M26 10v36M34 20v16M42 14v28M50 22v12"/><circle class="mk-acc" cx="62" cy="28" r="5"/>`,
        disc: `<circle cx="36" cy="28" r="22" class="mk-sand"/><circle cx="30" cy="30" r="10" class="mk-navy"/><rect class="mk-acc" x="46" y="10" width="9" height="9"/>`
    };
    const THUMB_ALIAS = {
        review: 'ochre',
        read: 'sand',
        practise: 'half',
        decks: 'cards',
        verb: 'bars',
        grammar: 'half',
        translation: 'beam',
        vocabulary: 'disc',
        listening: 'wave'
    };

    function thumb(id, opts) {
        const key = THUMBS[id] ? id : THUMB_ALIAS[id];
        const art = THUMBS[key];
        if (!art) return '';
        const due = opts && opts.due;
        return `<svg class="art art-thumb${due ? ' is-due' : ''}" viewBox="0 0 72 56"
            role="presentation" aria-hidden="true" focusable="false">${art}</svg>`;
    }


    return { section, svg, ids, icon, iconIds, heroSvg, heroIds, navIcon, levelMark, unitMark, thumb };
})();
