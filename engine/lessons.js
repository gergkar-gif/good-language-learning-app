// ============================================
// LESSON ENGINE
// ============================================
// Lessons are loaded dynamically from content/<lang>/lessons/*.json
// Two lesson formats are supported during the migration:
//   1. legacy  -> lesson.steps[] with embedded `html`
//   2. structured -> lesson.sections[] referencing content files
// The renderer builds all HTML. Content files stay data-only.
// ============================================

let lessons = {};
let currentLesson = null;
let currentStepIndex = 0;

// End-of-lesson remediation: exercises missed on their first try within a
// lesson are re-served, one at a time, after the last regular step — the
// "let's make sure that sticks" pass. missedSteps is the queue still to
// come; originalStepCount is where the regular lesson ends and the redo
// pass begins, so the progress bar can tell the two apart. See
// finalizeMissedTracking() and nextLessonStep().
let missedSteps = [];
let originalStepCount = 0;

// Which step INDICES have already been graded once this lesson sitting —
// keyed by position in currentLesson.steps, not by stepState (a fresh
// object every render, so it can't remember anything across a re-render
// on its own). The Back button re-renders an earlier step fully
// interactive, on purpose (a learner should be able to look at it again),
// but re-answering it must not count as a second graded interaction:
// without this, solveStep()/failStep() would double lessonStats, and for
// a recycle-block step, double-update its SM-2 schedule for one real
// review. A remediation redo is exempt from this by construction — it's
// pushed onto a NEW index at the end of currentLesson.steps (see
// nextLessonStep()), never the index it originally failed at, so it's
// correctly treated as a fresh, gradable attempt.
let gradedStepIndices = new Set();

// Feeds the end-of-lesson summary screen. lessonStartTime is a wall-clock
// timestamp so the elapsed time survives a tab switch mid-lesson the same
// way progress does. lessonStats counts every graded interaction across the
// lesson (including the remediation redo pass — those are additional
// attempts at mastery, not a do-over that should be forgotten): total is
// every step that reached solveStep()/failStep(), correctFirstTry is how
// many of those never failed on the way there. See solveStep()/failStep().
let lessonStartTime = null;
let lessonStats = { total: 0, correctFirstTry: 0 };
let lastLessonChecklist = null;

// The tab the lesson was opened from, so closing it goes back there.
let lessonReturnTab = 'learn';

// per-step interaction state, reset on every renderStep()
let stepState = {};

// Cache keyed by path, holding the in-flight/settled promise itself rather
// than only the resolved value — recycle.js now requests many of these
// concurrently via Promise.all, and several sections across different
// lessons can share the same exercise-group file. Caching the promise
// synchronously (before any await) means every concurrent caller for the
const contentCache = {};

if (typeof document !== 'undefined') {
    document.addEventListener('language-changed', () => {
        for (const key of Object.keys(contentCache)) {
            delete contentCache[key];
        }
    });
}

async function fetchContent(path) {
    const fullPath = Lang.content(path);
    // One retry before giving up: a transient fetch blip (flaky mobile
    // connection, a cold service worker) on the FIRST reference to a file
    // used to permanently drop that section's steps for the rest of the
    // lesson, while a later section referencing the same file would fetch
    // again (nothing had been cached) and quietly succeed — the lesson
    // would render with fewer total steps than it has, with no sign why.
    for (let attempt = 0; attempt < 2; attempt++) {
        try {
            const response = await fetch(fullPath);
            if (!response.ok) throw new Error('Content not found: ' + fullPath);
            return await response.json();
        } catch (error) {
            if (attempt === 0) continue;
            console.warn('Content missing, using placeholder:', path);
        }
    }
    // Return a safe placeholder so the lesson doesn't crash
    return { title: 'Coming soon', sections: [], words: [], lines: [], exercises: [], cards: [] };
}

function loadContent(path) {
    if (!(path in contentCache)) {
        contentCache[path] = fetchContent(path);
    }
    return contentCache[path];
}

async function loadLesson(lessonId) {
    const parts = lessonId.replace(/^lesson\./, '').split('.');

    const level = parts[0];                        // a1
    const rest = parts.slice(1).join('-');          // 01, 03a, or 01-01 / 01-consolidation

    const path = Lang.content(`lessons/${level}/${level}-${rest}.json`);

    try {
        const response = await fetch(path);
        if (!response.ok) {
            console.error('Lesson not found:', path);
            return null;
        }
        return await response.json();
    } catch (error) {
        console.error('Failed to load lesson:', path, error);
        return null;
    }
}

// ============================================
// SECTION EXPANSION
// ============================================
// Turns `sections` (refs to content files) into a flat list of steps.
// Legacy lessons that already ship `steps` are returned untouched.
// Every word the lesson teaches, in section order, de-duplicated by lemma.
async function collectLessonVocabulary(lesson) {
    const words = [];
    const seen = Object.create(null); // no Object.prototype keys to collide with a real lemma

    for (const section of lesson.sections || []) {
        if (section.type !== 'vocabulary') continue;
        if (section.ref) {
            const vocab = await loadContent(section.ref);
            for (const word of vocab.words || []) {
                if (!word || !word.lemma || seen[word.lemma]) continue;
                seen[word.lemma] = true;
                words.push({
                    lemma: word.lemma,
                    translation: word.translation || '',
                    pos: word.pos || 'unknown'
                });
            }
        } else if (Array.isArray(section.items)) {
            for (const item of section.items) {
                const parts = String(item).split(/\s*[—–-]\s*/);
                const lemma = (parts[0] || '').trim();
                const trans = (parts[1] || '').trim();
                if (lemma && !seen[lemma]) {
                    seen[lemma] = true;
                    words.push({
                        lemma: lemma,
                        translation: trans,
                        pos: 'unknown'
                    });
                }
            }
        }
    }

    return words;
}

async function buildSteps(lesson) {
    if (Array.isArray(lesson.steps) && lesson.steps.length) return lesson.steps;
    if (!Array.isArray(lesson.sections)) return [];

    const steps = [];
    const speakingCandidates = [];
    const seenSpeaking = new Set();

    function addSpeakingCandidate(spanish, english, priority = 1, skillIds = null) {
        if (!spanish || !english) return;
        const cleanEs = String(spanish).replace(/\([^)]*\)/g, '').trim();
        const cleanEn = String(english).replace(/\([^)]*\)/g, '').trim();
        if (cleanEs.length < 2 || seenSpeaking.has(cleanEs.toLowerCase())) return;
        seenSpeaking.add(cleanEs.toLowerCase());
        speakingCandidates.push({ spanish: cleanEs, english: cleanEn, priority, skillIds });
    }

    function injectSpeakingSteps() {
        if (steps.some(s => s.type === 'speaking') || !speakingCandidates.length) return;
        speakingCandidates.sort((a, b) => b.priority - a.priority);
        const cand1 = speakingCandidates[0];
        const cand2 = speakingCandidates[1] || speakingCandidates[0];
        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';

        steps.push({
            type: 'speaking',
            title: 'Speaking Practice 1/2',
            mode: 'read-repeat',
            sentence: cand1.spanish,
            spanish: cand1.spanish,
            english: cand1.english,
            skillIds: cand1.skillIds,
            prompt: `Listen and repeat this out loud in ${langName}:`
        });

        steps.push({
            type: 'speaking',
            title: 'Speaking Practice 2/2',
            mode: 'prompt-speak',
            sentence: cand2.spanish,
            spanish: cand2.spanish,
            english: cand2.english,
            skillIds: cand2.skillIds,
            prompt: `Translate and say this out loud in ${langName}:`
        });
    }

    async function injectCommunicativeChallenge() {
        if (steps.some(s => s.type === 'challenge')) return;
        if (!checklistStep || !checklistStep.items || !checklistStep.items.length) return;

        const primaryCanDo = checklistStep.items[0];
        const level = (lesson && lesson.level) || 'A1';
        const tier = (level === 'A1') ? 'tier1' : (level === 'A2') ? 'tier2' : 'tier3';
        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';

        // Check if curated challenges dictionary has a match
        let curated = null;
        try {
            const challengeData = await loadContent('curriculum/challenges.json');
            if (challengeData && challengeData.challenges) {
                const stem = (lesson.id || '').replace(/^lesson\./, '').split('.').join('-');
                curated = challengeData.challenges[stem];
                if (!curated) {
                    const keys = Object.keys(challengeData.challenges);
                    const matchedKey = keys.find(k => stem.startsWith(k) || (lesson.title && lesson.title.toLowerCase().includes(k.split('-')[1] || '')));
                    if (matchedKey) curated = challengeData.challenges[matchedKey];
                }
            }
        } catch (e) {}

        let challengeStep = null;
        if (curated) {
            challengeStep = {
                type: 'challenge',
                title: curated.title || 'Communicative Challenge',
                scenario: curated.scenario || '',
                prompt: curated.prompt || '',
                cues: curated.cues || [],
                target: curated.target || '',
                canDo: curated.canDo || primaryCanDo,
                level: curated.level || level,
                tier: curated.tier || tier,
                modality: curated.modality || 'oral'
            };
        } else {
            // Dynamic generation based on CEFR level and Can-Do item
            const formatted = (typeof CanDoPrompt !== 'undefined')
                ? CanDoPrompt.formatPrompt(primaryCanDo, {
                    language: langName,
                    langCode: (typeof Lang !== 'undefined' ? Lang.code() : 'es'),
                    level: level,
                    modality: 'oral'
                })
                : null;

            if (tier === 'tier1') {
                const cand = (speakingCandidates && speakingCandidates[0]) || null;
                challengeStep = {
                    type: 'challenge',
                    title: `Communicative Challenge: ${formatted ? formatted.title : 'Put It Into Practice'}`,
                    scenario: (formatted && formatted.scenario) || `Put your ${langName} into action for this lesson's core goal.`,
                    prompt: (formatted && formatted.prompt) || primaryCanDo.replace(/^I can\s+/i, 'Say this in ' + langName + ': ').replace(/\.$/, ''),
                    cues: cand ? [`Use what you learned: "${cand.english}"`] : ((formatted && formatted.cues) || ['Express this clearly out loud']),
                    target: cand ? (cand.spanish || cand.target || '') : '',
                    canDo: primaryCanDo,
                    level: level,
                    tier: 'tier1',
                    modality: 'oral'
                };
            } else if (tier === 'tier2') {
                challengeStep = {
                    type: 'challenge',
                    title: `Communicative Challenge: ${formatted ? formatted.title : 'Put It Into Practice'}`,
                    scenario: (formatted && formatted.scenario) || `You are in a practical everyday situation in ${langName}.`,
                    prompt: (formatted && formatted.prompt) || primaryCanDo.replace(/^I can\s+/i, 'In ' + langName + ', perform this task: '),
                    cues: (formatted && formatted.cues && formatted.cues.length) ? formatted.cues : [
                        'State your idea or request clearly',
                        `Use what you learned in this lesson`
                    ],
                    canDo: primaryCanDo,
                    level: level,
                    tier: 'tier2',
                    modality: 'oral'
                };
            } else {
                challengeStep = {
                    type: 'challenge',
                    title: `Communicative Challenge: ${formatted ? formatted.title : 'In-Depth Production'}`,
                    scenario: (formatted && formatted.scenario) || `Express your ideas, narrate, and evaluate in connected ${langName}.`,
                    prompt: (formatted && formatted.prompt) || primaryCanDo.replace(/^I can\s+/i, 'Discuss and explain: '),
                    cues: (formatted && formatted.cues && formatted.cues.length) ? formatted.cues : [
                        'Set the context or introduce the topic',
                        'Describe the details or analyze the situation',
                        'Share your conclusion, reaction, or recommendation'
                    ],
                    canDo: primaryCanDo,
                    level: level,
                    tier: 'tier3',
                    modality: 'oral'
                };
            }
        }

        if (challengeStep) {
            steps.push(challengeStep);
        }
    }

    let checklistStep = null;

    // Parallel pre-fetch of all section references to collapse serial waterfalls
    const sectionRefs = (lesson.sections || [])
        .filter(s => s && s.ref)
        .map(s => s.ref);
    if (sectionRefs.length) {
        await Promise.all(sectionRefs.map(ref => loadContent(ref)));
    }

    for (const section of lesson.sections) {
        try {
            if (section.type === 'goal') {
                steps.push({
                    type: 'goal',
                    title: section.title || 'Lesson Goals',
                    items: section.items || []
                });
            }

            // A one-off welcome screen, not a grammar concept — kept as its
            // own section type rather than reusing `grammar` so it never
            // shows up as a topic in that unit's Grammar Guide.
            else if (section.type === 'intro') {
                steps.push({
                    type: 'intro',
                    title: section.title || 'Welcome',
                    body: section.body || []
                });
            }

            else if (section.type === 'recycle') {
                const pool = (typeof Recycle !== 'undefined') ? await Recycle.collectPool(lesson) : [];
                const picks = (typeof Recycle !== 'undefined') ? Recycle.pick(pool, section.count || 3) : [];
                picks.forEach((exercise, i) => {
                    steps.push(Object.assign({}, exercise, {
                        title: (section.title || 'Quick Review')
                            + (picks.length > 1 ? ' ' + (i + 1) + '/' + picks.length : ''),
                        isRecycle: true
                    }));
                });
            }

            else if (section.type === 'grammar') {
                // One screen per grammar concept. The file's parts (text,
                // table, examples, tip) render together — splitting them into
                // a screen each produced a run of near-empty pages that all
                // carried the same heading.
                const grammar = await loadContent(section.ref);
                const parts = grammar.sections || [];
                parts.forEach(part => {
                    if (part.type === 'examples' && Array.isArray(part.items)) {
                        part.items.forEach(it => {
                            if (it.spanish && it.english) addSpeakingCandidate(it.spanish, it.english, 3);
                        });
                    } else if (part.type === 'table' && Array.isArray(part.rows)) {
                        part.rows.forEach(r => {
                            if (r[0] && r[1]) addSpeakingCandidate(r[0], r[1], 2);
                        });
                    }
                });
                steps.push({
                    type: 'grammar',
                    title: section.title || grammar.title,
                    parts: parts
                });
            }

            else if (section.type === 'vocabulary') {
                let words = [];
                let vocabTitle = 'Vocabulary';
                if (section.ref) {
                    const vocab = await loadContent(section.ref);
                    words = vocab.words || [];
                    vocabTitle = vocab.title || vocabTitle;
                } else if (Array.isArray(section.items)) {
                    words = section.items.map(item => {
                        const parts = String(item).split(/\s*[—–-]\s*/);
                        return {
                            lemma: (parts[0] || '').trim(),
                            translation: (parts[1] || '').trim(),
                            pos: 'unknown'
                        };
                    });
                }
                words.forEach(w => {
                    if (w.lemma && w.translation) addSpeakingCandidate(w.lemma, w.translation, 1);
                });
                steps.push({
                    type: 'vocabulary',
                    title: section.title || vocabTitle,
                    words: words
                });
            }

            else if (section.type === 'story') {
                const story = await loadContent(section.ref);
                const voices = (typeof Reader !== 'undefined' && typeof Reader.assignCharacterVoices === 'function')
                    ? Reader.assignCharacterVoices(story)
                    : {};
                steps.push({
                    type: 'story',
                    title: section.title || story.title,
                    // Story files use `paragraphs` (same schema the Library
                    // reader consumes), not a separate bilingual `lines` shape.
                    lines: story.paragraphs || [],
                    characterVoices: voices,
                    characterGenders: (voices && voices._genders) || {}
                });
            }

            else if (section.type === 'exercise-group') {
                const file = await loadContent(section.ref);
                const all = file.exercises || [];
                const ids = section.exerciseRefs || [];
                ids.forEach((id, i) => {
                    const exercise = all.find(e => e.id === id);
                    if (!exercise) {
                        console.warn('Exercise not found:', id);
                        return;
                    }
                    if (exercise.sentence && (exercise.english || exercise.translation)) {
                        const clean = exercise.sentence.replace(/_{2,}/g, exercise.answer || '');
                        addSpeakingCandidate(clean, exercise.english || exercise.translation, 2, exercise.teaches);
                    } else if (exercise.spanish && exercise.english) {
                        addSpeakingCandidate(exercise.spanish, exercise.english, 2, exercise.teaches);
                    }
                    steps.push(Object.assign({}, exercise, {
                        title: !section.title ? 'Exercise'
                            : ids.length > 1 ? section.title + ' ' + (i + 1) + '/' + ids.length
                            : section.title
                    }));
                });
            }

            else if (section.type === 'srs') {
                // Before Add to Review, inject the 2 dedicated speaking steps!
                injectSpeakingSteps();

                // Cards are the lesson's own vocabulary — there is no second
                // word list to keep in sync, and the learner picks which of
                // them are worth reviewing.
                steps.push({
                    type: 'srs',
                    title: section.title || 'Add to Review',
                    cards: await collectLessonVocabulary(lesson)
                });
            }

            else if (section.type === 'challenge') {
                steps.push({
                    type: 'challenge',
                    title: section.title || 'Communicative Challenge',
                    scenario: section.scenario || '',
                    prompt: section.prompt || '',
                    cues: section.cues || [],
                    target: section.target || '',
                    canDo: section.canDo || section.canDoRef || '',
                    level: lesson.level || 'A1',
                    tier: section.tier || null,
                    modality: section.modality || 'oral'
                });
            }

            else if (section.type === 'checklist') {
                checklistStep = {
                    type: 'checklist',
                    title: section.title || 'Can you do this?',
                    items: section.items || []
                };
            }

            else {
                console.warn('Unknown section type:', section.type);
            }
        } catch (error) {
            console.error('Failed to expand section', section, error);
        }
    }

    // Safety fallback: ensure speaking steps are injected even if lesson has no SRS
    injectSpeakingSteps();

    // Inject progressive communicative challenge linked to CEFR Can-Do
    await injectCommunicativeChallenge();

    // "I can do this" / checklist should ALWAYS be the last screen of the lesson, right before results.
    if (checklistStep) {
        steps.push(checklistStep);
    }

    return steps;
}

