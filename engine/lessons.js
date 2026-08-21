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

// The tab the lesson was opened from, so closing it goes back there.
let lessonReturnTab = 'learn';

// per-step interaction state, reset on every renderStep()
let stepState = {};

// cache so the same content file is not fetched twice
const contentCache = {};

async function loadContent(path) {
    if (contentCache[path]) return contentCache[path];
    try {
        const fullPath = Lang.content(path);
        const response = await fetch(fullPath);
        if (!response.ok) throw new Error('Content not found: ' + fullPath);
        const data = await response.json();
        contentCache[path] = data;
        return data;
    } catch (error) {
        console.warn('Content missing, using placeholder:', path);
        // Return a safe placeholder so the lesson doesn't crash
        return { title: 'Coming soon', sections: [], words: [], lines: [], exercises: [], cards: [] };
    }
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
    const seen = {};

    for (const section of lesson.sections || []) {
        if (section.type !== 'vocabulary') continue;
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
    }

    return words;
}

async function buildSteps(lesson) {
    if (Array.isArray(lesson.steps) && lesson.steps.length) return lesson.steps;
    if (!Array.isArray(lesson.sections)) return [];

    const steps = [];

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
                steps.push({
                    type: 'grammar',
                    title: section.title || grammar.title,
                    parts: grammar.sections || []
                });
            }

            else if (section.type === 'vocabulary') {
                const vocab = await loadContent(section.ref);
                steps.push({
                    type: 'vocabulary',
                    title: section.title || vocab.title || 'Vocabulary',
                    words: vocab.words || []
                });
            }

            else if (section.type === 'story') {
                const story = await loadContent(section.ref);
                steps.push({
                    type: 'story',
                    title: section.title || story.title,
                    // Story files use `paragraphs` (same schema the Library
                    // reader consumes), not a separate bilingual `lines` shape.
                    lines: story.paragraphs || []
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
                    steps.push(Object.assign({}, exercise, {
                        title: !section.title ? 'Exercise'
                            : ids.length > 1 ? section.title + ' ' + (i + 1) + '/' + ids.length
                            : section.title
                    }));
                });
            }

            else if (section.type === 'srs') {
                // Cards are the lesson's own vocabulary — there is no second
                // word list to keep in sync, and the learner picks which of
                // them are worth reviewing.
                steps.push({
                    type: 'srs',
                    title: section.title || 'Add to Review',
                    cards: await collectLessonVocabulary(lesson)
                });
            }

            else if (section.type === 'checklist') {
                steps.push({
                    type: 'checklist',
                    title: section.title || 'Can you do this?',
                    items: section.items || []
                });
            }

            else {
                console.warn('Unknown section type:', section.type);
            }
        } catch (error) {
            console.error('Failed to expand section', section, error);
        }
    }

    return steps;
}

async function startLesson(lessonId) {
    const lesson = await loadLesson(lessonId);
    if (!lesson) {
        alert('Lesson coming soon!');
        return;
    }

    lesson.steps = await buildSteps(lesson);

    if (!lesson.steps.length) {
        alert('This lesson has no content yet.');
        return;
    }

    currentLesson = lesson;
    currentStepIndex = 0;
    originalStepCount = lesson.steps.length;
    missedSteps = [];

    // A lesson can be opened from the level list or from Home's continue
    // card, and closing it should put the learner back where they were rather
    // than always on the level list.
    const from = document.querySelector('.tab:not(.hidden)');
    lessonReturnTab = (from && from.id !== 'lesson-screen') ? from.id : 'learn';

    document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
    document.getElementById('lesson-screen').classList.remove('hidden');

    document.getElementById('lesson-title').textContent = currentLesson.title;
    const subtitle = document.getElementById('lesson-subtitle');
    const levelMark = (typeof levelIcon === 'function') ? levelIcon(currentLesson.level, 'level-icon--sm') : '';
    subtitle.innerHTML = levelMark + '<span>' + UI.escape(currentLesson.level) + '</span>';

    renderStep();
}

