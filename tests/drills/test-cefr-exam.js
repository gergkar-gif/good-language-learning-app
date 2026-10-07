// tests/drills/test-cefr-exam.js
// Automated verification suite for CEFR Exam modules (DELE A1, DELE A2, DELE B1, ECL A1, ECL A2, ECL B1)

const assert = require('assert');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const DELE_A1_PATH = path.join(ROOT, 'content/es-es/dele-a1-exam.json');
const DELE_A2_PATH = path.join(ROOT, 'content/es-es/dele-a2-exam.json');
const DELE_B1_PATH = path.join(ROOT, 'content/es-es/dele-b1-exam.json');
const ECL_A1_PATH = path.join(ROOT, 'content/hu/ecl-a1-exam.json');
const ECL_A2_PATH = path.join(ROOT, 'content/hu/ecl-a2-exam.json');
const ECL_B1_PATH = path.join(ROOT, 'content/hu/ecl-b1-exam.json');
const LATAM_A1_PATH = path.join(ROOT, 'content/es-latam/dele-a1-exam.json');
const LATAM_A2_PATH = path.join(ROOT, 'content/es-latam/dele-a2-exam.json');
const ENGINE_PATH = path.join(ROOT, 'engine/cefr-exam.js');
const WORKSHOP_PATH = path.join(ROOT, 'engine/workshop.js');
const INDEX_PATH = path.join(ROOT, 'index.html');

console.log('Testing CEFR Exam Modules (DELE A1, DELE A2, DELE B1, ECL A1, ECL A2, ECL B1)...');

