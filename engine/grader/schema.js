// ============================================
// GRADER OUTPUT SCHEMA VALIDATOR & CLEANER
// ============================================
// Validates, normalizes, and sanitizes model output.
// Ensures complete resilience against minor LLM schema variances.

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.GraderSchema = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    const DIMENSIONS = ['grammar', 'vocabulary', 'coherence', 'complexity', 'naturalness'];
    const REQUIRED_FIELDS = [
        'overallScore', 'taskCompletion', 'dimensions',
        'errors', 'demonstratedSkills', 'weakSkills', 'feedback'
    ];

    function clampNumber(value, min, max, defaultValue) {
        if (typeof value !== 'number' || !Number.isFinite(value)) {
            const parsed = Number(value);
            if (!Number.isFinite(parsed)) return defaultValue;
            return Math.max(min, Math.min(max, parsed));
        }
        return Math.max(min, Math.min(max, value));
    }

    function normalizeSkillArray(rawArray, label) {
        if (!Array.isArray(rawArray)) return [];
        const result = [];
        for (const item of rawArray) {
            if (typeof item === 'string' && item.trim()) {
                result.push({ skillId: item.trim(), confidence: 0.8 });
            } else if (item && typeof item === 'object') {
                const id = String(item.skillId || item.id || '').trim();
                if (id) {
                    const confidence = clampNumber(item.confidence, 0, 1, 0.75);
                    result.push({ skillId: id, confidence });
                }
            }
        }
        return result;
    }

    // Builds a fallback priority grounded in the learner's actual submission stats,
    // used only when the model returns neither errors nor priorities to draw from.
    function buildFallbackPriority(localStats) {
        if (!localStats) return 'Keep practicing to build overall accuracy and natural phrasing';
        if (localStats.targetWordCountMet === false) {
            return localStats.lengthFeedback || 'Aim for a longer, more developed response';
        }
        if (typeof localStats.ttr === 'number' && localStats.ttr < 0.5) {
            return 'Vary your word choice more — avoid repeating the same words across sentences';
        }
        if (typeof localStats.avgSentenceLength === 'number' && localStats.avgSentenceLength < 6) {
            return 'Combine short sentences using connectors for more complex structure';
        }
        return 'Keep practicing to build overall accuracy and natural phrasing';
    }

    function validateAndCleanResult(raw, localStats) {
        if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
            throw new Error('Grader result must be a JSON object');
        }

        // Clean and clamp overallScore (0-100)
        const overallScore = Math.round(clampNumber(raw.overallScore, 0, 100, 70));

        // Clean and clamp taskCompletion (0.0-1.0)
        const taskCompletion = Math.round(clampNumber(raw.taskCompletion, 0, 1, overallScore / 100) * 100) / 100;

        // Clean dimensions (written-exchange prompts return them under "dimensionScores")
        const rawDimsSource = raw.dimensions || raw.dimensionScores;
        const rawDims = (rawDimsSource && typeof rawDimsSource === 'object') ? rawDimsSource : {};
        const dimensions = {};
        for (const dim of DIMENSIONS) {
            dimensions[dim] = Math.round(clampNumber(rawDims[dim], 0, 1, overallScore / 100) * 100) / 100;
        }

        // Clean errors array
        const rawErrors = Array.isArray(raw.errors) ? raw.errors : [];
        const errors = [];
        for (const err of rawErrors) {
            if (!err || typeof err !== 'object') continue;
            const text = String(err.text || err.quote || err.fragment || '').trim();
            const explanation = String(err.explanation || err.reason || err.message || '').trim();
            if (!text && !explanation) continue;

            const category = String(err.category || 'grammar').toLowerCase();
            let severity = String(err.severity || 'minor').toLowerCase();
            if (!['minor', 'moderate', 'major'].includes(severity)) {
                severity = severity === 'critical' ? 'major' : 'minor';
            }
            const skillId = err.skillId && typeof err.skillId === 'string' && err.skillId.trim()
                ? err.skillId.trim()
                : null;

            errors.push({
                category,
                severity,
                text,
                explanation,
                skillId
            });
            if (errors.length >= 8) break; // allow up to 8 errors across categories
        }

        // Clean demonstrated and weak skills
        const demonstratedSkills = normalizeSkillArray(raw.demonstratedSkills, 'demonstratedSkills').slice(0, 3);
        const weakSkills = normalizeSkillArray(raw.weakSkills, 'weakSkills').slice(0, 3);

        // Clean feedback
        const rawFeedback = (raw.feedback && typeof raw.feedback === 'object') ? raw.feedback : {};
        const strengths = Array.isArray(rawFeedback.strengths)
            ? rawFeedback.strengths.filter(s => typeof s === 'string' && s.trim()).map(s => s.trim().replace(/[.;,:!]+$/, '')).slice(0, 3)
            : [];
        const priorities = Array.isArray(rawFeedback.priorities)
            ? rawFeedback.priorities.filter(p => typeof p === 'string' && p.trim()).map(p => p.trim().replace(/[.;,:!]+$/, '')).slice(0, 3)
            : [];

        if (!strengths.length) {
            strengths.push('Demonstrates communicative ability in the target language');
        }
        if (!priorities.length && errors.length) {
            priorities.push((errors[0].explanation || '').replace(/[.;,:!]+$/, ''));
        } else if (!priorities.length) {
            priorities.push(buildFallbackPriority(localStats));
        }

        return {
            overallScore,
            taskCompletion,
            dimensions,
            errors,
            demonstratedSkills,
            weakSkills,
            feedback: {
                strengths,
                priorities
            }
        };
    }

    return {
        validateAndCleanResult,
        DIMENSIONS,
        REQUIRED_FIELDS
    };
});
