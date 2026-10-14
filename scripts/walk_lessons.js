#!/usr/bin/env node
// Gate-1 lesson walk test (ROADMAP 153(b)).
//
//   node scripts/walk_lessons.js <course> <level> [--base http://127.0.0.1:8131]
//                                [--only <stem>...] [--out report.json]
//                                [--jobs 4] [--live-tts]
//
//   python scripts/dev-server.py 8131 &        # serve the worktree first
//   node scripts/walk_lessons.js hu a1 --out /tmp/walk-hu-a1.json
//
// Opens every lesson of a course level (stems from
// content/<course>/curriculum/units/<level>.json) in headless Chromium, plays
// it to the summary screen answering correctly, and reports per lesson:
//   - console errors and uncaught page errors / unhandled rejections
//   - failed requests (4xx/5xx, network failure) on the app's own origin
//   - answer audio: failed audio files, failed/malformed TTS synth calls,
//     media element errors, play() rejections (speechSynthesis use is counted)
//   - the lesson not reaching its summary (step index, type, what was on screen)
// Exit code 1 if any lesson fails. Needs Node Playwright (require('playwright')).
//
// How it works
//   * Each lesson gets a fresh browser context (empty localStorage, so no
//     resume prompt, XP or progress leaks between lessons). The course is
//     chosen with the app's own ?lang=<course> deep link. The first-open
//     welcome dialog is skipped by setting the localStorage flag the app
//     itself writes (parlour_first_open_completed); the Sync backup invite
//     only shows once progress exists and Guide notes are non-blocking.
//   * The lesson is opened by calling startLesson('<level>.<n>') (the same
//     function the Lessons tab / Home continue card call), then the UI is
//     driven with real clicks and typing. The correct answer is read from the
//     engine's own stepState (it holds the shuffled option index, accepted
//     answers, tile solution), so shuffling does not matter.
//   * Speaking and communicative-challenge steps need a microphone: they use
//     the app's "Can't speak right now" button (which also snoozes later mic
//     steps) and are reported as "skipped: speaking" / "skipped: challenge".
//   * ParlourTTS posts to a cloud worker. By default that endpoint and all
//     other third-party hosts are stubbed (silent WAV / 204) so the run is
//     offline and deterministic; the TTS request count is reported. With
//     --live-tts the worker is called for real and a non-200 or a reply
//     without audioContent counts as an audio failure. Third-party hosts are
//     never counted as failures.
//   * "Failed to load resource" console lines are not listed as console
//     errors; the same failure is reported under failed requests with its URL.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');

// Files the engine probes on purpose and tolerates missing. None for now:
// engine/learnerModel.js no longer requests files a course is known not to
// have (its ABSENT list), so every 404 fails the lesson (gate 1: no failed
// requests). Add a pattern here only for a probe that can't be avoided.
const OPTIONAL_PROBES = [];

function parseArgs(argv) {
    const o = { base: 'http://127.0.0.1:8131', only: [], out: null, jobs: 4, liveTts: false, pos: [] };
    for (let i = 0; i < argv.length; i++) {
        const a = argv[i];
        if (a === '--base') o.base = argv[++i];
        else if (a === '--out') o.out = argv[++i];
        else if (a === '--jobs') o.jobs = Number(argv[++i]) || 1;
        else if (a === '--live-tts') o.liveTts = true;
        else if (a === '--only') { while (argv[i + 1] && !argv[i + 1].startsWith('--')) o.only.push(argv[++i]); }
        else o.pos.push(a);
    }
    return o;
}

// 0.05s of 8-bit mono silence, so the app's audio decoder has real audio.
function silentWavB64() {
    const n = 400, rate = 8000, buf = Buffer.alloc(44 + n, 128);
    buf.write('RIFF', 0); buf.writeUInt32LE(36 + n, 4); buf.write('WAVEfmt ', 8);
    buf.writeUInt32LE(16, 16); buf.writeUInt16LE(1, 20); buf.writeUInt16LE(1, 22);
    buf.writeUInt32LE(rate, 24); buf.writeUInt32LE(rate, 28); buf.writeUInt16LE(1, 32);
    buf.writeUInt16LE(8, 34); buf.write('data', 36); buf.writeUInt32LE(n, 40);
    return buf.toString('base64');
}

