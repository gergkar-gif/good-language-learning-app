// ============================================
// MORPHOLOGY DRILLER (Hungarian)
// ============================================
// A UI wrapper around engine/morphology/hungarian.js's ladder() — the exact
// function that already powers the Reader's tap-a-word step-by-step popup
// ("barátaimmal" -> barát -> barátaim -> barátaimmal). Nothing new to
// author: every question here is built from a real word-index entry run
// through the same decomposition the Reader already ships.
//
// Framed as decoding practice bridging Reader and Workshop, per the design
// doc's own description of this driller — dictionary-wide rather than
// curriculum-scoped, since multi-morpheme words need real inflectional
// stacking (case+possessive, plural+case) that the 5-lesson A1 course
// hasn't reached yet.
//
// Both exercise kinds here are multiple-choice, rendered by GrammarRunner.
// "Construction" (put a decomposed word back together) is a fill-blank
// rather than sentence-builder — GrammarRunner's sentence-builder always
// labels itself "Build the sentence", which reads wrong for assembling one
// word, so fill-blank fits the copy better without changes to the shared
// renderer.

const HuMorphologyDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;
    const MAX_LEMMA_RANK = 6000;

    let _phase = PHASE.SETTINGS;
    let _container = null;

    // Each entry: { word, chain, breakdown } — ladder()'s own return
    // shape, kept as-is rather than re-normalised.
    let _stacked = null; // breakdown.length >= 2 - genuinely multi-suffix
    let _single = null;  // breakdown.length === 1

    // content/hu/reference/cases.json, shared with the Suffix Driller —
    // this driller decomposes the exact same case/plural/possessive
    // suffixes, just as a stack rather than one at a time, so the same
    // reference answers "what is this suffix, in general" here too. Each
    // ladder() breakdown row now carries a `concept` key (a case code, or
    // 'plural'/'possessive') matching this file's own top-level keys.
    let _reference = null;

    function _referenceFor(concept) {
        if (!_reference || !concept) return null;
        if (concept === 'plural' || concept === 'possessive') return _reference[concept] || null;
        return (_reference.cases && _reference.cases[concept]) || null;
    }

    let _mode = MODE.COUNT;
    let _questionCount = 10;
    let _timerMinutes = 2;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;

    let _timerInterval = null;
    let _endTime = 0;
    let _timeRemaining = 0;

    // ---- Helpers ----
    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _sample(list) {
        return list[Math.floor(Math.random() * list.length)];
    }

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_stacked && _single) return;
        const [dict, wordIndex] = await Promise.all([
            fetch('imports/dictionary/hungarian-en.json').then(r => r.ok ? r.json() : {}),
            Content.json(Lang.content('indexes/word-index.json')).catch(() => ({})),
            Lexicon.load(),
            Content.json(Lang.content('reference/cases.json')).catch(() => null).then(r => { _reference = r; })
        ]);

        _stacked = [];
        _single = [];

        const seen = new Set();
        for (const form in wordIndex) {
            const tag = wordIndex[form][0];
            if (!tag || (tag.pos !== 'noun' && tag.pos !== 'adjective')) continue;
            const rank = Lexicon.frequencyRank(tag.lemma);
            if (rank === null || rank >= MAX_LEMMA_RANK) continue;
            if (seen.has(form)) continue;
            seen.add(form);

            const result = HungarianMorphology.ladder(form, dict, wordIndex, tag.lemma);
            if (!result.chain.length) continue;

            const entry = { word: form, chain: result.chain, breakdown: result.breakdown };
            (result.breakdown.length >= 2 ? _stacked : _single).push(entry);
        }
    }

    // ---- Exercise builders -> GrammarRunner shapes ----
    function _decoyRoots(entry, pool, n) {
        const root = entry.chain[0].form;
        const candidates = pool.filter(e => e.chain[0].form !== root);
        return _shuffled(candidates).slice(0, n).map(e => e.chain[0].form);
    }

    function _buildDecomposition(entry, pool) {
        const decoys = _decoyRoots(entry, pool, DECOY_COUNT);
        if (decoys.length < DECOY_COUNT) return null;
        const root = entry.chain[0].form;
        const options = _shuffled([root, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `What's the root of "${entry.word}"?`,
            options,
            correct: options.indexOf(root),
            explanation: `${entry.word} = ${entry.chain[entry.chain.length - 1].translation}`
        };
    }

    // Bug found 2026-08-20: this used to always read entry.breakdown[0] —
    // fine for a single-suffix word, but _buildRecognition below samples a
    // RANDOM row of entry.breakdown, and for a stacked word (the pool
    // deliberately weights toward these) that's often the 2nd or 3rd
    // suffix, not the 1st. Decoys ended up filtered/drawn against whatever
    // the word's FIRST suffix meant, unrelated to the suffix the question
    // actually asks about — e.g. a question about an instrumental case
    // ending could get possessive-meaning decoys, since those just
    // happened to be other entries' first suffix. Now takes the sampled
    // row itself, and samples one row per OTHER entry (matching the
    // original's "one decoy candidate per other entry" variety) rather
    // than always their first row either.
    function _decoyLabels(row, pool, n) {
        const candidates = pool
            .map(e => _sample(e.breakdown))
            .filter(b => b.label !== row.label);
        return _shuffled(candidates).slice(0, n).map(b => b.label);
    }

    function _buildRecognition(entry, pool) {
        const row = _sample(entry.breakdown);
        const decoys = _decoyLabels(row, pool, DECOY_COUNT);
        if (decoys.length < DECOY_COUNT) return null;
        const options = _shuffled([row.label, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `What does "-${row.suffix}" contribute to "${entry.word}"?`,
            options,
            correct: options.indexOf(row.label),
            explanation: row.why || undefined,
            moreInfo: _referenceFor(row.concept)
        };
    }

    function _buildConstruction(entry) {
        const steps = entry.breakdown.map(b => `+ -${b.suffix} (${b.label})`).join(' ');
        // The reference for the LAST layer applied — usually the case,
        // when there is one, since a stack builds inside-out (plural or
        // possessive first, case last) and that's the layer a learner
        // most often stumbles on.
        const lastRow = entry.breakdown[entry.breakdown.length - 1];
        return {
            kind: 'fill-blank',
            sentence: `"${entry.chain[0].form}" (${entry.chain[0].translation}) ${steps} = ______`,
            answer: entry.word,
            explanation: `${entry.word} = ${entry.chain[entry.chain.length - 1].translation}`,
            moreInfo: _referenceFor(lastRow && lastRow.concept)
        };
    }

    function _buildExerciseFor(entry, pool) {
        const candidates = [_buildDecomposition(entry, pool), _buildRecognition(entry, pool)].filter(Boolean);
        if (entry.breakdown.length >= 2) candidates.push(_buildConstruction(entry));
        return candidates.length ? _sample(candidates) : null;
    }

    function _buildPool() {
        // Weight toward stacked forms (the genuinely multi-step ones) but
        // keep some single-suffix items in the mix — a session that's only
        // ever three-layer words is a harder driller than the settings
        // screen promises.
        const source = _stacked.concat(_shuffled(_single).slice(0, Math.max(_stacked.length, 50)));
        return _shuffled(source).slice(0, 400).map(e => _buildExerciseFor(e, source)).filter(Boolean);
    }

    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Morphology Driller</h2>
                <p class="gd-hint">Take Hungarian words apart, and put them back together — the same
                    step-by-step breakdown the Reader shows when you tap a word. Runs on the full
                    dictionary, so it can go beyond your lessons so far.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="hm-count">Number of questions</label>
                        <select id="hm-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} questions</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="hm-timer">Timer</label>
                        <select id="hm-timer" class="vb-select">
                            ${TIMER_PRESETS.map(v => `
                                <option value="${v}"${v === _timerMinutes ? ' selected' : ''}>${v === 1 ? '1 minute' : v + ' minutes'}</option>
                            `).join('')}
                        </select>
                    </div>
                `}

                <button class="vbtn vbtn-primary vbtn-block" data-action="start">Start</button>
            </div>
        `;

        _container.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => { _mode = btn.dataset.mode; _renderSettings(); });
        });

        const countSelect = _container.querySelector('#hm-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#hm-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool();
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No decomposable words available yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-settings">Change settings</button>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            return;
        }

        if (_mode === MODE.COUNT) {
            _queue = _takeN(pool, _questionCount);
        } else {
            _queue = _shuffled(pool);
            _timeRemaining = _timerMinutes * 60;
            _endTime = Date.now() + _timeRemaining * 1000;
            _timerInterval = setInterval(_tick, 250);
        }

        _queueIndex = 0;
        _phase = PHASE.SESSION;
        _renderSession();
    }

    function _tick() {
        const remaining = Math.max(0, Math.ceil((_endTime - Date.now()) / 1000));
        _timeRemaining = remaining;
        const el = _container.querySelector('.vspeed-timer-display');
        if (el) el.textContent = _formatTime(remaining);
        if (remaining <= 0) _finishSession();
    }

    function _scoreLabel() {
        const base = `${_correct}/${_seen} correct`;
        return _mode === MODE.COUNT ? `${base} · Question ${_queueIndex + 1} of ${_queue.length}` : base;
    }

    function _renderSession() {
        _container.innerHTML = `
            <div class="gd-hud">
                <span class="gd-hud-score">${_scoreLabel()}</span>
                ${_mode === MODE.TIMED ? `<span class="vspeed-timer-display">${_formatTime(_timeRemaining)}</span>` : ''}
                <button class="gd-change-skill" data-action="change-settings">Change settings</button>
            </div>
            <div class="gd-exercise"></div>
        `;
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const exerciseRoot = _container.querySelector('.gd-exercise');
        GrammarRunner.render(exerciseRoot, {
            exercise: _queue[_queueIndex],
            onResult: correct => {
                _seen++;
                if (correct) _correct++;
                const score = _container.querySelector('.gd-hud-score');
                if (score) score.textContent = _scoreLabel();
            },
            onNext: _nextExercise
        });
    }

    function _nextExercise() {
        if (_mode === MODE.COUNT && _queueIndex + 1 >= _queue.length) {
            _finishSession();
            return;
        }

        _queueIndex++;
        if (_queueIndex >= _queue.length) {
            _queue = _shuffled(_queue);
            _queueIndex = 0;
        }
        _renderSession();
    }

    // ================================================================
    //  RENDERING — Results
    // ================================================================
    function _finishSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.RESULTS;
        _renderResults();
    }

    function _renderResults() {
        const accuracy = _seen ? Math.round((_correct / _seen) * 100) : 0;

        _container.innerHTML = `
            <div class="vspeed-results">
                <h3 class="vspeed-results-title">Session Results</h3>
                <div class="vspeed-results-grid">
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Correct</span>
                        <span class="vspeed-stat-value">${_correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Wrong</span>
                        <span class="vspeed-stat-value">${_seen - _correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Accuracy</span>
                        <span class="vspeed-stat-value">${accuracy}%</span>
                    </div>
                </div>
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-primary" data-action="play-again">Play Again</button>
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>
                </div>
            </div>
        `;

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
    }

    function _abortSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    async function render(root) {
        _container = root;

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            _renderSettings();
        } else if (_phase === PHASE.SESSION) {
            _renderSession();
        } else {
            _renderResults();
        }
    }

    return { render };
})();
