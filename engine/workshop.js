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
            icon: 'workshop',
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
            icon: 'reader',
            title: 'Translation Driller',
            sub: 'Translate real sentences, either direction.',
            containerId: 'translation-driller-root'
        },
        {
            id: 'vocabulary',
            icon: 'decks',
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
                        ${typeof Art !== 'undefined' ? Art.icon(d.icon) : ''}
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
