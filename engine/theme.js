// ============================================
// THEME MANAGER
// ============================================
// Manages light, dark, and system color schemes for Parlour.
// Supports:
// - 'system': Automatically follows OS / browser prefers-color-scheme
// - 'light': Traditional Kandinsky cream & navy palette
// - 'dark': Inverted Constructivist midnight navy & cream palette
// Persisted locally in localStorage ('parlour_theme').

const Theme = (function () {
    'use strict';

    const STORAGE_KEY = 'parlour_theme';

    function getPreference() {
        try {
            return localStorage.getItem(STORAGE_KEY) || 'system';
        } catch (e) {
            return 'system';
        }
    }

    function isDark() {
        const pref = getPreference();
        if (pref === 'dark') return true;
        if (pref === 'light') return false;
        return !!(typeof window !== 'undefined' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    }

    function apply() {
        const pref = getPreference();
        const dark = isDark();

        if (pref === 'system') {
            if (dark) {
                document.documentElement.setAttribute('data-theme', 'dark');
            } else {
                document.documentElement.removeAttribute('data-theme');
            }
        } else if (pref === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
        }

        _updateToggles();
    }

    function set(pref) {
        try {
            localStorage.setItem(STORAGE_KEY, pref);
        } catch (e) {}
        apply();
    }

    function toggle() {
        const currentDark = isDark();
        set(currentDark ? 'light' : 'dark');
    }

    function _updateToggles() {
        const pref = getPreference();
        const dark = isDark();
        const iconSvg = (typeof Art !== 'undefined')
            ? Art.icon(dark ? 'themeLight' : 'themeDark')
            : '';
        const label = dark ? 'Light theme' : 'Dark theme';

        document.querySelectorAll('.theme-toggle-btn, .nav-theme-btn').forEach(btn => {
            btn.setAttribute('title', 'Switch to ' + label.toLowerCase());
            btn.setAttribute('aria-label', 'Switch to ' + label.toLowerCase());
            const iconEl = btn.querySelector('.theme-toggle-icon');
            if (iconEl && iconSvg) iconEl.innerHTML = iconSvg;
            const labelEl = btn.querySelector('.nav-theme-label');
            if (labelEl) labelEl.textContent = label;
        });

        document.querySelectorAll('[data-theme-choice]').forEach(opt => {
            const choice = opt.getAttribute('data-theme-choice');
            const isActive = choice === pref;
            opt.classList.toggle('active', isActive);
            opt.setAttribute('aria-checked', String(isActive));
        });
    }

    // React to system OS theme changes when in 'system' mode
    if (typeof window !== 'undefined' && window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
            if (getPreference() === 'system') {
                apply();
            }
        });
    }

    // Global listener for theme toggles and choices
    if (typeof document !== 'undefined') {
        document.addEventListener('click', e => {
            const quickBtn = e.target.closest('.theme-toggle-btn, .nav-theme-btn');
            if (quickBtn) {
                toggle();
                return;
            }
            const choiceBtn = e.target.closest('[data-theme-choice]');
            if (choiceBtn) {
                const choice = choiceBtn.getAttribute('data-theme-choice');
                if (choice) set(choice);
            }
        });

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', apply);
        } else {
            apply();
        }
    }

    return {
        getPreference,
        isDark,
        set,
        toggle,
        apply,
        init() {
            apply();
        }
    };
})();