// Runs in every page before the app: records audio trouble.
const INIT = () => {
    window.__walk = { ttsSpeak: 0, media: [], playRejects: [], pageErrors: [] };
    document.addEventListener('error', e => {
        const t = e.target;
        if (t && (t.tagName === 'AUDIO' || t.tagName === 'VIDEO')) window.__walk.media.push((t.currentSrc || t.src || '').slice(0, 120));
    }, true);
    const play = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function () {
        const p = play.apply(this, arguments);
        if (p && p.catch) p.catch(err => window.__walk.playRejects.push(String(err && err.name || err)));
        return p;
    };
    if (window.speechSynthesis) {
        const speak = window.speechSynthesis.speak.bind(window.speechSynthesis);
        window.speechSynthesis.speak = u => { window.__walk.ttsSpeak++; return speak(u); };
    }
};

const sleep = ms => new Promise(r => setTimeout(r, ms));

// Snapshot of the lesson engine state (globals declared by engine/lessons.js).
const STATE = () => {
    /* eslint-disable no-undef */
    const content = document.getElementById('lesson-content');
    const btn = document.getElementById('lesson-next-btn');
    const step = (typeof stepState !== 'undefined' && stepState) ? stepState.sourceStep : null;
    return {
        index: typeof currentStepIndex === 'number' ? currentStepIndex : -1,
        total: (typeof currentLesson !== 'undefined' && currentLesson && currentLesson.steps) ? currentLesson.steps.length : 0,
        type: step ? step.type : null,
        id: step ? (step.id || null) : null,
        summary: !!(content && content.querySelector('.lsn-summary')) && !content.querySelector('.lsn-finishing'),
        fallbackSummary: !!(content && content.querySelector('.lsn-summary-title') && /Congratulations!/.test(content.textContent) && !content.querySelector('.lsn-summary-stats, .lsn-summary-words, .lsn-summary-goals')),
        gated: !!stepState.gated, solved: !!stepState.solved, gaveUp: !!stepState.gaveUp, attempts: stepState.attempts || 0,
        btnText: btn ? btn.textContent.trim() : null, btnDisabled: btn ? btn.disabled : null,
        screen: content ? content.innerText.replace(/\s+/g, ' ').trim().slice(0, 200) : '',
    };
};

// What the step needs to be answered correctly, read from stepState.
const PLAN = () => {
    /* eslint-disable no-undef */
    const s = stepState, type = s.sourceStep && s.sourceStep.type;
    const p = { type };
    if (s.checkFn === 'lessonCheckChoice') p.correct = Array.isArray(s.correct) ? s.correct[0] : s.correct;
    if (s.checkFn === 'lessonCheckBlank') p.answer = (s.acceptable && s.acceptable[0]) || s.answer;
    if (type === 'sentence-builder') p.solution = s.solution, p.tiles = s.tiles.map(t => t.text);
    if (type === 'sentence-order') p.order = s.solution;
    if (type === 'matching') p.pairs = (s.pairs || []).length;
    if (type === 'structured-writing') p.composition = !!s.isComposition, p.minWords = s.minWords || 6;
    if (type === 'substitution') p.options = (s.options || []).length;
    return p;
};

