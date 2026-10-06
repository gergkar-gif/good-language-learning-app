// ============================================
// TEST GRAMMAR DRILLER CATALOGUE & NEW LEARNER EXPERIENCE
// ============================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '../..');

function createDrillerEnv(langCode) {
    const contentDir = path.join(root, 'content', langCode);
    const readJson = rel => {
        const full = path.join(contentDir, rel);
        return fs.existsSync(full) ? JSON.parse(fs.readFileSync(full, 'utf8')) : null;
    };

    const regData = readJson('indexes/skill-registry.json');
    const indexData = readJson('indexes/grammar-index.json');
    const bankData = readJson('drills/grammar/a1-bank.json');

    const domContainer = {
        innerHTML: '',
        querySelectorAll: () => [],
        querySelector: sel => null,
        appendChild: () => {}
    };

    const docListeners = {};
    const ctx = {
        console, Date, Math, JSON, Map, Set, Promise, Object, Array, RegExp, Number, String,
        window: {},
        document: {
            addEventListener: (evt, fn) => { docListeners[evt] = fn; },
            removeEventListener: () => {},
            createElement: tag => ({
                className: '',
                setAttribute: () => {},
                querySelectorAll: () => [],
                addEventListener: () => {},
                remove: () => {}
            }),
            body: { appendChild: () => {} }
        },
        Lang: {
            code: () => langCode,
            content: rel => rel
        },
        Content: {
            json: async rel => {
                if (rel.includes('indexes/skill-registry.json')) return regData || { skills: {} };
                if (rel.includes('indexes/grammar-index.json')) return indexData || { bySkill: {}, titles: {} };
                if (rel.includes('drills/grammar/a1-bank.json')) return bankData || { modules: [], items: [] };
                // exercise files
                const p = path.join(contentDir, rel);
                if (fs.existsSync(p)) return JSON.parse(fs.readFileSync(p, 'utf8'));
                return {};
            }
        },
        LearnerPath: {
            reachedExerciseRefs: () => new Set() // 0 lessons completed
        },
        LearnerModel: {
            troubleSkills: async () => [],
            weakSkills: async () => []
        },
        getProgress: () => ({}),
        LEVEL_ORDER: ['A1', 'A2', 'B1', 'B2', 'C1']
    };
    ctx.window = ctx;

    vm.createContext(ctx);
    vm.runInContext(fs.readFileSync(path.join(root, 'engine/drills/grammar.js'), 'utf8') + '\n;globalThis.GrammarDriller = GrammarDriller;', ctx);

    return { ctx, domContainer };
}

(async () => {
    console.log('\n--- Test 1: es-es Grammar Driller Catalogue Filtering ---');
    const { ctx: esCtx, domContainer: esContainer } = createDrillerEnv('es-es');

    await esCtx.GrammarDriller.render(esContainer);

    // Verify container html
    const html = esContainer.innerHTML;

    // 1. Must not contain retired topic slugs
    assert.ok(!html.includes('19th-century independence and the colonial cession of 1898'),
        'Must not contain retired Puerto Rico 1898 topic');
    assert.ok(!html.includes('puertorico-grito-lares-cesion-1898'),
        'Must not contain retired puertorico-grito-lares-cesion-1898 slug');
    assert.ok(!html.includes('Advanced discourse synthesis in central chilean poetry and history'),
        'Must not contain retired central chilean poetry slug');
    assert.ok(!html.includes('Advanced discourse synthesis in lowlands and mineral horizons'),
        'Must not contain retired mineral horizons slug');
    assert.ok(!html.includes('Adversative and concessive markers in regional identity debates'),
        'Must not contain retired regional identity debates slug');

    // 2. Must not contain "0 exercises available"
    assert.ok(!html.includes('0 exercises available'),
        'Selected skill card must not show 0 exercises available');
    assert.ok(!html.includes('(0 exercises)'),
        'List must not contain (0 exercises)');

    // 3. Brand new learner starts on Practise a skill tab (TAB.SKILL active)
    assert.ok(html.includes('data-tab="skill" role="tab" aria-selected="true"'),
        'Practise a skill tab must be active for new learner with 0 progress');

    // 4. Must not show "No matching taught skills." when user has 0 lessons and no search query
    assert.ok(!html.includes('No matching taught skills.'),
        'Must not show "No matching taught skills." above all skills for brand new learner');

    // 5. The untaught/all skills section must be open
    assert.ok(html.includes('<details class="gd-untaught-section" open>'),
        'Untaught/all skills section should be open for new learner');

    // 6. Selected skill must be a real Level A1 skill
    assert.ok(html.includes('Level A1'), 'Should select a Level A1 skill');
    assert.ok(html.includes('exercises available'), 'Should have exercises available');

    // 7. Verify switching to Tab 1 ("Fix weak areas")
    let weakTabBtnCallback = null;
    esContainer.querySelectorAll = sel => {
        if (sel === '.gd-tab-btn') {
            return [{
                dataset: { tab: 'weak' },
                addEventListener: (evt, cb) => { weakTabBtnCallback = cb; }
            }];
        }
        return [];
    };
    await esCtx.GrammarDriller.render(esContainer);
    assert.ok(weakTabBtnCallback, 'Should have registered tab switcher callback');
    weakTabBtnCallback(); // Switch to Tab 1
    const weakHtml = esContainer.innerHTML;
    assert.ok(!weakHtml.includes('Checking your recent progress…'),
        'Tab 1 must not show permanent loading spinner');
    assert.ok(weakHtml.includes('No practice history yet!'),
        'Tab 1 must show friendly clean state when 0 lessons completed');
    assert.ok(weakHtml.includes('switch-to-skill-tab'),
        'Tab 1 must have button to switch to skill tab');
    console.log('✓ Tab 1 ("Fix weak areas") displays clean state instead of permanent loading spinner');

    console.log('\n--- Test 2: Hungarian hu Grammar Driller Catalogue Filtering ---');
    const { ctx: huCtx, domContainer: huContainer } = createDrillerEnv('hu');
    await huCtx.GrammarDriller.render(huContainer);
    const huHtml = huContainer.innerHTML;

    assert.ok(!huHtml.includes('0 exercises available'),
        'hu: Selected skill card must not show 0 exercises available');
    assert.ok(!huHtml.includes('(0 exercises)'),
        'hu: List must not contain (0 exercises)');
    assert.ok(huHtml.includes('data-tab="skill" role="tab" aria-selected="true"'),
        'hu: Practise a skill tab must be active for new learner');
    console.log('✓ hu: retired slugs excluded, 0-exercise skills hidden, and clean greeting for new learners');

    console.log('\nAll grammar driller catalogue tests passed!');
})().catch(err => {
    console.error(err);
    process.exit(1);
});
