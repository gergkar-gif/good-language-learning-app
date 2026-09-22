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

    console.log('\nAll SpeechInput Cloud STT integration tests passed successfully!');
}

runTests().catch(err => {
    console.error('Integration test failure:', err);
    process.exit(1);
});
