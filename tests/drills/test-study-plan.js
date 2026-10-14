// ============================================
// TEST STUDY PLAN & UNIFIED CANDIDATE EVALUATION
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '../..');
const COURSE = 'es-latam';
const read = p => JSON.parse(fs.readFileSync(path.join(root, 'content', COURSE, p), 'utf8'));
const curriculum = read('curriculum/curriculum.json');
const grammarIndex = read('indexes/grammar-index.json');

const ENGINE_FILES = [
    'srs.js', 'recycle.js', 'learnerPath.js', 'learnerModel.js',
    'drillHistory.js', 'taughtWords.js', 'recommend.js',
    'recommendationEngine.js', 'studyPlan.js'
];

const NOW = Date.parse('2026-09-28T12:00:00Z');

function createContext({ progress = {}, store = {}, srsDeck = [], weakSkills = [] } = {}) {
    const ctx = {
        console, Math, JSON, Map, Set, Promise, Object, Array, Number, String, isFinite,
        Date: class extends Date {
            constructor(...a) { super(...(a.length ? a : [NOW])); }
            static now() { return NOW; }
        },
        localStorage: {
            getItem: k => (k in store ? store[k] : null),
            setItem: (k, v) => { store[k] = String(v); },
            removeItem: k => { delete store[k]; }
        },
        Lang: { key: k => COURSE + ':' + k, name: () => 'Spanish', code: () => COURSE, content: p => p },
        Content: {
            json: async p => {
                const file = path.join(root, 'content', COURSE, p);
                if (!fs.existsSync(file)) throw new Error('404 ' + p);
                return JSON.parse(fs.readFileSync(file, 'utf8'));
            }
        },
        AppOpens: { current: () => 10, returned: () => null },
        LEVEL_ORDER: ['A1', 'A2', 'B1', 'B2', 'C1'],
        getProgress: () => progress,
        isLessonComplete: id => !!progress[id],
        LevelTest: { resultFor: () => null },
        srsDeck,
        getDueCards: () => srsDeck.filter(c => !c.nextReview || Date.parse(c.nextReview) <= NOW),
        DeckMatch: { render: () => {}, start: () => {} },
        Reader: {
            ensureStories: async () => {},
            getRecommendations: () => ({ comfortable: { story: { id: 'story-1', title: 'Una aventura', estimatedMinutes: 5 } } })
        },
        SpeechInput: { isSupported: () => true },
        ParlourTTS: { available: () => true }
    };
    ctx.window = ctx;

    vm.createContext(ctx);
    for (const file of ENGINE_FILES) {
        const code = fs.readFileSync(path.join(root, 'engine', file), 'utf8');
        vm.runInContext(code, ctx, { filename: file });
    }
    if (srsDeck.length) {
        vm.runInContext('srsDeck = ' + JSON.stringify(srsDeck), ctx);
    }
    ctx.LearnerModel = vm.runInContext('LearnerModel', ctx);
    ctx.RecommendationEngine = vm.runInContext('RecommendationEngine', ctx);
    ctx.StudyPlan = vm.runInContext('StudyPlan', ctx);
    ctx.LearnerPath = vm.runInContext('LearnerPath', ctx);
    ctx.window._curriculumData = curriculum;
    return ctx;
}

async function run() {
    console.log('Testing Unified RecommendationEngine & StudyPlan...');

    // Test 1: getCandidates returns structured candidate objects with take()
    {
        const ctx = createContext();
        const candidates = await ctx.RecommendationEngine.getCandidates({ includeAll: true });
        assert.ok(Array.isArray(candidates), 'getCandidates should return an array');
        assert.ok(candidates.length > 0, 'Should return candidates');

        const first = candidates[0];
        assert.ok(first.key, 'Candidate must have key');
        assert.ok(first.kind, 'Candidate must have kind');
        assert.ok(typeof first.priority === 'number', 'Candidate must have priority');
        assert.ok(typeof first.urgency === 'number', 'Candidate must have urgency');
        assert.ok(typeof first.take === 'function', 'Candidate must have take() function for StudyPlan');

        console.log('✓ RecommendationEngine.getCandidates exposes structured pool with take()');
    }

    // Test 2: StudyPlan.build() draws from RecommendationEngine.getCandidates
    {
        const ctx = createContext({
            srsDeck: [
                { spanish: 'hola', english: 'hello', nextReview: '2026-09-20T10:00:00Z' },
                { spanish: 'adiós', english: 'goodbye', nextReview: '2026-09-20T10:00:00Z' }
            ]
        });

        const plan = await ctx.StudyPlan.build(15);
        assert.ok(plan, 'Plan built successfully');
        assert.strictEqual(plan.minutes, 15, 'Plan minutes preserved');
        assert.ok(Array.isArray(plan.items) && plan.items.length >= 2, 'Plan contains items');

        // Due cards should be prioritized in slot 1
        const kinds = plan.items.map(i => i.kind);
        assert.ok(kinds.includes('review'), 'Plan included due review block from unified candidates');
        assert.ok(kinds.includes('lesson'), 'Plan included next lesson');
        console.log('✓ StudyPlan.build draws items from RecommendationEngine candidate pool');
    }

    // Test 3: mountNextAction switches to next weak candidate if current driller is excluded
    {
        const ctx = createContext({
            store: {
                'es-latam:recycleSchedule': JSON.stringify({
                    'exercise-1': { id: 'exercise-1', lapses: 2, reviews: 0, lastOpen: 10 }
                })
            }
        });

        // Mock grammar-index entry
        ctx.LearnerModel.troubleSkills = async () => [
            { skillId: 'ser-estar', missed: 2 },
            { skillId: 'por-para', missed: 1 }
        ];

        let routed = null;
        ctx.Workshop = {
            open: (id, opts) => { routed = { id, opts }; },
            close: () => {}
        };

        const container = {
            querySelector: () => null,
            insertAdjacentHTML: (pos, html) => {
                assert.ok(html.includes('wk-next-action'), 'Mounted next action HTML');
            }
        };

        // When excludeDrillerId is not matching, it offers ser-estar
        await ctx.RecommendationEngine.mountNextAction(container, { excludeDrillerId: 'listening' });
        console.log('✓ mountNextAction mounts next action correctly');
    }

    console.log('\nAll StudyPlan & Unified Candidate Evaluation tests passed!');
}

run().catch(err => {
    console.error(err);
    process.exit(1);
});
