// ============================================
// WRITING STUDIO DRILLER
// ============================================
// Longer-form open-ended production driller with CEFR formative assessment.
// Evaluates writing against curriculum standards, provides multi-dimensional
// feedback, and feeds production evidence into the Learner Model.

const WritingDriller = (function () {
    'use strict';

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
    // RENDER SCREENS
    // ----------------------------------------

    function _renderPromptSelect() {
        if (!_container) return;
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

        _container.innerHTML = `
            <div class="sp-driller-wrap">
                <div class="sp-setup-head">
                    <h2 class="sp-setup-title">Writing Studio</h2>
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

        _container.querySelectorAll('[data-select-prompt]').forEach(el => {
            el.addEventListener('click', () => {
                const id = el.getAttribute('data-select-prompt');
                const found = (_promptsData || []).find(p => p.id === id);
                if (found) {
                    _selectedPrompt = found;
                    _draftText = localStorage.getItem(_draftKey(found.id)) || '';
                    _phase = PHASE.WRITING;
                    _renderWriting();
                }
            });
        });

        const customBtn = _container.querySelector('[data-select-custom]');
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
                _renderWriting();
            });
        }
    }

    function _renderWriting() {
        if (!_container || !_selectedPrompt) return;
        const p = _selectedPrompt;

        const skillsPills = (p.targetSkills || []).map(s => {
            const label = typeof s === 'string' ? s : (s.description || s.id);
            return `<span class="sp-skill-pill">${_esc(label)}</span>`;
        }).join('');

        _container.innerHTML = `
            <div class="sp-driller-wrap sp-writing-wrap">
                <div class="sp-writing-header">
                    <button class="vbtn vbtn-secondary sp-back-btn" data-action="back-prompts">← Back</button>
                    <div class="sp-header-info">
                        <span class="sp-level-pill">${_esc(p.cefrLevel)}</span>
                        <span class="sp-words-target">Target: ~${_esc(p.targetWords)} words</span>
                    </div>
                </div>

                <div class="sp-task-card">
                    <h3 class="sp-task-title">${_esc(p.title)}</h3>
                    <p class="sp-task-prompt">${_esc(p.prompt)}</p>
                    ${skillsPills ? `<div class="sp-skills-row">${skillsPills}</div>` : ''}
                </div>

                <div class="sp-editor-box">
                    <textarea class="sp-writing-textarea" placeholder="Type your response here in the target language...">${_esc(_draftText)}</textarea>
                    <div class="sp-editor-status">
                        <div class="sp-counter-group">
                            <span class="sp-word-counter"><strong>0</strong> words</span>
                            <span class="sp-sentence-counter">0 sentences</span>
                        </div>
                        <div class="sp-meter-bar">
                            <div class="sp-meter-fill" style="width: 0%"></div>
                        </div>
                    </div>
                </div>

                <div class="sp-actions-bar">
                    <button class="vbtn vbtn-primary sp-submit-btn" data-action="submit-writing">Submit for Assessment →</button>
                </div>
            </div>
        `;

        const textarea = _container.querySelector('.sp-writing-textarea');
        const wordCounter = _container.querySelector('.sp-word-counter strong');
        const sentenceCounter = _container.querySelector('.sp-sentence-counter');
        const meterFill = _container.querySelector('.sp-meter-fill');
        const backBtn = _container.querySelector('[data-action="back-prompts"]');
        const submitBtn = _container.querySelector('[data-action="submit-writing"]');

        function updateStats() {
            const val = textarea.value;
            _draftText = val;
            try { localStorage.setItem(_draftKey(p.id), val); } catch (e) {}

            const words = val.trim() ? (val.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu) || []) : [];
            const count = words.length;
            wordCounter.textContent = count;

            const sentences = val.trim().split(/(?<=[.!?¿¡])\s+|\n+/).filter(s => s.trim().length > 0);
            sentenceCounter.textContent = `${sentences.length} ${sentences.length === 1 ? 'sentence' : 'sentences'}`;

            const pct = Math.min(100, Math.round((count / (p.targetWords || 150)) * 100));
            meterFill.style.width = pct + '%';
            if (count >= (p.minWords || 30)) {
                meterFill.classList.add('is-ready');
            } else {
                meterFill.classList.remove('is-ready');
            }
        }

        textarea.addEventListener('input', updateStats);
        updateStats();

        backBtn.addEventListener('click', () => {
            _phase = PHASE.PROMPT_SELECT;
            _renderPromptSelect();
        });

        submitBtn.addEventListener('click', async () => {
            const text = textarea.value.trim();
            if (!text || text.split(/\s+/).length < 5) {
                alert('Please write at least a few sentences before submitting.');
                return;
            }
            _phase = PHASE.ASSESSING;
            _renderAssessing();
            await _runAssessment(text);
        });
    }

    function _renderAssessing() {
        if (!_container) return;
        _container.innerHTML = `
            <div class="sp-driller-wrap sp-assessing-wrap">
                <div class="sp-spinner-box">
                    <div class="sp-pulsing-circle"></div>
                    <h3>Evaluating Your Writing</h3>
                    <p class="sp-assessing-sub">Analyzing task completion, grammar control, vocabulary, coherence, and complexity against CEFR standards...</p>
                </div>
            </div>
        `;
    }

    async function _runAssessment(text) {
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
            _renderResults();
        } catch (error) {
            console.error('Assessment failed:', error);
            alert('Could not complete evaluation: ' + error.message);
            _phase = PHASE.WRITING;
            _renderWriting();
        }
    }

    function _renderResults() {
        if (!_container || !_assessmentResult) return;
        const res = _assessmentResult;
        const p = _selectedPrompt || {};
        const score = res.overallScore || 0;
        const dims = res.dimensions || {};
        const errors = res.errors || [];
        const strengths = (res.feedback && res.feedback.strengths) || [];
        const priorities = (res.feedback && res.feedback.priorities) || [];
        const stats = res.localStats || {};

        let scoreColor = '#2e7d32'; // green
        if (score < 60) scoreColor = '#c62828'; // red
        else if (score < 80) scoreColor = '#f57c00'; // amber

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

        _container.innerHTML = `
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
                        <ul>${priorities.map(p => `<li>${_esc(p)}</li>`).join('')}</ul>
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

        const againBtn = _container.querySelector('[data-action="write-again"]');
        if (againBtn) {
            againBtn.addEventListener('click', () => {
                _phase = PHASE.PROMPT_SELECT;
                _selectedPrompt = null;
                _assessmentResult = null;
                _renderPromptSelect();
            });
        }

        // Mount RecommendationEngine Next Action
        if (typeof RecommendationEngine !== 'undefined') {
            const actionsEl = _container.querySelector('.vspeed-results-actions');
            if (actionsEl) {
                RecommendationEngine.mountNextAction(actionsEl, { excludeDrillerId: 'writing' });
            }
        }
    }

    // ----------------------------------------
    // PUBLIC API
    // ----------------------------------------

    async function render(container, options) {
        _container = container;
        await _loadPrompts();
        _phase = PHASE.PROMPT_SELECT;
        _renderPromptSelect();
    }

    function stop() {
        _container = null;
    }

    return {
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.WritingDriller = WritingDriller;
}
