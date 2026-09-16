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
    return new Response(JSON.stringify(data), {
        status: status || 200,
        headers: Object.assign({ 'Content-Type': 'application/json' }, cors)
    });
}

const LANGUAGE_CODE = { en: 'en-US', es: 'es-ES', hu: 'hu-HU' };

// Chirp3-HD voice names are shared across every language (same character
// bank, only the accent changes with languageCode), so one semantic map
// covers es/hu/en alike. Resolution order: an explicit per-character voice
// (a caller that already assigned "Meg" -> Aoede so she sounds the same in
// every line), then gender alone, then content type, then the narrator
// default.
const SHORT_VOICE = {
    male: 'Orus',          // firm — default dialogue/character voice
    female: 'Kore',        // firm — default dialogue/character voice
    narrator: 'Sulafat',   // warm, steady — stories and long reading passages
    reading: 'Sulafat',
    vocabulary: 'Iapetus', // clear — word-level clarity matters most
    listening: 'Iapetus',
    pronunciation: 'Iapetus',
    example: 'Despina',    // smooth
    instruction: 'Achird'  // friendly — reads as the app talking to you, not the language
};

function resolveVoiceName(payload, languageCode) {
    if (payload.voiceName) return payload.voiceName; // full override, e.g. a specific test voice
    const short = payload.character || SHORT_VOICE[payload.gender] || SHORT_VOICE[payload.type] || SHORT_VOICE.narrator;
    return `${languageCode}-Chirp3-HD-${short}`;
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
                hasApiKey: Boolean(env && env.GOOGLE_TTS_API_KEY)
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

        // Phonetic adaptation for Hungarian: 'ly' sounds like 'y', so Károly is pronounced Károy.
        text = text.replace(/\bKároly\b/g, 'Károy').replace(/\bKaroly\b/g, 'Károy');

        const apiKey = (env && env.GOOGLE_TTS_API_KEY) || payload.apiKey;
        if (!apiKey) {
            return json({
                error: 'Google Cloud TTS API key not configured. Please set GOOGLE_TTS_API_KEY secret on Cloudflare Worker.',
                code: 'API_KEY_MISSING'
            }, 500, cors);
        }

        const lang = payload.lang || 'es';
        const languageCode = payload.languageCode || LANGUAGE_CODE[lang] || LANGUAGE_CODE.es;
        const voiceName = resolveVoiceName(payload, languageCode);
        const speakingRate = Number(payload.speakingRate) || 1.0;
        const pitch = Number(payload.pitch) || 0.0;

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

            return json({
                audioContent: data.audioContent,
                voiceName,
                lang
            }, 200, cors);

        } catch (err) {
            return json({ error: 'Worker synthesis error', detail: err.message }, 500, cors);
        }
    }
};
