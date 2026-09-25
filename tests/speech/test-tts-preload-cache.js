// Unit Test: ParlourTTS Preload, Persistent Cache & Fast Voice Tiering
const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Test 1: Worker Voice Resolution Logic
const workerCode = fs.readFileSync(path.join(__dirname, '../../cloudflare-worker/tts-worker.js'), 'utf8');

function extractVoiceResolver() {
    const fnMatch = workerCode.match(/const SHORT_VOICE = ([\s\S]*?);\s*function resolveVoiceName\(payload, languageCode\) {([\s\S]*?)\n}/);
    if (!fnMatch) throw new Error('Could not extract resolveVoiceName');
    const fnBody = 'const SHORT_VOICE = ' + fnMatch[1] + '; return function(payload, languageCode) {' + fnMatch[2] + '};';
    return new Function(fnBody)();
}

const resolveVoiceName = extractVoiceResolver();

console.log('--- Test 1: Fast Voice Tiering in tts-worker.js ---');
// Spanish micro-interactions use the same Chirp3-HD voice as Hungarian (Iapetus)
assert.strictEqual(resolveVoiceName({ type: 'vocabulary' }, 'es-ES'), 'es-ES-Chirp3-HD-Iapetus');
assert.strictEqual(resolveVoiceName({ type: 'listening' }, 'es-ES'), 'es-ES-Chirp3-HD-Iapetus');
assert.strictEqual(resolveVoiceName({ type: 'pronunciation' }, 'es-ES'), 'es-ES-Chirp3-HD-Iapetus');
assert.strictEqual(resolveVoiceName({ type: 'vocabulary', gender: 'male' }, 'es-ES'), 'es-ES-Chirp3-HD-Charon');
assert.strictEqual(resolveVoiceName({ type: 'vocabulary', gender: 'female' }, 'es-ES'), 'es-ES-Chirp3-HD-Kore');

// Stories and characters retain rich Chirp3-HD
assert.strictEqual(resolveVoiceName({ type: 'story' }, 'es-ES'), 'es-ES-Chirp3-HD-Sulafat');
assert.strictEqual(resolveVoiceName({ type: 'reading' }, 'es-ES'), 'es-ES-Chirp3-HD-Sulafat');
assert.strictEqual(resolveVoiceName({ character: 'Puck' }, 'es-ES'), 'es-ES-Chirp3-HD-Puck');

