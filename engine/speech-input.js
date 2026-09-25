// ============================================
// SPEECH INPUT & EVALUATION ENGINE
// ============================================
// Provides speech-to-text recognition, microphone audio capture, live visualizer
// analysis, and fuzzy word-by-word pronunciation evaluation for Parlour.
//
// Designed to fix the core flaws of automated language speaking apps:
// 1. Transparent word-by-word breakdown (matched vs missed) rather than a black box.
// 2. Resilient speech recognition that doesn't fail users on minor ASR transcription quirks.
// 3. 2.8s automatic silence commit: learners take their time without needing to tap done.
// 4. Graceful fallback to self-evaluation when speech recognition is unavailable.
// 5. One-tap "Can't speak right now" preference to bypass voice drills when in public.

const SpeechInput = (function () {
    'use strict';

    function _getRecognitionClass() {
        if (typeof window === 'undefined') return null;
        return window.SpeechRecognition || window.webkitSpeechRecognition || null;
    }

    let _activeRecognition = null;
    let _mediaStream = null;
    let _mediaRecorder = null;
    let _recordedChunks = [];
    let _recordedAudioBlob = null;
    let _recordedAudioUrl = null;
    let _isListening = false;
    let _hasSpoken = false;
    let _listenStartTime = 0;
    let _isCloudSttSession = false;

    const CANT_SPEAK_KEY = 'parlour_cant_speak_until';
    const DEFAULT_STT_ENDPOINT = 'https://parlour-stt.gergkar.workers.dev/transcribe';
    const STT_ENDPOINT_KEY = 'parlour_stt_endpoint';
    const STT_MODE_KEY = 'parlour_stt_mode'; // 'auto' | 'cloud' | 'native'

    function getSttEndpoint() {
        try {
            const stored = localStorage.getItem(STT_ENDPOINT_KEY);
            if (stored === 'none' || stored === 'disabled') return null;
            return stored || DEFAULT_STT_ENDPOINT;
        } catch (e) {
            return DEFAULT_STT_ENDPOINT;
        }
    }

    function setSttEndpoint(url) {
        try {
            if (url) localStorage.setItem(STT_ENDPOINT_KEY, url);
            else localStorage.removeItem(STT_ENDPOINT_KEY);
        } catch (e) {}
    }

    function getSttMode() {
        try {
            return localStorage.getItem(STT_MODE_KEY) || 'auto';
        } catch (e) {
            return 'auto';
        }
    }

    function setSttMode(mode) {
        try {
            if (mode) localStorage.setItem(STT_MODE_KEY, mode);
            else localStorage.removeItem(STT_MODE_KEY);
        } catch (e) {}
    }

    function isCloudSttAvailable() {
        return !!getSttEndpoint() && typeof fetch === 'function';
    }

    async function transcribeBlob(audioBlob, lang, hint) {
        const endpoint = getSttEndpoint();
        if (!endpoint) throw new Error('No STT endpoint configured');

        const cleanLang = (lang || getSpeechLang() || 'es').split(/[-_]/)[0];
        const hintList = (Array.isArray(hint) ? hint : [hint]).filter(Boolean);
        const cleanHint = hintList.join(' · ').replace(/\s+/g, ' ').trim().slice(0, 240);

        let url = `${endpoint}${endpoint.includes('?') ? '&' : '?'}lang=${encodeURIComponent(cleanLang)}`;
        if (cleanHint) {
            url += `&prompt=${encodeURIComponent(cleanHint)}`;
        }

        const type = (audioBlob && audioBlob.type) || 'audio/webm';
        const headers = {
            'Content-Type': type,
            'X-Language': cleanLang
        };
        if (cleanHint) {
            headers['X-Prompt'] = cleanHint;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers,
            body: audioBlob
        });

        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.error || `STT HTTP ${response.status}`);
        }

        const data = await response.json();
        const rawText = stripWhisperHallucinations((data && (data.text || data.transcript || '')).trim());
        return hint ? canonicalizeTranscript(hint, rawText, cleanLang) : rawText;
    }

    // ---- Browser Support & State ----
    function isRecognitionSupported() {
        return !!_getRecognitionClass();
    }

    function isRecordingSupported() {
        return !!(typeof navigator !== 'undefined' && navigator.mediaDevices && navigator.mediaDevices.getUserMedia && (typeof MediaRecorder !== 'undefined' || (typeof window !== 'undefined' && window.MediaRecorder)));
    }

    function canSpeakNow() {
        try {
            const until = parseInt(localStorage.getItem(CANT_SPEAK_KEY) || '0', 10);
            return Date.now() > until;
        } catch (e) {
            return true;
        }
    }

    function setCantSpeakNow(durationMinutes = 10) {
        try {
            const until = Date.now() + (durationMinutes * 60 * 1000);
            localStorage.setItem(CANT_SPEAK_KEY, String(until));
        } catch (e) {}
    }

    function resetCantSpeakNow() {
        try {
            localStorage.removeItem(CANT_SPEAK_KEY);
        } catch (e) {}
    }

    // Language code mapper (e.g. 'es-latam' -> 'es-MX', 'es-es' -> 'es-ES', 'hu' -> 'hu-HU')
    function getSpeechLang() {
        if (typeof Lang !== 'undefined') {
            const code = Lang.code();
            if (code === 'es-latam' || code === 'es') return 'es-MX';
            if (code === 'es-es') return 'es-ES';
            if (code === 'hu') return 'hu-HU';
            return code;
        }
        return 'es-ES';
    }

    // Clean up any previously recorded audio blob URL to prevent memory leaks
    function _cleanAudioUrl() {
        if (_recordedAudioUrl) {
            URL.revokeObjectURL(_recordedAudioUrl);
            _recordedAudioUrl = null;
        }
        _recordedAudioBlob = null;
    }

    function getRecordedAudioUrl() {
        return _recordedAudioUrl;
    }

    let _finishTimeout = null;
    let _meterInterval = null;
    let _initialSilenceTimeout = null;
    let _maxDurationTimeout = null;
    let _onFinalCallback = null;
    let _onAudioReadyCallback = null;
    let _accumulatedFinal = '';
    let _currentInterim = '';
    let _bestTranscript = '';

    let _audioCtx = null;
    let _audioAnalyser = null;
    let _audioDataArray = null;

    function _cleanupAudioAnalysis() {
        if (_audioCtx) {
            try {
                if (_audioCtx.state !== 'closed' && typeof _audioCtx.close === 'function') {
                    _audioCtx.close().catch(() => {});
                }
            } catch (e) {}
            _audioCtx = null;
        }
        _audioAnalyser = null;
        _audioDataArray = null;
    }

    function _cleanupTimers() {
        _cleanupAudioAnalysis();
        if (_finishTimeout) {
            clearTimeout(_finishTimeout);
            _finishTimeout = null;
        }
        if (_initialSilenceTimeout) {
            clearTimeout(_initialSilenceTimeout);
            _initialSilenceTimeout = null;
        }
        if (_meterInterval) {
            clearInterval(_meterInterval);
            _meterInterval = null;
        }
        if (_maxDurationTimeout) {
            clearTimeout(_maxDurationTimeout);
            _maxDurationTimeout = null;
        }
    }

    let _sessionToken = 0;
    let _streamIdleTimer = null;

    function _clearStreamIdleTimer() {
        if (_streamIdleTimer) {
            clearTimeout(_streamIdleTimer);
            _streamIdleTimer = null;
        }
    }

    function _stopTracks() {
        _clearStreamIdleTimer();
        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        }
        _mediaRecorder = null;
        if (_mediaStream) {
            _mediaStream.getTracks().forEach(track => {
                try { track.stop(); } catch (e) {}
            });
            _mediaStream = null;
        }
    }

    function releaseStream() {
        _stopTracks();
    }

    function _cleanupRecognition() {
        if (_activeRecognition) {
            try {
                _activeRecognition.onstart = null;
                _activeRecognition.onresult = null;
                _activeRecognition.onerror = null;
                _activeRecognition.onend = null;
                _activeRecognition.abort();
            } catch (e) {}
            _activeRecognition = null;
        }
    }

    // Capture audio stream for user playback and unsupported browser fallback
    function _startRecordingStream(options = {}) {
        if (!isRecordingSupported()) return;

        const lang = options.lang || getSpeechLang();
        _clearStreamIdleTimer();
        const currentToken = ++_sessionToken;

        // Create the level-meter AudioContext now, synchronously inside the tap
        // that started listening. iOS Safari leaves a context created later (in
        // the getUserMedia .then) suspended, so the meter reads silence forever
        // and the initial-silence timer reports 'no-speech' after 10s.
        _cleanupAudioAnalysis();
        const AudioCtx = (typeof window !== 'undefined' && (window.AudioContext || window.webkitAudioContext));
        if (AudioCtx) {
            try {
                _audioCtx = new AudioCtx();
                if (_audioCtx.state === 'suspended' && typeof _audioCtx.resume === 'function') {
                    _audioCtx.resume().catch(() => {});
                }
            } catch (e) {
                _audioCtx = null;
            }
        }
        const meterCtx = _audioCtx;

        function _setupRecorder(stream) {
            if (!_isListening || currentToken !== _sessionToken) return;
            _mediaStream = stream;

            try {
                if (meterCtx && _audioCtx === meterCtx) {
                    if (_audioCtx.state === 'suspended' && typeof _audioCtx.resume === 'function') {
                        _audioCtx.resume().catch(() => {});
                    }
                    const source = _audioCtx.createMediaStreamSource(stream);
                    _audioAnalyser = _audioCtx.createAnalyser();
                    _audioAnalyser.fftSize = 64;
                    _audioAnalyser.smoothingTimeConstant = 0.3;
                    source.connect(_audioAnalyser);
                    _audioDataArray = new Uint8Array(_audioAnalyser.frequencyBinCount);
                }
            } catch (e) {}

            let mimeType = '';
            if (window.MediaRecorder && typeof MediaRecorder.isTypeSupported === 'function') {
                if (MediaRecorder.isTypeSupported('audio/webm;codecs=opus')) mimeType = 'audio/webm;codecs=opus';
                else if (MediaRecorder.isTypeSupported('audio/webm')) mimeType = 'audio/webm';
                else if (MediaRecorder.isTypeSupported('audio/mp4')) mimeType = 'audio/mp4';
                else if (MediaRecorder.isTypeSupported('audio/aac')) mimeType = 'audio/aac';
            }

            try {
                _mediaRecorder = mimeType ? new MediaRecorder(stream, { mimeType }) : new MediaRecorder(stream);
            } catch (e) {
                try {
                    _mediaRecorder = new MediaRecorder(stream);
                } catch (e2) {
                    console.warn('SpeechInput: MediaRecorder initialization failed:', e2);
                    _mediaRecorder = null;
                    return;
                }
            }

            _recordedChunks = [];
            _mediaRecorder.ondataavailable = e => {
                if (currentToken === _sessionToken && e.data && e.data.size > 0) {
                    _recordedChunks.push(e.data);
                }
            };

            _mediaRecorder.onstop = async () => {
                if (currentToken === _sessionToken && _recordedChunks.length > 0) {
                    _cleanAudioUrl();
                    const type = (_mediaRecorder && _mediaRecorder.mimeType) || mimeType || 'audio/webm';
                    _recordedAudioBlob = new Blob(_recordedChunks, { type });
                    _recordedAudioUrl = URL.createObjectURL(_recordedAudioBlob);
                    if (options.onAudioReady) options.onAudioReady(_recordedAudioUrl);
                    if (_onAudioReadyCallback) _onAudioReadyCallback(_recordedAudioUrl);

                    if (_isCloudSttSession && _onFinalCallback) {
                        const cb = _onFinalCallback;
                        _onFinalCallback = null;
                        const onStatus = options.onStatusChange || null;
                        if (onStatus) onStatus('analyzing');
                        try {
                            const transcript = await transcribeBlob(_recordedAudioBlob, lang, options.target);
                            cb(transcript || '');
                        } catch (err) {
                            console.warn('SpeechInput: Cloud STT transcription failed:', err);
                            const onErr = options.onError || null;
                            if (onErr) onErr('stt-failed');
                            else cb('');
                        }
                    }
                }
            };

            try {
                _mediaRecorder.start(100);
            } catch (e) {
                try {
                    _mediaRecorder.start();
                } catch (e2) {
                    console.warn('SpeechInput: mediaRecorder.start failed:', e2);
                }
            }
        }

        // Reuse warm stream if still active and has live audio tracks
        if (_mediaStream && _mediaStream.active && _mediaStream.getAudioTracks().some(t => t.readyState === 'live')) {
            _setupRecorder(_mediaStream);
            return;
        }

        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(stream => {
                _setupRecorder(stream);
            })
            .catch(err => {
                console.warn('SpeechInput: audio recording stream unavailable:', err);
                if (!isRecognitionSupported() || !_activeRecognition) {
                    _isListening = false;
                    const onError = options.onError || (() => {});
                    onError('permission-denied');
                }
            });
    }

    // ---- Start Voice Capture & Recognition ----
    function startListening(options = {}) {
        if (_isListening) {
            stopListening();
        } else {
            _cleanupRecognition();
            _stopTracks();
        }

        _cleanAudioUrl();
        _cleanupTimers();
        _recordedChunks = [];
        _accumulatedFinal = '';
        _currentInterim = '';
        _bestTranscript = '';
        _hasSpoken = false;
        _isListening = true;
        _listenStartTime = Date.now();

        const lang = options.lang || getSpeechLang();
        const target = options.target || null;
        const onInterim = options.onInterim || (() => {});
        const onFinal = options.onFinal || (() => {});
        const onError = options.onError || (() => {});
        const onAudioLevel = options.onAudioLevel || null;
        _onFinalCallback = onFinal;
        _onAudioReadyCallback = options.onAudioReady || null;

        const manualStop = !!options.manualStop;
        const maxDurationMs = options.maxDurationMs || (manualStop ? 300000 : 30000);

        // Allow learner to read prompt/prepare before speaking (30s in manual mode, 10s in quick drills)
        _initialSilenceTimeout = setTimeout(() => {
            if (_isListening && !_hasSpoken && !manualStop) {
                // In a cloud session, a meter that never got a running AudioContext
                // can't tell silence from speech -- send the recording to Whisper
                // (stopListening does) instead of declaring 'no-speech'.
                const meterBlind = _isCloudSttSession && !(_audioCtx && _audioCtx.state === 'running');
                stopListening();
                if (meterBlind) return;
                onError('no-speech');
            }
        }, manualStop ? 30000 : 10000);

        // Safety cap: default 30s for quick drills, up to 5 minutes (300s) for extended verbal production
        _maxDurationTimeout = setTimeout(() => {
            if (_isListening) {
                stopListening();
            }
        }, maxDurationMs);

        if (onAudioLevel) {
            let simAngle = 0;
            _meterInterval = setInterval(() => {
                if (!_isListening) return;

                let realLevel = 0;
                let isHearing = false;

                if (_audioAnalyser && _audioDataArray) {
                    try {
                        _audioAnalyser.getByteFrequencyData(_audioDataArray);
                        let sum = 0;
                        for (let i = 0; i < _audioDataArray.length; i++) sum += _audioDataArray[i];
                        const avg = sum / _audioDataArray.length;
                        realLevel = Math.min(1.0, Math.max(0, avg / 90));
                        if (realLevel > 0.08) {
                            _hasSpoken = true;
                            isHearing = true;
                        }
                    } catch (e) {}
                }

                // Automatic silence commit for Cloud STT sessions (matches native STT behavior)
                if (_isCloudSttSession && !manualStop) {
                    if (isHearing) {
                        if (_initialSilenceTimeout) {
                            clearTimeout(_initialSilenceTimeout);
                            _initialSilenceTimeout = null;
                        }
                        if (_finishTimeout) {
                            clearTimeout(_finishTimeout);
                            _finishTimeout = null;
                        }
                    } else if (_hasSpoken && !_finishTimeout) {
                        _finishTimeout = setTimeout(() => {
                            if (_isListening) stopListening();
                        }, 2200);
                    }
                }

                if (realLevel < 0.05) {
                    simAngle += 0.2;
                    const basePulse = _hasSpoken ? 0.22 : 0.08 + Math.sin(simAngle) * 0.05;
                    realLevel = Math.max(realLevel, basePulse);
                }

                onAudioLevel(realLevel, { isHearingVoice: isHearing, hasSpoken: _hasSpoken });
            }, 60);
        }

        const RecognitionClass = _getRecognitionClass();

        // Mobile browsers (both iOS WebKit and Android Chrome) require single-shot recognition (continuous: false).
        // Android Chrome does not support continuous: true reliably and aborts or fires premature no-speech errors.
        const isMobile = typeof navigator !== 'undefined' && (
            /iPad|iPhone|iPod|Android/i.test(navigator.userAgent) ||
            (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)
        );

        const isAndroid = typeof navigator !== 'undefined' && /Android/i.test(navigator.userAgent);

        // STT Provider resolution: 'auto' (default), 'cloud', 'native'
        const requestedProvider = options.sttProvider || 'auto';
        let useCloudStt = false;
        if (requestedProvider === 'cloud') {
            useCloudStt = isCloudSttAvailable();
        } else if (requestedProvider === 'native') {
            useCloudStt = false;
        } else {
            const pref = getSttMode();
            if (pref === 'cloud') {
                useCloudStt = isCloudSttAvailable();
            } else if (pref === 'native') {
                useCloudStt = false;
            } else if (options.preferRecording && isMobile && isCloudSttAvailable()) {
                useCloudStt = true;
            } else if (!RecognitionClass && isCloudSttAvailable()) {
                useCloudStt = true;
            }
        }

        _isCloudSttSession = useCloudStt;

        // 1. Primary: Native SpeechRecognition Engine
        if (RecognitionClass && !_isCloudSttSession) {
            function _startRecognitionInstance() {
                if (!_isListening) return;
                try {
                    const recognition = new RecognitionClass();
                    recognition.lang = lang;
                    recognition.continuous = !isMobile;
                    recognition.interimResults = true;
                    recognition.maxAlternatives = 1;

                    recognition.onstart = () => {
                        _isListening = true;
                    };

                    recognition.onresult = event => {
                        if (!_isListening) return;

                        let interim = '';
                        for (let i = event.resultIndex; i < event.results.length; ++i) {
                            const item = event.results[i];
                            if (item && item[0]) {
                                if (item.isFinal) {
                                    const text = item[0].transcript.trim();
                                    if (text) {
                                        _accumulatedFinal += (_accumulatedFinal ? ' ' : '') + text;
                                    }
                                } else {
                                    interim += item[0].transcript;
                                }
                            }
                        }
                        _currentInterim = interim;
                        const rawCombined = (_accumulatedFinal + ' ' + _currentInterim).trim();
                        const combined = (target && rawCombined) ? canonicalizeTranscript(target, rawCombined) : rawCombined;

                        if (combined) {
                            _hasSpoken = true;
                            _bestTranscript = combined;
                            if (_initialSilenceTimeout) {
                                clearTimeout(_initialSilenceTimeout);
                                _initialSilenceTimeout = null;
                            }

                            onInterim(combined);
                            if (onAudioLevel) {
                                onAudioLevel(0.5 + Math.random() * 0.45);
                            }

                            // Auto-stop recording immediately if learner hits 100% accuracy on target
                            if (target) {
                                const targetList = Array.isArray(target) ? target : [target];
                                const fullMatch = targetList.some(tgt => isFullTargetMatch(tgt, combined));
                                if (fullMatch) {
                                    stopListening();
                                    return;
                                }
                            }

                            // Silence buffer: automatically finish 2.8s after learner stops speaking (in auto mode only)
                            if (!manualStop) {
                                if (_finishTimeout) clearTimeout(_finishTimeout);
                                _finishTimeout = setTimeout(() => {
                                    stopListening();
                                }, 2800);
                            }
                        }
                    };

                    recognition.onerror = event => {
                        console.warn('SpeechInput recognition error:', event.error);
                        const combined = (_accumulatedFinal + ' ' + _currentInterim).trim() || _bestTranscript || '';
                        const isFatal = event.error === 'not-allowed' || event.error === 'service-not-allowed';

                        // Manual mode (Verbal Production, up to 5 minutes) only ends on
                        // Finish or the max-duration timeout -- once the learner has
                        // started speaking, a transient recognition error (aborted,
                        // no-speech, network) is routine mid-session, not the end of
                        // their turn. Restart instead of committing early (same as
                        // onend below), or a long recording gets cut off at whatever
                        // point the browser's recognition session happens to hiccup.
                        if (manualStop && _hasSpoken && !isFatal) {
                            try {
                                _startRecognitionInstance();
                                return;
                            } catch (e) {
                                console.warn('SpeechInput: recognition restart threw:', e);
                            }
                        }

                        // If the learner already spoke or a transcript was captured, any subsequent silence / no-speech
                        // error from the OS simply marks the end of their speech — never report an error!
                        if (_hasSpoken || combined) {
                            stopListening();
                            return;
                        }

                        if (event.error === 'no-speech') {
                            if (manualStop) return;

                            // If learner hasn't spoken yet and still within initial grace period, keep waiting
                            if (Date.now() - _listenStartTime < 10000) {
                                return;
                            }
                            stopListening();
                            onError('no-speech');
                        } else if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
                            stopListening();
                            onError('permission-denied');
                        } else if (event.error === 'aborted') {
                            stopListening();
                        } else if (event.error === 'network') {
                            stopListening();
                            onError('network');
                        } else {
                            stopListening();
                            onError(event.error || 'recognition-failed');
                        }
                    };

                    recognition.onend = () => {
                        if (!_isListening || _activeRecognition !== recognition) return;

                        const combined = (_accumulatedFinal + ' ' + _currentInterim).trim() || _bestTranscript || '';

                        // Manual mode only ends on Finish/max-duration -- native
                        // recognition sessions commonly end on their own well before
                        // then (most browsers cap a single continuous session at
                        // roughly a minute, or end after a short pause), so this is
                        // not "the learner is done." Restart instead of committing.
                        if (manualStop && _hasSpoken) {
                            try {
                                _startRecognitionInstance();
                                return;
                            } catch (e) {
                                console.warn('SpeechInput: recognition restart threw:', e);
                            }
                        }

                        // If learner already spoke, their utterance has completed — commit the answer immediately
                        if (_hasSpoken || combined) {
                            stopListening();
                            return;
                        }

                        // If learner hasn't spoken yet and still within initial grace period, keep listening
                        if (Date.now() - _listenStartTime < (manualStop ? 30000 : 10000)) {
                            try {
                                _startRecognitionInstance();
                                return;
                            } catch (e) {
                                console.warn('SpeechInput: recognition restart threw:', e);
                            }
                        }

                        // Grace period expired without speech
                        stopListening();
                        onError('no-speech');
                    };

                    _activeRecognition = recognition;
                    recognition.start();
                } catch (e) {
                    console.warn('SpeechInput: recognition start threw:', e);
                    _activeRecognition = null;
                }
            }

            _startRecognitionInstance();
        }

        // 2. Microphone audio recording for user playback and unsupported browser fallback
        // On mobile devices (both iOS WebKit and Android), getUserMedia and webkitSpeechRecognition
        // cannot run concurrently without microphone contention: the OS audio session / HAL strictly
        // allows only one active recording client, and getUserMedia locks the hardware, starving
        // SpeechRecognition of audio samples. As a result, SpeechRecognition receives silence:
        // audio is recorded into the blob (and can be replayed), but no transcript is ever produced
        // and speech recognition fails completely.
        // Therefore, on mobile devices (iOS and Android), SpeechRecognition gets exclusive microphone
        // access whenever native STT is available. Audio recording for playback runs only when native
        // STT is unsupported (fallback self-evaluation mode), or on desktop where concurrent capture
        // is fully supported by the platform's audio subsystem.
        const canRecordConcurrently = !isMobile;
        const needsAudioRecording = _isCloudSttSession || !RecognitionClass || (!!options.onAudioReady && canRecordConcurrently);
        if (isRecordingSupported() && needsAudioRecording) {
            _startRecordingStream(options);
        } else if (!RecognitionClass && !_isCloudSttSession && !isRecordingSupported()) {
            _isListening = false;
            onError('not-supported');
        }
    }

    function stopListening() {
        const wasListening = _isListening;
        const isCloud = _isCloudSttSession;
        _isListening = false;
        _cleanupTimers();
        _cleanupRecognition();

        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        }
        _stopTracks();

        const finalText = (_accumulatedFinal + ' ' + _currentInterim).trim() || _bestTranscript || '';
        _accumulatedFinal = '';
        _currentInterim = '';
        _bestTranscript = '';

        if (wasListening && _onFinalCallback && !isCloud) {
            const cb = _onFinalCallback;
            _onFinalCallback = null;
            cb(finalText || '');
        }
    }

    // ---- Text Normalization & Fuzzy Token Matching ----
    function normalizeForSpeech(text) {
        return String(text || '')
            .toLowerCase()
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '') // remove accent marks for relaxed comparison
            .replace(/[¿?¡!.,;:«»"'\(\)\/\-_–—]/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    // Splits on whitespace, colons between digits, hyphens, dashes, and punctuation
    // so signs (e.g. -, --, --, quotes) don't form phantom tokens that lower accuracy.
    function tokenize(text) {
        const cleaned = String(text || '')
            .replace(/(\d):(\d)/g, '$1 $2')
            .replace(/[-–—/\\()[\]{}«»"“”'’¿?¡!.,;:*~_+=]/g, ' ')
            .trim();
        const rawTokens = cleaned.split(/\s+/).filter(Boolean);
        return rawTokens.map(raw => ({
            raw,
            norm: normalizeForSpeech(raw)
        })).filter(t => t.norm.length > 0);
    }

    // Word-level Levenshtein distance
    function levenshtein(a, b) {
        const matrix = [];
        for (let i = 0; i <= b.length; i++) matrix[i] = [i];
        for (let j = 0; j <= a.length; j++) matrix[0][j] = j;

        for (let i = 1; i <= b.length; i++) {
            for (let j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1, // substitution
                        matrix[i][j - 1] + 1,     // insertion
                        matrix[i - 1][j] + 1      // deletion
                    );
                }
            }
        }
        return matrix[b.length][a.length];
    }

    const WHISPER_HALLUCINATION_PATTERNS = [
        /subt[íi]tulos\s+(realizados|creados|hechos|por)\b[^.?!]*/gi,
        /subtitulado\s+por\b[^.?!]*/gi,
        /amara\.org/gi,
        /suscr[íi]bete\s+al\s+canal[^.?!]*/gi,
        /gracias\s+por\s+ver(\s+el\s+v[íi]deo)?[^.?!]*/gi,
        /feliratozta\b[^.?!]*/gi,
        /a\s+feliratokat\s+k[ée]sz[íi]tette\b[^.?!]*/gi,
        /k[öo]sz[öo]n[öo]m\s+a\s+figyelmet[^.?!]*/gi,
        /subtitles\s+by\b[^.?!]*/gi,
        /thank\s+you\s+for\s+watching[^.?!]*/gi
    ];

    function stripWhisperHallucinations(text) {
        if (!text) return '';
        let cleaned = String(text);
        for (const pattern of WHISPER_HALLUCINATION_PATTERNS) {
            cleaned = cleaned.replace(pattern, '');
        }
        return cleaned.replace(/\s+/g, ' ').trim();
    }

    function _detectPhoneticLang(langHint, textSample) {
        if (langHint) {
            const l = String(langHint).toLowerCase();
            if (l.startsWith('hu')) return 'hu';
            if (l.startsWith('es')) return 'es';
        }
        if (textSample) {
            const s = String(textSample);
            if (/[őűŐŰ]|\b(hogy|vagy|laksz|szia|köszönöm|milyen)\b|(gy|sz|zs|cs|ly|ny|ty)/i.test(s)) {
                return 'hu';
            }
            if (/[ñ¿¡]/i.test(s)) {
                return 'es';
            }
        }
        const active = getSpeechLang();
        if (active && active.toLowerCase().startsWith('hu')) return 'hu';
        return 'es';
    }

    // Hungarian phonetic folding: resolves Hungarian digraph homophones and assimilations
    // while preserving Hungarian 'h' and 'b'/'v' distinctions.
    function phoneticFoldHu(word) {
        if (!word) return '';
        return String(word)
            .toLowerCase()
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '')
            .replace(/x/g, 'ksz')
            .replace(/ggy|gyj|dj/g, 'gy')
            .replace(/tty|tyj|tj/g, 'ty')
            .replace(/nny|nyj|nj/g, 'ny')
            .replace(/ly|jj/g, 'j')
            .replace(/ccs|tsz|ts/g, 'cs')
            .replace(/ddzs|dzsj|ds/g, 'dzs')
            .replace(/szs/g, 's')
            .replace(/ssz/g, 'sz')
            .replace(/(.)\1+/g, '$1');
    }

    // Spanish phonetic folding: resolves betacismo (b/v), silent h, seseo (z/ce/ci <-> s),
    // yeísmo (ll <-> y, word-final -y <-> -i), g/j before e/i, c/qu/k velars, and sinalefa
    // vowel fusions across word boundaries (e.g. 'voy a hablar' <-> 'voy hablar', 'a ver' <-> 'haber').
    function phoneticFoldEs(word) {
        if (!word) return '';
        return String(word)
            .toLowerCase()
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '')
            .replace(/ch/g, '\u010d')      // protect 'ch' (/tʃ/) before stripping silent 'h'
            .replace(/h/g, '')             // silent 'h' ('hola' <-> 'ola', 'haber' <-> 'a ver', 'hablar' <-> 'ablar')
            .replace(/ll/g, 'y')           // yeísmo ('valla' <-> 'vaya', 'calló' <-> 'cayó', 'pollo' <-> 'poyo')
            .replace(/y$/g, 'i')           // word-final '-y' /i/ ('hay' <-> 'ahí' <-> 'ay', 'hoy' <-> 'oi')
            .replace(/v/g, 'b')            // betacismo ('vaca' <-> 'baca', 'tubo' <-> 'tuvo', 'vienes' <-> 'bienes')
            .replace(/que/g, 'ke')
            .replace(/qui/g, 'ki')
            .replace(/ce/g, 'se')          // seseo ('cena' <-> 'sena', 'cocer' <-> 'coser', 'hice' <-> 'hise')
            .replace(/ci/g, 'si')          // seseo ('cien' <-> 'sien', 'cierra' <-> 'sierra')
            .replace(/z/g, 's')            // seseo ('casa' <-> 'caza', 'vez' <-> 'ves', 'haz' <-> 'has')
            .replace(/ge/g, 'je')          // velar fricative ('gente' <-> 'jente', 'coger' <-> 'cojer')
            .replace(/gi/g, 'ji')          // velar fricative ('elegir' <-> 'elejir', 'gira' <-> 'jira')
            .replace(/gue/g, 'ge')
            .replace(/gui/g, 'gi')
            .replace(/ca/g, 'ka')
            .replace(/co/g, 'ko')
            .replace(/cu/g, 'ku')
            .replace(/qu/g, 'k')
            .replace(/x/g, 'ks')
            .replace(/(.)\1+/g, '$1');     // collapse adjacent duplicates ('rr'->'r', sinalefa 'aa'->'a', 'ee'->'e')
    }

    function phoneticFold(word, langHint) {
        if (!word) return '';
        const lang = _detectPhoneticLang(langHint, word);
        return lang === 'hu' ? phoneticFoldHu(word) : phoneticFoldEs(word);
    }

    // Check if two individual words are phonetically close enough
    function isWordMatch(targetNorm, recNorm, langHint) {
        if (!targetNorm || !recNorm) return false;
        if (targetNorm === recNorm) return true;

        const lang = _detectPhoneticLang(langHint, `${targetNorm} ${recNorm}`);
        const targetFold = lang === 'hu' ? phoneticFoldHu(targetNorm) : phoneticFoldEs(targetNorm);
        const recFold = lang === 'hu' ? phoneticFoldHu(recNorm) : phoneticFoldEs(recNorm);
        if (targetFold && targetFold === recFold) return true;

        // Number words vs digits tolerance (e.g. "dos" vs "2"); Hungarian
        // words included alongside Spanish since spoken numbers rarely
        // collide across the two languages. "ket" covers Hungarian "két",
        // the form used before a noun, alongside the standalone "kettő".
        const numMap = {
            '1': ['uno', 'una', 'un', 'egy'], '2': ['dos', 'ketto', 'ket'], '3': ['tres', 'harom'],
            '4': ['cuatro', 'negy'], '5': ['cinco', 'ot'], '6': ['seis', 'hat'],
            '7': ['siete', 'het'], '8': ['ocho', 'nyolc'], '9': ['nueve', 'kilenc'],
            '10': ['diez', 'tiz']
        };
        if ((numMap[recNorm] || []).includes(targetNorm) || (numMap[targetNorm] || []).includes(recNorm)) return true;

        // Abbreviation & contraction equivalence
        const abbrMap = { 'db': 'darab', 'pa': 'para', 'pal': 'parael', 'al': 'ael', 'del': 'deel' };
        if (abbrMap[recNorm] === targetNorm || abbrMap[targetNorm] === recNorm) return true;

        // Short words (<= 3 chars) need exact or phonetic match
        if (targetNorm.length <= 3) return false;

        // Allow Levenshtein distance 1 for 4-7 chars, 2 for 8+ chars (on raw norm or phonetic fold)
        const maxDist = targetNorm.length >= 8 ? 2 : 1;
        if (levenshtein(targetNorm, recNorm) <= maxDist) return true;
        if (targetFold.length >= 4 && levenshtein(targetFold, recFold) <= (targetFold.length >= 8 ? 2 : 1)) return true;
        return false;
    }

    // Boundary merge/split check: requires exact normalized or phoneticFold equality
    // so 1-letter words (like Spanish 'a') are only merged when a genuine phonetic fusion
    // occurred (e.g. 'va'+'a' -> 'ba' === 'va', 'a'+'hablar' -> 'ablar' === 'hablar',
    // 'a'+'ver' -> 'aber' === 'haber', 'hol'+'laksz' -> 'holaksz' === 'hollax'),
    // and never swallowed by a 1-char Levenshtein deletion on an unrelated word like 'vamos'.
    function isBoundaryMergeMatch(mergedNorm, singleNorm, lang) {
        if (!mergedNorm || !singleNorm) return false;
        if (mergedNorm === singleNorm) return true;
        const mFold = lang === 'hu' ? phoneticFoldHu(mergedNorm) : phoneticFoldEs(mergedNorm);
        const sFold = lang === 'hu' ? phoneticFoldHu(singleNorm) : phoneticFoldEs(singleNorm);
        return !!(mFold && mFold === sFold);
    }

    // Evaluates target sentence against spoken transcript with word-by-word alignment
    // and multi-token word boundary handling (merged compounds/sinalefa like 'hol laksz' -> 'hollax',
    // 'voy a hablar' -> 'voy hablar', 'vamos a ver' -> 'vamos haber', 'por qué' <-> 'porque').
    function evaluate(targetSentence, recognizedTranscript, langHint) {
        const cleanedTranscript = stripWhisperHallucinations(recognizedTranscript);
        const targetTokens = tokenize(targetSentence);
        const recTokens = tokenize(cleanedTranscript);
        const lang = _detectPhoneticLang(langHint, `${targetSentence || ''} ${cleanedTranscript || ''}`);

        if (!targetTokens.length) {
            return { isCorrect: true, accuracy: 100, words: [], transcript: cleanedTranscript };
        }

        // Align target tokens with recognized tokens
        const matchedIndices = new Set();
        const wordResults = [];
        let recPointer = 0;

        for (let i = 0; i < targetTokens.length; i++) {
            const t = targetTokens[i];
            let found = false;

            // Check if t + nextT fused into a single recognized token (e.g. 'hol laksz' -> 'hollax',
            // 'a ver' -> 'haber', 'voy a hablar' -> 'voy hablar', or leftward sinalefa 'va a ir' -> 'va ir')
            // when the following recognized token does not separately match nextT.
            if (i + 1 < targetTokens.length) {
                const nextT = targetTokens[i + 1];
                const mergedTargetNorm = t.norm + nextT.norm;
                for (let j = recPointer; j < recTokens.length; j++) {
                    if (matchedIndices.has(j)) continue;
                    if (isBoundaryMergeMatch(mergedTargetNorm, recTokens[j].norm, lang)) {
                        const nextRecExistsAndMatchesNextT = (j + 1 < recTokens.length) &&
                            !matchedIndices.has(j + 1) &&
                            isWordMatch(nextT.norm, recTokens[j + 1].norm, lang);
                        if (!nextRecExistsAndMatchesNextT) {
                            matchedIndices.add(j);
                            recPointer = Math.max(recPointer, j + 1);
                            wordResults.push({ word: t.raw, status: 'matched' });
                            wordResults.push({ word: nextT.raw, status: 'matched' });
                            i++; // Advance past nextT since both target tokens are matched
                            found = true;
                            break;
                        }
                    }
                }
                if (found) continue;
            }

            // 1. Search ahead up to 3 tokens in recognized list for 1-to-1 match
            const searchEnd = Math.min(recTokens.length, recPointer + 4);
            for (let j = recPointer; j < searchEnd; j++) {
                if (!matchedIndices.has(j) && isWordMatch(t.norm, recTokens[j].norm, lang)) {
                    matchedIndices.add(j);
                    recPointer = j + 1;
                    found = true;
                    break;
                }
            }

            // If not found ahead, scan backwards once if missed
            if (!found) {
                for (let j = 0; j < recTokens.length; j++) {
                    if (!matchedIndices.has(j) && isWordMatch(t.norm, recTokens[j].norm, lang)) {
                        matchedIndices.add(j);
                        found = true;
                        break;
                    }
                }
            }

            // 2. Fallback 2-to-1 merged boundary scan across all remaining tokens
            if (!found && i + 1 < targetTokens.length) {
                const nextT = targetTokens[i + 1];
                const mergedTargetNorm = t.norm + nextT.norm;
                for (let j = 0; j < recTokens.length; j++) {
                    if (!matchedIndices.has(j) && isBoundaryMergeMatch(mergedTargetNorm, recTokens[j].norm, lang)) {
                        matchedIndices.add(j);
                        recPointer = Math.max(recPointer, j + 1);
                        wordResults.push({ word: t.raw, status: 'matched' });
                        wordResults.push({ word: nextT.raw, status: 'matched' });
                        i++;
                        found = true;
                        break;
                    }
                }
                if (found) continue;
            }

            // 3. 1-to-2 split boundary match: ASR split one target word into two tokens
            // (e.g. 'porque' -> 'por qué', 'haber' -> 'a ver', 'viszontlátásra' -> 'viszont látásra')
            if (!found) {
                for (let j = 0; j + 1 < recTokens.length; j++) {
                    if (!matchedIndices.has(j) && !matchedIndices.has(j + 1)) {
                        const mergedRecNorm = recTokens[j].norm + recTokens[j + 1].norm;
                        if (isBoundaryMergeMatch(t.norm, mergedRecNorm, lang)) {
                            matchedIndices.add(j);
                            matchedIndices.add(j + 1);
                            recPointer = Math.max(recPointer, j + 2);
                            found = true;
                            break;
                        }
                    }
                }
            }

            wordResults.push({
                word: t.raw,
                status: found ? 'matched' : 'missed'
            });
        }

        const matchedCount = wordResults.filter(w => w.status === 'matched').length;
        const accuracy = Math.round((matchedCount / targetTokens.length) * 100);

        // A realistic threshold: 70%+ match counts as correct (or 100% for 1-word responses),
        // preventing learners from being failed due to minor background noise or ASR quirks.
        const minPassPercent = targetTokens.length <= 2 ? 100 : (targetTokens.length <= 4 ? 75 : 65);
        const isCorrect = accuracy >= minPassPercent;

        return {
            isCorrect,
            accuracy,
            matchedCount,
            totalCount: targetTokens.length,
            words: wordResults,
            transcript: cleanedTranscript
        };
    }

    function _applyCasingOf(sourceWord, replacementText) {
        if (!sourceWord || !replacementText) return replacementText;
        const firstChar = sourceWord.charAt(0);
        const isCap = firstChar === firstChar.toUpperCase() && firstChar !== firstChar.toLowerCase();
        if (isCap) {
            return replacementText.charAt(0).toUpperCase() + replacementText.slice(1).toLowerCase();
        }
        return replacementText.toLowerCase();
    }

    // Normalises phonetic homophones, sinalefa merges, and word boundaries in an ASR transcript
    // against the expected target sentence (e.g. 'hogy vadj' -> 'hogy vagy', 'hollax' -> 'hol laksz',
    // 'vamos haber' -> 'vamos a ver', 'voy hablar' -> 'voy a hablar', 'va ir' -> 'va a ir', 'baca' -> 'vaca'),
    // while leaving genuinely different or mispronounced words untouched.
    function canonicalizeTranscript(target, rawTranscript, langHint) {
        const cleanedRaw = stripWhisperHallucinations(rawTranscript);
        if (!target || !cleanedRaw) return cleanedRaw || '';
        const targetList = (Array.isArray(target) ? target : [target]).filter(Boolean);
        if (!targetList.length) return cleanedRaw;

        let bestTarget = targetList[0];
        if (targetList.length > 1) {
            let bestAcc = -1;
            for (const cand of targetList) {
                const res = evaluate(cand, cleanedRaw, langHint);
                if (res.accuracy > bestAcc) {
                    bestAcc = res.accuracy;
                    bestTarget = cand;
                }
            }
        }

        const lang = _detectPhoneticLang(langHint, `${bestTarget} ${cleanedRaw}`);
        const targetTokens = tokenize(bestTarget);
        const recTokens = tokenize(cleanedRaw);
        if (!targetTokens.length || !recTokens.length) return cleanedRaw;

        const usedTarget = new Set();
        const outEntries = [];

        for (let j = 0; j < recTokens.length; j++) {
            const r = recTokens[j];
            let replaced = false;

            // 1. Check 2-to-1 merged boundary / sinalefa match when nextR does not separately match t2
            for (let i = 0; i + 1 < targetTokens.length; i++) {
                if (usedTarget.has(i) || usedTarget.has(i + 1)) continue;
                const t1 = targetTokens[i];
                const t2 = targetTokens[i + 1];
                if (isBoundaryMergeMatch(t1.norm + t2.norm, r.norm, lang)) {
                    const nextRecMatchesT2 = (j + 1 < recTokens.length) && isWordMatch(t2.norm, recTokens[j + 1].norm, lang);
                    if (!nextRecMatchesT2) {
                        usedTarget.add(i);
                        usedTarget.add(i + 1);
                        outEntries.push({ text: _applyCasingOf(r.raw, `${t1.raw} ${t2.raw.toLowerCase()}`), matched: true });
                        replaced = true;
                        break;
                    }
                }
            }
            if (replaced) continue;

            // 2. 1-to-1 phonetic / fuzzy match
            for (let i = 0; i < targetTokens.length; i++) {
                if (usedTarget.has(i)) continue;
                const t = targetTokens[i];
                if (isWordMatch(t.norm, r.norm, lang)) {
                    usedTarget.add(i);
                    if (r.norm === t.norm) {
                        outEntries.push({ text: r.raw, matched: true });
                    } else {
                        outEntries.push({ text: _applyCasingOf(r.raw, t.raw), matched: true });
                    }
                    replaced = true;
                    break;
                }
            }
            if (replaced) continue;

            // 3. 1-to-2 split boundary match
            if (j + 1 < recTokens.length) {
                const nextR = recTokens[j + 1];
                for (let i = 0; i < targetTokens.length; i++) {
                    if (usedTarget.has(i)) continue;
                    const t = targetTokens[i];
                    if (isBoundaryMergeMatch(t.norm, r.norm + nextR.norm, lang)) {
                        usedTarget.add(i);
                        outEntries.push({ text: _applyCasingOf(r.raw, t.raw), matched: true });
                        j++;
                        replaced = true;
                        break;
                    }
                }
            }
            if (replaced) continue;

            outEntries.push({ text: r.raw, matched: false });
        }

        // If 100% of target words were spoken and matched, strip at most 1 stray trailing/leading
        // hallucinated noise word (e.g. from a trailing breath or button tap) so it doesn't fail the user.
        if (usedTarget.size === targetTokens.length && recTokens.length <= targetTokens.length + 1) {
            return outEntries.filter(e => e.matched).map(e => e.text).join(' ');
        }

        return outEntries.map(e => e.text).join(' ');
    }

    // Determine if candidate speech has cleanly and fully matched the target (100% words matched)
    function isFullTargetMatch(targetSentence, candidateTranscript) {
        if (!targetSentence || !candidateTranscript) return false;
        const targetTokens = tokenize(targetSentence);
        const recTokens = tokenize(candidateTranscript);
        if (!targetTokens.length || !recTokens.length) return false;

        // Ensure learner didn't just speak a long rambling sentence that happened to contain the target words
        const maxTokens = targetTokens.length <= 2
            ? targetTokens.length + 1
            : targetTokens.length + Math.max(2, Math.floor(targetTokens.length * 0.35));

        if (recTokens.length > maxTokens) return false;

        const evalResult = evaluate(targetSentence, candidateTranscript);
        return evalResult.accuracy >= 100 && evalResult.matchedCount === targetTokens.length;
    }

    return {
        isRecognitionSupported,
        isRecordingSupported,
        isSupported: () => isRecognitionSupported() || isRecordingSupported(),
        canSpeakNow,
        isCantSpeakNow: () => !canSpeakNow(),
        setCantSpeakNow,
        resetCantSpeakNow,
        resumeSpeaking: resetCantSpeakNow,
        startListening,
        stopListening,
        isListening: () => _isListening,
        releaseStream,
        getRecordedAudioUrl,
        getSttEndpoint,
        setSttEndpoint,
        getSttMode,
        setSttMode,
        isCloudSttAvailable,
        transcribeBlob,
        evaluate,
        isFullTargetMatch,
        normalizeForSpeech,
        phoneticFold,
        canonicalizeTranscript
    };
})();

if (typeof window !== 'undefined') {
    window.SpeechInput = SpeechInput;
}

