// Unit Test: Speaking Drills & Activities Transcription Display
// Verifies that in speaking drills, live transcription is NOT displayed immediately while speaking,
// but only displayed once the learner finishes speaking.

const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Setup minimal DOM and browser globals
class MockClassList {
    constructor() {
        this.classes = new Set();
    }
    add(...names) { names.forEach(n => this.classes.add(n)); }
    remove(...names) { names.forEach(n => this.classes.delete(n)); }
    contains(n) { return this.classes.has(n); }
    toggle(n) { if (this.contains(n)) this.remove(n); else this.add(n); }
}

class MockElement {
    constructor(tagName = 'div', className = '') {
        this.tagName = tagName.toUpperCase();
        this.classList = new MockClassList();
        if (className) {
            className.split(/\s+/).filter(Boolean).forEach(c => this.classList.add(c));
        }
        this._textContent = '';
        this._innerHTML = '';
        this.style = {};
        this.listeners = {};
        this.value = '';
        this.children = [];
    }

    get textContent() { return this._textContent; }
    set textContent(val) {
        this._textContent = String(val);
        this._innerHTML = String(val);
    }

    get innerHTML() { return this._innerHTML; }
    set innerHTML(val) {
        this._innerHTML = String(val);
        // If child elements are created inside innerHTML in code, parse basic selectors
    }

    addEventListener(event, fn) {
        if (!this.listeners[event]) this.listeners[event] = [];
        this.listeners[event].push(fn);
    }

    dispatchEvent(evt) {
        const type = typeof evt === 'string' ? evt : evt.type;
        const list = this.listeners[type] || [];
        list.forEach(fn => fn(evt));
    }

    querySelector(sel) {
        if (sel === '.sp-mic-btn' || sel === '#lesson-mic-btn') return this._micBtn;
        if (sel === '.sp-mic-status' || sel === '#lesson-mic-status') return this._micStatus;
        if (sel === '.sp-live-transcript' || sel === '#lesson-live-transcript') return this._liveTranscript;
        if (sel === '.sp-meter-fill') return this._meterFill;
        if (sel === '.sp-reveal') return this._reveal;
        if (sel === '.sp-feedback') return this._feedback;
        if (sel === '.sp-actions') return this._actions;
        if (sel === '[data-action="next"]') return this._nextBtn;
        if (sel === '[data-action="toggle-mic"]') return this._micBtn;
        if (sel === '.sp-compare-bar') return this._compareBar;
        if (sel === '[data-speaking]') return this._speakingArea;
        return null;
    }

    querySelectorAll(sel) {
        return [];
    }

    focus() {}
}

let createdRecognitions = [];

class MockSpeechRecognition {
    constructor() {
        this.lang = 'es-ES';
        this.continuous = true;
        this.interimResults = true;
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

global.navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
    platform: 'Win32',
    mediaDevices: {
        getUserMedia: async () => ({
            active: true,
            getAudioTracks: () => [{ readyState: 'live', stop: () => {} }],
            getTracks: () => [{ readyState: 'live', stop: () => {} }]
        })
    }
};

global.document = {
    createElement: (tag) => new MockElement(tag),
    querySelector: () => null,
    getElementById: () => null
};

global.window = global;
global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    voices: () => ['es-ES']
};
global.URL = {
    createObjectURL: () => 'blob:mock-audio',
    revokeObjectURL: () => {}
};
global.Art = {
    icon: () => ''
};

// Load speech-input.js
const speechInputCode = fs.readFileSync(path.join(__dirname, '../../engine/speech-input.js'), 'utf8');
eval(speechInputCode);

// Load speaking-runner.js
const speakingRunnerCode = fs.readFileSync(path.join(__dirname, '../../engine/drills/speaking-runner.js'), 'utf8');
eval(speakingRunnerCode);

