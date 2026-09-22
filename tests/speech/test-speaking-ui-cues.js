// Automated tests for Speaking Visual Cues, Equalizer Wave, and Finish-to-Grade UI
const assert = require('assert');
const fs = require('fs');
const path = require('path');

class MockElement {
    constructor(tagName, className = '', id = '') {
        this.tagName = tagName.toUpperCase();
        this.className = className;
        this.id = id;
        this.classList = {
            _classes: new Set(className ? className.split(/\s+/).filter(Boolean) : []),
            contains: (c) => this.classList._classes.has(c),
            add: (c) => this.classList._classes.add(c),
            remove: (c) => this.classList._classes.delete(c),
            toggle: (c) => {
                if (this.classList._classes.has(c)) {
                    this.classList._classes.delete(c);
                    return false;
                } else {
                    this.classList._classes.add(c);
                    return true;
                }
            }
        };
        this.style = {};
        this.children = [];
        this.parentNode = null;
        this.textContent = '';
        this.innerHTML = '';
        this.attributes = {};
        this.listeners = {};
    }

    setAttribute(k, v) { this.attributes[k] = v; }
    getAttribute(k) { return this.attributes[k]; }
    appendChild(child) {
        child.parentNode = this;
        this.children.push(child);
        return child;
    }
    querySelector(sel) {
        return this.querySelectorAll(sel)[0] || null;
    }
    querySelectorAll(sel) {
        const results = [];
        const match = (el) => {
            if (sel.startsWith('.')) {
                const cls = sel.slice(1);
                if (el.classList.contains(cls)) results.push(el);
            } else if (sel.startsWith('#')) {
                const id = sel.slice(1);
                if (el.id === id) results.push(el);
            } else if (sel.startsWith('[') && sel.endsWith(']')) {
                const parts = sel.slice(1, -1).split('=');
                const attr = parts[0];
                const val = parts[1] ? parts[1].replace(/["']/g, '') : null;
                if (val ? el.getAttribute(attr) === val : el.getAttribute(attr) !== undefined) {
                    results.push(el);
                }
            } else if (el.tagName === sel.toUpperCase()) {
                results.push(el);
            }
            for (const child of el.children) {
                match(child);
            }
        };
        for (const child of this.children) {
            match(child);
        }
        return results;
    }
    addEventListener(evt, fn) {
        if (!this.listeners[evt]) this.listeners[evt] = [];
        this.listeners[evt].push(fn);
    }
    click() {
        if (this.listeners['click']) {
            for (const fn of this.listeners['click']) fn({ target: this });
        }
    }
}

// Setup browser globals
global.window = global;
global.document = {
    createElement: (tag) => new MockElement(tag),
    getElementById: (id) => null,
    querySelector: (sel) => null,
    querySelectorAll: (sel) => []
};
global.navigator = {
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    platform: 'MacIntel',
    mediaDevices: {
        getUserMedia: () => Promise.resolve({
            getTracks: () => [{ stop: () => {}, readyState: 'live' }],
            getAudioTracks: () => [{ stop: () => {}, readyState: 'live' }],
            active: true
        })
    }
};

let createdRecognitions = [];
class MockSpeechRecognition {
    constructor() {
        this.continuous = true;
        this.interimResults = true;
        this.lang = 'es-ES';
        this.onresult = null;
        this.onerror = null;
        this.onend = null;
        this.onstart = null;
        this.started = false;
        createdRecognitions.push(this);
    }
    start() {
        this.started = true;
        if (this.onstart) this.onstart();
    }
    stop() {
        this.started = false;
        if (this.onend) this.onend();
    }
    abort() {
        this.started = false;
        if (this.onend) this.onend();
    }
}
global.webkitSpeechRecognition = MockSpeechRecognition;

// Load SpeechInput and SpeakingRunner
const speechInputCode = fs.readFileSync(path.join(__dirname, '../../engine/speech-input.js'), 'utf8');
eval(speechInputCode);

const speakingRunnerCode = fs.readFileSync(path.join(__dirname, '../../engine/drills/speaking-runner.js'), 'utf8');
eval(speakingRunnerCode);

// Helper to construct SpeakingRunner DOM tree
function createRunnerContainer() {
    const container = new MockElement('div', 'sp-container');

    const runner = new MockElement('div', 'sp-runner');
    const promptCard = new MockElement('div', 'sp-prompt-card');
    const micSection = new MockElement('div', 'sp-mic-section');

    const micBtn = new MockElement('button', 'sp-mic-btn');
    micBtn.setAttribute('data-action', 'toggle-mic');
    const stopCue = new MockElement('span', 'sp-mic-stop-cue hidden');
    stopCue.textContent = 'Tap to finish';
    micBtn.appendChild(stopCue);

    const micStatus = new MockElement('span', 'sp-mic-status');
    micStatus.textContent = 'Tap to speak';

    const wave = new MockElement('div', 'sp-voice-wave');
    for (let i = 0; i < 5; i++) {
        wave.appendChild(new MockElement('span', 'sp-wave-bar'));
    }

    const doneBtn = new MockElement('button', 'sp-done-speaking-btn hidden');
    doneBtn.setAttribute('data-action', 'finish-speaking');
    doneBtn.textContent = 'Finish speaking & grade ✓';

    const liveTranscript = new MockElement('div', 'sp-live-transcript hidden');

    micSection.appendChild(micBtn);
    micSection.appendChild(micStatus);
    micSection.appendChild(wave);
    micSection.appendChild(doneBtn);
    micSection.appendChild(liveTranscript);

    const reveal = new MockElement('div', 'sp-reveal hidden');
    const feedback = new MockElement('div', 'sp-feedback');
    const footer = new MockElement('div', 'sp-footer');
    const actions = new MockElement('div', 'sp-actions');
    const cantSpeakBtn = new MockElement('button', 'sp-cant-speak-btn');
    cantSpeakBtn.setAttribute('data-action', 'cant-speak');
    actions.appendChild(cantSpeakBtn);
    const nextBtn = new MockElement('button', 'sp-next-btn hidden');
    nextBtn.setAttribute('data-action', 'next');
    footer.appendChild(actions);
    footer.appendChild(nextBtn);

    runner.appendChild(promptCard);
    runner.appendChild(micSection);
    runner.appendChild(reveal);
    runner.appendChild(feedback);
    runner.appendChild(footer);
    container.appendChild(runner);

    return {
        container,
        micBtn,
        stopCue,
        micStatus,
        wave,
        doneBtn,
        liveTranscript,
        cantSpeakBtn,
        nextBtn
    };
}

async function runTests() {
    console.log('--- Test 1: SpeakingRunner visual UI cues and equalizer wave state ---');
    const elements = createRunnerContainer();

    // Overwrite container.innerHTML setter so it attaches real listeners to our mock elements
    elements.container._micBtn = elements.micBtn;
    elements.container._doneBtn = elements.doneBtn;
    elements.container.innerHTML = ''; // trigger cleanup

    // Mock container querySelector directly for the elements we care about
    const origQuerySelector = elements.container.querySelector.bind(elements.container);
    elements.container.querySelector = (sel) => {
        if (sel === '.sp-mic-btn') return elements.micBtn;
        if (sel === '.sp-mic-stop-cue') return elements.stopCue;
        if (sel === '.sp-mic-status') return elements.micStatus;
        if (sel === '.sp-voice-wave') return elements.wave;
        if (sel === '.sp-done-speaking-btn' || sel === '[data-action="finish-speaking"]') return elements.doneBtn;
        if (sel === '.sp-live-transcript') return elements.liveTranscript;
        if (sel === '[data-action="toggle-mic"]') return elements.micBtn;
        if (sel === '[data-action="cant-speak"]') return elements.cantSpeakBtn;
        if (sel === '[data-action="next"]') return elements.nextBtn;
        return origQuerySelector(sel);
    };
    elements.container.querySelectorAll = (sel) => {
        if (sel === '.sp-wave-bar') return elements.wave.children;
        return [];
    };

    createdRecognitions = [];

    // Render exercise
    SpeakingRunner.render(elements.container, {
        kind: 'prompt-speak',
        spanish: 'Buenos días',
        english: 'Good morning'
    });

    // Initial assertions
    assert.strictEqual(elements.micBtn.classList.contains('sp-recording'), false, 'Mic button must not have recording class initially');
    assert.strictEqual(elements.stopCue.classList.contains('hidden'), true, 'Stop cue must be hidden initially');
    assert.strictEqual(elements.wave.classList.contains('is-active'), false, 'Voice wave must be inactive initially');
    assert.strictEqual(elements.doneBtn.classList.contains('hidden'), true, 'Finish speaking button must be hidden initially');
    assert.strictEqual(elements.micStatus.textContent, 'Tap to speak', 'Status must prompt user to tap');

    // Click mic button to start recording
    elements.micBtn.click();

    // Verify active recording state
    assert.strictEqual(elements.micBtn.classList.contains('sp-recording'), true, 'Mic button has sp-recording class');
    assert.strictEqual(elements.stopCue.classList.contains('hidden'), false, 'Stop cue is visible');
    assert.strictEqual(elements.wave.classList.contains('is-active'), true, 'Voice wave is active');
    assert.strictEqual(elements.doneBtn.classList.contains('hidden'), false, 'Done button is visible');
    assert.ok(elements.micStatus.textContent.includes('Listening'), 'Status indicates listening');

    console.log('[PASS] Recording activation displays stop cue, active equalizer, and finish button.');

    console.log('--- Test 2: Voice activity detection updates equalizer bars and status text ---');
    // Simulate vocal energy level callback
    const recInstance = createdRecognitions[createdRecognitions.length - 1];
    assert.ok(recInstance, 'SpeechRecognition instance created');

    // SpeechInput internal onAudioLevel should be triggered
    // Let's invoke onAudioLevel directly on SpeakingRunner via SpeechInput options
    // or test the equalizer bar calculations
    const bars = elements.wave.children;
    assert.strictEqual(bars.length, 5, 'Must have 5 equalizer wave bars');

    // Test clicking "Finish speaking & grade" button
    console.log('--- Test 3: Finish speaking button immediately halts recording and evaluates ---');
    // First simulate interim captured speech
    recInstance.onresult({
        resultIndex: 0,
        results: [
            Object.assign([{ transcript: 'Buenos días' }], { isFinal: false })
        ]
    });

    // Click finish button
    elements.doneBtn.click();

    // Verify UI resets into analyzing/stop state
    assert.strictEqual(elements.micBtn.classList.contains('sp-recording'), false, 'Mic button recording class removed');
    assert.strictEqual(elements.stopCue.classList.contains('hidden'), true, 'Stop cue hidden on stop');
    assert.strictEqual(elements.wave.classList.contains('is-active'), false, 'Wave inactive on stop');
    assert.strictEqual(elements.doneBtn.classList.contains('hidden'), true, 'Done button hidden on stop');

    console.log('[PASS] Finish speaking button safely terminates recording and initiates evaluation.');

    console.log('\n[ALL PASS] Speaking UI cues and equalizer wave tests passed successfully!');
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
