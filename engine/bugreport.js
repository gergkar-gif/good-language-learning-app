// ============================================
// BUG REPORT
// ============================================
// A floating flag button, present on every screen, that opens a GitHub
// "new issue" page prefilled with whatever the app can tell about where the
// learner was standing — lesson, step, language, tab — plus an optional
// note. Built so the two people testing this app can flag a mistake the
// instant they see it instead of writing it up by hand afterward.
//
// No token, on purpose: an earlier version POSTed straight to the GitHub
// API with an embedded fine-grained PAT. GitHub's own push protection
// rejected that commit outright — it scans for GitHub's own token formats
// and blocks them from ever landing in a repo, and would very likely have
// revoked the token anyway once its secret scanner found the same string
// served in plaintext by the live GitHub Pages site. There is no client-
// side way to hide a token from GitHub's own scanners in a public repo, so
// this uses GitHub's prefilled-issue URL scheme instead: no secret exists
// anywhere, but the reporter needs to be logged into GitHub and click
// "Submit new issue" themselves once the page opens.

const BugReport = (function () {
    'use strict';

    const GITHUB_REPO = 'gergkar-gif/good-language-learning-app';
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
    // Opens GitHub's own "new issue" form, prefilled — this is a plain link,
    // not a network call, so there is nothing to fail except a popup
    // blocker. The reporter still has to click "Submit new issue" on
    // GitHub's page; this only saves them typing it.
    function submitUrl(note) {
        const ctx = captureContext();
        const params = new URLSearchParams({
            title: formatTitle(ctx),
            body: formatBody(ctx, note),
            labels: LABEL
        });
        return 'https://github.com/' + GITHUB_REPO + '/issues/new?' + params.toString();
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
                    <p class="br-hint">Opens a prefilled GitHub issue in a new tab — you'll need to be signed in to submit it.</p>
                    ${!noteVisible ? `
                        <div class="br-actions">
                            <button class="br-primary" id="br-quick">Report issue</button>
                            <button class="br-secondary" id="br-write-in">Write in&hellip;</button>
                        </div>
                    ` : `
                        <textarea id="br-note" class="br-note" placeholder="What's wrong here?" autofocus></textarea>
                        <div class="br-actions">
                            <button class="br-primary" id="br-submit-note">Open on GitHub</button>
                            <button class="br-secondary" id="br-cancel-note">Cancel</button>
                        </div>
                    `}
                </div>
            </div>
        `;

        const textarea = document.getElementById('br-note');
        if (textarea) textarea.focus();
    }

    function goToGithub(note) {
        window.open(submitUrl(note), '_blank', 'noopener');
        open = false;
        noteVisible = false;
        render();
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
                goToGithub('');
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
                goToGithub(note ? note.value : '');
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
