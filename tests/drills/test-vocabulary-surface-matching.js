// ==========================================================
// Unit Tests: Vocabulary Driller Surface-Form & Lemma Matching
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}: ${str}`);
}

// Setup browser globals for Node.js
global.window = global;
const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { Object.keys(mockStorage).forEach(k => delete mockStorage[k]); }
};
global.document = {
    addEventListener: () => {},
    dispatchEvent: () => {}
};
global.CustomEvent = class CustomEvent {};

// File-backed fetch for Node
global.fetch = async (url) => {
    const cleanPath = url.replace(/^\.\//, '').replace(/\?.*$/, '');
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

// Load dependencies
vm.runInThisContext(fs.readFileSync(path.resolve('engine/lang.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/morphology/spanish.js'), 'utf8'));
vm.runInThisContext(fs.readFileSync(path.resolve('engine/lexicon.js'), 'utf8'));

// Load vocabulary driller in vm to ensure closure state loads
vm.runInThisContext(fs.readFileSync(path.resolve('engine/drills/vocabulary.js'), 'utf8'));

(async () => {
    console.log('--- Test 1: Loading Spanish Lexicon and Curriculum ---');
    Lang.set('es-latam');
    await Lexicon.load();

    const driller = VocabularyDriller;
    assert(driller, 'VocabularyDriller must be exported');
    assert(typeof driller._getOccurrences === 'function', '_getOccurrences must be exported for testing');

    // Trigger data loading headless
    await driller._load();

    console.log('[PASS] Modules and dictionary data loaded cleanly.');

    console.log('\n--- Test 2: Surface Verb Form Resolution ("soy", "eres", "quiero") ---');
    const surfaceVerbs = [
        { lemma: 'soy', en: 'I am', pos: 'verb' },
        { lemma: 'eres', en: 'you are', pos: 'verb' },
        { lemma: 'quiero', en: 'I want', pos: 'verb' }
    ];

    surfaceVerbs.forEach(v => {
        const occurrences = driller._getOccurrences(v);
        assert(occurrences.length > 0, `Occurrences should be found for surface verb "${v.lemma}"`);
        const exercise = driller._buildExerciseFor(v);
        assert(exercise, `Exercise should be generated for surface verb "${v.lemma}"`);
        assertZeroEmojis(JSON.stringify(exercise), `exercise for ${v.lemma}`);
        assert(exercise.kind, `Exercise for ${v.lemma} must have a kind`);
        console.log(`[PASS] Surface verb "${v.lemma}" (${occurrences.length} occurrences): [${exercise.kind}] ${exercise.question || exercise.sentence}`);
    });

    console.log('\n--- Test 3: Slash-Separated Adjective Resolution ("alto / alta", "bajo / baja") ---');
    const slashAdjectives = [
        { lemma: 'alto / alta', en: 'tall', pos: 'adjective' },
        { lemma: 'bajo / baja', en: 'short', pos: 'adjective' },
        { lemma: 'simpático / simpática', en: 'friendly / nice', pos: 'adjective' }
    ];

    slashAdjectives.forEach(adj => {
        const occurrences = driller._getOccurrences(adj);
        assert(occurrences.length > 0, `Occurrences should be found for slash adjective "${adj.lemma}"`);
        const exercise = driller._buildExerciseFor(adj);
        assert(exercise, `Exercise should be generated for slash adjective "${adj.lemma}"`);
        assertZeroEmojis(JSON.stringify(exercise), `exercise for ${adj.lemma}`);
        if (exercise.options && exercise.question && exercise.question.includes('_____')) {
            exercise.options.forEach(opt => {
                assert(!opt.includes('/'), `Spanish word decoy options should not contain raw slashes: "${opt}"`);
            });
        }
        console.log(`[PASS] Slash adjective "${adj.lemma}" (${occurrences.length} occurrences): [${exercise.kind}] ${exercise.question || exercise.sentence}`);
    });

    console.log('\n--- Test 4: Article-Prefixed Nouns Resolution ("el perro", "la casa") ---');
    const articleNouns = [
        { lemma: 'el perro', en: 'the dog', pos: 'noun' },
        { lemma: 'la casa', en: 'the house', pos: 'noun' },
        { lemma: 'la manzana', en: 'the apple', pos: 'noun' }
    ];

    articleNouns.forEach(noun => {
        const occurrences = driller._getOccurrences(noun);
        assert(occurrences.length > 0, `Occurrences should be found for article noun "${noun.lemma}"`);
        const exercise = driller._buildExerciseFor(noun);
        assert(exercise, `Exercise should be generated for article noun "${noun.lemma}"`);
        assertZeroEmojis(JSON.stringify(exercise), `exercise for ${noun.lemma}`);
        console.log(`[PASS] Article noun "${noun.lemma}" (${occurrences.length} occurrences): [${exercise.kind}] ${exercise.question || exercise.sentence}`);
    });

    console.log('\n--- Test 5: Fallback Resilience on Non-Corpus Entries ---');
    const nonCorpusWord = { lemma: 'supercalifragilístico', en: 'supercalifragilistic', pos: 'adjective' };
    const fallbackEx = driller._buildExerciseFor(nonCorpusWord);
    assert(fallbackEx, 'Non-corpus word should gracefully fall back to definition/recall');
    assert(['multiple-choice', 'fill-blank'].includes(fallbackEx.kind), 'Fallback must produce valid exercise');
    console.log(`[PASS] Non-corpus word handled gracefully without abort: [${fallbackEx.kind}]`);

    console.log('\n==========================================================');
    console.log('ALL VOCABULARY DRILLER SURFACE MATCHING TESTS PASSED [Zero Emojis Enforced]');
    console.log('==========================================================');
})();
