// ============================================
// APP INITIALISATION
// ============================================

const LEVELS = ['a1', 'a2', 'b1', 'b2', 'c1'];

// A Workshop driller's Timed-mode timer, an in-progress lesson, or an open
// story used to just get hidden by the blanket .tab-hiding below, not
// actually stopped — a driller's setInterval kept ticking against a
// container that no longer existed, and the abandoned lesson/story stayed
// resumable in memory even though nothing on screen suggested it. Each
// teardown here is a plain, idempotent state reset that doesn't itself
// navigate anywhere, so calling it from inside showTab() can't recurse.
function teardownTab(tabId) {
    if (tabId === 'drills' && typeof Workshop !== 'undefined') {
        Workshop.close();
    } else if (tabId === 'lesson-screen' && typeof teardownLesson === 'function') {
        teardownLesson();
    } else if (tabId === 'reader' && typeof Reader !== 'undefined' && Reader.currentStoryId) {
        Reader.closeStory();
    } else if (tabId === 'study-plan-screen' && typeof StudyPlanRunner !== 'undefined') {
        StudyPlanRunner.teardown();
    } else if (tabId === 'leveltest') {
        if (typeof LevelTest !== 'undefined' && typeof LevelTest.stop === 'function') LevelTest.stop();
        if (typeof DiagnosticTest !== 'undefined' && typeof DiagnosticTest.stop === 'function') DiagnosticTest.stop();
    }
}

function showTab(tabName, button, options) {
    const previousTab = document.querySelector('.tab:not(.hidden)');
    if (previousTab && previousTab.id !== tabName) {
        teardownTab(previousTab.id);
    }

    document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
    const tab = document.getElementById(tabName);
    if (tab) tab.classList.remove('hidden');

    document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
    const activeBtn = (button && button.matches && button.matches('.nav button[data-tab]'))
        ? button
        : (button && button.closest ? button.closest('.nav button[data-tab]') : null)
        || document.querySelector('.nav button[data-tab="' + tabName + '"]');
    if (activeBtn) activeBtn.classList.add('active');

    // The header is contextual — it names the room you just walked into.
    if (typeof PageHeader !== 'undefined') PageHeader.show(tabName);

    // Home is entirely counted from data other modules own, so it is redrawn
    // on entry rather than kept up to date. Walking back onto it after a
    // lesson is exactly when every number on it has just changed.
    if (tabName === 'home' && typeof Home !== 'undefined') {
        Home.render();
    }

    // Re-render on entry rather than trusting what was drawn last time. The
    // level list carries state the rest of the app changes — a finished
    // lesson, a passed level test — and coming back to a stale list is how a
    // pass appears not to have registered.
    if (tabName === 'learn' && typeof renderCurriculum === 'function') {
        renderCurriculum();
    }

    if (tabName === 'reader' && typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }

    if (tabName === 'drills' && typeof Workshop !== 'undefined') {
        Workshop.render();
    }

    // Decks opens on the browser, not mid-session: arriving at a flashcard
    // you did not ask for is disorienting, and the point of the tab now is
    // choosing what to study. Skipped when the caller is about to start a
    // specific session immediately (Home's "Review all" quick action) --
    // otherwise this fires an un-awaited Decks.render() that races the
    // quick action's own reviewDeck() call, and whichever async chain
    // resolves last silently wins the shared #decks-root/#review-session
    // DOM, sometimes freezing on the deck browser instead of the session.
    if (tabName === 'review' && typeof Decks !== 'undefined' && !(options && options.skipReviewReset)) {
        if (typeof endReviewSession === 'function') endReviewSession();
        else Decks.render();
    }

    // Rendered on entry rather than kept up to date: everything on it is
    // counted from data the rest of the app owns, so the only moment it can
    // be wrong is the moment you walk in.
    if (tabName === 'journey' && typeof Journey !== 'undefined') {
        Journey.render();
    }

    // Re-checked on every entry rather than relying solely on an explicit
    // advance signal: a lesson plan item's own "Done" button returns here
    // through closeLesson()'s generic lessonReturnTab, with no StudyPlan
    // awareness of its own — onEnter() reconciles the queue against real
    // curriculum state (LearnerPath.isComplete) whenever that happens.
    if (tabName === 'study-plan-screen' && typeof StudyPlanRunner !== 'undefined') {
        StudyPlanRunner.onEnter();
    }
}

