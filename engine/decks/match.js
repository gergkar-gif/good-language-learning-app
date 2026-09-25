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
    // Cut from 500/450/200ms (Quizlet-level fluidity was the ask; the old
    // values left ~650ms of dead time after every correct match) down to
    // just enough for the flash to register.
    const WRONG_FLASH_MS = 200;
    // How long a just-matched pair sits visibly "correct" (CSS fades it
    // to opacity 0 over this same window) before it's actually removed
    // from the board — long enough to read as a match, short enough that
    // a review session doesn't feel like it's stalling.
    const MATCH_FLASH_MS = 120;
    // A further pause AFTER the new pair (if any) is inserted, before
    // input re-enables — see _tileClick()'s match branch for why this is
    // a separate step from MATCH_FLASH_MS rather than just a longer flash.
    const SETTLE_MS = 50;

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
    let _onComplete = null;
    let _exitLabel = null;
    let _timeLimitSeconds = null;
    let _wordsByUid = {};
    let _missedWords = new Map();
    let _matchedUids = new Set();
    let _srsCredit = false; // Decks only — lessons and the study plan reuse this game without touching the SRS schedule
    let _credited = false;
    let _feedbackMsg = '';

    function _escapeHtml(text) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(text)
            : String(text == null ? '' : text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
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
    // A word missed at any point this session is 'again'; one matched
    // cleanly is 'weak' (see creditPractice() in engine/srs.js). Sent once
    // per session — at the end, or on leaving partway — so a word missed
    // then matched still counts as missed, and unplayed words count as
    // nothing.
    function _creditSrs() {
        if (!_srsCredit || _credited || typeof creditPractice !== 'function') return;
        _credited = true;
        const results = [];
        _missedWords.forEach(w => results.push({ lemma: w.lemma, rating: 'again' }));
        _matchedUids.forEach(uid => {
            if (!_missedWords.has(uid)) results.push({ lemma: _wordsByUid[uid].lemma, rating: 'weak' });
        });
        creditPractice(results);
    }

    function _startSession() {
        _creditSrs();
        const shuffledAll = _shuffled(_words0).map((w, i) => ({ uid: i, lemma: w.lemma, translation: w.translation }));
        _wordsByUid = {};
        shuffledAll.forEach(w => { _wordsByUid[w.uid] = w; });
        _missedWords = new Map();
        _matchedUids = new Set();
        _credited = false;
        _feedbackMsg = '';
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
            if (_timeLimitSeconds) {
                const remainingSec = Math.max(0, _timeLimitSeconds - (Date.now() - _startTime) / 1000);
                if (el) el.textContent = remainingSec.toFixed(1) + 's';
                if (remainingSec <= 0) {
                    _finish();
                }
            } else {
                if (el) el.textContent = _formatSeconds(Date.now() - _startTime);
            }
        }, 100);
    }

    function _finish() {
        _finished = true;
        _finishMs = Date.now() - (_startTime || Date.now());
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }

        // Track remaining unmatched words if session ended before all were matched
        _lemmaTiles.forEach(t => {
            if (!t.matched && _wordsByUid[t.uid]) _missedWords.set(t.uid, _wordsByUid[t.uid]);
        });
        _pool.forEach(w => {
            if (_wordsByUid[w.uid]) _missedWords.set(w.uid, _wordsByUid[w.uid]);
        });

        _recordBest(_finishMs);
        _creditSrs();
        _render();
        if (typeof _onComplete === 'function') {
            _onComplete({ matched: _matchedTotal, total: _totalWords, timeMs: _finishMs });
        }
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

        if (_selected.length < 2) {
            _feedbackMsg = '';
            _render();
            return;
        }

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
            _matchedUids.add(a.uid);
            _selected = [];
            _feedbackMsg = '';
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
            if (_wordsByUid[a.uid]) _missedWords.set(a.uid, _wordsByUid[a.uid]);
            if (_wordsByUid[b.uid]) _missedWords.set(b.uid, _wordsByUid[b.uid]);
            _feedbackMsg = `✗ "${a.text}" does not match "${b.text}"`;
            _render(); // show both as "wrong" briefly
            setTimeout(() => {
                _busy = false;
                _selected = [];
                _render();
            }, Math.max(WRONG_FLASH_MS, 400));
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

        const exitText = _exitLabel || 'Back to deck';

        if (!_words0.length) {
            _container.innerHTML = `
                <div class="dkm">
                    <button class="dk-back" data-match-exit="1">← ${_escapeHtml(exitText)}</button>
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
                    <button class="dk-back" data-match-exit="1">← ${_escapeHtml(exitText)}</button>
                    <div class="dkm-done">
                        <p class="dkm-done-time">${_formatSeconds(_finishMs)}</p>
                        <p class="dkm-done-count">${_matchedTotal} / ${_totalWords} word${_totalWords === 1 ? '' : 's'} matched</p>
                        ${isNewBest && !_timeLimitSeconds ? '<p class="dkm-new-best">New personal best!</p>' : (best !== null && !_timeLimitSeconds ? `<p class="dkm-best">Best: ${_formatSeconds(best)}</p>` : '')}
                        ${_missedWords.size ? `
                            <div class="gd-missed-recap">
                                <h4 class="gd-missed-title">Review Missed Pairs</h4>
                                <div class="gd-missed-list">
                                    ${Array.from(_missedWords.values()).map(w => `
                                        <div class="gd-missed-card">
                                            <div class="gd-missed-q">${_escapeHtml(_withArticle(w.lemma))}</div>
                                            <div class="gd-missed-answers">
                                                <div class="gd-missed-correct"><span class="gd-badge-correct">Meaning:</span> <strong>${_escapeHtml(w.translation)}</strong></div>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        ` : ''}
                        <div class="dkm-done-actions">
                            <button class="btn-primary" data-match-restart="1">Play again</button>
                            <button class="dk-secondary" data-match-exit="1">${_escapeHtml(exitText)}</button>
                        </div>
                    </div>
                </div>
            `;
            _wire();
            if (typeof RecommendationEngine !== 'undefined') {
                RecommendationEngine.mountNextAction(_container, { excludeDrillerId: 'match' });
            }
            return;
        }

        const best = _bestMs();
        const timerVal = _timeLimitSeconds ? _timeLimitSeconds + '.0s' : (_startTime ? _formatSeconds(Date.now() - _startTime) : '0.0s');
        _container.innerHTML = `
            <div class="dkm">
                <div class="dkm-head">
                    <button class="dk-back" data-match-exit="1">← ${_escapeHtml(exitText)}</button>
                    <span class="dkm-progress">${_matchedTotal} / ${_totalWords}</span>
                    <span class="dkm-timer">${timerVal}</span>
                </div>
                ${best !== null && !_timeLimitSeconds ? `<p class="dkm-best-line">Best: ${_formatSeconds(best)}</p>` : ''}
                <div class="dkm-feedback" aria-live="polite">${_escapeHtml(_feedbackMsg || '')}</div>
                <div class="dkm-grid">
                    <div class="dkm-col">${_transTiles.map(_tileHtml).join('')}</div>
                    <div class="dkm-col">${_lemmaTiles.map(_tileHtml).join('')}</div>
                </div>
            </div>
        `;
        _wire();
    }

    function _wire() {
        const exitBtns = _container.querySelectorAll('[data-match-exit]');
        exitBtns.forEach(btn => {
            btn.onclick = () => { if (_elapsedInterval) clearInterval(_elapsedInterval); _creditSrs(); if (_onExit) _onExit(); };
        });

        const restartBtn = _container.querySelector('[data-match-restart]');
        if (restartBtn) restartBtn.onclick = () => { _startSession(); _render(); };

        _container.querySelectorAll('[data-match-tile]').forEach(el => {
            el.onclick = () => { _tileClick(el.getAttribute('data-match-tile')); };
        });
    }

    /**
     * @param {HTMLElement} root
     * @param {{ words: {lemma:string, translation:string}[], deckId: string, limit: number, timeLimit: number, exitLabel: string, onExit: function, onComplete: function, srsCredit: boolean }} options
     */
    function render(root, options) {
        _container = root;
        _deckId = (options && options.deckId) || 'unknown';
        const rawWords = ((options && options.words) || []).filter(w => w && (w.lemma || w.spanish));
        _words0 = rawWords.map(w => ({
            lemma: w.lemma || w.spanish,
            translation: w.translation || w.english || '—'
        }));
        if (options && options.limit && options.limit > 0) {
            _words0 = _words0.slice(0, options.limit);
        }
        _timeLimitSeconds = (options && options.timeLimit) ? Number(options.timeLimit) : null;
        _exitLabel = (options && options.exitLabel) || null;
        _onExit = (options && options.onExit) || function () {};
        _onComplete = (options && options.onComplete) || null;
        _srsCredit = !!(options && options.srsCredit);
        _credited = true; // nothing from a previous render() to send
        _startSession();
        _render();
    }

    function stop() {
        if (_elapsedInterval) { clearInterval(_elapsedInterval); _elapsedInterval = null; }
        _busy = false;
        _finished = false;
    }

    return { render, stop };
})();
