// ============================================
// UI HELPERS
// ============================================

// Backs UI.showLoading()/hideLoading() — a short delay before the overlay
// actually appears so a fast (cached) open doesn't flash it at all.
let _actionLoaderTimer = null;
let _actionLoaderCount = 0;

const UI = {

    // Content is authored JSON rather than user input, but titles carry
    // ampersands ("Greetings & Introductions") that break markup unescaped.
    escape(text) {
        return String(text == null ? "" : text)
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;");
    },

    html(id, html) {
        const el = document.getElementById(id);
        if (el) el.innerHTML = html;
        return el;
    },

    append(id, html) {
        const el = document.getElementById(id);
        if (el) el.insertAdjacentHTML("beforeend", html);
        return el;
    },

    clear(id) {
        const el = document.getElementById(id);
        if (el) el.innerHTML = "";
        return el;
    },

    show(id) {
        const el = document.getElementById(id);
        if (el) el.classList.remove("hidden");
        return el;
    },

    hide(id) {
        const el = document.getElementById(id);
        if (el) el.classList.add("hidden");
        return el;
    },

    card(title, body, extra = "") {
        return `
            <div class="card ${extra}">
                <h3>${title}</h3>
                <p>${body}</p>
            </div>
        `;
    },

    button(text, onclick, cls = "btn-primary") {
        return `
            <button class="${cls}" onclick="${onclick}">
                ${text}
            </button>
        `;
    },

    badge(text, cls = "level-badge") {
        return `<span class="${cls}">${text}</span>`;
    },

    toast(message, type = 'info', duration = 3000) {
        if (typeof document === 'undefined' || !document.body) return null;
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container';
            container.setAttribute('aria-live', 'polite');
            document.body.appendChild(container);
        }
        const toastEl = document.createElement('div');
        toastEl.className = `app-toast app-toast--${type}`;
        toastEl.textContent = message;
        container.appendChild(toastEl);
        setTimeout(() => {
            toastEl.classList.add('is-active');
        }, 10);
        const timer = setTimeout(() => {
            toastEl.classList.remove('is-active');
            setTimeout(() => { if (toastEl.parentNode) toastEl.remove(); }, 300);
        }, duration);
        toastEl.onclick = () => {
            clearTimeout(timer);
            toastEl.classList.remove('is-active');
            setTimeout(() => { if (toastEl.parentNode) toastEl.remove(); }, 300);
        };
        return toastEl;
    },

    empty(message) {
        return `
            <div class="card" style="text-align:center;opacity:.7">
                <p>${message}</p>
            </div>
        `;
    },

    // Special characters by language for on-screen accent helper bars
    DIACRITICS: {
        es: ['á', 'é', 'í', 'ó', 'ú', 'ñ', 'ü', '¿', '¡'],
        hu: ['á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű'],
        fr: ['à', 'â', 'ç', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü', 'œ']
    },

    diacriticsBarHtml(targetSelector, lang) {
        const langCode = lang || (typeof Lang !== 'undefined' && Lang.code ? Lang.code() : 'es');
        const chars = UI.DIACRITICS[langCode] || UI.DIACRITICS.es;
        const targetAttr = targetSelector ? ` data-target="${targetSelector}"` : '';
        return `
            <div class="lsn-diacritics"${targetAttr} role="toolbar" aria-label="Special characters">
                ${chars.map(ch => `<button type="button" class="lsn-diacritic-btn" data-char="${ch}" tabindex="-1" aria-label="Insert ${ch}">${ch}</button>`).join('')}
            </div>
        `;
    },

    // A full-screen loading overlay for actions with a real network/parse
    // delay (opening a lesson, opening a Workshop driller) — blocks input
    // so a slow load doesn't invite the learner to tap around while it
    // catches up, per user report. Shown after a short delay so a
    // cache-warm open never flashes it, with an option for immediate display.
    showLoading(message = 'Loading…', options = {}) {
        _actionLoaderCount++;
        const updateLabel = (text) => {
            const label = document.querySelector('#action-loader .boot-label');
            if (label) label.textContent = text || 'Loading…';
        };

        const ensureAndShow = () => {
            let el = document.getElementById('action-loader');
            if (!el) {
                el = document.createElement('div');
                el.id = 'action-loader';
                el.setAttribute('role', 'status');
                el.setAttribute('aria-live', 'polite');
                el.innerHTML = `
                    <svg class="boot-spinner" viewBox="0 0 100 100" aria-hidden="true">
                        <g class="ps-spin-group">
                            <circle cx="50" cy="50" r="40" class="ps-wash"/>
                            <circle cx="50" cy="12" r="7" class="ps-accent"/>
                        </g>
                        <polygon points="50,42 58,58 42,58" class="ps-triangle"/>
                    </svg>
                    <p class="boot-label">${UI.escape(message || 'Loading…')}</p>
                `;
                document.body.appendChild(el);
            } else {
                updateLabel(message);
            }
            el.classList.add('is-visible');
        };

        if (options && options.immediate) {
            if (_actionLoaderTimer) {
                clearTimeout(_actionLoaderTimer);
                _actionLoaderTimer = null;
            }
            ensureAndShow();
        } else {
            if (_actionLoaderTimer) {
                updateLabel(message);
            } else {
                _actionLoaderTimer = setTimeout(() => {
                    _actionLoaderTimer = null;
                    ensureAndShow();
                }, 150);
            }
        }
    },

    hideLoading(force = false) {
        if (force) {
            _actionLoaderCount = 0;
        } else {
            _actionLoaderCount = Math.max(0, _actionLoaderCount - 1);
        }
        if (_actionLoaderCount === 0) {
            if (_actionLoaderTimer) {
                clearTimeout(_actionLoaderTimer);
                _actionLoaderTimer = null;
            }
            const el = document.getElementById('action-loader');
            if (el) el.classList.remove('is-visible');
            if (typeof document !== 'undefined') {
                document.querySelectorAll('.is-loading').forEach(node => node.classList.remove('is-loading'));
            }
        }
    }

};

if (typeof document !== 'undefined') {
    // Track the active/last-focused text input across the app so accent buttons know where to insert
    document.addEventListener('focusin', e => {
        if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) {
            window._lastFocusedInput = e.target;
        }
    });

    // Delegate diacritic button clicks to insert character at current caret position without losing focus
    document.addEventListener('click', e => {
        const btn = e.target.closest('.lsn-diacritic-btn');
        if (!btn) return;
        e.preventDefault();
        const char = btn.dataset.char;
        if (!char) return;

        const bar = btn.closest('.lsn-diacritics');
        const selector = bar ? bar.dataset.target : null;
        let target = selector ? document.querySelector(selector) : null;
        if (!target) {
            if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
                target = document.activeElement;
            } else if (window._lastFocusedInput && document.body.contains(window._lastFocusedInput)) {
                target = window._lastFocusedInput;
            } else if (bar) {
                target = bar.parentElement.querySelector('input[type="text"], textarea');
            }
        }
        if (!target) return;

        const start = target.selectionStart ?? target.value.length;
        const end = target.selectionEnd ?? target.value.length;
        const val = target.value;
        target.value = val.substring(0, start) + char + val.substring(end);
        target.selectionStart = target.selectionEnd = start + char.length;
        try { target.focus({ preventScroll: true }); } catch (e) { target.focus(); }
        target.dispatchEvent(new Event('input', { bubbles: true }));
    });
}

if (typeof window !== 'undefined') {
    window.UI = UI;
    window.showToast = (msg, type) => UI.toast(msg, type || 'info');
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = UI;
}