// The Learn page is rendered by engine/curriculum.js. An earlier accordion
// version lived here (renderLearnPage/toggleLevel); nothing called it once
// renderCurriculum took over, and the level list replaced it entirely.

// --------------------------------------------
// Lesson close button (replaces inline onclick)
// --------------------------------------------

function _attachLessonClose() {
    const btn = document.getElementById('lesson-close-btn');
    if (btn) btn.addEventListener('click', () => closeLesson());

    // Clean browser history navigation: when in a lesson, pressing the browser's
    // back button (or Android/iOS back gesture) cleanly closes the lesson back to
    // the previous tab, without navigating away from the web app.
    window.addEventListener('popstate', e => {
        const isLessonOpen = document.body.classList.contains('in-lesson') ||
            (document.getElementById('lesson-screen') && !document.getElementById('lesson-screen').classList.contains('hidden'));
        if (isLessonOpen && typeof closeLesson === 'function') {
            closeLesson({ fromPopstate: true });
        }
    });

    // The Continue button is not bound here: renderStep() sets its onclick
    // every step, because the last step has to call finishLesson instead. A
    // listener here as well fired alongside that onclick, so one press
    // advanced two steps and the learner never saw every other screen.
}

// --------------------------------------------
// Lesson sound-effects toggle
// --------------------------------------------
// One global mute preference (see engine/sound.js), surfaced here because
// the lesson screen is the only place a sound effect plays today. Wired
// once at startup rather than per-lesson since the button itself is
// static markup — only its icon/label need refreshing, on click.

function _renderSoundToggleIcon(btn) {
    const isMuted = (typeof Sound !== 'undefined') && Sound.muted();
    btn.innerHTML = (typeof Art !== 'undefined')
        ? Art.icon(isMuted ? 'soundOff' : 'soundOn')
        : '';
    btn.setAttribute('aria-label', isMuted ? 'Sound effects off — tap to turn on' : 'Sound effects on — tap to turn off');
    btn.setAttribute('aria-pressed', String(!isMuted));
}

function _attachSoundToggle() {
    const btn = document.getElementById('lesson-sound-btn');
    if (!btn || typeof Sound === 'undefined') return;

    _renderSoundToggleIcon(btn);
    btn.addEventListener('click', () => {
        Sound.toggleMuted();
        _renderSoundToggleIcon(btn);
        // Immediate confirmation that turning it back on actually worked,
        // rather than the learner having to wait for the next exercise.
        if (!Sound.muted()) Sound.correct();
    });
}

// --------------------------------------------
// Nav delegation (replaces inline onclick)
// --------------------------------------------

// Icons are put in from the registry rather than written into the markup, so
// there is one place a shape is defined and index.html stays readable.
function _drawNavIcons() {
    if (typeof Art === 'undefined') return;
    document.querySelectorAll('.nav button[data-icon]').forEach(btn => {
        const label = btn.textContent.trim();
        btn.innerHTML = Art.icon(btn.dataset.icon) +
            '<span class="nav-label">' + label + '</span>';
    });
    if (typeof Theme !== 'undefined') Theme.apply();
}

function _attachNavEvents() {
    document.querySelector('.nav').addEventListener('click', e => {
        const btn = e.target.closest('button[data-tab]');
        if (btn) showTab(btn.dataset.tab, btn);
    });
}

// --------------------------------------------
// Startup
// --------------------------------------------

