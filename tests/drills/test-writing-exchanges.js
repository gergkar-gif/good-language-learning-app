// ============================================
// TEST SUITE: WRITTEN EXCHANGES
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '../..');

console.log('\n--- Test 1: Written Exchange JSON Files & Schemas ---');
const esLatamPath = path.join(root, 'content/es-latam/writing-exchanges.json');
const esEsPath = path.join(root, 'content/es-es/writing-exchanges.json');
const huPath = path.join(root, 'content/hu/writing-exchanges.json');

assert(fs.existsSync(esLatamPath), 'es-latam writing-exchanges.json must exist');
assert(fs.existsSync(huPath), 'hu writing-exchanges.json must exist');

const esData = JSON.parse(fs.readFileSync(esLatamPath, 'utf8'));
const huData = JSON.parse(fs.readFileSync(huPath, 'utf8'));

assert(Array.isArray(esData.scenarios) && esData.scenarios.length >= 8, 'Spanish must provide at least 8 written exchanges');
assert(Array.isArray(huData.scenarios) && huData.scenarios.length >= 2, 'Hungarian must provide at least 2 written exchanges');

for (const sc of [...esData.scenarios, ...huData.scenarios]) {
    assert(sc.id, 'Scenario must have an id');
    assert(['A1', 'A2', 'B1', 'B2', 'C1'].includes(sc.cefrLevel), `Invalid CEFR level ${sc.cefrLevel} in ${sc.id}`);
    assert(sc.title, `Scenario ${sc.id} must have a title`);
    assert(sc.situation, `Scenario ${sc.id} must have a situation`);
    assert(sc.roleplay && sc.roleplay.interlocutorRole && sc.roleplay.learnerRole, `Scenario ${sc.id} must define roles`);
    assert(Array.isArray(sc.targetSkills) && sc.targetSkills.length > 0, `Scenario ${sc.id} must define targetSkills`);
    assert(Array.isArray(sc.turns) && sc.turns.length >= 2, `Scenario ${sc.id} must have at least 2 turns`);

    for (const turn of sc.turns) {
        assert(turn.turnIndex, `Turn in ${sc.id} must have turnIndex`);
        assert(turn.interlocutorPrompt, `Turn in ${sc.id} must have interlocutorPrompt`);
        assert(turn.learnerCue, `Turn in ${sc.id} must have learnerCue`);
        assert(turn.validationCriteria && typeof turn.validationCriteria.minWords === 'number', `Turn in ${sc.id} must have validationCriteria.minWords`);
        assert(Array.isArray(turn.validationCriteria.targetKeywords) && turn.validationCriteria.targetKeywords.length > 0, `Turn in ${sc.id} must have targetKeywords`);
    }
}
console.log(`[PASS] Verified ${esData.scenarios.length} Spanish and ${huData.scenarios.length} Hungarian written exchange schemas.`);

console.log('\n--- Test 2: Curriculum Unit ID Mapping Integrity ---');
function verifyUnitIds(scenarioData, curriculumFile, langLabel) {
    const curriculumData = JSON.parse(fs.readFileSync(curriculumFile, 'utf8'));
    const allUnitIds = new Set();
    Object.keys(curriculumData.levels || {}).forEach(lvl => {
        const levelObj = curriculumData.levels[lvl];
        (levelObj.units || []).forEach(u => {
            if (u.id) allUnitIds.add(u.id);
        });
    });

    for (const sc of scenarioData.scenarios) {
        assert(Array.isArray(sc.unitIds) && sc.unitIds.length > 0, `Scenario ${sc.id} in ${langLabel} must have unitIds array`);
        for (const uid of sc.unitIds) {
            assert(allUnitIds.has(uid), `Scenario ${sc.id} references unit ${uid} which does not exist in ${langLabel} curriculum!`);
        }
    }
    console.log(`[PASS] All ${scenarioData.scenarios.length} scenarios in ${langLabel} map to valid curriculum units.`);
}

verifyUnitIds(esData, path.join(root, 'content/es-latam/curriculum/curriculum.json'), 'es-latam');
if (fs.existsSync(esEsPath)) {
    const esEsData = JSON.parse(fs.readFileSync(esEsPath, 'utf8'));
    verifyUnitIds(esEsData, path.join(root, 'content/es-es/curriculum/curriculum.json'), 'es-es');
}
verifyUnitIds(huData, path.join(root, 'content/hu/curriculum/curriculum.json'), 'hu');

console.log('\n--- Test 3: Zero-Emoji Enforcement Across Code & Data ---');
const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

function assertNoEmojisInString(str, sourceName) {
    const lines = str.split('\n');
    const badLines = [];
    lines.forEach((line, idx) => {
        if (emojiRegex.test(line)) {
            badLines.push({ line: idx + 1, text: line.trim() });
        }
    });
    assert.strictEqual(badLines.length, 0, `Found emojis in ${sourceName}: ${JSON.stringify(badLines)}`);
}

