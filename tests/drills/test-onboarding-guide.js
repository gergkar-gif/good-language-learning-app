// ============================================
// TEST SUITE: NEW-LEARNER INTRODUCTION (engine/guide.js)
// ============================================
// Verifies:
// 1. Seen-state tracking and localStorage persistence
// 2. Zero emoji pictograms in the guide copy
// 3. Dead end-of-lesson invitations removed from Guide
// 4. Deferred sync prompt logic (does not show on initial empty state)
// 5. Home: first-open screen and the "About Parlour" link
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

// 3. Orphaned invitations removed
console.log('\n--- Test 3: Orphaned Invitations Removed ---');
assert.strictEqual(Guide.invitation, undefined, 'dead Guide.invitation removed');
assert.strictEqual(Guide.acceptInvitation, undefined, 'dead Guide.acceptInvitation removed');
console.log('[PASS] Dead end-of-lesson invitation code removed.');

// 4. Deferred Sync Prompt Logic & First-Open Sign-in
console.log('\n--- Test 4: Deferred Sync Prompt & Sign-In Modal Verification ---');
const syncCode = fs.readFileSync(path.join(__dirname, '../../engine/sync.js'), 'utf8');
assert(syncCode.includes('completedCount === 0 && xp === 0'), 'sync.js must check for completedCount and xp before prompting');
assert(syncCode.includes('// Defer until the learner has actual progress to protect'), 'sync.js must contain explanation comment');
assert(syncCode.includes('function openSignInModal()'), 'sync.js must expose openSignInModal() for returning users');
console.log('[PASS] Sync prompt deferral and openSignInModal verified.');

// 5. Home
console.log('\n--- Test 5: Home First-Open Screen & Post-Lesson Orientation ---');
const homeCode = fs.readFileSync(path.join(__dirname, '../../engine/home.js'), 'utf8');
assert(homeCode.includes('What would you like to learn?'), 'first-open screen asks for the language');
assert(homeCode.includes('Which ${_welcomeLangLabel}?'), 'first-open screen asks which variety of the chosen language');
assert(homeCode.includes('Start from the beginning') && homeCode.includes('Find my level'), 'two starting points');
assert(homeCode.includes('data-welcome-signin'), 'first-open screen offers Sign in for returning users');
assert(homeCode.includes("Guide.note('home-desk'"), 'Home shows home-desk orientation note after setup');
assert(homeCode.includes('data-open-guide-modal'), 'Home keeps the How Parlour works link');
assert(homeCode.includes('Guide.openOverviewModal()'), 'home.js must call Guide.openOverviewModal()');
assert(!homeCode.includes('hm-onboarding'), 'the old welcome card is gone');
assert(!EMOJI_REGEX.test(homeCode), 'home.js must not contain any emoji characters');
console.log('[PASS] First-open screen, Sign-in link, home-desk note, and About Parlour verified.');

// 6. App shell
console.log('\n--- Test 6: App Shell & Navigation Integration ---');
const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(indexHtml.includes('engine/guide.js'), 'index.html must load engine/guide.js');
assert(indexHtml.includes('nav-guide-btn'), 'index.html nav-footer must have nav-guide-btn');
assert(!indexHtml.includes('lesson-guide-slot'), 'the old lesson banner slot is gone');

const swCode = fs.readFileSync(path.join(__dirname, '../../sw.js'), 'utf8');
assert(swCode.includes('engine/guide.js'), 'sw.js must precache engine/guide.js');
console.log('[PASS] App shell and service worker integration verified.');

// 7. Margin note CSS (single source of truth)
console.log('\n--- Test 7: Margin Note CSS ---');
const compCss = fs.readFileSync(path.join(__dirname, '../../styles/components.css'), 'utf8').replace(/\r\n/g, '\n');
const workshopCss = fs.readFileSync(path.join(__dirname, '../../styles/workshop.css'), 'utf8').replace(/\r\n/g, '\n');
const noteRule = (compCss.match(/\.pl-note \{[^}]*\}/) || [''])[0];
assert(noteRule, 'components.css defines .pl-note');
assert(noteRule.includes('border-top: 2px solid var(--primary)'), 'the note has its primary top rule');
assert(!/margin-top/.test(noteRule), 'no duplicate margin-top offset');
assert(!/box-shadow/.test(noteRule), 'the note has no shadow (design principles)');
assert(/\.pl-note-text \{[^}]*font: italic/.test(compCss), 'the note text is italic');
assert(!compCss.includes('pl-guide-banner'), 'the old banner styles are gone');
assert(!workshopCss.includes('.pl-note'), 'workshop.css has no conflicting .pl-note overrides');
console.log('[PASS] Margin note CSS verified as single source of truth.');

