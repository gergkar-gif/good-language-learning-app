// ============================================
// CLOUDFLARE GOOGLE TTS PROXY WORKER
// ============================================
// Zero-dependency production Google Cloud Text-to-Speech proxy for Parlour.
// Keeps GOOGLE_TTS_API_KEY secure in Cloudflare Worker secrets.
//
// Deploy via Cloudflare Dashboard (Workers & Pages -> Create -> paste this in)
// or via Wrangler CLI. Add GOOGLE_TTS_API_KEY in Worker Settings -> Variables & Secrets
// (`wrangler secret put GOOGLE_TTS_API_KEY`), from a GCP project with the
// Cloud Text-to-Speech API enabled and billing linked.
//
// Audio is content-addressed and cached permanently in an R2 bucket bound as
// TTS_CACHE: lesson text is fixed, so almost every synthesis after the first
// is a repeat across learners and sessions. A cache hit skips Google TTS
// entirely. Bind an R2 bucket named TTS_CACHE in Worker Settings -> Bindings
// (see CLOUDFLARE_TTS_SETUP.md for the full walkthrough).

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131',
    'http://localhost:8000',
    'http://127.0.0.1:8000'
];

function corsHeaders(origin) {
    if (!ALLOWED_ORIGINS.includes(origin)) {
        return {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        };
    }
    return {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    };
}

function json(data, status, cors) {
    const headers = Object.assign({
        'Content-Type': 'application/json',
        'Cache-Control': status === 200 ? 'public, max-age=31536000, immutable' : 'no-store'
    }, cors);
    return new Response(JSON.stringify(data), {
        status: status || 200,
        headers
    });
}

const LANGUAGE_CODE = { en: 'en-US', es: 'es-ES', hu: 'hu-HU' };

// Chirp3-HD voice names are used for Spanish and Hungarian alike. Enceladus (deep
// male) is the main voice for both: words, drills and readings. English short-form uses Neural2.
const SHORT_VOICE = {
    male: 'Charon',        // firm, deep — default dialogue/character voice
    female: 'Kore',        // firm — default dialogue/character voice
    narrator: 'Sulafat',   // warm, steady — stories and long reading passages
    reading: 'Sulafat',
    vocabulary: 'Enceladus', // deep male — the main course voice
    listening: 'Enceladus',
    pronunciation: 'Enceladus',
    example: 'Despina',    // smooth
    instruction: 'Achird'  // friendly — reads as the app talking to you, not the language
};

function resolveVoiceName(payload, languageCode) {
    if (payload.voiceName) return payload.voiceName; // full override, e.g. a specific test voice

    // If a named story character is specified, preserve the distinct Chirp3-HD character voice
    if (payload.character) {
        return `${languageCode}-Chirp3-HD-${payload.character}`;
    }

    // Story narration and reading passages use rich multi-voice Chirp3-HD
    const isLongForm = payload.type === 'story' || payload.type === 'reading';

    // Spanish: Enceladus for everything without an explicit dialogue gender (words, drills, readings)
    if (languageCode === 'es-ES' && !SHORT_VOICE[payload.gender]) {
        return 'es-ES-Chirp3-HD-Enceladus';
    }

    if (languageCode === 'en-US' && !isLongForm) {
        if (payload.gender === 'male') return 'en-US-Neural2-D';
        return 'en-US-Neural2-F';
    }

    // Hungarian: Enceladus for story/reading narration and words (via SHORT_VOICE); dialogue genders and other types use SHORT_VOICE table
    if (languageCode === 'hu-HU') {
        if (payload.gender && SHORT_VOICE[payload.gender]) {
            return `hu-HU-Chirp3-HD-${SHORT_VOICE[payload.gender]}`;
        }
        if (isLongForm || payload.type === 'narrator') return 'hu-HU-Chirp3-HD-Enceladus';
        const short = SHORT_VOICE[payload.type] || SHORT_VOICE.narrator;
        return `hu-HU-Chirp3-HD-${short}`;
    }

    const short = SHORT_VOICE[payload.gender] || SHORT_VOICE[payload.type] || SHORT_VOICE.narrator;
    return `${languageCode}-Chirp3-HD-${short}`;
}

// ----------------------------------------
// R2 AUDIO CACHE (content-addressed by everything that affects the audio
// bytes — voice, rate and pitch, not just text — so two requests that
// resolve to identical synthesis params always hit the same object)
// ----------------------------------------

async function cacheKey(languageCode, voiceName, speakingRate, pitch, text) {
    const raw = `${languageCode}::${voiceName}::${speakingRate}::${pitch}::${text}`;
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(raw));
    const hex = Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
    return `${languageCode}/${voiceName}/${hex}.mp3`;
}

function bytesToBase64(bytes) {
    let binary = '';
    const chunkSize = 0x8000;
    for (let i = 0; i < bytes.length; i += chunkSize) {
        binary += String.fromCharCode.apply(null, bytes.subarray(i, i + chunkSize));
    }
    return btoa(binary);
}

