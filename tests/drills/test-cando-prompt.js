// ============================================
// CAN-DO PROMPT & SCAFFOLDING UNIT TESTS
// ============================================
const assert = require('assert');

// Mock browser globals for testing
global.window = global;
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
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
    code: () => 'hu',
    name: () => 'Hungarian',
    content: (p) => p,
    set: () => {}
};
global.Content = {
    json: async () => ({ pairs: [], prompts: [] })
};

// 1. Load CanDoPrompt module
require('../../engine/canDoPrompt.js');
assert(typeof CanDoPrompt !== 'undefined', 'CanDoPrompt must be defined');
assert(typeof CanDoPrompt.formatPrompt === 'function', 'CanDoPrompt.formatPrompt must be exported');
assert(typeof CanDoPrompt.extractCleanTitle === 'function', 'CanDoPrompt.extractCleanTitle must be exported');

console.log('--- Test 1: Clean Title Extraction ---');
const t1 = CanDoPrompt.extractCleanTitle('I can name all twelve months and say which month something is in.');
assert.strictEqual(t1, 'Months of the Year', `Expected "Months of the Year", got "${t1}"`);

const t2 = CanDoPrompt.extractCleanTitle('I can complete a short at the café interaction.');
assert.strictEqual(t2, 'At the Café', `Expected "At the Café", got "${t2}"`);

const t3 = CanDoPrompt.extractCleanTitle('I can describe my daily routine.');
assert.strictEqual(t3, 'Daily Routine', `Expected "Daily Routine", got "${t3}"`);

const t4 = CanDoPrompt.extractCleanTitle('I can ask for and understand simple directions in town.');
assert.strictEqual(t4, 'Asking for Directions', `Expected "Asking for Directions", got "${t4}"`);

const t5 = CanDoPrompt.extractCleanTitle('I can greet someone and introduce myself.');
assert.strictEqual(t5, 'Greetings & Introductions', `Expected "Greetings & Introductions", got "${t5}"`);
console.log('[PASS] Title extraction creates clean, readable titles without truncation.');

console.log('--- Test 2: Months of the Year (Hungarian & Spanish) ---');
const huMonths = CanDoPrompt.formatPrompt('I can name all twelve months and say which month something is in.', {
    language: 'Hungarian',
    langCode: 'hu',
    modality: 'oral'
});
assert.strictEqual(huMonths.type, 'enumeration');
assert.strictEqual(huMonths.title, 'Months of the Year');
assert(huMonths.prompt.includes('Say the months of the year in Hungarian'), 'Prompt should mention months of the year');
assert(huMonths.prompt.includes('birthday'), 'Prompt should mention birthday/event');
assert(huMonths.cues.length >= 2, 'Should have at least 2 scaffolding cues');
assert(huMonths.cues[0].includes('január'), 'Hungarian cues should include Hungarian month examples');
assert(huMonths.cues[1].includes('-ban / -ben'), 'Hungarian cues should mention -ban / -ben suffix');

const esMonths = CanDoPrompt.formatPrompt('I can name all twelve months and say which month something is in.', {
    language: 'Spanish',
    langCode: 'es',
    modality: 'oral'
});
assert.strictEqual(esMonths.type, 'enumeration');
assert(esMonths.cues[0].includes('enero'), 'Spanish cues should include Spanish month examples');
assert(esMonths.cues[1].includes('"en"'), 'Spanish cues should mention "en" preposition');
console.log('[PASS] Months enumeration formatting correctly scaffolded.');

console.log('--- Test 3: Café Interaction ---');
const huCafe = CanDoPrompt.formatPrompt('I can complete a short at the café interaction.', {
    language: 'Hungarian',
    langCode: 'hu',
    modality: 'oral'
});
assert.strictEqual(huCafe.type, 'transaction');
assert.strictEqual(huCafe.title, 'At the Café');
assert(huCafe.scenario.includes('café'), 'Scenario should mention café');
assert(huCafe.prompt.includes('Order at the café'), 'Prompt should be active ordering task');
assert(huCafe.cues.length >= 3, 'Café transaction should provide 3-part dialogue cues');
assert(huCafe.cues[1].includes('Kérek'), 'Hungarian cue should suggest Kérek');
console.log('[PASS] Café interaction correctly scaffolded.');

console.log('--- Test 4: Personal Monologue (Daily Routine) ---');
const routine = CanDoPrompt.formatPrompt('I can describe my daily routine.', {
    language: 'Spanish',
    langCode: 'es',
    modality: 'oral'
});
assert.strictEqual(routine.type, 'monologue');
assert.strictEqual(routine.title, 'Daily Routine');
assert(routine.prompt.includes('daily routine'), 'Prompt should instruct describing daily routine');
assert(routine.cues.length >= 2, 'Monologue should provide guidance cues');
console.log('[PASS] Monologue prompt correctly scaffolded.');

console.log('--- Test 4b: Incidental keywords do not trigger scenario templates ---');
[
    'I can explain who the Maya, Mexica and Inca were, and roughly where and when each flourished.',
    'I can describe how Budapest relates to the country\'s counties.',
    'I can state how much coffee prices fell between 1929 and 1932.',
    'I can use compass directions with -ra/-re and -tól/-től to say where something lies relative to Hungary.'
].forEach((canDo) => {
    const r = CanDoPrompt.formatPrompt(canDo, { language: 'Spanish', langCode: 'es', modality: 'oral' });
    assert.strictEqual(r.type, 'functional', `"${canDo}" should fall back to its own wording, got ${r.type}: ${r.prompt}`);
});
console.log('[PASS] Only genuine situational can-dos get a canned scenario.');

