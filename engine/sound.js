// ============================================
// SOUND
// ============================================
// Short, user-friendly sound cues for learning feedback. Synthesized
// via Web Audio API for zero latency, zero asset loading, and soft,
// non-annoying tones:
//   - Correct: crisp, gentle modern micro chime (E5 -> A5)
//   - Wrong: warm acoustic wooden marimba/block thud (220Hz + soft mallet attack)
//   - Complete: uplifting modern micro arpeggio (C5 -> E5 -> G5 -> C6)
//
// Muting is one global preference shared across the app.

const Sound = (function () {
    'use strict';

    const MUTE_KEY = 'app_sound_muted';
    let audioCtx = null;

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

    function getContext() {
        if (!audioCtx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (!AudioContextClass) return null;
            audioCtx = new AudioContextClass();
        }
        if (audioCtx.state === 'suspended') {
            audioCtx.resume().catch(() => {});
        }
        return audioCtx;
    }

    function safely(fn) {
        if (muted()) return;
        try {
            fn();
        } catch (error) {
            // Sound playback must never interrupt the learning flow.
        }
    }

    // Modern Micro Correct: gentle two-tone chime (E5 -> A5) with natural decay
    function correct() {
        safely(() => {
            const ctx = getContext();
            if (!ctx) return;
            const now = ctx.currentTime;
            const vol = 0.14;

            // Note 1: E5 (659.25Hz)
            const osc1 = ctx.createOscillator();
            const gain1 = ctx.createGain();
            osc1.type = 'sine';
            osc1.frequency.setValueAtTime(659.25, now);
            gain1.gain.setValueAtTime(0, now);
            gain1.gain.linearRampToValueAtTime(vol, now + 0.015);
            gain1.gain.exponentialRampToValueAtTime(0.0001, now + 0.22);
            osc1.connect(gain1).connect(ctx.destination);
            osc1.start(now);
            osc1.stop(now + 0.23);

            // Note 2: A5 (880Hz)
            const osc2 = ctx.createOscillator();
            const gain2 = ctx.createGain();
            osc2.type = 'sine';
            osc2.frequency.setValueAtTime(880, now + 0.08);
            gain2.gain.setValueAtTime(0, now + 0.08);
            gain2.gain.linearRampToValueAtTime(vol * 1.1, now + 0.095);
            gain2.gain.exponentialRampToValueAtTime(0.0001, now + 0.42);
            osc2.connect(gain2).connect(ctx.destination);
            osc2.start(now + 0.08);
            osc2.stop(now + 0.43);
        });
    }

    // Warm Wooden Wrong: acoustic marimba / wooden block tap with soft overtone
    function wrong() {
        safely(() => {
            const ctx = getContext();
            if (!ctx) return;
            const now = ctx.currentTime;
            const vol = 0.16;
            const duration = 0.24;

            // Fundamental: warm 220Hz wood body
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(220, now);
            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(vol, now + 0.008);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
            osc.connect(gain).connect(ctx.destination);
            osc.start(now);
            osc.stop(now + duration + 0.02);

            // Mallet strike harmonic (~3.98x) with fast decay for wooden tactile bite
            const oscHarmonic = ctx.createOscillator();
            const harmGain = ctx.createGain();
            oscHarmonic.type = 'sine';
            oscHarmonic.frequency.setValueAtTime(220 * 3.98, now);
            harmGain.gain.setValueAtTime(vol * 0.25, now);
            harmGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.05);
            oscHarmonic.connect(harmGain).connect(ctx.destination);
            oscHarmonic.start(now);
            oscHarmonic.stop(now + 0.06);
        });
    }

    // Modern Micro Complete: uplifting major triad arpeggio (C5 -> E5 -> G5 -> C6)
    function complete() {
        safely(() => {
            const ctx = getContext();
            if (!ctx) return;
            const now = ctx.currentTime;
            const vol = 0.13;
            const notes = [523.25, 659.25, 783.99, 1046.50];

            notes.forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                const t = now + idx * 0.09;
                const isFinal = idx === notes.length - 1;
                const noteDuration = isFinal ? 0.85 : 0.30;

                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, t);

                gain.gain.setValueAtTime(0, t);
                gain.gain.linearRampToValueAtTime(vol * (isFinal ? 1.15 : 0.95), t + 0.015);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + noteDuration);

                osc.connect(gain).connect(ctx.destination);
                osc.start(t);
                osc.stop(t + noteDuration + 0.02);
            });
        });
    }

    // Kept as a no-op so existing speaking exercise call sites need no changes.
    function speaking() {}

    return { correct, wrong, complete, speaking, muted, toggleMuted };
})();
