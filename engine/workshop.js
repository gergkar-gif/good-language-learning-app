// ============================================
// WORKSHOP
// ============================================
// Workshop is a hub, not a driller itself: it owns #drills-root and hands off
// to whichever driller the learner picks. Each driller (Verbs, GrammarDriller,
// ...) renders into its own container and knows nothing about the others —
// Workshop just remembers which one is open and draws the "back" chrome
// around it.

const Workshop = (function () {
    'use strict';

    // `langs` is omitted where a driller is genuinely language-agnostic
    // (drawn from generated indexes that, once HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md's
    // language-scoping fix lands, resolve per course) — those fail gracefully
    // to an honest empty pool today, which is a fine state to show. `verbs`
    // is the one exception: imports/verbs/verb-list.js is a plain global
    // script with no language scoping at all, so without a gate here a
    // Hungarian learner would silently drill *Spanish* conjugation under a
    // Hungarian course — wrong content, not just missing content — until
    // engine/verbs/ gets the rewrite multi-language-plan already calls for.
    const DRILLERS = [
        {
            id: 'speaking',
            icon: 'speaking',
            title: 'Speaking Studio',
            sub: () => `Practise pronunciation, shadowing, and open-ended oral production.`,
            containerId: 'speaking-driller-root',
            category: 'studios'
        },
        {
            id: 'writing',
            icon: 'writing',
            title: 'Writing Studio',
            sub: () => `Sentence translation and open-ended written production with CEFR grading.`,
            containerId: 'writing-driller-root',
            category: 'studios'
        },
        {
            id: 'hu-verb-studio',
            icon: 'hu-morphology',
            title: 'Verb & Morphology Studio',
            sub: 'Conjugation, verbal prefixes, suffixes, and word decomposition.',
            containerId: 'hu-verb-studio-root',
            langs: ['hu'],
            category: 'studios'
        },
        {
            id: 'hu-cultural-exam',
            icon: 'hu-cultural-exam',
            title: 'Hungarian Cultural Exam',
            sub: 'Magyar kulturális ismereti vizsga · 6 official categories, explained artifacts, matching & 3 mock exams.',
            containerId: 'hu-cultural-exam-root',
            langs: ['hu'],
            category: 'exams',
            level: 'B1'
        },
        {
            id: 'es-ccse-exam',
            icon: 'es-ccse-exam',
            title: 'Spanish CCSE Exam',
            sub: 'Prueba CCSE · Conocimientos Constitucionales y Socioculturales de España (Instituto Cervantes). 5 tareas, 25 preguntas y simulacros.',
            containerId: 'es-ccse-exam-root',
            langs: ['es-es'],
            category: 'exams',
            level: 'A2'
        },
        {
            id: 'es-dele-a1-exam',
            icon: 'es-dele-exam',
            title: 'DELE A1 Exam Prep',
            sub: 'Prueba DELE A1 · Instituto Cervantes. Entrenamiento por tareas oficiales: lectura, audición, escritura y conversación.',
            containerId: 'es-dele-a1-exam-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'exams',
            level: 'A1'
        },
        {
            id: 'es-dele-a2-exam',
            icon: 'es-dele-exam',
            title: 'DELE A2 Exam Prep',
            sub: 'Prueba DELE A2 · Instituto Cervantes. Entrenamiento por tareas oficiales: lectura, audición, escritura y conversación.',
            containerId: 'es-dele-a2-exam-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'exams',
            level: 'A2'
        },
        {
            id: 'es-dele-b1-exam',
            icon: 'es-dele-exam',
            title: 'DELE B1 Exam Prep',
            sub: 'Prueba DELE B1 · Instituto Cervantes. Entrenamiento por tareas oficiales: lectura, audición, escritura y conversación.',
            containerId: 'es-dele-b1-exam-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'exams',
            level: 'B1'
        },
        {
            id: 'es-dele-b2-exam',
            icon: 'es-dele-exam',
            title: 'DELE B2 Exam Prep',
            sub: 'Prueba DELE B2 · Instituto Cervantes. Entrenamiento por tareas oficiales: lectura, audición, escritura y conversación.',
            containerId: 'es-dele-b2-exam-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'exams',
            level: 'B2'
        },
        {
            id: 'hu-ecl-a1-exam',
            icon: 'hu-ecl-exam',
            title: 'ECL A1 Exam Prep',
            sub: 'ECL A1 nyelvvizsga · Pécsi Tudományegyetem. Olvasásértés, hallásértés, írásbeli és szóbeli készségek feladatonként.',
            containerId: 'hu-ecl-a1-exam-root',
            langs: ['hu'],
            category: 'exams',
            level: 'A1'
        },
        {
            id: 'hu-ecl-a2-exam',
            icon: 'hu-ecl-exam',
            title: 'ECL A2 Exam Prep',
            sub: 'ECL A2 nyelvvizsga · Pécsi Tudományegyetem. Olvasásértés, hallásértés, írásbeli és szóbeli készségek feladatonként.',
            containerId: 'hu-ecl-a2-exam-root',
            langs: ['hu'],
            category: 'exams',
            level: 'A2'
        },
        {
            id: 'hu-ecl-b1-exam',
            icon: 'hu-ecl-exam',
            title: 'ECL B1 Exam Prep',
            sub: 'ECL B1 nyelvvizsga · Pécsi Tudományegyetem. Olvasásértés, hallásértés, írásbeli és szóbeli készségek feladatonként.',
            containerId: 'hu-ecl-b1-exam-root',
            langs: ['hu'],
            category: 'exams',
            level: 'B1'
        },
        {
            id: 'hu-ecl-b2-exam',
            icon: 'hu-ecl-exam',
            title: 'ECL B2 Exam Prep',
            sub: 'ECL B2 nyelvvizsga · Pécsi Tudományegyetem. Olvasásértés, hallásértés, írásbeli és szóbeli készségek feladatonként.',
            containerId: 'hu-ecl-b2-exam-root',
            langs: ['hu'],
            category: 'exams',
            level: 'B2'
        },
        {
            id: 'verbs',
            icon: 'verbs',
            title: 'Verb Driller',
            sub: 'Conjugation tables and speed drills.',
            containerId: 'verb-driller-root',
            langs: ['es', 'es-latam', 'es-es'],
            category: 'foundations'
        },

        {
            id: 'listening',
            icon: 'listening',
            title: 'Listening Studio',
            sub: () => `Decoding drills and CEFR listening comprehension.`,
            containerId: 'listening-studio-root',
            category: 'studios'
        },
        {
            id: 'grammar',
            icon: 'grammar',
            title: 'Grammar Driller',
            sub: 'Practice by skill, drawn from every lesson.',
            containerId: 'grammar-driller-root',
            category: 'foundations'
        },
        {
            id: 'vocabulary',
            icon: 'vocabulary',
            title: 'Vocabulary Driller',
            sub: 'Meaning and context, drawn from every word taught.',
            containerId: 'vocabulary-driller-root',
            category: 'foundations',
            // Every exercise here infers a word from a real sentence context
            // (see PARLOUR_VOCABULARY_DRILLER_SPEC.md) — below B1 the
            // learner doesn't yet know enough surrounding vocabulary/grammar
            // for that inference to work, so it reads as a bare guessing
            // game rather than a useful drill. Gated the same way a
            // language-unavailable driller is: hidden from the picker, and
            // render() below bounces back to the picker if something still
            // tries to open it directly.
            minLevel: 'B1'
        }
    ];

    function _available(driller) {
        if (driller.langs) {
            const currentLang = typeof Lang !== 'undefined' ? Lang.code() : 'es-latam';
            if (!driller.langs.some(l => l === currentLang || currentLang.startsWith(l + '-'))) return false;
        }
        if (driller.minLevel) {
            const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];
            const level = (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel) ? LearnerPath.currentLevel() : 'A1';
            if (order.indexOf(level) < order.indexOf(driller.minLevel)) return false;
        }
        return true;
    }

    // Each driller's own mark, two-tone in the same --wash/--ink/--accent
    // formula as the Lessons path art (PATH_SHAPES in engine/curriculum.js)
    // — the visual language the user asked to keep for future work. These
    // used to borrow icons from unrelated sections (Translation wore the
    // Library icon, Vocabulary wore the Decks icon); each is now its own.
    const DRILLER_ICONS = {
        // a table corner — rows and columns, the conjugation grid
        verbs: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 50 50 8A42 42 0 0 1 92 50Z" class="ps-ink"/><rect x="20" y="60" width="16" height="16" class="ps-accent"/>',
        // a rule bracketing a peak — structure, the shape of a sentence
        grammar: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 10 84 70 16 70Z" class="ps-ink"/><circle cx="50" cy="10" r="7" class="ps-accent"/>',
        // a disc split in two and rejoined at the centre — meaning crossing between languages
        translation: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 8A42 42 0 0 1 50 92Z" class="ps-ink"/><circle cx="50" cy="50" r="7" class="ps-accent"/>',
        // a card standing on the disc — one word, given room
        vocabulary: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="30" y="22" width="30" height="42" rx="2" class="ps-ink"/><rect x="38" y="70" width="14" height="10" class="ps-accent"/>',
        // a waveform — sound decoded into bars
        listening: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="28" y="40" width="8" height="20" class="ps-ink"/><rect x="46" y="26" width="8" height="48" class="ps-ink"/><rect x="64" y="40" width="8" height="20" class="ps-accent"/>',
        // a microphone capsule with a projection beacon — oral production
        speaking: '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="42" y="22" width="16" height="28" rx="8" class="ps-ink"/><path d="M34 40a16 16 0 0 0 32 0" class="ps-ink" fill="none" stroke="currentColor" stroke-width="4"/><line x1="50" y1="56" x2="50" y2="72" class="ps-ink" stroke="currentColor" stroke-width="4"/><line x1="38" y1="72" x2="62" y2="72" class="ps-ink" stroke="currentColor" stroke-width="4"/><circle cx="72" cy="28" r="6" class="ps-accent"/>',
        // a quill and manuscript — written production
        writing: '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M30 70 L65 35 L75 45 L40 80 L25 85 Z" class="ps-ink"/><line x1="60" y1="40" x2="70" y2="50" class="ps-wash" stroke="currentColor" stroke-width="2"/><circle cx="75" cy="25" r="5" class="ps-accent"/>',
        // a root block with a smaller piece attached at its edge — a
        // suffix/case ending joining onto a stem
        'hu-suffix': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="20" y="34" width="36" height="32" class="ps-ink"/><rect x="56" y="42" width="20" height="16" class="ps-accent"/>',
        // the same join, mirrored — a prefix attaching ahead of the stem
        'hu-prefix': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="44" y="34" width="36" height="32" class="ps-ink"/><rect x="24" y="42" width="20" height="16" class="ps-accent"/>',
        // a word split into stacked segments — decomposition
        'hu-morphology': '<circle cx="50" cy="50" r="42" class="ps-wash"/><rect x="26" y="26" width="48" height="12" class="ps-ink"/><rect x="26" y="44" width="48" height="12" class="ps-accent"/><rect x="26" y="62" width="30" height="12" class="ps-ink"/>',
        // the table-corner mark again, distinct fill order from the
        // Spanish Verb Driller's since only one of the two ever shows
        'hu-verb': '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M50 92 50 8A42 42 0 0 1 50 92Z" class="ps-ink"/><rect x="60" y="60" width="16" height="16" class="ps-accent"/>',
        // a dome/arch crowned with an accent jewel — Hungarian Cultural Exam
        'hu-cultural-exam': '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M26 70V48a24 24 0 0 1 48 0v22Z" class="ps-ink"/><circle cx="50" cy="20" r="7" class="ps-accent"/>',
        // classical pillars supporting an arch with a royal crown jewel — Spanish CCSE Exam
        'es-ccse-exam': '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M25 72h50v-5H25v5Zm6-9h6V34h-6v29Zm16 0h6V34h-6v29Zm16 0h6V34h-6v29ZM22 30h56l-28-13-28 13Z" class="ps-ink"/><circle cx="50" cy="21" r="5" class="ps-accent"/>',
        // diploma parchment with ribbon seal — Spanish DELE Exam
        'es-dele-exam': '<circle cx="50" cy="50" r="42" class="ps-wash"/><path d="M28 26h44v48H28z" class="ps-ink"/><line x1="36" y1="36" x2="64" y2="36" class="ps-wash" stroke="currentColor" stroke-width="2.5"/><line x1="36" y1="44" x2="64" y2="44" class="ps-wash" stroke="currentColor" stroke-width="2.5"/><circle cx="50" cy="62" r="7" class="ps-accent"/><polygon points="46,67 43,77 50,73 57,77 54,67" class="ps-accent"/>',
        // geometric academic laurel seal — Hungarian ECL Exam
        'hu-ecl-exam': '<circle cx="50" cy="50" r="42" class="ps-wash"/><polygon points="50,22 58,36 74,38 62,50 65,66 50,58 35,66 38,50 26,38 42,36" class="ps-ink"/><circle cx="50" cy="45" r="7" class="ps-accent"/>'
    };

    function _drillerIcon(id) {
        // Row thumbnails come from the art registry (a grey accent; the
        // Workshop has nothing due, so none turns ochre).
        if (typeof Art !== 'undefined' && Art.thumb) {
            const t = Art.thumb(id);
            if (t) return t;
        }
        return `<svg class="wk-card-icon" viewBox="0 0 100 100" aria-hidden="true">${DRILLER_ICONS[id] || ''}</svg>`;
    }

    let _active = null; // null | 'verbs' | 'grammar'
    let _activeOptions = null; // passed through to the open driller's render(), e.g. { skill }
    let _activeTab = 'practice'; // 'practice' | 'exams'

    function _esc(text) {
        const d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _renderCards(items) {
        return items.map(d => `
            <button class="wk-card" data-driller="${d.id}">
                ${_drillerIcon(d.icon)}
                <span class="wk-card-body">
                    <span class="wk-card-title">${d.level ? `<span class="wk-badge">${_esc(d.level)}</span>` : ''}${_esc(d.title)}</span>
                    <span class="wk-card-sub">${_esc(typeof d.sub === 'function' ? d.sub() : d.sub)}</span>
                </span>
                <span class="wk-card-arrow geo-triangle" aria-hidden="true"></span>
            </button>
        `).join('');
    }

    function _isExam(d) {
        return d.category === 'exams' || (d.id && (d.id.includes('exam') || d.id.includes('ccse')));
    }

    function _pickerHtml() {
        const available = DRILLERS.filter(_available);
        const practiceItems = available.filter(d => !_isExam(d)).sort((a, b) => a.title.localeCompare(b.title));
        const examItems = available.filter(d => _isExam(d)).sort((a, b) => {
            const levelOrder = ['a1', 'a2', 'b1', 'b2', 'c1'];
            const aIdx = a.level ? levelOrder.indexOf(a.level.toLowerCase()) : 99;
            const bIdx = b.level ? levelOrder.indexOf(b.level.toLowerCase()) : 99;
            if (aIdx !== bIdx) return aIdx - bIdx;
            return a.title.localeCompare(b.title);
        });

        let contentHtml = '';
        if (_activeTab === 'exams') {
            if (examItems.length > 0) {
                contentHtml = `<div class="wk-cards-list">${_renderCards(examItems)}</div>`;
            } else {
                contentHtml = `
                    <div class="wk-empty-level">
                        <h4>Official Exam Preparation</h4>
                        <p>Official exam models and training modules for this language are currently in development.</p>
                    </div>
                `;
            }
        } else {
            contentHtml = `
                <div class="wk-cards-list">
                    ${_renderCards(practiceItems)}
                </div>
            `;
        }

        return `
            <div class="wk-picker">
                <div class="wk-tabs-bar" role="tablist">
                    <button type="button" class="wk-tab ${_activeTab === 'practice' ? 'is-active' : ''}" data-wk-tab="practice" role="tab" aria-selected="${_activeTab === 'practice'}">
                        Practice
                    </button>
                    <button type="button" class="wk-tab ${_activeTab === 'exams' ? 'is-active' : ''}" data-wk-tab="exams" role="tab" aria-selected="${_activeTab === 'exams'}">
                        Exam Preparation
                    </button>
                </div>
                <div class="wk-tab-content">
                    ${contentHtml}
                </div>
            </div>
        `;
    }

    function _activeHtml(driller) {
        return `
            <button type="button" class="wk-back" data-action="back" aria-label="Back to Workshop">
                <svg class="art icon wk-back-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <span>Workshop</span>
            </button>
            <div id="${driller.containerId}"></div>
        `;
    }

    function _attachPickerEvents(root) {
        root.querySelectorAll('[data-driller]').forEach(btn => {
            btn.addEventListener('click', () => open(btn.dataset.driller));
        });

        root.querySelectorAll('[data-wk-tab]').forEach(tabBtn => {
            tabBtn.addEventListener('click', () => {
                _activeTab = tabBtn.dataset.wkTab;
                render();
            });
        });
    }

    function _attachActiveEvents(root) {
        const back = root.querySelector('[data-action="back"]');
        if (back) back.addEventListener('click', close);
    }

    // Every driller except Verbs (which predates this shape and manages its
    // own container directly) shares one render(container, options) shape —
    // shared with _stopActiveDriller() below, so the id-to-module mapping
    // lives in exactly one place.
    function _moduleFor(id) {
        const DRILLER_MODULES = {
            grammar: typeof GrammarDriller !== 'undefined' ? GrammarDriller : null,
            translation: typeof TranslationDriller !== 'undefined' ? TranslationDriller : null,
            vocabulary: typeof VocabularyDriller !== 'undefined' ? VocabularyDriller : null,
            listening: typeof ListeningStudio !== 'undefined' ? ListeningStudio : (typeof ListeningDriller !== 'undefined' ? ListeningDriller : null),
            'listening-studio': typeof ListeningStudio !== 'undefined' ? ListeningStudio : null,
            'listening-driller': typeof ListeningDriller !== 'undefined' ? ListeningDriller : null,
            speaking: typeof SpeakingDriller !== 'undefined' ? SpeakingDriller : null,
            writing: typeof WritingDriller !== 'undefined' ? WritingDriller : null,
            'hu-verb-studio': typeof HuVerbStudio !== 'undefined' ? HuVerbStudio : null,
            'hu-cultural-exam': typeof HuCulturalExam !== 'undefined' ? HuCulturalExam : null,
            'es-ccse-exam': typeof CcseExam !== 'undefined' ? CcseExam : null,
            'es-dele-a1-exam': typeof DeleA1Exam !== 'undefined' ? DeleA1Exam : (typeof CefrExam !== 'undefined' ? CefrExam.DeleA1Exam : null),
            'es-dele-a2-exam': typeof DeleA2Exam !== 'undefined' ? DeleA2Exam : (typeof CefrExam !== 'undefined' ? CefrExam.DeleA2Exam : null),
            'es-dele-b1-exam': typeof DeleB1Exam !== 'undefined' ? DeleB1Exam : (typeof CefrExam !== 'undefined' ? CefrExam.DeleB1Exam : null),
            'es-dele-b2-exam': typeof DeleB2Exam !== 'undefined' ? DeleB2Exam : (typeof CefrExam !== 'undefined' ? CefrExam.DeleB2Exam : null),
            'hu-ecl-a1-exam': typeof EclA1Exam !== 'undefined' ? EclA1Exam : (typeof CefrExam !== 'undefined' ? CefrExam.EclA1Exam : null),
            'hu-ecl-a2-exam': typeof EclA2Exam !== 'undefined' ? EclA2Exam : (typeof CefrExam !== 'undefined' ? CefrExam.EclA2Exam : null),
            'hu-ecl-b1-exam': typeof EclB1Exam !== 'undefined' ? EclB1Exam : (typeof CefrExam !== 'undefined' ? CefrExam.EclB1Exam : null),
            'hu-ecl-b2-exam': typeof EclB2Exam !== 'undefined' ? EclB2Exam : (typeof CefrExam !== 'undefined' ? CefrExam.EclB2Exam : null),
            'hu-verb': typeof HuVerbDriller !== 'undefined' ? HuVerbDriller : null,
            'hu-suffix': typeof HuSuffixDriller !== 'undefined' ? HuSuffixDriller : null,
            'hu-prefix': typeof HuPrefixDriller !== 'undefined' ? HuPrefixDriller : null,
            'hu-morphology': typeof HuMorphologyDriller !== 'undefined' ? HuMorphologyDriller : null
        };
        return DRILLER_MODULES[id] || null;
    }

    function _renderDriller(driller) {
        if (driller.id === 'verbs' && typeof Verbs !== 'undefined') {
            return Verbs.render(_activeOptions);
        } else if (_moduleFor(driller.id)) {
            const container = document.getElementById(driller.containerId);
            if (container) return _moduleFor(driller.id).render(container, _activeOptions);
        }
    }

    // Stops whatever the currently-open driller is doing (chiefly: a
    // Timed-mode setInterval) before Workshop switches away from it —
    // closing a driller, whether via its own back button or by leaving the
    // Workshop tab entirely, used to only swap out the DOM, leaving that
    // timer running forever against a container that no longer exists.
    function _stopActiveDriller() {
        if (!_active) return;
        if (_active === 'verbs') {
            if (typeof VerbsSpeed !== 'undefined') VerbsSpeed.reset();
            return;
        }
        const mod = _moduleFor(_active);
        if (mod && typeof mod.stop === 'function') mod.stop();
    }

    function render() {
        const root = document.getElementById('drills-root');
        if (!root) return;

        if (!_active) {
            root.innerHTML = _pickerHtml();
            _attachPickerEvents(root);
            return;
        }

        const driller = DRILLERS.find(d => d.id === _active);
        if (!driller || !_available(driller)) { _active = null; return render(); }

        root.innerHTML = _activeHtml(driller);
        _attachActiveEvents(root);
        return _renderDriller(driller);
    }

    // `options` is opaque here — Workshop just carries it to whichever
    // driller opens (e.g. `{ skill: 'location-with-ban-ben' }` for
    // GrammarDriller, from Home's post-unit practice nudge). A driller that
    // doesn't understand `options` just ignores the second render() arg.
    // Several drillers fetch content in their own render() before they can
    // draw anything, so open() shows a loading overlay across the gap
    // (see UI.showLoading) rather than leaving the old screen tappable.
    function _renderAndHideLoader(drillerTitle) {
        const label = drillerTitle ? `Loading ${drillerTitle}…` : 'Loading…';
        if (typeof UI !== 'undefined') UI.showLoading(label);
        return Promise.resolve(render()).finally(() => {
            if (typeof UI !== 'undefined') UI.hideLoading();
        });
    }

    function open(id, options) {
        // Transparent routing for Hungarian sub-drillers into the unified Verb & Morphology Studio
        if (id === 'hu-verb' || id === 'hu-suffix' || id === 'hu-prefix' || id === 'hu-morphology') {
            if (typeof Lang !== 'undefined' && Lang.code() !== 'hu') {
                Lang.set('hu');
            }
            _active = 'hu-verb-studio';
            _activeOptions = Object.assign({ activeTab: id }, options);
            return _renderAndHideLoader('Verb & Morphology Studio');
        }

        // Transparent routing for Translation driller into Writing Studio
        if (id === 'translation') {
            _active = 'writing';
            _activeOptions = Object.assign({ activeTab: 'translation' }, options);
            return _renderAndHideLoader('Writing Studio');
        }

        // Transparent routing for listening sub-drillers into Listening Studio
        if (id === 'listening-driller' || id === 'listening-decoding') {
            _active = 'listening';
            _activeOptions = Object.assign({ activeTab: 'decoding' }, options);
            return _renderAndHideLoader('Listening Studio');
        }
        if (id === 'listening-comprehension' || id === 'listening-studio') {
            _active = 'listening';
            _activeOptions = Object.assign({ activeTab: 'comprehension' }, options);
            return _renderAndHideLoader('Listening Studio');
        }


        if (id === 'exam-prep' || id === 'exams') {
            _active = null;
            _activeTab = 'exams';
            render();
            return;
        }

        const driller = DRILLERS.find(d => d.id === id);
        if (driller) {
            _activeTab = _isExam(driller) ? 'exams' : 'practice';
        }

        if (driller && driller.langs && typeof Lang !== 'undefined' && !driller.langs.includes(Lang.code())) {
            Lang.set(driller.langs[0]);
        }
        _active = id;
        _activeOptions = options || null;
        return _renderAndHideLoader(driller ? driller.title : null);
    }

    function close() {
        _stopActiveDriller();
        _active = null;
        _activeOptions = null;
        render();
    }

    // Exposed for the bug-report button — it can only tell context apart at
    // the tab level (`#drills`) otherwise, so a flag filed from inside a
    // specific driller (Verb, Grammar, ...) would report the same generic
    // "drills" location as one filed from the driller picker itself.
    function activeDriller() {
        if (!_active) return null;
        const driller = DRILLERS.find(d => d.id === _active);
        return driller ? { id: driller.id, title: driller.title } : null;
    }

    document.addEventListener('language-changed', () => {
        if (!_active) {
            render();
        }
    });

    // Whether a driller can be opened right now (language, minimum level) —
    // for buttons elsewhere that open one directly, so they don't offer a
    // driller that open() would only bounce back to the picker.
    function isAvailable(id) {
        const driller = DRILLERS.find(d => d.id === id);
        return driller ? _available(driller) : false;
    }

    function getDriller(id) {
        return DRILLERS.find(d => d.id === id) || null;
    }

    function drillers() {
        return DRILLERS.slice();
    }

    function registerDriller(def) {
        if (!def || !def.id) return;
        const idx = DRILLERS.findIndex(d => d.id === def.id);
        if (idx >= 0) DRILLERS[idx] = def;
        else DRILLERS.push(def);
    }

    function setTab(tab) {
        if (tab === 'practice' || tab === 'exams') {
            _activeTab = tab;
            if (!_active) render();
        }
    }

    return { render, open, close, activeDriller, isAvailable, setTab, getDriller, drillers, registerDriller };
})();

if (typeof window !== 'undefined') {
    window.Workshop = Workshop;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Workshop;
}
