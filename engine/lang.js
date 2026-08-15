// ============================================
// LANGUAGE
// ============================================
// Which course the learner is studying. Everything that is per-course — the
// content path, the saved progress, the SRS deck, the voice the app speaks
// with — hangs off this, so adding Hungarian is a matter of filling
// content/hu/ rather than hunting hardcoded paths through the engine.
//
// Deliberately NOT scoped by language: XP and the daily streak. Those record
// that the learner sat down and studied, which is a habit rather than a
// property of one course; splitting them would reset a streak every time
// somebody switched language.
//
// Content ids stay language-relative — a Hungarian lesson is 'lesson.a1.03'
// exactly as the Spanish one is. They never collide, because everything that
// stores them against a learner goes through key(), and everything that
// fetches them goes through content().

const Lang = (function () {
    'use strict';

    const DEFAULT = 'es';
    const SETTING_KEY = 'app_language';

    // Voice tags per course, best first. Latin American Spanish leads because
    // it is what the course's characters speak.
    const VOICES = {
        es: ['es-MX', 'es-US', 'es-419', 'es-CO', 'es-AR', 'es-ES', 'es'],
        hu: ['hu-HU', 'hu'],
        fr: ['fr-FR', 'fr-CA', 'fr']
    };

    const NAMES = { es: 'Spanish', hu: 'Hungarian', fr: 'French' };

    // Courses with real content behind them — what the language picker
    // (My Journey) offers. content/fr is still an empty folder (scaffolded
    // per multi-language-plan) so it stays out. content/hu has Unit 1 of
    // A1 (5 lessons) as of 2026-08-15 — no lexicon yet, so tap-a-word
    // translation won't resolve Hungarian's inflected forms, but the
    // lessons, exercises and stories all render.
    const AVAILABLE = ['es', 'hu'];

    let current = DEFAULT;
    try {
        current = localStorage.getItem(SETTING_KEY) || DEFAULT;
    } catch (error) {
        // Private browsing with storage disabled: the default is fine.
    }

    function code() {
        return current;
    }

    function defaultCode() {
        return DEFAULT;
    }

    function name() {
        return NAMES[current] || current;
    }

    // The display name for any course code, not just the current one —
    // for rendering a picker over all of them.
    function nameFor(otherCode) {
        return NAMES[otherCode] || otherCode;
    }

    function available() {
        return AVAILABLE.slice();
    }

    function voices() {
        return VOICES[current] || [current];
    }

    // A path inside the current course: content('lessons/a1/a1-01.json').
    function content(path) {
        return `content/${current}/${path}`;
    }

    // A localStorage key scoped to the current course. Spanish lesson 3 and
    // Hungarian lesson 3 share an id, so without this, finishing one would
    // mark the other complete and both decks would pour into one pile.
    function key(name) {
        return `${current}:${name}`;
    }

    // The keys below predate language scoping and hold the Spanish course's
    // data. Copy each to its scoped name once, leaving the original in place
    // so an older build of the app still finds it.
    function migrateLegacyKeys() {
        const legacy = {
            'spanishApp_srsDeck': 'es:srsDeck',
            'spanishMastery_progress': 'es:progress',
            'spanishApp_readStories': 'es:readStories'
        };
        try {
            for (const [from, to] of Object.entries(legacy)) {
                const value = localStorage.getItem(from);
                if (value !== null && localStorage.getItem(to) === null) {
                    localStorage.setItem(to, value);
                }
            }
        } catch (error) {
            console.warn('Language: could not migrate saved data', error);
        }
    }

    function set(next) {
        if (!next || next === current) return;
        current = next;
        try {
            localStorage.setItem(SETTING_KEY, next);
        } catch (error) {
            console.warn('Language: could not save the chosen course', error);
        }
        document.dispatchEvent(new CustomEvent('language-changed', { detail: next }));
    }

    migrateLegacyKeys();

    return { code, defaultCode, name, nameFor, available, voices, content, key, set };
})();
