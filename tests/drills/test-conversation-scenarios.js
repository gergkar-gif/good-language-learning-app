// ============================================
// CONVERSATION SCENARIOS TEST SUITE
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('\n--- Test 1: Content Schema & Seed Scenarios Verification ---');

const esPath = fs.existsSync(path.resolve(__dirname, '../../content/es/conversation-scenarios.json'))
    ? path.resolve(__dirname, '../../content/es/conversation-scenarios.json')
    : path.resolve(__dirname, '../../content/es-latam/conversation-scenarios.json');
const huPath = path.resolve(__dirname, '../../content/hu/conversation-scenarios.json');

assert(fs.existsSync(esPath), 'Spanish conversation scenarios file must exist');
assert(fs.existsSync(huPath), 'Hungarian conversation scenarios file must exist');

const esData = JSON.parse(fs.readFileSync(esPath, 'utf8'));
const huData = JSON.parse(fs.readFileSync(huPath, 'utf8'));

assert(esData.language === 'es', 'Spanish scenario language code must be es');
assert(Array.isArray(esData.scenarios) && esData.scenarios.length >= 4, 'Spanish must provide at least 4 seed scenarios');
assert(huData.language === 'hu', 'Hungarian scenario language code must be hu');
assert(Array.isArray(huData.scenarios) && huData.scenarios.length >= 2, 'Hungarian must provide at least 2 seed scenarios');

for (const sc of [...esData.scenarios, ...huData.scenarios]) {
    assert(sc.id, `Scenario missing id: ${JSON.stringify(sc)}`);
    assert(sc.cefrLevel, `Scenario ${sc.id} missing cefrLevel`);
    assert(sc.title, `Scenario ${sc.id} missing title`);
    assert(sc.situation, `Scenario ${sc.id} missing situation`);
    assert(sc.roleplay && sc.roleplay.learnerRole && sc.roleplay.interlocutorRole, `Scenario ${sc.id} missing roleplay definitions`);
    assert(Array.isArray(sc.turns) && sc.turns.length >= 2, `Scenario ${sc.id} must have at least 2 turns`);

    // A1 and A2 scenarios should provide English descriptions for scaffolding
    if (sc.cefrLevel === 'A1' || sc.cefrLevel === 'A2') {
        assert(sc.titleEn, `A1/A2 Scenario ${sc.id} missing titleEn`);
        assert(sc.situationEn, `A1/A2 Scenario ${sc.id} missing situationEn`);
        assert(sc.roleplay.learnerRoleEn, `A1/A2 Scenario ${sc.id} missing roleplay.learnerRoleEn`);
        assert(sc.roleplay.interlocutorRoleEn, `A1/A2 Scenario ${sc.id} missing roleplay.interlocutorRoleEn`);
    }

    sc.turns.forEach((t, idx) => {
        assert(t.turnIndex === idx + 1, `Scenario ${sc.id} turn ${idx} index mismatch`);
        assert(t.interlocutorPrompt, `Scenario ${sc.id} turn ${idx} missing interlocutorPrompt`);
        assert(t.learnerCue, `Scenario ${sc.id} turn ${idx} missing learnerCue`);
        if (sc.cefrLevel === 'A1' || sc.cefrLevel === 'A2') {
            assert(t.learnerCueEn, `Scenario ${sc.id} turn ${idx} missing learnerCueEn`);
        }
        if (t.vocabularyHints) {
            assert(Array.isArray(t.vocabularyHints), `Scenario ${sc.id} turn ${idx} vocabularyHints must be array`);
        }
        assert(t.validationCriteria, `Scenario ${sc.id} turn ${idx} missing validationCriteria`);
        assert(typeof t.validationCriteria.minWords === 'number', `Scenario ${sc.id} turn ${idx} missing minWords`);
    });
}
console.log(`[PASS] Verified ${esData.scenarios.length} Spanish and ${huData.scenarios.length} Hungarian conversation scenarios with A1/A2 English scaffolding.`);

console.log('\n--- Test 2: SpeakingStudio Tab & Lifecycle ---');

