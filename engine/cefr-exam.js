// ============================================
// CEFR EXAM PRACTICE ENGINE (DELE B1 / ECL B1)
// ============================================
// Official CEFR exam preparation module for Workshop:
//   1. Targeted Task-by-Task practice (Entrenamiento por Tareas):
//      - Comprensión de lectura (Matching notices, deep article MCQs, gapped text, cloze)
//      - Comprensión auditiva (Authentic 2-pass protocol with 30s preview, multi-voice TTS, transcripts)
//      - Expresión e interacción escritas (Live word-counter, autosaved drafts, CEFR analytical rubric)
//      - Expresión e interacción orales (Audio visualizer, real-time STT streaming, oral evaluation)
//   2. Exam Strategy Guide & Discourse Connectors
//   3. Full 4-Skill Mock Exam Simulation (Phase 2)
//   4. Comprehensive Grade History & Score Matrix
//
// Strictly zero emojis across all UI chrome, tabs, badges, and exercises.

const CefrExam = (function () {
    'use strict';

    function createModule(config) {
        const _id = config.id;
        const _dataFile = config.dataFile;
        const _storageKey = `parlour_cefr_v1_${_id}`;

        let _data = null;
        let _container = null;

        let _state = {
            tab: 'tasks',           // 'tasks' | 'strategies' | 'mocks' | 'history'
            activeSkill: 'reading', // 'reading' | 'listening' | 'writing' | 'speaking'
            activeTareaId: null,

            // Reading state
            readingAnswers: {},     // itemId -> selectedValue
            readingSubmitted: false,

            // Listening state
            listeningAnswers: {},
            listeningSubmitted: false,
            listeningPreviewTimer: null,
            listeningPreviewCountdown: 30,
            listeningPass: 1,       // 1 or 2
            listeningPlaying: false,
            listeningIntermission: false,
            listeningIntermissionCountdown: 15,
            listeningIntermissionTimer: null,
            listeningCurrentTurn: -1,
            listeningSpeed: 1.0,
            listeningTranscriptRevealed: false,

            // Writing state
            writingActiveOption: 'A',
            writingDraftText: '',
            writingResult: null,

            // Speaking state
            speakingPrepTimer: null,
            speakingPrepCountdown: 60,
            speakingIsRecording: false,
            speakingMediaRecorder: null,
            speakingAudioChunks: [],
            speakingAudioBlobUrl: null,
            speakingTranscriptText: '',
            speakingRecognition: null,
            speakingAudioContext: null,
            speakingAnalyser: null,
            speakingAnimFrame: null,
            speakingResult: null
        };

        function _esc(str) {
            if (typeof UI !== 'undefined' && UI.escape) return UI.escape(String(str || ''));
            const d = document.createElement('div');
            d.textContent = String(str || '');
            return d.innerHTML;
        }

        function _loadProgress() {
            try {
                return JSON.parse(localStorage.getItem(_storageKey) || '{}');
            } catch (e) {
                return {};
            }
        }

        function _saveTaskScore(skillId, tareaId, score, maxScore) {
            try {
                const prog = _loadProgress();
                prog.scores = prog.scores || {};
                prog.scores[skillId] = prog.scores[skillId] || {};
                const prev = prog.scores[skillId][tareaId];
                if (!prev || score >= prev.score) {
                    prog.scores[skillId][tareaId] = {
                        score: score,
                        maxScore: maxScore,
                        pct: Math.round((score / maxScore) * 100),
                        date: new Date().toISOString()
                    };
                }
                localStorage.setItem(_storageKey, JSON.stringify(prog));
            } catch (e) {}
        }

        function _draftKey(tareaId) {
            return `parlour_cefr_draft_${_id}_${tareaId}`;
        }

        function _loadDraft(tareaId) {
            try {
                return localStorage.getItem(_draftKey(tareaId)) || '';
            } catch (e) {
                return '';
            }
        }

        function _saveDraft(tareaId, text) {
            try {
                localStorage.setItem(_draftKey(tareaId), text);
            } catch (e) {}
        }

        async function _loadData() {
            if (_data) return _data;
            try {
                const lang = typeof Lang !== 'undefined' ? Lang.code() : 'es';
                let res = await fetch(Lang.content(_dataFile));
                if (!res.ok && lang === 'es-latam') {
                    res = await fetch('content/es-es/' + _dataFile);
                }
                _data = res.ok ? await res.json() : null;
            } catch (e) {
                _data = null;
            }
            return _data;
        }

        // ========================================
        // AUDIO & LISTENING RUNNER HELPERS
        // ========================================
        function _stopListeningTimers() {
            if (_state.listeningPreviewTimer) {
                clearInterval(_state.listeningPreviewTimer);
                _state.listeningPreviewTimer = null;
            }
            if (_state.listeningIntermissionTimer) {
                clearInterval(_state.listeningIntermissionTimer);
                _state.listeningIntermissionTimer = null;
            }
            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.stop) {
                ParlourTTS.stop();
            } else if (typeof window !== 'undefined' && window.speechSynthesis) {
                window.speechSynthesis.cancel();
            }
            _state.listeningPlaying = false;
        }

        function _playTurnSequence(turns, turnIndex, onComplete) {
            if (!_state.listeningPlaying || turnIndex >= turns.length) {
                _state.listeningPlaying = false;
                _state.listeningCurrentTurn = -1;
                if (typeof onComplete === 'function') onComplete();
                return;
            }

            _state.listeningCurrentTurn = turnIndex;
            _updateListeningConsole();

            const turn = turns[turnIndex];
            const text = turn.text;
            const langCode = typeof Lang !== 'undefined' ? Lang.code() : 'es';
            const voiceGender = turn.gender || (turnIndex % 2 === 0 ? 'female' : 'male');

            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
                ParlourTTS.speak(text, {
                    lang: langCode,
                    gender: voiceGender,
                    rate: _state.listeningSpeed,
                    onEnd: () => {
                        setTimeout(() => {
                            if (_state.listeningPlaying) {
                                _playTurnSequence(turns, turnIndex + 1, onComplete);
                            }
                        }, 600);
                    }
                });
            } else if (typeof window !== 'undefined' && window.speechSynthesis) {
                const utter = new SpeechSynthesisUtterance(text);
                utter.lang = langCode.startsWith('hu') ? 'hu-HU' : 'es-ES';
                utter.rate = _state.listeningSpeed;
                utter.onend = () => {
                    setTimeout(() => {
                        if (_state.listeningPlaying) {
                            _playTurnSequence(turns, turnIndex + 1, onComplete);
                        }
                    }, 600);
                };
                utter.onerror = () => {
                    if (_state.listeningPlaying) {
                        _playTurnSequence(turns, turnIndex + 1, onComplete);
                    }
                };
                window.speechSynthesis.speak(utter);
            } else {
                setTimeout(() => {
                    if (_state.listeningPlaying) {
                        _playTurnSequence(turns, turnIndex + 1, onComplete);
                    }
                }, 2000);
            }
        }

        function _startAudioPass(passNum, turns) {
            _stopListeningTimers();
            _state.listeningPass = passNum;
            _state.listeningPlaying = true;
            _state.listeningIntermission = false;
            _updateListeningConsole();

            _playTurnSequence(turns, 0, () => {
                _state.listeningPlaying = false;
                _state.listeningCurrentTurn = -1;

                if (passNum === 1) {
                    _startListeningIntermission(turns);
                } else {
                    _updateListeningConsole();
                }
            });
        }

        function _startListeningIntermission(turns) {
            _state.listeningIntermission = true;
            _state.listeningIntermissionCountdown = 15;
            _updateListeningConsole();

            _state.listeningIntermissionTimer = setInterval(() => {
                _state.listeningIntermissionCountdown--;
                if (_state.listeningIntermissionCountdown <= 0) {
                    clearInterval(_state.listeningIntermissionTimer);
                    _state.listeningIntermissionTimer = null;
                    _state.listeningIntermission = false;
                    _startAudioPass(2, turns);
                } else {
                    _updateListeningConsole();
                }
            }, 1000);
        }

        function _updateListeningConsole() {
            const el = document.getElementById('cefr-audio-console');
            if (!el) return;
            const tarea = _getCurrentTarea();
            if (!tarea || !tarea.audio || !tarea.audio.turns) return;

            const turns = tarea.audio.turns;
            let statusText = '';
            let subText = '';
            let btnHtml = '';

            if (_state.listeningPlaying) {
                const turn = turns[_state.listeningCurrentTurn];
                statusText = `Pase ${_state.listeningPass} de 2: Reproduciendo audio`;
                subText = turn ? `Voz: ${turn.speaker}` : 'Escuchando con atención...';
                btnHtml = `
                    <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-pause">Detener audio</button>
                    <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                `;
            } else if (_state.listeningIntermission) {
                statusText = 'Pausa entre audiciones';
                subText = `La segunda audición comenzará en ${_state.listeningIntermissionCountdown} segundos. Revisa tus opciones.`;
                btnHtml = `
                    <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="skip-intermission">Comenzar segunda audición</button>
                `;
            } else if (_state.listeningPass === 2 && !_state.listeningPlaying) {
                statusText = 'Audición completada';
                subText = 'Has escuchado los dos pases oficiales. Selecciona tus respuestas y comprueba la tarea.';
                btnHtml = `
                    <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="replay-pass-2">Repetir segundo pase</button>
                    <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                `;
            } else {
                statusText = `Pase ${_state.listeningPass} de 2 preparado`;
                subText = 'Pulsa reproducir cuando estés listo.';
                btnHtml = `
                    <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="audio-play">Reproducir pase ${_state.listeningPass}</button>
                    <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                `;
            }

            el.innerHTML = `
                <div class="cefr-audio-status-wrap">
                    <span class="cefr-audio-status-label">${_esc(statusText)}</span>
                    <span class="cefr-audio-status-sub">${_esc(subText)}</span>
                </div>
                <div class="cefr-audio-controls">
                    ${btnHtml}
                </div>
            `;

            const playBtn = el.querySelector('[data-action="audio-play"]');
            if (playBtn) playBtn.addEventListener('click', () => _startAudioPass(_state.listeningPass, turns));

            const pauseBtn = el.querySelector('[data-action="audio-pause"]');
            if (pauseBtn) pauseBtn.addEventListener('click', () => { _stopListeningTimers(); _updateListeningConsole(); });

            const skipBtn = el.querySelector('[data-action="skip-intermission"]');
            if (skipBtn) skipBtn.addEventListener('click', () => {
                _stopListeningTimers();
                _startAudioPass(2, turns);
            });

            const replayBtn = el.querySelector('[data-action="replay-pass-2"]');
            if (replayBtn) replayBtn.addEventListener('click', () => _startAudioPass(2, turns));

            const speedBtn = el.querySelector('[data-action="audio-speed"]');
            if (speedBtn) {
                speedBtn.addEventListener('click', () => {
                    _state.listeningSpeed = (_state.listeningSpeed === 1.0) ? 0.85 : 1.0;
                    _updateListeningConsole();
                });
            }
        }

        // ========================================
        // SPEAKING RUNNER HELPERS (MIC & STT)
        // ========================================
        function _stopSpeakingStreams() {
            if (_state.speakingPrepTimer) {
                clearInterval(_state.speakingPrepTimer);
                _state.speakingPrepTimer = null;
            }
            if (_state.speakingMediaRecorder && _state.speakingIsRecording) {
                try { _state.speakingMediaRecorder.stop(); } catch (e) {}
            }
            if (_state.speakingRecognition) {
                try { _state.speakingRecognition.stop(); } catch (e) {}
            }
            if (_state.speakingAudioContext) {
                try { _state.speakingAudioContext.close(); } catch (e) {}
                _state.speakingAudioContext = null;
            }
            if (_state.speakingAnimFrame) {
                cancelAnimationFrame(_state.speakingAnimFrame);
                _state.speakingAnimFrame = null;
            }
            _state.speakingIsRecording = false;
        }

        async function _startSpeakingRecording() {
            _state.speakingAudioChunks = [];
            _state.speakingTranscriptText = '';

            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                _state.speakingMediaRecorder = new MediaRecorder(stream);

                _state.speakingMediaRecorder.ondataavailable = (e) => {
                    if (e.data.size > 0) _state.speakingAudioChunks.push(e.data);
                };

                _state.speakingMediaRecorder.onstop = () => {
                    const blob = new Blob(_state.speakingAudioChunks, { type: 'audio/webm' });
                    _state.speakingAudioBlobUrl = URL.createObjectURL(blob);
                    stream.getTracks().forEach(track => track.stop());
                    _renderActiveTarea();
                };

                _state.speakingMediaRecorder.start();
                _state.speakingIsRecording = true;

                // Speech recognition setup
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                if (SpeechRecognition) {
                    _state.speakingRecognition = new SpeechRecognition();
                    _state.speakingRecognition.continuous = true;
                    _state.speakingRecognition.interimResults = true;
                    _state.speakingRecognition.lang = (typeof Lang !== 'undefined' && Lang.code().startsWith('hu')) ? 'hu-HU' : 'es-ES';

                    _state.speakingRecognition.onresult = (event) => {
                        let finalStr = '';
                        for (let i = 0; i < event.results.length; ++i) {
                            finalStr += event.results[i][0].transcript;
                        }
                        _state.speakingTranscriptText = finalStr;
                        const transcriptBox = document.getElementById('cefr-speaking-transcript-input');
                        if (transcriptBox) transcriptBox.value = finalStr;
                    };

                    _state.speakingRecognition.onerror = () => {};
                    _state.speakingRecognition.start();
                }

                _updateSpeakingUI();
            } catch (err) {
                console.warn('Microphone access unavailable or denied:', err);
                alert('No se pudo acceder al micrófono. Puedes redactar tu respuesta oral en el campo de texto.');
            }
        }

        function _stopSpeakingRecording() {
            if (_state.speakingMediaRecorder && _state.speakingIsRecording) {
                _state.speakingMediaRecorder.stop();
            }
            if (_state.speakingRecognition) {
                try { _state.speakingRecognition.stop(); } catch (e) {}
            }
            _state.speakingIsRecording = false;
            _updateSpeakingUI();
        }

        function _updateSpeakingUI() {
            const btn = document.getElementById('cefr-mic-toggle-btn');
            const statusEl = document.getElementById('cefr-mic-status-label');
            if (!btn || !statusEl) return;

            if (_state.speakingIsRecording) {
                btn.textContent = 'Detener grabación';
                btn.className = 'btn btn-secondary cefr-record-btn is-recording';
                statusEl.textContent = 'Grabando voz... Habla con naturalidad.';
            } else {
                btn.textContent = 'Iniciar grabación de voz';
                btn.className = 'btn btn-primary cefr-record-btn';
                statusEl.textContent = 'Micrófono listo. Pulsa para comenzar tu producción oral.';
            }
        }

        // ========================================
        // EVALUATION ENGINES
        // ========================================
        function _countWords(str) {
            if (!str || typeof str !== 'string') return 0;
            const m = str.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu);
            return m ? m.length : 0;
        }

        function _evaluateWritingText(text, tarea) {
            const wordCount = _countWords(text);
            const minWords = tarea.minWords || 100;
            const maxWords = tarea.maxWords || 130;

            // Length score (up to 7 pts)
            let lengthScore = 7;
            if (wordCount < minWords * 0.7) lengthScore = 3;
            else if (wordCount < minWords) lengthScore = 5;
            else if (wordCount > maxWords * 1.3) lengthScore = 5;

            // Connectors & cohesion (up to 6 pts)
            const b1Connectors = [
                'sin embargo', 'por lo tanto', 'en mi opinión', 'por un lado', 'por otro lado',
                'en cuanto a', 'además', 'me encantaría', 'gracias por', 'un abrazo', 'aunque',
                'de modo que', 'así que', 'dado que', 'es importante que', 'no creo que',
                'véleményem szerint', 'egyrészt', 'másrészt', 'ezért', 'ugyanakkor', 'bár'
            ];
            const lowerText = text.toLowerCase();
            const foundConnectors = b1Connectors.filter(c => lowerText.includes(c));
            const cohesionScore = Math.min(6, Math.max(2, foundConnectors.length * 2));

            // Punctuation & paragraphs (up to 6 pts)
            const hasParagraphs = text.includes('\n');
            const hasPunctuation = /[.!?¿¡]/.test(text);
            const structScore = (hasParagraphs && hasPunctuation) ? 6 : 4;

            // Keyword compliance (up to 6 pts)
            const targetKeywords = tarea.targetKeywords || [];
            const matchedKw = targetKeywords.filter(kw => lowerText.includes(kw.toLowerCase()));
            const kwScore = Math.min(6, Math.max(2, matchedKw.length * 2));

            const totalScore = Math.min(25, lengthScore + cohesionScore + structScore + kwScore);

            return {
                totalScore: totalScore,
                maxScore: 25,
                wordCount: wordCount,
                minWords: minWords,
                maxWords: maxWords,
                foundConnectors: foundConnectors,
                matchedKeywords: matchedKw,
                criteria: {
                    adecuacion: lengthScore,
                    coherencia: cohesionScore,
                    estructura: structScore,
                    leves: kwScore
                }
            };
        }

        function _evaluateSpeakingText(text, tarea) {
            const wordCount = _countWords(text);
            const hasAudio = !!_state.speakingAudioBlobUrl;

            let lengthScore = (wordCount >= 60 || hasAudio) ? 7 : (wordCount >= 30 ? 4 : 2);
            const lowerText = text.toLowerCase();
            const b1Connectors = ['en primer lugar', 'por ejemplo', 'en mi opinión', 'además', 'por eso', 'véleményem szerint', 'szerintem'];
            const foundConnectors = b1Connectors.filter(c => lowerText.includes(c));
            const cohesionScore = Math.min(6, Math.max(2, foundConnectors.length * 2));

            const totalScore = Math.min(25, lengthScore + cohesionScore + (hasAudio ? 6 : 3) + 6);

            return {
                totalScore: totalScore,
                maxScore: 25,
                wordCount: wordCount,
                hasAudio: hasAudio,
                foundConnectors: foundConnectors
            };
        }

        // ========================================
        // NAVIGATION & RENDER
        // ========================================
        function _getCurrentSkill() {
            if (!_data || !_data.skills) return null;
            return _data.skills[_state.activeSkill] || null;
        }

        function _getCurrentTarea() {
            const skill = _getCurrentSkill();
            if (!skill || !skill.tareas) return null;
            return skill.tareas.find(t => t.id === _state.activeTareaId) || null;
        }

        function _renderTabs() {
            const tabs = [
                { id: 'tasks', label: (_id.includes('hu')) ? 'Hivatalos feladattípusok' : 'Tareas oficiales' },
                { id: 'strategies', label: (_id.includes('hu')) ? 'Guía és stratégiák' : 'Guía y estrategias' },
                { id: 'mocks', label: (_id.includes('hu')) ? 'Teljes próbavizsga' : 'Simulacro completo' },
                { id: 'history', label: (_id.includes('hu')) ? 'Eredmények' : 'Mis resultados' }
            ];

            return `
                <div class="hce-tabs cefr-tabs" role="tablist">
                    ${tabs.map(t => `
                        <button type="button" class="hce-tab ${_state.tab === t.id ? 'is-active' : ''}" data-cefr-tab="${t.id}" role="tab" aria-selected="${_state.tab === t.id}">
                            ${_esc(t.label)}
                        </button>
                    `).join('')}
                </div>
            `;
        }

        function _renderTasksTab() {
            const skillOrder = ['reading', 'listening', 'writing', 'speaking'];
            const skillLabels = {
                reading: (_id.includes('hu')) ? 'Olvasásértés' : 'Comprensión de lectura',
                listening: (_id.includes('hu')) ? 'Hallásértés' : 'Comprensión auditiva',
                writing: (_id.includes('hu')) ? 'Írásbeli kommunikáció' : 'Expresión escrita',
                speaking: (_id.includes('hu')) ? 'Szóbeli kommunikáció' : 'Expresión oral'
            };

            const prog = _loadProgress().scores || {};

            return `
                <div class="cefr-skills-nav" role="tablist">
                    ${skillOrder.map(s => {
                        const skillData = _data.skills[s];
                        if (!skillData) return '';
                        const taskCount = (skillData.tareas || []).length;
                        return `
                            <button type="button" class="cefr-skill-chip ${_state.activeSkill === s ? 'is-active' : ''}" data-cefr-skill="${s}">
                                <span class="cefr-chip-title">${_esc(skillLabels[s] || skillData.name)}</span>
                                <span class="cefr-chip-count">${taskCount} ${_id.includes('hu') ? 'feladat' : 'tareas'}</span>
                            </button>
                        `;
                    }).join('')}
                </div>

                <div class="cefr-tasks-list">
                    ${_renderTareasCards(prog)}
                </div>
            `;
        }

        function _renderTareasCards(prog) {
            const skill = _getCurrentSkill();
            if (!skill || !skill.tareas) return '<p class="cefr-empty">No hay tareas disponibles.</p>';

            const skillProg = prog[_state.activeSkill] || {};

            return skill.tareas.map(t => {
                const recorded = skillProg[t.id];
                const badgeHtml = recorded
                    ? `<span class="cefr-status-pill is-completed">${recorded.pct}% (${recorded.score}/${recorded.maxScore})</span>`
                    : `<span class="cefr-status-pill is-pending">${_id.includes('hu') ? 'Nincs kitöltve' : 'Pendiente'}</span>`;

                return `
                    <div class="cefr-task-card" data-cefr-open-tarea="${_esc(t.id)}">
                        <div class="cefr-task-card-header">
                            <span class="cefr-task-pill">${_esc(t.title || `Tarea ${t.tareaNum}`)}</span>
                            ${badgeHtml}
                        </div>
                        <div class="cefr-task-card-body">
                            <p class="cefr-task-inst">${_esc(t.instructions || t.prompt || '')}</p>
                        </div>
                        <div class="cefr-task-card-footer">
                            <span class="cefr-task-meta">${_id.includes('hu') ? 'Kattints a gyakorlás megkezdéséhez' : 'Comenzar práctica'}</span>
                            <span class="cefr-task-arrow geo-triangle" aria-hidden="true"></span>
                        </div>
                    </div>
                `;
            }).join('');
        }

        // ========================================
        // TAREA RUNNER VIEWS
        // ========================================
        function _renderActiveTarea() {
            const tarea = _getCurrentTarea();
            if (!tarea) return '';

            let contentHtml = '';
            if (_state.activeSkill === 'reading') {
                contentHtml = _renderReadingTarea(tarea);
            } else if (_state.activeSkill === 'listening') {
                contentHtml = _renderListeningTarea(tarea);
            } else if (_state.activeSkill === 'writing') {
                contentHtml = _renderWritingTarea(tarea);
            } else if (_state.activeSkill === 'speaking') {
                contentHtml = _renderSpeakingTarea(tarea);
            }

            return `
                <div class="cefr-runner-container">
                    <div class="cefr-runner-topbar">
                        <button type="button" class="btn btn-secondary cefr-back-btn" data-action="back-to-tasks">
                            ← ${_id.includes('hu') ? 'Vissza a feladatokhoz' : 'Volver a tareas'}
                        </button>
                        <h3 class="cefr-runner-title">${_esc(tarea.title)}</h3>
                    </div>
                    ${contentHtml}
                </div>
            `;
        }

        // 1. Reading Tarea View
        function _renderReadingTarea(tarea) {
            let leftPaneHtml = '';
            let rightPaneHtml = '';

            if (tarea.type === 'matching-notices') {
                leftPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Hirdetések' : 'Tablón de anuncios (A-J)'}</h4>
                    </div>
                    <div class="cefr-notices-grid">
                        ${(tarea.notices || []).map(n => `
                            <div class="cefr-notice-card" id="notice-${_esc(n.id)}">
                                <div class="cefr-notice-tag">[${_esc(n.letter)}] ${_esc(n.title)}</div>
                                <p class="cefr-notice-text">${_esc(n.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                rightPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Személyek és igények' : 'Personas y necesidades (1-6)'}</h4>
                    </div>
                    <div class="cefr-matching-items">
                        ${(tarea.people || []).map((p, idx) => {
                            const selected = _state.readingAnswers[p.id] || '';
                            const isCorrect = _state.readingSubmitted && selected === p.correctNoticeId;
                            const isWrong = _state.readingSubmitted && selected !== p.correctNoticeId;

                            return `
                                <div class="cefr-matching-item ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-matching-prompt">
                                        <strong>${_esc(p.name)}:</strong> ${_esc(p.text)}
                                    </div>
                                    <div class="cefr-matching-select-wrap">
                                        <select class="cefr-select" data-match-qid="${_esc(p.id)}" ${_state.readingSubmitted ? 'disabled' : ''}>
                                            <option value="">-- ${_id.includes('hu') ? 'Válassz hirdetést' : 'Elige anuncio'} --</option>
                                            ${(tarea.notices || []).map(n => `
                                                <option value="${_esc(n.id)}" ${selected === n.id ? 'selected' : ''}>
                                                    [${_esc(n.letter)}] ${_esc(n.title)}
                                                </option>
                                            `).join('')}
                                        </select>
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'reading-mc') {
                leftPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Olvasandó szöveg' : 'Texto de lectura'}</h4>
                    </div>
                    <div class="cefr-passage-content">
                        ${(tarea.passage || '').split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}
                    </div>
                `;

                rightPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Kérdések' : 'Preguntas de comprensión'}</h4>
                    </div>
                    <div class="cefr-questions-list">
                        ${(tarea.questions || []).map((q, qIdx) => {
                            const selectedOpt = _state.readingAnswers[q.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && selectedOpt === q.correct;
                            const isWrong = isSubmitted && selectedOpt !== q.correct && selectedOpt !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">${_esc(q.question)}</div>
                                    <div class="cefr-options-list">
                                        ${(q.options || []).map((opt, optIdx) => {
                                            const optChecked = selectedOpt === optIdx;
                                            return `
                                                <button type="button" class="cefr-opt-btn ${optChecked ? 'is-selected' : ''} ${isSubmitted && optIdx === q.correct ? 'is-correct-target' : ''}" data-ans-qid="${_esc(q.id)}" data-ans-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                                    <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                                    <span class="cefr-opt-text">${_esc(opt)}</span>
                                                </button>
                                            `;
                                        }).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${_id.includes('hu') ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(q.explanation || '')}
                                            <div class="cefr-evidence-quote"><em>"${_esc(q.evidence || '')}"</em></div>
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'person-matching') {
                leftPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Személyes vélemények' : 'Testimonios personales'}</h4>
                    </div>
                    <div class="cefr-people-cards">
                        ${(tarea.people || []).map(p => `
                            <div class="cefr-person-card">
                                <strong>[${_esc(p.letter)}] ${_esc(p.name)}</strong>
                                <p>${_esc(p.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                rightPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Állítások' : 'Afirmaciones'}</h4>
                    </div>
                    <div class="cefr-questions-list">
                        ${(tarea.statements || []).map(s => {
                            const chosen = _state.readingAnswers[s.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === s.correctPerson;
                            const isWrong = isSubmitted && chosen !== s.correctPerson;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">${_esc(s.text)}</div>
                                    <div class="cefr-btn-trio">
                                        ${['A', 'B', 'C'].map(letter => `
                                            <button type="button" class="cefr-opt-btn cefr-btn-compact ${chosen === letter ? 'is-selected' : ''}" data-stmt-qid="${_esc(s.id)}" data-stmt-letter="${letter}" ${isSubmitted ? 'disabled' : ''}>
                                                ${letter}
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            ${_esc(s.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'gapped-text') {
                leftPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Szöveg' : 'Texto principal'}</h4>
                    </div>
                    <div class="cefr-passage-content">
                        ${(tarea.passage || '').split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}
                    </div>
                `;

                rightPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Hiányzó mondatok' : 'Opciones para completar los huecos'}</h4>
                    </div>
                    <div class="cefr-gaps-options-pool">
                        ${(tarea.options || []).map(o => `
                            <div class="cefr-gap-pool-item">
                                <strong>[${_esc(o.letter)}]</strong> ${_esc(o.text)}
                            </div>
                        `).join('')}
                    </div>
                    <div class="cefr-gaps-selectors">
                        ${(tarea.gaps || []).map(g => {
                            const chosen = _state.readingAnswers[g.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === g.correct;
                            const isWrong = isSubmitted && chosen !== g.correct;

                            return `
                                <div class="cefr-gap-row ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <span class="cefr-gap-label">Hueco [___${g.num}___]:</span>
                                    <select class="cefr-select" data-gap-qid="${_esc(g.id)}" ${isSubmitted ? 'disabled' : ''}>
                                        <option value="">-- Selecciona letra --</option>
                                        ${(tarea.options || []).map(o => `
                                            <option value="${_esc(o.letter)}" ${chosen === o.letter ? 'selected' : ''}>
                                                [${_esc(o.letter)}] ${_esc(o.text.substring(0, 45))}...
                                            </option>
                                        `).join('')}
                                    </select>
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'cloze-mc') {
                leftPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Szöveg' : 'Texto con huecos gramaticales'}</h4>
                    </div>
                    <div class="cefr-passage-content">
                        ${(tarea.passage || '').split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}
                    </div>
                `;

                rightPaneHtml = `
                    <div class="cefr-pane-header">
                        <h4>${_id.includes('hu') ? 'Opciók' : 'Opciones de gramática y léxico'}</h4>
                    </div>
                    <div class="cefr-questions-list">
                        ${(tarea.items || []).map(item => {
                            const chosen = _state.readingAnswers[item.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === item.correct;
                            const isWrong = isSubmitted && chosen !== item.correct && chosen !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">Hueco [___${item.num}___]</div>
                                    <div class="cefr-options-list">
                                        ${(item.options || []).map((opt, optIdx) => `
                                            <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === item.correct ? 'is-correct-target' : ''}" data-cloze-qid="${_esc(item.id)}" data-cloze-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                                <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                                <span class="cefr-opt-text">${_esc(opt)}</span>
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            ${_esc(item.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            }

            return `
                <div class="cefr-dual-pane">
                    <div class="cefr-pane cefr-pane-left">
                        ${leftPaneHtml}
                    </div>
                    <div class="cefr-pane cefr-pane-right">
                        ${rightPaneHtml}
                        <div class="cefr-action-bar">
                            ${!_state.readingSubmitted ? `
                                <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-reading">
                                    ${_id.includes('hu') ? 'Feladat ellenőrzése' : 'Comprobar tarea'}
                                </button>
                            ` : `
                                <button type="button" class="btn btn-secondary cefr-reset-btn" data-action="reset-reading">
                                    ${_id.includes('hu') ? 'Újrapróbálás' : 'Repetir tarea'}
                                </button>
                            `}
                        </div>
                    </div>
                </div>
            `;
        }

        // 2. Listening Tarea View
        function _renderListeningTarea(tarea) {
            return `
                <div class="cefr-listening-wrapper">
                    <div id="cefr-audio-console" class="cefr-audio-console">
                        <!-- Populated by _updateListeningConsole() -->
                    </div>

                    <div class="cefr-listening-questions">
                        ${(tarea.questions || []).map((q, qIdx) => {
                            const chosen = _state.listeningAnswers[q.id];
                            const isSubmitted = _state.listeningSubmitted;
                            const isCorrect = isSubmitted && chosen === q.correct;
                            const isWrong = isSubmitted && chosen !== q.correct && chosen !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">${_esc(q.question)}</div>
                                    <div class="cefr-options-list">
                                        ${(q.options || []).map((opt, optIdx) => `
                                            <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === q.correct ? 'is-correct-target' : ''}" data-listen-qid="${_esc(q.id)}" data-listen-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                                <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                                <span class="cefr-opt-text">${_esc(opt)}</span>
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${_id.includes('hu') ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(q.explanation || '')}
                                            <div class="cefr-evidence-quote"><em>"${_esc(q.evidence || '')}"</em></div>
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>

                    ${_state.listeningSubmitted && tarea.audio && tarea.audio.turns ? `
                        <div class="cefr-transcript-section">
                            <div class="cefr-transcript-header">
                                <h4>${_id.includes('hu') ? 'Teljes hanganyag szövege' : 'Transcripción completa de la audición'}</h4>
                            </div>
                            <div class="cefr-transcript-turns">
                                ${tarea.audio.turns.map(t => `
                                    <div class="cefr-transcript-turn">
                                        <strong>${_esc(t.speaker)}:</strong> ${_esc(t.text)}
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : ''}

                    <div class="cefr-action-bar">
                        ${!_state.listeningSubmitted ? `
                            <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-listening">
                                ${_id.includes('hu') ? 'Válaszok ellenőrzése' : 'Comprobar respuestas'}
                            </button>
                        ` : `
                            <button type="button" class="btn btn-secondary cefr-reset-btn" data-action="reset-listening">
                                ${_id.includes('hu') ? 'Újrahallgatás' : 'Repetir audición'}
                            </button>
                        `}
                    </div>
                </div>
            `;
        }

        // 3. Writing Tarea View
        function _renderWritingTarea(tarea) {
            let activePrompt = tarea.prompt;
            let minWords = tarea.minWords || 100;
            let maxWords = tarea.maxWords || 120;

            let optionSwitcherHtml = '';
            if (tarea.options && tarea.options.length > 0) {
                const opt = tarea.options.find(o => o.optionLetter === _state.writingActiveOption) || tarea.options[0];
                activePrompt = opt.prompt;
                minWords = opt.minWords || 130;
                maxWords = opt.maxWords || 150;

                optionSwitcherHtml = `
                    <div class="cefr-option-switcher">
                        <span class="cefr-option-label">${_id.includes('hu') ? 'Válassz opciót' : 'Elige opción de redacción'}:</span>
                        ${tarea.options.map(o => `
                            <button type="button" class="btn btn-secondary cefr-opt-toggle ${o.optionLetter === _state.writingActiveOption ? 'is-active' : ''}" data-writing-option="${_esc(o.optionLetter)}">
                                ${_esc(o.title)}
                            </button>
                        `).join('')}
                    </div>
                `;
            }

            const currentWords = _countWords(_state.writingDraftText);
            const isWordCountGood = currentWords >= minWords && currentWords <= maxWords;

            return `
                <div class="cefr-writing-wrapper">
                    ${optionSwitcherHtml}

                    <div class="cefr-writing-prompt-card">
                        <div class="cefr-prompt-title">Instrucciones de la tarea:</div>
                        <div class="cefr-prompt-text">${_esc(activePrompt).split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}</div>
                    </div>

                    <div class="cefr-editor-container">
                        <div class="cefr-editor-toolbar">
                            <span class="cefr-word-counter ${isWordCountGood ? 'is-good' : (currentWords > maxWords ? 'is-over' : '')}">
                                Palabras: <strong>${currentWords}</strong> / ${minWords}–${maxWords}
                            </span>
                            <span class="cefr-draft-status">Borrador guardado automáticamente</span>
                        </div>
                        <textarea id="cefr-writing-textarea" class="cefr-textarea" placeholder="Escribe tu redacción aquí..." rows="12">${_esc(_state.writingDraftText)}</textarea>
                    </div>

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-writing">
                            ${_id.includes('hu') ? 'Fogalmazás értékelése' : 'Evaluar redacción (Rúbrica CEFR)'}
                        </button>
                    </div>

                    ${_state.writingResult ? `
                        <div class="cefr-writing-results-card">
                            <div class="cefr-res-header">
                                <h4>Informe de evaluación B1</h4>
                                <span class="cefr-score-badge">${_state.writingResult.totalScore} / 25 puntos</span>
                            </div>
                            <div class="cefr-rubric-breakdown">
                                <div class="cefr-rubric-item">
                                    <span>Adecuación y extensión (${_state.writingResult.wordCount} palabras):</span>
                                    <strong>${_state.writingResult.criteria.adecuacion} / 7 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>Coherencia y conectores (${_state.writingResult.foundConnectors.length} detectados):</span>
                                    <strong>${_state.writingResult.criteria.coherencia} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>Párrafos y estructuración:</span>
                                    <strong>${_state.writingResult.criteria.estructura} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>Puntos guía y riqueza léxica:</span>
                                    <strong>${_state.writingResult.criteria.leves} / 6 pts</strong>
                                </div>
                            </div>
                            ${_state.writingResult.foundConnectors.length > 0 ? `
                                <div class="cefr-detected-connectors">
                                    <span>Conectores B1 empleados:</span>
                                    <em>${_esc(_state.writingResult.foundConnectors.join(', '))}</em>
                                </div>
                            ` : ''}
                        </div>
                    ` : ''}
                </div>
            `;
        }

        // 4. Speaking Tarea View
        function _renderSpeakingTarea(tarea) {
            return `
                <div class="cefr-speaking-wrapper">
                    <div class="cefr-speaking-prompt-card">
                        <div class="cefr-prompt-title">${_esc(tarea.title)}</div>
                        <div class="cefr-prompt-text">${_esc(tarea.prompt).split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}</div>
                        ${tarea.bulletPoints ? `
                            <ul class="cefr-prompt-bullets">
                                ${tarea.bulletPoints.map(b => `<li>${_esc(b)}</li>`).join('')}
                            </ul>
                        ` : ''}
                    </div>

                    <div class="cefr-mic-console">
                        <div class="cefr-mic-status-wrap">
                            <span id="cefr-mic-status-label" class="cefr-mic-status-label">
                                Micrófono listo. Pulsa para comenzar tu producción oral.
                            </span>
                        </div>
                        <div class="cefr-mic-controls">
                            <button type="button" id="cefr-mic-toggle-btn" class="btn btn-primary cefr-record-btn" data-action="toggle-mic">
                                Iniciar grabación de voz
                            </button>
                        </div>
                    </div>

                    <div class="cefr-speaking-transcript-wrap">
                        <label for="cefr-speaking-transcript-input" class="cefr-transcript-label">
                            Transcripción de tu respuesta (puedes revisarla o editarla antes de evaluar):
                        </label>
                        <textarea id="cefr-speaking-transcript-input" class="cefr-textarea cefr-transcript-textarea" rows="5" placeholder="Tu voz se transcribirá aquí en tiempo real...">${_esc(_state.speakingTranscriptText)}</textarea>
                    </div>

                    ${_state.speakingAudioBlobUrl ? `
                        <div class="cefr-playback-card">
                            <span>Escucha tu grabación:</span>
                            <audio controls src="${_state.speakingAudioBlobUrl}" class="cefr-audio-player"></audio>
                        </div>
                    ` : ''}

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-speaking">
                            ${_id.includes('hu') ? 'Beszédkészség értékelése' : 'Evaluar expresión oral'}
                        </button>
                    </div>

                    ${_state.speakingResult ? `
                        <div class="cefr-speaking-results-card">
                            <div class="cefr-res-header">
                                <h4>Informe oral B1</h4>
                                <span class="cefr-score-badge">${_state.speakingResult.totalScore} / 25 puntos</span>
                            </div>
                            <p>Palabras producidas: <strong>${_state.speakingResult.wordCount}</strong></p>
                            <p>Conectores orales detectados: <em>${_esc(_state.speakingResult.foundConnectors.join(', ') || 'Ninguno detectado')}</em></p>
                        </div>
                    ` : ''}
                </div>
            `;
        }

        // Strategies Tab
        function _renderStrategiesTab() {
            if (!_data || !_data.strategies) return '<p class="cefr-empty">Guía no disponible.</p>';
            const s = _data.strategies;

            return `
                <div class="cefr-strategies-wrapper">
                    <h3 class="cefr-sec-title">${_esc(s.title || 'Guía oficial del examen')}</h3>
                    
                    <div class="cefr-strat-grid">
                        ${(s.structure || []).map(item => `
                            <div class="cefr-strat-card">
                                <h4>${_esc(item.prueba)}</h4>
                                <p>${_esc(item.tip)}</p>
                            </div>
                        `).join('')}
                    </div>

                    <div class="cefr-connectors-section">
                        <h4>Conectores y marcadores del discurso (Nivel B1)</h4>
                        <div class="cefr-connectors-grid">
                            ${(s.connectors || []).map(cat => `
                                <div class="cefr-connector-card">
                                    <div class="cefr-conn-cat">${_esc(cat.category)}</div>
                                    <ul class="cefr-conn-list">
                                        ${cat.examples.map(ex => `<li>${_esc(ex)}</li>`).join('')}
                                    </ul>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            `;
        }

        // Mocks Tab
        function _renderMocksTab() {
            return `
                <div class="cefr-mocks-wrapper">
                    <div class="cefr-mock-intro-card">
                        <h3>Simulacro oficial completo (4 Destrezas)</h3>
                        <p>El examen oficial evalúa las cuatro destrezas divididas en dos bloques eliminatorios:</p>
                        <div class="cefr-blocks-spec">
                            <div class="cefr-spec-card">
                                <strong>Bloque 1: Destrezas escritas (50 pts)</strong>
                                <ul>
                                    <li>Comprensión de lectura (70 min · 25 pts)</li>
                                    <li>Expresión escrita (60 min · 25 pts)</li>
                                </ul>
                                <span class="cefr-pass-pill">Apto: Mínimo 30 / 50 pts</span>
                            </div>
                            <div class="cefr-spec-card">
                                <strong>Bloque 2: Destrezas orales (50 pts)</strong>
                                <ul>
                                    <li>Comprensión auditiva (40 min · 25 pts)</li>
                                    <li>Expresión oral (15 min · 25 pts)</li>
                                </ul>
                                <span class="cefr-pass-pill">Apto: Mínimo 30 / 50 pts</span>
                            </div>
                        </div>
                        <div class="cefr-mock-cta-wrap">
                            <button type="button" class="btn btn-primary cefr-mock-btn" data-action="start-full-mock">
                                Iniciar simulacro completo cronometrado
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        // History Tab
        function _renderHistoryTab() {
            const prog = _loadProgress();
            const scores = prog.scores || {};

            let totalAttempted = 0;
            let sumScore = 0;
            let sumMax = 0;

            const rows = [];
            ['reading', 'listening', 'writing', 'speaking'].forEach(sk => {
                const skScores = scores[sk] || {};
                Object.keys(skScores).forEach(tid => {
                    totalAttempted++;
                    const rec = skScores[tid];
                    sumScore += rec.score;
                    sumMax += rec.maxScore;
                    rows.push({ skill: sk, tareaId: tid, rec: rec });
                });
            });

            const overallPct = sumMax > 0 ? Math.round((sumScore / sumMax) * 100) : 0;

            return `
                <div class="cefr-history-wrapper">
                    <div class="cefr-history-summary">
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${totalAttempted}</span>
                            <span class="cefr-sum-label">Tareas realizadas</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct}%</span>
                            <span class="cefr-sum-label">Puntuación media</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct >= 60 ? 'APTO' : (totalAttempted > 0 ? 'EN PROCESO' : '–')}</span>
                            <span class="cefr-sum-label">Calificación global</span>
                        </div>
                    </div>

                    <div class="cefr-history-table-card">
                        <h4>Registro detallado de tareas</h4>
                        ${rows.length === 0 ? `
                            <p class="cefr-empty">Aún no has completado ninguna tarea. Entrena en la pestaña 'Tareas oficiales'.</p>
                        ` : `
                            <table class="cefr-table">
                                <thead>
                                    <tr>
                                        <th>Destreza</th>
                                        <th>Tarea</th>
                                        <th>Puntos</th>
                                        <th>Porcentaje</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    ${rows.map(r => `
                                        <tr>
                                            <td><strong>${_esc(r.skill)}</strong></td>
                                            <td>${_esc(r.tareaId)}</td>
                                            <td>${r.rec.score} / ${r.rec.maxScore}</td>
                                            <td><span class="cefr-pct-badge ${r.rec.pct >= 60 ? 'is-pass' : 'is-fail'}">${r.rec.pct}%</span></td>
                                        </tr>
                                    `).join('')}
                                </tbody>
                            </table>
                        `}
                    </div>
                </div>
            `;
        }

        // ========================================
        // EVENT ATTACHMENTS
        // ========================================
        function _attachEvents(root) {
            // Main tabs
            root.querySelectorAll('[data-cefr-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.tab = btn.dataset.cefrTab;
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            });

            // Skill chips
            root.querySelectorAll('[data-cefr-skill]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.activeSkill = btn.dataset.cefrSkill;
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            });

            // Open Tarea card
            root.querySelectorAll('[data-cefr-open-tarea]').forEach(card => {
                card.addEventListener('click', () => {
                    _state.activeTareaId = card.dataset.cefrOpenTarea;
                    _state.readingSubmitted = false;
                    _state.listeningSubmitted = false;
                    _state.listeningPass = 1;
                    _state.writingResult = null;
                    _state.speakingResult = null;
                    _state.writingDraftText = _loadDraft(_state.activeTareaId);
                    render(_container);
                });
            });

            // Back button in runner
            const backBtn = root.querySelector('[data-action="back-to-tasks"]');
            if (backBtn) {
                backBtn.addEventListener('click', () => {
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            }

            // Reading Events
            root.querySelectorAll('[data-match-qid]').forEach(sel => {
                sel.addEventListener('change', () => {
                    _state.readingAnswers[sel.dataset.matchQid] = sel.value;
                });
            });

            root.querySelectorAll('[data-ans-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.ansQid] = parseInt(btn.dataset.ansIdx, 10);
                    render(_container);
                });
            });

            root.querySelectorAll('[data-stmt-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.stmtQid] = btn.dataset.stmtLetter;
                    render(_container);
                });
            });

            root.querySelectorAll('[data-gap-qid]').forEach(sel => {
                sel.addEventListener('change', () => {
                    _state.readingAnswers[sel.dataset.gapQid] = sel.value;
                });
            });

            root.querySelectorAll('[data-cloze-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.clozeQid] = parseInt(btn.dataset.clozeIdx, 10);
                    render(_container);
                });
            });

            const submitReadingBtn = root.querySelector('[data-action="submit-reading"]');
            if (submitReadingBtn) {
                submitReadingBtn.addEventListener('click', () => {
                    _state.readingSubmitted = true;
                    // Calculate reading score
                    const tarea = _getCurrentTarea();
                    let correctCount = 0;
                    let totalItems = 0;

                    if (tarea.type === 'matching-notices') {
                        totalItems = (tarea.people || []).length;
                        tarea.people.forEach(p => {
                            if (_state.readingAnswers[p.id] === p.correctNoticeId) correctCount++;
                        });
                    } else if (tarea.type === 'reading-mc') {
                        totalItems = (tarea.questions || []).length;
                        tarea.questions.forEach(q => {
                            if (_state.readingAnswers[q.id] === q.correct) correctCount++;
                        });
                    } else if (tarea.type === 'person-matching') {
                        totalItems = (tarea.statements || []).length;
                        tarea.statements.forEach(s => {
                            if (_state.readingAnswers[s.id] === s.correctPerson) correctCount++;
                        });
                    } else if (tarea.type === 'gapped-text') {
                        totalItems = (tarea.gaps || []).length;
                        tarea.gaps.forEach(g => {
                            if (_state.readingAnswers[g.id] === g.correct) correctCount++;
                        });
                    } else if (tarea.type === 'cloze-mc') {
                        totalItems = (tarea.items || []).length;
                        tarea.items.forEach(item => {
                            if (_state.readingAnswers[item.id] === item.correct) correctCount++;
                        });
                    }

                    _saveTaskScore('reading', tarea.id, correctCount, totalItems);
                    render(_container);
                });
            }

            const resetReadingBtn = root.querySelector('[data-action="reset-reading"]');
            if (resetReadingBtn) {
                resetReadingBtn.addEventListener('click', () => {
                    _state.readingAnswers = {};
                    _state.readingSubmitted = false;
                    render(_container);
                });
            }

            // Listening Events
            root.querySelectorAll('[data-listen-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.listeningAnswers[btn.dataset.listenQid] = parseInt(btn.dataset.listenIdx, 10);
                    render(_container);
                });
            });

            const submitListenBtn = root.querySelector('[data-action="submit-listening"]');
            if (submitListenBtn) {
                submitListenBtn.addEventListener('click', () => {
                    _state.listeningSubmitted = true;
                    _stopListeningTimers();
                    const tarea = _getCurrentTarea();
                    let correct = 0;
                    const questions = tarea.questions || [];
                    questions.forEach(q => {
                        if (_state.listeningAnswers[q.id] === q.correct) correct++;
                    });
                    _saveTaskScore('listening', tarea.id, correct, questions.length);
                    render(_container);
                });
            }

            const resetListenBtn = root.querySelector('[data-action="reset-listening"]');
            if (resetListenBtn) {
                resetListenBtn.addEventListener('click', () => {
                    _state.listeningAnswers = {};
                    _state.listeningSubmitted = false;
                    _state.listeningPass = 1;
                    _stopListeningTimers();
                    render(_container);
                });
            }

            // Writing Events
            const textarea = root.querySelector('#cefr-writing-textarea');
            if (textarea) {
                textarea.addEventListener('input', (e) => {
                    _state.writingDraftText = e.target.value;
                    _saveDraft(_state.activeTareaId, e.target.value);
                    const counter = root.querySelector('.cefr-word-counter strong');
                    if (counter) counter.textContent = _countWords(e.target.value);
                });
            }

            root.querySelectorAll('[data-writing-option]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.writingActiveOption = btn.dataset.writingOption;
                    render(_container);
                });
            });

            const submitWritingBtn = root.querySelector('[data-action="submit-writing"]');
            if (submitWritingBtn) {
                submitWritingBtn.addEventListener('click', () => {
                    const tarea = _getCurrentTarea();
                    _state.writingResult = _evaluateWritingText(_state.writingDraftText, tarea);
                    _saveTaskScore('writing', tarea.id, _state.writingResult.totalScore, 25);
                    render(_container);
                });
            }

            // Speaking Events
            const micBtn = root.querySelector('[data-action="toggle-mic"]');
            if (micBtn) {
                micBtn.addEventListener('click', () => {
                    if (_state.speakingIsRecording) {
                        _stopSpeakingRecording();
                    } else {
                        _startSpeakingRecording();
                    }
                });
            }

            const transcriptInput = root.querySelector('#cefr-speaking-transcript-input');
            if (transcriptInput) {
                transcriptInput.addEventListener('input', (e) => {
                    _state.speakingTranscriptText = e.target.value;
                });
            }

            const submitSpeakingBtn = root.querySelector('[data-action="submit-speaking"]');
            if (submitSpeakingBtn) {
                submitSpeakingBtn.addEventListener('click', () => {
                    const tarea = _getCurrentTarea();
                    _state.speakingResult = _evaluateSpeakingText(_state.speakingTranscriptText, tarea);
                    _saveTaskScore('speaking', tarea.id, _state.speakingResult.totalScore, 25);
                    render(_container);
                });
            }

            // Mock CTA
            const mockCta = root.querySelector('[data-action="start-full-mock"]');
            if (mockCta) {
                mockCta.addEventListener('click', () => {
                    // Open first reading task as preview for mock exam
                    _state.tab = 'tasks';
                    _state.activeSkill = 'reading';
                    const skill = _data.skills.reading;
                    if (skill && skill.tareas && skill.tareas.length > 0) {
                        _state.activeTareaId = skill.tareas[0].id;
                    }
                    render(_container);
                });
            }
        }

        async function render(container) {
            _container = container || _container;
            if (!_container) return;

            await _loadData();

            let mainContentHtml = '';
            if (_state.activeTareaId) {
                mainContentHtml = _renderActiveTarea();
            } else if (_state.tab === 'tasks') {
                mainContentHtml = _renderTasksTab();
            } else if (_state.tab === 'strategies') {
                mainContentHtml = _renderStrategiesTab();
            } else if (_state.tab === 'mocks') {
                mainContentHtml = _renderMocksTab();
            } else if (_state.tab === 'history') {
                mainContentHtml = _renderHistoryTab();
            }

            _container.innerHTML = `
                <div class="cefr-exam-hub" data-exam-id="${_esc(_id)}">
                    <div class="cefr-header">
                        <div class="cefr-header-left">
                            <h2 class="cefr-title">${_esc(_data ? _data.title : config.title)}</h2>
                            <p class="cefr-subtitle">${_esc(_data ? _data.subtitle : config.subtitle)}</p>
                        </div>
                    </div>

                    ${!_state.activeTareaId ? _renderTabs() : ''}

                    <div class="cefr-body">
                        ${mainContentHtml}
                    </div>
                </div>
            `;

            _attachEvents(_container);

            if (_state.activeTareaId && _state.activeSkill === 'listening') {
                _updateListeningConsole();
            }
        }

        function stop() {
            _stopListeningTimers();
            _stopSpeakingStreams();
        }

        return {
            id: _id,
            render: render,
            stop: stop
        };
    }

    const DeleB1Exam = createModule({
        id: 'es-dele-b1-exam',
        dataFile: 'dele-b1-exam.json',
        title: 'Prueba DELE B1',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial B1'
    });

    const EclB1Exam = createModule({
        id: 'hu-ecl-b1-exam',
        dataFile: 'ecl-b1-exam.json',
        title: 'ECL B1 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · B1 szintű komplex nyelvvizsga-felkészítő'
    });

    return {
        createModule: createModule,
        DeleB1Exam: DeleB1Exam,
        EclB1Exam: EclB1Exam
    };
})();

// Export globally and for CommonJS tests
if (typeof window !== 'undefined') {
    window.CefrExam = CefrExam;
    window.DeleB1Exam = CefrExam.DeleB1Exam;
    window.EclB1Exam = CefrExam.EclB1Exam;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CefrExam;
}
