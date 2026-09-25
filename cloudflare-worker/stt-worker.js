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
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Language, X-Prompt'
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

// Language-specific orthographic primer + optional drill vocabulary hint.
// Framed as a glossary/orthography header rather than a conversational dialogue so
// Whisper absorbs the target word spellings without trying to continue a dialogue turn.
const DEFAULT_LANGUAGE_PRIMERS = {
    hu: 'Tiszta magyar kiejtés és helyesírás: hogy vagy, hol laksz, köszönöm szépen, jó napot kívánok.',
    es: 'Pronunciación en español claro y estándar: hola, buenos días, cómo estás, dónde vives, muchas gracias.'
};

function buildInitialPrompt(targetLang, hint) {
    const cleanHint = String(hint || '').replace(/\s+/g, ' ').trim().slice(0, 240);
    if (targetLang === 'hu') {
        return cleanHint
            ? `Tiszta magyar kiejtés és helyesírás. Kifejezés: ${cleanHint}.`
            : DEFAULT_LANGUAGE_PRIMERS.hu;
    }
    if (targetLang === 'es') {
        return cleanHint
            ? `Pronunciación en español claro y estándar. Vocabulario: ${cleanHint}.`
            : DEFAULT_LANGUAGE_PRIMERS.es;
    }
    return cleanHint || DEFAULT_LANGUAGE_PRIMERS[targetLang] || '';
}

// Known Whisper training-set subtitle/outro hallucinations in Spanish, Hungarian, and English
// that can trigger on quiet or short recordings.
const WHISPER_HALLUCINATION_PATTERNS = [
    /subt[íi]tulos\s+(realizados|creados|hechos|por)\b[^.?!]*/gi,
    /subtitulado\s+por\b[^.?!]*/gi,
    /amara\.org/gi,
    /suscr[íi]bete\s+al\s+canal[^.?!]*/gi,
    /gracias\s+por\s+ver(\s+el\s+v[íi]deo)?[^.?!]*/gi,
    /feliratozta\b[^.?!]*/gi,
    /a\s+feliratokat\s+k[ée]sz[íi]tette\b[^.?!]*/gi,
    /k[öo]sz[öo]n[öo]m\s+a\s+figyelmet[^.?!]*/gi,
    /subtitles\s+by\b[^.?!]*/gi,
    /thank\s+you\s+for\s+watching[^.?!]*/gi
];

function cleanWhisperTranscript(aiResult) {
    if (!aiResult) return '';

    let rawText = '';
    if (Array.isArray(aiResult.segments) && aiResult.segments.length > 0) {
        // Filter out silent/noise segments (no_speech_prob > 0.65) or degenerate
        // repetitive loop segments (compression_ratio > 2.4)
        const validSegments = aiResult.segments.filter(seg => {
            if (!seg || typeof seg.text !== 'string') return false;
            if (typeof seg.no_speech_prob === 'number' && seg.no_speech_prob > 0.65) return false;
            if (typeof seg.compression_ratio === 'number' && seg.compression_ratio > 2.4) return false;
            return seg.text.trim().length > 0;
        });
        if (validSegments.length > 0) {
            rawText = validSegments.map(s => s.text.trim()).join(' ');
        } else if (aiResult.segments.every(s => typeof s.no_speech_prob === 'number' && s.no_speech_prob > 0.85)) {
            return '';
        }
    }

    if (!rawText) {
        rawText = String(aiResult.text || aiResult.transcript || '');
    }

    let cleaned = rawText;
    for (const pattern of WHISPER_HALLUCINATION_PATTERNS) {
        cleaned = cleaned.replace(pattern, '');
    }

    return cleaned.replace(/\s+/g, ' ').trim();
}

// Chunked to avoid blowing the call-stack limit of String.fromCharCode.apply
// on large recordings (a naive single-call spread fails around ~100KB+).
function bytesToBase64(bytes) {
    const CHUNK_SIZE = 0x8000;
    let binary = '';
    for (let i = 0; i < bytes.length; i += CHUNK_SIZE) {
        binary += String.fromCharCode.apply(null, bytes.subarray(i, i + CHUNK_SIZE));
    }
    return btoa(binary);
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

        // Extract language and optional vocabulary prompt parameters
        const reqLang = url.searchParams.get('lang') || request.headers.get('X-Language') || 'es';
        const targetLang = normaliseWhisperLang(reqLang);
        const reqPrompt = url.searchParams.get('prompt') || request.headers.get('X-Prompt') || '';
        const initialPrompt = buildInitialPrompt(targetLang, reqPrompt);

        // Read audio buffer from request body
        let audioBuffer = null;
        const contentType = request.headers.get('Content-Type') || '';

        try {
            if (contentType.includes('multipart/form-data')) {
                const formData = await request.formData();
                const file = formData.get('file') || formData.get('audio');
                if (!file || typeof file.arrayBuffer !== 'function') {
                    return json({ error: 'No audio file found in form-data payload' }, 400, cors);
                }
                audioBuffer = await file.arrayBuffer();
            } else {
                // Direct binary audio upload (audio/webm, audio/mp4, audio/wav, etc.)
                audioBuffer = await request.arrayBuffer();
                if (!audioBuffer || audioBuffer.byteLength < 64) {
                    return json({ error: 'Audio payload is empty or too short (< 64 bytes)' }, 400, cors);
                }
            }
        } catch (readErr) {
            return json({ error: 'Failed to read audio request body: ' + readErr.message }, 400, cors);
        }

        if (!audioBuffer || audioBuffer.byteLength === 0) {
            return json({ error: 'No audio data received' }, 400, cors);
        }

        // Call Cloudflare Workers AI Whisper (large-v3-turbo: 4-layer decoder distilled from
        // large-v3, honours the language hint and initial_prompt, and suppresses hallucinated
        // words during silence/noise via vad_filter).
        // - beam_size: 5 resolves multi-token Hungarian/Spanish digraphs & word boundaries
        // - temperature: 0 disables random sampling fallback (0.2..1.0) on short clips
        // - condition_on_previous_text: false prevents looping/drift
        try {
            const aiInput = {
                audio: bytesToBase64(new Uint8Array(audioBuffer)),
                task: 'transcribe',
                vad_filter: true,
                beam_size: 5,
                temperature: 0,
                condition_on_previous_text: false
            };
            if (targetLang) {
                aiInput.language = targetLang;
            }
            if (initialPrompt) {
                aiInput.initial_prompt = initialPrompt;
            }

            const aiResult = await env.AI.run('@cf/openai/whisper-large-v3-turbo', aiInput);

            const transcript = cleanWhisperTranscript(aiResult);

            // Word-level timestamps live nested under each segment, not at the top level.
            const words = [];
            if (aiResult && Array.isArray(aiResult.segments)) {
                for (const seg of aiResult.segments) {
                    if (seg && Array.isArray(seg.words)) words.push(...seg.words);
                }
            }

            return json({
                text: transcript,
                language: targetLang,
                words
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