async function startLesson(lessonId) {
    if (typeof UI !== 'undefined') UI.showLoading('Loading lesson…', { immediate: true });

    try {
        const lesson = await loadLesson(lessonId);
        if (!lesson) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Lesson coming soon!', 'info');
            else alert('Lesson coming soon!');
            return;
        }

        lesson.steps = await buildSteps(lesson);

        if (!lesson.steps.length) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('This lesson has no content yet.', 'info');
            else alert('This lesson has no content yet.');
            return;
        }

        currentLesson = lesson;
        if (typeof LearnerPath !== 'undefined') LearnerPath.touchActivity();
        currentStepIndex = 0;
        originalStepCount = lesson.steps.length;
        missedSteps = [];
        lessonStartTime = Date.now();
        lessonStats = { total: 0, correctFirstTry: 0 };
        gradedStepIndices = new Set();

        // A lesson can be opened from the level list or from Home's continue
        // card, and closing it should put the learner back where they were rather
        // than always on the level list.
        const from = document.querySelector('.tab:not(.hidden)');
        lessonReturnTab = (from && from.id !== 'lesson-screen') ? from.id : 'learn';

        document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
        document.getElementById('lesson-screen').classList.remove('hidden');
        document.body.classList.add('in-lesson');

        // Push browser history state so browser Back button returns cleanly instead of leaving the app
        if (typeof history !== 'undefined' && history.pushState) {
            history.pushState({ parlourModal: 'lesson', lessonId }, '');
        }

        document.getElementById('lesson-title').textContent = currentLesson.title;
        const subtitle = document.getElementById('lesson-subtitle');
        const levelMark = (typeof levelIcon === 'function') ? levelIcon(currentLesson.level, 'level-icon--sm') : '';
        subtitle.innerHTML = levelMark + '<span>' + UI.escape(currentLesson.level) + '</span>';

        const guideSlot = document.getElementById('lesson-guide-slot');
        if (guideSlot) {
            guideSlot.innerHTML = '';
            if (typeof Guide !== 'undefined' && !Guide.hasSeen('lesson')) {
                Guide.attachBanner(guideSlot, 'lesson');
            }
        }

        renderStep();
    } catch (err) {
        console.error('Failed to start lesson:', lessonId, err);
        if (typeof UI !== 'undefined' && UI.toast) UI.toast('Could not load lesson. Please try again.', 'error');
        else alert('Could not load lesson. Please try again.');
    } finally {
        if (typeof UI !== 'undefined') UI.hideLoading();
    }
}

// Pure state reset — no DOM/tab navigation — so it's safe to call from
// anywhere a lesson is being abandoned, including from showTab() when the
// learner leaves via the main nav instead of the lesson's own close button.
// closeLesson() below calls this too, then handles the navigation part.
function teardownLesson() {
    const guideSlot = document.getElementById('lesson-guide-slot');
    if (guideSlot) guideSlot.innerHTML = '';
    document.body.classList.remove('in-lesson');
    currentLesson = null;
    currentStepIndex = 0;
    missedSteps = [];
    originalStepCount = 0;
    gradedStepIndices = new Set();
    lessonStartTime = null;
    lessonStats = { total: 0, correctFirstTry: 0 };
    lastLessonChecklist = null;
    if (typeof _lessonUserAudioPlayer !== 'undefined' && _lessonUserAudioPlayer) {
        try { _lessonUserAudioPlayer.pause(); } catch (e) {}
        _lessonUserAudioPlayer = null;
    }
    if (typeof DeckMatch !== 'undefined' && typeof DeckMatch.stop === 'function') {
        DeckMatch.stop();
    }
    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.stopListening();
        SpeechInput.releaseStream();
    }
    _inlineVoiceActive = false;
    _lessonSpeakingRecording = false;
    const lessonFooter = document.querySelector('#lesson-screen .lesson-footer');
    if (lessonFooter) lessonFooter.style.display = '';
    stepState = {};
}

function closeLesson(options) {
    teardownLesson();
    document.getElementById('lesson-screen').classList.add('hidden');

    // If closed via on-screen button (not popstate event) and history state was pushed, pop it
    const fromPop = options && options.fromPopstate;
    if (!fromPop && typeof history !== 'undefined' && history.state && history.state.parlourModal === 'lesson') {
        history.back();
    }

    // Through showTab rather than by hand, so the section is re-rendered on
    // the way in: a lesson just finished is the moment its level list and
    // Home are both out of date.
    showTab(lessonReturnTab, document.querySelector('.nav button[data-tab="' + lessonReturnTab + '"]'));
}

// The lesson-complete screen's "Quick Reinforce" buttons (see
// summaryReinforceHtml()) — same teardown as Done/closeLesson, but landing
// on Workshop with a driller already open and scoped, instead of wherever
// the lesson was originally opened from. The learner chose to keep
// practicing, not to leave.
function _openReinforce(drillerId, options) {
    teardownLesson();
    document.getElementById('lesson-screen').classList.add('hidden');
    showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
    if (typeof Workshop !== 'undefined') Workshop.open(drillerId, options);
}

