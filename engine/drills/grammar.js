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
    let _activeSelectCleanup = null;

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
        const skillKey = _lessonSkillFor(moduleId);
        const entries = (_index && _index.bySkill && (_index.bySkill[skillKey] || _index.bySkill[moduleId])) || [];
        return entries ? entries.length : 0;
    }

    function _formatFallbackTitle(skillId) {
        if (!skillId) return '';
        const text = skillId
            .replace(/-isn-t\b/g, " isn't")
            .replace(/-aren-t\b/g, " aren't")
            .replace(/-don-t\b/g, " don't")
            .replace(/-doesn-t\b/g, " doesn't")
            .replace(/-won-t\b/g, " won't")
            .replace(/-can-t\b/g, " can't")
            .replace(/-s-([a-z])/g, "'s $1")
            .replace(/-s\b/g, "'s");
        const minorWords = new Set(['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'vs', 'yet', 'with']);
        return text.split('-').map((w, i) => {
            const wLower = w.toLowerCase();
            if (i > 0 && minorWords.has(wLower)) return wLower;
            return w.charAt(0).toUpperCase() + w.slice(1);
        }).join(' ');
    }

    function _getAvailableModules() {
        if (_bank && _bank.modules && _bank.modules.length > 0) {
            return _bank.modules.slice().sort((a, b) => a.title.localeCompare(b.title));
        }
        if (_index && _index.bySkill) {
            return Object.keys(_index.bySkill).map(skillId => {
                const title = (_index.titles && _index.titles[skillId]) || _formatFallbackTitle(skillId);
                return {
                    id: skillId,
                    title: title,
                    exercise_count: 0
                };
            }).sort((a, b) => a.title.localeCompare(b.title));
        }
        return [];
    }

    function _getLearnedSkillIds() {
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const completedLessonIds = Object.keys(progress).filter(id => progress[id]);
        if (!completedLessonIds.length) return new Set();

        const learned = new Set();
        const curriculum = window._curriculumData;

        if (_index && _index.bySkill) {
            const completedRefs = new Set();
            const completedPrefixes = new Set();
            completedLessonIds.forEach(id => {
                const cleaned = id.replace(/^lesson\./, '');
                const parts = cleaned.split('.');
                const level = parts[0];
                const rest = parts.slice(1).join('-');
                completedRefs.add(`exercises/${level}/${level}-${rest}-ex.json`);
                completedPrefixes.add(cleaned.replace(/\./g, '-'));
            });

            Object.keys(_index.bySkill).forEach(skill => {
                const entries = _index.bySkill[skill] || [];
                const hasCompleted = entries.some(e => {
                    if (completedRefs.has(e.ref)) return true;
                    for (const pfx of completedPrefixes) {
                        if (e.id && e.id.indexOf(pfx) !== -1) return true;
                    }
                    return false;
                });
                if (hasCompleted) learned.add(skill);
            });
        }

        if (curriculum && curriculum.levels) {
            const completedGrammarTitles = new Set();
            Object.keys(curriculum.levels).forEach(level => {
                const units = curriculum.levels[level].units || [];
                units.forEach(u => {
                    (u.lessons || []).forEach(l => {
                        if (progress[l.id] && l.grammar && l.grammar !== 'Consolidation') {
                            completedGrammarTitles.add(l.grammar.toLowerCase().trim());
                        }
                    });
                });
            });

            if (_bank && _bank.modules) {
                _bank.modules.forEach(m => {
                    const titleLower = (m.title || '').toLowerCase().trim();
                    for (const gTitle of completedGrammarTitles) {
                        if (titleLower.includes(gTitle) || gTitle.includes(titleLower)) {
                            learned.add(m.id);
                            learned.add(_lessonSkillFor(m.id));
                        }
                    }
                });
            }
        }

        return learned;
    }

    function _competenceBadgeHtml(moduleId, isLearned) {
        if (typeof DrillHistory !== 'undefined') {
            const cls = DrillHistory.classify('grammar:' + moduleId);
            if (cls && cls.state === 'strong') {
                const icon = (typeof Art !== 'undefined') ? Art.icon('check') : '';
                return `<span class="gd-badge-status gd-status-practiced" title="Practiced">${icon} practiced</span>`;
            }
            if (cls && cls.state === 'weak') {
                const icon = (typeof Art !== 'undefined') ? Art.icon('alert') : '';
                return `<span class="gd-badge-status gd-status-review" title="Needs review">${icon} needs review</span>`;
            }
            if (cls && cls.state === 'developing') {
                return '<span class="gd-badge-status gd-status-developing">developing</span>';
            }
        }
        if (isLearned) {
            return '<span class="gd-badge-new"><i>new</i></span>';
        }
        return '';
    }

    function _competenceBadgeText(moduleId, isLearned) {
        if (typeof DrillHistory !== 'undefined') {
            const cls = DrillHistory.classify('grammar:' + moduleId);
            if (cls && cls.state === 'strong') return ' [practiced]';
            if (cls && cls.state === 'weak') return ' [needs review]';
            if (cls && cls.state === 'developing') return ' [developing]';
        }
        if (isLearned) return ' [new]';
        return '';
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
                return {
                    kind: 'fill-blank',
                    sentence: ex.sentence,
                    answer: ex.answer || (ex.answers && ex.answers[0]),
                    acceptable: ex.answers || [ex.answer]
                };
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
            if (seenIds.has(entry.id)) continue;
            const file = byRef[entry.ref];
            const ex = (file && file.exercises || []).find(e => e.id === entry.id);
            if (!ex) continue;
            const normalised = _normaliseLessonExercise(ex);
            if (normalised) { resolved.push(normalised); seenIds.add(entry.id); }
        }
        return resolved;
    }

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
    // "mixed" or "mixed-learned"), in random order.
    async function _buildPool(moduleId) {
        let bankItems = [], lessonEntries = [];

        if (moduleId === 'mixed-learned') {
            const learnedIds = _getLearnedSkillIds();
            const availableModules = _getAvailableModules();
            const learnedModules = availableModules.filter(m =>
                learnedIds.has(m.id) || learnedIds.has(_lessonSkillFor(m.id))
            );
            const learnedSet = new Set(learnedModules.map(m => m.id));

            bankItems = (_bank && _bank.items ? _bank.items : []).filter(i => learnedSet.has(i.module));

            const entries = [];
            learnedModules.forEach(m => {
                const skillKey = _lessonSkillFor(m.id);
                if (_index && _index.bySkill) {
                    if (_index.bySkill[skillKey]) entries.push(..._index.bySkill[skillKey]);
                    if (_index.bySkill[m.id] && m.id !== skillKey) entries.push(..._index.bySkill[m.id]);
                }
            });
            lessonEntries = _sampleMixedEntries(entries);
        } else if (moduleId === 'mixed') {
            bankItems = (_bank && _bank.items) || [];
            lessonEntries = _sampleMixedEntries(Object.values((_index && _index.bySkill) || {}).flat());
        } else {
            bankItems = (_bank && _bank.items || []).filter(i => i.module === moduleId);
            lessonEntries = (_index && _index.bySkill && (_index.bySkill[_lessonSkillFor(moduleId)] || _index.bySkill[moduleId])) || [];
        }

        const lessonExercises = await _resolveLessonEntries(lessonEntries);
        const pool = bankItems.map(_normaliseBankItem).concat(lessonExercises);
        return _shuffled(pool);
    }

    // Exactly n items, cycling the (shuffled) pool if it's smaller than n
    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        if (_activeSelectCleanup) {
            _activeSelectCleanup();
            _activeSelectCleanup = null;
        }

        const modules = _getAvailableModules();
        const learnedSkillIds = _getLearnedSkillIds();
        const learnedModules = modules.filter(m =>
            learnedSkillIds.has(m.id) || learnedSkillIds.has(_lessonSkillFor(m.id))
        );

        const totalItems = (_bank ? _bank.items.length : 0) + Object.values((_index && _index.bySkill) || {}).flat().length;
        const learnedItems = learnedModules.reduce((acc, m) => acc + (m.exercise_count || 0) + _lessonPoolSize(m.id), 0);

        if (_selectedModule === 'mixed' && learnedModules.length > 0) {
            _selectedModule = 'mixed-learned';
        }

        const renderSelectOption = (m, isLearned) => {
            const count = (m.exercise_count || 0) + _lessonPoolSize(m.id);
            const badge = _competenceBadgeText(m.id, isLearned);
            return `<option value="${_escapeHtml(m.id)}">${_escapeHtml(m.title)} (${count})${badge}</option>`;
        };

        let skillOptionsHtml = '';
        if (learnedModules.length > 0) {
            skillOptionsHtml += `<option value="mixed-learned">Mixed — My Learned Skills (${learnedItems}+ items)</option>`;
        }
        skillOptionsHtml += `<option value="mixed">Mixed — All Skills (${totalItems}+ items)</option>`;

        if (learnedModules.length > 0) {
            skillOptionsHtml += `
                <optgroup label="My Skills (from lessons)">
                    ${learnedModules.map(m => renderSelectOption(m, true)).join('')}
                </optgroup>
                <optgroup label="All Skills">
                    ${modules.map(m => renderSelectOption(m, learnedSkillIds.has(m.id) || learnedSkillIds.has(_lessonSkillFor(m.id)))).join('')}
                </optgroup>
            `;
        } else {
            skillOptionsHtml += `
                <optgroup label="All Skills">
                    ${modules.map(m => renderSelectOption(m, false)).join('')}
                </optgroup>
            `;
        }

        let listItemsHtml = '';
        if (learnedModules.length > 0) {
            listItemsHtml += `
                <button type="button" class="gd-skill-item${_selectedModule === 'mixed-learned' ? ' is-selected' : ''}" data-skill-id="mixed-learned" role="option" aria-selected="${_selectedModule === 'mixed-learned'}">
                    <span class="gd-skill-item-title">Mixed — My Learned Skills <span class="gd-skill-item-count">(${learnedItems}+ items)</span></span>
                </button>
            `;
        }
        listItemsHtml += `
            <button type="button" class="gd-skill-item${_selectedModule === 'mixed' ? ' is-selected' : ''}" data-skill-id="mixed" role="option" aria-selected="${_selectedModule === 'mixed'}">
                <span class="gd-skill-item-title">Mixed — All Skills <span class="gd-skill-item-count">(${totalItems}+ items)</span></span>
            </button>
        `;

        if (learnedModules.length > 0) {
            listItemsHtml += `
                <div class="gd-skill-group-head" data-group="learned">
                    ${(typeof Art !== 'undefined') ? Art.icon('grammar') : ''}
                    <span>My Skills (from lessons)</span>
                </div>
                ${learnedModules.map(m => {
                    const count = (m.exercise_count || 0) + _lessonPoolSize(m.id);
                    const badge = _competenceBadgeHtml(m.id, true);
                    return `
                        <button type="button" class="gd-skill-item${_selectedModule === m.id ? ' is-selected' : ''}" data-skill-id="${_escapeHtml(m.id)}" data-group="learned" role="option" aria-selected="${_selectedModule === m.id}">
                            <span class="gd-skill-item-title">${_escapeHtml(m.title)} <span class="gd-skill-item-count">(${count})</span></span>
                            ${badge}
                        </button>
                    `;
                }).join('')}
                <div class="gd-skill-group-head" data-group="all">
                    <span>All Skills</span>
                </div>
                ${modules.map(m => {
                    const count = (m.exercise_count || 0) + _lessonPoolSize(m.id);
                    const isLearned = learnedSkillIds.has(m.id) || learnedSkillIds.has(_lessonSkillFor(m.id));
                    const badge = _competenceBadgeHtml(m.id, isLearned);
                    return `
                        <button type="button" class="gd-skill-item${_selectedModule === m.id ? ' is-selected' : ''}" data-skill-id="${_escapeHtml(m.id)}" data-group="all" role="option" aria-selected="${_selectedModule === m.id}">
                            <span class="gd-skill-item-title">${_escapeHtml(m.title)} <span class="gd-skill-item-count">(${count})</span></span>
                            ${badge}
                        </button>
                    `;
                }).join('')}
            `;
        } else {
            listItemsHtml += `
                <div class="gd-skill-group-head" data-group="all">
                    <span>All Skills</span>
                </div>
                ${modules.map(m => {
                    const count = (m.exercise_count || 0) + _lessonPoolSize(m.id);
                    const badge = _competenceBadgeHtml(m.id, false);
                    return `
                        <button type="button" class="gd-skill-item${_selectedModule === m.id ? ' is-selected' : ''}" data-skill-id="${_escapeHtml(m.id)}" data-group="all" role="option" aria-selected="${_selectedModule === m.id}">
                            <span class="gd-skill-item-title">${_escapeHtml(m.title)} <span class="gd-skill-item-count">(${count})</span></span>
                            ${badge}
                        </button>
                    `;
                }).join('')}
            `;
        }

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
                    <label id="gd-skill-label" for="gd-skill-trigger">Skill</label>
                    <div class="gd-custom-select" id="gd-custom-select">
                        <button type="button" class="gd-select-trigger" id="gd-skill-trigger" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="gd-skill-label gd-skill-trigger">
                            <span class="gd-trigger-main">
                                <span class="gd-trigger-title" id="gd-trigger-title"></span>
                            </span>
                            <span class="gd-trigger-badge" id="gd-trigger-badge"></span>
                            <span class="gd-trigger-arrow" aria-hidden="true"></span>
                        </button>
                        <div class="gd-select-panel" id="gd-select-panel" hidden>
                            <div class="gd-search-wrap">
                                <input type="search" id="gd-skill-filter" class="gd-skill-filter" placeholder="Filter skills…" autocomplete="off" />
                            </div>
                            <div class="gd-skill-list" id="gd-skill-list" role="listbox" tabindex="0">
                                ${listItemsHtml}
                            </div>
                        </div>
                    </div>
                    <select id="gd-skill" class="vb-select" style="display:none;" aria-hidden="true">
                        ${skillOptionsHtml}
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

        const customSelect = _container.querySelector('#gd-custom-select');
        const trigger = _container.querySelector('#gd-skill-trigger');
        const triggerTitle = _container.querySelector('#gd-trigger-title');
        const triggerBadge = _container.querySelector('#gd-trigger-badge');
        const panel = _container.querySelector('#gd-select-panel');
        const filterInput = _container.querySelector('#gd-skill-filter');
        const listEl = _container.querySelector('#gd-skill-list');
        const fallbackSelect = _container.querySelector('#gd-skill');

        function _getModuleDisplay(id) {
            if (id === 'mixed-learned') {
                return { title: `Mixed — My Learned Skills (${learnedItems}+ items)`, badge: '' };
            }
            if (id === 'mixed') {
                return { title: `Mixed — All Skills (${totalItems}+ items)`, badge: '' };
            }
            const found = modules.find(m => m.id === id);
            if (found) {
                const count = (found.exercise_count || 0) + _lessonPoolSize(found.id);
                const isLearned = learnedSkillIds.has(found.id) || learnedSkillIds.has(_lessonSkillFor(found.id));
                return {
                    title: `${found.title} (${count})`,
                    badge: _competenceBadgeHtml(found.id, isLearned)
                };
            }
            return { title: id, badge: '' };
        }

        function updateTrigger() {
            const disp = _getModuleDisplay(_selectedModule);
            triggerTitle.textContent = disp.title;
            triggerBadge.innerHTML = disp.badge;
        }

        if (fallbackSelect.querySelector(`option[value="${_selectedModule}"]`)) {
            fallbackSelect.value = _selectedModule;
        } else if (fallbackSelect.options.length > 0) {
            _selectedModule = fallbackSelect.value;
        }
        updateTrigger();

        function openPanel() {
            trigger.setAttribute('aria-expanded', 'true');
            panel.removeAttribute('hidden');
            filterInput.value = '';
            filterItems('');
            setTimeout(() => { if (filterInput) filterInput.focus(); }, 50);

            const selEl = listEl.querySelector(`.gd-skill-item[data-skill-id="${_selectedModule}"]`);
            if (selEl) selEl.scrollIntoView({ block: 'nearest' });
        }

        function closePanel() {
            trigger.setAttribute('aria-expanded', 'false');
            panel.setAttribute('hidden', '');
        }

        trigger.addEventListener('click', e => {
            e.stopPropagation();
            const isOpen = trigger.getAttribute('aria-expanded') === 'true';
            if (isOpen) closePanel();
            else openPanel();
        });

        function filterItems(query) {
            const q = query.toLowerCase().trim();
            const items = listEl.querySelectorAll('.gd-skill-item');
            let visibleCount = 0;

            items.forEach(item => {
                const text = item.textContent.toLowerCase();
                const matches = !q || text.includes(q);
                item.style.display = matches ? 'flex' : 'none';
                if (matches) visibleCount++;
            });

            const groupHeads = listEl.querySelectorAll('.gd-skill-group-head');
            groupHeads.forEach(head => {
                const group = head.getAttribute('data-group');
                const groupItems = listEl.querySelectorAll(`.gd-skill-item[data-group="${group}"]`);
                const hasVisible = Array.from(groupItems).some(i => i.style.display !== 'none');
                head.style.display = hasVisible ? 'flex' : 'none';
            });

            let emptyEl = listEl.querySelector('.gd-skill-empty');
            if (visibleCount === 0) {
                if (!emptyEl) {
                    emptyEl = document.createElement('div');
                    emptyEl.className = 'gd-skill-empty';
                    emptyEl.textContent = 'No matching skills found.';
                    listEl.appendChild(emptyEl);
                }
                emptyEl.style.display = 'block';
            } else if (emptyEl) {
                emptyEl.style.display = 'none';
            }
        }

        filterInput.addEventListener('input', () => {
            filterItems(filterInput.value);
        });

        listEl.addEventListener('click', e => {
            const btn = e.target.closest('.gd-skill-item');
            if (!btn) return;
            const skillId = btn.getAttribute('data-skill-id');
            if (skillId) {
                _selectedModule = skillId;
                if (fallbackSelect) fallbackSelect.value = skillId;
                listEl.querySelectorAll('.gd-skill-item').forEach(el => {
                    const isSel = el.getAttribute('data-skill-id') === skillId;
                    el.classList.toggle('is-selected', isSel);
                    el.setAttribute('aria-selected', isSel ? 'true' : 'false');
                });
                updateTrigger();
                closePanel();
                trigger.focus();
            }
        });

        const handleDocClick = e => {
            if (!customSelect.contains(e.target)) {
                closePanel();
            }
        };

        const handleKeyDown = e => {
            if (e.key === 'Escape' && trigger.getAttribute('aria-expanded') === 'true') {
                closePanel();
                trigger.focus();
            }
        };

        document.addEventListener('click', handleDocClick);
        document.addEventListener('keydown', handleKeyDown);

        _activeSelectCleanup = () => {
            document.removeEventListener('click', handleDocClick);
            document.removeEventListener('keydown', handleKeyDown);
        };

        const countSelect = _container.querySelector('#gd-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#gd-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', () => {
            if (_activeSelectCleanup) {
                _activeSelectCleanup();
                _activeSelectCleanup = null;
            }
            _startSession();
        });
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

    function _progressPercent() {
        if (_mode === MODE.COUNT) {
            return Math.min(100, Math.round((_queueIndex / Math.max(1, _queue.length)) * 100));
        }
        const total = _timerMinutes * 60;
        const elapsed = Math.max(0, total - _timeRemaining);
        return Math.min(100, Math.round((elapsed / Math.max(1, total)) * 100));
    }

    function _renderSession() {
        _container.innerHTML = `
            <div class="driller-progress-track" aria-hidden="true">
                <div class="driller-progress-bar" style="width: ${_progressPercent()}%"></div>
            </div>
            <div class="gd-hud">
                <span class="gd-hud-score">${_scoreLabel()}</span>
                ${_mode === MODE.TIMED ? `<span class="vspeed-timer-display">${_formatTime(_timeRemaining)}</span>` : ''}
                <button class="gd-change-skill" data-action="change-skill">← Settings</button>
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
                const bar = _container.querySelector('.driller-progress-bar');
                if (bar) bar.style.width = _progressPercent() + '%';
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
        if (typeof DrillHistory !== 'undefined' && _seen > 0) {
            DrillHistory.record('grammar:' + _selectedModule, {
                correct: _correct,
                wrong: _seen - _correct
            });
        }
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
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Total</span>
                        <span class="vspeed-stat-value">${_seen}</span>
                    </div>
                </div>
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-primary" data-action="play-again">Practice Again</button>
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>
                    <button class="vbtn vbtn-secondary" data-action="exit-workshop">Back to Workshop</button>
                </div>
            </div>
        `;

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
        const exitBtn = _container.querySelector('[data-action="exit-workshop"]');
        if (exitBtn) exitBtn.addEventListener('click', () => { if (typeof Workshop !== 'undefined') Workshop.close(); });

        if (typeof RecommendationEngine !== 'undefined') RecommendationEngine.mountNextAction(_container);
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
    // post-unit practice nudge and Workshop's "Recommended for you" card,
    // which already know which concept they want drilled and shouldn't
    // make the learner pick it again. `options.count`, alongside `skill`,
    // forces Count mode at that exact question count regardless of
    // whatever was last selected in Settings — used by the lesson-complete
    // screen's "Quick Reinforce" mini-game (engine/lessons.js), where a
    // handful of questions is the whole point and a stale "30" left over
    // from an earlier full session would defeat it. Both only take effect
    // from the settings phase: a driller resumed mid-session (e.g.
    // navigating back to Workshop) ignores them and shows what was already
    // in progress, same as opening this driller any other way.
    async function render(root, options) {
        _container = root;

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            if (options && options.skill) {
                _selectedModule = options.skill;
                if (options.count) {
                    _mode = MODE.COUNT;
                    _questionCount = options.count;
                }
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

    // Called when the learner leaves this driller mid-session via the main
    // nav rather than its own "change settings"/finish controls — without
    // this, a Timed-mode session's setInterval keeps ticking forever
    // against a container that's already been torn down. Idempotent: safe
    // to call even when no timer is running.
    function stop() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        if (_activeSelectCleanup) { _activeSelectCleanup(); _activeSelectCleanup = null; }
        _phase = PHASE.SETTINGS;
    }

    return { render, stop };
})();
