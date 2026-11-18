// ============================================
// PARLOUR GUIDE — NEW-LEARNER INTRODUCTION
// ============================================
// Parlour introduces itself over the first week rather than in a tour up
// front (plan and all copy: docs/feature-guidance-copy.md):
// 1. Margin notes — one short italic line floating just below the thing it
//    describes. Shown once per feature; closed by tapping anywhere, by the
//    ×, or by using the feature itself. At most one new note a day, except
//    the few that belong inside a lesson.
// 2. The "About Parlour" modal, opened from the sidebar or Home footer.

const Guide = (function () {
    'use strict';

    const STORAGE_PREFIX = 'parlour_guide_seen_';
    const SHOWS_PREFIX = 'parlour_guide_shows_';
    const VISITS_PREFIX = 'parlour_guide_visits_';
    const NOTE_DAY_KEY = 'parlour_guide_note_day';

    // A note shown this many times without being dismissed or used is
    // retired anyway: ignoring it twice is an answer too.
    const MAX_NOTE_SHOWS = 2;

    function _get(key) {
        try { return localStorage.getItem(key); } catch (e) { return null; }
    }

    function _set(key, value) {
        try { localStorage.setItem(key, value); } catch (e) {}
    }

    function _key(featureId) {
        return STORAGE_PREFIX + featureId;
    }

    function hasSeen(featureId) {
        return _get(_key(featureId)) === '1';
    }

    function markSeen(featureId) {
        _set(_key(featureId), '1');
    }

    function _count(prefix, id) {
        return parseInt(_get(prefix + id) || '0', 10) || 0;
    }

    function _bump(prefix, id) {
        const n = _count(prefix, id) + 1;
        _set(prefix + id, String(n));
        return n;
    }

    function _today() {
        const d = new Date();
        return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
    }

    function resetAll() {
        try {
            if (typeof localStorage === 'undefined') return;
            const prefixes = [STORAGE_PREFIX, SHOWS_PREFIX, VISITS_PREFIX, NOTE_DAY_KEY];
            const matches = k => k && prefixes.some(p => k.startsWith(p));
            const toRemove = [];
            if (typeof localStorage.length === 'number') {
                for (let i = 0; i < localStorage.length; i++) {
                    const k = localStorage.key(i);
                    if (matches(k)) toRemove.push(k);
                }
            }
            Object.keys(localStorage).forEach(k => {
                if (matches(k) && !toRemove.includes(k)) toRemove.push(k);
            });
            toRemove.forEach(k => localStorage.removeItem(k));
        } catch (e) {}
    }

    function _esc(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    // --------------------------------------------
    // AREA VISITS
    // --------------------------------------------
    // Counted per tab (home, learn, reader, drills, review, journey) from
    // showTab(), so an invitation to an area the learner already found on
    // their own is skipped, and "third visit to Decks" is answerable.

    function markVisited(tabId) {
        if (tabId) _bump(VISITS_PREFIX, tabId);
    }

    function visits(tabId) {
        return _count(VISITS_PREFIX, tabId);
    }

    // --------------------------------------------
    // MARGIN NOTES
    // --------------------------------------------

    let _active = null;

    function _removeActive() {
        if (!_active) return;
        const { el, cleanup } = _active;
        _active = null;
        cleanup();
        if (el.parentNode) el.parentNode.removeChild(el);
    }

    // Closed by the learner (× or tapping elsewhere) or by using the thing
    // it points at: either way it has done its job.
    function _dismiss() {
        if (!_active) return;
        markSeen(_active.id);
        _removeActive();
    }

    // Taken down without counting as read — the screen it belonged to is
    // being replaced (next lesson step, another tab).
    function clearNote() {
        _removeActive();
    }

    // Fixed to the viewport and re-placed on every scroll, so it follows
    // its anchor whichever element is doing the scrolling (the page on a
    // phone, .content on a wide screen). Hidden while the anchor is off
    // screen.
    // Returns whether the note is on screen.
    function _place(el, anchor) {
        const a = anchor.getBoundingClientRect();
        const vw = document.documentElement.clientWidth;
        const vh = document.documentElement.clientHeight;
        const onScreen = a.bottom >= 0 && a.bottom + 6 < vh;
        el.style.visibility = onScreen ? '' : 'hidden';
        const maxLeft = Math.max(8, vw - el.offsetWidth - 8);
        el.style.top = Math.round(a.bottom + 6) + 'px';
        el.style.left = Math.round(Math.min(Math.max(8, a.left), maxLeft)) + 'px';
        return onScreen;
    }

    // Shows a one-line note just below `anchor`. Returns the note element,
    // or null when it isn't shown (already seen, another note is up, the
    // day's note already used, or the anchor isn't rendered).
    //   options.inLesson — one of the first-lesson basics, not held back by
    //   the one-a-day limit.
    function note(featureId, anchor, text, options) {
        const opts = options || {};
        if (typeof document === 'undefined') return null;
        if (!anchor || !anchor.isConnected || hasSeen(featureId) || _active) return null;
        if (!opts.inLesson && _get(NOTE_DAY_KEY) === _today()) return null;

        if (!anchor.getClientRects().length) return null; // display: none

        const el = document.createElement('div');
        el.className = 'pl-note';
        el.setAttribute('role', 'note');
        el.innerHTML = `
            <p class="pl-note-text">${_esc(text)}</p>
            <button type="button" class="pl-note-close" aria-label="Close note">&times;</button>
        `;
        document.body.appendChild(el);

        // Counted (the day's note, one of its two showings) only once it
        // has actually been on screen — an anchor below the fold waits
        // until the learner scrolls to it.
        let counted = false;
        const countIfSeen = onScreen => {
            if (counted || !onScreen) return;
            counted = true;
            if (!opts.inLesson) _set(NOTE_DAY_KEY, _today());
            if (_bump(SHOWS_PREFIX, featureId) >= MAX_NOTE_SHOWS) markSeen(featureId);
        };
        countIfSeen(_place(el, anchor));

        // Any tap closes it — on the note's ×, on the thing it points at,
        // or anywhere else — and the tap still does whatever it would have.
        const onDocClick = e => {
            if (el.contains(e.target) && !e.target.closest('.pl-note-close')) return;
            if (counted) _dismiss();
            else clearNote();
        };
        const onMove = () => {
            if (anchor.isConnected) countIfSeen(_place(el, anchor));
            else clearNote();
        };

        // Attached a tick later so the click that made the note appear
        // doesn't immediately close it again.
        const timer = setTimeout(() => document.addEventListener('click', onDocClick, true), 0);
        window.addEventListener('resize', onMove);
        document.addEventListener('scroll', onMove, true);

        _active = {
            id: featureId,
            el: el,
            cleanup: () => {
                clearTimeout(timer);
                document.removeEventListener('click', onDocClick, true);
                window.removeEventListener('resize', onMove);
                document.removeEventListener('scroll', onMove, true);
            }
        };
        return el;
    }

    // --------------------------------------------
    // ABOUT PARLOUR (PHILOSOPHY & ROOMS MODAL)
    // --------------------------------------------

    function openOverviewModal() {
        closeOverviewModal();

        const overlay = document.createElement('div');
        overlay.id = 'pl-guide-modal-overlay';
        overlay.className = 'wp-overlay pl-guide-overlay';

        overlay.innerHTML = `
            <div class="wp-sheet pl-guide-modal" role="dialog" aria-modal="true" aria-labelledby="pl-guide-modal-title">
                <div class="wp-header pl-guide-modal-header">
                    <div>
                        <span class="hm-eyebrow">Guide</span>
                        <h2 id="pl-guide-modal-title" class="pl-guide-title">About Parlour</h2>
                    </div>
                    <button class="wp-close" data-guide-modal-close="1" aria-label="Close modal">&times;</button>
                </div>

                <div class="pl-guide-modal-scroll">
                    <!-- The Philosophy -->
                    <div class="pl-guide-section">
                        <h3 class="pl-guide-sec-title">Why I built this</h3>
                        <p class="pl-guide-p">
                            I started Parlour because I&rsquo;d had enough of language apps built around cartoon mascots, hearts, and paywalls. You shouldn&rsquo;t lose your own word list behind a subscription, and you shouldn&rsquo;t have to juggle five separate apps just to learn grammar, read real books, and review vocabulary.
                        </p>
                        <p class="pl-guide-p">
                            Learning a language is hard, and it should be &mdash; that&rsquo;s what gives it its flavour. Parlour tries to treat you like an adult: explain the grammar clearly, practise it in context, give you real stories to read, and get out of your way.
                        </p>
                        <p class="pl-guide-p">
                            Parlour covers Spanish (Latin America and Spain, CEFR A1&ndash;B2) and Hungarian (CEFR A1&ndash;C1). It is free, non-commercial, and has no ads or trackers &mdash; just tools that work. Your progress stays local in your browser unless you sign in to back it up.
                        </p>
                    </div>

                    <!-- The 6 Rooms -->
                    <div class="pl-guide-section">
                        <h3 class="pl-guide-sec-title">The Six Rooms</h3>
                        <div class="pl-guide-rooms">
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Home</span>
                                <h4>Your Study Desk</h4>
                                <p>Answers one question when you open the app: <em>&ldquo;What should I do right now?&rdquo;</em> Points you to your next lesson, overdue reviews, or a 5&ndash;30 minute study session.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Lessons</span>
                                <h4>The Course Workbook</h4>
                                <p>Structured CEFR courses (A1&ndash;B2 in Spanish, A1&ndash;C1 in Hungarian) with clear grammar explanations, contextual drills, and speaking tasks. Follow the sequence, jump straight to any unit, or take the placement diagnostic to skip what you already know.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Library</span>
                                <h4>The Reading Rooms</h4>
                                <p>Graded stories and classic literature matched to your level. Tap any word for an instant translation (with suffix breakdowns in Hungarian) and save the ones you want to learn. In <em>My Texts</em>, import <code>.epub</code>, <code>.docx</code>, or <code>.txt</code> files &mdash; or paste anything you want to read.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Workshop</span>
                                <h4>The Practice Studio</h4>
                                <p>Focused practice outside the lesson path: fast verb conjugations, Grammar &amp; Morphology Studios, Listening with songs and real video, CEFR-graded Speaking &amp; Writing, and official exam prep for DELE, ECL, CCSE, and the Hungarian Cultural Exam.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Decks</span>
                                <h4>The Memory Box</h4>
                                <p>Spaced-repetition flashcards alongside Learn, Match, and Blast modes. Vocabulary from your lessons collects here automatically, and you can add words while reading or import sets from Quizlet, Anki, Memrise, or CSV.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Journey</span>
                                <h4>Your Learning Record</h4>
                                <p>Milestones, skill breakdowns, a CEFR Can-Do Passport, dark/light theme settings, and optional cloud backup. Switching from another app? Import your existing streak so you don&rsquo;t start from zero.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Power Features / Imports -->
                    <div class="pl-guide-section pl-guide-features-box">
                        <h3 class="pl-guide-sec-title">Bring your study habits with you</h3>
                        <ul class="pl-guide-bullets">
                            <li>
                                <strong>Import your streak:</strong> In <em>Journey</em>, tap <em>Import a streak</em> to bring your day count over.
                            </li>
                            <li>
                                <strong>Import your flashcards:</strong> In <em>Decks</em>, tap <em>Import deck</em> to paste sets or upload exports from Quizlet, Anki, Memrise, or spreadsheets.
                            </li>
                            <li>
                                <strong>Read whatever you want:</strong> In <em>Library &rarr; My Texts</em>, upload <code>.epub</code>, <code>.docx</code>, <code>.txt</code>, or <code>.md</code> files &mdash; or paste articles and lyrics &mdash; for full tap-to-translate reading.
                            </li>
                        </ul>
                    </div>

                    <!-- Colophon & Contact -->
                    <div class="pl-guide-section" style="margin-bottom: 0;">
                        <h3 class="pl-guide-sec-title">Colophon &amp; Contact</h3>
                        <p class="pl-guide-p">
                            Parlour is an independent, non-commercial project by K&aacute;roly Gergely. Notice an error in a lesson, have feedback, or want to contribute? Use the flag button on any screen, email <a href="mailto:gergkar@gmail.com" style="color:var(--text); text-decoration:underline;">gergkar@gmail.com</a>, or open an issue on <a href="https://github.com/gergkar-gif/good-language-learning-app" target="_blank" rel="noopener" style="color:var(--text); text-decoration:underline;">GitHub</a>. &middot; <a href="privacy.html" style="color:var(--text); text-decoration:underline;">Privacy Policy</a>
                        </p>
                    </div>
                </div>

                <div class="pl-guide-modal-footer">
                    <button class="pl-guide-primary-btn" data-guide-modal-close="1">Close</button>
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        overlay.querySelectorAll('[data-guide-modal-close]').forEach(btn => {
            btn.addEventListener('click', closeOverviewModal);
        });
        overlay.addEventListener('click', e => {
            if (e.target === overlay) closeOverviewModal();
        });

        // Trap escape key
        function _onEsc(e) {
            if (e.key === 'Escape') {
                closeOverviewModal();
                document.removeEventListener('keydown', _onEsc);
            }
        }
        document.addEventListener('keydown', _onEsc);
    }

    function closeOverviewModal() {
        const existing = document.getElementById('pl-guide-modal-overlay');
        if (existing && existing.parentNode) {
            existing.parentNode.removeChild(existing);
        }
    }

    return {
        hasSeen,
        markSeen,
        resetAll,
        markVisited,
        visits,
        note,
        clearNote,
        openOverviewModal,
        closeOverviewModal
    };
})();

if (typeof module !== 'undefined' && module.exports) {
    module.exports = Guide;
}
