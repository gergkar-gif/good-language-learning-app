// ============================================
// CLOUDFLARE GRADER WORKER (Cloudflare Workers AI + AI Gateway)
// ============================================
// Zero-dependency production AI grading worker for Parlour.
// Keeps all AI provider keys and endpoint configurations off the browser client.
//
// Deploy via Cloudflare dashboard (Workers & Pages -> Create -> paste this in)
// or via wrangler. Runs on Cloudflare Workers AI free tier
// (e.g. @cf/meta/llama-3.3-70b-instruct or @cf/meta/llama-3.1-8b-instruct).

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk',
    'http://localhost:8131'
];

const DEFAULT_MODEL = '@cf/meta/llama-3.3-70b-instruct';

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

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin) || {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        };

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: cors });
        }

        if (request.method !== 'POST') {
            return json({ error: 'Method not allowed' }, 405, cors);
        }

        const url = new URL(request.url);
        let payload;
        try {
            payload = await request.json();
        } catch {
            return json({ error: 'Invalid JSON body' }, 400, cors);
        }

        // Support both direct /grade format and standard /v1/chat/completions format
        let prompt = '';
        let messages = [];

        if (payload.messages && Array.isArray(payload.messages)) {
            messages = payload.messages;
        } else if (payload.prompt) {
            prompt = payload.prompt;
            messages = [
                { role: 'system', content: 'You are an expert CEFR-aligned language-learning grader. Return only valid JSON.' },
                { role: 'user', content: prompt }
            ];
        } else {
            return json({ error: 'Missing prompt or messages payload' }, 400, cors);
        }

        // Check if Cloudflare Workers AI is available in environment
        if (env && env.AI) {
            try {
                const model = env.GRADER_MODEL || DEFAULT_MODEL;
                const aiResult = await env.AI.run(model, {
                    messages,
                    temperature: 0,
                    max_tokens: 3000
                });

                const content = aiResult.response || aiResult.content || '';
                return json({
                    choices: [
                        {
                            message: {
                                role: 'assistant',
                                content: content
                            }
                        }
                    ]
                }, 200, cors);
            } catch (aiError) {
                // If quota exhausted (rate limit / daily neurons exceeded)
                if (String(aiError).includes('quota') || String(aiError).includes('limit') || String(aiError).includes('429')) {
                    return json({
                        error: 'Daily AI grading quota exceeded. Local deterministic assessment remains active.',
                        code: 'QUOTA_EXHAUSTED'
                    }, 429, cors);
                }
                return json({ error: 'Workers AI inference failed', details: String(aiError) }, 500, cors);
            }
        }

        // Fallback: If AI Gateway or Upstream OpenAI endpoint is configured in env
        if (env && (env.AI_GATEWAY_URL || env.OPENAI_COMPATIBLE_URL)) {
            try {
                const upstreamUrl = env.AI_GATEWAY_URL || env.OPENAI_COMPATIBLE_URL;
                const apiKey = env.UPSTREAM_API_KEY || '';

                const upstreamRes = await fetch(upstreamUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        ...(apiKey ? { 'Authorization': `Bearer ${apiKey}` } : {})
                    },
                    body: JSON.stringify({
                        model: env.UPSTREAM_MODEL || 'auto',
                        messages,
                        temperature: 0,
                        max_tokens: 3000,
                        response_format: { type: 'json_object' }
                    })
                });

                const data = await upstreamRes.json();
                return json(data, upstreamRes.status, cors);
            } catch (upstreamErr) {
                return json({ error: 'Upstream gateway error', details: String(upstreamErr) }, 502, cors);
            }
        }

        return json({
            error: 'No AI provider configured on worker. Bind env.AI (Workers AI) or env.AI_GATEWAY_URL.'
        }, 503, cors);
    }
};
