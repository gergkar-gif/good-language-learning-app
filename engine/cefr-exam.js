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
            listeningActiveItemId: null,
            listeningItemPasses: {},
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
            _state.listeningActiveItemId = null;
        }

        function _speakTurn(text, voiceGender, onEnded) {
            const langCode = typeof Lang !== 'undefined' ? Lang.code() : 'es';
            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
                ParlourTTS.speak({
                    text: text,
                    language: langCode,
                    type: 'listening',
                    gender: voiceGender,
                    speed: _state.listeningSpeed,
                    onEnded: () => {
                        if (typeof onEnded === 'function') onEnded();
                    }
                }).then(started => {
                    if (!started) {
                        _fallbackSpeak(text, langCode, onEnded);
                    }
                }).catch(() => {
                    _fallbackSpeak(text, langCode, onEnded);
                });
            } else {
                _fallbackSpeak(text, langCode, onEnded);
            }
        }

        function _fallbackSpeak(text, langCode, onEnded) {
            if (typeof Speech !== 'undefined' && Speech.speak) {
                Speech.speak(text, { rate: _state.listeningSpeed, onEnd: onEnded });
            } else if (typeof window !== 'undefined' && window.speechSynthesis) {
                const utter = new SpeechSynthesisUtterance(text);
                utter.lang = langCode.startsWith('hu') ? 'hu-HU' : 'es-ES';
                utter.rate = _state.listeningSpeed;
                utter.onend = () => { if (typeof onEnded === 'function') onEnded(); };
                utter.onerror = () => { if (typeof onEnded === 'function') onEnded(); };
                window.speechSynthesis.speak(utter);
            } else {
                setTimeout(() => { if (typeof onEnded === 'function') onEnded(); }, 1500);
            }
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
            const voiceGender = turn.gender || (turnIndex % 2 === 0 ? 'female' : 'male');

            _speakTurn(text, voiceGender, () => {
                setTimeout(() => {
                    if (_state.listeningPlaying) {
                        _playTurnSequence(turns, turnIndex + 1, onComplete);
                    }
                }, 500);
            });
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
            if (!tarea) return;

            const isHu = _id.includes('hu');

            // Case A: Continuous Audio Tarea (like Tarea 2 Interview)
            if (tarea.audio && tarea.audio.turns) {
                const turns = tarea.audio.turns;
                let statusText = '';
                let subText = '';
                let btnHtml = '';

                if (_state.listeningPlaying) {
                    const turn = turns[_state.listeningCurrentTurn];
                    statusText = isHu
                        ? `${_state.listeningPass} / 2. meghallgatás: Hang lejátszása`
                        : `Pase ${_state.listeningPass} de 2: Reproduciendo audio`;
                    subText = turn
                        ? (isHu ? `Beszélő: ${turn.speaker}` : `Voz: ${turn.speaker}`)
                        : (isHu ? 'Figyelmes hallgatás...' : 'Escuchando con atención...');
                    btnHtml = `
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-pause">${isHu ? 'Lejátszás szüneteltetése' : 'Detener audio'}</button>
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    `;
                } else if (_state.listeningIntermission) {
                    statusText = isHu ? 'Szünet a meghallgatások között' : 'Pausa entre audiciones';
                    subText = isHu
                        ? `A második meghallgatás ${_state.listeningIntermissionCountdown} másodperc múlva kezdődik. Nézd át a válaszlehetőségeket.`
                        : `La segunda audición comenzará en ${_state.listeningIntermissionCountdown} segundos. Revisa tus opciones.`;
                    btnHtml = `
                        <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="skip-intermission">${isHu ? 'Második meghallgatás indítása' : 'Comenzar segunda audición'}</button>
                    `;
                } else if (_state.listeningPass === 2 && !_state.listeningPlaying) {
                    statusText = isHu ? 'Meghallgatás befejezve' : 'Audición completada';
                    subText = isHu
                        ? 'Mindkét hivatalos meghallgatás befejeződött. Jelöld be a válaszaidat és ellenőrizd a feladatot.'
                        : 'Has escuchado los dos pases oficiales. Selecciona tus respuestas y comprueba la tarea.';
                    btnHtml = `
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="replay-pass-2">${isHu ? 'Második meghallgatás ismétlése' : 'Repetir segundo pase'}</button>
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    `;
                } else {
                    statusText = isHu
                        ? `${_state.listeningPass} / 2. meghallgatás készen áll`
                        : `Pase ${_state.listeningPass} de 2 preparado`;
                    subText = isHu ? 'Kattints a lejátszásra, amikor készen állsz.' : 'Pulsa reproducir cuando estés listo.';
                    btnHtml = `
                        <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="audio-play">${isHu ? `${_state.listeningPass}. meghallgatás lejátszása` : `Reproducir pase ${_state.listeningPass}`}</button>
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
                return;
            }

            // Case B: Discrete Items Tarea (like Tarea 1 Short Messages)
            if (tarea.items && tarea.items.length > 0) {
                const isPlaying = _state.listeningPlaying;
                const activeItem = (tarea.items || []).find(it => it.id === _state.listeningActiveItemId);

                el.innerHTML = `
                    <div class="cefr-audio-status-wrap">
                        <span class="cefr-audio-status-label">${isHu ? `${tarea.items.length} rövid hanganyag` : `${tarea.items.length} avisos y mensajes breves`}</span>
                        <span class="cefr-audio-status-sub">${isPlaying && activeItem ? (isHu ? `${activeItem.num}. szöveg lejátszása...` : `Reproduciendo mensaje ${activeItem.num}...`) : (isHu ? 'Kattints az egyes kérdések hangfájljára a meghallgatáshoz (legfeljebb 2 lejátszás kérdésenként).' : 'Pulsa en cada pregunta para escuchar su mensaje correspondiente (hasta 2 pases por mensaje).')}</span>
                    </div>
                    <div class="cefr-audio-controls">
                        ${isPlaying ? `
                            <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-pause">${isHu ? 'Leállítás' : 'Detener audio'}</button>
                        ` : ''}
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    </div>
                `;

                const pauseBtn = el.querySelector('[data-action="audio-pause"]');
                if (pauseBtn) pauseBtn.addEventListener('click', () => {
                    _stopListeningTimers();
                    render(_container);
                });

                const speedBtn = el.querySelector('[data-action="audio-speed"]');
                if (speedBtn) {
                    speedBtn.addEventListener('click', () => {
                        _state.listeningSpeed = (_state.listeningSpeed === 1.0) ? 0.85 : 1.0;
                        _updateListeningConsole();
                    });
                }
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
                const isHu = _id.includes('hu');
                alert(isHu
                    ? 'A mikrofonhoz való hozzáférés nem sikerült. A válaszodat a szövegmezőbe is megírhatod.'
                    : 'No se pudo acceder al micrófono. Puedes redactar tu respuesta oral en el campo de texto.');
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

            const isHu = _id.includes('hu');
            if (_state.speakingIsRecording) {
                btn.textContent = isHu ? 'Felvétel leállítása' : 'Detener grabación';
                btn.className = 'btn btn-secondary cefr-record-btn is-recording';
                statusEl.textContent = isHu ? 'Hangfelvétel folyamatban... Beszélj természetesen.' : 'Grabando voz... Habla con naturalidad.';
            } else {
                btn.textContent = isHu ? 'Hangfelvétel indítása' : 'Iniciar grabación de voz';
                btn.className = 'btn btn-primary cefr-record-btn';
                statusEl.textContent = isHu ? 'A mikrofon készen áll. Kattints a felvételhez.' : 'Micrófono listo. Pulsa para comenzar tu producción oral.';
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
            const isHu = _id.includes('hu');
            const isA1 = (_data && _data.level === 'A1') || _id.includes('a1');
            const isA2 = (_data && _data.level === 'A2') || _id.includes('a2');
            const isB2 = (_data && _data.level === 'B2') || _id.includes('b2');
            const examConnectors = isHu ? (
                isA1 ? [
                    'és', 'de', 'mert', 'is', 'szintén', 'vagy',
                    'szia', 'sziasztok', 'jó napot', 'köszönöm', 'nagyon köszönöm',
                    'üdvözlettel', 'szép napot', 'viszlát', 'ezért'
                ] : (isA2 ? [
                    'és', 'de', 'mert', 'is', 'szintén', 'vagy', 'ezért',
                    'után', 'aztán', 'amikor', 'ha', 'szerintem', 'például',
                    'szia', 'sziasztok', 'kedves', 'köszönöm', 'nagyon köszönöm',
                    'üdvözlettel', 'remélem', 'viszlát'
                ] : (isB2 ? [
                    'véleményem szerint', 'úgy vélem, hogy', 'meglátásom szerint', 'álláspontom szerint',
                    'egyrészt', 'másrészt', 'elsőként', 'mindazonáltal', 'ennek ellenére',
                    'jóllehet', 'ugyanakkor', 'viszont', 'továbbá', 'ráadásul',
                    'következésképpen', 'tekintettel arra, hogy', 'ebből fakadóan', 'ennek következtében',
                    'összességében', 'kétségkívül', 'határozottan', 'fontos hangsúlyozni'
                ] : [
                    'véleményem szerint', 'úgy gondolom, hogy', 'szerintem', 'meglátásom szerint',
                    'egyrészt', 'másrészt', 'először is', 'továbbá', 'végül',
                    'azonban', 'ennek ellenére', 'bár', 'ugyanakkor', 'viszont',
                    'ezért', 'mivel', 'ennek következtében', 'így', 'tehát',
                    'nagyon köszönöm', 'üdvözlettel', 'remélem', 'fontos, hogy'
                ]))
            ) : (
                isA1 ? [
                    'y', 'pero', 'porque', 'también', 'además', 'o',
                    'hola', 'buenos días', 'gracias', 'muchas gracias',
                    'un saludo', 'un abrazo', 'hasta pronto', 'saludos', 'por eso'
                ] : (isA2 ? [
                    'y', 'pero', 'porque', 'también', 'además', 'o', 'por eso',
                    'cuando', 'después', 'luego', 'entonces', 'primero',
                    'hola', 'buenos días', 'estimado', 'gracias', 'muchas gracias',
                    'un saludo', 'un abrazo', 'hasta pronto', 'saludos', 'si', 'aunque'
                ] : (isB2 ? [
                    'en primer lugar', 'por una parte', 'por otra parte', 'en lo que respecta a',
                    'sin embargo', 'no obstante', 'a pesar de que', 'si bien', 'pese a',
                    'por consiguiente', 'en consecuencia', 'por lo tanto', 'de ahí que',
                    'desde mi punto de vista', 'en mi opinión', 'cabe destacar que', 'conviene señalar que',
                    'es imprescindible que', 'resulta fundamental que', 'en definitiva', 'en conclusión'
                ] : [
                    'sin embargo', 'por lo tanto', 'en mi opinión', 'por un lado', 'por otro lado',
                    'en cuanto a', 'además', 'me encantaría', 'gracias por', 'un abrazo', 'aunque',
                    'de modo que', 'así que', 'dado que', 'es importante que', 'no creo que'
                ]))
            );
            const lowerText = text.toLowerCase();
            const foundConnectors = examConnectors.filter(c => lowerText.includes(c));
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
            const isHu = _id.includes('hu');
            const isA1 = (_data && _data.level === 'A1') || _id.includes('a1');
            const isA2 = (_data && _data.level === 'A2') || _id.includes('a2');
            const isB2 = (_data && _data.level === 'B2') || _id.includes('b2');
            const speakingConnectors = isHu
                ? (isA1 ? ['és', 'mert', 'is', 'de', 'szintén', 'szerintem']
                    : (isA2 ? ['és', 'mert', 'is', 'de', 'szintén', 'szerintem', 'ezért', 'például', 'aztán']
                    : (isB2 ? ['véleményem szerint', 'úgy vélem', 'meglátásom szerint', 'elsőként', 'például', 'ugyanakkor', 'mindazonáltal', 'ennek következtében', 'másrészt', 'egyrészt', 'összességében']
                    : ['véleményem szerint', 'szerintem', 'úgy gondolom', 'először is', 'például', 'ugyanakkor', 'azonban', 'ezért', 'másrészt', 'egyrészt'])))
                : (isA1 ? ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo']
                    : (isA2 ? ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo', 'por eso', 'después', 'entonces']
                    : (isB2 ? ['en primer lugar', 'por ejemplo', 'en mi opinión', 'desde mi perspectiva', 'además', 'por consiguiente', 'no obstante', 'sin embargo', 'en definitiva', 'cabe destacar']
                    : ['en primer lugar', 'por ejemplo', 'en mi opinión', 'además', 'por eso'])));
            const foundConnectors = speakingConnectors.filter(c => lowerText.includes(c));
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
                { id: 'strategies', label: (_id.includes('hu')) ? 'Stratégiák és tanácsok' : 'Guía y estrategias' },
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
            if (!skill || !skill.tareas) return `<p class="cefr-empty">${_id.includes('hu') ? 'Nincsenek elérhető feladatok.' : 'No hay tareas disponibles.'}</p>`;

            const skillProg = prog[_state.activeSkill] || {};

            return skill.tareas.map(t => {
                const recorded = skillProg[t.id];
                const badgeHtml = recorded
                    ? `<span class="cefr-status-pill is-completed">${recorded.pct}% (${recorded.score}/${recorded.maxScore})</span>`
                    : `<span class="cefr-status-pill is-pending">${_id.includes('hu') ? 'Nincs kitöltve' : 'Pendiente'}</span>`;

                return `
                    <div class="cefr-task-card" data-cefr-open-tarea="${_esc(t.id)}">
                        <div class="cefr-task-card-header">
                            <span class="cefr-task-pill">${_esc(t.title || (_id.includes('hu') ? `${t.tareaNum}. feladat` : `Tarea ${t.tareaNum}`))}</span>
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
                        <button type="button" class="cefr-back-btn" data-action="back-to-tasks" aria-label="${_id.includes('hu') ? 'Vissza a feladatokhoz' : 'Volver a tareas'}">
                            <svg class="art icon cefr-back-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
                            <span>${_id.includes('hu') ? 'Vissza a feladatokhoz' : 'Volver a tareas'}</span>
                        </button>
                        <h3 class="cefr-runner-title">${_esc(tarea.title)}</h3>
                    </div>
                    ${contentHtml}
                </div>
            `;
        }

        function _formatGappedPassage(text) {
            const isHu = _id.includes('hu');
            return (text || '').split('\n\n').map(p => {
                const escaped = _esc(p);
                const tokenHtml = isHu
                    ? '<span class="cefr-inline-gap-token">[ $1. ]</span>'
                    : '<span class="cefr-inline-gap-token">[ Hueco $1 ]</span>';
                const withTokens = escaped.replace(/\[___(\d+)___\]/g, tokenHtml);
                return `<p class="cefr-passage-paragraph">${withTokens}</p>`;
            }).join('');
        }

        // 1. Reading Tarea View
        function _renderReadingTarea(tarea) {
            const isHu = _id.includes('hu');
            let stimulusTitle = '';
            let stimulusSubtitle = '';
            let stimulusHtml = '';
            let questionsTitle = '';
            let questionsSubtitle = '';
            let questionsHtml = '';

            if (tarea.type === 'matching-notices') {
                stimulusTitle = isHu ? 'Hirdetések (A-J)' : 'Tablón de anuncios (A-J)';
                stimulusSubtitle = isHu ? 'Olvasd el a 10 rövid hirdetést' : 'Lee los 10 avisos y anuncios breves';
                stimulusHtml = `
                    <div class="cefr-notices-editorial-grid">
                        ${(tarea.notices || []).map(n => `
                            <div class="cefr-notice-card" id="notice-${_esc(n.id)}">
                                <div class="cefr-notice-tag">[${_esc(n.letter)}] ${_esc(n.title)}</div>
                                <p class="cefr-notice-text">${_esc(n.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                questionsTitle = isHu ? 'Személyek és igények (1-6)' : 'Personas y necesidades (1-6)';
                questionsSubtitle = isHu ? 'Rendeld hozzá minden személyhez a megfelelő hirdetést' : 'Relaciona a cada persona con el anuncio adecuado';
                questionsHtml = `
                    <div class="cefr-matching-cards-list">
                        ${(tarea.people || []).map((p, idx) => {
                            const selected = _state.readingAnswers[p.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && selected === p.correctNoticeId;
                            const isWrong = isSubmitted && selected !== p.correctNoticeId;
                            const correctNotice = (tarea.notices || []).find(n => n.id === p.correctNoticeId);

                            return `
                                <div class="cefr-matching-row-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-matching-info">
                                        <span class="cefr-matching-idx">${idx + 1}</span>
                                        <div class="cefr-matching-text">
                                            <strong>${_esc(p.name)}:</strong> ${_esc(p.text)}
                                        </div>
                                    </div>
                                    <div class="cefr-matching-picker">
                                        <label class="cefr-select-label">${isHu ? 'Hozzárendelt hirdetés:' : 'Anuncio correspondiente:'}</label>
                                        <select class="cefr-select" data-match-qid="${_esc(p.id)}" ${isSubmitted ? 'disabled' : ''}>
                                            <option value="">-- ${isHu ? 'Válassz hirdetést' : 'Elige anuncio'} --</option>
                                            ${(tarea.notices || []).map(n => `
                                                <option value="${_esc(n.id)}" ${selected === n.id ? 'selected' : ''}>
                                                    [${_esc(n.letter)}] ${_esc(n.title)}
                                                </option>
                                            `).join('')}
                                        </select>
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-matching-feedback ${isCorrect ? 'is-correct' : 'is-wrong'}">
                                            ${isCorrect 
                                                ? `<span class="cefr-feedback-pass">${isHu ? 'Helyes' : 'Correcto'}: [${correctNotice ? _esc(correctNotice.letter) : ''}] ${correctNotice ? _esc(correctNotice.title) : ''}</span>`
                                                : `<span class="cefr-feedback-fail">${isHu ? 'Helyes megoldás' : 'Respuesta correcta'}: [${correctNotice ? _esc(correctNotice.letter) : ''}] ${correctNotice ? _esc(correctNotice.title) : ''}</span>`}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'reading-mc') {
                stimulusTitle = isHu ? 'Olvasandó szöveg' : 'Texto de lectura';
                stimulusSubtitle = isHu ? 'Olvasd el a cikket a kérdések megválaszolása előtt' : 'Lee el texto con atención antes de responder';
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${(tarea.passage || '').split('\n\n').map(p => `<p class="cefr-passage-paragraph">${_esc(p)}</p>`).join('')}
                    </div>
                `;

                questionsTitle = isHu ? 'Kérdések' : 'Preguntas de comprensión';
                questionsSubtitle = isHu ? 'Válaszd ki a helyes opciót (A, B vagy C)' : 'Selecciona la opción correcta (A, B o C)';
                questionsHtml = `
                    <div class="cefr-questions-stack">
                        ${(tarea.questions || []).map((q, qIdx) => {
                            const selectedOpt = _state.readingAnswers[q.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && selectedOpt === q.correct;
                            const isWrong = isSubmitted && selectedOpt !== q.correct && selectedOpt !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title"><span class="cefr-q-num">${qIdx + 1}.</span> ${_esc(q.question)}</div>
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
                                            <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(q.explanation || '')}
                                            ${q.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(q.evidence)}"</em></div>` : ''}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'person-matching') {
                const numPeople = (tarea.people || []).length;
                const peopleLetters = numPeople ? tarea.people.map(p => p.letter) : ['A', 'B', 'C'];
                stimulusTitle = isHu ? 'Személyes vélemények' : 'Testimonios personales';
                stimulusSubtitle = isHu
                    ? `${numPeople} személy tapasztalatai (${peopleLetters.join(', ')})`
                    : `${numPeople} experiencias y puntos de vista (${peopleLetters.join(', ')})`;
                stimulusHtml = `
                    <div class="cefr-people-editorial-grid">
                        ${(tarea.people || []).map(p => `
                            <div class="cefr-person-card">
                                <div class="cefr-person-header">
                                    <span class="cefr-person-badge">[${_esc(p.letter)}]</span>
                                    <strong class="cefr-person-title">${_esc(p.name)}</strong>
                                </div>
                                <p class="cefr-person-quote">${_esc(p.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                const numStatements = (tarea.statements || []).length;
                questionsTitle = isHu ? `Állítások (1-${numStatements})` : `Afirmaciones (1-${numStatements})`;
                questionsSubtitle = isHu
                    ? `Melyik személyre (${peopleLetters.join(', ')}) vonatkozik az állítás?`
                    : `¿A qué persona (${peopleLetters.join(', ')}) corresponde cada afirmación?`;
                questionsHtml = `
                    <div class="cefr-statements-stack">
                        ${(tarea.statements || []).map(s => {
                            const chosen = _state.readingAnswers[s.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === s.correctPerson;
                            const isWrong = isSubmitted && chosen !== s.correctPerson;

                            return `
                                <div class="cefr-statement-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-statement-text">${_esc(s.text)}</div>
                                    <div class="cefr-btn-trio">
                                        ${peopleLetters.map(letter => `
                                            <button type="button" class="cefr-opt-btn cefr-btn-compact ${chosen === letter ? 'is-selected' : ''}" data-stmt-qid="${_esc(s.id)}" data-stmt-letter="${letter}" ${isSubmitted ? 'disabled' : ''}>
                                                ${letter}
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(s.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'gapped-text') {
                const gapsCount = (tarea.gaps || []).length;
                const optLetterRange = (tarea.options && tarea.options.length)
                    ? `(${tarea.options[0].letter}–${tarea.options[tarea.options.length - 1].letter})`
                    : '';
                stimulusTitle = isHu ? 'Szöveg' : 'Texto principal';
                stimulusSubtitle = isHu
                    ? 'Figyeld meg a hiányzó mondatok helyét a szövegben'
                    : `Observa la posición de los ${gapsCount || 6} fragmentos omitidos`;
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${_formatGappedPassage(tarea.passage || '')}
                    </div>

                    <div class="cefr-gaps-options-pool-wrap">
                        <h5 class="cefr-gaps-pool-title">${isHu ? `Hiányzó mondatok ${optLetterRange}`.trim() : `Opciones de oraciones para los huecos ${optLetterRange}`.trim()}</h5>
                        <div class="cefr-gaps-options-pool">
                            ${(tarea.options || []).map(o => `
                                <div class="cefr-gap-pool-item">
                                    <span class="cefr-gap-badge">[${_esc(o.letter)}]</span>
                                    <span class="cefr-gap-desc">${_esc(o.text)}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;

                const gapNumRange = gapsCount ? `(1–${gapsCount})` : '';
                questionsTitle = isHu ? `Hiányzó mondatok beillesztése ${gapNumRange}`.trim() : `Completar los huecos ${gapNumRange}`.trim();
                questionsSubtitle = isHu ? 'Válaszd ki a megfelelő mondatot az egyes helyekre' : 'Selecciona la oración correcta para cada posición';
                questionsHtml = `
                    <div class="cefr-gaps-rows-stack">
                        ${(tarea.gaps || []).map(g => {
                            const chosen = _state.readingAnswers[g.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === g.correct;
                            const isWrong = isSubmitted && chosen !== g.correct;

                            return `
                                <div class="cefr-gap-row-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <span class="cefr-gap-row-label">${isHu ? `[ ${g.num}. ]` : `Hueco [___${g.num}___]:`}</span>
                                    <select class="cefr-select" data-gap-qid="${_esc(g.id)}" ${isSubmitted ? 'disabled' : ''}>
                                        <option value="">-- ${isHu ? 'Válassz megoldást' : 'Selecciona letra'} --</option>
                                        ${(tarea.options || []).map(o => `
                                            <option value="${_esc(o.letter)}" ${chosen === o.letter ? 'selected' : ''}>
                                                [${_esc(o.letter)}] ${_esc(o.text.substring(0, 60))}...
                                            </option>
                                        `).join('')}
                                    </select>
                                    ${isSubmitted ? `
                                        <div class="cefr-gap-feedback ${isCorrect ? 'is-correct' : 'is-wrong'}">
                                            ${isCorrect ? (isHu ? 'Helyes' : 'Correcto') : `${isHu ? 'Megoldás' : 'Solución'}: [${g.correct}]`}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'cloze-mc') {
                const itemsCount = (tarea.items || []).length;
                const itemNumRange = itemsCount ? `(1–${itemsCount})` : '';
                stimulusTitle = isHu ? 'Szöveg' : 'Texto con huecos gramaticales';
                stimulusSubtitle = isHu ? 'Olvasd el a szöveget és válaszd ki a helyes alakokat' : 'Lee el texto y completa los huecos con la opción correcta';
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${_formatGappedPassage(tarea.passage || '')}
                    </div>
                `;

                questionsTitle = isHu ? `Nyelvtani és lexikai opciók ${itemNumRange}`.trim() : `Opciones de gramática y léxico ${itemNumRange}`.trim();
                questionsSubtitle = isHu ? 'Válaszd ki a helyes alakot az egyes helyekre' : 'Selecciona la forma correcta para cada hueco';
                questionsHtml = `
                    <div class="cefr-cloze-grid">
                        ${(tarea.items || []).map(item => {
                            const chosen = _state.readingAnswers[item.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === item.correct;
                            const isWrong = isSubmitted && chosen !== item.correct && chosen !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">${isHu ? `[ ${item.num}. ]` : `Hueco [___${item.num}___]`}</div>
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
                                            <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(item.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            }

            return `
                <div class="cefr-reading-stack">
                    <div class="cefr-reading-stimulus-card">
                        <div class="cefr-stimulus-header">
                            <h4>${_esc(stimulusTitle)}</h4>
                            <span class="cefr-stimulus-sub">${_esc(stimulusSubtitle)}</span>
                        </div>
                        <div class="cefr-stimulus-body">
                            ${stimulusHtml}
                        </div>
                    </div>

                    <div class="cefr-reading-questions-block">
                        <div class="cefr-questions-header">
                            <h4>${_esc(questionsTitle)}</h4>
                            <span class="cefr-questions-sub">${_esc(questionsSubtitle)}</span>
                        </div>
                        <div class="cefr-questions-flow">
                            ${questionsHtml}
                        </div>

                        <div class="cefr-action-bar">
                            ${!_state.readingSubmitted ? `
                                <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-reading">
                                    ${isHu ? 'Feladat ellenőrzése' : 'Comprobar tarea'}
                                </button>
                            ` : `
                                <button type="button" class="btn btn-secondary cefr-reset-btn" data-action="reset-reading">
                                    ${isHu ? 'Újrapróbálás' : 'Repetir tarea'}
                                </button>
                            `}
                        </div>
                    </div>
                </div>
            `;
        }

        // 2. Listening Tarea View
        function _renderListeningTarea(tarea) {
            const isHu = _id.includes('hu');
            let questionsHtml = '';

            // Handle Discrete Items (Tarea 1: Avisos y mensajes breves)
            if (tarea.items && tarea.items.length > 0) {
                questionsHtml = tarea.items.map((item) => {
                    const chosen = _state.listeningAnswers[item.id];
                    const isSubmitted = _state.listeningSubmitted;
                    const isCorrect = isSubmitted && chosen === item.correct;
                    const isWrong = isSubmitted && chosen !== item.correct && chosen !== undefined;
                    const isThisPlaying = _state.listeningPlaying && _state.listeningActiveItemId === item.id;
                    const passes = _state.listeningItemPasses[item.id] || 0;

                    return `
                        <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                            <div class="cefr-item-topline">
                                <span class="cefr-q-num">${item.num}.</span>
                                <span class="cefr-item-situation">${_esc(item.situation || '')}</span>
                            </div>

                            <div class="cefr-item-audio-row">
                                <button type="button" class="cefr-item-play-btn ${isThisPlaying ? 'is-playing' : ''}" data-action="play-single-item" data-item-id="${_esc(item.id)}">
                                    <svg class="art icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                                        ${isThisPlaying ? '<rect x="6" y="6" width="12" height="12" fill="currentColor"/>' : '<polygon points="7 5 19 12 7 19 7 5" fill="currentColor"/>'}
                                    </svg>
                                    <span>${isThisPlaying ? (isHu ? 'Leállítás' : 'Detener reproducción') : (passes > 0 ? (isHu ? `Újrahallgatás (${passes}/2)` : `Repetir audio (${passes}/2 pases)`) : (isHu ? 'Meghallgatás (1/2)' : 'Escuchar audio (Pase 1/2)'))}</span>
                                </button>
                            </div>

                            <div class="cefr-q-title">${_esc(item.question)}</div>

                            <div class="cefr-options-list">
                                ${(item.options || []).map((opt, optIdx) => `
                                    <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === item.correct ? 'is-correct-target' : ''}" data-listen-qid="${_esc(item.id)}" data-listen-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                        <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                        <span class="cefr-opt-text">${_esc(opt)}</span>
                                    </button>
                                `).join('')}
                            </div>

                            ${isSubmitted ? `
                                <div class="cefr-explanation-box">
                                    <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(item.explanation || '')}
                                    ${item.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(item.evidence)}"</em></div>` : ''}
                                    ${(item.audio && item.audio.turns) ? `
                                        <div class="cefr-item-transcript">
                                            <strong>${isHu ? 'Szöveg' : 'Transcripción'}:</strong>
                                            ${item.audio.turns.map(t => `<p><em>${_esc(t.speaker)}:</em> ${_esc(t.text)}</p>`).join('')}
                                        </div>
                                    ` : ''}
                                </div>
                            ` : ''}
                        </div>
                    `;
                }).join('');
            } else if (tarea.questions && tarea.questions.length > 0) {
                // Continuous Audio (Tarea 2: Entrevista)
                questionsHtml = tarea.questions.map((q, qIdx) => {
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
                                    <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(q.explanation || '')}
                                    ${q.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(q.evidence)}"</em></div>` : ''}
                                </div>
                            ` : ''}
                        </div>
                    `;
                }).join('');
            }

            return `
                <div class="cefr-listening-wrapper">
                    <div id="cefr-audio-console" class="cefr-audio-console">
                        <!-- Populated by _updateListeningConsole() -->
                    </div>

                    <div class="cefr-listening-questions">
                        ${questionsHtml}
                    </div>

                    ${_state.listeningSubmitted && tarea.audio && tarea.audio.turns ? `
                        <div class="cefr-transcript-section">
                            <div class="cefr-transcript-header">
                                <h4>${isHu ? 'Teljes hanganyag szövege' : 'Transcripción completa de la audición'}</h4>
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

                    const isHu = _id.includes('hu');
                    return `
                <div class="cefr-writing-wrapper">
                    ${optionSwitcherHtml}

                    <div class="cefr-writing-prompt-card">
                        <div class="cefr-prompt-title">${isHu ? 'A feladat leírása:' : 'Instrucciones de la tarea:'}</div>
                        <div class="cefr-prompt-text">${_esc(activePrompt).split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}</div>
                    </div>

                    <div class="cefr-editor-container">
                        <div class="cefr-editor-toolbar">
                            <span class="cefr-word-counter ${isWordCountGood ? 'is-good' : (currentWords > maxWords ? 'is-over' : '')}">
                                ${isHu ? 'Szavak száma:' : 'Palabras:'} <strong>${currentWords}</strong> / ${minWords}–${maxWords}
                            </span>
                            <span class="cefr-draft-status">${isHu ? 'Piszkozat automatikusan mentve' : 'Borrador guardado automáticamente'}</span>
                        </div>
                        <textarea id="cefr-writing-textarea" class="cefr-textarea" placeholder="${isHu ? 'Írd ide a fogalmazásodat...' : 'Escribe tu redacción aquí...'}" rows="12">${_esc(_state.writingDraftText)}</textarea>
                    </div>

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-writing">
                            ${isHu ? 'Fogalmazás értékelése' : 'Evaluar redacción (Rúbrica CEFR)'}
                        </button>
                    </div>

                    ${_state.writingResult ? `
                        <div class="cefr-writing-results-card">
                            <div class="cefr-res-header">
                                <h4>${isHu ? `${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')))} Értékelési jelentés` : `Informe de evaluación ${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')))}`}</h4>
                                <span class="cefr-score-badge">${_state.writingResult.totalScore} / 25 ${isHu ? 'pont' : 'puntos'}</span>
                            </div>
                            <div class="cefr-rubric-breakdown">
                                <div class="cefr-rubric-item">
                                    <span>${isHu ? `Tartalmi megfelelés és terjedelem (${_state.writingResult.wordCount} szó):` : `Adecuación y extensión (${_state.writingResult.wordCount} palabras):`}</span>
                                    <strong>${_state.writingResult.criteria.adecuacion} / 7 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${isHu ? `Szövegösszefüggés és kötőszavak (${_state.writingResult.foundConnectors.length} észlelve):` : `Coherencia y conectores (${_state.writingResult.foundConnectors.length} detectados):`}</span>
                                    <strong>${_state.writingResult.criteria.coherencia} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${isHu ? 'Bekezdések és tagolás:' : 'Párrafos y estructuración:'}</span>
                                    <strong>${_state.writingResult.criteria.estructura} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${isHu ? 'Irányítási szempontok és szókincs:' : 'Puntos guía y riqueza léxica:'}</span>
                                    <strong>${_state.writingResult.criteria.leves} / 6 pts</strong>
                                </div>
                            </div>
                            ${_state.writingResult.foundConnectors.length > 0 ? `
                                <div class="cefr-detected-connectors">
                                    <span>${isHu ? `Használt ${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')))} kötőszavak:` : `Conectores ${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')))} empleados:`}</span>
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
            const isHu = _id.includes('hu');
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
                                ${isHu ? 'A mikrofon készen áll. Kattints a felvételhez.' : 'Micrófono listo. Pulsa para comenzar tu producción oral.'}
                            </span>
                        </div>
                        <div class="cefr-mic-controls">
                            <button type="button" id="cefr-mic-toggle-btn" class="btn btn-primary cefr-record-btn" data-action="toggle-mic">
                                ${isHu ? 'Hangfelvétel indítása' : 'Iniciar grabación de voz'}
                            </button>
                        </div>
                    </div>

                    <div class="cefr-speaking-transcript-wrap">
                        <label for="cefr-speaking-transcript-input" class="cefr-transcript-label">
                            ${isHu ? 'A válaszod leirata (átnézheted vagy szerkesztheted az értékelés előtt):' : 'Transcripción de tu respuesta (puedes revisarla o editarla antes de evaluar):'}
                        </label>
                        <textarea id="cefr-speaking-transcript-input" class="cefr-textarea cefr-transcript-textarea" rows="5" placeholder="${isHu ? 'A beszéded valós időben jelenik meg itt...' : 'Tu voz se transcribirá aquí en tiempo real...'}">${_esc(_state.speakingTranscriptText)}</textarea>
                    </div>

                    ${_state.speakingAudioBlobUrl ? `
                        <div class="cefr-playback-card">
                            <span>${isHu ? 'Hallgasd vissza a felvételt:' : 'Escucha tu grabación:'}</span>
                            <audio controls src="${_state.speakingAudioBlobUrl}" class="cefr-audio-player"></audio>
                        </div>
                    ` : ''}

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-speaking">
                            ${isHu ? 'Beszédkészség értékelése' : 'Evaluar expresión oral'}
                        </button>
                    </div>

                    ${_state.speakingResult ? `
                        <div class="cefr-speaking-results-card">
                            <div class="cefr-res-header">
                                <h4>${isHu ? `${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'))} Szóbeli értékelés` : `Informe oral ${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'))}`}</h4>
                                <span class="cefr-score-badge">${_state.speakingResult.totalScore} / 25 ${isHu ? 'pont' : 'puntos'}</span>
                            </div>
                            <p>${isHu ? 'Kimondott szavak száma:' : 'Palabras producidas:'} <strong>${_state.speakingResult.wordCount}</strong></p>
                            <p>${isHu ? 'Észlelt beszédkötőszavak:' : 'Conectores orales detectados:'} <em>${_esc(_state.speakingResult.foundConnectors.join(', ') || (isHu ? 'Egyik sem észlelhető' : 'Ninguno detectado'))}</em></p>
                        </div>
                    ` : ''}
                </div>
            `;
        }

        // Strategies Tab
        function _renderStrategiesTab() {
            const isHu = _id.includes('hu');
            if (!_data || !_data.strategies) return `<p class="cefr-empty">${isHu ? 'Nincsenek elérhető stratégiák.' : 'Guía no disponible.'}</p>`;
            const s = _data.strategies;

            return `
                <div class="cefr-strategies-wrapper">
                    <h3 class="cefr-sec-title">${_esc(s.title || (isHu ? 'Hivatalos vizsgaútmutató' : 'Guía oficial del examen'))}</h3>
                    
                    <div class="cefr-strat-grid">
                        ${(s.structure || []).map(item => `
                            <div class="cefr-strat-card">
                                <h4>${_esc(item.prueba)}</h4>
                                <p>${_esc(item.tip)}</p>
                            </div>
                        `).join('')}
                    </div>

                    <div class="cefr-connectors-section">
                        <h4>${isHu ? `Kötőszavak és szövegösszekötők (${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'))} szint)` : `Conectores y marcadores del discurso (Nivel ${(_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'))})`}</h4>
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
            const isHu = _id.includes('hu');
            const lvl = (_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')));
            const title = (_data && _data.title) || (isHu ? `ECL ${lvl} Nyelvvizsga` : `Prueba DELE ${lvl}`);
            const rTime = (_data && _data.skills && _data.skills.reading && _data.skills.reading.officialTimeMinutes) || 45;
            const wTime = (_data && _data.skills && _data.skills.writing && _data.skills.writing.officialTimeMinutes) || 45;
            const lTime = (_data && _data.skills && _data.skills.listening && _data.skills.listening.officialTimeMinutes) || 30;
            const sTime = (_data && _data.skills && _data.skills.speaking && _data.skills.speaking.officialTimeMinutes) || 15;
            const rTasks = (_data && _data.skills && _data.skills.reading && _data.skills.reading.tareas && _data.skills.reading.tareas.length) || 2;
            const wTasks = (_data && _data.skills && _data.skills.writing && _data.skills.writing.tareas && _data.skills.writing.tareas.length) || 2;
            const lTasks = (_data && _data.skills && _data.skills.listening && _data.skills.listening.tareas && _data.skills.listening.tareas.length) || 2;
            const sTasks = (_data && _data.skills && _data.skills.speaking && _data.skills.speaking.tareas && _data.skills.speaking.tareas.length) || 2;

            if (isHu) {
                return `
                    <div class="cefr-mocks-wrapper">
                        <div class="cefr-mock-intro-card">
                            <h3>Hivatalos ${_esc(title)} komplex próbavizsga (4 készség)</h3>
                            <p>A nemzetközi ECL vizsga négy különálló készséget mér fel, két fő vizsgarészre bontva:</p>
                            <div class="cefr-blocks-spec">
                                <div class="cefr-spec-card">
                                    <strong>1. rész: Írásbeli vizsga (50 pont)</strong>
                                    <ul>
                                        <li>Olvasásértés (${rTime} perc · ${rTasks} feladat · 25 pont)</li>
                                        <li>Írásbeli kommunikáció (${wTime} perc · ${wTasks} feladat · 25 pont)</li>
                                    </ul>
                                    <span class="cefr-pass-pill">Megfelelt: Legalább 30 / 50 pont (60%)</span>
                                </div>
                                <div class="cefr-spec-card">
                                    <strong>2. rész: Szóbeli vizsga (50 pont)</strong>
                                    <ul>
                                        <li>Hallásértés (${lTime} perc · ${lTasks} feladat · 25 pont)</li>
                                        <li>Szóbeli kommunikáció (${sTime} perc · ${sTasks} feladat · 25 pont)</li>
                                    </ul>
                                    <span class="cefr-pass-pill">Megfelelt: Legalább 30 / 50 pont (60%)</span>
                                </div>
                            </div>
                            <div class="cefr-mock-cta-wrap">
                                <button type="button" class="btn btn-primary cefr-mock-btn" data-action="start-full-mock">
                                    Teljes időmérős próbavizsga indítása
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }
            return `
                <div class="cefr-mocks-wrapper">
                    <div class="cefr-mock-intro-card">
                        <h3>Simulacro oficial ${_esc(title)} completo (4 Destrezas)</h3>
                        <p>El examen oficial evalúa las cuatro destrezas divididas en dos bloques eliminatorios:</p>
                        <div class="cefr-blocks-spec">
                            <div class="cefr-spec-card">
                                <strong>Bloque 1: Destrezas escritas (50 pts)</strong>
                                <ul>
                                    <li>Comprensión de lectura (${rTime} min · 25 pts)</li>
                                    <li>Expresión escrita (${wTime} min · 25 pts)</li>
                                </ul>
                                <span class="cefr-pass-pill">Apto: Mínimo 30 / 50 pts</span>
                            </div>
                            <div class="cefr-spec-card">
                                <strong>Bloque 2: Destrezas orales (50 pts)</strong>
                                <ul>
                                    <li>Comprensión auditiva (${lTime} min · 25 pts)</li>
                                    <li>Expresión oral (${sTime} min · 25 pts)</li>
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
            const isHu = _id.includes('hu');
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
            const passLabel = isHu ? 'MEGFELELT' : 'APTO';
            const inProgLabel = isHu ? 'FOLYAMATBAN' : 'EN PROCESO';

            const skillNames = {
                reading: isHu ? 'Olvasásértés' : 'Lectura',
                listening: isHu ? 'Hallásértés' : 'Audición',
                writing: isHu ? 'Írásbeli' : 'Escritura',
                speaking: isHu ? 'Szóbeli' : 'Oral'
            };

            return `
                <div class="cefr-history-wrapper">
                    <div class="cefr-history-summary">
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${totalAttempted}</span>
                            <span class="cefr-sum-label">${isHu ? 'Elvégzett feladatok' : 'Tareas realizadas'}</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct}%</span>
                            <span class="cefr-sum-label">${isHu ? 'Átlagos eredmény' : 'Puntuación media'}</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct >= 60 ? passLabel : (totalAttempted > 0 ? inProgLabel : '–')}</span>
                            <span class="cefr-sum-label">${isHu ? 'Összesített értékelés' : 'Calificación global'}</span>
                        </div>
                    </div>

                    <div class="cefr-history-table-card">
                        <h4>${isHu ? 'Részletes feladateredmények' : 'Registro detallado de tareas'}</h4>
                        ${rows.length === 0 ? `
                            <p class="cefr-empty">${isHu ? "Még nem fejeztél be egyetlen feladatot sem. Gyakorolj a 'Hivatalos feladattípusok' fülön!" : "Aún no has completado ninguna tarea. Entrena en la pestaña 'Tareas oficiales'."}</p>
                        ` : `
                            <table class="cefr-table">
                                <thead>
                                    <tr>
                                        <th>${isHu ? 'Készség' : 'Destreza'}</th>
                                        <th>${isHu ? 'Feladat' : 'Tarea'}</th>
                                        <th>${isHu ? 'Pontszám' : 'Puntos'}</th>
                                        <th>${isHu ? 'Százalék' : 'Porcentaje'}</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    ${rows.map(r => `
                                        <tr>
                                            <td><strong>${_esc(skillNames[r.skill] || r.skill)}</strong></td>
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
                    _state.listeningActiveItemId = null;
                    _state.listeningItemPasses = {};
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
            root.querySelectorAll('[data-action="play-single-item"]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const itemId = btn.dataset.itemId;
                    if (_state.listeningActiveItemId === itemId && _state.listeningPlaying) {
                        _stopListeningTimers();
                        render(_container);
                        return;
                    }

                    const tarea = _getCurrentTarea();
                    const item = (tarea.items || []).find(it => it.id === itemId);
                    if (!item || !item.audio || !item.audio.turns) return;

                    _stopListeningTimers();
                    _state.listeningActiveItemId = itemId;
                    _state.listeningPlaying = true;
                    _state.listeningItemPasses[itemId] = (_state.listeningItemPasses[itemId] || 0) + 1;
                    render(_container);

                    _playTurnSequence(item.audio.turns, 0, () => {
                        _state.listeningPlaying = false;
                        _state.listeningActiveItemId = null;
                        render(_container);
                    });
                });
            });

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
                    const items = tarea.items || tarea.questions || [];
                    let correct = 0;
                    items.forEach(q => {
                        if (_state.listeningAnswers[q.id] === q.correct) correct++;
                    });
                    _saveTaskScore('listening', tarea.id, correct, items.length);
                    render(_container);
                });
            }

            const resetListenBtn = root.querySelector('[data-action="reset-listening"]');
            if (resetListenBtn) {
                resetListenBtn.addEventListener('click', () => {
                    _state.listeningAnswers = {};
                    _state.listeningSubmitted = false;
                    _state.listeningPass = 1;
                    _state.listeningActiveItemId = null;
                    _state.listeningItemPasses = {};
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

    const DeleA1Exam = createModule({
        id: 'es-dele-a1-exam',
        dataFile: 'dele-a1-exam.json',
        title: 'Prueba DELE A1',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial A1'
    });

    const DeleA2Exam = createModule({
        id: 'es-dele-a2-exam',
        dataFile: 'dele-a2-exam.json',
        title: 'Prueba DELE A2',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial A2'
    });

    const DeleB1Exam = createModule({
        id: 'es-dele-b1-exam',
        dataFile: 'dele-b1-exam.json',
        title: 'Prueba DELE B1',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial B1'
    });

    const DeleB2Exam = createModule({
        id: 'es-dele-b2-exam',
        dataFile: 'dele-b2-exam.json',
        title: 'Prueba DELE B2',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial B2'
    });

    const EclA1Exam = createModule({
        id: 'hu-ecl-a1-exam',
        dataFile: 'ecl-a1-exam.json',
        title: 'ECL A1 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · A1 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclA2Exam = createModule({
        id: 'hu-ecl-a2-exam',
        dataFile: 'ecl-a2-exam.json',
        title: 'ECL A2 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · A2 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclB1Exam = createModule({
        id: 'hu-ecl-b1-exam',
        dataFile: 'ecl-b1-exam.json',
        title: 'ECL B1 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · B1 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclB2Exam = createModule({
        id: 'hu-ecl-b2-exam',
        dataFile: 'ecl-b2-exam.json',
        title: 'ECL B2 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · B2 szintű komplex nyelvvizsga-felkészítő'
    });

    return {
        createModule: createModule,
        DeleA1Exam: DeleA1Exam,
        DeleA2Exam: DeleA2Exam,
        DeleB1Exam: DeleB1Exam,
        DeleB2Exam: DeleB2Exam,
        EclA1Exam: EclA1Exam,
        EclA2Exam: EclA2Exam,
        EclB1Exam: EclB1Exam,
        EclB2Exam: EclB2Exam
    };
})();

// Export globally and for CommonJS tests
if (typeof window !== 'undefined') {
    window.CefrExam = CefrExam;
    window.DeleA1Exam = CefrExam.DeleA1Exam;
    window.DeleA2Exam = CefrExam.DeleA2Exam;
    window.DeleB1Exam = CefrExam.DeleB1Exam;
    window.DeleB2Exam = CefrExam.DeleB2Exam;
    window.EclA1Exam = CefrExam.EclA1Exam;
    window.EclA2Exam = CefrExam.EclA2Exam;
    window.EclB1Exam = CefrExam.EclB1Exam;
    window.EclB2Exam = CefrExam.EclB2Exam;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CefrExam;
}
