// ==========================================================
// Unit & Integration Tests: Calm Social Layer (Worker + D1)
// ==========================================================
const assert = require('assert');
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { DatabaseSync } = require('node:sqlite');

const rootDir = path.resolve(__dirname, '../../');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}`);
}

// ----------------------------------------------------------
// Test 1: Zero-Emoji Policy Across All Social Files
// ----------------------------------------------------------
console.log('--- Test 1: Zero-Emoji Compliance ---');
[
    'cloudflare-worker/sync-schema.sql',
    'cloudflare-worker/sync-worker.js',
    'engine/social.js',
    'engine/journey.js',
    'engine/sync.js',
    'styles/components.css',
    'privacy.html'
].forEach(relPath => {
    const content = fs.readFileSync(path.join(rootDir, relPath), 'utf8');
    assertZeroEmojis(content, relPath);
});
console.log('[PASS] Zero-emoji policy verified across all social files.');

// ----------------------------------------------------------
// Load Cloudflare Worker in a VM with real SQLite D1 adapter
// ----------------------------------------------------------
function createD1Adapter(sqliteDb) {
    return {
        prepare(sql) {
            let boundArgs = [];
            return {
                bind(...args) {
                    boundArgs = args;
                    return this;
                },
                async first() {
                    const row = sqliteDb.prepare(sql).get(...boundArgs);
                    return row || null;
                },
                async all() {
                    const results = sqliteDb.prepare(sql).all(...boundArgs);
                    return { results };
                },
                async run() {
                    const info = sqliteDb.prepare(sql).run(...boundArgs);
                    return { meta: { changes: info.changes } };
                }
            };
        }
    };
}

function loadWorker() {
    const raw = fs.readFileSync(path.join(rootDir, 'cloudflare-worker/sync-worker.js'), 'utf8');
    const transformed = raw.replace(/export\s+default\s+\{/, 'globalThis.__workerExport = {');

    const sandbox = {
        console,
        Date,
        Math,
        JSON,
        Number,
        String,
        Boolean,
        Array,
        Object,
        Set,
        Map,
        RegExp,
        Error,
        URL,
        URLSearchParams,
        TextEncoder,
        TextDecoder,
        Uint8Array,
        Response,
        Headers,
        Request,
        btoa: str => Buffer.from(str, 'binary').toString('base64'),
        atob: str => Buffer.from(str, 'base64').toString('binary'),
        crypto: crypto.webcrypto,
        fetch: async () => { throw new Error('Unexpected network fetch in unit test'); }
    };
    sandbox.globalThis = sandbox;
    vm.createContext(sandbox);
    vm.runInContext(transformed, sandbox);
    return {
        worker: sandbox.__workerExport,
        signSession: sandbox.signSession
    };
}

async function runTests() {
    const sqlite = new DatabaseSync(':memory:');
    sqlite.exec(fs.readFileSync(path.join(rootDir, 'cloudflare-worker/sync-schema.sql'), 'utf8'));

    const env = {
        DB: createD1Adapter(sqlite),
        JWT_SECRET: 'test-jwt-secret-key-for-social-suite'
    };

    const { worker, signSession } = loadWorker();

    async function seedUser(id, email) {
        sqlite.prepare('INSERT INTO users (id, email, state_json, updated_at, created_at) VALUES (?, ?, NULL, NULL, ?)')
            .run(id, email, Date.now());
        return signSession({ sub: id, email, exp: Date.now() + 86400000 }, env.JWT_SECRET);
    }

    async function call(pathname, method, token, body) {
        const headers = { 'Origin': 'https://parlour.me.uk' };
        if (token) headers['Authorization'] = 'Bearer ' + token;
        if (body !== undefined) headers['Content-Type'] = 'application/json';
        const req = new Request('https://parlour-sync.gergkar.workers.dev' + pathname, {
            method,
            headers,
            body: body !== undefined ? JSON.stringify(body) : undefined
        });
        const res = await worker.fetch(req, env);
        const data = await res.json();
        return { status: res.status, data };
    }

    const tokenA = await seedUser('user-a', 'alice@example.com');
    const tokenB = await seedUser('user-b', 'bob@example.com');
    const tokenC = await seedUser('user-c', 'carol@example.com');

    // ----------------------------------------------------------
    // Test 2: Opt-in Profiles, Validation & No Email Leaks
    // ----------------------------------------------------------
    console.log('--- Test 2: Opt-in Profiles & Friend Codes ---');
    const badName = await call('/social/profile', 'POST', tokenA, { displayName: 'A', socialOptIn: true });
    assert.strictEqual(badName.status, 400, '1-char display name must be rejected');

    const profA = await call('/social/profile', 'POST', tokenA, { displayName: 'Alice', socialOptIn: true, activeCourse: 'es-latam' });
    assert.strictEqual(profA.status, 200);
    assert.strictEqual(profA.data.optedIn, true);
    assert(/^PRL-[A-Z0-9]{5}$/.test(profA.data.profile.friendCode), 'Friend code format PRL-XXXXX');
    assert(!JSON.stringify(profA.data).includes('alice@example.com'), 'Email must never appear in social responses');

    const profB = await call('/social/profile', 'POST', tokenB, { displayName: 'Bob', socialOptIn: true, activeCourse: 'hu' });
    assert.strictEqual(profB.status, 200);
    assert.notStrictEqual(profA.data.profile.friendCode, profB.data.profile.friendCode);

    const profC = await call('/social/profile', 'POST', tokenC, { displayName: 'Carol', socialOptIn: true, activeCourse: 'es-latam' });
    assert.strictEqual(profC.status, 200);
    console.log('[PASS] Profiles created with unique friend codes and zero email leaks.');

    // ----------------------------------------------------------
    // Test 3: Anti-Gaming Server-Side Diff & Daily 120 XP Cap
    // ----------------------------------------------------------
    console.log('--- Test 3: Anti-Gaming Diff Engine & 120 XP Daily Cap ---');
    const today = new Date().toISOString().slice(0, 10);
    const oldDate = new Date(Date.now() - 5 * 86400000).toISOString().slice(0, 10);

    // Baseline sync with existing historical lessons: should NOT credit this week's board
    const stateA0 = {
        'es-latam': {
            progress: JSON.stringify({ 'lesson.a1.01.01': true, 'lesson.a1.01.02': true }),
            readStories: JSON.stringify(['a1-01'])
        },
        _global: {
            spanishApp_xp: JSON.stringify({ total: 350, history: { [today]: { total: 0, review: 0 } } })
        }
    };
    const sync0 = await call('/sync/state', 'POST', tokenA, { state: stateA0 });
    assert.strictEqual(sync0.status, 200);

    let boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 0, 'Baseline sync must not backfill weekly XP');

    // Genuine study: +2 lessons (40) + 1 story (15) + 25 review XP = 80 XP
    const stateA1 = {
        'es-latam': {
            progress: JSON.stringify({
                'lesson.a1.01.01': true, 'lesson.a1.01.02': true,
                'lesson.a1.01.03': true, 'lesson.a1.01.04': true
            }),
            readStories: JSON.stringify(['a1-01', 'a1-02'])
        },
        _global: {
            spanishApp_xp: JSON.stringify({ total: 430, history: { [today]: { total: 80, review: 25 } } })
        }
    };
    assert.strictEqual((await call('/sync/state', 'POST', tokenA, { state: stateA1 })).status, 200);

    boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 80, '2 lessons + 1 story + 25 review = 80 XP');
    assert.strictEqual(boardA.data.entries[0].activeDays, 1);
    assert.strictEqual(boardA.data.entries[0].lessonsDone, 2);
    assert.strictEqual(boardA.data.entries[0].storiesDone, 1);

    // Re-sync identical state: must add 0 XP
    assert.strictEqual((await call('/sync/state', 'POST', tokenA, { state: stateA1 })).status, 200);
    boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 80, 'Duplicate sync must not double-credit XP');

    // DevTools spoofing xpData.total and backdating review XP 5 days ago: must add 0 XP
    const stateSpoof = {
        'es-latam': stateA1['es-latam'],
        _global: {
            spanishApp_xp: JSON.stringify({
                total: 999999,
                history: {
                    [today]: { total: 9999, review: 25 },
                    [oldDate]: { total: 500, review: 500 }
                }
            })
        }
    };
    assert.strictEqual((await call('/sync/state', 'POST', tokenA, { state: stateSpoof })).status, 200);
    boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 80, 'DevTools total inflation and backdating must credit 0 XP');

    // Heavy same-day binge (+5 more lessons = 100 XP + 200 review XP): must clamp at 120 XP/day!
    const stateBinge = {
        'es-latam': {
            progress: JSON.stringify({
                'lesson.a1.01.01': true, 'lesson.a1.01.02': true,
                'lesson.a1.01.03': true, 'lesson.a1.01.04': true,
                'lesson.a1.02.01': true, 'lesson.a1.02.02': true,
                'lesson.a1.02.03': true, 'lesson.a1.02.04': true,
                'lesson.a1.02.05': true
            }),
            readStories: JSON.stringify(['a1-01', 'a1-02'])
        },
        _global: {
            spanishApp_xp: JSON.stringify({
                total: 999999,
                history: { [today]: { total: 9999, review: 225 } }
            })
        }
    };
    assert.strictEqual((await call('/sync/state', 'POST', tokenA, { state: stateBinge })).status, 200);
    boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 120, 'Daily board XP must clamp at 120 XP/day');
    console.log('[PASS] Anti-gaming diff engine, backdate rejection, and 120 XP/day cap verified.');

    // ----------------------------------------------------------
    // Test 4: Friends Flow & Weekly Friends Board
    // ----------------------------------------------------------
    console.log('--- Test 4: Friends Flow & Weekly Board ---');
    const reqAB = await call('/social/friends/request', 'POST', tokenA, { friendCode: profB.data.profile.friendCode });
    assert.strictEqual(reqAB.status, 200);
    assert.strictEqual(reqAB.data.status, 'pending');

    const friendsB = await call('/social/friends', 'GET', tokenB);
    assert.strictEqual(friendsB.data.incoming.length, 1);
    assert.strictEqual(friendsB.data.incoming[0].displayName, 'Alice');

    const accB = await call('/social/friends/respond', 'POST', tokenB, { userId: 'user-a', action: 'accept' });
    assert.strictEqual(accB.status, 200);

    // Give Bob a baseline + 1 lesson (20 XP)
    await call('/sync/state', 'POST', tokenB, { state: { hu: { progress: '{}' }, _global: { spanishApp_xp: '{"total":50,"history":{}}' } } });
    await call('/sync/state', 'POST', tokenB, { state: { hu: { progress: '{"hu.a1.01":true}' }, _global: { spanishApp_xp: '{"total":70,"history":{}}' } } });

    boardA = await call('/social/leaderboard?scope=friends', 'GET', tokenA);
    assert.strictEqual(boardA.data.entries.length, 2, 'Friends board contains Alice and Bob (not Carol)');
    assert.strictEqual(boardA.data.entries[0].displayName, 'Alice');
    assert.strictEqual(boardA.data.entries[0].weeklyXp, 120);
    assert.strictEqual(boardA.data.entries[1].displayName, 'Bob');
    assert.strictEqual(boardA.data.entries[1].weeklyXp, 20);
    console.log('[PASS] Friends invite/accept and Friends-only weekly board verified.');

    // ----------------------------------------------------------
    // Test 5: Friend Quest Auto-Match, Shared Progress & Cheer
    // ----------------------------------------------------------
    console.log('--- Test 5: Friend Quest Auto-Match, Progress & Cheer ---');
    const matchRes = await call('/social/quests/auto-match', 'POST', tokenA, { questType: 'stories' });
    assert.strictEqual(matchRes.status, 200);
    assert.strictEqual(matchRes.data.matched, true);
    assert.strictEqual(matchRes.data.quest.status, 'active');
    assert.strictEqual(matchRes.data.quest.partner.displayName, 'Bob');
    assert.strictEqual(matchRes.data.quest.target, 4);

    // Alice reads 2 stories, Bob reads 2 stories -> completes shared quest (target 4)
    const stateAStories = {
        'es-latam': {
            progress: stateBinge['es-latam'].progress,
            readStories: JSON.stringify(['a1-01', 'a1-02', 'a1-03', 'a1-04'])
        },
        _global: stateBinge._global
    };
    await call('/sync/state', 'POST', tokenA, { state: stateAStories });

    const stateBStories = {
        hu: {
            progress: '{"hu.a1.01":true}',
            readStories: JSON.stringify(['hu-s1', 'hu-s2'])
        },
        _global: { spanishApp_xp: '{"total":100,"history":{}}' }
    };
    await call('/sync/state', 'POST', tokenB, { state: stateBStories });

    const qRes = await call('/social/quests', 'GET', tokenB);
    assert.strictEqual(qRes.data.currentQuest.status, 'completed', 'Quest must complete when combined progress hits target');
    assert.strictEqual(qRes.data.currentQuest.myProgress, 2);
    assert.strictEqual(qRes.data.currentQuest.partnerProgress, 2);

    // Cheer cooldown check
    const cheer1 = await call('/social/quests/cheer', 'POST', tokenA, { questId: qRes.data.currentQuest.id });
    assert.strictEqual(cheer1.status, 200);
    assert.ok(cheer1.data.sentAt);
    const cheer2 = await call('/social/quests/cheer', 'POST', tokenA, { questId: qRes.data.currentQuest.id });
    assert.strictEqual(cheer2.data.alreadySent, true);
    console.log('[PASS] Friend Quest auto-match, collaborative completion, and cheer cooldown verified.');

    // ----------------------------------------------------------
    // Test 6: Account Deletion Cascade Cleanup
    // ----------------------------------------------------------
    console.log('--- Test 6: Account Deletion Cascade ---');
    const delA = await call('/auth/delete', 'POST', tokenA);
    assert.strictEqual(delA.status, 200);

    assert.strictEqual(sqlite.prepare('SELECT COUNT(*) AS n FROM user_profiles WHERE user_id = ?').get('user-a').n, 0);
    assert.strictEqual(sqlite.prepare('SELECT COUNT(*) AS n FROM user_weekly_stats WHERE user_id = ?').get('user-a').n, 0);
    assert.strictEqual(sqlite.prepare('SELECT COUNT(*) AS n FROM friendships WHERE user_a = ? OR user_b = ?').get('user-a', 'user-a').n, 0);
    assert.strictEqual(sqlite.prepare('SELECT COUNT(*) AS n FROM friend_quests WHERE user_a = ? OR user_b = ?').get('user-a', 'user-a').n, 0);

    const boardBAfter = await call('/social/leaderboard?scope=friends', 'GET', tokenB);
    assert.strictEqual(boardBAfter.data.entries.length, 1);
    assert.strictEqual(boardBAfter.data.entries[0].displayName, 'Bob');
    console.log('[PASS] Account deletion cascade verified across all social tables.');

    console.log('\nALL SOCIAL TESTS PASSED!');
}

runTests().catch(err => {
    console.error('TEST FAILED:', err);
    process.exit(1);
});
