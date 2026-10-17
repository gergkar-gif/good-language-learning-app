// ============================================
// SPANISH GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated Spanish driller addressing the 5 core contrastive bottlenecks:
// 1. Ser vs Estar (essence/identity vs state/location + meaning-shifting adjectives)
// 2. Por vs Para (cause/exchange/medium vs purpose/deadline/recipient)
// 3. Pretérito vs Imperfecto (aspectual past & meaning-shifting verbs)
// 4. Clitic Pronouns & Se Lo (IO+DO order, se lo rule, enclitic attachment & accents)
// 5. Subjunctive vs Indicative Triggers (doubt vs certainty, temporal future vs habitual, antecedents)
//
// Adheres strictly to Parlour design principles:
// - Zero 'vosotros' (valid for both es-es and es-latam)
// - Zero dialect-conflicting vocabulary (neutral shared lexicon)
// - Immediate diagnostic rule feedback on answer selection

const EsGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'ser-estar', label: 'Ser vs Estar', desc: 'Inherent traits, states, locations, and meaning-shifting adjectives' },
        { id: 'por-para', label: 'Por vs Para', desc: 'Cause, exchange, and medium vs purpose, deadline, and recipient' },
        { id: 'past-aspect', label: 'Pretérito vs Imperfecto', desc: 'Completed narrative actions vs background, habit, and aspect shifts' },
        { id: 'pronouns', label: 'Pronouns & Se Lo', desc: 'Double object pronoun order, the "se lo" rule, and clitic placement' },
        { id: 'subjunctive', label: 'Subjunctive Triggers', desc: 'Doubt vs certainty, temporal conjunctions, and antecedent specificity' }
    ];

    const SER_ESTAR_ITEMS = [
        {
            sentence: "¿Dónde ___ la nueva biblioteca municipal?",
            options: ["está", "es", "queda", "sea"],
            answer: "está",
            translation: "Where is the new municipal library?",
            rule: "Location of physical objects and buildings always requires 'estar'."
        },
        {
            sentence: "Mi hermano menor ___ muy tímido con la gente que no conoce.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "My younger brother is very shy with people he does not know.",
            rule: "Inherent personality traits and defining characteristics use 'ser'."
        },
        {
            sentence: "No puedo comer esta sopa todavía; ___ demasiado caliente.",
            options: ["está", "es", "sea", "esté"],
            answer: "está",
            translation: "I cannot eat this soup yet; it is too hot.",
            rule: "Current, fluctuating physical states and temperature use 'estar'."
        },
        {
            sentence: "Laura estudió tres carreras; ___ una persona muy lista.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "Laura studied three degrees; she is a very clever person.",
            rule: "'Ser listo' means to be clever/smart ('estar listo' means to be ready)."
        },
        {
            sentence: "Ya tenemos las maletas en la puerta; ¿___ listos para salir?",
            options: ["están", "son", "estén", "sean"],
            answer: "están",
            translation: "We already have the suitcases at the door; are you ready to leave?",
            rule: "'Estar listo' expresses readiness ('ser listo' means clever/smart)."
        },
        {
            sentence: "La conferencia sobre medio ambiente ___ en el auditorio principal.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "The conference on the environment takes place in the main auditorium.",
            rule: "The location/venue of an event or happening takes 'ser' (takes place), not 'estar'."
        },
        {
            sentence: "Esta película no me gusta nada; ___ sumamente aburrida.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "I don't like this movie at all; it is extremely boring.",
            rule: "'Ser aburrido' describes a boring quality ('estar aburrido' describes feeling bored)."
        },
        {
            sentence: "Estuve esperando dos horas en la sala y ya ___ muy aburrido.",
            options: ["estoy", "soy", "esté", "sea"],
            answer: "estoy",
            translation: "I have been waiting two hours in the room and I am already very bored.",
            rule: "'Estar aburrido' expresses the temporary state of feeling bored."
        },
        {
            sentence: "Por favor revisa la puerta principal; debe ___ cerrada con llave.",
            options: ["estar", "ser", "haber", "quedar"],
            answer: "estar",
            translation: "Please check the front door; it must be locked.",
            rule: "States resulting from a completed action use 'estar + participio'."
        },
        {
            sentence: "Este pastel de chocolate casero ___ riquísimo, tienes que probarlo.",
            options: ["está", "es", "sea", "esté"],
            answer: "está",
            translation: "This homemade chocolate cake tastes delicious; you have to try it.",
            rule: "Sensory tasting evaluation of food at the moment of eating takes 'estar bueno/rico'."
        }
    ];

    const POR_PARA_ITEMS = [
        {
            sentence: "Compré este libro de arte ___ el cumpleaños de mi madre.",
            options: ["para", "por", "hacia", "según"],
            answer: "para",
            translation: "I bought this art book for my mother's birthday.",
            rule: "Intended recipient and purpose take 'para'."
        },
        {
            sentence: "Tuvimos que aplazar la reunión ___ la fuerte tormenta de nieve.",
            options: ["por", "para", "hacia", "durante"],
            answer: "por",
            translation: "We had to postpone the meeting because of the heavy snowstorm.",
            rule: "Cause, motive, or reason for an action takes 'por'."
        },
        {
            sentence: "Te cambio mi bufanda de lana ___ tus guantes negros.",
            options: ["por", "para", "de", "con"],
            answer: "por",
            translation: "I'll trade my wool scarf for your black gloves.",
            rule: "Exchange, trade, or price takes 'por'."
        },
        {
            sentence: "Necesitamos entregar el informe final ___ el próximo viernes.",
            options: ["para", "por", "en", "hasta"],
            answer: "para",
            translation: "We need to submit the final report by next Friday.",
            rule: "Deadlines and specific future target dates take 'para'."
        },
        {
            sentence: "Nos gusta mucho caminar ___ el parque central al atardecer.",
            options: ["por", "para", "hacia", "con"],
            answer: "por",
            translation: "We really enjoy walking through the central park at dusk.",
            rule: "Movement along, through, or around a space takes 'por'."
        },
        {
            sentence: "Estudio tres horas cada noche ___ aprobar el examen oficial.",
            options: ["para", "por", "con", "hacia"],
            answer: "para",
            translation: "I study three hours every night in order to pass the official exam.",
            rule: "Goal or purpose followed by an infinitive ('in order to') takes 'para'."
        },
        {
            sentence: "Te enviaré todos los documentos firmados ___ correo electrónico.",
            options: ["por", "para", "con", "en"],
            answer: "por",
            translation: "I will send you all the signed documents by email.",
            rule: "Means or medium of communication/transport takes 'por'."
        },
        {
            sentence: "___ un niño de diez años, toca la guitarra extraordinariamente bien.",
            options: ["Para", "Por", "Hacia", "Según"],
            answer: "Para",
            translation: "For a ten-year-old child, he plays the guitar extraordinarily well.",
            rule: "Standard of comparison against an expectation takes 'para'."
        },
        {
            sentence: "Llevo siempre un paraguas pequeño ___ si acaso llueve más tarde.",
            options: ["por", "para", "con", "de"],
            answer: "por",
            translation: "I always carry a small umbrella just in case it rains later.",
            rule: "The fixed idiom 'por si acaso' (just in case) takes 'por'."
        },
        {
            sentence: "Tomás trabaja incansablemente ___ el bienestar de su familia.",
            options: ["por", "para", "con", "hacia"],
            answer: "por",
            translation: "Tomás works tirelessly for the sake of his family.",
            rule: "Doing something on behalf of or for the sake/benefit of someone takes 'por'."
        }
    ];

    const PAST_ASPECT_ITEMS = [
        {
            sentence: "Ayer, mientras yo leía una novela en la sala, de repente ___ el teléfono.",
            options: ["sonó", "sonaba", "ha sonado", "sonar"],
            answer: "sonó",
            translation: "Yesterday, while I was reading a novel in the living room, the phone suddenly rang.",
            rule: "An abrupt interrupting action in the past requires the preterite ('sonó')."
        },
        {
            sentence: "Cuando éramos niños, nosotros siempre ___ a la playa en las vacaciones.",
            options: ["íbamos", "fuimos", "hemos ido", "vayamos"],
            answer: "íbamos",
            translation: "When we were children, we always used to go to the beach on vacation.",
            rule: "Habitual routines and repeated customary actions in the past take the imperfect ('íbamos')."
        },
        {
            sentence: "Anoche ___ en un restaurante italiano con unos viejos amigos.",
            options: ["cené", "cenaba", "he cenado", "cenara"],
            answer: "cené",
            translation: "Last night I had dinner at an Italian restaurant with some old friends.",
            rule: "A completed event in a bounded, finished past time frame takes the preterite ('cené')."
        },
        {
            sentence: "Hacía bastante frío y el cielo ___ completamente cubierto de nubes.",
            options: ["estaba", "estuvo", "ha estado", "esté"],
            answer: "estaba",
            translation: "It was quite cold and the sky was completely covered with clouds.",
            rule: "Background setting and atmospheric description in a past narrative take the imperfect ('estaba')."
        },
        {
            sentence: "Ayer en la reunión ___ al nuevo director del departamento por primera vez.",
            options: ["conocí", "conocía", "he conocido", "conozca"],
            answer: "conocí",
            translation: "Yesterday at the meeting I met the new department director for the first time.",
            rule: "'Conocer' in the preterite means 'met for the first time' ('conocía' = already knew)."
        },
        {
            sentence: "Disculpe, yo no ___ que la tienda cerraba los domingos.",
            options: ["sabía", "supe", "he sabido", "supiera"],
            answer: "sabía",
            translation: "Excuse me, I didn't know that the store closed on Sundays.",
            rule: "Ongoing mental state/knowledge in the past takes the imperfect ('sabía'; 'supe' = found out)."
        },
        {
            sentence: "Intenté abrir la ventana durante media hora, pero no ___ moverla.",
            options: ["pude", "podía", "he podido", "pudiera"],
            answer: "pude",
            translation: "I tried to open the window for half an hour, but I couldn't manage to move it.",
            rule: "'No pude' in the preterite indicates an attempt that failed ('no podía' describes general ability)."
        },
        {
            sentence: "Eran exactamente las diez de la noche cuando finalmente ___ a casa.",
            options: ["llegué", "llegaba", "he llegado", "llegara"],
            answer: "llegué",
            translation: "It was exactly ten at night when I finally arrived home.",
            rule: "Telling time in the past uses imperfect ('eran'), but the point arrival uses preterite ('llegué')."
        },
        {
            sentence: "Mariana ___ muy preocupada por el examen, así que no logró dormir bien.",
            options: ["estaba", "estuvo", "ha estado", "estuviera"],
            answer: "estaba",
            translation: "Mariana was very worried about the exam, so she didn't manage to sleep well.",
            rule: "Ongoing emotional or physical background states in the past take the imperfect ('estaba')."
        },
        {
            sentence: "Ayer me desperté temprano, desayuné rápido y ___ hacia el trabajo.",
            options: ["salí", "salía", "he salido", "saliera"],
            answer: "salí",
            translation: "Yesterday I woke up early, ate breakfast quickly, and left for work.",
            rule: "A sequence of completed chronological events in a narrative takes the preterite ('salí')."
        }
    ];

    const PRONOUN_ITEMS = [
        {
            sentence: "¿Le entregaste la carta a la directora? — Sí, ya ___ entregué esta mañana.",
            options: ["se la", "le la", "la le", "se lo"],
            answer: "se la",
            translation: "Did you deliver the letter to the director? — Yes, I already delivered it to her this morning.",
            rule: "Indirect object 'le' changes to 'se' before direct object 'la' (le la -> se la)."
        },
        {
            sentence: "¿Quién te prestó ese dinero? — Mi hermano ___ prestó la semana pasada.",
            options: ["me lo", "lo me", "se lo", "te lo"],
            answer: "me lo",
            translation: "Who lent you that money? — My brother lent it to me last week.",
            rule: "Indirect object pronoun ('me') always precedes direct object pronoun ('lo')."
        },
        {
            sentence: "Si tienes el documento terminado, por favor ___ ahora mismo.",
            options: ["dámelo", "me lo da", "da me lo", "dátelo"],
            answer: "dámelo",
            translation: "If you have the document finished, please give it to me right now.",
            rule: "Affirmative imperative attaches pronouns enclitically (Verb+IO+DO) with an accent: 'dámelo'."
        },
        {
            sentence: "Ese secreto es confidencial; por favor, no ___ a nadie.",
            options: ["se lo digas", "díselo", "lo se digas", "te lo digas"],
            answer: "se lo digas",
            translation: "That secret is confidential; please don't tell it to anyone.",
            rule: "Negative imperatives place pronouns before the verb: 'no se lo digas'."
        },
        {
            sentence: "¿Puedes devolver el libro a Carlos? — Sí, voy a ___ esta tarde.",
            options: ["dárselo", "se lo dar", "darlelo", "dártelo"],
            answer: "dárselo",
            translation: "Can you return the book to Carlos? — Yes, I am going to give it to him this afternoon.",
            rule: "Pronouns attach to the end of an infinitive: 'dar + se + lo = dárselo'."
        },
        {
            sentence: "¿Estás preparando el informe para los clientes? — Sí, estoy ___ en este momento.",
            options: ["preparándoselo", "preparándolelo", "se lo preparando", "preparándotelo"],
            answer: "preparándoselo",
            translation: "Are you preparing the report for the clients? — Yes, I am preparing it for them right now.",
            rule: "Attached to a gerund, pronouns require a written accent to preserve stress: 'preparándoselo'."
        },
        {
            sentence: "¿Le enviaste los paquetes a tu tío? — Sí, ya ___ envié por correo.",
            options: ["se los", "le los", "los le", "se las"],
            answer: "se los",
            translation: "Did you send the packages to your uncle? — Yes, I already sent them to him by mail.",
            rule: "Indirect 'le' becomes 'se' before masculine plural direct object 'los' (le los -> se los)."
        },
        {
            sentence: "¿Me puedes pasar la sal, por favor? — Claro, aquí ___ paso.",
            options: ["te la", "la te", "me la", "se la"],
            answer: "te la",
            translation: "Can you pass me the salt, please? — Sure, here I pass it to you.",
            rule: "Second-person indirect object 'te' precedes feminine direct object 'la' (te la)."
        },
        {
            sentence: "¿Les mostraste las fotos a tus amigos? — Sí, ya ___ mostré.",
            options: ["se las", "les las", "las les", "se los"],
            answer: "se las",
            translation: "Did you show the photos to your friends? — Yes, I already showed them to them.",
            rule: "Plural indirect 'les' becomes 'se' before feminine direct object 'las' (les las -> se las)."
        },
        {
            sentence: "Esa flor es para mamá; por favor, no ___ quites.",
            options: ["se la", "la se", "le la", "te la"],
            answer: "se la",
            translation: "That flower is for mom; please don't take it from her.",
            rule: "Negative command with 3rd-person indirect and direct objects uses pre-verbal 'se la'."
        }
    ];

    const SUBJUNCTIVE_ITEMS = [
        {
            sentence: "No creo que Juan ___ la verdad sobre lo que ocurrió.",
            options: ["diga", "dice", "dirá", "decía"],
            answer: "diga",
            translation: "I don't think Juan is telling the truth about what happened.",
            rule: "Negative opinion or doubt ('no creo que') requires the subjunctive ('diga')."
        },
        {
            sentence: "Creo firmemente que nosotros ___ suficiente tiempo para terminar.",
            options: ["tenemos", "tengamos", "tuviéramos", "tengáis"],
            answer: "tenemos",
            translation: "I firmly believe that we have enough time to finish.",
            rule: "Affirmative belief ('creo que') expresses conviction and requires the indicative ('tenemos')."
        },
        {
            sentence: "Te llamaré por teléfono tan pronto como ___ al hotel.",
            options: ["llegue", "llego", "llegará", "llegaba"],
            answer: "llegue",
            translation: "I will call you on the phone as soon as I arrive at the hotel.",
            rule: "Temporal conjunctions ('tan pronto como', 'cuando') referring to a future event trigger the subjunctive."
        },
        {
            sentence: "Mi abuelo siempre me llama tan pronto como ___ del trabajo.",
            options: ["llega", "llegue", "llegará", "llegara"],
            answer: "llega",
            translation: "My grandfather always calls me as soon as he arrives from work.",
            rule: "Temporal conjunctions describing habitual, factual routines take the indicative ('llega')."
        },
        {
            sentence: "Dudo mucho que ellos ___ el tren de las ocho con este tráfico.",
            options: ["alcancen", "alcanzan", "alcanzarán", "alcanzaban"],
            answer: "alcancen",
            translation: "I doubt very much that they will catch the eight o'clock train with this traffic.",
            rule: "Verbs expressing explicit doubt ('dudar que') trigger the subjunctive ('alcancen')."
        },
        {
            sentence: "Es evidente que el nuevo plan de transporte ___ muy eficaz.",
            options: ["es", "sea", "fuera", "sería"],
            answer: "es",
            translation: "It is evident that the new transportation plan is very effective.",
            rule: "Impersonal expressions of objective certainty ('es evidente que') take the indicative ('es')."
        },
        {
            sentence: "Es necesario que tú ___ con el director antes de tomar una decisión.",
            options: ["hables", "hablas", "hablarás", "hablabas"],
            answer: "hables",
            translation: "It is necessary that you speak with the director before making a decision.",
            rule: "Impersonal expressions of necessity or judgment ('es necesario que') take the subjunctive ('hables')."
        },
        {
            sentence: "Busco un asistente que ___ hablar tres idiomas con fluidez.",
            options: ["sepa", "sabe", "sabrá", "sabía"],
            answer: "sepa",
            translation: "I am looking for an assistant who knows how to speak three languages fluently.",
            rule: "Unspecified or indefinite antecedents in adjective clauses trigger the subjunctive ('sepa')."
        },
        {
            sentence: "Tengo un asistente que ___ hablar tres idiomas con fluidez.",
            options: ["sabe", "sepa", "supiera", "sabrá"],
            answer: "sabe",
            translation: "I have an assistant who knows how to speak three languages fluently.",
            rule: "A specific, existing antecedent known to the speaker takes the indicative ('sabe')."
        },
        {
            sentence: "Iremos a la excursión en la montaña aunque ___ frío mañana.",
            options: ["haga", "hace", "hará", "hacía"],
            answer: "haga",
            translation: "We will go on the mountain excursion even if it is cold tomorrow.",
            rule: "Concessive 'aunque' referring to an uncertain future condition triggers the subjunctive ('haga')."
        }
    ];

    let _container = null;
    let _activeTab = 'ser-estar';
    let _queue = [];
    let _idx = 0;
    let _score = 0;
    let _mistakes = [];
    let _state = 'settings'; // 'settings' | 'quiz' | 'summary'

    function _esc(s) {
        if (!s) return '';
        const d = document.createElement('div');
        d.textContent = s;
        return d.innerHTML;
    }

    function _poolFor(tabId) {
        if (tabId === 'por-para') return POR_PARA_ITEMS;
        if (tabId === 'past-aspect') return PAST_ASPECT_ITEMS;
        if (tabId === 'pronouns') return PRONOUN_ITEMS;
        if (tabId === 'subjunctive') return SUBJUNCTIVE_ITEMS;
        return SER_ESTAR_ITEMS;
    }

    function _shuffle(arr) {
        const copy = arr.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const t = copy[i];
            copy[i] = copy[j];
            copy[j] = t;
        }
        return copy;
    }

    function stop() {
        _state = 'settings';
        _queue = [];
        _idx = 0;
    }

    function _startSession(count) {
        const pool = _poolFor(_activeTab);
        const shuffled = _shuffle(pool);
        _queue = (count && count > 0) ? shuffled.slice(0, count) : shuffled;
        _idx = 0;
        _score = 0;
        _mistakes = [];
        _state = 'quiz';
        _render();
    }

    function _onAnswer(selected) {
        const item = _queue[_idx];
        const isCorrect = (selected.trim() === item.answer.trim());
        if (isCorrect) {
            _score++;
        } else {
            _mistakes.push({ item, userAns: selected });
        }

        const feedbackEl = document.getElementById('es-quiz-feedback');
        if (!feedbackEl) return;

        feedbackEl.innerHTML = `
            <div class="wk-feedback-card ${isCorrect ? 'is-correct' : 'is-wrong'}">
                <div class="wk-feedback-title">${isCorrect ? '✓ ¡Correcto!' : '✗ No exactamente'}</div>
                <div class="wk-feedback-rule"><strong>Regla:</strong> ${_esc(item.rule)}</div>
                <div class="wk-feedback-trans"><em>${_esc(item.translation)}</em></div>
                <button type="button" class="btn btn-primary wk-next-btn" id="es-next-btn">Continuar</button>
            </div>
        `;

        document.querySelectorAll('.es-opt-btn').forEach(btn => {
            btn.disabled = true;
            if (btn.dataset.opt === item.answer) {
                btn.classList.add('is-right');
            } else if (btn.dataset.opt === selected) {
                btn.classList.add('is-wrong');
            }
        });

        const nextBtn = document.getElementById('es-next-btn');
        if (nextBtn) {
            nextBtn.focus();
            nextBtn.addEventListener('click', () => {
                _idx++;
                if (_idx >= _queue.length) {
                    _state = 'summary';
                }
                _render();
            });
        }
    }

    function _renderSettings() {
        const tabMeta = TABS.find(t => t.id === _activeTab) || TABS[0];
        const pool = _poolFor(_activeTab);
        const drillInfoBtn = (typeof DrillInfo !== 'undefined') ? DrillInfo.buttonHtml('es-grammar-studio') : '';

        return `
            <div class="es-studio-settings">
                <div class="wk-settings-header">
                    <div style="display: flex; align-items: baseline; justify-content: space-between; gap: 12px;">
                        <h3>${_esc(tabMeta.label)}</h3>
                        ${drillInfoBtn}
                    </div>
                    <p class="text-muted" style="margin-top: 4px;">${_esc(tabMeta.desc)}</p>
                </div>
                <div class="es-settings-counts" style="margin-top: 24px;">
                    <p style="margin-bottom: 12px; font-weight: 500;">Número de preguntas:</p>
                    <div class="btn-group" role="group">
                        <button type="button" class="btn btn-outline-primary" data-count="5">5</button>
                        <button type="button" class="btn btn-outline-primary" data-count="10">10</button>
                        <button type="button" class="btn btn-outline-primary" data-count="${pool.length}">Todas (${pool.length})</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _renderQuiz() {
        const item = _queue[_idx];
        const options = _shuffle(item.options);
        const promptSentence = item.sentence.replace('___', '<span class="es-blank">____</span>');

        return `
            <div class="es-quiz-container">
                <div class="es-quiz-progress">
                    <span>Pregunta ${_idx + 1} / ${_queue.length}</span>
                    <span class="es-score-counter">Aciertos: ${_score}</span>
                </div>
                <div class="es-quiz-sentence">${promptSentence}</div>
                <div class="es-quiz-options">
                    ${options.map(opt => `
                        <button type="button" class="btn btn-outline-secondary es-opt-btn" data-opt="${_esc(opt)}">
                            ${_esc(opt)}
                        </button>
                    `).join('')}
                </div>
                <div id="es-quiz-feedback"></div>
            </div>
        `;
    }

    function _renderSummary() {
        const total = _queue.length;
        const pct = Math.round((_score / total) * 100);

        return `
            <div class="es-quiz-summary">
                <h3>¡Sesión completada!</h3>
                <div class="es-score-badge ${pct >= 80 ? 'high' : (pct >= 50 ? 'med' : 'low')}">
                    ${pct}% (${_score} / ${total})
                </div>
                ${_mistakes.length > 0 ? `
                    <div class="es-mistakes-review">
                        <h4>Puntos para repasar:</h4>
                        <ul class="es-mistakes-list">
                            ${_mistakes.map(m => `
                                <li>
                                    <div class="es-mistake-sentence">${_esc(m.item.sentence.replace('___', m.item.answer))}</div>
                                    <div class="es-mistake-rule">${_esc(m.item.rule)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                ` : `<p class="text-success font-weight-bold" style="color: var(--pine-success, #2f7a4d);">¡Excelente! No cometiste ningún error.</p>`}
                <div class="es-summary-actions" style="margin-top: 24px;">
                    <button type="button" class="btn btn-primary" id="es-restart-btn">Volver a practicar</button>
                </div>
            </div>
        `;
    }

    function _attachEvents() {
        if (!_container) return;

        if (typeof DrillInfo !== 'undefined') {
            DrillInfo.attach(_container);
        }

        // Nav tabs
        _container.querySelectorAll('[data-es-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                _activeTab = btn.dataset.esTab;
                _state = 'settings';
                _render();
            });
        });

        // Settings start
        _container.querySelectorAll('[data-count]').forEach(btn => {
            btn.addEventListener('click', () => {
                const count = parseInt(btn.dataset.count, 10);
                _startSession(count);
            });
        });

        // Quiz option click
        _container.querySelectorAll('.es-opt-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                _onAnswer(btn.dataset.opt);
            });
        });

        // Restart
        const restartBtn = _container.querySelector('#es-restart-btn');
        if (restartBtn) {
            restartBtn.addEventListener('click', () => {
                _state = 'settings';
                _render();
            });
        }
    }

    function _render() {
        if (!_container) return;

        let bodyHtml = '';
        if (_state === 'settings') {
            bodyHtml = _renderSettings();
        } else if (_state === 'quiz') {
            bodyHtml = _renderQuiz();
        } else if (_state === 'summary') {
            bodyHtml = _renderSummary();
        }

        _container.innerHTML = `
            <div class="sp-studio-wrap es-grammar-studio-wrap">
                <div class="sp-studio-nav" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="sp-studio-tab ${_activeTab === tab.id ? 'active' : ''}" data-es-tab="${tab.id}" role="tab" aria-selected="${_activeTab === tab.id}">
                            ${tab.label}
                        </button>
                    `).join('')}
                </div>
                <div class="es-studio-body">${bodyHtml}</div>
            </div>
        `;

        _attachEvents();
    }

    function render(container, options) {
        _container = container;
        if (options && options.tab && TABS.some(t => t.id === options.tab)) {
            _activeTab = options.tab;
        }
        _state = 'settings';
        _render();
    }

    return {
        TABS,
        render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.EsGrammarStudio = EsGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EsGrammarStudio;
}
