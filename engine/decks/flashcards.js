// ============================================
// DECK FLASHCARDS
// ============================================
// The simplest of the three Quizlet-style study modes: one card at a
// time, tap to flip between the word and its translation, Prev/Next to
// move through the deck. Purely a study aid — unlike SRS review, nothing
// here is scheduled or persisted; the same deck can be flipped through as
// many times as the learner likes with no effect on review state.
//
// Shuffle here is a Spotify-style ON/OFF toggle over card PRESENTATION
// order only — it never touches the deck's own word list (that ordering,
// natural-vs-alphabetical, lives in engine/decks.js and is passed in as
// `options.words`). Toggling it on reshuffles from that original order;
// toggling it off restores that exact order — neither ever mutates the
// list the deck screen itself shows.

const DeckFlashcards = (function () {
    'use strict';

    let _container = null;
    let _original = []; // the order passed in — never reordered in place
    let _words = [];     // what's actually being presented: _original, or a shuffle of it
    let _shuffleOn = false;
    let _index = 0;
    let _flipped = false;
    let _onExit = null;

    function _escapeHtml(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _withArticle(lemma) {
        return (typeof Lexicon !== 'undefined' && Lexicon.withArticle) ? Lexicon.withArticle(lemma) : lemma;
    }

    function _render() {
        if (!_container) return;

        if (!_words.length) {
            _container.innerHTML = `
                <div class="dkf">
                    <button class="dk-back" data-flashcards-exit="1">← Back to deck</button>
                    <p class="dk-empty">No words to flip through yet.</p>
                </div>
            `;
            _wire();
            return;
        }

        const word = _words[_index];
        const done = _index >= _words.length;

        if (done) {
            _container.innerHTML = `
                <div class="dkf">
                    <button class="dk-back" data-flashcards-exit="1">← Back to deck</button>
                    <div class="dkf-done">
                        <p class="dkf-done-title">Done — ${_words.length} ${_words.length === 1 ? 'card' : 'cards'}</p>
                        <div class="dkf-done-actions">
                            <button class="btn-primary" data-flashcards-restart="1">Flip through again</button>
                            <button class="dk-secondary" data-flashcards-exit="1">Back to deck</button>
                        </div>
                    </div>
                </div>
            `;
            _wire();
            return;
        }

        _container.innerHTML = `
            <div class="dkf">
                <div class="dkf-head">
                    <button class="dk-back" data-flashcards-exit="1">← Back to deck</button>
                    <span class="dkf-count">${_index + 1} / ${_words.length}</span>
                    <button class="dkf-shuffle-toggle${_shuffleOn ? ' is-on' : ''}" data-flashcards-shuffle-toggle="1"
                        aria-pressed="${_shuffleOn}" aria-label="Shuffle">
                        ${(typeof Art !== 'undefined') ? Art.icon('shuffle') : ''}
                    </button>
                </div>
                <button class="dkf-card${_flipped ? ' is-flipped' : ''}" data-flashcards-flip="1" aria-label="Flip card">
                    <span class="dkf-card-face dkf-card-front">${_escapeHtml(_withArticle(word.lemma))}</span>
                    <span class="dkf-card-face dkf-card-back">${_escapeHtml(word.translation || '—')}</span>
                </button>
                <p class="dkf-hint">Tap the card to flip it</p>
                <div class="dkf-nav">
                    <button class="dk-secondary" data-flashcards-prev="1" ${_index === 0 ? 'disabled' : ''}>← Prev</button>
                    <button class="btn-primary" data-flashcards-next="1">${_index === _words.length - 1 ? 'Finish' : 'Next →'}</button>
                </div>
            </div>
        `;
        _wire();
    }

    function _wire() {
        const exitBtn = _container.querySelector('[data-flashcards-exit]');
        if (exitBtn) exitBtn.onclick = () => { if (_onExit) _onExit(); };

        const flipBtn = _container.querySelector('[data-flashcards-flip]');
        if (flipBtn) flipBtn.onclick = () => { _flipped = !_flipped; _render(); };

        const prevBtn = _container.querySelector('[data-flashcards-prev]');
        if (prevBtn) prevBtn.onclick = () => { if (_index > 0) { _index--; _flipped = false; _render(); } };

        const nextBtn = _container.querySelector('[data-flashcards-next]');
        if (nextBtn) nextBtn.onclick = () => { _index++; _flipped = false; _render(); };

        const shuffleToggle = _container.querySelector('[data-flashcards-shuffle-toggle]');
        if (shuffleToggle) shuffleToggle.onclick = () => {
            _shuffleOn = !_shuffleOn;
            _words = _shuffleOn ? _shuffled(_original) : _original.slice();
            _index = 0;
            _flipped = false;
            _render();
        };

        const restartBtn = _container.querySelector('[data-flashcards-restart]');
        if (restartBtn) restartBtn.onclick = () => {
            if (_shuffleOn) _words = _shuffled(_original); // a fresh shuffle each restart, not the same run replayed
            _index = 0;
            _flipped = false;
            _render();
        };
    }

    /**
     * @param {HTMLElement} root
     * @param {{ words: {lemma:string, translation:string}[], onExit: function }} options
     */
    function render(root, options) {
        _container = root;
        _original = ((options && options.words) || []).filter(w => w && w.lemma);
        _shuffleOn = false;
        _words = _original.slice();
        _index = 0;
        _flipped = false;
        _onExit = (options && options.onExit) || function () {};
        _render();
    }

    return { render };
})();