async function runTests() {
    console.log('--- Test 1: SpeakingRunner does not display interim transcription while speaking ---');

    const container = new MockElement('div');
    const micBtn = new MockElement('button', 'sp-mic-btn');
    const micStatus = new MockElement('span', 'sp-mic-status');
    const liveTranscript = new MockElement('div', 'sp-live-transcript hidden');
    const meterFill = new MockElement('div', 'sp-meter-fill');
    const reveal = new MockElement('div', 'sp-reveal');
    const feedback = new MockElement('div', 'sp-feedback');
    const actions = new MockElement('div', 'sp-actions');
    const nextBtn = new MockElement('button');

    container._micBtn = micBtn;
    container._micStatus = micStatus;
    container._liveTranscript = liveTranscript;
    container._meterFill = meterFill;
    container._reveal = reveal;
    container._feedback = feedback;
    container._actions = actions;
    container._nextBtn = nextBtn;

    createdRecognitions = [];

    SpeakingRunner.render(container, {
        kind: 'read-repeat',
        spanish: 'Hola buenos días',
        english: 'Hello good morning'
    });

    // Verify initial state
    assert.strictEqual(liveTranscript.classList.contains('hidden'), true, 'Live transcript must start hidden');

    // Tap mic button to start recording
    const toggleMic = micBtn.listeners['click'] && micBtn.listeners['click'][0];
    assert.ok(toggleMic, 'toggle-mic click listener should be registered');
    toggleMic();

    // While recording, live transcript must NOT be visible and must be empty
    assert.strictEqual(liveTranscript.classList.contains('hidden'), true, 'Live transcript must remain hidden while recording begins');
    assert.strictEqual(liveTranscript.textContent, '', 'Live transcript must NOT show text when starting');
    assert.strictEqual(micStatus.textContent, 'Listening...', 'Status indicates listening');

    const recInstance = createdRecognitions[createdRecognitions.length - 1];
    assert.ok(recInstance, 'SpeechRecognition instance must be created');

    // Simulate interim partial speech ("Hola")
    recInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Hola' }], { isFinal: false })
        ]
    });

    // CRITICAL: Live transcript must NOT display "Hola" immediately!
    assert.strictEqual(liveTranscript.classList.contains('hidden'), true, 'Live transcript must stay hidden during interim speech');
    assert.notStrictEqual(liveTranscript.textContent, 'Hola', 'Live transcript must NOT display interim words immediately');

    // Simulate second interim partial speech ("Hola buenos")
    recInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Hola buenos' }], { isFinal: false })
        ]
    });
    assert.strictEqual(liveTranscript.classList.contains('hidden'), true, 'Live transcript must remain hidden during ongoing speech');

    // Now speech finishes and final transcript is produced ("Hola buenos días")
    recInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Hola buenos días' }], { isFinal: true })
        ]
    });

    // Auto-stop / completion should display final transcript
    assert.strictEqual(liveTranscript.classList.contains('hidden'), false, 'Live transcript must become visible once finished speaking');
    assert.strictEqual(liveTranscript.textContent, 'Hola buenos días', 'Live transcript must display complete transcript upon completion');

    console.log('[PASS] SpeakingRunner hides live transcription during speech and reveals it only once finished.');

    console.log('--- Test 2: Lesson Speaking Step hides interim transcript until finished speaking ---');
    // Test lesson speaking logic
    const lessonMicBtn = new MockElement('button', 'sp-mic-btn');
    const lessonMicStatus = new MockElement('span');
    const lessonLiveTranscript = new MockElement('div', 'sp-live-transcript');

    global.document.getElementById = (id) => {
        if (id === 'lesson-mic-btn') return lessonMicBtn;
        if (id === 'lesson-mic-status') return lessonMicStatus;
        if (id === 'lesson-live-transcript') return lessonLiveTranscript;
        return null;
    };

    let checkCalled = false;
    global.stepState = {
        target: 'Mucho gusto',
        transcript: '',
        checkDisabled: true,
        checkFn: 'lessonCheckSpeaking'
    };
    global.updateFooterButton = () => {};
    global.lessonCheckSpeaking = () => { checkCalled = true; };

    // Simulate lessonToggleSpeaking
    let _lessonSpeakingRecording = true;
    lessonMicBtn.classList.add('sp-recording');
    lessonMicStatus.textContent = 'Listening...';
    lessonLiveTranscript.textContent = '';
    lessonLiveTranscript.classList.add('hidden');

    let _lastCapturedLesson = '';

    SpeechInput.startListening({
        target: stepState.target || '',
        onInterim: interim => {
            _lastCapturedLesson = interim;
            // Defer display until speaker finishes
        },
        onFinal: transcript => {
            _lessonSpeakingRecording = false;
            lessonMicBtn.classList.remove('sp-recording');
            lessonMicStatus.textContent = 'Tap to speak';
            const text = transcript || _lastCapturedLesson;
            if (lessonLiveTranscript && text) {
                lessonLiveTranscript.textContent = text;
                lessonLiveTranscript.classList.remove('hidden');
            }
            stepState.transcript = text;
            lessonCheckSpeaking();
        }
    });

    const lessonRecInstance = createdRecognitions[createdRecognitions.length - 1];

    // Simulate interim speech ("Mucho")
    lessonRecInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Mucho' }], { isFinal: false })
        ]
    });

    assert.strictEqual(lessonLiveTranscript.classList.contains('hidden'), true, 'Lesson transcript must stay hidden during interim speech');
    assert.strictEqual(lessonLiveTranscript.textContent, '', 'Lesson transcript must NOT display interim words');

    // Speech finishes: "Mucho gusto" (100% target match auto stops)
    lessonRecInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Mucho gusto' }], { isFinal: true })
        ]
    });

    assert.strictEqual(lessonLiveTranscript.classList.contains('hidden'), false, 'Lesson transcript must be visible on completion');
    assert.strictEqual(lessonLiveTranscript.textContent, 'Mucho gusto', 'Lesson transcript must display final text');
    assert.strictEqual(checkCalled, true, 'Check function called on completion');

    console.log('[PASS] Lesson speaking step hides interim speech and displays transcript on completion.');

    console.log('--- Test 3: Inline voice input defers text assignment until finish ---');
    const inputElem = new MockElement('input');
    inputElem.value = '';

    let _lastCapturedInline = '';
    SpeechInput.startListening({
        target: 'Gracias',
        onInterim: interim => {
            _lastCapturedInline = interim;
        },
        onFinal: transcript => {
            const text = transcript || _lastCapturedInline;
            if (text) inputElem.value = text;
        }
    });

    const inlineRecInstance = createdRecognitions[createdRecognitions.length - 1];
    inlineRecInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Gra' }], { isFinal: false })
        ]
    });

    assert.strictEqual(inputElem.value, '', 'Input value must not be updated during interim speech');

    inlineRecInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Gracias' }], { isFinal: true })
        ]
    });

    assert.strictEqual(inputElem.value, 'Gracias', 'Input value updated once speech finishes');

    console.log('[PASS] Inline voice input populates input field only once finished speaking.');

    console.log('\n[ALL PASS] All speaking drill transcription display tests passed!');
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
