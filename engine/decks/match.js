// ============================================
// DECK MATCH GAME
// ============================================
// Duolingo Match Madness-style matching game. The board holds a fixed
// number of pairs at once (BOARD_SIZE) rather than the whole deck — a
// hundred-word deck would make an unplayably huge grid otherwise — but
// the SESSION covers every word in the deck: matching a pair removes it
// and, if words remain in the pool, brings the next one onto the board.
// Each column (English / target language) keeps a STABLE order — a match
// just removes its two tiles and inserts one new pair at a random spot in
// each column, so every tile a learner hasn't matched yet stays right
// where they last saw it (nothing "reflows" except closing the gap the
// removed pair left). Timed from the first tap to the last pair of the
// whole session; the best time per deck is remembered so a learner can
// chase their own record, the same personal-best idea as the Verb Speed
// leaderboard (engine/verbs/leaderboard.js) — not a multiplayer ranking,
// this app has no accounts to compete against.
//
// Redesigned 2026-09-03: the previous version reshuffled EVERY remaining
// tile into a fresh random position on every match, on the theory that a
// stable slot would make the next pair guessable. In practice this meant
// a learner who tapped the next pair right as a match resolved could have
// their tap land on the wrong tile — nothing they'd already located held
// still. Told to look at how Duolingo's own Match Madness handles this:
// matched cards disappear, the rest of the board holds its position, and
// new cards enter without a full-board scramble. Kept the earlier
// "not obviously the very last slot" precaution — the new pair still
// lands at an independently random spot in each column, not stapled to
// the end — while dropping the "reshuffle everything" behavior entirely.

const DeckMatch = (function () {
    'use strict';

    const BOARD_SIZE = 8; // pairs visible on the board at once (up to 16 tiles)
    const WRONG_FLASH_MS = 500;
    // How long a just-matched pair sits visibly "correct" (CSS fades it
    // to opacity 0 over this same window) before it's actually removed
    // from the board — long enough to read as a match, short enough that
    // a review session doesn't feel like it's stalling.
    const MATCH_FLASH_MS = 450;
    // A further pause AFTER the new pair (if any) is inserted, before
    // input re-enables — see _tileClick()'s match branch for why this is
    // a separate step from MATCH_FLASH_MS rather than just a longer flash.
    const SETTLE_MS = 200;

    let _container = null;
    let _deckId = null;
    let _words0 = []; // the full deck word list passed in — this session works through all of it
    let _totalWords = 0;
    let _pool = [];    // words not yet placed on the board, { uid, lemma, translation }
    let _lemmaTiles = [];  // stable-order column: [{ id, uid, text, matched }]
    let _transTiles = [];  // stable-order column, same shape
    let _selected = [];  // up to 2 tile ids
    let _matchedTotal = 0; // pairs matched so far this whole session, not just the board
    let _busy = false;   // true while a wrong pair's flash or a match's flash+insert beat is showing
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

    // Inserts at a random index rather than always at the end — a brand
    // new pair landing on the exact same row in both columns (or always
    // at the bottom of both) would give away which two tiles just
    // arrived together. Each column gets its own independent random
    // index, so the two halves of a new pair essentially never line up.
    function _insertRandom(arr, item) {
        const idx = Math.floor(Math.random() * (arr.length + 1));
        arr.splice(idx, 0, item);
    }

    function _withArticle(lemma) {
        return (typeof Lexicon !== 'undefined' && Lexicon.withArticle) ? Lexicon.withArticle(lemma) : lemma;
    }

    // ---- Personal-best persistence, per deck ----
    // ":stream" distinguishes this from any personal-best value a learner
    // might have set under the original fixed-8-pair-sample version of
    // this game — that measured a different thing (time to clear one
    // small random sample) and isn't a fair comparison against this
    // version's time (clearing the whole deck), so this keeps its own
    // record rather than silently inheriting a now-incomparable number.
    // The reshuffle-every-match version in between used this same key —
    // its times are a reasonable comparison to this reflow version's
    // (both measure "time to clear the whole deck"), so no further key
    // change was needed for this redesign.
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
        const active = shuffledAll.slice(0, BOARD_SIZE);
        _pool = shuffledAll.slice(BOARD_SIZE);

        _selected = [];
        _matchedTotal = 0;
        _busy = false;
        _startTime = null;
        _finished = false;
        _finishMs = 0;
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }

        // Each column starts independently shuffled — matching still
        // isn't guessable from position alone — but from here on each
        // column's order is STABLE. A match only ever removes its own two
        // tiles and inserts one new pair (see _refill()); nothing else
        // in either column moves.
        _lemmaTiles = _shuffled(active).map(w =>
            ({ id: 'l' + w.uid, uid: w.uid, text: _withArticle(w.lemma), matched: false }));
        _transTiles = _shuffled(active).map(w =>
            ({ id: 't' + w.uid, uid: w.uid, text: w.translation || '—', matched: false }));
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

    // Removes a just-matched pair and, if the session isn't over, inserts
    // the next pool word into each column at its own random spot. Every
    // OTHER tile in both columns keeps its exact existing order — the
    // list just gets one shorter (or the same length, with the new pair
    // taking the matched pair's place) rather than being rebuilt.
    function _refill(matchedUid) {
        _lemmaTiles = _lemmaTiles.filter(t => t.uid !== matchedUid);
        _transTiles = _transTiles.filter(t => t.uid !== matchedUid);

        if (_matchedTotal >= _totalWords) { _finish(); return; }

        if (_pool.length) {
            const w = _pool.shift();
            _insertRandom(_lemmaTiles, { id: 'l' + w.uid, uid: w.uid, text: _withArticle(w.lemma), matched: false });
            _insertRandom(_transTiles, { id: 't' + w.uid, uid: w.uid, text: w.translation || '—', matched: false });
        }
        _render();
    }

    function _findTile(tileId) {
        return _lemmaTiles.find(t => t.id === tileId) || _transTiles.find(t => t.id === tileId);
    }

    function _tileClick(tileId) {
        if (_busy || _finished) return;
        const tile = _findTile(tileId);
        if (!tile || tile.matched || _selected.includes(tileId)) return;

        _startTimerIfNeeded();
        _selected.push(tileId);

        if (_selected.length < 2) { _render(); return; }

        const [aId, bId] = _selected;
        const a = _findTile(aId);
        const b = _findTile(bId);
        // Each uid appears exactly once per column, so two different tile
        // ids sharing a uid can only be one from each column already —
        // no separate "different column" check needed.
        const isMatch = a.uid === b.uid;

        if (isMatch) {
            a.matched = true;
            b.matched = true;
            _matchedTotal++;
            _selected = [];
            _busy = true; // lock input for the whole flash + remove/insert + settle sequence below
            _render();
            setTimeout(() => {
                // Removing/inserting while still "busy" (not the reverse
                // — see this file's header comment on why a learner's tap
                // landing right as the board changes used to go to the
                // wrong tile). Only once the updated layout is actually
                // painted, and has sat still for its own SETTLE_MS beat,
                // does input come back.
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
                    <div class="dkm-col">${_transTiles.map(_tileHtml).join('')}</div>
                    <div class="dkm-col">${_lemmaTiles.map(_tileHtml).join('')}</div>
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
