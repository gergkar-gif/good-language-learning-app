// ============================================
// WORKSHOP
// ============================================
// Workshop is a hub, not a driller itself: it owns #drills-root and hands off
// to whichever driller the learner picks. Each driller (Verbs, GrammarDriller,
// ...) renders into its own container and knows nothing about the others —
// Workshop just remembers which one is open and draws the "back" chrome
// around it.

const Workshop = (function () {
    'use strict';

    // `langs` is omitted where a driller is genuinely language-agnostic
    // (drawn from generated indexes that, once HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md's
    // language-scoping fix lands, resolve per course) — those fail gracefully
    // to an honest empty pool today, which is a fine state to show. `verbs`
    // is the one exception: imports/verbs/verb-list.js is a plain global
    // script with no language scoping at all, so without a gate here a
    // Hungarian learner would silently drill *Spanish* conjugation under a
    // Hungarian course — wrong content, not just missing content — until
    // engine/verbs/ gets the rewrite multi-language-plan already calls for.
    const DRILLERS = [
        {
            id: 'verbs',
            icon: 'verbs',
            title: 'Verb Driller',
            sub: 'Conjugation tables and speed drills.',
            containerId: 'verb-driller-root',
            langs: ['es']
        },
        {
            id: 'grammar',
            icon: 'grammar',
            title: 'Grammar Driller',
            sub: 'Practice by skill, drawn from every lesson.',
            containerId: 'grammar-driller-root'
        },
        {
            id: 'translation',
            icon: 'translation',
            title: 'Translation Driller',
            sub: 'Translate real sentences, either direction.',
            containerId: 'translation-driller-root'
        },
        {
            id: 'vocabulary',
            icon: 'vocabulary',
            title: 'Vocabulary Driller',
            sub: 'Meaning and context, drawn from every word taught.',
            containerId: 'vocabulary-driller-root'
        },
        {
            id: 'listening',
            icon: 'listening',
            title: 'Listening Driller',
            sub: `Decode spoken ${(typeof Lang !== 'undefined') ? Lang.name() : 'the language'}, by ear.`,
            containerId: 'listening-driller-root'
        },
        {
            id: 'hu-verb',
            icon: 'hu-verb',
            title: 'Verb Driller',
            sub: 'Decode and produce Hungarian verb forms.',
            containerId: 'hu-verb-driller-root',
            langs: ['hu']
        },
        {
            id: 'hu-suffix',
            icon: 'hu-suffix',
            title: 'Suffix Driller',
            sub: 'Plurals, possession, and case — attach the right ending.',
            containerId: 'hu-suffix-driller-root',
            langs: ['hu']
        },
        {
            id: 'hu-prefix',
            icon: 'hu-prefix',
            title: 'Prefix Driller',
            sub: 'Verb prefixes — meaning and construction.',
            containerId: 'hu-prefix-driller-root',
            langs: ['hu']
        },
        {
            id: 'hu-morphology',
            icon: 'hu-morphology',
            title: 'Morphology Driller',
            sub: 'Take Hungarian words apart, and put them back together.',
            containerId: 'hu-morphology-driller-root',
            langs: ['hu']
        }
    ];

    function _available(driller) {
        return !driller.langs || driller.langs.includes(Lang.code());
    }

    // Each driller's own mark, two-tone in the same --wash/--ink/--accent
    // formula as the Lessons path art (PATH_SHAPES in engine/curriculum.js)
    // — the visual language the user asked to keep for future work. These
    // used to borrow icons from unrelated sections (Translation wore the
    // Library icon, Vocabulary wore the Decks icon); each is now its own.
    const DRILLER_ICONS = {
        // a table corner — rows and columns, the conjugation grid
        verbs: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 50 8A42 42 0 0 1 92 50Z" class="ps-ink"/><rect x="20" y="60" width="16" height="16" class="ps-accent"/>',
        // a rule bracketing a peak — structure, the shape of a sentence
        grammar: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 10 84 70 16 70Z" class="ps-ink"/><circle cx="50" cy="10" r="7" class="ps-accent"/>',
        // a disc split in two and rejoined at the centre — meaning crossing between languages
        translation: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 8A42 42 0 0 1 50 92Z" class="ps-ink"/><circle cx="50" cy="50" r="7" class="ps-accent"/>',
        // a card standing on the disc — one word, given room
        vocabulary: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="30" y="22" width="30" height="42" rx="2" class="ps-ink"/><rect x="38" y="70" width="14" height="10" class="ps-accent"/>',
        // a waveform — sound decoded into bars
        listening: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="28" y="40" width="8" height="20" class="ps-ink"/><rect x="46" y="26" width="8" height="48" class="ps-ink"/><rect x="64" y="40" width="8" height="20" class="ps-accent"/>',
        // a root block with a smaller piece attached at its edge — a
        // suffix/case ending joining onto a stem
        'hu-suffix': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="20" y="34" width="36" height="32" class="ps-ink"/><rect x="56" y="42" width="20" height="16" class="ps-accent"/>',
        // the same join, mirrored — a prefix attaching ahead of the stem
        'hu-prefix': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="44" y="34" width="36" height="32" class="ps-ink"/><rect x="24" y="42" width="20" height="16" class="ps-accent"/>',
        // a word split into stacked segments — decomposition
        'hu-morphology': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="26" y="26" width="48" height="12" class="ps-ink"/><rect x="26" y="44" width="48" height="12" class="ps-accent"/><rect x="26" y="62" width="30" height="12" class="ps-ink"/>',
        // the table-corner mark again, distinct fill order from the
        // Spanish Verb Driller's since only one of the two ever shows
        'hu-verb': '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 92 50 8A42 42 0 0 1 50 92Z" class="ps-ink"/><rect x="60" y="60" width="16" height="16" class="ps-accent"/>'
    };

    function _drillerIcon(id) {
        return `<svg class="wk-card-icon" viewBox="0 0 100 100" aria-hidden="true">${DRILLER_ICONS[id] || ''}</svg>`;
    }

    let _active = null; // null | 'verbs' | 'grammar'
    let _activeOptions = null; // passed through to the open driller's render(), e.g. { skill }

    function _esc(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    // A raw skill id ("location-with-ban-ben", "subjuntivo-deseos") has no
    // curated display title outside GrammarDriller's own bank data, which
    // is private to that module — rather than reach into it, this just
    // turns hyphens into spaces and title-cases. Good enough for a one-line
    // recommendation; GrammarDriller's own settings screen still shows the
    // real bank title once the session is open.
    function _humanizeSkill(id) {
        return String(id || '').replace(/[-_]+/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    }

    // Grammar and vocabulary are independent halves (see engine/recommend.js)
    // — either, both, or neither can have something to suggest, so this
    // renders up to two action buttons under one shared blurb rather than
    // the single whole-card button it used to be when there was only ever
    // one thing to recommend.
    function _recommendationHtml(rec) {
        if (!rec || (!rec.skill && !rec.words.length)) return '';
        const anyWeak = rec.skillReason === 'weak' || rec.wordsReason === 'weak';
        const blurb = anyWeak
            ? "You've been shaky on some of this — a quick pass would help it stick."
            : "Fresh from your last lesson — reinforce it while it's recent.";
        return `
            <div class="wk-recommend">
                <span class="wk-recommend-eyebrow">Recommended for you</span>
                <span class="wk-recommend-body">${_esc(blurb)}</span>
                <div class="wk-recommend-actions">
                    ${rec.skill ? `
                        <button class="wk-recommend-btn" data-recommend-skill="${_esc(rec.skill)}">
                            Grammar: ${_esc(_humanizeSkill(rec.skill))} →
                        </button>
                    ` : ''}
                    ${rec.words.length ? `
                        <button class="wk-recommend-btn" data-recommend-vocab="1">
                            Vocabulary (${rec.words.length}) →
                        </button>
                    ` : ''}
                </div>
            </div>
        `;
    }

    function _pickerHtml(recommendation) {
        return `
            ${_recommendationHtml(recommendation)}
            <div class="wk-picker">
                ${DRILLERS.filter(_available).map(d => `
                    <button class="wk-card" data-driller="${d.id}">
                        ${_drillerIcon(d.icon)}
                        <span class="wk-card-body">
                            <span class="wk-card-title">${_esc(d.title)}</span>
                            <span class="wk-card-sub">${_esc(d.sub)}</span>
                        </span>
                        <span class="wk-card-arrow geo-triangle" aria-hidden="true"></span>
                    </button>
                `).join('')}
            </div>
        `;
    }

    function _activeHtml(driller) {
        return `
            <button class="wk-back" data-action="back">← Workshop</button>
            <div id="${driller.containerId}"></div>
        `;
    }

    function _attachPickerEvents(root) {
        root.querySelectorAll('[data-driller]').forEach(btn => {
            btn.addEventListener('click', () => open(btn.dataset.driller));
        });
        // The recommendation card itself is patched in later, by
        // _loadRecommendation() — it doesn't exist in `root` yet at this
        // point, so its own buttons are wired there instead.
    }

    function _attachActiveEvents(root) {
        const back = root.querySelector('[data-action="back"]');
        if (back) back.addEventListener('click', close);
    }

    // Every driller except Verbs (which predates this shape and manages its
    // own container directly) shares one render(container, options) shape —
    // shared with _stopActiveDriller() below, so the id-to-module mapping
    // lives in exactly one place.
    function _moduleFor(id) {
        const DRILLER_MODULES = {
            grammar: typeof GrammarDriller !== 'undefined' ? GrammarDriller : null,
            translation: typeof TranslationDriller !== 'undefined' ? TranslationDriller : null,
            vocabulary: typeof VocabularyDriller !== 'undefined' ? VocabularyDriller : null,
            listening: typeof ListeningDriller !== 'undefined' ? ListeningDriller : null,
            'hu-verb': typeof HuVerbDriller !== 'undefined' ? HuVerbDriller : null,
            'hu-suffix': typeof HuSuffixDriller !== 'undefined' ? HuSuffixDriller : null,
            'hu-prefix': typeof HuPrefixDriller !== 'undefined' ? HuPrefixDriller : null,
            'hu-morphology': typeof HuMorphologyDriller !== 'undefined' ? HuMorphologyDriller : null
        };
        return DRILLER_MODULES[id] || null;
    }

    function _renderDriller(driller) {
        if (driller.id === 'verbs' && typeof Verbs !== 'undefined') {
            Verbs.render();
        } else if (_moduleFor(driller.id)) {
            const container = document.getElementById(driller.containerId);
            if (container) _moduleFor(driller.id).render(container, _activeOptions);
        }
    }

    // Stops whatever the currently-open driller is doing (chiefly: a
    // Timed-mode setInterval) before Workshop switches away from it —
    // closing a driller, whether via its own back button or by leaving the
    // Workshop tab entirely, used to only swap out the DOM, leaving that
    // timer running forever against a container that no longer exists.
    function _stopActiveDriller() {
        if (!_active) return;
        if (_active === 'verbs') {
            if (typeof VerbsSpeed !== 'undefined') VerbsSpeed.reset();
            return;
        }
        const mod = _moduleFor(_active);
        if (mod && typeof mod.stop === 'function') mod.stop();
    }

    // The picker itself renders synchronously, same as always — the
    // "Recommended for you" card is fetched separately afterwards and
    // patched in once ready (grammar-index.json can be several hundred KB
    // on a course with a lot of content; blocking the whole picker on it
    // would turn opening Workshop into a wait). _pickerToken guards against
    // patching a stale picker if the learner has already navigated away or
    // opened a driller by the time the fetch resolves.
    let _pickerToken = 0;

    function _loadRecommendation(root, token) {
        if (typeof Recommend === 'undefined') return;
        Recommend.recommend().then(rec => {
            if (!rec || token !== _pickerToken) return;
            const target = document.getElementById('drills-root');
            if (!target || target !== root || _active) return;
            root.insertAdjacentHTML('afterbegin', _recommendationHtml(rec));

            const grammarBtn = root.querySelector('[data-recommend-skill]');
            if (grammarBtn) {
                grammarBtn.addEventListener('click', () => open('grammar', { skill: grammarBtn.getAttribute('data-recommend-skill') }));
            }
            // rec.words is closed over here rather than round-tripped through
            // a data attribute — a word list doesn't serialise cleanly into
            // one, and this handler is only ever wired against this exact
            // rec anyway.
            const vocabBtn = root.querySelector('[data-recommend-vocab]');
            if (vocabBtn) {
                vocabBtn.addEventListener('click', () => open('vocabulary', { words: rec.words }));
            }
        }).catch(() => {});
    }

    function render() {
        const root = document.getElementById('drills-root');
        if (!root) return;

        if (!_active) {
            _pickerToken++;
            root.innerHTML = _pickerHtml(null);
            _attachPickerEvents(root);
            _loadRecommendation(root, _pickerToken);
            return;
        }

        const driller = DRILLERS.find(d => d.id === _active);
        if (!driller || !_available(driller)) { _active = null; return render(); }

        root.innerHTML = _activeHtml(driller);
        _attachActiveEvents(root);
        _renderDriller(driller);
    }

    // `options` is opaque here — Workshop just carries it to whichever
    // driller opens (e.g. `{ skill: 'location-with-ban-ben' }` for
    // GrammarDriller, from Home's post-unit practice nudge). A driller that
    // doesn't understand `options` just ignores the second render() arg.
    function open(id, options) {
        _active = id;
        _activeOptions = options || null;
        render();
    }

    function close() {
        _stopActiveDriller();
        _active = null;
        _activeOptions = null;
        render();
    }

    // Exposed for the bug-report button — it can only tell context apart at
    // the tab level (`#drills`) otherwise, so a flag filed from inside a
    // specific driller (Verb, Grammar, ...) would report the same generic
    // "drills" location as one filed from the driller picker itself.
    function activeDriller() {
        if (!_active) return null;
        const driller = DRILLERS.find(d => d.id === _active);
        return driller ? { id: driller.id, title: driller.title } : null;
    }

    return { render, open, close, activeDriller };
})();
