// Unit Test: Cloudflare word-gloss Worker (cloudflare-worker/gloss-worker.js)
// Verifies origin gating, input validation, the model call and reply parsing,
// KV caching (positive and negative), the daily cap, quota handling and /export.

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Testing Cloudflare gloss Worker ---');

const code = fs.readFileSync(path.join(__dirname, '../../cloudflare-worker/gloss-worker.js'), 'utf8')
    .replace('export default', 'module.exports =');
const m = { exports: {} };
new Function('module', 'exports', 'Response', code)(m, m.exports, global.Response);
const worker = m.exports;

const GOOD = 'https://parlour.me.uk';

function request(method, url, { origin = GOOD, body = null, auth = null } = {}) {
    const headers = {};
    if (origin) headers.origin = origin;
    if (auth) headers.authorization = auth;
    return {
        method, url,
        headers: { get: h => headers[h.toLowerCase()] || null },
        json: async () => { if (body === 'BAD') throw new Error('bad json'); return body; }
    };
}

function kv() {
    const store = new Map();
    const puts = [];
    return {
        store, puts,
        get: async (key, type) => {
            if (!store.has(key)) return null;
            return type === 'json' ? JSON.parse(store.get(key)) : store.get(key);
        },
        put: async (key, value, opts) => { store.set(key, value); puts.push({ key, opts }); },
        list: async ({ prefix }) => ({ keys: [...store.keys()].filter(k => k.startsWith(prefix)).map(name => ({ name })), list_complete: true })
    };
}

function env(replyText, extra = {}) {
    const calls = [];
    return Object.assign({
        calls,
        GLOSS_CACHE: kv(),
        AI: { run: async (model, input) => { calls.push({ model, input }); return { response: replyText }; } }
    }, extra);
}

const REPLY = '{"lemma":"elnyom","pos":"verb","gloss":"to oppress","confident":true}';
const body = (word, lang = 'hu') => ({ word, lang, sentence: 'A hatalom elnyomta a népet.' });

async function post(e, b, opts) {
    const res = await worker.fetch(request('POST', 'https://x.test/gloss', Object.assign({ body: b }, opts)), e);
    return { status: res.status, data: await res.json() };
}

