// ============================================
// SPEAKING DRILLER
// ============================================
// Practice pronunciation and spoken recall out loud using curriculum-aligned
// sentences from translation-index.json.
//
// Features:
// - Read & Repeat (Shadowing) and Prompt & Speak (Oral Production)
// - Real-time speech recognition and automatic accuracy scoring
// - Word-by-word visual breakdown
// - Comparative dual-playback (Model vs User)
// - Supports CEFR level filtering (All, A1, A2, B1...)
// - Count mode (5, 10, 15, 20) and Timed mode (1, 2, 3, 5 min)
// - Results screen with XP award and recommendation engine integration

const SpeakingDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const DRILL_TYPE = { ALL: 'all', READ_REPEAT: 'read-repeat', PROMPT_SPEAK: 'prompt-speak' };
    const COUNT_OPTIONS = [5, 10, 15, 20];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

    let _phase = PHASE.SETTINGS;
    let _container = null;
    let _pairs = null;

    let _mode = MODE.COUNT;
    let _drillType = DRILL_TYPE.ALL;
    let _level = 'all';
    let _questionCount = 10;
    let _timerMinutes = 2;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;
    let _recap = [];

    let _timerInterval = null;
    let _endTime = 0;
    let _timeRemaining = 0;

    function _esc(text) {
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

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    let _loadedLang = null;

    // ---- Load Pairs ----
    async function _load() {
        if (_pairs && _loadedLang === Lang.code()) return;
        const index = await Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] }));
        _pairs = (index.pairs || []).filter(p => p.spanish && p.english);
        _loadedLang = Lang.code();
    }

    document.addEventListener('language-changed', () => {
        _pairs = null;
        _loadedLang = null;
    });

    function _poolFor(level) {
        if (!level || level === 'all') return _pairs;
        const target = level.toUpperCase();
        const filtered = _pairs.filter(p => p.level && p.level.toUpperCase() === target);
        return filtered.length ? filtered : _pairs;
    }

    function _availableLevels() {
        if (!_pairs) return [];
        const seen = new Set();
        for (const p of _pairs) {
            if (p.level) seen.add(p.level.toUpperCase());
        }
        return CEFR_ORDER.filter(lvl => seen.has(lvl));
    }

    // ---- Build Queue ----
    function _buildQueue() {
        const pool = _poolFor(_level);
        const shuffled = _shuffled(pool);
        const count = _mode === MODE.COUNT ? _questionCount : 40;
        const selected = shuffled.slice(0, count);

        _queue = selected.map((pair, idx) => {
            let kind = _drillType;
            if (kind === DRILL_TYPE.ALL) {
                // Alternate between Read & Repeat and Prompt & Speak
                kind = (idx % 2 === 0) ? DRILL_TYPE.READ_REPEAT : DRILL_TYPE.PROMPT_SPEAK;
            }
            return {
                kind,
                spanish: pair.spanish,
                english: pair.english,
                level: pair.level,
                topic: pair.topic
            };
        });

        _queueIndex = 0;
        _seen = 0;
        _correct = 0;
        _recap = [];
    }

    // ---- Timer Handling ----
    function _startTimer() {
        _stopTimer();
        _timeRemaining = _timerMinutes * 60;
        _endTime = Date.now() + (_timeRemaining * 1000);

        _timerInterval = setInterval(() => {
            const left = Math.max(0, Math.round((_endTime - Date.now()) / 1000));
            _timeRemaining = left;
            const display = _container.querySelector('.sp-timer-display');
            if (display) display.textContent = _formatTime(left);

            if (left <= 0) {
                _stopTimer();
                _finishSession();
            }
        }, 1000);
    }

    function _stopTimer() {
        if (_timerInterval) {
            clearInterval(_timerInterval);
            _timerInterval = null;
        }
    }

    function stop() {
        _stopTimer();
        if (typeof SpeechInput !== 'undefined') {
            SpeechInput.stopListening();
        }
    }

    // ---- Session Lifecycle ----
    function _startSession() {
        _buildQueue();
        _phase = PHASE.SESSION;
        _renderSession();
        if (_mode === MODE.TIMED) {
            _startTimer();
        }
    }

    function _nextItem() {
        _queueIndex++;
        if (_mode === MODE.COUNT && _queueIndex >= _queue.length) {
            _finishSession();
            return;
        }
        if (_mode === MODE.TIMED && _queueIndex >= _queue.length) {
            // Refill queue if running out of items in timed mode
            _buildQueue();
        }
        _renderSessionItem();
    }

    function _finishSession() {
        _stopTimer();
        _phase = PHASE.RESULTS;

        // Award XP
        const earnedXP = _correct * 3;
        if (earnedXP > 0 && typeof XP !== 'undefined' && typeof XP.award === 'function') {
            XP.award(earnedXP, 'speaking-driller');
        }

        // Record accuracy into DrillHistory
        if (typeof DrillHistory !== 'undefined' && _seen > 0) {
            DrillHistory.record('speaking', { correct: _correct, wrong: _seen - _correct });
        }

        _renderResults();
    }

    // ---- UI: Settings Screen ----
    function _renderSettings() {
        const levels = _availableLevels();

        _container.innerHTML = `
            <div class="sp-settings">
                <h2 class="gd-title">Speaking Driller</h2>
                <p class="gd-hint">Practise pronunciation and speak ${(typeof Lang !== 'undefined') ? Lang.name() : 'the language'} out loud.</p>

                <div class="wk-config-group">
                    <label class="wk-config-label">Level</label>
                    <div class="wk-pill-row">
                        <button type="button" class="wk-pill ${(_level === 'all' ? 'active' : '')}" data-level="all">All</button>
                        ${levels.map(lvl => `
                            <button type="button" class="wk-pill ${(_level === lvl ? 'active' : '')}" data-level="${lvl}">${lvl}</button>
                        `).join('')}
                    </div>
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label">Practice Style</label>
                    <div class="wk-pill-row">
                        <button type="button" class="wk-pill ${(_drillType === DRILL_TYPE.ALL ? 'active' : '')}" data-type="all">Mixed</button>
                        <button type="button" class="wk-pill ${(_drillType === DRILL_TYPE.READ_REPEAT ? 'active' : '')}" data-type="read-repeat">Read & Repeat</button>
                        <button type="button" class="wk-pill ${(_drillType === DRILL_TYPE.PROMPT_SPEAK ? 'active' : '')}" data-type="prompt-speak">Prompt & Speak</button>
                    </div>
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label">Session Mode</label>
                    <div class="wk-pill-row">
                        <button type="button" class="wk-pill ${(_mode === MODE.COUNT ? 'active' : '')}" data-mode="count">Questions</button>
                        <button type="button" class="wk-pill ${(_mode === MODE.TIMED ? 'active' : '')}" data-mode="timed">Timed</button>
                    </div>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="wk-config-group">
                        <label class="wk-config-label">Number of Sentences</label>
                        <div class="wk-pill-row">
                            ${COUNT_OPTIONS.map(cnt => `
                                <button type="button" class="wk-pill ${(_questionCount === cnt ? 'active' : '')}" data-count="${cnt}">${cnt}</button>
                            `).join('')}
                        </div>
                    </div>
                ` : `
                    <div class="wk-config-group">
                        <label class="wk-config-label">Time</label>
                        <div class="wk-pill-row">
                            ${TIMER_PRESETS.map(mins => `
                                <button type="button" class="wk-pill ${(_timerMinutes === mins ? 'active' : '')}" data-minutes="${mins}">${mins} min</button>
                            `).join('')}
                        </div>
                    </div>
                `}

                <div class="sp-settings-start">
                    <button type="button" class="sp-start-btn" data-action="start-session">
                        Start Speaking Practice
                    </button>
                </div>
            </div>
        `;

        _attachSettingsEvents();
    }

    function _attachSettingsEvents() {
        _container.querySelectorAll('[data-level]').forEach(btn => {
            btn.addEventListener('click', () => {
                _level = btn.getAttribute('data-level');
                _renderSettings();
            });
        });

        _container.querySelectorAll('[data-type]').forEach(btn => {
            btn.addEventListener('click', () => {
                _drillType = btn.getAttribute('data-type');
                _renderSettings();
            });
        });

        _container.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => {
                _mode = btn.getAttribute('data-mode');
                _renderSettings();
            });
        });

        _container.querySelectorAll('[data-count]').forEach(btn => {
            btn.addEventListener('click', () => {
                _questionCount = parseInt(btn.getAttribute('data-count'), 10);
                _renderSettings();
            });
        });

        _container.querySelectorAll('[data-minutes]').forEach(btn => {
            btn.addEventListener('click', () => {
                _timerMinutes = parseInt(btn.getAttribute('data-minutes'), 10);
                _renderSettings();
            });
        });

        const startBtn = _container.querySelector('[data-action="start-session"]');
        if (startBtn) {
            startBtn.addEventListener('click', _startSession);
        }
    }

    // ---- UI: Session Screen ----
    function _renderSession() {
        _container.innerHTML = `
            <div class="sp-session-shell">
                <div class="sp-session-header">
                    <div class="sp-session-progress">
                        ${_mode === MODE.COUNT
                            ? `<span class="sp-progress-text">Sentence ${_queueIndex + 1} of ${_queue.length}</span>`
                            : `<span class="sp-timer-display">${_formatTime(_timerMinutes * 60)}</span>`
                        }
                    </div>
                    <button type="button" class="sp-session-quit" data-action="quit-session" aria-label="End session">End Session</button>
                </div>

                <div id="sp-runner-mount"></div>
            </div>
        `;

        const quitBtn = _container.querySelector('[data-action="quit-session"]');
        if (quitBtn) {
            quitBtn.addEventListener('click', () => {
                _finishSession();
            });
        }

        _renderSessionItem();
    }

    function _renderSessionItem() {
        const mount = document.getElementById('sp-runner-mount');
        if (!mount) return;

        const current = _queue[_queueIndex];
        if (!current) {
            _finishSession();
            return;
        }

        // Update progress count
        const progressEl = _container.querySelector('.sp-progress-text');
        if (progressEl && _mode === MODE.COUNT) {
            progressEl.textContent = `Sentence ${_queueIndex + 1} of ${_queue.length}`;
        }

        SpeakingRunner.render(mount, current, {
            onResult: isCorrect => {
                _seen++;
                if (isCorrect) _correct++;
                _recap.push({
                    spanish: current.spanish,
                    english: current.english,
                    isCorrect
                });
            },
            onNext: () => {
                _nextItem();
            }
        });
    }

    // ---- UI: Results Screen ----
    function _renderResults() {
        const accuracy = _seen > 0 ? Math.round((_correct / _seen) * 100) : 0;
        const earnedXP = _correct * 3;

        _container.innerHTML = `
            <div class="sp-results">
                <div class="sp-results-hero">
                    <div class="sp-results-score">${accuracy}%</div>
                    <p class="sp-results-lead">${_correct} of ${_seen} sentences pronounced clearly</p>
                    ${earnedXP > 0 ? `<p class="sp-results-xp">+${earnedXP} XP earned</p>` : ''}
                </div>

                <div class="sp-recap-list">
                    <h4 class="sp-recap-title">Session Review</h4>
                    ${_recap.map(item => `
                        <div class="sp-recap-row ${item.isCorrect ? 'sp-recap-ok' : 'sp-recap-miss'}">
                            <span class="sp-recap-indicator">${item.isCorrect ? '✓' : '✗'}</span>
                            <div class="sp-recap-content">
                                <span class="sp-recap-es">${_esc(item.spanish)}</span>
                                <span class="sp-recap-en">${_esc(item.english)}</span>
                            </div>
                        </div>
                    `).join('')}
                </div>

                <div class="sp-results-actions">
                    <button type="button" class="sp-start-btn" data-action="practice-again">
                        Practice Again
                    </button>
                </div>

                <div class="wk-next-action-slot" id="sp-next-action-slot"></div>
            </div>
        `;

        const retryBtn = _container.querySelector('[data-action="practice-again"]');
        if (retryBtn) {
            retryBtn.addEventListener('click', () => {
                _phase = PHASE.SETTINGS;
                _renderSettings();
            });
        }

        // Mount recommendation engine next action
        if (typeof RecommendationEngine !== 'undefined' && typeof RecommendationEngine.mountNextAction === 'function') {
            const slot = document.getElementById('sp-next-action-slot');
            if (slot) {
                RecommendationEngine.mountNextAction(slot, { excludeDrillerId: 'speaking' });
            }
        }
    }

    // ---- Main Driller Mount ----
    async function render(container, options = {}) {
        _container = container;
        await _load();

        if (options && options.level) {
            _level = options.level;
        }
        if (options && options.count) {
            _questionCount = options.count;
            _mode = MODE.COUNT;
        }

        if (options && options.autoStart) {
            _phase = PHASE.SESSION;
            _startSession();
            return;
        }

        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    return {
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.SpeakingDriller = SpeakingDriller;
}

