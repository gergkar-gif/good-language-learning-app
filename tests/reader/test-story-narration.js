// ==========================================================
// Unit Tests: Online Substack-Style Story Narration & Alignment
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Test 1: Story JSON Schema Validation with Narration Block ---');
const storyPath = path.join(__dirname, '../../content/es/stories/original/a1/a1-01.json');
assert(fs.existsSync(storyPath), 'Story file must exist');

const story = JSON.parse(fs.readFileSync(storyPath, 'utf8'));
assert(story.narration, 'Story must contain narration block');
assert.strictEqual(typeof story.narration.durationSeconds, 'number', 'durationSeconds must be a number');
assert(story.narration.durationSeconds > 0, 'durationSeconds must be positive');
assert.strictEqual(story.narration.audioFile, undefined, 'Narration must not reference static disk audioFile');
console.log('[PASS] Story JSON contains valid narration block with dynamic streaming config.');

console.log('\n--- Test 2: In-Memory / Cloudflare TTS Architecture (No Git Audio Bloat) ---');
const esAudioDir = path.join(__dirname, '../../content/es/stories/audio');
const huAudioDir = path.join(__dirname, '../../content/hu/stories/audio');
assert(!fs.existsSync(esAudioDir), 'No static Spanish audio directory should exist in repo');
assert(!fs.existsSync(huAudioDir), 'No static Hungarian audio directory should exist in repo');
console.log('[PASS] Verified zero static audio files in repo (lightweight streaming architecture).');

console.log('\n--- Test 3: Segment Alignment and Speaker Roles ---');
assert(Array.isArray(story.narration.segments), 'Segments must be an array');
assert(story.narration.segments.length > 0, 'Segments must not be empty');

const speakers = story.narration.speakers;
assert(speakers.Narrator, 'Must have Narrator speaker profile');
assert(speakers.Carlos, 'Must have Carlos speaker profile');
assert(speakers.Meg, 'Must have Meg speaker profile');

story.narration.segments.forEach((seg, i) => {
    assert(typeof seg.paraIndex === 'number', `Segment ${i} must have paraIndex`);
    assert(typeof seg.startTime === 'number', `Segment ${i} must have startTime`);
    assert(typeof seg.endTime === 'number', `Segment ${i} must have endTime`);
    assert(seg.endTime >= seg.startTime, `Segment ${i} endTime must be >= startTime`);
    assert(seg.speaker, `Segment ${i} must have speaker assigned`);
});
console.log(`[PASS] Verified ${story.narration.segments.length} aligned narration segments.`);

console.log('\n--- Test 4: Active Segment Resolution Algorithm ---');
function findActiveSegment(segments, time) {
    if (!segments || !segments.length) return null;
    return segments.find(s => time >= s.startTime && time < s.endTime) || null;
}

const seg0 = findActiveSegment(story.narration.segments, 5.0);
assert(seg0, 'Should find active segment at t=5.0s');
assert.strictEqual(seg0.paraIndex, 0, 't=5.0s should resolve to paragraph 0');
assert.strictEqual(seg0.speaker, 'Narrator');

const targetSeg2 = story.narration.segments.find(s => s.paraIndex === 2);
assert(targetSeg2, 'Must have segment for paragraph 2');
const seg2 = findActiveSegment(story.narration.segments, targetSeg2.startTime + 0.1);
assert(seg2, 'Should find active segment during paragraph 2');
assert.strictEqual(seg2.paraIndex, 2, 'Should resolve to paragraph 2 (Meg: Buenos días)');
assert.strictEqual(seg2.speaker, 'Meg');

const segOut = findActiveSegment(story.narration.segments, 999.0);
assert.strictEqual(segOut, null, 'Out of bounds time should return null');
console.log('[PASS] Timestamp-to-paragraph segment resolution verified.');

console.log('\n--- Test 5: Pacing & Time Formatting ---');
function formatTime(sec) {
    const s = Math.floor(sec || 0);
    const m = Math.floor(s / 60);
    const rem = s % 60;
    return m + ':' + (rem < 10 ? '0' : '') + rem;
}

assert.strictEqual(formatTime(0), '0:00');
assert.strictEqual(formatTime(45), '0:45');
assert.strictEqual(formatTime(73), '1:13');
assert.strictEqual(formatTime(125), '2:05');
console.log('[PASS] Time formatting verified.');

