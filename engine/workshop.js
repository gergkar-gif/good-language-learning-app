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
            id: 'speaking',
            icon: 'speaking',
            title: 'Speaking Studio',
            sub: () => `Practise pronunciation, shadowing, and open-ended oral production.`,
            containerId: 'speaking-driller-root',
            category: 'studios'
        },
        {
            id: 'writing',
            icon: 'writing',
            title: 'Writing Studio',
            sub: () => `Sentence translation and open-ended composition with CEFR grading.`,
            containerId: 'writing-driller-root',
            category: 'studios'
        },
        {
            id: 'hu-verb-studio',
            icon: 'hu-morphology',
            title: 'Verb & Morphology Studio',
            sub: 'Conjugation, verbal prefixes, suffixes, and word decomposition.',
            containerId: 'hu-verb-studio-root',
            langs: ['hu'],
            category: 'studios'
        },
        {
            id: 'verbs',
            icon: 'verbs',
            title: 'Verb Driller',
            sub: 'Conjugation tables and speed drills.',
            containerId: 'verb-driller-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'foundations'
        },

        {
            id: 'listening',
            icon: 'listening',
            title: 'Listening Driller',
            sub: () => `Decode spoken ${(typeof Lang !== 'undefined') ? Lang.name() : 'the language'}, by ear.`,
            containerId: 'listening-driller-root',
            category: 'foundations'
        },
        {
            id: 'grammar',
            icon: 'grammar',
            title: 'Grammar Driller',
            sub: 'Practice by skill, drawn from every lesson.',
            containerId: 'grammar-driller-root',
            category: 'foundations'
        },
        {
            id: 'vocabulary',
            icon: 'vocabulary',
            title: 'Vocabulary Driller',
            sub: 'Meaning and context, drawn from every word taught.',
            containerId: 'vocabulary-driller-root',
            category: 'foundations',
            // Every exercise here infers a word from a real sentence context
            // (see PARLOUR_VOCABULARY_DRILLER_SPEC.md) — below B1 the
            // learner doesn't yet know enough surrounding vocabulary/grammar
            // for that inference to work, so it reads as a bare guessing
            // game rather than a useful drill. Gated the same way a
            // language-unavailable driller is: hidden from the picker, and
            // render() below bounces back to the picker if something still
            // tries to open it directly.
            minLevel: 'B1'
        }
    ];

    function _available(driller) {
        if (driller.langs) {
            const currentLang = typeof Lang !== 'undefined' ? Lang.code() : 'es-latam';
            if (!driller.langs.some(l => l === currentLang || currentLang.startsWith(l + '-'))) return false;
        }
        if (driller.minLevel) {
            const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];
            const level = (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel) ? LearnerPath.currentLevel() : 'A1';
            if (order.indexOf(level) < order.indexOf(driller.minLevel)) return false;
        }
        return true;
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
        // a microphone capsule with a projection beacon — oral production
        speaking: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="42" y="22" width="16" height="28" rx="8" class="ps-ink"/><path d="M34 40a16 16 0 0 0 32 0" class="ps-ink" fill="none" stroke="currentColor" stroke-width="4"/><line x1="50" y1="56" x2="50" y2="72" class="ps-ink" stroke="currentColor" stroke-width="4"/><line x1="38" y1="72" x2="62" y2="72" class="ps-ink" stroke="currentColor" stroke-width="4"/><circle cx="72" cy="28" r="6" class="ps-accent"/>',
        // a quill and manuscript — written production
        writing: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M30 70 L65 35 L75 45 L40 80 L25 85 Z" class="ps-ink"/><line x1="60" y1="40" x2="70" y2="50" class="ps-wash" stroke="currentColor" stroke-width="2"/><circle cx="75" cy="25" r="5" class="ps-accent"/>',
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

    // Grammar, vocabulary, and now any weak driller (see
    // engine/recommendationEngine.js) are independent candidates — any
    // subset can have something to suggest, so this renders up to three
    // action buttons under one shared blurb. Labels come from
    // RecommendationEngine.secondaryLabel() — shared with Home's own
    // secondary tier, so the two surfaces can't drift on how a candidate
    // reads. Each button carries its own index in the secondary array
    // (data-recommend-index) so _loadRecommendation() can route it via
    // RecommendationEngine.openSecondary() without re-deriving the kind.
    function _recommendationHtml(secondary) {
        if (!secondary || !secondary.length) return '';
        const anyWeak = secondary.some(c => c.reason === 'weak');
        const blurb = anyWeak
            ? "You've been shaky on some of this — a quick pass would help it stick."
            : "Fresh from your last lesson — reinforce it while it's recent.";
        const buttons = secondary.map((c, i) => `
            <span class="wk-recommend-item">
                <button class="wk-recommend-btn" data-recommend-index="${i}">
                    ${_esc(RecommendationEngine.secondaryLabel(c))} →
                </button>
                ${c.kind === 'elective' ? `<button class="wk-recommend-skip" data-recommend-skip="${i}">Not now</button>` : ''}
            </span>
        `).join('');
        return `
            <div class="wk-recommend">
                <span class="wk-recommend-eyebrow">Recommended for you</span>
                <span class="wk-recommend-body">${_esc(blurb)}</span>
                <div class="wk-recommend-actions">${buttons}</div>
            </div>
        `;
    }

    function _renderCards(items) {
        return items.map(d => `
            <button class="wk-card" data-driller="${d.id}">
                ${_drillerIcon(d.icon)}
                <span class="wk-card-body">
                    <span class="wk-card-title">${_esc(d.title)}</span>
                    <span class="wk-card-sub">${_esc(typeof d.sub === 'function' ? d.sub() : d.sub)}</span>
                </span>
                <span class="wk-card-arrow geo-triangle" aria-hidden="true"></span>
            </button>
        `).join('');
    }

    function _pickerHtml(recommendation) {
        const available = DRILLERS.filter(_available);
        const studios = available.filter(d => d.category === 'studios');
        const foundations = available.filter(d => d.category === 'foundations');
        return `
            ${_recommendationHtml(recommendation)}
            ${studios.length ? `
                <div class="wk-section-heading">Studios</div>
                <div class="wk-picker">
                    ${_renderCards(studios)}
                </div>
            ` : ''}
            ${foundations.length ? `
                <div class="wk-section-heading">Foundations</div>
                <div class="wk-picker">
                    ${_renderCards(foundations)}
                </div>
            ` : ''}
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
            speaking: typeof SpeakingDriller !== 'undefined' ? SpeakingDriller : null,
            writing: typeof WritingDriller !== 'undefined' ? WritingDriller : null,
            'hu-verb-studio': typeof HuVerbStudio !== 'undefined' ? HuVerbStudio : null,
            'hu-verb': typeof HuVerbDriller !== 'undefined' ? HuVerbDriller : null,
            'hu-suffix': typeof HuSuffixDriller !== 'undefined' ? HuSuffixDriller : null,
            'hu-prefix': typeof HuPrefixDriller !== 'undefined' ? HuPrefixDriller : null,
            'hu-morphology': typeof HuMorphologyDriller !== 'undefined' ? HuMorphologyDriller : null
        };
        return DRILLER_MODULES[id] || null;
    }

    function _renderDriller(driller) {
        if (driller.id === 'verbs' && typeof Verbs !== 'undefined') {
            return Verbs.render(_activeOptions);
        } else if (_moduleFor(driller.id)) {
            const container = document.getElementById(driller.containerId);
            if (container) return _moduleFor(driller.id).render(container, _activeOptions);
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
        if (typeof RecommendationEngine === 'undefined') return;
        RecommendationEngine.recommend().then(rec => {
            if (!rec || !rec.secondary.length || token !== _pickerToken) return;
            const target = document.getElementById('drills-root');
            if (!target || target !== root || _active) return;
            root.insertAdjacentHTML('afterbegin', _recommendationHtml(rec.secondary));

            // Each button's own candidate is closed over via its index
            // rather than round-tripped through data attributes — a word
            // list doesn't serialise cleanly into one, and every button
            // here is only ever wired against this exact rec anyway.
            root.querySelectorAll('[data-recommend-index]').forEach(btn => {
                const candidate = rec.secondary[Number(btn.getAttribute('data-recommend-index'))];
                btn.addEventListener('click', () => RecommendationEngine.openSecondary(candidate));
            });
            root.querySelectorAll('[data-recommend-skip]').forEach(btn => {
                const candidate = rec.secondary[Number(btn.getAttribute('data-recommend-skip'))];
                btn.addEventListener('click', () => {
                    RecommendationEngine.dismissUnit(candidate.unit.id);
                    render();
                });
            });
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
        return _renderDriller(driller);
    }

    // `options` is opaque here — Workshop just carries it to whichever
    // driller opens (e.g. `{ skill: 'location-with-ban-ben' }` for
    // GrammarDriller, from Home's post-unit practice nudge). A driller that
    // doesn't understand `options` just ignores the second render() arg.
    // Several drillers fetch content in their own render() before they can
    // draw anything, so open() shows a loading overlay across the gap
    // (see UI.showLoading) rather than leaving the old screen tappable.
    function _renderAndHideLoader(drillerTitle) {
        const label = drillerTitle ? `Loading ${drillerTitle}…` : 'Loading…';
        if (typeof UI !== 'undefined') UI.showLoading(label);
        return Promise.resolve(render()).finally(() => {
            if (typeof UI !== 'undefined') UI.hideLoading();
        });
    }

    function open(id, options) {
        // Transparent routing for Hungarian sub-drillers into the unified Verb & Morphology Studio
        if (id === 'hu-verb' || id === 'hu-suffix' || id === 'hu-prefix' || id === 'hu-morphology') {
            if (typeof Lang !== 'undefined' && Lang.code() !== 'hu') {
                Lang.set('hu');
            }
            _active = 'hu-verb-studio';
            _activeOptions = Object.assign({ activeTab: id }, options);
            return _renderAndHideLoader('Verb & Morphology Studio');
        }

        // Transparent routing for Translation driller into Writing Studio
        if (id === 'translation') {
            _active = 'writing';
            _activeOptions = Object.assign({ activeTab: 'translation' }, options);
            return _renderAndHideLoader('Writing Studio');
        }


        const driller = DRILLERS.find(d => d.id === id);
        if (driller && driller.langs && typeof Lang !== 'undefined' && !driller.langs.includes(Lang.code())) {
            Lang.set(driller.langs[0]);
        }
        _active = id;
        _activeOptions = options || null;
        return _renderAndHideLoader(driller ? driller.title : null);
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

    document.addEventListener('language-changed', () => {
        if (!_active) {
            render();
        }
    });

    // Whether a driller can be opened right now (language, minimum level) —
    // for buttons elsewhere that open one directly, so they don't offer a
    // driller that open() would only bounce back to the picker.
    function isAvailable(id) {
        const driller = DRILLERS.find(d => d.id === id);
        return !driller || _available(driller);
    }

    return { render, open, close, activeDriller, isAvailable };
})();

if (typeof window !== 'undefined') {
    window.Workshop = Workshop;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Workshop;
}
