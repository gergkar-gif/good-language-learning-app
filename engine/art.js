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

        // Workshop — building skill. Two forms brought into balance across a
        // beam; the fulcrum, small and off-centre, is what does the work.
        balance: `
            <line class="ink-hair" x1="40" y1="88" x2="280" y2="88"/>
            <line class="ink-rule" x1="66" y1="54" x2="266" y2="72"/>
            <path class="ink-solid" d="M196 66 210 88H182Z"/>
            <rect class="ink-solid" x="80" y="24" width="34" height="34"/>
            <circle class="accent-solid" cx="164" cy="52" r="14"/>
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

        // My Journey — distance already covered. A line that climbs by stages
        // rather than smoothly, each node a place the learner actually stood,
        // planted at the top with a flag. The climb dips once on purpose: no
        // honest account of learning a language only goes up.
        ascent: `
            <line class="ink-hair" x1="40" y1="86" x2="280" y2="86"/>
            <polyline class="ink-rule" points="66,78 108,58 148,64 192,40 236,30"/>
            <circle class="ink-solid" cx="66" cy="78" r="4"/>
            <circle class="ink-solid" cx="108" cy="58" r="4"/>
            <circle class="ink-solid" cx="148" cy="64" r="4"/>
            <circle class="ink-solid" cx="192" cy="40" r="4"/>
            <line class="ink-rule" x1="236" y1="30" x2="236" y2="86"/>
            <path class="accent-solid" d="M236 16h30l-8 9 8 9h-30Z"/>
        `,

        // Reader — the door the whole app is named for. A threshold standing
        // open, light falling forward across the floor. The accent sits where
        // a handle would: the point at which you push it open.
        threshold: `
            <line class="ink-hair" x1="20" y1="86" x2="300" y2="86"/>
            <g class="ink-hair">
                <line x1="176" y1="82" x2="44" y2="86"/>
                <line x1="176" y1="74" x2="52" y2="82"/>
                <line x1="176" y1="64" x2="66" y2="76"/>
                <line x1="176" y1="52" x2="86" y2="68"/>
                <line x1="176" y1="40" x2="112" y2="58"/>
            </g>
            <rect class="ink-line" x="176" y="18" width="72" height="68"/>
            <path class="ink-solid" d="M176 18 140 30v62l36-6Z"/>
            <circle class="accent-solid" cx="168" cy="60" r="4"/>
        `
    };

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
            <svg class="${className || 'page-header-art'}" viewBox="0 0 320 100"
                preserveAspectRatio="xMidYMid meet"
                role="presentation" aria-hidden="true" focusable="false">
                ${art}
            </svg>
        `;
    }

    function ids() {
        return Object.keys(SECTIONS);
    }

    return { section, svg, ids };
})();
