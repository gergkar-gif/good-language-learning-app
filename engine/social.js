// ============================================
// SOCIAL (Friends, Weekly Board & Friend Quests)
// ============================================
// Strictly opt-in client for Parlour's calm social endpoints on parlour-sync.
// Uses Sync's session token and worker URL, caches the last fetched snapshot
// locally for offline viewing, and handles ?friend=PRL-XXXXX invite links.

const Social = (function () {
    'use strict';

    const CACHE_KEY = 'parlour_social_cache';
    const INVITE_SESSION_KEY = 'parlour_pending_friend_code';

    function _workerUrl() {
        if (typeof Sync !== 'undefined' && typeof Sync.getWorkerUrl === 'function') {
            return Sync.getWorkerUrl();
        }
        return 'https://parlour-sync.gergkar.workers.dev';
    }

    function _token() {
        if (typeof Sync !== 'undefined' && typeof Sync.getToken === 'function') {
            return Sync.getToken();
        }
        try { return localStorage.getItem('syncToken'); } catch (e) { return null; }
    }

    function _activeCourse() {
        if (typeof Lang !== 'undefined' && typeof Lang.code === 'function') {
            return Lang.code();
        }
        return 'es-latam';
    }

    async function _api(path, method, body) {
        const token = _token();
        if (!token) throw new Error('Sign in to use friends and weekly boards.');

        const opts = {
            method: method || 'GET',
            headers: {
                'Authorization': 'Bearer ' + token
            }
        };
        if (body !== undefined) {
            opts.headers['Content-Type'] = 'application/json';
            opts.body = JSON.stringify(body);
        }

        const res = await fetch(_workerUrl() + path, opts);
        let data = null;
        try { data = await res.json(); } catch (e) { data = null; }
        if (!res.ok) {
            const msg = (data && data.error) ? data.error : ('Request failed (' + res.status + ')');
            const err = new Error(msg);
            err.status = res.status;
            throw err;
        }
        return data;
    }

    function readCache() {
        try {
            const raw = localStorage.getItem(CACHE_KEY);
            return raw ? JSON.parse(raw) : null;
        } catch (e) {
            return null;
        }
    }

    function writeCache(bundle) {
        try {
            localStorage.setItem(CACHE_KEY, JSON.stringify(Object.assign({}, bundle, { cachedAt: Date.now() })));
        } catch (e) { /* storage unavailable */ }
    }

    function clearCache() {
        try { localStorage.removeItem(CACHE_KEY); } catch (e) {}
    }

    // Captures ?friend=PRL-XXXXX from the landing URL and strips it cleanly.
    function captureFriendInviteFromUrl() {
        if (typeof window === 'undefined' || !window.location || !window.location.search) return null;
        try {
            const params = new URLSearchParams(window.location.search);
            const raw = params.get('friend');
            if (!raw) return null;
            const code = raw.trim().toUpperCase();
            params.delete('friend');
            const qs = params.toString();
            const cleanUrl = window.location.pathname + (qs ? '?' + qs : '') + (window.location.hash || '');
            if (window.history && typeof window.history.replaceState === 'function') {
                window.history.replaceState({}, '', cleanUrl);
            }
            if (/^PRL-[A-Z0-9]{4,8}$/.test(code)) {
                try { sessionStorage.setItem(INVITE_SESSION_KEY, code); } catch (e) {}
                return code;
            }
        } catch (e) { /* ignore malformed URL */ }
        return null;
    }

    function getPendingInvite() {
        try { return sessionStorage.getItem(INVITE_SESSION_KEY) || ''; } catch (e) { return ''; }
    }

    function clearPendingInvite() {
        try { sessionStorage.removeItem(INVITE_SESSION_KEY); } catch (e) {}
    }

    function inviteUrlFor(friendCode) {
        const origin = (typeof window !== 'undefined' && window.location && window.location.origin && window.location.origin.startsWith('http'))
            ? window.location.origin
            : 'https://parlour.me.uk';
        return origin + '/?friend=' + encodeURIComponent(friendCode);
    }

    async function getProfile() {
        return _api('/social/profile', 'GET');
    }

    async function saveProfile(opts) {
        const payload = Object.assign({ activeCourse: _activeCourse() }, opts || {});
        const res = await _api('/social/profile', 'POST', payload);
        return res;
    }

    async function getFriends() {
        return _api('/social/friends', 'GET');
    }

    async function requestFriend(friendCode) {
        return _api('/social/friends/request', 'POST', { friendCode: String(friendCode || '').trim().toUpperCase() });
    }

    async function respondFriend(userId, action) {
        return _api('/social/friends/respond', 'POST', { userId, action });
    }

    async function removeFriend(userId) {
        return _api('/social/friends/remove', 'POST', { userId });
    }

    async function getLeaderboard() {
        return _api('/social/leaderboard?scope=friends', 'GET');
    }

    async function getQuests() {
        return _api('/social/quests', 'GET');
    }

    async function startQuest(friendId, questType) {
        return _api('/social/quests/start', 'POST', { friendId, questType });
    }

    async function autoMatchQuest(questType) {
        return _api('/social/quests/auto-match', 'POST', { questType });
    }

    async function respondQuest(questId, action) {
        return _api('/social/quests/respond', 'POST', { questId, action });
    }

    async function sendCheer(questId) {
        return _api('/social/quests/cheer', 'POST', { questId });
    }

    async function loadDashboard() {
        const profileRes = await getProfile();
        if (!profileRes.optedIn) {
            const bundle = {
                optedIn: false,
                profile: profileRes.profile,
                weekKey: profileRes.weekKey,
                pendingFriendRequests: profileRes.pendingFriendRequests || 0,
                pendingQuestInvites: profileRes.pendingQuestInvites || 0,
                friendsData: { friends: [], incoming: [], outgoing: [] },
                leaderboard: { entries: [], dailyCap: 120 },
                quests: { currentQuest: null, lastWeekCompleted: null, questTypes: [] }
            };
            writeCache(bundle);
            return bundle;
        }

        const [friendsData, leaderboard, quests] = await Promise.all([
            getFriends(),
            getLeaderboard(),
            getQuests()
        ]);

        const bundle = {
            optedIn: true,
            profile: profileRes.profile,
            weekKey: profileRes.weekKey,
            pendingFriendRequests: profileRes.pendingFriendRequests || 0,
            pendingQuestInvites: profileRes.pendingQuestInvites || 0,
            friendsData,
            leaderboard,
            quests
        };
        writeCache(bundle);
        return bundle;
    }

    function initialsFor(name) {
        const clean = String(name || 'L').trim();
        const parts = clean.split(/\s+/).filter(Boolean);
        if (parts.length >= 2) {
            return (parts[0][0] + parts[1][0]).toUpperCase();
        }
        return clean.slice(0, 2).toUpperCase();
    }

    const api = {
        captureFriendInviteFromUrl,
        getPendingInvite,
        clearPendingInvite,
        inviteUrlFor,
        readCache,
        clearCache,
        getProfile,
        saveProfile,
        getFriends,
        requestFriend,
        respondFriend,
        removeFriend,
        getLeaderboard,
        getQuests,
        startQuest,
        autoMatchQuest,
        respondQuest,
        sendCheer,
        loadDashboard,
        initialsFor
    };

    if (typeof window !== 'undefined') window.Social = api;
    if (typeof module !== 'undefined' && module.exports) module.exports = api;

    return api;
})();
