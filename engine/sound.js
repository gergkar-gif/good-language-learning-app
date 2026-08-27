// ============================================
// SOUND
// ============================================
// Small UI sound effects — correct, wrong, lesson complete. Synthesised
// with the Web Audio API rather than shipped as audio files: a few lines
// of code and zero requests, where sourcing, licensing and loading actual
// sound assets would be a much bigger lift for the same result.
//
// The palette is deliberately not a game's: no bright synth "ding," no
// cha-ching. Two textures instead, both quiet —
//   - a soft paper rustle (filtered noise) for neutral/wrong feedback,
//     the sound of a page turning rather than a buzzer;
//   - a small singing-bowl-like tone (a few closely-detuned sine partials
//     over a slow decay) for correct and lesson-complete, the sound of a
//     struck bowl rather than an arcade chime.
// This is a language-learning tool, not a game — a sound here should
// register once and get out of the way, not perform.
//
// Muting is one global preference (not scoped per lesson/course): a
// learner who doesn't want sound effects in Lessons won't want them
// anywhere else they show up later either.

const Sound = (function () {
    'use strict';

    const MUTE_KEY = 'app_sound_muted';
    let ctx = null;
    let noiseBuffer = null;

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

    // A second of plain white noise, generated once and reused as the raw
    // material for every rustle — a bandpass filter shapes each play into
    // a soft swish, so the same buffer never sounds identically "sampled."
    function noiseBufferFor(c) {
        if (!noiseBuffer) {
            const length = c.sampleRate * 1;
            noiseBuffer = c.createBuffer(1, length, c.sampleRate);
            const data = noiseBuffer.getChannelData(0);
            for (let i = 0; i < length; i++) data[i] = Math.random() * 2 - 1;
        }
        return noiseBuffer;
    }

    // Paper rustle: a short burst of filtered noise, band-passed around
    // the upper-mid range so it reads as a soft swish (like a page
    // turning) rather than a hiss or a harsh click.
    function rustle(startAt, duration, peakGain) {
        const c = context();
        if (!c) return;

        const src = c.createBufferSource();
        src.buffer = noiseBufferFor(c);

        const band = c.createBiquadFilter();
        band.type = 'bandpass';
        band.frequency.value = 2200;
        band.Q.value = 0.7;

        const gain = c.createGain();
        src.connect(band);
        band.connect(gain);
        gain.connect(c.destination);

        const t0 = c.currentTime + startAt;
        gain.gain.setValueAtTime(0, t0);
        gain.gain.linearRampToValueAtTime(peakGain, t0 + 0.02);
        gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);

        src.start(t0);
        src.stop(t0 + duration + 0.02);
    }

    // One small struck-bowl tone: a fundamental plus two faint, slightly
    // detuned partials above it, so it shimmers a little rather than
    // reading as one flat pitch — the same beating a real bowl's
    // overtones produce. Soft attack, slow exponential decay.
    function bowl(frequency, startAt, duration, peakGain) {
        const c = context();
        if (!c) return;

        const gain = c.createGain();
        gain.connect(c.destination);

        const t0 = c.currentTime + startAt;
        gain.gain.setValueAtTime(0, t0);
        gain.gain.linearRampToValueAtTime(peakGain, t0 + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);

        // [overtone multiplier, relative level]
        [[1, 1], [2.005, 0.22], [3.011, 0.10]].forEach(([mult, level]) => {
            const osc = c.createOscillator();
            osc.type = 'sine';
            osc.frequency.value = frequency * mult;
            const partial = c.createGain();
            partial.gain.value = level;
            osc.connect(partial);
            partial.connect(gain);
            osc.start(t0);
            osc.stop(t0 + duration + 0.05);
        });
    }

    function safely(fn) {
        if (muted()) return;
        // A silently-failing AudioContext (blocked autoplay, no user
        // gesture yet, unsupported browser) should never throw and
        // interrupt the grading flow that triggered it.
        try {
            fn();
        } catch (error) {
            // Ignored — a missing sound is not worth breaking the lesson.
        }
    }

    // Correct answer: one brief, soft bowl tap.
    function correct() {
        safely(() => bowl(659.25, 0, 0.35, 0.06));
    }

    // Wrong answer: a soft rustle, not a buzzer — the same neutral texture
    // whether this is the first attempt or the third, so retrying never
    // starts to feel like a penalty.
    function wrong() {
        safely(() => rustle(0, 0.16, 0.045));
    }

    // Lesson complete: a page settling, then a fuller, longer bowl tone —
    // the one moment per lesson that earns more than the everyday tap.
    function complete() {
        safely(() => {
            rustle(0, 0.22, 0.04);
            bowl(440.00, 0.16, 1.3, 0.08);
        });
    }

    return { correct, wrong, complete, muted, toggleMuted };
})();
