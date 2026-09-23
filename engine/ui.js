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

    // Base-letter -> accented-variant lookup for the contextual accent
    // popover: when the learner types a base letter, we show only the
    // variants of that letter instead of a permanently-visible row of
    // every special character in the language (Conjuguemos-style).
    DIACRITIC_VARIANTS: {
        es: { a: ['á'], e: ['é'], i: ['í'], o: ['ó'], u: ['ú', 'ü'], n: ['ñ'] },
        hu: { a: ['á'], e: ['é'], i: ['í'], o: ['ó', 'ö', 'ő'], u: ['ú', 'ü', 'ű'] },
        fr: { a: ['à', 'â'], c: ['ç'], e: ['é', 'è', 'ê', 'ë'], i: ['î', 'ï'], o: ['ô', 'œ'], u: ['ù', 'û', 'ü'] }
    },

    // Inverted opening punctuation can't be derived from the letter the
    // learner just typed, so it's keyed off the closing mark instead: type
    // "?" and ¿ pops up to insert at the start of the sentence.
    DIACRITIC_OPENERS: {
        es: { '?': '¿', '!': '¡' }
    },

    // Marker only — no visible buttons. It records which input the
    // contextual accent popover (wired up below) should watch and which
    // language's accent map to use; call sites are unchanged from the old
    // always-visible bar.
    diacriticsBarHtml(targetSelector, lang) {
        const langCode = lang || (typeof Lang !== 'undefined' && Lang.code ? Lang.code() : 'es');
        const targetAttr = targetSelector ? ` data-target="${targetSelector}"` : '';
        return `<div class="lsn-diacritics" data-lang="${langCode}"${targetAttr}></div>`;
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
    // Track the active/last-focused text input across the app so the accent
    // popover still knows where to insert after its mousedown steals focus.
    document.addEventListener('focusin', e => {
        if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) {
            window._lastFocusedInput = e.target;
        }
    });

    let _diacPopoverChar = null; // base char (or opener trigger) the popover is currently showing for
    let _diacPopoverTarget = null;

    const getDiacPopover = () => {
        let el = document.getElementById('diacritics-popover');
        if (!el) {
            el = document.createElement('div');
            el.id = 'diacritics-popover';
            el.className = 'lsn-diacritic-popover';
            el.setAttribute('role', 'listbox');
            el.setAttribute('aria-label', 'Accent options');
            document.body.appendChild(el);
        }
        return el;
    };

    const hideDiacPopover = () => {
        const el = document.getElementById('diacritics-popover');
        if (el) el.classList.remove('is-visible');
        _diacPopoverChar = null;
        _diacPopoverTarget = null;
    };

    const insertReplacingLastChar = (target, char) => {
        const start = target.selectionStart ?? target.value.length;
        const val = target.value;
        target.value = val.substring(0, start - 1) + char + val.substring(start);
        target.selectionStart = target.selectionEnd = start - 1 + char.length;
    };

    // Openers (¿/¡) go at the start of the current sentence, not at the
    // caret — scan back for the nearest sentence boundary.
    const insertAtSentenceStart = (target, char) => {
        const start = target.selectionStart ?? target.value.length;
        const val = target.value;
        const before = val.substring(0, start);
        const boundary = Math.max(before.lastIndexOf('. '), before.lastIndexOf('! '), before.lastIndexOf('? '), before.lastIndexOf('\n'));
        const insertAt = boundary === -1 ? 0 : boundary + 2;
        if (val[insertAt] === char) return; // already there
        target.value = val.substring(0, insertAt) + char + val.substring(insertAt);
        target.selectionStart = target.selectionEnd = start + char.length;
    };

    const showDiacPopover = (target, bar, triggerChar, variants, insertMode) => {
        const el = getDiacPopover();
        el.innerHTML = variants.map(ch =>
            `<button type="button" class="lsn-diacritic-popover-btn" data-char="${ch}" data-mode="${insertMode}" tabindex="-1" aria-label="Insert ${ch}">${ch}</button>`
        ).join('');

        const rect = target.getBoundingClientRect();
        el.classList.add('is-visible');
        const popRect = el.getBoundingClientRect();
        let left = rect.left;
        if (left + popRect.width > window.innerWidth - 8) left = window.innerWidth - popRect.width - 8;
        if (left < 8) left = 8;
        let top = rect.bottom + 4;
        if (top + popRect.height > window.innerHeight - 8) top = rect.top - popRect.height - 4;
        el.style.left = `${left}px`;
        el.style.top = `${top}px`;

        _diacPopoverChar = triggerChar;
        _diacPopoverTarget = target;
    };

    // Find the marker bar (if any) watching this input, and its language.
    const findDiacBar = (input) => {
        const bars = document.querySelectorAll('.lsn-diacritics[data-target]');
        for (const bar of bars) {
            const el = document.querySelector(bar.dataset.target);
            if (el === input) return bar;
        }
        return null;
    };

    document.addEventListener('input', e => {
        const target = e.target;
        if (!target || (target.tagName !== 'INPUT' && target.tagName !== 'TEXTAREA')) return;
        if (e.inputType && !e.inputType.startsWith('insert')) { hideDiacPopover(); return; }

        const bar = findDiacBar(target);
        if (!bar) return;
        const langCode = bar.dataset.lang || 'es';

        const start = target.selectionStart;
        if (start == null || start === 0 || start !== target.selectionEnd) { hideDiacPopover(); return; }
        const typed = target.value[start - 1];
        const lower = typed.toLowerCase();

        const letterVariants = (UI.DIACRITIC_VARIANTS[langCode] || {})[lower];
        if (letterVariants) {
            const cased = typed === lower ? letterVariants : letterVariants.map(ch => ch.toUpperCase());
            showDiacPopover(target, bar, typed, cased, 'replace');
            return;
        }

        const opener = (UI.DIACRITIC_OPENERS[langCode] || {})[typed];
        if (opener) {
            showDiacPopover(target, bar, typed, [opener], 'sentence-start');
            return;
        }

        hideDiacPopover();
    });

    document.addEventListener('focusout', e => {
        if (e.target === _diacPopoverTarget) {
            // Give a click on the popover a chance to fire (it uses mousedown) before hiding.
            setTimeout(() => { if (document.activeElement !== _diacPopoverTarget) hideDiacPopover(); }, 150);
        }
    });

    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && _diacPopoverChar) hideDiacPopover();
    });

    document.addEventListener('mousedown', e => {
        const btn = e.target.closest('.lsn-diacritic-popover-btn');
        if (!btn) {
            if (!e.target.closest('.lsn-diacritic-popover')) hideDiacPopover();
            return;
        }
        e.preventDefault();
        const char = btn.dataset.char;
        const mode = btn.dataset.mode;
        let target = _diacPopoverTarget;
        if (!target || !document.body.contains(target)) target = window._lastFocusedInput;
        if (!target) return;

        if (mode === 'sentence-start') insertAtSentenceStart(target, char);
        else insertReplacingLastChar(target, char);

        try { target.focus({ preventScroll: true }); } catch (err) { target.focus(); }
        target.dispatchEvent(new Event('input', { bubbles: true }));
        hideDiacPopover();
    });
}

if (typeof window !== 'undefined') {
    window.UI = UI;
    window.showToast = (msg, type) => UI.toast(msg, type || 'info');
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = UI;
}