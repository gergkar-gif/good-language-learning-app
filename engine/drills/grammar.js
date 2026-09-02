// ============================================
// GRAMMAR DRILLER
// ============================================
// Draws practice from two sources, both already authored — nothing here
// needs new content to work:
//   1. content/es/drills/grammar/*.json — a dedicated skill-organised bank
//      (today: a1-bank.json, 41 modules, 600 multiple-choice items).
//   2. content/es/exercises/**/*.json — the same category:"grammar",
//      `teaches`-tagged exercises engine/recycle.js already recycles,
//      looked up through content/<lang>/indexes/grammar-index.json (built
//      per-course by scripts/build_grammar_index.py — any new grammar
//      exercise joins the pool the next time that script runs, no further
//      wiring needed).
//
// The browsable skill list is the bank's modules — a clean, curated
// catalogue. Each module is opportunistically enriched with lesson
// exercises whose `teaches` tag matches the module id (underscores
// normalised to hyphens: ser_estar -> ser-estar). Modules with no such
// match still work — they just run bank-only.
//
// Two session modes, same split as engine/verbs.js's Table/Speed switcher:
//   Count — answer a fixed number of questions, then see results.
//   Timed — race a countdown; whatever you've answered when it hits zero
//   is the result. Reuses engine/verbs/speed.js's timer/results markup
//   (.vspeed-*) rather than duplicating it under a gd- name.

const GrammarDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];

    let _phase = PHASE.SETTINGS;
    let _container = null;

    let _index = null;   // content/<lang>/indexes/grammar-index.json -> { bySkill }
    let _bank  = null;   // content/es/drills/grammar/a1-bank.json

    let _mode = MODE.COUNT;
    let _selectedModule = 'mixed';
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

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_index && _bank) return;
        const [index, bank] = await Promise.all([
            Content.json(Lang.content('indexes/grammar-index.json')).catch(() => ({ bySkill: {} })),
            Content.json(Lang.content('drills/grammar/a1-bank.json')).catch(() => ({ modules: [], items: [] }))
        ]);
        _index = index;
        _bank = bank;
    }

    function _lessonSkillFor(moduleId) {
        return moduleId.replace(/_/g, '-');
    }

    function _lessonPoolSize(moduleId) {
        const entries = _index.bySkill[_lessonSkillFor(moduleId)];
        return entries ? entries.length : 0;
    }

    // ---- Normalisation: raw content shapes -> GrammarRunner's shapes ----
    function _normaliseBankItem(item) {
        return {
            kind: 'multiple-choice',
            question: item.prompt,
            options: item.options,
            correct: item.options.indexOf(item.answer),
            explanation: item.explanation
        };
    }

    function _normaliseLessonExercise(ex) {
        switch (ex.type) {
            case 'multiple-choice':
                return { kind: 'multiple-choice', question: ex.question, options: ex.options, correct: ex.correct };
            case 'dialogue-complete':
                return { kind: 'dialogue-complete', prompt: ex.prompt, options: ex.options, correct: ex.correct };
            case 'fill-blank':
                return { kind: 'fill-blank', sentence: ex.sentence, answer: ex.answer };
            case 'sentence-builder':
                return { kind: 'sentence-builder', tiles: ex.tiles, solution: ex.solution, english: ex.english };
            case 'sentence-order':
                return { kind: 'sentence-order', sentences: ex.sentences, solution: ex.solution };
            case 'error-correction':
                return { kind: 'error-correction', sentence: ex.sentence, solution: ex.solution, explanation: ex.explanation };
            default:
                return null;
        }
    }

    // Fetches every lesson exercise file a set of index entries points at
    // (each once, via Content's own cache) and resolves each entry to its
    // actual exercise object.
    async function _resolveLessonEntries(entries) {
        const refs = [...new Set(entries.map(e => e.ref))];
        const files = await Promise.all(refs.map(ref =>
            Content.json(Lang.content(ref)).catch(() => ({ exercises: [] }))
        ));
        const byRef = {};
        refs.forEach((ref, i) => { byRef[ref] = files[i]; });

        const resolved = [];
        const seenIds = new Set();
        for (const entry of entries) {
            if (seenIds.has(entry.id)) continue; // same exercise, more than one matching teaches tag
            const file = byRef[entry.ref];
            const ex = (file.exercises || []).find(e => e.id === entry.id);
            if (!ex) continue;
            const normalised = _normaliseLessonExercise(ex);
            if (normalised) { resolved.push(normalised); seenIds.add(entry.id); }
        }
        return resolved;
    }

    // "Mixed" flattens every skill's lesson-exercise entries — 7000+ of them
    // across 550+ skills, pointing at 650+ distinct exercise files — even
    // though a session only ever needs a few dozen questions at most. Fetching
    // every one of those files up front (_resolveLessonEntries did exactly
    // that) was the "10 random exercises takes a while to load" report: the
    // pool-building cost scaled with the whole course, not the session size.
    // Deduping by exercise id, shuffling, then stopping once enough distinct
    // files are queued keeps the fetch count bounded while still leaving far
    // more variety than any single session (30 questions, max) can use.
    const MIXED_FILE_CAP = 40;

    function _sampleMixedEntries(entries) {
        const seenIds = new Set();
        const deduped = entries.filter(e => {
            if (seenIds.has(e.id)) return false;
            seenIds.add(e.id);
            return true;
        });

        const shuffled = _shuffled(deduped);
        const refs = new Set();
        const sampled = [];
        for (const entry of shuffled) {
            if (refs.size >= MIXED_FILE_CAP && !refs.has(entry.ref)) continue;
            refs.add(entry.ref);
            sampled.push(entry);
        }
        return sampled;
    }

    // Every normalised exercise available for a skill (or every skill, for
    // "mixed"), in random order. Count mode samples from this with
    // _takeN(); Timed mode uses it as-is and reshuffles when it runs out.
    async function _buildPool(moduleId) {
        let bankItems, lessonEntries;

        if (moduleId === 'mixed') {
            bankItems = _bank.items;
            lessonEntries = _sampleMixedEntries(Object.values(_index.bySkill).flat());
        } else {
            bankItems = _bank.items.filter(i => i.module === moduleId);
            lessonEntries = _index.bySkill[_lessonSkillFor(moduleId)] || [];
        }

        const lessonExercises = await _resolveLessonEntries(lessonEntries);
        const pool = bankItems.map(_normaliseBankItem).concat(lessonExercises);
        return _shuffled(pool);
    }

    // Exactly n items, cycling the (shuffled) pool if it's smaller than n —
    // a 4-item module can still support "20 questions", it just repeats.
    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        const modules = (_bank.modules || []).slice().sort((a, b) => a.title.localeCompare(b.title));
        // Bank items plus every lesson exercise across every skill — for a
        // course with no hand-authored bank yet (e.g. Hungarian), this is
        // the whole count, not "0+ items" implying the pool is empty when
        // it isn't.
        const totalItems = _bank.items.length + Object.values(_index.bySkill).flat().length;

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Grammar Driller</h2>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="gd-skill">Skill</label>
                    <select id="gd-skill" class="vb-select">
                        <option value="mixed">Mixed — all skills (${totalItems}+ items)</option>
                        ${modules.map(m => {
                            const count = m.exercise_count + _lessonPoolSize(m.id);
                            return `<option value="${_escapeHtml(m.id)}">${_escapeHtml(m.title)} (${count})</option>`;
                        }).join('')}
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="gd-count">Number of questions</label>
                        <select id="gd-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} questions</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="gd-timer">Timer</label>
                        <select id="gd-timer" class="vb-select">
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

        const skillSelect = _container.querySelector('#gd-skill');
        skillSelect.value = _selectedModule;
        skillSelect.addEventListener('change', e => { _selectedModule = e.target.value; });

        const countSelect = _container.querySelector('#gd-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#gd-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    async function _startSession() {
        _container.innerHTML = `<div class="gd-loading">Loading exercises…</div>`;
        const pool = await _buildPool(_selectedModule);
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No exercises found for this skill yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-skill">Change skill</button>
            `;
            _container.querySelector('[data-action="change-skill"]').addEventListener('click', _abortSession);
            return;
        }

        if (_mode === MODE.COUNT) {
            _queue = _takeN(pool, _questionCount);
        } else {
            _queue = pool;
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
                <button class="gd-change-skill" data-action="change-skill">Change skill</button>
            </div>
            <div class="gd-exercise"></div>
        `;
        _container.querySelector('[data-action="change-skill"]').addEventListener('click', _abortSession);

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
            _queue = _shuffled(_queue); // Timed mode ran through the pool once — go round again.
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
    // `options.skill`, when given, skips the settings screen and launches
    // straight into a session scoped to that skill — used by Home's
    // post-unit practice nudge, which already knows which concept it wants
    // drilled and shouldn't make the learner pick it again. Only takes
    // effect from the settings phase: a driller resumed mid-session (e.g.
    // navigating back to Workshop) ignores it and shows what was already in
    // progress, same as opening this driller any other way.
    async function render(root, options) {
        _container = root;

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            if (options && options.skill) {
                _selectedModule = options.skill;
                await _startSession();
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
