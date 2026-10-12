/**
 * Test Suite for Learn from Video (Video Listening Practice)
 */
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('Testing Learn from Video Integration...');

// 1. Verify existence of files
const videoEnginePath = path.join(__dirname, '../../engine/drills/video.js');
assert(fs.existsSync(videoEnginePath), 'engine/drills/video.js must exist');

const esVideosPath = path.join(__dirname, '../../content/es-es/videos.json');
assert(fs.existsSync(esVideosPath), 'content/es-es/videos.json must exist');
const esVideos = JSON.parse(fs.readFileSync(esVideosPath, 'utf8'));
assert(Array.isArray(esVideos.videos) && esVideos.videos.length >= 3, 'es-es must have at least 3 authentic videos');

const latamVideosPath = path.join(__dirname, '../../content/es-latam/videos.json');
assert(fs.existsSync(latamVideosPath), 'content/es-latam/videos.json must exist');
const latamVideos = JSON.parse(fs.readFileSync(latamVideosPath, 'utf8'));
assert(Array.isArray(latamVideos.videos) && latamVideos.videos.length >= 3, 'es-latam must have at least 3 authentic videos');

const huVideosPath = path.join(__dirname, '../../content/hu/videos.json');
assert(fs.existsSync(huVideosPath), 'content/hu/videos.json must exist');
const huVideos = JSON.parse(fs.readFileSync(huVideosPath, 'utf8'));
assert(Array.isArray(huVideos.videos) && huVideos.videos.length >= 2, 'hu must have at least 2 authentic videos');

console.log('  [PASS] Video data files exist and contain authentic entries.');

// 2. Validate video schema and structure
[...esVideos.videos, ...latamVideos.videos, ...huVideos.videos].forEach(video => {
    assert(video.id, 'Video must have id');
    assert(video.title, `Video ${video.id} must have title`);
    assert(video.source, `Video ${video.id} must have source/channel`);
    assert(video.youtubeId && video.youtubeId.length === 11, `Video ${video.id} must have valid 11-char YouTube ID`);
    assert(video.level, `Video ${video.id} must have CEFR level`);
    assert(video.duration, `Video ${video.id} must have duration`);

    // Questions validation
    assert(Array.isArray(video.questions) && video.questions.length >= 4, `Video ${video.id} must have at least 4 questions`);
    video.questions.forEach((q, idx) => {
        assert(q.id, `Question ${idx} in ${video.id} must have id`);
        assert(q.question && q.question.trim().length > 0, `Question ${q.id} in ${video.id} must have question text`);
        assert(Array.isArray(q.options) && q.options.length === 4, `Question ${q.id} in ${video.id} must have 4 options`);
        assert(typeof q.answerIndex === 'number' && q.answerIndex >= 0 && q.answerIndex < 4, `Question ${q.id} in ${video.id} must have valid answerIndex`);
        assert(q.explanation && q.explanation.length > 0, `Question ${q.id} in ${video.id} must have pedagogical explanation`);
    });

    // Cloze validation
    assert(Array.isArray(video.cloze) && video.cloze.length >= 5, `Video ${video.id} must have at least 5 cloze lines`);
    video.cloze.forEach((c, idx) => {
        assert(c.text && c.text.includes('[') && c.text.includes(']'), `Cloze ${idx} in ${video.id} must have bracketed target word`);
        assert(c.english && c.english.trim().length > 0, `Cloze ${idx} in ${video.id} must have english translation`);
        assert(Array.isArray(c.options) && c.options.length >= 3, `Cloze ${idx} in ${video.id} must have at least 3 options`);
    });

    // Paragraphs validation
    assert(Array.isArray(video.paragraphs) && video.paragraphs.length >= 3, `Video ${video.id} must have at least 3 paragraphs`);
    video.paragraphs.forEach((p, idx) => {
        const text = p.spanish || p.hungarian || p.text;
        assert(text && text.trim().length > 0, `Paragraph ${idx} in ${video.id} must have transcript text`);
        assert(p.english && p.english.trim().length > 0, `Paragraph ${idx} in ${video.id} must have english translation`);
    });
});
console.log('  [PASS] All videos conform strictly to authentic reportage, quiz, cloze, and transcript structures.');

// 3. Verify listening-studio.js integration
const studioCode = fs.readFileSync(path.join(__dirname, '../../engine/drills/listening-studio.js'), 'utf8');
assert(studioCode.includes("VIDEO: 'video'"), "listening-studio.js must include VIDEO tab constant");
assert(studioCode.includes('data-studio-tab="video"'), "listening-studio.js must include Video tab button");
assert(studioCode.includes('VideoDriller.render'), "listening-studio.js must render VideoDriller");
assert(studioCode.includes('VideoDriller.stop()'), "listening-studio.js must stop VideoDriller");
console.log('  [PASS] listening-studio.js 4th tab integration verified.');

// 4. Verify index.html script tag
const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
assert(indexHtml.includes('engine/drills/video.js'), 'index.html must include video.js script tag');
console.log('  [PASS] index.html registration verified.');

// 5. Verify workshop.js module mapping
const workshopCode = fs.readFileSync(path.join(__dirname, '../../engine/workshop.js'), 'utf8');
assert(workshopCode.includes("video: typeof VideoDriller !== 'undefined' ? VideoDriller"), 'workshop.js must map video to VideoDriller');
console.log('  [PASS] workshop.js module mapping verified.');

// 6. Test VideoDriller engine in simulated DOM environment
global.window = {};
global.document = {
    addEventListener: () => {},
    createElement: tag => ({
        textContent: '',
        innerHTML: '',
        style: {},
        classList: { add: () => {}, remove: () => {}, toggle: () => {} },
        appendChild: () => {},
        querySelectorAll: () => [],
        addEventListener: () => {}
    }),
    getElementById: id => null
};
global.UI = { toast: () => {} };
global.Lang = { code: () => 'es-es', content: rel => rel };
global.Content = {
    json: async () => esVideos
};

require('../../engine/drills/video.js');
assert(typeof global.window.VideoDriller === 'object', 'VideoDriller must be exposed on window');
assert(typeof global.window.VideoDriller.render === 'function', 'VideoDriller must have render function');
assert(typeof global.window.VideoDriller.stop === 'function', 'VideoDriller must have stop function');
console.log('  [PASS] VideoDriller module methods verified.');

// 7. Verify cloze numbering and note reveal logic in engine
const videoSrc = fs.readFileSync(videoEnginePath, 'utf8');
assert(videoSrc.includes('wk-video-cloze-num'), 'video.js must render numbered cloze badges');
assert(videoSrc.includes('wk-video-line-note'), 'video.js must render tip notes with class');
assert(videoSrc.includes('_clozeChecked'), 'video.js must gate tip display behind check/reveal');
console.log('  [PASS] Cloze numbering and conditional tip reveal logic verified.');

console.log('\nAll Learn from Video tests PASSED successfully!\n');

