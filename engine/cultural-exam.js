// ============================================
// HUNGARIAN CULTURAL KNOWLEDGE EXAM (Magyar kulturális ismereti vizsga)
// ============================================
// Exam-preparation layer sitting on top of the B1 Hungarian Citizenship track.
// Covers:
//   1. 6 official categories
//   2. Compact list of required facts & explained cultural artifacts
//   3. Exam-specific vocabulary
//   4. Targeted MCQs (filterable by category)
//   5. Name -> Work matching
//   6. Person -> Field matching
//   7. Date -> Event matching
//   8. Symbol -> Meaning matching
//   9. 3 full 30-point Mock Exams (pass mark: 16/30)

const HuCulturalExam = (function () {
    'use strict';

    const STORAGE_KEY = 'parlour_hu_cultural_exam_v1';
    let _data = null;
    let _state = {
        tab: 'categories',        // 'categories' | 'vocab' | 'mcq' | 'matching' | 'mocks'
        selectedCategory: 'all',  // 'all' or category.id
        showEnglishAll: true,
        mcqCategory: 'all',
        mcqAnswers: {},           // { [mcqId]: selectedOptionIdx }
        matchMode: 'nameToWork',  // 'nameToWork' | 'personToField' | 'dateToEvent' | 'symbolToMeaning'
        matchRoundPairs: [],      // array of { id, left, right }
        matchLeftOrder: [],
        matchRightOrder: [],
        matchSelectedLeft: null,
        matchSolvedIds: {},
        matchWrongFlash: false,
        activeMockId: 'mock-1',
        mockAnswers: {},          // { [qIndex]: optionIdx }
        mockSubmitted: false
    };

    function _loadSavedProgress() {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        } catch (e) {
            return {};
        }
    }

    function _saveMockScore(mockId, points, maxPoints, passed) {
        try {
            const saved = _loadSavedProgress();
            saved.mocks = saved.mocks || {};
            const prev = saved.mocks[mockId];
            if (!prev || points >= prev.points) {
                saved.mocks[mockId] = { points, maxPoints, passed, date: new Date().toISOString() };
            }
            localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
        } catch (e) {}
    }

    function _esc(str) {
        if (typeof UI !== 'undefined' && UI.escape) return UI.escape(String(str || ''));
        const d = document.createElement('div');
        d.textContent = String(str || '');
        return d.innerHTML;
    }

    function _shuffle(arr) {
        const copy = arr.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const tmp = copy[i];
            copy[i] = copy[j];
            copy[j] = tmp;
        }
        return copy;
    }

    async function _loadData() {
        if (_data) return _data;
        const path = (typeof Lang !== 'undefined' && Lang.content)
            ? Lang.content('cultural-exam.json')
            : 'content/hu/cultural-exam.json';
        const res = await fetch(path);
        if (!res.ok) throw new Error('Failed to load cultural-exam.json');
        _data = await res.json();
        _initMatchRound();
        return _data;
    }

    function _initMatchRound() {
        if (!_data || !_data.matchingSets) return;
        const set = _data.matchingSets[_state.matchMode] || _data.matchingSets.nameToWork;
        const pool = (set.pairs || []).map((p, idx) => ({
            id: 'pair-' + idx,
            left: p[0],
            right: p[1]
        }));
        const picked = _shuffle(pool).slice(0, 6);
        _state.matchRoundPairs = picked;
        _state.matchLeftOrder = _shuffle(picked.slice());
        _state.matchRightOrder = _shuffle(picked.slice());
        _state.matchSelectedLeft = null;
        _state.matchSolvedIds = {};
    }

    function _categoryBadge(catId) {
        if (!_data) return '';
        const cat = (_data.categories || []).find(c => c.id === catId);
        if (!cat) return '';
        return `<span class="hce-cat-pill">Témakör ${cat.num} · ${_esc(cat.titleHu)}</span>`;
    }

    function _renderHeader(options) {
        const backBtn = (options && options.onBackLabel)
            ? `<button type="button" class="level-back" data-hce-back="1">← ${_esc(options.onBackLabel)}</button>`
            : '';
        const tabs = [
            { id: 'categories', label: '1. 6 Témakör & Művek (Facts & Artifacts)' },
            { id: 'vocab',      label: '2. Vizsgaszókincs (Vocabulary)' },
            { id: 'mcq',        label: '3. Tesztkérdések (Targeted MCQs)' },
            { id: 'matching',   label: '4. Párosító gyakorlatok (4 Matching Modes)' },
            { id: 'mocks',      label: '5. Mintavizsgák (3 Mock Exams)' }
        ];
        return `
            ${backBtn}
            <header class="hce-header">
                <div class="hce-eyebrow">HUNGARIAN CULTURAL EXAM · MAGYAR KULTURÁLIS ISMERETI VIZSGA</div>
                <h2 class="hce-title">${_esc(_data.title)}</h2>
                <p class="hce-subtitle">
                    Official 6-category preparation layer on top of the Hungarian Citizenship track — covering national symbols, historical turning points, the European &amp; Hungarian literary/musical canon, the Fundamental Law, civic rights/duties, and everyday Hungary.
                </p>
                <nav class="hce-tabs" role="tablist">
                    ${tabs.map(t => `
                        <button type="button"
                                class="hce-tab${_state.tab === t.id ? ' is-active' : ''}"
                                data-hce-tab="${t.id}">
                            ${_esc(t.label)}
                        </button>
                    `).join('')}
                </nav>
            </header>
        `;
    }

    function _renderCategoriesTab() {
        const cats = _data.categories || [];
        const visibleCats = _state.selectedCategory === 'all'
            ? cats
            : cats.filter(c => c.id === _state.selectedCategory);

        return `
            <div class="hce-section">
                <div class="hce-toolbar">
                    <div class="hce-cat-grid">
                        <button type="button"
                                class="hce-cat-card${_state.selectedCategory === 'all' ? ' is-selected' : ''}"
                                data-hce-cat="all">
                            <span class="hce-cat-num">1–6</span>
                            <span class="hce-cat-name">Összes hivatalos témakör (All 6 Categories)</span>
                        </button>
                        ${cats.map(c => `
                            <button type="button"
                                    class="hce-cat-card${_state.selectedCategory === c.id ? ' is-selected' : ''}"
                                    data-hce-cat="${_esc(c.id)}">
                                <span class="hce-cat-num">${c.num}. témakör</span>
                                <span class="hce-cat-name">${_esc(c.titleHu)}</span>
                                <span class="hce-cat-en">${_esc(c.titleEn)}</span>
                            </button>
                        `).join('')}
                    </div>
                    <div class="hce-toggle-row">
                        <button type="button" class="hce-secondary-btn" data-hce-toggle-en="1">
                            ${_state.showEnglishAll ? 'Hide English Explanations' : 'Show English Explanations'}
                        </button>
                    </div>
                </div>

                ${visibleCats.map(c => `
                    <section class="hce-cat-block">
                        <div class="hce-cat-block-head">
                            <div>
                                <span class="hce-cat-eyebrow">${c.num}. HIVATALOS TÉMAKÖR</span>
                                <h3 class="hce-cat-block-title">${_esc(c.titleHu)}</h3>
                                <p class="hce-cat-block-sub">${_esc(c.titleEn)} — ${_esc(c.summary)}</p>
                            </div>
                            <button type="button" class="hce-secondary-btn" data-hce-practice-cat="${_esc(c.id)}">
                                Practice MCQs →
                            </button>
                        </div>

                        <div class="hce-facts-list">
                            ${(c.facts || []).map(f => `
                                <article class="hce-fact-card">
                                    <div class="hce-fact-head">
                                        <h4 class="hce-fact-title">${_esc(f.title)}</h4>
                                        <span class="hce-fact-sub">${_esc(f.subtitle)}</span>
                                    </div>
                                    <p class="hce-fact-hu">${_esc(f.explanationHu)}</p>
                                    ${_state.showEnglishAll ? `
                                        <p class="hce-fact-en"><strong>English explanation:</strong> ${_esc(f.explanationEn)}</p>
                                    ` : ''}
                                    <div class="hce-fact-clue">
                                        <strong>Vizsgakulcs (Required Fact):</strong> ${_esc(f.examClue)}
                                    </div>
                                </article>
                            `).join('')}
                        </div>
                    </section>
                `).join('')}
            </div>
        `;
    }

    function _renderVocabTab() {
        const vocab = _data.vocabulary || [];
        return `
            <div class="hce-section">
                <div class="hce-section-intro">
                    <h3 class="hce-section-title">Vizsgaszókincs (Exam-Specific Hungarian Vocabulary)</h3>
                    <p class="hce-section-desc">Key official terms and sentence patterns used in the written Hungarian Cultural Knowledge &amp; Citizenship exams.</p>
                </div>
                <div class="hce-vocab-grid">
                    ${vocab.map(v => `
                        <div class="hce-vocab-card">
                            <div class="hce-vocab-top">
                                <strong class="hce-vocab-term">${_esc(v.term)}</strong>
                                ${_categoryBadge(v.category)}
                            </div>
                            <div class="hce-vocab-en">${_esc(v.english)}</div>
                            <div class="hce-vocab-ctx">„${_esc(v.examContext)}”</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    function _renderMcqTab() {
        const cats = _data.categories || [];
        const allMcqs = _data.mcqs || [];
        const filtered = _state.mcqCategory === 'all'
            ? allMcqs
            : allMcqs.filter(q => q.category === _state.mcqCategory);

        let answeredCount = 0;
        let correctCount = 0;
        filtered.forEach(q => {
            if (_state.mcqAnswers[q.id] !== undefined) {
                answeredCount++;
                if (_state.mcqAnswers[q.id] === q.correct) correctCount++;
            }
        });

        return `
            <div class="hce-section">
                <div class="hce-mcq-bar">
                    <div class="hce-mcq-filters">
                        <button type="button"
                                class="hce-filter-chip${_state.mcqCategory === 'all' ? ' is-active' : ''}"
                                data-hce-mcq-cat="all">
                            All Categories (${allMcqs.length})
                        </button>
                        ${cats.map(c => `
                            <button type="button"
                                    class="hce-filter-chip${_state.mcqCategory === c.id ? ' is-active' : ''}"
                                    data-hce-mcq-cat="${_esc(c.id)}">
                                ${c.num}. ${_esc(c.titleEn)}
                            </button>
                        `).join('')}
                    </div>
                    <div class="hce-mcq-stats">
                        <span>Score: <strong>${correctCount} / ${answeredCount}</strong> answered</span>
                        <button type="button" class="hce-secondary-btn" data-hce-mcq-reset="1">Reset Answers</button>
                    </div>
                </div>

                <div class="hce-mcq-list">
                    ${filtered.map((q, idx) => {
                        const chosen = _state.mcqAnswers[q.id];
                        const isAnswered = chosen !== undefined;
                        return `
                            <div class="hce-mcq-card${isAnswered ? (chosen === q.correct ? ' is-correct' : ' is-wrong') : ''}">
                                <div class="hce-mcq-meta">
                                    <span class="hce-mcq-num">Question ${idx + 1}</span>
                                    ${_categoryBadge(q.category)}
                                </div>
                                <p class="hce-mcq-q">${_esc(q.question)}</p>
                                <div class="hce-mcq-options">
                                    ${(q.options || []).map((opt, oi) => {
                                        let cls = 'hce-mcq-opt';
                                        if (isAnswered) {
                                            if (oi === q.correct) cls += ' is-right-opt';
                                            else if (oi === chosen) cls += ' is-wrong-opt';
                                        }
                                        return `
                                            <button type="button"
                                                    class="${cls}"
                                                    data-hce-mcq-id="${_esc(q.id)}"
                                                    data-hce-mcq-opt="${oi}"
                                                    ${isAnswered ? 'disabled' : ''}>
                                                ${_esc(opt)}
                                            </button>
                                        `;
                                    }).join('')}
                                </div>
                                ${isAnswered && q.explanation ? `
                                    <div class="hce-mcq-exp">
                                        <strong>Magyarázat:</strong> ${_esc(q.explanation)}
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    function _renderMatchingTab() {
        const modes = [
            { id: 'nameToWork',      label: '5. Name → Work (Alkotó → Mű)' },
            { id: 'personToField',   label: '6. Person → Field (Személy → Szerep)' },
            { id: 'dateToEvent',     label: '7. Date → Event (Évszám → Esemény)' },
            { id: 'symbolToMeaning', label: '8. Symbol → Meaning (Jelkép → Jelentés)' }
        ];
        const currentSet = (_data.matchingSets && _data.matchingSets[_state.matchMode]) || { title: '', subtitle: '' };
        const totalInRound = _state.matchRoundPairs.length;
        const solvedCount = Object.keys(_state.matchSolvedIds).length;

        return `
            <div class="hce-section">
                <div class="hce-match-modes">
                    ${modes.map(m => `
                        <button type="button"
                                class="hce-filter-chip${_state.matchMode === m.id ? ' is-active' : ''}"
                                data-hce-match-mode="${m.id}">
                            ${_esc(m.label)}
                        </button>
                    `).join('')}
                </div>

                <div class="hce-match-head">
                    <div>
                        <h3 class="hce-section-title">${_esc(currentSet.title)}</h3>
                        <p class="hce-section-desc">${_esc(currentSet.subtitle)}</p>
                    </div>
                    <div class="hce-match-controls">
                        <span class="hce-match-progress">Matched: <strong>${solvedCount} / ${totalInRound}</strong></span>
                        <button type="button" class="hce-secondary-btn" data-hce-match-shuffle="1">New Shuffled Round ↻</button>
                    </div>
                </div>

                ${solvedCount === totalInRound && totalInRound > 0 ? `
                    <div class="hce-match-banner">
                        All 6 pairs matched! Click <strong>New Shuffled Round ↻</strong> to practice another batch from this pool.
                    </div>
                ` : ''}

                <div class="hce-match-board">
                    <div class="hce-match-col">
                        <div class="hce-match-col-title">Select item (Bal oszlop)</div>
                        ${_state.matchLeftOrder.map(item => {
                            const solved = !!_state.matchSolvedIds[item.id];
                            const selected = _state.matchSelectedLeft === item.id;
                            return `
                                <button type="button"
                                        class="hce-match-tile${solved ? ' is-solved' : ''}${selected ? ' is-selected' : ''}"
                                        data-hce-left="${item.id}"
                                        ${solved ? 'disabled' : ''}>
                                    ${_esc(item.left)}
                                </button>
                            `;
                        }).join('')}
                    </div>
                    <div class="hce-match-col">
                        <div class="hce-match-col-title">Match with pair (Jobb oszlop)</div>
                        ${_state.matchRightOrder.map(item => {
                            const solved = !!_state.matchSolvedIds[item.id];
                            return `
                                <button type="button"
                                        class="hce-match-tile${solved ? ' is-solved' : ''}"
                                        data-hce-right="${item.id}"
                                        ${solved ? 'disabled' : ''}>
                                    ${_esc(item.right)}
                                </button>
                            `;
                        }).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    function _renderMocksTab() {
        const mocks = _data.mockExams || [];
        const saved = (_loadSavedProgress().mocks) || {};
        const exam = mocks.find(m => m.id === _state.activeMockId) || mocks[0];
        if (!exam) return '';

        const questions = exam.questions || [];
        let earnedPoints = 0;
        const maxPoints = _data.maxPoints || 30;
        const passMark = _data.passThresholdPoints || 16;

        if (_state.mockSubmitted) {
            questions.forEach((q, idx) => {
                if (_state.mockAnswers[idx] === q.correct) {
                    earnedPoints += (q.points || 2);
                }
            });
        }

        const passed = earnedPoints >= passMark;

        return `
            <div class="hce-section">
                <div class="hce-mock-picker">
                    ${mocks.map(m => {
                        const prev = saved[m.id];
                        return `
                            <button type="button"
                                    class="hce-mock-card${exam.id === m.id ? ' is-active' : ''}"
                                    data-hce-mock-id="${_esc(m.id)}">
                                <div class="hce-mock-card-title">${_esc(m.title)}</div>
                                <div class="hce-mock-card-desc">${_esc(m.description)}</div>
                                ${prev ? `
                                    <div class="hce-mock-badge ${prev.passed ? 'is-pass' : 'is-fail'}">
                                        Best: ${prev.points} / ${prev.maxPoints} pts (${prev.passed ? 'PASSED' : 'RETRY'})
                                    </div>
                                ` : `<div class="hce-mock-badge">Not taken yet · 30 pts</div>`}
                            </button>
                        `;
                    }).join('')}
                </div>

                ${_state.mockSubmitted ? `
                    <div class="hce-mock-result ${passed ? 'is-pass' : 'is-fail'}">
                        <h4 class="hce-mock-result-title">
                            ${passed ? 'Sikeres vizsga! (Exam Passed)' : 'Ismétlés javasolt (Below 16-point threshold)'}
                            — ${earnedPoints} / ${maxPoints} pont
                        </h4>
                        <p>Official requirement: minimum <strong>${passMark} / ${maxPoints} points</strong> across the 6 categories.</p>
                        <button type="button" class="hce-secondary-btn" data-hce-mock-retry="1">Retake This Mock Exam</button>
                    </div>
                ` : ''}

                <div class="hce-mcq-list">
                    ${questions.map((q, idx) => {
                        const chosen = _state.mockAnswers[idx];
                        return `
                            <div class="hce-mcq-card${_state.mockSubmitted ? (chosen === q.correct ? ' is-correct' : ' is-wrong') : ''}">
                                <div class="hce-mcq-meta">
                                    ${_categoryBadge(q.category)}
                                    <span class="hce-points-badge">${q.points || 2} pont</span>
                                </div>
                                <p class="hce-mcq-q">${_esc(q.question)}</p>
                                <div class="hce-mcq-options">
                                    ${(q.options || []).map((opt, oi) => {
                                        let cls = 'hce-mcq-opt';
                                        if (!_state.mockSubmitted && chosen === oi) cls += ' is-selected-opt';
                                        if (_state.mockSubmitted) {
                                            if (oi === q.correct) cls += ' is-right-opt';
                                            else if (oi === chosen) cls += ' is-wrong-opt';
                                        }
                                        return `
                                            <button type="button"
                                                    class="${cls}"
                                                    data-hce-mock-q="${idx}"
                                                    data-hce-mock-opt="${oi}"
                                                    ${_state.mockSubmitted ? 'disabled' : ''}>
                                                ${_esc(opt)}
                                            </button>
                                        `;
                                    }).join('')}
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>

                ${!_state.mockSubmitted ? `
                    <div class="hce-mock-submit-bar">
                        <button type="button" class="hce-primary-btn" data-hce-mock-submit="1">
                            Submit Mock Exam &amp; Calculate Score (30 pts)
                        </button>
                    </div>
                ` : ''}
            </div>
        `;
    }

    function _renderBody() {
        switch (_state.tab) {
            case 'vocab': return _renderVocabTab();
            case 'mcq': return _renderMcqTab();
            case 'matching': return _renderMatchingTab();
            case 'mocks': return _renderMocksTab();
            case 'categories':
            default:
                return _renderCategoriesTab();
        }
    }

    function _wireEvents(container, options) {
        if (container.dataset.hceWired) return;
        container.dataset.hceWired = '1';

        container.addEventListener('click', e => {
            if (e.target.closest('[data-hce-back]')) {
                if (options && typeof options.onBack === 'function') {
                    options.onBack();
                }
                return;
            }

            const tabBtn = e.target.closest('[data-hce-tab]');
            if (tabBtn) {
                _state.tab = tabBtn.getAttribute('data-hce-tab');
                _paint(container, options);
                return;
            }

            const catBtn = e.target.closest('[data-hce-cat]');
            if (catBtn) {
                _state.selectedCategory = catBtn.getAttribute('data-hce-cat');
                _paint(container, options);
                return;
            }

            if (e.target.closest('[data-hce-toggle-en]')) {
                _state.showEnglishAll = !_state.showEnglishAll;
                _paint(container, options);
                return;
            }

            const practiceCatBtn = e.target.closest('[data-hce-practice-cat]');
            if (practiceCatBtn) {
                _state.mcqCategory = practiceCatBtn.getAttribute('data-hce-practice-cat');
                _state.tab = 'mcq';
                _paint(container, options);
                return;
            }

            const mcqCatBtn = e.target.closest('[data-hce-mcq-cat]');
            if (mcqCatBtn) {
                _state.mcqCategory = mcqCatBtn.getAttribute('data-hce-mcq-cat');
                _paint(container, options);
                return;
            }

            if (e.target.closest('[data-hce-mcq-reset]')) {
                _state.mcqAnswers = {};
                _paint(container, options);
                return;
            }

            const mcqOptBtn = e.target.closest('[data-hce-mcq-opt]');
            if (mcqOptBtn) {
                const qId = mcqOptBtn.getAttribute('data-hce-mcq-id');
                const optIdx = Number(mcqOptBtn.getAttribute('data-hce-mcq-opt'));
                _state.mcqAnswers[qId] = optIdx;
                _paint(container, options);
                return;
            }

            const matchModeBtn = e.target.closest('[data-hce-match-mode]');
            if (matchModeBtn) {
                _state.matchMode = matchModeBtn.getAttribute('data-hce-match-mode');
                _initMatchRound();
                _paint(container, options);
                return;
            }

            if (e.target.closest('[data-hce-match-shuffle]')) {
                _initMatchRound();
                _paint(container, options);
                return;
            }

            const leftTile = e.target.closest('[data-hce-left]');
            if (leftTile) {
                const id = leftTile.getAttribute('data-hce-left');
                _state.matchSelectedLeft = (_state.matchSelectedLeft === id) ? null : id;
                _paint(container, options);
                return;
            }

            const rightTile = e.target.closest('[data-hce-right]');
            if (rightTile && _state.matchSelectedLeft) {
                const rightId = rightTile.getAttribute('data-hce-right');
                if (rightId === _state.matchSelectedLeft) {
                    _state.matchSolvedIds[rightId] = true;
                    _state.matchSelectedLeft = null;
                } else {
                    _state.matchSelectedLeft = null;
                }
                _paint(container, options);
                return;
            }

            const mockPickBtn = e.target.closest('[data-hce-mock-id]');
            if (mockPickBtn) {
                _state.activeMockId = mockPickBtn.getAttribute('data-hce-mock-id');
                _state.mockAnswers = {};
                _state.mockSubmitted = false;
                _paint(container, options);
                return;
            }

            const mockOptBtn = e.target.closest('[data-hce-mock-opt]');
            if (mockOptBtn && !_state.mockSubmitted) {
                const qIdx = Number(mockOptBtn.getAttribute('data-hce-mock-q'));
                const optIdx = Number(mockOptBtn.getAttribute('data-hce-mock-opt'));
                _state.mockAnswers[qIdx] = optIdx;
                _paint(container, options);
                return;
            }

            if (e.target.closest('[data-hce-mock-submit]')) {
                _state.mockSubmitted = true;
                const exam = (_data.mockExams || []).find(m => m.id === _state.activeMockId) || (_data.mockExams || [])[0];
                if (exam) {
                    let pts = 0;
                    (exam.questions || []).forEach((q, idx) => {
                        if (_state.mockAnswers[idx] === q.correct) pts += (q.points || 2);
                    });
                    _saveMockScore(exam.id, pts, _data.maxPoints || 30, pts >= (_data.passThresholdPoints || 16));
                }
                _paint(container, options);
                return;
            }

            if (e.target.closest('[data-hce-mock-retry]')) {
                _state.mockAnswers = {};
                _state.mockSubmitted = false;
                _paint(container, options);
            }
        });
    }

    function _paint(container, options) {
        if (!_data) return;
        container.innerHTML = `
            <div class="hce-root">
                ${_renderHeader(options)}
                ${_renderBody()}
            </div>
        `;
    }

    async function render(container, options) {
        if (!container) return;
        container.innerHTML = '<p class="text-muted level-empty">Loading Hungarian Cultural Exam…</p>';
        try {
            await _loadData();
            _wireEvents(container, options);
            _paint(container, options);
        } catch (err) {
            console.error('HuCulturalExam render failed:', err);
            container.innerHTML = '<p class="text-muted level-empty">Could not load the Hungarian Cultural Exam module.</p>';
        }
    }

    return {
        render
    };
})();
