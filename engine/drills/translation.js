// ============================================
// TRANSLATION DRILLER
// ============================================
// Draws from content/<lang>/indexes/translation-index.json (built per-course
// by scripts/build_translation_index.py out of grammar examples and
// sentence-builder exercises — nothing authored specifically for this
// driller).
//
// Same shell as engine/drills/grammar.js — settings -> session -> results,
// Count/Timed modes reusing engine/verbs/speed.js's .vspeed-* timer/results
// CSS — but rendering is handed to TranslationRunner instead of
// GrammarRunner, since translation is self-graded rather than auto-checked.

const TranslationDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const DIRECTION = { ES_EN: 'es-en', EN_ES: 'en-es', MIXED: 'mixed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];

    let _phase = PHASE.SETTINGS;
    let _container = null;

    let _pairs = null; // content/<lang>/indexes/translation-index.json -> pairs[]

    let _mode = MODE.COUNT;
    let _direction = DIRECTION.ES_EN;
    let _level = 'all';
    let _topic = 'all';
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

    function _esc(text) {
        return (typeof UI !== 'undefined' && UI.escape) ? UI.escape(text) : String(text == null ? '' : text);
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_pairs) return;
        const index = await Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] }));
        _pairs = index.pairs || [];
    }

    function _byLevel(level) {
        return level === 'all' ? _pairs : _pairs.filter(p => p.level === level);
    }

    function _poolFor(level, topic) {
        const byLevel = _byLevel(level);
        return topic === 'all' ? byLevel : byLevel.filter(p => p.topic === topic);
    }

    // Distinct topics among this level's pairs, alphabetical, with counts —
    // scoped to the level so switching level always shows a topic list
    // that's actually browsable (the full cross-level set is 100+, one
    // level's worth is usually a few dozen). Pairs without a derived topic
    // (a handful of irregular filenames — see build_translation_index.py)
    // aren't lost, they're just not filterable by topic; "All topics"
    // still includes them.
    function _topicsFor(level) {
        const counts = new Map();
        _byLevel(level).forEach(p => {
            if (!p.topic) return;
            counts.set(p.topic, (counts.get(p.topic) || 0) + 1);
        });
        return Array.from(counts.entries()).sort((a, b) => a[0].localeCompare(b[0]));
    }

    // ---- Normalisation: a pair + direction -> TranslationRunner's shape ----
    function _normalisePair(pair) {
        const dir = _direction === DIRECTION.MIXED
            ? (Math.random() < 0.5 ? DIRECTION.ES_EN : DIRECTION.EN_ES)
            : _direction;

        return dir === DIRECTION.ES_EN
            ? { prompt: pair.spanish, model: pair.english, promptLabel: Lang.name() }
            : { prompt: pair.english, model: pair.spanish, promptLabel: 'English' };
    }

    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n).map(_normalisePair);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        const totalA1 = _pairs.filter(p => p.level === 'A1').length;
        const totalA2 = _pairs.filter(p => p.level === 'A2').length;
        const totalB1 = _pairs.filter(p => p.level === 'B1').length;
        const topics = _topicsFor(_level);
        // The level select above can leave _topic pointing at a topic that
        // doesn't exist at the newly-chosen level (e.g. picking A1 right
        // after selecting a B1-only topic) — fall back to "All topics"
        // rather than silently filtering to nothing.
        if (_topic !== 'all' && !topics.some(([name]) => name === _topic)) _topic = 'all';

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Translation Driller</h2>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="td-direction">Direction</label>
                    <select id="td-direction" class="vb-select">
                        <option value="${DIRECTION.ES_EN}">${Lang.name()} → English</option>
                        <option value="${DIRECTION.EN_ES}">English → ${Lang.name()}</option>
                        <option value="${DIRECTION.MIXED}">Mixed</option>
                    </select>
                </div>

                <div class="gd-setting">
                    <label for="td-level">Level</label>
                    <select id="td-level" class="vb-select">
                        <option value="all">All levels (${_pairs.length} sentences)</option>
                        <option value="A1">A1 (${totalA1} sentences)</option>
                        <option value="A2">A2 (${totalA2} sentences)</option>
                        <option value="B1">B1 (${totalB1} sentences)</option>
                    </select>
                </div>

                <div class="gd-setting">
                    <label for="td-topic">Topic</label>
                    <select id="td-topic" class="vb-select">
                        <option value="all">All topics</option>
                        ${topics.map(([name, count]) => `
                            <option value="${_esc(name)}">${_esc(name)} (${count})</option>
                        `).join('')}
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="td-count">Number of sentences</label>
                        <select id="td-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} sentences</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="td-timer">Timer</label>
                        <select id="td-timer" class="vb-select">
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

        const directionSelect = _container.querySelector('#td-direction');
        directionSelect.value = _direction;
        directionSelect.addEventListener('change', e => { _direction = e.target.value; });

        const levelSelect = _container.querySelector('#td-level');
        levelSelect.value = _level;
        // Full re-render, not just updating _level, since the topic list
        // below is scoped to whichever level is selected — picking a new
        // level needs to refresh which topics are even offered.
        levelSelect.addEventListener('change', e => { _level = e.target.value; _renderSettings(); });

        const topicSelect = _container.querySelector('#td-topic');
        topicSelect.value = _topic;
        topicSelect.addEventListener('change', e => { _topic = e.target.value; });

        const countSelect = _container.querySelector('#td-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#td-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _poolFor(_level, _topic);
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No sentences found for this level/topic yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-settings">Change settings</button>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            return;
        }

        if (_mode === MODE.COUNT) {
            _queue = _takeN(pool, _questionCount);
        } else {
            _queue = _shuffled(pool).map(_normalisePair);
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
        return _mode === MODE.COUNT ? `${base} · Sentence ${_queueIndex + 1} of ${_queue.length}` : base;
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
        TranslationRunner.render(exerciseRoot, {
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
                        <span class="vspeed-stat-label">Got it</span>
                        <span class="vspeed-stat-value">${_correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Not quite</span>
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
