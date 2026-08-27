// Personal best-tracking for the Verb Speed drill — not a competitive,
// multi-player leaderboard (this app has no accounts to rank against each
// other), but a persisted history of past sessions so a learner can see
// their own best accuracy and correct count over time, per course
// (Lang.key(), same as every other persisted feature — Spanish and
// Hungarian verb history must never mix).
const VerbsLeaderboard = (function () {
    'use strict';

    // Keeps the store small and relevant — a ranked top list, not an
    // ever-growing log. Sessions that fall out of the top 20 by accuracy
    // are simply forgotten.
    var MAX_ENTRIES = 20;

    function storageKey() {
        return Lang.key('verbSpeedScores');
    }

    function all() {
        try {
            var raw = localStorage.getItem(storageKey());
            var list = raw ? JSON.parse(raw) : [];
            return Array.isArray(list) ? list : [];
        } catch (error) {
            return [];
        }
    }

    // Best accuracy on record before this call — the caller compares its
    // own new entry against this to decide whether to show "New personal
    // best!", so it must be read before record() mutates the store.
    function best() {
        var list = all();
        return list.length ? list[0] : null;
    }

    // A session with zero answered questions (timer ran out before the
    // first submit, or Change Settings was hit immediately) isn't a real
    // result and shouldn't count toward or dilute the best-of list.
    function record(entry) {
        if (!entry || (entry.correct + entry.wrong) <= 0) return best();

        var list = all();
        list.push({
            date: entry.date || Date.now(),
            correct: entry.correct,
            wrong: entry.wrong,
            accuracy: entry.accuracy,
            tenseLabel: entry.tenseLabel || '',
            timerMinutes: entry.timerMinutes || null
        });

        // Ranked by accuracy first, then by correct count as a tiebreak —
        // a 100% streak of 3 shouldn't outrank a 95% streak of 40.
        list.sort(function (a, b) {
            if (b.accuracy !== a.accuracy) return b.accuracy - a.accuracy;
            return b.correct - a.correct;
        });
        list = list.slice(0, MAX_ENTRIES);

        try {
            localStorage.setItem(storageKey(), JSON.stringify(list));
        } catch (error) {
            // Private browsing with storage disabled: the session's own
            // results screen still shows fine, it just won't be remembered.
        }
        return list.length ? list[0] : null;
    }

    return { all: all, best: best, record: record };
})();
