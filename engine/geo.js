// ============================================
// GEO
// ============================================
// Wires up .geo-toggle elements: a role="switch" button whose visual state
// (styles/geometry.css) is a navy circle vs orange triangle rather than a
// sliding pill. Semantics are a plain switch — this only flips aria-checked
// and fires a change event; the shape transition itself is pure CSS.

const Geo = (function () {
    'use strict';

    function initToggles(root) {
        (root || document).querySelectorAll('.geo-toggle[role="switch"]').forEach((el) => {
            if (el.dataset.geoWired) return;
            el.dataset.geoWired = '1';
            el.addEventListener('click', () => toggle(el));
            el.addEventListener('keydown', (e) => {
                if (e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    toggle(el);
                }
            });
        });
    }

    function toggle(el) {
        if (el.disabled || el.getAttribute('aria-disabled') === 'true') return;
        const next = el.getAttribute('aria-checked') !== 'true';
        el.setAttribute('aria-checked', String(next));
        el.dispatchEvent(new CustomEvent('geo-change', { detail: { checked: next }, bubbles: true }));
    }

    return { initToggles };
})();
