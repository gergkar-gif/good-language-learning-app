// ============================================
// PRODUCTION CHECK: offline quick check of written / spoken answers
// ============================================
// The level tests and CEFR mock exams ask for a short piece of writing and a
// short spoken answer. Nothing offline can judge whether that text is good
// language; the AI grader (engine/grader/) is the only thing that reads it.
// This module is the fallback when the grader is unreachable, and it is built
// so that the cheap ways of fooling a word counter earn nothing:
//
//   - a word repeated over and over counts at most MAX_REPEATS times, and
//     a three-word sequence that has already appeared does not count again
//     (so a list of phrases pasted three times is not 3x the words);
//   - a run of COPY_RUN or more words lifted from the test's own texts
//     (prompt, reading passage, listening transcript) does not count;
//   - target phrases match from the start of a word, in order ("era" does
//     not match "primera"). A phrase word of STEM_MIN or more letters may
//     take an ending ("tapasztalat" matches "tapasztalatom", "visita"
//     matches "visitamos"), because Hungarian, Polish and Czech targets are
//     written as stems; shorter ones ("si", "era", "és") must match exactly.
//     Phrases only score once the text is long enough to be an answer
//     rather than a list of the phrases;
//   - an answer written mostly in English scores nothing.
//
// It still cannot tell a fluent answer from fluent nonsense, which is why
// the level tests no longer count production in the pass mark at all
// (user decision 2026-11-25): this score is feedback.

(function (root, factory) {
    if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.ProductionCheck = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    const MAX_REPEATS = 3;
    const COPY_RUN = 6;
    const ENGLISH_SHARE = 0.15;
    const STEM_MIN = 5;

    // English function words that are not also common words in the course
    // languages (so no "a", "i", "to", "on", "is", "be", "he", "has", "in",
    // "my" (Polish/Czech "we") or "but" (French "goal")).
    const ENGLISH_MARKERS = new Set([
        'the', 'and', 'you', 'she', 'they', 'your', 'with', 'this', 'that',
        'were', 'was', 'have', 'will', 'of', 'not', 'are', 'for', 'it',
        'we', 'our', 'there', 'what', 'when', 'would', 'because', 'very'
    ]);

    function fold(text) {
        return String(text || '')
            .toLowerCase()
            .normalize('NFD')
            .replace(/[̀-ͯ]/g, '');
    }

    function tokens(text) {
        return fold(text).match(/[\p{L}\p{N}]+(?:['’-][\p{L}\p{N}]+)*/gu) || [];
    }

    function tokenMatches(textTok, phraseTok) {
        if (textTok === phraseTok) return true;
        return phraseTok.length >= STEM_MIN && textTok.startsWith(phraseTok);
    }

    // In-order match of a target phrase, word by word.
    function hasPhrase(textTokens, phrase) {
        const p = tokens(phrase);
        if (!p.length) return false;
        outer:
        for (let i = 0; i + p.length <= textTokens.length; i++) {
            for (let j = 0; j < p.length; j++) {
                if (!tokenMatches(textTokens[i + j], p[j])) continue outer;
            }
            return true;
        }
        return false;
    }

    function matchPhrases(text, phrases) {
        const t = tokens(text);
        return (phrases || []).filter(p => hasPhrase(t, p));
    }

    // Indices of text tokens that sit inside a COPY_RUN-word run also found
    // in one of the source texts.
    function copiedIndices(textTokens, sourceTexts) {
        const grams = new Set();
        (sourceTexts || []).forEach(src => {
            const s = tokens(src);
            for (let i = 0; i + COPY_RUN <= s.length; i++) {
                grams.add(s.slice(i, i + COPY_RUN).join(' '));
            }
        });
        const copied = new Set();
        if (!grams.size) return copied;
        for (let i = 0; i + COPY_RUN <= textTokens.length; i++) {
            if (grams.has(textTokens.slice(i, i + COPY_RUN).join(' '))) {
                for (let j = i; j < i + COPY_RUN; j++) copied.add(j);
            }
        }
        return copied;
    }

    function countSentences(text) {
        return String(text || '')
            .split(/[.!?¿¡\n]+/)
            .filter(seg => tokens(seg).length >= 3)
            .length;
    }

    /**
     * analyse(text, task, opts) -> breakdown with a 0..3 score.
     *   task:  { minWords, targetKeywords }
     *   opts:  { modality: 'written' | 'oral', sourceTexts: [string] }
     */
    function analyse(text, task, opts) {
        const o = opts || {};
        const t = task || {};
        const oral = o.modality === 'oral';
        const all = tokens(text);
        const copied = copiedIndices(all, o.sourceTexts);

        // Tokens inside a repeat of an earlier three-word sequence.
        const repeatedRun = new Set();
        const trigrams = new Set();
        for (let i = 0; i + 3 <= all.length; i++) {
            const g = all.slice(i, i + 3).join(' ');
            if (trigrams.has(g)) { repeatedRun.add(i); repeatedRun.add(i + 1); repeatedRun.add(i + 2); }
            else trigrams.add(g);
        }

        const seen = Object.create(null);
        let effective = 0;
        let repeated = 0;
        all.forEach((tok, i) => {
            if (copied.has(i)) return;
            if (repeatedRun.has(i)) { repeated++; return; }
            seen[tok] = (seen[tok] || 0) + 1;
            if (seen[tok] <= MAX_REPEATS) effective++;
            else repeated++;
        });

        const englishHits = all.filter(tok => ENGLISH_MARKERS.has(tok)).length;
        const notTargetLanguage = all.length >= 5 && englishHits / all.length >= ENGLISH_SHARE;

        const required = t.minWords || (oral ? 15 : 20);
        const matched = matchPhrases(text, t.targetKeywords);
        const sentences = countSentences(text);
        const longEnough = effective >= required * 0.6;

        let lenPts = effective >= required ? 1 : (longEnough ? 0.5 : 0);
        let kwPts = !longEnough ? 0 : (matched.length >= 2 ? 1 : (matched.length >= 1 ? 0.5 : 0));
        let structPts = oral
            ? (effective >= 15 ? 1 : (effective >= 8 ? 0.5 : 0))
            : ((sentences >= 2 && effective >= 10) ? 1 : ((sentences >= 1 && effective >= 6) ? 0.5 : 0));

        const notes = [];
        if (notTargetLanguage) {
            lenPts = kwPts = structPts = 0;
            notes.push('Much of this answer looks like English, so it was not scored.');
        }
        if (copied.size) notes.push(`${copied.size} words copied from the test's own texts were not counted.`);
        if (repeated) notes.push(`${repeated} repeated words were not counted.`);
        if (matched.length && !longEnough && !notTargetLanguage) {
            notes.push('Target phrases only count inside an answer of the required length.');
        }

        return {
            words: all.length,
            effectiveWords: effective,
            distinctWords: Object.keys(seen).length,
            requiredWords: required,
            sentences: sentences,
            matchedKeywords: matched,
            copiedWords: copied.size,
            repeatedWords: repeated,
            notTargetLanguage: notTargetLanguage,
            score: Math.min(3, lenPts + kwPts + structPts),
            max: 3,
            notes: notes
        };
    }

    return { analyse, matchPhrases, tokens, fold, MAX_REPEATS, COPY_RUN };
});
