// ============================================
// GRAMMAR RUNNER
// ============================================
// Renders one grammar exercise at a time and checks the answer. Mirrors
// engine/verbs/table.js: a self-contained render(root, options) with its own
// Check -> feedback -> Next flow. Deliberately not shared with
// engine/lessons.js's stepRenderers — this is free practice (no attempt
// limit, no Continue-button gate, wrong answers just reveal the right one
// and the learner moves on whenever they like), where lessons.js's renderers
// are built around gating a lesson's Continue button. Same reason
// engine/verbs/table.js keeps its own normalise()/shuffle() rather than
// importing lessons.js's.
//
// GrammarDriller normalises every exercise (bank item or lesson exercise)
// into one of the shapes below before calling render(); this module only
// ever sees the normalised form, never the raw content-file shape.
//
//   multiple-choice:   { kind, question, options, correct, explanation? }
//   fill-blank:        { kind, sentence, answer, explanation? }
//   sentence-builder:  { kind, tiles, solution, english? }
//   sentence-order:    { kind, sentences, solution }
//   dialogue-complete: { kind, prompt, options, correct }
//   error-correction:  { kind, sentence, solution, explanation? }

const GrammarRunner = (function () {
    'use strict';

    let _container = null;
    let _exercise  = null;
    let _onResult  = null;
    let _onNext    = null;
    let _solved    = false;

    // ---- Helpers ----
    function _escapeHtml(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _normalise(text) {
        return String(text || '').toLowerCase().trim()
            .replace(/[.,!?¡¿;:]/g, '')
            .normalize('NFD').replace(/[̀-ͯ]/g, '');
    }

    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _shuffledOptions(options, correct) {
        const order = _shuffled(options.map((text, i) => ({ text, i })));
        return {
            options: order.map(o => o.text),
            correct: order.findIndex(o => o.i === correct)
        };
    }

    function _feedbackHtml() {
        return `<p class="gd-feedback" aria-live="polite"></p>`;
    }

    function _setFeedback(ok, message) {
        const el = _container.querySelector('.gd-feedback');
        if (!el) return;
        el.textContent = message;
        el.className = 'gd-feedback ' + (ok ? 'gd-feedback-correct' : 'gd-feedback-wrong');
    }

    function _explanationHtml(explanation) {
        return explanation
            ? `<p class="gd-explanation">${_escapeHtml(explanation)}</p>`
            : '';
    }

    // Next starts hidden — showing both buttons at once let a learner skip
    // straight past an answer without ever seeing whether they were right.
    // _resolve() (called by every renderer once it knows the result) swaps
    // them, so the flow is always Check -> see the answer -> Next.
    function _actionsHtml() {
        return `
            <div class="gd-actions">
                <button class="vbtn vbtn-primary" data-action="check">Check</button>
                <button class="vbtn vbtn-secondary hidden" data-action="next">Next</button>
            </div>
        `;
    }

    function _resolve(correct) {
        if (_solved) return;
        _solved = true;
        const checkBtn = _container.querySelector('[data-action="check"]');
        const nextBtn = _container.querySelector('[data-action="next"]');
        if (checkBtn) checkBtn.classList.add('hidden');
        if (nextBtn) nextBtn.classList.remove('hidden');
        if (_onResult) _onResult(correct);
    }

    // ---- Renderers, one per kind ----
    const renderers = {
        'multiple-choice': _renderMultipleChoice,
        'dialogue-complete': _renderDialogueComplete,
        'fill-blank': _renderFillBlank,
        'sentence-builder': _renderSentenceBuilder,
        'sentence-order': _renderSentenceOrder,
        'error-correction': _renderErrorCorrection
    };

    function _renderMultipleChoice(ex) {
        const pick = _shuffledOptions(ex.options, ex.correct);
        _container.innerHTML = `
            <p class="gd-question">${_escapeHtml(ex.question)}</p>
            <div class="gd-options">
                ${pick.options.map((option, i) => `
                    <button class="gd-option" data-index="${i}">${_escapeHtml(option)}</button>
                `).join('')}
            </div>
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;

        let picked = null;
        _container.querySelectorAll('.gd-option').forEach(btn => {
            btn.addEventListener('click', () => {
                if (_solved) return;
                _container.querySelectorAll('.gd-option').forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                picked = Number(btn.dataset.index);
            });
        });

        _onCheck(() => {
            if (picked === null) { _setFeedback(false, 'Pick an answer first.'); return; }
            const ok = picked === pick.correct;
            _container.querySelectorAll('.gd-option').forEach((b, i) => {
                if (i === pick.correct) b.classList.add('correct');
                else if (i === picked) b.classList.add('wrong');
            });
            _setFeedback(ok, ok ? '✓ Correct!' : '✗ Not quite.');
            if (ex.explanation) _container.insertAdjacentHTML('beforeend', _explanationHtml(ex.explanation));
            _resolve(ok);
        });
    }

    function _renderDialogueComplete(ex) {
        const pick = _shuffledOptions(ex.options, ex.correct);
        _container.innerHTML = `
            <div class="gd-dialogue">
                ${(ex.prompt || []).map(line => `
                    <div class="gd-dialogue-line">
                        <span class="gd-dialogue-speaker">${_escapeHtml(line.speaker)}</span>
                        <span>${_escapeHtml(line.text)}</span>
                    </div>
                `).join('')}
            </div>
            <p class="gd-question">Choose the missing line:</p>
            <div class="gd-options">
                ${pick.options.map((option, i) => `
                    <button class="gd-option" data-index="${i}">${_escapeHtml(option)}</button>
                `).join('')}
            </div>
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;

        let picked = null;
        _container.querySelectorAll('.gd-option').forEach(btn => {
            btn.addEventListener('click', () => {
                if (_solved) return;
                _container.querySelectorAll('.gd-option').forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                picked = Number(btn.dataset.index);
            });
        });

        _onCheck(() => {
            if (picked === null) { _setFeedback(false, 'Pick an answer first.'); return; }
            const ok = picked === pick.correct;
            _container.querySelectorAll('.gd-option').forEach((b, i) => {
                if (i === pick.correct) b.classList.add('correct');
                else if (i === picked) b.classList.add('wrong');
            });
            _setFeedback(ok, ok ? '✓ Correct!' : '✗ Not quite.');
            _resolve(ok);
        });
    }

    function _renderFillBlank(ex) {
        _container.innerHTML = `
            <p class="gd-question">${_escapeHtml(ex.sentence).replace(/_{2,}/, '<span class="gd-blank">?</span>')}</p>
            <input class="gd-input" type="text" placeholder="Type the missing word"
                autocomplete="off" autocapitalize="off" spellcheck="false">
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;

        const input = _container.querySelector('.gd-input');
        input.addEventListener('keydown', e => { if (e.key === 'Enter') _doCheck(); });

        _onCheck(() => {
            const ok = _normalise(input.value) === _normalise(ex.answer);
            input.classList.toggle('gd-correct', ok);
            input.classList.toggle('gd-wrong', !ok);
            if (!ok) input.value = ex.answer;
            _setFeedback(ok, ok ? '✓ Correct!' : `✗ The answer was "${ex.answer}".`);
            if (ex.explanation) _container.insertAdjacentHTML('beforeend', _explanationHtml(ex.explanation));
            _resolve(ok);
        });
    }

    function _renderErrorCorrection(ex) {
        _container.innerHTML = `
            <p class="gd-question">Fix the mistake:</p>
            <p class="gd-broken-sentence">${_escapeHtml(ex.sentence)}</p>
            <input class="gd-input" type="text" placeholder="Type the corrected sentence"
                autocomplete="off" autocapitalize="off" spellcheck="false">
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;

        const input = _container.querySelector('.gd-input');
        input.addEventListener('keydown', e => { if (e.key === 'Enter') _doCheck(); });

        _onCheck(() => {
            const ok = _normalise(input.value) === _normalise(ex.solution);
            input.classList.toggle('gd-correct', ok);
            input.classList.toggle('gd-wrong', !ok);
            if (!ok) input.value = ex.solution;
            _setFeedback(ok, ok ? '✓ Correct!' : `✗ The correct sentence was "${ex.solution}".`);
            if (ex.explanation) _container.insertAdjacentHTML('beforeend', _explanationHtml(ex.explanation));
            _resolve(ok);
        });
    }

    // ---- Sentence builder (tap tiles into place) ----
    function _renderSentenceBuilder(ex) {
        const tiles = _shuffled((ex.tiles || []).map((text, i) => ({ text, i })));
        let built = [];

        function tileText(i) { const t = tiles.find(t => t.i === i); return t ? t.text : ''; }

        function bankHtml() {
            return tiles.map(t => {
                const used = built.includes(t.i);
                return `<button class="gd-tile${used ? ' used' : ''}" data-add="${t.i}"${used ? ' disabled' : ''}>${_escapeHtml(t.text)}</button>`;
            }).join('');
        }

        function targetHtml() {
            if (!built.length) return '<span class="gd-target-empty">Tap the words below.</span>';
            return built.map((i, pos) => `<button class="gd-tile" data-remove="${pos}">${_escapeHtml(tileText(i))}</button>`).join('');
        }

        function redraw() {
            _container.querySelector('.gd-build-target').innerHTML = targetHtml();
            _container.querySelector('.gd-build-bank').innerHTML = bankHtml();
            attachTileEvents();
        }

        function attachTileEvents() {
            _container.querySelectorAll('[data-add]').forEach(btn => {
                btn.addEventListener('click', () => {
                    if (_solved) return;
                    built.push(Number(btn.dataset.add));
                    redraw();
                });
            });
            _container.querySelectorAll('[data-remove]').forEach(btn => {
                btn.addEventListener('click', () => {
                    if (_solved) return;
                    built.splice(Number(btn.dataset.remove), 1);
                    redraw();
                });
            });
        }

        _container.innerHTML = `
            <p class="gd-question">Build the sentence.</p>
            <div class="gd-build-target">${targetHtml()}</div>
            <div class="gd-build-bank gd-tiles">${bankHtml()}</div>
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;
        attachTileEvents();

        _onCheck(() => {
            const sentence = built.map(tileText).join(' ');
            const ok = _normalise(sentence) === _normalise((ex.solution || []).join(' '));

            _container.querySelector('.gd-build-target').innerHTML =
                `<span class="gd-built ${ok ? 'gd-correct' : 'gd-wrong'}">${_escapeHtml((ex.solution || []).join(' '))}</span>`;
            _container.querySelector('.gd-build-bank').innerHTML = '';

            if (ex.english) {
                _container.insertAdjacentHTML('afterbegin',
                    `<p class="gd-build-english">${_escapeHtml(ex.english)}</p>`);
            }

            _setFeedback(ok, ok ? '✓ Correct!' : '✗ Not quite — the right sentence is shown above.');
            _resolve(ok);
        });
    }

    // ---- Sentence order (tap sentences into sequence) ----
    function _renderSentenceOrder(ex) {
        let order = [];

        _container.innerHTML = `
            <p class="gd-question">Tap the sentences in the right order.</p>
            <div class="gd-options">
                ${_shuffled((ex.sentences || []).map((text, i) => ({ text, i }))).map(item => `
                    <button class="gd-option" data-index="${item.i}">${_escapeHtml(item.text)}</button>
                `).join('')}
            </div>
            ${_feedbackHtml()}
            ${_actionsHtml()}
        `;

        _container.querySelectorAll('.gd-option').forEach(btn => {
            btn.addEventListener('click', () => {
                if (_solved || btn.classList.contains('used')) return;
                btn.classList.add('used');
                order.push(Number(btn.dataset.index));
                btn.textContent = order.length + '. ' + btn.textContent;
            });
        });

        _onCheck(() => {
            const ok = order.length === (ex.solution || []).length
                && order.every((v, i) => v === ex.solution[i]);

            if (!ok) {
                _container.querySelector('.gd-options').insertAdjacentHTML('afterend', `
                    <div class="gd-reveal">
                        ${(ex.solution || []).map((i, pos) => `<div>${pos + 1}. ${_escapeHtml(ex.sentences[i])}</div>`).join('')}
                    </div>
                `);
            }

            _setFeedback(ok, ok ? '✓ Correct order!' : '✗ Not the right order — shown below.');
            _resolve(ok);
        });
    }

    // ---- Check/Next wiring ----
    let _checkHandler = null;
    function _onCheck(fn) { _checkHandler = fn; }
    function _doCheck() { if (_solved) return; if (_checkHandler) _checkHandler(); }

    function _attachActions() {
        const checkBtn = _container.querySelector('[data-action="check"]');
        const nextBtn = _container.querySelector('[data-action="next"]');
        if (checkBtn) checkBtn.addEventListener('click', _doCheck);
        if (nextBtn) nextBtn.addEventListener('click', () => { if (_onNext) _onNext(); });
    }

    // ---- Public API ----
    /**
     * @param {HTMLElement} root
     * @param {{ exercise:Object, onResult:function(boolean), onNext:function }} options
     */
    function render(root, options) {
        _container = root;
        _exercise  = options.exercise;
        _onResult  = options.onResult || function () {};
        _onNext    = options.onNext || function () {};
        _solved    = false;
        _checkHandler = null;

        const renderer = renderers[_exercise.kind];
        if (!renderer) {
            root.innerHTML = `<p class="gd-empty">This exercise type is not supported yet.</p>${_actionsHtml()}`;
            _attachActions();
            return;
        }

        renderer(_exercise);
        _attachActions();
    }

    return { render };
})();
