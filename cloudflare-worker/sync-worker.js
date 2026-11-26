// ============================================
// CLOUD SYNC WORKER (Cloudflare Worker + D1)
// ============================================
// Backs up a learner's local progress to the cloud and restores it on
// another device. Passwordless: a learner enters their email, gets a
// one-time login link, and that link's token becomes a signed session
// token the client sends back on every sync call. Last-write-wins by
// design — the client decides which direction to overwrite (see
// engine/sync.js), this worker never merges anything itself.
//
// Deploy via the Cloudflare dashboard (Workers & Pages -> Create ->
// paste this in), same as cloudflare-worker/bug-report-proxy.js — see
// docs/SERVICES.md for the full walkthrough, including the D1
// database and the two secrets this needs (JWT_SECRET, RESEND_API_KEY).
// Zero external imports on purpose, same reason bug-report-proxy.js has
// none: the dashboard's paste-and-deploy flow has no bundler.

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131'
];

const TOKEN_TTL_MS = 10 * 60 * 1000;        // magic-link token: 10 minutes
const SESSION_TTL_SECONDS = 365 * 24 * 60 * 60; // session token: 365 days
const MAX_LINKS_PER_HOUR = 3;
const DEFAULT_MAX_LINKS_PER_DAY = 90;
const MAX_STATE_BYTES = 1024 * 1024;
const MAX_BOOKS_PER_USER = 50;
const RESEND_FROM = 'Parlour <noreply@parlour.me.uk>';

function isAllowedOrigin(origin) {
    if (!origin) return false;
    if (ALLOWED_ORIGINS.includes(origin)) return true;
    return /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
}

function corsHeaders(origin) {
    if (!isAllowedOrigin(origin)) return null;
    return {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        'Vary': 'Origin'
    };
}

function json(data, status, cors) {
    return new Response(JSON.stringify(data), {
        status: status || 200,
        headers: Object.assign({ 'Content-Type': 'application/json' }, cors)
    });
}

// ----------------------------------------
// CRYPTO HELPERS (Web Crypto only — no libraries)
// ----------------------------------------

function toBase64Url(bytes) {
    let binary = '';
    bytes.forEach(b => { binary += String.fromCharCode(b); });
    return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function fromBase64Url(str) {
    const padded = str.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((str.length + 3) % 4);
    const binary = atob(padded);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
    return bytes;
}

function randomToken() {
    return toBase64Url(crypto.getRandomValues(new Uint8Array(32))); // 256 bits
}

async function sha256Hex(text) {
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
    return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
}

async function hmacKey(secret) {
    return crypto.subtle.importKey(
        'raw', new TextEncoder().encode(secret),
        { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']
    );
}

// A hand-rolled JWT-shaped session token: header.payload.signature, all
// base64url, HMAC-SHA256 signed. No external library, matching this
// worker's zero-dependency deploy convention.
async function signSession(payload, secret) {
    const header = toBase64Url(new TextEncoder().encode(JSON.stringify({ alg: 'HS256', typ: 'JWT' })));
    const body = toBase64Url(new TextEncoder().encode(JSON.stringify(payload)));
    const key = await hmacKey(secret);
    const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(header + '.' + body));
    return header + '.' + body + '.' + toBase64Url(new Uint8Array(sig));
}

async function verifySession(token, secret) {
    if (!token || typeof token !== 'string') return null;
    const parts = token.split('.');
    if (parts.length !== 3) return null;
    const [header, body, sig] = parts;
    const key = await hmacKey(secret);
    const ok = await crypto.subtle.verify('HMAC', key, fromBase64Url(sig), new TextEncoder().encode(header + '.' + body));
    if (!ok) return null;
    let payload;
    try {
        payload = JSON.parse(new TextDecoder().decode(fromBase64Url(body)));
    } catch (e) {
        return null;
    }
    if (!payload.exp || payload.exp < Date.now()) return null;
    return payload;
}

function requireSession(request, env) {
    const auth = request.headers.get('Authorization') || '';
    const token = auth.startsWith('Bearer ') ? auth.slice(7) : '';
    return verifySession(token, env.JWT_SECRET);
}

// ----------------------------------------
// EMAIL (Resend — Cloudflare's own outbound email sending is paid-plan
// only, so a magic link needs a third-party sender; Resend's free tier
// covers this app's scale and needs no domain verification via its
// onboarding@resend.dev sender)
// ----------------------------------------

async function sendMagicLinkEmail(email, link, env) {
    const res = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + env.RESEND_API_KEY,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            from: RESEND_FROM,
            to: [email],
            subject: 'Your Parlour sign-in link',
            html: '<p>Tap this link to sign in to Parlour:</p>'
                + '<p><a href="' + link + '">' + link + '</a></p>'
                + '<p>This link expires in 10 minutes and can only be used once. '
                + "If you didn't request this, you can ignore this email.</p>"
        })
    });
    if (!res.ok) {
        const errText = await res.text();
        throw new Error('Resend error ' + res.status + ': ' + errText);
    }
}

// ----------------------------------------
// TURNSTILE (bot check ahead of sending a real email — see
// docs/SERVICES.md). Verification is skipped entirely, not just
// permissive, when TURNSTILE_SECRET_KEY isn't set: that's the "not
// configured yet" state, matching engine/sync.js's client-side no-op when
// TURNSTILE_SITE_KEY is empty, so request-link keeps working before the
// widget exists rather than locking everyone out.
// ----------------------------------------

async function verifyTurnstile(token, env) {
    if (!env.TURNSTILE_SECRET_KEY) return true;
    if (!token) return false;

    const res = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `secret=${encodeURIComponent(env.TURNSTILE_SECRET_KEY)}&response=${encodeURIComponent(token)}`
    });
    if (!res.ok) return false;
    const data = await res.json();
    return Boolean(data.success);
}

// ----------------------------------------
// ROUTES
// ----------------------------------------

async function handleRequestLink(request, env, cors) {
    let payload;
    try {
        payload = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }
    const email = typeof payload.email === 'string' ? payload.email.trim().toLowerCase() : '';
    if (!email || !email.includes('@') || email.length > 254) {
        return json({ error: 'Invalid email' }, 400, cors);
    }

    const verified = await verifyTurnstile(payload.turnstileToken, env);
    if (!verified) {
        return json({ error: 'Verification failed — please try again' }, 403, cors);
    }

    // Global daily magic-link cap to protect the Resend free tier (3,000/month).
    const DEFAULT_DAY_CAP = parseInt(env.MAX_LINKS_PER_DAY, 10) || DEFAULT_MAX_LINKS_PER_DAY;
    const dayAgo = Date.now() - 24 * 60 * 60 * 1000;
    const dailyCount = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM magic_links WHERE expires_at > ?'
    ).bind(dayAgo + TOKEN_TTL_MS).first();
    if (dailyCount && dailyCount.n >= DEFAULT_DAY_CAP) {
        return json({ error: 'Daily sign-in email limit reached — try again tomorrow' }, 429, cors);
    }

    // Rate limit: at most MAX_LINKS_PER_HOUR requests per email per hour,
    // checked against D1 directly rather than a separate store.
    // expires_at is issued_at + TOKEN_TTL_MS, so "issued within the last
    // hour" is expires_at > (now - 1hour) + TOKEN_TTL_MS.
    const hourAgo = Date.now() - 60 * 60 * 1000;
    const recentCount = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM magic_links WHERE email = ? AND expires_at > ?'
    ).bind(email, hourAgo + TOKEN_TTL_MS).first();
    if (recentCount && recentCount.n >= MAX_LINKS_PER_HOUR) {
        return json({ error: 'Too many requests — try again later' }, 429, cors);
    }

    const rawToken = randomToken();
    const tokenHash = await sha256Hex(rawToken);
    const expiresAt = Date.now() + TOKEN_TTL_MS;

    await env.DB.prepare(
        'INSERT INTO magic_links (token_hash, email, expires_at, used) VALUES (?, ?, ?, 0)'
    ).bind(tokenHash, email, expiresAt).run();

    const link = 'https://parlour.me.uk/?verify=' + encodeURIComponent(rawToken);

    try {
        await sendMagicLinkEmail(email, link, env);
    } catch (error) {
        // Logged so the real Resend failure reason is visible in the
        // Worker's Logs tab — the client only ever sees the generic
        // message below, never Resend's raw response.
        console.error('sendMagicLinkEmail failed:', error.message);
        return json({ error: 'Could not send email' }, 502, cors);
    }

    return json({ ok: true }, 200, cors);
}

