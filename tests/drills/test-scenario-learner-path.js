// ============================================
// TEST SCENARIO LEARNER PATH INTEGRATION
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('\n--- Test 1: Scenario Unit ID Mapping Integrity ---');

function checkCurriculumUnits(scenarioPath, curriculumPath, lang) {
    assert(fs.existsSync(scenarioPath), `Scenario path must exist: ${scenarioPath}`);
    assert(fs.existsSync(curriculumPath), `Curriculum path must exist: ${curriculumPath}`);

    const scenarioData = JSON.parse(fs.readFileSync(scenarioPath, 'utf8'));
    const curriculumData = JSON.parse(fs.readFileSync(curriculumPath, 'utf8'));

    const allUnitIds = new Set();
    Object.keys(curriculumData.levels || {}).forEach(lvl => {
        const levelObj = curriculumData.levels[lvl];
        (levelObj.units || []).forEach(u => {
            if (u.id) allUnitIds.add(u.id);
        });
    });

    assert(Array.isArray(scenarioData.scenarios) && scenarioData.scenarios.length > 0, `Scenarios must exist for ${lang}`);

    for (const sc of scenarioData.scenarios) {
        assert(Array.isArray(sc.unitIds) && sc.unitIds.length > 0, `Scenario ${sc.id} in ${lang} must have unitIds array`);
        for (const uid of sc.unitIds) {
            assert(allUnitIds.has(uid), `Scenario ${sc.id} references unit ${uid} which does not exist in ${lang} curriculum!`);
        }
    }
    console.log(`✓ All ${scenarioData.scenarios.length} scenarios in ${lang} map to valid curriculum units`);
}

const root = path.resolve(__dirname, '../..');
checkCurriculumUnits(
    path.join(root, 'content/es-latam/conversation-scenarios.json'),
    path.join(root, 'content/es-latam/curriculum/curriculum.json'),
    'es-latam'
);

if (fs.existsSync(path.join(root, 'content/es-es/conversation-scenarios.json'))) {
    checkCurriculumUnits(
        path.join(root, 'content/es-es/conversation-scenarios.json'),
        path.join(root, 'content/es-es/curriculum/curriculum.json'),
        'es-es'
    );
}

checkCurriculumUnits(
    path.join(root, 'content/hu/conversation-scenarios.json'),
    path.join(root, 'content/hu/curriculum/curriculum.json'),
    'hu'
);

console.log('\n--- Test 2: Recommendation Engine Unit Scenario Matching ---');

// Mock browser globals for recommendationEngine
const esScenarios = JSON.parse(fs.readFileSync(path.join(root, 'content/es-latam/conversation-scenarios.json'), 'utf8'));
const esCurriculum = JSON.parse(fs.readFileSync(path.join(root, 'content/es-latam/curriculum/curriculum.json'), 'utf8'));

global.Content = {
    async json(p) {
        if (p.includes('conversation-scenarios.json')) return esScenarios;
        if (p.includes('indexes/grammar-titles.json')) return {};
        throw new Error('Not found: ' + p);
    }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    content: (p) => `content/es-latam/${p}`,
    key: (k) => `es_${k}`
};

