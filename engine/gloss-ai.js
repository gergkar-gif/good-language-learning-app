// ============================================
// GLOSS AI — machine-suggested gloss for words the dictionary lacks
// ============================================
// The Reader's last resort. When a tapped word has no dictionary entry, no
// morphological reading and isn't a name, this asks the gloss-worker
// Cloudflare Worker (cloudflare-worker/gloss-worker.js) for the base form and
// a short English gloss, so the learner isn't left with nothing. The answer is
// labelled a machine suggestion in the popup and is never saved to a deck.
//
// Everything here fails quietly: no network, a slow worker or a refusal all
// resolve to null and the Reader keeps showing "Not in the dictionary yet".
// Answers are remembered in this browser (localStorage), so tapping the same
// word again is instant and costs nothing. Setup: docs/SERVICES.md.

const GlossAI = (function () {
    'use strict';

    const DEFAULT_ENDPOINT = 'https://gloss-worker.gergkar.workers.dev/gloss';
    const ENDPOINT_KEY = 'parlour_gloss_endpoint';   // 'none' or 'disabled' switches the feature off
    const CACHE_PREFIX = 'glossAi:';
    const TIMEOUT_MS = 8000;
    const NOT_FOUND_DAYS = 7;
    const memory = new Map();

    function endpoint() {
        try {
            const stored = localStorage.getItem(ENDPOINT_KEY);
            if (stored === 'none' || stored === 'disabled') return null;
            return stored || DEFAULT_ENDPOINT;
        } catch (e) {
            return DEFAULT_ENDPOINT;
        }
    }

    function available() {
        return !!endpoint() && typeof fetch === 'function';
    }

    // 'es-latam' and 'es-es' share one dictionary and one worker language.
    function workerLang(courseCode) {
        const code = String(courseCode || (typeof Lang !== 'undefined' ? Lang.code() : 'es')).toLowerCase();
        return code.split('-')[0];
    }

    function readStored(key) {
        try {
            const raw = localStorage.getItem(CACHE_PREFIX + key);
            if (!raw) return null;
            const entry = JSON.parse(raw);
            if (entry && entry.found === false && Date.now() - (entry.at || 0) > NOT_FOUND_DAYS * 86400000) return null;
            return entry;
        } catch (e) {
            return null;
        }
    }

    function writeStored(key, entry) {
        try {
            localStorage.setItem(CACHE_PREFIX + key, JSON.stringify(Object.assign({ at: Date.now() }, entry)));
        } catch (e) { /* storage full or blocked: the answer just isn't remembered */ }
    }

    // -> { found: true, lemma, pos, gloss } | { found: false } | null (unavailable)
    async function lookup(word, sentence, courseCode) {
        const url = endpoint();
        const w = String(word || '').toLowerCase().trim();
        if (!url || !w) return null;
        const lang = workerLang(courseCode);
        const key = lang + ':' + w;

        if (memory.has(key)) return memory.get(key);
        const stored = readStored(key);
        if (stored) { memory.set(key, stored); return stored; }

        const controller = typeof AbortController === 'function' ? new AbortController() : null;
        const timer = controller ? setTimeout(() => controller.abort(), TIMEOUT_MS) : null;
        try {
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ word: w, sentence: String(sentence || '').slice(0, 300), lang: lang }),
                signal: controller ? controller.signal : undefined
            });
            if (!res.ok) return null;
            const data = await res.json();
            const answer = data && data.found
                ? { found: true, lemma: data.lemma, pos: data.pos, gloss: data.gloss }
                : { found: false };
            if (data && (data.found || !data.code)) {   // don't remember a "daily cap" refusal as "no answer"
                memory.set(key, answer);
                writeStored(key, answer);
            }
            return answer;
        } catch (e) {
            return null;
        } finally {
            if (timer) clearTimeout(timer);
        }
    }

    return { lookup: lookup, available: available, _workerLang: workerLang };
})();

if (typeof window !== 'undefined') window.GlossAI = GlossAI;