(async () => {
    console.log('1. health, CORS preflight, routing');
    let res = await worker.fetch(request('GET', 'https://x.test/health'), env(REPLY));
    let data = await res.json();
    assert.strictEqual(data.service, 'parlour-gloss');
    assert.strictEqual(data.workersAiAvailable, true);
    res = await worker.fetch(request('OPTIONS', 'https://x.test/gloss', { origin: 'http://localhost:8131' }), env(REPLY));
    assert.strictEqual(res.headers.get('Access-Control-Allow-Origin'), 'http://localhost:8131');
    res = await worker.fetch(request('GET', 'https://x.test/nope'), env(REPLY));
    assert.strictEqual(res.status, 404);

    console.log('2. origin gating');
    let e = env(REPLY);
    assert.strictEqual((await post(e, body('elnyomta'), { origin: 'https://evil.example' })).status, 403);
    assert.strictEqual((await post(e, body('elnyomta'), { origin: '' })).status, 403);
    assert.strictEqual(e.calls.length, 0, 'a refused origin must not reach the model');
    assert.strictEqual((await post(e, body('elnyomta'), { origin: 'http://localhost:8131' })).status, 200);
    assert.strictEqual((await post(env(REPLY), body('elnyomta'), { origin: 'http://127.0.0.1:9999' })).status, 200);

    console.log('3. validation');
    e = env(REPLY);
    assert.strictEqual((await post(e, body('elnyomta', 'fr'))).status, 400);
    assert.strictEqual((await post(e, body('a'))).status, 400);
    assert.strictEqual((await post(e, body('x'.repeat(41)))).status, 400);
    assert.strictEqual((await post(e, body('el nyomta'))).status, 400);
    assert.strictEqual((await post(e, body('<script>'))).status, 400);
    assert.strictEqual((await post(e, 'BAD')).status, 400);
    assert.strictEqual(e.calls.length, 0);

    console.log('4. a model answer is returned and cached; the second tap never reaches the model');
    e = env(REPLY);
    let r = await post(e, body('elnyomta'));
    assert.strictEqual(r.status, 200);
    assert.deepStrictEqual([r.data.found, r.data.lemma, r.data.pos, r.data.gloss, r.data.cached], [true, 'elnyom', 'verb', 'to oppress', false]);
    assert.strictEqual(e.calls.length, 1);
    assert(e.calls[0].input.messages[1].content.includes('Hungarian'), 'prompt names the language');
    assert(e.calls[0].input.messages[1].content.includes('"elnyomta"'), 'prompt carries the word');
    assert(e.calls[0].input.messages[1].content.includes('A hatalom elnyomta a népet.'), 'prompt carries the sentence');
    assert.strictEqual(e.GLOSS_CACHE.puts.filter(p => p.key.startsWith('v1:hu:')).length, 1);
    r = await post(e, body('Elnyomta'));   // different capitalisation, same cache entry
    assert.strictEqual(r.data.cached, true);
    assert.strictEqual(e.calls.length, 1, 'cache hit must not call the model again');
    r = await post(e, body('elnyomta', 'es'));   // another language is another key
    assert.strictEqual(r.data.cached, false);

    console.log('5. sloppy replies: prose around the JSON, code fences, quotes and pipes in the gloss');
    r = await post(env('Sure! ```json\n{"lemma":"Öröm","pos":"Noun","gloss":"joy | \\"delight\\"","confident":true}\n```'), body('örömmel'));
    assert.deepStrictEqual([r.data.found, r.data.lemma, r.data.pos], [true, 'öröm', 'noun']);
    assert(!/["|]/.test(r.data.gloss), 'quotes and pipes are stripped from the gloss');

    console.log('6. unsure, invalid or off-list answers are "not found", and an unsure one is cached with a TTL');
    e = env('{"lemma":"x","pos":"verb","gloss":"","confident":false}');
    r = await post(e, body('bizonytalan'));
    assert.strictEqual(r.data.found, false);
    const negativePut = e.GLOSS_CACHE.puts.find(p => p.key === 'v1:hu:bizonytalan');
    assert(negativePut && negativePut.opts && negativePut.opts.expirationTtl > 0, 'negative answers expire');
    assert.strictEqual((await post(env('{"lemma":"x","pos":"widget","gloss":"thing","confident":true}'), body('valami'))).data.found, false);
    assert.strictEqual((await post(env('not json at all'), body('valami'))).data.found, false);
    assert.strictEqual((await post(env('{"lemma":"x","pos":"noun","gloss":"' + 'a'.repeat(120) + '","confident":true}'), body('valami'))).data.found, false);

    console.log('7. daily cap protects the free AI allowance');
    e = env(REPLY, { GLOSS_DAILY_CAP: '2' });
    await post(e, body('egyik'));
    await post(e, body('masik'));
    r = await post(e, body('harmadik'));
    assert.strictEqual(r.data.found, false);
    assert.strictEqual(r.data.code, 'DAILY_CAP');
    assert.strictEqual(e.calls.length, 2, 'no model call once the cap is reached');
    r = await post(e, body('egyik'));   // already cached: still served
    assert.strictEqual(r.data.found, true);

    console.log('8. quota errors and unusable models');
    e = env(REPLY);
    e.AI.run = async () => { throw new Error('429: daily quota exceeded'); };
    r = await post(e, body('elnyomta'));
    assert.strictEqual(r.status, 429);
    assert.strictEqual(r.data.code, 'QUOTA_EXHAUSTED');
    e = env(REPLY);
    const tried = [];
    e.AI.run = async model => { tried.push(model); if (tried.length === 1) throw new Error('5028 deprecated'); return { response: REPLY }; };
    r = await post(e, body('elnyomta'));
    assert.strictEqual(r.data.found, true);
    assert.strictEqual(tried.length, 2, 'a deprecated model falls through to the next candidate');
    e = env(REPLY);
    delete e.AI;
    assert.strictEqual((await post(e, body('elnyomta'))).status, 503);

    console.log('9. works without a cache binding');
    e = env(REPLY);
    delete e.GLOSS_CACHE;
    assert.strictEqual((await post(e, body('elnyomta'))).data.found, true);

    console.log('10. /export needs the token and returns only real answers');
    e = env(REPLY, { EXPORT_TOKEN: 'secret' });
    await post(e, body('elnyomta'));
    await post(env('{"lemma":"","pos":"noun","gloss":"","confident":false}'), body('semmi'));
    e.GLOSS_CACHE.store.set('v1:hu:semmi', JSON.stringify({ found: false }));
    const exp = (auth) => worker.fetch(request('GET', 'https://x.test/export?lang=hu', { auth }), e);
    assert.strictEqual((await exp(null)).status, 401);
    assert.strictEqual((await exp('Bearer wrong')).status, 401);
    const ok = await (await exp('Bearer secret')).json();
    assert.strictEqual(ok.complete, true);
    assert.deepStrictEqual(ok.entries.map(x => x.word), ['elnyomta']);
    assert.strictEqual(ok.entries[0].lemma, 'elnyom');
    assert.strictEqual((await worker.fetch(request('GET', 'https://x.test/export?lang=hu', { auth: 'Bearer secret' }), env(REPLY))).status, 401, 'no EXPORT_TOKEN configured means no export');

    console.log('\nALL GLOSS WORKER TESTS PASSED');
})().catch(err => { console.error('FAILED:', err); process.exit(1); });
