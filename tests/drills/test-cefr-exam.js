// tests/drills/test-cefr-exam.js
// Automated verification suite for CEFR Exam modules (DELE B1 & ECL B1)

const assert = require('assert');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const DELE_PATH = path.join(ROOT, 'content/es-es/dele-b1-exam.json');
const ECL_PATH = path.join(ROOT, 'content/hu/ecl-b1-exam.json');
const ENGINE_PATH = path.join(ROOT, 'engine/cefr-exam.js');
const WORKSHOP_PATH = path.join(ROOT, 'engine/workshop.js');
const INDEX_PATH = path.join(ROOT, 'index.html');

console.log('Testing CEFR Exam Modules (DELE B1 & ECL B1)...');

// 1. Emoji ban check
const EMOJI_REGEX = /[\u{1F300}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

function assertZeroEmojis(filePath, content) {
    const match = content.match(EMOJI_REGEX);
    assert(!match, `File ${filePath} contains forbidden emoji: ${match ? match[0] : ''}`);
}

const deleRaw = fs.readFileSync(DELE_PATH, 'utf-8');
const eclRaw = fs.readFileSync(ECL_PATH, 'utf-8');
const engineRaw = fs.readFileSync(ENGINE_PATH, 'utf-8');

assertZeroEmojis('content/es-es/dele-b1-exam.json', deleRaw);
assertZeroEmojis('content/hu/ecl-b1-exam.json', eclRaw);
assertZeroEmojis('engine/cefr-exam.js', engineRaw);
console.log('[PASS] Strict zero emojis verified across content and engine files.');

// 2. Validate DELE B1 data
const deleData = JSON.parse(deleRaw);
assert.strictEqual(deleData.id, 'es-dele-b1-exam');
assert.strictEqual(deleData.level, 'B1');
assert.strictEqual(deleData.board, 'Instituto Cervantes');
assert(deleData.skills, 'DELE B1 must have skills object');

const requiredSkills = ['reading', 'listening', 'writing', 'speaking'];
requiredSkills.forEach(sk => {
    assert(deleData.skills[sk], `DELE B1 must include ${sk} skill`);
    assert(Array.isArray(deleData.skills[sk].tareas) && deleData.skills[sk].tareas.length >= 2, `${sk} must have at least 2 tareas`);
});

// Reading checks
const readingTareas = deleData.skills.reading.tareas;
assert.strictEqual(readingTareas.length, 5, 'DELE B1 reading must have 5 tareas');
const t1 = readingTareas[0];
assert.strictEqual(t1.type, 'matching-notices');
assert.strictEqual(t1.people.length, 6, 'Reading T1 must have 6 people');
assert.strictEqual(t1.notices.length, 10, 'Reading T1 must have 10 notices');

const t2 = readingTareas[1];
assert.strictEqual(t2.type, 'reading-mc');
assert.strictEqual(t2.questions.length, 6, 'Reading T2 must have 6 questions');

const t3 = readingTareas[2];
assert.strictEqual(t3.type, 'person-matching');
assert.strictEqual(t3.people.length, 3, 'Reading T3 must have 3 people');
assert.strictEqual(t3.statements.length, 6, 'Reading T3 must have 6 statements');

const t4 = readingTareas[3];
assert.strictEqual(t4.type, 'gapped-text');
assert.strictEqual(t4.gaps.length, 6, 'Reading T4 must have 6 gaps');
assert.strictEqual(t4.options.length, 8, 'Reading T4 must have 8 options');

const t5 = readingTareas[4];
assert.strictEqual(t5.type, 'cloze-mc');
assert.strictEqual(t5.items.length, 6, 'Reading T5 must have 6 cloze items');

console.log('[PASS] DELE B1 Reading tasks structure verified (5 official tareas).');

// Listening checks
const listeningTareas = deleData.skills.listening.tareas;
assert.strictEqual(listeningTareas.length, 2, 'DELE B1 listening has pilot tareas authored');
assert(listeningTareas[0].previewSeconds >= 20, 'Listening must have previewSeconds');
assert(listeningTareas[0].items.length === 6, 'Listening T1 must have 6 items');

// Writing checks
const writingTareas = deleData.skills.writing.tareas;
assert.strictEqual(writingTareas.length, 2, 'DELE B1 writing must have 2 tareas');
assert(writingTareas[0].minWords === 100 && writingTareas[0].maxWords === 120, 'Writing T1 word count range 100-120');
assert(Array.isArray(writingTareas[1].options) && writingTareas[1].options.length === 2, 'Writing T2 must offer Option A and Option B');

// Speaking checks
const speakingTareas = deleData.skills.speaking.tareas;
assert.strictEqual(speakingTareas.length, 4, 'DELE B1 speaking must have 4 tareas');

// Strategies checks
assert(deleData.strategies, 'DELE B1 must include strategies');
assert(Array.isArray(deleData.strategies.connectors) && deleData.strategies.connectors.length >= 4, 'Must have at least 4 connector categories');

console.log('[PASS] Full DELE B1 skills and strategy data verified.');

// 3. Validate ECL B1 data
const eclData = JSON.parse(eclRaw);
assert.strictEqual(eclData.id, 'hu-ecl-b1-exam');
assert.strictEqual(eclData.level, 'B1');
requiredSkills.forEach(sk => {
    assert(eclData.skills[sk], `ECL B1 must include ${sk} skill`);
    assert(Array.isArray(eclData.skills[sk].tareas) && eclData.skills[sk].tareas.length >= 2, `ECL ${sk} must have at least 2 tareas`);
});
console.log('[PASS] ECL B1 Hungarian exam data verified.');

// 4. Validate engine exports
const CefrExam = require(ENGINE_PATH);
assert(typeof CefrExam === 'object', 'CefrExam must be exported as an object');
assert(typeof CefrExam.createModule === 'function', 'CefrExam.createModule must be a function');
assert(typeof CefrExam.DeleB1Exam === 'object', 'DeleB1Exam must be exported');
assert(typeof CefrExam.DeleB1Exam.render === 'function', 'DeleB1Exam.render must be a function');
assert(typeof CefrExam.DeleB1Exam.stop === 'function', 'DeleB1Exam.stop must be a function');

assert(typeof CefrExam.EclB1Exam === 'object', 'EclB1Exam must be exported');
assert(typeof CefrExam.EclB1Exam.render === 'function', 'EclB1Exam.render must be a function');
assert(typeof CefrExam.EclB1Exam.stop === 'function', 'EclB1Exam.stop must be a function');
console.log('[PASS] engine/cefr-exam.js factory and module exports verified.');

// 5. Validate Workshop integration
const workshopContent = fs.readFileSync(WORKSHOP_PATH, 'utf-8');
assert(workshopContent.includes("id: 'es-dele-b1-exam'"), 'workshop.js must register es-dele-b1-exam');
assert(workshopContent.includes("id: 'hu-ecl-b1-exam'"), 'workshop.js must register hu-ecl-b1-exam');
assert(workshopContent.includes("'es-dele-exam':"), 'workshop.js must include es-dele-exam icon');
assert(workshopContent.includes("'hu-ecl-exam':"), 'workshop.js must include hu-ecl-exam icon');
assert(workshopContent.includes("'es-dele-b1-exam':"), 'workshop.js _moduleFor must map es-dele-b1-exam');
assert(workshopContent.includes("'hu-ecl-b1-exam':"), 'workshop.js _moduleFor must map hu-ecl-b1-exam');
console.log('[PASS] engine/workshop.js integration verified.');

// 6. Validate index.html script inclusion
const indexContent = fs.readFileSync(INDEX_PATH, 'utf-8');
assert(indexContent.includes('src="engine/cefr-exam.js'), 'index.html must load engine/cefr-exam.js');
console.log('[PASS] index.html script tag verified.');

console.log('\n[ALL PASS] CEFR Exam Module verification suite completed successfully.');