// ============================================
// HELPERS
// ============================================
function esc(value) {
    return String(value == null ? '' : value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

// Same escaping as esc(), plus *word* / **word** markdown emphasis rendered
// as italics — the convention content authors use to call out a Spanish
// word inside otherwise-English prose (e.g. "this means *adiós*"). Doubles
// are unwound first so **x** doesn't get read as two single-asterisk pairs.
function escMd(value) {
    return esc(value)
        .replace(/\*\*([^*]+)\*\*/g, '<em>$1</em>')
        .replace(/\*([^*]+)\*/g, '<em>$1</em>');
}

// Bolds `word` where it appears literally in `sentence` — used by the
// substitution exercise to show what changed. Deliberately a plain
// substring match, not a guess: the caller passes the word's ACTUAL
// inflected form as it appears in that exact sentence (content authors
// write both together), so this never has to reconcile a bare lemma
// against an inflected surface form itself. No match (wrong word passed,
// or the field is missing) just renders the plain escaped sentence.
function highlightWord(sentence, word) {
    const text = String(sentence || '');
    if (!word) return esc(text);
    const idx = text.indexOf(word);
    if (idx === -1) return esc(text);
    return esc(text.slice(0, idx)) + '<strong>' + esc(text.slice(idx, idx + word.length)) + '</strong>'
        + esc(text.slice(idx + word.length));
}

// A listen button for a piece of target language. Returns '' only when neither cloud
// nor device speech can run, so every caller can add it without a guard.
function say(text, options) {
    return (typeof ParlourTTS !== 'undefined') ? ParlourTTS.button(text, options) : '';
}

// A real recording beats TTS whenever content supplies one for this exact
// cell value — see table()'s audioMap. Falls back to the normal TTS button
// when there's no recording for this specific text.
function sayOrPlay(text, audioUrl) {
    if (audioUrl && typeof Speech !== 'undefined') return Speech.audioButton(audioUrl, text);
    return say(text);
}

function shuffled(list) {
    const copy = list.slice();
    for (let i = copy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
}

// Options are shuffled here rather than in the content files. Every
// multiple-choice item in the course stores its correct answer first, which
// keeps a file reviewable at a glance — and, shipped in that order, made the
// answer the top button every single time. Shuffling at render keeps the
// convention and takes away the tell. The index moves with the option, so
// stepState.correct always refers to what is on screen.
//
// `correct` is normally a single index, but a handful of items (e.g. a
// dialogue reply where more than one option is a genuinely natural answer)
// have more than one right option — those pass an array instead, and it is
// remapped through the shuffle the same way.
function shuffledOptions(options, correct) {
    const order = shuffled((options || []).map((text, i) => ({ text, i })));
    const remap = i => order.findIndex(option => option.i === i);
    return {
        options: order.map(option => option.text),
        correct: Array.isArray(correct) ? correct.map(remap) : remap(correct)
    };
}

// Accents are checked directly for every language, Spanish included as of
// 2026-08-27. Spanish used to drop them before comparing (leniency for a
// learner without a Spanish keyboard), but that leniency was hiding real
// content bugs rather than typing friction: a2-14-01's own grammar tip
// teaches "qué/dónde/cuándo/cómo carry an accent because they're asking,
// not relating" while the old lenient check accepted "que/donde/cuando/como"
// as equally correct for the same blank, silently disproving the lesson it
// sat right next to. A corpus-wide check of every interrogative/relative
// minimal pair (qué/que, cómo/como, dónde/donde, cuándo/cuando, cuál/cual,
// quién/quien) across every fill-blank and sentence-builder answer in A1,
// A2, and B1 found the content itself already gets this right everywhere -
// it was only the grading that was lenient. Hungarian was never lenient
// here: accents there are often the entire distinction between different
// words or grammatical forms (kor / kor-with-acute / kor-with-umlaut are
// three unrelated words), so this makes Spanish consistent with the
// standard the course already held Hungarian to.
function normalise(text) {
    const value = String(text || '')
        .toLowerCase()
        .replace(/["'«»“”„—–\-]/g, ' ')
        .replace(/[.,!?¡¿;:]/g, '')
        .replace(/\s+/g, ' ')
        .trim();
    // Normalise Unicode representation (NFC) so a precomposed accented
    // letter typed on one keyboard/IME matches a decomposed one from
    // another - this is normalisation of representation, not leniency;
    // the accent itself is never stripped.
    return value.normalize('NFC');
}

function baseChar(c) {
    return String(c || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
}

// Computes a granular character-level diff between the user's attempt and
// the acceptable answer(s). Accents are separated from typos so learners
// missing an accent get an actionable, pinpoint hint.
function generateAnswerDiff(userRaw, acceptableList) {
    const user = String(userRaw || '').trim();
    if (!user) return null;

    const list = Array.isArray(acceptableList) ? acceptableList : [acceptableList];
    if (!list.length) return null;

    // Find the closest candidate in acceptable list based on LCS length
    let bestCandidate = list[0];
    let bestLcs = -1;
    let bestDp = null;

    for (const cand of list) {
        const expected = String(cand || '').trim();
        const m = user.length;
        const n = expected.length;
        const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                if (baseChar(user[i - 1]) === baseChar(expected[j - 1])) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        if (dp[m][n] > bestLcs) {
            bestLcs = dp[m][n];
            bestCandidate = expected;
            bestDp = dp;
        }
    }

    const expected = bestCandidate;
    const m = user.length;
    const n = expected.length;
    const dp = bestDp;

    const lcsLen = dp[m][n];
    const maxLen = Math.max(m, n);
    // Don't show diff for completely dissimilar or trivial strings
    if (lcsLen < 2 && maxLen > 3) return null;
    if (lcsLen / maxLen < 0.35) return null;

    let i = m, j = n;
    const ops = [];
    let onlyAccents = true;
    while (i > 0 || j > 0) {
        if (i > 0 && j > 0 && baseChar(user[i - 1]) === baseChar(expected[j - 1])) {
            if (user[i - 1] === expected[j - 1]) {
                ops.unshift({ t: 'eq', text: user[i - 1] });
            } else {
                ops.unshift({ t: 'accent', text: user[i - 1], exp: expected[j - 1] });
            }
            i--; j--;
        } else if (i > 0 && (j === 0 || dp[i - 1][j] >= dp[i][j - 1])) {
            ops.unshift({ t: 'del', text: user[i - 1] });
            onlyAccents = false;
            i--;
        } else {
            ops.unshift({ t: 'ins', text: expected[j - 1] });
            onlyAccents = false;
            j--;
        }
    }

    // Merge consecutive insertions and deletions
    const merged = [];
    for (const op of ops) {
        const last = merged[merged.length - 1];
        if (last && last.t === op.t && op.t !== 'accent') {
            last.text += op.text;
        } else {
            merged.push({ ...op });
        }
    }

    let html = '';
    const accentList = [];
    for (const op of merged) {
        if (op.t === 'eq') {
            html += esc(op.text);
        } else if (op.t === 'accent') {
            accentList.push(`${op.text} → ${op.exp}`);
            html += `<span class="lsn-diff-accent">${esc(op.text)}<span class="lsn-diff-accent-hint">${esc(op.exp)}</span></span>`;
        } else if (op.t === 'del') {
            html += `<del class="lsn-diff-del">${esc(op.text)}</del>`;
        } else if (op.t === 'ins') {
            html += `<ins class="lsn-diff-ins">${esc(op.text)}</ins>`;
        }
    }

    return {
        onlyAccents,
        accentList,
        html,
        expected
    };
}

function feedbackHtml() {
    return '<p id="step-feedback" class="lsn-feedback"></p><div id="step-diff" class="lsn-diff" style="display:none;"></div><p id="step-translation" class="lsn-en"></p>';
}

// Shown once the answer is settled (solved or revealed after 3 tries), so a
// learner who just solved a Spanish sentence sees what it means in English.
// Only exercises whose content carries a translation (stepState.translation)
// have anything to show here — sentence-builder shows its own via
// revealBuildEnglish() instead, since that one sits above the sentence, not
// in the shared feedback area.
function showTranslation() {
    const el = document.getElementById('step-translation');
    if (el && stepState.translation) el.textContent = stepState.translation;
}

// Green for correct, matching .lsn-option.correct and every other
// correctness indicator in the app — a 2026-08-19 pass made this consistent
// on purpose after finding the app had drifted into a navy/green split with
// no functional reason (tap-based exercises were already green; typed
// inputs, sentence-builder, and this text were still navy). This
// intentionally supersedes the older "navy for correct, green is only for
// SRS mastery" rule from visual identity v2 (see base.css's --success
// comment) — green is the general correctness colour now, app-wide.
function setFeedback(ok, message) {
    const el = document.getElementById('step-feedback');
    if (!el) return;
    el.textContent = message;
    el.style.color = ok ? 'var(--success)' : 'var(--accent-dark)';
}

// ============================================
// STEP GATING
// ============================================
// Exercise steps hold the footer button locked until they are answered.
// Three wrong attempts reveal the answer and release the gate, so a learner
// can never be stuck on one item.
const MAX_ATTEMPTS = 3;

function gateStep() {
    stepState.gated = true;
    stepState.solved = false;
    stepState.attempts = 0;
}

// One button at the bottom of every lesson screen: it reads "Check" and
// calls the step's checkFn while the step is gated and unsolved, then flips
// to "Continue →" (or "Finish Lesson" on the last step) the moment the
// step is solved — whether by a correct answer or by burning every attempt.
// Steps with nothing to check (info screens, matching, srs) never set a
// checkFn, so this always shows Continue for them, gated only on `solved`.
function updateFooterButton() {
    const btn = document.getElementById('lesson-next-btn');
    if (!btn) return;

    if (stepState.gated && !stepState.solved && stepState.checkFn) {
        const fnName = stepState.checkFn;
        btn.textContent = 'Check';
        btn.onclick = () => { const fn = window[fnName]; if (fn) fn(); };
        btn.disabled = !!stepState.checkDisabled;
        btn.classList.toggle('is-locked', !!stepState.checkDisabled);
        return;
    }

    // "Last step" only means "finishing" once the remediation queue is
    // empty too — nextLessonStep() is what actually pulls the next missed
    // step in when there is one, so the button always just says Continue
    // until there is truly nothing left to do.
    const atEnd = currentStepIndex >= currentLesson.steps.length - 1;
    const finishing = atEnd && !missedSteps.length;
    const locked = !!stepState.gated && !stepState.solved;
    btn.textContent = finishing ? 'Finish Lesson ✓' : 'Continue →';
    btn.onclick = nextLessonStep;
    btn.disabled = locked;
    btn.classList.toggle('is-locked', locked);
}

function solveStep(message) {
    stepState.solved = true;
    setFeedback(true, message);
    const diffEl = document.getElementById('step-diff');
    if (diffEl) { diffEl.innerHTML = ''; diffEl.style.display = 'none'; }
    showTranslation();
    updateFooterButton();
    if (typeof Sound !== 'undefined') Sound.correct();

    // A revisit via the Back button re-renders this same step index fully
    // interactive (see gradedStepIndices' own comment) — the learner still
    // gets to see it marked right/wrong again, but it must not count a
    // second time toward lesson stats or a recycle item's SM-2 schedule.
    if (gradedStepIndices.has(currentStepIndex)) return;
    gradedStepIndices.add(currentStepIndex);

    noteRecycleResult(true);
    queueForRemediationIfMissed();
    lessonStats.total++;
    if (!stepState.wasMissed) lessonStats.correctFirstTry++;
}

// Records a wrong attempt. Returns true once the learner is out of tries,
// which is the caller's cue to reveal the answer.
function failStep(message) {
    stepState.attempts = (stepState.attempts || 0) + 1;
    const left = MAX_ATTEMPTS - stepState.attempts;
    if (typeof Sound !== 'undefined') Sound.wrong();

    // The first wrong attempt is what "missed on the first try" means —
    // later attempts on the same try-count just narrate how many are left.
    if (stepState.attempts === 1) stepState.wasMissed = true;

    if (left > 0) {
        setFeedback(false, message + ' — ' + left + (left === 1 ? ' try left' : ' tries left'));
        return false;
    }

    stepState.solved = true;
    // Exhausting every attempt already reveals the answer — that's the
    // existing "never stuck on one item" escape valve. Queuing a gaveUp step
    // for remediation too would turn a step the learner is genuinely stuck
    // on into a loop with no exit, so this path does not queue it again.
    stepState.gaveUp = true;
    showTranslation();
    updateFooterButton();

    // Same revisit guard as solveStep() — see gradedStepIndices' own
    // comment on why a Back-button redo mustn't double-count.
    if (gradedStepIndices.has(currentStepIndex)) return true;
    gradedStepIndices.add(currentStepIndex);

    noteRecycleResult(false);
    lessonStats.total++;
    return true;
}

// A step that took a wrong attempt before landing on the right answer goes
// back on the queue to be re-served once, after the last regular step —
// unless it's a recycle-block item, which already has its own SM-2 schedule
// outside this lesson and shouldn't be graded twice for one sitting.
function queueForRemediationIfMissed() {
    if (!stepState.wasMissed || stepState.gaveUp) return;
    if (!stepState.sourceStep || stepState.sourceStep.isRecycle) return;
    missedSteps.push(stepState.sourceStep);
}

// Every teaches-tagged exercise's outcome feeds its own SM-2 schedule, not
// just recycle-block repeats — a skill's first-ever encounter is evidence
// too, and used to be silently discarded unless that exact exercise later
// got redrawn into some future lesson's recycle pool. Solved clean is
// "good", solved only after burning every attempt is "again", same
// distinction the vocabulary deck's rating buttons make.
function noteRecycleResult(success) {
    if (stepState.recycleNoted) return;
    const step = currentLesson.steps[currentStepIndex];
    if (!step || !step.id || !step.teaches || !step.teaches.length) return;
    stepState.recycleNoted = true;
    if (typeof Recycle !== 'undefined') Recycle.record(step.id, success ? 'good' : 'again');
}

function revealHtml(inner) {
    return '<div class="lsn-reveal">' + inner + '</div>';
}

// The remediation queue can grow currentLesson.steps past its original
// length, so the bar tracks against originalStepCount instead — otherwise
// a lesson with 3 missed steps would show "23 of 23" and reset to 100% on
// every redo instead of counting down the redo pass itself.
function lessonProgressHtml() {
    if (currentStepIndex >= originalStepCount) {
        const position = currentStepIndex - originalStepCount + 1;
        const total = position + missedSteps.length;
        return `
            <div class="lsn-progress">
                <div class="lsn-progress-bar" style="width:100%"></div>
            </div>
            <div class="lsn-progress-label">Quick review — ${position} of ${total}</div>
        `;
    }

    const total = originalStepCount;
    const pct = Math.round(((currentStepIndex + 1) / total) * 100);
    return `
        <div class="lsn-progress">
            <div class="lsn-progress-bar" style="width:${pct}%"></div>
        </div>
        <div class="lsn-progress-label">Step ${currentStepIndex + 1} of ${total}</div>
    `;
}

// ============================================
// COMPONENT RENDERERS (JSON -> HTML)
// ============================================
const stepRenderers = {

    goal(step) {
        return `
            <ul class="lsn-goal">
                ${(step.items || []).map(item => `<li>${esc(item)}</li>`).join('')}
            </ul>
        `;
    },

    intro(step) {
        return (step.body || []).map(p => `<p class="lsn-text">${escMd(p)}</p>`).join('');
    },

    // A whole grammar concept on one screen. Only presentational parts are
    // rendered — an exercise belongs in an exercise-group, not in here.
    // Wrapped in .lsn-grammar so styles/components.css can italicize target-
    // language text (the examples/table target-language column, plus any
    // *word* markup in text/tip prose — see escMd()) without touching the
    // shared .lsn-es class every other lesson step also uses; grammar
    // screens are the one place a Hungarian/Spanish word needs to visually
    // stand apart from the English explaining it.
    grammar(step) {
        const allowed = ['text', 'table', 'examples', 'tip', 'external-link'];
        const body = (step.parts || [])
            .filter(part => allowed.indexOf(part.type) !== -1)
            .map(part => {
                const heading = part.title && part.title !== step.title
                    ? `<h4 class="lsn-subtitle">${escMd(part.title)}</h4>`
                    : '';
                return heading + stepRenderers[part.type](part);
            })
            .join('');
        return `<div class="lsn-grammar">${body}</div>`;
    },

    text(step) {
        return `<p class="lsn-text">${escMd(step.content)}</p>`;
    },

    tip(step) {
        return `<div class="lsn-tip"><strong>Tip</strong><p>${escMd(step.content)}</p></div>`;
    },

    // A table serves two different shapes of content: a sentence/translation
    // reference (row 0 Spanish, row 1 English — only row 0 needs audio) and a
    // conjugation paradigm (row 0 a bare pronoun, row 1 the conjugated
    // Spanish form — the form is the whole point, and used to have no listen
    // button at all). Detecting a pronoun in row 0 tells the two apart
    // without a schema change. A third shape — row 0 a bare letter/digraph,
    // row 1 the actual word demonstrating it — needs row 1 audible too, but
    // "is this a letter" isn't reliably detectable from the string alone, so
    // content opts in explicitly with `"bothAudible": true` on the section
    // rather than guessing. `audioMap` (optional) maps an exact cell string
    // to a real recording's URL — content that can source one (so far just
    // Hungarian's letter-sound tables) gets a human voice instead of TTS,
    // cell by cell, with TTS as the fallback for any cell not in the map.
    table(step) {
        const PRONOUN_PART = '(yo|tú|tu|usted|ud\\.?|él|el|ella|nosotros|nosotras|nosotros/as|vosotros|vosotras|vosotros/as|ustedes|uds\\.?|ellos|ellas|én|te|ő|ön|mi|ti|ők|önök|a\\s+mí|a\\s+ti|a\\s+él|a\\s+ella|a\\s+usted)';
        const PRONOUN_RE = new RegExp(`^${PRONOUN_PART}(\\s*[/,]\\s*${PRONOUN_PART})*$`, 'i');
        const audioMap = step.audioMap || {};
        return `
            <table class="lsn-table">
                ${(step.rows || []).map(row => {
                    const col0 = row[0] || '';
                    const col1 = row[1] || '';
                    const cleanCol0 = col0.replace(/[*_()]/g, '').trim();
                    const isConjugation = step.bothAudible || PRONOUN_RE.test(cleanCol0);
                    // If a table row was authored in [English, Target] order rather than standard [Target, English],
                    // swap on render so the target language is primary, bold, and voiced, never the English gloss.
                    const col0IsEnglish = !isConjugation && /^[a-z\s.,'?!-]*$/i.test(col0) && /\b(the|to|i|you|he|she|we|they|my|your|what|where|when|is|are|please|thank|good|hello|how|do|have|rest|drink|want)\b/i.test(col0);
                    const primaryText = col0IsEnglish ? col1 : col0;
                    const secondaryText = col0IsEnglish ? col0 : col1;
                    const primaryAudio = sayOrPlay(primaryText, audioMap[primaryText]);
                    const secondaryAudio = (isConjugation && !col0IsEnglish) ? sayOrPlay(secondaryText, audioMap[secondaryText]) : '';

                    return `
                    <tr>
                        <td><strong>${esc(primaryText)}</strong>${primaryAudio}</td>
                        <td>${esc(secondaryText)}${secondaryAudio}</td>
                    </tr>
                `;
                }).join('')}
            </table>
        `;
    },

    examples(step) {
        const target = window.Reader && window.Reader.makeClickable
            ? text => Reader.makeClickable(text)
            : escMd;
        return (step.items || []).map(item => `
            <div class="lsn-example">
                <div class="lsn-es">${target(item.spanish)}${say(item.spanish)}</div>
                <div class="lsn-en">${escMd(item.english)}</div>
            </div>
        `).join('');
    },

    // Closes a grammar explanation with a sentence rather than a bare link,
    // so the reference reads as part of the teaching.
    'external-link'(step) {
        const site = esc(step.site || 'Lingolia');
        const link = `<a href="${esc(step.url)}" target="_blank" rel="noopener noreferrer">${site}</a>`;
        return `<p class="lsn-reference">Read more about ${esc(step.topic || step.title || 'this')} on ${link}.</p>`;
    },

    // step.addToDeck (Word Bank only, not the in-lesson step — a lesson
    // already has its own end-of-lesson Review/Know-it flow for adding
    // words, see finishLesson()) adds a small per-row button wired via
    // data attributes + delegated click, not an inline onclick, since a
    // translation can contain a quote character ("don't") that would
    // break a naively-interpolated JS string literal.
    vocabulary(step) {
        return `
            <div class="lsn-vocab">
                ${(step.words || []).map(word => `
                    <div class="lsn-vocab-row">
                        <div>
                            <div class="lsn-es">${esc(word.lemma)}${say(word.lemma)}</div>
                            <div class="lsn-pos">${esc(word.pos)}</div>
                        </div>
                        <div class="lsn-vocab-row-end">
                            <div class="lsn-en">${esc(word.translation)}</div>
                            ${step.addToDeck ? `
                                <button class="lsn-vocab-add" data-add-to-deck
                                    data-lemma="${esc(word.lemma)}" data-translation="${esc(word.translation)}" data-pos="${esc(word.pos)}"
                                    aria-label="Add ${esc(word.lemma)} to a deck">+</button>
                            ` : ''}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    },

    dialogue(step) {
        return `
            <div class="lsn-dialogue">
                ${(step.lines || []).map(line => `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div>
                            <div class="lsn-es">${esc(line.es || line.text)}</div>
                            ${line.en ? `<div class="lsn-en">${esc(line.en)}</div>` : ''}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    },

    story(step) {
        // Same tap-a-word-to-translate interaction as the Library reader —
        // story files usually carry target-language text only, but a line's
        // own `lang`, when present, overrides the course language (see
        // Reader.renderStory's matching comment): Hungarian's A1 unit
        // stories deliberately narrate in English while dialogue stays in
        // Hungarian, and tapping/hearing that English narration as if it
        // were Hungarian would be actively wrong, not just unhelpful.
        const isTargetLanguage = line => !line.lang || line.lang === Lang.code();
        const clickable = text => (typeof Reader !== 'undefined') ? Reader.makeClickable(text) : esc(text);
        const body = line => isTargetLanguage(line) ? clickable(line.text) : esc(line.text);
        const voices = step.characterVoices || ((typeof Reader !== 'undefined' && typeof Reader.assignCharacterVoices === 'function')
            ? Reader.assignCharacterVoices({ characters: step.characters || [], paragraphs: step.lines || [] })
            : {});
        const genders = step.characterGenders || (voices && voices._genders) || {};
        const speech = line => {
            if (!isTargetLanguage(line)) return '';
            const spk = line.speaker;
            const isNarrator = !spk || spk === 'Narrator';
            const charVoice = isNarrator ? undefined : voices[spk];
            const charGender = isNarrator ? undefined : genders[spk];
            return say(line.text, {
                type: 'story',
                character: charVoice,
                gender: charGender
            });
        };
        return `
            <p class="lsn-hint">It's okay if you don't understand every word — this is here to get you used to
                natural ${esc(Lang.name())}, not another test sentence. Read for the general idea; a few questions follow.</p>
            <div class="lsn-story" id="story-body">
                ${(step.lines || []).map(line => line.type === 'dialogue' ? `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div class="lsn-es">${body(line)}${speech(line)}</div>
                    </div>
                ` : `
                    <p class="lsn-narration">${body(line)}${speech(line)}</p>
                `).join('')}
            </div>
        `;
    },

    'multiple-choice'(step) {
        gateStep();
        const pick = shuffledOptions(step.options, step.correct);
        stepState.correct = pick.correct;
        stepState.checkFn = 'lessonCheckChoice';
        const isMulti = Array.isArray(step.correct) && step.correct.length > 1;
        const multiHint = isMulti && !/more than one|multiple|either|any of|which two/i.test(step.question || '')
            ? `<p class="lsn-multi-hint">(More than one answer is acceptable — pick any)</p>`
            : '';
        return `
            <p class="lsn-question">${escMd(step.question)}</p>
            ${multiHint}
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})"><span class="lsn-key-hint">${i + 1}</span><span class="lsn-option-text">${escMd(option)}</span></button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    'dialogue-complete'(step) {
        gateStep();
        const pick = shuffledOptions(step.options, step.correct);
        stepState.correct = pick.correct;
        stepState.checkFn = 'lessonCheckChoice';
        const isMulti = Array.isArray(step.correct) && step.correct.length > 1;
        return `
            <div class="lsn-dialogue">
                ${(step.prompt || []).map(line => `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div class="lsn-es">${escMd(line.text)}</div>
                    </div>
                `).join('')}
            </div>
            <p class="lsn-question">Choose the missing line:${isMulti ? ' <span class="lsn-multi-hint">(more than one answer is acceptable — pick any)</span>' : ''}</p>
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})"><span class="lsn-key-hint">${i + 1}</span><span class="lsn-option-text">${escMd(option)}</span></button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    // Audio in place of visible Spanish — hearing it is the exercise, so
    // unlike the small inline `say()` icon this is the primary control.
    'listening-choice'(step) {
        gateStep();
        const pick = shuffledOptions(step.options, step.correct);
        stepState.correct = pick.correct;
        stepState.audio = step.sentence;
        stepState.checkFn = 'lessonCheckChoice';
        return `
            <p class="lsn-question">Listen and choose what it means.</p>
            <div class="lsn-listen">
                <button class="lsn-play" onclick="lessonPlayAudio()" aria-label="Play audio">${Art.icon('listening')} Play</button>
                ${(typeof ParlourTTS === 'undefined' || !ParlourTTS.available())
                    ? `<p class="lsn-hint">No audio available right now — you can still answer after 3 tries.</p>` : ''}
            </div>
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})"><span class="lsn-key-hint">${i + 1}</span><span class="lsn-option-text">${escMd(option)}</span></button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    // Same audio control as listening-choice; checked exactly like fill-blank
    // (lessonCheckBlank), since the whole sentence is the answer.
    dictation(step) {
        gateStep();
        stepState.answer = step.sentence;
        stepState.audio = step.sentence;
        stepState.translation = step.english || step.translation || '';
        stepState.checkFn = 'lessonCheckBlank';
        return `
            <p class="lsn-question">Listen and type or speak what you hear.</p>
            <div class="lsn-listen">
                <button class="lsn-play" onclick="lessonPlayAudio()" aria-label="Play audio">${Art.icon('listening')} Play</button>
                ${(typeof ParlourTTS === 'undefined' || !ParlourTTS.available())
                    ? `<p class="lsn-hint">No audio available right now — you can still answer after 3 tries.</p>` : ''}
            </div>
            <div class="lsn-input-with-mic">
                <input id="blank-input" class="lsn-input" type="text" placeholder="Type or speak what you hear" autocomplete="off" autocapitalize="off" spellcheck="false">
                <button type="button" class="lsn-mic-addon" onclick="lessonInlineVoiceInput('#blank-input', this)" aria-label="Speak to type" title="Speak to type">
                    ${typeof Art !== 'undefined' ? Art.icon('mic') : ''}
                </button>
            </div>
            ${typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('#blank-input') : ''}
            ${feedbackHtml()}
        `;
    },

    matching(step) {
        gateStep();
        const pairs = step.pairs || [];
        stepState.pairs = pairs;
        stepState.matched = 0;
        stepState.pick = null;
        return `
            <p class="lsn-question">Tap a ${esc(Lang.name())} word, then its translation.</p>
            <div class="lsn-match">
                <div class="lsn-match-col">
                    ${shuffled(pairs.map((p, i) => ({ text: p[0], i }))).map(item => `
                        <button class="lsn-option" data-side="left" data-index="${item.i}"
                            onclick="lessonMatch(this)">${esc(item.text)}</button>
                    `).join('')}
                </div>
                <div class="lsn-match-col">
                    ${shuffled(pairs.map((p, i) => ({ text: p[1], i }))).map(item => `
                        <button class="lsn-option" data-side="right" data-index="${item.i}"
                            onclick="lessonMatch(this)">${esc(item.text)}</button>
                    `).join('')}
                </div>
            </div>
            ${feedbackHtml()}
        `;
    },

    'fill-blank'(step) {
        gateStep();
        stepState.answer = step.answer || (step.answers && step.answers[0]) || '';
        stepState.acceptable = step.answers || [step.answer];
        stepState.translation = step.english || step.translation || '';
        stepState.checkFn = 'lessonCheckBlank';
        return `
            <p class="lsn-question">${escMd(step.sentence).replace(/_{2,}/, '<span class="lsn-blank">?</span>')}</p>
            <div class="lsn-input-with-mic">
                <input id="blank-input" class="lsn-input" type="text" placeholder="Type or speak the missing word" autocomplete="off" autocapitalize="off" spellcheck="false">
                <button type="button" class="lsn-mic-addon" onclick="lessonInlineVoiceInput('#blank-input', this)" aria-label="Speak to type" title="Speak to type">
                    ${typeof Art !== 'undefined' ? Art.icon('mic') : ''}
                </button>
            </div>
            ${typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('#blank-input') : ''}
            ${feedbackHtml()}
        `;
    },

    'sentence-builder'(step) {
        gateStep();
        // A few sentences have two clauses joined by "y"/"pero" with no
        // grammatical reason to prefer one order over the other (e.g. "dos
        // manzanas y una botella de agua" vs. the clauses swapped) — content
        // can list every acceptable tile order in `solutions` instead of one
        // fixed `solution`. stepState.solution stays the single canonical
        // one shown on reveal; stepState.solutions is the full accepted set.
        stepState.solutions = step.solutions || [step.solution || []];
        stepState.solution = stepState.solutions[0];
        stepState.english = step.english || '';
        stepState.checkFn = 'lessonCheckBuild';

        // Tiles are stored with their file index and shuffled once. The index
        // is what the two rows exchange, not the text — a sentence with the
        // same word twice ("la casa de la madre") has two distinct tiles, and
        // matching on text would take back whichever came first.
        stepState.tiles = shuffled((step.tiles || []).map((text, i) => ({ text, i })));
        stepState.built = [];

        return `
            <p class="lsn-question">Build the sentence.</p>
            <div id="build-target" class="lsn-target">${buildTargetHtml()}</div>
            <div id="build-bank" class="lsn-options lsn-tiles">${buildBankHtml()}</div>
            ${feedbackHtml()}
        `;
    },

    'sentence-order'(step) {
        gateStep();
        stepState.solution = step.solution || [];
        stepState.sentences = step.sentences || [];
        stepState.order = [];
        stepState.checkFn = 'lessonCheckOrder';
        return `
            <p class="lsn-question">Tap the sentences in the right order.</p>
            <div class="lsn-options">
                ${shuffled((step.sentences || []).map((text, i) => ({ text, i }))).map(item => `
                    <button class="lsn-option" data-index="${item.i}"
                        onclick="lessonPickOrder(this)">${esc(item.text)}</button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    'structured-writing'(step) {
        // Free writing can't be marked right or wrong, so instead of grading
        // it we show a model answer once every line is written and let the
        // learner compare. Continue unlocks on that comparison.
        gateStep();
        stepState.isComposition = !step.template || !step.template.length;
        stepState.lines = (step.template || []).map(line =>
            typeof line === 'string' ? { prompt: line, answer: '' } : line);
        stepState.minWords = step.minWords || ((currentLesson && currentLesson.level && (currentLesson.level.startsWith('B') || currentLesson.level.startsWith('C'))) ? 15 : 6);
        stepState.checkFn = 'lessonRevealWriting';
        stepState.checkDisabled = true;

        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';

        if (stepState.isComposition) {
            // Tier 3 / Open multi-sentence composition prompt
            const cues = step.cues || step.points || [];
            const prompt = step.prompt || step.instruction || 'Write a short text in ' + langName + '.';
            const scenario = step.scenario || step.situation || '';
            const modelAnswer = step.model || step.answer || '';

            return `
                <p class="lsn-question">Write in ${esc(langName)}.</p>
                <div class="sp-lesson-card" style="padding:14px; border:1px solid var(--border); border-radius:8px; margin-bottom:12px; background:var(--surface);">
                    ${scenario ? `<p style="font-size:0.92rem; color:var(--text-muted); margin:0 0 6px 0; font-style:italic;">${esc(scenario)}</p>` : ''}
                    <p style="font-size:1.15rem; font-weight:700; color:var(--text-heading); margin:0 0 8px 0;">${esc(prompt)}</p>
                    ${cues.length ? `
                        <div style="background:rgba(0,0,0,0.03); border-radius:6px; padding:8px 12px; margin-top:8px;">
                            <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:700; color:var(--text-muted);">Points to include:</span>
                            <ul style="margin:4px 0 0 0; padding-left:18px; font-size:0.9rem; color:var(--text);">
                                ${cues.map(c => `<li>${esc(c)}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>
                <div class="lsn-composition-wrap" style="margin-bottom:10px;">
                    <textarea class="lsn-input" data-write-composition="1" style="width:100%; min-height:90px; font-size:1rem; padding:10px; border-radius:8px;" placeholder="Write your response in ${esc(langName)}..." oninput="lessonCheckWriting()"></textarea>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span id="lsn-comp-wordcount" style="font-size:0.8rem; color:var(--text-muted);">0/${stepState.minWords} words</span>
                        ${typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('[data-write-composition]') : ''}
                    </div>
                </div>
                ${modelAnswer ? `
                    <div class="lsn-model hidden" data-model="comp" style="margin-top:12px; padding:12px; border-radius:8px; background:rgba(0,0,0,0.04);">
                        <span class="lsn-model-label" style="display:block; margin-bottom:4px; font-weight:700;">Example Model Text</span>
                        <span class="lsn-es" style="font-size:0.95rem; line-height:1.4;">${esc(modelAnswer)}</span>
                    </div>
                ` : ''}
                <div class="lsn-writing-feedback hidden" id="lsn-writing-feedback">
                    ${(typeof navigator === 'undefined' || navigator.onLine) ? `
                        <button type="button" class="dk-secondary" onclick="lessonGetWritingFeedback()">Get coach feedback</button>
                    ` : ''}
                    <div id="lsn-writing-feedback-result"></div>
                </div>
                ${feedbackHtml()}
            `;
        }

        return `
            <p class="lsn-question">Complete each line in ${esc(langName)}.</p>
            ${typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('.lsn-input') : ''}
            ${stepState.lines.map((line, i) => `
                <div class="lsn-write-row">
                    <div class="lsn-en">${esc(line.prompt)}</div>
                    <input class="lsn-input" type="text" placeholder="Your sentence"
                        data-write="${i}" oninput="lessonCheckWriting()" autocomplete="off" autocapitalize="off" spellcheck="false">
                    ${line.answer ? `
                        <div class="lsn-model" data-model="${i}">
                            <span class="lsn-model-label">One way to say it</span>
                            <span class="lsn-es">${esc(line.answer)}</span>
                        </div>
                    ` : ''}
                </div>
            `).join('')}
            <p class="lsn-hint">There is more than one right answer. Write every line, then compare yours with the examples.</p>
            <div class="lsn-writing-feedback hidden" id="lsn-writing-feedback">
                ${(typeof navigator === 'undefined' || navigator.onLine) ? `
                    <button type="button" class="dk-secondary" onclick="lessonGetWritingFeedback()">Get coach feedback</button>
                ` : ''}
                <div id="lsn-writing-feedback-result"></div>
            </div>
            ${feedbackHtml()}
        `;
    },

    // A "swap one word into the sentence" pattern drill (Hungarian's case
    // suffixes mean the swapped-in word is rarely just dropped in bare —
    // "kenyeret" -> "tejet", not "tej" — so content supplies each option's
    // ALREADY-inflected form and full resulting sentence rather than this
    // renderer trying to inflect anything itself; see the "why" comment on
    // highlightWord() below for the same reasoning applied to display).
    // No right/wrong to grade, same as structured-writing — tapping each
    // option reveals what the sentence becomes; Continue unlocks once every
    // option has been seen.
    substitution(step) {
        gateStep();
        stepState.options = step.options || [];
        stepState.viewed = new Set();
        return `
            <p class="lsn-question">See how the sentence changes.</p>
            <p class="lsn-sub-base">${highlightWord(step.base_sentence, step.base_word)}</p>
            ${step.base_gloss ? `<p class="lsn-hint">${esc(step.base_gloss)}</p>` : ''}
            ${stepState.options.map((opt, i) => `
                <div class="lsn-write-row">
                    <button class="lsn-option" data-sub-index="${i}" onclick="lessonRevealSub(${i})">
                        ${esc(opt.word)}${opt.gloss ? ' <span class="lsn-hint">(' + esc(opt.gloss) + ')</span>' : ''}
                    </button>
                    <div class="lsn-model" id="sub-result-${i}">
                        <span class="lsn-model-label">Becomes</span>
                        <span class="lsn-es"></span>
                    </div>
                </div>
            `).join('')}
            ${feedbackHtml()}
        `;
    },

    speaking(step) {
        gateStep();
        stepState.target = step.sentence || step.spanish || '';
        stepState.english = step.english || step.translation || '';
        stepState.mode = step.mode || 'read-repeat';
        stepState.checkFn = 'lessonCheckSpeaking';
        // Disabled until a recording produces a transcript, otherwise the
        // Check button is tappable (checkDisabled is falsy by default) the
        // instant the step renders, before the learner has spoken at all.
        stepState.checkDisabled = true;

        const isSnoozed = typeof SpeechInput !== 'undefined' && SpeechInput.isCantSpeakNow();
        if (isSnoozed) {
            // renderStep() calls updateFooterButton() right after this
            // renderer returns, so setting the flag here is enough.
            stepState.checkDisabled = false;
        }

        const isPromptSpeak = stepState.mode === 'prompt-speak';
        const target = stepState.target;
        const english = stepState.english;
        const safeTarget = esc(target).replace(/'/g, "\\'");
        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';
        let questionPrompt = step.prompt || (isPromptSpeak ? `Translate and say this out loud in ${langName}:` : `Listen and repeat this out loud in ${langName}:`);
        if (typeof Lang !== 'undefined' && !Lang.code().startsWith('es')) {
            questionPrompt = questionPrompt.replace(/in Spanish/gi, `in ${langName}`);
        }

        return `
            <p class="lsn-question">${esc(questionPrompt)}</p>
            ${isSnoozed ? `
                <div class="sp-snoozed-banner" style="background:var(--surface); border:1px dashed var(--border); padding:10px 14px; margin-bottom:14px; display:flex; align-items:center; justify-content:space-between; gap:10px;">
                    <span style="font-size:0.88rem; color:var(--text-muted, #687787);">Speaking practice is currently snoozed.</span>
                    <button type="button" class="btn-secondary" onclick="lessonResumeSpeaking()" style="padding:4px 10px; font-size:0.82rem;">Turn on</button>
                </div>
            ` : ''}
            <div class="sp-lesson-card">
                ${isPromptSpeak ? `
                    <p class="sp-en-prompt" style="font-size:1.3rem; font-weight:700; margin:0 0 6px 0;">${esc(english)}</p>
                    <p class="sp-instruction">Say the translation in ${esc(langName)}</p>
                    <div id="sp-prompt-target-reveal" class="hidden" style="margin-top:14px; padding-top:12px; border-top:1px solid var(--border);">
                        <div class="sp-target-lead">
                            <p class="sp-es-text">${esc(target)}</p>
                            <button type="button" class="sp-listen-btn" onclick="ParlourTTS.speak({text: '${safeTarget}', type: 'pronunciation'})" aria-label="Listen">
                                ${typeof Art !== 'undefined' ? Art.icon('listening') : ''} Listen
                            </button>
                        </div>
                    </div>
                ` : `
                    <div class="sp-target-lead">
                        <p class="sp-es-text">${esc(target)}</p>
                        <button type="button" class="sp-listen-btn" onclick="ParlourTTS.speak({text: '${safeTarget}', type: 'pronunciation'})" aria-label="Listen">
                            ${typeof Art !== 'undefined' ? Art.icon('listening') : ''} Listen
                        </button>
                    </div>
                    ${english ? `<p class="sp-en-sub">${esc(english)}</p>` : ''}
                `}
            </div>
            <div class="sp-mic-section">
                <button type="button" class="sp-mic-btn" id="lesson-mic-btn" onclick="lessonToggleSpeaking(this)" aria-label="Record speech">
                    <span class="sp-mic-icon-wrap">${typeof Art !== 'undefined' ? Art.icon('speaking') : ''}</span>
                </button>
                <span class="sp-mic-status" id="lesson-mic-status">Tap to speak</span>
                <div class="sp-live-transcript hidden" id="lesson-live-transcript" aria-live="polite"></div>
            </div>
            <div class="sp-reveal hidden" id="lesson-sp-reveal"></div>
            ${feedbackHtml()}
            <div style="text-align: center; margin-top: 12px;">
                <button type="button" class="sp-cant-speak-btn" onclick="lessonSkipSpeaking()">Can't speak right now</button>
            </div>
        `;
    },

    // Every word the lesson taught, each sorted into review or known — never
    // silently. Defaulting an unresolved choice to "known" would let one fast
    // click through a lesson quietly mark words the learner hasn't actually
    // learned, so every fresh word starts on "Review" and only moves to
    // "Know it" on a deliberate tap. Words already settled one way or the
    // other (already reviewing, or already in My Dictionary) show as a
    // plain fact instead of a choice — there's nothing left to decide.
    srs(step) {
        stepState.cards = step.cards || [];
        const inDeck = lemma => typeof srsDeck !== 'undefined'
            && srsDeck.some(card => card.spanish === lemma);
        const known = lemma => typeof isKnown === 'function' && isKnown(lemma);

        stepState.srsChoices = {};
        stepState.cards.forEach((card, i) => {
            if (!inDeck(card.lemma) && !known(card.lemma)) stepState.srsChoices[i] = 'review';
        });

        return `
            <p class="lsn-question">For each word: keep reviewing it, or mark it as one you already know.</p>
            <div class="lsn-vocab">
                ${stepState.cards.map((card, i) => {
                    const settled = inDeck(card.lemma) ? 'already reviewing'
                        : known(card.lemma) ? 'already known' : null;
                    return `
                    <div class="lsn-vocab-row lsn-srs-row">
                        <div>
                            <div class="lsn-es">${esc(card.lemma)}</div>
                            <div class="lsn-pos">${esc(card.pos)}</div>
                        </div>
                        <div class="lsn-en">${esc(card.translation)}</div>
                        ${settled ? `<span class="lsn-srs-badge">${settled}</span>` : `
                            <div class="lsn-srs-toggle" role="group">
                                <button type="button" class="lsn-srs-opt is-selected"
                                    data-srs-choice="${i}" data-srs-value="review"
                                    onclick="lessonSetSrsChoice(${i}, 'review')">Review</button>
                                <button type="button" class="lsn-srs-opt"
                                    data-srs-choice="${i}" data-srs-value="known"
                                    onclick="lessonSetSrsChoice(${i}, 'known')">Know it</button>
                            </div>
                        `}
                    </div>
                `;
                }).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    challenge(step) {
        gateStep();
        stepState.target = step.target || step.sentence || '';
        stepState.prompt = step.prompt || '';
        stepState.scenario = step.scenario || '';
        stepState.cues = step.cues || [];
        stepState.tier = step.tier || ((step.level === 'A1') ? 'tier1' : (step.level === 'A2') ? 'tier2' : 'tier3');
        stepState.canDo = step.canDo || '';
        stepState.checkFn = 'lessonCheckChallenge';
        stepState.checkDisabled = true;

        const isSnoozed = typeof SpeechInput !== 'undefined' && SpeechInput.isCantSpeakNow();
        if (isSnoozed) {
            stepState.checkDisabled = false;
        }

        const tierBadge = stepState.tier === 'tier1' ? 'Tier 1 • Guided Practice' : stepState.tier === 'tier2' ? 'Tier 2 • Situational Task' : 'Tier 3 • Extended Production';
        const level = step.level || 'A1';
        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';

        return `
            <div class="sp-challenge-header" style="margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
                <span class="cando-badge cando-badge-verified" style="font-size:0.75rem; padding:4px 8px; border-radius:4px; font-weight:700;">CEFR ${esc(level)} • ${esc(tierBadge)}</span>
                ${stepState.canDo ? `<span style="font-size:0.82rem; color:var(--text-muted); font-style:italic;">Target: "${esc(stepState.canDo)}"</span>` : ''}
            </div>

            ${isSnoozed ? `
                <div class="sp-snoozed-banner" style="background:var(--surface); border:1px dashed var(--border); padding:10px 14px; margin-bottom:14px; display:flex; align-items:center; justify-content:space-between; gap:10px;">
                    <span style="font-size:0.88rem; color:var(--text-muted, #687787);">Speaking practice is currently snoozed. You can type your answer below.</span>
                    <button type="button" class="btn-secondary" onclick="lessonResumeSpeaking()" style="padding:4px 10px; font-size:0.82rem;">Turn mic on</button>
                </div>
            ` : ''}

            <div class="sp-lesson-card" style="padding:16px; border:1px solid var(--border); border-radius:10px; background:var(--card-bg, var(--surface));">
                ${stepState.scenario ? `<p style="font-size:0.95rem; color:var(--text-muted); margin:0 0 8px 0; font-style:italic;">${esc(stepState.scenario)}</p>` : ''}
                <p style="font-size:1.2rem; font-weight:700; color:var(--text-heading); margin:0 0 10px 0; line-height:1.35;">${esc(stepState.prompt)}</p>

                ${stepState.cues && stepState.cues.length ? `
                    <div style="background:rgba(0,0,0,0.03); border-radius:6px; padding:10px 14px; margin-top:10px;">
                        <span style="font-size:0.78rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:700; color:var(--text-muted);">Points to include:</span>
                        <ul style="margin:6px 0 0 0; padding-left:20px; font-size:0.92rem; color:var(--text);">
                            ${stepState.cues.map(c => `<li style="margin-bottom:4px;">${esc(c)}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
            </div>

            <div class="sp-mic-section" style="margin-top:16px;">
                <button type="button" class="sp-mic-btn" id="lesson-mic-btn" onclick="lessonToggleSpeaking(this)" aria-label="Record speech">
                    <span class="sp-mic-icon-wrap">${typeof Art !== 'undefined' ? Art.icon('speaking') : ''}</span>
                </button>
                <span class="sp-mic-status" id="lesson-mic-status">Tap to speak</span>
                <div class="sp-live-transcript hidden" id="lesson-live-transcript" aria-live="polite"></div>
            </div>

            <div class="sp-challenge-alt-input" style="margin-top:12px; text-align:center;">
                <details style="display:inline-block; text-align:left; font-size:0.85rem; color:var(--text-muted);">
                    <summary style="cursor:pointer; user-select:none;">Or type your response</summary>
                    <div style="margin-top:8px;">
                        <textarea id="lesson-challenge-input" class="lsn-input" style="width:100%; min-height:60px; font-size:0.95rem; padding:8px; border-radius:6px;" placeholder="Type your response in ${esc(langName)}..." oninput="stepState.checkDisabled = false; updateFooterButton();"></textarea>
                    </div>
                </details>
            </div>

            <div class="sp-reveal hidden" id="lesson-challenge-reveal" style="margin-top:14px;"></div>
            ${feedbackHtml()}
            <div style="text-align: center; margin-top: 12px;">
                <button type="button" class="sp-cant-speak-btn" onclick="lessonSkipSpeaking()">Can't speak right now</button>
            </div>
        `;
    },

    checklist(step) {
        const store = (typeof LearnerModel !== 'undefined' && typeof LearnerModel.allCompetencies === 'function')
            ? LearnerModel.allCompetencies() : {};
        return `
            <div class="lsn-checklist">
                ${(step.items || []).map((item, i) => {
                    const rec = store[item];
                    const isVerified = rec && (rec.state === 'verified');
                    return `
                        <label class="lsn-check-item" style="display:flex; align-items:center; justify-content:space-between; gap:10px;">
                            <span style="display:flex; align-items:center; gap:8px;">
                                <input type="checkbox" data-check="${i}" ${isVerified || (rec && rec.checked) ? 'checked' : ''}>
                                <span>${esc(item)}</span>
                            </span>
                            ${isVerified ? `
                                <span class="cando-badge cando-badge-verified" style="font-size:0.75rem; white-space:nowrap; display:inline-flex; align-items:center; gap:4px;">
                                    ✓ Verified
                                </span>
                            ` : ''}
                        </label>
                    `;
                }).join('')}
            </div>
        `;
    }
};

// ============================================
// STEP RENDERING
// ============================================
// Enter submits whatever's on screen, so a keyboard user never has to reach
// for the footer button. #lesson-content itself survives every step's
// re-render (only its innerHTML changes), so this is wired once rather than
// per step. Two targets matter: a text input's Enter would otherwise do
// nothing, and an answer button's Enter would otherwise just re-fire its own
// select — both get redirected to the footer button instead, whatever it
// currently does (Check or Continue). Everything else (Reset, checkboxes)
// already does the right thing on Enter natively, so this leaves those alone.
function _wireLessonEnterToCheck() {
    if (window._lessonKeyboardWired) return;
    window._lessonKeyboardWired = true;

    window.addEventListener('keydown', e => {
        const lessonScreen = document.getElementById('lesson-screen');
        if (!lessonScreen || lessonScreen.classList.contains('hidden')) return;

        const target = e.target;
        const isTextInput = target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable);

        // 1. Enter key: triggers footer button (Check or Continue)
        if (e.key === 'Enter') {
            const btn = document.getElementById('lesson-next-btn');
            if (btn && !btn.disabled) {
                e.preventDefault();
                btn.click();
            }
            return;
        }

        // Never intercept keyboard shortcuts when the user is actively typing in a text field
        if (isTextInput) return;

        // 2. Hotkeys '1' - '4' (and Numpad 1 - 4): select multiple choice / dialogue options
        let digit = null;
        if (e.key >= '1' && e.key <= '4') {
            digit = parseInt(e.key, 10);
        } else if (e.code && e.code.startsWith('Numpad') && e.code.length === 7) {
            const val = parseInt(e.code.replace('Numpad', ''), 10);
            if (val >= 1 && val <= 4) digit = val;
        }

        if (digit !== null) {
            const container = document.getElementById('lesson-content');
            if (container) {
                const options = container.querySelectorAll('.lsn-options .lsn-option:not([disabled])');
                if (options && options.length >= digit) {
                    e.preventDefault();
                    options[digit - 1].click();
                    return;
                }
            }
        }

        // 3. Audio replay hotkey: 'p' or 'r'
        if (e.key === 'p' || e.key === 'P' || e.key === 'r' || e.key === 'R') {
            const container = document.getElementById('lesson-content');
            const playBtn = container ? container.querySelector('.lsn-play') : null;
            if (playBtn) {
                e.preventDefault();
                playBtn.click();
                return;
            }
        }
    });
}

function renderStep() {
    if (_inlineVoiceActive || _lessonSpeakingRecording) {
        _inlineVoiceActive = false;
        _lessonSpeakingRecording = false;
        if (typeof SpeechInput !== 'undefined') SpeechInput.stopListening();
    }

    const step = currentLesson.steps[currentStepIndex];
    const container = document.getElementById('lesson-content');

    _wireLessonEnterToCheck();
    stepState = { sourceStep: step };

    let html = lessonProgressHtml();
    html += `<h3 class="lsn-title">${esc(step.title || '')}</h3>`;

    // Legacy lessons (embedded HTML)
    if (step.html) {
        html += step.html;
    }
    // Structured JSON lessons
    else if (stepRenderers[step.type]) {
        html += stepRenderers[step.type](step);
    }
    else {
        html += `<p style="color:red;">Unknown step type: ${esc(step.type)}</p>`;
    }

    container.innerHTML = html;
    const scrollParent = container.closest('.content') || document.querySelector('.content');
    if (scrollParent) scrollParent.scrollTop = 0;
    else window.scrollTo(0, 0);

    if (typeof updateReaderWordColors === 'function') updateReaderWordColors();

    const backBtn = document.getElementById('lesson-back-btn');
    if (backBtn) backBtn.disabled = currentStepIndex === 0;

    updateFooterButton();
}

function nextLessonStep() {
    if (stepState.gated && !stepState.solved) return;

    _inlineVoiceActive = false;
    _lessonSpeakingRecording = false;
    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.stopListening();
    }

    // The srs step used to need its own "Save" tap before Continue did
    // anything useful — easy to miss, since Continue itself was already
    // enabled, so a learner could leave the choices on screen unsaved.
    // Saving here means Continue always commits them.
    if (stepState.sourceStep && stepState.sourceStep.type === 'srs') {
        lessonSaveSrsChoices();
    }
    if (stepState.sourceStep && stepState.sourceStep.type === 'checklist') {
        lessonSaveChecklistChoices();
    }

    currentStepIndex++;

    // "I can do this" / checklist should ALWAYS be the last screen before results.
    // If the next step is the checklist, but we still have missed exercises to remediate,
    // remediate the missed exercises first before presenting the self-evaluation checklist!
    if (currentStepIndex < currentLesson.steps.length) {
        const nextStep = currentLesson.steps[currentStepIndex];
        if (nextStep && nextStep.type === 'checklist' && missedSteps.length > 0) {
            currentLesson.steps.splice(currentStepIndex, 0, missedSteps.shift());
        }
        renderStep();
        return;
    }

    // Reached the end of the regular steps — work through anything missed
    // on its first try before actually finishing, one at a time.
    if (missedSteps.length) {
        currentLesson.steps.push(missedSteps.shift());
        renderStep();
        return;
    }

    finishLesson();
}

// Re-renders the previous step from scratch, same as arriving at it fresh —
// there is no saved answer to restore, so a re-visited exercise is ungraded
// again rather than showing its old solved state. Simple and consistent
// with renderStep() itself, which already treats every step as stateless.
function prevLessonStep() {
    if (currentStepIndex <= 0) return;
    _inlineVoiceActive = false;
    _lessonSpeakingRecording = false;
    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.stopListening();
    }
    currentStepIndex--;
    renderStep();
}

async function finishLesson() {
    // Fixed reward: a long lesson isn't worth more than a short one, and
    // scaling by step count rewarded lesson length rather than learning.
    const firstTime = typeof markLessonComplete === 'function'
        ? markLessonComplete(currentLesson.id)
        : true;

    // Captured before recordLessonCompleted() awards this lesson's XP, so
    // the summary can tell whether finishing THIS lesson is what pushed
    // the rank over a threshold — recordLessonCompleted() already updates
    // the shared xpData by the time renderLessonSummary() reads it.
    const rankBefore = (typeof getRank === 'function') ? getRank().rank : null;

    if (typeof recordLessonCompleted === 'function') {
        recordLessonCompleted(firstTime);
    }

    await renderLessonSummary(firstTime, rankBefore);
}

// Which of My Journey's milestones this exact completion just crossed —
// checked once, right after progress/XP are already updated for this
// lesson, so Journey.collect() reflects it. A milestone only ever shows up
// here once: a small seen-set (same Lang.key() pattern used elsewhere)
// remembers which have already been shown, so re-completing a lesson or
// simply visiting Journey later never re-announces the same one.
function milestonesSeenKey() {
    return Lang.key('milestonesSeen');
}

function newlyReachedMilestones() {
    if (typeof Journey === 'undefined') return [];

    const d = Journey.collect();
    let seen = [];
    try { seen = JSON.parse(localStorage.getItem(milestonesSeenKey()) || '[]'); }
    catch (error) { seen = []; }

    const reached = Journey.MILESTONES.filter(m => m.test(d) && !seen.includes(m.id));
    if (reached.length) {
        try {
            localStorage.setItem(milestonesSeenKey(), JSON.stringify(seen.concat(reached.map(m => m.id))));
        } catch (error) {
            // Private browsing with storage disabled — the milestone still
            // shows this once, it just risks showing again next time.
        }
    }
    return reached;
}

// "Unit 1 · Lesson 1.5" — the same within-unit numbering the unit's own
// lesson list uses (see lessonRowsHtml() in curriculum.js: unitLabel +
// "." + position), so a lesson reads as the same step in both places
// rather than acquiring a second numbering scheme just for this screen.
// Returns null if the curriculum index isn't loaded or the lesson isn't
// in it (e.g. the level test) — the summary screen just omits the line.
function lessonNumberLabel() {
    if (!currentLesson || !currentLesson.id) return null;

    const data = window._curriculumData;
    const level = data && data.levels && data.levels[currentLesson.level];
    if (!level) return null;

    const unit = (level.units || []).find(u =>
        (u.lessons || []).some(l => l.id === currentLesson.id));
    if (!unit) return null;

    const position = unit.lessons.findIndex(l => l.id === currentLesson.id) + 1;
    return `Unit ${unit.label} · Lesson ${unit.label}.${position}`;
}

// The general form of lessonNumberLabel() above — works for any lesson id,
// not just the one currently open — for the Tier 2 cross-links (Reader's
// word-tap popup, Decks' word-list rows) pointing a word back to the
// lesson word-lesson-index.json says taught it. Searches every level since
// the caller only has a lesson id, not which level it's in; returns null
// (not a guess) when the curriculum index isn't loaded yet or the id
// isn't in it.
function lessonLabelFor(lessonId) {
    const data = window._curriculumData;
    if (!data || !data.levels || !lessonId) return null;

    for (const levelKey of Object.keys(data.levels)) {
        const units = (data.levels[levelKey].units || []);
        const unit = units.find(u => (u.lessons || []).some(l => l.id === lessonId));
        if (!unit) continue;

        const position = unit.lessons.findIndex(l => l.id === lessonId) + 1;
        const lesson = unit.lessons[position - 1];
        return {
            lessonId,
            label: `Unit ${unit.label} · Lesson ${unit.label}.${position}`,
            title: lesson.title || ''
        };
    }
    return null;
}

// "4 min" rather than "4m 12s" — a learner checking how long a lesson took
// wants a rough sense of it, not a stopwatch reading. Anything under a
// minute still says "1 min" rather than "0 min", since "you took no time"
// reads as broken, not as a compliment.
function formatLessonElapsed(ms) {
    const totalMinutes = Math.max(1, Math.round(ms / 60000));
    if (totalMinutes < 60) return `${totalMinutes} min`;
    const hours = Math.floor(totalMinutes / 60);
    const minutes = totalMinutes % 60;
    return minutes ? `${hours} hr ${minutes} min` : `${hours} hr`;
}

// The words this lesson taught, ready to hand straight to Decks — same
// shape openBulkAddPicker() already expects (lemma/translation/pos), same
// source the Word Bank's own per-word add button reads from, just
// collected as a whole lesson instead of a whole unit.
function summaryWordsHtml(words) {
    if (!words.length) return '';
    return `
        <div class="lsn-summary-words">
            <p class="lsn-summary-words-label">${words.length} new ${words.length === 1 ? 'word' : 'words'}</p>
        </div>
    `;
}

// "Quick Reinforce" — a short Workshop session (same driller engines, no
// settings screen, a handful of questions) scoped to exactly what this
// lesson just taught, offered right here rather than only ever reachable
// by navigating to Workshop and picking a skill/word list manually. Two
// independent offers, either or both may be absent: grammarSkill is null
// for a lesson with no grammar-tagged exercises (e.g. a pure-vocabulary
// lesson), and words is empty for a lesson that introduced none. Reuses
// the exact scoping options GrammarDriller/VocabularyDriller already
// understand (see engine/recommend.js and engine/workshop.js's
// "Recommended for you" card) rather than a separate mini-game engine.
const QUICK_REINFORCE_COUNT = 5;

function summaryReinforceHtml(grammarSkill, words, level) {
    const hasVoice = typeof ParlourTTS !== 'undefined' && ParlourTTS.available();
    const hasSpeechInput = (typeof SpeechInput !== 'undefined' && SpeechInput.isSupported()) || hasVoice;

    if (!grammarSkill && !words.length && !hasVoice && !hasSpeechInput) return '';

    return `
        <div class="lsn-summary-reinforce">
            <p class="lsn-summary-reinforce-label">Reinforce what you learned:</p>
            <div class="lsn-summary-reinforce-actions">
                ${grammarSkill ? `
                    <button class="dk-secondary" data-drill-grammar="${esc(grammarSkill)}">
                        Practice in Workshop →
                    </button>
                    <button class="dk-secondary" data-reinforce-grammar="${esc(grammarSkill)}">
                        Quick Grammar (${QUICK_REINFORCE_COUNT} questions)
                    </button>
                ` : ''}
                ${words.length ? `
                    <button class="dk-secondary" data-reinforce-vocab="1">
                        Vocabulary (${words.length} ${words.length === 1 ? 'word' : 'words'})
                    </button>
                ` : ''}
                ${words.length >= 4 && typeof DeckMatch !== 'undefined' ? `
                    <button class="dk-secondary" data-reinforce-match="1" title="Timed matching game with lesson vocabulary">
                        Match Game (${Math.min(words.length, 12)} pairs)
                    </button>
                ` : ''}
                ${hasVoice ? `
                    <button class="dk-secondary" data-reinforce-listening="1" title="Practice listening to spoken sentences">
                        Listening (${QUICK_REINFORCE_COUNT} questions)
                    </button>
                ` : ''}
                ${hasSpeechInput ? `
                    <button class="dk-secondary" data-reinforce-speaking="1" title="Speak sentences out loud">
                        Speaking (${QUICK_REINFORCE_COUNT} sentences)
                    </button>
                ` : ''}
            </div>
        </div>
    `;
}

// A milestone crossed by finishing THIS lesson — rare, so it earns a line
// of its own, but stays plain text rather than reaching for the accent:
// the frontispiece above is already this screen's one accent element (see
// engine/art.js's own rule that the accent never doubles up in one
// composition).
function summaryMilestonesHtml(milestones) {
    if (!milestones.length) return '';
    return milestones.map(m => `<p class="lsn-summary-milestone">Milestone: ${esc(m.label)}</p>`).join('');
}

// Same wording Home's header-streak already uses (updateXPHeader() in
// engine/xp.js) — reused verbatim rather than inventing a second phrasing
// for the same fact. Always shown, even at zero: a blank line here would
// read as "did I lose my streak?", not as "nothing to report."
function summaryStreakLine() {
    if (typeof getStreak !== 'function') return '';
    const streak = getStreak();
    const text = streak > 0 ? `${streak}-day streak` : 'No streak yet';
    return `<p class="lsn-summary-streak">${esc(text)}</p>`;
}

// The screen shown after the last step (and any remediation redo) instead
// of returning straight to whatever tab the lesson was opened from — one
// beat to register the lesson is actually done before moving on. Reuses
// #lesson-content and the footer button rather than a separate overlay, so
// it inherits the same layout the rest of the lesson already has.
//
// firstTime tells apart a real completion from a redo (finishLesson()
// already knows this from markLessonComplete()'s own return value): XP was
// only actually awarded on a first completion, and a milestone (or a rank,
// via rankBefore — see finishLesson()) can only be newly crossed once, so
// all three are skipped on a redo rather than showing a stale or zeroed
// stat. The words-just-learned section isn't gated the same way —
// replaying a lesson to reinforce its vocabulary is a real reason to
// revisit it, and the words taught don't change on a redo.
function summaryGoalsHtml(checklistResults) {
    const list = checklistResults || (
        currentLesson && currentLesson.id && typeof LearnerModel !== 'undefined'
            ? LearnerModel.competenciesForLesson(currentLesson.id)
            : []
    );
    if (!list || !list.length) return '';

    const unverified = list.filter(item => !item.checked || item.state !== 'verified');
    const total = list.length;

    if (unverified.length === 0) {
        return `
            <div class="lsn-summary-goals lsn-summary-goals-achieved">
                <p class="lsn-summary-goals-badge">
                    <span class="lsn-goal-check-icon"><svg class="sp-verified-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span> All ${total} lesson ${total === 1 ? 'goal' : 'goals'} achieved
                </p>
            </div>
        `;
    }

    return `
        <div class="lsn-summary-goals lsn-summary-goals-remediation">
            <p class="lsn-summary-goals-title">Goals to lock down:</p>
            <div class="lsn-summary-goals-list">
                ${unverified.map(item => {
                    const badgeClass = item.state === 'confidence-gap' ? 'lsn-goal-badge-gap' : 'lsn-goal-badge-review';
                    const badgeText = item.state === 'confidence-gap' ? 'Confidence Gap' : 'Needs Practice';
                    return `
                        <div class="lsn-goal-item">
                            <div class="lsn-goal-header">
                                <span class="lsn-goal-text">"${esc(item.text)}"</span>
                                <span class="lsn-goal-badge ${badgeClass}">${badgeText}</span>
                            </div>
                            <div class="lsn-goal-actions">
                                <button type="button" class="dk-secondary lsn-goal-action-btn" data-remediate-practice="${esc(item.text)}">
                                    Quick 3-Question Practice
                                </button>
                                <button type="button" class="dk-secondary lsn-goal-action-btn" data-remediate-speaking="${esc(item.text)}">
                                    Practice in Speaking Studio →
                                </button>
                            </div>
                        </div>
                    `;
                }).join('')}
            </div>
        </div>
    `;
}

// Split into two screens: this one is the celebration/stats recap, the
// second (renderLessonSummaryNext(), reached via its own "Continue")
// carries the "what's next" reinforcement offers. Split rather than one
// long scroll so the result (accuracy, streak, goals) reads as its own
// moment before the app starts asking for more practice.
async function renderLessonSummary(firstTime, rankBefore) {
    const container = document.getElementById('lesson-content');
    if (!container) return;

    // Captured once, up front: currentLesson is a mutable global that
    // teardownLesson() nulls synchronously (e.g. the learner tapping close
    // during the awaits below). Every reference in this function reads
    // `lesson`, not the global, so a teardown mid-render can no longer
    // throw on a null property read partway through.
    const lesson = currentLesson;
    if (!lesson) return;

    if (typeof Sound !== 'undefined') Sound.complete();

    const elapsed = lessonStartTime ? formatLessonElapsed(Date.now() - lessonStartTime) : null;
    const accuracy = lessonStats.total > 0
        ? Math.round((lessonStats.correctFirstTry / lessonStats.total) * 100)
        : null;
    const numberLabel = lessonNumberLabel();
    const xpEarned = (firstTime && typeof GRAMMAR_XP === 'number') ? GRAMMAR_XP : null;

    const words = await collectLessonVocabulary(lesson);
    const grammarSkill = (typeof Recommend !== 'undefined' && lesson.id)
        ? await Recommend.lessonSkillFor(lesson.id)
        : null;
    const milestones = firstTime ? newlyReachedMilestones() : [];
    const rankAfter = (typeof getRank === 'function') ? getRank().rank : null;
    const rankedUp = firstTime && rankBefore != null && rankAfter != null && rankAfter > rankBefore;

    // Reused unchanged by renderLessonSummaryNext() below and by the Match
    // Game's onExit -- computed once here rather than re-awaited on every
    // screen transition or return trip from the embedded mini-game.
    _lessonSummaryCtx = { lesson, words, grammarSkill, firstTime, rankBefore };

    const statsHtml = (accuracy === null && !elapsed && !xpEarned) ? '' : `
        <div class="lsn-summary-stats">
            ${accuracy === null ? '' : `
                <div class="lsn-summary-stat">
                    <div class="jr-big">${accuracy}%</div>
                    <div class="jr-of">accuracy</div>
                </div>
            `}
            ${elapsed ? `
                <div class="lsn-summary-stat">
                    <div class="jr-big">${esc(elapsed)}</div>
                    <div class="jr-of">time</div>
                </div>
            ` : ''}
            ${xpEarned ? `
                <div class="lsn-summary-stat">
                    <div class="jr-big">+${xpEarned}</div>
                    <div class="jr-of">XP</div>
                </div>
            ` : ''}
        </div>
    `;

    container.innerHTML = `
        <div class="lsn-summary">
            <p class="lsn-summary-eyebrow">Lesson complete</p>
            <h2 class="lsn-summary-title">Congratulations!</h2>
            ${numberLabel ? `<p class="lsn-summary-lesson">${esc(numberLabel)} — ${esc(lesson.title || '')}</p>` : ''}
            ${Art.svg('summit', 'lsn-summary-art')}
            ${statsHtml}
            ${summaryStreakLine()}
            ${rankedUp ? `<p class="lsn-summary-milestone">Rank up! You're now Rank ${rankAfter}.</p>` : ''}
            ${summaryMilestonesHtml(milestones)}
            ${summaryGoalsHtml(lastLessonChecklist)}
            ${summaryWordsHtml(words)}
        </div>
    `;
    const summaryScrollParent = container.closest('.content') || document.querySelector('.content');
    if (summaryScrollParent) summaryScrollParent.scrollTop = 0;
    else window.scrollTo(0, 0);

    const remPracticeBtns = container.querySelectorAll('[data-remediate-practice]');
    remPracticeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (grammarSkill) {
                _openReinforce('grammar', { skill: grammarSkill, count: 3 });
            } else if (words && words.length) {
                _openReinforce('vocabulary', { words: words.slice(0, 3) });
            } else {
                _openReinforce('speaking', { count: 3 });
            }
        });
    });

    const remSpeakingBtns = container.querySelectorAll('[data-remediate-speaking]');
    remSpeakingBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const goalText = btn.getAttribute('data-remediate-speaking');
            _openReinforce('speaking', {
                targetCompetency: goalText,
                level: lesson.level || 'A1'
            });
        });
    });

    const addWordsBtn = container.querySelector('[data-add-lesson-words]');
    if (addWordsBtn) {
        addWordsBtn.addEventListener('click', () => {
            if (typeof Decks !== 'undefined') Decks.openBulkAddPicker(words);
        });
    }

    const backBtn = document.getElementById('lesson-back-btn');
    if (backBtn) backBtn.disabled = true;

    const nextBtn = document.getElementById('lesson-next-btn');
    if (nextBtn) {
        nextBtn.textContent = 'Continue →';
        nextBtn.disabled = false;
        nextBtn.classList.remove('is-locked');
        nextBtn.onclick = renderLessonSummaryNext;
    }
}

// Set by renderLessonSummary() just before it renders screen 1; read by
// this function and by the Match Game's onExit so returning from either
// doesn't need to re-await collectLessonVocabulary()/lessonSkillFor() a
// second time for data that hasn't changed.
let _lessonSummaryCtx = null;

// Screen 2 of the lesson-complete flow: the reinforcement offers
// (summaryReinforceHtml, RecommendationEngine's next-action card) that used
// to sit at the bottom of one long summary. "Done" lives here now instead
// of on screen 1, since this is the actual last stop before leaving the
// lesson.
function renderLessonSummaryNext() {
    const container = document.getElementById('lesson-content');
    const ctx = _lessonSummaryCtx;
    if (!container || !ctx) return;
    const { lesson, words, grammarSkill, firstTime, rankBefore } = ctx;

    container.innerHTML = `
        <div class="lsn-summary">
            <p class="lsn-summary-eyebrow">What's next</p>
            ${summaryReinforceHtml(grammarSkill, words, lesson.level)}
        </div>
    `;
    const summaryScrollParent = container.closest('.content') || document.querySelector('.content');
    if (summaryScrollParent) summaryScrollParent.scrollTop = 0;
    else window.scrollTo(0, 0);

    const drillGrammarBtn = container.querySelector('[data-drill-grammar]');
    if (drillGrammarBtn) {
        drillGrammarBtn.addEventListener('click', () => {
            _openReinforce('grammar', { skill: drillGrammarBtn.getAttribute('data-drill-grammar') });
        });
    }

    const reinforceGrammarBtn = container.querySelector('[data-reinforce-grammar]');
    if (reinforceGrammarBtn) {
        reinforceGrammarBtn.addEventListener('click', () => {
            _openReinforce('grammar', { skill: reinforceGrammarBtn.getAttribute('data-reinforce-grammar'), count: QUICK_REINFORCE_COUNT });
        });
    }

    const reinforceVocabBtn = container.querySelector('[data-reinforce-vocab]');
    if (reinforceVocabBtn) {
        reinforceVocabBtn.addEventListener('click', () => {
            _openReinforce('vocabulary', { words: words });
        });
    }

    const reinforceListeningBtn = container.querySelector('[data-reinforce-listening]');
    if (reinforceListeningBtn) {
        reinforceListeningBtn.addEventListener('click', () => {
            _openReinforce('listening', { count: QUICK_REINFORCE_COUNT, autoStart: true, level: lesson.level || null });
        });
    }

    const reinforceSpeakingBtn = container.querySelector('[data-reinforce-speaking]');
    if (reinforceSpeakingBtn) {
        reinforceSpeakingBtn.addEventListener('click', () => {
            _openReinforce('speaking', { count: QUICK_REINFORCE_COUNT, autoStart: true, level: lesson.level || null });
        });
    }

    const reinforceMatchBtn = container.querySelector('[data-reinforce-match]');
    if (reinforceMatchBtn) {
        reinforceMatchBtn.addEventListener('click', () => {
            const footer = document.querySelector('#lesson-screen .lesson-footer');
            if (footer) footer.style.display = 'none';
            const matchCount = Math.min(words.length, 12);
            const matchWords = words.slice(0, matchCount);
            const timeLimit = Math.min(120, matchCount * 8);
            DeckMatch.render(container, {
                words: matchWords,
                deckId: lesson.id || 'lesson-reinforce',
                limit: matchCount,
                timeLimit: timeLimit,
                exitLabel: 'Back to summary',
                onExit: () => {
                    if (footer) footer.style.display = '';
                    renderLessonSummaryNext();
                }
            });
        });
    }

    if (typeof RecommendationEngine !== 'undefined') RecommendationEngine.mountNextAction(container);

    const backBtn = document.getElementById('lesson-back-btn');
    if (backBtn) backBtn.disabled = true;

    const nextBtn = document.getElementById('lesson-next-btn');
    if (nextBtn) {
        nextBtn.textContent = 'Done';
        nextBtn.disabled = false;
        nextBtn.classList.remove('is-locked');
        nextBtn.onclick = closeLesson;
    }
}

// ============================================
// INTERACTION HANDLERS
// ============================================
// Picking an option only marks it selected — grading happens on Check,
// same as every other exercise type (fill-blank, sentence-builder, etc.).
// This used to grade instantly on click, which let a learner lock in an
// answer before ever meaning to commit to it.
function lessonSelectOption(btn, index) {
    if (stepState.solved) return;
    btn.parentElement.querySelectorAll('.lsn-option').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    stepState.picked = index;
}

function lessonCheckChoice() {
    if (stepState.solved) return;
    if (stepState.picked === undefined || stepState.picked === null) {
        setFeedback(false, 'Pick an answer first.');
        return;
    }

    const group = document.querySelectorAll('#lesson-content .lsn-option');
    const btn = group[stepState.picked];
    const isRight = Array.isArray(stepState.correct)
        ? stepState.correct.includes(stepState.picked)
        : stepState.picked === stepState.correct;

    if (isRight) {
        // Blur so the focus ring (still showing from the click that picked
        // this option) doesn't linger over the green correct state.
        if (btn) { btn.classList.add('correct'); btn.blur(); }
        solveStep('✓ Correct!');
        return;
    }

    if (btn) btn.classList.add('wrong');
    if (failStep('✗ Not quite.')) {
        const correctIndexes = Array.isArray(stepState.correct) ? stepState.correct : [stepState.correct];
        correctIndexes.forEach(i => { if (group[i]) group[i].classList.add('correct'); });
        setFeedback(false, 'The answer is highlighted — continue when you are ready.');
    }
}

function lessonMatch(btn) {
    if (btn.classList.contains('correct') || stepState.solved) return;

    if (!stepState.pick) {
        document.querySelectorAll('.lsn-option.selected').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        stepState.pick = btn;
        return;
    }

    if (stepState.pick === btn) {
        btn.classList.remove('selected');
        stepState.pick = null;
        return;
    }

    if (stepState.pick.dataset.side === btn.dataset.side) {
        stepState.pick.classList.remove('selected');
        btn.classList.add('selected');
        stepState.pick = btn;
        return;
    }

    const first = stepState.pick;
    first.classList.remove('selected');
    stepState.pick = null;

    if (first.dataset.index === btn.dataset.index) {
        first.classList.add('correct');
        btn.classList.add('correct');
        stepState.matched++;
        if (stepState.matched === stepState.pairs.length) {
            solveStep('✓ All matched!');
        } else {
            setFeedback(true, '✓ Match! ' + stepState.matched + '/' + stepState.pairs.length);
        }
        return;
    }

    btn.classList.add('wrong');
    setTimeout(() => btn.classList.remove('wrong'), 700);

    if (failStep('✗ Not a match.')) {
        revealMatches();
    }
}

function revealMatches() {
    const grid = document.querySelector('.lsn-match');
    if (grid) {
        grid.insertAdjacentHTML('afterend', revealHtml(
            (stepState.pairs || []).map(pair =>
                `<div><strong>${esc(pair[0])}</strong> — ${esc(pair[1])}</div>`
            ).join('')
        ));
        grid.style.display = 'none';
    }
    stepState.pick = null;
    setFeedback(false, 'Here are the pairs — continue when you are ready.');
}

function lessonCheckBlank() {
    const input = document.getElementById('blank-input');
    if (!input || stepState.solved) return;

    if (!input.value.trim()) {
        setFeedback(false, 'Type or speak an answer first.');
        return;
    }

    // Most blanks have exactly one right answer, but some genuinely accept
    // several (e.g. any of the story's characters completing "Soy ___.") —
    // stepState.acceptable carries the full list, stepState.answer stays the
    // one shown on reveal.
    const acceptable = stepState.acceptable || [stepState.answer];
    const ok = acceptable.some(a => normalise(input.value) === normalise(a));
    input.classList.toggle('correct', ok);
    input.classList.toggle('wrong', !ok);

    const diffContainer = document.getElementById('step-diff');

    if (ok) {
        if (diffContainer) { diffContainer.innerHTML = ''; diffContainer.style.display = 'none'; }
        solveStep('✓ Correct!');
        return;
    }

    const diff = generateAnswerDiff(input.value, acceptable);

    let failMsg = '✗ Try again.';
    if (diff && diff.onlyAccents && diff.accentList.length) {
        failMsg = `✗ Watch your accents (${diff.accentList.join(', ')}).`;
    }

    if (failStep(failMsg)) {
        if (diffContainer) { diffContainer.innerHTML = ''; diffContainer.style.display = 'none'; }
        input.value = stepState.answer;
        input.classList.remove('wrong');
        input.classList.add('correct');
        setFeedback(false, 'The answer was "' + stepState.answer + '" — continue when you are ready.');
    } else {
        if (diffContainer && diff) {
            const label = diff.onlyAccents ? 'Accents:' : 'Check:';
            diffContainer.innerHTML = `<span class="lsn-diff-label">${label}</span> <span class="lsn-diff-content">${diff.html}</span>`;
            diffContainer.style.display = 'flex';
        } else if (diffContainer) {
            diffContainer.innerHTML = '';
            diffContainer.style.display = 'none';
        }
    }
}

function lessonPlayAudio() {
    if (_inlineVoiceActive) {
        _inlineVoiceActive = false;
        if (typeof SpeechInput !== 'undefined') SpeechInput.stopListening();
        const micBtn = document.querySelector('.lsn-mic-addon.is-recording');
        if (micBtn) micBtn.classList.remove('is-recording');
    }
    if (_lessonSpeakingRecording) {
        _lessonSpeakingRecording = false;
        if (typeof SpeechInput !== 'undefined') SpeechInput.stopListening();
        const micBtn = document.getElementById('lesson-mic-btn');
        if (micBtn) micBtn.classList.remove('sp-recording');
        const statusEl = document.getElementById('lesson-mic-status');
        if (statusEl) statusEl.textContent = 'Tap to speak';
    }
    if (typeof ParlourTTS !== 'undefined') ParlourTTS.speak({ text: stepState.audio, type: 'listening' });
}

// ---- Sentence builder ----
// Tiles live in two rows and move freely between them: tap one in the bank to
// put it in the sentence, tap one in the sentence to take it back. A misplaced
// word costs one tap, not a reset of everything built so far.

function tileText(index) {
    const tile = (stepState.tiles || []).find(t => t.i === index);
    return tile ? tile.text : '';
}

// Used tiles stay in place, greyed, rather than being removed: taking a word
// out of the sentence would otherwise reflow the whole bank under the finger
// that is reaching for the next one.
function buildBankHtml() {
    return (stepState.tiles || []).map(tile => {
        const used = stepState.built.includes(tile.i);
        return `<button class="lsn-tile${used ? ' used' : ''}"${used ? ' disabled' : ''}
            onclick="lessonAddTile(${tile.i})">${esc(tile.text)}</button>`;
    }).join('');
}

function buildTargetHtml() {
    if (!stepState.built.length) {
        return '<span class="lsn-target-empty">Tap the words below.</span>';
    }
    return stepState.built.map((tileIndex, position) => `
        <button class="lsn-tile" onclick="lessonRemoveTile(${position})">${esc(tileText(tileIndex))}</button>
    `).join('');
}

function redrawBuild() {
    UI.html('build-target', buildTargetHtml());
    UI.html('build-bank', buildBankHtml());
    setFeedback(true, '');
}

function lessonAddTile(tileIndex) {
    if (stepState.solved || stepState.built.includes(tileIndex)) return;
    stepState.built.push(tileIndex);
    redrawBuild();
}

function lessonRemoveTile(position) {
    if (stepState.solved) return;
    stepState.built.splice(position, 1);
    redrawBuild();
}

// The English is feedback, not a prompt. On screen while the tiles are still
// on the table it turns building a sentence into translating one, so it
// appears only once the sentence is settled — right or wrong.
function revealBuildEnglish() {
    if (!stepState.english || document.getElementById('build-english')) return;
    const target = document.getElementById('build-target');
    if (target) {
        target.insertAdjacentHTML('afterend',
            `<p id="build-english" class="lsn-build-en">${esc(stepState.english)}</p>`);
    }
}

function lessonCheckBuild() {
    if (stepState.solved || !stepState.built.length) return;

    const built = normalise(stepState.built.map(tileText).join(' '));
    const ok = (stepState.solutions || [stepState.solution])
        .some(solution => built === normalise(solution.join(' ')));

    if (ok) {
        UI.html('build-target',
            `<span class="lsn-built is-correct">${esc(stepState.solution.join(' '))}</span>`);
        UI.html('build-bank', '');
        revealBuildEnglish();
        solveStep('✓ Correct!');
        return;
    }

    if (failStep('✗ Not right yet — tap a word in the sentence to take it back.')) {
        UI.html('build-target',
            `<span class="lsn-built is-correct">${esc(stepState.solution.join(' '))}</span>`);
        UI.html('build-bank', '');
        revealBuildEnglish();
        setFeedback(false, 'The sentence is shown above — continue when you are ready.');
    }
}

function lessonPickOrder(btn) {
    if (btn.classList.contains('used') || stepState.solved) return;
    btn.classList.add('used');
    stepState.order.push(Number(btn.dataset.index));
    btn.textContent = stepState.order.length + '. ' + btn.textContent;
}

function lessonCheckOrder() {
    if (stepState.solved) return;

    const ok = stepState.order.length === stepState.solution.length
        && stepState.order.every((v, i) => v === stepState.solution[i]);

    if (ok) {
        solveStep('✓ Correct order!');
        return;
    }

    if (failStep('✗ Not the right order.')) {
        revealOrder();
        return;
    }

    document.querySelectorAll('.lsn-option.used').forEach(b => {
        b.classList.remove('used');
        b.textContent = b.textContent.replace(/^\d+\.\s/, '');
    });
    stepState.order = [];
}

function revealOrder() {
    const list = document.querySelector('.lsn-options');
    if (list) {
        list.insertAdjacentHTML('afterend', revealHtml(
            (stepState.solution || []).map((index, i) =>
                `<div>${i + 1}. ${esc(stepState.sentences[index])}</div>`
            ).join('')
        ));
        list.style.display = 'none';
    }
    setFeedback(false, 'Here is the right order — continue when you are ready.');
}

// Enables the footer Check button once every line has something in it. The
// step is not solved yet — the learner still has to look at the model
// answers.
function lessonCheckWriting() {
    if (stepState.revealed) return;

    if (stepState.isComposition) {
        const textarea = document.querySelector('[data-write-composition]');
        const text = textarea ? textarea.value.trim() : '';
        const words = text ? text.split(/\s+/).filter(Boolean).length : 0;
        const minWords = stepState.minWords || 6;
        const wordCountEl = document.getElementById('lsn-comp-wordcount');
        if (wordCountEl) {
            wordCountEl.textContent = `${words}/${minWords} words`;
            wordCountEl.style.color = words >= minWords ? 'var(--accent, #2b6cb0)' : 'var(--text-muted)';
        }

        const filled = words >= minWords;
        stepState.checkDisabled = !filled;
        updateFooterButton();
        setFeedback(true, filled ? 'Ready — check your composition against the example.' : '');
        return;
    }

    const inputs = Array.prototype.slice.call(document.querySelectorAll('[data-write]'));
    const filled = inputs.length > 0 && inputs.every(input => input.value.trim().length > 0);

    stepState.checkDisabled = !filled;
    updateFooterButton();

    setFeedback(true, filled ? 'Ready — check your answers against the examples.' : '');
}

function lessonRevealWriting() {
    if (stepState.revealed) return;
    stepState.revealed = true;

    document.querySelectorAll('[data-model]').forEach(el => el.classList.remove('hidden'));
    document.querySelectorAll('[data-model]').forEach(el => el.classList.add('is-shown'));

    const feedbackWrap = document.getElementById('lsn-writing-feedback');
    if (feedbackWrap) feedbackWrap.classList.remove('hidden');

    // This step is self-compared, never objectively graded, so there's no
    // real right/wrong here -- but a completed attempt is still evidence
    // the learner used this skill, same as every other teaches-tagged
    // exercise's completion already feeds noteRecycleResult()'s SM-2
    // schedule. This is the same fact reaching LearnerModel too, which
    // that Recycle-only path never did.
    const step = stepState.sourceStep;
    if (step && step.teaches && step.teaches.length && typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
        LearnerModel.recordProduction(step.teaches, true, 100, 'written');
    }

    // Inputs stay editable so the learner can correct their own sentence.
    solveStep(stepState.isComposition ? 'Compare your writing with the example, then continue.' : 'Compare your sentences with the examples, then continue.');
}

// On-demand only (never automatic): a 1-line prompt embedded in every
// lesson can't afford to make the core lesson flow wait on a network/LLM
// round-trip, so this is opt-in via the "Get feedback" button, which the
// step's own renderer already hides when the learner is offline. Grades
// the learner's own typed sentences against the step's own prompts,
// through the same GraderEngine pipeline every other writing/speaking
// production already uses.
async function lessonGetWritingFeedback() {
    const resultEl = document.getElementById('lsn-writing-feedback-result');
    const btn = document.querySelector('#lsn-writing-feedback button');
    if (!resultEl || typeof GraderEngine === 'undefined') return;

    let learnerText = '';
    const compTextarea = document.querySelector('[data-write-composition]');
    if (compTextarea) {
        learnerText = compTextarea.value.trim();
    } else {
        const inputs = Array.prototype.slice.call(document.querySelectorAll('[data-write]'));
        learnerText = inputs.map(inp => inp.value.trim()).filter(Boolean).join(' ');
    }
    if (!learnerText) return;

    if (btn) btn.disabled = true;
    resultEl.textContent = 'Getting feedback…';

    const prompts = (stepState.lines && stepState.lines.length)
        ? stepState.lines.map(l => l.prompt).join(' / ')
        : (stepState.sourceStep && (stepState.sourceStep.prompt || stepState.sourceStep.title)) || 'Writing practice';
    const engine = new GraderEngine();

    let result;
    try {
        result = await engine.grade(learnerText, {
            cefrLevel: (currentLesson && currentLesson.level) || 'A1',
            taskType: (stepState.lines && stepState.lines.length) ? 'structured_writing' : 'written_production',
            taskInstructions: `Writing task: ${prompts}`,
            targetSkills: (stepState.sourceStep && stepState.sourceStep.teaches) || [],
            modality: 'written'
        });
    } catch (e) {
        if (btn) btn.disabled = false;
        resultEl.textContent = 'Could not get feedback right now. Try again.';
        return;
    }

    const score = result.overallScore || 0;
    const tip = _graderOneLineTip(result);
    resultEl.innerHTML = `
        <div class="sp-challenge-feedback-card" style="background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:12px 16px; margin:10px 0;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
                <span style="font-weight:700; font-size:0.9rem; color:var(--text-heading);">Writing Coach</span>
                <span class="cando-badge ${score >= 60 ? 'cando-badge-verified' : 'cando-badge-gap'}" style="font-size:0.8rem;">${score}%</span>
            </div>
            ${tip ? `<p style="margin:0; font-size:0.95rem; color:var(--text); line-height:1.4;">${esc(tip)}</p>` : ''}
        </div>
    `;
    if (btn) btn.remove();
}

// One-sentence coaching tip pulled from the grader's own qualitative
// feedback — the same data Writing/Speaking Studio already renders in full
// (errors[].explanation, feedback.strengths/priorities), condensed to the
// single line these in-lesson checkpoints have room for. Priorities are
// written to be specific and actionable ("use X instead of Y"), so they
// read better as the one tip than a raw error quote or a bare strength.
function _graderOneLineTip(result) {
    const priorities = (result.feedback && result.feedback.priorities) || [];
    if (priorities.length) return priorities[0];
    const errors = result.errors || [];
    if (errors.length && errors[0].explanation) return errors[0].explanation;
    const strengths = (result.feedback && result.feedback.strengths) || [];
    if (strengths.length) return strengths[0];
    return '';
}

// Reveals one substitution option's resulting sentence; Continue unlocks
// once every option has been viewed (no right/wrong here, same reasoning
// as lessonRevealWriting() above — this is exposure to a pattern, not a
// graded question).
function lessonRevealSub(i) {
    if (stepState.solved) return;
    const opt = (stepState.options || [])[i];
    if (!opt || stepState.viewed.has(i)) return;

    stepState.viewed.add(i);
    const result = document.getElementById('sub-result-' + i);
    if (result) {
        result.querySelector('.lsn-es').innerHTML = highlightWord(opt.sentence, opt.inflected || opt.word);
        result.classList.add('is-shown');
    }
    const btn = document.querySelector('[data-sub-index="' + i + '"]');
    if (btn) btn.classList.add('used');

    if (stepState.viewed.size >= stepState.options.length) {
        solveStep('✓ Same pattern, different word.');
    } else {
        setFeedback(true, stepState.viewed.size + '/' + stepState.options.length + ' seen');
    }
}

function lessonSetSrsChoice(index, value) {
    stepState.srsChoices[index] = value;
    document.querySelectorAll('[data-srs-choice="' + index + '"]').forEach(btn => {
        btn.classList.toggle('is-selected', btn.dataset.srsValue === value);
    });
}

// Where a card came from, in the form the Decks tab uses for its ids — so a
// word added during a lesson is recognisably part of that lesson's *unit*
// deck (decks.json groups by unit, not by individual lesson; see
// build_decks() in build-manifest.py). Falls back to the old per-lesson
// stem if the curriculum data needed to find the unit isn't loaded, so a
// card still gets a sensible-looking source either way.
function lessonDeckId() {
    if (!currentLesson || !currentLesson.id) return 'lesson';

    const data = window._curriculumData;
    const level = data && data.levels && data.levels[currentLesson.level];
    if (level) {
        const unit = (level.units || []).find(u =>
            (u.lessons || []).some(l => l.id === currentLesson.id));
        if (unit) return 'lesson:' + unit.id;
    }

    return 'lesson:' + currentLesson.id.replace(/^lesson\./, '').split('.').join('-');
}

function lessonSaveChecklistChoices() {
    const container = document.getElementById('lesson-content');
    if (!container || !stepState.sourceStep) return;
    const inputs = container.querySelectorAll('.lsn-check-item input[type="checkbox"]');
    const items = (stepState.sourceStep.items || []).map((text, i) => {
        const input = inputs[i];
        return {
            text: text,
            checked: input ? !!input.checked : false
        };
    });

    const acc = lessonStats.total > 0
        ? Math.round((lessonStats.correctFirstTry / lessonStats.total) * 100)
        : 100;

    const recorded = items.map(item => ({
        text: item.text,
        checked: item.checked,
        exerciseAccuracy: acc
    }));

    lastLessonChecklist = recorded;

    if (currentLesson && currentLesson.id && typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordCompetencies === 'function') {
        LearnerModel.recordCompetencies(currentLesson.id, recorded);
    }
}

function lessonSaveSrsChoices() {
    if (!stepState.cards) return;
    const source = lessonDeckId();

    Object.keys(stepState.srsChoices || {}).forEach(key => {
        const card = stepState.cards[Number(key)];
        if (!card) return;

        if (stepState.srsChoices[key] === 'known') {
            if (typeof addKnownWord === 'function') addKnownWord(card.lemma, card.translation, card.pos, source);
            return;
        }

        if (srsDeck.find(w => w.spanish === card.lemma)) return;
        srsDeck.push(Object.assign({
            spanish: card.lemma,
            english: card.translation || 'unknown',
            type: card.pos || 'unknown',
            source: source,
            added: new Date().toISOString()
        }, newCardSchedule()));
    });

    saveDeck();
    if (typeof updateReaderWordColors === 'function') updateReaderWordColors();
}

let _lessonSpeakingRecording = false;

function lessonToggleSpeaking(btn) {
    if (stepState.solved) return;

    if (typeof Speech !== 'undefined' && typeof window.speechSynthesis !== 'undefined') {
        window.speechSynthesis.cancel();
    }

    if (_lessonSpeakingRecording) {
        _lessonSpeakingRecording = false;
        if (typeof SpeechInput !== 'undefined') SpeechInput.stopListening();
        const statusEl = document.getElementById('lesson-mic-status');
        if (statusEl) statusEl.textContent = 'Tap to speak';
        if (btn) btn.classList.remove('sp-recording');
        return;
    }

    _lessonSpeakingRecording = true;
    if (btn) btn.classList.add('sp-recording');
    const statusEl = document.getElementById('lesson-mic-status');
    if (statusEl) statusEl.textContent = 'Listening...';
    const liveEl = document.getElementById('lesson-live-transcript');
    if (liveEl) {
        liveEl.textContent = '...';
        liveEl.classList.remove('hidden');
    }

    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.startListening({
            target: stepState.target || '',
            onInterim: interim => {
                if (liveEl) liveEl.textContent = interim;
            },
            onFinal: transcript => {
                _lessonSpeakingRecording = false;
                if (btn) btn.classList.remove('sp-recording');
                if (statusEl) statusEl.textContent = 'Tap to speak';
                if (liveEl) liveEl.textContent = transcript;
                stepState.transcript = transcript;
                stepState.checkDisabled = false;
                updateFooterButton();
                if (stepState.checkFn === 'lessonCheckChallenge') {
                    lessonCheckChallenge();
                } else {
                    lessonCheckSpeaking();
                }
            },
            onAudioReady: url => {
                stepState.userAudioUrl = url;
                _updateLessonCompareAudio();
            },
            onError: err => {
                _lessonSpeakingRecording = false;
                if (btn) btn.classList.remove('sp-recording');
                if (statusEl) statusEl.textContent = 'Tap to speak';

                // Defensive guard: if user already spoke and transcript was captured,
                // evaluate the captured speech rather than showing a spurious "No voice heard" error.
                const currentText = stepState.transcript || (liveEl && liveEl.textContent && liveEl.textContent !== '...' ? liveEl.textContent.trim() : '');
                if (currentText) {
                    stepState.transcript = currentText;
                    stepState.checkDisabled = false;
                    updateFooterButton();
                    if (stepState.checkFn === 'lessonCheckChallenge') {
                        lessonCheckChallenge();
                    } else {
                        lessonCheckSpeaking();
                    }
                    return;
                }

                if (err === 'permission-denied') {
                    setFeedback(false, 'Microphone permission was denied. Please allow microphone access in your browser settings.');
                } else if (err === 'no-speech') {
                    setFeedback(false, 'No voice heard. Did you speak into the microphone?');
                } else {
                    setFeedback(false, 'Could not hear clearly. Try again or skip.');
                }
                stepState.checkDisabled = false;
                updateFooterButton();
            }
        });
    }
}

let _lessonUserAudioPlayer = null;

function _updateLessonCompareAudio() {
    const btn = document.getElementById('lesson-btn-user-audio');
    if (btn && stepState.userAudioUrl) {
        btn.classList.remove('hidden');
    }
}

function lessonPlayModelAudio() {
    if (_lessonUserAudioPlayer) {
        try { _lessonUserAudioPlayer.pause(); } catch (e) {}
        _lessonUserAudioPlayer = null;
        const btn = document.getElementById('lesson-btn-user-audio');
        const label = document.getElementById('lesson-user-audio-label');
        if (btn) btn.classList.remove('is-playing');
        if (label) label.textContent = 'Your Voice';
    }

    const target = stepState.target || '';
    if (target && typeof ParlourTTS !== 'undefined') {
        ParlourTTS.speak({ text: target, type: 'pronunciation' });
    }
}

function lessonPlayUserAudio() {
    const url = stepState.userAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);
    if (!url) return;

    if (typeof Speech !== 'undefined' && typeof window.speechSynthesis !== 'undefined') {
        window.speechSynthesis.cancel();
    }
    if (_lessonUserAudioPlayer) {
        try { _lessonUserAudioPlayer.pause(); } catch (e) {}
        _lessonUserAudioPlayer = null;
    }

    const btn = document.getElementById('lesson-btn-user-audio');
    const label = document.getElementById('lesson-user-audio-label');

    try {
        _lessonUserAudioPlayer = new Audio(url);
        if (btn) btn.classList.add('is-playing');
        if (label) label.textContent = 'Playing...';

        _lessonUserAudioPlayer.onended = () => {
            if (btn) btn.classList.remove('is-playing');
            if (label) label.textContent = 'Your Voice';
            _lessonUserAudioPlayer = null;
        };

        _lessonUserAudioPlayer.onerror = () => {
            if (btn) btn.classList.remove('is-playing');
            if (label) label.textContent = 'Your Voice';
            _lessonUserAudioPlayer = null;
        };

        _lessonUserAudioPlayer.play().catch(e => {
            console.warn('Lesson audio playback error:', e);
            if (btn) btn.classList.remove('is-playing');
            if (label) label.textContent = 'Your Voice';
        });
    } catch (e) {
        console.warn('Lesson audio init error:', e);
    }
}

// Single-sentence speaking exercises (both read-repeat shadowing and
// prompt-speak translation) use the fast, local SpeechInput.evaluate()
// engine from the workshop drill runner — giving immediate word-by-word
// feedback and audio comparison without heavy CEFR dimension overhead.
// (Multi-sentence open tasks can invoke _lessonCheckSpeakingCEFR).
function lessonCheckSpeaking() {
    if (stepState.solved) return;

    const target = stepState.target || '';
    const transcript = stepState.transcript || '';

    let evalResult = { isCorrect: true, accuracy: 100, words: [] };
    if (typeof SpeechInput !== 'undefined') {
        evalResult = SpeechInput.evaluate(target, transcript);
    }

    const targetRevealEl = document.getElementById('sp-prompt-target-reveal');
    if (targetRevealEl) {
        targetRevealEl.classList.remove('hidden');
    }

    const revealEl = document.getElementById('lesson-sp-reveal');
    if (revealEl) {
        revealEl.classList.remove('hidden');
        const userAudioUrl = stepState.userAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);
        const listenIcon = (typeof Art !== 'undefined') ? Art.icon('listening') : '';
        const micIcon = (typeof Art !== 'undefined') ? Art.icon('mic') : '';

        revealEl.innerHTML = `
            ${evalResult.words && evalResult.words.length ? `
                <div class="sp-word-breakdown">
                    ${evalResult.words.map(w => `
                        <span class="sp-word-pill ${w.status === 'matched' ? 'sp-word-matched' : 'sp-word-missed'}">
                            ${esc(w.word)}
                        </span>
                    `).join('')}
                </div>
            ` : ''}
            <div class="sp-compare-bar">
                <button type="button" class="sp-audio-compare-btn sp-btn-model" onclick="lessonPlayModelAudio()" aria-label="Listen to model voice">
                    ${listenIcon}
                    <span>Model Voice</span>
                </button>
                <button type="button" class="sp-audio-compare-btn sp-btn-user ${userAudioUrl ? '' : 'hidden'}" id="lesson-btn-user-audio" onclick="lessonPlayUserAudio()" aria-label="Listen to your recording">
                    ${micIcon}
                    <span id="lesson-user-audio-label">Your Voice</span>
                </button>
            </div>
        `;
    }

    if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
        const skills = (stepState.sourceStep && stepState.sourceStep.skillIds) || null;
        if (skills && skills.length) {
            LearnerModel.recordProduction(skills, evalResult.isCorrect, evalResult.accuracy, 'oral');
        } else if (currentLesson && currentLesson.id && typeof Recommend !== 'undefined' && typeof Recommend.lessonSkillFor === 'function') {
            Recommend.lessonSkillFor(currentLesson.id).then(skill => {
                if (skill) LearnerModel.recordProduction([skill], evalResult.isCorrect, evalResult.accuracy, 'oral');
            }).catch(() => {});
        }
    }

    const isPrompt = stepState.mode === 'prompt-speak';
    if (evalResult.isCorrect) {
        solveStep(`✓ ${isPrompt ? 'Translated & spoken clearly!' : 'Spoken clearly!'} (${evalResult.accuracy}%)`);
    } else {
        if (failStep(`✗ Accuracy ${evalResult.accuracy}%. Try again or continue.`)) {
            setFeedback(false, `Keep practicing: listen to the model above.`);
        }
    }
}

// Progressive CEFR Communicative Challenge Evaluator:
// - Tier 1 (A1): Fast local word matching against target sentence (SpeechInput.evaluate)
// - Tier 2 (A2): Situational multi-cue transaction evaluation
// - Tier 3 (B1/B2): AI formative grading with a 1-sentence coaching feedback (strengths/priorities)
// Automatically verifies the Can-Do competency in LearnerModel upon passing (>= 60%).
async function lessonCheckChallenge() {
    if (stepState.solved) return;

    const transcript = (stepState.transcript || '').trim();
    const typedInput = document.getElementById('lesson-challenge-input');
    const typed = (typedInput ? typedInput.value : '').trim();
    const userText = transcript || typed;

    if (!userText) {
        setFeedback(false, 'Please speak or type your response first.');
        return;
    }

    const modality = transcript ? 'oral' : 'written';
    const tier = stepState.tier || 'tier1';
    const canDo = stepState.canDo || '';
    const level = (currentLesson && currentLesson.level) || 'A1';
    const lang = typeof Lang !== 'undefined' ? Lang.code() : 'es';
    const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';

    stepState.checkDisabled = true;
    updateFooterButton();
    setFeedback(true, 'Evaluating your response…');

    const revealEl = document.getElementById('lesson-challenge-reveal');
    const userAudioUrl = stepState.userAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);
    const listenIcon = (typeof Art !== 'undefined') ? Art.icon('listening') : '';
    const micIcon = (typeof Art !== 'undefined') ? Art.icon('mic') : '';

    if (tier === 'tier1') {
        // Tier 1: Local word/speech evaluation
        const target = stepState.target || '';
        let evalResult = { isCorrect: true, accuracy: 100, words: [] };
        if (target && typeof SpeechInput !== 'undefined') {
            evalResult = SpeechInput.evaluate(target, userText);
        } else {
            const words = userText.split(/\s+/).filter(Boolean);
            const ok = words.length >= 2;
            evalResult = { isCorrect: ok, accuracy: ok ? 85 : 50, words: [] };
        }

        if (revealEl) {
            revealEl.classList.remove('hidden');
            revealEl.innerHTML = `
                ${evalResult.words && evalResult.words.length ? `
                    <div class="sp-word-breakdown">
                        ${evalResult.words.map(w => `
                            <span class="sp-word-pill ${w.status === 'matched' ? 'sp-word-matched' : 'sp-word-missed'}">
                                ${esc(w.word)}
                            </span>
                        `).join('')}
                    </div>
                ` : ''}
                ${target ? `
                    <div style="margin-top:10px; padding:10px 14px; background:rgba(0,0,0,0.03); border-radius:6px;">
                        <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted); font-weight:700;">Model Answer:</span>
                        <p style="margin:4px 0 0 0; font-size:1.05rem; font-weight:600; color:var(--text-heading);">${esc(target)}</p>
                    </div>
                ` : ''}
                <div class="sp-compare-bar" style="margin-top:10px;">
                    ${target ? `
                        <button type="button" class="sp-audio-compare-btn sp-btn-model" onclick="lessonPlayModelAudio()" aria-label="Listen to model voice">
                            ${listenIcon}
                            <span>Model Voice</span>
                        </button>
                    ` : ''}
                    <button type="button" class="sp-audio-compare-btn sp-btn-user ${userAudioUrl ? '' : 'hidden'}" id="lesson-btn-user-audio" onclick="lessonPlayUserAudio()" aria-label="Listen to your recording">
                        ${micIcon}
                        <span id="lesson-user-audio-label">Your Voice</span>
                    </button>
                </div>
            `;
        }

        const skills = (stepState.sourceStep && stepState.sourceStep.skillIds) || null;
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
            if (skills && skills.length) {
                LearnerModel.recordProduction(skills, evalResult.isCorrect, evalResult.accuracy, modality);
            }
        }

        if (evalResult.isCorrect) {
            if (canDo && typeof LearnerModel !== 'undefined' && typeof LearnerModel.verifyCompetency === 'function') {
                LearnerModel.verifyCompetency(canDo, evalResult.accuracy, 'lesson-challenge', modality);
            }
            solveStep(`✓ Challenge complete! CEFR goal verified (${evalResult.accuracy}%)`);
        } else {
            if (failStep(`✗ Accuracy ${evalResult.accuracy}%. Try again or continue.`)) {
                setFeedback(false, 'Keep practicing to master this goal.');
            }
        }
    } else {
        // Tier 2 (A2) & Tier 3 (B1/B2): Communicative evaluation with 1-sentence coaching feedback
        let score = 75;
        let tip = '';

        if (typeof GraderEngine !== 'undefined' && (typeof navigator === 'undefined' || navigator.onLine)) {
            try {
                const engine = new GraderEngine();
                const result = await engine.grade(userText, {
                    cefrLevel: level,
                    taskType: tier === 'tier2' ? 'structured_transaction' : 'oral_production',
                    taskInstructions: stepState.prompt + (stepState.cues && stepState.cues.length ? ` Points: ${stepState.cues.join(', ')}` : ''),
                    language: lang,
                    modality: modality,
                    title: 'Lesson Communicative Challenge'
                });
                score = result.overallScore || 75;
                tip = _graderOneLineTip(result);
            } catch (e) {
                console.warn('GraderEngine challenge error:', e);
                const words = userText.split(/\s+/).filter(Boolean).length;
                score = words >= 5 ? 80 : 55;
            }
        } else {
            // Local fallback
            const words = userText.split(/\s+/).filter(Boolean).length;
            const minWords = tier === 'tier2' ? 6 : 12;
            score = words >= minWords ? 85 : Math.round((words / minWords) * 80);
            tip = score >= 70 ? 'Great job formulating your response in context!' : 'Try to expand your answer with more details.';
        }

        if (revealEl) {
            revealEl.classList.remove('hidden');
            revealEl.innerHTML = `
                <div class="sp-challenge-feedback-card" style="background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:12px 16px; margin:10px 0;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
                        <span style="font-weight:700; font-size:0.9rem; color:var(--text-heading);">Coach Feedback</span>
                        <span class="cando-badge ${score >= 60 ? 'cando-badge-verified' : 'cando-badge-gap'}" style="font-size:0.8rem;">${score}%</span>
                    </div>
                    ${tip ? `<p style="margin:0; font-size:0.95rem; color:var(--text); line-height:1.4;">${esc(tip)}</p>` : ''}
                </div>
                ${userAudioUrl ? `
                    <div class="sp-compare-bar" style="margin-top:8px;">
                        <button type="button" class="sp-audio-compare-btn sp-btn-user" id="lesson-btn-user-audio" onclick="lessonPlayUserAudio()" aria-label="Listen to your recording">
                            ${micIcon}
                            <span id="lesson-user-audio-label">Your Voice</span>
                        </button>
                    </div>
                ` : ''}
            `;
        }

        const isPass = score >= 60;
        const skills = (stepState.sourceStep && stepState.sourceStep.skillIds) || null;
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
            if (skills && skills.length) {
                LearnerModel.recordProduction(skills, isPass, score, modality);
            }
        }

        if (isPass) {
            if (canDo && typeof LearnerModel !== 'undefined' && typeof LearnerModel.verifyCompetency === 'function') {
                LearnerModel.verifyCompetency(canDo, score, 'lesson-challenge', modality);
            }
            solveStep(`✓ ${tier === 'tier2' ? 'Transaction complete!' : 'Challenge passed!'} CEFR goal verified (${score}%)`);
        } else {
            if (failStep(`Score ${score}%. Try again or continue.`)) {
                setFeedback(false, 'Review the cues above and try again.');
            }
        }
    }
}
window.lessonCheckChallenge = lessonCheckChallenge;

const CEFR_DIMENSION_LABELS = { grammar: 'Grammar', vocabulary: 'Vocabulary', coherence: 'Coherence', complexity: 'Complexity', naturalness: 'Naturalness' };

async function _lessonCheckSpeakingCEFR() {
    const target = stepState.target || '';
    const transcript = stepState.transcript || '';

    const targetRevealEl = document.getElementById('sp-prompt-target-reveal');
    if (targetRevealEl) targetRevealEl.classList.remove('hidden');

    // Grading is a network/LLM round-trip; lock the button so a slow
    // response can't be double-submitted. It's freed again the normal way,
    // by the next recording's onFinal (same as the word-match path above).
    stepState.checkDisabled = true;
    updateFooterButton();
    setFeedback(true, 'Grading your response…');

    const lang = typeof Lang !== 'undefined' ? Lang.code() : 'es';
    const langName = typeof Lang !== 'undefined' ? Lang.name() : 'Spanish';
    const skills = (stepState.sourceStep && stepState.sourceStep.skillIds) || null;
    const engine = new GraderEngine();

    let result;
    try {
        result = await engine.grade(transcript, {
            cefrLevel: (currentLesson && currentLesson.level) || 'A2',
            taskType: 'oral_production',
            taskInstructions: `Say in ${langName}: "${stepState.english || target}"`,
            targetSkills: skills || [],
            language: lang,
            modality: 'oral',
            title: 'Lesson speaking practice'
        });
    } catch (e) {
        // GraderEngine.grade() already falls back gracefully on network
        // failure; this only guards against something else going wrong.
        stepState.checkDisabled = false;
        updateFooterButton();
        setFeedback(false, 'Could not grade right now. Try again.');
        return;
    }

    const revealEl = document.getElementById('lesson-sp-reveal');
    if (revealEl) {
        revealEl.classList.remove('hidden');
        const userAudioUrl = stepState.userAudioUrl || (typeof SpeechInput !== 'undefined' ? SpeechInput.getRecordedAudioUrl() : null);
        const listenIcon = (typeof Art !== 'undefined') ? Art.icon('listening') : '';
        const micIcon = (typeof Art !== 'undefined') ? Art.icon('mic') : '';
        const dims = result.dimensions || {};
        const tip = _graderOneLineTip(result);

        revealEl.innerHTML = `
            <div class="sp-word-breakdown">
                ${Object.keys(dims).map(key => `
                    <span class="sp-word-pill ${dims[key] >= 0.6 ? 'sp-word-matched' : 'sp-word-missed'}">
                        ${esc(CEFR_DIMENSION_LABELS[key] || key)}: ${Math.round((dims[key] || 0) * 100)}%
                    </span>
                `).join('')}
            </div>
            ${tip ? `<p class="lsn-hint">${esc(tip)}</p>` : ''}
            <div class="sp-compare-bar">
                <button type="button" class="sp-audio-compare-btn sp-btn-model" onclick="lessonPlayModelAudio()" aria-label="Listen to model voice">
                    ${listenIcon}
                    <span>Model Voice</span>
                </button>
                <button type="button" class="sp-audio-compare-btn sp-btn-user ${userAudioUrl ? '' : 'hidden'}" id="lesson-btn-user-audio" onclick="lessonPlayUserAudio()" aria-label="Listen to your recording">
                    ${micIcon}
                    <span id="lesson-user-audio-label">Your Voice</span>
                </button>
            </div>
        `;
    }

    const score = result.overallScore || 0;
    const isPass = score >= 60;

    if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.recordProduction === 'function') {
        if (skills && skills.length) {
            LearnerModel.recordProduction(skills, isPass, score, 'oral');
        } else if (currentLesson && currentLesson.id && typeof Recommend !== 'undefined' && typeof Recommend.lessonSkillFor === 'function') {
            Recommend.lessonSkillFor(currentLesson.id).then(skill => {
                if (skill) LearnerModel.recordProduction([skill], isPass, score, 'oral');
            }).catch(() => {});
        }
    }

    if (isPass) {
        solveStep(`✓ Nice! CEFR score ${score}%`);
    } else {
        if (failStep(`CEFR score ${score}%. Try again or continue.`)) {
            setFeedback(false, `Keep practicing: listen to the model above.`);
        }
    }
}

function lessonResumeSpeaking() {
    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.resumeSpeaking();
    }
    renderStep(currentStepIndex);
}

function lessonSkipSpeaking() {
    if (stepState.solved) return;
    if (typeof SpeechInput !== 'undefined') {
        SpeechInput.setCantSpeakNow(10);
    }
    if (typeof showToast === 'function') {
        showToast('Understood — speaking exercises disabled for 10 minutes', 'info');
    } else if (typeof UI !== 'undefined' && UI.toast) {
        UI.toast('Understood — speaking exercises disabled for 10 minutes', 'info');
    }
    setFeedback(true, 'Speaking snoozed for 10 minutes.');
    solveStep('Skipped (Speaking snoozed)');
    advanceLessonStep();
}

let _inlineVoiceActive = false;

function lessonInlineVoiceInput(selector, btn) {
    if (typeof SpeechInput === 'undefined' || !SpeechInput.isRecognitionSupported()) {
        if (typeof showToast === 'function') showToast('Voice recognition is not supported in this browser.', 'warning');
        else if (typeof UI !== 'undefined' && UI.toast) UI.toast('Voice recognition is not supported in this browser.', 'warning');
        else alert('Voice recognition is not supported in this browser.');
        return;
    }

    if (typeof Speech !== 'undefined' && typeof window.speechSynthesis !== 'undefined') {
        window.speechSynthesis.cancel();
    }

    const input = document.querySelector(selector);
    if (!input) return;

    if (_inlineVoiceActive) {
        SpeechInput.stopListening();
        _inlineVoiceActive = false;
        if (btn) btn.classList.remove('is-recording');
        return;
    }

    _inlineVoiceActive = true;
    if (btn) btn.classList.add('is-recording');

    let target = null;
    let speechLang = undefined;
    if (selector === '#review-type-field') {
        const isEnglishTarget = (typeof reviewDirection !== 'undefined' && reviewDirection === 'es-en');
        speechLang = isEnglishTarget ? 'en-US' : (typeof Lang !== 'undefined' ? Lang.code() : 'es-ES');
        target = isEnglishTarget
            ? (typeof reviewExpectedEnglish !== 'undefined' ? reviewExpectedEnglish : null)
            : (typeof reviewExpectedSpanish !== 'undefined' ? reviewExpectedSpanish : null);
    } else if (typeof stepState !== 'undefined') {
        target = (stepState.acceptable || (stepState.answer ? [stepState.answer] : null));
    }

    SpeechInput.startListening({
        lang: speechLang,
        target: target,
        onInterim: interim => {
            input.value = interim;
            input.dispatchEvent(new Event('input', { bubbles: true }));
        },
        onFinal: transcript => {
            _inlineVoiceActive = false;
            if (btn) btn.classList.remove('is-recording');
            if (transcript) {
                input.value = transcript;
                input.dispatchEvent(new Event('input', { bubbles: true }));
            }
            try { input.focus(); } catch (e) {}
        },
        onError: err => {
            _inlineVoiceActive = false;
            if (btn) btn.classList.remove('is-recording');
        }
    });
}

// Legacy quiz handler — kept for old HTML lessons. Green for correct, same
// as everywhere else (see setFeedback() above).
function checkLessonAnswer(btn, isCorrect) {
    const allBtns = btn.parentElement.querySelectorAll('button');
    allBtns.forEach(b => {
        b.style.borderColor = 'var(--border)';
        b.style.background = 'none';
    });

    if (isCorrect) {
        btn.style.borderColor = 'var(--success)';
        btn.style.background = 'none';
        document.getElementById('quiz-feedback').textContent = '✓ Correct!';
        document.getElementById('quiz-feedback').style.color = 'var(--success)';
    } else {
        btn.style.borderColor = 'var(--danger)';
        btn.style.background = 'none';
        document.getElementById('quiz-feedback').textContent = '✗ Not quite. Try again!';
        document.getElementById('quiz-feedback').style.color = 'var(--accent-dark)';
    }
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        normalise,
        baseChar,
        generateAnswerDiff,
        contentCache
    };
}