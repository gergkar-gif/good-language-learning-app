// ============================================
// SUFFIX DRILLER (Hungarian)
// ============================================
// Plural, possessive and case suffixes, drawn from
// content/hu/indexes/word-index.json — the same 240k-entry index
// engine/lexicon.js already loads for the Reader's tap-a-word lookup,
// built by scripts/import_hu_dictionary.py from real Wiktionary
// declension tables. No new content or authoring: every option a learner
// sees, correct or decoy, is a real, validated inflected form already
// sitting in that index.
//
// Runs dictionary-wide rather than scoped to what the (currently 5-lesson)
// curriculum has taught — an explicit product decision, since plural
// content doesn't ship until Unit 5, possessive until Unit 6/9, and case
// until Unit 11+. The settings screen frames this plainly rather than
// pretending it's curriculum-paced.
//
// Case and Suffix started as separate drillers in the original design doc,
// but both just read differently-tagged word-index entries through the
// same generator, so they're one driller here with a Type filter instead
// of two Workshop tiles.
//
// Both exercise kinds (multiple-choice, fill-blank) are already renderable
// by GrammarRunner, so this module reuses it rather than writing a new one.

const HuSuffixDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const TYPE = { PLURAL: 'plural', POSSESSIVE: 'possessive', CASE: 'case', MIXED: 'mixed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;

    // "my"/"your"/etc — describePossessive()'s own table in
    // engine/morphology/hungarian.js isn't exported (it's a one-line
    // internal helper), so this is a deliberate small duplicate rather
    // than adding an export for three lines of lookup.
    const OWNER_WORDS = {
        1: { sg: 'my', pl: 'our' },
        2: { sg: 'your', pl: 'your (pl.)' },
        3: { sg: 'his/her', pl: 'their' }
    };

    let _phase = PHASE.SETTINGS;
    let _container = null;

    // Grouped once at load time. Each entry: { form, lemma, tag } where
    // tag is the raw word-index tag object ({case?, number?, person?,
    // ownerNumber?}) — kept around so decoy-matching can compare tags
    // directly rather than re-deriving a key from the label text.
    let _plural = null;
    let _possessive = null;
    let _case = null;

    // Grouped by exact tag (case code, or person+ownerNumber+number) so
    // decoy lookup is a map hit plus a filter over one group, not a scan
    // over the whole (up to ~172k-entry) case pool per exercise.
    let _caseGroups = null;      // caseCode -> entries
    let _possessiveGroups = null; // "person:ownerNumber:number" -> entries

    // content/hu/reference/cases.json — a general-purpose grammar reference
    // ("About the Illative case", not "why 'háztartás' becomes
    // 'háztartásokhoz'"), one entry per case code plus "plural" and
    // "possessive". Null if it failed to load; every caller through
    // _referenceFor() already tolerates that (no "Learn more" panel shown).
    let _reference = null;

    // The general reference entry for one exercise's tag, keyed the same
    // three ways _groupFor()/_promptFor() already branch on.
    function _referenceFor(entry) {
        if (!_reference) return null;
        if (entry.tag.person) return _reference.possessive || null;
        if (entry.tag.case) return (_reference.cases && _reference.cases[entry.tag.case]) || null;
        return _reference.plural || null;
    }

    function _possessiveKey(tag) {
        return tag.person + ':' + tag.ownerNumber + ':' + tag.number;
    }

    function _push(map, key, entry) {
        const list = map.get(key);
        if (list) list.push(entry); else map.set(key, [entry]);
    }

    // The word index covers 240k forms, most of them off far rarer lemmas
    // than a learner should meet in a drill ("gerinctelenekével" is a real
    // form, but not a useful question). Lexicon's own frequency ranking —
    // the same one that orders the Reader's competing readings — is the
    // existing, free way to keep the pool to words worth drilling.
    const MAX_LEMMA_RANK = 8000;
    function _isCommon(lemma) {
        const rank = Lexicon.frequencyRank(lemma);
        return rank !== null && rank < MAX_LEMMA_RANK;
    }

    let _mode = MODE.COUNT;
    let _type = TYPE.MIXED;
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

    function _gloss(lemma) {
        const sense = Lexicon.define(lemma);
        return (sense && sense.en) ? Lexicon.shortGloss(sense.en) : lemma;
    }

    // ---- Data loading (once) ----
    async function _load() {
        if (_plural && _possessive && _case) return;
        const [wordIndex] = await Promise.all([
            Content.json(Lang.content('indexes/word-index.json')).catch(() => ({})),
            Lexicon.load(),
            Content.json(Lang.content('reference/cases.json')).catch(() => null).then(r => { _reference = r; })
        ]);

        _plural = [];
        _possessive = [];
        _case = [];
        _caseGroups = new Map();
        _possessiveGroups = new Map();

        for (const form in wordIndex) {
            for (const tag of wordIndex[form]) {
                if (tag.pos !== 'noun' && tag.pos !== 'adjective') continue;
                if (!_isCommon(tag.lemma)) continue;
                const entry = { form, lemma: tag.lemma, tag };
                if (tag.person) {
                    _possessive.push(entry);
                    _push(_possessiveGroups, _possessiveKey(tag), entry);
                } else if (tag.case) {
                    _case.push(entry);
                    _push(_caseGroups, tag.case, entry);
                } else if (tag.number === 'pl') {
                    _plural.push(entry);
                }
            }
        }
    }

    function _poolFor(type) {
        if (type === TYPE.PLURAL) return _plural;
        if (type === TYPE.POSSESSIVE) return _possessive;
        if (type === TYPE.CASE) return _case;
        return _plural.concat(_possessive, _case);
    }

    // ---- English question text for one entry ----
    // Pluralization goes through HungarianMorphology.naivePluralize(gloss,
    // entry.tag.pos) rather than a bare "+ 's'" — gated by POS so an
    // adjective entry (this driller's pool is noun/adjective, see _load())
    // doesn't get "freshs", and it already trims a truncated gloss's
    // trailing "…" and drops all but the first sense of a multi-sense
    // gloss before pluralizing, avoiding the doubled/tripled "s" and
    // singular/plural-mismatch issues a plain "+ 's'" produced.
    function _promptFor(entry) {
        const gloss = _gloss(entry.lemma);
        if (entry.tag.person) {
            const owner = OWNER_WORDS[entry.tag.person][entry.tag.ownerNumber];
            const possessed = entry.tag.number === 'pl' ? HungarianMorphology.naivePluralize(gloss, entry.tag.pos) : gloss;
            return owner + ' ' + possessed;
        }
        if (entry.tag.case) {
            const prep = HungarianMorphology.caseSuffixLabel(entry.tag.case);
            // A case-tagged word-index entry can ALSO be plural
            // ("szerkezetűekre" = szerkezetű + plural + sublative) — the
            // case branch used to ignore tag.number entirely, so the
            // prompt read as if the answer were singular even when the
            // only correct form was the plural one.
            const noun = entry.tag.number === 'pl' ? HungarianMorphology.naivePluralize(gloss, entry.tag.pos) : gloss;
            return prep + ' ' + noun;
        }
        return HungarianMorphology.naivePluralize(gloss, entry.tag.pos); // plural
    }

    // Decoys: real forms of OTHER lemmas carrying the exact same tag
    // (same case, or same person+ownerNumber+number, or same plural) —
    // every option stays a real, validated word, never a fabricated
    // wrong-harmony guess. Looked up via the pre-grouped maps built in
    // _load() rather than scanning the whole pool (up to ~172k entries
    // for case) on every exercise.
    function _groupFor(entry) {
        if (entry.tag.person) return _possessiveGroups.get(_possessiveKey(entry.tag)) || [];
        if (entry.tag.case) return _caseGroups.get(entry.tag.case) || [];
        return _plural;
    }

    function _decoysFor(entry, n) {
        const group = _groupFor(entry);
        const candidates = group.filter(e => e.lemma !== entry.lemma && e.form !== entry.form);
        return _shuffled(candidates).slice(0, n).map(e => e.form);
    }

    // The question text already states the translation inline (via
    // _promptFor's English gloss), so this "why" names the grammar concept
    // itself — the case or possessive suffix responsible for the form —
    // which the question text doesn't spell out.
    function _explanationFor(entry) {
        const gloss = _gloss(entry.lemma);
        if (entry.tag.person) {
            const owner = OWNER_WORDS[entry.tag.person][entry.tag.ownerNumber];
            return `"${entry.lemma}" (${gloss}) takes the possessive suffix for "${owner}" to become "${entry.form}".`;
        }
        if (entry.tag.case) {
            const caseLabel = HungarianMorphology.caseName(entry.tag.case);
            return `"${entry.lemma}" (${gloss}) takes the ${caseLabel} case to become "${entry.form}".`;
        }
        return `"${entry.lemma}" (${gloss}) takes the plural suffix to become "${entry.form}".`;
    }

    // ---- Exercise builders -> GrammarRunner shapes ----
    function _buildMultipleChoice(entry) {
        const decoys = _decoysFor(entry, DECOY_COUNT);
        if (decoys.length < DECOY_COUNT) return null;
        const options = _shuffled([entry.form, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `Which form means "${_promptFor(entry)}"?`,
            options,
            correct: options.indexOf(entry.form),
            explanation: _explanationFor(entry),
            moreInfo: _referenceFor(entry)
        };
    }

    function _buildFillBlank(entry) {
        return {
            kind: 'fill-blank',
            sentence: `"${entry.lemma}" (${_gloss(entry.lemma)}) + ${_promptFor(entry)} = ______`,
            answer: entry.form,
            explanation: _explanationFor(entry),
            moreInfo: _referenceFor(entry)
        };
    }

    function _buildExerciseFor(entry) {
        // Multiple-choice needs 3 real same-tag decoys from other lemmas,
        // which thins out for rarer case/person combinations — fall back
        // to fill-blank (which needs none) rather than dropping the item.
        return _buildMultipleChoice(entry) || _buildFillBlank(entry);
    }

    function _buildPool(type) {
        const pool = _poolFor(type);
        return _shuffled(pool).slice(0, 400).map(_buildExerciseFor).filter(Boolean);
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
                <h2 class="gd-title">Suffix Driller</h2>
                <p class="gd-hint">Plurals, possession and case — attach the right ending. Draws from the
                    full Hungarian word index, so this can run ahead of what your lessons have covered so far.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="hs-type">Type</label>
                    <select id="hs-type" class="vb-select">
                        <option value="${TYPE.MIXED}">Mixed</option>
                        <option value="${TYPE.PLURAL}">Plural</option>
                        <option value="${TYPE.POSSESSIVE}">Possessive</option>
                        <option value="${TYPE.CASE}">Case</option>
                    </select>
                </div>

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="hs-count">Number of questions</label>
                        <select id="hs-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} questions</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="hs-timer">Timer</label>
                        <select id="hs-timer" class="vb-select">
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

        const typeSelect = _container.querySelector('#hs-type');
        typeSelect.value = _type;
        typeSelect.addEventListener('change', e => { _type = e.target.value; });

        const countSelect = _container.querySelector('#hs-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#hs-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        const pool = _buildPool(_type);
        _seen = 0;
        _correct = 0;

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No entries of this type yet.</div>
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