console.log('--- Test 5: SpeakingDriller Integration with CanDoPrompt ---');
require('../../engine/drills/speaking.js');
const mockContainer = { innerHTML: '', querySelector: () => null, querySelectorAll: () => [] };

SpeakingDriller.render(mockContainer, {
    targetCompetency: 'I can complete a short at the café interaction.',
    level: 'A1',
    maxSeconds: 40
}).then(() => {
    SpeakingDriller.stop();
    console.log('[PASS] SpeakingDriller correctly initializes with CanDoPrompt formatted prompt.');

    console.log('--- Test 6: SpeakingDriller 1-Sentence Coaching Formatting ---');
    const mockResultWithPriorities = {
        overallScore: 82,
        taskCompletion: 0.85,
        feedback: {
            priorities: ["Practice using the preterite tense.", "Remember to include polite expressions like 'por favor'."],
            strengths: ["Good fluency and natural delivery."]
        },
        errors: []
    };
    const tip1 = SpeakingDriller._prodOneLineTip(mockResultWithPriorities, { title: 'Order at a café' });
    console.log('Tip with priorities:', tip1);
    assert(!tip1.includes('..'), 'Must not contain double periods');
    assert(!tip1.includes('Focus on Practice'), 'Must not contain awkward capitalized concatenation');
    assert(!tip1.includes('You missed:'), 'Must not contain raw error header');
    assert.strictEqual((tip1.match(/\./g) || []).length, 1, 'Must contain exactly one period terminating the extended sentence');
    assert(tip1.startsWith('Well done — you got your message across'), 'Should start with clean completion appraisal');
    assert(tip1.includes('practice using the preterite tense and include polite expressions'), 'Should smoothly join action clauses');
    console.log('[PASS] Tip with priorities formatted as one clean extended sentence.');

    console.log('--- Test 7: SpeakingDriller & WritingDriller Error-Only and Flawless Cases ---');
    require('../../engine/drills/writing.js');
    const mockResultErrorOnly = {
        overallScore: 65,
        taskCompletion: 0.6,
        feedback: { priorities: [] },
        errors: [{ explanation: "The verb 'tener' should be used instead of 'ser' for age." }]
    };
    const tip2 = SpeakingDriller._prodOneLineTip(mockResultErrorOnly, { title: 'State your age' });
    console.log('Tip with error explanation:', tip2);
    assert(tip2.startsWith('Good effort — you got most of it across, but note that the verb \'tener\' should be used'), 'Should embed grammar explanation cleanly');
    assert.strictEqual((tip2.match(/\./g) || []).length, 1, 'Must end with single period');

    const mockResultFlawless = {
        overallScore: 95,
        taskCompletion: 1.0,
        feedback: {
            priorities: [],
            strengths: ["Natural rhythm and rich conversational vocabulary."]
        },
        errors: []
    };
    const tip3 = WritingDriller._shortTaskTip(mockResultFlawless, { title: 'Introduce yourself' });
    console.log('Flawless tip:', tip3);
    console.log('--- Test 8: Spurious Complexity Feedback Filter on Short Tasks ---');
    const mockShortWithComplexityPriority = {
        overallScore: 90,
        taskCompletion: 1.0,
        feedback: {
            priorities: ["Write more complex sentences", "Combine short sentences using connectors"],
            strengths: ["Accurate greeting and natural vocabulary."]
        },
        errors: []
    };
    const speakingTipFiltered = SpeakingDriller._prodOneLineTip(mockShortWithComplexityPriority, { title: 'Say hello' });
    console.log('Speaking tip filtered:', speakingTipFiltered);
    assert(!speakingTipFiltered.toLowerCase().includes('complex'), 'Should not advise complex sentences for short high-scoring tasks');
    assert(speakingTipFiltered.includes('with accurate greeting and natural vocabulary!'), 'Should fall back to strength when complexity priority is filtered');

    const writingTipFiltered = WritingDriller._shortTaskTip(mockShortWithComplexityPriority, { title: 'Greeting' });
    console.log('Writing tip filtered:', writingTipFiltered);
    assert(!writingTipFiltered.toLowerCase().includes('complex'), 'Writing driller should drop spurious complexity priority');
    assert(writingTipFiltered.includes('with accurate greeting and natural vocabulary!'), 'Writing driller should celebrate strength');

    // Schema level verification for short productions (e.g. "szia, meg!")
    const { GraderSchema, LocalGrader } = require('../../engine/grader');
    const localShort = LocalGrader.analyze('szia, meg!', { cefrLevel: 'A1' });
    const cleanedShort = GraderSchema.validateAndCleanResult({
        overallScore: 95,
        taskCompletion: 1.0,
        dimensions: { grammar: 1.0, vocabulary: 1.0, coherence: 1.0, complexity: 0.8, naturalness: 1.0 },
        errors: [],
        feedback: {
            strengths: ['Accurate Hungarian greeting.'],
            priorities: ['Write more complex sentences and use connectors']
        }
    }, localShort);
    assert.strictEqual(cleanedShort.feedback.priorities.length, 0, 'Schema should strip spurious complexity priorities for short A1 answers');
    console.log('[PASS] Spurious complexity advice successfully filtered on short/A1 productions.');

    console.log('[PASS] Single extended sentence coaching verified across Speaking and Writing drillers.');
    console.log('\n[ALL PASS] Can-Do Prompt & Scaffolding Test Suite passed.');
}).catch((e) => {
    console.error('SpeakingDriller render error:', e);
    process.exit(1);
});
