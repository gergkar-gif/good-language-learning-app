// ============================================
// LISTENING RUNNER
// ============================================
// Renders one listening exercise: a Play/Replay button, then (once played)
// the answer control for whichever kind this item is, then Check -> reveal
// the full Spanish transcript and English translation -> Next.
//
// Not built on GrammarRunner, per PARLOUR_LISTENING_SPEC.md — audio has its
// own gating (nothing is answerable before the learner has actually
// listened) that doesn't belong in a text-exercise renderer, so this keeps
// its own normalise()/shuffle(), same reasoning GrammarRunner's own header
// comment gives for not sharing those with engine/verbs/table.js.
//
//   listen-choice:        { kind, audio, promptText, options, correct, transcript, translation }
//   listen-type:          { kind, audio, answer, transcript, translation }
//   listen-missing-word:  { kind, audio, sentence, answer, transcript, translation }

const ListeningRunner = (function () {
    'use strict';

    let _container = null;
    let _exercise  = null;
    let _onResult  = null;
    let _onNext    = null;
    let _solved    = false;
    let _played    = false;
    let _checkFn   = null;

    // ---- Helpers ----
    function _esc(text) {
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

    function _setFeedback(ok, message) {
        const el = _container.querySelector('.gd-feedback');
        if (!el) return;
        el.textContent = message;
        el.className = 'gd-feedback ' + (ok ? 'gd-feedback-correct' : 'gd-feedback-wrong');
    }

    // Shown after Check regardless of exercise kind — "reveal the transcript
    // after the answer" applies even to the choice types, which never show
    // any Spanish text before that point.
    function _reveal(ex) {
        const el = _container.querySelector('.lr-reveal');
        el.classList.remove('hidden');
        el.innerHTML = `
            <p class="lr-transcript">${_esc(ex.transcript)}</p>
            <p class="lr-translation">${_esc(ex.translation)}</p>
        `;
    }

    function _finish(ok, ex) {
        _setFeedback(ok, ok ? '✓ Correct!' : '✗ Not quite.');
        _reveal(ex);
        _resolve(ok);
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
    function _renderChoice(ex) {
        const pick = _shuffledOptions(ex.options, ex.correct);
        _container.querySelector('.lr-answer').innerHTML = `
            <p class="gd-question">${_esc(ex.promptText)}</p>
            <div class="gd-options">
                ${pick.options.map((option, i) => `
                    <button class="gd-option" data-index="${i}">${_esc(option)}</button>
                `).join('')}
            </div>
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

        _checkFn = () => {
            if (picked === null) { _setFeedback(false, 'Pick an answer first.'); return; }
            const ok = picked === pick.correct;
            _container.querySelectorAll('.gd-option').forEach((b, i) => {
                if (i === pick.correct) b.classList.add('correct');
                else if (i === picked) b.classList.add('wrong');
            });
            _finish(ok, ex);
        };
    }

    function _renderType(ex) {
        _container.querySelector('.lr-answer').innerHTML = `
            <input class="gd-input" type="text" placeholder="Type what you heard"
                autocomplete="off" autocapitalize="off" spellcheck="false">
        `;
        const input = _container.querySelector('.gd-input');
        input.addEventListener('keydown', e => { if (e.key === 'Enter') _doCheck(); });

        _checkFn = () => {
            const ok = _normalise(input.value) === _normalise(ex.answer);
            input.classList.toggle('gd-correct', ok);
            input.classList.toggle('gd-wrong', !ok);
            if (!ok) input.value = ex.answer;
            _finish(ok, ex);
        };
    }

    function _renderMissingWord(ex) {
        _container.querySelector('.lr-answer').innerHTML = `
            <p class="gd-question">${_esc(ex.sentence).replace(/_{2,}/, '<span class="gd-blank">?</span>')}</p>
            <input class="gd-input" type="text" placeholder="Type the missing word"
                autocomplete="off" autocapitalize="off" spellcheck="false">
        `;
        const input = _container.querySelector('.gd-input');
        input.addEventListener('keydown', e => { if (e.key === 'Enter') _doCheck(); });

        _checkFn = () => {
            const ok = _normalise(input.value) === _normalise(ex.answer);
            input.classList.toggle('gd-correct', ok);
            input.classList.toggle('gd-wrong', !ok);
            if (!ok) input.value = ex.answer;
            _finish(ok, ex);
        };
    }

    const renderers = {
        'listen-choice': _renderChoice,
        'listen-type': _renderType,
        'listen-missing-word': _renderMissingWord
    };

    // ---- Check/Play wiring ----
    function _doCheck() {
        if (_solved) return;
        // Audio is the primary information source (spec §3) — nothing is
        // gradeable until the learner has actually pressed Play at least once.
        if (!_played) { _setFeedback(false, 'Play the audio first.'); return; }
        if (_checkFn) _checkFn();
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
        _played    = false;
        _checkFn   = null;

        _container.innerHTML = `
            <div class="lr-audio">
                <button class="lr-play-btn" data-action="play">▶ Play</button>
            </div>
            <div class="lr-answer hidden"></div>
            <div class="lr-reveal hidden"></div>
            <p class="gd-feedback" aria-live="polite"></p>
            <div class="gd-actions">
                <button class="vbtn vbtn-primary" data-action="check">Check</button>
                <button class="vbtn vbtn-secondary hidden" data-action="next">Next</button>
            </div>
        `;

        const renderer = renderers[_exercise.kind];
        if (renderer) renderer(_exercise);

        const playBtn = _container.querySelector('[data-action="play"]');
        playBtn.addEventListener('click', () => {
            Speech.speak(_exercise.audio);
            // Unlimited replay, never penalised (spec §3) — this only fires
            // the reveal-the-answer-controls step once.
            if (!_played) {
                _played = true;
                _container.querySelector('.lr-answer').classList.remove('hidden');
            }
            playBtn.textContent = '↻ Replay';
        });

        _container.querySelector('[data-action="check"]').addEventListener('click', _doCheck);
        _container.querySelector('[data-action="next"]').addEventListener('click', () => _onNext());
        _wireEnterToCheck();
    }

    // An option button's own Enter just re-fires its click (re-selecting the
    // same option) rather than submitting — redirect it to Check instead.
    // Text inputs already wire Enter directly where they're rendered.
    // _container is the same node across exercises in one session (only its
    // innerHTML is replaced), so this is wired once rather than per exercise.
    function _wireEnterToCheck() {
        if (_container.dataset.enterWired) return;
        _container.dataset.enterWired = '1';
        _container.addEventListener('keydown', e => {
            if (e.key !== 'Enter' || !e.target.classList.contains('gd-option')) return;
            const checkBtn = _container.querySelector('[data-action="check"]');
            if (checkBtn && !checkBtn.disabled) {
                e.preventDefault();
                checkBtn.click();
            }
        });
    }

    return { render };
})();
