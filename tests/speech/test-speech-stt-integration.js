// Unit Test: SpeechInput Cloud STT & 'Listen to My Recording' Integration
// Verifies:
// 1. Cloud STT configuration getters and setters (endpoint and mode)
// 2. Mobile automatic selection of exclusive MediaRecorder + Cloud STT when preferRecording is true
// 3. Audio blob and URL generation (unlocking 'Your Voice' button)
// 4. Successful transcription fetch and onFinal delivery
// 5. Word-by-word pronunciation scoring with Whisper transcript
// 6. Graceful error handling and fallback when STT endpoint fails

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Testing SpeechInput Cloud STT & Audio Replay Integration ---');

// Mock browser globals
global.window = global;
global.document = {
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener: () => {},
    removeEventListener: () => {}
};

const storage = {};
global.localStorage = {
    getItem: (k) => storage[k] || null,
    setItem: (k, v) => { storage[k] = String(v); },
    removeItem: (k) => { delete storage[k]; }
};

let recordedChunks = [];
let mockMediaRecorderInstance = null;

class MockMediaRecorder {
    constructor(stream, options = {}) {
        this.stream = stream;
        this.options = options;
        this.state = 'inactive';
        this.mimeType = 'audio/webm';
        this.ondataavailable = null;
        this.onstop = null;
        mockMediaRecorderInstance = this;
    }
    start(interval) {
        this.state = 'recording';
    }
    stop() {
        this.state = 'inactive';
        // Simulate data chunk
        if (this.ondataavailable) {
            this.ondataavailable({ data: { size: 500, type: 'audio/webm' } });
        }
        if (this.onstop) {
            this.onstop();
        }
    }
}
MockMediaRecorder.isTypeSupported = () => true;
global.MediaRecorder = MockMediaRecorder;

let mockTrackStopped = false;
if (typeof global.navigator === 'undefined') {
    global.navigator = {};
}
Object.defineProperty(global.navigator, 'userAgent', {
    value: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
    configurable: true
});
global.navigator.mediaDevices = {
    getUserMedia: async () => ({
        active: true,
        getAudioTracks: () => [{
            readyState: 'live',
            stop: () => { mockTrackStopped = true; }
        }],
        getTracks: () => [{
            readyState: 'live',
            stop: () => { mockTrackStopped = true; }
        }]
    })
};

global.Blob = class MockBlob {
    constructor(chunks, opts) {
        this.chunks = chunks;
        this.type = (opts && opts.type) || 'audio/webm';
        this.size = 500;
    }
};

global.URL = {
    createObjectURL: (blob) => 'blob:mock-audio-' + Math.random().toString(36).substring(2),
    revokeObjectURL: () => {}
};

// Mock fetch for STT endpoint
let lastFetchCall = null;
let mockFetchResponse = {
    ok: true,
    status: 200,
    json: async () => ({
        text: 'buenos días amigo',
        language: 'es'
    })
};

global.fetch = async (url, opts) => {
    lastFetchCall = { url, opts };
    return mockFetchResponse;
};

// Load SpeechInput engine
const speechInputPath = path.join(__dirname, '../../engine/speech-input.js');
const speechInputCode = fs.readFileSync(speechInputPath, 'utf8');
eval(speechInputCode);

