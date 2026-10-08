// ============================================
// Unit Test: SpeechInput Bidirectional Fallback (iOS / WebKit)
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock browser environment
global.window = global;
global.document = {
    body: { classList: { remove: () => {}, add: () => {}, contains: () => false } },
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => {}
};
global.localStorage = {
    getItem: () => null,
    setItem: () => {},
    removeItem: () => {}
};
global.Event = function (type) { this.type = type; };
global.CustomEvent = function (type) { this.type = type; };

// Track mock recognition instances and errors
let createdRecognitions = [];
let mockRecognitionErrorToTrigger = null;

class MockSpeechRecognition {
    constructor() {
        this.lang = '';
        this.continuous = false;
        this.interimResults = false;
        this.maxAlternatives = 1;
        this.onstart = null;
        this.onresult = null;
        this.onerror = null;
        this.onend = null;
        this.started = false;
        this.aborted = false;
        createdRecognitions.push(this);
    }
    start() {
        this.started = true;
        if (this.onstart) this.onstart();
        if (mockRecognitionErrorToTrigger) {
            const err = mockRecognitionErrorToTrigger;
            mockRecognitionErrorToTrigger = null;
            setTimeout(() => {
                if (this.onerror) this.onerror({ error: err });
            }, 10);
        }
    }
    abort() {
        this.aborted = true;
        if (this.onend) this.onend();
    }
    stop() {
        if (this.onend) this.onend();
    }
}

global.SpeechRecognition = MockSpeechRecognition;
global.webkitSpeechRecognition = MockSpeechRecognition;

let getUserMediaCallCount = 0;
let getUserMediaShouldFail = null;

const mockMediaDevices = {
    getUserMedia: async (constraints) => {
        getUserMediaCallCount++;
        if (getUserMediaShouldFail) {
            const err = getUserMediaShouldFail;
            throw err;
        }
        return {
            active: true,
            getAudioTracks: () => [{
                readyState: 'live',
                stop: () => {}
            }],
            getTracks: () => [{
                readyState: 'live',
                stop: () => {}
            }]
        };
    }
};

try {
    Object.defineProperty(global.navigator, 'mediaDevices', { value: mockMediaDevices, configurable: true, writable: true });
    Object.defineProperty(global.navigator, 'userAgent', { value: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', configurable: true, writable: true });
} catch (e) {
    global.navigator = {
        mediaDevices: mockMediaDevices,
        userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    };
}

class MockMediaRecorder {
    constructor(stream, opts) {
        this.stream = stream;
        this.state = 'inactive';
        this.ondataavailable = null;
        this.onstop = null;
    }
    start() {
        this.state = 'recording';
    }
    stop() {
        this.state = 'inactive';
        if (this.onstop) this.onstop();
    }
}
global.MediaRecorder = MockMediaRecorder;
global.MediaRecorder.isTypeSupported = () => true;
global.fetch = async () => ({ ok: true, json: async () => ({ text: 'hola' }) });

// Load SpeechInput
const speechInputCode = fs.readFileSync(path.join(__dirname, '../../engine/speech-input.js'), 'utf8');
eval(speechInputCode);

async function runTests() {
    console.log('--- Test 1: Native recognition service-not-allowed falls back to Cloud STT recording ---');
    createdRecognitions = [];
    getUserMediaCallCount = 0;
    mockRecognitionErrorToTrigger = 'service-not-allowed';
    getUserMediaShouldFail = null;

    let errorFired = null;
    SpeechInput.startListening({
        target: 'Hola',
        sttProvider: 'native',
        onError: err => { errorFired = err; }
    });

    // Wait for the simulated error event to trigger fallback
    await new Promise(r => setTimeout(r, 50));

    assert.strictEqual(getUserMediaCallCount, 1, 'getUserMedia must be called as fallback when native recognition returns service-not-allowed');
    assert.strictEqual(errorFired, null, 'No fatal permission-denied should be emitted when Cloud STT fallback succeeds');
    assert.strictEqual(SpeechInput.isListening(), true, 'SpeechInput must still be listening via Cloud STT');
    SpeechInput.stopListening();
    console.log('[PASS] Native service-not-allowed cleanly fell back to Cloud STT recording.');

    console.log('--- Test 2: Audio recording failure falls back to native SpeechRecognition ---');
    createdRecognitions = [];
    getUserMediaCallCount = 0;
    mockRecognitionErrorToTrigger = null;
    getUserMediaShouldFail = new Error('Device busy');
    getUserMediaShouldFail.name = 'NotReadableError';

    errorFired = null;
    SpeechInput.startListening({
        target: 'Hola',
        sttProvider: 'cloud',
        onError: err => { errorFired = err; }
    });

    await new Promise(r => setTimeout(r, 50));

    assert.strictEqual(createdRecognitions.length, 1, 'Native SpeechRecognition instance must be started as fallback when recording fails');
    assert.strictEqual(createdRecognitions[0].started, true, 'Native recognition must be started');
    assert.strictEqual(errorFired, null, 'No fatal error should be emitted when native fallback succeeds');
    assert.strictEqual(SpeechInput.isListening(), true, 'SpeechInput must still be listening via native STT');
    SpeechInput.stopListening();
    console.log('[PASS] Recording failure cleanly fell back to native SpeechRecognition.');

    console.log('--- Test 3: Specific error code emitted when both fail ---');
    createdRecognitions = [];
    getUserMediaCallCount = 0;
    mockRecognitionErrorToTrigger = 'service-not-allowed';
    getUserMediaShouldFail = new Error('Security Error');
    getUserMediaShouldFail.name = 'SecurityError';

    errorFired = null;
    SpeechInput.startListening({
        target: 'Hola',
        sttProvider: 'native',
        onError: err => { errorFired = err; }
    });

    await new Promise(r => setTimeout(r, 50));

    assert.strictEqual(errorFired, 'insecure-context', 'Specific error code (insecure-context) must be emitted when recording fails with SecurityError');
    SpeechInput.stopListening();
    console.log('[PASS] Specific error code reported when fallbacks are exhausted.');

    console.log('\n[ALL PASS] All bidirectional speech fallback tests passed successfully!');
}

runTests().catch(err => {
    console.error('Test failed:', err);
    process.exit(1);
});
