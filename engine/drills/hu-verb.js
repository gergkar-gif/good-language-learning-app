// ============================================
// VERB DRILLER (Hungarian)
// ============================================
// A second, separate Verb Driller entry alongside the existing Spanish one
// in engine/workshop.js (same title, disjoint `langs`, so only one shows
// per course) — NOT a change to engine/verbs.js. That module hardcodes
// Spanish tense-path strings, a single global Spanish verb list, and
// Content.verb()'s imports/verbs/ path across three files; Hungarian's
// paradigm (no gender, indefinite/definite conjugation, a different tense
// inventory) doesn't fit through that pipe without breaking Spanish, so
// this is its own module with its own data and paradigm constants,
// following the Settings->Session->Results shell every other driller uses.
//
// Present tense, indefinite conjugation only, per
// engine/morphology/hungarian.js's conjugate() — see that function's own
// scope note. Definite conjugation and past tense aren't modelled yet;
// matches how far the A1 curriculum has reached (Unit 1 doesn't teach
// regular verb conjugation at all yet, only the irregular copula "van").
//
// Four exercise types from HUNGARIAN_WORKSHOP_IMPLEMENTATION_HANDOVER.md's
// Verb Driller section: recognition, selection, production, transformation.

const HuVerbDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;
    const MAX_LEMMA_RANK = 4000;

    // scripts/import_hu_dictionary.py generally filters out "form-of"
    // dictionary entries (inflected-form pages, not real lemmas) but keeps
    // a "noun-from-verb" exception for genuinely independent meanings
    // ("alvás" = "sleep", derived from "alszik") — some of those exceptions
    // still carry a leftover gloss like "present participle of költ:"
    // rather than a real translation (caught live testing this driller:
    // "költő" is really the noun "poet", not a conjugatable verb). Filter
    // those out here rather than treating any verb-tagged sense as safe to
    // conjugate.
    const FORM_OF_GLOSS = /\b(participle|verbal noun|gerund|imperative) of\b/i;

    // [person, number, pronoun] — no gendered 3rd person, matches
    // Hungarian's actual pronoun set.
    const PERSONS = [
        [1, 'sg', 'Én'], [2, 'sg', 'Te'], [3, 'sg', 'Ő'],
        [1, 'pl', 'Mi'], [2, 'pl', 'Ti'], [3, 'pl', 'Ők']
    ];

    let _phase = PHASE.SETTINGS;
    let _container = null;

    // Each entry: { lemma, gloss, forms: [{person, number, pronoun, form}] }
    let _verbs = null;

    let _mode = MODE.COUNT;
    let _questionCount = 10;
    let _timerMinutes = 2;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;

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
        if (_verbs) return;
        const [dict] = await Promise.all([
            fetch('imports/dictionary/hungarian-en.json').then(r => r.ok ? r.json() : {}),
            Lexicon.load()
        ]);

        _verbs = [];
        for (const lemma in dict) {
            const rank = Lexicon.frequencyRank(lemma);
            if (rank === null || rank >= MAX_LEMMA_RANK) continue;
            const sense = HungarianMorphology.verbSense(dict[lemma]);
            if (!sense || FORM_OF_GLOSS.test(sense.en)) continue;

            const forms = PERSONS.map(([person, number, pronoun]) => ({
                person, number, pronoun,
                form: HungarianMorphology.conjugate(lemma, { tense: 'pres', person, number })
            })).filter(f => f.form);
            if (forms.length < PERSONS.length) continue; // skip anything conjugate() couldn't fill in

            _verbs.push({ lemma, gloss: sense.en, forms });
        }
    }

    // ---- Exercise builders -> GrammarRunner shapes ----
    function _personLabel(f) {
        return HungarianMorphology.personLabel(f.person, f.number);
    }

    // 1. Recognition — a conjugated form -> which person is it.
    function _buildRecognition(verb) {
        const target = _sample(verb.forms);
        const decoys = _shuffled(verb.forms.filter(f => f !== target)).slice(0, DECOY_COUNT);
        const options = _shuffled([target, ...decoys]).map(_personLabel);
        return {
            kind: 'multiple-choice',
            question: `"${target.form}" — which person is this?`,
            options,
            correct: options.indexOf(_personLabel(target)),
            explanation: `${verb.lemma} = ${verb.gloss}`
        };
    }

    // 2. Selection — fill in the sentence with the right person's form.
    function _buildSelection(verb) {
        const target = _sample(verb.forms);
        const decoys = _shuffled(verb.forms.filter(f => f !== target)).slice(0, DECOY_COUNT);
        const options = _shuffled([target, ...decoys]).map(f => f.form);
        return {
            kind: 'multiple-choice',
            question: `${target.pronoun} ___.`,
            options,
            correct: options.indexOf(target.form),
            explanation: `${verb.lemma} = ${verb.gloss}`
        };
    }

    // 3. Production — lemma + person prompt -> type the form.
    function _buildProduction(verb) {
        const target = _sample(verb.forms);
        return {
            kind: 'fill-blank',
            sentence: `"${verb.lemma}" (${verb.gloss}), ${_personLabel(target)} (${target.pronoun}) = ______`,
            answer: target.form
        };
    }

    // 4. Transformation — one person's form given, produce another's.
    function _buildTransformation(verb) {
        const [from, to] = _shuffled(verb.forms).slice(0, 2);
        if (!from || !to || from === to) return null;
        return {
            kind: 'fill-blank',
            sentence: `${from.pronoun} ${from.form} → ${to.pronoun} ______`,
            answer: to.form,
            explanation: `${verb.lemma} = ${verb.gloss}`
        };
    }

    const BUILDERS = [_buildRecognition, _buildSelection, _buildProduction, _buildTransformation];

    function _buildExerciseFor(verb) {
        const candidates = BUILDERS.map(fn => fn(verb)).filter(Boolean);
        return candidates.length ? _sample(candidates) : null;
    }

    function _buildPool() {
        return _shuffled(_verbs).slice(0, 300).map(_buildExerciseFor).filter(Boolean);
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
        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Verb Driller</h2>
                <p class="gd-hint">Decode and produce Hungarian verb forms — present tense, indefinite
                    conjugation. Draws from the full dictionary rather than just your lessons so far.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="hv-count">Number of questions</label>
                        <select id="hv-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} questions</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="hv-timer">Timer</label>
                        <select id="hv-timer" class="vb-select">
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

        const countSelect = _container.querySelector('#hv-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#hv-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool();
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No verbs available yet.</div>
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

    function _tick() {
        const remaining = Math.max(0, Math.ceil((_endTime - Date.now()) / 1000));
        _timeRemaining = remaining;
        const el = _container.querySelector('.vspeed-timer-display');
        if (el) el.textContent = _formatTime(remaining);
        if (remaining <= 0) _finishSession();
    }

    function _scoreLabel() {
        const base = `${_correct}/${_seen} correct`;
        return _mode === MODE.COUNT ? `${base} · Question ${_queueIndex + 1} of ${_queue.length}` : base;
    }

    function _renderSession() {
        _container.innerHTML = `
            <div class="gd-hud">
                <span class="gd-hud-score">${_scoreLabel()}</span>
                ${_mode === MODE.TIMED ? `<span class="vspeed-timer-display">${_formatTime(_timeRemaining)}</span>` : ''}
                <button class="gd-change-skill" data-action="change-settings">Change settings</button>
            </div>
            <div class="gd-exercise"></div>
        `;
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const exerciseRoot = _container.querySelector('.gd-exercise');
        GrammarRunner.render(exerciseRoot, {
            exercise: _queue[_queueIndex],
            onResult: correct => {
                _seen++;
                if (correct) _correct++;
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
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-primary" data-action="play-again">Play Again</button>
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>
                </div>
            </div>
        `;

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
    }

    function _abortSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    async function render(root) {
        _container = root;

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            _renderSettings();
        } else if (_phase === PHASE.SESSION) {
            _renderSession();
        } else {
            _renderResults();
        }
    }

    return { render };
})();