async function handleVerify(request, env, cors) {
    let payload;
    try {
        payload = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }
    const rawToken = typeof payload.token === 'string' ? payload.token : '';
    if (!rawToken) return json({ error: 'Missing token' }, 400, cors);

    const tokenHash = await sha256Hex(rawToken);
    const row = await env.DB.prepare(
        'SELECT * FROM magic_links WHERE token_hash = ?'
    ).bind(tokenHash).first();

    if (!row || row.used || row.expires_at < Date.now()) {
        return json({ error: 'Link is invalid or expired' }, 401, cors);
    }

    await env.DB.prepare('UPDATE magic_links SET used = 1 WHERE token_hash = ?').bind(tokenHash).run();

    let user = await env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(row.email).first();
    if (!user) {
        const id = randomToken();
        await env.DB.prepare(
            'INSERT INTO users (id, email, state_json, updated_at, created_at) VALUES (?, ?, NULL, NULL, ?)'
        ).bind(id, row.email, Date.now()).run();
        user = { id, email: row.email };
    }

    const session = await signSession(
        { sub: user.id, email: row.email, exp: Date.now() + SESSION_TTL_SECONDS * 1000 },
        env.JWT_SECRET
    );

    return json({ token: session, email: row.email }, 200, cors);
}

async function handleGoogleAuth(request, env, cors) {
    let payload;
    try {
        payload = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const credential = typeof payload.credential === 'string' ? payload.credential.trim() : '';
    if (!credential) {
        return json({ error: 'Missing credential' }, 400, cors);
    }

    if (!env.GOOGLE_CLIENT_ID) {
        return json({ error: 'Google Sign-In is not configured' }, 503, cors);
    }

    // Verify Google ID token via Google's tokeninfo endpoint (zero external dependencies)
    let tokenInfo;
    try {
        const verifyRes = await fetch(
            'https://oauth2.googleapis.com/tokeninfo?id_token=' + encodeURIComponent(credential)
        );
        if (!verifyRes.ok) {
            return json({ error: 'Invalid Google token' }, 401, cors);
        }
        tokenInfo = await verifyRes.json();
    } catch (error) {
        console.error('Google token verification failed:', error.message);
        return json({ error: 'Failed to verify token with Google' }, 502, cors);
    }

    // Validate claims
    if (tokenInfo.aud !== env.GOOGLE_CLIENT_ID) {
        return json({ error: 'Invalid Google client ID' }, 401, cors);
    }

    const validIssuers = ['accounts.google.com', 'https://accounts.google.com'];
    if (!validIssuers.includes(tokenInfo.iss)) {
        return json({ error: 'Invalid token issuer' }, 401, cors);
    }

    if (tokenInfo.email_verified !== 'true' && tokenInfo.email_verified !== true) {
        return json({ error: 'Google email is not verified' }, 401, cors);
    }

    const exp = Number(tokenInfo.exp);
    if (isNaN(exp) || exp * 1000 < Date.now()) {
        return json({ error: 'Google token has expired' }, 401, cors);
    }

    const email = typeof tokenInfo.email === 'string' ? tokenInfo.email.trim().toLowerCase() : '';
    if (!email || !email.includes('@') || email.length > 254) {
        return json({ error: 'Invalid email in Google token' }, 400, cors);
    }

    // Upsert or fetch existing user from D1 database
    let user = await env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(email).first();
    if (!user) {
        const id = randomToken();
        await env.DB.prepare(
            'INSERT INTO users (id, email, state_json, updated_at, created_at) VALUES (?, ?, NULL, NULL, ?)'
        ).bind(id, email, Date.now()).run();
        user = { id, email };
    }

    const session = await signSession(
        { sub: user.id, email, exp: Date.now() + SESSION_TTL_SECONDS * 1000 },
        env.JWT_SECRET
    );

    return json({
        token: session,
        email,
        name: tokenInfo.given_name || tokenInfo.name || ''
    }, 200, cors);
}

async function handleGetState(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);

    const user = await env.DB.prepare('SELECT state_json, updated_at FROM users WHERE id = ?').bind(session.sub).first();
    if (!user) return json({ error: 'Not found' }, 404, cors);

    return json({
        state: user.state_json ? JSON.parse(user.state_json) : null,
        updatedAt: user.updated_at
    }, 200, cors);
}

async function handlePostState(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);

    let payload;
    try {
        payload = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }
    if (typeof payload.state !== 'object' || payload.state === null) {
        return json({ error: 'Missing state' }, 400, cors);
    }

    const serialized = JSON.stringify(payload.state);
    if (serialized.length > MAX_STATE_BYTES) {
        return json({ error: 'State payload exceeds cloud storage limit' }, 413, cors);
    }

    const existingRow = await env.DB.prepare('SELECT state_json FROM users WHERE id = ?')
        .bind(session.sub).first();
    const prevState = existingRow && existingRow.state_json ? parseJsonSafe(existingRow.state_json, null) : null;

    const updatedAt = Date.now();
    // A save sent while the page closes can't read the cloud first, so it
    // says which cloud version it was based on. Write only if nobody has
    // saved since; otherwise refuse, and the device merges next session.
    if (typeof payload.baseUpdatedAt === 'number') {
        const result = await env.DB.prepare(
            'UPDATE users SET state_json = ?, updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at <= ?)'
        ).bind(serialized, updatedAt, session.sub, payload.baseUpdatedAt).run();
        if (!result.meta || !result.meta.changes) {
            return json({ error: 'Cloud copy is newer', conflict: true }, 409, cors);
        }
        try {
            await updateSocialStatsFromSync(env, session.sub, prevState, payload.state, updatedAt);
        } catch (err) {
            console.error('updateSocialStatsFromSync failed:', err && err.message ? err.message : err);
        }
        return json({ ok: true, updatedAt }, 200, cors);
    }

    await env.DB.prepare('UPDATE users SET state_json = ?, updated_at = ? WHERE id = ?')
        .bind(serialized, updatedAt, session.sub).run();

    try {
        await updateSocialStatsFromSync(env, session.sub, prevState, payload.state, updatedAt);
    } catch (err) {
        console.error('updateSocialStatsFromSync failed:', err && err.message ? err.message : err);
    }

    return json({ ok: true, updatedAt }, 200, cors);
}

// ----------------------------------------
// BOOK PAYLOAD STORAGE (user_books table)
// ----------------------------------------
// Multi-chapter book bodies (chapters + lemmas) live in their own D1 rows
// so the main /sync/state snapshot stays fast and under the 64 KB keepalive
// limit. Auto-creates the table on first use so upgrading the Worker needs
// no separate D1 Console step.

let _booksTableEnsured = false;

async function ensureBooksTable(env) {
    if (_booksTableEnsured) return;
    await env.DB.prepare(
        'CREATE TABLE IF NOT EXISTS user_books (user_id TEXT NOT NULL, book_key TEXT NOT NULL, payload_json TEXT NOT NULL, updated_at INTEGER NOT NULL, PRIMARY KEY (user_id, book_key))'
    ).run();
    _booksTableEnsured = true;
}

