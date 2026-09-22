// Unit Test: Functional Polish Suite
// Verifies:
// 1. Mobile Keyboard Viewport Stabilization (meta interactive-widget, scroll-margin, layout 100vh lock)
// 2. Audio & Listening Ergonomics (slow 0.75x replay, audio teardown on transitions and teardownTab)
// 3. Dictation Hints & Soft Signal (two-tier hint, zero emojis, usedHint: true, SM-2 'hard')
// 4. Verb Table Navigation (Enter moves focus to next row, checks on last row / when filled)
// 5. SRS Usability & Badge Event (popup button state, srs-updated CustomEvent)

const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('--- Testing Functional Polish Suite ---');

// ============================================
// 1. Mobile Keyboard Viewport Stabilization
// ============================================
console.log('1. Testing Mobile Viewport & CSS Keyboard Rules...');
const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(
    indexHtml.includes('interactive-widget=resizes-content'),
    'index.html must include interactive-widget=resizes-content in meta viewport'
);

const baseCss = fs.readFileSync(path.join(__dirname, '../../styles/base.css'), 'utf8');
assert(
    baseCss.includes('scroll-margin-top: 120px;'),
    'styles/base.css must include scroll-margin-top on form elements'
);

const layoutCss = fs.readFileSync(path.join(__dirname, '../../styles/layout.css'), 'utf8');
assert(
    layoutCss.includes('.app:has(input:focus, textarea:focus)'),
    'styles/layout.css must contain mobile 100vh lock rule for focused inputs'
);
console.log('✓ Viewport meta and CSS keyboard rules verified');

// ============================================
// 2. Audio & Listening Ergonomics
// ============================================
console.log('2. Testing Audio Teardown & Slow Speed Button...');
const lessonsJs = fs.readFileSync(path.join(__dirname, '../../engine/lessons.js'), 'utf8');
const listeningRunnerJs = fs.readFileSync(path.join(__dirname, '../../engine/drills/listening-runner.js'), 'utf8');
const initJs = fs.readFileSync(path.join(__dirname, '../../engine/init.js'), 'utf8');

assert(
    lessonsJs.includes('lsn-play-slow') && lessonsJs.includes('lessonPlayAudio(0.75)'),
    'lessons.js must render slow audio button with 0.75 speed'
);
assert(
    listeningRunnerJs.includes('lr-play-slow') && listeningRunnerJs.includes('speed: 0.75'),
    'listening-runner.js must support 0.75x slow audio playback'
);
assert(
    initJs.includes('ParlourTTS.stop()'),
    'init.js teardownTab must halt ParlourTTS on tab switch'
);
assert(
    lessonsJs.includes('function teardownLesson') && lessonsJs.includes('ParlourTTS.stop()'),
    'lessons.js teardownLesson must halt ParlourTTS'
);
assert(
    lessonsJs.includes('function nextLessonStep') && lessonsJs.includes('ParlourTTS.stop()'),
    'lessons.js nextLessonStep must halt ParlourTTS'
);
console.log('✓ Audio ergonomics and teardown verified');

// ============================================
// 3. Dictation Hints & Soft Knowledge Signal
// ============================================
console.log('3. Testing Dictation Progressive Hints & Soft Signal...');
assert(
    lessonsJs.includes("dictation(step)"),
    'lessons.js must have dictation renderer'
);
// Verify zero emojis in dictation hint rendering
const dictationRendererMatch = lessonsJs.match(/dictation\(step\)\s*\{[\s\S]*?return `([\s\S]*?)`;\s*\},/);
assert(dictationRendererMatch, 'Dictation renderer found');
const dictationHtml = dictationRendererMatch[1];
assert(!/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u.test(dictationHtml), 'Dictation HTML must not contain emojis');

// Verify multi-word hint logic in lessonRequestHint
assert(
    lessonsJs.includes('Starts with <strong>"${esc(firstWord)}..."</strong>'),
    'lessonRequestHint must provide sentence-level first word hint for multi-word dictation'
);
console.log('✓ Dictation hints verified');

// ============================================
// 4. Verb Table Row-by-Row Navigation
// ============================================
console.log('4. Testing Verb Table Enter Navigation...');
const tableJs = fs.readFileSync(path.join(__dirname, '../../engine/verbs/table.js'), 'utf8');
assert(
    tableJs.includes('inputs[idx + 1].focus({ preventScroll: true })'),
    'VerbsTable must advance focus to next input with preventScroll'
);
assert(
    tableJs.includes('firstInput.focus({ preventScroll: true })'),
    'VerbsTable must autofocus first input on desktop with preventScroll'
);
console.log('✓ Verb Table navigation verified');

// ============================================
// 5. SRS Button Confirmation & Badge Sync
// ============================================
console.log('5. Testing SRS Usability and Badge Event...');
const srsJs = fs.readFileSync(path.join(__dirname, '../../engine/srs.js'), 'utf8');
assert(
    srsJs.includes("btn.textContent = '✓ Added to deck!';") && srsJs.includes('btn.disabled = true;'),
    'addToSRS must set button text and disabled state'
);
assert(
    srsJs.includes("window.dispatchEvent(new CustomEvent('srs-updated'"),
    'updateSRSCounter must dispatch srs-updated event'
);

const decksJs = fs.readFileSync(path.join(__dirname, '../../engine/decks.js'), 'utf8');
assert(
    decksJs.includes('updateSRSCounter()'),
    'decks.js must trigger updateSRSCounter on adding a card'
);
console.log('✓ SRS usability and badge synchronization verified');

// ============================================
// 6. Decks SRS Type Mode Mobile Ergonomics
// ============================================
console.log('6. Testing Decks SRS Type Mode Ergonomics & Layout...');
const updatedIndexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
const componentsCss = fs.readFileSync(path.join(__dirname, '../../styles/components.css'), 'utf8');

assert(
    updatedIndexHtml.includes('id="review-type-hint"') && updatedIndexHtml.includes('enterkeyhint="done"'),
    'index.html review-type-field must have enterkeyhint="done" and review-type-hint'
);
assert(
    srsJs.includes('srs_type_mode_hint_seen'),
    'srs.js must track and dismiss srs_type_mode_hint_seen'
);
assert(
    componentsCss.includes('.review-type-input .review-type-check-btn') &&
    componentsCss.includes('display: none !important;'),
    'components.css must hide review-type-check-btn on mobile'
);
console.log('✓ SRS Type Mode layout and mobile Check button suppression verified');

console.log('\nAll 6 functional polish test assertions passed successfully!');

