// ============================================
// VERB STATS — Pure data tracking, no DOM, no globals
// ============================================

const VerbsStats = (function () {
    'use strict';

    let _data;

    function _empty() {
        return { correct: 0, wrong: 0, byTense: {}, byPerson: {} };
    }

    /** Reset all statistics. */
    function init() {
        _data = _empty();
    }

    /**
     * Record a single answer.
     * @param {boolean} isCorrect
     * @param {string}  tense   Display label e.g. "Present"
     * @param {string}  person  Display label e.g. "yo"
     */
    function record(isCorrect, tense, person) {
        if (isCorrect) { _data.correct++; } else { _data.wrong++; }

        if (!_data.byTense[tense]) _data.byTense[tense] = { correct: 0, wrong: 0 };
        if (isCorrect) { _data.byTense[tense].correct++; } else { _data.byTense[tense].wrong++; }

        if (!_data.byPerson[person]) _data.byPerson[person] = { correct: 0, wrong: 0 };
        if (isCorrect) { _data.byPerson[person].correct++; } else { _data.byPerson[person].wrong++; }
    }

    /** Accuracy as a whole-number percentage. Returns 0 when no answers. */
    function getAccuracy() {
        var total = _data.correct + _data.wrong;
        return total === 0 ? 0 : Math.round((_data.correct / total) * 100);
    }

    /**
     * Return the key with the lowest accuracy in the given map.
     * Returns null when every bucket is empty.
     */
    function _weakest(map) {
        var weakest = null;
        var worst = Infinity;
        var keys = Object.keys(map);
        for (var i = 0; i < keys.length; i++) {
            var c = map[keys[i]];
            var total = c.correct + c.wrong;
            if (total === 0) continue;
            var acc = c.correct / total;
            if (acc < worst) { worst = acc; weakest = keys[i]; }
        }
        return weakest;
    }

    /**
     * Snapshot of current statistics.
     * @returns {{ correct:number, wrong:number, accuracy:number,
   *             weakestTense:string, weakestPerson:string }}
     */
    function getStats() {
        return {
            correct:      _data.correct,
            wrong:        _data.wrong,
            accuracy:     getAccuracy(),
            weakestTense: _weakest(_data.byTense) || '\u2014',
            weakestPerson: _weakest(_data.byPerson) || '\u2014'
        };
    }

    return { init: init, record: record, getStats: getStats };
})();
