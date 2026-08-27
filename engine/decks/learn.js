// ============================================
// DECK LEARN MODE
// ============================================
// Adaptive practice through a deck's words: each word starts as
// multiple-choice (recognition), and only moves to a typed question
// (recall) once answered correctly there — a word is "mastered" and
// drops out of the round only after surviving BOTH. A wrong answer at
// either stage doesn't fail the word, it just re-queues it to come back
// around in a few questions rather than at the very end, so a missed
// word gets more repetition, not less.
//
// Deliberately NOT the same thing as SRS review (engine/srs.js): this is
// an unscheduled, on-demand pass through THIS deck's words that resets
// every time it's opened and touches no review-scheduling data at all —
// answering here doesn't advance or reset a word's SRS interval. SRS
// still owns "when should I see this word next"; this is just "let me
// drill this deck right now."

const DeckLearn = (function () {
    'use strict';

    const DECOY_COUNT = 3;
    const RETRY_DELAY = 3; // a missed word reappears after roughly this many other questions, not immediately and not at the very end

    let _container = null;
    let _pool = [];   // every word in the deck, for sourcing multiple-choice decoys
    let _queue = [];   // [{ lemma, translation, pos, stage: 'mc'|'typed' }] — working set, front = next question
    let _current = null;
    let _masteredCount = 0;
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

    // Lenient on purpose: this grades free-typed ENGLISH against a gloss
    // that's often several synonyms ("hello / hi", "to see, to watch") —
    // an exact-string match would fail a learner who typed a perfectly
    // good synonym. Accepts a match against any "/"- or ","-separated
    // alternative, with a leading "to "/"a "/"an "/"the " stripped from
    // both sides so "watch" matches "to watch" either direction.
    function _normaliseAnswer(text) {
        return String(text || '').toLowerCase().trim().replace(/^(to|a|an|the)\s+/, '');
    }

    function _gradeTyped(input, translation) {
        const guess = _normaliseAnswer(input);
        if (!guess) return false;
        const alternatives = String(translation || '').split(/[\/,;]/).map(_normaliseAnswer).filter(Boolean);
        return alternatives.includes(guess);
    }

    // ---- Queue setup ----
    function _buildQueue() {
        _queue = _shuffled(_pool).map(w => ({ lemma: w.lemma, translation: w.translation, pos: w.pos, stage: 'mc' }));
        _masteredCount = 0;
        _seen = 0;
        _correct = 0;
    }

    function _requeue(word) {
        // Reinsert a few slots in rather than at the very front (an
        // immediate repeat is trivial to "answer" from short-term memory
        // alone) or the very back (too long a gap to reinforce anything).
        const at = Math.min(RETRY_DELAY, _queue.length);
        _queue.splice(at, 0, word);
    }

    function _decoysFor(word, n) {
        const candidates = _pool.filter(w => w.lemma !== word.lemma && w.translation !== word.translation);
        return _shuffled(candidates).slice(0, n).map(w => w.translation);
    }

    // ---- Rendering ----
    function _renderQuestion() {
        _current = _queue.shift();
        _solved = false;

        if (!_current) { _renderResults(); return; }

        if (_current.stage === 'mc') {
            const decoys = _decoysFor(_current, DECOY_COUNT);
            if (decoys.length < DECOY_COUNT) {
                // Not enough other words in this deck to build a fair
                // multiple-choice round — fall through to typed instead of
                // showing a spuriously easy 1- or 2-option question.
                _current.stage = 'typed';
                _renderTyped();
                return;
            }
            _renderChoice(decoys);
            return;
        }
        _renderTyped();
    }

    function _progressHtml() {
        const remaining = _queue.length + 1; // +1 for _current
        return `<p class="dkl-progress">${_masteredCount} mastered · ${remaining} left this round</p>`;
    }

    function _renderChoice(decoys) {
        const options = _shuffled([_current.translation, ...decoys]);
        _container.innerHTML = `
            <div class="dkl">
                <div class="dkl-head">
                    <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                </div>
                ${_progressHtml()}
                <p class="dkl-question">${_escapeHtml(_withArticle(_current.lemma))}</p>
                <div class="dkl-options">
                    ${options.map((opt, i) => `<button class="dkl-option" data-learn-option="${i}">${_escapeHtml(opt)}</button>`).join('')}
                </div>
                <p class="dkl-feedback" aria-live="polite"></p>
                <div class="dkl-actions">
                    <button class="btn-primary hidden" data-learn-next="1">Next</button>
                </div>
            </div>
        `;
        const correctIndex = options.indexOf(_current.translation);
        _container.querySelectorAll('[data-learn-option]').forEach((btn, i) => {
            btn.onclick = () => {
                if (_solved) return;
                _solved = true;
                _container.querySelectorAll('[data-learn-option]').forEach((b, j) => {
                    if (j === correctIndex) b.classList.add('is-correct');
                    else if (j === i) b.classList.add('is-wrong');
                    b.disabled = true;
                });
                _resolve(i === correctIndex);
            };
        });
        _wireExitAndNext();
    }

    function _renderTyped() {
        _container.innerHTML = `
            <div class="dkl">
                <div class="dkl-head">
                    <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                </div>
                ${_progressHtml()}
                <p class="dkl-question">${_escapeHtml(_withArticle(_current.lemma))}</p>
                <input class="dkl-input" type="text" placeholder="Type the translation"
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
        const ok = _gradeTyped(input.value, _current.translation);
        input.disabled = true;
        input.classList.toggle('dkl-input-correct', ok);
        input.classList.toggle('dkl-input-wrong', !ok);
        if (!ok) input.value = _current.translation;
        const checkBtn = _container.querySelector('[data-learn-check]');
        if (checkBtn) checkBtn.classList.add('hidden');
        _resolve(ok);
    }

    function _resolve(ok) {
        _seen++;
        const feedback = _container.querySelector('.dkl-feedback');
        if (ok) {
            _correct++;
            if (feedback) { feedback.textContent = '✓ Correct!'; feedback.className = 'dkl-feedback dkl-feedback-correct'; }
            if (_current.stage === 'mc') {
                _current.stage = 'typed';
                _requeue(_current);
            } else {
                _masteredCount++;
            }
        } else {
            if (feedback) { feedback.textContent = `✗ ${_withArticle(_current.lemma)} = ${_current.translation}`; feedback.className = 'dkl-feedback dkl-feedback-wrong'; }
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

    function _renderResults() {
        const accuracy = _seen > 0 ? Math.round((_correct / _seen) * 100) : 0;
        _container.innerHTML = `
            <div class="dkl">
                <button class="dk-back" data-learn-exit="1">← Back to deck</button>
                <div class="dkl-done">
                    <p class="dkl-done-title">All ${_masteredCount} words learned!</p>
                    <p class="dkl-done-stat">${accuracy}% accuracy across ${_seen} questions</p>
                    <div class="dkl-done-actions">
                        <button class="btn-primary" data-learn-restart="1">Learn again</button>
                        <button class="dk-secondary" data-learn-exit="1">Back to deck</button>
                    </div>
                </div>
            </div>
        `;
        _container.querySelector('[data-learn-exit]').onclick = () => { if (_onExit) _onExit(); };
        _container.querySelector('[data-learn-restart]').onclick = () => { _buildQueue(); _renderQuestion(); };
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

        _buildQueue();
        _renderQuestion();
    }

    return { render };
})();
