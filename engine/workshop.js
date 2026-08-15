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

    const DRILLERS = [
        {
            id: 'verbs',
            icon: 'verbs',
            title: 'Verb Driller',
            sub: 'Conjugation tables and speed drills.',
            containerId: 'verb-driller-root'
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
            sub: 'Decode spoken Spanish, by ear.',
            containerId: 'listening-driller-root'
        }
    ];

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
        listening: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="28" y="40" width="8" height="20" class="ps-ink"/><rect x="46" y="26" width="8" height="48" class="ps-ink"/><rect x="64" y="40" width="8" height="20" class="ps-accent"/>'
    };

    function _drillerIcon(id) {
        return `<svg class="wk-card-icon" viewBox="0 0 100 100" aria-hidden="true">${DRILLER_ICONS[id] || ''}</svg>`;
    }

    let _active = null; // null | 'verbs' | 'grammar'

    function _esc(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _pickerHtml() {
        return `
            <div class="wk-picker">
                ${DRILLERS.map(d => `
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
    }

    function _attachActiveEvents(root) {
        const back = root.querySelector('[data-action="back"]');
        if (back) back.addEventListener('click', close);
    }

    function _renderDriller(driller) {
        const DRILLER_MODULES = {
            grammar: typeof GrammarDriller !== 'undefined' ? GrammarDriller : null,
            translation: typeof TranslationDriller !== 'undefined' ? TranslationDriller : null,
            vocabulary: typeof VocabularyDriller !== 'undefined' ? VocabularyDriller : null,
            listening: typeof ListeningDriller !== 'undefined' ? ListeningDriller : null
        };

        if (driller.id === 'verbs' && typeof Verbs !== 'undefined') {
            Verbs.render();
        } else if (DRILLER_MODULES[driller.id]) {
            const container = document.getElementById(driller.containerId);
            if (container) DRILLER_MODULES[driller.id].render(container);
        }
    }

    function render() {
        const root = document.getElementById('drills-root');
        if (!root) return;

        if (!_active) {
            root.innerHTML = _pickerHtml();
            _attachPickerEvents(root);
            return;
        }

        const driller = DRILLERS.find(d => d.id === _active);
        if (!driller) { _active = null; return render(); }

        root.innerHTML = _activeHtml(driller);
        _attachActiveEvents(root);
        _renderDriller(driller);
    }

    function open(id) {
        _active = id;
        render();
    }

    function close() {
        _active = null;
        render();
    }

    return { render, open, close };
})();
