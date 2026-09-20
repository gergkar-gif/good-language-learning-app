// ============================================
// TEST SUITE: ONBOARDING, PHILOSOPHY & ENCOUNTER GUIDE
// ============================================
// Verifies:
// 1. Guide module encounter tracking and localStorage persistence
// 2. Zero emoji pictograms across all guide texts, modal copy, and philosophy
// 3. Accessibility attributes (role="status", aria-label on dismiss)
// 4. Deferred sync prompt logic (does not show on initial empty state)
// 5. Home onboarding card markup (philosophy, language switcher, guide button)

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('=== Running Onboarding & Guide Test Suite ===\n');

// Mock localStorage for Node test runner
const mockStore = {};
global.localStorage = {
    getItem: (key) => mockStore[key] || null,
    setItem: (key, val) => { mockStore[key] = String(val); },
    removeItem: (key) => { delete mockStore[key]; },
    clear: () => { Object.keys(mockStore).forEach(k => delete mockStore[k]); },
    get length() { return Object.keys(mockStore).length; },
    key: (i) => Object.keys(mockStore)[i] || null
};

const Guide = require('../../engine/guide.js');

// Helper to detect emojis (constructivist design principle)
const EMOJI_REGEX = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

// 1. Test Guide tracking & state
console.log('--- Test 1: Guide State & Persistence ---');
assert.strictEqual(Guide.hasSeen('lesson'), false, 'Initial state of lesson guide should be false');
Guide.markSeen('lesson');
assert.strictEqual(Guide.hasSeen('lesson'), true, 'Guide.hasSeen(lesson) should be true after markSeen');
assert.strictEqual(mockStore['parlour_guide_seen_lesson'], '1', 'localStorage should store parlour_guide_seen_lesson = 1');

Guide.markSeen('reader');
assert.strictEqual(Guide.hasSeen('reader'), true, 'Guide.hasSeen(reader) should be true');

Guide.resetAll();
assert.strictEqual(Guide.hasSeen('lesson'), false, 'resetAll should clear seen guides');
assert.strictEqual(Guide.hasSeen('reader'), false, 'resetAll should clear seen guides');
console.log('[PASS] Guide state persistence verified.');

// 2. Zero Emoji Check across all TIPS
console.log('\n--- Test 2: Zero Emoji Validation ---');
Object.keys(Guide.TIPS).forEach(key => {
    const tip = Guide.TIPS[key];
    assert(!EMOJI_REGEX.test(tip.title), `Tip ${key} title contains emoji: ${tip.title}`);
    assert(!EMOJI_REGEX.test(tip.text), `Tip ${key} text contains emoji: ${tip.text}`);
});

const guideCode = fs.readFileSync(path.join(__dirname, '../../engine/guide.js'), 'utf8');
assert(!EMOJI_REGEX.test(guideCode), 'guide.js must not contain any emoji characters');
console.log('[PASS] Zero emojis confirmed across all guide copy.');

// 3. Accessibility & Banner Markup
console.log('\n--- Test 3: Accessibility & Markup Structure ---');
const bannerHtml = Guide.renderBannerHtml('lesson');
assert(bannerHtml.includes('role="status"'), 'Banner must have role="status"');
assert(bannerHtml.includes('aria-label="Dismiss tip"'), 'Dismiss button must have aria-label');
assert(bannerHtml.includes('data-guide-dismiss="lesson"'), 'Dismiss button must specify data-guide-dismiss');
assert(bannerHtml.includes('pl-guide-banner-icon'), 'Banner must render icon container');
assert(bannerHtml.includes('<svg'), 'Banner must contain inline SVG icon');
console.log('[PASS] Banner accessibility and markup structure verified.');

// 4. Deferred Sync Prompt Logic
console.log('\n--- Test 4: Deferred Sync Prompt Verification ---');
const syncCode = fs.readFileSync(path.join(__dirname, '../../engine/sync.js'), 'utf8');
assert(syncCode.includes('completedCount === 0 && xp === 0'), 'sync.js must check for completedCount and xp before prompting');
assert(syncCode.includes('// Defer until the learner has actual progress to protect'), 'sync.js must contain explanation comment');
console.log('[PASS] Sync prompt deferral verified.');

// 5. Home Onboarding Card Markup
console.log('\n--- Test 5: Home Onboarding Card Markup ---');
const homeCode = fs.readFileSync(path.join(__dirname, '../../engine/home.js'), 'utf8');
assert(homeCode.includes('hm-onboarding-blurb'), 'home.js must render hm-onboarding-blurb');
assert(homeCode.includes('hm-onboarding-btn-guide'), 'home.js must render How Parlour Works button');
assert(homeCode.includes('data-open-guide-modal'), 'home.js must wire data-open-guide-modal');
assert(homeCode.includes('Guide.openOverviewModal()'), 'home.js must call Guide.openOverviewModal()');
assert(!EMOJI_REGEX.test(homeCode), 'home.js must not contain any emoji characters');
console.log('[PASS] Home onboarding card markup and event wiring verified.');

// 6. Navigation Footer and Shell Integration
console.log('\n--- Test 6: App Shell & Navigation Integration ---');
const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(indexHtml.includes('engine/guide.js'), 'index.html must load engine/guide.js');
assert(indexHtml.includes('nav-guide-btn'), 'index.html nav-footer must have nav-guide-btn');
assert(indexHtml.includes('lesson-guide-slot'), 'index.html must include lesson-guide-slot');

const swCode = fs.readFileSync(path.join(__dirname, '../../sw.js'), 'utf8');
assert(swCode.includes('engine/guide.js'), 'sw.js must precache engine/guide.js');
console.log('[PASS] App shell and service worker integration verified.');

console.log('\n=== All Onboarding & Guide Tests Passed! ===\n');
