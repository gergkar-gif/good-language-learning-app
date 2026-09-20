// ============================================
// PARLOUR GUIDE & FIRST-ENCOUNTER COACH
// ============================================
// Provides lightweight, casual, non-intrusive guidance across Parlour:
// 1. First-encounter coach notes (Lessons, Library, Decks, Workshop, Production).
// 2. The "How Parlour Works" modal (Philosophy, 6 Rooms, Power Imports).
//
// Constructivist principles:
// - Casual, friendly, conversational tone (no robotic AI prose).
// - Zero emoji pictograms (100% SVG line/wash icon system).
// - Remembers dismissed state per feature in localStorage.

const Guide = (function () {
    'use strict';

    const STORAGE_PREFIX = 'parlour_guide_seen_';

    function _key(featureId) {
        return STORAGE_PREFIX + featureId;
    }

    function hasSeen(featureId) {
        try {
            return localStorage.getItem(_key(featureId)) === '1';
        } catch (e) {
            return false;
        }
    }

    function markSeen(featureId) {
        try {
            localStorage.setItem(_key(featureId), '1');
        } catch (e) {
            // Storage unavailable (e.g. private mode)
        }
    }

    function resetAll() {
        try {
            if (typeof localStorage === 'undefined') return;
            const toRemove = [];
            if (typeof localStorage.length === 'number') {
                for (let i = 0; i < localStorage.length; i++) {
                    const k = localStorage.key(i);
                    if (k && k.startsWith(STORAGE_PREFIX)) toRemove.push(k);
                }
            }
            Object.keys(localStorage).forEach(k => {
                if (k && k.startsWith(STORAGE_PREFIX) && !toRemove.includes(k)) toRemove.push(k);
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

    function _defaultIconSvg() {
        return `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
            <circle cx="12" cy="12" r="9" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
            <line x1="12" y1="8" x2="12" y2="12" class="ink-line" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
            <circle cx="12" cy="15.5" r="0.75" class="ink-line" fill="currentColor"/>
        </svg>`;
    }

    // Pre-defined encounter tips with casual, human tone
    const TIPS = {
        lesson: {
            title: 'Welcome to your first lesson!',
            text: 'Work through each card at your own pace. If you miss a question, no sweat — Parlour gathers your mistakes and brings them back at the end for a zero-pressure redo pass.',
            iconSvg: `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <line x1="8" y1="7" x2="16" y2="7" class="ink-line" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="8" y1="11" x2="14" y2="11" class="ink-line" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>`
        },
        reader: {
            title: 'This is the Library',
            text: 'Read graded stories and classic literature crafted for your level. <strong>Tap any word</strong> while reading to see an instant translation, grammar breakdown, and add it straight to your review deck. Want to read your own texts? Switch to the <strong>My Texts</strong> tab to paste in any article or story.',
            iconSvg: `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
                <rect x="3" y="4" width="18" height="16" rx="2" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <line x1="7" y1="8" x2="17" y2="8" class="ink-line" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="7" y1="12" x2="17" y2="12" class="ink-line" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <line x1="7" y1="16" x2="13" y2="16" class="ink-line" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>`
        },
        decks: {
            title: 'Your Memory Box (Decks)',
            text: 'As you complete lessons and read stories, target vocabulary collects here automatically for spaced repetition. Already have custom study sets? You can <strong>import decks directly from Quizlet or Anki</strong> via the Import button.',
            iconSvg: `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
                <rect x="5" y="7" width="14" height="14" rx="2" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <path d="M8 4h10a2 2 0 0 1 2 2v10" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.5"/>
            </svg>`
        },
        workshop: {
            title: 'The Practice Studio (Workshop)',
            text: 'Need to drill a specific skill? Workshop is where you can hammer out rapid verb conjugations, train your ear with spoken audio driller, or jump into the <strong>Speaking and Writing Studios</strong> for open-ended composition with instant CEFR feedback.',
            iconSvg: `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
                <circle cx="12" cy="12" r="3" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.5"/>
            </svg>`
        },
        production: {
            title: 'Express Yourself (Production)',
            text: 'Focus on getting your meaning across! In speaking and writing tasks, Parlour does not look for robotic cookie-cutter answers — you will receive personal coaching notes highlighting what worked well and what to tweak next time.',
            iconSvg: `<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false">
                <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75"/>
                <path d="M19 10v2a7 7 0 0 1-14 0v-2" class="ink-line" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
                <line x1="12" y1="19" x2="12" y2="22" class="ink-line" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
            </svg>`
        }
    };

    function renderBannerHtml(featureId, customOptions) {
        const config = Object.assign({}, TIPS[featureId] || {}, customOptions || {});
        const title = config.title || 'Tip';
        const text = config.text || '';
        const iconSvg = config.iconSvg || _defaultIconSvg();

        return `
            <div class="pl-guide-banner" data-guide-banner="${_esc(featureId)}" role="status">
                <div class="pl-guide-banner-icon" aria-hidden="true">
                    ${iconSvg}
                </div>
                <div class="pl-guide-banner-content">
                    <div class="pl-guide-banner-head">
                        <h4 class="pl-guide-banner-title">${_esc(title)}</h4>
                        <button type="button" class="pl-guide-dismiss-btn" data-guide-dismiss="${_esc(featureId)}" aria-label="Dismiss tip" title="Dismiss tip">&times;</button>
                    </div>
                    <div class="pl-guide-banner-body">${text}</div>
                </div>
            </div>
        `;
    }

    function attachBanner(container, featureId, customOptions) {
        if (!container || hasSeen(featureId)) return null;

        const wrapper = document.createElement('div');
        wrapper.className = 'pl-guide-banner-wrapper';
        wrapper.innerHTML = renderBannerHtml(featureId, customOptions);

        const bannerEl = wrapper.firstElementChild;
        container.insertBefore(wrapper, container.firstChild);

        const dismissBtn = wrapper.querySelector('[data-guide-dismiss]');
        if (dismissBtn) {
            dismissBtn.addEventListener('click', () => {
                markSeen(featureId);
                wrapper.style.transition = 'opacity 0.2s ease, transform 0.2s ease, max-height 0.25s ease';
                wrapper.style.opacity = '0';
                wrapper.style.transform = 'translateY(-6px)';
                wrapper.style.maxHeight = wrapper.offsetHeight + 'px';
                setTimeout(() => {
                    wrapper.style.maxHeight = '0px';
                    wrapper.style.margin = '0px';
                    wrapper.style.overflow = 'hidden';
                }, 10);
                setTimeout(() => {
                    if (wrapper.parentNode) wrapper.parentNode.removeChild(wrapper);
                }, 260);
            });
        }

        return wrapper;
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
        renderBannerHtml,
        attachBanner,
        openOverviewModal,
        closeOverviewModal,
        TIPS
    };
})();

if (typeof module !== 'undefined' && module.exports) {
    module.exports = Guide;
}
