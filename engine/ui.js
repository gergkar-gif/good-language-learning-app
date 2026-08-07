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
    }

};