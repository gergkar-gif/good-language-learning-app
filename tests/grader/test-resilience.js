// ============================================
// RESILIENCE, JSON REPAIR & FALLBACK TESTS
// ============================================
const assert = require('assert');
const { GraderEngine, GraderSchema, LocalGrader } = require('../../engine/grader');

async function testJsonRepair() {
    console.log('\n--- Testing JSON Repair & Sanitization ---');
    const engine = new GraderEngine();

    // 1. Markdown fences
    const fenced = '```json\n{"overallScore": 85, "taskCompletion": 0.9, "dimensions": {"grammar": 0.85, "vocabulary": 0.8, "coherence": 0.8, "complexity": 0.8, "naturalness": 0.8}, "errors": [], "demonstratedSkills": [], "weakSkills": [], "feedback": {"strengths": ["Good"], "priorities": ["Keep going"]}}\n```';
    const parsed1 = engine._parseJson(fenced);
    assert.strictEqual(parsed1.overallScore, 85, 'Should strip markdown fences');
    console.log('✓ Markdown fence stripping');

    // 2. Extraneous conversational text before and after JSON
    const surrounded = 'Here is your evaluation report:\n{"overallScore": 76, "taskCompletion": 0.8, "dimensions": {"grammar": 0.75, "vocabulary": 0.8, "coherence": 0.8, "complexity": 0.7, "naturalness": 0.75}, "errors": [], "demonstratedSkills": [], "weakSkills": [], "feedback": {"strengths": ["Solid"], "priorities": ["Practice"]}}\nI hope this helps your studies!';
    const parsed2 = engine._parseJson(surrounded);
    assert.strictEqual(parsed2.overallScore, 76, 'Should extract outermost JSON braces');
    console.log('✓ Conversational prose stripping (outer brace extraction)');

    // 3. Trailing commas in arrays and objects
    const trailingCommas = '{"overallScore": 90, "taskCompletion": 0.95, "dimensions": {"grammar": 0.9, "vocabulary": 0.9, "coherence": 0.9, "complexity": 0.9, "naturalness": 0.9, }, "errors": [], "demonstratedSkills": ["skill1", ], "weakSkills": [], "feedback": {"strengths": ["Accurate", ], "priorities": ["None", ], }, }';
    const parsed3 = engine._parseJson(trailingCommas);
    assert.strictEqual(parsed3.overallScore, 90, 'Should clean trailing commas');
    console.log('✓ Trailing comma repair');
}

async function testSchemaSanitization() {
    console.log('\n--- Testing Schema Normalization & Clamping ---');

    // Score clamping
    const rawOutlier = {
        overallScore: 145, // > 100
        taskCompletion: 1.8, // > 1.0
        dimensions: {
            grammar: -0.5, // < 0
            vocabulary: 0.85,
            coherence: 0.9,
            complexity: 0.8,
            naturalness: 0.8
        },
        errors: [
            { category: 'grammar', text: 'algo', explanation: 'error expl', severity: 'critical', skillId: 'ser' }
        ],
        demonstratedSkills: ['contrast_connectors'], // raw string instead of object
        weakSkills: [{ skillId: 'past_tense', confidence: 0.7 }],
        feedback: {
            strengths: ['Great vocabulary'],
            priorities: ['Review past tense']
        }
    };

    const cleaned = GraderSchema.validateAndCleanResult(rawOutlier);
    assert.strictEqual(cleaned.overallScore, 100, 'Score should clamp to 100');
    assert.strictEqual(cleaned.taskCompletion, 1.0, 'Task completion should clamp to 1.0');
    assert.strictEqual(cleaned.dimensions.grammar, 0.0, 'Dimension should clamp to 0.0');
    assert.strictEqual(cleaned.errors[0].severity, 'major', 'Critical severity should normalize to major');
    assert.strictEqual(cleaned.demonstratedSkills[0].skillId, 'contrast_connectors', 'String skill should normalize to object');
    assert.strictEqual(cleaned.demonstratedSkills[0].confidence, 0.8, 'Default confidence should be set');
    console.log('✓ Score clamping, severity normalization, and skill array normalization');
}

async function testOfflineFallback() {
    console.log('\n--- Testing Graceful Local Fallback ---');
    const local = LocalGrader.analyze('Esta es una prueba rápida de producción escrita en español para verificar las métricas locales.', { cefrLevel: 'A2' });

    assert.ok(local.wordCount > 10, 'Word count computed');
    assert.ok(local.sentenceCount >= 1, 'Sentence count computed');
    assert.ok(local.avgSentenceLength > 0, 'Average sentence length computed');
    assert.strictEqual(local.structuralChecks.startsWithCapital, true, 'Capitalization check works');
    assert.strictEqual(local.structuralChecks.endsWithPunctuation, true, 'Ending punctuation check works');
    console.log('✓ LocalGrader deterministic metrics verify cleanly');

    const engine = new GraderEngine({ endpoint: 'http://127.0.0.1:9999/unreachable' });
    const fallback = engine._fallbackAssessment('Texto de prueba...', 'B1', local, 'Connection refused');

    assert.strictEqual(fallback.aiEvaluated, false, 'aiEvaluated should be false in fallback');
    assert.strictEqual(fallback.offline, true, 'offline should be true in fallback');
    assert.ok(typeof fallback.overallScore === 'number', 'Fallback includes overall score');
    assert.ok(fallback.feedback.strengths.length > 0, 'Fallback provides constructive feedback');
    console.log('✓ Fallback assessment generates complete, safe object without crashing');
}

async function main() {
    await testJsonRepair();
    await testSchemaSanitization();
    await testOfflineFallback();
    console.log('\n[SUCCESS] All resilience and sanitization tests passed.');
}

main()
    .then(() => process.exit(0))
    .catch(err => {
        console.error('\n[FAILURE] Resilience test failed:', err);
        process.exit(1);
    });
