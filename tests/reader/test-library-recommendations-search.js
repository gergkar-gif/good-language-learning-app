// ==========================================================
// Unit Tests: Library Recommendations & Bilingual Topic Search
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock browser globals
global.window = global;

const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { Object.keys(mockStorage).forEach(k => delete mockStorage[k]); }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `parlour_es_${k}`,
    content: (p) => p
};

let currentMockLevel = 'A1';
global.LearnerPath = {
    currentLevel: () => currentMockLevel,
    isUnitCompleted: (unitId) => unitId === 'unit-01'
};

global.Art = {
    icon: (name) => `<svg class="art-${name}"></svg>`
};

// Document mock
class MockElement {
    constructor(tagName = 'div', attrs = {}) {
        this.tagName = tagName.toUpperCase();
        this._classList = new Set();
        this.attributes = { ...attrs };
        this.children = [];
        this.parentElement = null;
        this._text = '';
        this._listeners = {};
    }

    setAttribute(k, v) { this.attributes[k] = String(v); }
    getAttribute(k) { return this.attributes[k] !== undefined ? this.attributes[k] : null; }
    removeAttribute(k) { delete this.attributes[k]; }

    get classList() {
        const self = this;
        return {
            add: (c) => self._classList.add(c),
            remove: (c) => self._classList.delete(c),
            contains: (c) => self._classList.has(c),
            toggle: (c, force) => {
                if (force !== undefined) {
                    if (force) self._classList.add(c);
                    else self._classList.delete(c);
                    return force;
                }
                if (self._classList.has(c)) {
                    self._classList.delete(c);
                    return false;
                } else {
                    self._classList.add(c);
                    return true;
                }
            }
        };
    }

    get className() { return Array.from(this._classList).join(' '); }
    set className(v) {
        this._classList.clear();
        if (v) v.split(/\s+/).filter(Boolean).forEach(c => this._classList.add(c));
    }

    get textContent() { return this._text; }
    set textContent(v) { this._text = String(v); }
    get innerHTML() {
        return this._text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }
    set innerHTML(v) { this._text = String(v); }

    querySelector(selector) {
        return this.querySelectorAll(selector)[0] || null;
    }

