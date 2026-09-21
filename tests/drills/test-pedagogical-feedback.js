// ================================================================
// PEDAGOGICAL FEEDBACK & MISSED ITEMS RECAP TEST SUITE
// ================================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('Testing Pedagogical Feedback across Workshop drills and minigames...\n');

// 1. Verify ListeningRunner pedagogical error feedback
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/drills/listening-runner.js'), 'utf8');
    assert(code.includes('✗ Not quite. The correct answer is:'), 'ListeningRunner must provide explicit correction for choice exercises');
    assert(code.includes('✗ Not quite. You wrote "'), 'ListeningRunner must contrast user response with model in dictation');
    assert(code.includes('✗ Not quite. The missing word was "'), 'ListeningRunner must specify the missing word for fill-in exercises');
    assert(code.includes('_onResult(correct, details)'), 'ListeningRunner must pass detailed error payload to onResult');
    console.log('[PASS] ListeningRunner provides clear correction text and passes error details.');
}

// 2. Verify ListeningDriller missed items recap
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/drills/listening.js'), 'utf8');
    assert(code.includes('_missedDetails = []'), 'ListeningDriller must initialize and reset _missedDetails');
    assert(code.includes('gd-missed-recap'), 'ListeningDriller results must include .gd-missed-recap');
    assert(code.includes('Review Missed Items'), 'ListeningDriller must have Review Missed Items heading');
    assert(code.includes('gd-badge-wrong'), 'ListeningDriller must display badge for user answer');
    assert(code.includes('gd-badge-correct'), 'ListeningDriller must display badge for correct answer');
    console.log('[PASS] ListeningDriller collects missed items and renders review recap.');
}

// 3. Verify TranslationRunner pedagogical error feedback
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/drills/translation-runner.js'), 'utf8');
    assert(code.includes('gd-feedback-wrong'), 'TranslationRunner must show feedback on incorrect/partial translation');
    assert(code.includes('Marked for review \u2014 compare your attempt with the model:'), 'TranslationRunner must provide clear pedagogical instruction');
    assert(code.includes('_resolve(false, { question:'), 'TranslationRunner must forward error details on review');
    console.log('[PASS] TranslationRunner provides pedagogical contrast and forwards error details.');
}

// 4. Verify TranslationDriller missed items recap
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/drills/translation.js'), 'utf8');
    assert(code.includes('_missedDetails = []'), 'TranslationDriller must track missed items');
    assert(code.includes('gd-missed-recap'), 'TranslationDriller results must render .gd-missed-recap');
    assert(code.includes('Review Missed Items'), 'TranslationDriller must have Review Missed Items heading');
    console.log('[PASS] TranslationDriller renders review recap.');
}

// 5. Verify VerbsTable inline correction and feedback
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/verbs/table.js'), 'utf8');
    assert(code.includes('vtable-correction'), 'VerbsTable must render .vtable-correction element');
    assert(code.includes('Correct: \' + correctAnswer'), 'VerbsTable must state "Correct: <form>"');
    assert(code.includes('Review the corrections shown above'), 'VerbsTable feedback must guide user to look at corrections');
    assert(!code.includes("input.classList.add('vtable-wrong');\n                input.value = correctAnswer;"), 'VerbsTable must not overwrite input value when wrong');
    assert(code.includes('nextBtn.disabled = false;'), 'VerbsTable must enable Next Verb after checking so user can advance');
    console.log('[PASS] VerbsTable preserves user attempts, displays inline corrections, and updates feedback.');
}

// 6. Verify VerbsSpeed immediate feedback & results recap
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/verbs/speed.js'), 'utf8');
    assert(code.includes('_missedConjugations'), 'VerbsSpeed must track _missedConjugations');
    assert(code.includes('Correct: \' + _currentAnswer + \' (you wrote: "'), 'VerbsSpeed must contrast correct answer with user attempt');
    assert(code.includes('Review Missed Conjugations'), 'VerbsSpeed results must include Review Missed Conjugations recap');
    assert(code.includes('gd-missed-recap'), 'VerbsSpeed results must use standard .gd-missed-recap styling');
    console.log('[PASS] VerbsSpeed provides contrastive feedback and post-session conjugation recap.');
}

// 7. Verify Hungarian Drillers (hu-verb, hu-suffix, hu-prefix, hu-morphology)
{
    const huFiles = [
        'engine/drills/hu-verb.js',
        'engine/drills/hu-suffix.js',
        'engine/drills/hu-prefix.js',
        'engine/drills/hu-morphology.js'
    ];
    for (const relPath of huFiles) {
        const code = fs.readFileSync(path.join(__dirname, '../../', relPath), 'utf8');
        assert(code.includes('_missedDetails'), `${relPath} must track _missedDetails`);
        assert(code.includes('onResult: (correct, details)'), `${relPath} GrammarRunner hook must capture details`);
        assert(code.includes('gd-missed-recap'), `${relPath} must render .gd-missed-recap`);
        assert(code.includes('Review Missed Items'), `${relPath} must have Review Missed Items recap header`);
    }
    console.log('[PASS] All Hungarian drillers capture missed details and render post-session recaps.');
}

// 8. Verify DeckMatch mismatch notification & missed pairs recap
{
    const code = fs.readFileSync(path.join(__dirname, '../../engine/decks/match.js'), 'utf8');
    assert(code.includes('_missedWords'), 'DeckMatch must track _missedWords');
    assert(code.includes('dkm-feedback'), 'DeckMatch must have .dkm-feedback element');
    assert(code.includes('does not match'), 'DeckMatch must notify when clicked pair does not match');
    assert(code.includes('Review Missed Pairs'), 'DeckMatch results must include Review Missed Pairs recap');
    assert(code.includes('gd-missed-recap'), 'DeckMatch results must use .gd-missed-recap');
    console.log('[PASS] DeckMatch tracks failed attempts, shows mismatch feedback, and provides missed pairs recap.');
}

console.log('\nAll pedagogical feedback checks passed successfully!');
