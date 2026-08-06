// ============================================
// LESSON ENGINE
// ============================================
// Lessons are loaded dynamically from content/es/lessons/*.json
// Two lesson formats are supported during the migration:
//   1. legacy  -> lesson.steps[] with embedded `html`
//   2. structured -> lesson.sections[] referencing content files
// The renderer builds all HTML. Content files stay data-only.
// ============================================

let lessons = {};
let currentLesson = null;
let currentStepIndex = 0;

// per-step interaction state, reset on every renderStep()
let stepState = {};

// cache so the same content file is not fetched twice
const contentCache = {};

async function loadContent(path) {
    if (contentCache[path]) return contentCache[path];
    try {
        // Updated to include language prefix
        const fullPath = `content/es/${path}`;
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

    const level = parts[0];      // a1
    const number = parts[1];     // 01

    // Updated path to include language prefix
    const path = `content/es/lessons/${level}/${level}-${number}.json`;

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

            else if (section.type === 'grammar') {
                const grammar = await loadContent(section.ref);
                (grammar.sections || []).forEach(part => {
                    steps.push(Object.assign({}, part, {
                        title: part.title || grammar.title
                    }));
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
                        title: section.title
                            ? section.title + ' ' + (i + 1) + '/' + ids.length
                            : 'Exercise'
                    }));
                });
            }

            else if (section.type === 'srs') {
                const srs = await loadContent(section.ref);
                let words = [];
                const vocabRef = (lesson.metadata && lesson.metadata.vocabularyRefs) || [];
                for (const ref of vocabRef) {
                    const vocab = await loadContent(ref);
                    words = words.concat(vocab.words || []);
                }
                steps.push({
                    type: 'srs',
                    title: section.title || 'Add to Review',
                    cards: (srs.cards || []).map(card => {
                        const match = words.find(w => w.lemma === card.lemma);
                        return {
                            id: card.id,
                            lemma: card.lemma,
                            translation: card.translation || (match ? match.translation : ''),
                            pos: match ? match.pos : 'unknown'
                        };
                    })
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

    document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
    document.getElementById('lesson-screen').classList.remove('hidden');

    document.getElementById('lesson-title').textContent = currentLesson.title;
    document.getElementById('lesson-subtitle').textContent = currentLesson.level;

    renderStep();
}

function closeLesson() {
    document.getElementById('lesson-screen').classList.add('hidden');
    document.getElementById('learn').classList.remove('hidden');

    document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
    document.querySelector('.nav button:first-child').classList.add('active');
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

function shuffled(list) {
    const copy = list.slice();
    for (let i = copy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
}

function normalise(text) {
    return String(text || '')
        .toLowerCase()
        .trim()
        .replace(/[.,!?¡¿;:]/g, '')
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '');
}

function feedbackHtml() {
    return '<p id="step-feedback" class="lsn-feedback"></p>';
}

function setFeedback(ok, message) {
    const el = document.getElementById('step-feedback');
    if (!el) return;
    el.textContent = message;
    el.style.color = ok ? '#3E8E5B' : '#B8412F';
}

function lessonProgressHtml() {
    const total = currentLesson.steps.length;
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

    text(step) {
        return `<p class="lsn-text">${esc(step.content)}</p>`;
    },

    tip(step) {
        return `<div class="lsn-tip"><strong>Tip</strong><p>${esc(step.content)}</p></div>`;
    },

    table(step) {
        return `
            <table class="lsn-table">
                ${(step.rows || []).map(row => `
                    <tr>
                        <td><strong>${esc(row[0])}</strong></td>
                        <td>${esc(row[1])}</td>
                    </tr>
                `).join('')}
            </table>
        `;
    },

    examples(step) {
        return (step.items || []).map(item => `
            <div class="lsn-example">
                <div class="lsn-es">${esc(item.spanish)}</div>
                <div class="lsn-en">${esc(item.english)}</div>
            </div>
        `).join('');
    },

    'external-link'(step) {
        return `
            <a class="lsn-link" href="${esc(step.url)}" target="_blank" rel="noopener noreferrer">
                ${esc(step.title || step.url)} ↗
            </a>
        `;
    },

    vocabulary(step) {
        return `
            <div class="lsn-vocab">
                ${(step.words || []).map(word => `
                    <div class="lsn-vocab-row">
                        <div>
                            <div class="lsn-es">${esc(word.lemma)}</div>
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
        // story files carry Spanish text only, no parallel English lines.
        const clickable = text => (typeof Reader !== 'undefined') ? Reader.makeClickable(text) : esc(text);
        return `
            <div class="lsn-story" id="story-body">
                ${(step.lines || []).map(line => line.type === 'dialogue' ? `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div class="lsn-es">${clickable(line.text)}</div>
                    </div>
                ` : `
                    <p class="lsn-narration">${clickable(line.text)}</p>
                `).join('')}
            </div>
        `;
    },

    'multiple-choice'(step) {
        stepState.correct = step.correct;
        return `
            <p class="lsn-question">${esc(step.question)}</p>
            <div class="lsn-options">
                ${(step.options || []).map((option, i) => `
                    <button class="lsn-option" onclick="lessonChoose(this, ${i})">${esc(option)}</button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    'dialogue-complete'(step) {
        stepState.correct = step.correct;
        return `
            <div class="lsn-dialogue">
                ${(step.prompt || []).map(line => `
                    <div class="lsn-line">
                        <div class="lsn-speaker">${esc(line.speaker)}</div>
                        <div class="lsn-es">${esc(line.text)}</div>
                    </div>
                `).join('')}
            </div>
            <p class="lsn-question">Choose the missing line:</p>
            <div class="lsn-options">
                ${(step.options || []).map((option, i) => `
                    <button class="lsn-option" onclick="lessonChoose(this, ${i})">${esc(option)}</button>
                `).join('')}
            </div>
            ${feedbackHtml()}
        `;
    },

    matching(step) {
        const pairs = step.pairs || [];
        stepState.pairs = pairs;
        stepState.matched = 0;
        stepState.pick = null;
        return `
            <p class="lsn-question">Tap a Spanish word, then its translation.</p>
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
        stepState.answer = step.answer;
        return `
            <p class="lsn-question">${esc(step.sentence).replace(/_{2,}/, '<span class="lsn-blank">?</span>')}</p>
            <input id="blank-input" class="lsn-input" type="text" placeholder="Type the missing word"
                onkeydown="if(event.key==='Enter')lessonCheckBlank()">
            <button class="lsn-check" onclick="lessonCheckBlank()">Check</button>
            ${feedbackHtml()}
        `;
    },

    'sentence-builder'(step) {
        stepState.solution = step.solution || [];
        stepState.built = [];
        return `
            <p class="lsn-question">Build the sentence.</p>
            <div id="build-target" class="lsn-target"></div>
            <div class="lsn-options lsn-tiles">
                ${shuffled(step.tiles || []).map(tile => `
                    <button class="lsn-tile" onclick="lessonAddTile(this)">${esc(tile)}</button>
                `).join('')}
            </div>
            <button class="lsn-check" onclick="lessonCheckBuild()">Check</button>
            <button class="lsn-check lsn-secondary" onclick="lessonResetBuild()">Reset</button>
            ${feedbackHtml()}
        `;
    },

    'sentence-order'(step) {
        stepState.solution = step.solution || [];
        stepState.order = [];
        return `
            <p class="lsn-question">Tap the sentences in the right order.</p>
            <div class="lsn-options">
                ${shuffled((step.sentences || []).map((text, i) => ({ text, i }))).map(item => `
                    <button class="lsn-option" data-index="${item.i}"
                        onclick="lessonPickOrder(this)">${esc(item.text)}</button>
                `).join('')}
            </div>
            <button class="lsn-check" onclick="lessonCheckOrder()">Check</button>
            ${feedbackHtml()}
        `;
    },

    'structured-writing'(step) {
        return `
            <p class="lsn-question">Complete each line in Spanish.</p>
            ${(step.template || []).map((line, i) => `
                <div class="lsn-write-row">
                    <div class="lsn-en">${esc(line)}</div>
                    <input class="lsn-input" type="text" placeholder="Your sentence" data-write="${i}">
                </div>
            `).join('')}
            <p class="lsn-hint">Free writing — nothing to check. Continue when you're happy.</p>
        `;
    },

    srs(step) {
        stepState.cards = step.cards || [];
        return `
            <p class="lsn-question">These words will be added to your review deck.</p>
            <div class="lsn-vocab">
                ${(step.cards || []).map(card => `
                    <div class="lsn-vocab-row">
                        <div class="lsn-es">${esc(card.lemma)}</div>
                        <div class="lsn-en">${esc(card.translation)}</div>
                    </div>
                `).join('')}
            </div>
            <button class="lsn-check" id="srs-add-btn" onclick="lessonAddSrsCards()">Add ${(step.cards || []).length} words to review</button>
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
function renderStep() {
    const step = currentLesson.steps[currentStepIndex];
    const container = document.getElementById('lesson-content');

    stepState = {};

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

    const btn = document.querySelector('#lesson-screen .btn-primary');

    if (currentStepIndex >= currentLesson.steps.length - 1) {
        btn.textContent = 'Finish Lesson ✓';
        btn.onclick = finishLesson;
    } else {
        btn.textContent = 'Continue →';
        btn.onclick = nextLessonStep;
    }
}

function nextLessonStep() {
    currentStepIndex++;
    if (currentStepIndex < currentLesson.steps.length) {
        renderStep();
    }
}

function finishLesson() {
    const reward = currentLesson.steps.length * 10;

    if (typeof markLessonComplete === 'function') {
        markLessonComplete(currentLesson.id);
    }

    if (typeof awardXP === 'function') {
        awardXP(reward, 'Lesson complete');
    } else {
        alert('🎉 Lesson complete! +' + reward + ' XP');
    }
    closeLesson();
}

// ============================================
// INTERACTION HANDLERS
// ============================================
function lessonChoose(btn, index) {
    const group = btn.parentElement.querySelectorAll('.lsn-option');
    group.forEach(b => b.classList.remove('correct', 'wrong'));

    if (index === stepState.correct) {
        btn.classList.add('correct');
        setFeedback(true, '✓ Correct!');
    } else {
        btn.classList.add('wrong');
        setFeedback(false, '✗ Not quite. Try again!');
    }
}

function lessonMatch(btn) {
    if (btn.classList.contains('correct')) return;

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
            setFeedback(true, '✓ All matched!');
        } else {
            setFeedback(true, '✓ Match! ' + stepState.matched + '/' + stepState.pairs.length);
        }
    } else {
        btn.classList.add('wrong');
        setFeedback(false, '✗ Not a match.');
        setTimeout(() => btn.classList.remove('wrong'), 700);
    }
}

function lessonCheckBlank() {
    const input = document.getElementById('blank-input');
    if (!input) return;
    const ok = normalise(input.value) === normalise(stepState.answer);
    input.classList.toggle('correct', ok);
    input.classList.toggle('wrong', !ok);
    setFeedback(ok, ok ? '✓ Correct!' : '✗ Try again.');
}

function lessonAddTile(btn) {
    btn.disabled = true;
    btn.classList.add('used');
    stepState.built.push(btn.textContent.trim());
    document.getElementById('build-target').textContent = stepState.built.join(' ');
}

function lessonResetBuild() {
    stepState.built = [];
    document.getElementById('build-target').textContent = '';
    document.querySelectorAll('.lsn-tile').forEach(b => {
        b.disabled = false;
        b.classList.remove('used');
    });
    setFeedback(true, '');
}

function lessonCheckBuild() {
    const ok = normalise(stepState.built.join(' ')) === normalise(stepState.solution.join(' '));
    setFeedback(ok, ok ? '✓ Correct!' : '✗ Not right yet — try reset.');
}

function lessonPickOrder(btn) {
    if (btn.classList.contains('used')) return;
    btn.classList.add('used');
    stepState.order.push(Number(btn.dataset.index));
    btn.textContent = stepState.order.length + '. ' + btn.textContent;
}

function lessonCheckOrder() {
    const ok = stepState.order.length === stepState.solution.length
        && stepState.order.every((v, i) => v === stepState.solution[i]);
    setFeedback(ok, ok ? '✓ Correct order!' : '✗ Not the right order.');
    if (!ok) {
        document.querySelectorAll('.lsn-option.used').forEach(b => {
            b.classList.remove('used');
            b.textContent = b.textContent.replace(/^\d+\.\s/, '');
        });
        stepState.order = [];
    }
}

function lessonAddSrsCards() {
    let added = 0;

    (stepState.cards || []).forEach(card => {
        if (srsDeck.find(w => w.spanish === card.lemma)) return;
        srsDeck.push(Object.assign({
            spanish: card.lemma,
            english: card.translation || 'unknown',
            type: card.pos || 'unknown',
            added: new Date().toISOString()
        }, newCardSchedule()));
        added++;
    });

    saveDeck();
    if (typeof updateReaderWordColors === 'function') updateReaderWordColors();

    const btn = document.getElementById('srs-add-btn');
    if (btn) {
        btn.textContent = added ? '✓ Added ' + added + ' words' : '✓ Already in your deck';
        btn.disabled = true;
    }
    setFeedback(true, 'Review them in the Review tab.');
}

// Legacy quiz handler — kept for old HTML lessons
function checkLessonAnswer(btn, isCorrect) {
    const allBtns = btn.parentElement.querySelectorAll('button');
    allBtns.forEach(b => {
        b.style.borderColor = '#DCE6E8';
        b.style.background = 'white';
    });

    if (isCorrect) {
        btn.style.borderColor = '#3E8E5B';
        btn.style.background = '#e8f5ed';
        document.getElementById('quiz-feedback').textContent = '✓ Correct!';
        document.getElementById('quiz-feedback').style.color = '#3E8E5B';
    } else {
        btn.style.borderColor = '#B8412F';
        btn.style.background = '#fbecea';
        document.getElementById('quiz-feedback').textContent = '✗ Not quite. Try again!';
        document.getElementById('quiz-feedback').style.color = '#B8412F';
    }
}