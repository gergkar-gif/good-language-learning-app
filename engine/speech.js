// ============================================
// SPEECH
// ============================================
// Reads the course's language out loud with the browser's own voices. No
// audio files and
// no network: speechSynthesis says any string, so this works across every
// lesson the moment it ships, including content written later.
//
// The one thing it cannot do is invent a voice that is not installed. A
// sentence read by a voice from the wrong language teaches bad
// pronunciation, which is worse for a learner than silence — so when no
// voice for the course's language is present, the buttons are not rendered
// at all. Story narration recorded as real audio
// is a separate, later job; this covers words and single sentences.

const Speech = (function () {
    const synth = window.speechSynthesis;
    let voice = null;
    let ready = false;

    // Which accents to prefer comes from the course — Lang owns that list, so
    // a Hungarian course asks for hu-HU without this module knowing about it.
    function preferred() {
        return (typeof Lang !== 'undefined') ? Lang.voices() : ['es'];
    }

    function pickVoice() {
        if (!synth) return null;
        const voices = synth.getVoices();
        if (!voices.length) return null;

        const wanted = preferred();
        const base = wanted[wanted.length - 1].split('-')[0].toLowerCase();
        const inLanguage = voices.filter(v => (v.lang || '').toLowerCase().startsWith(base));
        if (!inLanguage.length) return null;

        for (const tag of wanted) {
            const match = inLanguage.find(v => (v.lang || '').toLowerCase().replace('_', '-') === tag.toLowerCase());
            if (match) return match;
        }
        return inLanguage[0];
    }

    function init() {
        if (!synth) { ready = true; return; }
        voice = pickVoice();
        ready = true;

        // Chrome populates the voice list asynchronously, and not always in
        // one go — the first event can carry the system voices and a later
        // one the downloaded ones. Listening only once meant a voice
        // arriving in the second batch was never noticed. Keep listening
        // until we have a voice, and re-announce when it changes.
        if (typeof synth.addEventListener === 'function') {
            synth.addEventListener('voiceschanged', () => {
                const previous = voice;
                voice = pickVoice();
                if (voice !== previous) {
                    document.dispatchEvent(new CustomEvent('speech-ready'));
                }
            });
        }
    }

    function available() {
        return !!(synth && voice);
    }

    // What is on screen is not always what should be said. Tables write
    // paradigms as 'cortar → corta' and pairs as 'el amigo · la amiga'; the
    // arrows and dots are typography, not speech. Bracketed hints are the
    // exercise talking to the learner in English, so they go too.
    function sayable(text) {
        return String(text || '')
            .replace(/\([^)]*\)/g, ' ')
            .replace(/[→·|]/g, ', ')
            .replace(/_{2,}/g, ' ')
            .replace(/\s*,\s*,\s*/g, ', ')
            .replace(/\s+([,.;:!?])/g, '$1')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function speak(text, options) {
        if (!available()) return false;
        const said = sayable(text);
        if (!said) return false;

        // One thing at a time: tapping a second word should replace the first,
        // not queue behind it.
        synth.cancel();

        const utterance = new SpeechSynthesisUtterance(said);
        // Naming the voice is the reliable way to get the accent we picked,
        // but a voice can go stale — uninstalled mid-session, or replaced
        // when the list is rebuilt — and assigning it then throws. The lang
        // tag alone still steers the engine to the right language, so fall
        // back to that rather than losing the click.
        try {
            utterance.voice = voice;
        } catch (error) {
            console.warn('Speech: voice unavailable, falling back to lang', error);
        }
        utterance.lang = voice.lang || preferred()[0];
        // A shade under natural pace. Beginners lose word boundaries at 1.0.
        utterance.rate = (options && options.rate) || 0.9;
        synth.speak(utterance);
        return true;
    }

    // Markup for a speaker button. Renders to nothing when there is no voice,
    // so callers can drop it into a template unconditionally.
    function button(text, label) {
        if (!available()) return '';
        const said = sayable(text);
        if (!said) return '';
        const escaped = said.replace(/&/g, '&amp;').replace(/"/g, '&quot;')
            .replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return `<button class="speak-btn" data-speak="${escaped}" type="button" aria-label="${label || 'Listen'}">🔊</button>`;
    }

    // One delegated listener rather than a handler per button: lesson steps
    // re-render constantly, and rebinding on every render is how listeners
    // end up doubled.
    document.addEventListener('click', event => {
        const btn = event.target.closest && event.target.closest('[data-speak]');
        if (!btn) return;
        event.preventDefault();
        event.stopPropagation();
        speak(btn.getAttribute('data-speak'));
    });

    init();

    return { speak, button, available, sayable };
})();
