// ============================================
// GRADER PROMPT BUILDER
// ============================================
// Constructs calibrated, language-agnostic CEFR formative evaluation prompts.
// Universal for Spanish, Hungarian, and any future Parlour courses.

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.GraderPrompt = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    function formatSkills(targetSkills) {
        if (!targetSkills || !Array.isArray(targetSkills)) return '- General communicative competence';
        return targetSkills.map(skill => {
            if (typeof skill === 'string') return `- ${skill}`;
            if (skill && typeof skill === 'object') {
                return `- ${skill.id || skill.skillId || 'skill'}: ${skill.description || skill.name || ''}`;
            }
            return '- General competence';
        }).join('\n');
    }

    function buildGraderPrompt(cefrLevel, taskType, taskInstructions, targetSkills, learnerProduction, options) {
        const opts = options || {};
        const language = opts.language ? opts.language.toUpperCase() : 'THE TARGET LANGUAGE';
        const formattedSkills = formatSkills(targetSkills);

        return `
Grade the following learner production as a CEFR-aligned formative assessment in ${language}.

CEFR level: ${cefrLevel}
Task type: ${taskType}

TASK:
${taskInstructions}

TARGET SKILLS:
${formattedSkills}

LEARNER PRODUCTION:
${learnerProduction}

IMPORTANT SCORING PRINCIPLES:
1. Judge the production itself, not the label or presumed quality of the test case.
2. Do not manufacture errors. Only record errors that are actually supported by the learner's text.
3. Do not treat simple vocabulary as an error merely because more advanced vocabulary exists.
4. Distinguish language quality from task fulfilment. A linguistically strong response can lose task-completion points if it genuinely fails part of the task, but task completion must not be used to arbitrarily suppress language scores.
5. Complexity measures the actual range and control of sentence structures, subordinate clauses, connectors, and other appropriately complex constructions for CEFR ${cefrLevel}.
6. Vocabulary measures range, precision, appropriateness, and control. Basic words are perfectly acceptable when they are accurate and natural. Penalise limited range only when the production genuinely shows limited lexical range for the level.
7. Grammar measures accuracy and control of forms and structures actually used.
8. Coherence measures organisation, progression, linking, and clarity of ideas.
9. Naturalness measures whether the language is idiomatic and appropriate. Do not penalise merely for being formal, simple, or different from your preferred phrasing.
10. Overall score must reflect the complete profile of the production. Do not let one dimension dominate the overall result unless it represents a substantial failure.
11. Stronger grammar, vocabulary range, complexity, coherence, and task fulfilment should normally produce a higher overall score than a weaker production. However, do not force an ordering when the evidence does not support it.
12. The overall score is a formative estimate, not an official certification exam score.

CALIBRATION:
- 90-100: Exceptionally strong performance for the stated task/level, with very good control and only minor limitations.
- 80-89: Strong performance, clearly meeting the level with good control and range.
- 70-79: Competent performance with noticeable but manageable limitations.
- 60-69: Weak/borderline performance with multiple meaningful limitations.
- Below 60: Substantially below expected performance for the task/level.

DIMENSION SCORING:
Score each dimension from 0.0 to 1.0 based on concrete evidence in the production.
Use the full range. Do not automatically cluster every dimension around 0.7-0.9.

For overallScore (0-100), use this conceptual weighting:
- Task completion: 20%
- Grammar: 20%
- Vocabulary: 20%
- Coherence: 15%
- Complexity: 15%
- Naturalness: 10%

The overall score should broadly correspond to the weighted profile, but use professional judgement when a dimension is unusually important to the task.

ERRORS:
Only include concrete, defensible errors or important limitations.
For each error:
- category: "grammar" | "vocabulary" | "spelling" | "punctuation" | "register" | "syntax"
- severity: "minor" | "moderate" | "major"
- text: Short quoted fragment from the learner production
- explanation: Concise description of the issue and how to correct it
- skillId: Canonical skill ID from TARGET SKILLS when clearly applicable; otherwise null

DEMONSTRATED SKILLS:
Only include skills from TARGET SKILLS that the learner actually demonstrates.
Give each a confidence score from 0.0 to 1.0.

WEAK SKILLS:
Only include skills from TARGET SKILLS for which the production provides meaningful evidence of weakness.
Do not mark a skill weak simply because it was not used.

FEEDBACK:
Give 2-3 concrete strengths and 2-3 actionable priorities.
Priorities should be based on actual weaknesses found in the production, not generic advice.

Return ONLY valid JSON. No Markdown fences. No introductory or trailing text.

OUTPUT ECONOMY:
- Keep each error explanation concise (1-2 sentences).
- Maximum 5 errors.
- Maximum 3 demonstratedSkills.
- Maximum 3 weakSkills.
- Maximum 3 strengths and 3 priorities.
- Do not repeat the learner's full production text.
- Keep the complete JSON comfortably below the output token limit.

Required JSON shape:
{
  "overallScore": 0,
  "taskCompletion": 0.0,
  "dimensions": {
    "grammar": 0.0,
    "vocabulary": 0.0,
    "coherence": 0.0,
    "complexity": 0.0,
    "naturalness": 0.0
  },
  "errors": [
    {
      "category": "grammar",
      "severity": "minor",
      "text": "short fragment",
      "explanation": "concise explanation",
      "skillId": null
    }
  ],
  "demonstratedSkills": [
    {
      "skillId": "skill_id",
      "confidence": 0.0
    }
  ],
  "weakSkills": [
    {
      "skillId": "skill_id",
      "confidence": 0.0
    }
  ],
  "feedback": {
    "strengths": ["strength 1", "strength 2"],
    "priorities": ["priority 1", "priority 2"]
  }
}
`.trim();
    }

    return {
        buildGraderPrompt,
        formatSkills
    };
});
