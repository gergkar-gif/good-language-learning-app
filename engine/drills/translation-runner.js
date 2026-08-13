// ============================================
// TRANSLATION RUNNER
// ============================================
// Renders one translation exercise: a source sentence, a text input, and a
// Check that reveals the model translation for the learner to compare
// against their own attempt — the same "show a model answer, let the
// learner judge it" philosophy engine/lessons.js already uses for
// structured-writing, applied here because a full sentence has too many
// valid phrasings for exact-string grading to be fair. The learner then
// self-rates ("Got it" / "Not quite"), which is what feeds the session
// score — nothing here grades automatically.
//
// Not built on GrammarRunner: that module's Check auto-grades a known-
// correct answer, which doesn't apply to open translation.

const TranslationRunner = (function () {
    'use strict';

    let _container = null;
    let _onResult  = null;
    let _onNext    = null;
    let _solved    = false;

    function _escapeHtml(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    // Next stays hidden until the learner has self-rated, not merely once
    // Check is pressed — Check only reveals the model translation, Got
    // it/Not quite is what actually resolves the exercise.
    function _resolve(correct) {
        if (_solved) return;
        _solved = true;
        const nextBtn = _container.querySelector('[data-action="next"]');
        if (nextBtn) nextBtn.classList.remove('hidden');
        if (_onResult) _onResult(correct);
    }

    function _reveal(exercise) {
        if (_solved) return; // one reveal per exercise — repeat clicks are no-ops
        const input = _container.querySelector('.td-input');
        input.disabled = true;

        _container.querySelector('.td-model-wrap').innerHTML = `
            <p class="td-model-label">Model translation</p>
            <p class="td-model">${_escapeHtml(exercise.model)}</p>
            <div class="td-self-rate">
                <button class="vbtn vbtn-primary" data-action="got-it">✓ Got it</button>
                <button class="vbtn vbtn-secondary" data-action="not-quite">✗ Not quite</button>
            </div>
        `;
        _container.querySelector('[data-action="check"]').classList.add('hidden');

        _container.querySelector('[data-action="got-it"]').addEventListener('click', () => {
            _container.querySelector('.td-self-rate').classList.add('td-rated');
            _resolve(true);
        });
        _container.querySelector('[data-action="not-quite"]').addEventListener('click', () => {
            _container.querySelector('.td-self-rate').classList.add('td-rated');
            _resolve(false);
        });
    }

    /**
     * @param {HTMLElement} root
     * @param {{ exercise:{prompt:string, model:string, promptLabel:string},
     *          onResult:function(boolean), onNext:function }} options
     */
    function render(root, options) {
        _container = root;
        _onResult  = options.onResult || function () {};
        _onNext    = options.onNext || function () {};
        _solved    = false;

        const exercise = options.exercise;

        _container.innerHTML = `
            <p class="td-source-label">${_escapeHtml(exercise.promptLabel)}</p>
            <p class="td-source">${_escapeHtml(exercise.prompt)}</p>
            <input class="td-input" type="text" placeholder="Type your translation"
                autocomplete="off" autocapitalize="off" spellcheck="false">
            <div class="td-model-wrap"></div>
            <div class="gd-actions">
                <button class="vbtn vbtn-primary" data-action="check">Check</button>
                <button class="vbtn vbtn-secondary hidden" data-action="next">Next</button>
            </div>
        `;

        _container.querySelector('.td-input').addEventListener('keydown', e => {
            if (e.key === 'Enter') _reveal(exercise);
        });
        _container.querySelector('[data-action="check"]').addEventListener('click', () => _reveal(exercise));
        _container.querySelector('[data-action="next"]').addEventListener('click', () => _onNext());
    }

    return { render };
})();
