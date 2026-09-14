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

    const PHASE = { PROMPT_SELECT: 1, WRITING: 2, ASSESSING: 3, RESULTS: 4 };

    let _container = null;
    let _phase = PHASE.PROMPT_SELECT;
    let _promptsData = null;
    let _loadedLang = null;
    let _selectedPrompt = null;
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
            else if (_phase === PHASE.WRITING) _renderWriting(body);
            else if (_phase === PHASE.ASSESSING) _renderAssessing(body);
            else if (_phase === PHASE.RESULTS) _renderResults(body);
        }
    }

    // ----------------------------------------
    // RENDER SCREENS (COMPOSITION)
    // ----------------------------------------

    function _renderPromptSelect(body) {
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the target language';
        const prompts = _promptsData || [];

        let promptsHtml = '';
        if (prompts.length > 0) {
            promptsHtml = prompts.map(p => `
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

                <div class="sp-prompt-grid">
                    ${promptsHtml}
                    <div class="wk-card sp-card-clickable sp-card-custom" data-select-custom="1">
                        <div class="sp-prompt-card-head">
                            <span class="sp-level-pill">Free Topic</span>
                        </div>
                        <h3 class="wk-card-title">Free Writing</h3>
                        <p class="wk-card-sub">Write freely on any topic of your choice and receive detailed structural and language feedback.</p>
                    </div>
                </div>
            </div>
        `;

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
                _selectedPrompt = {
                    id: 'custom-topic',
                    cefrLevel: (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel) ? LearnerPath.currentLevel() : 'B2',
                    taskType: 'free_writing',
                    title: 'Free Writing Topic',
                    prompt: 'Write on any topic of your choice in the target language. Focus on expressing clear, well-connected ideas.',
                    minWords: 50,
                    targetWords: 150,
                    maxWords: 350,
                    targetSkills: []
                };
                _draftText = localStorage.getItem(_draftKey('custom')) || '';
                _phase = PHASE.WRITING;
                _renderActiveTab();
            });
        }
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
                    alert('Please write something before submitting.');
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
            alert('Could not complete evaluation: ' + error.message);
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

        const errorsHtml = errors.length ? `
            <div class="sp-results-section">
                <h4 class="sp-section-heading">Detailed Observations & Errors (${errors.length})</h4>
                <div class="sp-errors-list">
                    ${errors.map(err => `
                        <div class="sp-error-card sp-severity-${_esc(err.severity)}">
                            <div class="sp-error-head">
                                <span class="sp-error-cat">${_esc(err.category || 'grammar')}</span>
                                ${err.skillId ? `<span class="sp-skill-tag">${_esc(err.skillId)}</span>` : ''}
                            </div>
                            <p class="sp-error-quote">"${_esc(err.text)}"</p>
                            <p class="sp-error-expl">${_esc(err.explanation)}</p>
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

