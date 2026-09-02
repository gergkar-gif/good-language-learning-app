// ============================================
// VOCABULARY DRILLER
// ============================================
// Per PARLOUR_VOCABULARY_DRILLER_SPEC.md: this driller does not duplicate
// My Decks/SRS (direct flashcard recall — "what does X mean?" with no
// context — belongs there). It trains recognising, inferring and
// retrieving vocabulary *in context*.
//
// No new content or exercise database. Everything is built at runtime from
// three things Parlour already has:
//   content/<lang>/decks/decks.json                  the curriculum word list
//   content/<lang>/indexes/translation-index.json    real sentences, per-course
//   engine/lexicon.js (word/verb index + dictionary)  surface form -> lemma
//
// _buildContextIndex() scans every sentence once, resolving each token to
// its lemma via Lexicon.lookup() — the same resolution the reader's word tap
// uses — so a sentence containing "agotadas" is correctly filed under the
// lemma "agotado". A sentence under 5 words is dropped as a context (the
// spec's "Yo quiero un ______" problem: too little to recover the answer
// from) — the one piece of automated quality control this needs, per the
// spec's own "conservative content selection, not an elaborate QC engine".
//
// Six exercise builders (see PARLOUR_VOCABULARY_DRILLER_SPEC.md's numbered
// list) each try to build one exercise for a word from its available
// contexts, returning null when the data doesn't support that type — a
// polysemy-style "same word, different context" exercise just doesn't exist
// for a word with only one sentence, same "some pools run smaller"
// precedent used elsewhere in this app. For each word in a session, one
// applicable type is picked at random, so a session is naturally a mix of
// all six rather than needing a type picker in the UI.
//
// Both exercise kinds (multiple-choice, fill-blank) are already renderable
// by GrammarRunner, so this module reuses it rather than writing a new one.

const VocabularyDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;

    // A sentence shorter than this can't reliably support an inferable
    // answer — see the spec's own "Yo quiero un ______" counter-example.
    const MIN_CONTEXT_WORDS = 5;
    const WORD_RE = /\p{L}+/gu;

    let _phase = PHASE.SETTINGS;
    let _container = null;

    // Canonical CEFR ordering for the level picker — only levels the course
    // actually has lesson decks for are ever shown (see _load()), so this
    // never hardcodes a language's highest level and silently drops it as
    // new levels are added (found 2026-09-01: the picker only ever offered
    // "All levels"/A1/A2, hardcoded, so a course's B1 words — real content,
    // reachable only via "All levels" — had no dedicated filter option).
    const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

    let _words = null;        // decks.json -> words { lemma: {en, pos} }
    let _wordLevels = null;   // lemma -> 'A1' | 'A2' | ... (from lesson decks)
    let _levels = null;       // distinct levels this course's lesson decks use, CEFR order
    let _pairs = null;        // translation-index.json -> pairs[]
    let _contextIndex = null; // lemma -> [{ sentence, english, form, inflected }]
    let _wordLessonIndex = null; // word-lesson-index.json's byLemma map — the Tier 2 cross-link

    let _mode = MODE.COUNT;
    let _level = 'all';
    let _questionCount = 10;
    let _timerMinutes = 2;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;
    let _missed = []; // {lemma, translation, pos} for each distinct word missed this session

    let _timerInterval = null;
    let _endTime = 0;
    let _timeRemaining = 0;

    // ---- Helpers ----
    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _sample(list) {
        return list[Math.floor(Math.random() * list.length)];
    }

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_words && _pairs && _contextIndex) return;
        const [deckData, translationIndex, wordLessonIndex] = await Promise.all([
            Content.json(Lang.content('decks/decks.json')).catch(() => ({ words: {}, decks: [] })),
            Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] })),
            Content.json(Lang.content('indexes/word-lesson-index.json')).catch(() => ({ byLemma: {} })),
            Lexicon.load()
        ]);
        _words = deckData.words || {};
        _pairs = translationIndex.pairs || [];
        _wordLessonIndex = wordLessonIndex.byLemma || {};
        _wordLevels = {};
        const seenLevels = new Set();
        (deckData.decks || []).filter(d => d.kind === 'lesson').forEach(d => {
            if (d.level) seenLevels.add(d.level);
            (d.lemmas || []).forEach(lemma => {
                if (!(lemma in _wordLevels)) _wordLevels[lemma] = d.level;
            });
        });
        _levels = CEFR_ORDER.filter(l => seenLevels.has(l));
        _contextIndex = _buildContextIndex();
    }

    // One pass over the sentence corpus, resolving every token to a lemma
    // the same way a tapped word in the Reader would be. Built once and
    // reused for every exercise type below, rather than re-scanning the
    // corpus per word (which would be O(words × sentences) instead of
    // O(sentences × words per sentence)).
    function _buildContextIndex() {
        const index = {};
        _pairs.forEach(pair => {
            const tokens = pair.spanish.match(WORD_RE) || [];
            if (tokens.length < MIN_CONTEXT_WORDS) return;

            const seenLemmas = new Set(); // one entry per lemma per sentence
            tokens.forEach(token => {
                const readings = Lexicon.lookup(token).readings;
                if (!readings.length) return;
                const lemma = readings[0].lemma.toLowerCase();
                if (seenLemmas.has(lemma)) return;
                seenLemmas.add(lemma);

                (index[lemma] || (index[lemma] = [])).push({
                    sentence: pair.spanish,
                    english: pair.english,
                    form: token,
                    inflected: token.toLowerCase() !== lemma
                });
            });
        });
        return index;
    }

    // Content words only — nouns, verbs, adjectives, adverbs. Articles,
    // pronouns, prepositions and the like are real vocabulary too, but
    // "what does 'las' mean here?" against random decoys isn't a
    // meaningful inference question the way "what does 'agotado' mean
    // here?" is; every example in the spec is a content word. Filtering
    // here also keeps them out of the decoy pools below, since those draw
    // from the same word list.
    const CONTENT_POS = new Set(['noun', 'verb', 'adjective', 'adverb']);

    function _wordList(level) {
        return Object.keys(_words)
            .filter(lemma => CONTENT_POS.has(_words[lemma].pos))
            .filter(lemma => level === 'all' || _wordLevels[lemma] === level)
            .map(lemma => ({ lemma, en: _words[lemma].en, pos: _words[lemma].pos }));
    }

    function _hasContext(word) {
        return !!(_contextIndex[word.lemma] && _contextIndex[word.lemma].length);
    }

    // Unicode-aware word boundaries so an accented form (día, agotadas) is
    // matched correctly — plain \b treats accented letters as non-word
    // characters and misses them.
    function _wordRegex(form) {
        const escaped = form.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp('(^|[^\\p{L}])(' + escaped + ')([^\\p{L}]|$)', 'iu');
    }

    function _blankSentence(sentence, form) {
        const m = sentence.match(_wordRegex(form));
        if (!m) return null;
        const start = m.index + m[1].length;
        return sentence.slice(0, start) + '_____' + sentence.slice(start + m[2].length);
    }

    // Translation decoys for a "what does this mean" question. `samePos`
    // narrows the pool to words of the same part of speech first — the
    // spec's "meaning discrimination" and "morphological inference" types
    // want decoys that are plausible, not just any random word, and sharing
    // a part of speech is a light, data-driven way to get that without
    // hand-curating distractor sets.
    function _pickTranslationDecoys(word, n, samePos) {
        let candidates = Object.keys(_words)
            .filter(l => CONTENT_POS.has(_words[l].pos) && l !== word.lemma && _words[l].en !== word.en);
        if (samePos) {
            const narrowed = candidates.filter(l => _words[l].pos === word.pos);
            if (narrowed.length >= n) candidates = narrowed;
        }
        return _shuffled(candidates).slice(0, n).map(l => _words[l].en);
    }

    // Same idea, but the decoys are Spanish words (for "which word fits the
    // blank" rather than "what does the word mean").
    function _pickWordDecoys(word, n) {
        let candidates = Object.keys(_words).filter(l => CONTENT_POS.has(_words[l].pos) && l !== word.lemma);
        const narrowed = candidates.filter(l => _words[l].pos === word.pos);
        if (narrowed.length >= n) candidates = narrowed;
        return _shuffled(candidates).slice(0, n);
    }

    // Some corpus sentences carry no terminal punctuation (fragments pulled
    // from grammar exercises rather than full prose) — without this the
    // follow-up question runs straight into the sentence with nothing
    // between them.
    function _withStop(sentence) {
        const trimmed = sentence.trim();
        return /[.!?]$/.test(trimmed) ? trimmed : trimmed + '.';
    }

    function _meaningQuestion(sentence, form) {
        return `${_withStop(sentence)} What does "${form}" mean here?`;
    }

    // Shown after Check, alongside the revealed answer — GrammarRunner
    // already renders ex.explanation once an exercise is solved, so this is
    // the sentence's own translation-index English pair, not anything new.
    function _translationExplanation(match) {
        return `Translation: ${match.english}`;
    }

    // ================================================================
    //  EXERCISE BUILDERS — one per type in PARLOUR_VOCABULARY_DRILLER_SPEC.md
    //  Each returns a GrammarRunner-shaped exercise, or null if this word
    //  doesn't have the context data this type needs.
    // ================================================================

    // 1. Contextual inference — the defining exercise: a real sentence, the
    // target word in it, plain multiple-choice decoys.
    function _buildInference(word) {
        const matches = _contextIndex[word.lemma];
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, false)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    // 2. Contextual recall — the sentence is blanked instead, with the
    // English meaning given as a hint; the learner types the Spanish word.
    // The expected answer is the exact form found in the sentence (an
    // inflected form if that's what appeared), not the bare dictionary
    // lemma — "agotadas" for a sentence that actually says "agotadas".
    function _buildRecall(word) {
        const matches = _contextIndex[word.lemma];
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const blanked = _blankSentence(m.sentence, m.form);
        if (!blanked) return null;
        return {
            kind: 'fill-blank',
            sentence: `English: ${word.en}. ${blanked}`,
            answer: m.form,
            explanation: _translationExplanation(m)
        };
    }

    // 3. Meaning discrimination — same shape as inference, but decoys are
    // drawn from the same part of speech, so they're plausible rather than
    // obviously-wrong.
    function _buildDiscrimination(word) {
        const matches = _contextIndex[word.lemma];
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, true)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    // 4. Same word, different context — the word as it appears in two
    // different real sentences at once. The dictionary here doesn't map
    // senses to specific sentences, so this doesn't force a "which sense"
    // split (that would risk marking a genuinely defensible answer wrong);
    // it tests recognising the same word holding its meaning across two
    // different settings, which is most valuable exactly for the
    // genuinely polysemous words the spec calls out.
    function _buildRepeat(word) {
        const matches = _contextIndex[word.lemma];
        if (!matches || matches.length < 2) return null;
        const [a, b] = _shuffled(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, false)]);
        return {
            kind: 'multiple-choice',
            question: `Sentence 1: ${_withStop(a.sentence)} Sentence 2: ${_withStop(b.sentence)} `
                + `What does "${word.lemma}" mean in both?`,
            options,
            correct: options.indexOf(word.en),
            explanation: `Translation: ${a.english} / ${b.english}`
        };
    }

    // 5. Contextual choice — the sentence is blanked, but instead of typing
    // the learner picks the right Spanish word from same-part-of-speech
    // decoys (no English hint at all — the context alone has to carry it).
    function _buildChoice(word) {
        const matches = _contextIndex[word.lemma];
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const blanked = _blankSentence(m.sentence, m.form);
        if (!blanked) return null;
        const options = _shuffled([m.form, ..._pickWordDecoys(word, DECOY_COUNT)]);
        return {
            kind: 'multiple-choice',
            question: blanked,
            options,
            correct: options.indexOf(m.form),
            explanation: _translationExplanation(m)
        };
    }

    // 6. Morphological inference — the same shape as discrimination, but
    // restricted to a sentence where the word actually shows up inflected
    // ("agotadas", not "agotado") — the point is recognising the word
    // despite the grammatical change.
    function _buildMorphological(word) {
        const matches = (_contextIndex[word.lemma] || []).filter(m => m.inflected);
        if (!matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, true)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    const BUILDERS = [_buildInference, _buildRecall, _buildDiscrimination, _buildRepeat, _buildChoice, _buildMorphological];

    // One random applicable type per word, so a session mixes all six
    // naturally instead of a fixed type dominating because it happens to
    // be tried first.
    // The source word rides along on the built exercise as _word — none of
    // the BUILDERS keep it (their output is GrammarRunner's own {kind,
    // question, options, ...} shape), but the session loop needs the
    // lemma/en/pos back to track a miss for the "add to a deck" link.
    // GrammarRunner only reads the fields it knows about, so an extra one
    // is harmless.
    function _buildExerciseFor(word) {
        const candidates = BUILDERS.map(fn => fn(word)).filter(Boolean);
        if (!candidates.length) return null;
        const exercise = _sample(candidates);
        exercise._word = word;
        return exercise;
    }

    function _buildPool(level) {
        return _wordList(level).map(_buildExerciseFor).filter(Boolean);
    }

    // A pool built directly from caller-supplied words (Decks' review
    // summary, when a session leaves some words shaky) rather than from
    // decks.json's curriculum table via _wordList() — a custom My Deck
    // word wouldn't be in that table at all, so this takes the
    // {lemma, translation, pos} shape Decks already hands around instead
    // of requiring the word to be a known curriculum lemma.
    function _buildPoolFromWords(words) {
        return words
            .map(w => _buildExerciseFor({ lemma: w.lemma, en: w.translation, pos: w.pos }))
            .filter(Boolean);
    }

    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        const available = _wordList(_level).filter(_hasContext).length;

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Vocabulary Driller</h2>
                <p class="gd-hint">Recognise, infer and retrieve vocabulary from real ${Lang.name()} sentences —
                    not bare flashcards. Direct recall lives in My Decks.</p>
                <p class="gd-hint">${available} words with example sentences at this level.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="vd-level">Level</label>
                    <select id="vd-level" class="vb-select">
                        <option value="all">All levels</option>
                        ${_levels.map(l => `<option value="${l}">${l}</option>`).join('')}
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="vd-count">Number of words</label>
                        <select id="vd-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} words</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="vd-timer">Timer</label>
                        <select id="vd-timer" class="vb-select">
                            ${TIMER_PRESETS.map(v => `
                                <option value="${v}"${v === _timerMinutes ? ' selected' : ''}>${v === 1 ? '1 minute' : v + ' minutes'}</option>
                            `).join('')}
                        </select>
                    </div>
                `}

                <button class="vbtn vbtn-primary vbtn-block" data-action="start">Start</button>
            </div>
        `;

        _container.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => { _mode = btn.dataset.mode; _renderSettings(); });
        });

        const levelSelect = _container.querySelector('#vd-level');
        levelSelect.value = _level;
        levelSelect.addEventListener('change', e => { _level = e.target.value; _renderSettings(); });

        const countSelect = _container.querySelector('#vd-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#vd-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool(_level);
        _seen = 0;
        _correct = 0;
        _missed = [];

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No words with example sentences at this level yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-settings">Change settings</button>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            return;
        }

        if (_mode === MODE.COUNT) {
            _queue = _takeN(pool, _questionCount);
        } else {
            _queue = _shuffled(pool);
            _timeRemaining = _timerMinutes * 60;
            _endTime = Date.now() + _timeRemaining * 1000;
            _timerInterval = setInterval(_tick, 250);
        }

        _queueIndex = 0;
        _phase = PHASE.SESSION;
        _renderSession();
    }

    // Entry point for a scoped session (Decks' review summary's "Practice
    // these words" link) — skips the level/count settings entirely and
    // just runs through the given words once, in Count mode so the
    // session has a real end rather than looping the same handful of
    // words on a timer.
    function _startSessionFromWords(words) {
        const pool = _buildPoolFromWords(words);
        _seen = 0;
        _correct = 0;
        _missed = [];

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No example sentences for these words yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-settings">Change settings</button>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            return;
        }

        _mode = MODE.COUNT;
        _queue = _shuffled(pool);
        _questionCount = _queue.length;
        _queueIndex = 0;
        _phase = PHASE.SESSION;
        _renderSession();
    }

    function _tick() {
        const remaining = Math.max(0, Math.ceil((_endTime - Date.now()) / 1000));
        _timeRemaining = remaining;
        const el = _container.querySelector('.vspeed-timer-display');
        if (el) el.textContent = _formatTime(remaining);
        if (remaining <= 0) _finishSession();
    }

    function _scoreLabel() {
        const base = `${_correct}/${_seen} correct`;
        return _mode === MODE.COUNT ? `${base} · Word ${_queueIndex + 1} of ${_queue.length}` : base;
    }

    function _renderSession() {
        const currentWord = _queue[_queueIndex]._word;

        // Tier 2 cross-link — same as the Reader popup and Decks' word-list
        // rows, just placed here instead of fighting GrammarRunner's own
        // append-don't-replace render lifecycle (its moreInfo/explanation
        // panels get inserted into the exercise container at several points
        // as an exercise is answered, so anything this module wants to add
        // reliably has to live outside that container, not inside it).
        // Shown up front rather than only after answering — it says where
        // a word was taught, never what it means, so it gives nothing away.
        const lessonId = currentWord && _wordLessonIndex ? _wordLessonIndex[currentWord.lemma] : null;
        const lessonInfo = lessonId && typeof lessonLabelFor === 'function' ? lessonLabelFor(lessonId) : null;

        _container.innerHTML = `
            <div class="gd-hud">
                <span class="gd-hud-score">${_scoreLabel()}</span>
                ${_mode === MODE.TIMED ? `<span class="vspeed-timer-display">${_formatTime(_timeRemaining)}</span>` : ''}
                <button class="gd-change-skill" data-action="change-settings">Change settings</button>
            </div>
            ${lessonInfo ? `
                <button class="dk-link-btn gd-word-lesson-link" data-open-lesson="${lessonId}">Taught in ${lessonInfo.label}</button>
            ` : ''}
            <div class="gd-exercise"></div>
        `;
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const lessonLinkBtn = _container.querySelector('[data-open-lesson]');
        if (lessonLinkBtn) {
            lessonLinkBtn.addEventListener('click', () => {
                if (typeof startLesson === 'function') startLesson(lessonLinkBtn.getAttribute('data-open-lesson'));
            });
        }

        const exerciseRoot = _container.querySelector('.gd-exercise');

        GrammarRunner.render(exerciseRoot, {
            exercise: _queue[_queueIndex],
            onResult: correct => {
                _seen++;
                if (correct) {
                    _correct++;
                } else if (currentWord && !_missed.some(w => w.lemma === currentWord.lemma)) {
                    _missed.push({ lemma: currentWord.lemma, translation: currentWord.en, pos: currentWord.pos });
                }
                const score = _container.querySelector('.gd-hud-score');
                if (score) score.textContent = _scoreLabel();
            },
            onNext: _nextExercise
        });
    }

    function _nextExercise() {
        if (_mode === MODE.COUNT && _queueIndex + 1 >= _queue.length) {
            _finishSession();
            return;
        }

        _queueIndex++;
        if (_queueIndex >= _queue.length) {
            _queue = _shuffled(_queue);
            _queueIndex = 0;
        }
        _renderSession();
    }

    // ================================================================
    //  RENDERING — Results
    // ================================================================
    function _finishSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.RESULTS;
        _renderResults();
    }

    function _renderResults() {
        const accuracy = _seen ? Math.round((_correct / _seen) * 100) : 0;

        _container.innerHTML = `
            <div class="vspeed-results">
                <h3 class="vspeed-results-title">Session Results</h3>
                <div class="vspeed-results-grid">
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Correct</span>
                        <span class="vspeed-stat-value">${_correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Wrong</span>
                        <span class="vspeed-stat-value">${_seen - _correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Accuracy</span>
                        <span class="vspeed-stat-value">${accuracy}%</span>
                    </div>
                </div>
                ${_missed.length ? `
                    <button class="vbtn vbtn-secondary vbtn-block" data-action="add-missed">
                        Add ${_missed.length} missed ${_missed.length === 1 ? 'word' : 'words'} to a deck
                    </button>
                ` : ''}
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-primary" data-action="play-again">Play Again</button>
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>
                </div>
            </div>
        `;

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const addMissedBtn = _container.querySelector('[data-action="add-missed"]');
        if (addMissedBtn) {
            addMissedBtn.addEventListener('click', () => {
                if (typeof Decks !== 'undefined') Decks.openBulkAddPicker(_missed);
            });
        }
    }

    function _abortSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    // `options.words`, when given, skips the settings screen and launches
    // straight into a session over exactly those words — used by Decks'
    // review summary. Same firstTime-style guard as GrammarDriller's own
    // `options.skill`: only takes effect from the settings phase, so a
    // driller resumed mid-session (e.g. navigating back to Workshop)
    // shows what was already in progress instead.
    async function render(root, options) {
        _container = root;

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            if (options && options.words && options.words.length) {
                _startSessionFromWords(options.words);
            } else {
                _renderSettings();
            }
        } else if (_phase === PHASE.SESSION) {
            _renderSession();
        } else {
            _renderResults();
        }
    }

    return { render };
})();
