// ============================================
// DECK MATCH GAME
// ============================================
// Quizlet-style timed matching game. The board holds a fixed number of
// pairs at once (BOARD_SIZE) rather than the whole deck — a hundred-word
// deck would make an unplayably huge grid otherwise — but the SESSION
// covers every word in the deck: matching a pair removes it and, if
// words remain in the pool, pulls the next one onto the board in its
// place. The whole board (not just the vacated slot) reshuffles when
// that happens, so the new pair doesn't land somewhere a learner could
// predict just from watching where the old one disappeared. Timed from
// the first tap to the last pair of the whole session; the best time per
// deck is remembered so a learner can chase their own record, the same
// personal-best idea as the Verb Speed leaderboard
// (engine/verbs/leaderboard.js) — not a multiplayer ranking, this app
// has no accounts to compete against.
//
// Redesigned 2026-09-02 from an earlier version that dealt one fixed
// 8-pair sample and ended there — feedback was that a "match" round
// should work through everything a learner wants to review, the way
// Quizlet's own Match keeps serving new pairs until the set is done,
// not stop after one small random sample of it.

const DeckMatch = (function () {
    'use strict';

    const BOARD_SIZE = 8; // pairs visible on the board at once (up to 16 tiles)
    const WRONG_FLASH_MS = 500;
    // How long a just-matched pair sits visibly "correct" (CSS fades it
    // to opacity 0 over this same window) before the board reshuffles
    // around its replacement — long enough to read as a match, short
    // enough that a review session doesn't feel like it's stalling.
    const MATCH_FLASH_MS = 450;
    // A further pause AFTER the board has already reorganized, before
    // input re-enables — see _tileClick()'s match branch for why this is
    // a separate step from MATCH_FLASH_MS rather than just a longer flash.
    const SETTLE_MS = 250;

    let _container = null;
    let _deckId = null;
    let _words0 = []; // the full deck word list passed in — this session works through all of it
    let _totalWords = 0;
    let _pool = [];    // words not yet placed on the board, { uid, lemma, translation }
    let _active = [];  // words currently occupying board slots
    let _tiles = [];    // [{ id, uid, kind: 'lemma'|'translation', text, matched }]
    let _selected = [];  // up to 2 tile ids
    let _matchedTotal = 0; // pairs matched so far this whole session, not just the board
    let _busy = false;   // true while a wrong pair's flash or a match's refill beat is showing
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
    // ":stream" distinguishes this from any personal-best value a learner
    // might have set under the old fixed-8-pair-sample version of this
    // game — that measured a different thing (time to clear one small
    // random sample) and isn't a fair comparison against this version's
    // time (clearing the whole deck), so this starts its own record
    // rather than silently inheriting a now-incomparable number.
    function _bestKey() {
        return (typeof Lang !== 'undefined' ? Lang.key('deckMatchBest') : 'deckMatchBest') + ':stream:' + _deckId;
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

    // ---- Session setup ----
    function _startSession() {
        const shuffledAll = _shuffled(_words0).map((w, i) => ({ uid: i, lemma: w.lemma, translation: w.translation }));
        _totalWords = shuffledAll.length;
        _active = shuffledAll.slice(0, BOARD_SIZE);
        _pool = shuffledAll.slice(BOARD_SIZE);

        _selected = [];
        _matchedTotal = 0;
        _busy = false;
        _startTime = null;
        _finished = false;
        _finishMs = 0;
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }
        _buildTiles();
    }

    // Rebuilds the tile grid from whatever's currently in _active — called
    // both at session start and every time a match pulls a replacement in,
    // so the board's layout is always freshly (independently, per column)
    // shuffled rather than a new tile simply appearing wherever the old
    // one was.
    function _buildTiles() {
        const lemmaTiles = _active.map(w =>
            ({ id: 'l' + w.uid, uid: w.uid, kind: 'lemma', text: _withArticle(w.lemma), matched: false }));
        const translationTiles = _active.map(w =>
            ({ id: 't' + w.uid, uid: w.uid, kind: 'translation', text: w.translation || '—', matched: false }));
        const shuffledLemma = _shuffled(lemmaTiles);
        const shuffledTranslation = _shuffled(translationTiles);

        // Two fixed columns rather than one board shuffled as a whole —
        // .dkm-grid is a plain 2-column grid filled in DOM order, so
        // interleaving lemma/translation here (each shuffled only within
        // its own side) keeps English always in the left column and the
        // target language always in the right (2026-08-27: "English
        // should be in the left column"). Feedback: matching "which makes
        // the quick matching quite annoying" when either language could
        // land in either column and a learner had to scan the whole
        // board rather than just their own side.
        _tiles = [];
        for (let i = 0; i < shuffledLemma.length; i++) {
            _tiles.push(shuffledTranslation[i]);
            _tiles.push(shuffledLemma[i]);
        }
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
        _render();
    }

    // Removes a just-matched pair from the board and, if the session
    // isn't over, pulls the next word in from the pool and reshuffles the
    // remaining board around it.
    function _refill(matchedUid) {
        _active = _active.filter(w => w.uid !== matchedUid);

        if (_matchedTotal >= _totalWords) { _finish(); return; }

        if (_pool.length) _active.push(_pool.shift());
        _buildTiles();
        _render();
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
        const isMatch = a.uid === b.uid && a.kind !== b.kind;

        if (isMatch) {
            a.matched = true;
            b.matched = true;
            _matchedTotal++;
            _selected = [];
            _busy = true; // lock input for the whole flash + reorganize + settle sequence below
            _render();
            setTimeout(() => {
                // Reorganizing while still "busy" (not the reverse — a
                // learner tapping right as the previous match resolved
                // used to have their tap land on whatever new tile ended
                // up under their finger, since input unlocked in the same
                // instant the board reshuffled). Only once the new layout
                // is actually painted, and has sat still for its own
                // SETTLE_MS beat, does input come back — so the first tap
                // after a match always lands on the layout the learner
                // can actually see, never one still mid-change.
                _refill(a.uid);
                setTimeout(() => { _busy = false; }, SETTLE_MS);
            }, MATCH_FLASH_MS);
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
                        <p class="dkm-done-count">${_totalWords} word${_totalWords === 1 ? '' : 's'} matched</p>
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
                    <span class="dkm-progress">${_matchedTotal} / ${_totalWords}</span>
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
        if (restartBtn) restartBtn.onclick = () => { _startSession(); _render(); };

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
        _startSession();
        _render();
    }

    return { render };
})();