async function runTests() {
    // 1. Endpoint configuration
    console.log('1. Testing STT endpoint configuration...');
    assert.strictEqual(
        SpeechInput.getSttEndpoint(),
        'https://parlour-stt.gergkar.workers.dev/transcribe',
        'Default endpoint must point to parlour-stt.gergkar.workers.dev'
    );

    SpeechInput.setSttEndpoint('https://custom-stt.example.com/transcribe');
    assert.strictEqual(SpeechInput.getSttEndpoint(), 'https://custom-stt.example.com/transcribe');
    SpeechInput.setSttEndpoint(null); // Reset
    assert.strictEqual(SpeechInput.getSttEndpoint(), 'https://parlour-stt.gergkar.workers.dev/transcribe');
    console.log('✓ STT endpoint configuration verified');

    // 2. STT Mode configuration
    console.log('2. Testing STT mode configuration...');
    assert.strictEqual(SpeechInput.getSttMode(), 'auto');
    SpeechInput.setSttMode('cloud');
    assert.strictEqual(SpeechInput.getSttMode(), 'cloud');
    SpeechInput.setSttMode('auto');
    console.log('✓ STT mode configuration verified');

    // 3. Mobile Cloud STT capture with audio blob & URL generation
    console.log('3. Testing mobile exclusive MediaRecorder capture and audio URL generation...');
    let audioUrlReceived = null;
    let finalTranscript = null;
    let statusUpdates = [];

    SpeechInput.startListening({
        target: 'Buenos días amigo',
        preferRecording: true,
        lang: 'es-ES',
        onAudioReady: (url) => {
            audioUrlReceived = url;
        },
        onStatusChange: (st) => {
            statusUpdates.push(st);
        },
        onFinal: (txt) => {
            finalTranscript = txt;
        }
    });

    assert.strictEqual(SpeechInput.isListening(), true, 'SpeechInput must be listening');
    await new Promise(r => setTimeout(r, 10));
    assert.ok(mockMediaRecorderInstance, 'MediaRecorder must be started');
    assert.strictEqual(mockMediaRecorderInstance.state, 'recording', 'MediaRecorder must be in recording state');

    // Stop listening (simulating user finish)
    SpeechInput.stopListening();

    // Allow async MediaRecorder.onstop and fetch to resolve
    await new Promise(r => setTimeout(r, 50));

    // Verify audio URL was produced (unlocking 'Your Voice' button)
    assert.ok(audioUrlReceived, 'onAudioReady must receive audio blob URL');
    assert.ok(audioUrlReceived.startsWith('blob:mock-audio-'), 'Must be a valid blob URL');
    assert.strictEqual(SpeechInput.getRecordedAudioUrl(), audioUrlReceived, 'getRecordedAudioUrl must return the active URL');

    // Verify status changed to 'analyzing'
    assert(statusUpdates.includes('analyzing'), 'Must dispatch analyzing status while transcribing');

    // Verify fetch call to Cloudflare STT Worker
    assert.ok(lastFetchCall, 'fetch must be called to STT worker');
    assert(lastFetchCall.url.includes('lang=es'), 'Must include normalised language query param');
    assert.strictEqual(lastFetchCall.opts.method, 'POST');
    assert.strictEqual(lastFetchCall.opts.headers['Content-Type'], 'audio/webm');

    // Verify onFinal received transcript from Worker
    assert.strictEqual(finalTranscript, 'buenos días amigo', 'onFinal must receive transcribed text');
    console.log('✓ Mobile MediaRecorder capture and Cloud STT transcription verified');

    // 4. Pronunciation Evaluation against Target
    console.log('4. Testing pronunciation evaluation with Whisper transcript...');
    const evalResult = SpeechInput.evaluate('Buenos días amigo', finalTranscript);
    assert.strictEqual(evalResult.accuracy, 100, 'Exact match must score 100% accuracy');
    assert.strictEqual(evalResult.matchedCount, 3, 'All 3 tokens must be matched');
    assert.strictEqual(evalResult.isCorrect, true);
    console.log('✓ Pronunciation evaluation verified');

    // 5. Error handling and fallback on Worker failure
    console.log('5. Testing STT failure handling...');
    mockFetchResponse = {
        ok: false,
        status: 500,
        json: async () => ({ error: 'AI_ERROR' })
    };

    let errorReceived = null;
    SpeechInput.startListening({
        target: 'Hola',
        preferRecording: true,
        onError: (err) => {
            errorReceived = err;
        },
        onFinal: () => {}
    });

    await new Promise(r => setTimeout(r, 10));
    SpeechInput.stopListening();
    await new Promise(r => setTimeout(r, 50));

    assert.strictEqual(errorReceived, 'stt-failed', 'Worker error must report stt-failed to trigger self-eval fallback');
    console.log('✓ Error handling and fallback verified');

    // 6. Hungarian homophone and boundary-merge canonicalization & evaluation ('hogy vadj' -> 'hogy vagy', 'hollax' -> 'hol laksz')
    console.log('6. Testing Hungarian ASR homophone and word-boundary resolution...');

    // Case A: 'hogy vagy' transcribed as 'hogy vadj'
    const evalHogy = SpeechInput.evaluate('Hogy vagy?', 'hogy vadj');
    assert.strictEqual(evalHogy.isCorrect, true, "'hogy vadj' must pass as 100% phonetic match for 'Hogy vagy?'");
    assert.strictEqual(evalHogy.accuracy, 100);
    assert.strictEqual(evalHogy.matchedCount, 2);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Hogy vagy?', 'hogy vadj'), 'hogy vagy');

    // Case B: 'hol laksz' transcribed as 'hollax' (merged word boundary + x/ksz homophone)
    const evalHol = SpeechInput.evaluate('Hol laksz?', 'hollax');
    assert.strictEqual(evalHol.isCorrect, true, "'hollax' must pass as 100% merged phonetic match for 'Hol laksz?'");
    assert.strictEqual(evalHol.accuracy, 100);
    assert.strictEqual(evalHol.matchedCount, 2);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Hol laksz?', 'hollax'), 'hol laksz');
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Hol laksz?', 'Hollax'), 'Hol laksz');

    // Case C: End-to-end Cloud STT flow with 'hollax' from Whisper worker
    mockFetchResponse = {
        ok: true,
        status: 200,
        json: async () => ({
            text: 'hollax',
            language: 'hu'
        })
    };
    let huFinalTranscript = null;
    SpeechInput.startListening({
        target: 'Hol laksz?',
        preferRecording: true,
        lang: 'hu-HU',
        onFinal: (txt) => {
            huFinalTranscript = txt;
        }
    });
    await new Promise(r => setTimeout(r, 10));
    SpeechInput.stopListening();
    await new Promise(r => setTimeout(r, 50));

    assert.ok(lastFetchCall.url.includes('lang=hu'), 'Must send lang=hu');
    assert.ok(lastFetchCall.url.includes('prompt='), 'Must send target prompt hint to Whisper worker');
    assert.strictEqual(huFinalTranscript, 'hol laksz', "Cloud STT must canonicalize 'hollax' to 'hol laksz'");

    // Case D: Genuine wrong answer must NOT be falsely matched
    const evalWrong = SpeechInput.evaluate('Hol laksz?', 'hol vagy');
    assert.strictEqual(evalWrong.isCorrect, false, "Wrong word 'vagy' must not match 'laksz'");
    assert.strictEqual(evalWrong.accuracy, 50);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Hol laksz?', 'hol vagy'), 'hol vagy');
    // Hungarian 'h' and 'b'/'v' must remain distinct
    assert.strictEqual(SpeechInput.evaluate('Hol', 'ol', 'hu').isCorrect, false, "Hungarian 'h' is pronounced and must not match 'ol'");
    console.log('✓ Hungarian homophone and boundary resolution verified');

    // 7. Spanish homophones, seseo, yeísmo, betacismo, sinalefa & hallucination stripping
    console.log('7. Testing Spanish ASR homophones, sinalefa boundary merges, and hallucination filtering...');

    // Betacismo (b/v), seseo (z/c/s), yeísmo (ll/y), silent h
    assert.strictEqual(SpeechInput.evaluate('Hola, ¿cómo estás?', 'ola como estas', 'es').accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Hola, ¿cómo estás?', 'ola como estas', 'es'), 'hola como estas');
    assert.strictEqual(SpeechInput.evaluate('La vaca tuvo un bello pollo en casa', 'la baca tubo un vello poyo en caza', 'es').accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('La vaca tuvo un bello pollo en casa', 'la baca tubo un vello poyo en caza', 'es'), 'la vaca tuvo un bello pollo en casa');

    // Sinalefa & compound boundary merges ('vamos a ver' <-> 'vamos haber', 'voy a hablar' <-> 'voy hablar', 'va a ir' <-> 'va ir', 'por qué' <-> 'porque')
    const evalHaber = SpeechInput.evaluate('Vamos a ver qué pasa', 'vamos haber que pasa', 'es');
    assert.strictEqual(evalHaber.isCorrect, true, "'vamos haber' must match 'Vamos a ver'");
    assert.strictEqual(evalHaber.accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Vamos a ver qué pasa', 'vamos haber que pasa', 'es'), 'vamos a ver que pasa');

    const evalSinalefaRight = SpeechInput.evaluate('Voy a hablar español', 'voy hablar español', 'es');
    assert.strictEqual(evalSinalefaRight.isCorrect, true, "'voy hablar' (rightward sinalefa) must match 'Voy a hablar'");
    assert.strictEqual(evalSinalefaRight.accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Voy a hablar español', 'voy hablar español', 'es'), 'voy a hablar español');

    const evalSinalefaLeft = SpeechInput.evaluate('Ella va a ir mañana', 'ella va ir mañana', 'es');
    assert.strictEqual(evalSinalefaLeft.isCorrect, true, "'va ir' (leftward sinalefa) must match 'va a ir'");
    assert.strictEqual(evalSinalefaLeft.accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Ella va a ir mañana', 'ella va ir mañana', 'es'), 'ella va a ir mañana');

    const evalPorque = SpeechInput.evaluate('¿Por qué no vienes?', 'Porque no bienes', 'es');
    assert.strictEqual(evalPorque.isCorrect, true, "'Porque no bienes' must match '¿Por qué no vienes?'");
    assert.strictEqual(evalPorque.accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('¿Por qué no vienes?', 'Porque no bienes', 'es'), 'Por qué no vienes');

    // Whisper subtitle / outro hallucination stripping
    const hallucinatedEs = 'Buenos días amigo. Subtítulos realizados por la comunidad de Amara.org';
    const evalHallucinated = SpeechInput.evaluate('Buenos días amigo', hallucinatedEs, 'es');
    assert.strictEqual(evalHallucinated.accuracy, 100);
    assert.strictEqual(SpeechInput.canonicalizeTranscript('Buenos días amigo', hallucinatedEs, 'es'), 'Buenos días amigo');
    console.log('✓ Spanish homophones, sinalefa, and hallucination filtering verified');

    console.log('\nAll SpeechInput Cloud STT integration tests passed successfully!');
}

runTests().catch(err => {
    console.error('Integration test failure:', err);
    process.exit(1);
});
