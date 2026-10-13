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
    const fetchCalls = [];

    const mockFetch = async (url, options) => {
        lastFetchCall = { url, options };
        fetchCalls.push(lastFetchCall);
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
        Buffer: global.Buffer,
        Uint8Array: global.Uint8Array,
        require: require,
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
        getLastFetchCall: () => lastFetchCall,
        getFetchCalls: () => fetchCalls
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
})().then(async () => {
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

    // The upload must start synchronously, inside the pagehide handler: a
    // read-then-merge first would never finish before the page is gone.
    const calls = testEnv.getFetchCalls();
    assert.strictEqual(calls.length, 1, 'pagehide must send exactly one request, without reading the cloud first');
    const lastCall = calls[0];
    assert.strictEqual(lastCall.options.method, 'POST', 'pagehide request must be the upload');
    assert.strictEqual(lastCall.options.keepalive, true, 'pagehide save must specify keepalive: true');
    const leaveBody = JSON.parse(lastCall.options.body);
    assert.strictEqual(typeof leaveBody.baseUpdatedAt, 'number', 'leave-save must say which cloud version it is based on');
    console.log('[PASS] Leaving the app/tab starts the upload at once, with keepalive and baseUpdatedAt.');

    console.log('\n--- Test 9: Normal Save Still Reads Before Writing ---');
    const normalEnv = createMockEnvironment({ syncToken: 'test-token' });
    normalEnv.setFetchResponse({
        ok: true,
        json: async () => ({ ok: true, updatedAt: 9999, state: null })
    });
    await normalEnv.Sync.backup();
    const normalCalls = normalEnv.getFetchCalls();
    assert.strictEqual(normalCalls.length, 2, 'a normal save reads the cloud, then uploads');
    assert.notStrictEqual((normalCalls[0].options || {}).method, 'POST', 'first request must be the read');
    assert.strictEqual(normalCalls[1].options.method, 'POST', 'second request must be the upload');
    assert.strictEqual(JSON.parse(normalCalls[1].options.body).baseUpdatedAt, undefined, 'a normal save sends no baseUpdatedAt');
    console.log('[PASS] A normal save reads and merges the cloud copy before uploading.');

    console.log('\n--- Test 10: 401 Unauthorized Session Expiration Recovery ---');
    const authEnv = createMockEnvironment({
        syncToken: 'active-session-token',
        syncEmail: 'learner@example.com'
    });
    authEnv.setFetchResponse({
        ok: false,
        status: 401,
        json: async () => ({ error: 'Not signed in' })
    });

    let threwExpired = false;
    try {
        await authEnv.Sync.status();
    } catch (err) {
        threwExpired = err.message.includes('Session expired');
    }
    assert.strictEqual(threwExpired, true, 'status() on 401 must throw Session expired error');
    assert.strictEqual(authEnv.Sync.isLoggedIn(), false, 'isLoggedIn() must become false after 401');
    assert.strictEqual(authEnv.sandbox.localStorage.getItem('syncToken'), null, 'syncToken must be removed from storage on 401');
    assert.strictEqual(authEnv.sandbox.localStorage.getItem('syncEmail'), 'learner@example.com', 'syncEmail must be retained for re-login');

    // Test client-side JWT timestamp expiry detection
    const expiredPayload = Buffer.from(JSON.stringify({ sub: 'user1', exp: Date.now() - 60000 })).toString('base64');
    const expiredJwt = `header.${expiredPayload}.signature`;
    const jwtEnv = createMockEnvironment({
        syncToken: expiredJwt,
        syncEmail: 'learner@example.com'
    });
    assert.strictEqual(jwtEnv.Sync.isLoggedIn(), false, 'Expired JWT should immediately register as logged out');
    assert.strictEqual(jwtEnv.sandbox.localStorage.getItem('syncToken'), null, 'Expired JWT should be cleared from storage');
    console.log('[PASS] 401 responses and expired tokens gracefully reset session and retain user email.');

    console.log('\n--- Test 11: Deck Reset & Per-Lemma Removal Survive Cloud Sync ---');
    {
        const resetAt = Date.parse('2026-10-12T20:00:00Z');
        const localAfterReset = {
            es: {
                srsDeck: JSON.stringify([
                    { spanish: 'nuevo', reviews: 0, interval: 0, added: '2026-10-12T21:00:00Z' }
                ]),
                knownWords: JSON.stringify([]),
                srsResetLog: JSON.stringify({ resetAt, lemmas: {} })
            }
        };
        const cloudWith300Words = {
            es: {
                srsDeck: JSON.stringify([
                    { spanish: 'antiguo1', reviews: 3, interval: 7, added: '2026-09-01T10:00:00Z', lastReviewed: '2026-10-10T10:00:00Z' },
                    { spanish: 'antiguo2', reviews: 1, interval: 1 } // legacy card with no timestamps
                ]),
                knownWords: JSON.stringify([
                    { spanish: 'conocido1', english: 'known', added: '2026-09-15T10:00:00Z' }
                ])
            }
        };

        const mergedFull = Sync.mergeSnapshots(localAfterReset, cloudWith300Words);
        const mergedCards = JSON.parse(mergedFull.es.srsDeck);
        const mergedKnown = JSON.parse(mergedFull.es.knownWords);
        assert.strictEqual(mergedCards.length, 1, 'Cloud cards predating full reset must not resurrect');
        assert.strictEqual(mergedCards[0].spanish, 'nuevo', 'Cards added after full reset must be preserved');
        assert.strictEqual(mergedKnown.length, 0, 'Cloud knownWords predating full reset must not resurrect');

        // Per-deck / per-lemma reset: only reset lemmas are filtered; other decks remain untouched
        const lemmaResetAt = Date.parse('2026-10-12T20:00:00Z');
        const localPartialReset = {
            es: {
                srsDeck: JSON.stringify([
                    { spanish: 'quedarse', reviews: 2, interval: 3, added: '2026-09-01T00:00:00Z' }
                ]),
                knownWords: JSON.stringify([]),
                srsResetLog: JSON.stringify({ resetAt: 0, lemmas: { borrar: lemmaResetAt } })
            }
        };
        const cloudBeforePartial = {
            es: {
                srsDeck: JSON.stringify([
                    { spanish: 'quedarse', reviews: 2, interval: 3, added: '2026-09-01T00:00:00Z' },
                    { spanish: 'borrar', reviews: 5, interval: 20, added: '2026-09-01T00:00:00Z', lastReviewed: '2026-10-01T00:00:00Z' }
                ]),
                knownWords: JSON.stringify([
                    { spanish: 'borrar', english: 'to erase', added: '2026-09-05T00:00:00Z' }
                ])
            }
        };
        const mergedPartial = Sync.mergeSnapshots(localPartialReset, cloudBeforePartial);
        const partialCards = JSON.parse(mergedPartial.es.srsDeck);
        const partialKnown = JSON.parse(mergedPartial.es.knownWords);
        assert.strictEqual(partialCards.length, 1, 'Per-lemma reset card must not return from cloud');
        assert.strictEqual(partialCards[0].spanish, 'quedarse', 'Untouched deck card must remain');
        assert.strictEqual(partialKnown.length, 0, 'Per-lemma reset knownWord must not return from cloud');
        console.log('[PASS] Full and per-deck resets survive cloud sync merges without resurrecting old words.');
    }

    console.log('\n--- Test 12: My Texts Progress Merge, Deletion Log, & Book Payload Compression ---');
    {
        const cloudMyTexts = [
            {
                id: 'book-shared',
                title: 'Rayuela',
                author: 'Cortazar',
                modified: '2026-10-12T10:00:00Z',
                progress: { chapterIndex: 4, pct: 75, paraIndex: 12, readChapters: [0, 1, 2, 3], at: 5000 }
            },
            {
                id: 'book-deleted-locally',
                title: 'Old Book',
                modified: '2026-10-01T10:00:00Z',
                progress: { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: 1000 }
            }
        ];
        const localMyTexts = [
            {
                id: 'book-shared',
                title: 'Rayuela',
                author: 'Cortazar',
                modified: '2026-10-10T10:00:00Z',
                progress: { chapterIndex: 1, pct: 20, paraIndex: 2, readChapters: [0], at: 2000 }
            },
            {
                id: 'book-new-local',
                title: 'Ficciones',
                author: 'Borges',
                modified: '2026-10-13T08:00:00Z',
                progress: { chapterIndex: 0, pct: 10, paraIndex: 1, readChapters: [], at: 6000 }
            }
        ];

        const mergedBooksSnap = Sync.mergeSnapshots(
            {
                es: {
                    myTexts: JSON.stringify(localMyTexts),
                    myTextsResetLog: JSON.stringify({ 'book-deleted-locally': Date.parse('2026-10-12T12:00:00Z') })
                }
            },
            {
                es: {
                    myTexts: JSON.stringify(cloudMyTexts)
                }
            }
        );

        const mergedBooks = JSON.parse(mergedBooksSnap.es.myTexts);
        assert.strictEqual(mergedBooks.length, 2, 'Deleted book must be filtered out while active books from both devices remain');
        const rayuela = mergedBooks.find(b => b.id === 'book-shared');
        assert(rayuela, 'Shared book must exist');
        assert.strictEqual(rayuela.progress.chapterIndex, 4, 'Newer cloud reading chapterIndex must win over older local position');
        assert.strictEqual(rayuela.progress.pct, 75, 'Newer cloud reading percentage must win');
        assert.deepStrictEqual(rayuela.progress.readChapters, [0, 1, 2, 3], 'Completed chapters must union across devices');

        // Verify saveBook / loadBook compressed payload round-trip
        const bookEnv = createMockEnvironment({ syncToken: 'test-token' });
        let uploadedBody = null;
        bookEnv.setFetchResponse({
            ok: true,
            status: 200,
            json: async () => ({ ok: true, updatedAt: 12345 })
        });
        const samplePayload = {
            chapters: [
                { index: 0, title: 'Capitulo 1', paragraphs: ['En un lugar de la Mancha.', 'Segunda frase del capitulo.'], wordCount: 11, estimatedMinutes: 1 }
            ],
            lemmas: [{ lemma: 'lugar', translation: 'place', pos: 'noun' }]
        };
        const savedOk = await bookEnv.Sync.saveBook('es:book:book-shared', samplePayload);
        assert.strictEqual(savedOk, true, 'saveBook should succeed when signed in');
        uploadedBody = JSON.parse(bookEnv.getLastFetchCall().options.body);
        assert.strictEqual(uploadedBody.key, 'es:book:book-shared');
        assert.strictEqual(uploadedBody.payload.encoding, 'deflate-base64', 'Book payload should be deflate-compressed for cloud storage');

        bookEnv.setFetchResponse({
            ok: true,
            status: 200,
            json: async () => ({ payload: uploadedBody.payload, updatedAt: 12345 })
        });
        const loadedPayload = await bookEnv.Sync.loadBook('es:book:book-shared');
        assert(loadedPayload && Array.isArray(loadedPayload.chapters), 'loadBook should decompress book chapters');
        assert.strictEqual(loadedPayload.chapters.length, 1);
        assert.strictEqual(loadedPayload.chapters[0].title, 'Capitulo 1');
        assert.strictEqual(loadedPayload.chapters[0].paragraphs[0], 'En un lugar de la Mancha.');
        console.log('[PASS] My Texts progress merge, deletion log, and deflate book payload sync verified.');
    }

    console.log('\n==========================================================');
    console.log('ALL TWO-WAY SYNC & SAVE-ON-LEAVE TESTS PASSED');
    console.log('==========================================================');
}).catch(err => {
    console.error(err);
    process.exit(1);
});
