// ============================================
// LOCAL DETERMINISTIC GRADER
// ============================================
// Computes instant, 100% deterministic, offline statistics for learner production:
// - Word count, sentence count, paragraph count
// - Average sentence length
// - Target word count verification based on CEFR level & task requirements
// - Type-token ratio (lexical diversity)
// - Basic structural checks (capitalization, ending punctuation, paragraphing)

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.LocalGrader = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    // Standard CEFR target word ranges for extended writing tasks
    const CEFR_TARGET_RANGES = {
        A1: { min: 25, idealMin: 35, idealMax: 60, max: 100 },
        A2: { min: 50, idealMin: 70, idealMax: 120, max: 180 },
        B1: { min: 100, idealMin: 130, idealMax: 200, max: 280 },
        B2: { min: 160, idealMin: 200, idealMax: 300, max: 400 },
        C1: { min: 250, idealMin: 320, idealMax: 450, max: 600 },
        C2: { min: 350, idealMin: 450, idealMax: 650, max: 900 }
    };

    /**
     * Clean and split text into words across Latin, accented, and extended character sets.
     */
    function tokenizeWords(text) {
        if (!text || typeof text !== 'string') return [];
        // Matches Unicode words including accents and hyphens inside words
        const matches = text.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu);
        return matches || [];
    }

    /**
     * Split text into sentences using sentence-terminating punctuation.
     */
    function tokenizeSentences(text) {
        if (!text || typeof text !== 'string') return [];
        // Split on ., !, ?, or newlines followed by whitespace/capital letter
        const cleaned = text.trim();
        if (!cleaned) return [];
        const raw = cleaned.split(/(?<=[.!?¿¡])\s+|\n+/);
        return raw.map(s => s.trim()).filter(s => s.length > 0 && /[\p{L}\p{N}]/u.test(s));
    }

    /**
     * Split text into paragraphs.
     */
    function tokenizeParagraphs(text) {
        if (!text || typeof text !== 'string') return [];
        return text.split(/\n\s*\n/).map(p => p.trim()).filter(p => p.length > 0);
    }

    /**
     * Analyze production text deterministically.
     */
    function analyze(productionText, options) {
        const opts = options || {};
        const text = String(productionText || '').trim();
        const cefrLevel = (opts.cefrLevel || 'B2').toUpperCase();

        const words = tokenizeWords(text);
        const sentences = tokenizeSentences(text);
        const paragraphs = tokenizeParagraphs(text);

        const wordCount = words.length;
        const sentenceCount = Math.max(1, sentences.length);
        const paragraphCount = Math.max(1, paragraphs.length);
        const avgSentenceLength = Math.round((wordCount / sentenceCount) * 10) / 10;

        // Lexical diversity: Type-Token Ratio (unique lemmas/words / total words)
        const uniqueWords = new Set(words.map(w => w.toLowerCase()));
        const ttr = wordCount > 0 ? Math.round((uniqueWords.size / wordCount) * 100) / 100 : 0;

        // Target length compliance
        const target = CEFR_TARGET_RANGES[cefrLevel] || CEFR_TARGET_RANGES.B2;
        let targetWordCountMet = true;
        let lengthFeedback = 'Length is appropriate for the target level.';

        if (wordCount < target.min) {
            targetWordCountMet = false;
            lengthFeedback = `Text is shorter than expected for ${cefrLevel} (minimum ${target.min} words, ideally ${target.idealMin}-${target.idealMax}).`;
        } else if (wordCount < target.idealMin) {
            lengthFeedback = `Slightly brief for ${cefrLevel} (target: ${target.idealMin}-${target.idealMax} words).`;
        } else if (wordCount > target.max) {
            lengthFeedback = `Text exceeds recommended maximum for ${cefrLevel} (${target.max} words).`;
        }

        // Structural checks
        const startsWithCapital = /^\p{Lu}/u.test(text);
        const endsWithPunctuation = /[.!?]$/.test(text);

        return {
            wordCount,
            uniqueWordCount: uniqueWords.size,
            sentenceCount,
            paragraphCount,
            avgSentenceLength,
            ttr,
            cefrLevel,
            targetRange: target,
            targetWordCountMet,
            lengthFeedback,
            structuralChecks: {
                startsWithCapital,
                endsWithPunctuation,
                hasMultipleParagraphs: paragraphCount > 1
            }
        };
    }

    return {
        analyze,
        tokenizeWords,
        tokenizeSentences,
        tokenizeParagraphs,
        CEFR_TARGET_RANGES
    };
});