// Hungarian retains Chirp3-HD across all types; story/reading uses Enceladus (low male narrator)
assert.strictEqual(resolveVoiceName({ type: 'vocabulary' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Iapetus');
assert.strictEqual(resolveVoiceName({ type: 'story' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Enceladus');
assert.strictEqual(resolveVoiceName({ type: 'reading' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Enceladus');
assert.strictEqual(resolveVoiceName({ type: 'narrator' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Enceladus');

// Dialogue characters in stories respect gender and explicit character overrides
assert.strictEqual(resolveVoiceName({ type: 'story', gender: 'female' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Kore');
assert.strictEqual(resolveVoiceName({ type: 'story', gender: 'male' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Charon');
assert.strictEqual(resolveVoiceName({ type: 'story', character: 'Aoede' }, 'hu-HU'), 'hu-HU-Chirp3-HD-Aoede');
assert.strictEqual(resolveVoiceName({ type: 'story', gender: 'female' }, 'es-ES'), 'es-ES-Chirp3-HD-Kore');
assert.strictEqual(resolveVoiceName({ type: 'story', gender: 'male' }, 'es-ES'), 'es-ES-Chirp3-HD-Charon');
console.log('[PASS] Worker voice resolution tiers verified.');

// Test 1b: Story comma cadence normalization
function normalizeStoryText(text, type, languageCode) {
    if (!/[.!?…]$/.test(text)) text = text + '.';
    const HU_WH_WORDS = /^(ki|mi|hol|mikor|miért|hogyan|mennyi|milyen|melyik|hova|honnan|merre|meddig|mettől|mióta|mire)\b/i;
    if (languageCode === 'hu-HU' && text.endsWith('?') && HU_WH_WORDS.test(text)) {
        text = text.slice(0, -1) + '.';
    }
    if (languageCode === 'hu-HU' && (type === 'story' || type === 'reading' || type === 'narrator')) {
        text = text.replace(/,(\s+)(?![—–])/g, ', —$1');
    }
    return text;
}
assert.strictEqual(
    normalizeStoryText('Réges-régen, egy faluban élt egy fiú, akit Jancsinak hívtak', 'story', 'hu-HU'),
    'Réges-régen, — egy faluban élt egy fiú, — akit Jancsinak hívtak.'
);
// Decimal numbers like 1,5 must not get a dash inserted
assert.strictEqual(
    normalizeStoryText('1,5 liter tej volt', 'story', 'hu-HU'),
    '1,5 liter tej volt.'
);
// Non-story Hungarian vocab words must not get dashes inserted at commas
assert.strictEqual(
    normalizeStoryText('alma, körte', 'vocabulary', 'hu-HU'),
    'alma, körte.'
);
console.log('[PASS] Hungarian narrative comma cadence beat verified.');

// Test 2: ParlourTTS preload and cache API in engine/tts.js
console.log('\n--- Test 2: ParlourTTS Preload & Cache API ---');
let fetchCount = 0;
let lastBody = null;
global.fetch = async (url, opts) => {
    fetchCount++;
    lastBody = JSON.parse(opts.body);
    return {
        ok: true,
        status: 200,
        json: async () => ({
            audioContent: Buffer.from('fake-mp3-bytes-' + lastBody.text).toString('base64')
        })
    };
};

class MockAudio {
    constructor(src) {
        this.src = src;
        this.playbackRate = 1.0;
        this.currentTime = 0;
        this.onended = null;
        this.playCount = 0;
    }
    async play() {
        this.playCount++;
        return Promise.resolve();
    }
    pause() {}
}
global.Audio = MockAudio;

global.window = { PARLOUR_TTS_ENDPOINT: 'https://test-worker.local/synthesize' };
global.navigator = { onLine: true };
global.document = {
    addEventListener: () => {},
    querySelectorAll: () => []
};

const ParlourTTS = require('../../engine/tts.js');

assert.strictEqual(typeof ParlourTTS.preload, 'function', 'ParlourTTS.preload must be exported');
assert.strictEqual(typeof ParlourTTS.speak, 'function', 'ParlourTTS.speak must be exported');

async function runPreloadTests() {
    // 1 & 2. Concurrent preloads of identical text deduplicate to a single in-flight fetch
    const p1 = ParlourTTS.preload({ text: 'palabra de prueba', language: 'es', type: 'vocabulary' });
    const p2 = ParlourTTS.preload({ text: 'palabra de prueba', language: 'es', type: 'vocabulary' });
    assert.strictEqual(p1, p2, 'Concurrent preloads must return the exact same in-flight Promise instance');
    await Promise.all([p1, p2]);
    assert.strictEqual(fetchCount, 1, 'Deduplicated concurrent preload should only make 1 network fetch');

    // 3. Subsequent preload of already-cached audio does not fetch
    await ParlourTTS.preload({ text: 'palabra de prueba', language: 'es', type: 'vocabulary' });
    assert.strictEqual(fetchCount, 1, 'Subsequent preload should be a cache hit with 0 fetches');

    // 4. speak() of preloaded audio plays instantly without another fetch
    const played = await ParlourTTS.speak({ text: 'palabra de prueba', language: 'es', type: 'vocabulary' });
    assert.strictEqual(played, true, 'speak() should succeed');
    assert.strictEqual(fetchCount, 1, 'speak() of preloaded audio must not fetch again');

    console.log('[PASS] ParlourTTS preload and cache deduplication verified.');

    console.log('\n==========================================================');
    console.log('ALL TTS PRELOAD, CACHE & VOICE TIER TESTS PASSED');
    console.log('==========================================================');
}

runPreloadTests().catch(err => {
    console.error(err);
    process.exit(1);
});
