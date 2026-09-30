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
        subtitle: 'Welcome back to your language journey.',
        illustration: 'home'
    },
    learn: {
        title: 'Lessons',
        subtitle: () => `Your ${(typeof Lang !== 'undefined') ? Lang.name() : 'Spanish'} course.`,
        illustration: 'lessons'
    },
    reader: {
        title: 'Library',
        subtitle: 'Your reading rooms.',
        illustration: 'library'
    },
    drills: {
        title: 'Workshop',
        subtitle: 'Focused practice.',
        illustration: 'workshop'
    },
    review: {
        title: 'Decks',
        subtitle: 'Spaced repetition.',
        illustration: 'decks'
    },
    journey: {
        title: 'My Journey',
        subtitle: 'How far you have come.',
        illustration: 'journey'
    }
};

const PageHeader = {

    render(config) {
        const host = document.getElementById('page-header');
        if (!host || !config) return;

        const art = Art.heroSvg(config.illustration);
        const actions = (config.actions || []).filter(Boolean);
        const dark = (typeof Theme !== 'undefined' && typeof Theme.isDark === 'function') ? Theme.isDark() : false;
        const themeIcon = (typeof Art !== 'undefined' && typeof Art.icon === 'function')
            ? Art.icon(dark ? 'themeLight' : 'themeDark')
            : '';
        const mobileThemeToggle = `<button type="button" class="theme-toggle-btn mobile-theme-btn" aria-label="${dark ? 'Light theme' : 'Dark theme'}" title="${dark ? 'Light theme' : 'Dark theme'}"><span class="theme-toggle-icon" aria-hidden="true">${themeIcon}</span></button>`;
        const allActions = [mobileThemeToggle, ...actions];
        const title = (typeof config.title === 'function') ? config.title() : config.title;
        const subtitle = (typeof config.subtitle === 'function') ? config.subtitle() : config.subtitle;

        host.innerHTML = `
            <div class="page-header-text">
                <h1 class="page-header-title">${UI.escape(title)}</h1>
                <p class="page-header-sub">${UI.escape(subtitle || '')}</p>
            </div>
            ${allActions.length ? `<div class="page-header-actions">${allActions.join('')}</div>` : ''}
            ${art}
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
