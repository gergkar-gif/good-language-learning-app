/**
 * tests/test-browser-nonlesson-smoke.js
 * Headless Chromium (CDP) end-to-end smoke check across fr, it, pl, cs, sk:
 * Home, Library + story reader + word lookup popup, Decks, Journey,
 * and Workshop (Grammar Studio, Verbs Table & Speed, Listening/Music/Video,
 * Writing, Speaking, CEFR B1 Exam Prep).
 */
'use strict';

const assert = require('assert');
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const os = require('os');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const MIME = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.woff2': 'font/woff2',
    '.webp': 'image/webp',
    '.ico': 'image/x-icon'
};

const LANG_CONFIGS = [
    { lang: 'fr', studio: 'fr-grammar-studio', exam: 'fr-delf-exam' },
    { lang: 'it', studio: 'it-grammar-studio', exam: 'it-cils-exam' },
    { lang: 'pl', studio: 'pl-grammar-studio', exam: 'pl-certyfikat-b1-exam' },
    { lang: 'cs', studio: 'cs-grammar-studio', exam: 'cs-cce-b1-exam' },
    { lang: 'sk', studio: 'sk-grammar-studio', exam: 'sk-ecl-b1-exam' }
];

function findBrowser() {
    const candidates = [
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    ];
    for (const p of candidates) {
        if (fs.existsSync(p)) return p;
    }
    throw new Error('No headless Chrome or Edge binary found');
}

function startStaticServer() {
    return new Promise((resolve, reject) => {
        const server = http.createServer((req, res) => {
            const urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
            const rel = urlPath === '/' ? 'index.html' : urlPath.replace(/^\/+/, '');
            const fp = path.resolve(ROOT, rel);
            if (!fp.startsWith(ROOT)) {
                res.writeHead(403);
                res.end('Forbidden');
                return;
            }
            fs.stat(fp, (err, st) => {
                if (err || !st.isFile()) {
                    res.writeHead(404);
                    res.end('Not found');
                    return;
                }
                const ext = path.extname(fp).toLowerCase();
                res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
                fs.createReadStream(fp).pipe(res);
            });
        });
        server.on('error', reject);
        server.listen(0, '127.0.0.1', () => resolve({ server, port: server.address().port }));
    });
}

class CDPClient {
    constructor(wsUrl) {
        this.ws = new WebSocket(wsUrl);
        this.nextId = 1;
        this.pending = new Map();
        this.events = [];
        this.ready = new Promise((res, rej) => {
            this.ws.addEventListener('open', res, { once: true });
            this.ws.addEventListener('error', rej, { once: true });
        });
        this.ws.addEventListener('message', (ev) => {
            const msg = JSON.parse(ev.data);
            if (msg.id) {
                const p = this.pending.get(msg.id);
                if (p) {
                    this.pending.delete(msg.id);
                    if (msg.error) p.rej(new Error(msg.error.message || JSON.stringify(msg.error)));
                    else p.res(msg.result);
                }
            } else if (msg.method) {
                for (const fn of this.events) fn(msg.method, msg.params);
            }
        });
    }
    async connect() {
        await this.ready;
    }
    onEvent(fn) {
        this.events.push(fn);
    }
    send(method, params = {}) {
        const id = this.nextId++;
        return new Promise((res, rej) => {
            this.pending.set(id, { res, rej });
            this.ws.send(JSON.stringify({ id, method, params }));
        });
    }
    async eval(expression) {
        const res = await this.send('Runtime.evaluate', {
            expression: `(async () => { ${expression} })()`,
            awaitPromise: true,
            returnByValue: true
        });
        if (res.exceptionDetails) {
            throw new Error(res.exceptionDetails.exception?.description || res.exceptionDetails.text || 'JS eval failed');
        }
        return res.result ? res.result.value : undefined;
    }
    async waitFor(fnExpr, timeoutMs = 12000) {
        const deadline = Date.now() + timeoutMs;
        while (Date.now() < deadline) {
            const val = await this.eval(`return (${fnExpr});`);
            if (val) return val;
            await new Promise(r => setTimeout(r, 120));
        }
        throw new Error(`Timeout waiting for: ${fnExpr}`);
    }
    close() {
        try { this.ws.close(); } catch (_) {}
    }
}

