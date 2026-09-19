// ============================================
// CONVERSATION GRADER TEST SUITE
// ============================================
const assert = require('assert');
const GraderPrompt = require('../../engine/grader/grader-prompt');
const LocalGrader = require('../../engine/grader/local-grader');

console.log('\n--- Test 1: GraderPrompt Interactive Conversation Scenarios ---');
const conversationDialogue = `
Interlocutor (Camarero): ¡Hola, buenas tardes! Bienvenido. ¿Qué le gustaría tomar?
Learner: Buenas tardes, un café con leche y una tostada, por favor.

Interlocutor (Camarero): Perfecto, un café con leche y una tostada. ¿Desea el café caliente o con hielo?
Learner: Caliente y con poco azúcar, por favor.

Interlocutor (Camarero): Aquí tiene su pedido. ¡Que lo disfrute! ¿Necesita algo más?
Learner: Muchas gracias, todo está muy bien. ¿Me trae la cuenta, por favor?
`.trim();

const convPrompt = GraderPrompt.buildGraderPrompt(
    'A1',
    'interactive_conversation',
    'Scenario: En el Café\nRoleplay: Camarero & Cliente\nTasks: Order food/drink, specify preferences, request the bill.',
    ['ordering_food', 'social_interaction', 'numbers_and_prices'],
    conversationDialogue,
    { language: 'es', taskType: 'interactive_conversation' }
);

assert(convPrompt.includes('Interactive Conversation Scenario'), 'Prompt should identify conversation task type');
assert(convPrompt.includes('Multi-turn spoken dialogue transcribed via automated speech recognition (ASR)'), 'Prompt should specify multi-turn ASR modality');
assert(convPrompt.includes('SCENARIO & ROLEPLAY OBJECTIVES:'), 'Prompt should contain scenario and roleplay objectives');
assert(convPrompt.includes('CONVERSATION DIALOGUE TRANSCRIPT:'), 'Prompt should contain conversation dialogue transcript');
assert(convPrompt.includes('PUNCTUATION & CAPITALIZATION: 0% penalty'), 'Prompt must enforce 0% penalty on punctuation');
console.log('[PASS] GraderPrompt correctly builds interactive conversation assessment prompt.');

console.log('\n--- Test 2: LocalGrader validateTurn ---');
const turnCriteria = {
    minWords: 3,
    targetKeywords: ['café', 'leche', 'tostada', 'por favor']
};

// Valid turn with keywords
const validTurnRes = LocalGrader.validateTurn('Buenas tardes un café con leche por favor', turnCriteria);
assert(validTurnRes.valid === true, 'Turn with 8 words and keywords should be valid');
assert(validTurnRes.wordCount === 8, 'Word count should be 8');
assert(validTurnRes.matchedKeywords.length >= 2, 'Should match keywords');

// Too short turn
const shortTurnRes = LocalGrader.validateTurn('hola', turnCriteria);
assert(shortTurnRes.valid === false, 'Turn with 1 word should fail minWords requirement');

// Turn with sufficient words but no direct keywords
const longTurnRes = LocalGrader.validateTurn('me gustaría pedir algo rico para desayunar hoy', turnCriteria);
assert(longTurnRes.valid === true, 'Turn with >= minWords + 3 should pass even without explicit keyword');

console.log('[PASS] LocalGrader validateTurn handles word counts, keyword matches, and leniency.');

console.log('\n--- Test 3: LocalGrader gradeConversation (Offline Fallback) ---');
const dummyScenario = {
    title: 'En el Café',
    cefrLevel: 'A1',
    targetSkills: ['ordering_food', 'social_interaction'],
    roleplay: { learnerRole: 'Cliente', interlocutorRole: 'Camarero' }
};

const completedTurns = [
    {
        turnIndex: 1,
        interlocutorPrompt: '¿Qué le gustaría tomar?',
        learnerTranscript: 'Un café con leche y un cruasán por favor',
        validation: { valid: true, matchedKeywords: ['café', 'leche'] }
    },
    {
        turnIndex: 2,
        interlocutorPrompt: '¿Caliente o frío?',
        learnerTranscript: 'Caliente y sin azúcar gracias',
        validation: { valid: true, matchedKeywords: ['caliente', 'azúcar'] }
    },
    {
        turnIndex: 3,
        interlocutorPrompt: '¿Algo más?',
        learnerTranscript: 'La cuenta por favor muchas gracias',
        validation: { valid: true, matchedKeywords: ['cuenta', 'gracias'] }
    }
];

const gradeRes = LocalGrader.gradeConversation(completedTurns, dummyScenario);
assert(typeof gradeRes.overallScore === 'number' && gradeRes.overallScore >= 80, 'Score should be high for 3 completed turns');
assert(gradeRes.taskCompletion === 1.0, 'Task completion should be 1.0');
assert(gradeRes.strengths.length > 0, 'Strengths should be generated');
assert(gradeRes.priorities.length > 0, 'Priorities should be generated');
assert(typeof gradeRes._prodOneLineTip === 'string' && gradeRes._prodOneLineTip.length > 0, 'One-line tip should be present');
assert(gradeRes.isOfflineFallback === true, 'isOfflineFallback flag must be set');

console.log('[PASS] LocalGrader gradeConversation produces rich, schema-compliant debrief.');

console.log('\n[ALL PASS] All conversation grader tests passed successfully!');
