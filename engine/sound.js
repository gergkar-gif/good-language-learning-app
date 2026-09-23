// ============================================
// SOUND
// ============================================
// Short, user-provided sound cues for learning feedback and speaking.
// Muting is one global preference shared across the app.

const Sound = (function () {
    'use strict';

    const MUTE_KEY = 'app_sound_muted';
    const CLIPS = {
        correct: 'assets/audio/pencil-cue.mp3',
        wrong: 'assets/audio/rewind-cue.mp3',
        complete: 'assets/audio/gong-cue.mp3',
        speaking: 'assets/audio/speaking-cue.mp3'
    };
    const GONG_SOURCE = 'assets/audio/gong.mp3';

    let gongContext = null;
    let gongBufferPromise = null;

    function muted() {
        try {
            const stored = localStorage.getItem(MUTE_KEY);
            return stored === null ? true : stored === '1';
        } catch (error) {
            return true;
        }
    }

    function setMuted(value) {
        try {
            localStorage.setItem(MUTE_KEY, value ? '1' : '0');
        } catch (error) {
            // The setting still applies for the current page if storage is unavailable.
        }
    }

    function toggleMuted() {
        setMuted(!muted());
        return muted();
    }

    function play(name) {
        if (muted() || typeof Audio === 'undefined') return;
        try {
            const audio = new Audio(CLIPS[name]);
            audio.play().catch(() => {});
        } catch (error) {
            // Sound playback must never interrupt the learning flow.
        }
    }

    function correct() { play('correct'); }
    function wrong() { play('wrong'); }
    function complete() {
        if (muted()) return;

        // Use only the opening two seconds of the gong, fading the final
        // 650ms so the cue resolves gently instead of cutting off sharply.
        if (typeof AudioContext === 'undefined') {
            play('complete');
            return;
        }

        try {
            gongContext = gongContext || new AudioContext();
            const context = gongContext;
            const resume = context.state === 'suspended'
                ? context.resume()
                : Promise.resolve();
            gongBufferPromise = gongBufferPromise || fetch(GONG_SOURCE)
                .then(response => {
                    if (!response.ok) throw new Error('Could not load gong audio');
                    return response.arrayBuffer();
                })
                .then(data => context.decodeAudioData(data));

            gongBufferPromise.then(async buffer => {
                if (muted()) return;
                await resume;

                const source = context.createBufferSource();
                const gain = context.createGain();
                const duration = Math.min(2, buffer.duration);
                const start = context.currentTime;
                source.buffer = buffer;
                source.connect(gain);
                gain.connect(context.destination);
                gain.gain.setValueAtTime(1, start);
                gain.gain.setValueAtTime(1, start + Math.max(0, duration - 0.65));
                gain.gain.linearRampToValueAtTime(0, start + duration);
                source.start(start, 0, duration);
            }).catch(() => play('complete'));
        } catch (error) {
            play('complete');
        }
    }
    function speaking() { play('speaking'); }

    return { correct, wrong, complete, speaking, muted, toggleMuted };
})();
