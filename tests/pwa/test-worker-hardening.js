// ==========================================================
// Unit Tests: Cloudflare Worker Hardening & Abuse Guardrails
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}`);
}

const rootDir = path.resolve(__dirname, '../../');

function loadWorker(relPath, extraGlobals = {}) {
    const absPath = path.join(rootDir, relPath);
    const raw = fs.readFileSync(absPath, 'utf8');
    assertZeroEmojis(raw, relPath);
    const cjs = raw.replace(/export\s+default\s+/, 'module.exports = ');
    const m = { exports: {} };
    const keys = ['module', 'exports', 'Response', 'URL', 'TextEncoder', 'TextDecoder', 'btoa', 'atob', 'crypto', ...Object.keys(extraGlobals)];
    const vals = [m, m.exports, global.Response, global.URL, global.TextEncoder, global.TextDecoder, global.btoa, global.atob, global.crypto, ...Object.values(extraGlobals)];
    new Function(...keys, cjs)(...vals);
    return m.exports;
}

function makeReq(method, url, { origin = 'https://parlour.me.uk', body = null, headers = {} } = {}) {
    const h = Object.assign({}, headers);
    if (origin !== null) h.origin = origin;
    return {
        method,
        url,
        headers: {
            get: (name) => h[name.toLowerCase()] || h[name] || null
        },
        json: async () => {
            if (body === 'BAD_JSON') throw new Error('bad json');
            return body;
        }
    };
}

function makeMockR2() {
    const store = new Map();
    return {
        store,
        get: async (key) => {
            if (!store.has(key)) return null;
            const val = store.get(key);
            return {
                text: async () => (typeof val === 'string' ? val : Buffer.from(val).toString('utf8')),
                arrayBuffer: async () => (val instanceof Uint8Array ? val.buffer.slice(val.byteOffset, val.byteOffset + val.byteLength) : new Uint8Array(Buffer.from(String(val))).buffer)
            };
        },
        put: async (key, val) => {
            store.set(key, val);
        }
    };
}

(async function run() {
    console.log('--- 1. TTS Worker Hardening ---');
    let googleTtsCalls = 0;
    const mockTtsFetch = async () => {
        googleTtsCalls++;
        const audio = Buffer.alloc(1500, 7).toString('base64');
        return {
            ok: true,
            status: 200,
            json: async () => ({ audioContent: audio }),
            text: async () => ''
        };
    };
    const ttsWorker = loadWorker('cloudflare-worker/tts-worker.js', { fetch: mockTtsFetch });
    const ttsR2 = makeMockR2();
    const ttsEnv = {
        GOOGLE_TTS_API_KEY: 'test-key',
        TTS_CACHE: ttsR2,
        TTS_DAILY_CHAR_CAP: '20'
    };

    const ttsHealth = await ttsWorker.fetch(makeReq('GET', 'https://tts.test/health', { origin: null }), ttsEnv);
    assert.strictEqual(ttsHealth.status, 200);
    const ttsHealthJson = await ttsHealth.json();
    assert.strictEqual(ttsHealthJson.service, 'parlour-google-tts-proxy');
    assert.strictEqual(ttsHealthJson.dailyCharCap, 20);

    const ttsBadOrigin = await ttsWorker.fetch(makeReq('POST', 'https://tts.test/synthesize', {
        origin: 'https://evil.example',
        body: { text: 'Hola' }
    }), ttsEnv);
    assert.strictEqual(ttsBadOrigin.status, 403);
    assert.strictEqual(ttsBadOrigin.headers.get('Access-Control-Allow-Origin'), 'https://gergkar-gif.github.io');

    const ttsTooLong = await ttsWorker.fetch(makeReq('POST', 'https://tts.test/synthesize', {
        body: { text: 'a'.repeat(3001) }
    }), ttsEnv);
    assert.strictEqual(ttsTooLong.status, 400);
    assert.strictEqual((await ttsTooLong.json()).code, 'TEXT_TOO_LONG');

    const ttsHit1 = await ttsWorker.fetch(makeReq('POST', 'https://tts.test/synthesize', {
        body: { text: 'Hola mundo.', lang: 'es' }
    }), ttsEnv);
    assert.strictEqual(ttsHit1.status, 200);
    assert.strictEqual(googleTtsCalls, 1);

    const ttsCapBlocked = await ttsWorker.fetch(makeReq('POST', 'https://tts.test/synthesize', {
        body: { text: 'Buenos dias a todos.', lang: 'es' }
    }), ttsEnv);
    assert.strictEqual(ttsCapBlocked.status, 429);
    assert.strictEqual((await ttsCapBlocked.json()).code, 'DAILY_CAP');
    assert.strictEqual(googleTtsCalls, 1);

    const ttsCachedHit = await ttsWorker.fetch(makeReq('POST', 'https://tts.test/synthesize', {
        body: { text: 'Hola mundo.', lang: 'es' }
    }), ttsEnv);
    assert.strictEqual(ttsCachedHit.status, 200);
    assert.strictEqual((await ttsCachedHit.json()).cached, true);
    assert.strictEqual(googleTtsCalls, 1);
    console.log('[PASS] TTS worker origin, length, and R2 daily cap verified.');

    console.log('--- 2. Grader Worker Hardening ---');
    const graderAiCalls = [];
    const graderEnv = {
        AI: {
            run: async (model, input) => {
                graderAiCalls.push({ model, input });
                return { response: '{"overallScore":80}' };
            }
        }
    };
    const graderWorker = loadWorker('cloudflare-worker/grader-worker.js');

    const graderHealth = await graderWorker.fetch(makeReq('GET', 'https://grader.test/health', { origin: null }), graderEnv);
    assert.strictEqual(graderHealth.status, 200);
    const graderHealthJson = await graderHealth.json();
    assert.strictEqual(graderHealthJson.service, 'parlour-grader');
    assert.strictEqual(graderHealthJson.workersAiAvailable, true);

    const graderBadOrigin = await graderWorker.fetch(makeReq('POST', 'https://grader.test/grade', {
        origin: 'https://evil.example',
        body: { prompt: 'Test' }
    }), graderEnv);
    assert.strictEqual(graderBadOrigin.status, 403);

    const graderTooBig = await graderWorker.fetch(makeReq('POST', 'https://grader.test/grade', {
        body: { prompt: 'x'.repeat(16001) }
    }), graderEnv);
    assert.strictEqual(graderTooBig.status, 413);

    const graderModelTest = await graderWorker.fetch(makeReq('POST', 'https://grader.test/grade', {
        body: { model: 'evil/arbitrary-model', prompt: 'Hola' }
    }), graderEnv);
    assert.strictEqual(graderModelTest.status, 200);
    assert.strictEqual(graderAiCalls.length, 1);
    assert.notStrictEqual(graderAiCalls[0].model, 'evil/arbitrary-model');
    console.log('[PASS] Grader worker health, origin, prompt limit, and model allowlist verified.');

    console.log('--- 3. Bug Report Worker Hardening ---');
    let ghCalls = 0;
    const bugWorker = loadWorker('cloudflare-worker/bug-report-proxy.js', {
        fetch: async () => {
            ghCalls++;
            return { ok: true, status: 201, text: async () => '' };
        }
    });
    const bugEnv = { GITHUB_TOKEN: 'ghp_test' };

    const bugHealth = await bugWorker.fetch(makeReq('GET', 'https://bug.test/health', { origin: null }), bugEnv);
    assert.strictEqual(bugHealth.status, 200);
    assert.strictEqual((await bugHealth.json()).hasGithubToken, true);

    const bugBadOrigin = await bugWorker.fetch(makeReq('POST', 'https://bug.test/', {
        origin: 'https://evil.example',
        body: { title: 'Test', body: 'Body' }
    }), bugEnv);
    assert.strictEqual(bugBadOrigin.status, 403);

    for (let i = 0; i < 5; i++) {
        const res = await bugWorker.fetch(makeReq('POST', 'https://bug.test/', {
            headers: { 'cf-connecting-ip': '203.0.113.10' },
            body: { title: `Issue ${i}`, body: 'Detail' }
        }), bugEnv);
        assert.strictEqual(res.status, 200);
    }
    const bugRateLimited = await bugWorker.fetch(makeReq('POST', 'https://bug.test/', {
        headers: { 'cf-connecting-ip': '203.0.113.10' },
        body: { title: 'Issue 6', body: 'Detail' }
    }), bugEnv);
    assert.strictEqual(bugRateLimited.status, 429);
    assert.strictEqual(ghCalls, 5);
    console.log('[PASS] Bug report worker health, origin, and rate limit verified.');

    console.log('--- 4. Sync Worker Hardening ---');
    const syncSqlCalls = [];
    const syncWorker = loadWorker('cloudflare-worker/sync-worker.js', { fetch: async () => ({ ok: true, json: async () => ({}) }) });
    const mockDb = {
        dailyLinksCount: 90,
        prepare: (sql) => ({
            run: async () => {
                syncSqlCalls.push({ sql, args: [] });
                return { meta: { changes: 1 } };
            },
            bind: (...args) => ({
                first: async () => {
                    syncSqlCalls.push({ sql, args });
                    if (sql.includes('FROM magic_links')) return { n: mockDb.dailyLinksCount };
                    if (sql.includes('FROM users WHERE id = ?')) return { id: 'u1', email: 'a@example.com' };
                    return { n: 0 };
                },
                run: async () => {
                    syncSqlCalls.push({ sql, args });
                    return { meta: { changes: 1 } };
                }
            })
        })
    };
    const syncEnv = {
        DB: mockDb,
        JWT_SECRET: 'super-secret-jwt-key-123456',
        RESEND_API_KEY: 're_test',
        GOOGLE_CLIENT_ID: '',
        TURNSTILE_SECRET_KEY: 'ts_secret',
        MAX_LINKS_PER_DAY: '90'
    };

    const syncHealth = await syncWorker.fetch(makeReq('GET', 'https://sync.test/health', { origin: null }), syncEnv);
    assert.strictEqual(syncHealth.status, 200);
    const syncHealthJson = await syncHealth.json();
    assert.strictEqual(syncHealthJson.service, 'parlour-sync');
    assert.strictEqual(syncHealthJson.turnstileEnabled, true);
    assert.strictEqual(syncHealthJson.hasGoogleClientId, false);

    const syncDailyCap = await syncWorker.fetch(makeReq('POST', 'https://sync.test/auth/request-link', {
        body: { email: 'user@example.com', turnstileToken: 'ok' }
    }), Object.assign({}, syncEnv, { TURNSTILE_SECRET_KEY: '' }));
    assert.strictEqual(syncDailyCap.status, 429);

    const syncNoGoogle = await syncWorker.fetch(makeReq('POST', 'https://sync.test/auth/google', {
        body: { credential: 'fake-jwt' }
    }), syncEnv);
    assert.strictEqual(syncNoGoogle.status, 503);

    // Mint a valid session token via web crypto for state size check
    const header = Buffer.from(JSON.stringify({ alg: 'HS256', typ: 'JWT' })).toString('base64url');
    const payloadB64 = Buffer.from(JSON.stringify({ sub: 'u1', email: 'a@example.com', exp: Date.now() + 60000 })).toString('base64url');
    const nodeCrypto = require('crypto');
    const sig = nodeCrypto.createHmac('sha256', syncEnv.JWT_SECRET).update(`${header}.${payloadB64}`).digest('base64url');
    const token = `${header}.${payloadB64}.${sig}`;

    const syncHugeState = await syncWorker.fetch(makeReq('POST', 'https://sync.test/sync/state', {
        headers: { authorization: `Bearer ${token}` },
        body: { state: { blob: 'x'.repeat(1024 * 1024 + 50) } }
    }), syncEnv);
    assert.strictEqual(syncHugeState.status, 413);

    const syncDeleteUnauth = await syncWorker.fetch(makeReq('POST', 'https://sync.test/auth/delete'), syncEnv);
    assert.strictEqual(syncDeleteUnauth.status, 401);

    syncSqlCalls.length = 0;
    const syncDeleteAuth = await syncWorker.fetch(makeReq('POST', 'https://sync.test/auth/delete', {
        headers: { authorization: `Bearer ${token}` }
    }), syncEnv);
    assert.strictEqual(syncDeleteAuth.status, 200);
    const syncDeleteBody = await syncDeleteAuth.json();
    assert.strictEqual(syncDeleteBody.ok, true);
    assert.strictEqual(syncDeleteBody.deleted, true);
    assert(syncSqlCalls.some(c => c.sql.includes('DELETE FROM user_books WHERE user_id = ?') && c.args[0] === 'u1'));
    assert(syncSqlCalls.some(c => c.sql.includes('DELETE FROM magic_links WHERE email = ?') && c.args[0] === 'a@example.com'));
    assert(syncSqlCalls.some(c => c.sql.includes('DELETE FROM users WHERE id = ?') && c.args[0] === 'u1'));
    console.log('[PASS] Sync worker health, daily email cap, Google fail-closed, 1 MB state cap, and account deletion verified.');

    console.log('\nALL WORKER HARDENING TESTS PASSED');
})().catch((err) => {
    console.error('FAILED:', err);
    process.exit(1);
});
