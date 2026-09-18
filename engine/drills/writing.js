// ============================================
// WRITING STUDIO DRILLER
// ============================================
// Complete written production hub for Parlour:
//
// 1. Composition Studio:
//    - Longer-form open-ended production driller with CEFR formative assessment.
//    - Evaluates writing against curriculum standards, provides multi-dimensional
//      feedback, and feeds production evidence into the Learner Model.
//
// 2. Sentence Translation:
//    - Bidirectional sentence translation practice drawn from curriculum pairs.
//    - Timed and count modes, level filters, dual-track support.

const WritingDriller = (function () {
    'use strict';

    const STUDIO_TAB = { COMPOSITION: 'composition', TRANSLATION: 'translation' };
    let _activeStudioTab = STUDIO_TAB.COMPOSITION;
    let _subOptions = null;

    const PHASE = { PROMPT_SELECT: 1, WRITING: 2, ASSESSING: 3, RESULTS: 4, CUSTOM_TASK: 5 };
    const CUSTOM_WORD_OPTIONS = [30, 50, 100, 150, 250];

    let _container = null;
    let _phase = PHASE.PROMPT_SELECT;
    let _promptsData = null;
    let _loadedLang = null;
    let _selectedPrompt = null;
    // 'all' or a CEFR code -- filters the topic cards below without
    // touching them individually (still full title+description cards, per
    // the "unless it becomes too busy" caveat: today's handful of prompts
    // isn't a wall of buttons yet, so this filter is the scalable part).
    let _promptLevelFilter = 'all';
    let _draftText = '';
    let _assessmentResult = null;
    let _engine = null;

    function _esc(text) {
        if (typeof UI !== 'undefined' && UI.escape) return UI.escape(text);
        const d = document.createElement('div');
        d.textContent = String(text == null ? '' : text);
        return d.innerHTML;
    }

    function _draftKey(promptId) {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        return `parlour_writing_draft_${lang}_${promptId || 'custom'}`;
    }

    async function _loadPrompts() {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        if (_promptsData && _loadedLang === lang) return;
        try {
            const data = await Content.json(Lang.content('writing-prompts.json'));
            _promptsData = data && data.prompts ? data.prompts : [];
            _loadedLang = lang;
        } catch (e) {
            _promptsData = [];
        }
    }

    function _getEngine() {
        if (!_engine) {
            if (typeof GraderEngine !== 'undefined') {
                _engine = new GraderEngine();
            } else if (typeof ParlourGrader !== 'undefined' && ParlourGrader.GraderEngine) {
                _engine = new ParlourGrader.GraderEngine();
            }
        }
        return _engine;
    }

    // ----------------------------------------
    // STUDIO SHELL & SWITCHER
    // ----------------------------------------

    function _renderStudioShell() {
        if (!_container) return;

        _container.innerHTML = `
            <div class="sp-studio-wrap">
                <div class="sp-studio-nav" role="tablist">
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.COMPOSITION ? 'active' : ''}" data-studio-tab="composition" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.COMPOSITION}">
                        Composition Studio
                    </button>
                    <button type="button" class="sp-studio-tab ${_activeStudioTab === STUDIO_TAB.TRANSLATION ? 'active' : ''}" data-studio-tab="translation" role="tab" aria-selected="${_activeStudioTab === STUDIO_TAB.TRANSLATION}">
                        Sentence Translation
                    </button>
                </div>
                <div class="sp-studio-body" id="wr-studio-body"></div>
            </div>
        `;

        _container.querySelectorAll('[data-studio-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-studio-tab');
                if (target === _activeStudioTab) return;
                stop();
                _activeStudioTab = target;
                _subOptions = null;
                _renderStudioShell();
            });
        });

        _renderActiveTab();
    }

    function _renderActiveTab() {
        const body = document.getElementById('wr-studio-body');
        if (!body) return;

        if (_activeStudioTab === STUDIO_TAB.TRANSLATION) {
            if (typeof TranslationDriller !== 'undefined') {
                TranslationDriller.render(body, _subOptions);
            } else {
                body.innerHTML = '<div class="gd-loading">Loading Translation Driller…</div>';
            }
        } else {
            if (_phase === PHASE.PROMPT_SELECT) _renderPromptSelect(body);
            else if (_phase === PHASE.CUSTOM_TASK) _renderCustomTask(body);
            else if (_phase === PHASE.WRITING) _renderWriting(body);
            else if (_phase === PHASE.ASSESSING) _renderAssessing(body);
            else if (_phase === PHASE.RESULTS) _renderResults(body);
        }
    }

    // ----------------------------------------
    // RENDER SCREENS (COMPOSITION)
    // ----------------------------------------

    async function _renderPromptSelect(body) {
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the target language';
        const prompts = _promptsData || [];

        let unverifiedList = [];
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.unverifiedCompetencies === 'function') {
            try {
                unverifiedList = await LearnerModel.unverifiedCompetencies();
            } catch (e) { unverifiedList = []; }
        }

        const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
        const availableLevels = Array.from(new Set(prompts.map(p => p.cefrLevel).filter(Boolean)))
            .sort((a, b) => CEFR_ORDER.indexOf(a) - CEFR_ORDER.indexOf(b));
        const filteredPrompts = _promptLevelFilter === 'all'
            ? prompts
            : prompts.filter(p => p.cefrLevel === _promptLevelFilter);

        const levelFilterHtml = availableLevels.length > 1 ? `
            <div class="wk-config-group">
                <label class="wk-config-label">Level</label>
                <div class="wk-pill-row">
                    <button type="button" class="wk-pill ${_promptLevelFilter === 'all' ? 'active' : ''}" data-prompt-level-filter="all">All</button>
                    ${availableLevels.map(lvl => `
                        <button type="button" class="wk-pill ${_promptLevelFilter === lvl ? 'active' : ''}" data-prompt-level-filter="${_esc(lvl)}">${_esc(lvl)}</button>
                    `).join('')}
                </div>
            </div>
        ` : '';

        let promptsHtml = '';
        if (filteredPrompts.length > 0) {
            promptsHtml = filteredPrompts.map(p => `
                <div class="wk-card sp-card-clickable" data-select-prompt="${_esc(p.id)}">
                    <div class="sp-prompt-card-head">
                        <span class="sp-level-pill">${_esc(p.cefrLevel)}</span>
                        <span class="sp-words-target">${_esc(p.targetWords)} words</span>
                    </div>
                    <h3 class="wk-card-title">${_esc(p.title)}</h3>
                    <p class="wk-card-sub">${_esc(p.prompt.slice(0, 110))}...</p>
                </div>
            `).join('');
        }

        body.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Composition Studio</h2>
                    <p class="sp-setup-sub">Write open-ended texts in ${langName} and receive CEFR-aligned formative feedback.</p>
                </div>

                ${unverifiedList.length > 0 ? `
                    <div class="sp-unverified-section" style="margin-bottom: 24px;">
                        <h3 class="sp-section-heading" style="margin-bottom: 12px; font-size: 15px; color: var(--accent-dark);">
                            Target Unverified Goals (${unverifiedList.length})
                        </h3>
                        <div class="sp-prompt-grid">
                            ${unverifiedList.slice(0, 3).map(c => `
                                <div class="wk-card sp-card-clickable sp-card-competency" data-select-comp="${_esc(c.text)}">
                                    <div class="sp-prompt-card-head">
                                        <span class="sp-level-pill">${_esc(c.level || 'A1')}</span>
                                        <span class="sp-words-target">Can-Do Goal</span>
                                    </div>
                                    <h3 class="wk-card-title">${_esc(c.text)}</h3>
                                    <p class="wk-card-sub">${_esc(c.reason || 'Practice and demonstrate this capability in writing.')}</p>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${levelFilterHtml}

                <div class="sp-prompt-grid">
                    ${promptsHtml}
                    <div class="wk-card sp-card-clickable sp-card-custom" data-select-custom="1">
                        <div class="sp-prompt-card-head">
                            <span class="sp-level-pill">Free Topic</span>
                        </div>
                        <h3 class="wk-card-title">Set Your Own Task</h3>
                        <p class="wk-card-sub">Write your own one-line task and word limit (e.g. "describe your hobbies in 100 words"), then get feedback against exactly that.</p>
                    </div>
                </div>
            </div>
        `;

        body.querySelectorAll('[data-prompt-level-filter]').forEach(el => {
            el.addEventListener('click', () => {
                _promptLevelFilter = el.getAttribute('data-prompt-level-filter');
                _renderActiveTab();
            });
        });

        body.querySelectorAll('[data-select-comp]').forEach(el => {
            el.addEventListener('click', () => {
                const text = el.getAttribute('data-select-comp');
                const found = unverifiedList.find(c => c.text === text);
                _selectedPrompt = {
                    id: 'comp_' + Date.now(),
                    title: text.length > 40 ? text.slice(0, 37) + '...' : text,
                    cefrLevel: (found && found.level) || 'A1',
                    targetWords: 35,
                    prompt: `Demonstrate this ability in writing: "${text}". Write clearly and naturally — however much the task itself calls for.`,
                    targetCompetency: text,
                    taskCompletionPrimary: true
                };
                _draftText = '';
                _phase = PHASE.WRITING;
                _renderActiveTab();
            });
        });

        body.querySelectorAll('[data-select-prompt]').forEach(el => {
            el.addEventListener('click', () => {
                const id = el.getAttribute('data-select-prompt');
                const found = (_promptsData || []).find(p => p.id === id);
                if (found) {
                    _selectedPrompt = found;
                    _draftText = localStorage.getItem(_draftKey(found.id)) || '';
                    _phase = PHASE.WRITING;
                    _renderActiveTab();
                }
            });
        });

        const customBtn = body.querySelector('[data-select-custom]');
        if (customBtn) {
            customBtn.addEventListener('click', () => {
                _phase = PHASE.CUSTOM_TASK;
                _renderActiveTab();
            });
        }
    }

    // A learner-authored task ("describe your hobbies in 100 words") plus
    // an explicit word-count target, in front of the exact same writing
    // screen / GraderEngine.grade() pipeline every other prompt already
    // uses -- taskInstructions in _submitForGrading() is just p.prompt,
    // so grading the learner's own task needs no change there at all.
    let _customTaskWords = CUSTOM_WORD_OPTIONS[2];

    function _renderCustomTask(body) {
        body.innerHTML = `
            <div class="sp-driller-wrap">
                <button class="vbtn vbtn-secondary sp-back-btn" data-action="back-to-prompts">← Back</button>
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Set Your Own Task</h2>
                    <p class="sp-setup-sub">Describe what you want to write about, and how much. You'll be graded against exactly this.</p>
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label" for="wr-custom-task-input">Task</label>
                    <input type="text" id="wr-custom-task-input" class="review-input" style="width:100%;"
                        placeholder="e.g. Describe your hobbies" maxlength="200">
                </div>

                <div class="wk-config-group">
                    <label class="wk-config-label">Word Limit</label>
                    <div class="wk-pill-row">
                        ${CUSTOM_WORD_OPTIONS.map(n => `
                            <button type="button" class="wk-pill ${_customTaskWords === n ? 'active' : ''}" data-custom-words="${n}">${n}</button>
                        `).join('')}
                    </div>
                </div>

                <div class="sp-settings-start">
                    <button type="button" class="sp-start-btn" data-action="start-custom-task" disabled>
                        Start Writing
                    </button>
                </div>
            </div>
        `;

        const backBtn = body.querySelector('[data-action="back-to-prompts"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                _phase = PHASE.PROMPT_SELECT;
                _renderActiveTab();
            });
        }

        const input = body.querySelector('#wr-custom-task-input');
        const startBtn = body.querySelector('[data-action="start-custom-task"]');
        input.addEventListener('input', () => {
            startBtn.disabled = !input.value.trim();
        });
        input.focus();

        body.querySelectorAll('[data-custom-words]').forEach(el => {
            el.addEventListener('click', () => {
                _customTaskWords = Number(el.getAttribute('data-custom-words'));
                body.querySelectorAll('[data-custom-words]').forEach(p => p.classList.toggle('active', Number(p.getAttribute('data-custom-words')) === _customTaskWords));
            });
        });

        startBtn.addEventListener('click', () => {
            const task = input.value.trim();
            if (!task) return;
            _selectedPrompt = {
                id: 'custom-task-' + Date.now(),
                cefrLevel: (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel) ? LearnerPath.currentLevel() : 'B2',
                taskType: 'free_writing',
                title: task.length > 40 ? task.slice(0, 37) + '...' : task,
                prompt: task,
                minWords: Math.round(_customTaskWords * 0.5),
                targetWords: _customTaskWords,
                maxWords: Math.round(_customTaskWords * 2),
                targetSkills: []
            };
            _draftText = '';
            _phase = PHASE.WRITING;
            _renderActiveTab();
        });
    }

    function _renderWriting(body) {
        if (!_selectedPrompt) return;
        const p = _selectedPrompt;

        const skillsPills = (p.targetSkills || []).map(s => {
            const label = typeof s === 'string' ? s : (s.description || s.id);
            return `<span class="sp-skill-pill">${_esc(label)}</span>`;
        }).join('');

        body.innerHTML = `
            <div class="sp-driller-wrap sp-writing-wrap">
                <div class="sp-writing-header">
                    <button class="vbtn vbtn-secondary sp-back-btn" data-action="back-prompts">← Back</button>
                    <div class="sp-header-info">
                        <span class="sp-level-pill">${_esc(p.cefrLevel)}</span>
                        <span class="sp-words-target">Target: ~${_esc(p.targetWords)} words</span>
                    </div>
                </div>

                <div class="sp-prompt-detail-card">
                    <h3 class="sp-prompt-detail-title">${_esc(p.title)}</h3>
                    <p class="sp-prompt-detail-desc">${_esc(p.prompt)}</p>
                    ${skillsPills ? `<div class="sp-prompt-skills">${skillsPills}</div>` : ''}
                </div>

                <div class="sp-editor-area">
                    <textarea class="sp-writing-textarea" placeholder="Start writing here..." rows="12">${_esc(_draftText)}</textarea>
                    <div class="sp-editor-footer">
                        <div class="sp-counter-box">
                            <span class="sp-word-count">0 words</span>
                            <span class="sp-sentence-count">· 0 sentences</span>
                        </div>
                        <div class="sp-editor-actions">
                            <button class="vbtn vbtn-secondary" data-action="clear-draft">Clear</button>
                            <button class="vbtn vbtn-primary" data-action="submit-grade">Submit for Evaluation</button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const textarea = body.querySelector('.sp-writing-textarea');
        const countEl = body.querySelector('.sp-word-count');
        const sentEl = body.querySelector('.sp-sentence-count');

        function _updateCounts() {
            const val = textarea.value.trim();
            const words = val ? val.split(/\s+/).length : 0;
            const sentences = val ? (val.match(/[.!?]+(?:\s+|$)/g) || []).length : 0;
            countEl.textContent = `${words} words`;
            sentEl.textContent = `· ${sentences} sentence${sentences === 1 ? '' : 's'}`;

            // Save draft
            _draftText = textarea.value;
            try {
                localStorage.setItem(_draftKey(p.id), _draftText);
            } catch (e) {}
        }

        textarea.addEventListener('input', _updateCounts);
        _updateCounts();

        const backBtn = body.querySelector('[data-action="back-prompts"]');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                _phase = PHASE.PROMPT_SELECT;
                _renderActiveTab();
            });
        }

        const clearBtn = body.querySelector('[data-action="clear-draft"]');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                if (confirm('Clear your current draft?')) {
                    textarea.value = '';
                    _updateCounts();
                }
            });
        }

        const submitBtn = body.querySelector('[data-action="submit-grade"]');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                const text = textarea.value.trim();
                if (!text) {
                    if (typeof UI !== 'undefined' && UI.toast) UI.toast('Please write something before submitting.', 'warning');
                    else alert('Please write something before submitting.');
                    return;
                }
                _submitForGrading(text);
            });
        }
    }

    function _renderAssessing(body) {
        body.innerHTML = `
            <div class="sp-driller-wrap sp-assessing-wrap">
                <div class="sp-assessing-card">
                    <div class="sp-spinner"></div>
                    <h3 class="sp-assessing-title">Grading Your Submission</h3>
                    <p class="sp-assessing-sub">Evaluating CEFR level, grammar, vocabulary precision, and structural coherence...</p>
                </div>
            </div>
        `;
    }

    async function _submitForGrading(text) {
        _phase = PHASE.ASSESSING;
        _renderActiveTab();

        const engine = _getEngine();
        const p = _selectedPrompt;
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';

        try {
            const context = {
                cefrLevel: p.cefrLevel || 'B2',
                taskType: p.taskType || 'written_production',
                taskInstructions: p.prompt || '',
                targetSkills: p.targetSkills || [],
                taskCompletionPrimary: !!p.taskCompletionPrimary,
                language: lang,
                modality: 'written-production',
                title: p.title || 'Writing Production'
            };

            const result = await engine.grade(text, context);
            _assessmentResult = result;

            // Ingest into LearnerModel
            if (typeof LearnerModel !== 'undefined' && LearnerModel.recordAssessment) {
                LearnerModel.recordAssessment(result, context);
            }
            if (p.targetCompetency && (result.overallScore || 0) >= 75) {
                if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.verifyCompetency === 'function') {
                    LearnerModel.verifyCompetency(p.targetCompetency, result.overallScore, 'writing-studio');
                }
            }

            // Award XP
            if (typeof XP !== 'undefined') {
                const earnedXP = Math.max(10, Math.round(result.overallScore / 5));
                XP.award(earnedXP, 'writing-driller');
            }

            // Clear draft
            try { localStorage.removeItem(_draftKey(p.id)); } catch (e) {}

            _phase = PHASE.RESULTS;
            _renderActiveTab();
        } catch (error) {
            console.error('Assessment failed:', error);
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Could not complete evaluation: ' + error.message, 'error');
            else alert('Could not complete evaluation: ' + error.message);
            _phase = PHASE.WRITING;
            _renderActiveTab();
        }
    }

    function _renderResults(body) {
        if (!_assessmentResult) return;
        const res = _assessmentResult;
        const p = _selectedPrompt || {};
        const score = res.overallScore || 0;
        const dims = res.dimensions || {};
        const errors = res.errors || [];
        const strengths = (res.feedback && res.feedback.strengths) || [];
        const priorities = (res.feedback && res.feedback.priorities) || [];
        const stats = res.localStats || {};

        let scoreColor = 'var(--success)';
        if (score < 60) scoreColor = 'var(--danger)';
        else if (score < 80) scoreColor = 'var(--accent)';

        const catLabels = {
            grammar: 'Grammar',
            vocabulary: 'Vocabulary',
            syntax: 'Syntax & Sentence Structure',
            spelling: 'Spelling',
            punctuation: 'Punctuation',
            register: 'Register & Tone',
            expression: 'Expression & Flow'
        };

        const groupedErrors = {};
        for (const err of errors) {
            const cat = (err.category || 'grammar').toLowerCase();
            if (!groupedErrors[cat]) groupedErrors[cat] = [];
            groupedErrors[cat].push(err);
        }

        const errorsHtml = errors.length ? `
            <div class="sp-results-section">
                <h4 class="sp-section-heading">Detailed Observations & Errors (${errors.length})</h4>
                <div class="sp-error-groups">
                    ${Object.entries(groupedErrors).map(([catKey, catErrors]) => `
                        <div class="sp-error-group">
                            <div class="sp-error-group-header">
                                <span class="sp-error-group-title">${_esc(catLabels[catKey] || catKey.charAt(0).toUpperCase() + catKey.slice(1))}</span>
                                <span class="sp-error-group-badge">${catErrors.length} ${catErrors.length === 1 ? 'observation' : 'observations'}</span>
                            </div>
                            <div class="sp-errors-list">
                                ${catErrors.map(err => `
                                    <div class="sp-error-card sp-severity-${_esc(err.severity)}">
                                        <div class="sp-error-head">
                                            <span class="sp-severity-tag sp-severity-${_esc(err.severity)}">${_esc(err.severity)}</span>
                                            ${err.skillId ? `<span class="sp-skill-tag">${_esc(err.skillId)}</span>` : ''}
                                        </div>
                                        <p class="sp-error-quote">"${_esc(err.text)}"</p>
                                        <p class="sp-error-expl">${_esc(err.explanation)}</p>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        ` : '';


        body.innerHTML = `
            <div class="sp-driller-wrap sp-results-wrap">
                <div class="sp-results-score-card">
                    <div class="sp-score-circle" style="border-color: ${scoreColor}">
                        <span class="sp-score-num">${score}</span>
                        <span class="sp-score-max">/100</span>
                    </div>
                    <div class="sp-score-meta">
                        <h3 class="sp-score-title">${score >= 80 ? 'Strong Performance' : (score >= 60 ? 'Developing Competence' : 'Needs Practice')}</h3>
                        <p class="sp-score-sub">${_esc(p.title || 'Writing Production')} · CEFR ${_esc(p.cefrLevel || 'B2')}</p>
                    </div>
                </div>

                ${p.targetCompetency && score >= 75 ? `
                    <div class="sp-competency-verified-banner">
                        <span class="sp-verified-check"><svg class="sp-verified-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                        <span>Demonstrated &amp; Verified: "${_esc(p.targetCompetency)}"</span>
                    </div>
                ` : ''}

                <div class="sp-dimensions-grid">
                    ${Object.entries(dims).map(([dim, val]) => `
                        <div class="sp-dim-card">
                            <span class="sp-dim-name">${_esc(dim.charAt(0).toUpperCase() + dim.slice(1))}</span>
                            <div class="sp-dim-bar"><div class="sp-dim-fill" style="width: ${Math.round(val * 100)}%"></div></div>
                            <span class="sp-dim-val">${Math.round(val * 100)}%</span>
                        </div>
                    `).join('')}
                </div>

                <div class="sp-feedback-cols">
                    <div class="sp-feedback-col sp-strengths">
                        <h4>Strengths</h4>
                        <ul>${strengths.map(s => `<li>${_esc(s)}</li>`).join('')}</ul>
                    </div>
                    <div class="sp-feedback-col sp-priorities">
                        <h4>Focus Priorities</h4>
                        <ul>${priorities.map(pr => `<li>${_esc(pr)}</li>`).join('')}</ul>
                    </div>
                </div>

                ${errorsHtml}

                <div class="sp-local-metrics">
                    <span><strong>${stats.wordCount || 0}</strong> words</span>
                    <span><strong>${stats.sentenceCount || 0}</strong> sentences</span>
                    <span><strong>${stats.avgSentenceLength || 0}</strong> avg words/sentence</span>
                </div>

                <div class="vspeed-results-actions" style="margin-top: 2rem;">
                    <button class="vbtn vbtn-secondary" data-action="write-again">Write Another Text</button>
                </div>
            </div>
        `;

        const againBtn = body.querySelector('[data-action="write-again"]');
        if (againBtn) {
            againBtn.addEventListener('click', () => {
                _phase = PHASE.PROMPT_SELECT;
                _selectedPrompt = null;
                _assessmentResult = null;
                _renderActiveTab();
            });
        }

        // Mount RecommendationEngine Next Action
        if (typeof RecommendationEngine !== 'undefined') {
            const actionsEl = body.querySelector('.vspeed-results-actions');
            if (actionsEl) {
                RecommendationEngine.mountNextAction(actionsEl, { excludeDrillerId: 'writing' });
            }
        }
    }

    // ----------------------------------------
    // PUBLIC API
    // ----------------------------------------

    async function render(container, options = {}) {
        _container = container;
        await _loadPrompts();

        if (options && options.targetCompetency) {
            _activeStudioTab = STUDIO_TAB.COMPOSITION;
            _selectedPrompt = {
                id: 'comp_' + Date.now(),
                title: options.targetCompetency.length > 40 ? options.targetCompetency.slice(0, 37) + '...' : options.targetCompetency,
                cefrLevel: options.level || 'A1',
                targetWords: 35,
                prompt: `Demonstrate this ability in writing: "${options.targetCompetency}". Write clearly and naturally — however much the task itself calls for.`,
                targetCompetency: options.targetCompetency,
                taskCompletionPrimary: true
            };
            _draftText = '';
            _phase = PHASE.WRITING;
            _renderStudioShell();
            return;
        }

        if (options && options.activeTab) {
            _activeStudioTab = (options.activeTab === 'translation' || options.activeTab === 'translate')
                ? STUDIO_TAB.TRANSLATION
                : STUDIO_TAB.COMPOSITION;
        }
        _subOptions = options;

        _phase = PHASE.PROMPT_SELECT;
        _renderStudioShell();
    }

    function stop() {
        if (_activeStudioTab === STUDIO_TAB.TRANSLATION && typeof TranslationDriller !== 'undefined') {
            try { TranslationDriller.stop(); } catch (e) {}
        }
    }

    return {
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.WritingDriller = WritingDriller;
    window.WritingStudio = WritingDriller; // alias for clarity
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = WritingDriller;
}

