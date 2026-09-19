// ==========================================================
// Unit Tests: Workshop Drillers Track Isolation (B1 Cultural Tracks)
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

// Browser globals mock for Node.js
global.window = global;
const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { Object.keys(mockStorage).forEach(k => delete mockStorage[k]); }
};
const listeners = {};
global.document = {
    addEventListener: (event, handler) => {
        (listeners[event] || (listeners[event] = [])).push(handler);
    },
    dispatchEvent: (event) => {
        const type = event.type || event;
        (listeners[type] || []).forEach(h => h(event));
    }
};
global.CustomEvent = class CustomEvent {
    constructor(type) { this.type = type; }
};

global.fetch = async (url) => {
    const cleanPath = String(url).replace(/^\.\//, '').replace(/\?.*$/, '');
    const diskPath = path.resolve(cleanPath);
    if (!fs.existsSync(diskPath)) {
        return { ok: false, status: 404, json: async () => ({}) };
    }
    return {
        ok: true,
        status: 200,
        json: async () => JSON.parse(fs.readFileSync(diskPath, 'utf8'))
    };
};

global.Content = {
    json: async (relPath) => {
        const fullPath = path.resolve(relPath);
        return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    }
};

// Load modules
vm.runInThisContext(fs.readFileSync(path.resolve('engine/lang.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/morphology/spanish.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/morphology/hungarian.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/lexicon.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/drills/listening.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/drills/speaking.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/drills/vocabulary.js'), 'utf8'));

(async () => {
    console.log('--- Testing Hungarian Track Isolation ---');
    Lang.set('hu');
    document.dispatchEvent('language-changed');

    // 1. ListeningDriller in HU
    await ListeningDriller._load();
    assert.strictEqual(ListeningDriller._secondTrack('A1'), null, 'HU A1 should have no second track in ListeningDriller');
    assert.strictEqual(ListeningDriller._secondTrack('B1'), 'citizenship', 'HU B1 second track should be "citizenship" in ListeningDriller');
    
    const huCoreListening = ListeningDriller._poolFor('B1', 'core');
    const huCitizenshipListening = ListeningDriller._poolFor('B1', 'citizenship');
    assert(huCoreListening.length > 0, 'HU B1 core listening pool should have items');
    assert(huCitizenshipListening.length > 0, 'HU B1 citizenship listening pool should have items');
    assert(huCoreListening.every(p => (p.track || 'core') === 'core'), 'HU B1 core listening should only have core items');
    assert(huCitizenshipListening.every(p => p.track === 'citizenship'), 'HU B1 citizenship listening should only have citizenship items');
    console.log(`[PASS] HU ListeningDriller: core=${huCoreListening.length}, citizenship=${huCitizenshipListening.length}`);

    // 2. SpeakingStudio in HU
    await SpeakingStudio._load();
    assert.strictEqual(SpeakingStudio._secondTrack('A1'), null, 'HU A1 should have no second track in SpeakingStudio');
    assert.strictEqual(SpeakingStudio._secondTrack('B1'), 'citizenship', 'HU B1 second track should be "citizenship" in SpeakingStudio');

    const huCoreSpeaking = SpeakingStudio._poolFor('B1', 'repeat', 'core');
    const huCitizenshipSpeaking = SpeakingStudio._poolFor('B1', 'repeat', 'citizenship');
    assert(huCoreSpeaking.length > 0, 'HU B1 core speaking pool should have items');
    assert(huCitizenshipSpeaking.length > 0, 'HU B1 citizenship speaking pool should have items');
    assert(huCoreSpeaking.every(p => (p.track || 'core') === 'core'), 'HU B1 core speaking should only have core items');
    assert(huCitizenshipSpeaking.every(p => p.track === 'citizenship'), 'HU B1 citizenship speaking should only have citizenship items');
    console.log(`[PASS] HU SpeakingStudio: core=${huCoreSpeaking.length}, citizenship=${huCitizenshipSpeaking.length}`);

    // 3. VocabularyDriller in HU
    await VocabularyDriller._load();
    assert.strictEqual(VocabularyDriller._secondTrack('A1'), null, 'HU A1 should have no second track in VocabularyDriller');
    assert.strictEqual(VocabularyDriller._secondTrack('B1'), 'citizenship', 'HU B1 second track should be "citizenship" in VocabularyDriller');

    const huCoreWords = VocabularyDriller._wordList('B1', 'core');
    const huCitizenshipWords = VocabularyDriller._wordList('B1', 'citizenship');
    assert(huCoreWords.length > 0, 'HU B1 core vocabulary words should exist');
    assert(huCitizenshipWords.length > 0, 'HU B1 citizenship vocabulary words should exist');
    console.log(`[PASS] HU VocabularyDriller word list: core=${huCoreWords.length}, citizenship=${huCitizenshipWords.length}`);

    // Verify occurrence filtering in HU VocabularyDriller
    // A citizenship word should find citizenship contexts
    const sampleCitWord = huCitizenshipWords[0];
    const citOccurrences = VocabularyDriller._getOccurrences(sampleCitWord, 'citizenship');
    const coreOccurrences = VocabularyDriller._getOccurrences(sampleCitWord, 'core');
    assert(coreOccurrences.every(o => (!o.track || o.track === 'core')), 'Core context queries must never return citizenship sentences');
    console.log(`[PASS] HU VocabularyDriller context isolation verified for "${sampleCitWord.lemma}"`);

    console.log('\n--- Testing Spanish Track Isolation ---');
    Lang.set('es');
    document.dispatchEvent('language-changed');

    // 1. ListeningDriller in ES
    await ListeningDriller._load();
    assert.strictEqual(ListeningDriller._secondTrack('A1'), null, 'ES A1 should have no second track in ListeningDriller');
    assert.strictEqual(ListeningDriller._secondTrack('B1'), 'latam', 'ES B1 second track should be "latam" in ListeningDriller');
    
    const esCoreListening = ListeningDriller._poolFor('B1', 'core');
    const esLatamListening = ListeningDriller._poolFor('B1', 'latam');
    assert(esCoreListening.length > 0, 'ES B1 core listening pool should have items');
    assert(esLatamListening.length > 0, 'ES B1 latam listening pool should have items');
    assert(esCoreListening.every(p => (p.track || 'core') === 'core'), 'ES B1 core listening should only have core items');
    assert(esLatamListening.every(p => p.track === 'latam'), 'ES B1 latam listening should only have latam items');
    console.log(`[PASS] ES ListeningDriller: core=${esCoreListening.length}, latam=${esLatamListening.length}`);

    // 2. SpeakingStudio in ES
    await SpeakingStudio._load();
    assert.strictEqual(SpeakingStudio._secondTrack('A1'), null, 'ES A1 should have no second track in SpeakingStudio');
    assert.strictEqual(SpeakingStudio._secondTrack('B1'), 'latam', 'ES B1 second track should be "latam" in SpeakingStudio');

    const esCoreSpeaking = SpeakingStudio._poolFor('B1', 'repeat', 'core');
    const esLatamSpeaking = SpeakingStudio._poolFor('B1', 'repeat', 'latam');
    assert(esCoreSpeaking.length > 0, 'ES B1 core speaking pool should have items');
    assert(esLatamSpeaking.length > 0, 'ES B1 latam speaking pool should have items');
    assert(esCoreSpeaking.every(p => (p.track || 'core') === 'core'), 'ES B1 core speaking should only have core items');
    assert(esLatamSpeaking.every(p => p.track === 'latam'), 'ES B1 latam speaking should only have latam items');
    console.log(`[PASS] ES SpeakingStudio: core=${esCoreSpeaking.length}, latam=${esLatamSpeaking.length}`);

    // 3. VocabularyDriller in ES
    await VocabularyDriller._load();
    assert.strictEqual(VocabularyDriller._secondTrack('A1'), null, 'ES A1 should have no second track in VocabularyDriller');
    assert.strictEqual(VocabularyDriller._secondTrack('B1'), 'latam', 'ES B1 second track should be "latam" in VocabularyDriller');

    const esCoreWords = VocabularyDriller._wordList('B1', 'core');
    const esLatamWords = VocabularyDriller._wordList('B1', 'latam');
    assert(esCoreWords.length > 0, 'ES B1 core vocabulary words should exist');
    assert(esLatamWords.length > 0, 'ES B1 latam vocabulary words should exist');
    console.log(`[PASS] ES VocabularyDriller word list: core=${esCoreWords.length}, latam=${esLatamWords.length}`);

    console.log('\n[ALL PASS] Track isolation in ListeningDriller, SpeakingStudio, and VocabularyDriller verified!');
})().catch(err => {
    console.error(err);
    process.exit(1);
});
