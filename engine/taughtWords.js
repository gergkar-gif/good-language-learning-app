// ============================================
// TAUGHT WORDS
// ============================================
// A shared "has this lemma actually been taught yet" check, backed by
// content/<lang>/indexes/word-lesson-index.json (lemma -> the lesson that
// first introduces it) — the same index engine/drills/vocabulary.js has
// filtered its own pool through since bug report #151 (2026-09-16), though
// that module's own _isReached() stays separate (see isReached()'s own
// comment on why this module's fail-open/closed default differs from it).
// Backs an opt-in "only words from my lessons" toggle on the drillers that
// deliberately draw from the full dictionary by default (Verb/Suffix/
// Prefix/Morphology Driller, Hungarian and Spanish — see each one's own
// header comment) — restricting to taught words has to be something the
// learner asks for there, not silent default behaviour.

const TaughtWords = (function () {
    'use strict';

    let _index = null;       // lemma -> lessonId
    let _indexLang = null;

    async function load() {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : null;
        if (_index && _indexLang === lang) return;
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') { _index = {}; return; }
        const data = await Content.json(Lang.content('indexes/word-lesson-index.json')).catch(() => ({ byLemma: {} }));
        _index = data.byLemma || {};
        _indexLang = lang;
    }

    // Deliberately fail CLOSED, unlike vocabulary.js's own _isReached() —
    // that one lets an indexless lemma through because it's an always-on
    // background filter over a pool already scoped to "words with a real
    // example sentence at this CEFR level," so a little slack there is
    // harmless. This module backs an opt-in "only words from my lessons"
    // toggle over the dictionary-wide drillers (hu-verb, hu-suffix, etc.),
    // where the whole point is a strict guarantee — checked empirically
    // (2026-09-23): only ~28% of hu-verb's candidate verbs have any
    // word-lesson-index entry at all, so failing open here would leave the
    // toggle barely restricting anything, defeating its own purpose. A
    // lemma with no entry counts as NOT yet encountered.
    const ACCENTED_IR = {
        oir: 'o\u00edr',
        reir: 're\u00edr',
        sonreir: 'sonre\u00edr',
        freir: 'fre\u00edr'
    };

    function _variants(raw) {
        const clean = String(raw || '').trim().toLowerCase();
        if (!clean) return [];
        const set = new Set([clean]);
        if (clean.indexOf('ny') !== -1) set.add(clean.replace(/ny/g, '\u00f1'));
        if (ACCENTED_IR[clean]) set.add(ACCENTED_IR[clean]);
        for (const base of Array.from(set)) {
            if (base.endsWith('se') && base.length > 4) {
                set.add(base.slice(0, -2));
                if (ACCENTED_IR[base.slice(0, -2)]) set.add(ACCENTED_IR[base.slice(0, -2)]);
            } else if (/(?:ar|er|ir|\u00edr)$/.test(base)) {
                set.add(base + 'se');
            }
        }
        return Array.from(set);
    }

    function _inKnownOrSrs(candidates) {
        if (typeof knownWords !== 'undefined' && Array.isArray(knownWords)) {
            for (let i = 0; i < knownWords.length; i++) {
                const w = knownWords[i];
                const t = String((w && (w.spanish || w.lemma || w.target)) || '').trim().toLowerCase();
                if (t && candidates.indexOf(t) !== -1) return true;
            }
        }
        if (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) {
            for (let i = 0; i < srsDeck.length; i++) {
                const c = srsDeck[i];
                if (!c || !(c.reviews > 0 || c.lapses > 0)) continue;
                const t = String(c.spanish || c.lemma || c.target || '').trim().toLowerCase();
                if (t && candidates.indexOf(t) !== -1) return true;
            }
        }
        return false;
    }

    function isReached(lemma) {
        if (!lemma) return false;
        const candidates = _variants(lemma);
        if (!candidates.length) return false;
        if (_inKnownOrSrs(candidates)) return true;
        if (!_index) return false; // load() not called yet — fail closed, not open

        const canCheckLesson = (typeof LearnerPath !== 'undefined' && typeof LearnerPath.isComplete === 'function');
        if (!canCheckLesson) return false;

        for (let i = 0; i < candidates.length; i++) {
            const cand = candidates[i];
            let lessonId = _index[cand];
            if (!lessonId) {
                // Check with common gendered articles in Spanish or Hungarian
                lessonId = _index['el ' + cand] || _index['la ' + cand] || _index['los ' + cand] || _index['las ' + cand];
            }
            if (!lessonId && (cand.startsWith('el ') || cand.startsWith('la '))) {
                lessonId = _index[cand.slice(3)];
            }
            if (lessonId && LearnerPath.isComplete(lessonId)) return true;
        }
        return false;
    }

    function reachedVerbs(pool) {
        if (Array.isArray(pool)) return pool.filter(v => isReached(v));
        if (typeof ALL_VERBS !== 'undefined' && Array.isArray(ALL_VERBS)) {
            return ALL_VERBS.filter(v => isReached(v));
        }
        if (!_index || typeof LearnerPath === 'undefined' || typeof LearnerPath.isComplete !== 'function') return [];
        const isHu = _indexLang === 'hu';
        const out = [];
        Object.keys(_index).forEach(lemma => {
            if (!LearnerPath.isComplete(_index[lemma])) return;
            if (isHu) {
                if (lemma.indexOf(' ') === -1) out.push(lemma);
            } else if (/^[a-z\u00e1\u00e9\u00ed\u00f3\u00fa\u00fc\u00f1]+(?:ar|er|ir|\u00edr)(?:se)?$/i.test(lemma) && lemma !== 'mujer' && lemma !== 'taller' && lemma !== 'placer') {
                out.push(lemma.replace(/\u00f1/g, 'ny').replace(/\u00edr$/, 'ir'));
            }
        });
        return out;
    }

    return { load, isReached, reachedVerbs };
})();

if (typeof window !== 'undefined') {
    window.TaughtWords = TaughtWords;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TaughtWords;
}
