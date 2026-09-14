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
    let _maxDurationTimeout = null;
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

    // Stop audio meter animation and release audio context
    function _stopStream() {
        _cleanupTimers();
        if (_animFrameId) {
            cancelAnimationFrame(_animFrameId);
            _animFrameId = null;
        }
        if (_audioContext && _audioContext.state !== 'closed') {
            try { _audioContext.close(); } catch (e) {}
            _audioContext = null;
        }
        _analyser = null;
    }

    // Capture microphone audio for user playback
    function _startRecordingStream(options = {}) {
        if (!isRecordingSupported()) return;

        navigator.mediaDevices.getUserMedia({ audio: true, video: false })
            .then(stream => {
                if (!_isListening) {
                    stream.getTracks().forEach(t => {
                        try { t.stop(); } catch (e) {}
                    });
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
                console.warn('SpeechInput: audio recording capture stream unavailable:', err);
                if (!isRecognitionSupported()) {
                    _isListening = false;
                    const onError = options.onError || (() => {});
                    onError('permission-denied');
                }
            });
    }

    // ---- Start Voice Capture & Recognition ----
    // MUST call recognition.start() synchronously within user gesture (tap/click handler) on iOS Safari
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
        _onAudioReadyCallback = options.onAudioReady || null;

        // Safety cap: maximum 25s per recording session
        _maxDurationTimeout = setTimeout(() => {
            if (_isListening) {
                stopListening();
            }
        }, 25000);

        // 1. Primary: SpeechRecognition Engine (started synchronously within user gesture)
        if (isRecognitionSupported()) {
            try {
                const recognition = new RecognitionConstructor();
                recognition.lang = lang;
                // continuous: true prevents mobile engines from aborting after the first syllable or brief pause
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

                    // Reset silence debounce: give language learners 2.8s of breathing room
                    // so hesitations and pauses ("um, uh, mhh") between words don't cut off their answer.
                    if (_finishTimeout) clearTimeout(_finishTimeout);
                    _finishTimeout = setTimeout(() => {
                        stopListening();
                    }, 2800);
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
                    } else if (event.error === 'audio-capture') {
                        console.warn('SpeechInput: audio-capture issue; falling back to recorded audio');
                        stopListening();
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
                    if (_isListening) {
                        // If learner paused and silence debounce hasn't expired yet,
                        // attempt to resume recognition so they can continue speaking.
                        if (_finishTimeout) {
                            try {
                                recognition.start();
                                return;
                            } catch (e) {
                                // If browser forbids restarting without user gesture, stop cleanly
                            }
                        }
                        _cleanupTimers();
                        stopListening();
                    }
                };

                _activeRecognition = recognition;
                recognition.start();
            } catch (e) {
                console.warn('SpeechInput: recognition.start() threw; falling back to recorder', e);
                _activeRecognition = null;
            }
        }

        // 2. Capture microphone audio stream so user can listen back to their recording
        if (isRecordingSupported()) {
            _startRecordingStream(options);
        } else if (!isRecognitionSupported()) {
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
            try { _activeRecognition.stop(); } catch (e) {}
            _activeRecognition = null;
        }

        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        } else {
            _stopTracks();
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

