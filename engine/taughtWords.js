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
    function isReached(lemma) {
        if (!_index) return false; // load() not called yet — fail closed, not open
        const lessonId = _index[lemma];
        if (!lessonId) return false;
        return (typeof LearnerPath !== 'undefined' && LearnerPath.isComplete) ? LearnerPath.isComplete(lessonId) : false;
    }

    return { load, isReached };
})();

if (typeof window !== 'undefined') {
    window.TaughtWords = TaughtWords;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TaughtWords;
}
