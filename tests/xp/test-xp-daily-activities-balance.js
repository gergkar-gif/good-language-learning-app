/**
 * Test suite for XP System & Daily Activities balance:
 * 1. Dynamic review goal: 20 or everything due, whichever is smaller.
 *    0 due = satisfied ("nothing due"), 6 due = 6 needed.
 * 2. Lesson story integration: stories inside lessons count towards daily Read.
 * 3. Library re-read recommendations when all level stories are completed.
 */

const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Mock localStorage
const storage = {};
global.localStorage = {
    getItem: (k) => (k in storage ? storage[k] : null),
    setItem: (k, v) => { storage[k] = String(v); },
    removeItem: (k) => { delete storage[k]; },
    clear: () => { Object.keys(storage).forEach(k => delete storage[k]); }
};

// Mock Lang
global.Lang = {
    code: () => 'es-es',
    name: () => 'Spanish',
    key: (k) => 'parlour_es_' + k,
    content: (p) => 'content/es-es/' + p
};

// Mock window and document
global.window = global;
global.document = {
    createElement: () => ({
        classList: { add: () => {}, remove: () => {} },
        setAttribute: () => {},
        innerHTML: '',
        remove: () => {}
    }),
    getElementById: () => null,
    addEventListener: () => {},
    removeEventListener: () => {}
};

// Load modules
const XpModule = require('../../engine/xp.js');
const Reader = require('../../engine/reader.js');
global.Reader = Reader;
global.markStoryRead = Reader.markStoryRead;
global.getReadStoryIds = Reader.getReadStoryIds;
const Lessons = require('../../engine/lessons.js');

