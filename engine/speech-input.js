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

    const CANT_SPEAK_KEY = 'parlour_cant_speak_until';

    // ---- Browser Support & State ----
    function isRecognitionSupported() {
        return !!_getRecognitionClass();
    }

    function isRecordingSupported() {
        return !!(typeof navigator !== 'undefined' && navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);
    }

    function canSpeakNow() {
        try {
            const until = parseInt(localStorage.getItem(CANT_SPEAK_KEY) || '0', 10);
            return Date.now() > until;
        } catch (e) {
            return true;
        }
    }

    function setCantSpeakNow(durationMinutes = 30) {
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

    // Language code mapper (e.g. 'es' -> 'es-ES', 'hu' -> 'hu-HU')
    function getSpeechLang() {
        if (typeof Lang !== 'undefined') {
            const code = Lang.code();
            if (code === 'es') return 'es-ES';
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

    let _finishTimeout = null;
    let _meterInterval = null;
    let _initialSilenceTimeout = null;
    let _maxDurationTimeout = null;
    let _onFinalCallback = null;
    let _onAudioReadyCallback = null;
    let _accumulatedFinal = '';
    let _currentInterim = '';

    function _cleanupTimers() {
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

    function _stopTracks() {
        if (_mediaStream) {
            _mediaStream.getTracks().forEach(track => {
                try { track.stop(); } catch (e) {}
            });
            _mediaStream = null;
        }
    }

    // Fallback: capture audio stream when SpeechRecognition is NOT available (e.g. Firefox)
    function _startRecordingFallback(options = {}) {
        if (!isRecordingSupported()) return;

        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(stream => {
                if (!_isListening) {
                    stream.getTracks().forEach(t => { try { t.stop(); } catch (e) {} });
                    return;
                }
                _mediaStream = stream;

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
                    _mediaRecorder = new MediaRecorder(stream);
                }

                _recordedChunks = [];
                _mediaRecorder.ondataavailable = e => {
                    if (e.data && e.data.size > 0) _recordedChunks.push(e.data);
                };

                _mediaRecorder.onstop = () => {
                    if (_recordedChunks.length > 0) {
                        _cleanAudioUrl();
                        const type = (_mediaRecorder && _mediaRecorder.mimeType) || mimeType || 'audio/webm';
                        _recordedAudioBlob = new Blob(_recordedChunks, { type });
                        _recordedAudioUrl = URL.createObjectURL(_recordedAudioBlob);
                        if (options.onAudioReady) options.onAudioReady(_recordedAudioUrl);
                        if (_onAudioReadyCallback) _onAudioReadyCallback(_recordedAudioUrl);
                    }
                    _stopTracks();
                };

                _mediaRecorder.start(100);
            })
            .catch(err => {
                console.warn('SpeechInput: fallback audio recording unavailable:', err);
                _isListening = false;
                const onError = options.onError || (() => {});
                onError('permission-denied');
            });
    }

    // ---- Start Voice Capture & Recognition ----
    function startListening(options = {}) {
        if (_isListening) {
            stopListening();
        }

        _cleanAudioUrl();
        _cleanupTimers();
        _recordedChunks = [];
        _accumulatedFinal = '';
        _currentInterim = '';
        _hasSpoken = false;
        _isListening = true;
        _listenStartTime = Date.now();

        const lang = options.lang || getSpeechLang();
        const onInterim = options.onInterim || (() => {});
        const onFinal = options.onFinal || (() => {});
        const onError = options.onError || (() => {});
        const onAudioLevel = options.onAudioLevel || null;
        _onFinalCallback = onFinal;
        _onAudioReadyCallback = options.onAudioReady || null;

        // Allow up to 10s for learner to start speaking before timing out
        _initialSilenceTimeout = setTimeout(() => {
            if (_isListening && !_hasSpoken) {
                stopListening();
                onError('no-speech');
            }
        }, 10000);

        // Safety cap: maximum 30s per recording session
        _maxDurationTimeout = setTimeout(() => {
            if (_isListening) {
                stopListening();
            }
        }, 30000);

        const RecognitionClass = _getRecognitionClass();

        // 1. Primary: Native SpeechRecognition Engine
        if (RecognitionClass) {
            try {
                const recognition = new RecognitionClass();
                recognition.lang = lang;

                // WebKit on iOS fails if continuous: true; Chrome desktop works well with continuous: true
                const isIOS = typeof navigator !== 'undefined' && (/iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1));
                recognition.continuous = !isIOS;
                recognition.interimResults = true;
                recognition.maxAlternatives = 1;

                if (onAudioLevel) {
                    let simAngle = 0;
                    _meterInterval = setInterval(() => {
                        if (!_isListening) return;
                        simAngle += 0.2;
                        // Ambient breathing wave while waiting, showing mic is hot
                        const basePulse = _hasSpoken ? 0.35 : 0.12 + Math.sin(simAngle) * 0.08;
                        onAudioLevel(basePulse);
                    }, 80);
                }

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
                    const combined = (_accumulatedFinal + ' ' + _currentInterim).trim();

                    if (combined) {
                        _hasSpoken = true;
                        if (_initialSilenceTimeout) {
                            clearTimeout(_initialSilenceTimeout);
                            _initialSilenceTimeout = null;
                        }

                        onInterim(combined);
                        if (onAudioLevel) {
                            onAudioLevel(0.5 + Math.random() * 0.45);
                        }

                        // Silence buffer: automatically finish and evaluate 2.8s after learner stops speaking
                        if (_finishTimeout) clearTimeout(_finishTimeout);
                        _finishTimeout = setTimeout(() => {
                            stopListening();
                        }, 2800);
                    }
                };

                recognition.onerror = event => {
                    console.warn('SpeechInput recognition error:', event.error);
                    const combined = (_accumulatedFinal + ' ' + _currentInterim).trim();

                    if (event.error === 'no-speech') {
                        // If learner already spoke, silence means they are done
                        if (combined) {
                            if (!_finishTimeout) {
                                _finishTimeout = setTimeout(() => {
                                    stopListening();
                                }, 1200);
                            }
                            return;
                        }
                        // If learner hasn't spoken yet and still within initial 10s grace period, keep waiting
                        if (Date.now() - _listenStartTime < 10000) {
                            return;
                        }
                        _isListening = false;
                        _cleanupTimers();
                        onError('no-speech');
                    } else if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
                        _isListening = false;
                        _cleanupTimers();
                        onError('permission-denied');
                    } else if (event.error === 'aborted') {
                        if (combined && _isListening) {
                            stopListening();
                        }
                    } else if (event.error === 'network') {
                        if (combined) {
                            stopListening();
                            return;
                        }
                        _isListening = false;
                        _cleanupTimers();
                        onError('network');
                    } else {
                        if (combined) {
                            stopListening();
                            return;
                        }
                        _isListening = false;
                        _cleanupTimers();
                        onError(event.error || 'recognition-failed');
                    }
                };

                recognition.onend = () => {
                    if (!_isListening) return;

                    // If still active, seamlessly restart recognition (especially on iOS Safari where continuous=false)
                    // so pauses between phrases are not truncated before the 2.8s timer expires
                    try {
                        recognition.start();
                    } catch (e) {
                        if (_hasSpoken) {
                            if (!_finishTimeout) {
                                _finishTimeout = setTimeout(() => {
                                    stopListening();
                                }, 1000);
                            }
                        }
                    }
                };

                _activeRecognition = recognition;
                recognition.start();
            } catch (e) {
                console.warn('SpeechInput: recognition.start() threw:', e);
                _activeRecognition = null;
                // If native recognition threw, fallback to recording if possible
                if (isRecordingSupported()) {
                    _startRecordingFallback(options);
                } else {
                    _isListening = false;
                    onError('not-supported');
                }
            }
        } else if (isRecordingSupported()) {
            // Fallback for browsers without Web Speech API (e.g. Firefox)
            _startRecordingFallback(options);
            onError('not-supported');
        } else {
            _isListening = false;
            onError('not-supported');
        }
    }

    function stopListening() {
        if (!_isListening) return;
        _isListening = false;
        _cleanupTimers();

        const finalText = (_accumulatedFinal + ' ' + _currentInterim).trim();
        _accumulatedFinal = '';
        _currentInterim = '';

        if (_activeRecognition) {
            try { _activeRecognition.abort(); } catch (e) {}
            _activeRecognition = null;
        }

        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        } else {
            _stopTracks();
        }

        if (finalText && _onFinalCallback) {
            const cb = _onFinalCallback;
            _onFinalCallback = null;
            cb(finalText);
        }
    }

    function getRecordedAudioUrl() {
        return _recordedAudioUrl;
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

    function tokenize(text) {
        const rawTokens = String(text || '').trim().split(/\s+/).filter(Boolean);
        return rawTokens.map(raw => ({
            raw,
            norm: normalizeForSpeech(raw)
        }));
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

    // Check if two individual words are phonetically close enough
    function isWordMatch(targetNorm, recNorm) {
        if (!targetNorm || !recNorm) return false;
        if (targetNorm === recNorm) return true;

        // Number words vs digits tolerance (e.g. "dos" vs "2")
        const numMap = { '1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco', '6': 'seis', '7': 'siete', '8': 'ocho', '9': 'nueve', '10': 'diez' };
        if (numMap[recNorm] === targetNorm || numMap[targetNorm] === recNorm) return true;

        // Short words (<= 3 chars) need exact match
        if (targetNorm.length <= 3) return targetNorm === recNorm;

        // Allow Levenshtein distance 1 for 4-7 chars, 2 for 8+ chars
        const maxDist = targetNorm.length >= 8 ? 2 : 1;
        return levenshtein(targetNorm, recNorm) <= maxDist;
    }

    // Evaluates target sentence against spoken transcript with word-by-word alignment
    function evaluate(targetSentence, recognizedTranscript) {
        const targetTokens = tokenize(targetSentence);
        const recTokens = tokenize(recognizedTranscript);

        if (!targetTokens.length) {
            return { isCorrect: true, accuracy: 100, words: [], transcript: recognizedTranscript };
        }

        // Align target tokens with recognized tokens
        const matchedIndices = new Set();
        const wordResults = [];
        let recPointer = 0;

        for (let i = 0; i < targetTokens.length; i++) {
            const t = targetTokens[i];
            let found = false;

            // Search ahead up to 3 tokens in recognized list
            const searchEnd = Math.min(recTokens.length, recPointer + 4);
            for (let j = recPointer; j < searchEnd; j++) {
                if (!matchedIndices.has(j) && isWordMatch(t.norm, recTokens[j].norm)) {
                    matchedIndices.add(j);
                    recPointer = j + 1;
                    found = true;
                    break;
                }
            }

            // If not found ahead, scan backwards once if missed
            if (!found) {
                for (let j = 0; j < recTokens.length; j++) {
                    if (!matchedIndices.has(j) && isWordMatch(t.norm, recTokens[j].norm)) {
                        matchedIndices.add(j);
                        found = true;
                        break;
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
            transcript: recognizedTranscript
        };
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
        getRecordedAudioUrl,
        evaluate,
        normalizeForSpeech
    };
})();

if (typeof window !== 'undefined') {
    window.SpeechInput = SpeechInput;
}

