// ============================================
// PAGE HEADER
// ============================================
// One editorial header, re-rendered per section. Each page supplies only a
// title, subtitle, illustration id and optional actions; spacing, motion and
// responsive behaviour live here so every section is identical.
//
//   PageHeader.render({ title, subtitle, illustration, actions })
//
// A title may be a function, resolved at render rather than at load. Only
// Home needs it — its title is the time of day — and the rule stands that a
// header carries no running state: the greeting is the one thing that changes
// without saying anything about how the learner is doing.
//
// Illustrations live in engine/art.js, which the nav and story cards also
// draw from. This module only names which one belongs to which section.

const PAGE_HEADERS = {
    home: {
        title: () => (typeof Home !== 'undefined') ? Home.greeting() : 'Home',
        subtitle: 'Where you left off.',
        illustration: 'threshold'
    },
    learn: {
        title: 'Lessons',
        subtitle: () => `Your ${(typeof Lang !== 'undefined') ? Lang.name() : 'Spanish'} course.`,
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
    },
    journey: {
        title: 'My Journey',
        subtitle: 'How far you have come.',
        illustration: 'ascent'
    }
};

const PageHeader = {

    render(config) {
        const host = document.getElementById('page-header');
        if (!host || !config) return;

        const art = Art.section(config.illustration);
        const actions = (config.actions || []).filter(Boolean);
        const title = (typeof config.title === 'function') ? config.title() : config.title;
        const subtitle = (typeof config.subtitle === 'function') ? config.subtitle() : config.subtitle;

        host.innerHTML = `
            <div class="page-header-text">
                <h1 class="page-header-title">${UI.escape(title)}</h1>
                <p class="page-header-sub">${UI.escape(subtitle || '')}</p>
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
