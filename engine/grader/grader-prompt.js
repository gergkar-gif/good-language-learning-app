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
        const isOral = opts.modality === 'oral' ||
            (opts.taskType && String(opts.taskType).toLowerCase().includes('oral')) ||
            (taskType && String(taskType).toLowerCase().includes('oral'));

        if (isOral) {
            return `
Grade the following learner spoken production as a CEFR-aligned formative oral assessment in ${language}.

CEFR level: ${cefrLevel}
Task type: ${taskType} (Spoken / Oral Production)
Modality: Spoken speech transcribed via automated speech recognition (ASR)

TASK:
${taskInstructions}

TARGET SKILLS:
${formattedSkills}

LEARNER SPOKEN TRANSCRIPT:
${learnerProduction}

IMPORTANT ORAL SCORING PRINCIPLES:
1. SPOKEN MODALITY & ASR LENIENCY: This text is an automated speech-to-text transcript of real-time learner speech. Do NOT evaluate it purely as formal written text.
2. PUNCTUATION & CAPITALIZATION: 0% penalty. Do not penalise for missing, incomplete, or erratic punctuation or capitalization. Punctuation in ASR is an automated software artefact, not a learner error.
3. SPELLING & HOMOPHONES: 0% penalty. Spoken speech has no spelling. Do NOT penalise orthographic spelling errors, missing accents, or homophones (e.g. "haber" vs "a ver" in Spanish, or short vs long vowels in Hungarian). Never flag spelling or punctuation errors.
4. CONVERSATIONAL FILLERS & DISCOURSE MARKERS: Spoken discourse markers and conversational fillers (such as "bueno", "pues", "o sea", "a ver", "entonces" in Spanish, or "hát", "szóval", "nos" in Hungarian) are natural, authentic hallmarks of spoken fluency. Treat them as positive or neutral features of spoken flow, not errors or verbosity.
5. SELF-REPAIRS & FALSE STARTS: Spoken false starts, mid-sentence adjustments, and self-repairs (e.g. "ayer fui... digo, iba...") demonstrate positive metacognitive monitoring and real-time self-correction. Do NOT penalise them as grammatical or syntactic errors.
6. COMMUNICATIVE INTELLIGIBILITY: Prioritise communicative effectiveness, intelligibility, and task fulfilment over pedantic formal syntax. In natural spoken language, coordination, parataxis, ellipsis, and short clauses are completely standard.
7. Judge the spoken production itself, not the label or presumed quality of the test case.
8. Do not manufacture errors. Only record genuine, unambiguous spoken errors that clearly impede intelligibility or break core grammatical agreement.
9. Do not treat simple vocabulary as an error merely because more advanced vocabulary exists.
10. Distinguish language quality from task fulfilment. A linguistically capable speaker can lose task-completion points if they fail part of the task, but task completion must not be used to arbitrarily suppress language scores.
11. Complexity measures the range and control of spoken sentence structures, connectors, and expressions appropriate for CEFR ${cefrLevel}.
12. Vocabulary measures lexical range, precision, and situational appropriateness in speech. Basic words are perfectly acceptable when accurate and natural.
13. Grammar measures accuracy and control of forms actually spoken. Focus on major breakdowns (e.g. broken agreements or wrong verb tenses) rather than spoken shortcuts.
14. Coherence measures spoken idea progression, clarity, and thematic flow.
15. Naturalness measures whether the spoken phrasing sounds authentic, conversational, and idiomatic.
16. Overall score is a formative estimate, not an official certification exam score.

CALIBRATION:
- 90-100: Exceptionally strong oral performance for the stated task/level, with fluent delivery and only minor limitations.
- 80-89: Strong spoken performance, clearly meeting the level with good conversational flow and lexical range.
- 70-79: Competent spoken performance with noticeable but manageable limitations.
- 60-69: Weak/borderline spoken performance with multiple meaningful communicative limitations.
- Below 60: Substantially below expected oral performance for the task/level.

DIMENSION SCORING:
Score each dimension from 0.0 to 1.0 based on concrete evidence in the spoken transcript.
Use the full range. Do not automatically cluster every dimension around 0.7-0.9.

For overallScore (0-100), use this conceptual weighting calibrated for oral production:
- Task completion: 30%
- Naturalness & spoken fluency: 25%
- Vocabulary range & appropriateness: 20%
- Grammar & intelligibility: 15%
- Complexity: 10%

The overall score should broadly correspond to the weighted profile, but use professional judgement when a dimension is unusually important to the task.

CRITICAL SCALE RULE: overallScore is an INTEGER from 0 to 100 (a percentage-style grade, e.g. 45, 72, 91) — it is NOT on the same 0.0-1.0 scale as taskCompletion or the dimension scores. Never output overallScore as a decimal below 1.

CRITICAL SHAPE RULE: every entry in demonstratedSkills and weakSkills MUST be an object of the exact form {"skillId": "...", "confidence": 0.0} — never a bare string. Do not output ["skill_name"]; always output [{"skillId": "skill_name", "confidence": 0.5}].
${opts.taskCompletionPrimary ? `
TASK-COMPLETION-PRIMARY MODE:
This is a concrete, bounded can-do check (e.g. "count to 10", "state your name and where you're from", "list the days of the week") rather than an open-ended fluency topic. Ignore the weighting above; task completion now dominates. If the learner's spoken production correctly and completely conveys everything the task asked for, score 85-100 even if the response is a brief list, a single phrase, or otherwise not full-sentence prose — a task that only calls for an enumeration or a short factual answer must not be penalised for lacking length, complexity, or grammatical elaboration the task never asked for. Only reduce the score for content that is missing, wrong, or unintelligible.` : ''}

ERRORS:
Only include concrete, defensible spoken errors that impair intelligibility or break grammatical agreement.
Under NO circumstances should you flag spelling, punctuation, capitalization, or conversational discourse markers.
Permissible categories for oral evaluation: "grammar" | "vocabulary" | "register" | "syntax"
For each error:
- category: "grammar" | "vocabulary" | "register" | "syntax"
- severity: "minor" | "moderate" | "major"
- text: Short quoted fragment from the spoken transcript
- explanation: Concise description of the spoken issue and how to express it naturally in speech
- skillId: Canonical skill ID from TARGET SKILLS when clearly applicable; otherwise null

DEMONSTRATED SKILLS:
Only include skills from TARGET SKILLS that the learner actually demonstrates.
Give each a confidence score from 0.0 to 1.0.

WEAK SKILLS:
Only include skills from TARGET SKILLS for which the production provides meaningful evidence of weakness.
Do not mark a skill weak simply because it was not used.

FEEDBACK:
Give 2-3 concrete strengths and 2-3 actionable priorities focused on conversational speaking.
Priorities should be based on actual spoken weaknesses found in the production, not generic advice.

Return ONLY valid JSON. No Markdown fences. No introductory or trailing text.

OUTPUT ECONOMY:
- Keep each error explanation concise (1-2 sentences).
- Maximum 8 errors.
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

CRITICAL SCALE RULE: overallScore is an INTEGER from 0 to 100 (a percentage-style grade, e.g. 45, 72, 91) — it is NOT on the same 0.0-1.0 scale as taskCompletion or the dimension scores. Never output overallScore as a decimal below 1.

CRITICAL SHAPE RULE: every entry in demonstratedSkills and weakSkills MUST be an object of the exact form {"skillId": "...", "confidence": 0.0} — never a bare string. Do not output ["skill_name"]; always output [{"skillId": "skill_name", "confidence": 0.5}].
${opts.taskCompletionPrimary ? `
TASK-COMPLETION-PRIMARY MODE:
This is a concrete, bounded can-do check (e.g. "list the days of the week", "reserve a hotel room with a window and two separate beds") rather than an open-ended fluency topic. Ignore the weighting above; task completion now dominates. If the learner's production correctly and completely conveys everything the task asked for, score 85-100 even if the response is short or structurally simple — a task with a bounded, concrete requirement must not be penalised for lacking length, complexity, or grammatical elaboration the task never asked for. Only reduce the score for content that is missing, wrong, or unintelligible.` : ''}

ERRORS:
Only include concrete, defensible errors or important limitations.
You may include multiple distinct errors under the same category (e.g. several specific grammar errors or vocabulary choices) when supported by the learner's text.
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
- Maximum 8 errors.
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
