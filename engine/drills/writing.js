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

        const guideBanner = (typeof Guide !== 'undefined' && !Guide.hasSeen('production'))
            ? Guide.renderBannerHtml('production')
            : '';

        _container.innerHTML = `
            ${guideBanner}
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

        _container.querySelectorAll('[data-guide-dismiss]').forEach(btn => {
            btn.addEventListener('click', () => {
                const featureId = btn.getAttribute('data-guide-dismiss');
                if (typeof Guide !== 'undefined') Guide.markSeen(featureId);
                const banner = btn.closest('.pl-guide-banner');
                if (banner) banner.remove();
            });
        });

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
                const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';
                const langCode = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
                const formatted = (typeof CanDoPrompt !== 'undefined')
                    ? CanDoPrompt.formatPrompt(text, {
                        language: langName,
                        langCode: langCode,
                        modality: 'written',
                        level: (found && found.level) || 'A1'
                    })
                    : null;
                _selectedPrompt = {
                    id: 'comp_' + Date.now(),
                    title: formatted ? formatted.title : (text.length > 35 ? text.slice(0, 32) + '...' : text),
                    scenario: formatted ? formatted.scenario : '',
                    cefrLevel: (found && found.level) || 'A1',
                    targetWords: 35,
                    prompt: formatted ? formatted.prompt : `Demonstrate this ability in writing: "${text}". Write clearly and naturally — however much the task itself calls for.`,
                    cues: formatted ? formatted.cues : [],
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
                    ${p.scenario ? `<p class="sp-prompt-detail-scenario" style="margin: 4px 0 8px 0; font-size: 0.9rem; color: var(--text-muted); font-style: italic;">${_esc(p.scenario)}</p>` : ''}
                    <p class="sp-prompt-detail-desc">${_esc(p.prompt)}</p>
                    ${p.cues && p.cues.length ? `
                        <div class="sp-prompt-cues" style="margin-top: 10px; padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 6px; text-align: left;">
                            <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); letter-spacing: 0.04em; display: block; margin-bottom: 2px;">Points to include:</span>
                            <ul style="margin: 2px 0 0 0; padding-left: 18px; font-size: 0.88rem; color: var(--text);">
                                ${p.cues.map(c => `<li style="margin-bottom: 2px;">${_esc(c)}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
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

    function _cleanFragment(str) {
        if (!str || typeof str !== 'string') return '';
        let s = str.trim();
        if ((s.startsWith('"') && s.endsWith('"')) || 
            (s.startsWith('“') && s.endsWith('”')) || 
            (s.startsWith("'") && s.endsWith("'") && !s.slice(1, -1).includes("'"))) {
            s = s.slice(1, -1).trim();
        }
        s = s.replace(/[.;,:!]+$/, '').trim();
        return s;
    }

    function _lowerFirstChar(str) {
        if (!str) return '';
        if (/^[A-Z]{2,}\b/.test(str)) return str;
        if (/^(Spanish|Hungarian|English|Castilian)\b/i.test(str)) return str;
        return str.charAt(0).toLowerCase() + str.slice(1);
    }

    function _formatCoachingClause(raw) {
        let text = _cleanFragment(raw);
        if (!text) return '';

        // Strip meta prefixes like "Remember to...", "Be sure to...", "Try to..."
        text = text.replace(/^(please\s+)?(remember\s+to|be\s+sure\s+to|make\s+sure\s+to|ensure\s+you|try\s+to)\s+/i, '');
        text = _cleanFragment(text);

        // Standard action verbs (practice, review, use, conjugate, keep, watch, avoid, pay attention to, focus on, etc.)
        const actionVerbPattern = /^(practice|review|use|conjugate|keep|watch|avoid|pay\s+attention|focus\s+on|apply|distinguish|work\s+on|include|add)\b/i;
        if (actionVerbPattern.test(text)) {
            return _lowerFirstChar(text);
        }

        // Grammar error explanations ("The verb 'tener' should be used...", "Gender agreement...")
        if (/^the\s+(verb|noun|adjective|article|pronoun|preposition|phrase|word)\b/i.test(text) ||
            /^(in\s+spanish|in\s+hungarian|gender\s+agreement|subject-verb\s+agreement|verb\s+tense)\b/i.test(text)) {
            return 'note that ' + _lowerFirstChar(text);
        }

        return 'focus on ' + _lowerFirstChar(text);
    }

    // Composes a single, naturally flowing extended sentence for short task coaching:
    // an opening completion appraisal connected smoothly to actionable coaching advice.
    function _shortTaskTip(result, prompt) {
        const score = result.overallScore || 0;
        const completion = typeof result.taskCompletion === 'number' ? result.taskCompletion : (score / 100);
        const priorities = ((result.feedback && result.feedback.priorities) || []).filter(Boolean);
        const errors = (result.errors || []).map(e => e.explanation).filter(Boolean);
        const strengths = ((result.feedback && result.feedback.strengths) || []).filter(Boolean);

        let opener;
        if (completion >= 0.75 || score >= 75) {
            opener = 'Well done — you got your message across';
        } else if (completion >= 0.4 || score >= 50) {
            opener = 'Good effort — you got most of it across';
        } else {
            opener = 'Good start, but you didn\'t quite cover the prompt';
        }

        // Gather up to 2 actionable priorities or error explanations
        const rawSuggestions = [];
        for (const p of priorities) {
            if (rawSuggestions.length < 2 && p) rawSuggestions.push(p);
        }
        if (rawSuggestions.length < 2) {
            for (const e of errors) {
                if (rawSuggestions.length < 2 && e && !rawSuggestions.includes(e)) {
                    rawSuggestions.push(e);
                }
            }
        }

        // If no suggestions, celebrate success with strength or clear delivery
        if (rawSuggestions.length === 0) {
            if (strengths.length) {
                const cleanStrength = _cleanFragment(strengths[0]);
                return `${opener} with ${_lowerFirstChar(cleanStrength)}!`;
            }
            return `${opener} with clear and accurate phrasing!`;
        }

        const clause1 = _formatCoachingClause(rawSuggestions[0]);
        let combinedCoaching = clause1;

        if (rawSuggestions.length > 1) {
            let clause2 = _formatCoachingClause(rawSuggestions[1]);
            if (clause2.startsWith('focus on ') && clause1.startsWith('focus on ')) {
                clause2 = clause2.slice(9);
            }
            if (clause2.startsWith('note that ') && clause1.startsWith('note that ')) {
                clause2 = clause2.slice(10);
            }
            combinedCoaching = `${clause1} and ${clause2}`;
        }

        if (combinedCoaching.startsWith('note that ')) {
            return `${opener}, but ${combinedCoaching}.`;
        }

        return `${opener}; for next time, ${combinedCoaching}.`;
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

        const isShortProd = !!p.taskCompletionPrimary;
        if (isShortProd) {
            const tip = _shortTaskTip(res, p);

            body.innerHTML = `
                <div class="sp-driller-wrap sp-results-wrap">
                    <div class="sp-results-score-card">
                        <div class="sp-score-circle" style="border-color: ${scoreColor}">
                            <span class="sp-score-num">${score}</span>
                            <span class="sp-score-max">/100</span>
                        </div>
                        <div class="sp-score-meta">
                            <h3 class="sp-score-title">${p.targetCompetency && score >= 75 ? 'Competency Verified' : (score >= 60 ? 'Competent Written Production' : 'Developing Practice')}</h3>
                            <p class="sp-score-sub">${_esc(p.title || 'Writing Production')} · CEFR ${_esc(p.cefrLevel || 'A1')}</p>
                        </div>
                    </div>

                    ${p.targetCompetency && score >= 75 ? `
                        <div class="sp-competency-verified-banner">
                            <span class="sp-verified-check"><svg class="sp-verified-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                            <span>Demonstrated &amp; Verified: "${_esc(p.targetCompetency)}"</span>
                        </div>
                    ` : ''}

                    <div class="sp-challenge-feedback-card" style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px 18px; margin: 16px 0;">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-weight: 700; font-size: 0.92rem; color: var(--text-heading);">Writing Coach</span>
                            <span class="cando-badge ${score >= 60 ? 'cando-badge-verified' : 'cando-badge-gap'}" style="font-size: 0.8rem;">${score}%</span>
                        </div>
                        <p style="margin: 0; font-size: 0.98rem; color: var(--text); line-height: 1.45;">${_esc(tip)}</p>
                    </div>

                    ${_draftText && _draftText.trim() ? `
                        <div class="sp-prod-transcript-preview" style="margin-top: 12px; padding: 10px 14px; background: rgba(0,0,0,0.03); border-radius: 8px; font-size: 0.92rem; color: var(--text);">
                            <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); letter-spacing: 0.04em; display: block; margin-bottom: 4px;">What you wrote:</span>
                            <p style="margin: 0; font-style: italic;">“${_esc(_draftText.trim())}”</p>
                        </div>
                    ` : ''}

                    <div class="sp-local-metrics" style="margin-top: 14px;">
                        <span><strong>${stats.wordCount || 0}</strong> words</span>
                        <span><strong>${stats.sentenceCount || 0}</strong> sentences</span>
                        <span><strong>CEFR ${_esc(p.cefrLevel || 'A1')}</strong> target</span>
                    </div>

                    <div class="vspeed-results-actions" style="margin-top: 1.5rem; display: flex; gap: 12px; flex-wrap: wrap;">
                        <button type="button" class="vbtn vbtn-primary" data-action="practice-again">Revise &amp; Try Again</button>
                        <button type="button" class="vbtn vbtn-secondary" data-action="write-another">Choose Another Topic</button>
                    </div>
                </div>
            `;

            const againBtn = body.querySelector('[data-action="practice-again"]') || body.querySelector('[data-action="write-again"]');
            if (againBtn) {
                againBtn.addEventListener('click', () => {
                    _phase = PHASE.WRITING;
                    _assessmentResult = null;
                    _renderActiveTab();
                });
            }

            const anotherBtn = body.querySelector('[data-action="write-another"]');
            if (anotherBtn) {
                anotherBtn.addEventListener('click', () => {
                    _phase = PHASE.PROMPT_SELECT;
                    _selectedPrompt = null;
                    _assessmentResult = null;
                    _renderActiveTab();
                });
            }

            if (typeof RecommendationEngine !== 'undefined') {
                const actionsEl = body.querySelector('.vspeed-results-actions');
                if (actionsEl) {
                    RecommendationEngine.mountNextAction(actionsEl, { excludeDrillerId: 'writing' });
                }
            }
            return;
        }

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

                <div class="vspeed-results-actions" style="margin-top: 2rem; display: flex; gap: 12px; flex-wrap: wrap;">
                    <button type="button" class="vbtn vbtn-primary" data-action="practice-again">Revise &amp; Try Again</button>
                    <button type="button" class="vbtn vbtn-secondary" data-action="write-another">Choose Another Topic</button>
                </div>
            </div>
        `;

        const againBtn = body.querySelector('[data-action="practice-again"]');
        if (againBtn) {
            againBtn.addEventListener('click', () => {
                _phase = PHASE.WRITING;
                _assessmentResult = null;
                _renderActiveTab();
            });
        }

        const anotherBtn = body.querySelector('[data-action="write-another"]') || body.querySelector('[data-action="write-again"]');
        if (anotherBtn) {
            anotherBtn.addEventListener('click', () => {
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
            const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';
            const langCode = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
            const formatted = (typeof CanDoPrompt !== 'undefined')
                ? CanDoPrompt.formatPrompt(options.targetCompetency, {
                    language: langName,
                    langCode: langCode,
                    modality: 'written',
                    level: options.level || 'A1'
                })
                : null;
            _selectedPrompt = {
                id: 'comp_' + Date.now(),
                title: formatted ? formatted.title : (options.targetCompetency.length > 35 ? options.targetCompetency.slice(0, 32) + '...' : options.targetCompetency),
                scenario: formatted ? formatted.scenario : '',
                cefrLevel: options.level || 'A1',
                targetWords: 35,
                prompt: formatted ? formatted.prompt : `Demonstrate this ability in writing: "${options.targetCompetency}". Write clearly and naturally — however much the task itself calls for.`,
                cues: formatted ? formatted.cues : [],
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
        stop,
        _shortTaskTip
    };
})();

if (typeof window !== 'undefined') {
    window.WritingDriller = WritingDriller;
    window.WritingStudio = WritingDriller; // alias for clarity
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = WritingDriller;
}

