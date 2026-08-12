// ============================================
// VOCABULARY DRILLER
// ============================================
// Draws from content/es/decks/decks.json (1,214 words, already built by
// build-manifest.py — the same file engine/decks.js fetches for the Decks
// tab) and generated/indexes/translation-index.json (the same sentence pool
// engine/drills/translation.js uses). Nothing authored specifically for
// this driller.
//
// Two exercise types, both already renderable by GrammarRunner, so this
// module reuses it rather than writing a third renderer:
//   Meaning — a word + 3 decoy translations -> multiple-choice.
//   Context — a real sentence containing the word, blanked out -> fill-blank.
// A word with no matching sentence in the corpus just doesn't appear in
// Context mode's pool (same "some pools run smaller" precedent as the
// Grammar Driller's skill enrichment).
//
// Collocations (the other sub-mode on the original roadmap) has no source
// data anywhere yet and is deliberately left out — see grammar-driller-spec
// memory for the equivalent Error Correction call.

const VocabularyDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const EXTYPE = { MEANING: 'meaning', CONTEXT: 'context' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;

    let _phase = PHASE.SETTINGS;
    let _container = null;

    let _words = null;      // decks.json -> words { lemma: {en, pos} }
    let _wordLevels = null; // lemma -> 'A1' | 'A2' | ... (from lesson decks)
    let _pairs = null;      // translation-index.json -> pairs[]

    let _mode = MODE.COUNT;
    let _exType = EXTYPE.MEANING;
    let _level = 'all';
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

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_words && _pairs) return;
        const [deckData, translationIndex] = await Promise.all([
            Content.json(Lang.content('decks/decks.json')).catch(() => ({ words: {}, decks: [] })),
            Content.json('generated/indexes/translation-index.json').catch(() => ({ pairs: [] }))
        ]);
        _words = deckData.words || {};
        _pairs = translationIndex.pairs || [];
        _wordLevels = {};
        (deckData.decks || []).filter(d => d.kind === 'lesson').forEach(d => {
            (d.lemmas || []).forEach(lemma => {
                if (!(lemma in _wordLevels)) _wordLevels[lemma] = d.level;
            });
        });
    }

    function _wordList(level) {
        return Object.keys(_words)
            .filter(lemma => level === 'all' || _wordLevels[lemma] === level)
            .map(lemma => ({ lemma, en: _words[lemma].en, pos: _words[lemma].pos }));
    }

    // Unicode-aware word boundaries so an accented lemma (día, año) is
    // matched correctly — plain \b treats accented letters as non-word
    // characters and misses them.
    function _wordRegex(lemma) {
        const escaped = lemma.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp('(^|[^\\p{L}])(' + escaped + ')([^\\p{L}]|$)', 'iu');
    }

    function _blankSentence(sentence, lemma) {
        const m = sentence.match(_wordRegex(lemma));
        if (!m) return null;
        const start = m.index + m[1].length;
        return sentence.slice(0, start) + '_____' + sentence.slice(start + m[2].length);
    }

    function _sentencesContaining(lemma) {
        const re = _wordRegex(lemma);
        return _pairs.filter(p => re.test(p.spanish));
    }

    // ---- Normalisation: a word -> GrammarRunner's shapes ----
    function _pickDecoys(word, n) {
        const candidates = Object.keys(_words).filter(l => l !== word.lemma && _words[l].en !== word.en);
        return _shuffled(candidates).slice(0, n).map(l => _words[l].en);
    }

    function _normaliseMeaning(word) {
        const options = _shuffled([word.en, ..._pickDecoys(word, DECOY_COUNT)]);
        return { kind: 'multiple-choice', question: `What does "${word.lemma}" mean?`, options, correct: options.indexOf(word.en) };
    }

    // Returns null when no sentence in the corpus contains this word —
    // caller filters those out rather than shipping a broken exercise.
    function _normaliseContext(word) {
        const candidates = _sentencesContaining(word.lemma);
        if (!candidates.length) return null;
        const pair = candidates[Math.floor(Math.random() * candidates.length)];
        const blanked = _blankSentence(pair.spanish, word.lemma);
        return blanked ? { kind: 'fill-blank', sentence: blanked, answer: word.lemma } : null;
    }

    function _buildPool(exType, level) {
        const words = _wordList(level);
        if (exType === EXTYPE.CONTEXT) {
            return words.map(_normaliseContext).filter(Boolean);
        }
        return words.map(_normaliseMeaning);
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
        const contextCount = _exType === EXTYPE.CONTEXT
            ? _buildPool(EXTYPE.CONTEXT, _level).length
            : null;
        const meaningCount = _wordList(_level).length;

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Vocabulary Driller</h2>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_exType === EXTYPE.MEANING ? ' active' : ''}"
                        data-extype="${EXTYPE.MEANING}" role="tab" aria-selected="${_exType === EXTYPE.MEANING}">Meaning</button>
                    <button class="vb-mode-btn${_exType === EXTYPE.CONTEXT ? ' active' : ''}"
                        data-extype="${EXTYPE.CONTEXT}" role="tab" aria-selected="${_exType === EXTYPE.CONTEXT}">Context</button>
                </div>
                <p class="gd-hint">
                    ${_exType === EXTYPE.MEANING
                        ? `${meaningCount} words · pick what a word means`
                        : `${contextCount} words with an example sentence · fill in the blank`}
                </p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="vd-level">Level</label>
                    <select id="vd-level" class="vb-select">
                        <option value="all">All levels</option>
                        <option value="A1">A1</option>
                        <option value="A2">A2</option>
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="vd-count">Number of words</label>
                        <select id="vd-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} words</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="vd-timer">Timer</label>
                        <select id="vd-timer" class="vb-select">
                            ${TIMER_PRESETS.map(v => `
                                <option value="${v}"${v === _timerMinutes ? ' selected' : ''}>${v === 1 ? '1 minute' : v + ' minutes'}</option>
                            `).join('')}
                        </select>
                    </div>
                `}

                <button class="vbtn vbtn-primary vbtn-block" data-action="start">Start</button>
            </div>
        `;

        _container.querySelectorAll('[data-extype]').forEach(btn => {
            btn.addEventListener('click', () => { _exType = btn.dataset.extype; _renderSettings(); });
        });
        _container.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => { _mode = btn.dataset.mode; _renderSettings(); });
        });

        const levelSelect = _container.querySelector('#vd-level');
        levelSelect.value = _level;
        levelSelect.addEventListener('change', e => { _level = e.target.value; });

        const countSelect = _container.querySelector('#vd-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#vd-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool(_exType, _level);
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No words found for this combination yet.</div>
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
        return _mode === MODE.COUNT ? `${base} · Word ${_queueIndex + 1} of ${_queue.length}` : base;
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
