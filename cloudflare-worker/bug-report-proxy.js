// ============================================
// BUG REPORT PROXY (Cloudflare Worker)
// ============================================
// Holds the GitHub token server-side so the static site never has to ship
// it to a browser. The client (engine/bugreport.js) POSTs {title, body}
// here; this worker attaches the token and files the actual GitHub issue.
//
// Deploy via the Cloudflare dashboard (Workers & Pages -> Create -> paste
// this in), not committed-and-auto-deployed from this repo - see
// BUG_REPORT_SETUP.md for the full walkthrough. The token itself is set as
// a Worker secret (Settings -> Variables -> "GITHUB_TOKEN", encrypted),
// never as plain text anywhere, including here.

const GITHUB_REPO = 'gergkar-gif/good-language-learning-app';
const LABEL = 'bug-report';

// Only requests from these origins are allowed through — anyone else's
// request is refused before it ever touches the GitHub token. Add other
// origins here (e.g. a custom domain) if the site ever moves.
const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'http://localhost:8131'
];

function corsHeaders(origin) {
    if (!ALLOWED_ORIGINS.includes(origin)) return null;
    return {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    };
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
        if (request.method !== 'POST') {
            return new Response('Method not allowed', { status: 405, headers: cors });
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
            return new Response('GitHub error ' + ghResponse.status + ': ' + errText, {
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
