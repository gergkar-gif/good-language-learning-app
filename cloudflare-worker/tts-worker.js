// ============================================
// CLOUDFLARE GOOGLE TTS PROXY WORKER
// ============================================
// Zero-dependency production Google Cloud Text-to-Speech proxy for Parlour.
// Keeps GOOGLE_TTS_API_KEY secure in Cloudflare Worker secrets.
//
// Deploy via Cloudflare Dashboard (Workers & Pages -> Create -> paste this in)
// or via Wrangler CLI. Add GOOGLE_TTS_API_KEY in Worker Settings -> Variables & Secrets.

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131',
    'http://localhost:8000',
    'http://127.0.0.1:8000'
];

function corsHeaders(origin) {
    if (!ALLOWED_ORIGINS.includes(origin)) return null;
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

// Default recommended voice mapping
const DEFAULT_VOICES = {
    'en': { languageCode: 'en-US', name: 'en-US-Journey-F' },
    'es': { languageCode: 'es-ES', name: 'es-ES-Studio-C' },
    'hu': { languageCode: 'hu-HU', name: 'hu-HU-Wavenet-A' }
};

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin) || {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        };

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

        const text = (payload.text || '').trim();
        if (!text) {
            return json({ error: 'Missing text in payload' }, 400, cors);
        }

        const apiKey = (env && env.GOOGLE_TTS_API_KEY) || payload.apiKey;
        if (!apiKey) {
            return json({
                error: 'Google Cloud TTS API key not configured. Please set GOOGLE_TTS_API_KEY secret on Cloudflare Worker.',
                code: 'API_KEY_MISSING'
            }, 500, cors);
        }

        const lang = payload.lang || 'es';
        const defaultVoice = DEFAULT_VOICES[lang] || DEFAULT_VOICES['es'];
        const languageCode = payload.languageCode || defaultVoice.languageCode;
        const voiceName = payload.voiceName || defaultVoice.name;
        const speakingRate = Number(payload.speakingRate) || 1.0;
        const pitch = Number(payload.pitch) || 0.0;

        const googlePayload = {
            input: { text: text },
            voice: {
                languageCode: languageCode,
                name: voiceName
            },
            audioConfig: {
                audioEncoding: 'MP3',
                speakingRate: speakingRate,
                pitch: pitch
            }
        };

        try {
            const googleResponse = await fetch(
                `https://texttospeech.googleapis.com/v1/text:synthesize?key=${apiKey}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(googlePayload)
                }
            );

            if (!googleResponse.ok) {
                const errText = await googleResponse.text();
                return json({
                    error: `Google TTS API error: ${googleResponse.status}`,
                    details: errText
                }, googleResponse.status, cors);
            }

            const data = await googleResponse.json();
            return json({
                audioContent: data.audioContent,
                languageCode: languageCode,
                voiceName: voiceName
            }, 200, cors);
        } catch (fetchErr) {
            return json({
                error: 'Failed to communicate with Google Cloud TTS',
                details: String(fetchErr)
            }, 502, cors);
        }
    }
};
