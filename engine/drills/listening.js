// ============================================
// LISTENING DRILLER
// ============================================
// Draws from content/<lang>/indexes/translation-index.json — the same
// sentence pairs Translation and Vocabulary Driller use, per-course —
// nothing authored specifically for this driller, per
// PARLOUR_LISTENING_SPEC.md §4's "the existing curriculum should provide
// much of the initial controlled content".
//
// Audio is speechSynthesis via engine/speech.js — no audio files, no
// pipeline (spec §3, §13: "TTS can be used where appropriate", "do not
// build... long-form authentic listening infrastructure" for v1). A course
// with no installed voice can't run this driller at all (there is nothing
// to test without audio), so the settings screen gates on Speech.available()
// the same way Speech itself hides its buttons rather than mispronouncing.
//
// Same shell as engine/drills/translation.js — settings -> session ->
// results, Count/Timed modes — but rendering goes to ListeningRunner
// instead of GrammarRunner, per spec §12: "Do not force audio exercises
// into the existing GrammarRunner."
//
// Four exercise types (spec §2), each normalised from the same pair:
//   Listen -> Meaning        multiple-choice English translations
//   Listen -> Spanish        multiple-choice Spanish sentences
//   Listen -> Type           type the full sentence
//   Listen -> Missing Word   partial transcript, type the blanked word
// One random applicable type per pair, same "mix instead of a type picker"
// approach as Vocabulary Driller — a builder returns null when a pair can't
// support it (e.g. too small a pool to find plausible decoys), so a session
// still naturally favours whichever types the data actually supports.

const ListeningDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;
    const WORD_RE = /\p{L}+/gu;

    let _phase = PHASE.SETTINGS;
    let _container = null;

    let _pairs = null; // content/<lang>/indexes/translation-index.json -> pairs[]

    let _mode = MODE.COUNT;
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

    function _wordCount(text) {
        return (text.match(/\S+/g) || []).length;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_pairs) return;
        const index = await Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] }));
        _pairs = index.pairs || [];
    }

    function _poolFor(level) {
        return level === 'all' ? _pairs : _pairs.filter(p => p.level === level);
    }

    // ---- Exercise builders — one per type in PARLOUR_LISTENING_SPEC.md §2 ----

    // Decoys of similar length from the same pool, so a learner can't just
    // spot the odd one out by size — spec §6's "linguistically plausible,
    // not obvious elimination", applied as a light, data-driven heuristic
    // rather than hand-authored near-miss sentences.
    function _pickSimilar(pool, pair, key, n) {
        const targetLen = _wordCount(pair[key]);
        const targetText = pair[key].toLowerCase();
        let candidates = pool.filter(p => p !== pair && p[key].toLowerCase() !== targetText);
        const similar = candidates.filter(p => Math.abs(_wordCount(p[key]) - targetLen) <= 2);
        if (similar.length >= n) candidates = similar;
        return _shuffled(candidates).slice(0, n).map(p => p[key]);
    }

    function _buildMeaning(pair, pool) {
        const decoys = _pickSimilar(pool, pair, 'english', DECOY_COUNT);
        if (decoys.length < DECOY_COUNT) return null;
        const options = _shuffled([pair.english, ...decoys]);
        return {
            kind: 'listen-choice',
            audio: pair.spanish,
            promptText: 'What does it mean?',
            options,
            correct: options.indexOf(pair.english),
            transcript: pair.spanish,
            translation: pair.english
        };
    }

    function _buildSpanishChoice(pair, pool) {
        const decoys = _pickSimilar(pool, pair, 'spanish', DECOY_COUNT);
        if (decoys.length < DECOY_COUNT) return null;
        const options = _shuffled([pair.spanish, ...decoys]);
        return {
            kind: 'listen-choice',
            audio: pair.spanish,
            promptText: 'Which sentence did you hear?',
            options,
            correct: options.indexOf(pair.spanish),
            transcript: pair.spanish,
            translation: pair.english
        };
    }

    function _buildType(pair) {
        return {
            kind: 'listen-type',
            audio: pair.spanish,
            answer: pair.spanish,
            transcript: pair.spanish,
            translation: pair.english
        };
    }

    // A blank shorter than 3 letters is usually "de/un/la" — trivially
    // guessable without listening at all, so the target word is picked from
    // whatever's left first.
    function _pickBlankWord(sentence) {
        const words = sentence.match(WORD_RE) || [];
        const eligible = words.filter(w => w.length >= 3);
        const pool = eligible.length ? eligible : words;
        return pool.length ? pool[Math.floor(Math.random() * pool.length)] : null;
    }

    // Unicode-aware word boundaries so an accented word (día) is matched
    // correctly — plain \b treats accented letters as non-word characters.
    function _blank(sentence, word) {
        const escaped = word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const re = new RegExp('(^|[^\\p{L}])(' + escaped + ')([^\\p{L}]|$)', 'iu');
        const m = sentence.match(re);
        if (!m) return null;
        const start = m.index + m[1].length;
        return sentence.slice(0, start) + '_____' + sentence.slice(start + m[2].length);
    }

    function _buildMissingWord(pair) {
        const word = _pickBlankWord(pair.spanish);
        if (!word) return null;
        const blanked = _blank(pair.spanish, word);
        if (!blanked) return null;
        return {
            kind: 'listen-missing-word',
            audio: pair.spanish,
            sentence: blanked,
            answer: word,
            transcript: pair.spanish,
            translation: pair.english
        };
    }

    const BUILDERS = [_buildMeaning, _buildSpanishChoice, _buildType, _buildMissingWord];

    function _buildExerciseFor(pair, pool) {
        const candidates = BUILDERS.map(fn => fn(pair, pool)).filter(Boolean);
        return candidates.length ? candidates[Math.floor(Math.random() * candidates.length)] : null;
    }

    function _buildPool(level) {
        const pool = _poolFor(level);
        return pool.map(pair => _buildExerciseFor(pair, pool)).filter(Boolean);
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
        if (!Speech.available()) {
            _container.innerHTML = `
                <h2 class="gd-title">Listening Driller</h2>
                <div class="gd-empty">This browser has no ${typeof Lang !== 'undefined' ? Lang.name() : 'course'}
                    voice installed, so there's nothing to listen to yet. Add one in your device's
                    language/speech settings and reopen this driller.</div>
            `;
            return;
        }

        const totalA1 = _pairs.filter(p => p.level === 'A1').length;
        const totalA2 = _pairs.filter(p => p.level === 'A2').length;

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Listening Driller</h2>
                <p class="gd-hint">Decode spoken ${Lang.name()} — meaning, matching, dictation and missing
                    words, all by ear. Play as many times as you like.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="ld-level">Level</label>
                    <select id="ld-level" class="vb-select">
                        <option value="all">All levels (${_pairs.length} sentences)</option>
                        <option value="A1">A1 (${totalA1} sentences)</option>
                        <option value="A2">A2 (${totalA2} sentences)</option>
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="ld-count">Number of items</label>
                        <select id="ld-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} items</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="ld-timer">Timer</label>
                        <select id="ld-timer" class="vb-select">
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

        const levelSelect = _container.querySelector('#ld-level');
        levelSelect.value = _level;
        levelSelect.addEventListener('change', e => { _level = e.target.value; });

        const countSelect = _container.querySelector('#ld-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#ld-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool(_level);
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No listening items found for this level yet.</div>
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
        return _mode === MODE.COUNT ? `${base} · Item ${_queueIndex + 1} of ${_queue.length}` : base;
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
        ListeningRunner.render(exerciseRoot, {
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
