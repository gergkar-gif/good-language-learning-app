// ============================================
// Unit Test: SpeechInput & Lesson Voice Lifecycle
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock browser environment
global.window = global;
global.document = {
    body: { classList: { remove: () => {}, add: () => {}, contains: () => false } },
    getElementById: (id) => null,
    querySelector: (sel) => null,
    querySelectorAll: (sel) => [],
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

// Track mock recognition instances
let createdRecognitions = [];
let mockTrackStopped = false;

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
const mockMediaDevices = {
    getUserMedia: async (constraints) => {
        getUserMediaCallCount++;
        return {
            active: true,
            getAudioTracks: () => [{
                readyState: 'live',
                stop: () => { mockTrackStopped = true; }
            }],
            getTracks: () => [{
                readyState: 'live',
                stop: () => { mockTrackStopped = true; }
            }]
        };
    }
};

try {
    Object.defineProperty(global.navigator, 'mediaDevices', { value: mockMediaDevices, configurable: true, writable: true });
} catch (e) {
    global.navigator = { mediaDevices: mockMediaDevices, userAgent: 'Chrome', platform: 'Win32' };
}

global.MediaRecorder = class {
    constructor(stream, opts) {
        this.stream = stream;
        this.state = 'inactive';
        this.ondataavailable = null;
        this.onstop = null;
    }
    static isTypeSupported() { return true; }
    start() { this.state = 'recording'; }
    stop() {
        this.state = 'inactive';
        if (this.onstop) this.onstop();
    }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    voices: () => ['es-ES']
};

global.URL = {
    createObjectURL: () => 'blob:mock-audio',
    revokeObjectURL: () => {}
};

// Load speech-input.js
const speechInputCode = fs.readFileSync(path.join(__dirname, '../../engine/speech-input.js'), 'utf8');
eval(speechInputCode);

console.log('--- Test 1: First listening step with text-only transcription ---');
getUserMediaCallCount = 0;
createdRecognitions = [];

SpeechInput.startListening({
    onInterim: (text) => {},
    onFinal: (text) => {}
});

assert.strictEqual(SpeechInput.isListening(), true, 'SpeechInput should be listening');
assert.strictEqual(createdRecognitions.length, 1, 'Exactly one MockSpeechRecognition should be instantiated');
assert.strictEqual(getUserMediaCallCount, 0, 'getUserMedia should NOT be called for text-only transcription');

console.log('[PASS] Text-only listening does not hold MediaStream hardware lock.');

console.log('--- Test 2: Stopping Step 1 and starting Step 2 consecutively ---');
SpeechInput.stopListening();
assert.strictEqual(SpeechInput.isListening(), false, 'SpeechInput should be stopped');
assert.strictEqual(createdRecognitions[0].aborted, true, 'First recognition should be aborted');
assert.strictEqual(createdRecognitions[0].onend, null, 'Previous recognition listeners should be detached');

// Start Step 2
SpeechInput.startListening({
    onInterim: (text) => {},
    onFinal: (text) => {}
});

assert.strictEqual(SpeechInput.isListening(), true, 'Step 2 SpeechInput should be listening');
assert.strictEqual(createdRecognitions.length, 2, 'A fresh second MockSpeechRecognition should be created');
assert.strictEqual(createdRecognitions[1].started, true, 'Second recognition should have started successfully');

console.log('[PASS] Step 2 speech recognition starts cleanly without collision from Step 1.');

async function runTests() {
    console.log('--- Test 3: Audio recording release when audio playback is used ---');
    SpeechInput.stopListening();
    getUserMediaCallCount = 0;
    mockTrackStopped = false;

    SpeechInput.startListening({
        onAudioReady: (url) => {},
        onFinal: (text) => {}
    });

    assert.strictEqual(SpeechInput.isListening(), true);
    assert.strictEqual(getUserMediaCallCount, 1, 'getUserMedia called when onAudioReady is requested');

    // Allow promise resolution for getUserMedia
    await new Promise(r => setTimeout(r, 20));

    SpeechInput.stopListening();
    assert.strictEqual(mockTrackStopped, true, 'Microphone tracks are stopped immediately upon stopListening');

    console.log('[PASS] Media tracks are immediately released, freeing hardware for next exercise.');

    console.log('--- Test 4: Lesson step transitions and inline voice input state ---');
    let mockInputVal = '';
    const mockInput = {
        get value() { return mockInputVal; },
        set value(v) { mockInputVal = v; },
        dispatchEvent: () => {},
        focus: () => {}
    };
    global.document.querySelector = (sel) => {
        if (sel === '#blank-input') return mockInput;
        return null;
    };

    // Load lessons.js minimal state to test inline voice toggling
    let _inlineVoiceActive = false;
    function testInlineVoice(btn) {
        if (_inlineVoiceActive) {
            SpeechInput.stopListening();
            _inlineVoiceActive = false;
            return 'stopped';
        }
        _inlineVoiceActive = true;
        SpeechInput.startListening({
            onFinal: (txt) => {
                _inlineVoiceActive = false;
                mockInput.value = txt;
            }
        });
        return 'started';
    }

    // Step 1: user taps mic to start
    assert.strictEqual(testInlineVoice(), 'started');
    assert.strictEqual(SpeechInput.isListening(), true);

    // Step transition occurs without waiting for silence timeout (user presses Enter / next step)
    // Step transition logic:
    _inlineVoiceActive = false;
    SpeechInput.stopListening();
    assert.strictEqual(SpeechInput.isListening(), false);
    assert.strictEqual(_inlineVoiceActive, false);

    // Step 2: user taps mic on the second listening step
    assert.strictEqual(testInlineVoice(), 'started', 'Second listening step mic must start on first click');
    assert.strictEqual(SpeechInput.isListening(), true, 'SpeechInput must be active on second listening step');

    SpeechInput.stopListening();
    console.log('[PASS] Second listening step starts cleanly without stuck toggle state.');

    console.log('--- Test 5: Auto-stop recording on 100% target match ---');
    // Verify isFullTargetMatch
    assert.strictEqual(SpeechInput.isFullTargetMatch('Buenos días', 'buenos dias'), true, 'Exact normalized match should be 100%');
    assert.strictEqual(SpeechInput.isFullTargetMatch('Si elegimos esta opción', 'si elegimos esta opcion'), true);
    assert.strictEqual(SpeechInput.isFullTargetMatch('Buenos días', 'buenos'), false, 'Partial utterance is not 100%');
    assert.strictEqual(SpeechInput.isFullTargetMatch('Hola', 'hola amigo que tal como estas hoy en tu casa'), false, 'Rambling phrase should not auto-match');

    // Test startListening with target and auto-stop on simulated recognition result
    let finalReceived = '';
    SpeechInput.startListening({
        target: 'Buenos días',
        onFinal: (txt) => {
            finalReceived = txt;
        }
    });
    assert.strictEqual(SpeechInput.isListening(), true);

    const activeRec = createdRecognitions[createdRecognitions.length - 1];
    assert.ok(activeRec, 'Mock recognition instance must exist');

    // 1. Partial interim speech: should NOT stop
    activeRec.onresult({
        resultIndex: 0,
        results: [[{ transcript: 'Buenos', isFinal: false }]]
    });
    assert.strictEqual(SpeechInput.isListening(), true, 'Partial match should keep recording active');

    // 2. Full match speech (100%): should automatically stop recording!
    activeRec.onresult({
        resultIndex: 0,
        results: [[{ transcript: 'Buenos días', isFinal: true }]]
    });
    assert.strictEqual(SpeechInput.isListening(), false, '100% match should automatically stop recording');
    assert.strictEqual(finalReceived, 'Buenos días', 'onFinal should receive the 100% matched transcript');

    console.log('[PASS] Recording automatically stops the moment learner gets 100% match without clicking mic.');

    console.log('--- Test 6: Android mobile speech lifecycle (speech + subsequent OS no-speech error) ---');
    let androidFinal = '';
    let androidError = null;
    SpeechInput.startListening({
        target: 'Hola amigo cómo estás',
        onFinal: (txt) => {
            androidFinal = txt;
        },
        onError: (err) => {
            androidError = err;
        }
    });

    const androidRec = createdRecognitions[createdRecognitions.length - 1];
    assert.ok(androidRec, 'Android recognition instance must exist');

    // Simulate Android single-shot interim speech (partial, not 100% match so auto-stop does not fire)
    androidRec.onresult({
        resultIndex: 0,
        results: [[{ transcript: 'Hola amigo', isFinal: false }]]
    });
    assert.strictEqual(SpeechInput.isListening(), true, 'Partial match must keep listening');

    // On Android, silence after speech emits onerror with 'no-speech'
    androidRec.onerror({ error: 'no-speech' });

    // Verify it committed the speech and DID NOT report an error!
    assert.strictEqual(androidError, null, 'Spoken voice followed by silence must NEVER trigger an error');
    assert.strictEqual(androidFinal, 'Hola amigo', 'Spoken voice followed by silence must successfully commit final transcript');
    assert.strictEqual(SpeechInput.isListening(), false, 'SpeechInput must be stopped after committing');
    console.log('[PASS] Android silence following speech commits transcript cleanly without error.');

    console.log('--- Test 7: Android onend after speech commits without restarting loop ---');
    let onendFinal = '';
    let onendError = null;
    const initialRecCount = createdRecognitions.length;
    SpeechInput.startListening({
        target: 'Buenos días',
        onFinal: (txt) => {
            onendFinal = txt;
        },
        onError: (err) => {
            onendError = err;
        }
    });

    const onendRec = createdRecognitions[createdRecognitions.length - 1];
    onendRec.onresult({
        resultIndex: 0,
        results: [[{ transcript: 'Buenos', isFinal: false }]]
    });

    // Mobile recognition closes onend after utterance
    onendRec.onend();

    assert.strictEqual(onendError, null, 'onend after speech must not trigger error');
    assert.strictEqual(onendFinal, 'Buenos', 'onend after speech must commit captured speech');
    assert.strictEqual(createdRecognitions.length, initialRecCount + 1, 'Must NOT spin up new recognition instance when speech was already spoken');
    console.log('[PASS] onend after speech commits immediately and avoids duplicate instance loops.');

    console.log('\n[ALL PASS] SpeechInput lifecycle test suite passed.');
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