async function walkLesson(browser, opts, stem) {
    const res = { stem, ok: true, reasons: [], steps: 0, skipped: [], consoleErrors: [], pageErrors: [], failedRequests: [], audio: [], notes: [], tts: { requests: 0, speechSynthesis: 0 }, stuck: null };
    const fail = r => { res.ok = false; res.reasons.push(r); };
    const origin = new URL(opts.base).origin;
    const ctx = await browser.newContext({ viewport: { width: 420, height: 900 }, serviceWorkers: 'block' });
    const page = await ctx.newPage();
    await page.addInitScript(INIT);
    // First-open welcome dialog (engine/home.js showWelcome) covers the whole
    // app until a starting point is chosen; the app skips it when this flag
    // is set, which is what hideWelcome() writes after a learner picks one.
    await page.addInitScript(() => { try { localStorage.setItem('parlour_first_open_completed', 'true'); } catch (e) {} });

    const wav = silentWavB64();
    await ctx.route(url => new URL(url).origin !== origin, async route => {
        const url = route.request().url();
        if (/\/synthesize(\?|$)/.test(url)) {
            res.tts.requests++;
            if (opts.liveTts) {
                try {
                    const r = await route.fetch();
                    let ok = r.status() === 200;
                    if (ok) { try { ok = !!(await r.json()).audioContent; } catch (e) { ok = false; } }
                    if (!ok) res.audio.push(`TTS synth ${r.status()} ${url}`);
                    return route.fulfill({ response: r });
                } catch (e) { res.audio.push(`TTS synth network failure ${url}: ${e.message}`); return route.abort(); }
            }
            if (route.request().method() === 'OPTIONS') return route.fulfill({ status: 204, headers: { 'access-control-allow-origin': '*', 'access-control-allow-headers': '*' } });
            return route.fulfill({ status: 200, contentType: 'application/json', headers: { 'access-control-allow-origin': '*' }, body: JSON.stringify({ audioContent: wav }) });
        }
        res.notes.includes('external stubbed') || res.notes.push('external stubbed');
        return route.fulfill({ status: 204, headers: { 'access-control-allow-origin': '*' }, body: '' });
    });

    page.on('console', m => {
        if (m.type() !== 'error') return;
        const t = m.text();
        if (/^Failed to load resource/.test(t)) return; // reported under failedRequests
        res.consoleErrors.push(t.slice(0, 300));
    });
    page.on('pageerror', e => res.pageErrors.push(String(e && e.message || e).slice(0, 300)));
    page.on('response', r => {
        const u = r.url();
        if (new URL(u).origin !== origin || r.status() < 400) return;
        const line = `${r.status()} ${u}`;
        if (OPTIONAL_PROBES.some(re => re.test(new URL(u).pathname))) { res.notes.push('optional probe missing: ' + line); return; }
        res.failedRequests.push(line);
        if (/\.(mp3|wav|ogg|m4a|webm|aac)(\?|$)/i.test(u)) res.audio.push('audio file ' + line);
    });
    page.on('requestfailed', r => {
        const u = r.url();
        if (new URL(u).origin !== origin) return;
        const line = `FAILED ${u} (${r.failure() && r.failure().errorText})`;
        if (/net::ERR_ABORTED/.test(line) && /\.(mp3|wav)/.test(u) === false) return; // navigation/teardown aborts
        res.failedRequests.push(line);
        if (/\.(mp3|wav|ogg|m4a|webm|aac)(\?|$)/i.test(u)) res.audio.push('audio file ' + line);
    });

    const click = sel => page.locator(sel).first().click({ timeout: 4000 });
    const footer = () => page.locator('#lesson-next-btn');

    try {
        await page.goto(`${opts.base}/index.html?lang=${opts.course}`, { waitUntil: 'load' });
        await page.waitForFunction(() => typeof startLesson === 'function' && !document.getElementById('boot-screen'), null, { timeout: 15000 });
        const lessonId = stem.replace('-', '.');
        await page.evaluate(id => startLesson(id), lessonId);
        await page.waitForSelector('#lesson-screen:not(.hidden) #lesson-content > *', { timeout: 10000 });
        // Resume prompt cannot appear in a fresh context; if it ever does, start over.
        const guard = 400;
        let finishWaits = 0;
        for (let n = 0; n < guard; n++) {
            const st = await page.evaluate(STATE);
            if (st.summary) { if (st.fallbackSummary) fail('summary fell back to the minimal "Congratulations!" screen'); break; }
            if (st.index >= st.total) {
                // Past the last step: finishLesson() is building the summary.
                await page.waitForFunction(() => { const c = document.getElementById('lesson-content'); return c && c.querySelector('.lsn-summary') && !c.querySelector('.lsn-finishing'); }, null, { timeout: 15000 }).catch(() => {});
                if (++finishWaits > 1) { res.stuck = { index: st.index, type: st.type, id: st.id, why: 'summary never appeared after the last step', screen: st.screen }; fail(`summary never appeared after the last step (screen: "${st.screen}")`); break; }
                continue;
            }
            const plan = await page.evaluate(PLAN);
            const tok = await page.evaluateHandle(() => stepState);
            const here = `step ${st.index + 1}/${st.total} ${st.type}${st.id ? ' ' + st.id : ''}`;
            const stuck = why => { res.stuck = { index: st.index, type: st.type, id: st.id, why, screen: st.screen }; fail(`stuck at ${here}: ${why}`); };
            if (st.type === null && !st.summary) {
                // finishing spinner, or nothing rendered
                await sleep(150);
                const again = await page.evaluate(STATE);
                if (again.summary) continue;
                if (n > 5 && again.type === null) { stuck('no step rendered'); break; }
                continue;
            }
            res.steps++; res.total = st.total;
            let advanced = false;
            try {
                if (plan.correct !== undefined) {
                    await page.locator('#lesson-content .lsn-option').nth(plan.correct).click({ timeout: 4000 });
                    await footer().click({ timeout: 4000 });
                } else if (plan.answer !== undefined) {
                    await page.locator('#blank-input').fill(String(plan.answer), { timeout: 4000 });
                    await footer().click({ timeout: 4000 });
                } else if (plan.type === 'matching') {
                    for (let i = 0; i < plan.pairs; i++) {
                        await page.locator(`.lsn-match [data-side="left"][data-index="${i}"]`).click({ timeout: 4000 });
                        await page.locator(`.lsn-match [data-side="right"][data-index="${i}"]`).click({ timeout: 4000 });
                    }
                } else if (plan.type === 'sentence-builder') {
                    const used = new Set();
                    for (const word of plan.solution) {
                        const k = plan.tiles.findIndex((t, i) => t === word && !used.has(i));
                        if (k < 0) throw new Error(`no tile "${word}" for solution ${JSON.stringify(plan.solution)} in tiles ${JSON.stringify(plan.tiles)}`);
                        used.add(k);
                        await page.locator('#build-bank .lsn-tile').nth(k).click({ timeout: 4000 });
                    }
                    await footer().click({ timeout: 4000 });
                } else if (plan.type === 'sentence-order') {
                    for (const idx of plan.order) await page.locator(`#lesson-content .lsn-option[data-index="${idx}"]`).click({ timeout: 4000 });
                    await footer().click({ timeout: 4000 });
                } else if (plan.type === 'structured-writing') {
                    const text = Array.from({ length: Math.max(plan.minWords, 6) }, () => 'szia').join(' ');
                    if (plan.composition) await page.locator('[data-write-composition]').fill(text, { timeout: 4000 });
                    else {
                        const n2 = await page.locator('[data-write]').count();
                        for (let i = 0; i < n2; i++) await page.locator('[data-write]').nth(i).fill(text, { timeout: 4000 });
                    }
                    await footer().click({ timeout: 4000 });
                } else if (plan.type === 'substitution') {
                    for (let i = 0; i < plan.options; i++) await page.locator(`[data-sub-index="${i}"]`).click({ timeout: 4000 });
                } else if (plan.type === 'speaking' || plan.type === 'challenge') {
                    // Needs a microphone: use the app's own skip path.
                    await page.locator('.sp-cant-speak-btn').click({ timeout: 4000 });
                    res.skipped.push(plan.type);
                    advanced = true;
                } else if (st.gated && !st.solved) {
                    stuck(`unknown gated step type "${st.type}" with no driver`);
                    break;
                }
            } catch (e) {
                stuck('could not drive step: ' + String(e.message).split('\n')[0]);
                break;
            }
            if (!advanced) {
                // Gated steps are now solved: check it was accepted, then Continue.
                const after = await page.evaluate(STATE);
                if (after.gated && !after.solved) { stuck(`answer not accepted (button "${after.btnText}", attempts ${after.attempts})`); break; }
                if (after.gated && after.gaveUp) { fail(`correct answer rejected at ${here} (attempts ${after.attempts}, gave up)`); }
                else if (after.gated && after.attempts > 0) res.notes.push(`${here}: needed ${after.attempts + 1} attempts`);
                const dis = await footer().isDisabled();
                if (dis) { stuck(`Continue disabled (button "${after.btnText}")`); break; }
                await footer().click({ timeout: 4000 });
            }
            // Wait for the engine to move on (new stepState, or summary).
            const moved = await page.waitForFunction(tok => {
                const c = document.getElementById('lesson-content');
                return stepState !== tok || (c && c.querySelector('.lsn-summary, .lsn-finishing'));
            }, tok, { timeout: 8000 }).then(() => true).catch(() => false);
            if (!moved) { stuck('did not advance after Continue'); break; }
            // Mic steps skipped silently by the snooze after the first skip.
            const nxt = await page.evaluate(STATE);
            if (nxt.index > st.index + 1) {
                const types = await page.evaluate(([a, b]) => currentLesson.steps.slice(a, b).map(x => x.type), [st.index + 1, nxt.index]);
                types.filter(t => t === 'speaking' || t === 'challenge').forEach(t => res.skipped.push(t));
            }
        }
        const fin = await page.evaluate(STATE);
        if (!fin.summary && res.ok) { fail(`did not reach the summary screen (step ${fin.index + 1}/${fin.total})`); }
        // Settle: the summary and the TTS tail can still throw.
        await sleep(300);
    } catch (e) {
        fail('walk error: ' + String(e.message).split('\n')[0]);
        try { const s = await page.evaluate(STATE); res.stuck = res.stuck || { index: s.index, type: s.type, id: s.id, why: 'walk error', screen: s.screen }; } catch (_) {}
    }

    try {
        const w = await page.evaluate(() => window.__walk);
        res.tts.speechSynthesis = w.ttsSpeak;
        w.media.forEach(m => { if (!opts.liveTts && /^data:/.test(m)) res.notes.push('media error on data: audio (stub)'); else res.audio.push('media element error ' + m); });
        w.playRejects.filter(r => r !== 'NotAllowedError' && r !== 'AbortError').forEach(r => res.audio.push('audio play() rejected: ' + r));
    } catch (_) {}
    await ctx.close();

    res.notes = [...new Set(res.notes)];
    res.consoleErrors = [...new Set(res.consoleErrors)];
    res.failedRequests = [...new Set(res.failedRequests)];
    res.audio = [...new Set(res.audio)];
    res.skipped = res.skipped.reduce((a, t) => { a['skipped: ' + t] = (a['skipped: ' + t] || 0) + 1; return a; }, {});
    res.skipped = Object.entries(res.skipped).map(([k, v]) => v > 1 ? `${k} x${v}` : k);
    if (res.consoleErrors.length) fail(`${res.consoleErrors.length} console error(s)`);
    if (res.pageErrors.length) fail(`${res.pageErrors.length} page error(s)`);
    if (res.failedRequests.length) fail(`${res.failedRequests.length} failed request(s)`);
    if (res.audio.length) fail(`${res.audio.length} audio problem(s)`);
    return res;
}