async function launchBrowser() {
    const exe = findBrowser();
    const userDataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'parlour-cdp-'));
    const proc = spawn(exe, [
        '--headless=new',
        '--disable-gpu',
        '--no-first-run',
        '--no-default-browser-check',
        '--remote-debugging-port=0',
        `--user-data-dir=${userDataDir}`,
        'about:blank'
    ], { stdio: ['ignore', 'ignore', 'pipe'] });

    const wsUrl = await new Promise((resolve, reject) => {
        let stderr = '';
        const timer = setTimeout(() => reject(new Error('Browser launch timeout: ' + stderr)), 15000);
        proc.stderr.on('data', (chunk) => {
            stderr += chunk.toString();
            const m = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/);
            if (m) {
                clearTimeout(timer);
                resolve(m[1]);
            }
        });
        proc.once('exit', (code) => {
            clearTimeout(timer);
            reject(new Error(`Browser exited early (${code}): ${stderr}`));
        });
    });

    const u = new URL(wsUrl);
    const listResp = await fetch(`http://${u.host}/json/list`);
    const targets = await listResp.json();
    const pageTarget = targets.find(t => t.type === 'page') || targets[0];
    return {
        proc,
        userDataDir,
        pageWsUrl: pageTarget.webSocketDebuggerUrl
    };
}

