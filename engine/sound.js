// ============================================
// SOUND
// ============================================
// Short, user-provided sound cues for learning feedback and speaking.
// Muting is one global preference shared across the app.

const Sound = (function () {
    'use strict';

    const MUTE_KEY = 'app_sound_muted';
    const CLIPS = {
        correct: 'assets/audio/pencil.mp3',
        wrong: 'assets/audio/rewind.mp3',
        complete: 'assets/audio/gong.mp3',
        speaking: 'assets/audio/speaking.mp3'
    };

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
    function complete() { play('complete'); }
    function speaking() { play('speaking'); }

    return { correct, wrong, complete, speaking, muted, toggleMuted };
})();