async function handleGetBook(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);

    const url = new URL(request.url);
    const bookKey = (url.searchParams.get('key') || '').trim();
    if (!bookKey || bookKey.length > 160) {
        return json({ error: 'Invalid book key' }, 400, cors);
    }

    await ensureBooksTable(env);
    const row = await env.DB.prepare(
        'SELECT payload_json, updated_at FROM user_books WHERE user_id = ? AND book_key = ?'
    ).bind(session.sub, bookKey).first();

    if (!row) {
        return json({ payload: null, updatedAt: null }, 200, cors);
    }

    let parsed = null;
    try {
        parsed = JSON.parse(row.payload_json);
    } catch (e) {
        parsed = null;
    }

    return json({
        payload: parsed,
        updatedAt: row.updated_at
    }, 200, cors);
}

async function handlePostBook(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const bookKey = (body && typeof body.key === 'string') ? body.key.trim() : '';
    if (!bookKey || bookKey.length > 160) {
        return json({ error: 'Invalid book key' }, 400, cors);
    }

    await ensureBooksTable(env);

    if (body.deleted === true || body.payload === null) {
        await env.DB.prepare(
            'DELETE FROM user_books WHERE user_id = ? AND book_key = ?'
        ).bind(session.sub, bookKey).run();
        return json({ ok: true, deleted: true }, 200, cors);
    }

    if (typeof body.payload !== 'object' || body.payload === null) {
        return json({ error: 'Missing book payload' }, 400, cors);
    }

    const serialized = JSON.stringify(body.payload);
    if (serialized.length > 1800000) {
        return json({ error: 'Book payload exceeds cloud storage limit' }, 413, cors);
    }

    const existingBook = await env.DB.prepare(
        'SELECT 1 AS found FROM user_books WHERE user_id = ? AND book_key = ?'
    ).bind(session.sub, bookKey).first();
    if (!existingBook) {
        const bookCount = await env.DB.prepare(
            'SELECT COUNT(*) AS n FROM user_books WHERE user_id = ?'
        ).bind(session.sub).first();
        if (bookCount && bookCount.n >= MAX_BOOKS_PER_USER) {
            return json({ error: 'Cloud book limit reached' }, 403, cors);
        }
    }

    const updatedAt = Date.now();
    await env.DB.prepare(
        'INSERT INTO user_books (user_id, book_key, payload_json, updated_at) VALUES (?, ?, ?, ?) ON CONFLICT(user_id, book_key) DO UPDATE SET payload_json = excluded.payload_json, updated_at = excluded.updated_at'
    ).bind(session.sub, bookKey, serialized, updatedAt).run();

    return json({ ok: true, updatedAt }, 200, cors);
}

// ----------------------------------------
// SOCIAL LAYER (Profiles, Verified Weekly Stats, Friends, Friend Quests)
// ----------------------------------------
// Strictly opt-in. Weekly leaderboard XP is derived server-side by diffing
// synced state_json snapshots (newly completed lessons, newly read stories,
// and daily-capped review XP within a 48h window) with a 120 XP/day cap so
// steady daily study beats grinding and client-side XP edits have no effect.

const MAX_DAILY_BOARD_XP = 120;
const MAX_DAILY_REVIEW_XP = 60;
const SOCIAL_LESSON_XP = 20;
const SOCIAL_STORY_XP = 15;
const MAX_SYNC_LESSONS_PER_POST = 15;
const MAX_SYNC_STORIES_PER_POST = 15;
const MAX_PENDING_FRIEND_REQUESTS = 20;
const CHEER_COOLDOWN_MS = 20 * 60 * 60 * 1000;
const FRIEND_CODE_ALPHABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';

const QUEST_TYPES = {
    lessons: { type: 'lessons', label: 'Complete lessons together', unit: 'lessons', target: 6 },
    stories: { type: 'stories', label: 'Read stories together', unit: 'stories', target: 4 },
    active_days: { type: 'active_days', label: 'Study days together', unit: 'days', target: 8 },
    xp: { type: 'xp', label: 'Earn XP together', unit: 'XP', target: 350 }
};

let _socialTablesEnsured = false;

async function ensureSocialTables(env) {
    if (_socialTablesEnsured) return;
    await env.DB.prepare(
        'CREATE TABLE IF NOT EXISTS user_profiles (user_id TEXT PRIMARY KEY, display_name TEXT NOT NULL, friend_code TEXT UNIQUE NOT NULL, social_opt_in INTEGER NOT NULL DEFAULT 0, public_board_opt_in INTEGER NOT NULL DEFAULT 0, active_course TEXT NOT NULL DEFAULT \'es-latam\', updated_at INTEGER NOT NULL)'
    ).run();
    await env.DB.prepare(
        'CREATE TABLE IF NOT EXISTS user_weekly_stats (user_id TEXT NOT NULL, week_key TEXT NOT NULL, capped_xp INTEGER NOT NULL DEFAULT 0, active_days_json TEXT NOT NULL DEFAULT \'[]\', daily_xp_json TEXT NOT NULL DEFAULT \'{}\', lessons_done INTEGER NOT NULL DEFAULT 0, stories_done INTEGER NOT NULL DEFAULT 0, rank INTEGER NOT NULL DEFAULT 1, streak_days INTEGER NOT NULL DEFAULT 0, updated_at INTEGER NOT NULL, PRIMARY KEY (user_id, week_key))'
    ).run();
    await env.DB.prepare(
        'CREATE INDEX IF NOT EXISTS idx_weekly_board ON user_weekly_stats (week_key, capped_xp DESC)'
    ).run();
    await env.DB.prepare(
        'CREATE TABLE IF NOT EXISTS friendships (user_a TEXT NOT NULL, user_b TEXT NOT NULL, status TEXT NOT NULL, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL, PRIMARY KEY (user_a, user_b))'
    ).run();
    await env.DB.prepare(
        'CREATE TABLE IF NOT EXISTS friend_quests (id TEXT PRIMARY KEY, week_key TEXT NOT NULL, user_a TEXT NOT NULL, user_b TEXT NOT NULL, quest_type TEXT NOT NULL, target INTEGER NOT NULL, progress_a INTEGER NOT NULL DEFAULT 0, progress_b INTEGER NOT NULL DEFAULT 0, status TEXT NOT NULL DEFAULT \'pending\', cheer_a_at INTEGER, cheer_b_at INTEGER, completed_at INTEGER, created_at INTEGER NOT NULL)'
    ).run();
    _socialTablesEnsured = true;
}

function parseJsonSafe(raw, fallback) {
    if (raw == null) return fallback;
    if (typeof raw === 'object') return raw;
    if (typeof raw !== 'string') return fallback;
    try {
        return JSON.parse(raw);
    } catch (e) {
        return fallback;
    }
}

function utcDateString(ms) {
    return new Date(ms).toISOString().slice(0, 10);
}

function getIsoWeekKey(ms) {
    const d = new Date(ms);
    const utc = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()));
    const dayNum = utc.getUTCDay() || 7;
    utc.setUTCDate(utc.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(utc.getUTCFullYear(), 0, 1));
    const weekNo = Math.ceil((((utc - yearStart) / 86400000) + 1) / 7);
    return utc.getUTCFullYear() + '-W' + String(weekNo).padStart(2, '0');
}

function getPreviousIsoWeekKey(ms) {
    return getIsoWeekKey(ms - 7 * 86400000);
}

function rankForXP(xp) {
    const safeXp = Math.max(0, Number(xp) || 0);
    let rank = 1;
    while (100 * rank * (rank + 1) / 2 <= safeXp) rank++;
    return rank;
}

function generateFriendCode() {
    const bytes = crypto.getRandomValues(new Uint8Array(5));
    let suffix = '';
    for (let i = 0; i < bytes.length; i++) {
        suffix += FRIEND_CODE_ALPHABET[bytes[i] % FRIEND_CODE_ALPHABET.length];
    }
    return 'PRL-' + suffix;
}

