// ============================================
// DECK LEARN MODE
// ============================================
// Gradual, escalating-difficulty practice through a deck, in small
// rounds rather than the whole deck at once. Feedback that shaped this
// (2026-08-27): "you only go through one round, and it's not enough...
// not too many words at one go... maybe seven, maximum ten... it needs
// to be asked at least three times with increasing difficulty."
//
// A deck's words are shuffled once and chunked into rounds of
// ROUND_SIZE. Only the current round's words are in play — the rest of
// the deck isn't touched until this round is cleared, which is what
// keeps a single pass manageable instead of dumping a 40+ word deck into
// one session. Within a round, each word must be answered correctly at
// each of three STAGES, in order, before it's mastered and drops out:
//   1. Multiple choice, English shown -> pick the target-language term.
//   2. Multiple choice, target-language term shown -> pick the English
//      meaning (the reverse direction, so recognition is solid both ways
//      before asking for production).
//   3. Typed, English shown -> type the target-language term. The one
//      genuinely productive stage, so it's last.
// A wrong answer at any stage doesn't demote the word, just re-asks the
// same stage a few questions later (_requeue) rather than immediately —
// long enough that the answer isn't just sitting in short-term memory,
// short enough it isn't the following round. Passing a stage does the
// same: it doesn't re-ask stage 2 back-to-back with stage 1, it comes
// back around a few words later, which is the "gradual recall" this was
// built for, not just three ticks in a row.
// Once every word in the round is mastered, the next round starts
// automatically (new words, same rules) until the deck is done.
//
// Deliberately NOT the same thing as SRS review (engine/srs.js): this is
// an unscheduled, on-demand pass through THIS deck's words that resets
// every time it's opened and touches no review-scheduling data at all —
// answering here doesn't advance or reset a word's SRS interval. SRS
// still owns "when should I see this word next"; this is just "let me
// drill this deck right now."

