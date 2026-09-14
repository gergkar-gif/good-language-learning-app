// ============================================
// SPEECH INPUT & EVALUATION ENGINE
// ============================================
// Provides speech-to-text recognition, microphone audio capture, live visualizer
// analysis, and fuzzy word-by-word pronunciation evaluation for Parlour.
//
// Designed to fix the core flaws of automated language speaking apps:
// 1. Transparent word-by-word breakdown (matched vs missed) rather than a black box.
// 2. Dual audio replay: compare recorded learner voice side-by-side with native TTS.
// 3. Resilient fuzzy matching that doesn't fail users on minor ASR transcription quirks.
// 4. Graceful fallback to self-evaluation when speech recognition is unavailable.
// 5. One-tap "Can't speak right now" preference to bypass voice drills when in public.

const SpeechInput = (function () {
    'use strict';

    const RecognitionConstructor = window.SpeechRecognition || window.webkitSpeechRecognition || null;
    let _activeRecognition = null;
    let _mediaStream = null;
    let _mediaRecorder = null;
    let _recordedChunks = [];
    let _recordedAudioBlob = null;
    let _recordedAudioUrl = null;
    let _audioContext = null;
    let _analyser = null;
    let _animFrameId = null;
    let _isListening = false;

    const CANT_SPEAK_KEY = 'parlour_cant_speak_until';

    // ---- Browser Support & State ----
    function isRecognitionSupported() {
        return !!RecognitionConstructor;
    }

    function isRecordingSupported() {
        return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);
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

    // Language code mapper (e.g. 'es' -> 'es-ES' or 'es-MX', 'hu' -> 'hu-HU')
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
    let _onFinalCallback = null;
    let _accumulatedFinal = '';
    let _currentInterim = '';

    function _cleanupTimers() {
        if (_finishTimeout) {
            clearTimeout(_finishTimeout);
            _finishTimeout = null;
        }
        if (_meterInterval) {
            clearInterval(_meterInterval);
            _meterInterval = null;
        }
    }

    // Stop audio meter animation and release audio stream tracks
    function _stopStream() {
        _cleanupTimers();
        if (_animFrameId) {
            cancelAnimationFrame(_animFrameId);
            _animFrameId = null;
        }
        if (_mediaStream) {
            _mediaStream.getTracks().forEach(track => {
                try { track.stop(); } catch (e) {}
            });
            _mediaStream = null;
        }
        if (_audioContext && _audioContext.state !== 'closed') {
            try { _audioContext.close(); } catch (e) {}
            _audioContext = null;
        }
        _analyser = null;
    }

    // Fallback audio recorder for browsers without SpeechRecognition (e.g. desktop Firefox)
    function _startMediaRecorderFallback(options) {
        const onError = options.onError || (() => {});
        const onAudioLevel = options.onAudioLevel || null;

        if (!isRecordingSupported()) {
            _isListening = false;
            onError('not-supported');
            return;
        }

        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(stream => {
                if (!_isListening) {
                    stream.getTracks().forEach(t => t.stop());
                    return;
                }
                _mediaStream = stream;

                if (onAudioLevel && (window.AudioContext || window.webkitAudioContext)) {
                    try {
                        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
                        _audioContext = new AudioContextClass();
                        const source = _audioContext.createMediaStreamSource(_mediaStream);
                        _analyser = _audioContext.createAnalyser();
                        _analyser.fftSize = 64;
                        source.connect(_analyser);

                        const dataArray = new Uint8Array(_analyser.frequencyBinCount);
                        const updateMeter = () => {
                            if (!_isListening || !_analyser) return;
                            _analyser.getByteFrequencyData(dataArray);
                            let sum = 0;
                            for (let i = 0; i < dataArray.length; i++) sum += dataArray[i];
                            onAudioLevel(Math.min(1, (sum / dataArray.length) / 128));
                            _animFrameId = requestAnimationFrame(updateMeter);
                        };
                        updateMeter();
                    } catch (err) {}
                }

                let mimeType = 'audio/webm';
                if (window.MediaRecorder && typeof MediaRecorder.isTypeSupported === 'function') {
                    if (!MediaRecorder.isTypeSupported('audio/webm')) {
                        if (MediaRecorder.isTypeSupported('audio/mp4')) mimeType = 'audio/mp4';
                        else if (MediaRecorder.isTypeSupported('audio/aac')) mimeType = 'audio/aac';
                        else mimeType = '';
                    }
                }

                _mediaRecorder = mimeType ? new MediaRecorder(_mediaStream, { mimeType }) : new MediaRecorder(_mediaStream);
                _mediaRecorder.ondataavailable = e => {
                    if (e.data && e.data.size > 0) _recordedChunks.push(e.data);
                };
                _mediaRecorder.onstop = () => {
                    if (_recordedChunks.length > 0) {
                        _recordedAudioBlob = new Blob(_recordedChunks, { type: _mediaRecorder.mimeType || 'audio/webm' });
                        _recordedAudioUrl = URL.createObjectURL(_recordedAudioBlob);
                        if (options.onAudioReady) options.onAudioReady(_recordedAudioUrl);
                    }
                };
                _mediaRecorder.start();
            })
            .catch(err => {
                _isListening = false;
                onError('permission-denied');
            });
    }

    // ---- Start Voice Capture & Recognition ----
    // MUST be called synchronously within user gesture (tap/click handler) on iOS Safari
    function startListening(options = {}) {
        if (_isListening) {
            stopListening();
        }

        _cleanAudioUrl();
        _cleanupTimers();
        _recordedChunks = [];
        _accumulatedFinal = '';
        _currentInterim = '';
        _isListening = true;

        const lang = options.lang || getSpeechLang();
        const onInterim = options.onInterim || (() => {});
        const onFinal = options.onFinal || (() => {});
        const onError = options.onError || (() => {});
        const onAudioLevel = options.onAudioLevel || null;
        _onFinalCallback = onFinal;

        // 1. Primary: SpeechRecognition Engine
        // Runs standalone WITHOUT concurrent getUserMedia to prevent mobile mic contention and iOS gesture expiry
        if (isRecognitionSupported()) {
            try {
                const recognition = new RecognitionConstructor();
                recognition.lang = lang;
                // continuous: true prevents Android & iOS from aborting after the first syllable or brief pause
                recognition.continuous = true;
                recognition.interimResults = true;
                recognition.maxAlternatives = 1;

                if (onAudioLevel) {
                    let levelSim = 0.05;
                    _meterInterval = setInterval(() => {
                        if (!_isListening) return;
                        levelSim = Math.max(0.05, levelSim * 0.88);
                        onAudioLevel(levelSim);
                    }, 80);
                }

                recognition.onstart = () => {
                    _isListening = true;
                };

                recognition.onresult = event => {
                    let interim = '';
                    for (let i = event.resultIndex; i < event.results.length; ++i) {
                        const item = event.results[i];
                        if (item && item[0]) {
                            if (item.isFinal) {
                                _accumulatedFinal += (_accumulatedFinal ? ' ' : '') + item[0].transcript;
                            } else {
                                interim += item[0].transcript;
                            }
                        }
                    }
                    _currentInterim = interim;
                    const combined = (_accumulatedFinal + ' ' + _currentInterim).trim();
                    if (combined) {
                        onInterim(combined);
                        if (onAudioLevel) {
                            onAudioLevel(0.4 + Math.random() * 0.5);
                        }
                    }

                    // Reset silence debounce: when learner finishes speaking and pauses 1.3s, finalize
                    if (_finishTimeout) clearTimeout(_finishTimeout);
                    _finishTimeout = setTimeout(() => {
                        stopListening();
                    }, 1300);
                };

                recognition.onerror = event => {
                    console.warn('SpeechInput recognition error:', event.error);
                    const combined = (_accumulatedFinal + ' ' + _currentInterim).trim();
                    if (event.error === 'no-speech') {
                        if (combined) {
                            stopListening();
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
                        _isListening = false;
                        _cleanupTimers();
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
                    _cleanupTimers();
                    if (_isListening) {
                        stopListening();
                    }
                };

                _activeRecognition = recognition;
                // Start synchronously within user gesture
                recognition.start();
                return;
            } catch (e) {
                console.warn('SpeechInput: recognition.start() threw; falling back to recorder', e);
                _activeRecognition = null;
            }
        }

        // 2. Fallback for browsers without SpeechRecognition (Firefox desktop, etc.)
        _startMediaRecorderFallback(options);
    }

    function stopListening() {
        if (!_isListening) return;
        _isListening = false;
        _cleanupTimers();

        const finalText = (_accumulatedFinal + ' ' + _currentInterim).trim();
        _accumulatedFinal = '';
        _currentInterim = '';

        if (_activeRecognition) {
            try { _activeRecognition.stop(); } catch (e) {}
            _activeRecognition = null;
        }

        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        }

        _stopStream();

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