function sanitizeDisplayName(raw) {
    if (typeof raw !== 'string') return '';
    // Strip control chars and emoji ranges; keep letters, digits, spaces, basic punctuation
    const cleaned = raw
        .replace(/[\u0000-\u001F\u007F]/g, '')
        .replace(/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{1F1E6}-\u{1F1FF}]/gu, '')
        .replace(/\s+/g, ' ')
        .trim();
    if (cleaned.length < 2 || cleaned.length > 24) return '';
    return cleaned;
}

function sanitizeCourseCode(raw) {
    if (typeof raw !== 'string') return 'es-latam';
    const clean = raw.trim().toLowerCase();
    return /^[a-z]{2}(-[a-z]{2,8})?$/.test(clean) ? clean : 'es-latam';
}

function extractCompletedSets(state) {
    const lessons = new Set();
    const stories = new Set();
    if (!state || typeof state !== 'object') return { lessons, stories };

    Object.keys(state).forEach(course => {
        if (course === '_global') return;
        const bucket = state[course];
        if (!bucket || typeof bucket !== 'object') return;

        const prog = parseJsonSafe(bucket.progress, null);
        if (prog && typeof prog === 'object') {
            Object.keys(prog).forEach(lessonId => {
                if (prog[lessonId]) lessons.add(course + ':' + lessonId);
            });
        }

        const read = parseJsonSafe(bucket.readStories, null);
        if (Array.isArray(read)) {
            read.forEach(storyId => {
                if (typeof storyId === 'string' && storyId) stories.add(course + ':' + storyId);
            });
        } else if (read && typeof read === 'object') {
            Object.keys(read).forEach(storyId => {
                if (read[storyId]) stories.add(course + ':' + storyId);
            });
        }
    });

    return { lessons, stories };
}

function extractXpState(state) {
    if (!state || typeof state !== 'object' || !state._global) {
        return { total: 0, history: {} };
    }
    const parsed = parseJsonSafe(state._global.spanishApp_xp, null);
    if (!parsed || typeof parsed !== 'object') {
        return { total: 0, history: {} };
    }
    return {
        total: Math.max(0, Number(parsed.total) || 0),
        history: (parsed.history && typeof parsed.history === 'object') ? parsed.history : {}
    };
}

function computeStreakDays(history, nowMs) {
    if (!history || typeof history !== 'object') return 0;
    let streak = 0;
    for (let offset = 0; offset < 365; offset++) {
        const d = utcDateString(nowMs - offset * 86400000);
        const rec = history[d];
        const hasActivity = rec && (
            (typeof rec === 'number' && rec > 0) ||
            (typeof rec === 'object' && ((Number(rec.total) || 0) > 0 || (Number(rec.reviewsDone) || 0) > 0 || (Number(rec.lessonsDone) || 0) > 0 || (Number(rec.storiesDone) || 0) > 0))
        );
        if (hasActivity) {
            streak++;
        } else if (offset === 0) {
            // Today not yet completed does not break yesterday's streak
            continue;
        } else {
            break;
        }
    }
    return streak;
}

async function updateSocialStatsFromSync(env, userId, prevState, nextState, nowMs) {
    await ensureSocialTables(env);
    const profile = await env.DB.prepare(
        'SELECT social_opt_in FROM user_profiles WHERE user_id = ?'
    ).bind(userId).first();
    if (!profile || !profile.social_opt_in) return;

    const weekKey = getIsoWeekKey(nowMs);
    const todayUtc = utcDateString(nowMs);
    const yesterdayUtc = utcDateString(nowMs - 86400000);

    const nextXp = extractXpState(nextState);
    const rank = rankForXP(nextXp.total);
    const streakDays = computeStreakDays(nextXp.history, nowMs);

    const existingStats = await env.DB.prepare(
        'SELECT * FROM user_weekly_stats WHERE user_id = ? AND week_key = ?'
    ).bind(userId, weekKey).first();

    let cappedXp = existingStats ? (Number(existingStats.capped_xp) || 0) : 0;
    let lessonsDone = existingStats ? (Number(existingStats.lessons_done) || 0) : 0;
    let storiesDone = existingStats ? (Number(existingStats.stories_done) || 0) : 0;
    const activeDays = new Set(parseJsonSafe(existingStats && existingStats.active_days_json, []));
    const dailyXp = parseJsonSafe(existingStats && existingStats.daily_xp_json, {});

    let newLessons = 0;
    let newStories = 0;
    let xpDeltaAdded = 0;
    let activeDaysDelta = 0;

    // First sync ever establishes the baseline so importing old progress cannot
    // backfill the current week's board.
    if (prevState && typeof prevState === 'object') {
        const prevSets = extractCompletedSets(prevState);
        const nextSets = extractCompletedSets(nextState);
        const prevXp = extractXpState(prevState);

        nextSets.lessons.forEach(id => {
            if (!prevSets.lessons.has(id)) newLessons++;
        });
        nextSets.stories.forEach(id => {
            if (!prevSets.stories.has(id)) newStories++;
        });

        newLessons = Math.min(newLessons, MAX_SYNC_LESSONS_PER_POST);
        newStories = Math.min(newStories, MAX_SYNC_STORIES_PER_POST);

        const allowedDates = [todayUtc, yesterdayUtc].filter(d => getIsoWeekKey(Date.parse(d + 'T12:00:00Z')) === weekKey);

        allowedDates.forEach(d => {
            if (!dailyXp[d] || typeof dailyXp[d] !== 'object') {
                dailyXp[d] = { total: 0, review: 0 };
            }
            const dayRec = dailyXp[d];
            const prevDayHist = prevXp.history[d];
            const nextDayHist = nextXp.history[d];
            const prevRev = (prevDayHist && typeof prevDayHist === 'object') ? Math.max(0, Number(prevDayHist.review) || 0) : 0;
            const nextRev = (nextDayHist && typeof nextDayHist === 'object') ? Math.max(0, Number(nextDayHist.review) || 0) : 0;
            const revDeltaRaw = Math.max(0, nextRev - prevRev);

            const revRoom = Math.max(0, MAX_DAILY_REVIEW_XP - (Number(dayRec.review) || 0));
            const revCredited = Math.min(revDeltaRaw, revRoom);

            const lessonStoryXp = (d === todayUtc)
                ? (newLessons * SOCIAL_LESSON_XP + newStories * SOCIAL_STORY_XP)
                : 0;

            const rawDayAdd = revCredited + lessonStoryXp;
            if (rawDayAdd > 0) {
                const dayRoom = Math.max(0, MAX_DAILY_BOARD_XP - (Number(dayRec.total) || 0));
                const dayCredited = Math.min(rawDayAdd, dayRoom);
                dayRec.review = (Number(dayRec.review) || 0) + revCredited;
                dayRec.total = (Number(dayRec.total) || 0) + dayCredited;
                cappedXp += dayCredited;
                xpDeltaAdded += dayCredited;

                if (!activeDays.has(d)) {
                    activeDays.add(d);
                    activeDaysDelta++;
                }
            }
        });

        lessonsDone += newLessons;
        storiesDone += newStories;
    }

    const activeDaysArr = Array.from(activeDays).sort();
    await env.DB.prepare(
        'INSERT INTO user_weekly_stats (user_id, week_key, capped_xp, active_days_json, daily_xp_json, lessons_done, stories_done, rank, streak_days, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(user_id, week_key) DO UPDATE SET capped_xp = excluded.capped_xp, active_days_json = excluded.active_days_json, daily_xp_json = excluded.daily_xp_json, lessons_done = excluded.lessons_done, stories_done = excluded.stories_done, rank = excluded.rank, streak_days = excluded.streak_days, updated_at = excluded.updated_at'
    ).bind(
        userId,
        weekKey,
        cappedXp,
        JSON.stringify(activeDaysArr),
        JSON.stringify(dailyXp),
        lessonsDone,
        storiesDone,
        rank,
        streakDays,
        nowMs
    ).run();

    // Advance any active Friend Quest for this user in the current week
    if (newLessons > 0 || newStories > 0 || xpDeltaAdded > 0 || activeDaysDelta > 0) {
        const quest = await env.DB.prepare(
            'SELECT * FROM friend_quests WHERE week_key = ? AND status = \'active\' AND (user_a = ? OR user_b = ?)'
        ).bind(weekKey, userId, userId).first();

        if (quest) {
            let delta = 0;
            if (quest.quest_type === 'lessons') delta = newLessons;
            else if (quest.quest_type === 'stories') delta = newStories;
            else if (quest.quest_type === 'active_days') delta = activeDaysDelta;
            else if (quest.quest_type === 'xp') delta = xpDeltaAdded;

            if (delta > 0) {
                const isA = quest.user_a === userId;
                const nextA = (Number(quest.progress_a) || 0) + (isA ? delta : 0);
                const nextB = (Number(quest.progress_b) || 0) + (isA ? 0 : delta);
                const done = (nextA + nextB) >= (Number(quest.target) || 1);
                const nextStatus = done ? 'completed' : 'active';
                const completedAt = done ? (quest.completed_at || nowMs) : null;

                await env.DB.prepare(
                    'UPDATE friend_quests SET progress_a = ?, progress_b = ?, status = ?, completed_at = ? WHERE id = ?'
                ).bind(nextA, nextB, nextStatus, completedAt, quest.id).run();
            }
        }
    }
}