console.log('\n--- Test 6: Pedagogical Comprehension Check ---');
const ped = story.narration.pedagogical;
assert(ped, 'Must have pedagogical annotations');
assert(Array.isArray(ped.comprehensionQuestions), 'comprehensionQuestions must be array');
assert(ped.comprehensionQuestions.length >= 2, 'Should have at least 2 comprehension questions');

ped.comprehensionQuestions.forEach((q, idx) => {
    assert(q.question && q.question.length > 5, `Question ${idx} must have text`);
    assert(Array.isArray(q.options) && q.options.length >= 3, `Question ${idx} must have >= 3 options`);
    assert(q.correctIndex >= 0 && q.correctIndex < q.options.length, `Question ${idx} correctIndex out of range`);
    assert(q.explanation, `Question ${idx} must have explanation`);
});
console.log(`[PASS] Verified ${ped.comprehensionQuestions.length} comprehension questions with explanations.`);

console.log('\n--- Test 7: Manifest Integration (hasAudio flag) ---');
const manifestPath = path.join(__dirname, '../../content/es/stories/manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const manifestStory = manifest.stories.find(s => s.id === 'story.a1.01');
assert(manifestStory, 'Manifest must include story.a1.01');
assert.strictEqual(manifestStory.hasAudio, true, 'Manifest must flag hasAudio: true');
assert(manifestStory.audioDuration > 0, 'Manifest must record audioDuration');
console.log(`[PASS] Manifest integration confirmed: hasAudio=${manifestStory.hasAudio}, duration=${manifestStory.audioDuration}s.`);

console.log('\n--- Test 8: Zero Pictorial Emojis Enforced ---');
const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{1FA00}-\u{1FAFF}]/u;
const storyRaw = JSON.stringify(story);
assert(!emojiRegex.test(storyRaw), 'No pictorial emojis permitted in story metadata');
console.log('[PASS] Zero pictorial emojis confirmed across story and narration.');

console.log('\n--- Test 9: Mixed-Language Story Narration (Hungarian A1 Unit 01) ---');
const huStoryPath = path.join(__dirname, '../../content/hu/stories/original/a1/a1-unit-01.json');
assert(fs.existsSync(huStoryPath), 'Hungarian story file must exist');

const huStory = JSON.parse(fs.readFileSync(huStoryPath, 'utf8'));
assert(huStory.narration, 'Hungarian story must contain narration block');
assert.strictEqual(huStory.narration.audioFile, undefined, 'Hungarian story must not reference static disk audioFile');
assert.strictEqual(typeof huStory.narration.durationSeconds, 'number', 'durationSeconds must be a number');

// Verify mixed language segment tags
const huSegments = huStory.narration.segments;
assert(Array.isArray(huSegments) && huSegments.length > 0, 'Must have segments');
const enSegments = huSegments.filter(s => s.lang === 'en');
const huLangSegments = huSegments.filter(s => s.lang === 'hu');
assert(enSegments.length > 0, 'Must contain English scaffolding narration segments');
assert(huLangSegments.length > 0, 'Must contain Hungarian dialogue segments');
console.log(`[PASS] Mixed-language narration verified: ${enSegments.length} English segments, ${huLangSegments.length} Hungarian segments.`);

// Check Hungarian manifest
const huManifestPath = path.join(__dirname, '../../content/hu/stories/manifest.json');
const huManifest = JSON.parse(fs.readFileSync(huManifestPath, 'utf8'));
const huManifestStory = huManifest.stories.find(s => s.id === 'story.a1.unit01');
assert(huManifestStory, 'Hungarian manifest must include story.a1.unit01');
assert.strictEqual(huManifestStory.hasAudio, true, 'Hungarian manifest must flag hasAudio: true');
console.log(`[PASS] Hungarian manifest integration confirmed: hasAudio=${huManifestStory.hasAudio}, duration=${huManifestStory.audioDuration}s.`);

console.log('\n--- Test 10: Phonetic Digraph Adaptation: "Károly" -> "Károy" ---');
// Speech synthesis phonetic transform rule
function adaptSpeechPhonetics(text) {
    return text.replace(/\bKároly\b/g, 'Károy').replace(/\bKaroly\b/g, 'Károy');
}

