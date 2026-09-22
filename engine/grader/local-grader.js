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

        // Structural checks (irrelevant for oral transcripts produced by ASR)
        const isOral = opts.modality === 'oral';
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
            structuralChecks: isOral ? {
                startsWithCapital: true,
                endsWithPunctuation: true,
                hasMultipleParagraphs: false,
                isOral: true
            } : {
                startsWithCapital,
                endsWithPunctuation,
                hasMultipleParagraphs: paragraphCount > 1
            }
        };
    }

    /**
     * Validate a single conversational turn transcript against turn criteria.
     * Used for zero-latency turn-level feedback in Option B.
     * @param {string} transcript - Speech-to-text transcript of learner's reply
     * @param {object} criteria - { minWords, targetKeywords, requiredConcepts }
     * @returns {object} { valid: boolean, wordCount: number, matchedKeywords: string[], feedback: string }
     */
    function validateTurn(transcript, criteria) {
        const text = String(transcript || '').trim();
        const words = tokenizeWords(text);
        const crit = criteria || {};
        const minWords = typeof crit.minWords === 'number' ? crit.minWords : 2;
        const targetKeywords = Array.isArray(crit.targetKeywords) ? crit.targetKeywords : [];

        // Normalise transcript for keyword matching (lowercase, accent-folding)
        const normalisedText = text.toLowerCase()
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '');

        const matchedKeywords = [];
        for (const kw of targetKeywords) {
            const normKw = String(kw).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
            if (normalisedText.includes(normKw)) {
                matchedKeywords.push(kw);
            }
        }

        const hasMinWords = words.length >= minWords;
        const matchedKeywordRequirement = targetKeywords.length === 0 || matchedKeywords.length > 0 || words.length >= (minWords + 3);
        const valid = hasMinWords && matchedKeywordRequirement;

        let feedback = 'Turn completed successfully.';
        if (!hasMinWords) {
            feedback = `Spoken response was very short (${words.length} word${words.length === 1 ? '' : 's'}). Try to speak in a full phrase or sentence.`;
        } else if (!matchedKeywordRequirement) {
            feedback = `Good attempt, but make sure to address the specific request in the prompt.`;
        } else if (matchedKeywords.length > 0) {
            feedback = `Understood! Good use of target terms: ${matchedKeywords.slice(0, 3).join(', ')}.`;
        }

        return {
            valid,
            wordCount: words.length,
            matchedKeywords,
            feedback
        };
    }

    /**
     * Complete deterministic evaluation of an entire conversation scenario (offline fallback).
     * @param {Array} completedTurns - [{ turnIndex, interlocutorPrompt, learnerCue, learnerTranscript, validation }]
     * @param {object} scenario - The scenario metadata { title, cefrLevel, targetSkills, roleplay }
     * @returns {object} Schema-compliant evaluation object with overallScore, dimensions, and feedback
     */
    function gradeConversation(completedTurns, scenario, options) {
        const turns = Array.isArray(completedTurns) ? completedTurns : [];
        const sc = scenario || {};
        const opts = options || {};
        const isWritten = opts.modality === 'written' || sc.modality === 'written' ||
            opts.taskType === 'written_exchange' || sc.taskType === 'written_exchange';
        const level = (sc.cefrLevel || 'A1').toUpperCase();

        let totalWords = 0;
        let validTurns = 0;
        let allMatchedKeywords = [];

        for (const t of turns) {
            const words = tokenizeWords(t.learnerTranscript || '');
            totalWords += words.length;
            if (t.validation && t.validation.valid) {
                validTurns++;
            }
            if (t.validation && Array.isArray(t.validation.matchedKeywords)) {
                allMatchedKeywords = allMatchedKeywords.concat(t.validation.matchedKeywords);
            }
        }

        const totalTurns = Math.max(1, turns.length);
        const turnCompletionRate = validTurns / totalTurns;

        let score = Math.round(50 + (turnCompletionRate * 35));
        if (totalWords >= totalTurns * 5) score += 10;
        else if (totalWords >= totalTurns * 3) score += 5;
        score = Math.min(95, Math.max(40, score));

        const taskComp = Math.round(turnCompletionRate * 10) / 10;
        const fluency = Math.min(1.0, Math.round((0.6 + (totalWords / (totalTurns * 10)) * 0.4) * 10) / 10);
        const vocabScore = Math.min(1.0, Math.round((0.6 + (allMatchedKeywords.length / Math.max(1, totalTurns * 1.5)) * 0.4) * 10) / 10);
        const grammarScore = Math.min(1.0, Math.round((0.7 + (turnCompletionRate * 0.25)) * 10) / 10);

        const targetSkills = Array.isArray(sc.targetSkills) ? sc.targetSkills : (isWritten ? ['written_interaction', 'social_exchange'] : ['social_interaction', 'oral_fluency']);
        const demonstratedSkills = targetSkills.map(s => ({
            skillId: typeof s === 'string' ? s : (s.id || (isWritten ? 'written_skill' : 'oral_skill')),
            confidence: turnCompletionRate >= 0.8 ? 0.85 : 0.65
        }));

        const strengths = [
            `Completed ${validTurns} of ${totalTurns} ${isWritten ? 'written exchange' : 'conversational'} turns with appropriate communicative intent.`,
            `Demonstrated responsive ${isWritten ? 'written correspondence' : 'conversational turn-taking'} in the role of ${sc.roleplay ? sc.roleplay.learnerRole : (isWritten ? 'the writer' : 'the speaker')}.`
        ];
        if (allMatchedKeywords.length > 0) {
            strengths.push(`Used relevant situational vocabulary: ${[...new Set(allMatchedKeywords)].slice(0, 4).join(', ')}.`);
        }

        const priorities = [];
        if (turnCompletionRate < 1.0) {
            priorities.push(`Address each prompt's specific requirement directly to ensure complete communicative task achievement.`);
        }
        priorities.push(isWritten
            ? `Continue practicing situational written correspondence with natural openings, appropriate register, and accurate diacritics`
            : `Continue practicing spontaneous oral turn-taking with polite openers and situational formulas`);

        const oneLineCoachNote = turnCompletionRate >= 0.8
            ? (isWritten
                ? `Solid written exchange! You communicated clearly and met each message objective effectively.`
                : `Solid roleplay performance! You handled all the key transactions naturally and communicatively.`)
            : `Good communicative effort. Focus on providing complete, direct responses to each prompt.`;

        return {
            overallScore: score,
            cefrLevel: level,
            taskCompletion: taskComp,
            dimensionScores: {
                taskCompletion: taskComp,
                fluency,
                vocabulary: vocabScore,
                grammar: grammarScore,
                coherence: 0.8,
                naturalness: 0.8
            },
            strengths,
            priorities,
            errors: [],
            demonstratedSkills,
            weakSkills: turnCompletionRate < 0.7 ? [{ skillId: targetSkills[0] || (isWritten ? 'written_interaction' : 'oral_interaction'), confidence: 0.6 }] : [],
            examinerFeedback: `In this ${level} ${isWritten ? 'written exchange' : 'oral roleplay'} (${sc.title || (isWritten ? 'Written Exchange' : 'Conversation Scenario')}), the ${isWritten ? 'writer' : 'speaker'} completed ${validTurns}/${totalTurns} turns with an average of ${Math.round(totalWords / totalTurns)} words per turn. ${oneLineCoachNote}`,
            _prodOneLineTip: oneLineCoachNote,
            isOfflineFallback: true
        };
    }

    return {
        analyze,
        validateTurn,
        gradeConversation,
        tokenizeWords,
        tokenizeSentences,
        tokenizeParagraphs,
        CEFR_TARGET_RANGES
    };
});