(async () => {
    const o = parseArgs(process.argv.slice(2));
    const [course, level] = o.pos;
    if (!course || !level) { console.error('usage: node scripts/walk_lessons.js <course> <level> [--base URL] [--only stem...] [--out file] [--jobs N] [--live-tts]'); process.exit(2); }
    o.course = course;
    const units = JSON.parse(fs.readFileSync(path.join(ROOT, `content/${course}/curriculum/units/${level}.json`), 'utf8'));
    let stems = [...new Set(units.flatMap(u => u.stems || []))];
    if (o.only.length) stems = stems.filter(s => o.only.includes(s));
    if (!stems.length) { console.error('no lessons selected'); process.exit(2); }

    const browser = await chromium.launch();
    const results = new Array(stems.length);
    let next = 0;
    const t0 = Date.now();
    async function worker() {
        while (next < stems.length) {
            const i = next++;
            const r = await walkLesson(browser, o, stems[i]).catch(e => ({ stem: stems[i], ok: false, reasons: ['harness error: ' + e.message], consoleErrors: [], pageErrors: [], failedRequests: [], audio: [], skipped: [], notes: [], tts: {} }));
            results[i] = r;
            console.log(`${r.ok ? 'OK  ' : 'FAIL'} ${r.stem.padEnd(22)} ${String(r.steps || 0).padStart(3)} steps` +
                `${r.skipped && r.skipped.length ? '  [' + r.skipped.join(', ') + ']' : ''}${r.ok ? '' : '  ' + r.reasons.join('; ')}`);
        }
    }
    await Promise.all(Array.from({ length: Math.min(o.jobs, stems.length) }, worker));
    await browser.close();

    const bad = results.filter(r => !r.ok);
    console.log(`\n${results.length - bad.length}/${results.length} lessons OK, ${bad.length} FAIL (${Math.round((Date.now() - t0) / 1000)}s)`);
    for (const r of bad) {
        console.log(`\n${r.stem}`);
        r.reasons.forEach(x => console.log('  - ' + x));
        r.consoleErrors.forEach(x => console.log('  console: ' + x));
        r.pageErrors.forEach(x => console.log('  pageerror: ' + x));
        r.failedRequests.forEach(x => console.log('  request: ' + x));
        r.audio.forEach(x => console.log('  audio: ' + x));
        if (r.stuck) console.log(`  stuck: step ${r.stuck.index + 1} ${r.stuck.type} ${r.stuck.id || ''} -- ${r.stuck.why} -- screen: "${r.stuck.screen}"`);
    }
    if (o.out) fs.writeFileSync(o.out, JSON.stringify({ course, level, base: o.base, liveTts: o.liveTts, ok: results.length - bad.length, fail: bad.length, results }, null, 2));
    process.exit(bad.length ? 1 : 0);
})();
