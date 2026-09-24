// ============================================
// PARLOUR GUIDE — NEW-LEARNER INTRODUCTION
// ============================================
// Parlour introduces itself over the first week rather than in a tour up
// front (plan and all copy: docs/feature-guidance-copy.md):
// 1. Margin notes — one short italic line floating just below the thing it
//    describes. Shown once per feature; closed by tapping anywhere, by the
//    ×, or by using the feature itself. At most one new note a day, except
//    the few that belong inside a lesson.
// 2. Invitations — one line plus a button on the end-of-lesson screen that
//    takes a new learner to an area they haven't found yet (Decks, then the
//    Library, then the Workshop). A skipped invitation comes back once.
// 3. The "How Parlour works" modal, opened from Home.

const Guide = (function () {
    'use strict';

    const STORAGE_PREFIX = 'parlour_guide_seen_';
    const SHOWS_PREFIX = 'parlour_guide_shows_';
    const VISITS_PREFIX = 'parlour_guide_visits_';
    const NOTE_DAY_KEY = 'parlour_guide_note_day';

    // A note shown this many times without being dismissed or used is
    // retired anyway: ignoring it twice is an answer too.
    const MAX_NOTE_SHOWS = 2;
    const MAX_INVITATION_SHOWS = 2;

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
    // INVITATIONS (END-OF-LESSON SCREEN)
    // --------------------------------------------
    // In order: the deck after the first lesson, the Library after Unit 1,
    // the Workshop after Unit 2. The first one that applies is offered.
    //   ctx.firstTime     — the lesson was finished for the first time
    //   ctx.newWords      — words this lesson added to the deck
    //   ctx.unitCompleted — this completion finished a unit
    //   ctx.unitsDone     — units finished in the course so far
    const INVITATIONS = [
        {
            id: 'invite-decks',
            tab: 'review',
            applies: ctx => ctx.firstTime && ctx.newWords > 0,
            text: ctx => `${ctx.newWords} new ${ctx.newWords === 1 ? 'word is' : 'words are'} in your deck, ready for a short review.`,
            button: 'See your deck',
            nextLesson: true
        },
        {
            id: 'invite-library',
            tab: 'reader',
            applies: ctx => ctx.unitCompleted && ctx.unitsDone >= 1,
            text: () => 'There\'s a short story in the Library written for where you are now.',
            button: 'Read it'
        },
        {
            id: 'invite-workshop',
            tab: 'drills',
            applies: ctx => ctx.unitCompleted && ctx.unitsDone >= 2,
            text: () => 'The Workshop is for practising one thing at a time: verbs, listening, speaking.',
            button: 'Have a look'
        }
    ];

    // The invitation for this lesson completion, or null. Counts as shown
    // once returned.
    function invitation(ctx) {
        const inv = INVITATIONS.find(i =>
            !hasSeen(i.id)
            && visits(i.tab) === 0
            && _count(SHOWS_PREFIX, i.id) < MAX_INVITATION_SHOWS
            && i.applies(ctx));
        if (!inv) return null;
        _bump(SHOWS_PREFIX, inv.id);
        return {
            id: inv.id,
            tab: inv.tab,
            text: inv.text(ctx),
            button: inv.button,
            nextLesson: !!inv.nextLesson
        };
    }

    function acceptInvitation(id) {
        markSeen(id);
    }

    // --------------------------------------------
    // HOW PARLOUR WORKS (PHILOSOPHY & ROOMS MODAL)
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
                        <span class="hm-eyebrow">A Quick Tour</span>
                        <h2 id="pl-guide-modal-title" class="pl-guide-title">How Parlour works</h2>
                    </div>
                    <button class="wp-close" data-guide-modal-close="1" aria-label="Close modal">&times;</button>
                </div>

                <div class="pl-guide-modal-scroll">
                    <!-- The Philosophy -->
                    <div class="pl-guide-section">
                        <h3 class="pl-guide-sec-title">The Idea</h3>
                        <p class="pl-guide-p">
                            Parlour is for people who actually want to learn languages and cultures. A non-commercial project, we want to provide a place where you can learn, read, review, and practice — welcome!
                        </p>
                        <p class="pl-guide-p">
                            Real fluency comes from three things working together: <strong>comprehensible input</strong> (reading real stories), 
                            <strong>structured grammar</strong> (understanding how sentences fit together), and <strong>active production</strong> (writing and speaking your own thoughts).
                        </p>
                    </div>

                    <!-- The 6 Rooms -->
                    <div class="pl-guide-section">
                        <h3 class="pl-guide-sec-title">The 6 Rooms</h3>
                        <div class="pl-guide-rooms">
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Home</span>
                                <h4>Your Study Desk</h4>
                                <p>Answers one question every day: <em>"What is the single best thing to do right now?"</em> Recommends your next lesson, reviews due cards, or suggests a quick 5–15 minute study budget.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Lessons</span>
                                <h4>The Course Workbook</h4>
                                <p>Structured CEFR curriculum (A1 to B1+). Each unit breaks down grammar clearly with interactive steps, vocabulary in context, and communicative tasks.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Library</span>
                                <h4>The Reading Rooms</h4>
                                <p>Graded stories and classic literature. Tap any word to see instant translations and add it to your deck. Plus: paste your own texts into <em>My Texts</em>.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Decks</span>
                                <h4>The Memory Box</h4>
                                <p>Spaced repetition (SRS) flashcards. Target words from your lessons and reading flow here automatically. You can also import decks directly from Quizlet or Anki.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Workshop</span>
                                <h4>The Practice Studio</h4>
                                <p>Focused micro-practice. Drill fast verb conjugations, train your listening ear, or use the Speaking & Writing Studios for open-ended composition with CEFR grading.</p>
                            </div>
                            <div class="pl-guide-room-card">
                                <span class="pl-guide-room-tag">Journey</span>
                                <h4>Your Learning Record</h4>
                                <p>Visual milestones, CEFR proficiency levels, and streak stats. You can also import your existing streak from Duolingo or another app so you never lose momentum.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Power Features / Imports -->
                    <div class="pl-guide-section pl-guide-features-box">
                        <h3 class="pl-guide-sec-title">Bring your study habits with you</h3>
                        <ul class="pl-guide-bullets">
                            <li>
                                <strong>Import your streak:</strong> Head to <em>Journey</em> and tap <em>Import streak from another app</em> to bring your Duolingo or Babbel streak over.
                            </li>
                            <li>
                                <strong>Import your flashcards:</strong> In <em>Decks</em>, tap <em>Import</em> to paste sets from Quizlet, Anki, or CSV spreadsheets.
                            </li>
                            <li>
                                <strong>Read whatever you want:</strong> In <em>Library &rarr; My Texts</em>, paste any Spanish or Hungarian article, story, or song lyrics to read with full tap-to-translate dictionary support.
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="pl-guide-modal-footer">
                    <button class="pl-guide-primary-btn" data-guide-modal-close="1">Got it, let's explore</button>
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
        invitation,
        acceptInvitation,
        openOverviewModal,
        closeOverviewModal
    };
})();

if (typeof module !== 'undefined' && module.exports) {
    module.exports = Guide;
}
