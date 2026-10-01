// ============================================
// TEST SUITE: END-OF-LESSON DRILLER NOTES (ROADMAP item 5)
// ============================================
// The Verb Driller note and the Listening Driller note, and the signals that
// trigger them:
// 1. Listening log: recorded per course, capped, weak only with enough attempts
// 2. Verb signal: a weak verb-tense skill (Spanish), false when there is no mapping
// 3. Invitations: right text, order before the general Workshop note, stop once
//    the Workshop has been visited, limited shows
// 4. lessons.js feeds the log from the graded steps and passes both signals on
// 5. Zero emoji; the signals are synced with the other per-course data

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log('=== Running Driller Notes Test Suite ===\n');

const mockStore = {};
global.localStorage = {
    getItem: k => (k in mockStore ? mockStore[k] : null),
    setItem: (k, v) => { mockStore[k] = String(v); },
    removeItem: k => { delete mockStore[k]; },
    clear: () => { Object.keys(mockStore).forEach(k => delete mockStore[k]); },
    get length() { return Object.keys(mockStore).length; },
    key: i => Object.keys(mockStore)[i] || null
};
global.window = global;
let course = 'es-latam';
global.Lang = { key: name => course + ':' + name, code: () => course };
let contentFiles = {};
global.Content = { json: async rel => { if (rel in contentFiles) return contentFiles[rel]; throw new Error('missing ' + rel); } };

const root = path.join(__dirname, '../..');
vm.runInThisContext(fs.readFileSync(path.join(root, 'engine/learnerModel.js'), 'utf8'), { filename: 'learnerModel.js' });
const Guide = require('../../engine/guide.js');

