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

    const DEFAULT = 'es-latam';
    const SETTING_KEY = 'app_language';

    // Voice tags per course, best first.
    const VOICES = {
        'es-latam': ['es-MX', 'es-US', 'es-419', 'es-CO', 'es-AR', 'es-ES', 'es'],
        'es-es':    ['es-ES', 'es'],
        hu:         ['hu-HU', 'hu'],
        fr:         ['fr-FR', 'fr-CA', 'fr']
    };

    const NAMES = {
        'es-latam': 'Spanish (Latin America)',
        'es-es':    'Spanish (Spain)',
        hu:         'Hungarian',
        fr:         'French'
    };

    // Courses with real content behind them — what the language picker
    // (My Journey) offers. content/fr is still an empty folder (scaffolded
    // per multi-language-plan) so it stays out.
    const AVAILABLE = ['es-latam', 'es-es', 'hu'];

    let current = DEFAULT;
    try {
        const stored = localStorage.getItem(SETTING_KEY);
        current = (stored === 'es') ? 'es-latam' : (stored || DEFAULT);
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

    // Migrate older keys to course-scoped names without losing learner progress.
    function migrateLegacyKeys() {
        try {
            // 1. Unscoped legacy keys -> es:
            const legacy = {
                'spanishApp_srsDeck': 'es:srsDeck',
                'spanishMastery_progress': 'es:progress',
                'spanishApp_readStories': 'es:readStories'
            };
            for (const [from, to] of Object.entries(legacy)) {
                const value = localStorage.getItem(from);
                if (value !== null && localStorage.getItem(to) === null) {
                    localStorage.setItem(to, value);
                }
            }

            // 2. es: -> es-latam:
            const esToLatam = {
                'es:srsDeck': 'es-latam:srsDeck',
                'es:progress': 'es-latam:progress',
                'es:readStories': 'es-latam:readStories'
            };
            for (const [from, to] of Object.entries(esToLatam)) {
                const value = localStorage.getItem(from);
                if (value !== null && localStorage.getItem(to) === null) {
                    localStorage.setItem(to, value);
                }
            }

            // 3. Stored language setting migration
            if (localStorage.getItem(SETTING_KEY) === 'es') {
                localStorage.setItem(SETTING_KEY, 'es-latam');
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
