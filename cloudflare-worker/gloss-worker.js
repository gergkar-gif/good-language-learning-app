// ============================================
// CLOUDFLARE WORD-GLOSS WORKER (Cloudflare Workers AI + KV cache)
// ============================================
// The Reader's safety net for words the dictionary and the morphology rules
// can't resolve. The client sends the tapped word and its sentence; this
// worker asks a model for the base form and a short English gloss and caches
// the answer, so each word is generated once for every learner.
//
//   POST /gloss   { word, sentence, lang: 'hu' | 'es' }
//        -> { found: true, lemma, pos, gloss, model, cached } | { found: false }
//   GET  /health
//   GET  /export?lang=hu[&cursor=...]   (Authorization: Bearer EXPORT_TOKEN)
//        -> { entries: [{ word, lemma, pos, gloss }], cursor, complete }
//        Used by scripts/fill-dictionary-gaps.py pull-ai to turn the words
//        learners actually tapped into reviewed dictionary entries.
//
// Bindings (Settings -> Bindings): AI (Workers AI) and GLOSS_CACHE (a KV
// namespace; without it the worker still works, just uncached).
// Optional: GLOSS_DAILY_CAP (variable, default 600 uncached model calls a
// day, protecting the free Workers AI allowance), GLOSS_MODEL (variable),
// EXPORT_TOKEN (encrypted secret that enables /export).
// Deploy by pasting into the Cloudflare dashboard. See docs/SERVICES.md.

const ALLOWED_ORIGINS = [
    'https://gergkar-gif.github.io',
    'https://parlour.me.uk'
];

const CANDIDATE_MODELS = [
    '@cf/meta/llama-3.3-70b-instruct-fp8-fast',
    '@cf/mistralai/mistral-small-3.1-24b-instruct'
];

const LANG_NAME = { hu: 'Hungarian', es: 'Spanish' };
const POS_VALUES = ['noun', 'verb', 'adjective', 'adverb', 'pronoun', 'numeral', 'preposition',
    'postposition', 'conjunction', 'interjection', 'particle', 'determiner', 'phrase'];
const DEFAULT_DAILY_CAP = 600;
const NOT_FOUND_TTL = 7 * 24 * 3600;   // an "unsure" answer is retried after a week

function isAllowedOrigin(origin) {
    if (!origin) return false;
    if (ALLOWED_ORIGINS.includes(origin)) return true;
    return /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
}

