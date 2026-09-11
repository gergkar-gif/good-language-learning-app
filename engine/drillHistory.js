// ============================================
// DRILL HISTORY — session-accuracy signal for drillers with no other one
// ============================================
// Grammar and vocabulary already have a real competence signal via
// engine/learnerModel.js (SM-2 ease from recycle-schedule/srsDeck review
// history). Every other driller — Verb Speed, Translation, Listening, and
// the four Hungarian-specific drillers (suffix/prefix/morphology/verb) —
// has none: they're stateless session runners with no persisted evidence
// at all. This is a small, generic, id-keyed store any of those can write
// a session result to, and a matching weak/developing/strong classifier
// from repeated accuracy — "if someone keeps scoring 50% on a drill, that
// is quite weak; if they keep scoring 90%, they are clearly good."
//
// Deliberately NOT a generalization of engine/verbs/leaderboard.js's
// verbSpeedScores — that's a ranked best-of list (sorted by accuracy,
// capped top 20, "personal best" framing), the wrong shape for
// classification, which needs a chronological recency window instead
// ("keeps scoring" means recent-in-a-row, not all-time best). Both stores
// exist in parallel; verb-speed writes to this one too, alongside its own
// unchanged leaderboard.

const DrillHistory = (function () {
    'use strict';

    const MAX_SESSIONS = 10;           // stored, most-recent-first
    const CLASSIFY_WINDOW = 5;         // most recent N sessions used for the signal
    const MIN_SESSIONS = 3;            // fewer than this -> no signal yet, same
                                        // "don't call it a trend off too little
                                        // data" reasoning as LearnerModel's
                                        // MIN_REVIEWED_WORDS
    const WEAK_ACCURACY_CEILING = 60;  // % average over the window
    const STRONG_ACCURACY_FLOOR = 85;

    function storageKey(drillerId) {
        return Lang.key('drillHistory:' + drillerId);
    }

    function all(drillerId) {
        try {
            return JSON.parse(localStorage.getItem(storageKey(drillerId)) || '[]');
        } catch (error) {
            return [];
        }
    }

    // Records one finished session. Zero-question sessions are ignored —
    // an aborted or empty run carries no accuracy signal, same guard
    // VerbsLeaderboard.record() already applies.
    function record(drillerId, session) {
        const correct = session.correct || 0;
        const wrong = session.wrong || 0;
        const total = correct + wrong;
        if (!total) return;

        const entry = {
            date: new Date().toISOString(),
            correct,
            wrong,
            accuracy: Math.round((correct / total) * 100)
        };

        const history = [entry, ...all(drillerId)].slice(0, MAX_SESSIONS);
        try {
            localStorage.setItem(storageKey(drillerId), JSON.stringify(history));
        } catch (error) {
            // Private browsing with storage disabled — the signal just won't
            // persist this session, same tradeoff other stores accept.
        }
    }

    // The classification from the most recent CLASSIFY_WINDOW sessions —
    // null state (not a fourth "not-yet-seen" string, since a driller with
    // fewer than MIN_SESSIONS genuinely has no signal to report yet, unlike
    // LearnerModel's skills/words which distinguish "never attempted" from
    // "not enough attempts") until there's enough real data to trust.
    // Thresholds are on accuracy's own scale (a closed-form multiple-choice/
    // fill-blank floor from guessing), not reused from LearnerModel's ease
    // cutoffs, which measure a different thing (SM-2 ease, 1.3-3.0).
    function classify(drillerId) {
        const sessions = all(drillerId).slice(0, CLASSIFY_WINDOW);
        if (sessions.length < MIN_SESSIONS) {
            return { state: null, sessions: sessions.length, avgAccuracy: null };
        }

        const avgAccuracy = Math.round(
            sessions.reduce((sum, s) => sum + s.accuracy, 0) / sessions.length
        );

        let state;
        if (avgAccuracy < WEAK_ACCURACY_CEILING) state = 'weak';
        else if (avgAccuracy < STRONG_ACCURACY_FLOOR) state = 'developing';
        else state = 'strong';

        return { state, sessions: sessions.length, avgAccuracy };
    }

    return { record, classify };
})();
