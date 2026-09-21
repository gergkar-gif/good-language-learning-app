// Unit Test: In-Lesson Story Character Voice Assignment & ParlourTTS Attributes
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

global.window = { PARLOUR_TTS_ENDPOINT: 'https://test-worker.local/synthesize' };
global.navigator = { onLine: true };
global.document = {
    addEventListener: () => {},
    querySelectorAll: () => []
};
global.Speech = { sayable: (t) => t, available: () => true };
global.Art = { icon: () => '<svg></svg>' };

console.log('--- Test 1: ParlourTTS.button with Character and Gender Attributes ---');
const ParlourTTS = require('../../engine/tts.js');
assert(ParlourTTS, 'ParlourTTS must be exported');

const btnHtml = ParlourTTS.button('Buenos días, Carlos.', {
    type: 'story',
    character: 'Kore',
    gender: 'female'
});

assert(btnHtml.includes('data-tts-character="Kore"'), 'Button must include data-tts-character="Kore"');
assert(btnHtml.includes('data-tts-gender="female"'), 'Button must include data-tts-gender="female"');
assert(btnHtml.includes('data-tts-type="story"'), 'Button must include data-tts-type="story"');
console.log('[PASS] ParlourTTS.button correctly emits character, gender, and type attributes.');

console.log('\n--- Test 2: Reader.assignCharacterVoices on "Una mañana ocupada en Hanói" ---');
const readerCode = fs.readFileSync(path.join(__dirname, '../../engine/reader.js'), 'utf8');
const readerContext = {
    window: global.window,
    document: global.document,
    navigator: global.navigator,
    console: console,
    Lang: { code: () => 'es', content: (p) => p },
    Lexicon: { isLoaded: () => true, lookup: () => ({ readings: [] }), stripExplanatoryClauses: (t) => t },
    Speech: { button: () => '' },
    ParlourTTS: ParlourTTS,
    Art: global.Art
};
vm.createContext(readerContext);
vm.runInContext(readerCode, readerContext);

const Reader = readerContext.window.Reader;
assert(Reader, 'Reader must be defined on window');
assert.strictEqual(typeof Reader.assignCharacterVoices, 'function', 'Reader.assignCharacterVoices must be exposed');
assert.strictEqual(typeof Reader.inferCharacterGender, 'function', 'Reader.inferCharacterGender must be exposed');

const storyPath = path.join(__dirname, '../../content/es-es/stories/original/a1/a1-reflexive.json');
assert(fs.existsSync(storyPath), 'Story file must exist');
const story = JSON.parse(fs.readFileSync(storyPath, 'utf8'));

const assigned = Reader.assignCharacterVoices(story);
assert(assigned, 'Voices must be assigned');
assert.strictEqual(assigned._genders.Meg, 'female', 'Meg must be inferred as female');
assert.strictEqual(assigned._genders.Carlos, 'male', 'Carlos must be inferred as male');
assert(['Kore', 'Aoede', 'Leda', 'Zephyr', 'Callirrhoe', 'Autonoe'].includes(assigned.Meg), 'Meg voice must be from female pool');
assert(['Charon', 'Enceladus', 'Algieba', 'Achird', 'Algenib', 'Alnilam'].includes(assigned.Carlos), 'Carlos voice must be from male pool');

console.log(`[PASS] "Una mañana ocupada en Hanói" character voice casting: Meg=${assigned.Meg} (${assigned._genders.Meg}), Carlos=${assigned.Carlos} (${assigned._genders.Carlos})`);

console.log('\n--- Test 3: In-Lesson stepRenderers.story Voice Tagging ---');
const lessonsCode = fs.readFileSync(path.join(__dirname, '../../engine/lessons.js'), 'utf8');

const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const say = (text, options) => ParlourTTS.button(text, options);

const lessonContext = {
    window: { Reader },
    document: global.document,
    navigator: global.navigator,
    console: console,
    Reader: Reader,
    Lang: { code: () => 'es', name: () => 'Spanish' },
    ParlourTTS: ParlourTTS,
    say: say,
    Speech: global.Speech,
    Art: global.Art,
    esc: esc,
    escMd: (s) => String(s || '')
};
vm.createContext(lessonContext);

const step = {
    type: 'story',
    title: story.title,
    lines: story.paragraphs,
    characterVoices: assigned,
    characterGenders: assigned._genders
};

const extractRenderer = lessonsCode.match(/story\(step\) {([\s\S]*?)\r?\n\s*},\r?\n\s*'multiple-choice'/);
assert(extractRenderer, 'Could not extract story renderer');

const renderStory = vm.runInContext('(function(step) {' + extractRenderer[1] + '})', lessonContext);
const html = renderStory(step);

assert(html.includes('Meg'), 'HTML must contain Meg');
assert(html.includes('Carlos'), 'HTML must contain Carlos');

// Verify Meg's lines get Meg's character voice and female gender
assert(html.includes(`data-tts-character="${assigned.Meg}"`), `HTML must contain Meg voice attribute (${assigned.Meg})`);
assert(html.includes('data-tts-gender="female"'), 'HTML must contain female gender attribute');

// Verify Carlos's lines get Carlos's character voice and male gender
assert(html.includes(`data-tts-character="${assigned.Carlos}"`), `HTML must contain Carlos voice attribute (${assigned.Carlos})`);
assert(html.includes('data-tts-gender="male"'), 'HTML must contain male gender attribute');

console.log('[PASS] Story renderer produced correct data-tts-character and data-tts-gender for both Meg and Carlos.');

console.log('\n==========================================================');
console.log('ALL IN-LESSON CHARACTER VOICE TESTS PASSED');
console.log('==========================================================');
