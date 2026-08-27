// ============================================
// SOUND
// ============================================
// Small UI sound effects — correct, wrong, lesson complete. Synthesised
// with the Web Audio API rather than shipped as audio files: three short
// tones are a few lines of code and zero requests, where sourcing,
// licensing and loading actual sound assets would be a much bigger lift
// for the same result. Every tone is a plain sine wave with a soft
// attack/decay envelope, kept quiet and brief on purpose — this is a
// language-learning tool, not a game, so a chime should register and get
// out of the way rather than announce itself.
//
// Muting is one global preference (not scoped per lesson/course): a
// learner who doesn't want sound effects in Lessons won't want them
// anywhere else they show up later either.

const Sound = (function () {
    'use strict';

    const MUTE_KEY = 'app_sound_muted';
    let ctx = null;

    function muted() {
        try {
            return localStorage.getItem(MUTE_KEY) === '1';
        } catch (error) {
            return false;
        }
    }

    function setMuted(value) {
        try {
            localStorage.setItem(MUTE_KEY, value ? '1' : '0');
        } catch (error) {
            // Private browsing with storage disabled: the toggle still
            // works for the rest of this session, it just won't persist.
        }
    }

    function toggleMuted() {
        setMuted(!muted());
        return muted();
    }

    // Created lazily, on first actual use rather than at load time —
    // browsers suspend an AudioContext until a user gesture happens, and
    // constructing one earlier just logs a console warning for nothing.
    function context() {
        if (!ctx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (!AudioContextClass) return null;
            ctx = new AudioContextClass();
        }
        if (ctx.state === 'suspended') ctx.resume();
        return ctx;
    }

    // One tone: a sine wave with a fast linear attack (so it doesn't
    // click) and an exponential decay (so it fades rather than cuts off).
    // startAt is an offset in seconds from now, for sequencing notes into
    // a short phrase.
    function tone(frequency, startAt, duration, peakGain) {
        const c = context();
        if (!c) return;

        const osc = c.createOscillator();
        const gain = c.createGain();
        osc.type = 'sine';
        osc.frequency.value = frequency;
        osc.connect(gain);
        gain.connect(c.destination);

        const t0 = c.currentTime + startAt;
        gain.gain.setValueAtTime(0, t0);
        gain.gain.linearRampToValueAtTime(peakGain, t0 + 0.012);
        gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);

        osc.start(t0);
        osc.stop(t0 + duration + 0.02);
    }

    function play(notes) {
        if (muted()) return;
        // A silently-failing AudioContext (blocked autoplay, no user
        // gesture yet, unsupported browser) should never throw and
        // interrupt the grading flow that triggered it.
        try {
            notes.forEach(note => tone(note[0], note[1], note[2], note[3]));
        } catch (error) {
            // Ignored — a missing chime is not worth breaking the lesson.
        }
    }

    // Correct answer: a short rising interval (C6 -> E6) — an "up"
    // gesture, not a game-show ding.
    function correct() {
        play([
            [1046.50, 0,    0.14, 0.10],
            [1318.51, 0.07, 0.16, 0.10]
        ]);
    }

    // Wrong answer: one soft, low note — a gentle "not quite" rather than
    // a buzzer. Quieter than correct() on purpose, so it reads as neutral
    // feedback rather than a penalty.
    function wrong() {
        play([[220.00, 0, 0.18, 0.07]]);
    }

    // Lesson complete: a short three-note rise (C5-E5-G5) — fuller and a
    // little longer than correct(), for the one moment per lesson that
    // deserves more than a single chime.
    function complete() {
        play([
            [523.25, 0,    0.18, 0.09],
            [659.25, 0.11, 0.18, 0.09],
            [783.99, 0.22, 0.30, 0.11]
        ]);
    }

    return { correct, wrong, complete, muted, toggleMuted };
})();