async function handleGetSocialProfile(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    const profile = await env.DB.prepare(
        'SELECT user_id, display_name, friend_code, social_opt_in, public_board_opt_in, active_course, updated_at FROM user_profiles WHERE user_id = ?'
    ).bind(session.sub).first();

    const weekKey = getIsoWeekKey(Date.now());
    const pendingFriends = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM friendships WHERE user_b = ? AND status = \'pending\''
    ).bind(session.sub).first();
    const pendingQuests = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM friend_quests WHERE user_b = ? AND week_key = ? AND status = \'pending\''
    ).bind(session.sub, weekKey).first();

    if (!profile) {
        return json({
            optedIn: false,
            profile: null,
            weekKey,
            pendingFriendRequests: pendingFriends ? pendingFriends.n : 0,
            pendingQuestInvites: pendingQuests ? pendingQuests.n : 0
        }, 200, cors);
    }

    return json({
        optedIn: Boolean(profile.social_opt_in),
        profile: {
            displayName: profile.display_name,
            friendCode: profile.friend_code,
            socialOptIn: Boolean(profile.social_opt_in),
            publicBoardOptIn: Boolean(profile.public_board_opt_in),
            activeCourse: profile.active_course,
            updatedAt: profile.updated_at
        },
        weekKey,
        pendingFriendRequests: pendingFriends ? pendingFriends.n : 0,
        pendingQuestInvites: pendingQuests ? pendingQuests.n : 0
    }, 200, cors);
}

async function handlePostSocialProfile(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const existing = await env.DB.prepare(
        'SELECT * FROM user_profiles WHERE user_id = ?'
    ).bind(session.sub).first();

    const socialOptIn = typeof body.socialOptIn === 'boolean'
        ? (body.socialOptIn ? 1 : 0)
        : (existing ? existing.social_opt_in : 1);

    const publicBoardOptIn = typeof body.publicBoardOptIn === 'boolean'
        ? (body.publicBoardOptIn ? 1 : 0)
        : (existing ? existing.public_board_opt_in : 0);

    const activeCourse = body.activeCourse
        ? sanitizeCourseCode(body.activeCourse)
        : (existing ? existing.active_course : 'es-latam');

    let displayName = existing ? existing.display_name : '';
    if (typeof body.displayName === 'string') {
        const cleaned = sanitizeDisplayName(body.displayName);
        if (!cleaned) {
            return json({ error: 'Display name must be 2 to 24 characters (no emojis).' }, 400, cors);
        }
        displayName = cleaned;
    } else if (!displayName && socialOptIn) {
        return json({ error: 'Enter a display name (2 to 24 characters).' }, 400, cors);
    }

    let friendCode = existing ? existing.friend_code : '';
    if (!friendCode) {
        for (let attempt = 0; attempt < 6; attempt++) {
            const candidate = generateFriendCode();
            const taken = await env.DB.prepare(
                'SELECT 1 AS found FROM user_profiles WHERE friend_code = ?'
            ).bind(candidate).first();
            if (!taken) {
                friendCode = candidate;
                break;
            }
        }
        if (!friendCode) return json({ error: 'Could not generate friend code' }, 500, cors);
    }

    const nowMs = Date.now();
    await env.DB.prepare(
        'INSERT INTO user_profiles (user_id, display_name, friend_code, social_opt_in, public_board_opt_in, active_course, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT(user_id) DO UPDATE SET display_name = excluded.display_name, social_opt_in = excluded.social_opt_in, public_board_opt_in = excluded.public_board_opt_in, active_course = excluded.active_course, updated_at = excluded.updated_at'
    ).bind(session.sub, displayName || 'Learner', friendCode, socialOptIn, publicBoardOptIn, activeCourse, nowMs).run();

    // Seed current week's stats row with Rank/streak if opting in for the first time
    if (socialOptIn) {
        const weekKey = getIsoWeekKey(nowMs);
        const existingStats = await env.DB.prepare(
            'SELECT 1 AS found FROM user_weekly_stats WHERE user_id = ? AND week_key = ?'
        ).bind(session.sub, weekKey).first();
        if (!existingStats) {
            const userRow = await env.DB.prepare('SELECT state_json FROM users WHERE id = ?').bind(session.sub).first();
            const parsedState = userRow && userRow.state_json ? parseJsonSafe(userRow.state_json, null) : null;
            const xp = extractXpState(parsedState);
            await env.DB.prepare(
                'INSERT INTO user_weekly_stats (user_id, week_key, capped_xp, active_days_json, daily_xp_json, lessons_done, stories_done, rank, streak_days, updated_at) VALUES (?, ?, 0, \'[]\', \'{}\', 0, 0, ?, ?, ?)'
            ).bind(session.sub, weekKey, rankForXP(xp.total), computeStreakDays(xp.history, nowMs), nowMs).run();
        }
    }

    return json({
        ok: true,
        optedIn: Boolean(socialOptIn),
        profile: {
            displayName: displayName || 'Learner',
            friendCode,
            socialOptIn: Boolean(socialOptIn),
            publicBoardOptIn: Boolean(publicBoardOptIn),
            activeCourse,
            updatedAt: nowMs
        }
    }, 200, cors);
}

