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
let simulatedFreqValue = 0;
class MockAudioContext {
    constructor() { this.state = 'suspended'; ctxCreatedDuringStart++; }
    resume() { if (resumeWorks) this.state = 'running'; return Promise.resolve(); }
    close() { this.state = 'closed'; return Promise.resolve(); }
    createMediaStreamSource() { return { connect: () => {}, disconnect: () => {} }; }
    createAnalyser() {
        return {
            fftSize: 64,
            frequencyBinCount: 8,
            connect: () => {},
            disconnect: () => {},
            getByteFrequencyData: arr => arr.fill(simulatedFreqValue),
            getByteTimeDomainData: arr => arr.fill(128)
        };
    }
}
global.AudioContext = MockAudioContext;

// Shrink the 10s initial-silence and 2.6s finish timers so the test runs fast.
const realSetTimeout = setTimeout;
let silenceTimerMs = 30;
global.setTimeout = (fn, ms, ...a) => realSetTimeout(fn, ms === 10000 ? silenceTimerMs : (ms === 2600 ? 30 : ms), ...a);
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
    simulatedFreqValue = 0;
    silenceTimerMs = 30;
    let r = await listenInSilence();
    assert.strictEqual(r.createdSync, 1, 'AudioContext must be created synchronously inside startListening');
    assert.deepStrictEqual(r.errors, [], 'Blind meter must not report no-speech');
    assert.deepStrictEqual(r.finals, ['hola'], 'Recording must be transcribed and delivered via onFinal');
    console.log('✓ Suspended meter falls through to Whisper transcription');

    console.log('3. Running meter hearing silence still reports no-speech...');
    resumeWorks = true;
    simulatedFreqValue = 0;
    silenceTimerMs = 30;
    r = await listenInSilence();
    assert.deepStrictEqual(r.errors, ['no-speech'], 'Working meter with no voice must report no-speech');
    console.log('✓ Genuine silence still reported');

    console.log('4. Short utterance (2 frames / 120ms) without onAudioLevel auto-commits via VAD...');
    resumeWorks = true;
    simulatedFreqValue = 40; // > 0.06 threshold
    silenceTimerMs = 500;
    const shortResult = { errors: [], finals: [] };
    SpeechInput.startListening({
        target: 'hola',
        preferRecording: true,
        lang: 'es-ES',
        onError: e => shortResult.errors.push(e),
        onFinal: t => shortResult.finals.push(t)
    });
    await wait(140); // 2 meter ticks (120ms) of speech
    simulatedFreqValue = 0; // silence after short utterance
    await wait(160); // wait for next tick + shortened _finishTimeout (40ms)
    assert.deepStrictEqual(shortResult.errors, [], 'Short utterance must not report error');
    assert.deepStrictEqual(shortResult.finals, ['hola'], 'Short utterance must auto-commit via _finishTimeout');
    console.log('✓ Short utterance auto-commits cleanly without hanging');

    console.log('5. cancelListening aborts session without firing onFinal or onError...');
    const cancelResult = { errors: [], finals: [] };
    SpeechInput.startListening({
        target: 'hola',
        preferRecording: true,
        lang: 'es-ES',
        onError: e => cancelResult.errors.push(e),
        onFinal: t => cancelResult.finals.push(t)
    });
    await wait(20);
    SpeechInput.cancelListening();
    await wait(100);
    assert.strictEqual(SpeechInput.isListening(), false, 'cancelListening must stop listening');
    assert.deepStrictEqual(cancelResult.errors, [], 'cancelListening must not fire onError');
    assert.deepStrictEqual(cancelResult.finals, [], 'cancelListening must not fire onFinal');
    console.log('✓ cancelListening suppresses stale callbacks');

    console.log('6. Async iOS WebKit MediaRecorder.stop() flushes chunks before stopping tracks or leaving play-and-record...');
    let trackAliveAtFlush = false;
    let sessionAtFlush = null;
    let trackStoppedAfterOnstop = false;
    global.navigator.audioSession = { type: 'playback' };
    const asyncTrack = {
        readyState: 'live',
        stop() { this.readyState = 'ended'; trackStoppedAfterOnstop = true; }
    };
    const origGetUserMedia = global.navigator.mediaDevices.getUserMedia;
    global.navigator.mediaDevices.getUserMedia = async () => ({
        active: true,
        getAudioTracks: () => [asyncTrack],
        getTracks: () => [asyncTrack]
    });
    class AsyncIosMediaRecorder {
        constructor() { this.state = 'inactive'; this.mimeType = 'audio/mp4'; }
        start() { this.state = 'recording'; }
        stop() {
            this.state = 'inactive';
            realSetTimeout(() => {
                trackAliveAtFlush = (asyncTrack.readyState === 'live');
                sessionAtFlush = global.navigator.audioSession.type;
                // Simulate iOS WebKit AVAssetWriter producing 0 bytes if track was already killed
                const size = trackAliveAtFlush ? 500 : 0;
                if (this.ondataavailable) this.ondataavailable({ data: { size } });
                if (this.onstop) this.onstop();
            }, 25);
        }
    }
    AsyncIosMediaRecorder.isTypeSupported = () => true;
    global.MediaRecorder = AsyncIosMediaRecorder;

    const asyncRecResult = { audioUrls: [], finals: [], errors: [] };
    SpeechInput.startListening({
        target: 'hola',
        preferRecording: true,
        lang: 'es-ES',
        onAudioReady: u => asyncRecResult.audioUrls.push(u),
        onFinal: t => asyncRecResult.finals.push(t),
        onError: e => asyncRecResult.errors.push(e)
    });
    await wait(20);
    SpeechInput.stopListening();
    assert.strictEqual(asyncTrack.readyState, 'live', 'Track must remain live while async MediaRecorder.stop() flushes');
    await wait(60);
    assert.strictEqual(trackAliveAtFlush, true, 'Track must still be live when ondataavailable flushes');
    assert.strictEqual(sessionAtFlush, 'play-and-record', 'audioSession must stay play-and-record until flush finishes');
    assert.strictEqual(trackStoppedAfterOnstop, true, 'Track must be stopped once recorder.onstop runs');
    assert.strictEqual(global.navigator.audioSession.type, 'playback', 'audioSession must return to playback after recorder.onstop');
    assert.strictEqual(asyncRecResult.audioUrls.length, 1, 'onAudioReady must receive recorded blob URL');
    assert.deepStrictEqual(asyncRecResult.finals, ['hola'], 'onFinal must receive transcribed speech');
    assert.deepStrictEqual(asyncRecResult.errors, [], 'Must not report no-speech');
    global.MediaRecorder = MockMediaRecorder;
    global.navigator.mediaDevices.getUserMedia = origGetUserMedia;
    console.log('✓ Async iOS MediaRecorder flush preserves recording and transcribes cleanly');

    console.log('\nAll iOS meter tests passed successfully!');
    process.exit(0);
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
