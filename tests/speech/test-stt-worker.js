// Unit Test: Cloudflare STT Worker (@cf/openai/whisper-large-v3-turbo)
// Verifies:
// 1. Health check endpoint (GET /health)
// 2. CORS headers for localhost and production domains
// 3. Binary audio processing and language normalisation for Whisper
// 4. Correct invocation of env.AI.run('@cf/openai/whisper-large-v3-turbo', ...)
// 5. Error handling: empty audio, 429 quota exhaustion, missing AI binding

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Testing Cloudflare STT Worker ---');

async function runTests() {
    const workerPath = path.join(__dirname, '../../cloudflare-worker/stt-worker.js');
    const workerCode = fs.readFileSync(workerPath, 'utf8');
    const cjsCode = workerCode.replace('export default', 'module.exports =');
    const m = { exports: {} };
    const fn = new Function('module', 'exports', 'Response', cjsCode);
    fn(m, m.exports, global.Response);
    const worker = m.exports;

    // Mock env with AI binding
    let lastAiCall = null;
    const mockEnv = {
        AI: {
            run: async (model, input) => {
                lastAiCall = { model, input };
                return {
                    text: 'hola buenos días',
                    segments: [
                        {
                            text: 'hola buenos días',
                            words: [
                                { word: 'hola', start: 0, end: 0.5 },
                                { word: 'buenos', start: 0.6, end: 1.1 },
                                { word: 'días', start: 1.2, end: 1.6 }
                            ]
                        }
                    ]
                };
            }
        }
    };

    // Helper to create mock Request
    function createRequest(method, url, headers = {}, body = null) {
        return {
            method,
            url,
            headers: {
                get: (h) => headers[h.toLowerCase()] || headers[h] || null
            },
            arrayBuffer: async () => body || new ArrayBuffer(0)
        };
    }

    // 1. Health check
    console.log('1. Testing GET /health check...');
    const healthReq = createRequest('GET', 'https://parlour-stt.gergkar.workers.dev/health', {
        Origin: 'https://parlour.me.uk'
    });
    const healthRes = await worker.fetch(healthReq, mockEnv);
    assert.strictEqual(healthRes.status, 200);
    const healthData = JSON.parse(await healthRes.text());
    assert.strictEqual(healthData.status, 'ok');
    assert.strictEqual(healthData.service, 'parlour-stt');
    assert.strictEqual(healthData.workersAiAvailable, true);
    console.log('✓ Health check endpoint verified');

    // 2. CORS preflight OPTIONS
    console.log('2. Testing OPTIONS CORS preflight...');
    const optionsReq = createRequest('OPTIONS', 'https://parlour-stt.gergkar.workers.dev/transcribe', {
        Origin: 'https://gergkar-gif.github.io'
    });
    const optionsRes = await worker.fetch(optionsReq, mockEnv);
    assert.strictEqual(optionsRes.headers.get('Access-Control-Allow-Origin'), 'https://gergkar-gif.github.io');
    assert(optionsRes.headers.get('Access-Control-Allow-Methods').includes('POST'));
    console.log('✓ CORS headers verified');

    // 3. Binary audio transcription with Spanish language normalisation
    console.log('3. Testing POST /transcribe with binary audio...');
    const fakeAudio = new Uint8Array(200);
    fakeAudio.fill(42); // 200 bytes of audio data

    const transcribeReq = createRequest('POST', 'https://parlour-stt.gergkar.workers.dev/transcribe?lang=es-MX', {
        Origin: 'https://parlour.me.uk',
        'Content-Type': 'audio/webm'
    }, fakeAudio.buffer);

    const transcribeRes = await worker.fetch(transcribeReq, mockEnv);
    assert.strictEqual(transcribeRes.status, 200);
    const transcribeData = JSON.parse(await transcribeRes.text());
    assert.strictEqual(transcribeData.text, 'hola buenos días');
    assert.strictEqual(transcribeData.language, 'es');

    assert.ok(lastAiCall, 'AI.run should be called');
    assert.strictEqual(lastAiCall.model, '@cf/openai/whisper-large-v3-turbo');
    assert.strictEqual(lastAiCall.input.language, 'es');
    assert.strictEqual(lastAiCall.input.vad_filter, true);
    assert.strictEqual(lastAiCall.input.beam_size, 5);
    assert.strictEqual(lastAiCall.input.temperature, 0);
    assert.ok(lastAiCall.input.initial_prompt.includes('español'), 'Spanish initial_prompt primer must be included');
    // whisper-large-v3-turbo requires 'audio' as a base64 string (per Cloudflare's
    // input schema), not the raw byte array the base whisper model accepted.
    assert.strictEqual(typeof lastAiCall.input.audio, 'string');
    assert.strictEqual(Buffer.from(lastAiCall.input.audio, 'base64').length, 200);
    // Word-level timestamps come nested under segments[].words and must be
    // flattened into a top-level array in the response.
    assert.strictEqual(transcribeData.words.length, 3);
    assert.strictEqual(transcribeData.words[0].word, 'hola');
    console.log('✓ Binary audio transcription, base64 encoding, and word flattening verified');

    // 4. Hungarian language code normalisation and vocabulary prompt hint
    console.log('4. Testing Hungarian language code normalisation (hu-HU -> hu) and prompt hint...');
    const huReq = createRequest('POST', 'https://parlour-stt.gergkar.workers.dev/transcribe?lang=hu-HU&prompt=Hol%20laksz%3F', {
        Origin: 'http://localhost:8131',
        'Content-Type': 'audio/webm'
    }, fakeAudio.buffer);

    const huRes = await worker.fetch(huReq, mockEnv);
    assert.strictEqual(huRes.status, 200);
    assert.strictEqual(lastAiCall.input.language, 'hu');
    assert.strictEqual(lastAiCall.input.beam_size, 5);
    assert.ok(lastAiCall.input.initial_prompt.toLowerCase().includes('magyar'), 'Hungarian orthographic primer must be included');
    assert.ok(lastAiCall.input.initial_prompt.includes('Hol laksz?'), 'Target prompt hint must be included in initial_prompt');
    console.log('✓ Hungarian normalisation and initial_prompt verified');

    // 5. Empty audio handling (400)
    console.log('5. Testing empty audio validation...');
    const emptyReq = createRequest('POST', 'https://parlour-stt.gergkar.workers.dev/transcribe', {
        Origin: 'https://parlour.me.uk',
        'Content-Type': 'audio/webm'
    }, new ArrayBuffer(10)); // < 64 bytes

    const emptyRes = await worker.fetch(emptyReq, mockEnv);
    assert.strictEqual(emptyRes.status, 400);
    console.log('✓ Empty audio payload returns 400 Bad Request');

    // 6. Quota exceeded handling (429)
    console.log('6. Testing quota exceeded handling (429)...');
    const quotaEnv = {
        AI: {
            run: async () => {
                throw new Error('429 Daily AI quota limit reached');
            }
        }
    };
    const quotaReq = createRequest('POST', 'https://parlour-stt.gergkar.workers.dev/transcribe', {
        Origin: 'https://parlour.me.uk',
        'Content-Type': 'audio/webm'
    }, fakeAudio.buffer);

    const quotaRes = await worker.fetch(quotaReq, quotaEnv);
    assert.strictEqual(quotaRes.status, 429);
    const quotaData = JSON.parse(await quotaRes.text());
    assert.strictEqual(quotaData.code, 'QUOTA_EXHAUSTED');
    console.log('✓ Quota exhaustion returns 429');

    // 7. Missing AI binding handling (500)
    console.log('7. Testing missing env.AI binding error handling...');
    const noAiRes = await worker.fetch(transcribeReq, {});
    assert.strictEqual(noAiRes.status, 500);
    const noAiData = JSON.parse(await noAiRes.text());
    assert.strictEqual(noAiData.code, 'BINDING_MISSING');
    console.log('✓ Missing env.AI binding returns informative 500');

    console.log('\nAll Cloudflare STT Worker tests passed successfully!');
}

runTests().catch(err => {
    console.error('Test failure:', err);
    process.exit(1);
});
