// ============================================
// PARLOUR TTS
// ============================================
// The one interface every piece of spoken content goes through, regardless
// of whether it's a vocabulary word, a story paragraph, or a listening
// exercise: content -> ParlourTTS -> provider -> audio. Callers never talk
// to a provider directly, so the provider can change (or fail over) without
// any caller knowing.
//
// "Best available" is decided here, not exposed as a setting: try the cloud
// provider (natural, Google Cloud TTS via the Cloudflare worker), and fall
// back to the device's own speechSynthesis (engine/speech.js's `Speech`
// module) when offline, the worker errors, or no API key is configured yet.
// Audio already generated once this session is cached and replayed for
// free instead of re-synthesized.

const ParlourTTS = (function () {
    const CLOUD_ENDPOINT = (typeof window !== 'undefined' && window.PARLOUR_TTS_ENDPOINT) ||
        (typeof localStorage !== 'undefined' && localStorage.getItem('parlour_tts_endpoint')) ||
        'https://parlour-tts.gergkar.workers.dev/synthesize';

    const cache = {}; // sessionKey -> HTMLAudioElement, generated once and replayed
    let activeAudio = null;

    function sessionKey(text, language, voiceName, character, gender, type) {
        return `${language}::${voiceName || ''}::${character || ''}::${gender || ''}::${type || ''}::${text}`;
    }

    function isOnline() {
        return typeof navigator === 'undefined' || navigator.onLine !== false;
    }

    async function cloudSynthesize(text, { language, voiceName, character, gender, type }) {
        const res = await fetch(CLOUD_ENDPOINT, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, lang: language, voiceName, character, gender, type })
        });
        if (!res.ok) throw new Error(`TTS worker error: ${res.status}`);

        const data = await res.json();
        if (!data.audioContent) throw new Error('No audioContent in response');

        return new Audio('data:audio/mp3;base64,' + data.audioContent);
    }

    // Adjusts the pace of whatever is playing right now — a story's speed
    // control changing mid-paragraph, for instance. No-op on the device
    // path: SpeechSynthesisUtterance.rate can't be changed after speak().
    function setRate(rate) {
        if (activeAudio) activeAudio.playbackRate = rate;
    }

    function stop() {
        if (activeAudio) {
            activeAudio.pause();
            activeAudio = null;
        }
        if (typeof window !== 'undefined' && typeof window.speechSynthesis !== 'undefined') {
            window.speechSynthesis.cancel();
        }
    }

    // text: what to say. language: course language code ('es'/'hu'/'en'), defaults
    // to the active course. type: what kind of content this is (vocabulary,
    // example, instruction, dialogue, listening, story, reading, pronunciation) —
    // picks a purposeful default voice per type. character: a short Chirp3-HD
    // voice name (e.g. 'Puck') a caller already assigned to a specific named
    // character, so the same character sounds the same in every line — takes
    // priority over gender/type. gender: 'male'/'female' when a caller knows
    // who's speaking but hasn't assigned a specific voice. voiceName/speed:
    // optional overrides a caller already knows. onEnded: called once
    // playback finishes, whichever provider actually spoke — cloud audio and
    // device speech report "done" through different browser APIs, so a
    // caller that wants to chain onto the next line needs a provider-agnostic
    // hook rather than an audio element it can't get from the device path.
    async function speak({ text, language, type, voiceName, character, gender, speed, onEnded } = {}) {
        stop();

        const lang = language || (typeof Lang !== 'undefined' ? Lang.code() : 'es');
        const said = (typeof Speech !== 'undefined') ? Speech.sayable(text) : String(text || '').trim();
        if (!said) return false;

        const key = sessionKey(said, lang, voiceName, character, gender, type);
        const rate = speed || 1.0;

        if (cache[key]) {
            activeAudio = cache[key];
            activeAudio.currentTime = 0;
            activeAudio.playbackRate = rate;
            if (onEnded) activeAudio.onended = onEnded;
            await activeAudio.play();
            return true;
        }

        if (isOnline()) {
            try {
                const audio = await cloudSynthesize(said, { language: lang, voiceName, character, gender, type });
                cache[key] = audio;
                activeAudio = audio;
                audio.playbackRate = rate;
                if (onEnded) audio.onended = onEnded;
                await audio.play();
                return true;
            } catch (error) {
                console.warn('ParlourTTS: cloud provider unavailable, falling back to device speech', error);
            }
        }

        if (typeof Speech !== 'undefined') {
            return Speech.speak(said, { rate: speed || 0.9, onEnd: onEnded });
        }
        return false;
    }

    // Whether *something* can plausibly speak right now — online (cloud is
    // worth trying even before an API key is confirmed, same best-effort
    // assumption StoryAudioPlayer already makes) or a device voice as
    // fallback. Callers use this to decide whether to render a listen
    // button/offer at all, not to predict which provider will actually run.
    function available() {
        return isOnline() || (typeof Speech !== 'undefined' && Speech.available());
    }

    // Markup for a speak-on-click button, rendering to nothing when
    // available() is false so callers can drop it into a template
    // unconditionally — same ergonomics as Speech.button().
    function button(text, options) {
        if (!available()) return '';
        const said = (typeof Speech !== 'undefined') ? Speech.sayable(text) : String(text || '').trim();
        if (!said) return '';
        const escaped = said.replace(/&/g, '&amp;').replace(/"/g, '&quot;')
            .replace(/</g, '&lt;').replace(/>/g, '&gt;');
        const opts = options || {};
        const mark = (typeof Art !== 'undefined') ? Art.icon('listening') : '';
        const attrs = [`data-tts-text="${escaped}"`];
        if (opts.type) attrs.push(`data-tts-type="${esc(opts.type)}"`);
        if (opts.language) attrs.push(`data-tts-lang="${esc(opts.language)}"`);
        return `<button class="speak-btn" ${attrs.join(' ')} type="button" aria-label="${opts.label || 'Listen'}">${mark}</button>`;
    }

    function esc(s) {
        return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    // One delegated listener rather than a handler per button — mirrors
    // engine/speech.js's own [data-speak] listener, on its own attribute so
    // the two don't collide as call sites migrate one at a time.
    if (typeof document !== 'undefined') {
        document.addEventListener('click', event => {
            const btn = event.target.closest && event.target.closest('[data-tts-text]');
            if (!btn) return;
            event.preventDefault();
            event.stopPropagation();
            speak({
                text: btn.getAttribute('data-tts-text'),
                type: btn.getAttribute('data-tts-type') || undefined,
                language: btn.getAttribute('data-tts-lang') || undefined
            });
        });
    }

    return { speak, stop, setRate, available, button };
})();