const DeckLearn = (function () {
    'use strict';

    const ROUND_SIZE = 7; // words per round — Quizlet's own Learn mode uses roughly this, and it's the low end of the "seven, maximum ten" the feedback asked for
    const DECOY_COUNT = 3;
    const RETRY_DELAY = 3; // a requeued word reappears after roughly this many other questions, not immediately and not at the very end

    // Increasing difficulty, in order. `kind` is 'mc' or 'typed'; for
    // 'mc', `prompt`/`answer` say which field (lemma or translation) is
    // shown as the question vs. offered as multiple-choice options.
    const STAGES = [
        { kind: 'mc', prompt: 'translation', answer: 'lemma', label: 'Step 1 of 3 · Recognize it' },
        { kind: 'mc', prompt: 'lemma', answer: 'translation', label: 'Step 2 of 3 · Recall it' },
        { kind: 'typed', prompt: 'translation', answer: 'lemma', label: 'Step 3 of 3 · Produce it' }
    ];

    let _container = null;
    let _pool = [];      // every word in the deck — sourced for multiple-choice decoys regardless of which round is active
    let _rounds = [];     // [[word, ...], ...] — the deck chunked into ROUND_SIZE-word rounds
    let _roundIndex = 0;
    let _queue = [];      // this round's working set: [{ lemma, translation, pos, stage: 0|1|2 }], front = next question
    let _current = null;
    let _masteredThisRound = 0;
    let _masteredTotal = 0;
    let _seen = 0;
    let _correct = 0;
    let _onExit = null;
    let _solved = false; // true once the current question has been checked, before Next

    function _escapeHtml(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _withArticle(lemma) {
        return (typeof Lexicon !== 'undefined' && Lexicon.withArticle) ? Lexicon.withArticle(lemma) : lemma;
    }

    function _targetLabel() {
        return (typeof Lang !== 'undefined' && Lang.name) ? Lang.name() : 'the target language';
    }

    // Lenient on purpose: this grades free-typed ENGLISH meanings against a
    // gloss that's often several synonyms ("hello / hi", "to see, to
    // watch") — an exact-string match would fail a learner who typed a
    // perfectly good synonym.
    function _normaliseEnglish(text) {
        return String(text || '').toLowerCase().trim().replace(/^(to|a|an|the)\s+/, '');
    }

    // Strict on purpose, unlike the English grading above: accents are
    // checked for every language here, matching the standard the main
    // lesson flow settled on for the same reason (engine/lessons.js's
    // normalise(), 2026-08-27) — an accent is often the entire distinction
    // between two different target-language words, not typing friction to
    // wave through. Only Unicode representation (NFC) and surrounding
    // punctuation/whitespace are normalised; the accent itself never is.
    // Lenient about the article, though: a learner who typed the bare noun
    // without "el"/"la" still knew the word.
    function _normaliseTarget(text) {
        return String(text || '').toLowerCase().trim().replace(/[.,!?¡¿;:]/g, '').normalize('NFC');
    }

    function _gradeEnglish(input, translation) {
        const guess = _normaliseEnglish(input);
        if (!guess) return false;
        const alternatives = String(translation || '').split(/[\/,;]/).map(_normaliseEnglish).filter(Boolean);
        return alternatives.includes(guess);
    }

    function _gradeTarget(input, lemma) {
        const guess = _normaliseTarget(input);
        if (!guess) return false;
        return guess === _normaliseTarget(lemma) || guess === _normaliseTarget(_withArticle(lemma));
    }

    // ---- Round setup ----
    function _buildRounds() {
        const shuffledPool = _shuffled(_pool);
        _rounds = [];
        for (let i = 0; i < shuffledPool.length; i += ROUND_SIZE) {
            _rounds.push(shuffledPool.slice(i, i + ROUND_SIZE));
        }
        _roundIndex = 0;
        _masteredTotal = 0;
        _seen = 0;
        _correct = 0;
    }

    function _startRound() {
        _queue = _shuffled(_rounds[_roundIndex]).map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos, stage: 0 }));
        _masteredThisRound = 0;
    }

    function _requeue(word) {
        // Reinsert a few slots in rather than at the very front (an
        // immediate repeat is trivial to "answer" from short-term memory
        // alone) or the very back (too long a gap to reinforce anything).
        const at = Math.min(RETRY_DELAY, _queue.length);
        _queue.splice(at, 0, word);
    }

    function _decoysFor(word, n, field) {
        const candidates = _pool.filter(w => w.lemma !== word.lemma && w.translation !== word.translation);
        const seen = new Set();
        const out = [];
        _shuffled(candidates).forEach(w => {
            if (out.length >= n) return;
            const text = field === 'lemma' ? _withArticle(w.lemma) : w.translation;
            if (seen.has(text)) return;
            seen.add(text);
            out.push(text);
        });
        return out;
    }

    // ---- Rendering ----
    function _renderQuestion() {
        _current = _queue.shift();
        _solved = false;

        if (!_current) { _finishRound(); return; }

        const stage = STAGES[_current.stage];
        if (stage.kind === 'mc') {
            const decoys = _decoysFor(_current, DECOY_COUNT, stage.answer);
            if (decoys.length < 2) {
                // Not enough other words in this deck to build a fair
                // multiple-choice round at this stage — skip straight past
                // it rather than show a spuriously easy 1-option question,
                // so a tiny deck still runs, just with less friction.
                _current.stage++;
                if (_current.stage >= STAGES.length) {
                    _masteredThisRound++;
                    _masteredTotal++;
                } else {
                    _queue.unshift(_current);
                }
                _renderQuestion();
                return;
            }
            _renderChoice(decoys, stage);
            return;
        }
        _renderTyped(stage);
    }

    function _progressHtml() {
        const remaining = _queue.length + 1; // +1 for _current
        const stage = STAGES[_current.stage];
        return `
            <p class="dkl-round-line">Round ${_roundIndex + 1} of ${_rounds.length} ·
                ${_masteredTotal} of ${_pool.length} words learned</p>
            <p class="dkl-progress">${stage.label} · ${_masteredThisRound} mastered this round · ${remaining} left this round</p>
        `;
    }

    function _renderChoice(decoys, stage) {
        const promptText = stage.prompt === 'lemma' ? _withArticle(_current.lemma) : _current.translation;
        const correctAnswer = stage.answer === 'lemma' ? _withArticle(_current.lemma) : _current.translation;
        const options = _shuffled([correctAnswer, ...decoys]);
        _container.innerHTML = `
            <div class="dkl">
                <div class="dkl-head">
                    <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                </div>
                ${_progressHtml()}
                <p class="dkl-question">${_escapeHtml(promptText)}</p>
                <div class="dkl-options">
                    ${options.map((opt, i) => `<button class="dkl-option" data-learn-option="${i}">${_escapeHtml(opt)}</button>`).join('')}
                </div>
                <p class="dkl-feedback" aria-live="polite"></p>
                <div class="dkl-actions">
                    <button class="btn-primary hidden" data-learn-next="1">Next</button>
                </div>
            </div>
        `;
        const correctIndex = options.indexOf(correctAnswer);
        _container.querySelectorAll('[data-learn-option]').forEach((btn, i) => {
            btn.onclick = () => {
                if (_solved) return;
                _solved = true;
                _container.querySelectorAll('[data-learn-option]').forEach((b, j) => {
                    if (j === correctIndex) b.classList.add('is-correct');
                    else if (j === i) b.classList.add('is-wrong');
                    b.disabled = true;
                });
                _resolve(i === correctIndex, correctAnswer);
            };
        });
        _wireExitAndNext();
    }

    function _renderTyped(stage) {
        const promptText = stage.prompt === 'lemma' ? _withArticle(_current.lemma) : _current.translation;
        _container.innerHTML = `
            <div class="dkl">
                <div class="dkl-head">
                    <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                </div>
                ${_progressHtml()}
                <p class="dkl-question">${_escapeHtml(promptText)}</p>
                <input class="dkl-input" type="text" placeholder="Type it in ${_escapeHtml(_targetLabel())}"
                    autocomplete="off" autocapitalize="off" spellcheck="false">
                <p class="dkl-feedback" aria-live="polite"></p>
                <div class="dkl-actions">
                    <button class="btn-primary" data-learn-check="1">Check</button>
                    <button class="btn-primary hidden" data-learn-next="1">Next</button>
                </div>
            </div>
        `;
        const input = _container.querySelector('.dkl-input');
        input.focus();
        input.addEventListener('keydown', e => { if (e.key === 'Enter') _checkTyped(); });
        _container.querySelector('[data-learn-check]').onclick = _checkTyped;
        _wireExitAndNext();
    }

    function _checkTyped() {
        if (_solved) return;
        _solved = true;
        const input = _container.querySelector('.dkl-input');
        const ok = _gradeTarget(input.value, _current.lemma);
        input.disabled = true;
        input.classList.toggle('dkl-input-correct', ok);
        input.classList.toggle('dkl-input-wrong', !ok);
        if (!ok) input.value = _withArticle(_current.lemma);
        const checkBtn = _container.querySelector('[data-learn-check]');
        if (checkBtn) checkBtn.classList.add('hidden');
        _resolve(ok, _withArticle(_current.lemma));
    }

    function _resolve(ok, correctAnswerText) {
        _seen++;
        const feedback = _container.querySelector('.dkl-feedback');
        if (ok) {
            _correct++;
            _current.stage++;
            if (_current.stage >= STAGES.length) {
                _masteredThisRound++;
                _masteredTotal++;
                if (feedback) { feedback.textContent = '✓ Mastered!'; feedback.className = 'dkl-feedback dkl-feedback-correct'; }
            } else {
                if (feedback) { feedback.textContent = '✓ Correct!'; feedback.className = 'dkl-feedback dkl-feedback-correct'; }
                _requeue(_current);
            }
        } else {
            if (feedback) { feedback.textContent = `✗ ${correctAnswerText}`; feedback.className = 'dkl-feedback dkl-feedback-wrong'; }
            _requeue(_current);
        }
        const nextBtn = _container.querySelector('[data-learn-next]');
        if (nextBtn) nextBtn.classList.remove('hidden');
    }

    function _wireExitAndNext() {
        const exitBtn = _container.querySelector('[data-learn-exit]');
        if (exitBtn) exitBtn.onclick = () => { if (_onExit) _onExit(); };
        const nextBtn = _container.querySelector('[data-learn-next]');
        if (nextBtn) nextBtn.onclick = () => { _renderQuestion(); };
    }

    function _finishRound() {
        const isLastRound = _roundIndex >= _rounds.length - 1;
        if (isLastRound) { _renderResults(); return; }

        _container.innerHTML = `
            <div class="dkl">
                <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                <div class="dkl-done">
                    <p class="dkl-done-title">Round ${_roundIndex + 1} complete — ${_masteredThisRound} words mastered</p>
                    <p class="dkl-done-stat">${_masteredTotal} of ${_pool.length} words learned so far</p>
                    <div class="dkl-done-actions">
                        <button class="btn-primary" data-learn-continue="1">Start round ${_roundIndex + 2}</button>
                        <button class="dk-secondary" data-learn-exit="1">Back to deck</button>
                    </div>
                </div>
            </div>
        `;
        _container.querySelector('[data-learn-exit]').onclick = () => { if (_onExit) _onExit(); };
        _container.querySelector('[data-learn-continue]').onclick = () => {
            _roundIndex++;
            _startRound();
            _renderQuestion();
        };
    }

    function _renderResults() {
        const accuracy = _seen > 0 ? Math.round((_correct / _seen) * 100) : 0;
        _container.innerHTML = `
            <div class="dkl">
                <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                <div class="dkl-done">
                    <p class="dkl-done-title">All ${_masteredTotal} words learned!</p>
                    <p class="dkl-done-stat">${accuracy}% accuracy across ${_seen} questions · ${_rounds.length} round${_rounds.length === 1 ? '' : 's'}</p>
                    <div class="dkl-done-actions">
                        <button class="btn-primary" data-learn-restart="1">Learn again</button>
                        <button class="dk-secondary" data-learn-exit="1">Back to deck</button>
                    </div>
                </div>
            </div>
        `;
        _container.querySelector('[data-learn-exit]').onclick = () => { if (_onExit) _onExit(); };
        _container.querySelector('[data-learn-restart]').onclick = () => { _buildRounds(); _startRound(); _renderQuestion(); };
    }

    /**
     * @param {HTMLElement} root
     * @param {{ words: {lemma:string, translation:string, pos?:string}[], onExit: function }} options
     */
    function render(root, options) {
        _container = root;
        _pool = ((options && options.words) || []).filter(w => w && w.lemma && w.translation);
        _onExit = (options && options.onExit) || function () {};

        if (_pool.length < 2) {
            _container.innerHTML = `
                <div class="dkl">
                    <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                    <p class="dk-empty">Not enough words in this deck to learn yet.</p>
                </div>
            `;
            _container.querySelector('[data-learn-exit]').onclick = () => { if (_onExit) _onExit(); };
            return;
        }

        _buildRounds();
        _startRound();
        _renderQuestion();
    }

    return { render };
})();