async function initialiseApp() {
    // Safety timer: guarantee boot screen dismissal within 6s even under network/runtime failure
    let _bootTimer = setTimeout(() => {
        _hideBootScreen();
    }, 6000);

    // Deep-link or course switch via query parameters e.g. ?minigame=hu-suffix or ?lang=hu
    const searchParams = new URLSearchParams(location.search);
    const langParam = searchParams.get('lang');
    const minigameParam = searchParams.get('minigame') || searchParams.get('driller');

    if (typeof Lang !== 'undefined') {
        if (langParam && Lang.available().includes(langParam)) {
            Lang.set(langParam);
        } else if (minigameParam) {
            if (minigameParam.startsWith('hu-') && Lang.code() !== 'hu') {
                Lang.set('hu');
            } else if (minigameParam === 'verbs' && !Lang.code().startsWith('es')) {
                Lang.set(Lang.defaultCode());
            }
        }
    }

    // A magic-link email lands back here as ?verify=<token> — exchange it
    // for a session before anything else, so My Journey's Account card
    // already reads as signed-in the moment the learner arrives.
    if (typeof Sync !== 'undefined') {
        try { await Sync.completeVerify(); } catch (error) { /* offline — the link stays usable */ }
    }

    loadDeck();
    loadKnownWords();
    loadXP();
    updateXPHeader();

    // Home is the landing section, so its header is the first one drawn.
    if (typeof PageHeader !== 'undefined') PageHeader.show('home');

    // Falls back to the default course when the chosen one has no content.
    try {
        window._curriculumData = await loadCurriculumData();
    } catch (err) {
        console.error('Failed to load curriculum data:', err);
        window._curriculumData = { units: [] };
    }

    // Nav
    _drawNavIcons();
    _attachNavEvents();

    // Learn page. Drawn at startup even though Home is what is on screen —
    // the Lessons tab is one tap away and should not arrive empty.
    if (typeof renderCurriculum === 'function') {
        try {
            await renderCurriculum();
        } catch (e) {
            console.error('Failed to render curriculum:', e);
        }
    }

    // Home page. After the curriculum, which it reads to name the next lesson.
    if (typeof Home !== 'undefined') {
        try {
            await Home.render();
        } catch (e) {
            console.error('Failed to render home:', e);
        }
    }

    _hideBootScreen();

    // Lesson screen events
    _attachLessonClose();
    _attachSoundToggle();

    // Verbs module — imports/verbs/verb-list.js is Spanish content with
    // no language scoping (same reason Workshop's own DRILLERS list gates
    // the Verb Driller card to Spanish), so initialising it under any
    // non-Spanish course fetches Spanish verb data nobody can reach and fails.
    if (typeof Verbs !== 'undefined' && (typeof Lang === 'undefined' || Lang.code().startsWith('es'))) {
        Verbs.init();
    }

    if (typeof updateReaderWordColors === 'function') {
        updateReaderWordColors();
    }

    // A one-time, friendly invite to back up progress — after everything
    // else has rendered, so it never delays or competes with the actual
    // app content. No-ops on its own if already signed in or already
    // shown once on this device.
    if (typeof Sync !== 'undefined') Sync.maybeShowFirstVisitPrompt();

    // Deep-link to a minigame/driller via query parameter e.g. ?minigame=verbs
    if (minigameParam && typeof Workshop !== 'undefined') {
        showTab('drills');
        const count = parseInt(searchParams.get('count') || '5', 10);
        const duration = parseInt(searchParams.get('duration') || '60', 10);
        const mode = searchParams.get('mode') || (minigameParam === 'verbs' ? 'speed' : undefined);
        const skill = searchParams.get('skill') || undefined;
        const direction = searchParams.get('direction') || (minigameParam === 'translation' ? 'alternate' : undefined);
        Workshop.open(minigameParam, { autoStart: true, count, duration, mode, skill, direction });
    }

    // Register Service Worker for offline PWA capabilities
    _initServiceWorker();
}

function _hideBootScreen() {
    const boot = document.getElementById('boot-screen');
    if (!boot) return;
    boot.classList.add('is-hidden');
    boot.addEventListener('transitionend', () => {
        if (boot.parentNode) boot.remove();
    }, { once: true });
    // Safety fallback in case transitionend event is missed
    setTimeout(() => {
        if (boot.parentNode) boot.remove();
    }, 600);
}

function _initServiceWorker() {
    if (typeof window === 'undefined' || !('serviceWorker' in navigator)) return;

    window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js').then(reg => {
            console.log('Parlour: ServiceWorker registered successfully, scope:', reg.scope);

            reg.addEventListener('updatefound', () => {
                const newWorker = reg.installing;
                if (!newWorker) return;
                newWorker.addEventListener('statechange', () => {
                    if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                        console.log('Parlour: New content available; will apply on refresh.');
                    }
                });
            });
        }).catch(err => {
            console.warn('Parlour: ServiceWorker registration skipped/failed:', err);
        });
    });

    function updateOnlineStatus() {
        const isOffline = !navigator.onLine;
        document.body.classList.toggle('is-offline', isOffline);
        let indicator = document.getElementById('offline-indicator');
        if (isOffline) {
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.id = 'offline-indicator';
                indicator.className = 'offline-banner';
                indicator.textContent = 'Working offline — your progress will be saved locally.';
                document.body.appendChild(indicator);
            }
            indicator.classList.remove('hidden');
        } else if (indicator) {
            indicator.classList.add('hidden');
        }
    }

    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    if (!navigator.onLine) {
        updateOnlineStatus();
    }
}

document.addEventListener('DOMContentLoaded', initialiseApp);