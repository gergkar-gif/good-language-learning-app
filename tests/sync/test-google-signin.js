// ==========================================================
// Unit Tests: Google Sign-In Setup & Multi-Device Auth
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

function assertZeroEmojis(str, contextName) {
    // Exclude standard typographical symbols like checkmark while catching real emoji ranges
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}: ${str}`);
}

const rootDir = path.resolve(__dirname, '../../');

console.log('--- Test 1: Zero-Emoji Compliance Across All Auth Files ---');
const filesToCheck = [
    'cloudflare-worker/sync-worker.js',
    'engine/sync.js',
    'engine/journey.js',
    'styles/components.css',
    'GOOGLE_SIGNIN_SETUP.md',
    'CLOUD_SYNC_SETUP.md',
    'ROADMAP.md',
    'ACHIEVED.md'
];

filesToCheck.forEach(relPath => {
    const absPath = path.join(rootDir, relPath);
    assert(fs.existsSync(absPath), `File must exist: ${relPath}`);
    const content = fs.readFileSync(absPath, 'utf8');
    assertZeroEmojis(content, relPath);
});
console.log('[PASS] Zero-emoji policy verified across all auth documentation, worker, and engine files.');

console.log('\n--- Test 2: Worker /auth/google Route Syntax & Structure ---');
const workerPath = path.join(rootDir, 'cloudflare-worker/sync-worker.js');
const workerContent = fs.readFileSync(workerPath, 'utf8');

assert(workerContent.includes("path === '/auth/google'"), 'Worker fetch handler must route /auth/google');
assert(workerContent.includes('handleGoogleAuth'), 'Worker must implement handleGoogleAuth handler');
assert(workerContent.includes('oauth2.googleapis.com/tokeninfo'), 'Worker must verify token with Google tokeninfo endpoint');
assert(workerContent.includes('GOOGLE_CLIENT_ID'), 'Worker must support GOOGLE_CLIENT_ID claim validation');
assert(workerContent.includes('email_verified'), 'Worker must enforce email_verified check');
console.log('[PASS] Worker contains required /auth/google routing and claim verification logic.');

console.log('\n--- Test 3: Worker Google Auth Handler Logic (Simulated Environment) ---');
// Extract handleGoogleAuth function and its dependencies to test in node vm
const crypto = require('crypto');

// Polyfill Web Crypto for node vm testing if needed
const mockWebCrypto = {
    subtle: {
        importKey: async (format, keyData, algorithm, extractable, keyUsages) => {
            return { format, keyData, algorithm, extractable, keyUsages };
        },
        sign: async (algorithm, key, data) => {
            const hmac = crypto.createHmac('sha256', Buffer.from(key.keyData));
            hmac.update(Buffer.from(data));
            return hmac.digest();
        },
        verify: async (algorithm, key, signature, data) => {
            const hmac = crypto.createHmac('sha256', Buffer.from(key.keyData));
            hmac.update(Buffer.from(data));
            const expected = hmac.digest();
            return Buffer.from(signature).equals(expected);
        },
        digest: async (algorithm, data) => {
            const hash = crypto.createHash('sha256');
            hash.update(Buffer.from(data));
            return hash.digest();
        }
    },
    getRandomValues: (typedArray) => {
        return crypto.randomFillSync(typedArray);
    }
};

(async function runWorkerSimulationTests() {
    let mockFetchResponse = null;
    let lastFetchedUrl = null;

    const mockFetch = async (url) => {
        lastFetchedUrl = url;
        return mockFetchResponse;
    };

    // Mock D1 Database
    const usersStore = new Map();
    const mockDB = {
        prepare: (query) => {
            return {
                bind: (...params) => {
                    return {
                        first: async () => {
                            if (query.includes('FROM users WHERE email = ?')) {
                                const email = params[0];
                                return usersStore.get(email) || null;
                            }
                            return null;
                        },
                        run: async () => {
                            if (query.includes('INSERT INTO users')) {
                                const [id, email, date] = [params[0], params[1], params[2]];
                                usersStore.set(email, { id, email, state_json: null, updated_at: null, created_at: date });
                                return { success: true };
                            }
                            return { success: true };
                        }
                    };
                }
            };
        }
    };

    const workerSandbox = {
        crypto: mockWebCrypto,
        TextEncoder: TextEncoder,
        TextDecoder: TextDecoder,
        btoa: (str) => Buffer.from(str, 'binary').toString('base64'),
        atob: (b64) => Buffer.from(b64, 'base64').toString('binary'),
        fetch: mockFetch,
        Response: class Response {
            constructor(body, init = {}) {
                this.body = body;
                this.status = init.status || 200;
                this.headers = init.headers || {};
            }
            async json() {
                return JSON.parse(this.body);
            }
        },
        URL: URL,
        console: console
    };

    // Extract worker code minus export default
    const workerScriptCode = workerContent.replace(/export\s+default\s*\{[\s\S]*\};?\s*$/, '');
    vm.runInNewContext(workerScriptCode, workerSandbox);

    const env = {
        DB: mockDB,
        JWT_SECRET: 'test-secret-key-1234567890-test',
        GOOGLE_CLIENT_ID: 'test-client-id.apps.googleusercontent.com'
    };
    const cors = { 'Access-Control-Allow-Origin': '*' };

    // Scenario A: Missing credential payload
    const reqMissing = {
        json: async () => ({})
    };
    const resMissing = await workerSandbox.handleGoogleAuth(reqMissing, env, cors);
    assert.strictEqual(resMissing.status, 400, 'Missing credential should return HTTP 400');

    // Scenario B: Invalid token returned by Google
    mockFetchResponse = {
        ok: false,
        status: 401,
        json: async () => ({ error_description: 'Invalid Value' })
    };
    const reqInvalid = {
        json: async () => ({ credential: 'bad-token' })
    };
    const resInvalid = await workerSandbox.handleGoogleAuth(reqInvalid, env, cors);
    assert.strictEqual(resInvalid.status, 401, 'Invalid Google token response should return HTTP 401');

    // Scenario C: Audience mismatch
    mockFetchResponse = {
        ok: true,
        status: 200,
        json: async () => ({
            aud: 'wrong-client-id.apps.googleusercontent.com',
            iss: 'https://accounts.google.com',
            email_verified: 'true',
            exp: String(Math.floor(Date.now() / 1000) + 3600),
            email: 'learner@example.com'
        })
    };
    const resAudMismatch = await workerSandbox.handleGoogleAuth(reqInvalid, env, cors);
    assert.strictEqual(resAudMismatch.status, 401, 'Mismatched audience should return HTTP 401');

    // Scenario D: Email not verified
    mockFetchResponse = {
        ok: true,
        status: 200,
        json: async () => ({
            aud: env.GOOGLE_CLIENT_ID,
            iss: 'https://accounts.google.com',
            email_verified: 'false',
            exp: String(Math.floor(Date.now() / 1000) + 3600),
            email: 'unverified@example.com'
        })
    };
    const resUnverified = await workerSandbox.handleGoogleAuth(reqInvalid, env, cors);
    assert.strictEqual(resUnverified.status, 401, 'Unverified email should return HTTP 401');

    // Scenario E: Expired token
    mockFetchResponse = {
        ok: true,
        status: 200,
        json: async () => ({
            aud: env.GOOGLE_CLIENT_ID,
            iss: 'https://accounts.google.com',
            email_verified: 'true',
            exp: String(Math.floor(Date.now() / 1000) - 100),
            email: 'expired@example.com'
        })
    };
    const resExpired = await workerSandbox.handleGoogleAuth(reqInvalid, env, cors);
    assert.strictEqual(resExpired.status, 401, 'Expired token should return HTTP 401');

    // Scenario F: Successful authentication and session issuance
    mockFetchResponse = {
        ok: true,
        status: 200,
        json: async () => ({
            aud: env.GOOGLE_CLIENT_ID,
            iss: 'accounts.google.com',
            email_verified: 'true',
            exp: String(Math.floor(Date.now() / 1000) + 3600),
            email: 'valid.learner@example.com'
        })
    };
    const reqValid = {
        json: async () => ({ credential: 'valid-google-jwt-token' })
    };
    const resValid = await workerSandbox.handleGoogleAuth(reqValid, env, cors);
    assert.strictEqual(resValid.status, 200, 'Valid Google token should return HTTP 200');
    const validBody = await resValid.json();
    assert.strictEqual(validBody.email, 'valid.learner@example.com', 'Result email should match token email');
    assert(validBody.token, 'Result must contain session token');

    // Verify session token can be verified by requireSession / verifySession
    const verifyReq = {
        headers: {
            get: (h) => (h === 'Authorization' ? 'Bearer ' + validBody.token : null)
        }
    };
    const sessionClaims = await workerSandbox.requireSession(verifyReq, env);
    assert(sessionClaims, 'Issued session token must be verifiable by requireSession');
    assert.strictEqual(sessionClaims.email, 'valid.learner@example.com', 'Session claims must contain email');
    assert(usersStore.has('valid.learner@example.com'), 'User should be persisted in D1 database');

    console.log('[PASS] Worker handleGoogleAuth security checks, D1 persistence, and JWT session issuance verified.');
})().then(() => {
    console.log('\n--- Test 4: Engine Sync Module Google Integration ---');
    const syncPath = path.join(rootDir, 'engine/sync.js');
    const syncContent = fs.readFileSync(syncPath, 'utf8');

    assert(syncContent.includes('GOOGLE_CLIENT_ID'), 'engine/sync.js must define GOOGLE_CLIENT_ID');
    assert(syncContent.includes('loginWithGoogle'), 'engine/sync.js must implement loginWithGoogle');
    assert(syncContent.includes('renderGoogleButton'), 'engine/sync.js must implement renderGoogleButton');
    assert(syncContent.includes('promptGoogleOneTap'), 'engine/sync.js must implement promptGoogleOneTap');
    assert(syncContent.includes('isGoogleAuthAvailable'), 'engine/sync.js must implement isGoogleAuthAvailable');
    assert(syncContent.includes('accounts.google.com/gsi/client'), 'engine/sync.js must load Google Identity Services SDK lazily');
    console.log('[PASS] engine/sync.js implements all required Google auth functions.');

    console.log('\n--- Test 5: Engine Journey UI Account Card Wiring ---');
    const journeyPath = path.join(rootDir, 'engine/journey.js');
    const journeyContent = fs.readFileSync(journeyPath, 'utf8');

    assert(journeyContent.includes('isGoogleAuthAvailable'), 'engine/journey.js must check isGoogleAuthAvailable');
    assert(journeyContent.includes('jr-google-signin-btn'), 'engine/journey.js must render jr-google-signin-btn container');
    assert(journeyContent.includes('jr-account-divider'), 'engine/journey.js must render jr-account-divider');
    assert(journeyContent.includes('renderGoogleButton'), 'engine/journey.js must wire renderGoogleButton in render()');
    console.log('[PASS] engine/journey.js Account card properly integrates Google Sign-In container and divider.');

    console.log('\n--- Test 6: CSS Styling Rules Verification ---');
    const cssPath = path.join(rootDir, 'styles/components.css');
    const cssContent = fs.readFileSync(cssPath, 'utf8');

    assert(cssContent.includes('.jr-google-signin-container'), 'components.css must define .jr-google-signin-container');
    assert(cssContent.includes('.jr-account-divider'), 'components.css must define .jr-account-divider');
    console.log('[PASS] styles/components.css contains required styling rules.');

    console.log('\n==========================================================');
    console.log('ALL GOOGLE SIGN-IN SETUP TESTS PASSED [Zero Emojis Enforced]');
    console.log('==========================================================');
}).catch(err => {
    console.error('Test execution failed:', err);
    process.exit(1);
});
