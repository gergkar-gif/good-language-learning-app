// ============================================
// PAGE HEADER
// ============================================
// One editorial header, re-rendered per section. Each page supplies only a
// title, subtitle, illustration id and optional actions; spacing, motion and
// responsive behaviour live here so every section is identical.
//
//   PageHeader.render({ title, subtitle, illustration, actions })
//
// The illustrations are frontispieces, not decoration. Each is built from a
// handful of primitives — circles, rectangles, lines, arcs, triangles — and
// states one idea by metaphor rather than depiction. Roughly three quarters
// of each composition is deliberately empty; the accent colour is rationed to
// a single element so it never competes with the page title.

const PAGE_ILLUSTRATIONS = {

    // Lessons — structured progression. A path opening out of a horizon,
    // perspective lines converging on a single point ahead.
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
    // line, a sun standing behind them.
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
    // beam; the fulcrum is what does the work.
    balance: `
        <line class="ink-hair" x1="40" y1="88" x2="280" y2="88"/>
        <line class="ink-rule" x1="66" y1="54" x2="266" y2="72"/>
        <path class="ink-solid" d="M196 66 210 88H182Z"/>
        <rect class="ink-solid" x="80" y="24" width="34" height="34"/>
        <circle class="accent-solid" cx="164" cy="52" r="14"/>
    `,

    // Decks — memory through repetition. The same form recurring, each pass
    // a little further back; only the newest is fully filled in.
    stack: `
        <line class="ink-hair" x1="40" y1="90" x2="280" y2="90"/>
        <rect class="accent-line" x="176" y="24" width="44" height="62" rx="3"/>
        <rect class="ink-line" x="152" y="24" width="44" height="62" rx="3"/>
        <rect class="ink-line" x="128" y="24" width="44" height="62" rx="3"/>
        <rect class="ink-solid" x="104" y="24" width="44" height="62" rx="3"/>
    `
};

const PAGE_HEADERS = {
    learn: {
        title: 'Lessons',
        subtitle: 'Your Spanish course.',
        illustration: 'path'
    },
    reader: {
        title: 'Library',
        subtitle: 'Your reading rooms.',
        illustration: 'horizon'
    },
    drills: {
        title: 'Workshop',
        subtitle: 'Focused practice.',
        illustration: 'balance'
    },
    review: {
        title: 'Decks',
        subtitle: 'Spaced repetition.',
        illustration: 'stack'
    }
};

const PageHeader = {

    render(config) {
        const host = document.getElementById('page-header');
        if (!host || !config) return;

        const art = PAGE_ILLUSTRATIONS[config.illustration];
        const actions = (config.actions || []).filter(Boolean);

        host.innerHTML = `
            <div class="page-header-text">
                <h1 class="page-header-title">${UI.escape(config.title)}</h1>
                <p class="page-header-sub">${UI.escape(config.subtitle || '')}</p>
            </div>
            ${actions.length ? `<div class="page-header-actions">${actions.join('')}</div>` : ''}
            ${art ? `
                <svg class="page-header-art" viewBox="0 0 320 100" preserveAspectRatio="xMidYMid meet"
                    role="presentation" aria-hidden="true" focusable="false">
                    ${art}
                </svg>
            ` : ''}
        `;

        // Restart the entrance animation on every change of section.
        host.classList.remove('is-entering');
        void host.offsetWidth;
        host.classList.add('is-entering');
    },

    // Called on every tab change. Unknown sections leave the header alone.
    show(tabName) {
        const config = PAGE_HEADERS[tabName];
        if (config) this.render(config);
    }
};
