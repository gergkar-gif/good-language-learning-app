// ============================================
// CLOUDFLARE SPEECH-TO-TEXT WORKER (Cloudflare Workers AI Whisper)
// ============================================
// Zero-dependency production AI speech-to-text worker for Parlour.
// Transcribes user-recorded audio via @cf/openai/whisper-large-v3-turbo on Cloudflare Workers AI free tier.
//
// Solves mobile browser microphone contention:
// Mobile browsers cannot run webkitSpeechRecognition and MediaRecorder simultaneously.
// By capturing clean audio via MediaRecorder exclusively on the client and transcribing it
// here, learners get both instant pronunciation scoring AND a replayable "Your Voice" button.
//
// Deploy via Cloudflare Dashboard (Workers & Pages -> Create -> paste this in)
// or via Wrangler CLI. Bind Workers AI as 'AI' in Settings -> Bindings.
// See STT_SETUP.md for full walkthrough.

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8131'
];

function corsHeaders(origin) {
    const isAllowed = ALLOWED_ORIGINS.includes(origin) || (origin && origin.startsWith('http://localhost:'));
    const allowOrigin = isAllowed ? origin : '*';
    return {
        'Access-Control-Allow-Origin': allowOrigin,
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Language'
    };
}

function json(data, status = 200, cors = {}) {
    return new Response(JSON.stringify(data), {
        status,
        headers: Object.assign({ 'Content-Type': 'application/json' }, cors)
    });
}

// Normalise language code for Whisper (e.g. 'es-latam', 'es-MX', 'es-ES' -> 'es')
function normaliseWhisperLang(lang) {
    if (!lang) return 'es';
    const clean = String(lang).toLowerCase().trim();
    if (clean.startsWith('es')) return 'es';
    if (clean.startsWith('hu')) return 'hu';
    if (clean.startsWith('en')) return 'en';
    if (clean.startsWith('fr')) return 'fr';
    if (clean.startsWith('de')) return 'de';
    if (clean.startsWith('it')) return 'it';
    if (clean.startsWith('pt')) return 'pt';
    return clean.split(/[-_]/)[0];
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin);

        // Preflight CORS
        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors });
        }

        const url = new URL(request.url);

        // Health check endpoint
        if (request.method === 'GET' && (url.pathname === '/' || url.pathname === '/health')) {
            return json({
                status: 'ok',
                service: 'parlour-stt',
                model: '@cf/openai/whisper-large-v3-turbo',
                workersAiAvailable: !!(env && env.AI)
            }, 200, cors);
        }

        if (request.method !== 'POST') {
            return json({ error: 'Method not allowed. Send POST to /transcribe' }, 405, cors);
        }

        if (url.pathname !== '/transcribe' && url.pathname !== '/') {
            return json({ error: 'Not found' }, 404, cors);
        }

        // Verify Workers AI binding
        if (!env || !env.AI) {
            return json({
                error: 'Workers AI binding (env.AI) not configured in Cloudflare Worker settings.',
                code: 'BINDING_MISSING'
            }, 500, cors);
        }

        // Extract language parameter
        const reqLang = url.searchParams.get('lang') || request.headers.get('X-Language') || 'es';
        const targetLang = normaliseWhisperLang(reqLang);

        // Read audio buffer from request body
        let audioBytes = null;
        const contentType = request.headers.get('Content-Type') || '';

        try {
            if (contentType.includes('multipart/form-data')) {
                const formData = await request.formData();
                const file = formData.get('file') || formData.get('audio');
                if (!file || typeof file.arrayBuffer !== 'function') {
                    return json({ error: 'No audio file found in form-data payload' }, 400, cors);
                }
                const buffer = await file.arrayBuffer();
                audioBytes = [...new Uint8Array(buffer)];
            } else {
                // Direct binary audio upload (audio/webm, audio/mp4, audio/wav, etc.)
                const buffer = await request.arrayBuffer();
                if (!buffer || buffer.byteLength < 64) {
                    return json({ error: 'Audio payload is empty or too short (< 64 bytes)' }, 400, cors);
                }
                audioBytes = [...new Uint8Array(buffer)];
            }
        } catch (readErr) {
            return json({ error: 'Failed to read audio request body: ' + readErr.message }, 400, cors);
        }

        if (!audioBytes || audioBytes.length === 0) {
            return json({ error: 'No audio data received' }, 400, cors);
        }

        // Call Cloudflare Workers AI Whisper (large-v3-turbo: far more accurate than the
        // base @cf/openai/whisper model, honours the language hint, and suppresses
        // hallucinated words during silence/noise via vad_filter).
        try {
            const aiInput = {
                audio: audioBytes,
                task: 'transcribe',
                vad_filter: true
            };
            if (targetLang) {
                aiInput.language = targetLang;
            }

            const aiResult = await env.AI.run('@cf/openai/whisper-large-v3-turbo', aiInput);

            const transcript = (aiResult && (aiResult.text || aiResult.transcript || '')).trim();

            return json({
                text: transcript,
                language: targetLang,
                words: (aiResult && aiResult.words) || []
            }, 200, cors);

        } catch (aiErr) {
            const errStr = String(aiErr);

            if (errStr.includes('quota') || errStr.includes('limit') || errStr.includes('429')) {
                return json({
                    error: 'Daily AI speech transcription quota exceeded.',
                    code: 'QUOTA_EXHAUSTED'
                }, 429, cors);
            }

            return json({
                error: 'Workers AI Whisper transcription error: ' + (aiErr.message || errStr),
                code: 'AI_ERROR'
            }, 500, cors);
        }
    }
};