function base64ToBytes(b64) {
    const binary = atob(b64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
    return bytes;
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin);

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors });
        }

        const url = new URL(request.url);

        // GET /health
        if (request.method === 'GET' && url.pathname === '/health') {
            return json({
                status: 'ok',
                service: 'parlour-google-tts-proxy',
                hasApiKey: Boolean(env && env.GOOGLE_TTS_API_KEY),
                hasR2Cache: Boolean(env && env.TTS_CACHE)
            }, 200, cors);
        }

        if (request.method !== 'POST') {
            return json({ error: 'Method not allowed' }, 405, cors);
        }

        let payload;
        try {
            payload = await request.json();
        } catch {
            return json({ error: 'Invalid JSON body' }, 400, cors);
        }

        let text = (payload.text || '').trim();
        if (!text) {
            return json({ error: 'Missing text in payload' }, 400, cors);
        }

        // Resolve language early — normalization rules below depend on it.
        const lang = payload.lang || 'es';
        const languageCode = payload.languageCode || LANGUAGE_CODE[lang] || LANGUAGE_CODE.es;

        // Phonetic adaptation for Hungarian: 'ly' sounds like 'y', so Károly is pronounced Károy.
        text = text.replace(/\bKároly\b/g, 'Károy').replace(/\bKaroly\b/g, 'Károy');

        // Intonation fix: if text has no terminal punctuation, append '.' to enforce falling
        // declarative cadence. Critical for Hungarian isolated vocabulary words (e.g. "kutya" → "kutya.")
        // — without punctuation the neural model treats the word as an open clause and raises pitch.
        if (!/[.!?…]$/.test(text)) {
            text = text + '.';
        }

        // Hungarian Wh-question cadence: Hungarian Wh-questions (*ki, mi, hol...*) naturally use
        // a falling tone. When '?' is sent to the model it produces an English-style high-rise
        // on the final syllable which sounds unnatural. Replace the terminal '?' with '.' so the
        // model uses falling declarative cadence.
        const HU_WH_WORDS = /^(ki|mi|hol|mikor|miért|hogyan|mennyi|milyen|melyik|hova|honnan|merre|meddig|mettől|mióta|mire)\b/i;
        if (languageCode === 'hu-HU' && text.endsWith('?') && HU_WH_WORDS.test(text)) {
            text = text.slice(0, -1) + '.';
        }

        // Hungarian story comma cadence: in narrative readings, commas mark rhythmic clause
        // boundaries (szólamhatárok). Appending a typographic em-dash after commas followed by
        // whitespace provides a natural breathing pause so complex Hungarian sentences don't
        // feel rushed. Only applies to long-form reading/story narration; preserves decimal numbers (e.g. 1,5).
        if (languageCode === 'hu-HU' && (payload.type === 'story' || payload.type === 'reading' || payload.type === 'narrator')) {
            text = text.replace(/,(\s+)(?![—–])/g, ', —$1');
        }

        const apiKey = (env && env.GOOGLE_TTS_API_KEY) || payload.apiKey;
        if (!apiKey) {
            return json({
                error: 'Google Cloud TTS API key not configured. Please set GOOGLE_TTS_API_KEY secret on Cloudflare Worker.',
                code: 'API_KEY_MISSING'
            }, 500, cors);
        }

        const voiceName = resolveVoiceName(payload, languageCode);
        const speakingRate = Number(payload.speakingRate) || 1.0;
        const pitch = Number(payload.pitch) || 0.0;

        const r2 = env && env.TTS_CACHE;
        const key = r2 ? await cacheKey(languageCode, voiceName, speakingRate, pitch, text) : null;

        if (r2) {
            const cached = await r2.get(key);
            if (cached) {
                const bytes = new Uint8Array(await cached.arrayBuffer());
                return json({
                    audioContent: bytesToBase64(bytes),
                    voiceName,
                    lang,
                    cached: true
                }, 200, cors);
            }
        }

        const googlePayload = {
            input: { text },
            voice: {
                languageCode,
                name: voiceName
            },
            audioConfig: {
                audioEncoding: 'MP3',
                speakingRate,
                pitch
            }
        };

        try {
            const ttsRes = await fetch(
                `https://texttospeech.googleapis.com/v1/text:synthesize?key=${apiKey}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(googlePayload)
                }
            );

            if (!ttsRes.ok) {
                const errText = await ttsRes.text();
                return json({ error: 'Google TTS synthesis failed: ' + ttsRes.status, detail: errText }, 502, cors);
            }

            const data = await ttsRes.json();
            if (!data.audioContent) {
                return json({ error: 'No audioContent in Google TTS response' }, 502, cors);
            }

            if (r2) {
                // Best-effort: a write failure shouldn't fail the response the
                // learner is waiting on, just cost a repeat Google TTS call later.
                try {
                    await r2.put(key, base64ToBytes(data.audioContent), {
                        httpMetadata: { contentType: 'audio/mpeg' }
                    });
                } catch (cacheErr) {
                    console.error('TTS_CACHE put failed:', cacheErr.message);
                }
            }

            return json({
                audioContent: data.audioContent,
                voiceName,
                lang,
                cached: false
            }, 200, cors);

        } catch (err) {
            return json({ error: 'Worker synthesis error', detail: err.message }, 500, cors);
        }
    }
};
