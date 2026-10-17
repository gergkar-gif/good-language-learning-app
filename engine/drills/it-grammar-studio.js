// ============================================
// ITALIAN GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated Italian driller addressing the core contrastive difficulties:
// 1. Preposizioni Articolate (di, a, da, in, su + definite articles)
// 2. Essere vs Avere in Passato Prossimo & Participle Agreement
// 3. Pronomi Diretti, Indiretti e Combinati (mi/ti/lo/la/gli/le/ci/vi/loro & glielo/me la/ce ne)
// 4. Particelle Ci vs Ne (locativo/esistenziale vs partitivo/argomentale)
// 5. Congiuntivo vs Indicativo Triggers (opinione, dubbio, speranza, congiunzioni)

const ItGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'prepositions', label: 'Preposizioni', desc: 'Articulated prepositions (del, al, dal, nel, sul)' },
        { id: 'auxiliary', label: 'Essere vs Avere', desc: 'Passato prossimo auxiliary selection & agreement' },
        { id: 'pronouns', label: 'Pronomi', desc: 'Direct, indirect, and combined pronouns' },
        { id: 'ci_ne', label: 'Ci vs Ne', desc: 'Locative and idiomatic ci vs partitive ne' },
        { id: 'subjunctive', label: 'Congiuntivo', desc: 'Subjunctive vs indicative triggers' }
    ];

    const PREPOSITION_ITEMS = [
        {
            sentence: "Vado ___ stazione a prendere un amico.",
            options: ["alla", "al", "dalla", "nella"],
            answer: "alla",
            translation: "I am going to the station to pick up a friend.",
            rule: "'stazione' is feminine singular beginning with a consonant: a + la = alla."
        },
        {
            sentence: "Il libro è ___ tavolo in salotto.",
            options: ["sul", "nel", "al", "del"],
            answer: "sul",
            translation: "The book is on the table in the living room.",
            rule: "Location on a surface: su + il tavolo = sul."
        },
        {
            sentence: "La camera da letto è ___ primo piano.",
            options: ["al", "nel", "sul", "dal"],
            answer: "al",
            translation: "The bedroom is on the first floor.",
            rule: "Floors take 'a': a + il primo piano = al primo piano."
        },
        {
            sentence: "Metto lo zucchero ___ caffè.",
            options: ["nel", "sul", "al", "del"],
            answer: "nel",
            translation: "I put sugar in the coffee.",
            rule: "Inside a container: in + il caffè = nel."
        },
        {
            sentence: "Questo è il cane ___ zia di Marco.",
            options: ["della", "dalla", "alla", "nella"],
            answer: "della",
            translation: "This is the dog of Marco's aunt.",
            rule: "Possession: di + la zia = della."
        },
        {
            sentence: "Torno adesso ___ ufficio del direttore.",
            options: ["dall'", "dallo", "dal", "dell'"],
            answer: "dall'",
            translation: "I am returning right now from the director's office.",
            rule: "Origin from a masculine singular noun starting with a vowel: da + l'ufficio = dall'."
        },
        {
            sentence: "Le chiavi sono ___ zaino di Luca.",
            options: ["nello", "nel", "sullo", "dallo"],
            answer: "nello",
            translation: "The keys are in Luca's backpack.",
            rule: "in + lo (before z- or s+consonant): in + lo zaino = nello zaino."
        },
        {
            sentence: "Telefoniamo spesso ___ nostri nonni.",
            options: ["ai", "agli", "dei", "dai"],
            answer: "ai",
            translation: "We often call our grandparents.",
            rule: "Indirect object to masculine plural: a + i nostri nonni = ai."
        },
        {
            sentence: "Distribuisco i fogli ___ studenti.",
            options: ["agli", "ai", "degli", "dagli"],
            answer: "agli",
            translation: "I distribute the sheets to the students.",
            rule: "a + gli (masculine plural starting with s+consonant): agli studenti."
        },
        {
            sentence: "Parliamo ___ nostre vacanze in Sicilia.",
            options: ["delle", "dalle", "alle", "nelle"],
            answer: "delle",
            translation: "We talk about our holidays in Sicily.",
            rule: "Topic / of: di + le nostre vacanze = delle."
        }
    ];

    const AUXILIARY_ITEMS = [
        {
            sentence: "Ieri sera Francesca ___ a casa presto.",
            options: ["è tornata", "ha tornato", "è tornato", "ha tornata"],
            answer: "è tornata",
            translation: "Yesterday evening Francesca returned home early.",
            rule: "'Tornare' is a verb of movement and takes 'essere'; the past participle agrees with the feminine subject (tornata)."
        },
        {
            sentence: "I ragazzi ___ una pizza deliziosa.",
            options: ["hanno mangiato", "sono mangiati", "hanno mangiati", "sono mangiato"],
            answer: "hanno mangiato",
            translation: "The boys ate a delicious pizza.",
            rule: "Transitive verbs take 'avere'; with no preceding direct pronoun, the participle ends in -o."
        },
        {
            sentence: "Noi (ragazze) ___ a Roma per tre giorni.",
            options: ["siamo rimaste", "abbiamo rimasto", "siamo rimasti", "abbiamo rimaste"],
            answer: "siamo rimaste",
            translation: "We (girls) stayed in Rome for three days.",
            rule: "'Rimanere' expresses state and takes 'essere'; feminine plural agrees as 'rimaste'."
        },
        {
            sentence: "Mio fratello ___ un nuovo computer.",
            options: ["ha comprato", "è comprato", "ha comprata", "è comprata"],
            answer: "ha comprato",
            translation: "My brother bought a new computer.",
            rule: "'Comprare' takes 'avere' (ha comprato)."
        },
        {
            sentence: "A che ora ___ stamattina, Marco e Matteo?",
            options: ["vi siete svegliati", "avete svegliato", "vi siete svegliato", "avete svegliati"],
            answer: "vi siete svegliati",
            translation: "What time did you wake up this morning, Marco and Matteo?",
            rule: "Reflexive verbs always take 'essere' with subject agreement: vi siete svegliati."
        },
        {
            sentence: "Chiara ___ il treno delle otto.",
            options: ["ha perso", "è persa", "è perso", "ha persa"],
            answer: "ha perso",
            translation: "Chiara missed the eight o'clock train.",
            rule: "'Perdere' is transitive and takes 'avere' (ha perso)."
        },
        {
            sentence: "Le ragazze ___ al concerto insieme.",
            options: ["sono andate", "hanno andato", "sono andati", "hanno andate"],
            answer: "sono andate",
            translation: "The girls went to the concert together.",
            rule: "'Andare' takes 'essere'; feminine plural agrees as 'andate'."
        },
        {
            sentence: "Luigi ___ venti chilometri in bicicletta.",
            options: ["ha percorso", "è percorso", "ha percorsa", "è percorsa"],
            answer: "ha percorso",
            translation: "Luigi covered twenty kilometres by bicycle.",
            rule: "'Percorrere' takes 'avere' when followed by the distance/object (ha percorso)."
        },
        {
            sentence: "Ieri sera Giulia ___ al ristorante con gli amici.",
            options: ["è uscita", "ha uscito", "è uscito", "ha uscita"],
            answer: "è uscita",
            translation: "Yesterday evening Giulia went out to the restaurant with friends.",
            rule: "'Uscire' is an intransitive verb of movement taking 'essere' with feminine singular agreement: è uscita."
        },
        {
            sentence: "I bambini ___ tutta la notte senza svegliarsi.",
            options: ["hanno dormito", "sono dormiti", "hanno dormiti", "sono dormito"],
            answer: "hanno dormito",
            translation: "The children slept all night without waking up.",
            rule: "'Dormire' takes 'avere' in passato prossimo: hanno dormito."
        }
    ];

    const PRONOUN_ITEMS = [
        {
            sentence: "Hai visto il film di Fellini? — Sì, ___ visto ieri sera.",
            options: ["l'ho", "lo ho", "gli ho", "li ho"],
            answer: "l'ho",
            translation: "Did you see Fellini's film? — Yes, I saw it yesterday evening.",
            rule: "Direct object pronoun 'lo' elides before auxiliary avere: lo + ho = l'ho."
        },
        {
            sentence: "Hai comprato le mele? — Sì, ___ comprate al mercato.",
            options: ["le ho", "l'ho", "li ho", "la ho"],
            answer: "le ho",
            translation: "Did you buy the apples? — Yes, I bought them at the market.",
            rule: "With preceding direct object 'le', the past participle agrees in gender and number: le ho comprate."
        },
        {
            sentence: "Hai parlato a Maria? — Sì, ___ telefonato poco fa.",
            options: ["le ho", "l'ho", "gli ho", "la ho"],
            answer: "le ho",
            translation: "Did you speak to Maria? — Yes, I phoned her a little while ago.",
            rule: "Indirect object to a female is 'le' (to her); indirect pronouns do NOT cause past participle agreement."
        },
        {
            sentence: "Hai restituito il libro a Marco? — Sì, ___ restituito ieri.",
            options: ["gliel'ho", "lo gli ho", "gli l'ho", "me l'ho"],
            answer: "gliel'ho",
            translation: "Did you return the book to Marco? — Yes, I returned it to him yesterday.",
            rule: "Combined pronouns: gli (to him) + lo (it) -> glielo + ho -> gliel'ho."
        },
        {
            sentence: "Mi presti la tua penna? — Certo, ___ presto volentieri.",
            options: ["te la", "la ti", "me la", "te lo"],
            answer: "te la",
            translation: "Will you lend me your pen? — Of course, I'll gladly lend it to you.",
            rule: "Combined pronoun: ti (to you) becomes 'te' before direct 'la' (la penna): te la presto."
        },
        {
            sentence: "Hai mandato i documenti agli avvocati? — Sì, ___ mandati stamattina.",
            options: ["glieli ho", "li loro ho", "li ho loro", "glielo ho"],
            answer: "glieli ho",
            translation: "Did you send the documents to the lawyers? — Yes, I sent them to them this morning.",
            rule: "gli + li = glieli; participle agrees with 'li' (mandati)."
        },
        {
            sentence: "Porti queste chiavi a tua madre? — Va bene, ___ porto adesso.",
            options: ["gliele", "le le", "le gli", "glielo"],
            answer: "gliele",
            translation: "Are you taking these keys to your mother? — Okay, I'll take them to her now.",
            rule: "le (to her) + le (keys) combines to 'gliele'."
        },
        {
            sentence: "Chi ti ha regalato quel bel maglione? — ___ ha regalato mia nonna.",
            options: ["Me l'ha", "Te l'ha", "Me lo ha", "Se l'ha"],
            answer: "Me l'ha",
            translation: "Who gave you that nice sweater? — My grandmother gave it to me.",
            rule: "Combined pronoun: mi (to me) + lo (it) -> me lo + ha -> Me l'ha."
        },
        {
            sentence: "Hai salutato i tuoi cugini? — Sì, ___ salutati prima di partire.",
            options: ["li ho", "l'ho", "le ho", "gli ho"],
            answer: "li ho",
            translation: "Did you say goodbye to your cousins? — Yes, I said goodbye to them before leaving.",
            rule: "Direct object 'li' (masculine plural) triggers agreement: li ho salutati."
        },
        {
            sentence: "Ci puoi spiegare questa regola? — Sì, ___ spiego subito.",
            options: ["ve la", "ce la", "ve lo", "ce lo"],
            answer: "ve la",
            translation: "Can you explain this rule to us? — Yes, I will explain it to you right away.",
            rule: "Indirect 'voi' (to you plural) becomes 've' before direct 'la' (la regola): ve la spiego."
        }
    ];

    const CI_NE_ITEMS = [
        {
            sentence: "Vai spesso a Roma? — Sì, ___ vado quasi tutti i mesi.",
            options: ["ci", "ne", "lo", "li"],
            answer: "ci",
            translation: "Do you often go to Rome? — Yes, I go there almost every month.",
            rule: "'Ci' replaces a place/destination introduced by 'a', 'in', or 'su' (a Roma -> ci)."
        },
        {
            sentence: "Quanti caffè bevi al giorno? — ___ bevo tre.",
            options: ["Ne", "Ci", "Li", "Lo"],
            answer: "Ne",
            translation: "How many coffees do you drink a day? — I drink three of them.",
            rule: "'Ne' is the partitive pronoun used with quantities and numbers (tre di essi -> ne bevo tre)."
        },
        {
            sentence: "Che cosa pensi di questa situazione? — Non ___ so niente.",
            options: ["ne", "ci", "lo", "la"],
            answer: "ne",
            translation: "What do you think of this situation? — I know nothing about it.",
            rule: "'Ne' replaces topics introduced by 'di' (sapere di qualcosa -> non ne so niente)."
        },
        {
            sentence: "Credi ai miracoli? — No, non ___ credo affatto.",
            options: ["ci", "ne", "li", "gli"],
            answer: "ci",
            translation: "Do you believe in miracles? — No, I don't believe in them at all.",
            rule: "'Credere a' takes 'ci' to replace the prepositional phrase (ai miracoli -> ci credo)."
        },
        {
            sentence: "Quante mele hai comprato? — ___ comprate quattro.",
            options: ["Ne ho", "Ci ho", "Le ho", "Ne ho avute"],
            answer: "Ne ho",
            translation: "How many apples did you buy? — I bought four of them.",
            rule: "With 'ne' referring to a quantity of a feminine plural noun (mele), the participle agrees: ne ho comprate quattro."
        },
        {
            sentence: "Riesci a venire alla festa stasera? — No, non ___ riesco, mi dispiace.",
            options: ["ci", "ne", "lo", "la"],
            answer: "ci",
            translation: "Can you make it to the party tonight? — No, I can't manage it, I'm sorry.",
            rule: "'Riuscire a + infinito' is replaced by 'ci' (non ci riesco)."
        },
        {
            sentence: "Sei mai stato a Venezia? — No, non ___ sono mai stato.",
            options: ["ci", "ne", "lo", "la"],
            answer: "ci",
            translation: "Have you ever been to Venice? — No, I have never been there.",
            rule: "'Ci' is the locative pronoun replacing 'a Venezia' (essere stato a -> ci sono stato)."
        },
        {
            sentence: "Hai bisogno di aiuto con la valigia? — Grazie, non ___ ho bisogno.",
            options: ["ne", "ci", "lo", "la"],
            answer: "ne",
            translation: "Do you need help with the suitcase? — Thanks, I don't need any.",
            rule: "'Avere bisogno di' takes 'ne' to replace the 'di' complement."
        },
        {
            sentence: "Che cosa c'è dentro quella scatola? — Non ___ è rimasto niente.",
            options: ["ci", "ne", "lo", "se"],
            answer: "ci",
            translation: "What is inside that box? — Nothing is left in there.",
            rule: "'Esserci' (c'è / ci sono) uses existential 'ci'."
        },
        {
            sentence: "Vuoi un po' di torta? — Sì grazie, ___ prendo solo una fetta.",
            options: ["ne", "ci", "la", "lo"],
            answer: "ne",
            translation: "Do you want some cake? — Yes thanks, I will take only a slice of it.",
            rule: "'Ne' replaces the partitive quantity (una fetta di torta -> ne prendo solo una fetta)."
        },
        {
            sentence: "Pensi ancora all'esame di ieri? — No, non ___ penso più.",
            options: ["ci", "ne", "lo", "li"],
            answer: "ci",
            translation: "Are you still thinking about yesterday's exam? — No, I'm not thinking about it anymore.",
            rule: "'Pensare a' takes 'ci' to replace the 'a' complement (all'esame -> ci penso)."
        }
    ];

    const SUBJUNCTIVE_ITEMS = [
        {
            sentence: "Penso che Marco ___ ragione in questo caso.",
            options: ["abbia", "ha", "avrà", "avrebbe"],
            answer: "abbia",
            translation: "I think that Marco is right in this case.",
            rule: "Verbs of personal opinion ('pensare che', 'credere che') require the subjunctive in the dependent clause."
        },
        {
            sentence: "So che Marco ___ ragione, ne sono sicuro.",
            options: ["ha", "abbia", "avesse", "abbiano"],
            answer: "ha",
            translation: "I know that Marco is right, I am sure of it.",
            rule: "'Sapere che' and expressions of certainty express fact, so they take the indicative ('ha', not 'abbia')."
        },
        {
            sentence: "Spero che voi ___ fare una bella vacanza.",
            options: ["possiate", "potete", "possate", "potreste"],
            answer: "possiate",
            translation: "I hope that you can have a wonderful holiday.",
            rule: "'Sperare che' (expression of hope and desire) requires the subjunctive: voi possiate."
        },
        {
            sentence: "Usciamo a fare una passeggiata, benché ___ molto freddo.",
            options: ["faccia", "fa", "farà", "facesse"],
            answer: "faccia",
            translation: "Let's go out for a walk, although it is very cold.",
            rule: "Conjunctions of concession ('benché', 'sebbene', 'quantunque') always require the subjunctive."
        },
        {
            sentence: "È necessario che tutti gli studenti ___ puntuali alla prova.",
            options: ["siano", "sono", "saranno", "fossero"],
            answer: "siano",
            translation: "It is necessary that all students be on time for the exam.",
            rule: "Impersonal expressions of necessity ('è necessario che', 'bisogna che') take the subjunctive."
        },
        {
            sentence: "Ti chiamo prima che il treno ___ dalla stazione.",
            options: ["parta", "parte", "partirà", "partisse"],
            answer: "parta",
            translation: "I'll call you before the train leaves the station.",
            rule: "'Prima che' always triggers the subjunctive ('parta')."
        },
        {
            sentence: "Dubito che loro ___ la verità su quanto accaduto.",
            options: ["dicano", "dicono", "diranno", "dicessero"],
            answer: "dicano",
            translation: "I doubt that they are telling the truth about what happened.",
            rule: "Verbs of doubt ('dubitare che') require the subjunctive in the subordinate clause (loro dicano)."
        },
        {
            sentence: "Credo che questo ristorante ___ troppo caro per noi.",
            options: ["sia", "è", "sarà", "fosse"],
            answer: "sia",
            translation: "I believe that this restaurant is too expensive for us.",
            rule: "'Credere che' expresses subjective belief and requires the subjunctive ('sia')."
        },
        {
            sentence: "Ho l'impressione che tu non mi ___ ascoltando.",
            options: ["stia", "stai", "stessi", "starai"],
            answer: "stia",
            translation: "I have the impression that you are not listening to me.",
            rule: "'Avere l'impressione che' expresses uncertainty and triggers the subjunctive (tu stia)."
        },
        {
            sentence: "Benché ___ tardi, abbiamo deciso di fare una passeggiata.",
            options: ["fosse", "era", "è", "sia stato"],
            answer: "fosse",
            translation: "Although it was late, we decided to take a walk.",
            rule: "Concessive conjunctions ('benché') with a past main clause take the imperfect subjunctive (fosse)."
        }
    ];

    let _container = null;
    let _activeTab = 'prepositions';
    let _queue = [];
    let _index = 0;
    let _score = 0;
    let _answered = false;

    function _getItems(tabId) {
        switch (tabId) {
            case 'prepositions': return PREPOSITION_ITEMS;
            case 'auxiliary': return AUXILIARY_ITEMS;
            case 'pronouns': return PRONOUN_ITEMS;
            case 'ci_ne': return CI_NE_ITEMS;
            case 'subjunctive': return SUBJUNCTIVE_ITEMS;
            default: return PREPOSITION_ITEMS;
        }
    }

    function _shuffle(arr) {
        const copy = arr.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const tmp = copy[i]; copy[i] = copy[j]; copy[j] = tmp;
        }
        return copy;
    }

    function init(container) {
        _container = container;
        _setTab('prepositions');
    }

    function _setTab(tabId) {
        _activeTab = tabId;
        _queue = _shuffle(_getItems(tabId));
        _index = 0;
        _score = 0;
        _answered = false;
        _render();
    }

    function _render() {
        if (!_container) return;

        let navHtml = '<div class="driller-sub-tabs" style="display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:16px;">';
        TABS.forEach(t => {
            const active = t.id === _activeTab ? ' active is-active' : '';
            navHtml += `<button class="driller-tab-btn${active}" data-tab="${t.id}" style="padding:8px 14px;border-radius:20px;font-size:13px;border:1px solid var(--border);background:${t.id === _activeTab ? 'var(--accent)' : 'var(--card)'};color:${t.id === _activeTab ? '#fff' : 'inherit'};cursor:pointer;">${t.label}</button>`;
        });
        navHtml += '</div>';

        if (_index >= _queue.length) {
            _renderSummary(navHtml);
            return;
        }

        const item = _queue[_index];
        const parts = item.sentence.split('___');
        const sentenceHtml = `${parts[0]}<span class="it-blank" style="display:inline-block;min-width:70px;border-bottom:2px solid var(--accent);text-align:center;font-weight:bold;color:var(--accent);margin:0 4px;">___</span>${parts[1] || ''}`;

        let optsHtml = '<div class="it-opts-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px;">';
        item.options.forEach(opt => {
            optsHtml += `<button class="it-opt-btn" data-val="${opt}" style="padding:14px;border-radius:12px;border:1px solid var(--border);background:var(--card);font-size:16px;cursor:pointer;font-weight:600;text-align:center;transition:all 0.15s ease;">${opt}</button>`;
        });
        optsHtml += '</div>';

        _container.innerHTML = `
            <div class="it-grammar-container" style="max-width:640px;margin:0 auto;padding:16px;">
                ${navHtml}
                <div class="it-prog-bar" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;font-size:13px;color:var(--ink-light);">
                    <span>Domanda ${_index + 1} di ${_queue.length}</span>
                    <span>Punteggio: ${_score}</span>
                </div>
                <div class="it-card" style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
                    <div class="it-sentence" style="font-size:20px;line-height:1.5;margin-bottom:8px;">${sentenceHtml}</div>
                    <div class="it-translation" style="font-size:14px;color:var(--ink-light);margin-bottom:16px;">${item.translation}</div>
                    ${optsHtml}
                    <div id="it-feedback" style="display:none;margin-top:20px;padding:16px;border-radius:12px;font-size:14px;line-height:1.4;"></div>
                    <button id="it-next-btn" style="display:none;width:100%;margin-top:16px;padding:14px;background:var(--accent);color:#fff;border:none;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;">Avanti</button>
                </div>
            </div>
        `;

        _attachEvents();
    }

    function _attachEvents() {
        _container.querySelectorAll('.driller-tab-btn').forEach(btn => {
            btn.onclick = () => _setTab(btn.dataset.tab);
        });

        _container.querySelectorAll('.it-opt-btn').forEach(btn => {
            btn.onclick = () => {
                if (_answered) return;
                _submitAnswer(btn.dataset.val, btn);
            };
        });

        const nextBtn = _container.querySelector('#it-next-btn');
        if (nextBtn) {
            nextBtn.onclick = () => {
                _index++;
                _answered = false;
                _render();
            };
        }
    }

    function _submitAnswer(val, clickedBtn) {
        _answered = true;
        const item = _queue[_index];
        const isCorrect = val === item.answer;
        if (isCorrect) _score++;

        // Update blank
        const blank = _container.querySelector('.it-blank');
        if (blank) {
            blank.textContent = val;
            blank.style.color = isCorrect ? '#10b981' : '#ef4444';
        }

        // Highlight buttons
        _container.querySelectorAll('.it-opt-btn').forEach(btn => {
            if (btn.dataset.val === item.answer) {
                btn.style.background = '#d1fae5';
                btn.style.borderColor = '#10b981';
                btn.style.color = '#065f46';
            } else if (btn === clickedBtn && !isCorrect) {
                btn.style.background = '#fee2e2';
                btn.style.borderColor = '#ef4444';
                btn.style.color = '#991b1b';
            }
        });

        // Feedback box
        const fb = _container.querySelector('#it-feedback');
        fb.style.display = 'block';
        fb.style.background = isCorrect ? '#f0fdf4' : '#fef2f2';
        fb.style.border = `1px solid ${isCorrect ? '#86efac' : '#fca5a5'}`;
        fb.style.color = isCorrect ? '#166534' : '#991b1b';
        fb.innerHTML = `<strong>${isCorrect ? 'Esatto!' : 'Attenzione:'}</strong> ${item.rule}`;

        const nextBtn = _container.querySelector('#it-next-btn');
        nextBtn.style.display = 'block';
        nextBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function _renderSummary(navHtml) {
        const pct = Math.round((_score / _queue.length) * 100);
        _container.innerHTML = `
            <div class="it-grammar-container" style="max-width:640px;margin:0 auto;padding:16px;">
                ${navHtml}
                <div class="it-card" style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:32px;text-align:center;">
                    <h3 style="font-size:24px;margin-bottom:8px;">Esercizio completato!</h3>
                    <p style="font-size:16px;color:var(--ink-light);margin-bottom:24px;">Hai risposto correttamente a ${_score} su ${_queue.length} domande (${pct}%).</p>
                    <button id="it-retry-btn" style="padding:14px 28px;background:var(--accent);color:#fff;border:none;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;">Riprova</button>
                </div>
            </div>
        `;
        const retryBtn = _container.querySelector('#it-retry-btn');
        if (retryBtn) retryBtn.onclick = () => _setTab(_activeTab);
        _container.querySelectorAll('.driller-tab-btn').forEach(btn => {
            btn.onclick = () => _setTab(btn.dataset.tab);
        });
    }

    return {
        TABS: TABS,
        _poolFor: _getItems,
        render: init,
        init: init,
        stop: () => {}
    };
})();

if (typeof window !== 'undefined') {
    window.ItGrammarStudio = ItGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ItGrammarStudio;
}