    querySelectorAll(selector) {
        const results = [];
        const match = (el) => {
            if (selector.startsWith('.')) {
                const cls = selector.slice(1);
                if (el._classList.has(cls)) results.push(el);
            } else if (selector.startsWith('#')) {
                const id = selector.slice(1);
                if (el.getAttribute('id') === id) results.push(el);
            } else if (selector.startsWith('[') && selector.endsWith(']')) {
                const attr = selector.slice(1, -1);
                if (el.getAttribute(attr) !== null) results.push(el);
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

    appendChild(child) {
        child.parentElement = this;
        this.children.push(child);
        return child;
    }

    remove() {
        if (this.parentElement) {
            const idx = this.parentElement.children.indexOf(this);
            if (idx >= 0) this.parentElement.children.splice(idx, 1);
        }
    }
}

global.document = {
    createElement: (tag) => new MockElement(tag),
    getElementById: (id) => null,
    addEventListener: () => {},
    removeEventListener: () => {}
};

// Require reader engine
const Reader = require('../../engine/reader.js');

// Load Spanish manifest for realistic tests
const esManifestPath = path.resolve(__dirname, '../../content/es/stories/manifest.json');
const manifestData = JSON.parse(fs.readFileSync(esManifestPath, 'utf8'));
assert(Array.isArray(manifestData.stories), 'Manifest must contain stories array');
Reader.stories = manifestData.stories;

// Ensure zero emojis in text
function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}: ${str}`);
}

console.log('--- Test 1: Comfortable & Challenging Recommendations for A1 Learner ---');
currentMockLevel = 'A1';
global.localStorage.clear();

let recs = Reader.getRecommendations();
assert(recs, 'Recommendations must be returned');
assert(recs.comfortable && recs.comfortable.story, 'Comfortable recommendation required');
assert(recs.challenging && recs.challenging.story, 'Challenging recommendation required');

assert.strictEqual((recs.comfortable.story.level || '').toUpperCase(), 'A1', 'Comfortable pick for A1 learner should be A1');
assert(recs.comfortable.reason.length > 5, 'Reason must be descriptive');
assertZeroEmojis(recs.comfortable.reason, 'Comfortable reason');

// For A1 learner, next level is A2 which exists in manifest
const challLevel = (recs.challenging.story.level || '').toUpperCase();
assert.strictEqual(challLevel, 'A2', `Challenging level for A1 learner should step up to A2, got ${challLevel}`);
assert(recs.challenging.reason.length > 5, 'Reason must be descriptive');
assertZeroEmojis(recs.challenging.reason, 'Challenging reason');

// Verify HTML generation
const htmlA1 = Reader.buildRecommendationsHtml();
assert(htmlA1.includes('lib-recs-container'), 'HTML must include container');
assert(htmlA1.includes('badge-comfortable'), 'HTML must include comfortable badge');
assert(htmlA1.includes('badge-challenging'), 'HTML must include challenging badge');
assert(htmlA1.includes(recs.comfortable.story.title), 'HTML must show comfortable story title');
assert(htmlA1.includes(recs.challenging.story.title), 'HTML must show challenging story title');
assertZeroEmojis(htmlA1, 'buildRecommendationsHtml output');
console.log(`[PASS] A1 learner received: Comfortable (${recs.comfortable.story.level} - "${recs.comfortable.story.title}"), Challenging (${recs.challenging.story.level} - "${recs.challenging.story.title}")`);

console.log('\n--- Test 2: Recommendations for B1 Learner ---');
currentMockLevel = 'B1';
recs = Reader.getRecommendations();
assert(recs.comfortable && recs.challenging, 'Recommendations must exist for B1');
assert.strictEqual((recs.comfortable.story.level || '').toUpperCase(), 'B1', 'Comfortable pick for B1 learner should be B1');
// When next level (B2) is not yet in manifest, recommender picks deep authentic narrative in B1 (or B2 if added)
const b1ChallLevel = (recs.challenging.story.level || '').toUpperCase();
assert(['B1', 'B2'].includes(b1ChallLevel), `Challenging pick for B1 learner should be B1 (deep narrative) or B2, got ${b1ChallLevel}`);
assert(recs.challenging.reason.length > 5, 'Challenging reason must be descriptive');
console.log(`[PASS] B1 learner received: Comfortable (${recs.comfortable.story.level} - "${recs.comfortable.story.title}"), Challenging (${recs.challenging.story.level} - "${recs.challenging.story.title}")`);

console.log('\n--- Test 3: Recommendation Pool Resilience when stories are read ---');
// Mark some stories as read
const readStories = [recs.comfortable.story.id, recs.challenging.story.id];
global.localStorage.setItem('parlour_es_readStories', JSON.stringify(readStories));

const recsAfterRead = Reader.getRecommendations();
assert.notStrictEqual(recsAfterRead.comfortable.story.id, recs.comfortable.story.id, 'Should recommend a different unread story');
console.log('[PASS] Recommender respects read stories and surfaces new unread content.');

console.log('\n--- Test 4: Bilingual Topic Search - English query "technology" ---');
// Construct simulated library DOM
const libraryEl = new MockElement('div', { id: 'reader-library' });
const recsEl = new MockElement('div', { class: 'lib-recs-container' });
recsEl.classList.add('lib-recs-container');
libraryEl.appendChild(recsEl);

const searchSummaryEl = new MockElement('div', { id: 'library-search-summary' });
searchSummaryEl.setAttribute('id', 'library-search-summary');
libraryEl.appendChild(searchSummaryEl);

const roomEl = new MockElement('div');
roomEl.classList.add('reading-room');
const shelfEl = new MockElement('div');
shelfEl.classList.add('story-shelf');

// Find a known tech story and a non-tech story from manifest
const techStory = Reader.stories.find(s => s.id === 'story.b1.14') || Reader.stories.find(s => (s.topics || []).some(t => /tecnolog/i.test(t)));
assert(techStory, 'Must find a tech story in manifest');

const nonTechStory = Reader.stories.find(s => s.id !== techStory.id && !(s.topics || []).some(t => /tecnolog/i.test(t)));
assert(nonTechStory, 'Must find a non-tech story in manifest');

const cardTech = new MockElement('div');
cardTech.classList.add('story-card');
cardTech.setAttribute('data-story-id', techStory.id);
shelfEl.appendChild(cardTech);

const cardNonTech = new MockElement('div');
cardNonTech.classList.add('story-card');
cardNonTech.setAttribute('data-story-id', nonTechStory.id);
shelfEl.appendChild(cardNonTech);

roomEl.appendChild(shelfEl);
libraryEl.appendChild(roomEl);

// Search for 'technology'
Reader._filterUniversalSearch('technology', libraryEl);

// Recs should be hidden during search
assert(recsEl.classList.contains('hidden'), 'Recommendations should be hidden when search is active');

// Tech card should be visible and have match badge
assert(!cardTech.classList.contains('hidden'), 'Tech card should be visible for "technology" query');
const techBadge = cardTech.querySelector('.story-card-topic-match');
assert(techBadge, 'Tech card should have topic match badge');
assert.strictEqual(techBadge.textContent, 'Topic match');

// Non-tech card should be hidden
assert(cardNonTech.classList.contains('hidden'), 'Non-tech card should be hidden for "technology" query');
console.log('[PASS] Query "technology" correctly matched topic, tagged card, and hid irrelevant cards.');

console.log('\n--- Test 5: Bilingual Topic Search - Spanish query "tecnologia" ---');
Reader._filterUniversalSearch('tecnologia', libraryEl);
assert(!cardTech.classList.contains('hidden'), 'Tech card should match Spanish "tecnologia" query');
assert(cardNonTech.classList.contains('hidden'), 'Non-tech card should be hidden for "tecnologia" query');
console.log('[PASS] Spanish query "tecnologia" matches same story.');

console.log('\n--- Test 6: Whole-word matching prevents false positives for short words ---');
// Querying a short word like 'red' shouldn't match words containing 'red' as substring (e.g. 'ingredientes')
assert.strictEqual(Reader._matchesTerm('ingredientes para cocinar', 'red'), false, '"red" must not match inside "ingredientes"');
assert.strictEqual(Reader._matchesTerm('la red social en linea', 'red'), true, '"red" must match as standalone word');
console.log('[PASS] Short keyword boundary matching verified.');

console.log('\n--- Test 7: Clearing Search Restores Library View ---');
Reader._filterUniversalSearch('', libraryEl);

// Recs should be visible again
assert(!recsEl.classList.contains('hidden'), 'Recommendations should be restored when query is cleared');
// Cards should be visible and match badges removed
assert(!cardTech.classList.contains('hidden'), 'Tech card should be visible after clearing search');
assert(!cardNonTech.classList.contains('hidden'), 'Non-tech card should be visible after clearing search');
assert(!cardTech.querySelector('.story-card-topic-match'), 'Match badges should be removed upon search clear');
console.log('[PASS] Search clear cleanly restores recommendations and all story cards.');

console.log('\n==========================================================');
console.log('ALL TESTS PASSED [Zero Emojis Enforced]');
console.log('==========================================================');