(async () => {
    console.log('--- Test 1: Listening log ---');
    assert.deepStrictEqual(LearnerModel.listeningState(), { attempts: 0, accuracy: null, weak: false });
    for (let i = 0; i < 7; i++) LearnerModel.recordListeningOutcome(false);
    assert.strictEqual(LearnerModel.listeningState().weak, false, 'seven misses are too few to judge');
    LearnerModel.recordListeningOutcome(false);
    let s = LearnerModel.listeningState();
    assert.deepStrictEqual([s.attempts, s.accuracy, s.weak], [8, 0, true], 'eight attempts, none right: weak');
    for (let i = 0; i < 12; i++) LearnerModel.recordListeningOutcome(true);
    s = LearnerModel.listeningState();
    assert.strictEqual(s.attempts, 20, 'the log keeps the latest 20');
    assert.deepStrictEqual([s.accuracy, s.weak], [0.6, true], 'exactly 60% right still counts as weak ("60% or less")');
    LearnerModel.recordListeningOutcome(true);
    s = LearnerModel.listeningState();
    assert.strictEqual(s.attempts, 20, 'still capped');
    assert(s.accuracy > 0.6 && !s.weak, 'accuracy above 60% is not weak');
    assert(mockStore['es-latam:listeningLog'], 'stored under the course-scoped key');
    course = 'hu';
    assert.strictEqual(LearnerModel.listeningState().attempts, 0, 'each course has its own log');
    course = 'es-latam';
    mockStore['es-latam:listeningLog'] = 'not json';
    assert.strictEqual(LearnerModel.listeningState().attempts, 0, 'a corrupt log reads as empty');
    console.log('[PASS] Listening log records, caps, scopes by course and judges weak sensibly.');

    console.log('\n--- Test 2: Verb-tense signal ---');
    const tenseIds = new Set(['preterito-indefinido', 'imperfecto']);
    assert.strictEqual(LearnerModel._anyWeakTenseSkill([{ skillId: 'preterito-indefinido', state: 'weak' }], tenseIds), true);
    assert.strictEqual(LearnerModel._anyWeakTenseSkill([{ skillId: 'preterito-indefinido', state: 'developing' }], tenseIds), false, 'developing is not weak');
    assert.strictEqual(LearnerModel._anyWeakTenseSkill([{ skillId: 'ser-estar', state: 'weak' }], tenseIds), false, 'a weak skill that is not a tense does not count');
    assert.strictEqual(LearnerModel._anyWeakTenseSkill([], tenseIds), false);
    assert.strictEqual(LearnerModel._anyWeakTenseSkill(undefined, tenseIds), false);
    contentFiles = {};   // no verb-tense-skills.json (Hungarian): never a verb note
    assert.strictEqual(await LearnerModel.weakVerbTense(), false);
    contentFiles = { 'indexes/verb-tense-skills.json': { _comment: 'x' } };
    assert.strictEqual(await LearnerModel.weakVerbTense(), false, 'a mapping with no skills means no signal');
    for (let i = 0; i < 8; i++) LearnerModel.recordListeningOutcome(false);
    const signals = await LearnerModel.guideSignals();
    assert.deepStrictEqual([signals.weakVerbTense, signals.weakListening], [false, true]);
    console.log('[PASS] Only a weak tense skill counts, and the signal is quietly false without a mapping.');

    console.log('\n--- Test 3: Invitations ---');
    Guide.resetAll();
    const ctx = over => Object.assign({ firstTime: false, newWords: 0, unitCompleted: false, unitsDone: 0, weakVerbTense: false, weakListening: false }, over);
    assert.strictEqual(Guide.invitation(ctx()), null, 'no signal, no note');
    let inv = Guide.invitation(ctx({ weakVerbTense: true, weakListening: true }));
    assert(inv && inv.id === 'invite-verb-driller', 'the verb note leads when both apply');
    assert.strictEqual(inv.text, 'If a verb keeps catching you out, the Verb Driller practises just that.');
    assert.strictEqual(inv.tab, 'drills');
    Guide.acceptInvitation('invite-verb-driller');
    inv = Guide.invitation(ctx({ weakVerbTense: true, weakListening: true }));
    assert(inv && inv.id === 'invite-listening-driller', 'then the listening note');
    assert.strictEqual(inv.text, 'Listening practice has its own space in the Workshop.');
    Guide.acceptInvitation('invite-listening-driller');
    assert.strictEqual(Guide.invitation(ctx({ weakVerbTense: true, weakListening: true })), null, 'accepted notes are not repeated');

    Guide.resetAll();
    assert(Guide.invitation(ctx({ weakListening: true })).id === 'invite-listening-driller', 'listening alone');
    assert(Guide.invitation(ctx({ weakListening: true })).id === 'invite-listening-driller', 'a skipped note comes back once');
    assert.strictEqual(Guide.invitation(ctx({ weakListening: true })), null, 'and then stops');

    Guide.resetAll();
    Guide.markVisited('drills');
    assert.strictEqual(Guide.invitation(ctx({ weakVerbTense: true, weakListening: true })), null, 'a learner who has opened the Workshop is not pointed at it');

    Guide.resetAll();
    Guide.markSeen('invite-library');
    inv = Guide.invitation(ctx({ unitCompleted: true, unitsDone: 2, weakVerbTense: true }));
    assert(inv.id === 'invite-verb-driller', 'a driller note is more specific than the general Workshop one');
    Guide.resetAll();
    Guide.markSeen('invite-library');
    inv = Guide.invitation(ctx({ unitCompleted: true, unitsDone: 2 }));
    assert(inv.id === 'invite-workshop', 'with no weak signal the general Workshop note still appears at a unit end');
    console.log('[PASS] Notes appear in the right order, once each, and never after the Workshop is found.');

    console.log('\n--- Test 4: lessons.js is wired in ---');
    const lessons = fs.readFileSync(path.join(root, 'engine/lessons.js'), 'utf8');
    assert(/function noteListeningOutcome\(/.test(lessons), 'noteListeningOutcome exists');
    const solve = lessons.slice(lessons.indexOf('function solveStep('), lessons.indexOf('function failStep('));
    const fail = lessons.slice(lessons.indexOf('function failStep('), lessons.indexOf('function queueForRemediationIfMissed('));
    assert(solve.includes('noteListeningOutcome(!stepState.wasMissed && !stepState.usedHint)'), 'a solved step records a clean first try only without a miss or hint');
    assert(fail.includes('noteListeningOutcome(false)'), 'a step given up on records a miss');
    const fn = lessons.slice(lessons.indexOf('function noteListeningOutcome('), lessons.indexOf('function noteRecycleResult('));
    assert(fn.includes("'listening'") && fn.includes("'listening-choice'") && fn.includes("'dictation'"), 'only listening steps are recorded');
    assert(lessons.includes('await LearnerModel.guideSignals()'), 'the summary asks for the signals');
    assert(lessons.includes('guideInvitation(lesson, firstTime, guideSignals)'), 'and passes them on');
    assert(/weakVerbTense: !!\(signals && signals\.weakVerbTense\)/.test(lessons) && /weakListening: !!\(signals && signals\.weakListening\)/.test(lessons), 'into the invitation context');
    console.log('[PASS] Graded steps feed the log and the summary passes both signals to the guide.');

    console.log('\n--- Test 5: Emoji and sync ---');
    const emoji = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
    assert(!emoji.test(fs.readFileSync(path.join(root, 'engine/guide.js'), 'utf8')), 'no emoji in guide.js');
    assert(/'listeningLog'/.test(fs.readFileSync(path.join(root, 'engine/sync.js'), 'utf8')), 'the listening log is synced with the other per-course data');
    console.log('[PASS] No emoji; listening log synced.');

    console.log('\n=== ALL DRILLER NOTES TESTS PASSED ===');
})().catch(err => { console.error('FAILED:', err); process.exit(1); });
