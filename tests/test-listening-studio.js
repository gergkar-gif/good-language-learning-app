/**
 * Test Suite for Listening Studio (CEFR Passage Comprehension + Sentence Decoding Drills)
 */
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('Testing Listening Studio Integration...');

// 1. Verify existence of engine and data files
const studioFile = path.join(__dirname, '../engine/drills/listening-studio.js');
assert(fs.existsSync(studioFile), 'engine/drills/listening-studio.js must exist');

const esTasksFile = path.join(__dirname, '../content/es-es/listening-tasks.json');
assert(fs.existsSync(esTasksFile), 'content/es-es/listening-tasks.json must exist');
const esTasks = JSON.parse(fs.readFileSync(esTasksFile, 'utf8'));
assert(Array.isArray(esTasks.tasks) && esTasks.tasks.length >= 3, 'es-es must have at least 3 listening tasks');

const latamTasksFile = path.join(__dirname, '../content/es-latam/listening-tasks.json');
assert(fs.existsSync(latamTasksFile), 'content/es-latam/listening-tasks.json must exist');
const latamTasks = JSON.parse(fs.readFileSync(latamTasksFile, 'utf8'));
assert(Array.isArray(latamTasks.tasks) && latamTasks.tasks.length >= 3, 'es-latam must have at least 3 listening tasks');

const huTasksFile = path.join(__dirname, '../content/hu/listening-tasks.json');
assert(fs.existsSync(huTasksFile), 'content/hu/listening-tasks.json must exist');
const huTasks = JSON.parse(fs.readFileSync(huTasksFile, 'utf8'));
assert(Array.isArray(huTasks.tasks) && huTasks.tasks.length >= 3, 'hu must have at least 3 listening tasks');

console.log('  [PASS] All task bank files exist and contain valid tasks.');

// 2. Validate CEFR task schema conformance
[...esTasks.tasks, ...latamTasks.tasks, ...huTasks.tasks].forEach(task => {
    assert(task.id, 'Task must have id');
    assert(['A1', 'A2', 'B1', 'B2', 'C1'].includes(task.level), `Task ${task.id} must have valid CEFR level`);
    assert(task.title, `Task ${task.id} must have title`);
    assert(task.audio && Array.isArray(task.audio.turns) && task.audio.turns.length > 0, `Task ${task.id} must have audio turns`);
    task.audio.turns.forEach((turn, idx) => {
        assert(turn.speaker, `Turn ${idx} in ${task.id} must have speaker`);
        assert(['male', 'female'].includes(turn.gender), `Turn ${idx} in ${task.id} must have valid gender`);
        assert(turn.text && turn.text.length > 0, `Turn ${idx} in ${task.id} must have text`);
    });
    assert(Array.isArray(task.questions) && task.questions.length >= 3, `Task ${task.id} must have at least 3 questions`);
    task.questions.forEach((q, idx) => {
        assert(q.id, `Question ${idx} in ${task.id} must have id`);
        assert(['listening-mc', 'true-false-not-stated'].includes(q.type), `Question ${q.id} must have valid type`);
        assert(typeof q.correct === 'number', `Question ${q.id} must have numeric correct answer index`);
        assert(q.evidence, `Question ${q.id} must have spoken evidence quote`);
        assert(q.explanation, `Question ${q.id} must have pedagogical explanation`);
    });
});
console.log('  [PASS] All tasks conform strictly to CEFR audio and question structure.');

// 3. Test ListeningStudio Module in simulated DOM environment
global.window = {};
global.document = {
    addEventListener: () => {},
    createElement: tag => ({
        textContent: '',
        innerHTML: '',
        style: {}
    }),
    getElementById: id => null
};
global.UI = {
    escape: s => String(s == null ? '' : s).replace(/</g, '&lt;').replace(/>/g, '&gt;'),
    showLoading: () => {},
    hideLoading: () => {}
};
global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    content: rel => rel
};
global.Content = {
    json: async url => {
        if (url.includes('listening-tasks.json')) return esTasks;
        return null;
    }
};

const ListeningStudio = require('../engine/drills/listening-studio.js');
assert(typeof ListeningStudio.render === 'function', 'ListeningStudio must expose render');
assert(typeof ListeningStudio.stop === 'function', 'ListeningStudio must expose stop');
assert(typeof ListeningStudio._loadTasks === 'function', 'ListeningStudio must expose _loadTasks');

// Mock container for rendering
const createMockContainer = () => {
    let _html = '';
    const listeners = {};
    return {
        get innerHTML() { return _html; },
        set innerHTML(val) { _html = val; },
        querySelector: sel => null,
        querySelectorAll: sel => []
    };
};

(async () => {
    const tasks = await ListeningStudio._loadTasks();
    assert(tasks.length >= 3, 'ListeningStudio must load tasks from task bank');
    console.log(`  [PASS] ListeningStudio._loadTasks() loaded ${tasks.length} tasks.`);

    // 4. Test Workshop.js registration
    const workshopCode = fs.readFileSync(path.join(__dirname, '../engine/workshop.js'), 'utf8');
    assert(workshopCode.includes("title: 'Listening Studio'"), "Workshop must register 'Listening Studio'");
    assert(workshopCode.includes("category: 'studios'"), "Workshop listening driller must have category 'studios'");
    assert(workshopCode.includes("listening: typeof ListeningStudio !== 'undefined' ? ListeningStudio"), "Workshop must map listening to ListeningStudio");
    assert(workshopCode.includes("if (id === 'listening-driller' || id === 'listening-decoding')"), "Workshop must transparently route listening-driller");
    assert(workshopCode.includes("if (id === 'listening-comprehension' || id === 'listening-studio')"), "Workshop must transparently route listening-comprehension");
    console.log('  [PASS] Workshop.js drillers configuration verified for Listening Studio.');

    // 5. Test index.html script tag
    const indexHtml = fs.readFileSync(path.join(__dirname, '../index.html'), 'utf8');
    assert(indexHtml.includes('engine/drills/listening-studio.js'), 'index.html must include listening-studio.js');
    console.log('  [PASS] index.html registration verified.');

    console.log('\nAll Listening Studio tests PASSED successfully!');
})();