function corsHeaders(origin) {
    return {
        'Access-Control-Allow-Origin': isAllowedOrigin(origin) ? origin : ALLOWED_ORIGINS[0],
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

function validWord(word) {
    return typeof word === 'string' && word.length >= 2 && word.length <= 40 &&
        /^[\p{L}'’-]+$/u.test(word);
}

function cleanSentence(sentence) {
    return String(sentence || '').replace(/[\u0000-\u001f]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 300);
}

function cacheKey(lang, word) {
    return 'v1:' + lang + ':' + word.toLowerCase();
}

function buildMessages(lang, word, sentence) {
    return [
        { role: 'system', content: 'You are a precise bilingual dictionary. Reply with one JSON object and nothing else.' },
        {
            role: 'user',
            content:
                'Language: ' + LANG_NAME[lang] + '. A learner tapped the word "' + word + '"' +
                (sentence ? ' in this sentence:\n"' + sentence + '"\n' : '.\n') +
                '\nGive its dictionary form and a short English gloss. Reply with JSON only, in exactly this shape:\n' +
                '{"lemma":"base form, lower case","pos":"' + POS_VALUES.join('|') + '","gloss":"2 to 8 words of English","confident":true}\n' +
                'Rules: the gloss describes the lemma as used in the sentence. Use no double quotes inside values. ' +
                'If the word is a typo, a fragment of a longer word, or you are not sure of its meaning, ' +
                'set "confident" to false and "gloss" to an empty string. Never guess.'
        }
    ];
}

// A model reply -> { found, lemma, pos, gloss } or { found: false }. Defensive on
// purpose: models wrap JSON in prose or code fences, and may invent a part of speech.
function parseModelReply(reply) {
    // Workers AI sometimes hands back JSON already parsed (an object), sometimes text.
    // `unreadable` marks a reply we couldn't make sense of, as opposed to a model that
    // answered "not sure": only the second is worth caching.
    let data = null;
    if (reply && typeof reply === 'object') {
        data = reply;
    } else {
        const match = /\{[\s\S]*\}/.exec(String(reply || ''));
        if (!match) return { found: false, unreadable: true };
        try { data = JSON.parse(match[0]); } catch (e) { return { found: false, unreadable: true }; }
    }
    if (!data || typeof data !== 'object') return { found: false, unreadable: true };
    if (data.confident === false) return { found: false };
    const lemma = String(data.lemma || '').trim().toLowerCase();
    const pos = String(data.pos || '').trim().toLowerCase();
    const gloss = String(data.gloss || '').replace(/["|]/g, '').replace(/\s+/g, ' ').trim();
    if (!lemma || lemma.length > 40 || !/^[\p{L}'’ -]+$/u.test(lemma)) return { found: false };
    if (!POS_VALUES.includes(pos)) return { found: false };
    if (!gloss || gloss.length > 90) return { found: false };
    return { found: true, lemma: lemma, pos: pos, gloss: gloss };
}

async function underDailyCap(env) {
    if (!env.GLOSS_CACHE) return true;
    const cap = parseInt(env.GLOSS_DAILY_CAP, 10) || DEFAULT_DAILY_CAP;
    const key = 'cap:' + new Date().toISOString().slice(0, 10);
    const used = parseInt(await env.GLOSS_CACHE.get(key), 10) || 0;
    if (used >= cap) return false;
    await env.GLOSS_CACHE.put(key, String(used + 1), { expirationTtl: 172800 });
    return true;
}

async function askModel(env, lang, word, sentence) {
    const models = [];
    if (env.GLOSS_MODEL) models.push(env.GLOSS_MODEL);
    models.push(...CANDIDATE_MODELS);
    let lastError = null;
    for (const model of [...new Set(models)]) {
        try {
            const result = await env.AI.run(model, {
                messages: buildMessages(lang, word, sentence),
                temperature: 0,
                max_tokens: 160
            });
            const reply = result.response !== undefined && result.response !== null ? result.response : result.content;
            return Object.assign(parseModelReply(reply), { model: model });
        } catch (err) {
            lastError = err;
            const text = String(err);
            if (text.includes('quota') || text.includes('limit') || text.includes('429')) {
                const quota = new Error('QUOTA');
                quota.code = 'QUOTA_EXHAUSTED';
                throw quota;
            }
            // unusable model (missing, deprecated): try the next candidate
            if (text.includes('5007') || text.includes('5028') || text.includes('No such model') || text.includes('deprecated')) continue;
            throw err;
        }
    }
    throw lastError || new Error('No model available');
}

async function handleGloss(request, env, cors) {
    let payload;
    try { payload = await request.json(); } catch (e) { return json({ error: 'Invalid JSON body' }, 400, cors); }
    const lang = payload && payload.lang;
    const word = payload && payload.word;
    if (!LANG_NAME[lang]) return json({ error: 'lang must be hu or es' }, 400, cors);
    if (!validWord(word)) return json({ error: 'word must be 2-40 letters' }, 400, cors);
    const sentence = cleanSentence(payload.sentence);

    const key = cacheKey(lang, word);
    if (env.GLOSS_CACHE) {
        const hit = await env.GLOSS_CACHE.get(key, 'json');
        if (hit) return json(Object.assign({ cached: true }, hit), 200, cors);
    }
    if (!env.AI) return json({ error: 'No AI binding on this worker' }, 503, cors);

    if (!(await underDailyCap(env))) {
        return json({ found: false, code: 'DAILY_CAP' }, 200, cors);
    }
    let answer;
    try {
        answer = await askModel(env, lang, word, sentence);
    } catch (err) {
        if (err && err.code === 'QUOTA_EXHAUSTED') {
            return json({ found: false, code: 'QUOTA_EXHAUSTED' }, 429, cors);
        }
        return json({ error: 'Workers AI inference failed', details: String(err) }, 500, cors);
    }
    if (env.GLOSS_CACHE && !answer.unreadable) {
        await env.GLOSS_CACHE.put(key, JSON.stringify(answer), answer.found ? undefined : { expirationTtl: NOT_FOUND_TTL });
    }
    delete answer.unreadable;
    return json(Object.assign({ cached: false }, answer), 200, cors);
}

async function handleExport(request, url, env, cors) {
    const auth = request.headers.get('Authorization') || '';
    if (!env.EXPORT_TOKEN || auth !== 'Bearer ' + env.EXPORT_TOKEN) {
        return json({ error: 'Unauthorized' }, 401, cors);
    }
    if (!env.GLOSS_CACHE) return json({ error: 'No cache bound' }, 503, cors);
    const lang = url.searchParams.get('lang');
    if (!LANG_NAME[lang]) return json({ error: 'lang must be hu or es' }, 400, cors);
    const prefix = 'v1:' + lang + ':';
    const page = await env.GLOSS_CACHE.list({ prefix: prefix, cursor: url.searchParams.get('cursor') || undefined, limit: 200 });
    const entries = [];
    for (const k of page.keys) {
        const value = await env.GLOSS_CACHE.get(k.name, 'json');
        if (value && value.found) {
            entries.push({ word: k.name.slice(prefix.length), lemma: value.lemma, pos: value.pos, gloss: value.gloss });
        }
    }
    return json({ entries: entries, cursor: page.list_complete ? null : page.cursor, complete: !!page.list_complete }, 200, cors);
}

export default {
    async fetch(request, env) {
        const origin = request.headers.get('Origin') || '';
        const cors = corsHeaders(origin);
        const url = new URL(request.url);

        if (request.method === 'OPTIONS') return new Response(null, { headers: cors });

        if (request.method === 'GET' && url.pathname === '/health') {
            return json({ status: 'ok', service: 'parlour-gloss', workersAiAvailable: !!(env && env.AI), cacheAvailable: !!(env && env.GLOSS_CACHE) }, 200, cors);
        }
        if (request.method === 'GET' && url.pathname === '/export') {
            return handleExport(request, url, env || {}, cors);
        }
        if (request.method !== 'POST' || url.pathname !== '/gloss') {
            return json({ error: 'Not found' }, 404, cors);
        }
        // Browsers always send Origin on a cross-origin POST; refusing anything else
        // keeps casual scripts from spending the AI allowance.
        if (!isAllowedOrigin(origin)) return json({ error: 'Origin not allowed' }, 403, cors);
        return handleGloss(request, env || {}, cors);
    }
};
