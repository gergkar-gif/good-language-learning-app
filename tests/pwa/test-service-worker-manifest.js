// ==========================================================
// Unit Tests: Service Worker, PWA Manifest & Offline Architecture
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}: ${str}`);
}

const rootDir = path.resolve(__dirname, '../../');

console.log('--- Test 1: PWA Web App Manifest Validation ---');
const manifestPath = path.join(rootDir, 'manifest.webmanifest');
assert(fs.existsSync(manifestPath), 'manifest.webmanifest must exist at workspace root');

const manifestRaw = fs.readFileSync(manifestPath, 'utf8');
assertZeroEmojis(manifestRaw, 'manifest.webmanifest');

let manifest;
try {
    manifest = JSON.parse(manifestRaw);
} catch (e) {
    assert.fail(`manifest.webmanifest is not valid JSON: ${e.message}`);
}

assert(manifest.name && manifest.name.includes('Parlour'), 'Manifest name should include Parlour');
assert.strictEqual(manifest.short_name, 'Parlour', 'Manifest short_name must be Parlour');
assert(manifest.id, 'Manifest id must be defined');
assert.strictEqual(manifest.start_url, './index.html', 'start_url must point to ./index.html');
assert.strictEqual(manifest.display, 'standalone', 'display mode must be standalone');
assert(manifest.theme_color, 'theme_color must be defined');
assert(manifest.background_color, 'background_color must be defined');
assert(Array.isArray(manifest.icons) && manifest.icons.length > 0, 'Icons array must contain at least one icon');

manifest.icons.forEach((icon, idx) => {
    assert(icon.src, `Icon at index ${idx} must have src`);
    assert(icon.purpose !== 'any maskable', `Icon at index ${idx} must not combine "any maskable"`);
    const iconDiskPath = path.join(rootDir, icon.src);
    assert(fs.existsSync(iconDiskPath), `Icon file on disk must exist: ${icon.src}`);
});
assert(manifest.icons.some(i => i.type === 'image/png' && i.sizes === '192x192' && i.purpose === 'any'), 'Manifest must include a 192x192 PNG icon');
assert(manifest.icons.some(i => i.type === 'image/png' && i.sizes === '512x512' && i.purpose === 'any'), 'Manifest must include a 512x512 PNG icon');
assert(manifest.icons.some(i => i.type === 'image/png' && i.sizes === '512x512' && i.purpose === 'maskable'), 'Manifest must include a 512x512 maskable PNG icon');
console.log('[PASS] manifest.webmanifest is fully compliant with PWA specifications.');

console.log('\n--- Test 2: HTML Shell Manifest & Meta Tag Integration ---');
const indexPath = path.join(rootDir, 'index.html');
const indexHtml = fs.readFileSync(indexPath, 'utf8');

assert(indexHtml.includes('<link rel="manifest" href="manifest.webmanifest">'), 'index.html must link to manifest.webmanifest');
assert(indexHtml.includes('<meta name="theme-color"'), 'index.html must specify theme-color meta tag');
assert(indexHtml.includes('<meta name="apple-mobile-web-app-capable" content="yes">'), 'index.html must specify apple-mobile-web-app-capable');
console.log('[PASS] index.html includes all required PWA manifest and mobile capability tags.');

console.log('\n--- Test 3: Service Worker Syntax & Context Execution ---');
const swPath = path.join(rootDir, 'sw.js');
assert(fs.existsSync(swPath), 'sw.js must exist at workspace root');

const swContent = fs.readFileSync(swPath, 'utf8');
assertZeroEmojis(swContent, 'sw.js');

// Mock ServiceWorkerGlobalScope
const mockListeners = {};
const mockSelf = {
    location: { origin: 'https://parlour.local' },
    addEventListener: (event, handler) => {
        mockListeners[event] = handler;
    },
    skipWaiting: () => Promise.resolve(),
    clients: { claim: () => Promise.resolve() }
};

const sandbox = {
    self: mockSelf,
    console: { log: () => {}, warn: () => {}, error: () => {} },
    caches: {
        open: () => Promise.resolve({ addAll: () => Promise.resolve(), put: () => Promise.resolve() }),
        keys: () => Promise.resolve([]),
        delete: () => Promise.resolve(true),
        match: () => Promise.resolve(null)
    },
    fetch: () => Promise.resolve(),
    URL: URL,
    Response: class Response {}
};

// Execute sw.js in sandbox to verify syntax and lifecycle binding
assert.doesNotThrow(() => {
    vm.runInNewContext(swContent, sandbox);
}, 'sw.js must parse and execute without syntax errors');

assert(typeof mockListeners.install === 'function', 'sw.js must register install listener');
assert(typeof mockListeners.activate === 'function', 'sw.js must register activate listener');
assert(typeof mockListeners.fetch === 'function', 'sw.js must register fetch listener');
assert(typeof mockListeners.message === 'function', 'sw.js must register message listener');
console.log('[PASS] sw.js registers install, activate, fetch, and message lifecycle hooks.');

console.log('\n--- Test 4: Precache Asset Integrity Check (All Assets on Disk) ---');
// Extract PRECACHE_ASSETS array from sw.js
const precacheMatch = swContent.match(/const PRECACHE_ASSETS\s*=\s*(\[[^\]]+\])/s);
assert(precacheMatch, 'PRECACHE_ASSETS array must be defined in sw.js');

let precacheAssets;
try {
    precacheAssets = vm.runInNewContext(precacheMatch[1]);
} catch (e) {
    assert.fail(`Could not evaluate PRECACHE_ASSETS: ${e.message}`);
}

assert(Array.isArray(precacheAssets) && precacheAssets.length >= 50, `PRECACHE_ASSETS should contain comprehensive app shell, found ${precacheAssets.length}`);

const missingOnDisk = [];
precacheAssets.forEach(relPath => {
    if (relPath === './') return;
    const absPath = path.join(rootDir, relPath);
    if (!fs.existsSync(absPath)) {
        missingOnDisk.push(relPath);
    }
});

assert.strictEqual(missingOnDisk.length, 0, `Missing precached assets on disk: ${missingOnDisk.join(', ')}`);
console.log(`[PASS] All ${precacheAssets.length} precached app shell and curriculum assets verified on disk.`);

console.log('\n--- Test 5: Service Worker Routing & Offline Behavior ---');
// Verify fetch handler bypasses external sync worker
let fetchHandled = false;
const syncRequest = {
    method: 'POST',
    url: 'https://parlour-sync.gergkar.workers.dev/auth/request-link'
};
mockListeners.fetch({
    request: syncRequest,
    respondWith: () => { fetchHandled = true; }
});
assert.strictEqual(fetchHandled, false, 'Non-GET and external origin requests must bypass service worker');

// Verify navigation request interception
let navResponded = false;
const navRequest = {
    method: 'GET',
    mode: 'navigate',
    url: 'https://parlour.local/learn'
};
mockListeners.fetch({
    request: navRequest,
    respondWith: (promise) => {
        navResponded = true;
        assert(promise, 'respondWith must receive a promise for navigation requests');
    }
});
assert.strictEqual(navResponded, true, 'Navigation requests must be intercepted for offline fallback');

// Verify dynamic content request interception
let contentResponded = false;
const contentRequest = {
    method: 'GET',
    url: 'https://parlour.local/content/es/stories/original/a1/story.a1.01.json'
};
mockListeners.fetch({
    request: contentRequest,
    respondWith: (promise) => {
        contentResponded = true;
        assert(promise, 'respondWith must receive a promise for content requests');
    }
});
assert.strictEqual(contentResponded, true, 'Content JSON requests must be intercepted for dynamic offline caching');
console.log('[PASS] Service worker routing strategies (bypass, navigation fallback, dynamic content cache) verified.');

console.log('\n--- Test 6: Engine Initialization & Offline Status Indicator ---');
const initPath = path.join(rootDir, 'engine/init.js');
const initContent = fs.readFileSync(initPath, 'utf8');

assert(initContent.includes('_initServiceWorker'), 'engine/init.js must define _initServiceWorker');
assert(/navigator\.serviceWorker\.register\(['"]\.\/sw\.js['"]/.test(initContent), 'engine/init.js must register ./sw.js');
assert(initContent.includes('offline-indicator'), 'engine/init.js must manage offline-indicator');
assert(initContent.includes('is-offline'), 'engine/init.js must toggle is-offline class');
console.log('[PASS] Service worker registration and offline status indicator wired into engine/init.js.');

console.log('\n--- Test 7: Play Store TWA, Account Deletion & Credits Prep ---');
assert(fs.existsSync(path.join(rootDir, '.nojekyll')), '.nojekyll must exist at workspace root');
const assetLinksPath = path.join(rootDir, '.well-known/assetlinks.json');
assert(fs.existsSync(assetLinksPath), '.well-known/assetlinks.json must exist');
assert(Array.isArray(JSON.parse(fs.readFileSync(assetLinksPath, 'utf8'))), '.well-known/assetlinks.json must be a JSON array');
const privacyHtml = fs.readFileSync(path.join(rootDir, 'privacy.html'), 'utf8');
assertZeroEmojis(privacyHtml, 'privacy.html');
assert(privacyHtml.includes('id="delete-account"'), 'privacy.html must include #delete-account section');
const creditsPath = path.join(rootDir, 'credits.html');
assert(fs.existsSync(creditsPath), 'credits.html must exist at workspace root');
assertZeroEmojis(fs.readFileSync(creditsPath, 'utf8'), 'credits.html');
console.log('[PASS] .nojekyll, Digital Asset Links placeholder, privacy deletion section, and credits.html verified.');

console.log('\n--- Test 8: Android Hardware Back Navigation Handling ---');
assertZeroEmojis(initContent, 'engine/init.js');
assert(initContent.includes('pushNavState'), 'engine/init.js must define pushNavState');
assert(initContent.includes('popNavState'), 'engine/init.js must define popNavState');
assert(initContent.includes('_handleAppBack'), 'engine/init.js must define _handleAppBack');
assert(initContent.includes('_ignoreNavPops'), 'engine/init.js must track _ignoreNavPops for popstate');

const backCalls = [];
let mockOverlays = [];
let mockActiveTab = 'home';
let mockHiddenIds = new Set(['lesson-screen', 'leveltest', 'study-plan-screen', 'reader-content', 'review-session']);
let mockActiveDriller = null;
let mockStoryId = null;

function makeClassList(id) {
    return {
        contains: (cls) => cls === 'hidden' && mockHiddenIds.has(id),
        add: (cls) => { if (cls === 'hidden') mockHiddenIds.add(id); },
        remove: (cls) => { if (cls === 'hidden') mockHiddenIds.delete(id); },
        toggle: () => {}
    };
}
function makeMockEl(id, extra = {}) {
    return Object.assign({
        id,
        style: {},
        classList: makeClassList(id),
        querySelector: () => null,
        querySelectorAll: () => [],
        remove: () => {}
    }, extra);
}

const initSandbox = {
    window: { addEventListener: () => {} },
    localStorage: { getItem: () => null, setItem: () => {} },
    document: {
        body: { classList: { contains: () => false } },
        addEventListener: () => {},
        getElementById: (id) => {
            if (id === 'word-popup') return null;
            if (id === mockActiveTab || !mockHiddenIds.has(id) || ['lesson-screen', 'leveltest', 'study-plan-screen', 'reader', 'reader-content', 'drills', 'review', 'review-session', 'journey', 'home'].includes(id)) {
                return makeMockEl(id);
            }
            return null;
        },
        querySelectorAll: (sel) => {
            if (sel === '.wp-overlay') return mockOverlays;
            if (sel === '.tab') return ['home', 'reader', 'drills', 'review'].map(id => makeMockEl(id));
            return [];
        },
        querySelector: (sel) => {
            if (sel === '.tab:not(.hidden)') return makeMockEl(mockActiveTab);
            return null;
        }
    },
    Reader: { get currentStoryId() { return mockStoryId; }, closeStory: () => { mockStoryId = null; mockHiddenIds.add('reader-content'); backCalls.push('reader'); } },
    Workshop: { activeDriller: () => mockActiveDriller, close: () => { mockActiveDriller = null; backCalls.push('workshop'); }, render: () => {} },
    endReviewSession: () => { mockHiddenIds.add('review-session'); backCalls.push('review'); },
    showTab: undefined,
    history: { pushState: () => {}, back: () => {}, state: null }
};
vm.runInNewContext(initContent, initSandbox);

// (a) Open .wp-overlay closes first
let modalClosed = false;
mockOverlays = [makeMockEl('m1', { querySelector: () => ({ click: () => { modalClosed = true; } }) })];
assert.strictEqual(initSandbox.window._handleAppBack(), true);
assert.strictEqual(modalClosed, true, 'Open .wp-overlay modal must close first on Back');
mockOverlays = [];

// (b) Open Reader story closes
mockActiveTab = 'reader';
mockHiddenIds.delete('reader');
mockHiddenIds.delete('reader-content');
mockStoryId = 'story-1';
assert.strictEqual(initSandbox.window._handleAppBack(), true);
assert.deepStrictEqual(backCalls.slice(-1), ['reader']);

// (c) Open Workshop driller closes
mockActiveTab = 'drills';
mockHiddenIds.delete('drills');
mockActiveDriller = { id: 'verbs', title: 'Verbs' };
assert.strictEqual(initSandbox.window._handleAppBack(), true);
assert.deepStrictEqual(backCalls.slice(-1), ['workshop']);

// (d) Open Decks review session closes
mockActiveTab = 'review';
mockHiddenIds.delete('review');
mockHiddenIds.delete('review-session');
assert.strictEqual(initSandbox.window._handleAppBack(), true);
assert.deepStrictEqual(backCalls.slice(-1), ['review']);

// (e) Non-Home tab returns to home
mockActiveTab = 'reader';
assert.strictEqual(initSandbox.window._handleAppBack(), true);
assert.strictEqual(mockHiddenIds.has('home'), false, 'Non-Home tab must return to home on Back');

// (f) Home root returns false
mockActiveTab = 'home';
assert.strictEqual(initSandbox.window._handleAppBack(), false, 'Home root must return false on Back');
console.log('[PASS] Android Back navigation priority order verified across overlays, Reader, Workshop, Decks, and tabs.');

console.log('\n==========================================================');
console.log('ALL PWA & OFFLINE TESTS PASSED [Zero Emojis Enforced]');
console.log('==========================================================');
