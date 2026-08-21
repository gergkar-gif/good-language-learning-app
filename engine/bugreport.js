// ============================================
// BUG REPORT
// ============================================
// A floating flag button, present on every screen, that files a GitHub
// issue with whatever the app can tell about where the learner was standing
// — lesson, step, language, tab — plus an optional note. Built so the two
// people testing this app (not yet the public) can flag a mistake the
// instant they see it instead of writing it up by hand afterward.
//
// The GitHub token below is embedded in this public, client-side file on
// purpose — a deliberate, discussed tradeoff for a small trusted audience,
// not an oversight. It is a fine-grained personal access token scoped to
// ONLY this repository and ONLY "Issues: Read and write" — nothing else it
// could be used for if someone found it. Revisit this (move to a proxied
// backend, or gate the button behind a shared passphrase) before this app
// has any audience beyond people the owner already trusts. See
// BUG_REPORT_SETUP.md for how the token was created and how to rotate it.

const BugReport = (function () {
    'use strict';

    const GITHUB_REPO = 'gergkar-gif/good-language-learning-app';
    const GITHUB_TOKEN = 'PASTE_YOUR_FINE_GRAINED_TOKEN_HERE';
    const LABEL = 'bug-report';

    let open = false;
    let noteVisible = false;

    // ----------------------------------------
    // CONTEXT
    // ----------------------------------------
    // Best-effort: every field is optional, since this button has to work
    // from screens (Home, Library, Workshop) that never touch a lesson at
    // all, not just mid-lesson.
    function captureContext() {
        const ctx = {
            url: location.href,
            timestamp: new Date().toISOString(),
            lang: (typeof Lang !== 'undefined' && Lang.code) ? Lang.code() : null,
            tab: null,
            lesson: null,
            step: null
        };

        const activeTab = document.querySelector('.tab:not(.hidden)');
        if (activeTab) ctx.tab = activeTab.id;

        if (typeof currentLesson !== 'undefined' && currentLesson) {
            ctx.lesson = { id: currentLesson.id, title: currentLesson.title };
            const steps = currentLesson.steps || [];
            const step = steps[currentStepIndex];
            if (step) {
                ctx.step = {
                    index: currentStepIndex,
                    total: steps.length,
                    type: step.type,
                    id: step.id || null,
                    title: step.title || null
                };
            }
        }

        return ctx;
    }

    function summaryLine(ctx) {
        if (ctx.step) {
            return (ctx.lesson.title || ctx.lesson.id) +
                ' — step ' + (ctx.step.index + 1) + '/' + ctx.step.total +
                ' (' + ctx.step.type + ')';
        }
        if (ctx.lesson) return ctx.lesson.title || ctx.lesson.id;
        if (ctx.tab) return 'Tab: ' + ctx.tab;
        return 'Unknown location';
    }

    function formatTitle(ctx) {
        const bits = [];
        if (ctx.lang) bits.push(ctx.lang.toUpperCase());
        bits.push(summaryLine(ctx));
        return '[Bug report] ' + bits.join(' — ');
    }

    function formatBody(ctx, note) {
        let body = '';
        if (note) body += note.trim() + '\n\n---\n\n';
        body += '**Context**\n';
        body += '- URL: ' + ctx.url + '\n';
        if (ctx.lang) body += '- Language: ' + ctx.lang + '\n';
        if (ctx.tab) body += '- Tab: ' + ctx.tab + '\n';
        if (ctx.lesson) body += '- Lesson: ' + (ctx.lesson.title || '') + ' (`' + ctx.lesson.id + '`)\n';
        if (ctx.step) {
            body += '- Step: ' + (ctx.step.index + 1) + '/' + ctx.step.total +
                ', type `' + ctx.step.type + '`' +
                (ctx.step.id ? ', id `' + ctx.step.id + '`' : '') + '\n';
        }
        body += '- Reported: ' + ctx.timestamp + '\n';
        return body;
    }

    // ----------------------------------------
    // SUBMIT
    // ----------------------------------------
    async function submit(note) {
        const ctx = captureContext();
        const res = await fetch('https://api.github.com/repos/' + GITHUB_REPO + '/issues', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + GITHUB_TOKEN,
                'Accept': 'application/vnd.github+json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: formatTitle(ctx),
                body: formatBody(ctx, note),
                labels: [LABEL]
            })
        });

        if (!res.ok) throw new Error('GitHub API responded ' + res.status);
        return res.json();
    }

    // ----------------------------------------
    // UI
    // ----------------------------------------
    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape) ? UI.escape(value) : String(value == null ? '' : value);
    }

    function render() {
        let host = document.getElementById('bug-report-root');
        if (!host) {
            host = document.createElement('div');
            host.id = 'bug-report-root';
            document.body.appendChild(host);
            wire(host);
        }

        if (!open) {
            host.innerHTML = `
                <button id="br-flag-btn" class="br-flag-btn" aria-label="Report a problem" title="Report a problem">
                    ${(typeof Art !== 'undefined') ? Art.icon('flag') : ''}
                </button>
            `;
            return;
        }

        const ctx = captureContext();
        host.innerHTML = `
            <button id="br-flag-btn" class="br-flag-btn" aria-label="Report a problem" title="Report a problem">
                ${(typeof Art !== 'undefined') ? Art.icon('flag') : ''}
            </button>
            <div class="br-overlay" id="br-overlay">
                <div class="br-sheet">
                    <div class="br-header">
                        <h3 class="br-title">Report a problem</h3>
                        <button class="br-close" id="br-close" aria-label="Close">&times;</button>
                    </div>
                    <p class="br-context">${esc(summaryLine(ctx))}</p>
                    <div id="br-status" class="br-status" aria-live="polite"></div>
                    ${!noteVisible ? `
                        <div class="br-actions">
                            <button class="br-primary" id="br-quick">Report issue</button>
                            <button class="br-secondary" id="br-write-in">Write in&hellip;</button>
                        </div>
                    ` : `
                        <textarea id="br-note" class="br-note" placeholder="What's wrong here?" autofocus></textarea>
                        <div class="br-actions">
                            <button class="br-primary" id="br-submit-note">Submit</button>
                            <button class="br-secondary" id="br-cancel-note">Cancel</button>
                        </div>
                    `}
                </div>
            </div>
        `;

        const textarea = document.getElementById('br-note');
        if (textarea) textarea.focus();
    }

    async function handleSubmit(note) {
        const status = document.getElementById('br-status');
        const actions = document.querySelector('.br-actions');
        if (actions) actions.style.display = 'none';
        if (status) status.textContent = 'Sending…';

        try {
            await submit(note);
            if (status) status.textContent = 'Reported — thank you.';
            setTimeout(() => { open = false; noteVisible = false; render(); }, 1100);
        } catch (err) {
            console.error('Bug report failed:', err);
            if (status) status.textContent = 'Could not send — check your connection and try again.';
            if (actions) actions.style.display = '';
        }
    }

    function wire(host) {
        host.addEventListener('click', e => {
            if (e.target.closest('#br-flag-btn')) {
                open = !open;
                noteVisible = false;
                render();
                return;
            }
            if (e.target.closest('#br-close') || e.target === document.getElementById('br-overlay')) {
                open = false;
                noteVisible = false;
                render();
                return;
            }
            if (e.target.closest('#br-quick')) {
                handleSubmit('');
                return;
            }
            if (e.target.closest('#br-write-in')) {
                noteVisible = true;
                render();
                return;
            }
            if (e.target.closest('#br-cancel-note')) {
                noteVisible = false;
                render();
                return;
            }
            if (e.target.closest('#br-submit-note')) {
                const note = document.getElementById('br-note');
                handleSubmit(note ? note.value : '');
                return;
            }
        });
    }

    return { render };
})();

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', BugReport.render);
} else {
    BugReport.render();
}
