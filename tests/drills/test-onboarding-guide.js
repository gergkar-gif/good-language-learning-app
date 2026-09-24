// ============================================
// TEST SUITE: NEW-LEARNER INTRODUCTION (engine/guide.js)
// ============================================
// Verifies:
// 1. Seen-state tracking and localStorage persistence
// 2. Zero emoji pictograms in the guide copy
// 3. End-of-lesson invitations: order, skipping areas already found,
//    coming back once, acceptance
// 4. Deferred sync prompt logic (does not show on initial empty state)
// 5. Home: first-open screen and the "How Parlour works" link
// 6. App shell: guide.js loaded and precached, old banner slot gone
// 7. Margin note CSS: no box, no shadow, the old banner styles gone

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('=== Running New-Learner Introduction Test Suite ===\n');

// Mock localStorage for Node test runner
const mockStore = {};
global.localStorage = {
    getItem: (key) => (key in mockStore ? mockStore[key] : null),
    setItem: (key, val) => { mockStore[key] = String(val); },
    removeItem: (key) => { delete mockStore[key]; },
    clear: () => { Object.keys(mockStore).forEach(k => delete mockStore[k]); },
    get length() { return Object.keys(mockStore).length; },
    key: (i) => Object.keys(mockStore)[i] || null
};

const Guide = require('../../engine/guide.js');

const EMOJI_REGEX = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

// 1. Seen state
console.log('--- Test 1: Seen State & Persistence ---');
assert.strictEqual(Guide.hasSeen('lesson-listen'), false);
Guide.markSeen('lesson-listen');
assert.strictEqual(Guide.hasSeen('lesson-listen'), true);
assert.strictEqual(mockStore['parlour_guide_seen_lesson-listen'], '1');
Guide.markVisited('review');
assert.strictEqual(Guide.visits('review'), 1);
Guide.resetAll();
assert.strictEqual(Guide.hasSeen('lesson-listen'), false, 'resetAll clears seen notes');
assert.strictEqual(Guide.visits('review'), 0, 'resetAll clears visit counts');
console.log('[PASS] Seen state and visit counts persist and reset.');

// 2. Zero emoji
console.log('\n--- Test 2: Zero Emoji Validation ---');
const guideCode = fs.readFileSync(path.join(__dirname, '../../engine/guide.js'), 'utf8');
assert(!EMOJI_REGEX.test(guideCode), 'guide.js must not contain any emoji characters');
console.log('[PASS] No emoji in guide copy.');

// 3. Invitations
console.log('\n--- Test 3: End-of-Lesson Invitations ---');
Guide.resetAll();
const ctx = (over) => Object.assign({ firstTime: true, newWords: 0, unitCompleted: false, unitsDone: 0 }, over);

let inv = Guide.invitation(ctx({ newWords: 12 }));
assert(inv && inv.id === 'invite-decks', 'first lesson with new words invites to Decks');
assert.strictEqual(inv.text, '12 new words are in your deck, ready for a short review.');
assert.strictEqual(inv.nextLesson, true, 'the Decks invitation also offers the next lesson');
assert.strictEqual(Guide.invitation(ctx({ newWords: 0 })), null, 'no new words, no Decks invitation');

// Skipped once: comes back once more, then stops.
inv = Guide.invitation(ctx({ newWords: 3 }));
assert(inv && inv.id === 'invite-decks', 'a skipped invitation comes back once');
assert.strictEqual(Guide.invitation(ctx({ newWords: 3 })), null, 'and then stops');

// Library after Unit 1, unless the learner already found it.
inv = Guide.invitation(ctx({ unitCompleted: true, unitsDone: 1 }));
assert(inv && inv.id === 'invite-library' && inv.tab === 'reader', 'Unit 1 end invites to the Library');
Guide.acceptInvitation(inv.id);
assert.strictEqual(Guide.invitation(ctx({ unitCompleted: true, unitsDone: 1 })), null, 'accepted invitations are not repeated');

Guide.markVisited('drills');
assert.strictEqual(Guide.invitation(ctx({ unitCompleted: true, unitsDone: 2 })), null,
    'no Workshop invitation once the learner has found the Workshop');

Guide.resetAll();
assert.strictEqual(Guide.invitation(ctx({ unitCompleted: false, unitsDone: 3 })), null,
    'unit invitations only appear at the end of a unit');
console.log('[PASS] Invitation order, skipping and repetition verified.');

// 4. Deferred Sync Prompt Logic
console.log('\n--- Test 4: Deferred Sync Prompt Verification ---');
const syncCode = fs.readFileSync(path.join(__dirname, '../../engine/sync.js'), 'utf8');
assert(syncCode.includes('completedCount === 0 && xp === 0'), 'sync.js must check for completedCount and xp before prompting');
assert(syncCode.includes('// Defer until the learner has actual progress to protect'), 'sync.js must contain explanation comment');
console.log('[PASS] Sync prompt deferral verified.');

// 5. Home
console.log('\n--- Test 5: Home First-Open Screen ---');
const homeCode = fs.readFileSync(path.join(__dirname, '../../engine/home.js'), 'utf8');
assert(homeCode.includes('What would you like to learn?'), 'first-open screen asks for the language');
assert(homeCode.includes('Which Spanish?'), 'first-open screen asks which Spanish');
assert(homeCode.includes('Start from the beginning') && homeCode.includes('Find my level'), 'two starting points');
assert(homeCode.includes('data-open-guide-modal'), 'Home keeps the How Parlour works link');
assert(homeCode.includes('Guide.openOverviewModal()'), 'home.js must call Guide.openOverviewModal()');
assert(!homeCode.includes('hm-onboarding'), 'the old welcome card is gone');
assert(!EMOJI_REGEX.test(homeCode), 'home.js must not contain any emoji characters');
console.log('[PASS] First-open screen and How Parlour works link verified.');

// 6. App shell
console.log('\n--- Test 6: App Shell & Navigation Integration ---');
const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(indexHtml.includes('engine/guide.js'), 'index.html must load engine/guide.js');
assert(indexHtml.includes('nav-guide-btn'), 'index.html nav-footer must have nav-guide-btn');
assert(!indexHtml.includes('lesson-guide-slot'), 'the old lesson banner slot is gone');

const swCode = fs.readFileSync(path.join(__dirname, '../../sw.js'), 'utf8');
assert(swCode.includes('engine/guide.js'), 'sw.js must precache engine/guide.js');
console.log('[PASS] App shell and service worker integration verified.');

// 7. Margin note CSS
console.log('\n--- Test 7: Margin Note CSS ---');
const compCss = fs.readFileSync(path.join(__dirname, '../../styles/components.css'), 'utf8').replace(/\r\n/g, '\n');
const noteRule = (compCss.match(/\.pl-note \{[^}]*\}/) || [''])[0];
assert(noteRule, 'components.css defines .pl-note');
assert(noteRule.includes('border-left'), 'the note has its accent rule');
assert(!/box-shadow/.test(noteRule), 'the note has no shadow (design principles)');
assert(/\.pl-note-text \{[^}]*font-style: italic/.test(compCss), 'the note text is italic');
assert(!compCss.includes('pl-guide-banner'), 'the old banner styles are gone');
console.log('[PASS] Margin note CSS verified.');

console.log('\n=== All New-Learner Introduction Tests Passed! ===\n');