async function main() {
    const { server, port } = await startStaticServer();
    const baseUrl = `http://127.0.0.1:${port}`;
    const browser = await launchBrowser();
    const cdp = new CDPClient(browser.pageWsUrl);
    await cdp.connect();

    const errors = [];
    let activeLang = 'init';
    cdp.onEvent((method, params) => {
        if (method === 'Runtime.exceptionThrown') {
            const det = params.exceptionDetails || {};
            errors.push(`[${activeLang}] JS Exception: ${det.exception?.description || det.text}`);
        } else if (method === 'Runtime.consoleAPICalled' && params.type === 'error') {
            const msg = (params.args || []).map(a => a.value || a.description || '').join(' ');
            // Ignore third-party YouTube/external network blocks if offline, catch all app/same-origin errors
            if (!msg.includes('youtube.com') && !msg.includes('ERR_NAME_NOT_RESOLVED')) {
                errors.push(`[${activeLang}] console.error: ${msg}`);
            }
        } else if (method === 'Network.responseReceived') {
            const resp = params.response || {};
            if (resp.url && resp.url.startsWith(baseUrl) && resp.status >= 400 && !resp.url.endsWith('/favicon.ico')) {
                // Intentional graceful probes for unauthored level tests or pre-lesson skill files
                const isExpectedOptionalProbe =
                    /\/content\/[^/]+\/tests\/(?:a1|a2|b1|b2|c1|diagnostic)-test\.json$/.test(resp.url) ||
                    /\/content\/(?:pl|cs|sk)\/indexes\/(?:skill-registry|grammar-titles)\.json$/.test(resp.url);
                if (!isExpectedOptionalProbe) {
                    errors.push(`[${activeLang}] HTTP ${resp.status} for ${resp.url}`);
                }
            }
        }
    });

    await cdp.send('Page.enable');
    await cdp.send('Runtime.enable');
    await cdp.send('Network.enable');

    try {
        for (const cfg of LANG_CONFIGS) {
            const { lang, studio, exam } = cfg;
            activeLang = lang;

            // Load origin cleanly, seed localStorage for this course, then reload
            await cdp.send('Page.navigate', { url: `${baseUrl}/` });
            await cdp.waitFor(`typeof Lang !== 'undefined' && document.readyState === 'complete'`);
            await cdp.eval(`
                localStorage.clear();
                localStorage.setItem('app_language', ${JSON.stringify(lang)});
                localStorage.setItem('parlour_first_open_completed', 'true');
                localStorage.setItem('${lang}:diagnosticOnboardingDismissed', 'true');
            `);
            await cdp.send('Page.reload', { ignoreCache: true });

            await cdp.waitFor(`
                typeof Lang !== 'undefined' &&
                Lang.code() === ${JSON.stringify(lang)} &&
                document.getElementById('home') &&
                document.getElementById('home').innerText.trim().length > 40 &&
                (!document.getElementById('boot-screen') || document.getElementById('boot-screen').classList.contains('is-hidden'))
            `, 15000);

            // 1. Library + story + word lookup popup
            await cdp.eval(`showTab('reader');`);
            await cdp.waitFor(`document.querySelectorAll('#reader .story-card[data-story-id]').length > 0`, 10000);
            await cdp.eval(`document.querySelector('#reader .story-card[data-story-id]').click();`);
            await cdp.waitFor(`document.querySelectorAll('#reader .word[data-word]').length > 3`, 10000);
            await cdp.eval(`
                const words = Array.from(document.querySelectorAll('#reader .word[data-word]'));
                const target = words.find(w => (w.getAttribute('data-word') || '').length >= 4) || words[0];
                target.click();
            `);
            await cdp.waitFor(`(() => {
                const p = document.getElementById('word-popup');
                const b = document.getElementById('popup-body');
                return !!(p && p.style.display === 'block' && b && !b.textContent.includes('Loading dictionary') && b.textContent.trim().length > 0);
            })()`, 15000);
            const lookupText = await cdp.eval(`
                const t = document.getElementById('popup-body').innerText.trim();
                closePopup();
                return t;
            `);
            assert(!lookupText.includes('undefined'), `[${lang}] Word popup contains 'undefined': ${lookupText}`);

            // 2. Decks
            await cdp.eval(`showTab('review');`);
            await cdp.waitFor(`document.getElementById('review') && document.getElementById('review').innerText.trim().length > 20`, 10000);

            // 3. Journey (verify renders & keeps non-lesson course picker gated)
            await cdp.eval(`showTab('journey');`);
            await cdp.waitFor(`document.getElementById('journey') && document.getElementById('journey').innerText.trim().length > 20`, 10000);
            const avail = await cdp.eval(`return Lang.available();`);
            assert.deepStrictEqual(avail, ['es-latam', 'es-es', 'hu'], 'Lang.available() must stay gated');

            // 4. Workshop: Grammar Studio, Verbs (Table + Speed), Listening (+ Music/Video tabs), Writing, Speaking, CEFR B1 Exam
            await cdp.eval(`showTab('drills');`);
            await cdp.waitFor(`document.querySelectorAll('#drills [data-driller]').length >= 5`, 10000);
            const cardIds = await cdp.eval(`return Array.from(document.querySelectorAll('#drills [data-driller]')).map(el => el.dataset.driller);`);
            assert(cardIds.includes(studio), `[${lang}] Missing card ${studio} in ${cardIds}`);
            assert(cardIds.includes('verbs'), `[${lang}] Missing card verbs`);
            assert(cardIds.includes('listening'), `[${lang}] Missing card listening`);
            assert(cardIds.includes('writing'), `[${lang}] Missing card writing`);
            assert(cardIds.includes('speaking'), `[${lang}] Missing card speaking`);

            await cdp.eval(`document.querySelector('#drills [data-wk-tab="exams"]').click();`);
            await cdp.waitFor(`document.querySelector('#drills [data-driller="' + ${JSON.stringify(exam)} + '"]') !== null`, 5000);
            await cdp.eval(`document.querySelector('#drills [data-wk-tab="practice"]').click();`);

            // 4a. Grammar Studio
            await cdp.eval(`Workshop.open(${JSON.stringify(studio)});`);
            await cdp.waitFor(`document.getElementById(${JSON.stringify(studio + '-root')}).innerText.trim().length > 40`, 10000);
            await cdp.eval(`Workshop.close();`);

            // 4b. Verbs (Table + Speed)
            await cdp.eval(`Workshop.open('verbs');`);
            await cdp.waitFor(`document.querySelectorAll('#verb-driller-root .vtable-input').length >= 3`, 10000);
            await cdp.eval(`document.querySelector('#verb-driller-root [data-action="switch-mode"][data-mode="speed"]').click();`);
            await cdp.waitFor(`document.querySelector('#verb-driller-root [data-action="start"]') !== null`, 5000);
            await cdp.eval(`document.querySelector('#verb-driller-root [data-action="start"]').click();`);
            await cdp.waitFor(`document.querySelector('#verb-driller-root .vspeed-verb') !== null`, 10000);
            const speedText = await cdp.eval(`return document.getElementById('verb-driller-root').innerText;`);
            assert(!speedText.includes('No questions available'), `[${lang}] VerbsSpeed hit No questions available`);
            await cdp.eval(`Workshop.close();`);

            // 4c. Listening Studio (Tasks + Music + Video subtabs)
            await cdp.eval(`Workshop.open('listening');`);
            await cdp.waitFor(`document.getElementById('listening-studio-root').innerText.trim().length > 40`, 10000);
            const subTabClick = await cdp.eval(`
                const btns = Array.from(document.querySelectorAll('#listening-studio-root button, #listening-studio-root [role="tab"]'));
                const results = [];
                for (const kw of ['Song', 'Music', 'Video']) {
                    const b = btns.find(x => x.textContent.includes(kw));
                    if (b) { b.click(); results.push(kw); }
                }
                return results;
            `);
            assert(subTabClick.length >= 1, `[${lang}] Expected Listening Studio Music/Video tabs`);
            await cdp.eval(`Workshop.close();`);

            // 4d. Writing & Speaking
            await cdp.eval(`Workshop.open('writing');`);
            await cdp.waitFor(`document.getElementById('writing-driller-root').innerText.trim().length > 40`, 10000);
            await cdp.eval(`Workshop.close();`);

            await cdp.eval(`Workshop.open('speaking');`);
            await cdp.waitFor(`document.getElementById('speaking-driller-root').innerText.trim().length > 40`, 10000);
            await cdp.eval(`Workshop.close();`);

            // 4e. CEFR B1 Exam Prep
            await cdp.eval(`Workshop.open(${JSON.stringify(exam)});`);
            await cdp.waitFor(`(() => {
                const el = document.querySelector('#drills-root .tab-panel:not(.hidden), [id$="-exam-root"]');
                return !!(el && el.innerText.trim().length > 60);
            })()`, 10000);
            const examText = await cdp.eval(`
                const roots = Array.from(document.querySelectorAll('[id$="-exam-root"]'));
                const active = roots.find(r => r.innerText.trim().length > 0);
                return active ? active.innerText : '';
            `);
            assert(examText.length > 60 && !examText.includes('undefined'), `[${lang}] CEFR exam rendered badly`);
            await cdp.eval(`Workshop.close();`);

            console.log(`[PASS] Browser smoke check passed for ${lang}: Home, Library+Lookup, Decks, Journey, Grammar Studio, Verbs Table/Speed, Listening/Music/Video, Writing, Speaking, ${exam}.`);
        }

        assert.strictEqual(errors.length, 0, `Runtime/Network errors detected:\n${errors.join('\n')}`);
        console.log('[PASS] All 5 non-lesson languages verified cleanly in live headless Chromium.');
    } finally {
        cdp.close();
        try { browser.proc.kill(); } catch (_) {}
        server.close();
        await new Promise(r => setTimeout(r, 300));
        try { fs.rmSync(browser.userDataDir, { recursive: true, force: true }); } catch (_) {}
    }
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
