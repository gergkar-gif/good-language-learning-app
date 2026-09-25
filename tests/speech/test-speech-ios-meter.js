// Unit Test: iOS cloud-STT sessions whose level meter can't hear.
// iOS Safari leaves an AudioContext suspended when it isn't created inside the
// user's tap, so the meter reads silence and the 10s initial-silence timer used
// to fire 'no-speech' -- dropping Speaking Studio into self-evaluation from the
// second sentence on. Verifies:
// 1. The meter AudioContext is created synchronously inside startListening
// 2. A blind (suspended) meter sends the recording to Whisper instead of 'no-speech'
// 3. A running meter that hears nothing still reports 'no-speech'

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Testing SpeechInput iOS meter / initial-silence handling ---');

global.window = global;
global.document = { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [] };
const storage = {};
global.localStorage = {
    getItem: k => storage[k] || null,
    setItem: (k, v) => { storage[k] = String(v); },
    removeItem: k => { delete storage[k]; }
};

class MockMediaRecorder {
    constructor() { this.state = 'inactive'; this.mimeType = 'audio/mp4'; }
    start() { this.state = 'recording'; }
    stop() {
        this.state = 'inactive';
        if (this.ondataavailable) this.ondataavailable({ data: { size: 500 } });
        if (this.onstop) this.onstop();
    }
}
MockMediaRecorder.isTypeSupported = () => true;
global.MediaRecorder = MockMediaRecorder;

global.navigator = {};
Object.defineProperty(global.navigator, 'userAgent', {
    value: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
    configurable: true
});
const track = { readyState: 'live', stop: () => {} };
global.navigator.mediaDevices = {
    getUserMedia: async () => ({ active: true, getAudioTracks: () => [track], getTracks: () => [track] })
};

global.Blob = class { constructor(c, o) { this.type = (o && o.type) || 'audio/webm'; this.size = 500; } };
global.URL = { createObjectURL: () => 'blob:mock', revokeObjectURL: () => {} };
global.fetch = async () => ({ ok: true, status: 200, json: async () => ({ text: 'hola' }) });

// AudioContext mock: 'running' controls whether resume() takes effect.
let ctxCreatedDuringStart = 0;
let resumeWorks = false;
class MockAudioContext {
    constructor() { this.state = 'suspended'; ctxCreatedDuringStart++; }
    resume() { if (resumeWorks) this.state = 'running'; return Promise.resolve(); }
    close() { this.state = 'closed'; return Promise.resolve(); }
    createMediaStreamSource() { return { connect: () => {} }; }
    createAnalyser() {
        return { fftSize: 0, frequencyBinCount: 8, getByteFrequencyData: arr => arr.fill(0) };
    }
}
global.AudioContext = MockAudioContext;

// Shrink the 10s initial-silence timer so the test runs fast.
const realSetTimeout = setTimeout;
global.setTimeout = (fn, ms, ...a) => realSetTimeout(fn, ms === 10000 ? 30 : ms, ...a);
const wait = ms => new Promise(r => realSetTimeout(r, ms));

eval(fs.readFileSync(path.join(__dirname, '../../engine/speech-input.js'), 'utf8'));

async function listenInSilence() {
    const result = { errors: [], finals: [] };
    SpeechInput.startListening({
        target: 'hola',
        preferRecording: true,
        lang: 'es-ES',
        onAudioLevel: () => {},
        onAudioReady: () => {},
        onError: e => result.errors.push(e),
        onFinal: t => result.finals.push(t)
    });
    result.createdSync = ctxCreatedDuringStart;
    await wait(150);
    return result;
}

async function runTests() {
    console.log('1-2. Suspended meter (iOS): recording goes to Whisper, no no-speech...');
    ctxCreatedDuringStart = 0;
    resumeWorks = false;
    let r = await listenInSilence();
    assert.strictEqual(r.createdSync, 1, 'AudioContext must be created synchronously inside startListening');
    assert.deepStrictEqual(r.errors, [], 'Blind meter must not report no-speech');
    assert.deepStrictEqual(r.finals, ['hola'], 'Recording must be transcribed and delivered via onFinal');
    console.log('✓ Suspended meter falls through to Whisper transcription');

    console.log('3. Running meter hearing silence still reports no-speech...');
    resumeWorks = true;
    r = await listenInSilence();
    assert.deepStrictEqual(r.errors, ['no-speech'], 'Working meter with no voice must report no-speech');
    console.log('✓ Genuine silence still reported');

    console.log('\nAll iOS meter tests passed successfully!');
    process.exit(0);
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
