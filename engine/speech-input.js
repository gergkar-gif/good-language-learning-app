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

    // Stop audio meter animation and release audio stream tracks
    function _stopStream() {
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

    // ---- Start Voice Capture & Recognition ----
    async function startListening(options = {}) {
        if (_isListening) {
            stopListening();
        }

        _cleanAudioUrl();
        _recordedChunks = [];
        _isListening = true;

        const lang = options.lang || getSpeechLang();
        const onInterim = options.onInterim || (() => {});
        const onFinal = options.onFinal || (() => {});
        const onError = options.onError || (() => {});
        const onAudioLevel = options.onAudioLevel || null;

        // 1. Microphone stream & MediaRecorder for voice playback and level meter
        if (isRecordingSupported()) {
            try {
                _mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });

                // Audio level analyzer for the Constructivist waveform visualizer
                if (onAudioLevel && (window.AudioContext || window.webkitAudioContext)) {
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
                        for (let i = 0; i < dataArray.length; i++) {
                            sum += dataArray[i];
                        }
                        const avg = sum / dataArray.length;
                        const norm = Math.min(1, avg / 128); // 0.0 to 1.0
                        onAudioLevel(norm);
                        _animFrameId = requestAnimationFrame(updateMeter);
                    };
                    updateMeter();
                }

                // MediaRecorder to capture audio snippet
                _mediaRecorder = new MediaRecorder(_mediaStream);
                _mediaRecorder.ondataavailable = e => {
                    if (e.data && e.data.size > 0) {
                        _recordedChunks.push(e.data);
                    }
                };
                _mediaRecorder.onstop = () => {
                    if (_recordedChunks.length > 0) {
                        _recordedAudioBlob = new Blob(_recordedChunks, { type: _mediaRecorder.mimeType || 'audio/webm' });
                        _recordedAudioUrl = URL.createObjectURL(_recordedAudioBlob);
                        if (options.onAudioReady) {
                            options.onAudioReady(_recordedAudioUrl);
                        }
                    }
                };
                _mediaRecorder.start();
            } catch (err) {
                console.warn('SpeechInput: microphone capture failed or denied:', err);
                if (!isRecognitionSupported()) {
                    _isListening = false;
                    onError('mic-permission-denied');
                    return;
                }
            }
        }

        // 2. SpeechRecognition Engine
        if (isRecognitionSupported()) {
            try {
                const recognition = new RecognitionConstructor();
                recognition.lang = lang;
                recognition.continuous = false;
                recognition.interimResults = true;
                recognition.maxAlternatives = 2;

                let finalTranscript = '';

                recognition.onresult = event => {
                    let interim = '';
                    for (let i = event.resultIndex; i < event.results.length; ++i) {
                        const transcript = event.results[i][0].transcript;
                        if (event.results[i].isFinal) {
                            finalTranscript += transcript;
                        } else {
                            interim += transcript;
                        }
                    }
                    if (interim) {
                        onInterim(interim);
                    }
                    if (finalTranscript) {
                        onFinal(finalTranscript.trim());
                    }
                };

                recognition.onerror = event => {
                    console.warn('SpeechInput recognition error:', event.error);
                    if (event.error !== 'no-speech' && event.error !== 'aborted') {
                        onError(event.error);
                    }
                };

                recognition.onend = () => {
                    stopListening();
                };

                _activeRecognition = recognition;
                recognition.start();
            } catch (e) {
                console.error('SpeechInput: failed to start speech recognition', e);
                onError('recognition-failed');
                stopListening();
            }
        } else {
            // Self-evaluation mode: no STT available, but MediaRecorder records audio
            console.info('SpeechInput: SpeechRecognition not available; running in self-eval recording mode.');
        }
    }

    function stopListening() {
        if (!_isListening) return;
        _isListening = false;

        if (_activeRecognition) {
            try { _activeRecognition.stop(); } catch (e) {}
            _activeRecognition = null;
        }

        if (_mediaRecorder && _mediaRecorder.state !== 'inactive') {
            try { _mediaRecorder.stop(); } catch (e) {}
        }

        _stopStream();
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
        canSpeakNow,
        setCantSpeakNow,
        resetCantSpeakNow,
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

