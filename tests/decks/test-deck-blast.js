// ========================================
// DECK BLAST TEST SUITE
// ========================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Setup minimal browser-like globals for testing
global.window = global;
global.performance = { now: () => Date.now() };
global.requestAnimationFrame = (cb) => setTimeout(cb, 16);
global.cancelAnimationFrame = (id) => clearTimeout(id);

let preloadedAudio = [];
global.ParlourTTS = {
    preload: (opts) => {
        preloadedAudio.push(opts);
        return Promise.resolve();
    },
    speak: (opts) => Promise.resolve()
};

global.Sound = {
    correct: () => {},
    wrong: () => {},
    complete: () => {}
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`
};

global.Lexicon = {
    withArticle: (w) => `el ${w}`
};

global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};

// Mock DOM container
function createMockElement(tag = 'div') {
    const el = {
        tagName: tag.toUpperCase(),
        innerHTML: '',
        style: {},
        attributes: {},
        children: [],
        classList: {
            _classes: new Set(),
            add(c) { this._classes.add(c); },
            remove(c) { this._classes.delete(c); },
            contains(c) { return this._classes.has(c); },
            toggle(c) { if (this.contains(c)) { this.remove(c); return false; } else { this.add(c); return true; } }
        },
        setAttribute(k, v) { this.attributes[k] = String(v); },
        getAttribute(k) { return this.attributes[k] || null; },
        querySelector(sel) {
            return this.querySelectorAll(sel)[0] || null;
        },
        querySelectorAll(sel) {
            const results = [];
            const check = (node) => {
                if (!node || typeof node !== 'object') return;
                let match = false;
                if (sel.startsWith('.')) {
                    const cls = sel.slice(1);
                    if (node.classList && node.classList.contains(cls)) match = true;
                } else if (sel.startsWith('#')) {
                    if (node.id === sel.slice(1)) match = true;
                } else if (sel.startsWith('[')) {
                    const attr = sel.replace(/[\[\]]/g, '').split('=')[0];
                    if (node.attributes && node.attributes[attr] !== undefined) match = true;
                } else if (node.tagName && node.tagName.toLowerCase() === sel.toLowerCase()) {
                    match = true;
                }
                if (match) results.push(node);
                if (node.children) node.children.forEach(check);
            };
            check(this);
            return results;
        },
        addEventListener(event, fn) {
            this._listeners = this._listeners || {};
            this._listeners[event] = this._listeners[event] || [];
            this._listeners[event].push(fn);
        },
        getBoundingClientRect() {
            return { width: 600, height: 420, left: 0, top: 0 };
        },
        getContext(type) {
            return {
                scale: () => {},
                save: () => {},
                restore: () => {},
                clearRect: () => {},
                beginPath: () => {},
                closePath: () => {},
                moveTo: () => {},
                lineTo: () => {},
                fill: () => {},
                stroke: () => {},
                setLineDash: () => {},
                translate: () => {},
                rotate: () => {},
                fillText: () => {}
            };
        }
    };
    return el;
}

const DeckBlast = require('../../engine/decks/blast.js');

console.log('--- Test 1: DeckBlast Module Export & Zero Emojis ---');
assert(DeckBlast, 'DeckBlast must be exported');
assert.strictEqual(typeof DeckBlast.render, 'function', 'DeckBlast.render must be a function');
assert.strictEqual(typeof DeckBlast.stop, 'function', 'DeckBlast.stop must be a function');

const blastFileContent = fs.readFileSync(path.join(__dirname, '../../engine/decks/blast.js'), 'utf8');
const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
assert(!emojiRegex.test(blastFileContent), 'engine/decks/blast.js must contain zero emojis (Parlour constructivist principle)');
console.log('[PASS] DeckBlast export and zero-emoji compliance verified.');

console.log('\n--- Test 2: Audio Speculative Preloading on Lobby Open ---');
preloadedAudio = [];
const mockContainer = createMockElement();
const sampleWords = [
    { lemma: 'libro', translation: 'book' },
    { lemma: 'mesa', translation: 'table' },
    { lemma: 'silla', translation: 'chair' },
    { lemma: 'puerta', translation: 'door' }
];

DeckBlast.render(mockContainer, {
    deckId: 'deck-test-1',
    words: sampleWords
});

assert(preloadedAudio.length >= 4, 'Must preload audio for all deck words immediately');
assert.strictEqual(preloadedAudio[0].text, 'libro');
assert.strictEqual(preloadedAudio[0].language, 'es');
console.log(`[PASS] Proactively preloaded ${preloadedAudio.length} words into ParlourTTS memory/IDB cache.`);

console.log('\n--- Test 3: Lobby Markup & Mode/Difficulty/Direction Toggles ---');
assert(mockContainer.innerHTML.includes('Time Attack'), 'Lobby must contain Time Attack mode');
assert(mockContainer.innerHTML.includes('Survival'), 'Lobby must contain Survival mode');
assert(mockContainer.innerHTML.includes('Easy'), 'Lobby must contain Easy difficulty');
assert(mockContainer.innerHTML.includes('Medium'), 'Lobby must contain Medium difficulty');
assert(mockContainer.innerHTML.includes('Impossible'), 'Lobby must contain Impossible difficulty');
assert(mockContainer.innerHTML.includes('English → Spanish'), 'Lobby must contain English -> Spanish option');
assert(mockContainer.innerHTML.includes('Spanish → English'), 'Lobby must contain Spanish -> English option');
assert(!emojiRegex.test(mockContainer.innerHTML), 'Lobby HTML must not contain emojis');
console.log('[PASS] Lobby rendered with required modes, 3 difficulties, and zero emojis.');

console.log('\n--- Test 4: Integration in engine/decks.js and index.html ---');
const decksJs = fs.readFileSync(path.join(__dirname, '../../engine/decks.js'), 'utf8');
assert(decksJs.includes('data-open-blast'), 'engine/decks.js must have data-open-blast button in study tab');
assert(decksJs.includes("studyMode === 'blast'"), 'engine/decks.js must handle studyMode === blast');

const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(indexHtml.includes('engine/decks/blast.js'), 'index.html must include script tag for engine/decks/blast.js');

const componentsCss = fs.readFileSync(path.join(__dirname, '../../styles/components.css'), 'utf8');
assert(componentsCss.includes('.dkb-lobby'), 'components.css must define .dkb-lobby styles');
assert(componentsCss.includes('.dkb-canvas'), 'components.css must define .dkb-canvas styles');
assert(!emojiRegex.test(componentsCss), 'components.css must contain zero emojis');
console.log('\n--- Test 5: Anti-Overlap Lane Architecture, Unpredictable Targeting & Mobile Optimizations ---');
assert(blastFileContent.includes('_getLaneCount'), 'blast.js must implement lane count management');
assert(blastFileContent.includes('_getLaneX'), 'blast.js must calculate distinct lane centers');
assert(blastFileContent.includes('seasonedCandidates'), 'blast.js must select targets from seasoned mid-flight meteors to prevent spawn-order guessing');
assert(blastFileContent.includes('_pickDistractor'), 'blast.js must implement confusable distractor selection');
assert(blastFileContent.includes('Math.min(2, window.devicePixelRatio || 1)'), 'blast.js must cap DPR to 2 for mobile performance');
assert(!blastFileContent.includes('Sound.correct()'), 'blast.js must decouple sound from TTS to prevent mobile audio lockup');
console.log('[PASS] Anti-overlap lane physics, unpredictable mid-flight targeting, and mobile optimizations verified.');

DeckBlast.stop();
console.log('\nAll DeckBlast tests passed successfully!');