async function handleGetFriends(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    const weekKey = getIsoWeekKey(Date.now());
    const rowsRes = await env.DB.prepare(
        'SELECT user_a, user_b, status, created_at FROM friendships WHERE (user_a = ? OR user_b = ?) AND status IN (\'accepted\', \'pending\')'
    ).bind(session.sub, session.sub).all();
    const rels = (rowsRes && rowsRes.results) ? rowsRes.results : [];

    const friends = [];
    const incoming = [];
    const outgoing = [];

    for (let i = 0; i < rels.length; i++) {
        const rel = rels[i];
        const otherId = rel.user_a === session.sub ? rel.user_b : rel.user_a;
        const prof = await env.DB.prepare(
            'SELECT user_id, display_name, friend_code, social_opt_in, active_course FROM user_profiles WHERE user_id = ?'
        ).bind(otherId).first();
        if (!prof || !prof.social_opt_in) continue;

        if (rel.status === 'accepted') {
            const st = await env.DB.prepare(
                'SELECT capped_xp, active_days_json, lessons_done, stories_done, rank, streak_days, updated_at FROM user_weekly_stats WHERE user_id = ? AND week_key = ?'
            ).bind(otherId, weekKey).first();
            const days = parseJsonSafe(st && st.active_days_json, []);
            friends.push({
                userId: otherId,
                displayName: prof.display_name,
                friendCode: prof.friend_code,
                activeCourse: prof.active_course,
                weeklyXp: st ? (Number(st.capped_xp) || 0) : 0,
                activeDays: Array.isArray(days) ? days.length : 0,
                lessonsDone: st ? (Number(st.lessons_done) || 0) : 0,
                storiesDone: st ? (Number(st.stories_done) || 0) : 0,
                rank: st ? (Number(st.rank) || 1) : 1,
                streakDays: st ? (Number(st.streak_days) || 0) : 0
            });
        } else if (rel.status === 'pending') {
            const item = {
                userId: otherId,
                displayName: prof.display_name,
                friendCode: prof.friend_code,
                activeCourse: prof.active_course,
                createdAt: rel.created_at
            };
            if (rel.user_b === session.sub) incoming.push(item);
            else outgoing.push(item);
        }
    }

    friends.sort((a, b) => (b.weeklyXp - a.weeklyXp) || (b.activeDays - a.activeDays) || a.displayName.localeCompare(b.displayName));

    return json({ weekKey, friends, incoming, outgoing }, 200, cors);
}

async function handleFriendRequest(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const myProfile = await env.DB.prepare(
        'SELECT social_opt_in FROM user_profiles WHERE user_id = ?'
    ).bind(session.sub).first();
    if (!myProfile || !myProfile.social_opt_in) {
        return json({ error: 'Enable your social profile first.' }, 403, cors);
    }

    const rawCode = typeof body.friendCode === 'string' ? body.friendCode.trim().toUpperCase() : '';
    if (!/^PRL-[A-Z0-9]{4,8}$/.test(rawCode)) {
        return json({ error: 'Enter a valid friend code (e.g. PRL-7K4M2).' }, 400, cors);
    }

    const target = await env.DB.prepare(
        'SELECT user_id, display_name, social_opt_in FROM user_profiles WHERE friend_code = ?'
    ).bind(rawCode).first();
    if (!target || !target.social_opt_in) {
        return json({ error: 'No learner found with that friend code.' }, 404, cors);
    }
    if (target.user_id === session.sub) {
        return json({ error: 'That is your own friend code.' }, 400, cors);
    }

    const existing = await env.DB.prepare(
        'SELECT user_a, user_b, status FROM friendships WHERE (user_a = ? AND user_b = ?) OR (user_a = ? AND user_b = ?)'
    ).bind(session.sub, target.user_id, target.user_id, session.sub).first();

    if (existing) {
        if (existing.status === 'blocked') {
            return json({ error: 'Unable to send a request to this learner.' }, 403, cors);
        }
        if (existing.status === 'accepted') {
            return json({ ok: true, status: 'accepted', displayName: target.display_name }, 200, cors);
        }
        if (existing.status === 'pending' && existing.user_b === session.sub) {
            // Mutual request: auto-accept
            const nowMs = Date.now();
            await env.DB.prepare(
                'UPDATE friendships SET status = \'accepted\', updated_at = ? WHERE user_a = ? AND user_b = ?'
            ).bind(nowMs, existing.user_a, existing.user_b).run();
            return json({ ok: true, status: 'accepted', displayName: target.display_name }, 200, cors);
        }
        return json({ ok: true, status: 'pending', displayName: target.display_name }, 200, cors);
    }

    const pendingCount = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM friendships WHERE user_a = ? AND status = \'pending\''
    ).bind(session.sub).first();
    if (pendingCount && pendingCount.n >= MAX_PENDING_FRIEND_REQUESTS) {
        return json({ error: 'Too many pending friend requests.' }, 429, cors);
    }

    const nowMs = Date.now();
    await env.DB.prepare(
        'INSERT INTO friendships (user_a, user_b, status, created_at, updated_at) VALUES (?, ?, \'pending\', ?, ?)'
    ).bind(session.sub, target.user_id, nowMs, nowMs).run();

    return json({ ok: true, status: 'pending', displayName: target.display_name }, 200, cors);
}

async function handleFriendRespond(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const fromUserId = typeof body.userId === 'string' ? body.userId.trim() : '';
    const action = typeof body.action === 'string' ? body.action.trim() : '';
    if (!fromUserId || !['accept', 'decline', 'block'].includes(action)) {
        return json({ error: 'Invalid request' }, 400, cors);
    }

    const rel = await env.DB.prepare(
        'SELECT * FROM friendships WHERE user_a = ? AND user_b = ? AND status = \'pending\''
    ).bind(fromUserId, session.sub).first();
    if (!rel) return json({ error: 'Friend request not found' }, 404, cors);

    const nowMs = Date.now();
    if (action === 'accept') {
        await env.DB.prepare(
            'UPDATE friendships SET status = \'accepted\', updated_at = ? WHERE user_a = ? AND user_b = ?'
        ).bind(nowMs, fromUserId, session.sub).run();
    } else if (action === 'block') {
        await env.DB.prepare(
            'UPDATE friendships SET status = \'blocked\', updated_at = ? WHERE user_a = ? AND user_b = ?'
        ).bind(nowMs, fromUserId, session.sub).run();
    } else {
        await env.DB.prepare(
            'DELETE FROM friendships WHERE user_a = ? AND user_b = ?'
        ).bind(fromUserId, session.sub).run();
    }

    return json({ ok: true, action }, 200, cors);
}

async function handleFriendRemove(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const otherId = typeof body.userId === 'string' ? body.userId.trim() : '';
    if (!otherId) return json({ error: 'Missing userId' }, 400, cors);

    await env.DB.prepare(
        'DELETE FROM friendships WHERE (user_a = ? AND user_b = ?) OR (user_a = ? AND user_b = ?)'
    ).bind(session.sub, otherId, otherId, session.sub).run();

    return json({ ok: true, removed: true }, 200, cors);
}

async function handleGetLeaderboard(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    const weekKey = getIsoWeekKey(Date.now());
    const myProfile = await env.DB.prepare(
        'SELECT user_id, display_name, friend_code, social_opt_in, active_course FROM user_profiles WHERE user_id = ?'
    ).bind(session.sub).first();

    if (!myProfile || !myProfile.social_opt_in) {
        return json({ weekKey, dailyCap: MAX_DAILY_BOARD_XP, entries: [] }, 200, cors);
    }

    const relsRes = await env.DB.prepare(
        'SELECT user_a, user_b FROM friendships WHERE (user_a = ? OR user_b = ?) AND status = \'accepted\''
    ).bind(session.sub, session.sub).all();
    const rels = (relsRes && relsRes.results) ? relsRes.results : [];

    const memberIds = new Set([session.sub]);
    rels.forEach(r => {
        memberIds.add(r.user_a === session.sub ? r.user_b : r.user_a);
    });

    const entries = [];
    for (const uid of memberIds) {
        const prof = uid === session.sub
            ? myProfile
            : await env.DB.prepare(
                'SELECT user_id, display_name, friend_code, social_opt_in, active_course FROM user_profiles WHERE user_id = ?'
            ).bind(uid).first();
        if (!prof || !prof.social_opt_in) continue;

        const st = await env.DB.prepare(
            'SELECT capped_xp, active_days_json, lessons_done, stories_done, rank, streak_days FROM user_weekly_stats WHERE user_id = ? AND week_key = ?'
        ).bind(uid, weekKey).first();
        const days = parseJsonSafe(st && st.active_days_json, []);

        entries.push({
            userId: uid,
            isSelf: uid === session.sub,
            displayName: prof.display_name,
            activeCourse: prof.active_course,
            weeklyXp: st ? (Number(st.capped_xp) || 0) : 0,
            activeDays: Array.isArray(days) ? days.length : 0,
            lessonsDone: st ? (Number(st.lessons_done) || 0) : 0,
            storiesDone: st ? (Number(st.stories_done) || 0) : 0,
            rank: st ? (Number(st.rank) || 1) : 1,
            streakDays: st ? (Number(st.streak_days) || 0) : 0
        });
    }

    entries.sort((a, b) =>
        (b.weeklyXp - a.weeklyXp) ||
        (b.activeDays - a.activeDays) ||
        (b.rank - a.rank) ||
        a.displayName.localeCompare(b.displayName)
    );

    entries.forEach((entry, idx) => {
        entry.position = idx + 1;
    });

    return json({
        weekKey,
        scope: 'friends',
        dailyCap: MAX_DAILY_BOARD_XP,
        reviewDailyCap: MAX_DAILY_REVIEW_XP,
        entries
    }, 200, cors);
}

