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
// CLOUD_SYNC_SETUP.md for the full walkthrough, including the D1
// database and the two secrets this needs (JWT_SECRET, RESEND_API_KEY).
// Zero external imports on purpose, same reason bug-report-proxy.js has
// none: the dashboard's paste-and-deploy flow has no bundler.

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131'
];

const TOKEN_TTL_MS = 10 * 60 * 1000;        // magic-link token: 10 minutes
const SESSION_TTL_SECONDS = 30 * 24 * 60 * 60; // session token: 30 days
const MAX_LINKS_PER_HOUR = 3;
const RESEND_FROM = 'Parlour <noreply@parlour.me.uk>';

function corsHeaders(origin) {
    if (!ALLOWED_ORIGINS.includes(origin)) return null;
    return {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
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

    const updatedAt = Date.now();
    await env.DB.prepare('UPDATE users SET state_json = ?, updated_at = ? WHERE id = ?')
        .bind(JSON.stringify(payload.state), updatedAt, session.sub).run();

    return json({ ok: true, updatedAt }, 200, cors);
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin);

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors || {} });
        }
        if (!cors) {
            return new Response('Forbidden', { status: 403 });
        }

        const path = new URL(request.url).pathname;

        if (path === '/auth/request-link' && request.method === 'POST') return handleRequestLink(request, env, cors);
        if (path === '/auth/verify' && request.method === 'POST') return handleVerify(request, env, cors);
        if (path === '/sync/state' && request.method === 'GET') return handleGetState(request, env, cors);
        if (path === '/sync/state' && request.method === 'POST') return handlePostState(request, env, cors);

        return json({ error: 'Not found' }, 404, cors);
    }
};
