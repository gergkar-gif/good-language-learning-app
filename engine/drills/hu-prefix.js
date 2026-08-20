// ============================================
// PREFIX DRILLER (Hungarian)
// ============================================
// Hungarian's separable verbal prefixes (meg-, el-, ki-, be-, ...). The
// first version of this driller synthesised prefix+verb pairs by simple
// concatenation (any of the 15 prefixes onto any bare verb lemma) — wrong,
// caught by live testing turning up sentences like "emlékezik" + "át-" =
// "átemlékezik", which isn't a real Hungarian word. Prefix+verb combination
// in Hungarian isn't freely compositional (same reason "look up" and
// "look into" are real English phrasal verbs but "look sideways-under"
// isn't just because the pieces exist) — only specific pairs are attested,
// real words with real meanings.
//
// So instead: only pairs where BOTH the prefixed form and its bare stem
// are independent headwords in imports/dictionary/hungarian-en.json are
// used, and the prefixed form's own dictionary gloss is the answer for
// "what does this mean" — never a composed guess. That still leaves 1,000+
// attested pairs (checked directly against the dictionary file, 2026-08-19)
// to draw from. No A1 curriculum backing exists for this yet — prefixes
// only get "limited high-frequency exposure" in A1, the full system is an
// A2 topic — so like the Suffix Driller this runs dictionary-wide.
//
// Not in v1: prefix movement ("Bemegyek" vs "Megyek be") — the design doc
// itself calls this optional for a first pass.

const HuPrefixDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;
    const MAX_LEMMA_RANK = 5000;

    // Same leak hu-verb.js already had to filter (2026-08-19): a dictionary
    // entry can carry a verb-tagged sense that's really a leftover
    // "participle of X:"/"verbal noun of X:" gloss, not a real translation
    // ("költő" = the noun "poet", not a conjugatable verb, despite
    // verbSense() finding a verb-tagged sense on it). hu-verb.js filters
    // this after calling verbSense(); this file called the same function on
    // both halves of every prefix pair without it — found auditing this
    // driller against the fix already made in its sibling (2026-08-20).
    const FORM_OF_GLOSS = /\b(participle|verbal noun|gerund|imperative) of\b/i;

    // VERB_PREFIXES' own sense text is written for the Reader's tap-word
    // popup, where a qualifier reads fine alongside the whole surrounding
    // explanation. Every entry there is already a short word/phrase except
    // "meg" (Hungarian's single most common verb prefix, so this shows up
    // constantly), whose sense is dense enough to read as broken quiz copy
    // ("Which prefix means 'completive — often "up"/"through"/"done"'?").
    // Overridden here for display only — engine/morphology/hungarian.js's
    // own table is untouched, so the Reader's explanation is unaffected.
    const QUIZ_SENSE_OVERRIDE = { meg: 'completive, up/through/done' };
    function _quizSense(prefix) {
        return QUIZ_SENSE_OVERRIDE[prefix.prefix] || prefix.sense;
    }

    let _phase = PHASE.SETTINGS;
    let _container = null;

    let _prefixes = null; // [{prefix, sense}], longest prefix first
    // Each entry: an attested pair, both halves real dictionary headwords.
    let _pairs = null;    // [{prefix, sense, bareLemma, bareGloss, prefixedLemma, prefixedGloss}]

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
        if (_prefixes && _pairs) return;
        const [dict] = await Promise.all([
            fetch('imports/dictionary/hungarian-en.json').then(r => r.ok ? r.json() : {}),
            Lexicon.load()
        ]);

        // Longest-first, same reason VERB_PREFIXES itself is sorted that
        // way: "elő-" must be tried before "el-" or "előmegy" would be
        // mis-split as "el" + "őmegy".
        _prefixes = HungarianMorphology.prefixList().sort((a, b) => b.prefix.length - a.prefix.length);

        _pairs = [];
        for (const lemma in dict) {
            const rank = Lexicon.frequencyRank(lemma);
            if (rank === null || rank >= MAX_LEMMA_RANK) continue;
            const prefixedSense = HungarianMorphology.verbSense(dict[lemma]);
            if (!prefixedSense || FORM_OF_GLOSS.test(prefixedSense.en)) continue;

            for (const p of _prefixes) {
                if (!lemma.startsWith(p.prefix) || lemma.length - p.prefix.length < 2) continue;
                const bareLemma = lemma.slice(p.prefix.length);
                const bareSense = HungarianMorphology.verbSense(dict[bareLemma]);
                if (!bareSense || FORM_OF_GLOSS.test(bareSense.en)) continue; // only pairs where the bare verb is ALSO a real, genuine headword
                _pairs.push({
                    prefix: p.prefix, sense: p.sense,
                    bareLemma, bareGloss: Lexicon.shortGloss(bareSense.en),
                    prefixedLemma: lemma, prefixedGloss: Lexicon.shortGloss(prefixedSense.en)
                });
                break; // longest matching prefix wins, don't also try shorter ones
            }
        }
    }

    // ---- Exercise builders -> GrammarRunner shapes ----
    function _decoyPrefixes(correct, n) {
        const candidates = _prefixes.filter(p => p.prefix !== correct);
        return _shuffled(candidates).slice(0, n).map(p => p.prefix);
    }

    // 1. Meaning -> prefix. Doesn't need a verb pairing at all — just the
    // prefix table itself, so always safe regardless of dictionary data.
    function _buildMeaningToPrefix(prefix) {
        const decoys = _decoyPrefixes(prefix.prefix, DECOY_COUNT);
        const options = _shuffled([prefix.prefix, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `Which prefix means "${_quizSense(prefix)}"?`,
            options,
            correct: options.indexOf(prefix.prefix)
        };
    }

    // 2. Form -> meaning. The prefixed word's own dictionary gloss is the
    // answer — a real translation, not a composed guess — so decoys are
    // OTHER pairs' real prefixed-form glosses, never invented text.
    function _buildFormToMeaning(pair, pool) {
        const decoys = _shuffled(pool.filter(p => p.prefixedGloss !== pair.prefixedGloss))
            .slice(0, DECOY_COUNT).map(p => p.prefixedGloss);
        if (decoys.length < DECOY_COUNT) return null;
        const options = _shuffled([pair.prefixedGloss, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `What does "${pair.prefixedLemma}" mean?`,
            options,
            correct: options.indexOf(pair.prefixedGloss),
            explanation: `${pair.bareLemma} (${pair.bareGloss}) + "${pair.prefix}-" (${_quizSense(pair)})`
        };
    }

    // 3. Construction. Both halves are real dictionary headwords and the
    // combination itself is an attested word, verified at load time — so
    // the expected answer is never a synthesised guess.
    function _buildConstruction(pair) {
        return {
            kind: 'fill-blank',
            sentence: `"${pair.bareLemma}" (${pair.bareGloss}) + "${pair.prefix}-" (${_quizSense(pair)}) = ______`,
            answer: pair.prefixedLemma,
            explanation: `${pair.prefixedLemma} = ${pair.prefixedGloss}`
        };
    }

    function _buildExerciseFor(pair, pool) {
        const candidates = [_buildMeaningToPrefix(pair), _buildFormToMeaning(pair, pool), _buildConstruction(pair)]
            .filter(Boolean);
        return _sample(candidates);
    }

    function _buildPool() {
        const pool = _pairs;
        return _shuffled(pool).slice(0, 300).map(p => _buildExerciseFor(p, pool)).filter(Boolean);
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
                <h2 class="gd-title">Prefix Driller</h2>
                <p class="gd-hint">Meaning and construction for Hungarian's separable verb prefixes
                    (meg-, el-, ki-, be-, ...). Draws from the full dictionary — prefixes get only light
                    coverage in the early lessons, so this runs ahead of the curriculum.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="hp-count">Number of questions</label>
                        <select id="hp-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} questions</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="hp-timer">Timer</label>
                        <select id="hp-timer" class="vb-select">
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

        const countSelect = _container.querySelector('#hp-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#hp-timer');
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