// Mock browser globals
global.window = global;
let lastRenderedHtml = '';
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {},
    getElementById: (id) => {
        if (id === 'sp-studio-body') {
            return {
                innerHTML: '',
                querySelector: () => null,
                querySelectorAll: () => []
            };
        }
        return null;
    },
    createElement: () => ({
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
    set: () => {}
};
global.Content = {
    json: async (p) => {
        if (p.includes('conversation-scenarios')) return esData;
        if (p.includes('speaking-prompts')) return { prompts: [] };
        return { pairs: [] };
    }
};

require('../../engine/drills/speaking.js');

const container = {
    innerHTML: '',
    querySelectorAll: () => [],
    querySelector: () => null
};

(async () => {
    await SpeakingDriller.render(container, { activeTab: 'scenarios' });
    assert(container.innerHTML.includes('Conversation Scenarios'), 'Speaking studio must render Conversation Scenarios tab');
    console.log('[PASS] SpeakingStudio renders Conversation Scenarios tab successfully.');
    SpeakingDriller.stop();

    console.log('\n--- Test 3: Zero Emojis in Scenarios Feature ---');
    const speakingJsContent = fs.readFileSync(path.resolve(__dirname, '../../engine/drills/speaking.js'), 'utf8');
    const lines = speakingJsContent.split('\n');
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
    const scenarioLinesWithEmojis = [];
    lines.forEach((line, idx) => {
        if (idx >= 1500 && idx <= 2350 && emojiRegex.test(line)) {
            scenarioLinesWithEmojis.push({ line: idx + 1, text: line.trim() });
        }
    });
    assert.strictEqual(scenarioLinesWithEmojis.length, 0, `Scenario code must contain zero emojis. Found: ${JSON.stringify(scenarioLinesWithEmojis)}`);
    console.log('[PASS] Verified zero emojis in conversation scenarios code.');

    console.log('\n--- Test 4: ParlourTTS.speak Signature & Invocation ---');
    let ttsCallArgs = null;
    global.ParlourTTS = {
        speak: (opts) => {
            ttsCallArgs = opts;
            return Promise.resolve(true);
        },
        stop: () => {}
    };

    // Render a specific scenario with autoStartScenario
    await SpeakingDriller.render(container, { scenarioId: 'es-a1-sc01-cafe', autoStartScenario: true });
    assert(ttsCallArgs !== null, 'Starting scenario session must invoke ParlourTTS.speak');
    assert.strictEqual(typeof ttsCallArgs, 'object', 'ParlourTTS.speak must be called with an options object');
    assert(ttsCallArgs.text && ttsCallArgs.text.length > 0, 'ParlourTTS.speak must receive text property');
    assert.strictEqual(ttsCallArgs.language, 'es', 'ParlourTTS.speak must receive correct language code');
    assert.strictEqual(ttsCallArgs.type, 'dialogue', 'ParlourTTS.speak must specify dialogue type');
    console.log('[PASS] Verified ParlourTTS.speak is invoked with proper options object { text, language, type: "dialogue" }.');

    console.log('\n--- Test 5: Debrief Screen Simplification & Custom Audio Player ---');
    const debriefCode = speakingJsContent.slice(speakingJsContent.indexOf('function _renderScenarioDebrief'), speakingJsContent.indexOf('function stop('));
    assert(!debriefCode.includes('sp-dimensions-grid'), 'Scenario debrief must not contain sp-dimensions-grid');
    assert(!debriefCode.includes('sp-dim-card'), 'Scenario debrief must not contain dimension score cards');
    assert(debriefCode.includes('coachSentence'), 'Scenario debrief must compute single extended coach/examiner sentence');
    assert(debriefCode.includes('_customAudioPlayerHtml'), 'Scenario debrief must invoke _customAudioPlayerHtml instead of raw browser audio controls');
    assert(speakingJsContent.includes('sp-custom-player'), 'Speaking studio must define sp-custom-player');
    assert(!debriefCode.includes('<audio controls'), 'Raw audio controls must be replaced with custom player in scenario debrief');
    console.log('[PASS] Verified debrief screen does not render 5 dimensions grid and uses Parlour custom player.');

    console.log('\n[ALL PASS] All conversation scenario tests passed cleanly!');
})();

