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
        // Navigation: the exam opens on a hub of five sections. A section opens
        // its own screen, and most of those open one item at a time.
        tab: null,                // null (hub) | 'categories' | 'vocab' | 'mcq' | 'matching' | 'mocks'
        selectedCategory: null,   // null (list of categories) or category.id
        showEnglishAll: true,
        mcqOpen: false,           // false: list of question sets; true: the questions
        mcqCategory: 'all',
        mcqAnswers: {},           // { [mcqId]: selectedOptionIdx }
        matchOpen: false,         // false: list of modes; true: the board
        matchMode: 'nameToWork',  // 'nameToWork' | 'personToField' | 'dateToEvent' | 'symbolToMeaning'
        matchRoundPairs: [],      // array of { id, left, right }
        matchLeftOrder: [],
        matchRightOrder: [],
        matchSelectedLeft: null,
        matchSolvedIds: {},
        matchWrongFlash: false,
        mockOpen: false,          // false: list of mock exams; true: the exam
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

    function _shuffleQuestionOptions(q) {
        if (!q || !Array.isArray(q.options) || q.options.length < 2) return;
        const tagged = q.options.map((text, idx) => ({
            text,
            isCorrect: idx === q.correct
        }));
        const shuffled = _shuffle(tagged);
        q.options = shuffled.map(item => item.text);
        q.correct = shuffled.findIndex(item => item.isCorrect);
    }

    function _shuffleAllMcqs() {
        if (!_data) return;
        (_data.mcqs || []).forEach(_shuffleQuestionOptions);
    }

    function _shuffleMockExam(mockId) {
        if (!_data || !_data.mockExams) return;
        const exam = _data.mockExams.find(m => m.id === mockId);
        if (exam && Array.isArray(exam.questions)) {
            exam.questions.forEach(_shuffleQuestionOptions);
        }
    }

    async function _loadData() {
        if (_data) return _data;
        const path = (typeof Lang !== 'undefined' && Lang.content)
            ? Lang.content('cultural-exam.json')
            : 'content/hu/cultural-exam.json';
        const res = await fetch(path);
        if (!res.ok) throw new Error('Failed to load cultural-exam.json');
        _data = await res.json();
        _shuffleAllMcqs();
        (_data.mockExams || []).forEach(m => _shuffleMockExam(m.id));
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

    const SECTIONS = [
        { id: 'categories', hu: 'Témakörök és művek',    en: 'Facts and artifacts' },
        { id: 'vocab',      hu: 'Vizsgaszókincs',        en: 'Exam vocabulary' },
        { id: 'mcq',        hu: 'Tesztkérdések',         en: 'Targeted questions' },
        { id: 'matching',   hu: 'Párosító gyakorlatok',  en: 'Matching practice' },
        { id: 'mocks',      hu: 'Mintavizsgák',          en: 'Mock exams' }
    ];

    const MATCH_MODES = [
        { id: 'nameToWork',      hu: 'Alkotó → Mű',        en: 'Name to work' },
        { id: 'personToField',   hu: 'Személy → Szerep',   en: 'Person to field' },
        { id: 'dateToEvent',     hu: 'Évszám → Esemény',   en: 'Date to event' },
        { id: 'symbolToMeaning', hu: 'Jelkép → Jelentés',  en: 'Symbol to meaning' }
    ];

    function _section(id) { return SECTIONS.find(x => x.id === id) || null; }
    function _category(id) { return (_data.categories || []).find(c => c.id === id) || null; }

    // Is an item (one category, one question set, one mode, one exam) open
    // inside the current section?
    function _itemOpen() {
        switch (_state.tab) {
            case 'categories': return !!_state.selectedCategory;
            case 'mcq': return _state.mcqOpen;
            case 'matching': return _state.matchOpen;
            case 'mocks': return _state.mockOpen;
            default: return false;
        }
    }

    function _backBtn(kind, label) {
        return `<button type="button" class="level-back" data-hce-back="${kind}">← ${_esc(label)}</button>`;
    }

    // One row: name in serif, a muted gloss beneath, an optional figure and a
    // drawn chevron. The same row is used at every level of the exam.
    function _row(attrs, name, gloss, value) {
        const line = [gloss, value].filter(Boolean).join(' · ');
        return `
            <button type="button" class="hce-row" ${attrs}>
                <span class="hce-row-text">
                    <span class="hce-row-name">${_esc(name)}</span>
                    ${line ? `<span class="hce-row-en">${_esc(line)}</span>` : ''}
                </span>
                <span class="hce-row-chev" aria-hidden="true"></span>
            </button>
        `;
    }

    function _rows(html) { return `<div class="hce-rows">${html}</div>`; }

    function _renderHeader(options) {
        const sec = _section(_state.tab);
        const exitLabel = options && options.onBackLabel;

        // The hub.
        if (!sec) {
            return `
                ${exitLabel ? _backBtn('exit', exitLabel) : ''}
                <header class="hce-header">
                    <div class="hce-eyebrow">Magyar kulturális ismereti vizsga</div>
                    <h2 class="hce-title">${_esc(_data.title)}</h2>
                    <p class="hce-subtitle">Preparation for the Hungarian citizenship culture exam: six official categories, from national symbols to everyday Hungary.</p>
                </header>
            `;
        }

        // A section's own list.
        if (!_itemOpen()) {
            return `
                ${_backBtn('hub', 'Cultural exam')}
                <header class="hce-header">
                    <h2 class="hce-title">${_esc(sec.hu)}</h2>
                    <p class="hce-subtitle">${_esc(sec.en)}</p>
                </header>
            `;
        }

        // One item inside a section.
        let title = sec.hu, sub = sec.en;
        if (_state.tab === 'categories') {
            const c = _category(_state.selectedCategory);
            if (c) { title = `${c.num}. ${c.titleHu}`; sub = c.titleEn; }
        } else if (_state.tab === 'mcq') {
            const c = _category(_state.mcqCategory);
            title = c ? `${c.num}. ${c.titleHu}` : 'Összes témakör';
            sub = c ? c.titleEn : 'All categories';
        } else if (_state.tab === 'matching') {
            const set = (_data.matchingSets && _data.matchingSets[_state.matchMode]) || {};
            title = set.title || sec.hu;
            sub = set.subtitle || sec.en;
        } else if (_state.tab === 'mocks') {
            const exam = (_data.mockExams || []).find(m => m.id === _state.activeMockId) || (_data.mockExams || [])[0];
            if (exam) { title = exam.title; sub = exam.description; }
        }
        return `
            ${_backBtn('section', sec.hu)}
            <header class="hce-header">
                <h2 class="hce-title">${_esc(title)}</h2>
                ${sub ? `<p class="hce-subtitle">${_esc(sub)}</p>` : ''}
            </header>
        `;
    }

    function _renderHub() {
        const cats = _data.categories || [];
        const factCount = cats.reduce((n, c) => n + (c.facts || []).length, 0);
        const mocks = _data.mockExams || [];
        const saved = (_loadSavedProgress().mocks) || {};
        const passed = mocks.filter(m => saved[m.id] && saved[m.id].passed).length;
        const values = {
            categories: `${cats.length} témakör · ${factCount} facts`,
            vocab: `${(_data.vocabulary || []).length} terms`,
            mcq: `${(_data.mcqs || []).length} questions`,
            matching: `${MATCH_MODES.length} modes`,
            mocks: mocks.length ? `${passed} of ${mocks.length} passed` : ''
        };
        return `<div class="hce-section">${_rows(SECTIONS.map(x =>
            _row(`data-hce-tab="${x.id}"`, x.hu, x.en, values[x.id])).join(''))}</div>`;
    }

    function _renderCategoriesTab() {
        const cats = _data.categories || [];

        // The six categories, one row each.
        if (!_state.selectedCategory) {
            return `<div class="hce-section">${_rows(cats.map(c =>
                _row(`data-hce-cat="${_esc(c.id)}"`, `${c.num}. ${c.titleHu}`, c.titleEn,
                     `${(c.facts || []).length} facts`)).join(''))}</div>`;
        }

        // One category: its facts, and a way to practise it.
        const c = _category(_state.selectedCategory) || cats[0];
        if (!c) return '';
        return `
            <div class="hce-section">
                <p class="hce-cat-block-sub">${_esc(c.summary)}</p>
                <div class="hce-toolbar hce-actions">
                    <button type="button" class="hce-secondary-btn" data-hce-practice-cat="${_esc(c.id)}">Practise these questions →</button>
                    <button type="button" class="hce-link-btn" data-hce-toggle-en="1">
                        ${_state.showEnglishAll ? 'Hide English' : 'Show English'}
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
                                <p class="hce-fact-en">${_esc(f.explanationEn)}</p>
                            ` : ''}
                            <div class="hce-fact-clue">
                                <strong>Vizsgakulcs:</strong> ${_esc(f.examClue)}
                            </div>
                        </article>
                    `).join('')}
                </div>
            </div>
        `;
    }

    function _renderVocabTab() {
        const vocab = _data.vocabulary || [];
        return `
            <div class="hce-section">
                <p class="hce-section-desc">Key official terms and sentence patterns used in the written exam.</p>
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

    function _mcqProgress(list) {
        let answered = 0, correct = 0;
        list.forEach(q => {
            if (_state.mcqAnswers[q.id] !== undefined) {
                answered++;
                if (_state.mcqAnswers[q.id] === q.correct) correct++;
            }
        });
        return { answered, correct };
    }

    function _renderMcqTab() {
        const cats = _data.categories || [];
        const allMcqs = _data.mcqs || [];

        // Pick a set of questions: all of them, or one category's.
        if (!_state.mcqOpen) {
            const value = list => {
                const p = _mcqProgress(list);
                return p.answered ? `${p.correct} / ${p.answered} right` : `${list.length} questions`;
            };
            return `<div class="hce-section">${_rows(
                _row('data-hce-mcq-cat="all"', 'Összes témakör', 'All categories', value(allMcqs)) +
                cats.map(c => _row(`data-hce-mcq-cat="${_esc(c.id)}"`, `${c.num}. ${c.titleHu}`, c.titleEn,
                    value(allMcqs.filter(q => q.category === c.id)))).join('')
            )}</div>`;
        }

        const filtered = _state.mcqCategory === 'all'
            ? allMcqs
            : allMcqs.filter(q => q.category === _state.mcqCategory);
        const prog = _mcqProgress(filtered);

        return `
            <div class="hce-section">
                <div class="hce-mcq-stats">
                    <span>${prog.answered ? `${prog.correct} / ${prog.answered} right · ` : ''}${filtered.length} questions</span>
                    <button type="button" class="hce-link-btn" data-hce-mcq-reset="1">Reset answers</button>
                </div>

                <div class="hce-mcq-list">
                    ${filtered.map((q, idx) => {
                        const chosen = _state.mcqAnswers[q.id];
                        const isAnswered = chosen !== undefined;
                        return `
                            <div class="hce-mcq-card${isAnswered ? (chosen === q.correct ? ' is-correct' : ' is-wrong') : ''}">
                                <div class="hce-mcq-meta">
                                    <span class="hce-mcq-num">Question ${idx + 1}</span>
                                    ${_state.mcqCategory === 'all' ? _categoryBadge(q.category) : ''}
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
        // Pick a mode.
        if (!_state.matchOpen) {
            return `<div class="hce-section">${_rows(MATCH_MODES.map(m => {
                const set = (_data.matchingSets && _data.matchingSets[m.id]) || {};
                return _row(`data-hce-match-mode="${m.id}"`, m.hu, set.title || m.en, '');
            }).join(''))}</div>`;
        }

        const totalInRound = _state.matchRoundPairs.length;
        const solvedCount = Object.keys(_state.matchSolvedIds).length;

        return `
            <div class="hce-section">
                <div class="hce-match-head">
                    <span class="hce-match-progress">${solvedCount} / ${totalInRound} matched</span>
                    <button type="button" class="hce-link-btn" data-hce-match-shuffle="1">New round ↻</button>
                </div>

                ${solvedCount === totalInRound && totalInRound > 0 ? `
                    <div class="hce-match-banner">
                        All ${totalInRound} pairs matched. Start a new round to practise another batch.
                    </div>
                ` : ''}

                <div class="hce-match-board">
                    <div class="hce-match-col">
                        <div class="hce-match-col-title">Select an item</div>
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
                        <div class="hce-match-col-title">Then its pair</div>
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
        const maxPoints = _data.maxPoints || 30;
        const passMark = _data.passThresholdPoints || 16;

        // Pick a mock exam.
        if (!_state.mockOpen) {
            return `<div class="hce-section">
                <p class="hce-section-desc">Each mock has 30 points; the pass mark is ${passMark}.</p>
                ${_rows(mocks.map(m => {
                    const prev = saved[m.id];
                    return _row(`data-hce-mock-id="${_esc(m.id)}"`, m.title,
                        `${(m.questions || []).length} questions · ${maxPoints} points`,
                        prev ? `Best ${prev.points}${prev.passed ? ', passed' : ''}` : 'Not taken');
                }).join(''))}
            </div>`;
        }

        const exam = mocks.find(m => m.id === _state.activeMockId) || mocks[0];
        if (!exam) return '';
        const questions = exam.questions || [];
        let earnedPoints = 0;
        if (_state.mockSubmitted) {
            questions.forEach((q, idx) => {
                if (_state.mockAnswers[idx] === q.correct) earnedPoints += (q.points || 2);
            });
        }
        const passed = earnedPoints >= passMark;

        return `
            <div class="hce-section">
                ${_state.mockSubmitted ? `
                    <div class="hce-mock-result ${passed ? 'is-pass' : 'is-fail'}">
                        <h4 class="hce-mock-result-title">
                            ${passed ? 'Sikeres vizsga' : 'Ismétlés javasolt'}
                            — ${earnedPoints} / ${maxPoints} pont
                        </h4>
                        <p>${passed ? 'You passed.' : `Below the ${passMark}-point pass mark.`} The official requirement is at least ${passMark} of ${maxPoints} points across the six categories.</p>
                        <button type="button" class="hce-secondary-btn" data-hce-mock-retry="1">Retake this mock exam</button>
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
                            Submit and see my score
                        </button>
                    </div>
                ` : ''}
            </div>
        `;
    }

    function _renderBody() {
        switch (_state.tab) {
            case 'categories': return _renderCategoriesTab();
            case 'vocab': return _renderVocabTab();
            case 'mcq': return _renderMcqTab();
            case 'matching': return _renderMatchingTab();
            case 'mocks': return _renderMocksTab();
            default: return _renderHub();
        }
    }

    // Closes whatever item is open in the current section, back to its list.
    function _closeItem() {
        _state.selectedCategory = null;
        _state.mcqOpen = false;
        _state.matchOpen = false;
        _state.mockOpen = false;
    }

    // Repaint after moving between screens, and start at the top.
    function _go(container, options) {
        _paint(container, options);
        if (typeof window !== 'undefined' && window.scrollTo) window.scrollTo(0, 0);
    }

    function _wireEvents(container, options) {
        if (container.dataset.hceWired) return;
        container.dataset.hceWired = '1';

        container.addEventListener('click', e => {
            const backBtn = e.target.closest('[data-hce-back]');
            if (backBtn) {
                const kind = backBtn.getAttribute('data-hce-back');
                if (kind === 'exit') {
                    if (options && typeof options.onBack === 'function') options.onBack();
                    return;
                }
                if (kind === 'hub') {
                    _state.tab = null;
                } else {
                    _closeItem();
                }
                _go(container, options);
                return;
            }

            const tabBtn = e.target.closest('[data-hce-tab]');
            if (tabBtn) {
                _state.tab = tabBtn.getAttribute('data-hce-tab');
                _closeItem();
                _go(container, options);
                return;
            }

            const catBtn = e.target.closest('[data-hce-cat]');
            if (catBtn) {
                _state.selectedCategory = catBtn.getAttribute('data-hce-cat');
                _go(container, options);
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
                _state.mcqOpen = true;
                _state.tab = 'mcq';
                _go(container, options);
                return;
            }

            const mcqCatBtn = e.target.closest('[data-hce-mcq-cat]');
            if (mcqCatBtn) {
                _state.mcqCategory = mcqCatBtn.getAttribute('data-hce-mcq-cat');
                _state.mcqOpen = true;
                _go(container, options);
                return;
            }

            if (e.target.closest('[data-hce-mcq-reset]')) {
                _state.mcqAnswers = {};
                _shuffleAllMcqs();
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
                _state.matchOpen = true;
                _initMatchRound();
                _go(container, options);
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
                _state.mockOpen = true;
                _shuffleMockExam(_state.activeMockId);
                _go(container, options);
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
                _shuffleMockExam(_state.activeMockId);
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
            _state.tab = null;
            _closeItem();
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
