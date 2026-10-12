// ============================================
// VIDEO STUDIO (Learn from Video)
// ============================================
// Authentic video listening comprehension driller inspired by
// Conjuguemos video listening.
//
// Tabs:
// 1. Comprehension Quiz: Multi-question comprehension assessment based on
//    the authentic reportage, arguments, facts, and figures.
// 2. Fill-in-the-Blank: Aural Cloze transcription with Easy (dropdown)
//    and Hard (typed input) options.
// 3. Transcript: Full unredacted authentic transcript with Reader word lookup,
//    optional line translations, and lexical footnotes.

const VideoDriller = (function () {
    'use strict';

    let _container = null;
    let _videos = [];
    let _currentVideoId = null;
    let _activeTab = 'quiz'; // 'quiz' | 'cloze' | 'transcript'
    let _clozeSubMode = 'easy'; // 'easy' | 'hard'
    let _showTranslations = false;
    let _quizAnswers = {}; // { [qId]: selectedIndex }

    // Built-in fallback video collection in case of offline / test environments
    const _FALLBACK_VIDEOS = [
        {
            id: "espana-crisis-vivienda-bbc",
            title: "Cómo pasó España del boom inmobiliario a una crisis de vivienda",
            source: "BBC News Mundo",
            youtubeId: "wNJ0RT7enm4",
            level: "B1",
            duration: "6:27",
            topic: "Sociedad y Economía",
            origin: "Spain",
            description: "Reportaje de investigación de BBC News Mundo sobre las causas del déficit habitacional en España, el estallido de la burbuja inmobiliaria de 2008 y la situación del alquiler juvenil.",
            questions: [
                {
                    id: "q1",
                    question: "¿Por qué miles de personas protestaron acampando con carpas en la céntrica Puerta del Sol de Madrid?",
                    options: [
                        "Protestaban por la crisis de vivienda y la falta de un techo accesible",
                        "Reclamaban la rebaja de impuestos a los grandes inversores inmobiliarios",
                        "Celebraban la aprobación de nuevos créditos hipotecarios del Banco de España",
                        "Exigían la demolición de edificios antiguos en el centro histórico"
                    ],
                    answerIndex: 0,
                    explanation: "Miles de manifestantes instalaron carpas en la Puerta del Sol reclamando que 'tener un techo es un derecho' y denunciando que la vivienda se ha vuelto impagable para millones de familias."
                },
                {
                    id: "q2",
                    question: "¿Qué caracterizó al llamado «boom del ladrillo» en España entre 1997 y 2007?",
                    options: [
                        "Se construyó a un ritmo sin precedentes (hasta 5 millones de viviendas) con crédito descontrolado",
                        "El gobierno prohibió por completo la concesión de hipotecas a particulares",
                        "El Estado asumió la propiedad del 90% de las viviendas en alquiler",
                        "La construcción se detuvo totalmente debido a las altas tasas de interés del euro"
                    ],
                    answerIndex: 0,
                    explanation: "Durante el 'boom del ladrillo' se construyeron hasta 5 millones de viviendas impulsadas por tasas de interés bajas tras adoptar el euro y una gran especulación bancaria e inmobiliaria."
                },
                {
                    id: "q3",
                    question: "Según estimaciones del Banco de España y CaixaBank citadas en el video, ¿a cuánto asciende el déficit actual de viviendas?",
                    options: [
                        "Unas 750.000 viviendas",
                        "Aproximadamente 50.000 viviendas",
                        "Alrededor de 5 millones de viviendas",
                        "Menos de 10.000 viviendas"
                    ],
                    answerIndex: 0,
                    explanation: "El informe señala textualmente que el Banco de España y CaixaBank estiman un déficit de unas 750.000 viviendas debido a la falta de mano de obra, pocas empresas y altos costes de materiales."
                },
                {
                    id: "q4",
                    question: "¿Qué porcentaje del total representan las viviendas sociales en España en comparación con la media de la Unión Europea?",
                    options: [
                        "Apenas un 2%, frente al 7% de media en la Unión Europea",
                        "Un 15%, superando ampliamente la media europea",
                        "Un 30%, situándose como líder en vivienda protegida",
                        "No existen viviendas de protección social en España"
                    ],
                    answerIndex: 0,
                    explanation: "Las viviendas sociales en España representan tan solo el 2% del parque inmobiliario, una cifra muy reducida frente al promedio del 7% en los países de la Unión Europea."
                },
                {
                    id: "q5",
                    question: "¿Cuál es la consecuencia más grave de la subida del alquiler para los jóvenes españoles según el reportaje?",
                    options: [
                        "El alquiler medio alcanza el 98,7% del salario medio de un joven, retrasando la emancipación más allá de los 30 años",
                        "Los jóvenes solo necesitan destinar el 15% de sus ingresos al pago de un piso",
                        "La edad media de independencia juvenil ha bajado a los 18 años",
                        "El 85% de los menores de 30 años compra vivienda propia al terminar sus estudios"
                    ],
                    answerIndex: 0,
                    explanation: "El alquiler medio (1.176 euros mensuales) equivale al 98,7% del sueldo medio juvenil, lo que duplica el riesgo de pobreza y hace que la edad media para independizarse supere los 30 años."
                }
            ],
            cloze: [
                {
                    text: "Miles de personas protestan por una crisis que se ha convertido en una de las principales preocupaciones de los españoles: la [vivienda].",
                    english: "Thousands of people protest over a crisis that has become one of the main concerns of Spaniards: housing.",
                    options: ["vivienda", "salud", "justicia", "educación"]
                },
                {
                    text: "Hemos visto a muchas personas en las manifestaciones en Madrid repetir algo: tener un techo es un [derecho].",
                    english: "We have seen many people in the demonstrations in Madrid repeat something: having a roof over one's head is a right.",
                    options: ["derecho", "regalo", "negocio", "premio"],
                    note: "tener un techo es un derecho: Common Spanish social slogan highlighting shelter as a fundamental constitutional right."
                },
                {
                    text: "Alrededor de 3,4 millones de personas viven en condiciones de [hacinamiento] y otros 3 millones están en peligro de desalojo.",
                    english: "Around 3.4 million people live in overcrowded conditions and another 3 million are at risk of eviction.",
                    options: ["hacinamiento", "comodidad", "aislamiento", "privacidad"],
                    note: "hacinamiento: Overcrowding (excessive number of people residing in inadequate living space)."
                },
                {
                    text: "En España esta crisis se vivió como la explosión de la [burbuja] inmobiliaria que se había inflado en la década anterior.",
                    english: "In Spain this crisis was experienced as the burst of the real estate bubble that had inflated in the preceding decade.",
                    options: ["burbuja", "deuda", "bolsa", "rueda"],
                    note: "burbuja inmobiliaria: Housing / real estate bubble."
                },
                {
                    text: "En el caso español, evidentemente el crédito se salió de [madre], completamente.",
                    english: "In the Spanish case, credit obviously got completely out of hand.",
                    options: ["madre", "control", "rumbo", "foco"],
                    note: "salirse de madre: Idiomatic Spanish phrase meaning to get completely out of hand / out of control."
                },
                {
                    text: "Pero entonces llegó la crisis financiera, explotó esa burbuja y los precios se [desplomaron] hasta un 40%.",
                    english: "But then the financial crisis arrived, that bubble burst, and prices plummeted by up to 40%.",
                    options: ["desplomaron", "mantuvieron", "duplicaron", "elevaron"]
                },
                {
                    text: "Hoy, el Banco de España y CaixaBank estiman que existe un [déficit] de unas 750.000 viviendas.",
                    english: "Today, the Bank of Spain and CaixaBank estimate that there is a shortfall of around 750,000 homes.",
                    options: ["déficit", "exceso", "superávit", "aumento"]
                },
                {
                    text: "Hay pocas empresas, no hay [mano] de obra, los costes de materiales son muy caros.",
                    english: "There are few companies, there is no workforce, material costs are very expensive.",
                    options: ["mano", "falta", "tipo", "bolsa"],
                    note: "mano de obra: Manual workforce / labour supply."
                },
                {
                    text: "En 10 años el arriendo aumentó más de un 90%, es decir, hoy casi cuesta el [doble].",
                    english: "In 10 years rent increased by more than 90%, which means today it costs almost double.",
                    options: ["doble", "triple", "tercio", "mitad"]
                },
                {
                    text: "Para que te hagas una idea, el salario medio se ha incrementado en un 27,8% - las [cuentas] no dan.",
                    english: "To give you an idea, the average salary has increased by 27.8% - the numbers just don't add up.",
                    options: ["cuentas", "cifras", "tablas", "sumas"],
                    note: "las cuentas no dan: Spanish idiom meaning the math doesn't add up / expenses exceed income."
                },
                {
                    text: "La edad de [emancipación] en España ha roto récord histórico: la edad media para independizarse supera hoy los 30 años.",
                    english: "The age of emancipation in Spain has broken a historic record: the average age to become independent now exceeds 30.",
                    options: ["emancipación", "jubilación", "votación", "graduación"],
                    note: "emancipación: Moving out of the parental household into independent living."
                }
            ],
            paragraphs: [
                {
                    spanish: "¿Qué hacen estas cientos de carpas en la céntrica Puerta del Sol en Madrid? Miles de personas protestan por una crisis que se ha convertido en una de las principales preocupaciones de los españoles: la vivienda. Así que exigen al gobierno progresista de Pedro Sánchez una solución. Ojo: está claro que España no es el único país con problemas de vivienda en el mundo, pero aquí te cuento cómo pasó España del 'boom del ladrillo' a no tener suficiente vivienda accesible para su población.",
                    english: "What are these hundreds of tents doing in the central Puerta del Sol in Madrid? Thousands of people are protesting over a crisis that has become one of the main concerns of Spaniards: housing. So they demand a solution from the government. Be aware: Spain is certainly not the only country in the world facing housing issues, but here I'll tell you how Spain went from the 'construction boom' to not having enough affordable housing for its people."
                },
                {
                    spanish: "Hemos visto a muchas personas en las manifestaciones en Madrid repetir algo: tener un techo es un derecho. Y es algo que en España se ha vuelto impagable para millones de personas. Te muestro algunos datos. Una encuesta de la Fundación FOESSA, que estudia temas sociales en España, reveló que una de cada 4 personas en el país tenía dificultades para acceder y mantener una vivienda en 2024. Alrededor de 3,4 millones de personas viven en condiciones de hacinamiento y otros 3 millones están en peligro de desalojo.",
                    english: "We have seen many people at the demonstrations in Madrid repeating something: having a roof is a right. And that is something that in Spain has become unaffordable for millions. Here is some data: A survey by the FOESSA Foundation revealed that 1 in 4 people in the country had difficulties accessing and keeping housing in 2024. Around 3.4 million live in overcrowded conditions and another 3 million face the threat of eviction."
                },
                {
                    spanish: "Así como le pasó a Maricarmen, la anciana de 87 años que fue desalojada por la policía ante las cámaras del mundo y que se ha convertido en el rostro de esta crisis. El mismo estudio dice que una quinta parte de los hogares de menor renta en España dedica hoy más del 70% de sus ingresos al pago del alquiler. Y esto es un aumento del 50% de lo que tenía que pagar en 2007. Pero ¿entonces qué pasó desde ese año?",
                    english: "Just as happened to Maricarmen, the 87-year-old woman evicted by police before the world's cameras, who became the face of this crisis. The same study indicates that one-fifth of lower-income households in Spain today dedicate over 70% of their earnings to rent payments—a 50% jump compared to 2007. But what happened since then?"
                },
                {
                    spanish: "Recordemos que en 2008 el mundo se enfrentó a una de las peores crisis financieras. En España esta crisis se vivió como la explosión de la burbuja inmobiliaria que se había inflado en la década anterior. Durante el llamado 'boom del ladrillo' se construyó a un ritmo sin precedentes, hasta 5 millones de viviendas entre 1997 y 2007. Como el país había adoptado el euro, se beneficiaba de tasas de interés muy bajas y era muy fácil obtener una hipoteca, con mucha especulación. El crédito se salió de madre: superó el PIB. Pero entonces llegó la crisis, los precios se desplomaron hasta un 40% y sumió al país en una recesión hasta 2014.",
                    english: "Let's remember that in 2008 the world faced one of its worst financial crises. In Spain this was experienced as the bursting of the housing bubble inflated in the previous decade. During the 'construction boom' up to 5 million homes were built between 1997 and 2007. Having adopted the euro, Spain enjoyed low interest rates, easy mortgages, and massive speculation. Credit spiraled completely out of hand, exceeding GDP. Then the crash hit: prices plunged up to 40%, plunging Spain into recession until 2014."
                },
                {
                    spanish: "Desde entonces los niveles de construcción no han vuelto a esos números. Hoy el Banco de España y CaixaBank estiman que existe un déficit de unas 750.000 viviendas. Hay pocas empresas, falta mano de obra, los costes de materiales son muy caros y las licencias muy complejas. Además, hay casi 4 millones de viviendas vacías, muchas en pueblos y ciudades pequeñas, mientras la población creció en 1,2 millones de hogares. A esto se suma el auge de las viviendas de alquiler turístico en ciudades como Barcelona o Málaga, y que las viviendas sociales representan solo un 2%, frente al 7% de media europea.",
                    english: "Since then construction has never returned to those levels. Today the Bank of Spain and CaixaBank estimate a deficit of some 750,000 homes. There are few firms, labor shortages, high material costs, and bureaucratic licensing. Moreover, nearly 4 million homes sit vacant, many in small towns, while population growth added 1.2 million households. Tourist rentals boom in cities like Barcelona or Málaga, while social housing represents merely 2%, versus the 7% European average."
                },
                {
                    spanish: "En 10 años el arriendo aumentó más del 90%, casi el doble, mientras el salario medio solo creció un 27,8%: las cuentas no dan. El sector más afectado son los jóvenes: el precio medio del alquiler (1.176 euros) equivale al 98,7% del salario medio juvenil. Casi la mitad de los hogares jóvenes que alquilan están sobreendeudados. Por eso la edad media de emancipación ha roto récord histórico y supera hoy los 30 años.",
                    english: "Over 10 years rents surged over 90%—almost doubling—while average wages rose only 27.8%: the numbers don't add up. Young people bear the brunt: average rent (1,176 euros) equals 98.7% of the average young person's wage. Nearly half of young renting households are over-indebted. Consequently, the average emancipation age has broken records, now exceeding 30 years."
                }
            ]
        }
    ];

    async function _loadVideos() {
        let loaded = null;
        if (typeof Content !== 'undefined' && typeof Lang !== 'undefined' && Lang.content) {
            try {
                const data = await Content.json(Lang.content('videos.json'));
                if (data && Array.isArray(data.videos) && data.videos.length) {
                    loaded = data.videos;
                }
            } catch (e) {
                // fall through
            }
        }
        if (!loaded) {
            try {
                const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es-es';
                const resp = await fetch(`content/${lang}/videos.json`);
                if (resp.ok) {
                    const data = await resp.json();
                    if (data && Array.isArray(data.videos) && data.videos.length) {
                        loaded = data.videos;
                    }
                }
            } catch (e) {
                // fall through
            }
        }
        if (!loaded) loaded = _FALLBACK_VIDEOS;
        return loaded.slice().sort((a, b) => (a.title || '').localeCompare(b.title || '', undefined, { sensitivity: 'base' }));
    }

    function _normalize(str) {
        return String(str || '')
            .trim()
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/[¿¡,.]/g, '');
    }

    function _getCurrentVideo() {
        return _videos.find(v => v.id === _currentVideoId) || _videos[0];
    }

    function _renderBaseHtml() {
        const current = _getCurrentVideo();
        const optionsHtml = _videos.map(v => `
            <option value="${v.id}" ${v.id === current.id ? 'selected' : ''}>
                ${v.title} — ${v.source} (${v.level || 'B1'}${v.origin ? ' · ' + v.origin : ''})
            </option>
        `).join('');

        return `
            <div class="wk-music-root wk-video-root" style="padding-top: 8px;">
                <div class="sp-setup-head" style="margin-bottom: 14px;">
                    <p class="sp-setup-desc" style="margin: 0; color: var(--muted); font-size: 0.92rem;">
                        Authentic video listening practice with native reportage and interviews. Watch the video, solve comprehension quizzes, complete Cloze exercises, or read the verified transcript with word lookup.
                    </p>
                </div>

                <div class="wk-music-shelf">
                    <div class="wk-music-cluster">
                        <label for="wk-video-picker" class="wk-music-shelf-label">Video:</label>
                        <select id="wk-video-picker" class="wk-music-song-select">
                            ${optionsHtml}
                        </select>
                    </div>

                    <div class="wk-music-cluster">
                        <button type="button" class="wk-music-btn ${_showTranslations ? 'is-active' : ''}" id="wk-video-toggle-trans">
                            ${_showTranslations ? 'Translations: On' : 'Translations: Off'}
                        </button>
                    </div>
                </div>

                <div class="wk-music-tabs">
                    <button type="button" class="wk-music-tab ${_activeTab === 'quiz' ? 'is-active' : ''}" data-video-tab="quiz">Comprehension Quiz</button>
                    <button type="button" class="wk-music-tab ${_activeTab === 'cloze' ? 'is-active' : ''}" data-video-tab="cloze">Fill-in-the-Blank</button>
                    <button type="button" class="wk-music-tab ${_activeTab === 'transcript' ? 'is-active' : ''}" data-video-tab="transcript">Transcript</button>
                </div>

                <div class="wk-music-grid">
                    <aside class="wk-music-player-col">
                        <div class="wk-music-video-wrap">
                            <iframe id="wk-video-yt-iframe"
                                    src="https://www.youtube.com/embed/${current.youtubeId}?enablejsapi=1&rel=0&modestbranding=1"
                                    allow="autoplay; encrypted-media"
                                    allowfullscreen></iframe>
                        </div>

                        <div style="margin: 6px 0 10px; display: flex; justify-content: flex-end;">
                            <a id="wk-video-yt-link" href="https://www.youtube.com/watch?v=${current.youtubeId}" target="_blank" rel="noopener noreferrer" class="wk-music-yt-link" style="display: inline-flex; align-items: center; gap: 4px; font-size: 0.8rem; color: var(--primary); text-decoration: none; opacity: 0.85;">
                                Open on YouTube ↗
                            </a>
                        </div>

                        <div class="wk-music-status-card">
                            <span id="wk-video-status-mode-label">Comprehension Quiz</span>
                            <span class="wk-music-badge" id="wk-video-score-readout">0 answered</span>
                        </div>

                        <div class="wk-music-helper" id="wk-video-helper-text">
                            Watch the reportage and answer the comprehension questions based on the video arguments and figures.
                        </div>

                        ${_activeTab === 'cloze' ? `
                            <div class="wk-video-cloze-submodes" style="margin-top: 12px; display: flex; gap: 8px;">
                                <button type="button" class="wk-music-btn ${_clozeSubMode === 'easy' ? 'is-active' : ''}" id="wk-video-sub-easy" style="flex: 1; font-size: 0.82rem; padding: 6px 10px;">Easy (Choices)</button>
                                <button type="button" class="wk-music-btn ${_clozeSubMode === 'hard' ? 'is-active' : ''}" id="wk-video-sub-hard" style="flex: 1; font-size: 0.82rem; padding: 6px 10px;">Hard (Typing)</button>
                            </div>
                        ` : ''}
                    </aside>

                    <main class="wk-music-lyrics-col">
                        <div class="wk-music-lyrics-sheet" id="wk-video-content-sheet">
                            <!-- Rendered by _renderTabBody -->
                        </div>

                        <div class="wk-music-actions" id="wk-video-exercise-actions" style="display: none;">
                            <button type="button" class="wk-music-btn is-active" id="wk-video-btn-check">Check All</button>
                            <button type="button" class="wk-music-btn" id="wk-video-btn-reveal">Reveal Answers</button>
                            <button type="button" class="wk-music-btn" id="wk-video-btn-reset">Reset</button>
                        </div>
                    </main>
                </div>
            </div>
        `;
    }

    function _renderTabBody() {
        const sheetEl = document.getElementById('wk-video-content-sheet');
        const actionsEl = document.getElementById('wk-video-exercise-actions');
        const modeLabel = document.getElementById('wk-video-status-mode-label');
        const helperText = document.getElementById('wk-video-helper-text');
        const current = _getCurrentVideo();
        if (!sheetEl) return;

        sheetEl.innerHTML = '';

        if (_activeTab === 'quiz') {
            if (actionsEl) actionsEl.style.display = 'none';
            if (modeLabel) modeLabel.textContent = 'Comprehension Quiz';
            if (helperText) helperText.textContent = 'Watch the reportage and answer the comprehension questions based on the video arguments and figures.';
            _renderQuiz(sheetEl, current);
        } else if (_activeTab === 'cloze') {
            if (actionsEl) actionsEl.style.display = 'flex';
            if (modeLabel) modeLabel.textContent = _clozeSubMode === 'easy' ? 'Listening Cloze (Easy)' : 'Listening Cloze (Hard)';
            if (helperText) {
                helperText.textContent = _clozeSubMode === 'easy'
                    ? 'Listen to the video sentences and select the missing word from the roll-down choices.'
                    : 'Listen to the video sentences and type the exact missing word into each blank.';
            }
            _renderCloze(sheetEl, current);
        } else {
            if (actionsEl) actionsEl.style.display = 'none';
            if (modeLabel) modeLabel.textContent = 'Authentic Transcript';
            if (helperText) helperText.textContent = 'Follow along with the verified authentic transcript. Tap any word to look up definitions and grammar in the Lexicon.';
            _renderTranscript(sheetEl, current);
        }

        _updateScoreReadout();
    }

    // ----------------------------------------
    // TAB 1: COMPREHENSION QUIZ
    // ----------------------------------------
    function _renderQuiz(sheetEl, video) {
        const questions = video.questions || [];
        if (!questions.length) {
            sheetEl.innerHTML = '<div class="gd-loading">No questions available for this video.</div>';
            return;
        }

        const wrap = document.createElement('div');
        wrap.className = 'wk-video-quiz-list';
        wrap.style.display = 'flex';
        wrap.style.flexDirection = 'column';
        wrap.style.gap = '18px';

        questions.forEach((q, qIdx) => {
            const card = document.createElement('div');
            card.className = 'wk-video-quiz-card';
            card.style.background = 'var(--panel)';
            card.style.border = '1px solid var(--border)';
            card.style.borderRadius = 'var(--radius-md, 8px)';
            card.style.padding = '14px 16px';

            const answeredIndex = _quizAnswers[q.id];
            const isAnswered = typeof answeredIndex === 'number';

            const title = document.createElement('div');
            title.className = 'wk-video-quiz-q';
            title.style.fontWeight = '600';
            title.style.fontSize = '0.96rem';
            title.style.marginBottom = '10px';
            title.style.color = 'var(--ink)';
            title.textContent = `${qIdx + 1}. ${q.question}`;
            card.appendChild(title);

            const optList = document.createElement('div');
            optList.className = 'wk-video-quiz-options';
            optList.style.display = 'flex';
            optList.style.flexDirection = 'column';
            optList.style.gap = '6px';

            q.options.forEach((optText, optIdx) => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'wk-video-quiz-opt';
                btn.style.textAlign = 'left';
                btn.style.padding = '8px 12px';
                btn.style.fontSize = '0.9rem';
                btn.style.border = '1px solid var(--border)';
                btn.style.borderRadius = 'var(--radius-sm, 6px)';
                btn.style.background = 'var(--wash)';
                btn.style.cursor = isAnswered ? 'default' : 'pointer';
                btn.style.transition = 'all var(--dur-fast, 0.15s)';
                btn.textContent = optText;

                if (isAnswered) {
                    if (optIdx === q.answerIndex) {
                        btn.style.background = 'rgba(46, 125, 50, 0.15)';
                        btn.style.borderColor = 'var(--accent, #2e7d32)';
                        btn.style.color = 'var(--accent, #2e7d32)';
                        btn.style.fontWeight = '600';
                    } else if (optIdx === answeredIndex) {
                        btn.style.background = 'rgba(211, 47, 47, 0.15)';
                        btn.style.borderColor = '#d32f2f';
                        btn.style.color = '#d32f2f';
                    } else {
                        btn.style.opacity = '0.6';
                    }
                } else {
                    btn.addEventListener('click', () => {
                        _quizAnswers[q.id] = optIdx;
                        _renderTabBody();
                    });
                }

                optList.appendChild(btn);
            });
            card.appendChild(optList);

            if (isAnswered && q.explanation) {
                const expl = document.createElement('div');
                expl.className = 'wk-video-quiz-expl';
                expl.style.marginTop = '10px';
                expl.style.padding = '8px 10px';
                expl.style.borderRadius = 'var(--radius-sm, 6px)';
                expl.style.fontSize = '0.85rem';
                expl.style.background = 'var(--wash)';
                expl.style.borderLeft = `3px solid ${answeredIndex === q.answerIndex ? 'var(--accent, #2e7d32)' : '#d32f2f'}`;
                expl.innerHTML = `<strong>${answeredIndex === q.answerIndex ? '✓ Correcto:' : '✗ Explicación:'}</strong> ${q.explanation}`;
                card.appendChild(expl);
            }

            wrap.appendChild(card);
        });

        sheetEl.appendChild(wrap);
    }

    // ----------------------------------------
    // TAB 2: FILL-IN-THE-BLANK (CLOZE)
    // ----------------------------------------
    function _renderCloze(sheetEl, video) {
        const clozeLines = video.cloze || [];
        if (!clozeLines.length) {
            sheetEl.innerHTML = '<div class="gd-loading">No Cloze exercises available for this video.</div>';
            return;
        }

        const stanzaEl = document.createElement('div');
        stanzaEl.className = 'wk-music-stanza';

        clozeLines.forEach((line) => {
            const lineEl = document.createElement('div');
            lineEl.className = 'wk-music-line';

            const regex = /\[(.*?)\]/g;
            const parts = line.text.split(regex);

            parts.forEach((part, idx) => {
                const isTargetBlank = (idx % 2 === 1);
                if (isTargetBlank) {
                    const targetWord = part;

                    if (_clozeSubMode === 'easy') {
                        const select = document.createElement('select');
                        select.className = 'wk-music-blank-select';
                        select.dataset.answer = targetWord;

                        const emptyOpt = document.createElement('option');
                        emptyOpt.value = '';
                        emptyOpt.textContent = '— ? —';
                        select.appendChild(emptyOpt);

                        const opts = Array.isArray(line.options) && line.options.length ? line.options.slice() : [targetWord];
                        if (!opts.includes(targetWord)) opts.push(targetWord);
                        const shuffled = opts.slice().sort(() => Math.random() - 0.5);

                        shuffled.forEach(opt => {
                            const o = document.createElement('option');
                            o.value = opt;
                            o.textContent = opt;
                            select.appendChild(o);
                        });

                        select.addEventListener('change', () => {
                            select.classList.remove('is-correct', 'is-wrong');
                            _updateScoreReadout();
                        });

                        lineEl.appendChild(select);
                    } else {
                        const input = document.createElement('input');
                        input.type = 'text';
                        input.className = 'wk-music-blank-input';
                        input.dataset.answer = targetWord;
                        input.placeholder = '____';
                        input.addEventListener('input', () => {
                            input.classList.remove('is-correct', 'is-wrong');
                            _updateScoreReadout();
                        });
                        input.addEventListener('keydown', (e) => {
                            if (e.key === 'Enter') _checkClozeAnswers();
                        });
                        lineEl.appendChild(input);
                    }
                } else {
                    if (typeof Reader !== 'undefined' && Reader.makeClickable) {
                        const partSpan = document.createElement('span');
                        partSpan.innerHTML = Reader.makeClickable(part);
                        lineEl.appendChild(partSpan);
                    } else {
                        const words = part.split(' ');
                        words.forEach((w, wIdx) => {
                            if (!w) return;
                            const span = document.createElement('span');
                            span.className = 'wk-music-word-tap word';
                            span.textContent = w;
                            const cleanWord = w.toLowerCase().replace(/[¿¡,.]/g, '');
                            span.addEventListener('click', (e) => _handleWordTap(cleanWord, e));
                            lineEl.appendChild(span);
                            if (wIdx < words.length - 1) {
                                lineEl.appendChild(document.createTextNode(' '));
                            }
                        });
                    }
                }
            });

            if (_showTranslations && line.english) {
                const transEl = document.createElement('div');
                transEl.className = 'wk-music-line-trans';
                transEl.textContent = line.english;
                lineEl.appendChild(transEl);
            }

            if (line.note) {
                const noteEl = document.createElement('div');
                noteEl.className = 'wk-music-line-note';
                noteEl.innerHTML = `<span class="wk-note-tag">Note</span> <span class="wk-note-body">${line.note}</span>`;
                lineEl.appendChild(noteEl);
            }

            stanzaEl.appendChild(lineEl);
        });

        sheetEl.appendChild(stanzaEl);
    }

    // ----------------------------------------
    // TAB 3: TRANSCRIPT
    // ----------------------------------------
    function _renderTranscript(sheetEl, video) {
        const paragraphs = video.paragraphs || [];
        if (!paragraphs.length) {
            sheetEl.innerHTML = '<div class="gd-loading">No transcript available for this video.</div>';
            return;
        }

        const wrap = document.createElement('div');
        wrap.className = 'wk-video-transcript-wrap';
        wrap.style.display = 'flex';
        wrap.style.flexDirection = 'column';
        wrap.style.gap = '16px';

        paragraphs.forEach((p, idx) => {
            const pBox = document.createElement('div');
            pBox.className = 'wk-video-p-box';
            pBox.style.padding = '12px 14px';
            pBox.style.background = 'var(--panel)';
            pBox.style.border = '1px solid var(--border)';
            pBox.style.borderRadius = 'var(--radius-md, 8px)';

            const spanishP = document.createElement('div');
            spanishP.className = 'wk-video-spanish-text';
            spanishP.style.lineHeight = '1.7';
            spanishP.style.fontSize = '0.96rem';
            spanishP.style.color = 'var(--ink)';

            if (typeof Reader !== 'undefined' && Reader.makeClickable) {
                spanishP.innerHTML = Reader.makeClickable(p.spanish);
            } else {
                spanishP.textContent = p.spanish;
            }
            pBox.appendChild(spanishP);

            if (_showTranslations && p.english) {
                const engP = document.createElement('div');
                engP.className = 'wk-video-eng-text';
                engP.style.marginTop = '8px';
                engP.style.fontSize = '0.88rem';
                engP.style.color = 'var(--muted)';
                engP.style.fontStyle = 'italic';
                engP.style.lineHeight = '1.5';
                engP.textContent = p.english;
                pBox.appendChild(engP);
            }

            wrap.appendChild(pBox);
        });

        sheetEl.appendChild(wrap);
    }

    // ----------------------------------------
    // CLOZE CHECKING & SCORE
    // ----------------------------------------
    function _checkClozeAnswers() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        let correctCount = 0;

        blanks.forEach(el => {
            const answer = _normalize(el.dataset.answer);
            const val = _normalize(el.value);
            if (val && val === answer) {
                el.classList.add('is-correct');
                el.classList.remove('is-wrong');
                correctCount++;
            } else if (val) {
                el.classList.add('is-wrong');
                el.classList.remove('is-correct');
            } else {
                el.classList.remove('is-correct', 'is-wrong');
            }
        });

        _updateScoreReadout(`${correctCount} of ${blanks.length} correct`);
        _showToast(`${correctCount} of ${blanks.length} correct`);
    }

    function _revealClozeAnswers() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        blanks.forEach(el => {
            el.value = el.dataset.answer;
            el.classList.add('is-correct');
            el.classList.remove('is-wrong');
        });
        _updateScoreReadout(`${blanks.length} of ${blanks.length} correct`);
    }

    function _resetClozeExercises() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        blanks.forEach(el => {
            el.value = '';
            el.classList.remove('is-correct', 'is-wrong');
        });
        _updateScoreReadout();
    }

    function _updateScoreReadout(overrideText) {
        const readout = document.getElementById('wk-video-score-readout');
        if (!readout) return;

        if (overrideText) {
            readout.textContent = overrideText;
            return;
        }

        const current = _getCurrentVideo();
        if (_activeTab === 'quiz') {
            const questions = current.questions || [];
            const answered = Object.keys(_quizAnswers).length;
            let correct = 0;
            questions.forEach(q => {
                if (_quizAnswers[q.id] === q.answerIndex) correct++;
            });
            readout.textContent = answered === 0 ? `0 of ${questions.length} answered` : `${correct} of ${questions.length} correct`;
        } else if (_activeTab === 'cloze') {
            const root = _container;
            if (!root) return;
            const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
            let answered = 0;
            blanks.forEach(b => { if (b.value && b.value.trim()) answered++; });
            readout.textContent = `${answered} of ${blanks.length} answered`;
        } else {
            readout.textContent = 'Reading mode';
        }
    }

    function _showToast(msg) {
        if (typeof UI !== 'undefined' && typeof UI.toast === 'function') {
            UI.toast(msg);
            return;
        }
        const t = document.createElement('div');
        t.style.position = 'fixed';
        t.style.bottom = '24px';
        t.style.left = '50%';
        t.style.transform = 'translateX(-50%)';
        t.style.background = 'var(--ink, #102a47)';
        t.style.color = '#fff';
        t.style.padding = '8px 16px';
        t.style.borderRadius = '20px';
        t.style.fontSize = '0.85rem';
        t.style.zIndex = '9999';
        t.textContent = msg;
        document.body.appendChild(t);
        setTimeout(() => t.remove(), 2200);
    }

    async function _handleWordTap(cleanWord, event) {
        if (event && event.stopPropagation) event.stopPropagation();
        if (typeof showWord === 'function') {
            showWord(cleanWord, [cleanWord], 0, false, cleanWord);
            return;
        }
        if (typeof Reader !== 'undefined' && typeof Reader.showWord === 'function') {
            Reader.showWord(cleanWord, [cleanWord], 0, false, cleanWord);
        }
    }

    // ----------------------------------------
    // EVENT BINDINGS
    // ----------------------------------------
    function _attachEvents() {
        if (!_container) return;

        // Video picker
        const picker = document.getElementById('wk-video-picker');
        if (picker) {
            picker.addEventListener('change', (e) => {
                _currentVideoId = e.target.value;
                _quizAnswers = {};
                _renderTabBody();

                const current = _getCurrentVideo();
                const iframe = document.getElementById('wk-video-yt-iframe');
                if (iframe) {
                    iframe.src = `https://www.youtube.com/embed/${current.youtubeId}?enablejsapi=1&rel=0&modestbranding=1`;
                }
                const link = document.getElementById('wk-video-yt-link');
                if (link) {
                    link.href = `https://www.youtube.com/watch?v=${current.youtubeId}`;
                }
            });
        }

        // Translation toggle
        const toggleBtn = document.getElementById('wk-video-toggle-trans');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                _showTranslations = !_showTranslations;
                toggleBtn.textContent = _showTranslations ? 'Translations: On' : 'Translations: Off';
                toggleBtn.classList.toggle('is-active', _showTranslations);
                _renderTabBody();
            });
        }

        // Tab buttons
        _container.querySelectorAll('[data-video-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-video-tab');
                if (target === _activeTab) return;
                _activeTab = target;

                _container.querySelectorAll('[data-video-tab]').forEach(b => {
                    b.classList.toggle('is-active', b.getAttribute('data-video-tab') === _activeTab);
                });

                // Update submode buttons visibility in sidebar
                const subWrap = _container.querySelector('.wk-video-cloze-submodes');
                if (_activeTab === 'cloze' && !subWrap) {
                    _renderShell();
                    return;
                } else if (_activeTab !== 'cloze' && subWrap) {
                    _renderShell();
                    return;
                }

                _renderTabBody();
            });
        });

        // Cloze sub-mode buttons
        const subEasy = document.getElementById('wk-video-sub-easy');
        const subHard = document.getElementById('wk-video-sub-hard');
        if (subEasy) {
            subEasy.addEventListener('click', () => {
                if (_clozeSubMode === 'easy') return;
                _clozeSubMode = 'easy';
                subEasy.classList.add('is-active');
                if (subHard) subHard.classList.remove('is-active');
                _renderTabBody();
            });
        }
        if (subHard) {
            subHard.addEventListener('click', () => {
                if (_clozeSubMode === 'hard') return;
                _clozeSubMode = 'hard';
                subHard.classList.add('is-active');
                if (subEasy) subEasy.classList.remove('is-active');
                _renderTabBody();
            });
        }

        // Cloze action buttons
        const btnCheck = document.getElementById('wk-video-btn-check');
        if (btnCheck) btnCheck.addEventListener('click', _checkClozeAnswers);

        const btnReveal = document.getElementById('wk-video-btn-reveal');
        if (btnReveal) btnReveal.addEventListener('click', _revealClozeAnswers);

        const btnReset = document.getElementById('wk-video-btn-reset');
        if (btnReset) btnReset.addEventListener('click', _resetClozeExercises);
    }

    function _renderShell() {
        if (!_container) return;
        _container.innerHTML = _renderBaseHtml();
        _attachEvents();
        _renderTabBody();
    }

    // ----------------------------------------
    // PUBLIC INTERFACE
    // ----------------------------------------
    async function render(container, options) {
        _container = container;
        if (!_container) return;

        _container.innerHTML = '<div class="gd-loading">Loading authentic video library…</div>';

        _videos = await _loadVideos();
        if (!_videos || !_videos.length) {
            _container.innerHTML = '<div class="gd-empty">No authentic video drills found for this language.</div>';
            return;
        }

        if (options && options.videoId && _videos.some(v => v.id === options.videoId)) {
            _currentVideoId = options.videoId;
        } else if (!_currentVideoId || !_videos.some(v => v.id === _currentVideoId)) {
            _currentVideoId = _videos[0].id;
        }

        _quizAnswers = {};
        _renderShell();
    }

    function stop() {
        const iframe = document.getElementById('wk-video-yt-iframe');
        if (iframe) {
            iframe.src = '';
        }
    }

    return {
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.VideoDriller = VideoDriller;
}
