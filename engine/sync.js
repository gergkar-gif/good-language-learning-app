// ============================================
// CLOUD SYNC
// ============================================
// Step 7 (last step) of the Learner model & personalized path roadmap
// initiative. Opt-in backup/restore of a learner's local progress via a
// small Cloudflare Worker + D1 (see cloudflare-worker/sync-worker.js) —
// see CLOUD_SYNC_SETUP.md for how to deploy it and where WORKER_URL
// below comes from, same one-time-setup pattern engine/bugreport.js
// already established for its own worker.
//
// Deliberately last-write-wins, not an automatic merge: the learner picks
// a direction (Back up / Restore), nothing silent happens in the
// background. A smarter per-field merge (e.g. "keep whichever SRS card
// is more advanced" instead of overwriting) is a real future need, not
// built here — most use is expected to be a single primary device.
//
// An account spans both courses, so its own keys (syncToken/syncEmail)
// are bare, not Lang.key()-scoped, unlike almost everything else in this
// app. The synced snapshot itself is built by walking every course in
// Lang.available() directly (`${course}:${name}`) rather than through
// Lang.key(), which only ever answers for the CURRENTLY selected course.

const Sync = (function () {
    'use strict';

    const WORKER_URL = 'https://parlour-sync.gergkar.workers.dev';

    // Public Turnstile site key (safe to ship client-side — it's the secret
    // key, held only by the Worker, that actually matters). Empty until a
    // Turnstile widget is created in the Cloudflare dashboard; while empty,
    // getTurnstileToken() is a no-op and the Worker skips verification too
    // (see TURNSTILE_SETUP.md), so requestLink() keeps working unprotected
    // rather than breaking sign-in before the widget exists.
    const TURNSTILE_SITE_KEY = '0x4AAAAAAE5nXnu8zfuPH7yB';

    // Public Google OAuth 2.0 Web Client ID (safe to ship client-side — see
    // GOOGLE_SIGNIN_SETUP.md). Enables 1-tap Google Sign-In button and prompt.
    const GOOGLE_CLIENT_ID = '191870279923-7ed8193v1av9q5tpm9u1h046idqc6k7s.apps.googleusercontent.com';

    const TOKEN_STORAGE_KEY = 'syncToken';
    const EMAIL_STORAGE_KEY = 'syncEmail';
    const FIRST_VISIT_PROMPT_KEY = 'syncPromptSeen';
    const LAST_SYNCED_KEY = 'syncLastSyncedAt';

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    // Per-course stores worth backing up — everything that represents real
    // learner progress. Deliberately excludes device/UI preferences
    // (app_language, app_sound_muted, app_reviewDirection, app_reviewMode),
    // each already documented in its own file as a per-device setting that
    // shouldn't silently change on restore.
    const COURSE_KEYS = [
        'progress', 'srsDeck', 'knownWords', 'recycleSchedule', 'testResults',
        'readStories', 'savedReadings', 'myTexts', 'myDecks',
        'verbSpeedScores', 'unitPracticeDismissed', 'miniGameDismissed',
        'milestonesSeen', 'lastActivity', 'productionEvidence', 'assessmentHistory'
    ];
    // Per-course, but with a variable suffix (one key per deck/driller) —
    // matched by prefix instead of an exact name.
    const COURSE_KEY_PREFIXES = ['deckMatchBest:stream:', 'drillHistory:'];

    // Not Lang.key()-scoped at all — a habit stat, not one course's data
    // (see engine/lang.js's own header comment on this exact point).
    const GLOBAL_KEYS = ['spanishApp_xp'];

    function getToken() {
        try { return localStorage.getItem(TOKEN_STORAGE_KEY); }
        catch (error) { return null; }
    }

    function isLoggedIn() {
        return !!getToken();
    }

    function email() {
        try { return localStorage.getItem(EMAIL_STORAGE_KEY) || ''; }
        catch (error) { return ''; }
    }

    function logout() {
        try {
            localStorage.removeItem(TOKEN_STORAGE_KEY);
            localStorage.removeItem(EMAIL_STORAGE_KEY);
            localStorage.removeItem('parlour_user_name');
            localStorage.removeItem(LAST_SYNCED_KEY);
        } catch (error) { /* private browsing — nothing to clear */ }
    }

    function getUserName() {
        try {
            return localStorage.getItem('parlour_user_name') || '';
        } catch (e) {
            return '';
        }
    }

    // ----------------------------------------
    // FIRST-VISIT PROMPT
    // ----------------------------------------
    // A one-time, friendly invite to back up progress — shown once ever
    // per device, whether the learner signs up or dismisses it. Reachable
    // afterward via My Journey's own Account card either way, so
    // dismissing here loses nothing, just stops the one-time ask from
    // repeating. Same wp-overlay/wp-sheet body-level pattern used
    // elsewhere (e.g. engine/decks.js's add-to-deck picker).
    function ensurePromptHost() {
        let el = document.getElementById('sync-first-visit-prompt');
        if (el) return el;
        el = document.createElement('div');
        el.id = 'sync-first-visit-prompt';
        document.body.appendChild(el);
        return el;
    }

    function closeFirstVisitPrompt() {
        const el = document.getElementById('sync-first-visit-prompt');
        if (el) el.innerHTML = '';
    }

    function _promptFormHtml() {
        const googleSection = isGoogleAuthAvailable() ? `
            <div id="sync-prompt-google-btn" class="jr-google-signin-container"></div>
            <div class="jr-account-divider"><span>or sign in with email</span></div>
        ` : '';

        return `
            <div class="wp-overlay" id="sync-prompt-overlay">
                <div class="wp-sheet sync-prompt-sheet">
                    <div class="wp-header">
                        <h2 class="sync-prompt-title">Keep your progress safe</h2>
                        <button class="wp-close" data-sync-prompt-close="1" aria-label="Close">&times;</button>
                    </div>
                    <p class="jr-account-blurb">Sign in to sync your progress across devices &mdash;
                        no password, and you won't need to log in again.</p>
                    ${googleSection}
                    <div class="jr-account-login">
                        <input type="email" id="sync-prompt-email-input" class="dk-editor-input"
                            placeholder="you@example.com" maxlength="254">
                        <button class="dk-secondary" data-sync-prompt-send="1">Send me a link</button>
                    </div>
                    <p class="jr-account-status" id="sync-prompt-status"></p>
                    <button class="jr-account-logout" data-sync-prompt-close="1">Not now</button>
                </div>
            </div>
        `;
    }

    function _promptConfirmationHtml(sentEmail) {
        return `
            <div class="wp-overlay" id="sync-prompt-overlay">
                <div class="wp-sheet sync-prompt-sheet">
                    <div class="wp-header">
                        <h2 class="sync-prompt-title">Check your email</h2>
                        <button class="wp-close" data-sync-prompt-close="1" aria-label="Close">&times;</button>
                    </div>
                    <p class="jr-account-blurb">We sent a link to ${esc(sentEmail)}. Tap it and
                        you're all set — no password, no need to log in again.</p>
                    <button class="dk-secondary" data-sync-prompt-close="1">Got it</button>
                </div>
            </div>
        `;
    }

    function maybeShowFirstVisitPrompt() {
        if (isLoggedIn()) return;

        // Defer until the learner has actual progress to protect (at least 1 lesson completed or XP earned).
        // Never interrupt a brand new user on their very first visit before they even know what Parlour is.
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const completedCount = Object.keys(progress).length;
        const xp = (typeof xpData !== 'undefined' && xpData && xpData.xp) ? xpData.xp : 0;
        if (completedCount === 0 && xp === 0) return;

        try {
            if (localStorage.getItem(FIRST_VISIT_PROMPT_KEY)) return;
            localStorage.setItem(FIRST_VISIT_PROMPT_KEY, '1');
        } catch (error) {
            return; // private browsing with storage disabled — nothing to persist the ask against
        }

        const host = ensurePromptHost();
        host.innerHTML = _promptFormHtml();

        host.querySelectorAll('[data-sync-prompt-close]').forEach(el => {
            el.addEventListener('click', closeFirstVisitPrompt);
        });
        const overlay = document.getElementById('sync-prompt-overlay');
        if (overlay) overlay.addEventListener('click', e => { if (e.target === overlay) closeFirstVisitPrompt(); });

        if (isGoogleAuthAvailable()) {
            renderGoogleButton('sync-prompt-google-btn', {
                onStart: () => {
                    const statusEl = host.querySelector('#sync-prompt-status');
                    if (statusEl) statusEl.textContent = 'Signing in with Google\u2026';
                },
                onSuccess: () => {
                    closeFirstVisitPrompt();
                    location.reload();
                },
                onError: (err) => {
                    const statusEl = host.querySelector('#sync-prompt-status');
                    if (statusEl) statusEl.textContent = err.message || 'Google sign-in failed.';
                }
            });
        }

        const sendBtn = host.querySelector('[data-sync-prompt-send]');
        if (sendBtn) {
            sendBtn.addEventListener('click', () => {
                const input = host.querySelector('#sync-prompt-email-input');
                const statusEl = host.querySelector('#sync-prompt-status');
                const value = input ? input.value.trim() : '';
                if (!value) {
                    if (statusEl) statusEl.textContent = 'Enter an email first.';
                    return;
                }
                if (statusEl) statusEl.textContent = 'Sending…';
                requestLink(value)
                    .then(() => { host.innerHTML = _promptConfirmationHtml(value); wireClose(); })
                    .catch(error => { if (statusEl) statusEl.textContent = error.message || 'Something went wrong.'; });
            });
        }

        function wireClose() {
            host.querySelectorAll('[data-sync-prompt-close]').forEach(el => {
                el.addEventListener('click', closeFirstVisitPrompt);
            });
            const ov = document.getElementById('sync-prompt-overlay');
            if (ov) ov.addEventListener('click', e => { if (e.target === ov) closeFirstVisitPrompt(); });
        }
    }

    // ----------------------------------------
    // TURNSTILE (bot check before requestLink emails anyone)
    // ----------------------------------------
    // Invisible widget: no checkbox in the UI, just a token minted in the
    // background and handed to the Worker, which verifies it with
    // Cloudflare before sending the magic-link email. Loaded lazily — most
    // visits never open the sign-in form, so there's no reason to fetch
    // Cloudflare's script on every page load.
    let _turnstileLoadPromise = null;
    let _turnstileWidgetId = null;
    let _turnstileResolve = null;
    let _turnstileReject = null;

    function _loadTurnstileScript() {
        if (_turnstileLoadPromise) return _turnstileLoadPromise;
        _turnstileLoadPromise = new Promise((resolve, reject) => {
            if (window.turnstile) { resolve(window.turnstile); return; }
            const script = document.createElement('script');
            script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js';
            script.async = true;
            script.onload = () => resolve(window.turnstile);
            script.onerror = () => reject(new Error('Could not load Turnstile'));
            document.head.appendChild(script);
        });
        return _turnstileLoadPromise;
    }

    async function getTurnstileToken() {
        if (!TURNSTILE_SITE_KEY) return null; // not configured yet — Worker skips verification too
        const turnstile = await _loadTurnstileScript();
        if (_turnstileWidgetId === null) {
            const host = document.createElement('div');
            host.style.display = 'none';
            document.body.appendChild(host);
            _turnstileWidgetId = turnstile.render(host, {
                sitekey: TURNSTILE_SITE_KEY,
                size: 'invisible',
                callback: token => { if (_turnstileResolve) _turnstileResolve(token); },
                'error-callback': () => { if (_turnstileReject) _turnstileReject(new Error('Verification failed')); }
            });
        }
        return new Promise((resolve, reject) => {
            _turnstileResolve = resolve;
            _turnstileReject = reject;
            turnstile.execute(_turnstileWidgetId);
        });
    }

    async function requestLink(userEmail) {
        let turnstileToken = null;
        try {
            turnstileToken = await getTurnstileToken();
        } catch (error) {
            // Falls through with turnstileToken = null — the Worker rejects
            // the request outright once TURNSTILE_SECRET_KEY is configured,
            // same as a missing token, so nothing needs handling here.
        }

        const res = await fetch(WORKER_URL + '/auth/request-link', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: userEmail, turnstileToken })
        });
        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            throw new Error(body.error || 'Could not send link');
        }
    }

    // ----------------------------------------
    // GOOGLE SIGN-IN (OpenID Connect / Google Identity Services)
    // ----------------------------------------
    let _gsiLoadPromise = null;

    function isGoogleAuthAvailable() {
        return Boolean(GOOGLE_CLIENT_ID);
    }

    function getGoogleClientId() {
        return GOOGLE_CLIENT_ID;
    }

    function _loadGoogleScript() {
        if (_gsiLoadPromise) return _gsiLoadPromise;
        _gsiLoadPromise = new Promise((resolve, reject) => {
            if (typeof window !== 'undefined' && window.google && window.google.accounts && window.google.accounts.id) {
                resolve(window.google.accounts.id);
                return;
            }
            if (typeof document === 'undefined') {
                reject(new Error('Document not available'));
                return;
            }
            const script = document.createElement('script');
            script.src = 'https://accounts.google.com/gsi/client?hl=en';
            script.async = true;
            script.defer = true;
            script.onload = () => {
                if (window.google && window.google.accounts && window.google.accounts.id) {
                    resolve(window.google.accounts.id);
                } else {
                    reject(new Error('Google Identity Services SDK failed to initialize'));
                }
            };
            script.onerror = () => reject(new Error('Could not load Google Sign-In SDK'));
            document.head.appendChild(script);
        });
        return _gsiLoadPromise;
    }

    async function loginWithGoogle(credential) {
        if (!credential) throw new Error('Missing Google credential');

        const res = await fetch(WORKER_URL + '/auth/google', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ credential })
        });

        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            throw new Error(body.error || 'Google sign-in failed');
        }

        const data = await res.json();
        localStorage.setItem(TOKEN_STORAGE_KEY, data.token);
        localStorage.setItem(EMAIL_STORAGE_KEY, data.email);

        let userName = data.name || '';
        if (!userName) {
            try {
                const parts = credential.split('.');
                if (parts.length === 3) {
                    const b64 = parts[1].replace(/-/g, '+').replace(/_/g, '/');
                    const decoded = JSON.parse(decodeURIComponent(escape(atob(b64))));
                    userName = decoded.given_name || decoded.name || '';
                }
            } catch (e) {
                console.warn('Sync: could not decode name from Google credential', e);
            }
        }
        if (userName) {
            localStorage.setItem('parlour_user_name', userName);
        }

        // Merge local state with cloud backup upon login so progress is never lost
        try {
            const cloudData = await status();
            if (cloudData && cloudData.state) {
                const localSnapshot = gatherSnapshot();
                const merged = mergeSnapshots(localSnapshot, cloudData.state);
                applySnapshot(merged);
                const cloudUpdatedAt = cloudData.updatedAt ? new Date(cloudData.updatedAt).getTime() : Date.now();
                localStorage.setItem(LAST_SYNCED_KEY, String(cloudUpdatedAt));
                if (hasLocalAdditions(localSnapshot, cloudData.state)) {
                    await backup();
                }
            }
        } catch (err) {
            console.warn('Sync: initial auto-merge skipped', err);
        }

        return data;
    }

    async function renderGoogleButton(target, options = {}) {
        if (!GOOGLE_CLIENT_ID) return;
        const container = (typeof target === 'string') ? document.getElementById(target) : target;
        if (!container) return;

        try {
            const gsi = await _loadGoogleScript();
            gsi.initialize({
                client_id: GOOGLE_CLIENT_ID,
                callback: async (response) => {
                    if (!response || !response.credential) return;
                    try {
                        if (options.onStart) options.onStart();
                        const result = await loginWithGoogle(response.credential);
                        if (options.onSuccess) options.onSuccess(result);
                        else location.reload();
                    } catch (err) {
                        if (options.onError) options.onError(err);
                        else console.error('Google sign-in error:', err);
                    }
                },
                auto_select: false,
                cancel_on_tap_outside: true
            });

            const isDark = (typeof document !== 'undefined') &&
                document.documentElement.getAttribute('data-theme') === 'dark';

            const btnConfig = Object.assign({
                type: 'standard',
                shape: 'rectangular',
                theme: isDark ? 'filled_black' : 'outline',
                text: 'signin_with',
                size: 'large',
                logo_alignment: 'left',
                width: options.width || 250
            }, options.buttonConfig || {});

            container.innerHTML = '';
            gsi.renderButton(container, btnConfig);

            if (options.enableOneTap) {
                gsi.prompt(options.onPromptNotification);
            }
        } catch (error) {
            console.warn('Google Sign-In initialization skipped or failed:', error.message || error);
        }
    }

    async function promptGoogleOneTap(options = {}) {
        if (!GOOGLE_CLIENT_ID || isLoggedIn()) return;
        try {
            const gsi = await _loadGoogleScript();
            gsi.initialize({
                client_id: GOOGLE_CLIENT_ID,
                callback: async (response) => {
                    if (!response || !response.credential) return;
                    try {
                        const result = await loginWithGoogle(response.credential);
                        if (options.onSuccess) options.onSuccess(result);
                        else location.reload();
                    } catch (err) {
                        if (options.onError) options.onError(err);
                    }
                },
                cancel_on_tap_outside: true
            });
            gsi.prompt(options.onPromptNotification);
        } catch (error) {
            // Silently ignore One Tap failure
        }
    }

    // Called once at boot (engine/init.js). If the page was opened from a
    // magic-link email (?verify=<token>), exchanges it for a session and
    // strips the token from the URL either way — it's single-use, so it
    // must never linger in the address bar or browser history.
    async function completeVerify() {
        const params = new URLSearchParams(location.search);
        const token = params.get('verify');
        if (!token) return;

        params.delete('verify');
        const cleanUrl = location.pathname + (params.toString() ? '?' + params.toString() : '');
        history.replaceState(null, '', cleanUrl);

        try {
            const res = await fetch(WORKER_URL + '/auth/verify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ token })
            });
            if (!res.ok) return;
            const data = await res.json();
            localStorage.setItem(TOKEN_STORAGE_KEY, data.token);
            localStorage.setItem(EMAIL_STORAGE_KEY, data.email);

            // Merge local state with cloud backup upon login so progress is never lost
            try {
                const cloudData = await status();
                if (cloudData && cloudData.state) {
                    const localSnapshot = gatherSnapshot();
                    const merged = mergeSnapshots(localSnapshot, cloudData.state);
                    applySnapshot(merged);
                    const cloudUpdatedAt = cloudData.updatedAt ? new Date(cloudData.updatedAt).getTime() : Date.now();
                    localStorage.setItem(LAST_SYNCED_KEY, String(cloudUpdatedAt));
                    if (hasLocalAdditions(localSnapshot, cloudData.state)) {
                        await backup();
                    }
                }
            } catch (err) {
                console.warn('Sync: initial auto-merge skipped', err);
            }
        } catch (error) {
            // Offline or the worker is unreachable — the learner can just
            // request a fresh link; nothing else to do here.
        }
    }

    // ----------------------------------------
    // SNAPSHOT (gather / apply)
    // ----------------------------------------

    function gatherSnapshot() {
        const snapshot = {};
        const courses = (typeof Lang !== 'undefined') ? Lang.available() : ['es'];

        courses.forEach(course => {
            const data = {};
            COURSE_KEYS.forEach(name => {
                const raw = localStorage.getItem(course + ':' + name);
                if (raw !== null) data[name] = raw;
            });
            Object.keys(localStorage).forEach(key => {
                const prefix = course + ':';
                if (!key.startsWith(prefix)) return;
                const rest = key.slice(prefix.length);
                if (COURSE_KEY_PREFIXES.some(p => rest.startsWith(p))) {
                    data[rest] = localStorage.getItem(key);
                }
            });
            snapshot[course] = data;
        });

        const globals = {};
        GLOBAL_KEYS.forEach(name => {
            const raw = localStorage.getItem(name);
            if (raw !== null) globals[name] = raw;
        });
        snapshot._global = globals;

        return snapshot;
    }

    function applySnapshot(snapshot) {
        if (!snapshot || typeof snapshot !== 'object') return;

        Object.keys(snapshot).forEach(course => {
            if (course === '_global') return;
            const data = snapshot[course] || {};
            Object.keys(data).forEach(name => {
                localStorage.setItem(course + ':' + name, data[name]);
            });
        });

        const globals = snapshot._global || {};
        Object.keys(globals).forEach(name => {
            localStorage.setItem(name, globals[name]);
        });
    }

    // ----------------------------------------
    // BACKUP / RESTORE
    // ----------------------------------------

    async function backup(options = {}) {
        const token = getToken();
        if (!token) throw new Error('Not signed in');

        const fetchInit = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({ state: gatherSnapshot() })
        };
        if (options.keepalive) {
            fetchInit.keepalive = true;
        }

        const res = await fetch(WORKER_URL + '/sync/state', fetchInit);
        if (!res.ok) throw new Error('Backup failed (' + res.status + ')');
        const data = await res.json();
        _isDirty = false;
        if (data && data.updatedAt) {
            _lastSavedAt = new Date(data.updatedAt).getTime();
            try {
                localStorage.setItem(LAST_SYNCED_KEY, String(_lastSavedAt));
            } catch (e) {}
        }
        return data;
    }

    // Returns the cloud's last-backed-up timestamp without touching local
    // data — used to label the Restore button so the learner can see how
    // stale it is before choosing to overwrite local data with it.
    async function status(options = {}) {
        const token = getToken();
        if (!token) return null;

        const controller = (typeof AbortController !== 'undefined' && options.timeoutMs) ? new AbortController() : null;
        const timer = controller ? setTimeout(() => controller.abort(), options.timeoutMs) : null;

        try {
            const res = await fetch(WORKER_URL + '/sync/state', {
                headers: { 'Authorization': 'Bearer ' + token },
                signal: controller ? controller.signal : undefined
            });
            if (!res.ok) throw new Error('Could not reach cloud (' + res.status + ')');
            return await res.json();
        } finally {
            if (timer) clearTimeout(timer);
        }
    }

    // Overwrites local data with the cloud copy, then reloads the page —
    // not optional: most modules (srsDeck, xpData, myDecks, etc.) load
    // their in-memory state once at boot from localStorage, so swapping
    // the underlying storage in place would leave those globals stale
    // until the next reload happens anyway.
    async function restore() {
        const data = await status();
        if (!data || !data.state) throw new Error('Nothing backed up yet');
        applySnapshot(data.state);
        _isDirty = false;
        if (data && data.updatedAt) {
            _lastSavedAt = new Date(data.updatedAt).getTime();
            try {
                localStorage.setItem(LAST_SYNCED_KEY, String(_lastSavedAt));
            } catch (e) {}
        }
        location.reload();
    }

    // ----------------------------------------
    // ADDITIVE MERGING (Multi-Device Resolution)
    // ----------------------------------------

    function safeJsonParse(raw, fallback) {
        if (!raw || typeof raw !== 'string') return fallback;
        try {
            return JSON.parse(raw);
        } catch (e) {
            return fallback;
        }
    }

    function mergeProgress(localRaw, cloudRaw) {
        const lProg = safeJsonParse(localRaw, {});
        const cProg = safeJsonParse(cloudRaw, {});
        const allIds = new Set([...Object.keys(lProg || {}), ...Object.keys(cProg || {})]);
        const res = {};
        allIds.forEach(id => {
            const l = lProg[id];
            const c = cProg[id];
            if (l && c) {
                const lTime = l.completedAt ? new Date(l.completedAt).getTime() : 0;
                const cTime = c.completedAt ? new Date(c.completedAt).getTime() : 0;
                const bestTime = (lTime && cTime)
                    ? new Date(Math.min(lTime, cTime)).toISOString()
                    : (l.completedAt || c.completedAt);
                res[id] = Object.assign({}, c, l, { completedAt: bestTime });
            } else {
                res[id] = l || c;
            }
        });
        return JSON.stringify(res);
    }

    function mergeKnownWords(localRaw, cloudRaw) {
        const lWords = safeJsonParse(localRaw, []);
        const cWords = safeJsonParse(cloudRaw, []);
        const map = new Map();
        [...cWords, ...lWords].forEach(w => {
            if (!w) return;
            const key = w.spanish || w.lemma || w.word;
            if (!key) return;
            if (!map.has(key)) {
                map.set(key, w);
            } else {
                const existing = map.get(key);
                const t1 = existing.added ? new Date(existing.added).getTime() : Infinity;
                const t2 = w.added ? new Date(w.added).getTime() : Infinity;
                map.set(key, Object.assign({}, existing, w, {
                    added: (t1 < t2 ? existing.added : w.added) || existing.added
                }));
            }
        });
        return JSON.stringify(Array.from(map.values()));
    }

    function mergeSrsDeck(localRaw, cloudRaw) {
        const lCards = safeJsonParse(localRaw, []);
        const cCards = safeJsonParse(cloudRaw, []);
        const cardMap = new Map();
        [...cCards, ...lCards].forEach(card => {
            if (!card) return;
            const key = card.spanish || card.lemma || card.word;
            if (!key) return;
            if (!cardMap.has(key)) {
                cardMap.set(key, card);
            } else {
                const existing = cardMap.get(key);
                const exReviews = existing.reviews || 0;
                const newReviews = card.reviews || 0;
                const exInterval = existing.interval || 0;
                const newInterval = card.interval || 0;
                if (newReviews > exReviews || (newReviews === exReviews && newInterval > exInterval)) {
                    cardMap.set(key, card);
                }
            }
        });
        return JSON.stringify(Array.from(cardMap.values()));
    }

    function mergeXP(localRaw, cloudRaw) {
        const lXP = safeJsonParse(localRaw, {});
        const cXP = safeJsonParse(cloudRaw, {});
        const mXP = {
            xp: Math.max(lXP.xp || 0, cXP.xp || 0),
            dailyNewWords: Object.assign({}, cXP.dailyNewWords || {}, lXP.dailyNewWords || {}),
            history: {},
            streak: Math.max(lXP.streak || 0, cXP.streak || 0),
            streakFreezeAvailable: lXP.streakFreezeAvailable !== false && cXP.streakFreezeAvailable !== false,
            lastPracticeDate: (lXP.lastPracticeDate > (cXP.lastPracticeDate || ''))
                ? lXP.lastPracticeDate
                : (cXP.lastPracticeDate || lXP.lastPracticeDate || '')
        };
        const lHist = lXP.history || {};
        const cHist = cXP.history || {};
        const allDates = new Set([...Object.keys(lHist), ...Object.keys(cHist)]);
        allDates.forEach(d => {
            const lh = lHist[d] || {};
            const ch = cHist[d] || {};
            mXP.history[d] = {
                total: Math.max(lh.total || 0, ch.total || 0),
                lessons: Math.max(lh.lessons || 0, ch.lessons || 0),
                drills: Math.max(lh.drills || 0, ch.drills || 0),
                stories: Math.max(lh.stories || 0, ch.stories || 0),
                verbs: Math.max(lh.verbs || 0, ch.verbs || 0),
                bonus: Math.max(lh.bonus || 0, ch.bonus || 0),
                newWords: Math.max(lh.newWords || 0, ch.newWords || 0)
            };
        });
        return JSON.stringify(mXP);
    }

    function mergeArrayById(localRaw, cloudRaw) {
        const lArr = safeJsonParse(localRaw, []);
        const cArr = safeJsonParse(cloudRaw, []);
        const map = new Map();
        [...cArr, ...lArr].forEach(item => {
            if (!item) return;
            const key = item.id || item.spanish || item.lemma || (typeof item === 'string' ? item : null);
            if (key) {
                if (!map.has(key)) map.set(key, item);
                else map.set(key, Object.assign({}, map.get(key), item));
            } else {
                map.set(JSON.stringify(item), item);
            }
        });
        return JSON.stringify(Array.from(map.values()));
    }

    function mergeField(name, localRaw, cloudRaw) {
        if (!localRaw) return cloudRaw;
        if (!cloudRaw) return localRaw;
        if (localRaw === cloudRaw) return localRaw;

        if (name === 'progress') return mergeProgress(localRaw, cloudRaw);
        if (name === 'knownWords') return mergeKnownWords(localRaw, cloudRaw);
        if (name === 'srsDeck') return mergeSrsDeck(localRaw, cloudRaw);
        if (name === 'spanishApp_xp') return mergeXP(localRaw, cloudRaw);
        if (name === 'readStories' || name === 'savedReadings' || name === 'myTexts' || name === 'myDecks') {
            return mergeArrayById(localRaw, cloudRaw);
        }
        if (name.startsWith('drillHistory:')) {
            return mergeArrayById(localRaw, cloudRaw);
        }

        // Generic JSON object fallback
        try {
            const lObj = JSON.parse(localRaw);
            const cObj = JSON.parse(cloudRaw);
            if (typeof lObj === 'object' && lObj !== null && typeof cObj === 'object' && cObj !== null) {
                return JSON.stringify(Object.assign({}, cObj, lObj));
            }
        } catch (e) {}

        return cloudRaw;
    }

    function mergeSnapshots(local, cloud) {
        if (!cloud || typeof cloud !== 'object') return local || {};
        if (!local || typeof local !== 'object') return cloud || {};

        const merged = {};
        const courses = new Set([...Object.keys(local), ...Object.keys(cloud)]);

        courses.forEach(course => {
            if (course === '_global') return;
            const lData = local[course] || {};
            const cData = cloud[course] || {};
            const mData = {};
            const keys = new Set([...Object.keys(lData), ...Object.keys(cData)]);

            keys.forEach(key => {
                const lRaw = lData[key];
                const cRaw = cData[key];
                if (lRaw === undefined) {
                    mData[key] = cRaw;
                } else if (cRaw === undefined) {
                    mData[key] = lRaw;
                } else {
                    mData[key] = mergeField(key, lRaw, cRaw);
                }
            });
            merged[course] = mData;
        });

        // Merge _global
        const lGlobal = local._global || {};
        const cGlobal = cloud._global || {};
        const mGlobal = {};
        const gKeys = new Set([...Object.keys(lGlobal), ...Object.keys(cGlobal)]);

        gKeys.forEach(key => {
            const lRaw = lGlobal[key];
            const cRaw = cGlobal[key];
            if (lRaw === undefined) {
                mGlobal[key] = cRaw;
            } else if (cRaw === undefined) {
                mGlobal[key] = lRaw;
            } else {
                mGlobal[key] = mergeField(key, lRaw, cRaw);
            }
        });
        merged._global = mGlobal;

        return merged;
    }

    function hasLocalAdditions(localSnapshot, cloudSnapshot) {
        if (!localSnapshot) return false;
        if (!cloudSnapshot) return true;

        for (const course of Object.keys(localSnapshot)) {
            if (course === '_global') continue;
            const lData = localSnapshot[course] || {};
            const cData = cloudSnapshot[course] || {};

            const lProg = safeJsonParse(lData.progress, {});
            const cProg = safeJsonParse(cData.progress, {});
            for (const id of Object.keys(lProg)) {
                if (!cProg[id]) return true;
            }

            const lWords = safeJsonParse(lData.knownWords, []);
            const cWords = safeJsonParse(cData.knownWords, []);
            const cWordSet = new Set(cWords.map(w => w.spanish || w.lemma || w.word));
            for (const w of lWords) {
                const key = w && (w.spanish || w.lemma || w.word);
                if (key && !cWordSet.has(key)) return true;
            }
        }

        const lXP = safeJsonParse(localSnapshot._global?.spanishApp_xp, {});
        const cXP = safeJsonParse(cloudSnapshot._global?.spanishApp_xp, {});
        if ((lXP.xp || 0) > (cXP.xp || 0)) return true;

        return false;
    }

    function hasAnyProgress(snapshot) {
        if (!snapshot || typeof snapshot !== 'object') return false;
        for (const course of Object.keys(snapshot)) {
            if (course === '_global') continue;
            const data = snapshot[course] || {};
            const prog = safeJsonParse(data.progress, {});
            if (Object.keys(prog).length > 0) return true;
        }
        const xp = safeJsonParse(snapshot._global?.spanishApp_xp, {});
        if ((xp.xp || 0) > 0) return true;
        return false;
    }

    // ----------------------------------------
    // AUTOMATIC BACKGROUND SYNC
    // ----------------------------------------
    let _autoSaveTimer = null;
    let _isSaving = false;
    let _isDirty = false;
    let _lastSavedAt = null;

    function scheduleAutoSave() {
        if (!isLoggedIn()) return;
        _isDirty = true;
        if (_autoSaveTimer) clearTimeout(_autoSaveTimer);
        _autoSaveTimer = setTimeout(() => {
            performAutoSave();
        }, 2500);
    }

    async function performAutoSave(options = {}) {
        if (!isLoggedIn() || _isSaving) return;
        _isSaving = true;
        try {
            const data = await backup(options);
            _lastSavedAt = (data && data.updatedAt) ? new Date(data.updatedAt).getTime() : Date.now();
            _isDirty = false;
            try {
                localStorage.setItem(LAST_SYNCED_KEY, String(_lastSavedAt));
            } catch (e) {}
            if (typeof window !== 'undefined' && typeof window.dispatchEvent === 'function') {
                window.dispatchEvent(new CustomEvent('sync-saved', { detail: { timestamp: _lastSavedAt } }));
            }
        } catch (error) {
            console.warn('Sync: background auto-save failed', error);
        } finally {
            _isSaving = false;
        }
    }

    function lastSavedAt() {
        return _lastSavedAt;
    }

    async function syncOnStartup() {
        if (!isLoggedIn()) return false;
        try {
            const cloudData = await status({ timeoutMs: 3500 });
            if (!cloudData) return false;

            const cloudUpdatedAt = cloudData.updatedAt ? new Date(cloudData.updatedAt).getTime() : 0;
            const lastSyncedAt = Number(localStorage.getItem(LAST_SYNCED_KEY) || '0');

            if (!cloudData.state) {
                const localSnapshot = gatherSnapshot();
                if (hasAnyProgress(localSnapshot)) {
                    await backup();
                }
                return false;
            }

            const localSnapshot = gatherSnapshot();

            if (cloudUpdatedAt > lastSyncedAt || !lastSyncedAt) {
                const merged = mergeSnapshots(localSnapshot, cloudData.state);
                applySnapshot(merged);
                _lastSavedAt = cloudUpdatedAt;
                try {
                    localStorage.setItem(LAST_SYNCED_KEY, String(cloudUpdatedAt));
                } catch (e) {}
                _isDirty = false;

                if (hasLocalAdditions(localSnapshot, cloudData.state)) {
                    await backup();
                }
                return true;
            } else if (_isDirty) {
                await backup();
            }
        } catch (err) {
            console.warn('Sync: startup check skipped or timed out', err);
        }
        return false;
    }

    let _lastFocusCheck = 0;
    async function checkForRemoteUpdates() {
        if (!isLoggedIn()) return false;
        const now = Date.now();
        if (now - _lastFocusCheck < 10000) return false;
        _lastFocusCheck = now;

        if (typeof document !== 'undefined') {
            const lessonEl = document.getElementById('lesson-screen');
            if (lessonEl && !lessonEl.classList.contains('hidden')) return false;
        }

        try {
            const cloudData = await status({ timeoutMs: 3000 });
            if (!cloudData || !cloudData.state) return false;

            const cloudUpdatedAt = cloudData.updatedAt ? new Date(cloudData.updatedAt).getTime() : 0;
            const lastSyncedAt = Number(localStorage.getItem(LAST_SYNCED_KEY) || '0');

            if (cloudUpdatedAt > lastSyncedAt) {
                const localSnapshot = gatherSnapshot();
                const merged = mergeSnapshots(localSnapshot, cloudData.state);
                applySnapshot(merged);
                _lastSavedAt = cloudUpdatedAt;
                try {
                    localStorage.setItem(LAST_SYNCED_KEY, String(cloudUpdatedAt));
                } catch (e) {}

                if (hasLocalAdditions(localSnapshot, cloudData.state)) {
                    await backup();
                }

                if (typeof location !== 'undefined' && location.reload) {
                    location.reload();
                }
                return true;
            }
        } catch (err) {
            console.warn('Sync: remote update check failed', err);
        }
        return false;
    }

    // Flush pending auto-saves when the user switches tabs or navigates away
    if (typeof document !== 'undefined') {
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'hidden') {
                if (isLoggedIn() && (_autoSaveTimer || _isDirty)) {
                    if (_autoSaveTimer) {
                        clearTimeout(_autoSaveTimer);
                        _autoSaveTimer = null;
                    }
                    performAutoSave({ keepalive: true });
                }
            } else if (document.visibilityState === 'visible') {
                if (isLoggedIn()) {
                    checkForRemoteUpdates();
                }
            }
        });
        window.addEventListener('pagehide', () => {
            if (isLoggedIn() && (_autoSaveTimer || _isDirty)) {
                if (_autoSaveTimer) {
                    clearTimeout(_autoSaveTimer);
                    _autoSaveTimer = null;
                }
                performAutoSave({ keepalive: true });
            }
        });
        window.addEventListener('beforeunload', () => {
            if (isLoggedIn() && (_autoSaveTimer || _isDirty)) {
                if (_autoSaveTimer) {
                    clearTimeout(_autoSaveTimer);
                    _autoSaveTimer = null;
                }
                performAutoSave({ keepalive: true });
            }
        });
    }

    const api = {
        isLoggedIn, email, getUserName, logout, requestLink, completeVerify,
        loginWithGoogle, renderGoogleButton, promptGoogleOneTap,
        isGoogleAuthAvailable, getGoogleClientId,
        gatherSnapshot, applySnapshot, backup, restore, status,
        maybeShowFirstVisitPrompt, scheduleAutoSave, performAutoSave,
        lastSavedAt, syncOnStartup, checkForRemoteUpdates, mergeSnapshots,
        isDirty: () => _isDirty
    };

    if (typeof window !== 'undefined') {
        window.Sync = api;
    }
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = api;
    }

    return api;
})();
