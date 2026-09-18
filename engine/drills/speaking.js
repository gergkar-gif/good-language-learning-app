// ============================================
// SPEAKING STUDIO
// ============================================
// Complete oral practice hub for Parlour:
//
// 1. Sentence Drills:
//    - Read & Repeat (Shadowing) and Prompt & Speak (Oral Production)
//    - Real-time speech recognition and automatic accuracy scoring
//    - Word-by-word visual breakdown
//    - Comparative dual-playback (Model vs User)
//    - CEFR filtering, count mode (5, 10, 15, 20) and timed mode (1, 2, 3, 5 min)
//
// 2. Verbal Production (5-minute open oral studio):
//    - Longer-form spoken production on CEFR-aligned topics (or free speaking)
//    - Live microphone capture (up to 5 minutes) with audio level visualizer
//    - Real-time speech-to-text transcript streaming
//    - User voice playback ("Listen to your own voice")
//    - Transcript review & edit before submission
//    - AI Formative evaluation via GraderEngine (fluency, coherence, vocabulary, grammar)
//    - Oral evidence ingestion into LearnerModel with modality: 'oral'

const SpeakingDriller = (function () {
    'use strict';

    // ---- Studio Modes ----
    const STUDIO_TAB = { DRILLS: 'drills', PRODUCTION: 'production' };
    let _activeStudioTab = STUDIO_TAB.DRILLS;
    let _container = null;

    // ---- Sentence Drills State ----
    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const DRILL_TYPE = { ALL: 'all', READ_REPEAT: 'read-repeat', PROMPT_SPEAK: 'prompt-speak' };
    const COUNT_OPTIONS = [5, 10, 15, 20];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

    let _phase = PHASE.SETTINGS;
    let _pairs = null;
    let _mode = MODE.COUNT;
    let _drillType = DRILL_TYPE.ALL;
    let _level = 'all';
    let _questionCount = 10;
    let _timerMinutes = 2;
    let _skill = null;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;
    let _recap = [];

    let _timerInterval = null;
    let _endTime = 0;
    let _timeRemaining = 0;
    let _loadedLang = null;

    // ---- Verbal Production State ----
    const PROD_PHASE = { PROMPT_SELECT: 1, RECORDING: 2, REVIEW: 3, ASSESSING: 4, RESULTS: 5, CUSTOM_TASK: 6 };
    const CUSTOM_TIME_OPTIONS = [1, 2, 3, 5]; // minutes
    // Below this cap a task is graded task-completion-primary and shown the
    // one-line coaching result instead of the full CEFR dimensions/errors
    // breakdown (see isShortProd in _renderProdResults) -- can-do checks
    // ("say and ask the date") are bounded asks, not open-ended fluency
    // topics, so they're scored and reported that way.
    const SHORT_TASK_MAX_SECONDS = 60;
    let _prodPhase = PROD_PHASE.PROMPT_SELECT;
    let _prodPrompts = null;
    let _prodLoadedLang = null;
    let _selectedProdPrompt = null;
    // Recording ceiling in seconds -- 300 (5 min) for every curated topic
    // and Free Speaking; can-do/competency prompts default to
    // SHORT_TASK_MAX_SECONDS instead, and the custom-task screen below
    // overrides it to the learner's chosen limit.
    let _prodMaxSeconds = 300;
    let _customTaskMinutes = CUSTOM_TIME_OPTIONS[1];
    // 'all' or a CEFR code -- see the identical field in WritingDriller for
    // why this filters the topic cards rather than converting them to bare
    // pills at today's low prompt count.
    let _prodLevelFilter = 'all';
    let _prodTranscript = '';
    let _prodAudioUrl = null;
    let _prodElapsedSeconds = 0;
    let _prodTimerInterval = null;
    let _prodAssessmentResult = null;
    let _onExit = null;

    function _esc(text) {
        if (typeof UI !== 'undefined' && UI.escape) return UI.escape(text);
        const d = document.createElement('div');
        d.textContent = String(text == null ? '' : text);
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

    // ============================================
    // DATA LOADING
    // ============================================

    async function _load() {
        if (_pairs && _loadedLang === Lang.code()) return;
        const index = await Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] }));
        _pairs = (index.pairs || []).filter(p => p.spanish && p.english);
        _loadedLang = Lang.code();
    }

    async function _loadProdPrompts() {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        if (_prodPrompts && _prodLoadedLang === lang) return;
        try {
            const data = await Content.json(Lang.content('speaking-prompts.json'));
            _prodPrompts = (data && data.prompts) ? data.prompts : [];
            _prodLoadedLang = lang;
        } catch (e) {
            _prodPrompts = [];
        }
    }

    document.addEventListener('language-changed', () => {
        _pairs = null;
        _loadedLang = null;
        _prodPrompts = null;
        _prodLoadedLang = null;
    });

    // ============================================
    // TOP-LEVEL STUDIO SHELL & SWITCHER
    // ============================================

    function _renderStudioShell() {
        if (!_container) return;

        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        _container.innerHTML = `
            <div class="sp-studio-wrap">
                <div class="sp-studio-nav" role="tablist">
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.DRILLS ? 'active' : ''}" data-studio-tab="drills" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.DRILLS}">
                        Sentence Drills
                    </button>
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.PRODUCTION ? 'active' : ''}" data-studio-tab="production" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.PRODUCTION}">
                        Verbal Production (${_prodMaxSeconds < 60 ? _prodMaxSeconds + 's' : Math.round(_prodMaxSeconds / 60) + ' min'})
                    </button>
                </div>
                <div class="sp-studio-body" id="sp-studio-body"></div>
            </div>
        `;

        _container.querySelectorAll('[data-studio-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-studio-tab');
                if (target === _activeStudioTab) return;
                stop();
                _activeStudioTab = target;
                _renderStudioShell();
            });
        });

        _renderActiveTab();
    }

    function _renderActiveTab() {
        const body = document.getElementById('sp-studio-body');
        if (!body) return;

        if (_activeStudioTab === STUDIO_TAB.DRILLS) {
            if (_phase === PHASE.SETTINGS) _renderSettings(body);
            else if (_phase === PHASE.SESSION) _renderSession(body);
            else if (_phase === PHASE.RESULTS) _renderResults(body);
        } else {
            if (_prodPhase === PROD_PHASE.PROMPT_SELECT) _renderProdPromptSelect(body);
            else if (_prodPhase === PROD_PHASE.CUSTOM_TASK) _renderProdCustomTask(body);
            else if (_prodPhase === PROD_PHASE.RECORDING) _renderProdRecording(body);
            else if (_prodPhase === PROD_PHASE.REVIEW) _renderProdReview(body);
            else if (_prodPhase === PROD_PHASE.ASSESSING) _renderProdAssessing(body);
            else if (_prodPhase === PROD_PHASE.RESULTS) _renderProdResults(body);
        }
    }

    // ============================================
    // PART 1: SENTENCE DRILLS IMPLEMENTATION
    // ============================================

    function _poolFor(level, skill) {
        let pool = _pairs || [];
        if (skill) {
            const skillFiltered = pool.filter(p => p.skillIds && p.skillIds.includes(skill));
            if (skillFiltered.length) pool = skillFiltered;
        }
        if (!level || level === 'all') return pool;
        const target = level.toUpperCase();
        const filtered = pool.filter(p => p.level && p.level.toUpperCase() === target);
        return filtered.length ? filtered : pool;
    }

    function _availableLevels() {
        if (!_pairs) return [];
        const seen = new Set();
        for (const p of _pairs) {
            if (p.level) seen.add(p.level.toUpperCase());
        }
        return CEFR_ORDER.filter(lvl => seen.has(lvl));
    }

    function _buildQueue() {
        const pool = _poolFor(_level, _skill);
        const shuffled = _shuffled(pool);
        const count = _mode === MODE.COUNT ? _questionCount : 40;
        const selected = shuffled.slice(0, count);

        _queue = selected.map((pair, idx) => {
            let kind = _drillType;
            if (kind === DRILL_TYPE.ALL) {
                kind = (idx % 2 === 0) ? DRILL_TYPE.READ_REPEAT : DRILL_TYPE.PROMPT_SPEAK;
            }
            return {
                id: pair.id,
                kind,
                spanish: pair.spanish,
                english: pair.english,
                level: pair.level,
                topic: pair.topic,
                skillIds: pair.skillIds
            };
        });

        _queueIndex = 0;
        _seen = 0;
        _correct = 0;
        _recap = [];
    }

    function _startTimer() {
        _stopTimer();
        _timeRemaining = _timerMinutes * 60;
        _endTime = Date.now() + (_timeRemaining * 1000);

        _timerInterval = setInterval(() => {
            const left = Math.max(0, Math.round((_endTime - Date.now()) / 1000));
            _timeRemaining = left;
            const display = document.querySelector('.sp-timer-display');
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

    function _startSession() {
        _buildQueue();
        _phase = PHASE.SESSION;
        _renderActiveTab();
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
            _buildQueue();
        }
        _renderSessionItem();
    }

    function _finishSession() {
        _stopTimer();
        _phase = PHASE.RESULTS;

        const earnedXP = _correct * 3;
        if (earnedXP > 0 && typeof XP !== 'undefined' && typeof XP.award === 'function') {
            XP.award(earnedXP, 'speaking-driller');
        }

        if (typeof DrillHistory !== 'undefined' && _seen > 0) {
            DrillHistory.record('speaking', { correct: _correct, wrong: _seen - _correct });
        }

        _renderActiveTab();
    }

    function _renderSettings(body) {
        const levels = _availableLevels();
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        body.innerHTML = `
            <div class="sp-settings">
                <h2 class="gd-title">Sentence Speaking Drills</h2>
                <p class="gd-hint">Practise pronunciation, shadowing, and spoken recall in ${langName}.</p>

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

        _attachSettingsEvents(body);
    }

    function _attachSettingsEvents(body) {
        body.querySelectorAll('[data-level]').forEach(btn => {
            btn.addEventListener('click', () => {
                _level = btn.getAttribute('data-level');
                _renderSettings(body);
            });
        });

        body.querySelectorAll('[data-type]').forEach(btn => {
            btn.addEventListener('click', () => {
                _drillType = btn.getAttribute('data-type');
                _renderSettings(body);
            });
        });

        body.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => {
                _mode = btn.getAttribute('data-mode');
                _renderSettings(body);
            });
        });

        body.querySelectorAll('[data-count]').forEach(btn => {
            btn.addEventListener('click', () => {
                _questionCount = parseInt(btn.getAttribute('data-count'), 10);
                _renderSettings(body);
            });
        });

        body.querySelectorAll('[data-minutes]').forEach(btn => {
            btn.addEventListener('click', () => {
                _timerMinutes = parseInt(btn.getAttribute('data-minutes'), 10);
                _renderSettings(body);
            });
        });

        const startBtn = body.querySelector('[data-action="start-session"]');
        if (startBtn) {
            startBtn.addEventListener('click', _startSession);
        }
    }

    function _renderSession(body) {
        body.innerHTML = `
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

        const quitBtn = body.querySelector('[data-action="quit-session"]');
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

        const progressEl = document.querySelector('.sp-progress-text');
        if (progressEl && _mode === MODE.COUNT) {
            progressEl.textContent = `Sentence ${_queueIndex + 1} of ${_queue.length}`;
        }

        SpeakingRunner.render(mount, current, {
            onResult: (isCorrect, evalResult) => {
                _seen++;
                if (isCorrect) _correct++;
                _recap.push({
                    spanish: current.spanish,
                    english: current.english,
                    isCorrect
                });
                if (!evalResult || !evalResult.isSnoozed) {
                    if (current.skillIds && typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
                        const acc = (evalResult && typeof evalResult.accuracy === 'number') ? evalResult.accuracy : (isCorrect ? 100 : 0);
                        LearnerModel.recordProduction(current.skillIds, isCorrect, acc, 'oral');
                    }
                }
            },
            onNext: () => {
                _nextItem();
            }
        });
    }

    function _renderResults(body) {
        const accuracy = _seen > 0 ? Math.round((_correct / _seen) * 100) : 0;
        const earnedXP = _correct * 3;

        body.innerHTML = `
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

        const retryBtn = body.querySelector('[data-action="practice-again"]');
        if (retryBtn) {
            retryBtn.addEventListener('click', () => {
                _phase = PHASE.SETTINGS;
                _renderActiveTab();
            });
        }

        if (typeof RecommendationEngine !== 'undefined' && typeof RecommendationEngine.mountNextAction === 'function') {
            const slot = document.getElementById('sp-next-action-slot');
            if (slot) {
                RecommendationEngine.mountNextAction(slot, { excludeDrillerId: 'speaking' });
            }
        }
    }

    // ============================================
    // PART 2: VERBAL PRODUCTION (5-MINUTE EXTENDED ORAL STUDIO)
    // ============================================

    async function _renderProdPromptSelect(body) {
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';
        const prompts = _prodPrompts || [];

        let unverifiedList = [];
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.unverifiedCompetencies === 'function') {
            try {
                unverifiedList = await LearnerModel.unverifiedCompetencies();
            } catch (e) { unverifiedList = []; }
        }

        const availableLevels = Array.from(new Set(prompts.map(p => p.cefrLevel || 'B1')))
            .sort((a, b) => CEFR_ORDER.indexOf(a) - CEFR_ORDER.indexOf(b));
        const filteredPrompts = _prodLevelFilter === 'all'
            ? prompts
            : prompts.filter(p => (p.cefrLevel || 'B1') === _prodLevelFilter);

        const levelFilterHtml = availableLevels.length > 1 ? `
            <div class="wk-config-group">
                <label class="wk-config-label">Level</label>
                <div class="wk-pill-row">
                    <button type="button" class="wk-pill ${_prodLevelFilter === 'all' ? 'active' : ''}" data-prod-level-filter="all">All</button>
                    ${availableLevels.map(lvl => `
                        <button type="button" class="wk-pill ${_prodLevelFilter === lvl ? 'active' : ''}" data-prod-level-filter="${_esc(lvl)}">${_esc(lvl)}</button>
                    `).join('')}
                </div>
            </div>
        ` : '';

        let promptsHtml = '';
        if (filteredPrompts.length > 0) {
            promptsHtml = filteredPrompts.map(p => {
                const timeLabel = p.minSeconds
                    ? `Spoken · ~${Math.round(p.minSeconds / 60)}-${Math.round(p.maxSeconds / 60)} min`
                    : 'Spoken · ~1-3 min';
                return `
                <div class="wk-card sp-card-clickable" data-select-prod-prompt="${_esc(p.id)}">
                    <div class="sp-prompt-card-head">
                        <span class="sp-level-pill">${_esc(p.cefrLevel || 'B1')}</span>
                        <span class="sp-words-target">${timeLabel}</span>
                    </div>
                    <h3 class="wk-card-title">${_esc(p.title)}</h3>
                    <p class="wk-card-sub">${_esc(p.prompt.slice(0, 115))}...</p>
                </div>
            `;
            }).join('');
        }

        body.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Verbal Production Studio</h2>
                    <p class="sp-setup-sub">Speak freely or pick a topic. Record up to 5 minutes out loud, listen to your own voice, and receive CEFR-aligned formative feedback.</p>
                </div>

                ${unverifiedList.length > 0 ? `
                    <div class="sp-unverified-section" style="margin-bottom: 24px;">
                        <h3 class="sp-section-heading" style="margin-bottom: 12px; font-size: 15px; color: var(--accent-dark);">
                            Target Unverified Goals (${unverifiedList.length})
                        </h3>
                        <div class="sp-prompt-grid">
                            ${unverifiedList.slice(0, 3).map(c => `
                                <div class="wk-card sp-card-clickable sp-card-competency" data-select-prod-comp="${_esc(c.text)}">
                                    <div class="sp-prompt-card-head">
                                        <span class="sp-level-pill">${_esc(c.level || 'A1')}</span>
                                        <span class="sp-words-target">Can-Do Goal</span>
                                    </div>
                                    <h3 class="wk-card-title">${_esc(c.text)}</h3>
                                    <p class="wk-card-sub">${_esc(c.reason || 'Record 1-2 minutes demonstrating this ability out loud.')}</p>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${levelFilterHtml}

                <div class="sp-prompt-grid">
                    <div class="wk-card sp-card-clickable sp-card-custom" data-select-prod-custom="1">
                        <div class="sp-prompt-card-head">
                            <span class="sp-level-pill">Free Topic</span>
                            <span class="sp-words-target">Max 5 min</span>
                        </div>
                        <h3 class="wk-card-title">Free Speaking</h3>
                        <p class="wk-card-sub">Speak freely about your day, opinions, or any topic of choice in ${langName}.</p>
                    </div>
                    ${promptsHtml}
                </div>
            </div>
        `;

        body.querySelectorAll('[data-prod-level-filter]').forEach(el => {
            el.addEventListener('click', () => {
                _prodLevelFilter = el.getAttribute('data-prod-level-filter');
                _renderActiveTab();
            });
        });

        body.querySelectorAll('[data-select-prod-comp]').forEach(el => {
            el.addEventListener('click', () => {
                const text = el.getAttribute('data-select-prod-comp');
                const found = unverifiedList.find(c => c.text === text);
                const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';
                const langCode = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
                const formatted = (typeof CanDoPrompt !== 'undefined')
                    ? CanDoPrompt.formatPrompt(text, {
                        language: langName,
                        langCode: langCode,
                        modality: 'oral',
                        level: (found && found.level) || 'A1'
                    })
                    : null;
                _selectedProdPrompt = {
                    id: 'comp_' + Date.now(),
                    title: formatted ? formatted.title : (text.length > 35 ? text.slice(0, 32) + '...' : text),
                    scenario: formatted ? formatted.scenario : '',
                    cefrLevel: (found && found.level) || 'A1',
                    prompt: formatted ? formatted.prompt : `Demonstrate this ability out loud: "${text}". Speak clearly and naturally — however much the task itself calls for.`,
                    cues: formatted ? formatted.cues : [],
                    targetCompetency: text,
                    taskCompletionPrimary: true
                };
                _prodMaxSeconds = SHORT_TASK_MAX_SECONDS;
                _startProdRecording();
            });
        });

        body.querySelectorAll('[data-select-prod-prompt]').forEach(el => {
            el.addEventListener('click', () => {
                const pid = el.getAttribute('data-select-prod-prompt');
                _selectedProdPrompt = prompts.find(p => p.id === pid) || null;
                _prodMaxSeconds = (_selectedProdPrompt && _selectedProdPrompt.maxSeconds) || 300;
                _startProdRecording();
            });
        });

        const customBtn = body.querySelector('[data-select-prod-custom]');
        if (customBtn) {
            customBtn.addEventListener('click', () => {
                _prodPhase = PROD_PHASE.CUSTOM_TASK;
                _renderActiveTab();
            });
        }
    }

    // Same idea as WritingDriller's _renderCustomTask(): a learner-authored
    // task plus an explicit time limit, in front of the same
    // _startProdRecording()/GraderEngine.grade() pipeline every other
    // prompt already uses.
    function _renderProdCustomTask(body) {
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        body.innerHTML = `
            <div class="sp-driller-wrap">
                <button type="button" class="sp-btn-link" data-action="back-prompts">← Back</button>
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Set Your Own Task</h2>
                    <p class="sp-setup-sub">Describe what you want to talk about, and for how long. You'll be graded against exactly this.</p>
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label" for="sp-custom-task-input">Task</label>
                    <input type="text" id="sp-custom-task-input" class="review-input" style="width:100%;"
                        placeholder="e.g. Describe your hobbies" maxlength="200">
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label">Time Limit</label>
                    <div class="wk-pill-row">
                        ${CUSTOM_TIME_OPTIONS.map(mins => `
                            <button type="button" class="wk-pill ${_customTaskMinutes === mins ? 'active' : ''}" data-custom-minutes="${mins}">${mins} min</button>
                        `).join('')}
                    </div>
                </div>

                <div class="sp-settings-start">
                    <button type="button" class="sp-start-btn" data-action="start-custom-task" disabled>
                        Start Speaking
                    </button>
                </div>
            </div>
        `;

        const backBtn = body.querySelector('[data-action="back-prompts"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                _prodPhase = PROD_PHASE.PROMPT_SELECT;
                _renderActiveTab();
            });
        }

        const input = body.querySelector('#sp-custom-task-input');
        const startBtn = body.querySelector('[data-action="start-custom-task"]');
        input.addEventListener('input', () => {
            startBtn.disabled = !input.value.trim();
        });
        input.focus();

        body.querySelectorAll('[data-custom-minutes]').forEach(el => {
            el.addEventListener('click', () => {
                _customTaskMinutes = Number(el.getAttribute('data-custom-minutes'));
                body.querySelectorAll('[data-custom-minutes]').forEach(p => p.classList.toggle('active', Number(p.getAttribute('data-custom-minutes')) === _customTaskMinutes));
            });
        });

        startBtn.addEventListener('click', () => {
            const task = input.value.trim();
            if (!task) return;
            _selectedProdPrompt = {
                id: 'custom-task-' + Date.now(),
                title: task.length > 40 ? task.slice(0, 37) + '...' : task,
                cefrLevel: 'B1',
                prompt: `${task} (speak in ${langName})`,
                targetSkills: ['extended_speech', 'fluency', 'communicative_effectiveness']
            };
            _prodMaxSeconds = _customTaskMinutes * 60;
            _startProdRecording();
        });
    }

    function _startProdRecording() {
        _prodTranscript = '';
        _prodAudioUrl = null;
        _prodElapsedSeconds = 0;
        _prodPhase = PROD_PHASE.RECORDING;
        _renderActiveTab();

        if (_prodTimerInterval) clearInterval(_prodTimerInterval);
        _prodTimerInterval = setInterval(() => {
            _prodElapsedSeconds++;
            const timerEl = document.querySelector('.sp-prod-timer-text');
            const fillEl = document.querySelector('.sp-prod-timer-fill');
            if (timerEl) {
                timerEl.textContent = `${_formatTime(_prodElapsedSeconds)} / ${_formatTime(_prodMaxSeconds)}`;
            }
            if (fillEl) {
                const pct = Math.min(100, (_prodElapsedSeconds / _prodMaxSeconds) * 100);
                fillEl.style.width = pct + '%';
            }
            if (_prodElapsedSeconds >= _prodMaxSeconds) {
                _finishProdRecording();
            }
        }, 1000);

        if (typeof SpeechInput !== 'undefined') {
            SpeechInput.startListening({
                manualStop: true,
                maxDurationMs: _prodMaxSeconds * 1000,
                onInterim: (text) => {
                    _prodTranscript = text;
                    const wordCountEl = document.querySelector('.sp-prod-word-count');
                    if (wordCountEl) {
                        const words = text.trim() ? text.trim().split(/\s+/).length : 0;
                        wordCountEl.textContent = `${words} words captured`;
                    }
                },
                onFinal: (text) => {
                    if (text) _prodTranscript = text;
                    const wordCountEl = document.querySelector('.sp-prod-word-count');
                    if (wordCountEl) {
                        const words = _prodTranscript.trim() ? _prodTranscript.trim().split(/\s+/).length : 0;
                        wordCountEl.textContent = `${words} words captured`;
                    }
                },
                onAudioReady: (audioUrl) => {
                    _prodAudioUrl = audioUrl;
                },
                onAudioLevel: (level) => {
                    const ring = document.querySelector('.sp-mic-pulse-ring');
                    if (ring) {
                        const scale = 1 + (level * 0.45);
                        ring.style.transform = `scale(${scale.toFixed(2)})`;
                        ring.style.opacity = Math.min(1, 0.4 + level).toFixed(2);
                    }
                },
                onError: (err) => {
                    console.warn('SpeechInput oral error:', err);
                }
            });
        }
    }

    function _finishProdRecording() {
        if (_prodTimerInterval) {
            clearInterval(_prodTimerInterval);
            _prodTimerInterval = null;
        }
        if (typeof SpeechInput !== 'undefined') {
            SpeechInput.stopListening();
            _prodAudioUrl = SpeechInput.getRecordedAudioUrl();
        }
        _prodPhase = PROD_PHASE.REVIEW;
        _renderActiveTab();
    }

    function _renderProdRecording(body) {
        const p = _selectedProdPrompt || {};
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        body.innerHTML = `
            <div class="sp-driller-wrap sp-prod-recording-wrap">
                <div class="sp-prod-header">
                    <button type="button" class="sp-btn-link" data-action="back-prompts">← Choose another topic</button>
                    <div class="sp-prod-timer-box">
                        <div class="sp-prod-timer-bar"><div class="sp-prod-timer-fill" style="width: 0%"></div></div>
                        <span class="sp-prod-timer-text">00:00 / ${_formatTime(_prodMaxSeconds)}</span>
                    </div>
                </div>

                <div class="sp-prod-prompt-banner">
                    <span class="sp-level-pill">${_esc(p.cefrLevel || 'B1')}</span>
                    <h3 class="sp-prod-prompt-title">${_esc(p.title || 'Verbal Production')}</h3>
                    ${p.scenario ? `<p class="sp-prod-prompt-scenario" style="margin: 4px 0 8px 0; font-size: 0.9rem; color: var(--text-muted); font-style: italic;">${_esc(p.scenario)}</p>` : ''}
                    <p class="sp-prod-prompt-desc">${_esc(p.prompt || '')}</p>
                    ${p.cues && p.cues.length ? `
                        <div class="sp-prod-prompt-cues" style="margin-top: 10px; padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 6px; text-align: left;">
                            <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); letter-spacing: 0.04em; display: block; margin-bottom: 2px;">Points to include:</span>
                            <ul style="margin: 2px 0 0 0; padding-left: 18px; font-size: 0.88rem; color: var(--text);">
                                ${p.cues.map(c => `<li style="margin-bottom: 2px;">${_esc(c)}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>

                <div class="sp-prod-stage">
                    <div class="sp-mic-pulse-container">
                        <div class="sp-mic-pulse-ring"></div>
                        <div class="sp-mic-pulse-center">
                            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                        </div>
                    </div>
                    <div class="sp-prod-status-line">
                        <span class="sp-recording-dot"></span>
                        <span>Recording live... Speak naturally in ${langName}</span>
                    </div>
                    <span class="sp-prod-word-count">0 words captured</span>
                </div>

                <div class="sp-prod-quiet-hint">
                    Transcribing your speech in the background — you can review and edit your words after speaking.
                </div>

                <div class="sp-prod-actions">
                    <button type="button" class="vbtn vbtn-primary sp-finish-btn" data-action="finish-recording">
                        Finish Speaking & Review
                    </button>
                    <button type="button" class="vbtn vbtn-secondary" data-action="restart-recording">
                        Restart
                    </button>
                </div>
            </div>
        `;

        const backBtn = body.querySelector('[data-action="back-prompts"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                stop();
                _prodPhase = PROD_PHASE.PROMPT_SELECT;
                _renderActiveTab();
            });
        }

        const finishBtn = body.querySelector('[data-action="finish-recording"]');
        if (finishBtn) {
            finishBtn.addEventListener('click', _finishProdRecording);
        }

        const restartBtn = body.querySelector('[data-action="restart-recording"]');
        if (restartBtn) {
            restartBtn.addEventListener('click', () => {
                stop();
                _startProdRecording();
            });
        }
    }

    function _renderProdReview(body) {
        const p = _selectedProdPrompt || {};
        const audioUrl = _prodAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);
        const words = _prodTranscript.trim() ? _prodTranscript.trim().split(/\s+/).length : 0;
        const durationStr = _formatTime(_prodElapsedSeconds);

        // On some Android phones, live transcription and the recorder used
        // for playback fight over the microphone — the recording plays back
        // fine but the transcript never arrives. Without this, the honour-
        // system box just looks blank and the learner reads it as the app
        // failing to recognise them, when really it just needs typing.
        const transcriptMissing = !!audioUrl && !_prodTranscript.trim();

        body.innerHTML = `
            <div class="sp-driller-wrap sp-prod-review-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Review Your Spoken Production</h2>
                    <p class="sp-setup-sub">Listen back to your recording and verify the transcribed text before submitting for CEFR evaluation.</p>
                </div>

                <div class="sp-prod-audio-card">
                    <div class="sp-audio-card-head">
                        <div class="sp-audio-meta">
                            <h4>Listen To Your Own Voice</h4>
                            <p>${durationStr} recording · ${words} words</p>
                        </div>
                    </div>
                    ${audioUrl ? `
                        <audio controls class="sp-own-voice-player" src="${audioUrl}"></audio>
                    ` : `
                        <p class="sp-audio-empty-note">Your recording wasn't captured for playback this time — your answer was still recognised and graded normally.</p>
                    `}
                </div>

                <div class="sp-prod-edit-card">
                    <label class="sp-edit-label" for="sp-transcript-input">
                        Transcribed Speech (Honour System)
                        <span class="sp-edit-hint">${transcriptMissing
                            ? 'Your recording came through fine, but the phone couldn\'t transcribe it automatically this time (this happens on some Android phones). Listen back above and type what you said — it still counts:'
                            : 'Speech-to-text preview — feel free to fix any words misheard by the microphone before submitting:'
                        }</span>
                    </label>
                    <textarea id="sp-transcript-input" class="sp-transcript-input" rows="7" placeholder="Your transcribed words will appear here...">${_esc(_prodTranscript)}</textarea>
                </div>

                <div class="sp-prod-review-actions">
                    <button type="button" class="vbtn vbtn-primary sp-grade-btn" data-action="submit-grading">
                        Grade My Spoken Production
                    </button>
                    <button type="button" class="vbtn vbtn-secondary" data-action="re-record">
                        Re-record
                    </button>
                    <button type="button" class="vbtn vbtn-secondary" data-action="back-prompts">
                        Back to Topics
                    </button>
                </div>
            </div>
        `;

        if (transcriptMissing) {
            const textarea = body.querySelector('#sp-transcript-input');
            if (textarea) textarea.focus();
        }

        const submitBtn = body.querySelector('[data-action="submit-grading"]');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                const textarea = body.querySelector('#sp-transcript-input');
                const text = textarea ? textarea.value.trim() : _prodTranscript.trim();
                if (!text) {
                    const msg = audioUrl
                        ? 'We heard your recording but couldn\'t transcribe it — type what you said in the box above before submitting.'
                        : 'Please speak or enter some text before submitting.';
                    if (typeof UI !== 'undefined' && UI.toast) UI.toast(msg, 'warning');
                    else alert(msg);
                    return;
                }
                _submitProdForGrading(text);
            });
        }

        const reRecordBtn = body.querySelector('[data-action="re-record"]');
        if (reRecordBtn) {
            reRecordBtn.addEventListener('click', () => {
                _startProdRecording();
            });
        }

        const backBtn = body.querySelector('[data-action="back-prompts"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                _prodPhase = PROD_PHASE.PROMPT_SELECT;
                _renderActiveTab();
            });
        }
    }

    function _renderProdAssessing(body) {
        body.innerHTML = `
            <div class="sp-driller-wrap sp-assessing-wrap">
                <div class="sp-assessing-card">
                    <div class="sp-spinner"></div>
                    <h3 class="sp-assessing-title">Evaluating Spoken Production</h3>
                    <p class="sp-assessing-sub">Analyzing fluency, coherence, grammatical accuracy, and lexical range against CEFR standards...</p>
                </div>
            </div>
        `;
    }

    async function _submitProdForGrading(text) {
        _prodTranscript = text;
        _prodPhase = PROD_PHASE.ASSESSING;
        _renderActiveTab();

        const p = _selectedProdPrompt || {};
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';

        let engine = null;
        if (typeof GraderEngine !== 'undefined') {
            engine = new GraderEngine();
        } else if (typeof ParlourGrader !== 'undefined' && ParlourGrader.GraderEngine) {
            engine = new ParlourGrader.GraderEngine();
        }

        try {
            // Grade sub-minute tasks task-completion-primary regardless of
            // whether the prompt itself was flagged can-do -- a short
            // recording is a bounded ask by construction, not an
            // open-ended fluency topic (see SHORT_TASK_MAX_SECONDS).
            const isShortTask = _prodMaxSeconds <= SHORT_TASK_MAX_SECONDS || !!p.taskCompletionPrimary;
            const context = {
                cefrLevel: p.cefrLevel || 'B1',
                taskType: 'oral_production',
                taskInstructions: p.prompt || 'Spoken production task.',
                targetSkills: p.targetSkills || ['fluency', 'oral_expression'],
                taskCompletionPrimary: isShortTask,
                language: lang,
                modality: 'oral',
                title: p.title || 'Verbal Production'
            };

            const result = await engine.grade(text, context);
            _prodAssessmentResult = result;

            if (typeof LearnerModel !== 'undefined' && LearnerModel.recordAssessment) {
                LearnerModel.recordAssessment(result, context);
            }
            if (p.targetSkills && typeof LearnerModel !== 'undefined' && LearnerModel.recordProduction) {
                const isPass = (result.overallScore || 0) >= 60;
                LearnerModel.recordProduction(p.targetSkills, isPass, result.overallScore || 0, 'oral');
            }
            if (p.targetCompetency && (result.overallScore || 0) >= 75) {
                if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.verifyCompetency === 'function') {
                    LearnerModel.verifyCompetency(p.targetCompetency, result.overallScore, 'speaking-studio');
                }
            }
            if (typeof XP !== 'undefined' && XP.award) {
                const earnedXP = Math.max(10, Math.round((result.overallScore || 70) / 5));
                XP.award(earnedXP, 'speaking-studio');
            }

            _prodPhase = PROD_PHASE.RESULTS;
            _renderActiveTab();
        } catch (error) {
            console.error('Oral assessment grading failed:', error);
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Could not complete oral evaluation: ' + error.message, 'error');
            else alert('Could not complete oral evaluation: ' + error.message);
            _prodPhase = PROD_PHASE.REVIEW;
            _renderActiveTab();
        }
    }

    // "I can ask for a coffee" -> "ask for a coffee", for weaving the
    // can-do statement into the coaching sentence below. Falls back to the
    // prompt title for non-can-do short tasks (custom sub-minute tasks).
    function _taskPhrase(prompt) {
        if (!prompt) return null;
        const raw = prompt.targetCompetency || prompt.title || null;
        if (!raw) return null;
        return raw.replace(/^i can\s+/i, '').replace(/\.\s*$/, '').trim() || null;
    }

    // Composes the short-task coaching line: a task-completion-first verdict
    // ("Well done, you've successfully asked for a coffee!"), what was
    // missed, and what to focus on next -- rather than a single feedback
    // string pulled from whichever field happened to be non-empty.
    function _prodOneLineTip(result, prompt) {
        const score = result.overallScore || 0;
        const completion = typeof result.taskCompletion === 'number' ? result.taskCompletion : (score / 100);
        const priorities = ((result.feedback && result.feedback.priorities) || []).filter(Boolean);
        const missed = (result.errors || []).map(e => e.explanation).filter(Boolean);
        const strengths = ((result.feedback && result.feedback.strengths) || []).filter(Boolean);
        const taskPhrase = _taskPhrase(prompt);

        let opener;
        if (completion >= 0.75) {
            opener = taskPhrase ? `Well done — you successfully ${taskPhrase}!` : 'Well done — task completed!';
        } else if (completion >= 0.4) {
            opener = taskPhrase ? `Good attempt at ${taskPhrase} — you got most of it across.` : 'Good attempt — you got most of it across.';
        } else {
            opener = taskPhrase ? `Not quite there yet on ${taskPhrase}.` : 'Not quite there yet.';
        }

        const sentences = [opener];
        if (missed.length) sentences.push(`You missed: ${missed.slice(0, 2).join('; ')}.`);
        if (priorities.length) sentences.push(`Focus on ${priorities.slice(0, 2).join(' and ')}.`);
        if (sentences.length === 1 && strengths.length) sentences.push(strengths[0]);
        return sentences.join(' ');
    }

    function _renderProdResults(body) {
        if (!body || !_prodAssessmentResult) return;
        const res = _prodAssessmentResult;
        const p = _selectedProdPrompt || {};
        const score = res.overallScore || 0;
        const dims = res.dimensions || {};
        const errors = res.errors || [];
        const strengths = (res.feedback && res.feedback.strengths) || [];
        const priorities = (res.feedback && res.feedback.priorities) || [];
        const stats = res.localStats || {};
        const audioUrl = _prodAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);

        let scoreColor = 'var(--success)';
        if (score < 60) scoreColor = 'var(--danger)';
        else if (score < 80) scoreColor = 'var(--accent)';

        const isShortProd = (_prodMaxSeconds <= SHORT_TASK_MAX_SECONDS) || !!p.taskCompletionPrimary;

        if (isShortProd) {
            const tip = _prodOneLineTip(res, p);
            body.innerHTML = `
                <div class="sp-driller-wrap sp-results-wrap">
                    <div class="sp-results-score-card">
                        <div class="sp-score-circle" style="border-color: ${scoreColor}">
                            <span class="sp-score-num">${score}</span>
                            <span class="sp-score-max">/100</span>
                        </div>
                        <div class="sp-score-meta">
                            <h3 class="sp-score-title">${p.targetCompetency && score >= 75 ? 'Competency Verified' : (score >= 60 ? 'Competent Oral Production' : 'Developing Oral Practice')}</h3>
                            <p class="sp-score-sub">${_esc(p.title || 'Verbal Production')} · CEFR ${_esc(p.cefrLevel || 'A1')}</p>
                        </div>
                    </div>

                    ${p.targetCompetency && score >= 75 ? `
                        <div class="sp-competency-verified-banner">
                            <span class="sp-verified-check"><svg class="sp-verified-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                            <span>Demonstrated &amp; Verified: "${_esc(p.targetCompetency)}"</span>
                        </div>
                    ` : ''}

                    <div class="sp-challenge-feedback-card" style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px 18px; margin: 16px 0;">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-weight: 700; font-size: 0.92rem; color: var(--text-heading);">Speaking Coach</span>
                            <span class="cando-badge ${score >= 60 ? 'cando-badge-verified' : 'cando-badge-gap'}" style="font-size: 0.8rem;">${score}%</span>
                        </div>
                        <p style="margin: 0; font-size: 0.98rem; color: var(--text); line-height: 1.45;">${_esc(tip)}</p>
                    </div>

                    ${audioUrl ? `
                        <div class="sp-prod-audio-replay-card">
                            <span class="sp-replay-label">Your Spoken Recording:</span>
                            <audio controls class="sp-own-voice-player" src="${audioUrl}"></audio>
                        </div>
                    ` : ''}

                    ${_prodTranscript && _prodTranscript.trim() ? `
                        <div class="sp-prod-transcript-preview" style="margin-top: 12px; padding: 10px 14px; background: rgba(0,0,0,0.03); border-radius: 8px; font-size: 0.92rem; color: var(--text);">
                            <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); letter-spacing: 0.04em; display: block; margin-bottom: 4px;">What you said:</span>
                            <p style="margin: 0; font-style: italic;">“${_esc(_prodTranscript.trim())}”</p>
                        </div>
                    ` : ''}

                    <div class="sp-local-metrics" style="margin-top: 14px;">
                        <span><strong>${stats.wordCount || (_prodTranscript.trim().split(/\s+/).length)}</strong> words</span>
                        <span><strong>${_formatTime(_prodElapsedSeconds)}</strong> speaking duration</span>
                        <span><strong>CEFR ${_esc(p.cefrLevel || 'A1')}</strong> target level</span>
                    </div>

                    <div class="vspeed-results-actions" style="margin-top: 1.5rem;">
                        <button class="vbtn vbtn-secondary" data-action="speak-again">Try Again</button>
                    </div>
                </div>
            `;

            const againBtn = body.querySelector('[data-action="speak-again"]');
            if (againBtn) {
                againBtn.addEventListener('click', () => {
                    _prodPhase = PROD_PHASE.RECORDING;
                    _prodAssessmentResult = null;
                    _prodElapsedSeconds = 0;
                    _prodTranscript = '';
                    _prodAudioUrl = null;
                    _renderActiveTab();
                    _startProdRecording();
                });
            }

            if (typeof RecommendationEngine !== 'undefined') {
                const actionsEl = body.querySelector('.vspeed-results-actions');
                if (actionsEl) {
                    RecommendationEngine.mountNextAction(actionsEl, { excludeDrillerId: 'speaking' });
                }
            }
            return;
        }

        const catLabels = {
            grammar: 'Grammar',
            vocabulary: 'Vocabulary',
            syntax: 'Syntax & Sentence Structure',
            pronunciation: 'Pronunciation & Phrasing',
            expression: 'Expression & Idiomatic Usage',
            register: 'Register & Tone'
        };

        const groupedErrors = {};
        for (const err of errors) {
            const cat = (err.category || 'expression').toLowerCase();
            if (!groupedErrors[cat]) groupedErrors[cat] = [];
            groupedErrors[cat].push(err);
        }

        const errorsHtml = errors.length ? `
            <div class="sp-results-section">
                <h4 class="sp-section-heading">Detailed Observations (${errors.length})</h4>
                <div class="sp-error-groups">
                    ${Object.entries(groupedErrors).map(([catKey, catErrors]) => `
                        <div class="sp-error-group">
                            <div class="sp-error-group-header">
                                <span class="sp-error-group-title">${_esc(catLabels[catKey] || catKey.charAt(0).toUpperCase() + catKey.slice(1))}</span>
                                <span class="sp-error-group-badge">${catErrors.length} ${catErrors.length === 1 ? 'observation' : 'observations'}</span>
                            </div>
                            <div class="sp-errors-list">
                                ${catErrors.map(err => `
                                    <div class="sp-error-card sp-severity-${_esc(err.severity)}">
                                        <div class="sp-error-head">
                                            <span class="sp-severity-tag sp-severity-${_esc(err.severity)}">${_esc(err.severity)}</span>
                                            ${err.skillId ? `<span class="sp-skill-tag">${_esc(err.skillId)}</span>` : ''}
                                        </div>
                                        <p class="sp-error-quote">"${_esc(err.text)}"</p>
                                        <p class="sp-error-expl">${_esc(err.explanation)}</p>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        ` : '';


        body.innerHTML = `
            <div class="sp-driller-wrap sp-results-wrap">
                <div class="sp-results-score-card">
                    <div class="sp-score-circle" style="border-color: ${scoreColor}">
                        <span class="sp-score-num">${score}</span>
                        <span class="sp-score-max">/100</span>
                    </div>
                    <div class="sp-score-meta">
                        <h3 class="sp-score-title">${score >= 80 ? 'Strong Oral Production' : (score >= 60 ? 'Competent Oral Production' : 'Developing Oral Competence')}</h3>
                        <p class="sp-score-sub">${_esc(p.title || 'Verbal Production')} · CEFR ${_esc(p.cefrLevel || 'B1')}</p>
                    </div>
                </div>

                ${p.targetCompetency && score >= 75 ? `
                    <div class="sp-competency-verified-banner">
                        <span class="sp-verified-check"><svg class="sp-verified-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                        <span>Demonstrated &amp; Verified: "${_esc(p.targetCompetency)}"</span>
                    </div>
                ` : ''}

                ${audioUrl ? `
                    <div class="sp-prod-audio-replay-card">
                        <span class="sp-replay-label">Your Spoken Recording:</span>
                        <audio controls class="sp-own-voice-player" src="${audioUrl}"></audio>
                    </div>
                ` : ''}

                <div class="sp-dimensions-grid">
                    ${Object.entries(dims).map(([dim, val]) => `
                        <div class="sp-dim-card">
                            <span class="sp-dim-name">${_esc(dim.charAt(0).toUpperCase() + dim.slice(1))}</span>
                            <div class="sp-dim-bar"><div class="sp-dim-fill" style="width: ${Math.round(val * 100)}%"></div></div>
                            <span class="sp-dim-val">${Math.round(val * 100)}%</span>
                        </div>
                    `).join('')}
                </div>

                <div class="sp-feedback-cols">
                    <div class="sp-feedback-col sp-strengths">
                        <h4>Oral Strengths</h4>
                        <ul>${strengths.map(s => `<li>${_esc(s)}</li>`).join('')}</ul>
                    </div>
                    <div class="sp-feedback-col sp-priorities">
                        <h4>Improvement Priorities</h4>
                        <ul>${priorities.map(pr => `<li>${_esc(pr)}</li>`).join('')}</ul>
                    </div>
                </div>

                ${errorsHtml}

                <div class="sp-local-metrics">
                    <span><strong>${stats.wordCount || (_prodTranscript.trim().split(/\s+/).length)}</strong> words</span>
                    <span><strong>${_formatTime(_prodElapsedSeconds)}</strong> speaking duration</span>
                    <span><strong>CEFR ${_esc(p.cefrLevel || 'B1')}</strong> target level</span>
                </div>

                <div class="vspeed-results-actions" style="margin-top: 2rem;">
                    <button class="vbtn vbtn-secondary" data-action="speak-again">Speak Another Topic</button>
                </div>
            </div>
        `;

        const againBtn = body.querySelector('[data-action="speak-again"]');
        if (againBtn) {
            againBtn.addEventListener('click', () => {
                _prodPhase = PROD_PHASE.PROMPT_SELECT;
                _selectedProdPrompt = null;
                _prodAssessmentResult = null;
                _renderActiveTab();
            });
        }

        if (typeof RecommendationEngine !== 'undefined') {
            const actionsEl = body.querySelector('.vspeed-results-actions');
            if (actionsEl) {
                RecommendationEngine.mountNextAction(actionsEl, { excludeDrillerId: 'speaking' });
            }
        }
    }

    // ============================================
    // MAIN ENTRY POINT & LIFECYCLE
    // ============================================

    function stop() {
        _stopTimer();
        if (_prodTimerInterval) {
            clearInterval(_prodTimerInterval);
            _prodTimerInterval = null;
        }
        if (typeof SpeechInput !== 'undefined') {
            SpeechInput.stopListening();
        }
    }

    async function render(container, options = {}) {
        _container = container;
        _onExit = (options && options.onExit) || null;
        await _load();
        await _loadProdPrompts();

        // Reset to the default cap unless this render is about to set its
        // own (targetCompetency below) — otherwise a short maxSeconds from
        // an earlier quick-speaking prompt this page session would leak
        // into the tab label/timer of an unrelated later normal entry into
        // Verbal Production.
        if (!(options && options.targetCompetency)) {
            _prodMaxSeconds = 300;
        }

        if (options && options.activeTab) {
            _activeStudioTab = options.activeTab;
        }

        if (options && options.level) {
            _level = options.level;
        }
        if (options && options.skill) {
            _skill = options.skill;
        } else {
            _skill = null;
        }
        if (options && options.count) {
            _questionCount = options.count;
            _mode = MODE.COUNT;
        }

        if (options && options.targetCompetency) {
            _activeStudioTab = STUDIO_TAB.PRODUCTION;
            const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';
            const langCode = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
            const formatted = (typeof CanDoPrompt !== 'undefined')
                ? CanDoPrompt.formatPrompt(options.targetCompetency, {
                    language: langName,
                    langCode: langCode,
                    modality: 'oral',
                    level: options.level || 'A1'
                })
                : null;
            _selectedProdPrompt = {
                id: 'comp_' + Date.now(),
                title: formatted ? formatted.title : (options.targetCompetency.length > 35 ? options.targetCompetency.slice(0, 32) + '...' : options.targetCompetency),
                scenario: formatted ? formatted.scenario : '',
                cefrLevel: options.level || 'A1',
                prompt: formatted ? formatted.prompt : `Demonstrate this ability out loud: "${options.targetCompetency}". Speak clearly and naturally — however much the task itself calls for.`,
                cues: formatted ? formatted.cues : [],
                targetCompetency: options.targetCompetency,
                taskCompletionPrimary: true
            };
            // Defaults to SHORT_TASK_MAX_SECONDS (Journey's "unverified
            // competencies" nudge, the Studio's own card) — a can-do prompt
            // like "greet someone" is a bounded ask, not an open-ended
            // fluency topic, so it stays short unless a caller (e.g.
            // Time-Based Sessions) passes its own maxSeconds.
            _prodMaxSeconds = options.maxSeconds || SHORT_TASK_MAX_SECONDS;
            _prodPhase = PROD_PHASE.RECORDING;
            _renderStudioShell();
            _startProdRecording();
            return;
        }

        if (options && options.autoStart) {
            _activeStudioTab = STUDIO_TAB.DRILLS;
            _phase = PHASE.SESSION;
            _renderStudioShell();
            _startSession();
            return;
        }

        _phase = PHASE.SETTINGS;
        _prodPhase = PROD_PHASE.PROMPT_SELECT;
        _renderStudioShell();
    }

    return {
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.SpeakingDriller = SpeakingDriller;
    window.SpeakingStudio = SpeakingDriller; // alias for clarity
}