// 1. Emoji ban check
const EMOJI_REGEX = /[\u{1F300}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

function assertZeroEmojis(filePath, content) {
    const match = content.match(EMOJI_REGEX);
    assert(!match, `File ${filePath} contains forbidden emoji: ${match ? match[0] : ''}`);
}

const deleA1Raw = fs.readFileSync(DELE_A1_PATH, 'utf-8');
const deleA2Raw = fs.readFileSync(DELE_A2_PATH, 'utf-8');
const deleB1Raw = fs.readFileSync(DELE_B1_PATH, 'utf-8');
const eclA1Raw = fs.readFileSync(ECL_A1_PATH, 'utf-8');
const eclA2Raw = fs.readFileSync(ECL_A2_PATH, 'utf-8');
const eclB1Raw = fs.readFileSync(ECL_B1_PATH, 'utf-8');
const latamA1Raw = fs.readFileSync(LATAM_A1_PATH, 'utf-8');
const latamA2Raw = fs.readFileSync(LATAM_A2_PATH, 'utf-8');
const engineRaw = fs.readFileSync(ENGINE_PATH, 'utf-8');

assertZeroEmojis('content/es-es/dele-a1-exam.json', deleA1Raw);
assertZeroEmojis('content/es-es/dele-a2-exam.json', deleA2Raw);
assertZeroEmojis('content/es-es/dele-b1-exam.json', deleB1Raw);
assertZeroEmojis('content/hu/ecl-a1-exam.json', eclA1Raw);
assertZeroEmojis('content/hu/ecl-a2-exam.json', eclA2Raw);
assertZeroEmojis('content/hu/ecl-b1-exam.json', eclB1Raw);
assertZeroEmojis('content/es-latam/dele-a1-exam.json', latamA1Raw);
assertZeroEmojis('content/es-latam/dele-a2-exam.json', latamA2Raw);
assertZeroEmojis('engine/cefr-exam.js', engineRaw);
console.log('[PASS] Strict zero emojis verified across content and engine files.');

// 2. Validate DELE B1 data
const deleB1Data = JSON.parse(deleB1Raw);
assert.strictEqual(deleB1Data.id, 'es-dele-b1-exam');
assert.strictEqual(deleB1Data.level, 'B1');
assert.strictEqual(deleB1Data.board, 'Instituto Cervantes');
assert(deleB1Data.skills, 'DELE B1 must have skills object');

const requiredSkills = ['reading', 'listening', 'writing', 'speaking'];
requiredSkills.forEach(sk => {
    assert(deleB1Data.skills[sk], `DELE B1 must include ${sk} skill`);
    assert(Array.isArray(deleB1Data.skills[sk].tareas) && deleB1Data.skills[sk].tareas.length >= 2, `${sk} must have at least 2 tareas`);
});

// Reading checks DELE B1
const readingTareasB1 = deleB1Data.skills.reading.tareas;
assert.strictEqual(readingTareasB1.length, 5, 'DELE B1 reading must have 5 tareas');
assert.strictEqual(readingTareasB1[0].type, 'matching-notices');
assert.strictEqual(readingTareasB1[1].type, 'reading-mc');
assert.strictEqual(readingTareasB1[2].type, 'person-matching');
assert.strictEqual(readingTareasB1[3].type, 'gapped-text');
assert.strictEqual(readingTareasB1[4].type, 'cloze-mc');
console.log('[PASS] Full DELE B1 skills and strategy data verified.');

// 3. Validate DELE A1 data
const deleA1Data = JSON.parse(deleA1Raw);
assert.strictEqual(deleA1Data.id, 'es-dele-a1-exam');
assert.strictEqual(deleA1Data.level, 'A1');
assert.strictEqual(deleA1Data.board, 'Instituto Cervantes');
assert(deleA1Data.skills, 'DELE A1 must have skills object');

requiredSkills.forEach(sk => {
    assert(deleA1Data.skills[sk], `DELE A1 must include ${sk} skill`);
    assert(Array.isArray(deleA1Data.skills[sk].tareas) && deleA1Data.skills[sk].tareas.length >= 2, `DELE A1 ${sk} must have at least 2 tareas`);
});

const readingTareasA1 = deleA1Data.skills.reading.tareas;
assert.strictEqual(readingTareasA1.length, 4, 'DELE A1 reading must have 4 official tareas');
assert.strictEqual(readingTareasA1[0].type, 'reading-mc', 'Reading T1 must be reading-mc');
assert.strictEqual(readingTareasA1[0].questions.length, 5, 'Reading T1 must have 5 questions');
assert.strictEqual(readingTareasA1[1].type, 'matching-notices', 'Reading T2 must be matching-notices');
assert.strictEqual(readingTareasA1[1].people.length, 6, 'Reading T2 must have 6 people');
assert.strictEqual(readingTareasA1[1].notices.length, 10, 'Reading T2 must have 10 notices');
assert.strictEqual(readingTareasA1[2].type, 'person-matching', 'Reading T3 must be person-matching');
assert.strictEqual(readingTareasA1[2].people.length, 3, 'Reading T3 must have 3 people');
assert.strictEqual(readingTareasA1[2].statements.length, 6, 'Reading T3 must have 6 statements');
assert.strictEqual(readingTareasA1[3].type, 'cloze-mc', 'Reading T4 must be cloze-mc');
assert.strictEqual(readingTareasA1[3].items.length, 6, 'Reading T4 must have 6 items');

const listeningTareasA1 = deleA1Data.skills.listening.tareas;
assert.strictEqual(listeningTareasA1.length, 2, 'DELE A1 listening must have 2 tareas');
assert.strictEqual(listeningTareasA1[0].type, 'audio-mc');
assert.strictEqual(listeningTareasA1[0].items.length, 6, 'Listening T1 must have 6 audio items');
assert.strictEqual(listeningTareasA1[1].type, 'audio-interview');
assert.strictEqual(listeningTareasA1[1].questions.length, 4, 'Listening T2 must have 4 questions');

const writingTareasA1 = deleA1Data.skills.writing.tareas;
assert.strictEqual(writingTareasA1.length, 2, 'DELE A1 writing must have 2 tareas');
assert.strictEqual(writingTareasA1[0].minWords, 30, 'DELE A1 writing T1 minWords must be 30');
assert.strictEqual(writingTareasA1[0].maxWords, 40, 'DELE A1 writing T1 maxWords must be 40');
assert(Array.isArray(writingTareasA1[1].options) && writingTareasA1[1].options.length === 2, 'DELE A1 writing T2 must have 2 options');

const speakingTareasA1 = deleA1Data.skills.speaking.tareas;
assert.strictEqual(speakingTareasA1.length, 3, 'DELE A1 speaking must have 3 tareas');

console.log('[PASS] Full DELE A1 skills and tasks structure verified.');

// 4. Validate DELE A2 data
const deleA2Data = JSON.parse(deleA2Raw);
assert.strictEqual(deleA2Data.id, 'es-dele-a2-exam');
assert.strictEqual(deleA2Data.level, 'A2');
assert.strictEqual(deleA2Data.board, 'Instituto Cervantes');
assert(deleA2Data.skills, 'DELE A2 must have skills object');

requiredSkills.forEach(sk => {
    assert(deleA2Data.skills[sk], `DELE A2 must include ${sk} skill`);
    assert(Array.isArray(deleA2Data.skills[sk].tareas) && deleA2Data.skills[sk].tareas.length >= 2, `DELE A2 ${sk} must have at least 2 tareas`);
});

const readingTareasA2 = deleA2Data.skills.reading.tareas;
assert.strictEqual(readingTareasA2.length, 4, 'DELE A2 reading must have 4 official tareas');
assert.strictEqual(readingTareasA2[0].type, 'reading-mc', 'Reading T1 must be reading-mc');
assert.strictEqual(readingTareasA2[0].questions.length, 5, 'Reading T1 must have 5 questions');
assert.strictEqual(readingTareasA2[1].type, 'matching-notices', 'Reading T2 must be matching-notices');
assert.strictEqual(readingTareasA2[1].people.length, 6, 'Reading T2 must have 6 people');
assert.strictEqual(readingTareasA2[1].notices.length, 10, 'Reading T2 must have 10 notices');
assert.strictEqual(readingTareasA2[2].type, 'person-matching', 'Reading T3 must be person-matching');
assert.strictEqual(readingTareasA2[2].people.length, 3, 'Reading T3 must have 3 people');
assert.strictEqual(readingTareasA2[2].statements.length, 6, 'Reading T3 must have 6 statements');
assert.strictEqual(readingTareasA2[3].type, 'cloze-mc', 'Reading T4 must be cloze-mc');
assert.strictEqual(readingTareasA2[3].items.length, 6, 'Reading T4 must have 6 items');

const listeningTareasA2 = deleA2Data.skills.listening.tareas;
assert.strictEqual(listeningTareasA2.length, 2, 'DELE A2 listening must have 2 tareas');
assert.strictEqual(listeningTareasA2[0].type, 'audio-mc');
assert.strictEqual(listeningTareasA2[0].items.length, 6, 'Listening T1 must have 6 audio items');
assert.strictEqual(listeningTareasA2[1].type, 'audio-interview');
assert.strictEqual(listeningTareasA2[1].questions.length, 6, 'Listening T2 must have 6 questions');

const writingTareasA2 = deleA2Data.skills.writing.tareas;
assert.strictEqual(writingTareasA2.length, 2, 'DELE A2 writing must have 2 tareas');
assert.strictEqual(writingTareasA2[0].minWords, 50, 'DELE A2 writing T1 minWords must be 50');
assert.strictEqual(writingTareasA2[0].maxWords, 65, 'DELE A2 writing T1 maxWords must be 65');
assert(Array.isArray(writingTareasA2[1].options) && writingTareasA2[1].options.length === 2, 'DELE A2 writing T2 must have 2 options');

const speakingTareasA2 = deleA2Data.skills.speaking.tareas;
assert.strictEqual(speakingTareasA2.length, 3, 'DELE A2 speaking must have 3 tareas');

console.log('[PASS] Full DELE A2 skills and tasks structure verified.');

// 5. Validate ECL B1 data
const eclB1Data = JSON.parse(eclB1Raw);
assert.strictEqual(eclB1Data.id, 'hu-ecl-b1-exam');
assert.strictEqual(eclB1Data.level, 'B1');
requiredSkills.forEach(sk => {
    assert(eclB1Data.skills[sk], `ECL B1 must include ${sk} skill`);
    assert(Array.isArray(eclB1Data.skills[sk].tareas) && eclB1Data.skills[sk].tareas.length >= 2, `ECL ${sk} must have at least 2 tareas`);
});
console.log('[PASS] ECL B1 Hungarian exam data verified.');

// 6. Validate ECL A1 data
const eclA1Data = JSON.parse(eclA1Raw);
assert.strictEqual(eclA1Data.id, 'hu-ecl-a1-exam');
assert.strictEqual(eclA1Data.level, 'A1');
assert.strictEqual(eclA1Data.board, 'Pécsi Tudományegyetem / Nemzetközi ECL Központ');
requiredSkills.forEach(sk => {
    assert(eclA1Data.skills[sk], `ECL A1 must include ${sk} skill`);
    assert(Array.isArray(eclA1Data.skills[sk].tareas) && eclA1Data.skills[sk].tareas.length >= 2, `ECL A1 ${sk} must have at least 2 tareas`);
});

const huReadingA1 = eclA1Data.skills.reading.tareas;
assert.strictEqual(huReadingA1.length, 2, 'ECL A1 reading has 2 tareas');
assert.strictEqual(huReadingA1[0].type, 'matching-notices');
assert.strictEqual(huReadingA1[0].people.length, 6);
assert.strictEqual(huReadingA1[0].notices.length, 10);
assert.strictEqual(huReadingA1[1].type, 'reading-mc');
assert.strictEqual(huReadingA1[1].questions.length, 5);

const huListeningA1 = eclA1Data.skills.listening.tareas;
assert.strictEqual(huListeningA1.length, 2, 'ECL A1 listening has 2 tareas');
assert.strictEqual(huListeningA1[0].items.length, 4);
assert.strictEqual(huListeningA1[1].questions.length, 4);

const huWritingA1 = eclA1Data.skills.writing.tareas;
assert.strictEqual(huWritingA1.length, 2, 'ECL A1 writing has 2 tareas');
assert.strictEqual(huWritingA1[0].minWords, 30);
assert.strictEqual(huWritingA1[0].maxWords, 40);
assert(Array.isArray(huWritingA1[1].options) && huWritingA1[1].options.length === 2);

console.log('[PASS] ECL A1 Hungarian exam data verified.');

// 7. Validate ECL A2 data
const eclA2Data = JSON.parse(eclA2Raw);
assert.strictEqual(eclA2Data.id, 'hu-ecl-a2-exam');
assert.strictEqual(eclA2Data.level, 'A2');
assert.strictEqual(eclA2Data.board, 'Pécsi Tudományegyetem / Nemzetközi ECL Központ');
requiredSkills.forEach(sk => {
    assert(eclA2Data.skills[sk], `ECL A2 must include ${sk} skill`);
    assert(Array.isArray(eclA2Data.skills[sk].tareas) && eclA2Data.skills[sk].tareas.length >= 2, `ECL A2 ${sk} must have at least 2 tareas`);
});

const huReadingA2 = eclA2Data.skills.reading.tareas;
assert.strictEqual(huReadingA2.length, 2, 'ECL A2 reading has 2 tareas');
assert.strictEqual(huReadingA2[0].type, 'matching-notices');
assert.strictEqual(huReadingA2[0].people.length, 6);
assert.strictEqual(huReadingA2[0].notices.length, 10);
assert.strictEqual(huReadingA2[1].type, 'reading-mc');
assert.strictEqual(huReadingA2[1].questions.length, 5);

const huListeningA2 = eclA2Data.skills.listening.tareas;
assert.strictEqual(huListeningA2.length, 2, 'ECL A2 listening has 2 tareas');
assert.strictEqual(huListeningA2[0].items.length, 5);
assert.strictEqual(huListeningA2[1].questions.length, 5);

const huWritingA2 = eclA2Data.skills.writing.tareas;
assert.strictEqual(huWritingA2.length, 2, 'ECL A2 writing has 2 tareas');
assert.strictEqual(huWritingA2[0].minWords, 50);
assert.strictEqual(huWritingA2[0].maxWords, 65);
assert(Array.isArray(huWritingA2[1].options) && huWritingA2[1].options.length === 2);

const huSpeakingA2 = eclA2Data.skills.speaking.tareas;
assert.strictEqual(huSpeakingA2.length, 2, 'ECL A2 speaking has 2 tareas');

console.log('[PASS] ECL A2 Hungarian exam data verified.');

// 8. Validate Latin American Spanish model (no vosotros)
assert(!latamA1Raw.includes('vosotros'), 'es-latam dele-a1-exam.json must not include vosotros');
assert(!latamA1Raw.includes('podéis'), 'es-latam dele-a1-exam.json must not include podéis');
assert(!latamA1Raw.includes('confirmad'), 'es-latam dele-a1-exam.json must not include confirmad');
assert(!latamA2Raw.includes('vosotros'), 'es-latam dele-a2-exam.json must not include vosotros');
assert(!latamA2Raw.includes('podéis'), 'es-latam dele-a2-exam.json must not include podéis');
assert(!latamA2Raw.includes('confirmad'), 'es-latam dele-a2-exam.json must not include confirmad');
assert(!latamA2Raw.includes('sabéis'), 'es-latam dele-a2-exam.json must not include sabéis');
console.log('[PASS] Latin American Spanish variants conform strictly to no-vosotros rule.');

// 9. Validate engine exports
const CefrExam = require(ENGINE_PATH);
assert(typeof CefrExam === 'object', 'CefrExam must be exported as an object');
assert(typeof CefrExam.createModule === 'function', 'CefrExam.createModule must be a function');

assert(typeof CefrExam.DeleA1Exam === 'object', 'DeleA1Exam must be exported');
assert(typeof CefrExam.DeleA1Exam.render === 'function', 'DeleA1Exam.render must be a function');
assert(typeof CefrExam.DeleA1Exam.stop === 'function', 'DeleA1Exam.stop must be a function');

assert(typeof CefrExam.DeleA2Exam === 'object', 'DeleA2Exam must be exported');
assert(typeof CefrExam.DeleA2Exam.render === 'function', 'DeleA2Exam.render must be a function');
assert(typeof CefrExam.DeleA2Exam.stop === 'function', 'DeleA2Exam.stop must be a function');

assert(typeof CefrExam.DeleB1Exam === 'object', 'DeleB1Exam must be exported');
assert(typeof CefrExam.DeleB1Exam.render === 'function', 'DeleB1Exam.render must be a function');
assert(typeof CefrExam.DeleB1Exam.stop === 'function', 'DeleB1Exam.stop must be a function');

assert(typeof CefrExam.EclA1Exam === 'object', 'EclA1Exam must be exported');
assert(typeof CefrExam.EclA1Exam.render === 'function', 'EclA1Exam.render must be a function');
assert(typeof CefrExam.EclA1Exam.stop === 'function', 'EclA1Exam.stop must be a function');

assert(typeof CefrExam.EclA2Exam === 'object', 'EclA2Exam must be exported');
assert(typeof CefrExam.EclA2Exam.render === 'function', 'EclA2Exam.render must be a function');
assert(typeof CefrExam.EclA2Exam.stop === 'function', 'EclA2Exam.stop must be a function');

assert(typeof CefrExam.EclB1Exam === 'object', 'EclB1Exam must be exported');
assert(typeof CefrExam.EclB1Exam.render === 'function', 'EclB1Exam.render must be a function');
assert(typeof CefrExam.EclB1Exam.stop === 'function', 'EclB1Exam.stop must be a function');
console.log('[PASS] engine/cefr-exam.js factory and 6 module exports verified.');

// 10. Validate Workshop integration
const workshopContent = fs.readFileSync(WORKSHOP_PATH, 'utf-8');
assert(workshopContent.includes("id: 'es-dele-a1-exam'"), 'workshop.js must register es-dele-a1-exam');
assert(workshopContent.includes("id: 'es-dele-a2-exam'"), 'workshop.js must register es-dele-a2-exam');
assert(workshopContent.includes("id: 'es-dele-b1-exam'"), 'workshop.js must register es-dele-b1-exam');
assert(workshopContent.includes("id: 'hu-ecl-a1-exam'"), 'workshop.js must register hu-ecl-a1-exam');
assert(workshopContent.includes("id: 'hu-ecl-a2-exam'"), 'workshop.js must register hu-ecl-a2-exam');
assert(workshopContent.includes("id: 'hu-ecl-b1-exam'"), 'workshop.js must register hu-ecl-b1-exam');
assert(workshopContent.includes("'es-dele-exam':"), 'workshop.js must include es-dele-exam icon');
assert(workshopContent.includes("'hu-ecl-exam':"), 'workshop.js must include hu-ecl-exam icon');
assert(workshopContent.includes("'es-dele-a1-exam':"), 'workshop.js _moduleFor must map es-dele-a1-exam');
assert(workshopContent.includes("'es-dele-a2-exam':"), 'workshop.js _moduleFor must map es-dele-a2-exam');
assert(workshopContent.includes("'es-dele-b1-exam':"), 'workshop.js _moduleFor must map es-dele-b1-exam');
assert(workshopContent.includes("'hu-ecl-a1-exam':"), 'workshop.js _moduleFor must map hu-ecl-a1-exam');
assert(workshopContent.includes("'hu-ecl-a2-exam':"), 'workshop.js _moduleFor must map hu-ecl-a2-exam');
assert(workshopContent.includes("'hu-ecl-b1-exam':"), 'workshop.js _moduleFor must map hu-ecl-b1-exam');
assert(workshopContent.includes('data-wk-tab="exams"'), 'workshop.js must include Exam Preparation tab button');
assert(workshopContent.includes('data-wk-tab="practice"'), 'workshop.js must include Practice tab button');
assert(!workshopContent.includes('wk-level-pills'), 'workshop.js must not include pill filters');
assert(workshopContent.includes('setTab'), 'workshop.js must export setTab');
console.log('[PASS] engine/workshop.js integration and Exam Preparation tab verified.');

// 11. Validate index.html script inclusion
const indexContent = fs.readFileSync(INDEX_PATH, 'utf-8');
assert(indexContent.includes('src="engine/cefr-exam.js'), 'index.html must load engine/cefr-exam.js');
console.log('[PASS] index.html script tag verified.');

// 12. Validate UI layout, audio runner, and back button
assert(engineRaw.includes('cefr-reading-stack'), 'cefr-exam.js must implement Option 1 cefr-reading-stack');
assert(engineRaw.includes('cefr-reading-stimulus-card'), 'cefr-exam.js must include stimulus card');
assert(engineRaw.includes('cefr-reading-questions-block'), 'cefr-exam.js must include questions block below');
assert(!engineRaw.includes('cefr-dual-pane'), 'cefr-exam.js must not retain old cefr-dual-pane');
assert(engineRaw.includes('ParlourTTS.speak('), 'ParlourTTS.speak must be called with options object');
assert(engineRaw.includes('play-single-item'), 'cefr-exam.js must support discrete listening item play');
assert(engineRaw.includes('cefr-back-icon') && engineRaw.includes('polyline'), 'cefr-exam.js back button must use vector SVG chevron');
console.log('[PASS] Option 1 reading stack, TTS playback signatures, and vector back button verified.');

console.log('\n[ALL PASS] CEFR Exam Module verification suite completed successfully.');