global.UI = {
    escape: (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
};

let dismissedList = [];
global.localStorage = {
    getItem: (k) => {
        if (k.includes('unitPracticeDismissed')) return JSON.stringify(dismissedList);
        return null;
    },
    setItem: (k, v) => {
        if (k.includes('unitPracticeDismissed')) dismissedList = JSON.parse(v);
    }
};

global.LearnerModel = {
    weakSkills: async () => [],
    weakWords: () => [],
    weakDrillers: () => [],
    weakProductionSkills: () => []
};

global.Recommend = {
    unitSkillFor: async (unit) => 'unit-skill-placeholder'
};

// Load RecommendationEngine
const RecommendationEngine = require('../../engine/recommendationEngine.js');

(async () => {
    // Test _scenarioForUnit
    const cafeScenario = await RecommendationEngine._scenarioForUnit('unit.a1.11');
    assert(cafeScenario, 'unit.a1.11 should match café scenario');
    assert.strictEqual(cafeScenario.id, 'es-a1-sc01-cafe');

    const noScenario = await RecommendationEngine._scenarioForUnit('unit.nonexistent');
    assert.strictEqual(noScenario, null, 'Nonexistent unit should return null');

    console.log('✓ _scenarioForUnit resolves mapped scenario correctly');

    console.log('\n--- Test 3: Milestone Capstone Practice Nudge Surfaces Scenario ---');

    // Unit unit.a1.11 has lessons. Let's find the last lesson of unit.a1.11
    const a1Units = esCurriculum.levels.A1.units;
    const cafeUnit = a1Units.find(u => u.id === 'unit.a1.11');
    assert(cafeUnit, 'unit.a1.11 must exist in A1');
    const lastLesson = cafeUnit.lessons[cafeUnit.lessons.length - 1];

    global.LearnerPath = {
        lastCompletedLessonId: () => lastLesson.id,
        unitFor: (lid) => ({ levelKey: 'A1', unit: cafeUnit }),
        nextStep: () => ({ kind: 'lesson', lesson: { id: 'next.lesson', title: 'Next Lesson' }, level: 'A1' }),
        completedCount: () => 15,
        currentLevel: () => 'A1'
    };

    dismissedList = [];
    const nudge = await RecommendationEngine._practiceNudge();
    assert(nudge, 'Practice nudge should be generated');
    assert.strictEqual(nudge.type, 'scenario', 'Nudge type must be scenario');
    assert.strictEqual(nudge.scenario.id, 'es-a1-sc01-cafe', 'Nudge scenario must be es-a1-sc01-cafe');
    assert.strictEqual(nudge.unit.id, 'unit.a1.11');
    console.log('✓ Unit completion generates scenario milestone nudge');

    // Regression: recommend() wraps this result via
    // Object.assign({ kind: 'unit-nudge' }, nudge). If `nudge` carried its
    // own `kind` field (it used to, until 2026-09-23 — see the `type` field
    // above), that field would win the merge and silently overwrite
    // 'unit-nudge', so every caller checking primary.kind === 'unit-nudge'
    // (engine/home.js's render, this engine's own _nextActionInfo/_routeTo)
    // would never fire. Asserting the merge directly here, the same way
    // recommend() performs it, catches that regression without having to
    // mock recommend()'s unrelated candidate sources (window, LearnerPath.currentLevel, etc).
    const wrapped = Object.assign({ kind: 'unit-nudge' }, nudge);
    assert.strictEqual(wrapped.kind, 'unit-nudge', 'recommend()-style wrapping must keep kind as unit-nudge');
    console.log('✓ Practice nudge survives recommend()\'s kind:unit-nudge wrapping');

    console.log('\n--- Test 4: Mini-game Candidate Surfaces Oral Roleplay ---');
    // If not the last lesson (e.g. lesson 1 of cafeUnit)
    const firstLesson = cafeUnit.lessons[0];
    global.LearnerPath.lastCompletedLessonId = () => firstLesson.id;

    const mini = await RecommendationEngine._miniGameNudge();
    assert(mini, 'Mini-game nudge should be generated');
    assert(mini.drillerId === 'speaking' || (mini.alt && mini.alt.drillerId === 'speaking'), 'Speaking scenario roleplay should be a candidate');
    if (mini.drillerId === 'speaking') {
        assert.strictEqual(mini.challengeTitle, 'Oral Roleplay');
        assert.strictEqual(mini.options.scenarioId, 'es-a1-sc01-cafe');
        assert.strictEqual(mini.options.returnTab, 'home');
    }
    console.log('✓ Mini-game candidate surfaces oral roleplay for matching lesson unit');

    console.log('\n--- Test 5: Parlour Style Zero-Emoji Check ---');
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

    const wholeFilesToCheck = [
        'engine/curriculum.js',
        'engine/recommendationEngine.js',
        'engine/home.js',
        'content/es-latam/conversation-scenarios.json',
        'content/hu/conversation-scenarios.json'
    ];

    for (const f of wholeFilesToCheck) {
        const fullPath = path.join(root, f);
        const content = fs.readFileSync(fullPath, 'utf8');
        assert(!emojiRegex.test(content), `File ${f} contains emojis, violating Parlour constructivist style!`);
    }

    // For speaking.js, check the scenario integration section (lines 1500+)
    const speakingLines = fs.readFileSync(path.join(root, 'engine/drills/speaking.js'), 'utf8').split('\n');
    speakingLines.slice(1500).forEach((line, idx) => {
        assert(!emojiRegex.test(line), `Speaking scenario line ${idx + 1501} contains emojis!`);
    });
    console.log('✓ Zero emojis across all modified engine and scenario files');

    console.log('\nALL SCENARIO LEARNER PATH TESTS PASSED!\n');
})().catch(err => {
    console.error('Test failure:', err);
    process.exit(1);
});