// 8. Runtime Guide.note() placement, auto-flip, hidden-anchor clear, Escape & rate-limit
console.log('\n--- Test 8: Runtime Guide.note() Placement & Lifecycle ---');
Guide.resetAll();
const docListeners = {};
const winListeners = {};
const bodyChildren = [];
function makeEl(tag) {
    const classes = new Set();
    const el = {
        tagName: tag.toUpperCase(),
        className: '',
        innerHTML: '',
        style: {},
        offsetWidth: 260,
        offsetHeight: 60,
        parentNode: null,
        attributes: {},
        classList: {
            toggle: (c, force) => { if (force) classes.add(c); else classes.delete(c); },
            contains: (c) => classes.has(c)
        },
        setAttribute: (k, v) => { el.attributes[k] = v; }
    };
    return el;
}
global.window = {
    addEventListener: (ev, fn) => { (winListeners[ev] = winListeners[ev] || []).push(fn); },
    removeEventListener: (ev, fn) => { if (winListeners[ev]) winListeners[ev] = winListeners[ev].filter(f => f !== fn); }
};
global.document = {
    documentElement: { clientWidth: 390, clientHeight: 700 },
    body: {
        appendChild: (el) => { el.parentNode = global.document.body; bodyChildren.push(el); return el; },
        removeChild: (el) => { const i = bodyChildren.indexOf(el); if (i >= 0) bodyChildren.splice(i, 1); el.parentNode = null; }
    },
    createElement: makeEl,
    addEventListener: (ev, fn) => { (docListeners[ev] = docListeners[ev] || []).push(fn); },
    removeEventListener: (ev, fn) => { if (docListeners[ev]) docListeners[ev] = docListeners[ev].filter(f => f !== fn); }
};
function makeAnchor(rect, visible = true) {
    return {
        isConnected: true,
        _visible: visible,
        _rect: rect,
        getClientRects() { return this._visible ? [this._rect] : []; },
        getBoundingClientRect() { return this._visible ? this._rect : { top: 0, bottom: 0, left: 0, right: 0, width: 0, height: 0 }; }
    };
}

// 8a. Anchor near bottom on mobile flips above instead of clipping behind bottom nav
const bottomAnchor = makeAnchor({ top: 580, bottom: 620, left: 20, right: 300 });
const flipped = Guide.note('test-bottom', bottomAnchor, 'Flip above.');
assert(flipped, 'note near bottom renders');
assert.strictEqual(flipped.classList.contains('is-above'), true, 'note flips above when near mobile bottom nav');
assert.strictEqual(parseInt(flipped.style.top, 10), 580 - 8 - 60, 'placed 8px above anchor');

// 8b. Escape dismisses and marks seen
(docListeners.keydown || []).slice().forEach(fn => fn({ key: 'Escape' }));
assert.strictEqual(bodyChildren.length, 0, 'Escape removes note from DOM');
assert.strictEqual(Guide.hasSeen('test-bottom'), true, 'Escape marks note seen');

// 8c. Daily quota blocks a second non-lesson note on the same day, but inLesson bypasses it
const topAnchor = makeAnchor({ top: 80, bottom: 120, left: 20, right: 300 });
assert.strictEqual(Guide.note('test-second-today', topAnchor, 'Blocked today.'), null, 'daily cap blocks second non-lesson note');
const inLessonNote = Guide.note('test-in-lesson', topAnchor, 'Allowed in lesson.', { inLesson: true });
assert(inLessonNote, 'inLesson bypasses daily cap');
assert.strictEqual(inLessonNote.classList.contains('is-above'), false, 'placed below when space permits');

// 8d. Hidden anchor (display: none) on scroll auto-clears note instead of snapping to (6px, 8px)
topAnchor._visible = false;
(docListeners.scroll || []).slice().forEach(fn => fn());
assert.strictEqual(bodyChildren.length, 0, 'hidden anchor clears active note on scroll');

// 8e. Off-screen anchor does not hold _active hostage
Guide.resetAll();
const offscreenAnchor = makeAnchor({ top: 900, bottom: 950, left: 20, right: 300 });
assert.strictEqual(Guide.note('test-offscreen', offscreenAnchor, 'Off screen.'), null, 'off-screen anchor returns null');
const visibleAnchor = makeAnchor({ top: 100, bottom: 140, left: 20, right: 300 });
const visibleNote = Guide.note('test-visible', visibleAnchor, 'Visible now.');
assert(visibleNote, 'visible note still shows after off-screen attempt');
Guide.clearNote();
console.log('[PASS] Runtime Guide.note() placement, auto-flip, hidden-anchor clear, Escape, and daily cap verified.');

console.log('\n=== All New-Learner Introduction Tests Passed! ===\n');
