// ============================================
// SPANISH CCSE EXAM (Prueba de Conocimientos Constitucionales y Socioculturales de España)
// ============================================
// Official citizenship exam preparation module for Spanish nationality by residency (Instituto Cervantes).
// Covers:
//   1. 5 official thematic syllabus categories (Constitución, derechos, geografía, cultura, sociedad)
//   2. Essential civic and administrative vocabulary
//   3. Targeted practice by official task (Tareas 1 to 5)
//   4. 4 interactive matching modes (Institución, Región, Creador, Fecha)
//   5. Authentic 25-question Mock Exams (pass mark: 15/25 aciertos) + Dynamic Random Exam Generator

const CcseExam = (function () {
    'use strict';

    const STORAGE_KEY = 'parlour_es_ccse_exam_v1';
    let _data = null;
    let _state = {
        tab: null,                // null (hub) | 'categories' | 'vocab' | 'mcq' | 'matching' | 'mocks'
        selectedCategory: null,   // null or category.id
        showEnglishAll: true,
        mcqOpen: false,
        mcqTarea: 'all',          // 'all' | 'tarea1' | 'tarea2' | 'tarea3' | 'tarea4' | 'tarea5'
        mcqAnswers: {},           // { [mcqId]: selectedOptionIdx }
        matchOpen: false,
        matchMode: 'institutionToRole', // 'institutionToRole' | 'regionToCapital' | 'creatorToWork' | 'dateToEvent'
        matchRoundPairs: [],
        matchLeftOrder: [],
        matchRightOrder: [],
        matchSelectedLeft: null,
        matchSolvedIds: {},
        mockOpen: false,
        activeMockId: 'mock-1',
        mockQuestions: [],
        mockAnswers: {},          // { [qIndex]: optionIdx }
        mockSubmitted: false,
        timerEnabled: false,      // untimed by default per learner setting
        timerRemaining: 45 * 60,  // 45 minutes = 2700 seconds
        timerInterval: null
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
        // Keep true/false in natural order (Verdadero, Falso)
        if (q.options.length === 2 && q.options[0] === 'Verdadero' && q.options[1] === 'Falso') {
            return;
        }
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

    function _initMatchRound() {
        if (!_data || !_data.matchingSets) return;
        const set = _data.matchingSets[_state.matchMode] || _data.matchingSets.institutionToRole;
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

    // Official Tarea Labels according to Instituto Cervantes specifications
    const TAREA_META = {
        tarea1: { num: 1, name: 'Tarea 1', title: 'Gobierno, poderes e instituciones', count: 10, format: 'Selección múltiple (3 opciones)' },
        tarea2: { num: 2, name: 'Tarea 2', title: 'Derechos y deberes fundamentales', count: 3, format: 'Verdadero / Falso (2 opciones)' },
        tarea3: { num: 3, name: 'Tarea 3', title: 'Organización territorial y geografía', count: 2, format: 'Selección múltiple (3 opciones)' },
        tarea4: { num: 4, name: 'Tarea 4', title: 'Cultura, arte e historia relevante', count: 3, format: 'Selección múltiple (3 opciones)' },
        tarea5: { num: 5, name: 'Tarea 5', title: 'Sociedad, trámites y vida cotidiana', count: 7, format: 'Selección múltiple (3 opciones)' }
    };

    const SECTIONS = [
        { id: 'categories', es: 'Temario y contenidos clave',    en: 'Official syllabus and core facts' },
        { id: 'vocab',      es: 'Vocabulario cívico y legal',    en: 'Essential exam & administrative terms' },
        { id: 'mcq',        es: 'Práctica por tareas oficiales', en: 'Targeted drills by official task' },
        { id: 'matching',   es: 'Ejercicios de emparejamiento',  en: 'High-speed matching practice' },
        { id: 'mocks',      es: 'Simulacros de examen (25 Q)',   en: 'Official mock exams & random generator' }
    ];

    const MATCH_MODES = [
        { id: 'institutionToRole', es: 'Institución → Función',      en: 'Institution to constitutional role' },
        { id: 'regionToCapital',    es: 'Comunidad → Capital',        en: 'Autonomous Community to capital' },
        { id: 'creatorToWork',      es: 'Creador → Obra célebre',     en: 'Author/Artist to masterpiece' },
        { id: 'dateToEvent',        es: 'Fecha → Acontecimiento',     en: 'Historical date to milestone' }
    ];

    function _section(id) { return SECTIONS.find(x => x.id === id) || null; }
    function _category(id) { return (_data.categories || []).find(c => c.id === id) || null; }

    function _tareaBadge(tareaId) {
        const t = TAREA_META[tareaId];
        if (!t) return '';
        return `<span class="hce-cat-pill">${_esc(t.name)} · ${_esc(t.title)}</span>`;
    }

    function _categoryBadge(catId) {
        if (!_data) return '';
        const cat = (_data.categories || []).find(c => c.id === catId);
        if (!cat) return '';
        return `<span class="hce-cat-pill">Tema ${cat.num} · ${_esc(cat.titleEs)}</span>`;
    }

    function _generateRandomMock() {
        if (!_data || !_data.mcqs) return [];
        const pool = _data.mcqs;
        const byTarea = {
            tarea1: _shuffle(pool.filter(q => q.tarea === 'tarea1')),
            tarea2: _shuffle(pool.filter(q => q.tarea === 'tarea2')),
            tarea3: _shuffle(pool.filter(q => q.tarea === 'tarea3')),
            tarea4: _shuffle(pool.filter(q => q.tarea === 'tarea4')),
            tarea5: _shuffle(pool.filter(q => q.tarea === 'tarea5'))
        };

        const picked = [
            ...byTarea.tarea1.slice(0, 10),
            ...byTarea.tarea2.slice(0, 3),
            ...byTarea.tarea3.slice(0, 2),
            ...byTarea.tarea4.slice(0, 3),
            ...byTarea.tarea5.slice(0, 7)
        ].map(q => {
            const cloned = JSON.parse(JSON.stringify(q));
            _shuffleQuestionOptions(cloned);
            cloned.points = 1;
            return cloned;
        });

        return picked;
    }

    function _loadMockQuestions(mockId) {
        if (mockId === 'random') {
            return _generateRandomMock();
        }
        const exam = (_data.mockExams || []).find(m => m.id === mockId);
        if (!exam) return [];
        return (exam.questions || []).map(q => {
            const cloned = JSON.parse(JSON.stringify(q));
            _shuffleQuestionOptions(cloned);
            cloned.points = 1;
            return cloned;
        });
    }

    async function _loadData() {
        if (_data) return _data;
        const path = 'content/es-es/ccse-exam.json';
        const res = await fetch(path);
        if (!res.ok) throw new Error('Failed to load ccse-exam.json');
        _data = await res.json();
        _shuffleAllMcqs();
        _initMatchRound();
        return _data;
    }

    // --------------------------------------------
    // Timer Management
    // --------------------------------------------
    function _stopTimer() {
        if (_state.timerInterval) {
            clearInterval(_state.timerInterval);
            _state.timerInterval = null;
        }
    }

    function _startTimer(container, options) {
        _stopTimer();
        _state.timerRemaining = 45 * 60; // 45 minutes
        _state.timerInterval = setInterval(() => {
            _state.timerRemaining--;
            if (_state.timerRemaining <= 0) {
                _stopTimer();
                _state.mockSubmitted = true;
                _recordMockResults();
                _paint(container, options);
            } else {
                _updateTimerDisplay(container);
            }
        }, 1000);
    }

    function _formatTime(sec) {
        const m = Math.floor(sec / 60);
        const s = sec % 60;
        return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    function _updateTimerDisplay(container) {
        const badge = container.querySelector('#ccse-timer-display');
        if (badge) {
            badge.textContent = _formatTime(_state.timerRemaining);
            if (_state.timerRemaining < 300) {
                badge.classList.add('is-warning');
            } else {
                badge.classList.remove('is-warning');
            }
        }
    }

    function _recordMockResults() {
        const questions = _state.mockQuestions || [];
        let earned = 0;
        questions.forEach((q, idx) => {
            if (_state.mockAnswers[idx] === q.correct) earned += 1;
        });
        const passed = earned >= (_data.passThresholdPoints || 15);
        _saveMockScore(_state.activeMockId, earned, _data.maxPoints || 25, passed);
    }

    // --------------------------------------------
    // UI Helpers
    // --------------------------------------------
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
        return `<button type="button" class="level-back" data-ccse-back="${kind}">← ${_esc(label)}</button>`;
    }

    function _row(attrs, name, gloss, value) {
        return `
            <button type="button" class="hce-row" ${attrs}>
                <span class="hce-row-text">
                    <span class="hce-row-name">${_esc(name)}</span>
                    ${(gloss || value) ? `<span class="hce-row-en">${_esc(gloss || '')}${value ? `<span class="hce-row-inline">${gloss ? ' · ' : ''}${_esc(value)}</span>` : ''}</span>` : ''}
                </span>
                ${value ? `<span class="hce-row-value">${_esc(value)}</span>` : ''}
                <span class="hce-row-chev" aria-hidden="true"></span>
            </button>
        `;
    }

    function _rows(html) { return `<div class="hce-rows">${html}</div>`; }

    function _renderHeader(options) {
        const sec = _section(_state.tab);
        const exitLabel = options && options.onBackLabel;

        if (!sec) {
            return `
                ${exitLabel ? _backBtn('exit', exitLabel) : ''}
                <header class="hce-header">
                    <div class="hce-eyebrow">Prueba oficial de nacionalidad · Instituto Cervantes</div>
                    <h2 class="hce-title">${_esc(_data.title)}</h2>
                    <p class="hce-subtitle">Preparación integral para la prueba de Conocimientos Constitucionales y Socioculturales de España: temario oficial, vocabulario cívico, ejercicios y simulacros de 25 preguntas.</p>
                </header>
            `;
        }

        if (!_itemOpen()) {
            return `
                ${_backBtn('hub', 'Examen CCSE')}
                <header class="hce-header">
                    <h2 class="hce-title">${_esc(sec.es)}</h2>
                    <p class="hce-subtitle">${_esc(sec.en)}</p>
                </header>
            `;
        }

        let title = sec.es, sub = sec.en;
        if (_state.tab === 'categories') {
            const c = _category(_state.selectedCategory);
            if (c) { title = `Tema ${c.num} · ${c.titleEs}`; sub = c.titleEn; }
        } else if (_state.tab === 'mcq') {
            const t = TAREA_META[_state.mcqTarea];
            title = t ? `${t.name}: ${t.title}` : 'Todas las preguntas oficiales';
            sub = t ? `${t.count} preguntas en el examen oficial · ${t.format}` : 'Banco completo de preparación CCSE';
        } else if (_state.tab === 'matching') {
            const set = (_data.matchingSets && _data.matchingSets[_state.matchMode]) || {};
            title = set.title || sec.es;
            sub = set.subtitle || sec.en;
        } else if (_state.tab === 'mocks') {
            if (_state.activeMockId === 'random') {
                title = 'Simulacro Aleatorio Dinámico';
                sub = '25 preguntas generadas según las cuotas oficiales (10 T1, 3 T2, 2 T3, 3 T4, 7 T5).';
            } else {
                const exam = (_data.mockExams || []).find(m => m.id === _state.activeMockId) || (_data.mockExams || [])[0];
                if (exam) { title = exam.title; sub = exam.description; }
            }
        }

        return `
            ${_backBtn('section', sec.es)}
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
        const passedCount = Object.keys(saved).filter(k => saved[k] && saved[k].passed).length;

        const values = {
            categories: `${cats.length} temas · ${factCount} hechos clave`,
            vocab: `${(_data.vocabulary || []).length} términos oficiales`,
            mcq: `${(_data.mcqs || []).length} preguntas oficiales`,
            matching: `${MATCH_MODES.length} modos interactivos`,
            mocks: `${mocks.length} modelos + simulador libre · ${passedCount} superados`
        };

        return `<div class="hce-section">${_rows(SECTIONS.map(x =>
            _row(`data-ccse-tab="${x.id}"`, x.es, x.en, values[x.id])).join(''))}</div>`;
    }

    // --------------------------------------------
    // Section 1: Categories / Facts
    // --------------------------------------------
    function _renderCategoriesTab() {
        const cats = _data.categories || [];
        if (!_state.selectedCategory) {
            return `<div class="hce-section">${_rows(cats.map(c =>
                _row(`data-ccse-cat="${_esc(c.id)}"`, `Tema ${c.num} · ${c.titleEs}`, c.titleEn,
                     `${(c.facts || []).length} hechos clave`)).join(''))}</div>`;
        }

        const c = _category(_state.selectedCategory) || cats[0];
        if (!c) return '';

        return `
            <div class="hce-section">
                <p class="hce-cat-block-sub">${_esc(c.summary)}</p>
                <div class="hce-toolbar hce-actions">
                    <button type="button" class="hce-secondary-btn" data-ccse-practice-cat="${_esc(c.tarea || 'all')}">Practicar preguntas de este bloque →</button>
                    <button type="button" class="hce-link-btn" data-ccse-toggle-en="1">
                        ${_state.showEnglishAll ? 'Ocultar inglés' : 'Mostrar inglés'}
                    </button>
                </div>
                <div class="hce-facts-list">
                    ${(c.facts || []).map(f => `
                        <article class="hce-fact-card">
                            <div class="hce-fact-head">
                                <h4 class="hce-fact-title">${_esc(f.title)}</h4>
                                <span class="hce-fact-sub">${_esc(f.subtitle)}</span>
                            </div>
                            <p class="hce-fact-hu">${_esc(f.explanationEs)}</p>
                            ${_state.showEnglishAll ? `
                                <p class="hce-fact-en">${_esc(f.explanationEn)}</p>
                            ` : ''}
                            <div class="hce-fact-clue">
                                <strong>Clave de examen:</strong> ${_esc(f.examClue)}
                            </div>
                        </article>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // --------------------------------------------
    // Section 2: Vocabulary
    // --------------------------------------------
    function _renderVocabTab() {
        const vocab = _data.vocabulary || [];
        return `
            <div class="hce-section">
                <p class="hce-section-desc">Términos oficiales, instituciones y conceptos jurídicos y administrativos imprescindibles para superar la prueba.</p>
                <div class="hce-vocab-grid">
                    ${vocab.map(v => `
                        <div class="hce-vocab-card">
                            <div class="hce-vocab-top">
                                <strong class="hce-vocab-term">${_esc(v.term)}</strong>
                                ${_categoryBadge(v.category)}
                            </div>
                            <div class="hce-vocab-en">${_esc(v.english)}</div>
                            <div class="hce-vocab-ctx">«${_esc(v.examContext)}»</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // --------------------------------------------
    // Section 3: Targeted Drills by Tarea
    // --------------------------------------------
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
        const allMcqs = _data.mcqs || [];
        if (!_state.mcqOpen) {
            const value = list => {
                const p = _mcqProgress(list);
                return p.answered ? `${p.correct} / ${p.answered} aciertos` : `${list.length} preguntas`;
            };
            return `<div class="hce-section">${_rows(
                _row('data-ccse-mcq-tarea="all"', 'Todas las tareas oficiales', 'Banco completo de preguntas', value(allMcqs)) +
                Object.keys(TAREA_META).map(k => {
                    const t = TAREA_META[k];
                    const list = allMcqs.filter(q => q.tarea === k);
                    return _row(`data-ccse-mcq-tarea="${k}"`, `${t.name}: ${t.title}`, t.format, value(list));
                }).join('')
            )}</div>`;
        }

        const filtered = _state.mcqTarea === 'all'
            ? allMcqs
            : allMcqs.filter(q => q.tarea === _state.mcqTarea);
        const prog = _mcqProgress(filtered);

        return `
            <div class="hce-section">
                <div class="hce-mcq-stats">
                    <span>${prog.answered ? `${prog.correct} / ${prog.answered} correctas · ` : ''}${filtered.length} preguntas</span>
                    <button type="button" class="hce-link-btn" data-ccse-mcq-reset="1">Reiniciar respuestas</button>
                </div>

                <div class="hce-mcq-list">
                    ${filtered.map((q, idx) => {
                        const chosen = _state.mcqAnswers[q.id];
                        const isAnswered = chosen !== undefined;
                        return `
                            <div class="hce-mcq-card${isAnswered ? (chosen === q.correct ? ' is-correct' : ' is-wrong') : ''}">
                                <div class="hce-mcq-meta">
                                    <span class="hce-mcq-num">Pregunta ${idx + 1}</span>
                                    ${_tareaBadge(q.tarea)}
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
                                                    data-ccse-mcq-id="${_esc(q.id)}"
                                                    data-ccse-mcq-opt="${oi}"
                                                    ${isAnswered ? 'disabled' : ''}>
                                                ${_esc(opt)}
                                            </button>
                                        `;
                                    }).join('')}
                                </div>
                                ${isAnswered && q.explanation ? `
                                    <div class="hce-mcq-exp">
                                        <strong>Explicación oficial:</strong> ${_esc(q.explanation)}
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    // --------------------------------------------
    // Section 4: Matching Exercises
    // --------------------------------------------
    function _renderMatchingTab() {
        if (!_state.matchOpen) {
            return `<div class="hce-section">${_rows(MATCH_MODES.map(m => {
                const set = (_data.matchingSets && _data.matchingSets[m.id]) || {};
                return _row(`data-ccse-match-mode="${m.id}"`, m.es, set.title || m.en, `${(set.pairs || []).length} parejas`);
            }).join(''))}</div>`;
        }

        const totalInRound = _state.matchRoundPairs.length;
        const solvedCount = Object.keys(_state.matchSolvedIds).length;

        return `
            <div class="hce-section">
                <div class="hce-match-head">
                    <span class="hce-match-progress">${solvedCount} / ${totalInRound} emparejados</span>
                    <button type="button" class="hce-link-btn" data-ccse-match-shuffle="1">Nueva ronda ↻</button>
                </div>

                ${solvedCount === totalInRound && totalInRound > 0 ? `
                    <div class="hce-match-banner" style="margin-bottom:16px; padding:12px 16px; background:var(--success-bg); border-left:3px solid var(--success); font-size:14px;">
                        ¡Excelente! Has emparejado todos los elementos de esta ronda. Pulsa «Nueva ronda» para continuar practicando.
                    </div>
                ` : ''}

                <div class="hce-match-board">
                    <div class="hce-match-col">
                        <div class="hce-match-col-title">Selecciona un elemento</div>
                        ${_state.matchLeftOrder.map(item => {
                            const solved = !!_state.matchSolvedIds[item.id];
                            const selected = _state.matchSelectedLeft === item.id;
                            return `
                                <button type="button"
                                        class="hce-match-tile${solved ? ' is-solved' : ''}${selected ? ' is-selected' : ''}"
                                        data-ccse-left="${item.id}"
                                        ${solved ? 'disabled' : ''}>
                                    ${_esc(item.left)}
                                </button>
                            `;
                        }).join('')}
                    </div>
                    <div class="hce-match-col">
                        <div class="hce-match-col-title">Y luego su pareja correspondiente</div>
                        ${_state.matchRightOrder.map(item => {
                            const solved = !!_state.matchSolvedIds[item.id];
                            return `
                                <button type="button"
                                        class="hce-match-tile${solved ? ' is-solved' : ''}"
                                        data-ccse-right="${item.id}"
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

    // --------------------------------------------
    // Section 5: Mock Exams & Simulator
    // --------------------------------------------
    function _renderMocksTab() {
        const mocks = _data.mockExams || [];
        const saved = (_loadSavedProgress().mocks) || {};
        const passMark = _data.passThresholdPoints || 15;
        const maxPoints = _data.maxPoints || 25;

        // Mock list view
        if (!_state.mockOpen) {
            return `
                <div class="hce-section">
                    <p class="hce-section-desc">Cada examen consta de <strong>25 preguntas oficiales</strong> distribuidas estrictamente según el modelo del Instituto Cervantes. Se supera con un mínimo de <strong>${passMark} aciertos (60%)</strong>.</p>
                    
                    <div style="margin: 16px 0 20px;">
                        <button type="button" class="hce-primary-btn" data-ccse-mock-random="1" style="width:100%; justify-content:center; padding:14px 20px; font-size:1rem; cursor:pointer;">
                            ⚡ Generar nuevo simulacro aleatorio (25 preguntas oficiales)
                        </button>
                    </div>

                    <h3 style="font-size:1.1rem; margin:24px 0 8px; color:var(--text); font-family:var(--font-display);">Modelos oficiales de referencia</h3>
                    ${_rows(mocks.map(m => {
                        const prev = saved[m.id];
                        return _row(`data-ccse-mock-id="${_esc(m.id)}"`, m.title,
                            `${(m.questions || []).length} preguntas · Umbral de apto: ${passMark}/25`,
                            prev ? `Mejor: ${prev.points}/25 (${prev.passed ? 'APTO' : 'NO APTO'})` : 'No realizado');
                    }).join(''))}
                </div>
            `;
        }

        // Active Mock Exam View
        const questions = _state.mockQuestions || [];
        const answeredCount = Object.keys(_state.mockAnswers).length;

        let earnedPoints = 0;
        const taskScores = { tarea1: { got: 0, total: 0 }, tarea2: { got: 0, total: 0 }, tarea3: { got: 0, total: 0 }, tarea4: { got: 0, total: 0 }, tarea5: { got: 0, total: 0 } };

        questions.forEach((q, idx) => {
            const t = q.tarea || 'tarea1';
            if (taskScores[t]) taskScores[t].total++;
            if (_state.mockSubmitted && _state.mockAnswers[idx] === q.correct) {
                earnedPoints += 1;
                if (taskScores[t]) taskScores[t].got++;
            }
        });

        const passed = earnedPoints >= passMark;
        const pct = Math.round((earnedPoints / maxPoints) * 100);

        return `
            <div class="hce-section">
                <!-- Top Status Bar -->
                <div class="hce-toolbar hce-actions" style="margin-top:0; padding-bottom:12px; border-bottom:1px solid var(--border);">
                    <span style="font-weight:500;">
                        ${_state.mockSubmitted ? `Examen finalizado · ${earnedPoints} / ${maxPoints} aciertos` : `${answeredCount} de ${questions.length} respondidas`}
                    </span>
                    <div style="display:flex; align-items:center; gap:12px;">
                        ${!_state.mockSubmitted ? `
                            ${_state.timerEnabled ? `
                                <span class="hce-points-badge" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; font-weight:600;">
                                    ⏱ <span id="ccse-timer-display">${_formatTime(_state.timerRemaining)}</span>
                                </span>
                                <button type="button" class="hce-link-btn" data-ccse-timer-toggle="0">Desactivar reloj</button>
                            ` : `
                                <button type="button" class="hce-secondary-btn" data-ccse-timer-toggle="1" style="padding:6px 12px; font-size:13px;">
                                    ⏱ Activar temporizador (45 min)
                                </button>
                            `}
                        ` : ''}
                    </div>
                </div>

                <!-- Submitted Results Dashboard -->
                ${_state.mockSubmitted ? `
                    <div class="hce-mock-result ${passed ? 'is-pass' : 'is-fail'}" style="margin:20px 0 24px; padding:18px 20px; background:var(--wash); border-radius:var(--radius-sm); border-top:3px solid ${passed ? 'var(--success)' : 'var(--danger)'};">
                        <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:8px;">
                            <h4 class="hce-mock-result-title" style="margin:0; font-size:1.4rem;">
                                Calificación Oficial: <span style="font-weight:700; color:${passed ? 'var(--success)' : 'var(--danger)'};">${passed ? 'APTO' : 'NO APTO'}</span>
                            </h4>
                            <span style="font-size:1.1rem; font-weight:600;">${earnedPoints} / ${maxPoints} aciertos (${pct}%)</span>
                        </div>
                        <p style="margin:10px 0 16px; font-size:15px; line-height:1.5;">
                            ${passed 
                                ? '¡Enhorabuena! Has superado con éxito la prueba de Conocimientos Constitucionales y Socioculturales de España superando el mínimo legal de 15 aciertos.'
                                : 'Resultado insuficiente para superar la prueba real. El Instituto Cervantes exige un mínimo de 15 aciertos sobre 25 preguntas. Revisa tus respuestas a continuación y vuelve a intentarlo.'}
                        </p>

                        <!-- Breakdown by Task -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px; margin-bottom:18px;">
                            ${Object.keys(taskScores).map(tk => {
                                const st = taskScores[tk];
                                const meta = TAREA_META[tk];
                                return `
                                    <div style="background:var(--bg); border:1px solid var(--border); border-radius:var(--radius-sm); padding:8px 10px; text-align:center;">
                                        <div style="font-size:12px; color:var(--muted);">${meta.name}</div>
                                        <div style="font-size:1.1rem; font-weight:600; margin-top:2px;">${st.got} / ${st.total}</div>
                                    </div>
                                `;
                            }).join('')}
                        </div>

                        <div style="display:flex; gap:12px; flex-wrap:wrap;">
                            <button type="button" class="hce-primary-btn" data-ccse-mock-retry="1">Repetir este examen</button>
                            <button type="button" class="hce-secondary-btn" data-ccse-mock-random="1">Nuevo simulacro aleatorio</button>
                            <button type="button" class="hce-link-btn" data-ccse-back="section" style="margin-left:auto;">← Lista de simulacros</button>
                        </div>
                    </div>
                ` : ''}

                <!-- Question List with Task Separators -->
                <div class="hce-mcq-list" style="margin-top:20px;">
                    ${questions.map((q, idx) => {
                        const chosen = _state.mockAnswers[idx];
                        const meta = TAREA_META[q.tarea] || { name: 'Tarea', title: '' };
                        
                        // Show task header divider before the first question of each task
                        const isTaskHeader = idx === 0 || q.tarea !== questions[idx - 1].tarea;
                        const headerHtml = isTaskHeader ? `
                            <div class="ccse-task-header" style="margin:28px 0 14px; padding:10px 14px; background:var(--wash); border-left:3px solid var(--primary); border-radius:var(--radius-sm);">
                                <h4 style="margin:0; font-size:1rem; font-weight:600; font-family:var(--font-display);">${meta.name} · ${meta.title}</h4>
                                <span style="font-size:13px; color:var(--muted);">${meta.format}</span>
                            </div>
                        ` : '';

                        return `
                            ${headerHtml}
                            <div class="hce-mcq-card${_state.mockSubmitted ? (chosen === q.correct ? ' is-correct' : ' is-wrong') : ''}">
                                <div class="hce-mcq-meta">
                                    <span class="hce-mcq-num">Pregunta ${idx + 1} de ${questions.length}</span>
                                    <span class="hce-points-badge">1 punto</span>
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
                                                    data-ccse-mock-q="${idx}"
                                                    data-ccse-mock-opt="${oi}"
                                                    ${_state.mockSubmitted ? 'disabled' : ''}>
                                                ${_esc(opt)}
                                            </button>
                                        `;
                                    }).join('')}
                                </div>
                                ${_state.mockSubmitted && q.explanation ? `
                                    <div class="hce-mcq-exp">
                                        <strong>Explicación:</strong> ${_esc(q.explanation)}
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>

                <!-- Submit Bar -->
                ${!_state.mockSubmitted ? `
                    <div class="hce-mock-submit-bar" style="margin-top:28px; padding-top:20px; border-top:1px solid var(--border); text-align:center;">
                        <button type="button" class="hce-primary-btn" data-ccse-mock-submit="1" style="padding:14px 28px; font-size:1.05rem; cursor:pointer;">
                            Entregar examen y ver calificación oficial (${answeredCount} de ${questions.length})
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

    function _closeItem() {
        _state.selectedCategory = null;
        _state.mcqOpen = false;
        _state.matchOpen = false;
        _state.mockOpen = false;
        _stopTimer();
    }

    function _go(container, options) {
        _paint(container, options);
        if (typeof window !== 'undefined' && window.scrollTo) window.scrollTo(0, 0);
    }

    function _wireEvents(container, options) {
        if (container.dataset.ccseWired) return;
        container.dataset.ccseWired = '1';

        container.addEventListener('click', e => {
            const backBtn = e.target.closest('[data-ccse-back]');
            if (backBtn) {
                const kind = backBtn.getAttribute('data-ccse-back');
                if (kind === 'exit') {
                    _stopTimer();
                    if (options && typeof options.onBack === 'function') options.onBack();
                    return;
                }
                if (kind === 'hub') {
                    _stopTimer();
                    _state.tab = null;
                } else {
                    _closeItem();
                }
                _go(container, options);
                return;
            }

            const tabBtn = e.target.closest('[data-ccse-tab]');
            if (tabBtn) {
                _state.tab = tabBtn.getAttribute('data-ccse-tab');
                _closeItem();
                _go(container, options);
                return;
            }

            const catBtn = e.target.closest('[data-ccse-cat]');
            if (catBtn) {
                _state.selectedCategory = catBtn.getAttribute('data-ccse-cat');
                _go(container, options);
                return;
            }

            if (e.target.closest('[data-ccse-toggle-en]')) {
                _state.showEnglishAll = !_state.showEnglishAll;
                _paint(container, options);
                return;
            }

            const practiceCatBtn = e.target.closest('[data-ccse-practice-cat]');
            if (practiceCatBtn) {
                _state.mcqTarea = practiceCatBtn.getAttribute('data-ccse-practice-cat');
                _state.mcqOpen = true;
                _state.tab = 'mcq';
                _go(container, options);
                return;
            }

            const mcqTareaBtn = e.target.closest('[data-ccse-mcq-tarea]');
            if (mcqTareaBtn) {
                _state.mcqTarea = mcqTareaBtn.getAttribute('data-ccse-mcq-tarea');
                _state.mcqOpen = true;
                _go(container, options);
                return;
            }

            if (e.target.closest('[data-ccse-mcq-reset]')) {
                _state.mcqAnswers = {};
                _shuffleAllMcqs();
                _paint(container, options);
                return;
            }

            const mcqOptBtn = e.target.closest('[data-ccse-mcq-opt]');
            if (mcqOptBtn) {
                const qId = mcqOptBtn.getAttribute('data-ccse-mcq-id');
                const optIdx = Number(mcqOptBtn.getAttribute('data-ccse-mcq-opt'));
                _state.mcqAnswers[qId] = optIdx;
                _paint(container, options);
                return;
            }

            const matchModeBtn = e.target.closest('[data-ccse-match-mode]');
            if (matchModeBtn) {
                _state.matchMode = matchModeBtn.getAttribute('data-ccse-match-mode');
                _state.matchOpen = true;
                _initMatchRound();
                _go(container, options);
                return;
            }

            if (e.target.closest('[data-ccse-match-shuffle]')) {
                _initMatchRound();
                _paint(container, options);
                return;
            }

            const leftTile = e.target.closest('[data-ccse-left]');
            if (leftTile) {
                const id = leftTile.getAttribute('data-ccse-left');
                _state.matchSelectedLeft = (_state.matchSelectedLeft === id) ? null : id;
                _paint(container, options);
                return;
            }

            const rightTile = e.target.closest('[data-ccse-right]');
            if (rightTile && _state.matchSelectedLeft) {
                const rightId = rightTile.getAttribute('data-ccse-right');
                if (rightId === _state.matchSelectedLeft) {
                    _state.matchSolvedIds[rightId] = true;
                    _state.matchSelectedLeft = null;
                } else {
                    _state.matchSelectedLeft = null;
                }
                _paint(container, options);
                return;
            }

            // Pick standard mock exam
            const mockPickBtn = e.target.closest('[data-ccse-mock-id]');
            if (mockPickBtn) {
                _state.activeMockId = mockPickBtn.getAttribute('data-ccse-mock-id');
                _state.mockQuestions = _loadMockQuestions(_state.activeMockId);
                _state.mockAnswers = {};
                _state.mockSubmitted = false;
                _state.mockOpen = true;
                _stopTimer();
                if (_state.timerEnabled) _startTimer(container, options);
                _go(container, options);
                return;
            }

            // Pick random dynamic mock exam
            if (e.target.closest('[data-ccse-mock-random]')) {
                _state.activeMockId = 'random';
                _state.mockQuestions = _loadMockQuestions('random');
                _state.mockAnswers = {};
                _state.mockSubmitted = false;
                _state.mockOpen = true;
                _stopTimer();
                if (_state.timerEnabled) _startTimer(container, options);
                _go(container, options);
                return;
            }

            // Toggle Timer
            const timerToggleBtn = e.target.closest('[data-ccse-timer-toggle]');
            if (timerToggleBtn) {
                const enable = timerToggleBtn.getAttribute('data-ccse-timer-toggle') === '1';
                _state.timerEnabled = enable;
                if (enable && !_state.mockSubmitted) {
                    _startTimer(container, options);
                } else {
                    _stopTimer();
                }
                _paint(container, options);
                return;
            }

            // Answer mock question
            const mockOptBtn = e.target.closest('[data-ccse-mock-opt]');
            if (mockOptBtn && !_state.mockSubmitted) {
                const qIdx = Number(mockOptBtn.getAttribute('data-ccse-mock-q'));
                const optIdx = Number(mockOptBtn.getAttribute('data-ccse-mock-opt'));
                _state.mockAnswers[qIdx] = optIdx;
                _paint(container, options);
                return;
            }

            // Submit mock exam
            if (e.target.closest('[data-ccse-mock-submit]')) {
                _stopTimer();
                _state.mockSubmitted = true;
                _recordMockResults();
                _paint(container, options);
                return;
            }

            // Retry mock exam
            if (e.target.closest('[data-ccse-mock-retry]')) {
                _state.mockQuestions = _loadMockQuestions(_state.activeMockId);
                _state.mockAnswers = {};
                _state.mockSubmitted = false;
                _stopTimer();
                if (_state.timerEnabled) _startTimer(container, options);
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
        container.innerHTML = '<p class="text-muted level-empty">Cargando preparación del Examen CCSE…</p>';
        try {
            await _loadData();
            _state.tab = null;
            _closeItem();
            _wireEvents(container, options);
            _paint(container, options);
        } catch (err) {
            console.error('CcseExam render failed:', err);
            container.innerHTML = '<p class="text-muted level-empty">No se pudo cargar el módulo de examen CCSE.</p>';
        }
    }

    // Called by Workshop when navigating away
    function stop() {
        _stopTimer();
    }

    return {
        render,
        stop,
        // Exposed for testing
        _generateRandomMock,
        _loadMockQuestions
    };
})();
