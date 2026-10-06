// ============================================
// LISTENING STUDIO
// ============================================
// Complete CEFR aural hub for Parlour:
//
// 1. Listening Comprehension (CEFR Passage Exam Lab):
//    - Multi-speaker dialogues, announcements, and narrative passages.
//    - Authentic CEFR two-pass protocol (Pass 1 -> 15s intermission pause -> Pass 2).
//    - Real-time turn highlighting and speech synthesis via ParlourTTS with character voices.
//    - Single-choice (listening-mc) and True/False/Not Stated (true-false-not-stated).
//    - Interactive full audio transcript with per-turn audio replay & translation toggle.
//    - Deep pedagogical review with highlighted evidence quotes and explanations.
//
// 2. Decoding Drills (Sentence Drills):
//    - Rapid aural decoding drills embedded from ListeningDriller:
//      Listen -> Meaning, Listen -> Spanish, Listen -> Type, Listen -> Missing word.
//    - Timed and count modes, level filters, dual-track support.

const ListeningStudio = (function () {
    'use strict';

    const STUDIO_TAB = {
        COMPREHENSION: 'comprehension',
        DECODING: 'decoding'
    };

    const PHASE = {
        PICKER: 'picker',
        PREVIEW: 'preview',
        SESSION: 'session',
        RESULTS: 'results'
    };

    let _container = null;
    let _activeStudioTab = STUDIO_TAB.COMPREHENSION;
    let _subOptions = null;

    // ---- Comprehension State ----
    let _phase = PHASE.PICKER;
    let _tasksData = null;
    let _loadedLang = null;
    let _levelFilter = 'all';
    let _selectedTask = null;
    let _userAnswers = {};

    // Audio Playback State
    let _currentPass = 1; // 1 or 2
    let _isPlaying = false;
    let _currentTurnIndex = -1;
    let _turnTimer = null;
    let _intermissionTimer = null;
    let _countdownSeconds = 0;
    let _playbackSpeed = 1.0;
    let _showTranscriptInResults = true;
    let _showEnglishTranslations = false;

    function _esc(text) {
        if (typeof UI !== 'undefined' && UI.escape) return UI.escape(text);
        const d = document.createElement('div');
        d.textContent = String(text == null ? '' : text);
        return d.innerHTML;
    }

    // ----------------------------------------
    // DATA LOADING
    // ----------------------------------------
    async function _loadTasks() {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        if (_tasksData && _loadedLang === lang) return _tasksData;

        let tasks = [];

        // 1. Try loading from content/<lang>/listening-tasks.json
        if (typeof Content !== 'undefined' && typeof Lang !== 'undefined' && Lang.content) {
            try {
                const data = await Content.json(Lang.content('listening-tasks.json'));
                if (data && Array.isArray(data.tasks)) {
                    tasks = tasks.concat(data.tasks);
                }
            } catch (e) {
                // Ignore missing file
            }
        }

        // 2. Scan level tests for listeningSection (a1, a2, b1, b2, c1)
        const testLevels = ['a1', 'a2', 'b1', 'b2', 'c1'];
        if (typeof Content !== 'undefined' && typeof Lang !== 'undefined' && Lang.content) {
            for (const lvl of testLevels) {
                try {
                    const testData = await Content.json(Lang.content(`tests/${lvl}-test.json`));
                    if (testData && testData.listeningSection) {
                        const ls = testData.listeningSection;
                        const taskId = ls.id || `test-${lvl}`;
                        if (!tasks.some(t => t.id === taskId)) {
                            tasks.push({
                                id: taskId,
                                level: (testData.level || lvl).toUpperCase(),
                                title: ls.title || `${(testData.level || lvl).toUpperCase()} Level Test Passage`,
                                topic: ls.topic || 'Official Assessment',
                                format: (ls.audio && ls.audio.turns && ls.audio.turns.length > 2) ? 'dialogue' : 'announcement',
                                context: ls.context || '',
                                previewSeconds: ls.previewSeconds || 30,
                                audio: ls.audio,
                                questions: ls.questions || [],
                                source: `Level Test ${(testData.level || lvl).toUpperCase()}`
                            });
                        }
                    }
                } catch (e) {
                    // Ignore missing test file
                }
            }
        }

        // 3. Fallback built-in tasks if none loaded
        if (tasks.length === 0) {
            tasks = _getFallbackTasks(lang);
        }

        _tasksData = tasks;
        _loadedLang = lang;
        return _tasksData;
    }

    function _getFallbackTasks(lang) {
        if (lang === 'hu') {
            return [
                {
                    id: 'ls-hu-fallback-01',
                    level: 'A1',
                    title: 'A kávézóban',
                    topic: 'Rendelés és mindennapi helyzetek',
                    format: 'dialogue',
                    context: 'Egy budapesti kávézóban Anna rendel a pincértől.',
                    previewSeconds: 30,
                    audio: {
                        turns: [
                            { speaker: 'Pincér', gender: 'male', text: 'Jó napot kívánok! Mit hozhatok Önnek?', textEn: 'Good day! What can I bring you?' },
                            { speaker: 'Anna', gender: 'female', text: 'Jó napot! Egy kapucsínót és egy szénsavmentes ásványvizet kérek szépen.', textEn: 'Good day! A cappuccino and a still mineral water, please.' },
                            { speaker: 'Pincér', gender: 'male', text: 'Rendben van. Cukorral kéri a kávét?', textEn: 'All right. Would you like the coffee with sugar?' },
                            { speaker: 'Anna', gender: 'female', text: 'Cukor nélkül, köszönöm. És egy szelet túrós rétest is kérek.', textEn: 'Without sugar, thank you. And a slice of strudel please.' },
                            { speaker: 'Pincér', gender: 'male', text: 'Összesen kétezer-négyszáz forint lesz. Kártyával vagy készpénzzel fizet?', textEn: 'Total will be 2400 forints. Card or cash?' },
                            { speaker: 'Anna', gender: 'female', text: 'Kártyával fizetek, köszönöm.', textEn: 'I pay by card, thank you.' }
                        ]
                    },
                    questions: [
                        {
                            id: 'q1',
                            type: 'listening-mc',
                            question: 'Mit rendel Anna inni?',
                            options: ['Egy kapucsínót és szénsavmentes ásványvizet', 'Egy fekete teát', 'Egy pohár bort'],
                            correct: 0,
                            evidence: 'Egy kapucsínót és egy szénsavmentes ásványvizet kérek szépen.',
                            explanation: 'Anna egy kapucsínót és szénsavmentes vizet rendel.'
                        },
                        {
                            id: 'q2',
                            type: 'listening-mc',
                            question: 'Hogyan kéri Anna a kávét?',
                            options: ['Cukor nélkül', 'Sok cukorral', 'Tejszínnel'],
                            correct: 0,
                            evidence: 'Cukor nélkül, köszönöm.',
                            explanation: 'Anna egyértelműen kijelenti, hogy cukor nélkül kéri.'
                        },
                        {
                            id: 'q3',
                            type: 'listening-mc',
                            question: 'Milyen süteményt kér a vendég?',
                            options: ['Egy szelet túrós rétest', 'Egy almás pitét', 'Egy csokitortát'],
                            correct: 0,
                            evidence: 'És egy szelet túrós rétest is kérek.',
                            explanation: 'Anna túrós rétest választ.'
                        }
                    ]
                }
            ];
        }

        // Spanish default fallback
        return [
            {
                id: 'ls-es-fallback-01',
                level: 'A1',
                title: 'En la cafetería',
                topic: 'Pedir comida y bebida',
                format: 'dialogue',
                context: 'Vas a escuchar una conversación entre una clienta (Elena) y un camarero en una cafetería en Madrid.',
                previewSeconds: 30,
                audio: {
                    turns: [
                        { speaker: 'Camarero', gender: 'male', text: '¡Hola! Buenas tardes. ¿Qué le pongo?', textEn: 'Hello! Good afternoon. What can I get you?' },
                        { speaker: 'Elena', gender: 'female', text: 'Hola. Para mí un café con leche y una tostada con aceite y tomate, por favor.', textEn: 'Hello. For me, a white coffee and toast with olive oil and tomato, please.' },
                        { speaker: 'Camarero', gender: 'male', text: 'Muy bien. ¿El café con azúcar o sin azúcar?', textEn: 'Very well. Coffee with sugar or without sugar?' },
                        { speaker: 'Elena', gender: 'female', text: 'Con azúcar, gracias. ¿Y cuánto cuesta todo?', textEn: 'With sugar, thank you. And how much is everything?' },
                        { speaker: 'Camarero', gender: 'male', text: 'Son tres euros con cincuenta céntimos.', textEn: 'It is three euros and fifty cents.' },
                        { speaker: 'Elena', gender: 'female', text: 'Aquí tiene cuatro euros. Quédese con el cambio.', textEn: 'Here is four euros. Keep the change.' },
                        { speaker: 'Camarero', gender: 'male', text: 'Muchas gracias. Ahora mismo se lo traigo a la mesa tres.', textEn: 'Thank you very much. I will bring it right away to table three.' }
                    ]
                },
                questions: [
                    {
                        id: 'q1',
                        type: 'listening-mc',
                        question: '¿Qué pide Elena para desayunar?',
                        options: ['Un café con leche y una tostada', 'Un té verde y un cruasán', 'Un zumo y un bocadillo'],
                        correct: 0,
                        evidence: 'Para mí un café con leche y una tostada con aceite y tomate, por favor.',
                        explanation: 'Elena pide directamente un café con leche y una tostada.'
                    },
                    {
                        id: 'q2',
                        type: 'listening-mc',
                        question: '¿Cómo prefiere el café Elena?',
                        options: ['Con azúcar', 'Sin azúcar', 'Con hielo'],
                        correct: 0,
                        evidence: 'Con azúcar, gracias.',
                        explanation: 'Elena contesta afirmativamente cuando el camarero pregunta si desea azúcar.'
                    },
                    {
                        id: 'q3',
                        type: 'listening-mc',
                        question: '¿Cuánto cuesta el desayuno en total?',
                        options: ['Tres euros con cincuenta', 'Cuatro euros', 'Dos euros con cincuenta'],
                        correct: 0,
                        evidence: 'Son tres euros con cincuenta céntimos.',
                        explanation: 'El camarero confirma que la cuenta total asciende a 3,50 €.'
                    },
                    {
                        id: 'q4',
                        type: 'listening-mc',
                        question: '¿Dónde se sentará la clienta?',
                        options: ['En la mesa tres', 'En la barra', 'En la terraza'],
                        correct: 0,
                        evidence: 'Ahora mismo se lo traigo a la mesa tres.',
                        explanation: 'El camarero indica que le servirá el pedido en la mesa número tres.'
                    }
                ]
            }
        ];
    }

    if (typeof document !== 'undefined') {
        document.addEventListener('language-changed', () => {
            _tasksData = null;
            _loadedLang = null;
            _selectedTask = null;
            _stopAudio();
        });
    }

    // ----------------------------------------
    // AUDIO ENGINE (CEFR TWO-PASS PROTOCOL)
    // ----------------------------------------
    function _stopAudio() {
        _isPlaying = false;
        _currentTurnIndex = -1;
        if (_turnTimer) { clearTimeout(_turnTimer); _turnTimer = null; }
        if (_intermissionTimer) { clearInterval(_intermissionTimer); _intermissionTimer = null; }
        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.stop) {
            ParlourTTS.stop();
        }
    }

    // TTS options for one turn. Only `gender` picks the voice: ParlourTTS's
    // `character` is a Chirp3-HD voice name (e.g. 'Charon'), not a speaker
    // name, and passing 'Camarero' there asks Google for a voice that
    // doesn't exist, so every turn failed.
    function _turnTtsOptions(turn) {
        return {
            text: turn.text,
            type: 'listening',
            gender: turn.gender || 'male'
        };
    }

    function _preloadTurns() {
        if (!_selectedTask || !_selectedTask.audio || !_selectedTask.audio.turns) return;
        if (typeof ParlourTTS === 'undefined' || !ParlourTTS.preload) return;
        _selectedTask.audio.turns.forEach(turn => ParlourTTS.preload(_turnTtsOptions(turn)));
    }

    function _startPass(passNumber) {
        if (!_selectedTask || !_selectedTask.audio || !_selectedTask.audio.turns) return;
        _stopAudio();
        _currentPass = passNumber;
        _isPlaying = true;
        _currentTurnIndex = 0;
        _preloadTurns();
        _playTurnSequence();
    }

    let _turnToken = 0;

    function _playTurnSequence() {
        if (!_isPlaying || !_selectedTask || !_selectedTask.audio || !_selectedTask.audio.turns) return;
        const turns = _selectedTask.audio.turns;

        if (_currentTurnIndex >= turns.length) {
            // End of pass
            _isPlaying = false;
            _currentTurnIndex = -1;
            if (_currentPass === 1) {
                _startIntermission();
            } else {
                _updateAudioConsole();
            }
            return;
        }

        const turn = turns[_currentTurnIndex];
        _updateAudioConsole();

        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
            const token = ++_turnToken;
            const isCurrent = () => token === _turnToken && _isPlaying;
            const advance = () => {
                if (!isCurrent()) return;
                _turnToken++; // any late callback for this turn is now stale
                if (_turnTimer) { clearTimeout(_turnTimer); _turnTimer = null; }
                _currentTurnIndex++;
                _turnTimer = setTimeout(_playTurnSequence, 450); // natural conversational pause
            };

            const started = ParlourTTS.speak(Object.assign(_turnTtsOptions(turn), {
                speed: _playbackSpeed,
                onEnded: advance
            }));

            // speak() resolves once audio has started (true) or nothing could
            // play (false). Arm the safety net only after that, so a slow
            // network fetch can't cut a turn off before it's even begun.
            Promise.resolve(started).then(ok => {
                if (!isCurrent()) return;
                if (!ok) { advance(); return; }
                const estMs = Math.max(2500, turn.text.length * 110) / _playbackSpeed;
                _turnTimer = setTimeout(advance, estMs + 4000);
            }, () => advance());
        } else {
            // Fallback if no TTS
            _turnTimer = setTimeout(() => {
                _currentTurnIndex++;
                _playTurnSequence();
            }, 3000);
        }
    }

    function _startIntermission() {
        _countdownSeconds = 15;
        _updateAudioConsole();

        _intermissionTimer = setInterval(() => {
            _countdownSeconds--;
            if (_countdownSeconds <= 0) {
                clearInterval(_intermissionTimer);
                _intermissionTimer = null;
                _startPass(2);
            } else {
                _updateAudioConsole();
            }
        }, 1000);
    }

    function _skipIntermission() {
        if (_intermissionTimer) {
            clearInterval(_intermissionTimer);
            _intermissionTimer = null;
        }
        _startPass(2);
    }

    function _playSingleTurn(turnIndex) {
        if (!_selectedTask || !_selectedTask.audio || !_selectedTask.audio.turns) return;
        const turn = _selectedTask.audio.turns[turnIndex];
        if (!turn) return;

        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
            ParlourTTS.speak(Object.assign(_turnTtsOptions(turn), { speed: _playbackSpeed }));
        }
    }

    // ----------------------------------------
    // STUDIO SHELL RENDERER
    // ----------------------------------------
    function _renderStudioShell() {
        if (!_container) return;

        _container.innerHTML = `
            <div class="sp-studio-wrap ls-studio-wrap">
                <div class="sp-studio-nav ls-studio-nav" role="tablist">
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.COMPREHENSION ? 'active' : ''}" data-studio-tab="comprehension" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.COMPREHENSION}">
                        Listening Comprehension
                    </button>
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.DECODING ? 'active' : ''}" data-studio-tab="decoding" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.DECODING}">
                        Decoding Drills
                    </button>
                </div>
                <div class="sp-studio-body ls-studio-body" id="ls-studio-mount"></div>
            </div>
        `;

        _container.querySelectorAll('[data-studio-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-studio-tab');
                if (target === _activeStudioTab) return;
                stop();
                _activeStudioTab = target;
                _subOptions = null;
                _renderStudioShell();
            });
        });

        _renderActiveTab();
    }

    function _renderActiveTab() {
        const mount = document.getElementById('ls-studio-mount');
        if (!mount) return;

        if (_activeStudioTab === STUDIO_TAB.DECODING) {
            if (typeof ListeningDriller !== 'undefined') {
                ListeningDriller.render(mount, _subOptions);
            } else {
                mount.innerHTML = '<div class="gd-loading">Loading Decoding Drills…</div>';
            }
        } else {
            _renderComprehension(mount);
        }
    }

    // ----------------------------------------
    // COMPREHENSION VIEWS
    // ----------------------------------------
    async function _renderComprehension(mount) {
        if (_phase === PHASE.PICKER) {
            await _renderTaskPicker(mount);
        } else if (_phase === PHASE.PREVIEW) {
            _renderTaskPreview(mount);
        } else if (_phase === PHASE.SESSION) {
            _renderActiveSession(mount);
        } else if (_phase === PHASE.RESULTS) {
            _renderResults(mount);
        }
    }

    // 1. Task Picker Screen
    async function _renderTaskPicker(mount) {
        mount.innerHTML = '<div class="gd-loading">Loading listening passages…</div>';
        const tasks = await _loadTasks();

        const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
        const availableLevels = Array.from(new Set(tasks.map(t => t.level).filter(Boolean)))
            .sort((a, b) => CEFR_ORDER.indexOf(a) - CEFR_ORDER.indexOf(b));

        const filteredTasks = _levelFilter === 'all'
            ? tasks
            : tasks.filter(t => t.level === _levelFilter);

        mount.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Listening Comprehension Studio</h2>
                    <p class="sp-setup-desc">
                        Simulate CEFR exam listening tasks. Listen to authentic multi-speaker dialogues and announcements, answer comprehension questions, and inspect detailed evidence quotes.
                    </p>
                </div>

                ${availableLevels.length > 1 ? `
                    <div class="wk-config-group">
                        <label class="wk-config-label">Level</label>
                        <div class="wk-pill-row">
                            <button type="button" class="wk-pill ${_levelFilter === 'all' ? 'active' : ''}" data-ls-level="all">All</button>
                            ${availableLevels.map(lvl => `
                                <button type="button" class="wk-pill ${_levelFilter === lvl ? 'active' : ''}" data-ls-level="${_esc(lvl)}">${_esc(lvl)}</button>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                <div class="wk-picker-grid">
                    ${filteredTasks.map(task => {
                        const turnsCount = (task.audio && task.audio.turns) ? task.audio.turns.length : 0;
                        const questionsCount = (task.questions) ? task.questions.length : 0;
                        return `
                            <div class="wk-card sp-card-clickable ls-task-card" data-select-task="${_esc(task.id)}">
                                <div class="sp-prompt-card-head">
                                    <span class="sp-level-pill">${_esc(task.level)}</span>
                                    <span class="sp-words-target">${turnsCount} turns · ${questionsCount} questions</span>
                                </div>
                                <h3 class="wk-card-title">${_esc(task.title)}</h3>
                                <p class="wk-card-sub">${_esc(task.context || task.topic || 'Audio comprehension task')}</p>
                                <div class="ls-task-card-footer">
                                    <span class="ls-format-badge">${_esc(task.format || 'dialogue')}</span>
                                    <span class="ls-task-arrow">Start task →</span>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;

        mount.querySelectorAll('[data-ls-level]').forEach(btn => {
            btn.addEventListener('click', () => {
                _levelFilter = btn.getAttribute('data-ls-level');
                _renderTaskPicker(mount);
            });
        });

        mount.querySelectorAll('[data-select-task]').forEach(card => {
            card.addEventListener('click', () => {
                const id = card.getAttribute('data-select-task');
                _selectedTask = tasks.find(t => t.id === id);
                if (_selectedTask) {
                    _userAnswers = {};
                    _phase = PHASE.PREVIEW;
                    _renderComprehension(mount);
                }
            });
        });
    }

    // 2. Task Preview (Pre-listening preparation)
    function _renderTaskPreview(mount) {
        if (!_selectedTask) { _phase = PHASE.PICKER; return _renderComprehension(mount); }

        const questions = _selectedTask.questions || [];

        mount.innerHTML = `
            <div class="sp-driller-wrap">
                <button type="button" class="wk-back" data-action="back-to-picker" aria-label="All Passages">
                    <svg class="art icon wk-back-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    <span>All Passages</span>
                </button>

                <div class="sp-setup-head">
                    <div class="sp-prompt-card-head" style="margin-bottom:8px;">
                        <span class="sp-level-pill">${_esc(_selectedTask.level)}</span>
                        <span class="sp-words-target">${_selectedTask.format || 'Dialogue'}</span>
                    </div>
                    <h2 class="sp-setup-title">${_esc(_selectedTask.title)}</h2>
                    <p class="sp-setup-desc">${_esc(_selectedTask.context)}</p>
                </div>

                <div class="ls-exam-protocol-banner">
                    <div class="ls-protocol-badge">CEFR 2-Pass Protocol</div>
                    <p>
                        In this task, you will hear the recording <strong>twice</strong>. There will be a short pause between the two listenings.
                        Before listening, review the questions below so you know what details to focus on.
                    </p>
                </div>

                <div class="ls-preview-questions-card">
                    <h3 class="ls-preview-header">Questions Preview (${questions.length} questions)</h3>
                    <div class="ls-preview-list">
                        ${questions.map((q, idx) => `
                            <div class="ls-preview-q-item">
                                <span class="ls-preview-num">${idx + 1}.</span>
                                <div class="ls-preview-text">
                                    <div class="ls-q-title">${_esc(q.question || q.statement)}</div>
                                    ${q.options ? `
                                        <div class="ls-preview-options-row">
                                            ${q.options.map(opt => `<span class="ls-preview-opt-chip">${_esc(opt)}</span>`).join('')}
                                        </div>
                                    ` : ''}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <div class="sp-action-row" style="margin-top:24px;">
                    <button type="button" class="btn btn-primary ls-start-btn" data-action="start-listening">
                        ▶ Begin Listening (Pass 1 of 2)
                    </button>
                </div>
            </div>
        `;

        const backBtn = mount.querySelector('[data-action="back-to-picker"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                _stopAudio();
                _phase = PHASE.PICKER;
                _renderComprehension(mount);
            });
        }

        const startBtn = mount.querySelector('[data-action="start-listening"]');
        if (startBtn) {
            startBtn.addEventListener('click', () => {
                _phase = PHASE.SESSION;
                _renderComprehension(mount);
                _startPass(1);
            });
        }
    }

    // 3. Active Session Screen (Two-pass playback + questions answering)
    function _renderActiveSession(mount) {
        if (!_selectedTask) { _phase = PHASE.PICKER; return _renderComprehension(mount); }

        mount.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="ls-session-header">
                    <button type="button" class="wk-back" data-action="abandon-session" aria-label="Exit Task">
                        <svg class="art icon wk-back-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
                        <span>Exit Task</span>
                    </button>
                    <div class="ls-session-badge">${_esc(_selectedTask.level)} · ${_esc(_selectedTask.title)}</div>
                </div>

                <!-- Audio Console Box -->
                <div class="lt-audio-console" id="ls-audio-console"></div>

                <!-- Questions List -->
                <div class="ls-questions-container" id="ls-questions-list"></div>

                <!-- Submission Controls -->
                <div class="sp-action-row" style="margin-top:24px;">
                    <button type="button" class="btn btn-primary" id="ls-submit-answers-btn" data-action="submit-answers">
                        Check Answers & Review Evidence
                    </button>
                </div>
            </div>
        `;

        const exitBtn = mount.querySelector('[data-action="abandon-session"]');
        if (exitBtn) {
            exitBtn.addEventListener('click', () => {
                _stopAudio();
                _phase = PHASE.PREVIEW;
                _renderComprehension(mount);
            });
        }

        const submitBtn = mount.querySelector('[data-action="submit-answers"]');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                _stopAudio();
                _phase = PHASE.RESULTS;
                _renderComprehension(mount);
            });
        }

        _updateAudioConsole();
        _renderQuestionsList();
    }

    function _updateAudioConsole() {
        const consoleEl = document.getElementById('ls-audio-console');
        if (!consoleEl || !_selectedTask) return;

        let statusTitle = '';
        let statusSub = '';
        let controlsHtml = '';

        if (_isPlaying) {
            const turn = (_selectedTask.audio && _selectedTask.audio.turns && _currentTurnIndex >= 0)
                ? _selectedTask.audio.turns[_currentTurnIndex]
                : null;

            statusTitle = `Pass ${_currentPass} of 2: Playing audio`;
            statusSub = turn ? `Speaking: ${turn.speaker}` : 'Listening attentively...';

            controlsHtml = `
                <button type="button" class="lt-audio-btn lt-audio-btn-stop" data-action="audio-pause">⏸ Stop Audio</button>
                <button type="button" class="lt-audio-btn-sm" data-action="toggle-speed">${_playbackSpeed}x Speed</button>
            `;
        } else if (_intermissionTimer) {
            statusTitle = 'Intermission: Pause between listenings';
            statusSub = `Second listen begins in ${_countdownSeconds}s — review your answers.`;

            controlsHtml = `
                <button type="button" class="btn btn-primary lt-audio-btn" data-action="skip-pause">▶ Skip to Second Listen</button>
            `;
        } else if (_currentPass === 2 && !_isPlaying) {
            statusTitle = 'Listening Complete';
            statusSub = 'Both passes finished. Review your answers below and submit.';

            controlsHtml = `
                <button type="button" class="lt-audio-btn" data-action="replay-pass-2">↺ Replay Pass 2</button>
                <button type="button" class="lt-audio-btn-sm" data-action="toggle-speed">${_playbackSpeed}x Speed</button>
            `;
        } else {
            statusTitle = `Pass ${_currentPass} of 2 ready`;
            statusSub = 'Press play when ready.';

            controlsHtml = `
                <button type="button" class="btn btn-primary lt-audio-btn" data-action="audio-play">▶ Play Pass ${_currentPass}</button>
            `;
        }

        const audioIconHtml = (typeof Art !== 'undefined' && Art.icon)
            ? Art.icon('listening')
            : '<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false"><line class="ink-line" x1="4" y1="10" x2="4" y2="14"/><line class="ink-line" x1="8" y1="7" x2="8" y2="17"/><line class="ink-line" x1="12" y1="4" x2="12" y2="20"/><line class="ink-line" x1="16" y1="8" x2="16" y2="16"/><line class="ink-line" x1="20" y1="11" x2="20" y2="13"/></svg>';

        consoleEl.innerHTML = `
            <div class="lt-audio-console-top">
                <div class="lt-audio-icon ${_isPlaying ? 'is-playing' : ''}" aria-hidden="true">${audioIconHtml}</div>
                <div class="lt-audio-status-wrap">
                    <span class="lt-audio-status-label">${_esc(statusTitle)}</span>
                    <span class="lt-audio-status-detail">${_esc(statusSub)}</span>
                </div>
            </div>
            <div class="lt-audio-controls">
                ${controlsHtml}
            </div>
        `;

        const playBtn = consoleEl.querySelector('[data-action="audio-play"]');
        if (playBtn) playBtn.addEventListener('click', () => _startPass(_currentPass));

        const pauseBtn = consoleEl.querySelector('[data-action="audio-pause"]');
        if (pauseBtn) pauseBtn.addEventListener('click', () => { _stopAudio(); _updateAudioConsole(); });

        const skipBtn = consoleEl.querySelector('[data-action="skip-pause"]');
        if (skipBtn) skipBtn.addEventListener('click', () => _skipIntermission());

        const replayBtn = consoleEl.querySelector('[data-action="replay-pass-2"]');
        if (replayBtn) replayBtn.addEventListener('click', () => _startPass(2));

        const speedBtn = consoleEl.querySelector('[data-action="toggle-speed"]');
        if (speedBtn) {
            speedBtn.addEventListener('click', () => {
                _playbackSpeed = (_playbackSpeed === 1.0) ? 0.85 : 1.0;
                _updateAudioConsole();
            });
        }
    }

    function _renderQuestionsList() {
        const listEl = document.getElementById('ls-questions-list');
        if (!listEl || !_selectedTask) return;

        const questions = _selectedTask.questions || [];

        listEl.innerHTML = questions.map((q, qIndex) => {
            const userAns = _userAnswers[q.id];

            if (q.type === 'true-false-not-stated') {
                const labels = (_loadedLang === 'hu')
                    ? ['Igaz', 'Hamis', 'Nincs említve']
                    : ['Verdadero', 'Falso', 'No se menciona'];

                return `
                    <div class="lt-question-card" data-qid="${_esc(q.id)}">
                        <div class="lt-q-num">Question ${qIndex + 1}</div>
                        <div class="lt-q-text">${_esc(q.statement)}</div>
                        <div class="lt-options-row">
                            ${labels.map((lbl, idx) => `
                                <button type="button" class="lt-opt-btn ${userAns === idx ? 'selected' : ''}" data-ans="${idx}">
                                    ${_esc(lbl)}
                                </button>
                            `).join('')}
                        </div>
                    </div>
                `;
            }

            // listening-mc
            return `
                <div class="lt-question-card" data-qid="${_esc(q.id)}">
                    <div class="lt-q-num">Question ${qIndex + 1}</div>
                    <div class="lt-q-text">${_esc(q.question)}</div>
                    <div class="lt-options-col">
                        ${(q.options || []).map((opt, idx) => `
                            <button type="button" class="lt-opt-btn ${userAns === idx ? 'selected' : ''}" data-ans="${idx}">
                                <span class="lt-opt-bullet">${String.fromCharCode(65 + idx)}.</span>
                                <span class="lt-opt-label">${_esc(opt)}</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
            `;
        }).join('');

        // Attach option selection events
        listEl.querySelectorAll('.lt-opt-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const card = btn.closest('.lt-question-card');
                const qid = card.getAttribute('data-qid');
                const ansIdx = parseInt(btn.getAttribute('data-ans'), 10);
                _userAnswers[qid] = ansIdx;
                _renderQuestionsList();
            });
        });
    }

    // 4. Results & Pedagogical Review Screen
    function _renderResults(mount) {
        if (!_selectedTask) { _phase = PHASE.PICKER; return _renderComprehension(mount); }

        const questions = _selectedTask.questions || [];
        let score = 0;
        questions.forEach(q => {
            if (_userAnswers[q.id] === q.correct) score++;
        });

        const pct = Math.round((score / Math.max(1, questions.length)) * 100);
        const passed = pct >= 75;

        mount.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Task Results</h2>
                    <p class="sp-setup-desc">${_esc(_selectedTask.level)} · ${_esc(_selectedTask.title)}</p>
                </div>

                <div class="ls-results-banner ${passed ? 'ls-banner-pass' : 'ls-banner-retry'}">
                    <div class="ls-results-score">${score} / ${questions.length}</div>
                    <div class="ls-results-pct">${pct}% Correct</div>
                    <div class="ls-results-desc">
                        ${passed
                            ? 'Excellent CEFR listening comprehension achieved! You retrieved key details and accurately parsed the conversation.'
                            : 'Good effort. Review the audio transcript and highlighted evidence quotes below to identify where details differed.'}
                    </div>
                </div>

                <div class="sp-action-row" style="margin-bottom:20px;">
                    <button type="button" class="btn btn-secondary" data-action="toggle-transcript">
                        ${_showTranscriptInResults ? 'Hide Transcript' : 'Show Full Audio Transcript'}
                    </button>
                    <button type="button" class="btn btn-secondary" data-action="toggle-translations">
                        ${_showEnglishTranslations ? 'Hide Translations' : 'Show Translations'}
                    </button>
                </div>

                <!-- Transcript Card -->
                <div class="lt-transcript-card ${_showTranscriptInResults ? '' : 'hidden'}" id="ls-results-transcript">
                    <div class="lt-transcript-head">Full Audio Recording Transcript</div>
                    <div class="lt-transcript-turns">
                        ${(_selectedTask.audio && _selectedTask.audio.turns || []).map((t, idx) => `
                            <div class="lt-turn-row">
                                <div class="lt-turn-header">
                                    <span class="lt-turn-speaker">${_esc(t.speaker)}:</span>
                                    <button type="button" class="lt-audio-btn-sm" data-play-turn="${idx}">▶ Replay</button>
                                </div>
                                <span class="lt-turn-text">${_esc(t.text)}</span>
                                ${_showEnglishTranslations && t.textEn ? `
                                    <div class="lt-turn-translation">${_esc(t.textEn)}</div>
                                ` : ''}
                            </div>
                        `).join('')}
                    </div>
                </div>

                <!-- Questions Deep Dive Review -->
                <div class="ls-review-section">
                    <h3 class="ls-review-header">Detailed Question Breakdown</h3>
                    ${questions.map((q, idx) => {
                        const userAns = _userAnswers[q.id];
                        const isCorrect = userAns === q.correct;
                        const correctLabel = q.options ? q.options[q.correct] : ((_loadedLang === 'hu') ? ['Igaz', 'Hamis', 'Nincs említve'][q.correct] : ['Verdadero', 'Falso', 'No se menciona'][q.correct]);
                        const userLabel = userAns != null
                            ? (q.options ? q.options[userAns] : ((_loadedLang === 'hu') ? ['Igaz', 'Hamis', 'Nincs említve'][userAns] : ['Verdadero', 'Falso', 'No se menciona'][userAns]))
                            : 'No answer';

                        return `
                            <div class="lt-question-card ${isCorrect ? 'lt-card-correct' : 'lt-card-wrong'}">
                                <div class="lt-review-card-head">
                                    <span class="lt-q-num">Question ${idx + 1}</span>
                                    <span class="lt-badge ${isCorrect ? 'lt-badge-correct' : 'lt-badge-wrong'}">
                                        ${isCorrect ? '✓ Correct' : '✗ Incorrect'}
                                    </span>
                                </div>
                                <div class="lt-q-text">${_esc(q.question || q.statement)}</div>

                                <div class="lt-review-answers-box">
                                    <div class="lt-ans-row">
                                        <span class="lt-ans-lbl">Your Answer:</span>
                                        <span class="lt-ans-val ${isCorrect ? 'lt-ans-correct' : 'lt-ans-wrong'}">${_esc(userLabel)}</span>
                                    </div>
                                    ${!isCorrect ? `
                                        <div class="lt-ans-row">
                                            <span class="lt-ans-lbl">Correct Answer:</span>
                                            <span class="lt-ans-val lt-ans-correct">${_esc(correctLabel)}</span>
                                        </div>
                                    ` : ''}
                                </div>

                                ${q.evidence ? `
                                    <div class="lt-evidence-box">
                                        <span class="lt-evidence-title">Spoken Evidence in Audio:</span>
                                        <blockquote class="lt-evidence-quote">“${_esc(q.evidence)}”</blockquote>
                                    </div>
                                ` : ''}

                                ${q.explanation ? `
                                    <div class="lt-explanation-box">
                                        <strong>Why this is correct:</strong> ${_esc(q.explanation)}
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>

                <div class="sp-action-row" style="margin-top:28px;">
                    <button type="button" class="btn btn-secondary" data-action="retake-task">↺ Retake Passage</button>
                    <button type="button" class="btn btn-primary" data-action="all-tasks">Choose Another Passage →</button>
                </div>
            </div>
        `;

        mount.querySelector('[data-action="toggle-transcript"]').addEventListener('click', () => {
            _showTranscriptInResults = !_showTranscriptInResults;
            _renderResults(mount);
        });

        mount.querySelector('[data-action="toggle-translations"]').addEventListener('click', () => {
            _showEnglishTranslations = !_showEnglishTranslations;
            _renderResults(mount);
        });

        mount.querySelectorAll('[data-play-turn]').forEach(btn => {
            btn.addEventListener('click', () => {
                const turnIdx = parseInt(btn.getAttribute('data-play-turn'), 10);
                _playSingleTurn(turnIdx);
            });
        });

        mount.querySelector('[data-action="retake-task"]').addEventListener('click', () => {
            _userAnswers = {};
            _phase = PHASE.PREVIEW;
            _renderComprehension(mount);
        });

        mount.querySelector('[data-action="all-tasks"]').addEventListener('click', () => {
            _userAnswers = {};
            _selectedTask = null;
            _phase = PHASE.PICKER;
            _renderComprehension(mount);
        });
    }

    // ----------------------------------------
    // PUBLIC API
    // ----------------------------------------
    function stop() {
        _stopAudio();
        if (typeof ListeningDriller !== 'undefined' && typeof ListeningDriller.stop === 'function') {
            try { ListeningDriller.stop(); } catch (e) {}
        }
    }

    async function render(container, options = {}) {
        _container = container;

        if (options && (options.autoStart || options.count)) {
            _activeStudioTab = STUDIO_TAB.DECODING;
            _subOptions = options;
        } else if (options && options.activeTab) {
            _activeStudioTab = (options.activeTab === 'decoding' || options.activeTab === 'drills')
                ? STUDIO_TAB.DECODING
                : STUDIO_TAB.COMPREHENSION;
            _subOptions = options;
        }

        _renderStudioShell();
    }

    return {
        render,
        stop,
        _loadTasks,
        _getFallbackTasks,
        STUDIO_TAB,
        PHASE
    };
})();

if (typeof window !== 'undefined') {
    window.ListeningStudio = ListeningStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ListeningStudio;
}