async function main() {
    console.log('\n--- Test 1: Dynamic Review Goal Scaling ---');

    // Case 1A: Empty deck / 0 cards due
    global.srsDeck = [];
    global.localStorage.clear();
    XpModule.loadXP();

    let acts = XpModule.getDailyActivities();
    let reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.goal, 0, 'Goal should be 0 when no cards are due');
    assert.strictEqual(reviewAct.done, true, 'Review should be done when nothing is due');
    assert.strictEqual(reviewAct.nothingDue, true, 'nothingDue flag should be true');

    // If user now finishes 1 lesson, streak should be preserved (2 of 3 completed: Review + Learn)
    XpModule.recordLessonCompleted(true);
    acts = XpModule.getDailyActivities();
    assert.strictEqual(acts.completed, 2, 'Should have 2 activities completed (Review + Learn)');
    assert.strictEqual(acts.keepsStreak, true, '1 lesson with 0 cards due must keep streak');

    // Case 1B: 6 cards due, none reviewed yet
    global.localStorage.clear();
    XpModule.loadXP();
    global.srsDeck = [
        { spanish: 'a', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'b', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'c', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'd', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'e', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'f', nextReview: new Date(Date.now() - 10000).toISOString() },
        { spanish: 'future', nextReview: new Date(Date.now() + 100000).toISOString() }
    ];

    acts = XpModule.getDailyActivities();
    reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.goal, 6, 'Review goal should be 6 when 6 cards are due');
    assert.strictEqual(reviewAct.done, false, 'Review should not be done yet');
    assert.strictEqual(reviewAct.count, 0, 'Review count should be 0');

    // Review 4 cards
    for (let i = 0; i < 4; i++) {
        global.srsDeck.shift(); // 1 less due
        XpModule.recordReview({ spanish: 'word' + i, reviews: 1 }, 'good');
    }
    acts = XpModule.getDailyActivities();
    reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.count, 4, 'Count should be 4');
    assert.strictEqual(reviewAct.goal, 6, 'Goal remains 6 (4 done + 2 remaining due)');
    assert.strictEqual(reviewAct.done, false, 'Review should not be done yet');

    // Review remaining 2 cards
    for (let i = 0; i < 2; i++) {
        global.srsDeck.shift();
        XpModule.recordReview({ spanish: 'word_rem_' + i, reviews: 1 }, 'good');
    }
    acts = XpModule.getDailyActivities();
    reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.count, 6, 'Count should be 6');
    assert.strictEqual(reviewAct.done, true, 'Review should now be done');

    // Lock-in test: if another card comes due later in the day, review remains done
    global.srsDeck.push({ spanish: 'late_card', nextReview: new Date(Date.now() - 1000).toISOString() });
    acts = XpModule.getDailyActivities();
    reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.done, true, 'Review goal once met today must stay met even if new card comes due');

    // Case 1C: Over 20 cards due caps at 20
    global.localStorage.clear();
    XpModule.loadXP();
    global.srsDeck = Array.from({ length: 35 }, (_, idx) => ({
        spanish: 'word_' + idx,
        nextReview: new Date(Date.now() - 10000).toISOString()
    }));
    acts = XpModule.getDailyActivities();
    reviewAct = acts.list.find(a => a.key === 'review');
    assert.strictEqual(reviewAct.goal, 20, 'Review goal should cap at 20 when > 20 are due');

    console.log('[PASS] Dynamic review goal correctly handles 0-due, partial-due, cap-at-20, and goal lock-in.');

    console.log('\n--- Test 2: Lesson Story Reading Credit ---');
    // Mock globals for finishLesson
    global.recordLessonCompleted = XpModule.recordLessonCompleted;
    global.recordStoryCompleted = XpModule.recordStoryCompleted;
    global.getRank = XpModule.getRank;
    global.renderLessonSummary = async () => {};

    // Reset read storage for lesson test
    global.localStorage.clear();
    XpModule.loadXP();

    // Set up currentLesson with a story step
    Lessons.setCurrentLesson({
        id: 'lesson.a1.01.01',
        steps: [
            { type: 'vocabulary', words: [] },
            { type: 'story', storyId: 'story-a1-carlos', title: 'Carlos conoce a Meg' },
            { type: 'multiple-choice', question: 'Q?' }
        ]
    });

    // Call finishLesson
    await Lessons.finishLesson();

    const todayActs = XpModule.getDailyActivities();
    const readAct = todayActs.list.find(a => a.key === 'reading');
    const learnAct = todayActs.list.find(a => a.key === 'learn');

    assert.strictEqual(learnAct.done, true, 'Lesson completion must be credited');
    assert.strictEqual(readAct.done, true, 'Story step inside lesson must credit Read activity');
    assert.strictEqual(readAct.count, 1, 'Read count should be 1');
    assert.strictEqual(todayActs.completed >= 2, true, 'Streak criteria satisfied by lesson with story');
    assert(Reader.getReadStoryIds().includes('story-a1-carlos'), 'Story id must be in readStoryIds');

    console.log('[PASS] Story inside lesson correctly credits Read activity and updates streak.');

    console.log('\n--- Test 3: Library Re-Read Recommendations when level is complete ---');

    const esManifestPath = path.resolve(__dirname, '../../content/es-es/stories/manifest.json');
    const manifestData = JSON.parse(fs.readFileSync(esManifestPath, 'utf8'));
    Reader.stories = manifestData.stories;

    global.LearnerPath = {
        currentLevel: () => 'A1'
    };

    // Find all browsable A1 stories
    const browsableA1 = Reader.stories.filter(s => Reader._isBrowsableStory(s) && (s.level || '').toUpperCase() === 'A1');
    assert(browsableA1.length > 0, 'Must have browsable A1 stories');

    // When not all A1 stories are read:
    global.localStorage.clear();
    assert.strictEqual(Reader.allStoriesReadInCurrentLevel(), false, 'Should be false when no stories are read');

    // Mark ALL browsable A1 stories as read
    const a1Ids = browsableA1.map(s => s.id);
    global.localStorage.setItem('parlour_es_readStories', JSON.stringify(a1Ids));

    assert.strictEqual(Reader.allStoriesReadInCurrentLevel(), true, 'Should be true when all A1 stories are read');

    // Check recommendations
    const recs = Reader.getRecommendations();
    assert(recs && recs.comfortable, 'Comfortable recommendation required');
    assert.strictEqual((recs.comfortable.story.level || '').toUpperCase(), 'A1', 'Comfortable pick must stay in A1 for re-reading, not jump to A2');
    assert.strictEqual(recs.comfortable.isReRead, true, 'isReRead flag must be true');
    assert(/re-reads count/i.test(recs.comfortable.reason), 'Reason must explain that re-reads count toward streak');

    // Check recommendations HTML
    const recsHtml = Reader.buildRecommendationsHtml();
    assert(recsHtml.includes('Re-read · Fluency'), 'HTML must display Re-read · Fluency badge');
    assert(recsHtml.includes('Re-read story →'), 'HTML button must say Re-read story →');

    console.log('[PASS] Library recommendations smoothly point to re-reading at current level without premature level jump.');

    console.log('\n==========================================================');
    console.log('ALL XP & READING BALANCE TESTS PASSED!');
    console.log('==========================================================\n');
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