assertNoEmojisInString(fs.readFileSync(esLatamPath, 'utf8'), 'content/es-latam/writing-exchanges.json');
assertNoEmojisInString(fs.readFileSync(huPath, 'utf8'), 'content/hu/writing-exchanges.json');
assertNoEmojisInString(fs.readFileSync(path.join(root, 'engine/drills/writing.js'), 'utf8'), 'engine/drills/writing.js');
console.log('[PASS] Verified zero emojis in written exchanges data and code.');

console.log('\n--- Test 4: GraderPrompt & LocalGrader for Written Exchanges ---');
const GraderPrompt = require('../../engine/grader/grader-prompt');
const LocalGrader = require('../../engine/grader/local-grader');

const prompt = GraderPrompt.buildGraderPrompt(
    'A2',
    'written_exchange',
    'Scenario: Averia en la caldera\nSituation: Boiler broken\nRoleplay: Inquilino & Casero',
    ['housing', 'explaining_problems', 'formal_register'],
    'Message 1:\nSr. Navarro: Podria indicarme que ocurre?\nYou: Buenos dias, no sale agua caliente desde ayer.',
    { language: 'es', taskType: 'written_exchange' }
);

assert(prompt.includes('Interactive Written Exchange'), 'Prompt must identify task as Interactive Written Exchange');
assert(prompt.includes('Multi-turn written digital text correspondence'), 'Prompt must specify written digital correspondence modality');
assert(prompt.includes('ORTHOGRAPHY & ACCENTS:'), 'Prompt must include orthography and accents guidance for writing');
assert(!prompt.includes('0% penalty. Spoken speech has no spelling'), 'Written prompt must not contain spoken ASR 0% spelling penalty');
console.log('[PASS] GraderPrompt correctly builds written exchange evaluation prompt.');

// Test LocalGrader for written exchange
const mockTurns = [
    {
        turnIndex: 1,
        interlocutorPrompt: 'Hace falta comprar algo para la cena de hoy?',
        learnerTranscript: 'Hola Mateo, necesitamos comprar pan, pasta y queso por favor.',
        validation: { valid: true, matchedKeywords: ['pan', 'pasta', 'queso', 'necesitamos'] }
    },
    {
        turnIndex: 2,
        interlocutorPrompt: 'Quieres que compre tambien agua?',
        learnerTranscript: 'Si, una botella de agua grande por favor, gracias.',
        validation: { valid: true, matchedKeywords: ['agua', 'botella', 'gracias'] }
    }
];

const mockScenario = esData.scenarios[0];
const gradeRes = LocalGrader.gradeConversation(mockTurns, mockScenario, { modality: 'written', taskType: 'written_exchange' });
assert(gradeRes.overallScore >= 70, 'Completed turns should yield competent score');
assert(gradeRes.strengths.some(s => s.includes('written exchange')), 'Strengths should reference written exchange');
console.log('[PASS] LocalGrader successfully grades written exchange with written-specific feedback.');

console.log('\n--- Test 5: WritingDriller UI Mounting & Tab Switching ---');
// Set up minimal browser mock environment
global.document = {
    addEventListener: () => {},
    getElementById: (id) => {
        if (id === 'wr-studio-body') return global._mockBody;
        return null;
    },
    createElement: () => {
        let _text = '';
        return {
            set textContent(v) { _text = String(v == null ? '' : v); },
            get innerHTML() { return _text; }
        };
    }
};
global.window = global;
global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    content: (p) => p
};
global.Content = {
    json: async (p) => {
        if (p.includes('writing-exchanges.json')) return esData;
        if (p.includes('writing-prompts.json')) return { prompts: [] };
        return {};
    }
};

const WritingDriller = require('../../engine/drills/writing.js');
assert(typeof WritingDriller.render === 'function', 'WritingDriller must export render');
assert(typeof WritingDriller.stop === 'function', 'WritingDriller must export stop');

async function testDrillerMount() {
    let capturedHtml = '';
    const container = {
        innerHTML: '',
        querySelectorAll: () => [],
        querySelector: () => null
    };

    global._mockBody = {
        set innerHTML(val) { capturedHtml = val; },
        get innerHTML() { return capturedHtml; },
        querySelectorAll: () => [],
        querySelector: () => null
    };

    await WritingDriller.render(container, { activeTab: 'exchanges' });
    assert(capturedHtml.includes('Written Exchanges'), 'Active tab body must render Written Exchanges view');
    // A1 and A2 scenarios provide English scaffolding for titles and roles
    assert(capturedHtml.includes('Shopping for Dinner') || capturedHtml.includes('Compras para la cena'), 'Must render sample scenario title');
    assert(capturedHtml.includes('Mateo (Flatmate)') || capturedHtml.includes('Mateo (Companero de piso)'), 'Must render interlocutor roleplay tag');
    console.log('[PASS] WritingDriller cleanly mounts and displays Written Exchanges studio tab.');
}

testDrillerMount().then(() => {
    console.log('\n=== ALL WRITTEN EXCHANGES TESTS PASSED ===\n');
});
