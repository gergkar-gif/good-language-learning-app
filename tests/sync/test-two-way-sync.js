// ==========================================================
// Unit Tests: Two-Way Cloud Sync & Multi-Device Resolution
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}: ${str}`);
}

const rootDir = path.resolve(__dirname, '../../');

console.log('--- Test 1: Zero-Emoji Compliance Across All Auth & Sync Files ---');
const filesToCheck = [
    'engine/sync.js',
    'engine/init.js',
    'engine/journey.js',
    'cloudflare-worker/sync-worker.js',
    'tests/sync/test-two-way-sync.js'
];

filesToCheck.forEach(relPath => {
    const absPath = path.join(rootDir, relPath);
    assert(fs.existsSync(absPath), `File must exist: ${relPath}`);
    const content = fs.readFileSync(absPath, 'utf8');
    assertZeroEmojis(content, relPath);
});
console.log('[PASS] Zero-emoji policy verified.');

console.log('\n--- Test 2: In-Memory Sync Sandbox Setup ---');
const syncCode = fs.readFileSync(path.join(rootDir, 'engine/sync.js'), 'utf8');

function createMockEnvironment(initialStorage = {}) {
    const storage = new Map(Object.entries(initialStorage));
    const eventListeners = new Map();

    const mockLocalStorage = {
        getItem: (k) => storage.has(k) ? storage.get(k) : null,
        setItem: (k, v) => storage.set(k, String(v)),
        removeItem: (k) => storage.delete(k),
        clear: () => storage.clear()
    };

    const mockDocument = {
        visibilityState: 'visible',
        addEventListener: (event, handler) => {
            if (!eventListeners.has(event)) eventListeners.set(event, []);
            eventListeners.get(event).push(handler);
        },
        getElementById: () => null,
        head: { appendChild: () => {} },
        body: { appendChild: () => {} }
    };

    const mockWindow = {
        addEventListener: (event, handler) => {
            if (!eventListeners.has(event)) eventListeners.set(event, []);
            eventListeners.get(event).push(handler);
        },
        dispatchEvent: () => {}
    };

    const mockLang = {
        available: () => ['es', 'hu'],
        key: (name) => 'es:' + name
    };

    let lastFetchCall = null;
    let mockFetchResponse = null;

    const mockFetch = async (url, options) => {
        lastFetchCall = { url, options };
        return mockFetchResponse;
    };

    const sandbox = {
        localStorage: mockLocalStorage,
        document: mockDocument,
        window: mockWindow,
        Lang: mockLang,
        fetch: mockFetch,
        setTimeout: global.setTimeout,
        clearTimeout: global.clearTimeout,
        Date: global.Date,
        JSON: global.JSON,
        Math: global.Math,
        Set: global.Set,
        Map: global.Map,
        Array: global.Array,
        Object: global.Object,
        String: global.String,
        Number: global.Number,
        Boolean: global.Boolean,
        console: { warn: () => {}, error: () => {}, log: () => {} }
    };

    vm.createContext(sandbox);
    vm.runInContext(syncCode, sandbox);

    const syncInstance = sandbox.Sync || (sandbox.window && sandbox.window.Sync) || vm.runInContext('Sync', sandbox);

    return {
        Sync: syncInstance,
        sandbox,
        storage,
        eventListeners,
        setFetchResponse: (resp) => { mockFetchResponse = resp; },
        getLastFetchCall: () => lastFetchCall
    };
}

const env = createMockEnvironment();
const Sync = env.Sync;
assert(Sync, 'Sync module must export on window/global');
console.log('[PASS] Sync module loaded in isolated sandbox.');

console.log('\n--- Test 3: Additive Progress Merging ---');
{
    const localSnapshot = {
        es: {
            progress: JSON.stringify({
                'lesson.a1.01.01': { completedAt: '2026-09-20T10:00:00Z' }
            })
        }
    };
    const cloudSnapshot = {
        es: {
            progress: JSON.stringify({
                'lesson.a1.01.02': { completedAt: '2026-09-21T12:00:00Z' }
            })
        }
    };

    const merged = Sync.mergeSnapshots(localSnapshot, cloudSnapshot);
    const mergedProg = JSON.parse(merged.es.progress);
    assert(mergedProg['lesson.a1.01.01'], 'Must retain lesson completed on local device');
    assert(mergedProg['lesson.a1.01.02'], 'Must include lesson completed on cloud/remote device');
    assert.strictEqual(mergedProg['lesson.a1.01.01'].completedAt, '2026-09-20T10:00:00Z');
    assert.strictEqual(mergedProg['lesson.a1.01.02'].completedAt, '2026-09-21T12:00:00Z');
    console.log('[PASS] Progress union merged seamlessly without dropping lessons.');
}

console.log('\n--- Test 4: Known Words Deduplication & Union ---');
{
    const localSnapshot = {
        es: {
            knownWords: JSON.stringify([
                { spanish: 'hola', english: 'hello', added: '2026-09-10T00:00:00Z' }
            ])
        }
    };
    const cloudSnapshot = {
        es: {
            knownWords: JSON.stringify([
                { spanish: 'hola', english: 'hello', added: '2026-09-12T00:00:00Z' },
                { spanish: 'gracias', english: 'thank you', added: '2026-09-21T00:00:00Z' }
            ])
        }
    };

    const merged = Sync.mergeSnapshots(localSnapshot, cloudSnapshot);
    const mergedWords = JSON.parse(merged.es.knownWords);
    assert.strictEqual(mergedWords.length, 2, 'Should combine known words to exactly 2');
    const hola = mergedWords.find(w => w.spanish === 'hola');
    assert(hola, 'Word "hola" must exist');
    assert.strictEqual(hola.added, '2026-09-10T00:00:00Z', 'Must preserve earliest added timestamp');
    assert(mergedWords.some(w => w.spanish === 'gracias'), 'Word "gracias" must exist');
    console.log('[PASS] Known words combined and deduplicated correctly.');
}

console.log('\n--- Test 5: SRS Deck Smart Resolution ---');
{
    const localSnapshot = {
        es: {
            srsDeck: JSON.stringify([
                { spanish: 'perro', reviews: 1, interval: 1 }
            ])
        }
    };
    const cloudSnapshot = {
        es: {
            srsDeck: JSON.stringify([
                { spanish: 'perro', reviews: 4, interval: 14 },
                { spanish: 'gato', reviews: 2, interval: 3 }
            ])
        }
    };

    const merged = Sync.mergeSnapshots(localSnapshot, cloudSnapshot);
    const mergedDeck = JSON.parse(merged.es.srsDeck);
    assert.strictEqual(mergedDeck.length, 2);
    const perro = mergedDeck.find(c => c.spanish === 'perro');
    assert.strictEqual(perro.reviews, 4, 'Must retain more advanced card review count');
    assert.strictEqual(perro.interval, 14, 'Must retain more advanced card interval');
    console.log('[PASS] SRS cards resolved keeping more advanced progress.');
}

console.log('\n--- Test 6: XP & Daily History Deep Merge ---');
{
    const localSnapshot = {
        _global: {
            spanishApp_xp: JSON.stringify({
                xp: 150,
                streak: 3,
                history: {
                    '2026-09-20': { total: 50, lessons: 50 }
                }
            })
        }
    };
    const cloudSnapshot = {
        _global: {
            spanishApp_xp: JSON.stringify({
                xp: 220,
                streak: 5,
                history: {
                    '2026-09-20': { total: 40, lessons: 40 },
                    '2026-09-21': { total: 80, lessons: 80 }
                }
            })
        }
    };

    const merged = Sync.mergeSnapshots(localSnapshot, cloudSnapshot);
    const mergedXP = JSON.parse(merged._global.spanishApp_xp);
    assert.strictEqual(mergedXP.xp, 220, 'Total XP must take maximum');
    assert.strictEqual(mergedXP.streak, 5, 'Streak must take maximum');
    assert.strictEqual(mergedXP.history['2026-09-20'].total, 50, 'Daily history must take max for overlapping days');
    assert.strictEqual(mergedXP.history['2026-09-21'].total, 80, 'Must include unique cloud days');
    console.log('[PASS] XP and daily stats merged without losing points.');
}

console.log('\n--- Test 7: Startup Sync Automatic Pull & Apply ---');
(async function testStartupSync() {
    const testEnv = createMockEnvironment({
        syncToken: 'test-token',
        syncLastSyncedAt: '1000'
    });
    const s = testEnv.Sync;

    const cloudUpdated = 5000;
    testEnv.setFetchResponse({
        ok: true,
        json: async () => ({
            updatedAt: cloudUpdated,
            state: {
                es: {
                    progress: JSON.stringify({
                        'lesson.b1.01.01': { completedAt: '2026-09-21T15:00:00Z' }
                    })
                }
            }
        })
    });

    const updated = await s.syncOnStartup();
    assert.strictEqual(updated, true, 'syncOnStartup must report true when new cloud data is merged');
    assert.strictEqual(testEnv.storage.get('syncLastSyncedAt'), '5000', 'Must update syncLastSyncedAt timestamp');
    const storedProg = JSON.parse(testEnv.storage.get('es:progress'));
    assert(storedProg['lesson.b1.01.01'], 'Remote lesson must be applied to local storage');
    console.log('[PASS] Startup sync automatically detected newer cloud data and updated local storage.');
})().then(() => {
    console.log('\n--- Test 8: Save-on-Leave Lifecycle Hooks ---');
    const testEnv = createMockEnvironment({
        syncToken: 'test-token'
    });
    const s = testEnv.Sync;

    testEnv.setFetchResponse({
        ok: true,
        json: async () => ({ ok: true, updatedAt: 9999 })
    });

    // Mark dirty via scheduleAutoSave
    s.scheduleAutoSave();
    assert.strictEqual(s.isDirty(), true, 'Schedule auto save should mark state dirty');

    // Simulate pagehide event
    const pagehideHandlers = testEnv.eventListeners.get('pagehide') || [];
    assert(pagehideHandlers.length > 0, 'pagehide listener must be registered');

    pagehideHandlers[0]();

    // Verify fetch was invoked with keepalive: true
    const lastCall = testEnv.getLastFetchCall();
    assert(lastCall, 'Fetch must be called on pagehide');
    assert.strictEqual(lastCall.options.keepalive, true, 'pagehide save must specify keepalive: true');
    console.log('[PASS] Leaving the app/tab triggers immediate flush with keepalive: true.');

    console.log('\n==========================================================');
    console.log('ALL TWO-WAY SYNC & SAVE-ON-LEAVE TESTS PASSED');
    console.log('==========================================================');
}).catch(err => {
    console.error(err);
    process.exit(1);
});