function closeLesson() {
    document.getElementById('lesson-screen').classList.add('hidden');

    // Through showTab rather than by hand, so the section is re-rendered on
    // the way in: a lesson just finished is the moment its level list and
    // Home are both out of date.
    showTab(lessonReturnTab, document.querySelector('.nav button[data-tab="' + lessonReturnTab + '"]'));
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

// A listen button for a piece of Spanish. Returns '' when the device has no
// Spanish voice, so every caller can add it without a guard.
function say(text) {
    return (typeof Speech !== 'undefined') ? Speech.button(text) : '';
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

// Dropping accents before comparing a typed answer is a deliberate
// leniency for Spanish (see exercises.schema.json's fill-blank
// description) - rarely changes which word is meant, so it is friendlier
// to a learner without a Spanish keyboard. It is NOT safe for Hungarian:
// accents there are often the entire distinction between different words
// or grammatical forms (kor / kor-with-acute / kor-with-umlaut are three
// unrelated words; several lessons exist specifically to teach a vowel
// pattern like viz -> vizet), and checked directly - 187 of the course's
// 394 fill-blank answers carry an accent. Stripping them the same way
// would make those exercises unable to verify the one thing many of them
// are actually testing.
function normalise(text) {
    const value = String(text || '')
        .toLowerCase()
        .trim()
        .replace(/[.,!?¡¿;:]/g, '');
    if (Lang.code() === 'hu') {
        // Still normalise Unicode representation (NFC) so a precomposed
        // accented letter typed on one keyboard/IME matches a decomposed
        // one from another - just do not strip the accent itself.
        return value.normalize('NFC');
    }
    return value.normalize('NFD').replace(/[̀-ͯ]/g, '');
}

function feedbackHtml() {
    return '<p id="step-feedback" class="lsn-feedback"></p><p id="step-translation" class="lsn-en"></p>';
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
    showTranslation();
    updateFooterButton();
    noteRecycleResult(true);
    queueForRemediationIfMissed();
}

// Records a wrong attempt. Returns true once the learner is out of tries,
// which is the caller's cue to reveal the answer.
function failStep(message) {
    stepState.attempts = (stepState.attempts || 0) + 1;
    const left = MAX_ATTEMPTS - stepState.attempts;

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
    noteRecycleResult(false);
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

// A recycle step's outcome feeds straight back into its own SM-2 schedule —
// solved clean is "good", solved only after burning every attempt is
// "again", same distinction the vocabulary deck's rating buttons make.
function noteRecycleResult(success) {
    if (stepState.recycleNoted) return;
    const step = currentLesson.steps[currentStepIndex];
    if (!step || !step.isRecycle || !step.id) return;
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
    grammar(step) {
        const allowed = ['text', 'table', 'examples', 'tip', 'external-link'];
        return (step.parts || [])
            .filter(part => allowed.indexOf(part.type) !== -1)
            .map(part => {
                const heading = part.title && part.title !== step.title
                    ? `<h4 class="lsn-subtitle">${esc(part.title)}</h4>`
                    : '';
                return heading + stepRenderers[part.type](part);
            })
            .join('');
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
    // rather than guessing.
    table(step) {
        const PRONOUN_RE = /^(yo|tú|usted|él|ella|nosotros|nosotras|vosotros|vosotras|ustedes|ellos|ellas)(\s*\/\s*(yo|tú|usted|él|ella|nosotros|nosotras|vosotros|vosotras|ustedes|ellos|ellas))*$/i;
        return `
            <table class="lsn-table">
                ${(step.rows || []).map(row => {
                    const isConjugation = step.bothAudible || PRONOUN_RE.test((row[0] || '').trim());
                    return `
                    <tr>
                        <td><strong>${esc(row[0])}</strong>${say(row[0])}</td>
                        <td>${esc(row[1])}${isConjugation ? say(row[1]) : ''}</td>
                    </tr>
                `;
                }).join('')}
            </table>
        `;
    },

    examples(step) {
        return (step.items || []).map(item => `
            <div class="lsn-example">
                <div class="lsn-es">${escMd(item.spanish)}${say(item.spanish)}</div>
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

    vocabulary(step) {
        return `
            <div class="lsn-vocab">
                ${(step.words || []).map(word => `
                    <div class="lsn-vocab-row">
                        <div>
                            <div class="lsn-es">${esc(word.lemma)}${say(word.lemma)}</div>
                            <div class="lsn-pos">${esc(word.pos)}</div>
                        </div>
                        <div class="lsn-en">${esc(word.translation)}</div>
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
        const speech = line => isTargetLanguage(line) ? say(line.text) : '';
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
        return `
            <p class="lsn-question">${escMd(step.question)}</p>
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})">${escMd(option)}</button>
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
        return `
            <div class="lsn-dialogue">
                ${(step.prompt || []).map(line => `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div class="lsn-es">${escMd(line.text)}</div>
                    </div>
                `).join('')}
            </div>
            <p class="lsn-question">Choose the missing line:</p>
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})">${escMd(option)}</button>
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
                ${(typeof Speech === 'undefined' || !Speech.available())
                    ? `<p class="lsn-hint">No ${esc(Lang.name())} voice found on this device — you can still answer after 3 tries.</p>` : ''}
            </div>
            <div class="lsn-options">
                ${pick.options.map((option, i) => `
                    <button class="lsn-option" onclick="lessonSelectOption(this, ${i})">${escMd(option)}</button>
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
            <p class="lsn-question">Listen and type what you hear.</p>
            <div class="lsn-listen">
                <button class="lsn-play" onclick="lessonPlayAudio()" aria-label="Play audio">${Art.icon('listening')} Play</button>
                ${(typeof Speech === 'undefined' || !Speech.available())
                    ? `<p class="lsn-hint">No ${esc(Lang.name())} voice found on this device — you can still answer after 3 tries.</p>` : ''}
            </div>
            <input id="blank-input" class="lsn-input" type="text" placeholder="Type what you hear">
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
            <input id="blank-input" class="lsn-input" type="text" placeholder="Type the missing word">
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
        stepState.lines = (step.template || []).map(line =>
            typeof line === 'string' ? { prompt: line, answer: '' } : line);
        stepState.checkFn = 'lessonRevealWriting';
        stepState.checkDisabled = true;

        return `
            <p class="lsn-question">Complete each line in ${esc(Lang.name())}.</p>
            ${stepState.lines.map((line, i) => `
                <div class="lsn-write-row">
                    <div class="lsn-en">${esc(line.prompt)}</div>
                    <input class="lsn-input" type="text" placeholder="Your sentence"
                        data-write="${i}" oninput="lessonCheckWriting()">
                    ${line.answer ? `
                        <div class="lsn-model" data-model="${i}">
                            <span class="lsn-model-label">One way to say it</span>
                            <span class="lsn-es">${esc(line.answer)}</span>
                        </div>
                    ` : ''}
                </div>
            `).join('')}
            <p class="lsn-hint">There is more than one right answer. Write every line, then compare yours with the examples.</p>
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
            <button class="lsn-check" id="srs-add-btn" onclick="lessonSaveSrsChoices()">Save</button>
            ${feedbackHtml()}
        `;
    },

    checklist(step) {
        return `
            <div class="lsn-checklist">
                ${(step.items || []).map((item, i) => `
                    <label class="lsn-check-item">
                        <input type="checkbox" data-check="${i}">
                        <span>${esc(item)}</span>
                    </label>
                `).join('')}
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
    const container = document.getElementById('lesson-content');
    if (!container || container.dataset.enterWired) return;
    container.dataset.enterWired = '1';

    container.addEventListener('keydown', e => {
        if (e.key !== 'Enter') return;
        const target = e.target;
        const isTextInput = target.tagName === 'INPUT' && target.type === 'text';
        const isAnswer = target.classList.contains('lsn-option') || target.classList.contains('lsn-tile');
        if (!isTextInput && !isAnswer) return;

        const btn = document.getElementById('lesson-next-btn');
        if (btn && !btn.disabled) {
            e.preventDefault();
            btn.click();
        }
    });
}

function renderStep() {
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
    container.scrollIntoView({ block: 'start' });

    if (typeof updateReaderWordColors === 'function') updateReaderWordColors();

    const backBtn = document.getElementById('lesson-back-btn');
    if (backBtn) backBtn.disabled = currentStepIndex === 0;

    updateFooterButton();
}

function nextLessonStep() {
    if (stepState.gated && !stepState.solved) return;

    currentStepIndex++;
    if (currentStepIndex < currentLesson.steps.length) {
        renderStep();
        return;
    }

    // Reached the end of the regular steps — work through anything missed
    // on its first try before actually finishing, one at a time, so it's
    // the last thing the learner sees rather than the first thing they
    // forget. Re-queues itself (via queueForRemediationIfMissed()) if this
    // attempt is missed too, so a step keeps coming back until it's solved
    // clean or the 3-try reveal kicks in.
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
    currentStepIndex--;
    renderStep();
}

function finishLesson() {
    // Fixed reward: a long lesson isn't worth more than a short one, and
    // scaling by step count rewarded lesson length rather than learning.
    const firstTime = typeof markLessonComplete === 'function'
        ? markLessonComplete(currentLesson.id)
        : true;

    if (typeof recordLessonCompleted === 'function') {
        recordLessonCompleted(firstTime);
    }

    closeLesson();
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

    // Most blanks have exactly one right answer, but some genuinely accept
    // several (e.g. any of the story's characters completing "Soy ___.") —
    // stepState.acceptable carries the full list, stepState.answer stays the
    // one shown on reveal.
    const acceptable = stepState.acceptable || [stepState.answer];
    const ok = acceptable.some(a => normalise(input.value) === normalise(a));
    input.classList.toggle('correct', ok);
    input.classList.toggle('wrong', !ok);

    if (ok) {
        solveStep('✓ Correct!');
        return;
    }

    if (failStep('✗ Try again.')) {
        input.value = stepState.answer;
        input.classList.remove('wrong');
        input.classList.add('correct');
        setFeedback(false, 'The answer was "' + stepState.answer + '" — continue when you are ready.');
    }
}

function lessonPlayAudio() {
    if (typeof Speech !== 'undefined') Speech.speak(stepState.audio);
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

    const inputs = Array.prototype.slice.call(document.querySelectorAll('[data-write]'));
    const filled = inputs.length > 0 && inputs.every(input => input.value.trim().length > 0);

    stepState.checkDisabled = !filled;
    updateFooterButton();

    setFeedback(true, filled ? 'Ready — check your answers against the examples.' : '');
}

function lessonRevealWriting() {
    if (stepState.revealed) return;
    stepState.revealed = true;

    document.querySelectorAll('[data-model]').forEach(el => el.classList.add('is-shown'));

    // Inputs stay editable so the learner can correct their own sentence.
    solveStep('Compare your sentences with the examples, then continue.');
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

// Where a card came from, in the form the Decks tab uses for its ids, so a
// word added during Lesson 4 is recognisably part of Lesson 4's deck.
// 'lesson.a1.03a' -> 'lesson:a1-03a'.
function lessonDeckId() {
    if (!currentLesson || !currentLesson.id) return 'lesson';
    return 'lesson:' + currentLesson.id.replace(/^lesson\./, '').split('.').join('-');
}

function lessonSaveSrsChoices() {
    if (!stepState.cards) return;
    let toReview = 0, toKnown = 0;
    const source = lessonDeckId();

    Object.keys(stepState.srsChoices || {}).forEach(key => {
        const card = stepState.cards[Number(key)];
        if (!card) return;

        if (stepState.srsChoices[key] === 'known') {
            if (typeof addKnownWord === 'function'
                && addKnownWord(card.lemma, card.translation, card.pos, source)) toKnown++;
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
        toReview++;
    });

    saveDeck();
    if (typeof updateReaderWordColors === 'function') updateReaderWordColors();

    const btn = document.getElementById('srs-add-btn');
    if (btn) {
        btn.textContent = '✓ Saved (' + toReview + ' to review, ' + toKnown + ' known)';
        btn.disabled = true;
    }
    document.querySelectorAll('.lsn-srs-opt').forEach(opt => { opt.disabled = true; });
    setFeedback(true, 'You can move words between review and My Dictionary any time from Decks.');
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