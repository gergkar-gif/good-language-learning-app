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

    const TOKEN_STORAGE_KEY = 'syncToken';
    const EMAIL_STORAGE_KEY = 'syncEmail';

    // Per-course stores worth backing up — everything that represents real
    // learner progress. Deliberately excludes device/UI preferences
    // (app_language, app_sound_muted, app_reviewDirection, app_reviewMode),
    // each already documented in its own file as a per-device setting that
    // shouldn't silently change on restore.
    const COURSE_KEYS = [
        'progress', 'srsDeck', 'knownWords', 'recycleSchedule', 'testResults',
        'readStories', 'savedReadings', 'myTexts', 'myDecks',
        'verbSpeedScores', 'unitPracticeDismissed', 'miniGameDismissed',
        'milestonesSeen', 'lastActivity'
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
        } catch (error) { /* private browsing — nothing to clear */ }
    }

    async function requestLink(userEmail) {
        const res = await fetch(WORKER_URL + '/auth/request-link', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: userEmail })
        });
        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            throw new Error(body.error || 'Could not send link');
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

    async function backup() {
        const token = getToken();
        if (!token) throw new Error('Not signed in');

        const res = await fetch(WORKER_URL + '/sync/state', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({ state: gatherSnapshot() })
        });
        if (!res.ok) throw new Error('Backup failed (' + res.status + ')');
        return res.json();
    }

    // Returns the cloud's last-backed-up timestamp without touching local
    // data — used to label the Restore button so the learner can see how
    // stale it is before choosing to overwrite local data with it.
    async function status() {
        const token = getToken();
        if (!token) return null;

        const res = await fetch(WORKER_URL + '/sync/state', {
            headers: { 'Authorization': 'Bearer ' + token }
        });
        if (!res.ok) throw new Error('Could not reach cloud (' + res.status + ')');
        return res.json();
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
        location.reload();
    }

    return {
        isLoggedIn, email, logout, requestLink, completeVerify,
        gatherSnapshot, applySnapshot, backup, restore, status
    };
})();
