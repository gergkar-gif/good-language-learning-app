// ============================================
// CEFR LEVEL DIAGNOSTIC PLACEMENT TEST
// ============================================
// Multi-tier, deterministic diagnostic placement exam assessing learner
// proficiency across CEFR tiers (A1, A2, B1, and expandable to B2/C1).
//
// Pedagogical principle:
// "This is just a quick diagnostic test; mistakes are possible. If you feel
// shaky, you should still do the classes — we are not doing language learning
// to finish a course, but to actually be able to communicate."
//
// Designed to be completely course-agnostic: reads whatever tiers are defined
// in content/<lang>/tests/diagnostic-test.json and dynamically evaluates placement.

const DiagnosticTest = (function () {
    'use strict';

    const PHASE = {
        PREFACE: 'preface',
        TESTING: 'testing',
        TIER_TRANSITION: 'tier_transition',
        DEBRIEF: 'debrief'
    };

    let _testData = null;
    let _loadedLang = null;
    let _phase = PHASE.PREFACE;
    let _currentTierIdx = 0;
    let _currentQuestionIdx = 0;
    let _answers = {}; // qId -> optionIndex
    let _shuffledOptions = {}; // qId -> array of { text, originalIdx }
    let _tierResults = []; // array of { level, correct, total, passed }
    let _openingTab = 'home';
    let _exitCallback = null;

    function _storageKey() {
        return (typeof Lang !== 'undefined') ? Lang.key('diagnosticResult') : 'parlour_diagnostic_result';
    }

    function _onboardingDismissedKey() {
        return (typeof Lang !== 'undefined') ? Lang.key('diagnosticOnboardingDismissed') : 'parlour_diag_dismissed';
    }

    function result() {
        try {
            return JSON.parse(localStorage.getItem(_storageKey()) || 'null');
        } catch (e) {
            return null;
        }
    }

    function hasTaken() {
        return !!result();
    }

    function isOnboardingDismissed() {
        return localStorage.getItem(_onboardingDismissedKey()) === 'true';
    }

    function dismissOnboarding() {
        localStorage.setItem(_onboardingDismissedKey(), 'true');
    }

    function _saveResult(placedLevel, tierResults, jumpedAhead) {
        const payload = {
            level: placedLevel,
            completedAt: new Date().toISOString(),
            tierResults: tierResults || [],
            jumpedAhead: !!jumpedAhead
        };
        try {
            localStorage.setItem(_storageKey(), JSON.stringify(payload));
        } catch (e) {
            console.warn('Could not save diagnostic result:', e);
        }
        dismissOnboarding();
        if (typeof document !== 'undefined') {
            document.dispatchEvent(new CustomEvent('diagnostic-completed', { detail: payload }));
        }
    }

    async function _load() {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        if (_testData && _loadedLang === lang) return _testData;
        try {
            const url = (typeof Lang !== 'undefined')
                ? Lang.content('tests/diagnostic-test.json')
                : `content/${lang}/tests/diagnostic-test.json`;
            const res = await fetch(url);
            _testData = res.ok ? await res.json() : null;
            _loadedLang = lang;
        } catch (e) {
            console.warn('DiagnosticTest: failed to load diagnostic-test.json', e);
            _testData = null;
        }
        return _testData;
    }

    function _shuffle(arr) {
        const out = arr.slice();
        for (let i = out.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [out[i], out[j]] = [out[j], out[i]];
        }
        return out;
    }

    function _esc(v) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(v)
            : String(v == null ? '' : v).replace(/[&<>"']/g, c => ({
                '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
            }[c]));
    }

    function _host() {
        let el = document.getElementById('leveltest-root');
        if (!el) el = document.getElementById('diagnostic-root');
        return el;
    }

    function _render() {
        const host = _host();
        if (!host) return;

        if (_phase === PHASE.PREFACE) {
            _renderPreface(host);
        } else if (_phase === PHASE.TESTING) {
            _renderTesting(host);
        } else if (_phase === PHASE.TIER_TRANSITION) {
            _renderTierTransition(host);
        } else if (_phase === PHASE.DEBRIEF) {
            _renderDebrief(host);
        }
    }

    function _renderPreface(host) {
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        host.innerHTML = `
            <div class="diag-wrap">
                <div class="diag-header-bar">
                    <button type="button" class="dk-back" data-action="close-diag">← Back</button>
                    <span class="sp-level-pill">CEFR Diagnostic</span>
                </div>

                <div class="diag-preface-card">
                    <h2 class="diag-title">CEFR Level Diagnostic Placement</h2>
                    <p class="diag-lead">
                        Find your optimal starting place in ${langName}. This adaptive test quickly checks your language foundations and guides you to the right level.
                    </p>

                    <div class="diag-philosophy-callout">
                        <div class="diag-callout-header">
                            <svg class="sp-icon-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
                            <strong>Quick Diagnostic Screener</strong>
                        </div>
                        <p class="diag-callout-text">
                            This is a rapid 10-question placement screener evaluating core grammar, situational communication, and active recall. Each tier requires <strong>85% mastery</strong> (including open production) to advance.
                        </p>
                        <p class="diag-callout-text" style="margin-top: 8px;">
                            <strong>Full Certification Note:</strong> This screener provides an initial course entry recommendation. For comprehensive multi-modal proficiency verification (including extended written composition and recorded oral speech evaluation), complete the official <strong>Level Test</strong> at the end of each curriculum tier.
                        </p>
                    </div>

                    <div class="diag-preface-meta">
                        <div class="diag-meta-item">
                            <span class="diag-meta-label">Course</span>
                            <div class="diag-lang-chips">
                                ${(typeof Lang !== 'undefined' ? Lang.available() : ['es', 'hu']).map(c => {
                                    const isCur = c === ((typeof Lang !== 'undefined') ? Lang.code() : 'es');
                                    const cName = (typeof Lang !== 'undefined') ? Lang.nameFor(c) : c;
                                    return `
                                        <button type="button" class="diag-lang-chip ${isCur ? 'is-active' : ''}" data-diag-lang="${_esc(c)}" ${isCur ? 'aria-pressed="true"' : 'aria-pressed="false"'}>
                                            ${_esc(cName)}
                                        </button>
                                    `;
                                }).join('')}
                            </div>
                        </div>
                        <div class="diag-meta-item">
                            <span class="diag-meta-label">Format</span>
                            <span class="diag-meta-val">10 Questions/Tier (MC &amp; Open Production)</span>
                        </div>
                        <div class="diag-meta-item">
                            <span class="diag-meta-label">Duration</span>
                            <span class="diag-meta-val">5–7 minutes</span>
                        </div>
                        <div class="diag-meta-item">
                            <span class="diag-meta-label">Passing Standard</span>
                            <span class="diag-meta-val">85% Required to Advance</span>
                        </div>
                    </div>

                    <div class="diag-preface-actions">
                        <button type="button" class="wk-primary-btn diag-btn-start" data-action="begin-diag">
                            Begin Diagnostic Test →
                        </button>
                        <button type="button" class="wk-secondary-btn diag-btn-skip" data-action="skip-to-a1">
                            Start from Level A1 (No Test)
                        </button>
                    </div>
                </div>
            </div>
        `;

        const closeBtn = host.querySelector('[data-action="close-diag"]');
        if (closeBtn) closeBtn.addEventListener('click', close);

        host.querySelectorAll('[data-diag-lang]').forEach(btn => {
            btn.addEventListener('click', async () => {
                const nextLang = btn.getAttribute('data-diag-lang');
                if (nextLang && typeof Lang !== 'undefined' && nextLang !== Lang.code()) {
                    Lang.set(nextLang);
                    _testData = null;
                    _loadedLang = null;
                    await _load();
                    _render();
                }
            });
        });

        const startBtn = host.querySelector('[data-action="begin-diag"]');
        if (startBtn) startBtn.addEventListener('click', _startTesting);

        const skipBtn = host.querySelector('[data-action="skip-to-a1"]');
        if (skipBtn) skipBtn.addEventListener('click', () => {
            dismissOnboarding();
            close();
            if (typeof showTab === 'function') {
                showTab('learn', document.querySelector('.nav button[data-tab="learn"]'));
            }
        });
    }

    function _startTesting() {
        _currentTierIdx = 0;
        _currentQuestionIdx = 0;
        _answers = {};
        _shuffledOptions = {};
        _tierResults = [];
        _phase = PHASE.TESTING;
        _render();
    }

    function _renderTesting(host) {
        const tiers = (_testData && _testData.tiers) ? _testData.tiers : [];
        const tier = tiers[_currentTierIdx];
        if (!tier) {
            _finishDebrief();
            return;
        }

        const questions = tier.questions || [];
        const q = questions[_currentQuestionIdx];
        if (!q) {
            _evaluateCurrentTier();
            return;
        }

        const isTextInput = q.type === 'text-input';
        let canAdvance = false;
        let questionBodyHtml = '';

        if (isTextInput) {
            const typedVal = (typeof _answers[q.id] === 'string') ? _answers[q.id] : '';
            canAdvance = typedVal.trim().length > 0;
            questionBodyHtml = `
                <div class="diag-production-box">
                    <div class="diag-text-input-wrap">
                        <input type="text"
                               class="diag-text-input"
                               id="diag-input-${_esc(q.id)}"
                               autocomplete="off"
                               autocapitalize="off"
                               spellcheck="false"
                               placeholder="Type the missing word or phrase..."
                               value="${_esc(typedVal)}"
                               aria-label="Your answer">
                    </div>
                    ${typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('.diag-text-input') : ''}
                    <div class="diag-production-hint">
                        Type the exact missing word or phrase. Accented letters (like ñ) will pop up as you type them. Press Enter to proceed.
                    </div>
                </div>
            `;
        } else {
            if (!_shuffledOptions[q.id]) {
                const raw = (q.options || []).map((text, idx) => ({ text, originalIdx: idx }));
                _shuffledOptions[q.id] = _shuffle(raw);
            }
            const optionsList = _shuffledOptions[q.id];
            const selectedOrigIdx = _answers[q.id];
            canAdvance = selectedOrigIdx !== undefined;

            questionBodyHtml = `
                <div class="diag-options-grid" role="radiogroup" aria-label="Answer options">
                    ${optionsList.map((opt, i) => {
                        const isSelected = selectedOrigIdx === opt.originalIdx;
                        return `
                            <button type="button" class="diag-opt-btn ${isSelected ? 'selected' : ''}" data-option-idx="${opt.originalIdx}" role="radio" aria-checked="${isSelected}">
                                <span class="diag-opt-letter">${String.fromCharCode(65 + i)}</span>
                                <span class="diag-opt-text">${_esc(opt.text)}</span>
                                ${isSelected ? '<span class="diag-opt-check"><svg class="sp-icon-svg" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>' : ''}
                            </button>
                        `;
                    }).join('')}
                </div>
            `;
        }

        const isLastQuestionInTier = _currentQuestionIdx === questions.length - 1;
        const promptHtml = q.prompt ? `
            <div class="diag-situational-prompt">
                <span class="diag-situational-label">Situational Context</span>
                <div>${_esc(q.prompt)}</div>
            </div>
        ` : '';

        host.innerHTML = `
            <div class="diag-wrap">
                <div class="diag-header-bar">
                    <button type="button" class="dk-back" data-action="close-diag">← Quit</button>
                    <div class="diag-tier-status">
                        <span class="diag-tier-pill">Tier ${_currentTierIdx + 1} of ${tiers.length}: ${_esc(tier.level)} · 85% to Pass</span>
                        <span class="diag-q-counter">Question ${_currentQuestionIdx + 1} of ${questions.length}</span>
                    </div>
                </div>

                <div class="diag-question-card">
                    <div class="diag-tier-info">
                        <h3 class="diag-tier-name">${_esc(tier.name || tier.level)}</h3>
                        <p class="diag-tier-sub">${_esc(tier.description || '')}</p>
                    </div>

                    ${promptHtml}

                    <div class="diag-prompt-box">
                        <div class="diag-sentence">${_esc(q.sentence || '').replace(/_____/g, '<span class="diag-blank">_____</span>')}</div>
                    </div>

                    ${questionBodyHtml}

                    <div class="diag-nav-bar">
                        ${_currentQuestionIdx > 0 ? `
                            <button type="button" class="wk-secondary-btn" data-action="prev-q">← Previous</button>
                        ` : '<div></div>'}

                        <button type="button" class="wk-primary-btn" data-action="next-q" ${canAdvance ? '' : 'disabled'}>
                            ${isLastQuestionInTier ? 'Complete Tier →' : 'Next Question →'}
                        </button>
                    </div>
                </div>
            </div>
        `;

        const closeBtn = host.querySelector('[data-action="close-diag"]');
        if (closeBtn) closeBtn.addEventListener('click', close);

        if (isTextInput) {
            const inputEl = host.querySelector('.diag-text-input');
            if (inputEl) {
                setTimeout(() => {
                    try { inputEl.focus(); } catch (e) {}
                }, 40);

                inputEl.addEventListener('input', () => {
                    _answers[q.id] = inputEl.value;
                    const nextBtn = host.querySelector('[data-action="next-q"]');
                    if (nextBtn) {
                        nextBtn.disabled = !inputEl.value.trim();
                    }
                });

                inputEl.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        if (inputEl.value.trim()) {
                            const nextBtn = host.querySelector('[data-action="next-q"]');
                            if (nextBtn && !nextBtn.disabled) {
                                nextBtn.click();
                            }
                        }
                    }
                });
            }
        } else {
            host.querySelectorAll('[data-option-idx]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const idx = parseInt(btn.getAttribute('data-option-idx'), 10);
                    _answers[q.id] = idx;
                    _render();
                });
            });
        }

        const prevBtn = host.querySelector('[data-action="prev-q"]');
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (_currentQuestionIdx > 0) {
                    _currentQuestionIdx--;
                    _render();
                }
            });
        }

        const nextBtn = host.querySelector('[data-action="next-q"]');
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (_currentQuestionIdx + 1 < questions.length) {
                    _currentQuestionIdx++;
                    _render();
                } else {
                    _evaluateCurrentTier();
                }
            });
        }
    }

    function _evaluateCurrentTier() {
        const tiers = (_testData && _testData.tiers) ? _testData.tiers : [];
        const tier = tiers[_currentTierIdx];
        if (!tier) {
            _finishDebrief();
            return;
        }

        const questions = tier.questions || [];
        let correct = 0;
        questions.forEach(q => {
            const userAns = _answers[q.id];
            if (q.type === 'text-input') {
                if (typeof userAns === 'string' && userAns.trim()) {
                    const cleanUser = userAns.trim().toLowerCase();
                    const normUser = cleanUser.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
                    const accepted = [q.answer, ...(q.altAnswers || [])].filter(Boolean).map(a => a.trim().toLowerCase());
                    const normAccepted = accepted.map(a => a.normalize('NFD').replace(/[\u0300-\u036f]/g, ''));
                    if (accepted.includes(cleanUser) || normAccepted.includes(normUser)) {
                        correct++;
                    }
                }
            } else {
                if (userAns === q.correct) correct++;
            }
        });

        const ratio = questions.length > 0 ? (correct / questions.length) : 0;
        const passRatio = (typeof _testData.passRatio === 'number') ? _testData.passRatio : 0.85;
        const passed = ratio >= passRatio;

        _tierResults.push({
            level: tier.level,
            name: tier.name || tier.level,
            correct,
            total: questions.length,
            passed
        });

        if (passed && _currentTierIdx + 1 < tiers.length) {
            _currentTierIdx++;
            _currentQuestionIdx = 0;
            _phase = PHASE.TIER_TRANSITION;
            _render();
        } else {
            _finishDebrief();
        }
    }

    function _renderTierTransition(host) {
        const tiers = (_testData && _testData.tiers) ? _testData.tiers : [];
        const prevTier = tiers[_currentTierIdx - 1];
        const nextTier = tiers[_currentTierIdx];
        const lastResult = _tierResults[_tierResults.length - 1];

        host.innerHTML = `
            <div class="diag-wrap">
                <div class="diag-transition-card">
                    <span class="sp-level-pill">${_esc(prevTier.level)} Tier Cleared</span>
                    <h2 class="diag-title">${_esc(prevTier.level)} Foundations Mastered!</h2>
                    <p class="diag-transition-score">
                        You scored <strong>${lastResult.correct} of ${lastResult.total}</strong> (85%+ required) on ${_esc(prevTier.level)}.
                    </p>
                    <p class="diag-lead" style="margin-bottom: 24px;">
                        Advancing to <strong>${_esc(nextTier.name || nextTier.level)}</strong> to evaluate higher CEFR competencies.
                    </p>
                    <button type="button" class="wk-primary-btn diag-btn-start" data-action="continue-next-tier">
                        Continue to Tier ${_currentTierIdx + 1} (${_esc(nextTier.level)}) →
                    </button>
                </div>
            </div>
        `;

        const contBtn = host.querySelector('[data-action="continue-next-tier"]');
        if (contBtn) {
            contBtn.addEventListener('click', () => {
                _phase = PHASE.TESTING;
                _render();
            });
        }
    }

    function _finishDebrief() {
        _phase = PHASE.DEBRIEF;
        _render();
    }

    function _determinePlacement() {
        const tiers = (_testData && _testData.tiers) ? _testData.tiers : [];
        const levelsOrder = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];

        if (_tierResults.length === 0) return 'A1';

        // Find the highest tier that was passed
        let highestPassedIdx = -1;
        for (let i = 0; i < _tierResults.length; i++) {
            if (_tierResults[i].passed) {
                highestPassedIdx = i;
            } else {
                break;
            }
        }

        if (highestPassedIdx === -1) {
            return tiers[0] ? tiers[0].level : 'A1';
        }

        // If learner passed tier i, place them into tier i + 1
        const passedLevel = _tierResults[highestPassedIdx].level;
        const normPassed = passedLevel.toUpperCase();
        const orderIdx = levelsOrder.indexOf(normPassed);

        if (orderIdx !== -1 && orderIdx + 1 < levelsOrder.length) {
            return levelsOrder[orderIdx + 1];
        }

        return passedLevel;
    }

    function _renderDebrief(host) {
        const placedLevel = _determinePlacement();
        const langName = (typeof Lang !== 'undefined') ? Lang.name() : 'the language';

        let coachSentence = '';
        if (placedLevel.toUpperCase() === 'A1') {
            coachSentence = `You are starting at Level A1 (Foundations), which is the perfect place to build solid roots in ${langName} pronunciation, essential grammar, and daily conversational formulas.`;
        } else if (placedLevel.toUpperCase() === 'A2') {
            coachSentence = `You demonstrated solid command of A1 fundamentals; your optimal starting place is Level A2 (Elementary) to master narrative past tenses, pronouns, and everyday communicative situations.`;
        } else if (placedLevel.toUpperCase() === 'B1') {
            coachSentence = `You demonstrated clear competence in basic communication and past narration; Level B1 (Intermediate) is your ideal starting stage to tackle the subjunctive mood, complex clauses, and independent expression.`;
        } else {
            coachSentence = `Outstanding proficiency! You demonstrated command of foundational and intermediate ${langName}; you are placed directly into ${placedLevel} for advanced communicative expression.`;
        }

        const levelsOrder = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];
        const placedIdx = levelsOrder.indexOf(placedLevel.toUpperCase());
        const precedingLevels = placedIdx > 0 ? levelsOrder.slice(0, placedIdx) : [];

        host.innerHTML = `
            <div class="diag-wrap">
                <div class="diag-header-bar">
                    <button type="button" class="dk-back" data-action="close-diag">← Exit</button>
                    <span class="sp-level-pill">Placement Debrief</span>
                </div>

                <div class="diag-debrief-card">
                    <div class="diag-verdict-banner">
                        <span class="diag-verdict-eyebrow">Diagnostic Recommendation</span>
                        <h2 class="diag-verdict-title">Placed into Level ${_esc(placedLevel)}</h2>
                        <span class="diag-verdict-level-pill">${_esc(placedLevel)} · CEFR Recommended</span>
                    </div>

                    <div class="sp-coach-note-card" style="margin: 20px 0;">
                        <div class="sp-coach-note-header">
                            <span class="sp-coach-avatar">
                                <svg class="sp-icon-svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                            </span>
                            <strong>Diagnostic Assessment Summary</strong>
                        </div>
                        <p class="sp-coach-note-body">${_esc(coachSentence)}</p>
                    </div>

                    <div class="diag-breakdown-section">
                        <h4 style="margin: 0 0 10px; font-size: 0.9rem; color: var(--muted); text-transform: uppercase;">Tier Performance Breakdown</h4>
                        <div class="diag-tiers-summary">
                            ${_tierResults.map(r => `
                                <div class="diag-tier-summary-item ${r.passed ? 'passed' : 'developing'}">
                                    <div class="diag-ts-left">
                                        <strong>Tier ${_esc(r.level)}</strong>
                                        <span class="diag-ts-desc">${_esc(r.name)}</span>
                                    </div>
                                    <div class="diag-ts-right">
                                        <span class="diag-ts-score">${r.correct}/${r.total}</span>
                                        <span class="diag-ts-badge">${r.passed ? 'Mastered' : 'Developing'}</span>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>

                    <div class="diag-pedagogical-reminder" style="margin-top: 20px; padding: 14px; background: var(--wash, #f8f9fa); border-radius: var(--radius-sm, 4px); font-size: 0.85rem; color: var(--muted); line-height: 1.55;">
                        <p style="margin: 0 0 8px;"><strong>Placement Recommendation:</strong> Accepting placement unlocks your recommended starting level (${_esc(placedLevel)}), but all previous curriculum lessons remain open for practice and review at any time.</p>
                        <p style="margin: 0;"><strong>Comprehensive Multi-Modal Verification:</strong> This test is an initial rapid screener. Full CEFR certifications (including spoken recording and extended writing evaluation) are verified via the official <strong>Level Tests</strong> at the end of each curriculum level.</p>
                    </div>

                    <div class="diag-debrief-actions" style="margin-top: 24px; display: flex; flex-direction: column; gap: 10px;">
                        ${precedingLevels.length > 0 ? `
                            <button type="button" class="wk-primary-btn" data-action="accept-jump">
                                Accept Placement &amp; Jump to Level ${_esc(placedLevel)} →
                            </button>
                        ` : `
                            <button type="button" class="wk-primary-btn" data-action="accept-start">
                                Start Learning at Level A1 →
                            </button>
                        `}

                        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                            <button type="button" class="wk-secondary-btn" data-action="start-a1-anyway" style="flex: 1;">
                                Start from Level A1 Anyway
                            </button>
                            <button type="button" class="wk-secondary-btn" data-action="retake-diag" style="flex: 1;">
                                Retake Diagnostic
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const closeBtn = host.querySelector('[data-action="close-diag"]');
        if (closeBtn) closeBtn.addEventListener('click', close);

        const acceptJumpBtn = host.querySelector('[data-action="accept-jump"]');
        if (acceptJumpBtn) {
            acceptJumpBtn.addEventListener('click', () => {
                _executeJumpAhead(placedLevel);
            });
        }

        const acceptStartBtn = host.querySelector('[data-action="accept-start"]');
        if (acceptStartBtn) {
            acceptStartBtn.addEventListener('click', () => {
                _saveResult(placedLevel, _tierResults, false);
                close();
                if (typeof showTab === 'function') {
                    showTab('learn', document.querySelector('.nav button[data-tab="learn"]'));
                }
            });
        }

        const startA1Btn = host.querySelector('[data-action="start-a1-anyway"]');
        if (startA1Btn) {
            startA1Btn.addEventListener('click', () => {
                _saveResult(placedLevel, _tierResults, false);
                close();
                if (typeof showTab === 'function') {
                    showTab('learn', document.querySelector('.nav button[data-tab="learn"]'));
                }
            });
        }

        const retakeBtn = host.querySelector('[data-action="retake-diag"]');
        if (retakeBtn) {
            retakeBtn.addEventListener('click', () => {
                _startTesting();
            });
        }
    }

    async function _executeJumpAhead(placedLevel) {
        if (!window._curriculumData && typeof loadCurriculumData === 'function') {
            try {
                window._curriculumData = await loadCurriculumData();
            } catch (e) {
                console.warn('DiagnosticTest: could not preload curriculum data:', e);
            }
        }

        const levelsOrder = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];
        const placedIdx = levelsOrder.indexOf(placedLevel.toUpperCase());
        const precedingLevels = placedIdx > 0 ? levelsOrder.slice(0, placedIdx) : [];

        if (typeof markLevelComplete === 'function') {
            precedingLevels.forEach(lvl => {
                try {
                    markLevelComplete(lvl);
                } catch (e) {
                    console.warn('Could not mark level complete:', lvl, e);
                }
            });
        }

        _saveResult(placedLevel, _tierResults, true);

        if (typeof UI !== 'undefined' && UI.toast) {
            UI.toast(`Placed into Level ${placedLevel}! Preceding levels marked complete.`, 'success');
        }

        close();
        if (typeof showTab === 'function') {
            showTab('learn', document.querySelector('.nav button[data-tab="learn"]'));
        }
    }

    async function open(options = {}) {
        _exitCallback = (options && typeof options.onExit === 'function') ? options.onExit : null;
        try {
            const currentTab = document.querySelector('.tab:not(.hidden)');
            if (currentTab && currentTab.id && currentTab.id !== 'leveltest') {
                _openingTab = currentTab.id;
            }
        } catch (e) {}

        await _load();
        if (!_testData) {
            if (typeof UI !== 'undefined' && UI.toast) {
                UI.toast('Diagnostic test content not available for this course yet.', 'warning');
            }
            return;
        }

        _phase = (options && options.phase) ? options.phase : PHASE.PREFACE;

        if (typeof document !== 'undefined') {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
            const hostTab = document.getElementById('leveltest');
            if (hostTab) hostTab.classList.remove('hidden');

            if (typeof PageHeader !== 'undefined' && PageHeader.render) {
                PageHeader.render({
                    title: 'CEFR Diagnostic',
                    subtitle: 'Adaptive placement assessment.',
                    illustration: 'ascent'
                });
            }
        }

        _render();
    }

    function close() {
        stop();
        if (typeof document !== 'undefined') {
            const hostTab = document.getElementById('leveltest');
            if (hostTab) hostTab.classList.add('hidden');

            const targetTab = _openingTab || 'home';
            const btn = document.querySelector(`.nav button[data-tab="${targetTab}"]`);
            if (typeof showTab === 'function') {
                showTab(targetTab, btn);
            }
        }
        if (typeof _exitCallback === 'function') {
            _exitCallback();
            _exitCallback = null;
        }
    }

    function stop() {
        _phase = PHASE.PREFACE;
        const host = _host();
        if (host) host.innerHTML = '';
    }

    return {
        open,
        close,
        stop,
        result,
        hasTaken,
        isOnboardingDismissed,
        dismissOnboarding,
        _determinePlacement,
        _evaluateCurrentTier
    };
})();

if (typeof window !== 'undefined') {
    window.DiagnosticTest = DiagnosticTest;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DiagnosticTest;
}