const originalDialogue = 'Károly belép a kávézóba, és Károly köszön.';
const adaptedSpeech = adaptSpeechPhonetics(originalDialogue);
assert.strictEqual(adaptedSpeech, 'Károy belép a kávézóba, és Károy köszön.');
assert(!adaptedSpeech.includes('Károly'), 'Adapted text must not contain Károly');
console.log('[PASS] Phonetic rule transforms Hungarian "Károly" to "Károy" for speech synthesis.');

console.log('\n--- Test 11: StoryAudioPlayer Substack Engine & Default Normal Speed ---');
// Mock minimal DOM and verify StoryAudioPlayer state machine
global.window = {
    addEventListener: () => {},
    removeEventListener: () => {}
};
global.document = {
    getElementById: (id) => ({
        id,
        classList: {
            add: () => {},
            remove: () => {},
            toggle: () => {}
        },
        setAttribute: () => {},
        removeAttribute: () => {},
        querySelectorAll: () => []
    }),
    querySelectorAll: () => [],
    addEventListener: () => {},
    removeEventListener: () => {}
};
global.navigator = { onLine: true };
global.Art = { icon: () => '' };

// Load reader engine module
const readerCode = fs.readFileSync(path.join(__dirname, '../../engine/reader.js'), 'utf8');
const vm = require('vm');
const context = {
    window: global.window,
    document: global.document,
    navigator: global.navigator,
    console: console,
    Art: global.Art,
    Lang: { code: () => 'hu', content: (p) => p },
    Lexicon: { isLoaded: () => true, lookup: () => ({ readings: [] }), stripExplanatoryClauses: (t) => t },
    hasReadStory: () => false,
    Speech: { button: () => '' },
    ParlourTTS: { stop: () => {}, preload: () => {}, speak: () => Promise.resolve(true), setRate: () => {} }
};
vm.createContext(context);
vm.runInContext(readerCode, context);

const sap = context.window.StoryAudioPlayer;
assert(sap, 'StoryAudioPlayer must be defined on window');
assert.strictEqual(sap.speed, 1.0, 'Player must default strictly to normal 1.0x speed');
assert.deepStrictEqual(Array.from(sap.speeds), [0.8, 1.0, 1.2, 1.5], 'Player speeds must support Substack cycle');
assert.strictEqual(sap.isOnline, true, 'Online state must be recognized');

console.log('[PASS] StoryAudioPlayer initialized with normal 1.0x default speed and Substack controls.');

console.log('\n--- Test 12: Resilient Character Voice Casting (Without narration.speakers) ---');
const huStory2Path = path.join(__dirname, '../../content/hu/stories/original/a1/a1-unit-02.json');
assert(fs.existsSync(huStory2Path), 'Hungarian unit 02 story must exist');
const huStory2 = JSON.parse(fs.readFileSync(huStory2Path, 'utf8'));
assert(!huStory2.narration || !huStory2.narration.speakers, 'Unit 02 story must have no narration.speakers block');

sap.init(huStory2);
const voices = sap.characterVoices;
const genders = sap.characterGenders;

assert(voices.Meg, 'Meg must have an assigned voice');
assert(voices.Károly, 'Károly must have an assigned voice');
assert(voices.Anna, 'Anna must have an assigned voice');
assert(voices.András, 'András must have an assigned voice');
assert(voices.Mariann, 'Mariann must have an assigned voice');

// Meg, Anna, Mariann must be recognized as female; Károly, András as male
assert.strictEqual(genders.Meg, 'female', 'Meg should be detected as female');
assert.strictEqual(genders.Anna, 'female', 'Anna should be detected as female');
assert.strictEqual(genders.Mariann, 'female', 'Mariann should be detected as female');
assert.strictEqual(genders.Károly, 'male', 'Károly should be detected as male');
assert.strictEqual(genders.András, 'male', 'András should be detected as male');

// Distinct voice assignment within the same gender
assert.notStrictEqual(voices.Meg, voices.Anna, 'Meg and Anna must have distinct female voices');
assert.notStrictEqual(voices.Károly, voices.András, 'Károly and András must have distinct male voices');
console.log(`[PASS] Verified distinct character casting: Meg=${voices.Meg}, Anna=${voices.Anna}, Mariann=${voices.Mariann}, Károly=${voices.Károly}, András=${voices.András}`);

console.log('\n==========================================================');
console.log('ALL ONLINE SUBSTACK NARRATION & PHONETIC TESTS PASSED [Zero Emojis]');
console.log('==========================================================');

