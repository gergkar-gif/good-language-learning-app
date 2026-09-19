// ============================================
// CONVERSATION SCENARIOS TEST SUITE
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('\n--- Test 1: Content Schema & Seed Scenarios Verification ---');

const esPath = path.resolve(__dirname, '../../content/es/conversation-scenarios.json');
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

    sc.turns.forEach((t, idx) => {
        assert(t.turnIndex === idx + 1, `Scenario ${sc.id} turn ${idx} index mismatch`);
        assert(t.interlocutorPrompt, `Scenario ${sc.id} turn ${idx} missing interlocutorPrompt`);
        assert(t.learnerCue, `Scenario ${sc.id} turn ${idx} missing learnerCue`);
        assert(t.validationCriteria, `Scenario ${sc.id} turn ${idx} missing validationCriteria`);
        assert(typeof t.validationCriteria.minWords === 'number', `Scenario ${sc.id} turn ${idx} missing minWords`);
    });
}
console.log(`[PASS] Verified ${esData.scenarios.length} Spanish and ${huData.scenarios.length} Hungarian conversation scenarios.`);

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
    console.log('\n[ALL PASS] All conversation scenario tests passed cleanly!');
})();