async function formatQuestRow(env, quest, viewerId) {
    if (!quest) return null;
    const isA = quest.user_a === viewerId;
    const partnerId = isA ? quest.user_b : quest.user_a;
    const partnerProf = await env.DB.prepare(
        'SELECT display_name, active_course FROM user_profiles WHERE user_id = ?'
    ).bind(partnerId).first();
    const meta = QUEST_TYPES[quest.quest_type] || QUEST_TYPES.xp;
    const myProgress = isA ? (Number(quest.progress_a) || 0) : (Number(quest.progress_b) || 0);
    const partnerProgress = isA ? (Number(quest.progress_b) || 0) : (Number(quest.progress_a) || 0);
    const myLastCheer = isA ? quest.cheer_a_at : quest.cheer_b_at;
    const partnerLastCheer = isA ? quest.cheer_b_at : quest.cheer_a_at;

    return {
        id: quest.id,
        weekKey: quest.week_key,
        questType: quest.quest_type,
        label: meta.label,
        unit: meta.unit,
        target: Number(quest.target) || meta.target,
        myProgress,
        partnerProgress,
        totalProgress: Math.min(Number(quest.target) || meta.target, myProgress + partnerProgress),
        status: quest.status,
        isInviter: isA,
        partner: {
            userId: partnerId,
            displayName: partnerProf ? partnerProf.display_name : 'Friend',
            activeCourse: partnerProf ? partnerProf.active_course : 'es-latam'
        },
        myLastCheerAt: myLastCheer || null,
        partnerLastCheerAt: partnerLastCheer || null,
        completedAt: quest.completed_at || null
    };
}

async function handleGetQuests(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    const nowMs = Date.now();
    const weekKey = getIsoWeekKey(nowMs);
    const prevWeekKey = getPreviousIsoWeekKey(nowMs);

    const currentRow = await env.DB.prepare(
        'SELECT * FROM friend_quests WHERE week_key = ? AND status IN (\'pending\', \'active\', \'completed\') AND (user_a = ? OR user_b = ?) ORDER BY created_at DESC LIMIT 1'
    ).bind(weekKey, session.sub, session.sub).first();

    const prevRow = await env.DB.prepare(
        'SELECT * FROM friend_quests WHERE week_key = ? AND status = \'completed\' AND (user_a = ? OR user_b = ?) ORDER BY completed_at DESC LIMIT 1'
    ).bind(prevWeekKey, session.sub, session.sub).first();

    return json({
        weekKey,
        questTypes: Object.values(QUEST_TYPES),
        currentQuest: await formatQuestRow(env, currentRow, session.sub),
        lastWeekCompleted: await formatQuestRow(env, prevRow, session.sub)
    }, 200, cors);
}

async function handleStartQuest(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const friendId = typeof body.friendId === 'string' ? body.friendId.trim() : '';
    const questType = (typeof body.questType === 'string' && QUEST_TYPES[body.questType]) ? body.questType : 'lessons';
    if (!friendId || friendId === session.sub) {
        return json({ error: 'Choose a friend for this quest.' }, 400, cors);
    }

    const friendship = await env.DB.prepare(
        'SELECT 1 AS found FROM friendships WHERE ((user_a = ? AND user_b = ?) OR (user_a = ? AND user_b = ?)) AND status = \'accepted\''
    ).bind(session.sub, friendId, friendId, session.sub).first();
    if (!friendship) {
        return json({ error: 'You can only start quests with accepted friends.' }, 403, cors);
    }

    const nowMs = Date.now();
    const weekKey = getIsoWeekKey(nowMs);

    const myBusy = await env.DB.prepare(
        'SELECT 1 AS found FROM friend_quests WHERE week_key = ? AND status IN (\'pending\', \'active\', \'completed\') AND (user_a = ? OR user_b = ?)'
    ).bind(weekKey, session.sub, session.sub).first();
    if (myBusy) {
        return json({ error: 'You already have a quest for this week.' }, 409, cors);
    }

    const friendBusy = await env.DB.prepare(
        'SELECT 1 AS found FROM friend_quests WHERE week_key = ? AND status IN (\'pending\', \'active\', \'completed\') AND (user_a = ? OR user_b = ?)'
    ).bind(weekKey, friendId, friendId).first();
    if (friendBusy) {
        return json({ error: 'That friend already has a quest this week.' }, 409, cors);
    }

    const meta = QUEST_TYPES[questType];
    const id = randomToken();
    await env.DB.prepare(
        'INSERT INTO friend_quests (id, week_key, user_a, user_b, quest_type, target, progress_a, progress_b, status, created_at) VALUES (?, ?, ?, ?, ?, ?, 0, 0, \'pending\', ?)'
    ).bind(id, weekKey, session.sub, friendId, meta.type, meta.target, nowMs).run();

    const created = await env.DB.prepare('SELECT * FROM friend_quests WHERE id = ?').bind(id).first();
    return json({ ok: true, quest: await formatQuestRow(env, created, session.sub) }, 200, cors);
}

async function handleAutoMatchQuest(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body = {};
    try {
        body = await request.json();
    } catch (e) {
        body = {};
    }

    const questType = (typeof body.questType === 'string' && QUEST_TYPES[body.questType]) ? body.questType : 'lessons';
    const nowMs = Date.now();
    const weekKey = getIsoWeekKey(nowMs);

    const myBusy = await env.DB.prepare(
        'SELECT 1 AS found FROM friend_quests WHERE week_key = ? AND status IN (\'pending\', \'active\', \'completed\') AND (user_a = ? OR user_b = ?)'
    ).bind(weekKey, session.sub, session.sub).first();
    if (myBusy) {
        return json({ error: 'You already have a quest for this week.' }, 409, cors);
    }

    const relsRes = await env.DB.prepare(
        'SELECT user_a, user_b FROM friendships WHERE (user_a = ? OR user_b = ?) AND status = \'accepted\''
    ).bind(session.sub, session.sub).all();
    const rels = (relsRes && relsRes.results) ? relsRes.results : [];

    const candidates = [];
    for (let i = 0; i < rels.length; i++) {
        const friendId = rels[i].user_a === session.sub ? rels[i].user_b : rels[i].user_a;
        const prof = await env.DB.prepare(
            'SELECT user_id, social_opt_in, updated_at FROM user_profiles WHERE user_id = ?'
        ).bind(friendId).first();
        if (!prof || !prof.social_opt_in) continue;

        const busy = await env.DB.prepare(
            'SELECT 1 AS found FROM friend_quests WHERE week_key = ? AND status IN (\'pending\', \'active\', \'completed\') AND (user_a = ? OR user_b = ?)'
        ).bind(weekKey, friendId, friendId).first();
        if (busy) continue;

        const st = await env.DB.prepare(
            'SELECT updated_at FROM user_weekly_stats WHERE user_id = ? AND week_key = ?'
        ).bind(friendId, weekKey).first();

        candidates.push({
            userId: friendId,
            lastActive: (st && st.updated_at) ? Number(st.updated_at) : (Number(prof.updated_at) || 0)
        });
    }

    if (!candidates.length) {
        return json({
            ok: true,
            matched: false,
            message: 'No friends are free for a quest this week yet.'
        }, 200, cors);
    }

    candidates.sort((a, b) => b.lastActive - a.lastActive);
    const partnerId = candidates[0].userId;
    const meta = QUEST_TYPES[questType];
    const id = randomToken();

    await env.DB.prepare(
        'INSERT INTO friend_quests (id, week_key, user_a, user_b, quest_type, target, progress_a, progress_b, status, created_at) VALUES (?, ?, ?, ?, ?, ?, 0, 0, \'active\', ?)'
    ).bind(id, weekKey, session.sub, partnerId, meta.type, meta.target, nowMs).run();

    const created = await env.DB.prepare('SELECT * FROM friend_quests WHERE id = ?').bind(id).first();
    return json({ ok: true, matched: true, quest: await formatQuestRow(env, created, session.sub) }, 200, cors);
}

