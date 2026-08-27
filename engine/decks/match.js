// ============================================
// DECK MATCH GAME
// ============================================
// Quizlet-style timed matching game: tap a word, then tap its
// translation — a correct pair locks in place, a wrong one just clears
// the selection and tries again. One round is a fixed-size sample of the
// deck (large decks would make an unplayably huge grid otherwise), timed
// from the first tap; the best time per deck is remembered so a learner
// can chase their own record, the same personal-best idea as the Verb
// Speed leaderboard (engine/verbs/leaderboard.js) — not a multiplayer
// ranking, this app has no accounts to compete against.

const DeckMatch = (function () {
    'use strict';

    const ROUND_SIZE = 8; // pairs per round (up to 16 tiles) — Quizlet's own Match plays about this many at once
    const WRONG_FLASH_MS = 500;

    let _container = null;
    let _deckId = null;
    let _words0 = []; // the full deck word list passed in — this round's _words is a fresh sample of it
    let _words = [];   // this round's sampled words
    let _tiles = [];    // [{ id, wordIndex, kind: 'lemma'|'translation', text, matched }]
    let _selected = [];  // up to 2 tile ids
    let _matchedCount = 0;
    let _busy = false;   // true while a wrong pair's flash is showing
    let _startTime = null;
    let _elapsedInterval = null;
    let _finished = false;
    let _finishMs = 0;
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

    // ---- Personal-best persistence, per deck ----
    function _bestKey() {
        return (typeof Lang !== 'undefined' ? Lang.key('deckMatchBest') : 'deckMatchBest') + ':' + _deckId;
    }

    function _bestMs() {
        try {
            const raw = localStorage.getItem(_bestKey());
            return raw ? parseInt(raw, 10) : null;
        } catch (error) {
            return null;
        }
    }

    function _recordBest(ms) {
        const prev = _bestMs();
        if (prev !== null && prev <= ms) return prev;
        try { localStorage.setItem(_bestKey(), String(ms)); } catch (error) { /* private browsing: not fatal */ }
        return ms;
    }

    function _formatSeconds(ms) {
        return (ms / 1000).toFixed(1) + 's';
    }

    // ---- Round setup ----
    function _newRound() {
        const sample = _shuffled(_words0).slice(0, Math.min(ROUND_SIZE, _words0.length));
        _words = sample;

        const lemmaTiles = sample.map((word, i) =>
            ({ id: 'l' + i, wordIndex: i, kind: 'lemma', text: _withArticle(word.lemma), matched: false }));
        const translationTiles = sample.map((word, i) =>
            ({ id: 't' + i, wordIndex: i, kind: 'translation', text: word.translation || '—', matched: false }));
        const shuffledLemma = _shuffled(lemmaTiles);
        const shuffledTranslation = _shuffled(translationTiles);

        // Two fixed columns rather than one board shuffled as a whole —
        // .dkm-grid is a plain 2-column grid filled in DOM order, so
        // interleaving lemma/translation here (each shuffled only within
        // its own side) keeps the target language always in the left
        // column and English always in the right. Feedback: matching
        // "which makes the quick matching quite annoying" when either
        // language could land in either column and a learner had to scan
        // the whole board rather than just their own side (2026-08-27).
        _tiles = [];
        for (let i = 0; i < shuffledLemma.length; i++) {
            _tiles.push(shuffledLemma[i]);
            _tiles.push(shuffledTranslation[i]);
        }

        _selected = [];
        _matchedCount = 0;
        _busy = false;
        _startTime = null;
        _finished = false;
        _finishMs = 0;
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }
    }

    function _startTimerIfNeeded() {
        if (_startTime !== null) return;
        _startTime = Date.now();
        _elapsedInterval = setInterval(() => {
            const el = _container && _container.querySelector('.dkm-timer');
            if (el) el.textContent = _formatSeconds(Date.now() - _startTime);
        }, 100);
    }

    function _finish() {
        _finished = true;
        _finishMs = Date.now() - _startTime;
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }
        _recordBest(_finishMs);
    }

    function _tileClick(tileId) {
        if (_busy || _finished) return;
        const tile = _tiles.find(t => t.id === tileId);
        if (!tile || tile.matched || _selected.includes(tileId)) return;

        _startTimerIfNeeded();
        _selected.push(tileId);

        if (_selected.length < 2) { _render(); return; }

        const [aId, bId] = _selected;
        const a = _tiles.find(t => t.id === aId);
        const b = _tiles.find(t => t.id === bId);
        const isMatch = a.wordIndex === b.wordIndex && a.kind !== b.kind;

        if (isMatch) {
            a.matched = true;
            b.matched = true;
            _matchedCount++;
            _selected = [];
            if (_matchedCount === _words.length) _finish();
            _render();
        } else {
            _busy = true;
            _render(); // show both as "wrong" briefly
            setTimeout(() => {
                _busy = false;
                _selected = [];
                _render();
            }, WRONG_FLASH_MS);
        }
    }

    function _tileHtml(tile) {
        const isSelected = _selected.includes(tile.id);
        const isWrong = _busy && isSelected;
        const classes = ['dkm-tile'];
        if (tile.matched) classes.push('is-matched');
        else if (isWrong) classes.push('is-wrong');
        else if (isSelected) classes.push('is-selected');
        return `
            <button class="${classes.join(' ')}" data-match-tile="${tile.id}" ${tile.matched ? 'disabled' : ''}>
                ${_escapeHtml(tile.text)}
            </button>
        `;
    }

    function _render() {
        if (!_container) return;

        if (!_words0.length) {
            _container.innerHTML = `
                <div class="dkm">
                    <button class="dk-back" data-match-exit="1">← Back to deck</button>
                    <p class="dk-empty">Not enough words to play a matching round yet.</p>
                </div>
            `;
            _wire();
            return;
        }

        if (_finished) {
            const best = _bestMs();
            const isNewBest = best === _finishMs;
            _container.innerHTML = `
                <div class="dkm">
                    <button class="dk-back" data-match-exit="1">← Back to deck</button>
                    <div class="dkm-done">
                        <p class="dkm-done-time">${_formatSeconds(_finishMs)}</p>
                        ${isNewBest ? '<p class="dkm-new-best">New personal best!</p>' : (best !== null ? `<p class="dkm-best">Best: ${_formatSeconds(best)}</p>` : '')}
                        <div class="dkm-done-actions">
                            <button class="btn-primary" data-match-restart="1">Play again</button>
                            <button class="dk-secondary" data-match-exit="1">Back to deck</button>
                        </div>
                    </div>
                </div>
            `;
            _wire();
            return;
        }

        const best = _bestMs();
        _container.innerHTML = `
            <div class="dkm">
                <div class="dkm-head">
                    <button class="dk-back" data-match-exit="1">← Back to deck</button>
                    <span class="dkm-timer">${_startTime ? _formatSeconds(Date.now() - _startTime) : '0.0s'}</span>
                </div>
                ${best !== null ? `<p class="dkm-best-line">Best: ${_formatSeconds(best)}</p>` : ''}
                <div class="dkm-grid">
                    ${_tiles.map(_tileHtml).join('')}
                </div>
            </div>
        `;
        _wire();
    }

    function _wire() {
        const exitBtn = _container.querySelector('[data-match-exit]');
        if (exitBtn) exitBtn.onclick = () => { if (_elapsedInterval) clearInterval(_elapsedInterval); if (_onExit) _onExit(); };

        const restartBtn = _container.querySelector('[data-match-restart]');
        if (restartBtn) restartBtn.onclick = () => { _newRound(); _render(); };

        _container.querySelectorAll('[data-match-tile]').forEach(el => {
            el.onclick = () => { _tileClick(el.getAttribute('data-match-tile')); };
        });
    }

    /**
     * @param {HTMLElement} root
     * @param {{ words: {lemma:string, translation:string}[], deckId: string, onExit: function }} options
     */
    function render(root, options) {
        _container = root;
        _deckId = (options && options.deckId) || 'unknown';
        _words0 = ((options && options.words) || []).filter(w => w && w.lemma);
        _onExit = (options && options.onExit) || function () {};
        _newRound();
        _render();
    }

    return { render };
})();
