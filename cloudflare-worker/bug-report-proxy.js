// ============================================
// BUG REPORT PROXY (Cloudflare Worker)
// ============================================
// Holds the GitHub token server-side so the static site never has to ship
// it to a browser. The client (engine/bugreport.js) POSTs {title, body}
// here; this worker attaches the token and files the actual GitHub issue.
//
// Deploy via the Cloudflare dashboard (Workers & Pages -> Create -> paste
// this in), not committed-and-auto-deployed from this repo - see
// docs/SERVICES.md for the full walkthrough. The token itself is set as
// a Worker secret (Settings -> Variables -> "GITHUB_TOKEN", encrypted),
// never as plain text anywhere, including here.

const GITHUB_REPO = 'gergkar-gif/good-language-learning-app';
const LABEL = 'bug-report';

// Only requests from these origins are allowed through — anyone else's
// request is refused before it ever touches the GitHub token. Add other
// origins here (e.g. a custom domain) if the site ever moves.
const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131'
];

const MAX_PER_IP = 5;
const IP_WINDOW_MS = 10 * 60 * 1000;
const MAX_GLOBAL_PER_HOUR = 25;
const GLOBAL_WINDOW_MS = 60 * 60 * 1000;

// shortcut: per-isolate in-memory limiter resets on cold start; upgrade to KV or Cloudflare WAF rate limit if distributed spam occurs
const ipHits = new Map();
const globalHits = [];

function checkRateLimit(ip, now) {
    while (globalHits.length && globalHits[0] <= now - GLOBAL_WINDOW_MS) {
        globalHits.shift();
    }
    if (globalHits.length >= MAX_GLOBAL_PER_HOUR) return false;

    const recentIp = (ipHits.get(ip) || []).filter(t => t > now - IP_WINDOW_MS);
    if (recentIp.length >= MAX_PER_IP) {
        ipHits.set(ip, recentIp);
        return false;
    }

    if (ipHits.size > 1000) {
        for (const [k, list] of ipHits.entries()) {
            const kept = list.filter(t => t > now - IP_WINDOW_MS);
            if (kept.length) ipHits.set(k, kept);
            else ipHits.delete(k);
        }
    }

    recentIp.push(now);
    ipHits.set(ip, recentIp);
    globalHits.push(now);
    return true;
}

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
        'Access-Control-Allow-Headers': 'Content-Type',
        'Vary': 'Origin'
    };
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const url = new URL(request.url);

        if (request.method === 'GET' && url.pathname === '/health') {
            return new Response(JSON.stringify({
                status: 'ok',
                service: 'parlour-bug-report',
                hasGithubToken: Boolean(env && env.GITHUB_TOKEN)
            }), {
                status: 200,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': isAllowedOrigin(origin) ? origin : ALLOWED_ORIGINS[0],
                    'Vary': 'Origin'
                }
            });
        }

        const cors = corsHeaders(origin);

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors || {} });
        }
        if (!cors) {
            return new Response('Forbidden', { status: 403 });
        }
        if (request.method !== 'POST') {
            return new Response('Method not allowed', { status: 405, headers: cors });
        }

        const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
        if (!checkRateLimit(ip, Date.now())) {
            return new Response('Too many bug reports — try again later', { status: 429, headers: cors });
        }

        let payload;
        try {
            payload = await request.json();
        } catch (e) {
            return new Response('Bad request', { status: 400, headers: cors });
        }

        const title = typeof payload.title === 'string' ? payload.title.slice(0, 250) : '';
        if (!title) {
            return new Response('Missing title', { status: 400, headers: cors });
        }
        const body = typeof payload.body === 'string' ? payload.body.slice(0, 5000) : '';

        const ghResponse = await fetch('https://api.github.com/repos/' + GITHUB_REPO + '/issues', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + env.GITHUB_TOKEN,
                'Accept': 'application/vnd.github+json',
                'Content-Type': 'application/json',
                'User-Agent': 'parlour-bug-report-worker'
            },
            body: JSON.stringify({ title, body, labels: [LABEL] })
        });

        if (!ghResponse.ok) {
            const errText = await ghResponse.text();
            console.error('GitHub error ' + ghResponse.status + ': ' + errText);
            return new Response('GitHub error ' + ghResponse.status, {
                status: 502,
                headers: cors
            });
        }

        return new Response(JSON.stringify({ ok: true }), {
            status: 200,
            headers: Object.assign({ 'Content-Type': 'application/json' }, cors)
        });
    }
};
