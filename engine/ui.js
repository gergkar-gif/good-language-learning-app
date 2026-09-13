// ============================================
// UI HELPERS
// ============================================

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
    }

};

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
    target.focus();
    target.dispatchEvent(new Event('input', { bubbles: true }));
});