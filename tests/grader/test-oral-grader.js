// ============================================
// ORAL GRADER PROMPT & LENIENCY TEST SUITE
// ============================================
const assert = require('assert');
const GraderPrompt = require('../../engine/grader/grader-prompt');
const LocalGrader = require('../../engine/grader/local-grader');
const { GraderEngine } = require('../../engine/grader');

console.log('\n--- Test 1: GraderPrompt Oral Modality Calibration ---');
const oralPrompt = GraderPrompt.buildGraderPrompt(
    'B1',
    'oral_production',
    'Describe your hometown and why you like living there.',
    ['fluency', 'oral_expression'],
    'Bueno, pues vivo en Valencia y me gusta mucho porque tiene la playa cerca. Ayer fui... digo, iba cada verano con mi familia.',
    { language: 'es', modality: 'oral' }
);

// 1. Check ASR Leniency & Spoken Principles
assert(oralPrompt.includes('Spoken / Oral Production'), 'Oral prompt should identify spoken task');
assert(oralPrompt.includes('automated speech-to-text transcript'), 'Oral prompt should identify ASR transcript');
assert(oralPrompt.includes('PUNCTUATION & CAPITALIZATION: 0% penalty'), 'Oral prompt must enforce 0% penalty on punctuation/caps');
assert(oralPrompt.includes('SPELLING & HOMOPHONES: 0% penalty'), 'Oral prompt must enforce 0% penalty on spelling/homophones');
assert(oralPrompt.includes('CONVERSATIONAL FILLERS & DISCOURSE MARKERS'), 'Oral prompt must recognize spoken discourse markers');
assert(oralPrompt.includes('SELF-REPAIRS & FALSE STARTS'), 'Oral prompt must treat self-repairs as positive monitoring');
assert(oralPrompt.includes('COMMUNICATIVE INTELLIGIBILITY'), 'Oral prompt must prioritize intelligibility over rigid essay syntax');

// 2. Check Rebalanced Weights
assert(oralPrompt.includes('Task completion: 30%'), 'Oral prompt must weight Task completion at 30%');
assert(oralPrompt.includes('Naturalness & spoken fluency: 25%'), 'Oral prompt must weight Naturalness & spoken fluency at 25%');
assert(oralPrompt.includes('Vocabulary range & appropriateness: 20%'), 'Oral prompt must weight Vocabulary at 20%');
assert(oralPrompt.includes('Grammar & intelligibility: 15%'), 'Oral prompt must weight Grammar at 15%');
assert(oralPrompt.includes('Complexity: 10%'), 'Oral prompt must weight Complexity at 10%');

// 3. Check Error Restrictions
assert(oralPrompt.includes('Under NO circumstances should you flag spelling, punctuation, capitalization'), 'Oral prompt must forbid spelling/punctuation errors');
assert(!oralPrompt.includes('"spelling" | "punctuation"'), 'Oral prompt error categories must not include spelling or punctuation');

console.log('[PASS] GraderPrompt oral modality calibrated with speech leniency and oral weights.');

console.log('\n--- Test 2: GraderPrompt Written Modality Preserved ---');
const writtenPrompt = GraderPrompt.buildGraderPrompt(
    'B1',
    'essay_writing',
    'Write a letter to a friend about your holiday.',
    ['past_tenses', 'connectors'],
    'Querido amigo, te escribo para contarte sobre mis vacaciones...',
    { language: 'es', modality: 'written' }
);

assert(writtenPrompt.includes('Task completion: 20%'), 'Written prompt must retain 20% Task completion');
assert(writtenPrompt.includes('Grammar: 20%'), 'Written prompt must retain 20% Grammar');
assert(writtenPrompt.includes('Vocabulary: 20%'), 'Written prompt must retain 20% Vocabulary');
assert(writtenPrompt.includes('"spelling" | "punctuation"'), 'Written prompt must include spelling/punctuation categories');
console.log('[PASS] GraderPrompt written modality intact and unperturbed.');

console.log('\n--- Test 3: LocalGrader Deterministic Metrics with Oral Modality ---');
const unpunctuatedTranscript = 'bueno pues me gusta la comida mexicana porque es muy picante y sabrosa';
const oralStats = LocalGrader.analyze(unpunctuatedTranscript, { cefrLevel: 'A2', modality: 'oral' });
assert(oralStats.structuralChecks.isOral === true, 'LocalGrader should flag structuralChecks as oral');
assert(oralStats.structuralChecks.startsWithCapital === true, 'Oral transcript should not fail capitalization check');
assert(oralStats.structuralChecks.endsWithPunctuation === true, 'Oral transcript should not fail ending punctuation check');
console.log('[PASS] LocalGrader handles unpunctuated oral transcript without spurious structural penalties.');

console.log('\n--- Test 4: GraderEngine Modality Propagation ---');
const engine = new GraderEngine();
let capturedParams = null;
engine._callAiGrader = async (params) => {
    capturedParams = params;
    return {
        overallScore: 78,
        taskCompletion: 0.8,
        dimensions: { grammar: 0.75, vocabulary: 0.8, coherence: 0.75, complexity: 0.7, naturalness: 0.85 },
        errors: [],
        demonstratedSkills: [],
        weakSkills: [],
        feedback: { strengths: ['Clear delivery'], priorities: ['Keep practicing'] }
    };
};

async function testEngineModality() {
    const result = await engine.grade('me gusta valencia mucho', {
        cefrLevel: 'A2',
        taskType: 'oral_production',
        modality: 'oral'
    });
    assert(capturedParams !== null, '_callAiGrader should be invoked');
    assert.strictEqual(capturedParams.modality, 'oral', 'Engine should pass oral modality');
    assert.strictEqual(result.meta.modality, 'oral', 'Result metadata should record oral modality');
    assert.strictEqual(result.localStats.structuralChecks.isOral, true, 'Result localStats should reflect oral modality');
    console.log('[PASS] GraderEngine correctly wires oral modality into analysis and evaluation pipeline.');
}

// 5. Zero Emoji Verification across prompts
const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
assert(!emojiRegex.test(oralPrompt), 'Oral prompt must contain zero emojis');
assert(!emojiRegex.test(writtenPrompt), 'Written prompt must contain zero emojis');
console.log('[PASS] Zero emojis verified across grader prompts.');

testEngineModality()
    .then(() => {
        console.log('\n[ALL PASS] Oral Grader Prompt & Leniency test suite passed cleanly.\n');
    })
    .catch(err => {
        console.error('[FAIL]', err);
        process.exitCode = 1;
    });
