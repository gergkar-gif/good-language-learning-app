// ============================================
// SPEAKING RUNNER
// ============================================
// Renders and manages one speaking exercise:
// - Pronunciation & Shadowing (Read & Repeat): Listen to model, speak, see word-by-word match
// - Oral Production (Prompt & Speak): Prompted in English, formulate and speak in Spanish
// - Real-time microphone capture with live visual meter
// - Word-by-word diagnostic feedback (matched vs mispronounced words)
// - Dual audio playback: Listen to native TTS vs your own recorded voice
// - "Can't speak right now" quick skip

const SpeakingRunner = (function () {
    'use strict';

    let _container = null;
    let _exercise = null;
    let _onResult = null;
    let _onNext = null;
    let _solved = false;
    let _isRecording = false;
    let _userAudioUrl = null;
    let _evalResult = null;
    let _userAudioPlayer = null;
    let _capturedTranscript = '';

    function _esc(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _setFeedback(ok, message) {
        const el = _container.querySelector('.sp-feedback');
        if (!el) return;
        el.textContent = message;
        el.className = 'sp-feedback ' + (ok ? 'sp-feedback-correct' : 'sp-feedback-wrong');
    }

    function _resolve(correct) {
        if (_solved) return;
        _solved = true;

        if (_isRecording) {
            _stopRecording();
        }

        const actionBtns = _container.querySelector('.sp-actions');
        const nextBtn = _container.querySelector('[data-action="next"]');
        if (actionBtns) actionBtns.classList.add('hidden');
        if (nextBtn) {
            nextBtn.classList.remove('hidden');
            try { nextBtn.focus(); } catch (e) {}
        }
        if (_onResult) _onResult(correct, _evalResult);
    }

    // Reveals full model sentence, word breakdown, and dual audio comparison
    function _reveal(evalResult) {
        const revealEl = _container.querySelector('.sp-reveal');
        if (!revealEl) return;
        revealEl.classList.remove('hidden');

        const isPromptSpeak = _exercise.kind === 'prompt-speak';

        // Word-by-word pills breakdown
        let wordsHtml = '';
        if (evalResult && evalResult.words && evalResult.words.length) {
            wordsHtml = `
                <div class="sp-word-breakdown" aria-label="Word pronunciation breakdown">
                    ${evalResult.words.map(w => `
                        <span class="sp-word-pill ${w.status === 'matched' ? 'sp-word-matched' : 'sp-word-missed'}"
                              title="${w.status === 'matched' ? 'Clearly recognized' : 'Mispronounced or omitted'}">
                            ${_esc(w.word)}
                        </span>
                    `).join('')}
                </div>
            `;
        }

        // Dual audio comparison: Native Model vs User Voice
        const userUrl = _userAudioUrl || (typeof SpeechInput !== 'undefined' && SpeechInput.getRecordedAudioUrl ? SpeechInput.getRecordedAudioUrl() : null);
        const compareHtml = `
            <div class="sp-compare-bar">
                <button type="button" class="sp-audio-compare-btn sp-btn-model" data-action="play-model">
                    ${typeof Art !== 'undefined' ? Art.icon('listening') : ''}
                    <span>Model Voice</span>
                </button>
                <button type="button" class="sp-audio-compare-btn sp-btn-user ${userUrl ? '' : 'hidden'}" data-action="play-user" aria-label="Listen to your recording">
                    ${typeof Art !== 'undefined' ? Art.icon('mic') : ''}
                    <span>Your Voice</span>
                </button>
            </div>
        `;

        revealEl.innerHTML = `
            ${isPromptSpeak ? `
                <div class="sp-target-text">
                    <p class="sp-es-lead">${_esc(_exercise.spanish)}</p>
                </div>
            ` : ''}
            ${wordsHtml}
            ${evalResult && evalResult.transcript ? `
                <p class="sp-transcript-note">Heard: <em>"${_esc(evalResult.transcript)}"</em></p>
            ` : ''}
            ${compareHtml}
        `;

        // Wire audio compare buttons
        _attachAudioCompareEvents(revealEl);
    }

    function _attachAudioCompareEvents(parent) {
        const playModelBtn = parent.querySelector('[data-action="play-model"]');
        if (playModelBtn) {
            playModelBtn.addEventListener('click', _playModelAudio);
        }

        const playUserBtn = parent.querySelector('[data-action="play-user"]');
        if (playUserBtn) {
            playUserBtn.addEventListener('click', _playUserAudio);
        }
    }

    function _playModelAudio() {
        if (_userAudioPlayer) {
            _userAudioPlayer.pause();
            _userAudioPlayer = null;
            const btn = _container ? _container.querySelector('[data-action="play-user"]') : null;
            if (btn) {
                btn.classList.remove('is-playing');
                const span = btn.querySelector('span');
                if (span) span.textContent = 'Your Voice';
            }
        }
        if (typeof ParlourTTS !== 'undefined') {
            ParlourTTS.speak({ text: _exercise.spanish, type: 'pronunciation' });
        }
    }

    function _playUserAudio() {
        const url = _userAudioUrl || (typeof SpeechInput !== 'undefined' && SpeechInput.getRecordedAudioUrl ? SpeechInput.getRecordedAudioUrl() : null);
        if (!url) return;
        if (typeof ParlourTTS !== 'undefined') {
            ParlourTTS.stop();
        }
        if (_userAudioPlayer) {
            _userAudioPlayer.pause();
            _userAudioPlayer = null;
        }

        const btn = _container ? _container.querySelector('[data-action="play-user"]') : null;
        const span = btn ? btn.querySelector('span') : null;

        try {
            _userAudioPlayer = new Audio(url);
            if (btn) btn.classList.add('is-playing');
            if (span) span.textContent = 'Playing...';

            _userAudioPlayer.onended = () => {
                if (btn) btn.classList.remove('is-playing');
                if (span) span.textContent = 'Your Voice';
                _userAudioPlayer = null;
            };

            _userAudioPlayer.onerror = () => {
                if (btn) btn.classList.remove('is-playing');
                if (span) span.textContent = 'Your Voice';
                _userAudioPlayer = null;
            };

            _userAudioPlayer.play().catch(e => {
                console.warn('Could not play user audio', e);
                if (btn) btn.classList.remove('is-playing');
                if (span) span.textContent = 'Your Voice';
            });
        } catch (e) {
            console.warn('Audio player init error', e);
        }
    }

    function _updateUserAudioButton() {
        if (!_container) return;
        const userUrl = _userAudioUrl || (typeof SpeechInput !== 'undefined' && SpeechInput.getRecordedAudioUrl ? SpeechInput.getRecordedAudioUrl() : null);
        if (!userUrl) return;
        const compareBar = _container.querySelector('.sp-compare-bar');
        if (!compareBar) return;
        let playUserBtn = compareBar.querySelector('[data-action="play-user"]');
        if (playUserBtn) {
            playUserBtn.classList.remove('hidden');
        } else {
            playUserBtn = document.createElement('button');
            playUserBtn.type = 'button';
            playUserBtn.className = 'sp-audio-compare-btn sp-btn-user';
            playUserBtn.setAttribute('data-action', 'play-user');
            playUserBtn.setAttribute('aria-label', 'Listen to your recording');
            const icon = (typeof Art !== 'undefined') ? Art.icon('mic') : '';
            playUserBtn.innerHTML = `${icon}<span>Your Voice</span>`;
            playUserBtn.addEventListener('click', _playUserAudio);
            compareBar.appendChild(playUserBtn);
        }
    }

    // Handles result calculation and finish state
    function _finishEvaluation(evalResult) {
        _evalResult = evalResult;
        const ok = evalResult.isCorrect;
        const scoreStr = evalResult.accuracy !== undefined ? ` (${evalResult.accuracy}%)` : '';
        const msg = ok
            ? (evalResult.accuracy >= 90 ? `✓ Excellent!${scoreStr}` : `✓ Good job!${scoreStr}`)
            : `✗ Not quite clear${scoreStr}. Try listening to the model.`;

        _setFeedback(ok, msg);
        _reveal(evalResult);
        _resolve(ok);
    }

    // Start voice recording and STT
    function _startRecording() {
        if (_solved || _isRecording) return;
        _isRecording = true;
        if (typeof Sound !== 'undefined') Sound.speaking();

        _capturedTranscript = '';
        const micBtn = _container.querySelector('.sp-mic-btn');
        const micLabel = _container.querySelector('.sp-mic-status');
        const liveText = _container.querySelector('.sp-live-transcript');
        const stopCue = _container.querySelector('.sp-mic-stop-cue');
        const waveContainer = _container.querySelector('.sp-voice-wave');
        const doneBtn = _container.querySelector('.sp-done-speaking-btn');

        if (micBtn) micBtn.classList.add('sp-recording');
        if (stopCue) stopCue.classList.remove('hidden');
        if (waveContainer) waveContainer.classList.add('is-active');
        if (doneBtn) doneBtn.classList.remove('hidden');
        if (micLabel) micLabel.textContent = 'Listening… speak your response';
        if (liveText) {
            liveText.textContent = '';
            liveText.classList.add('hidden');
        }

        SpeechInput.startListening({
            target: _exercise.spanish || _exercise.sentence || '',
            preferRecording: true,
            onInterim: interim => {
                _capturedTranscript = interim;
                // Defer displaying transcribed text until speaker finishes
            },
            onStatusChange: status => {
                const micLabel = _container.querySelector('.sp-mic-status');
                if (micLabel && status === 'analyzing') {
                    micLabel.textContent = 'Analyzing speech…';
                }
            },
            onFinal: transcript => {
                const text = transcript || _capturedTranscript;
                if (liveText && text) {
                    liveText.textContent = text;
                    liveText.classList.remove('hidden');
                }
                _stopRecording();
                const micLabel = _container.querySelector('.sp-mic-status');
                if (micLabel) micLabel.textContent = 'Tap to speak';
                const evalResult = SpeechInput.evaluate(_exercise.spanish, text);
                _finishEvaluation(evalResult);
            },
            onAudioReady: url => {
                _userAudioUrl = url;
                _updateUserAudioButton();
            },
            onAudioLevel: (level, meta) => {
                const waveContainer = _container.querySelector('.sp-voice-wave');
                const micLabel = _container.querySelector('.sp-mic-status');
                const bars = _container.querySelectorAll('.sp-wave-bar');
                if (meta && meta.isHearingVoice) {
                    if (waveContainer) waveContainer.classList.add('is-hearing');
                    if (micLabel && _isRecording) {
                        micLabel.textContent = 'Hearing voice · Tap mic when done';
                    }
                } else {
                    if (waveContainer) waveContainer.classList.remove('is-hearing');
                    if (micLabel && _isRecording) {
                        micLabel.textContent = meta && meta.hasSpoken
                            ? 'Tap mic or button below to grade'
                            : 'Listening… speak your response';
                    }
                }
                if (bars && bars.length > 0) {
                    const factors = [0.6, 1.1, 1.5, 1.1, 0.7];
                    bars.forEach((bar, idx) => {
                        const h = Math.min(1.0, Math.max(0.18, level * factors[idx % factors.length]));
                        bar.style.transform = `scaleY(${h})`;
                    });
                }
            },
            onError: err => {
                console.warn('SpeakingRunner error:', err);
                _stopRecording();
                const micLabel = _container.querySelector('.sp-mic-status');
                if (micLabel) micLabel.textContent = 'Tap to speak';

                // Defensive guard: if user already spoke and text was captured, evaluate it
                const captured = _capturedTranscript || (liveText ? liveText.textContent.trim() : '');
                if (captured && captured !== '...') {
                    if (liveText) {
                        liveText.textContent = captured;
                        liveText.classList.remove('hidden');
                    }
                    const evalResult = SpeechInput.evaluate(_exercise.spanish, captured);
                    _finishEvaluation(evalResult);
                    return;
                }

                // If recognition failed or not supported, offer self-eval
                if (err === 'permission-denied') {
                    _setFeedback(false, 'Microphone permission was denied. Please allow microphone access in your browser settings.');
                    _offerSelfEvaluation('Microphone permission denied.');
                } else if (!SpeechInput.isRecognitionSupported() || err === 'recognition-failed' || err === 'no-speech' || err === 'stt-failed') {
                    _offerSelfEvaluation(err === 'no-speech' ? 'No voice heard. Did you speak into the microphone?' : null);
                } else {
                    _setFeedback(false, 'Microphone error. You can try again or skip.');
                }
            }
        });
    }

    // Stop recording manually
    function _stopRecording() {
        if (!_isRecording) return;
        _isRecording = false;
        if (typeof Sound !== 'undefined') Sound.speaking();

        const micBtn = _container.querySelector('.sp-mic-btn');
        const micLabel = _container.querySelector('.sp-mic-status');
        const stopCue = _container.querySelector('.sp-mic-stop-cue');
        const waveContainer = _container.querySelector('.sp-voice-wave');
        const doneBtn = _container.querySelector('.sp-done-speaking-btn');
        const bars = _container.querySelectorAll('.sp-wave-bar');

        if (micBtn) micBtn.classList.remove('sp-recording');
        if (stopCue) stopCue.classList.add('hidden');
        if (doneBtn) doneBtn.classList.add('hidden');
        if (waveContainer) {
            waveContainer.classList.remove('is-active', 'is-hearing');
        }
        if (bars) {
            bars.forEach(b => { b.style.transform = 'scaleY(0.2)'; });
        }
        if (micLabel) micLabel.textContent = 'Analyzing speech…';

        SpeechInput.stopListening();
    }

    // Fallback self-evaluation mode for unsupported browsers or quiet rooms
    function _offerSelfEvaluation(customMsg) {
        const selfEvalEl = _container.querySelector('.sp-self-eval');
        if (!selfEvalEl) return;
        selfEvalEl.classList.remove('hidden');

        const liveText = _container.querySelector('.sp-live-transcript');
        if (liveText) liveText.classList.add('hidden');

        if (customMsg) {
            _setFeedback(false, customMsg);
        }
    }

    // ---- Render Exercise ----
    function render(container, exercise, options = {}) {
        _container = container;
        _exercise = exercise; // { kind, spanish, english, level, topic }
        _onResult = options.onResult || null;
        _onNext = options.onNext || null;
        _solved = false;
        _isRecording = false;
        _userAudioUrl = null;
        _evalResult = null;
        _capturedTranscript = '';

        const isPromptSpeak = exercise.kind === 'prompt-speak';
        const hasSTT = SpeechInput.isRecognitionSupported();
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the target language';
        let instruction = exercise.prompt || `Translate and say this out loud in ${langName}:`;
        if (typeof Lang !== 'undefined' && !Lang.code().startsWith('es')) {
            instruction = instruction.replace(/in Spanish/gi, `in ${langName}`);
        }

        _container.innerHTML = `
            <div class="sp-runner">
                <div class="sp-prompt-card">
                    <span class="sp-eyebrow">${isPromptSpeak ? 'Prompt & Speak' : 'Read & Repeat'}</span>

                    ${isPromptSpeak ? `
                        <p class="sp-en-prompt">${_esc(exercise.english)}</p>
                        <p class="sp-instruction">${_esc(instruction)}</p>
                    ` : `
                        <div class="sp-target-lead">
                            <p class="sp-es-text">${_esc(exercise.spanish)}</p>
                            <button type="button" class="sp-listen-btn" data-action="listen-lead" aria-label="Listen to model pronunciation">
                                ${typeof Art !== 'undefined' ? Art.icon('listening') : ''} Listen
                            </button>
                        </div>
                        <p class="sp-en-sub">${_esc(exercise.english)}</p>
                    `}
                </div>

                <!-- Microphone Interaction Area -->
                <div class="sp-mic-section">
                    <button type="button" class="sp-mic-btn" data-action="toggle-mic" aria-label="Start recording speech">
                        <span class="sp-mic-icon-wrap">
                            ${typeof Art !== 'undefined' ? Art.icon('speaking') : ''}
                        </span>
                        <span class="sp-mic-stop-cue hidden">Tap to finish</span>
                    </button>
                    <span class="sp-mic-status">Tap to speak</span>

                    <!-- Voice wave equalizer -->
                    <div class="sp-voice-wave" aria-hidden="true">
                        <span class="sp-wave-bar"></span>
                        <span class="sp-wave-bar"></span>
                        <span class="sp-wave-bar"></span>
                        <span class="sp-wave-bar"></span>
                        <span class="sp-wave-bar"></span>
                    </div>

                    <!-- Explicit finish button shown while recording -->
                    <button type="button" class="sp-done-speaking-btn hidden" data-action="finish-speaking">
                        Finish speaking & grade ✓
                    </button>

                    <!-- Live transcription bubble -->
                    <div class="sp-live-transcript hidden" aria-live="polite"></div>
                </div>

                <!-- Self-evaluation fallback (shown if STT unavailable or manual check requested) -->
                <div class="sp-self-eval hidden">
                    <p class="sp-self-eval-prompt">How did it sound compared to the model?</p>
                    <div class="sp-self-eval-actions">
                        <button type="button" class="sp-eval-btn sp-eval-good" data-action="eval-good">✓ Sounded Good</button>
                        <button type="button" class="sp-eval-btn sp-eval-retry" data-action="eval-retry">✗ Try Again</button>
                    </div>
                </div>

                <!-- Post-answer reveal & diagnostic -->
                <div class="sp-reveal hidden"></div>

                <!-- Feedback row -->
                <div class="sp-feedback"></div>

                <!-- Footer Action Buttons -->
                <div class="sp-footer">
                    <div class="sp-actions">
                        <button type="button" class="sp-cant-speak-btn" data-action="cant-speak">
                            Can't speak right now
                        </button>
                    </div>
                    <button type="button" class="sp-next-btn hidden" data-action="next">
                        Continue →
                    </button>
                </div>
            </div>
        `;

        _attachEvents();
    }

    function _attachEvents() {
        // 1. Model Audio button
        const listenBtn = _container.querySelector('[data-action="listen-lead"]');
        if (listenBtn) {
            listenBtn.addEventListener('click', () => {
                if (typeof ParlourTTS !== 'undefined') {
                    ParlourTTS.speak({ text: _exercise.spanish, type: 'pronunciation' });
                }
            });
        }

        // 2. Mic toggle button
        const micBtn = _container.querySelector('[data-action="toggle-mic"]');
        if (micBtn) {
            micBtn.addEventListener('click', () => {
                if (_isRecording) {
                    _stopRecording();
                } else {
                    _startRecording();
                }
            });
        }

        // 2b. Explicit finish speaking & grade button
        const finishBtn = _container.querySelector('[data-action="finish-speaking"]');
        if (finishBtn) {
            finishBtn.addEventListener('click', () => {
                if (_isRecording) {
                    _stopRecording();
                }
            });
        }

        // 3. Self-evaluation buttons
        const evalGood = _container.querySelector('[data-action="eval-good"]');
        if (evalGood) {
            evalGood.addEventListener('click', () => {
                _finishEvaluation({ isCorrect: true, accuracy: 100, words: [], transcript: '(Self-evaluated)' });
            });
        }

        const evalRetry = _container.querySelector('[data-action="eval-retry"]');
        if (evalRetry) {
            evalRetry.addEventListener('click', () => {
                _finishEvaluation({ isCorrect: false, accuracy: 50, words: [], transcript: '(Self-evaluated)' });
            });
        }

        // 4. "Can't speak right now" button
        const cantSpeakBtn = _container.querySelector('[data-action="cant-speak"]');
        if (cantSpeakBtn) {
            cantSpeakBtn.addEventListener('click', () => {
                SpeechInput.setCantSpeakNow(10);
                if (typeof UI !== 'undefined' && UI.toast) {
                    UI.toast('Understood — speaking exercises disabled for 10 minutes', 'info');
                } else if (typeof showToast === 'function') {
                    showToast('Understood — speaking exercises disabled for 10 minutes', 'info');
                }
                _evalResult = { isCorrect: true, accuracy: 100, isSnoozed: true, words: [], transcript: '(Skipped)' };
                _resolve(true);
                if (_userAudioPlayer) {
                    _userAudioPlayer.pause();
                    _userAudioPlayer = null;
                }
                if (_onNext) _onNext();
            });
        }

        // 5. Next button
        const nextBtn = _container.querySelector('[data-action="next"]');
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (_userAudioPlayer) {
                    _userAudioPlayer.pause();
                    _userAudioPlayer = null;
                }
                if (_onNext) _onNext();
            });
        }
    }

    return {
        render
    };
})();

if (typeof window !== 'undefined') {
    window.SpeakingRunner = SpeakingRunner;
}

