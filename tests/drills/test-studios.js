// ============================================
// SPEAKING STUDIO & HU VERB STUDIO TEST SUITE
// ============================================
const assert = require('assert');

// Mock browser globals for node testing
global.window = global;
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: () => null,
    createElement: (tag) => ({
        innerHTML: '',
        textContent: '',
        appendChild: () => {},
        setAttribute: () => {},
        querySelectorAll: () => [],
        querySelector: () => null
    })
};
global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};
global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    content: (p) => p,
    set: (c) => {}
};
global.Content = {
    json: async () => ({ pairs: [], prompts: [] })
};

// 1. Test HuVerbStudio
require('../../engine/drills/hu-verb-studio.js');
assert(typeof HuVerbStudio !== 'undefined', 'HuVerbStudio must be defined');
assert(typeof HuVerbStudio.render === 'function', 'HuVerbStudio must export render()');
assert(typeof HuVerbStudio.stop === 'function', 'HuVerbStudio must export stop()');
assert(Array.isArray(HuVerbStudio.TABS) && HuVerbStudio.TABS.length === 4, 'HuVerbStudio must define 4 tabs (verb, suffix, prefix, morphology)');
console.log('[PASS] HuVerbStudio module structure verified.');

// 2. Test SpeakingDriller / SpeakingStudio
require('../../engine/drills/speaking.js');
assert(typeof SpeakingDriller !== 'undefined', 'SpeakingDriller must be defined');
assert(typeof SpeakingStudio !== 'undefined', 'SpeakingStudio alias must be defined');
assert(typeof SpeakingDriller.render === 'function', 'SpeakingDriller must export render()');
assert(typeof SpeakingDriller.stop === 'function', 'SpeakingDriller must export stop()');
console.log('[PASS] SpeakingStudio module structure verified.');

// 3. Test WritingDriller / WritingStudio
require('../../engine/drills/writing.js');
assert(typeof WritingDriller !== 'undefined', 'WritingDriller must be defined');
assert(typeof WritingStudio !== 'undefined', 'WritingStudio alias must be defined');
assert(typeof WritingDriller.render === 'function', 'WritingDriller must export render()');
assert(typeof WritingDriller.stop === 'function', 'WritingDriller must export stop()');
console.log('[PASS] WritingStudio module structure verified.');

// 4. Test Workshop Routing & Order
require('../../engine/workshop.js');
assert(typeof Workshop !== 'undefined', 'Workshop must be defined');

// Verify active driller before and after routing
Workshop.open('hu-verb');
let active = Workshop.activeDriller();
assert(active && active.id === 'hu-verb-studio', `Workshop.open('hu-verb') must route to hu-verb-studio, got ${active ? active.id : 'null'}`);
console.log('[PASS] Workshop legacy hu-verb routing to hu-verb-studio verified.');

Workshop.open('translation');
active = Workshop.activeDriller();
assert(active && active.id === 'writing', `Workshop.open('translation') must route to writing, got ${active ? active.id : 'null'}`);
console.log('[PASS] Workshop legacy translation routing to writing verified.');


// 4. Test GraderEngine with Oral Modality Context
const { GraderEngine } = require('../../engine/grader');
const grader = new GraderEngine();

async function testOralGrading() {
    const speechProduction = 'Hola, buenas tardes. Hoy quiero hablar de mi ciudad favorita en España. Sevilla tiene muchos monumentos históricos como la Giralda y la Plaza de España. La gente es muy simpática y la comida es deliciosa.';
    const context = {
        cefrLevel: 'B1',
        taskType: 'oral_production',
        taskInstructions: 'Habla sobre una ciudad que conoces bien.',
        targetSkills: ['fluency', 'oral_expression', 'describing_places'],
        language: 'es',
        modality: 'oral',
        title: 'Mi Ciudad Favorita'
    };

    console.log('Testing GraderEngine with oral production context...');
    const result = await grader.grade(speechProduction, context);
    assert(typeof result.overallScore === 'number', 'overallScore must be a number');
    assert(result.overallScore >= 0 && result.overallScore <= 100, 'overallScore must be 0-100');
    assert(result.dimensions, 'dimensions must exist');
    console.log(`[PASS] Oral grading completed with score: ${result.overallScore}/100.`);

    // 5. Test Multiple Errors per Category in GraderSchema
    const { validateAndCleanResult } = require('../../engine/grader/schema.js');
    const multiErrorMock = {
        overallScore: 65,
        taskCompletion: 0.7,
        dimensions: { grammar: 0.5, vocabulary: 0.7, coherence: 0.7, complexity: 0.6, naturalness: 0.6 },
        errors: [
            { category: 'grammar', severity: 'moderate', text: 'yo fue', explanation: 'Use fui for 1st person preterite', skillId: 'preterite' },
            { category: 'grammar', severity: 'minor', text: 'las problema', explanation: 'Problema is masculine (los problemas)', skillId: 'gender' },
            { category: 'grammar', severity: 'major', text: 'para que vas', explanation: 'Requires subjunctive: para que vayas', skillId: 'subjunctive' },
            { category: 'vocabulary', severity: 'minor', text: 'hacer un paseo', explanation: 'Prefer dar un paseo', skillId: 'collocations' }
        ],
        demonstratedSkills: [],
        weakSkills: [],
        feedback: { strengths: ['Understood'], priorities: ['Grammar review'] }
    };

    const cleaned = validateAndCleanResult(multiErrorMock);
    assert(cleaned.errors.length === 4, `Should preserve all 4 errors, got ${cleaned.errors.length}`);
    const grammarErrors = cleaned.errors.filter(e => e.category === 'grammar');
    assert(grammarErrors.length === 3, `Should allow 3 distinct errors under grammar, got ${grammarErrors.length}`);
    console.log('[PASS] Multiple errors under single category (grammar: 3, vocabulary: 1) verified.');
}

testOralGrading()
    .then(() => {
        console.log('\n[ALL PASS] Speaking Studio & Hungarian Verb Studio test suite passed.');
    })
    .catch(err => {
        console.error('\n[FAIL] Test error:', err);
        process.exitCode = 1;
    });
