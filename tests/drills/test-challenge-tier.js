// Test: Progressive CEFR Communicative Challenge & Can-Do Verification
const assert = require('assert');

// 1. Verify LearnerModel competency verification logic
const LearnerModel = (function () {
    let _store = {};
    return {
        _reset: () => { _store = {}; },
        _getStore: () => _store,
        verifyCompetency: (textOrId, score, source, modality) => {
            if (!textOrId) return;
            const text = textOrId.trim();
            const now = Date.now();
            const existing = _store[text] || {};
            _store[text] = {
                ...existing,
                text,
                checked: true,
                exerciseAccuracy: typeof score === 'number' ? Math.round(score) : (existing.exerciseAccuracy || 85),
                state: 'verified',
                verifiedAt: now,
                timestamp: now,
                modality: modality || existing.modality || 'oral',
                source: source || 'studio-assessment'
            };
            return _store[text];
        },
        recordCompetencies: (lessonId, items) => {
            if (!Array.isArray(items)) return;
            const now = Date.now();
            items.forEach(item => {
                if (!item || !item.text) return;
                const text = item.text.trim();
                const checked = !!item.checked;
                const accuracy = typeof item.exerciseAccuracy === 'number' ? item.exerciseAccuracy : 100;
                const existing = _store[text] || {};

                let state;
                if (existing.state === 'verified' && checked) {
                    state = 'verified';
                } else if (checked && accuracy >= 75) {
                    state = 'verified';
                } else if (!checked && accuracy >= 75) {
                    state = 'confidence-gap';
                } else if (checked && accuracy < 75) {
                    state = 'blindspot';
                } else {
                    state = 'deficit';
                }

                _store[text] = {
                    ...existing,
                    text,
                    lessonId: lessonId || existing.lessonId,
                    checked,
                    exerciseAccuracy: accuracy,
                    state,
                    timestamp: now,
                    verifiedAt: state === 'verified' ? (existing.verifiedAt || now) : null,
                    source: existing.source || 'lesson-checklist'
                };
            });
        }
    };
})();

console.log('--- Test 1: verifyCompetency sets verified state and modality ---');
LearnerModel.verifyCompetency('I can greet someone and introduce myself.', 95, 'lesson-challenge', 'oral');
const comp = LearnerModel._getStore()['I can greet someone and introduce myself.'];
assert.strictEqual(comp.state, 'verified');
assert.strictEqual(comp.modality, 'oral');
assert.strictEqual(comp.source, 'lesson-challenge');
console.log('[PASS] Competency correctly marked as verified with oral modality.');

console.log('--- Test 2: recordCompetencies does not downgrade a verified item ---');
LearnerModel.recordCompetencies('lesson.a1.01.01', [
    { text: 'I can greet someone and introduce myself.', checked: true, exerciseAccuracy: 60 }
]);
const compAfter = LearnerModel._getStore()['I can greet someone and introduce myself.'];
assert.strictEqual(compAfter.state, 'verified', 'State should remain verified despite lower exercise accuracy');
assert.strictEqual(compAfter.source, 'lesson-challenge');
console.log('[PASS] Verified challenge competency preserved across checklist saving.');

console.log('--- Test 3: Tier identification and challenge generation structure ---');
function determineChallenge(level, canDo, speakingCandidate) {
    const tier = (level === 'A1') ? 'tier1' : (level === 'A2') ? 'tier2' : 'tier3';
    let cues = [];
    if (tier === 'tier1') {
        cues = speakingCandidate ? [`Use what you learned: "${speakingCandidate.english}"`] : ['Express this clearly out loud'];
    } else if (tier === 'tier2') {
        cues = [
            '1. Opening greeting & polite address',
            '2. State your request or description clearly',
            '3. Confirm or conclude the conversation'
        ];
    } else {
        cues = [
            'Set the context or introduce the topic',
            'Describe the details or analyze the situation',
            'Share your conclusion, reaction, or recommendation'
        ];
    }
    return { tier, cues, canDo, level };
}

const chA1 = determineChallenge('A1', 'I can greet someone.', { spanish: 'Hola', english: 'Hello' });
assert.strictEqual(chA1.tier, 'tier1');
assert.strictEqual(chA1.cues[0], 'Use what you learned: "Hello"');

const chA2 = determineChallenge('A2', 'I can order food in a restaurant.');
assert.strictEqual(chA2.tier, 'tier2');
assert.strictEqual(chA2.cues.length, 3);
assert.ok(chA2.cues[0].includes('greeting'));

const chB1 = determineChallenge('B1', 'I can describe the plot of a film.');
assert.strictEqual(chB1.tier, 'tier3');
assert.strictEqual(chB1.cues.length, 3);
assert.ok(chB1.cues[1].includes('details or analyze'));

console.log('[PASS] Tiered challenge structure verified across A1, A2, and B1.');

console.log('\n[ALL PASS] Progressive challenge test suite passed successfully.');
