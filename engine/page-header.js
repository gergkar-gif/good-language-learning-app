// ============================================
// PAGE HEADER
// ============================================
// One editorial header, re-rendered per section. Each page supplies only a
// title, subtitle, illustration id and optional actions; spacing, motion and
// responsive behaviour live here so every section is identical.
//
//   PageHeader.render({ title, subtitle, illustration, actions })
//
// The illustration is decorative: monochrome, very low contrast, and hidden
// from assistive tech. It must never compete with the title.

const PAGE_ILLUSTRATIONS = {
    // sprout
    sprout: '<path d="M12 21V10m0 0C12 6.5 9.5 4 6 4H4c0 3.5 2.5 6 6 6h2Zm0 0c0-4 3-7 7-7h2c0 4-3 7-7 7h-2Z"/>',
    // books on a shelf
    bookshelf: '<path d="M4 20h16M6 20V7h3v13M11 20V4h3v16M16 20l1.6-11 3 .5L18.9 20"/>',
    // hammer and wrench
    tools: '<path d="M14.5 5.5a3.5 3.5 0 0 0 4.6 4.6L21 12l-2 2-1.9-1.9a3.5 3.5 0 0 0-4.6-4.6L14.5 5.5ZM10 10 4 16v4h4l6-6"/>',
    // card catalogue drawer
    cards: '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 11h18M10 15h4"/><path d="M7 6V4h10v2"/>',
    // mountain
    mountain: '<path d="M3 19 10 7l4 6.5 2.5-3.5L21 19H3Z"/>'
};

const PAGE_HEADERS = {
    learn: {
        title: 'Lessons',
        subtitle: 'Your Spanish course.',
        illustration: 'sprout'
    },
    reader: {
        title: 'Library',
        subtitle: 'Your reading rooms.',
        illustration: 'bookshelf'
    },
    drills: {
        title: 'Workshop',
        subtitle: 'Focused practice.',
        illustration: 'tools'
    },
    review: {
        title: 'Decks',
        subtitle: 'Spaced repetition.',
        illustration: 'cards'
    }
};

const PageHeader = {

    render(config) {
        const host = document.getElementById('page-header');
        if (!host || !config) return;

        const art = PAGE_ILLUSTRATIONS[config.illustration];
        const actions = (config.actions || []).filter(Boolean);

        host.innerHTML = `
            ${art ? `
                <svg class="page-header-art" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    ${art}
                </svg>
            ` : ''}
            <div class="page-header-text">
                <h1 class="page-header-title">${UI.escape(config.title)}</h1>
                <p class="page-header-sub">${UI.escape(config.subtitle || '')}</p>
            </div>
            ${actions.length ? `<div class="page-header-actions">${actions.join('')}</div>` : ''}
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