async function handleRespondQuest(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const questId = typeof body.questId === 'string' ? body.questId.trim() : '';
    const action = typeof body.action === 'string' ? body.action.trim() : '';
    if (!questId || !['accept', 'decline'].includes(action)) {
        return json({ error: 'Invalid request' }, 400, cors);
    }

    const quest = await env.DB.prepare(
        'SELECT * FROM friend_quests WHERE id = ? AND user_b = ? AND status = \'pending\''
    ).bind(questId, session.sub).first();
    if (!quest) return json({ error: 'Quest invite not found' }, 404, cors);

    const nextStatus = action === 'accept' ? 'active' : 'declined';
    await env.DB.prepare('UPDATE friend_quests SET status = ? WHERE id = ?')
        .bind(nextStatus, questId).run();

    const updated = await env.DB.prepare('SELECT * FROM friend_quests WHERE id = ?').bind(questId).first();
    return json({ ok: true, quest: nextStatus === 'active' ? await formatQuestRow(env, updated, session.sub) : null }, 200, cors);
}

async function handleCheerQuest(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);
    await ensureSocialTables(env);

    let body;
    try {
        body = await request.json();
    } catch (e) {
        return json({ error: 'Bad request' }, 400, cors);
    }

    const questId = typeof body.questId === 'string' ? body.questId.trim() : '';
    if (!questId) return json({ error: 'Missing questId' }, 400, cors);

    const quest = await env.DB.prepare(
        'SELECT * FROM friend_quests WHERE id = ? AND status IN (\'active\', \'completed\') AND (user_a = ? OR user_b = ?)'
    ).bind(questId, session.sub, session.sub).first();
    if (!quest) return json({ error: 'Quest not found' }, 404, cors);

    const isA = quest.user_a === session.sub;
    const lastCheer = isA ? quest.cheer_a_at : quest.cheer_b_at;
    const nowMs = Date.now();
    if (lastCheer && (nowMs - Number(lastCheer)) < CHEER_COOLDOWN_MS) {
        return json({ ok: true, alreadySent: true }, 200, cors);
    }

    const col = isA ? 'cheer_a_at' : 'cheer_b_at';
    await env.DB.prepare('UPDATE friend_quests SET ' + col + ' = ? WHERE id = ?')
        .bind(nowMs, questId).run();

    return json({ ok: true, sentAt: nowMs }, 200, cors);
}

async function handleDeleteAccount(request, env, cors) {
    const session = await requireSession(request, env);
    if (!session) return json({ error: 'Not signed in' }, 401, cors);

    await ensureBooksTable(env);
    await ensureSocialTables(env);

    let email = typeof session.email === 'string' ? session.email.trim().toLowerCase() : '';
    if (!email) {
        const userRow = await env.DB.prepare('SELECT email FROM users WHERE id = ?').bind(session.sub).first();
        email = userRow && typeof userRow.email === 'string' ? userRow.email.trim().toLowerCase() : '';
    }

    await env.DB.prepare('DELETE FROM friend_quests WHERE user_a = ? OR user_b = ?').bind(session.sub, session.sub).run();
    await env.DB.prepare('DELETE FROM friendships WHERE user_a = ? OR user_b = ?').bind(session.sub, session.sub).run();
    await env.DB.prepare('DELETE FROM user_weekly_stats WHERE user_id = ?').bind(session.sub).run();
    await env.DB.prepare('DELETE FROM user_profiles WHERE user_id = ?').bind(session.sub).run();
    await env.DB.prepare('DELETE FROM user_books WHERE user_id = ?').bind(session.sub).run();
    if (email) {
        await env.DB.prepare('DELETE FROM magic_links WHERE email = ?').bind(email).run();
    }
    await env.DB.prepare('DELETE FROM users WHERE id = ?').bind(session.sub).run();

    return json({ ok: true, deleted: true }, 200, cors);
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const path = new URL(request.url).pathname;

        if (request.method === 'GET' && path === '/health') {
            return json({
                status: 'ok',
                service: 'parlour-sync',
                hasDb: Boolean(env && env.DB),
                hasJwtSecret: Boolean(env && env.JWT_SECRET),
                hasResendKey: Boolean(env && env.RESEND_API_KEY),
                hasGoogleClientId: Boolean(env && env.GOOGLE_CLIENT_ID),
                turnstileEnabled: Boolean(env && env.TURNSTILE_SECRET_KEY)
            }, 200, {
                'Access-Control-Allow-Origin': isAllowedOrigin(origin) ? origin : ALLOWED_ORIGINS[0],
                'Vary': 'Origin'
            });
        }

        const cors = corsHeaders(origin);

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors || {} });
        }
        if (!cors) {
            return new Response('Forbidden', { status: 403 });
        }

        if (path === '/auth/request-link' && request.method === 'POST') return handleRequestLink(request, env, cors);
        if (path === '/auth/verify' && request.method === 'POST') return handleVerify(request, env, cors);
        if (path === '/auth/google' && request.method === 'POST') return handleGoogleAuth(request, env, cors);
        if (path === '/auth/delete' && request.method === 'POST') return handleDeleteAccount(request, env, cors);
        if (path === '/sync/state' && request.method === 'GET') return handleGetState(request, env, cors);
        if (path === '/sync/state' && request.method === 'POST') return handlePostState(request, env, cors);
        if (path === '/sync/book' && request.method === 'GET') return handleGetBook(request, env, cors);
        if (path === '/sync/book' && request.method === 'POST') return handlePostBook(request, env, cors);
        if (path === '/social/profile' && request.method === 'GET') return handleGetSocialProfile(request, env, cors);
        if (path === '/social/profile' && request.method === 'POST') return handlePostSocialProfile(request, env, cors);
        if (path === '/social/friends' && request.method === 'GET') return handleGetFriends(request, env, cors);
        if (path === '/social/friends/request' && request.method === 'POST') return handleFriendRequest(request, env, cors);
        if (path === '/social/friends/respond' && request.method === 'POST') return handleFriendRespond(request, env, cors);
        if (path === '/social/friends/remove' && request.method === 'POST') return handleFriendRemove(request, env, cors);
        if (path === '/social/leaderboard' && request.method === 'GET') return handleGetLeaderboard(request, env, cors);
        if (path === '/social/quests' && request.method === 'GET') return handleGetQuests(request, env, cors);
        if (path === '/social/quests/start' && request.method === 'POST') return handleStartQuest(request, env, cors);
        if (path === '/social/quests/auto-match' && request.method === 'POST') return handleAutoMatchQuest(request, env, cors);
        if (path === '/social/quests/respond' && request.method === 'POST') return handleRespondQuest(request, env, cors);
        if (path === '/social/quests/cheer' && request.method === 'POST') return handleCheerQuest(request, env, cors);

        return json({ error: 'Not found' }, 404, cors);
    }
};

