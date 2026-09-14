// ==========================================================
// Unit Tests: AI-Aware Story Narration & Alignment
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Test 1: Story JSON Schema Validation with Narration Block ---');
const storyPath = path.join(__dirname, '../../content/es/stories/original/a1/a1-01.json');
assert(fs.existsSync(storyPath), 'Story file must exist');

const story = JSON.parse(fs.readFileSync(storyPath, 'utf8'));
assert(story.narration, 'Story must contain narration block');
assert(story.narration.audioFile, 'Narration must define audioFile');
assert.strictEqual(typeof story.narration.durationSeconds, 'number', 'durationSeconds must be a number');
assert(story.narration.durationSeconds > 0, 'durationSeconds must be positive');
console.log('[PASS] Story JSON contains valid narration block with audioFile:', story.narration.audioFile);

console.log('\n--- Test 2: Audio File Asset Verification on Disk ---');
const audioDiskPath = path.join(__dirname, '../../content/es/stories', story.narration.audioFile);
assert(fs.existsSync(audioDiskPath), `Audio file must exist at ${audioDiskPath}`);
const stat = fs.statSync(audioDiskPath);
assert(stat.size > 100000, `Audio file should be non-empty (size: ${stat.size} bytes)`);
console.log(`[PASS] Audio file verified on disk: ${story.narration.audioFile} (${(stat.size / 1024).toFixed(1)} KB)`);

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
// Mock StoryAudioPlayer segment lookup
function findActiveSegment(segments, time) {
    if (!segments || !segments.length) return null;
    return segments.find(s => time >= s.startTime && time < s.endTime) || null;
}

const seg0 = findActiveSegment(story.narration.segments, 5.0);
assert(seg0, 'Should find active segment at t=5.0s');
assert.strictEqual(seg0.paraIndex, 0, 't=5.0s should resolve to paragraph 0');
assert.strictEqual(seg0.speaker, 'Narrator');

const seg2 = findActiveSegment(story.narration.segments, 26.0);
assert(seg2, 'Should find active segment at t=26.0s');
assert.strictEqual(seg2.paraIndex, 2, 't=26.0s should resolve to paragraph 2 (Meg: Buenos días)');
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

console.log('\n==========================================================');
console.log('ALL AI NARRATION & METADATA TESTS PASSED [Zero Emojis Enforced]');
console.log('==========================================================');
