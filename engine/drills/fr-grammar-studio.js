// ============================================
// FRENCH GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated French driller addressing the core structural difficulties:
// 1. Clitic Pronoun Placement & Double Pronouns (me/te/se/nous/vous -> le/la/les -> lui/leur -> y -> en)
// 2. Past Participle Agreement (Accord du participe passé avec être vs avoir vs pronominaux)
// 3. Subjunctive vs Indicative Triggers (Déclencheurs du subjonctif)

const FrGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'pronouns', label: 'Pronouns', desc: 'Double object placement and clitic order' },
        { id: 'agreement', label: 'Agreement', desc: 'Past participle agreement with être & avoir' },
        { id: 'subjunctive', label: 'Subjunctive', desc: 'Subjunctive vs indicative triggers' }
    ];

    const PRONOUN_ITEMS = [
        {
            sentence: "Tu as donné le livre à Thomas ? — Oui, je ___ ai donné.",
            options: ["le lui", "lui le", "l'y", "le leur"],
            answer: "le lui",
            translation: "Did you give the book to Thomas? — Yes, I gave it to him.",
            rule: "COD 'le' precedes COI 3rd person 'lui' (le/la/les + lui/leur)."
        },
        {
            sentence: "Tu me prêtes ta voiture ? — D'accord, je ___ prête.",
            options: ["te la", "la te", "me la", "te l'"],
            answer: "te la",
            translation: "Will you lend me your car? — Okay, I'll lend it to you.",
            rule: "1st/2nd person (me/te/se/nous/vous) precedes COD (le/la/les)."
        },
        {
            sentence: "Tu as parlé de ton voyage à tes parents ? — Oui, je ___ ai parlé.",
            options: ["leur en", "en leur", "les en", "lui en"],
            answer: "leur en",
            translation: "Did you speak about your trip to your parents? — Yes, I spoke to them about it.",
            rule: "COI 'leur' precedes adverbial pronoun 'en' (lui/leur + en)."
        },
        {
            sentence: "Est-ce qu'elle va au cinéma ce soir ? — Oui, elle ___ va.",
            options: ["y", "en", "l'y", "lui"],
            answer: "y",
            translation: "Is she going to the cinema tonight? — Yes, she is going there.",
            rule: "'y' replaces location introduced by 'à' (au cinéma)."
        },
        {
            sentence: "Donne ce document à Marie immédiatement ! — D'accord, je vais ___ donner.",
            options: ["le lui", "lui le", "la lui", "le leur"],
            answer: "le lui",
            translation: "Give this document to Marie immediately! — Okay, I am going to give it to her.",
            rule: "Before infinitive: 'aller + le lui donner' (COD before COI)."
        },
        {
            sentence: "Rends-moi mon stylo ! — ___ tout de suite !",
            options: ["Rends-le-moi", "Rends-moi-le", "Me le rends", "Rends-lui-moi"],
            answer: "Rends-le-moi",
            translation: "Return my pen! — Return it to me right away!",
            rule: "Affirmative imperative: Verb-COD-COI (verb-le-moi / verb-la-moi)."
        },
        {
            sentence: "Tu ne dois pas raconter cette histoire à Paul. — Ne ___ raconte pas.",
            options: ["la lui", "lui la", "le lui", "la leur"],
            answer: "la lui",
            translation: "You must not tell this story to Paul. — Don't tell it to him.",
            rule: "Negative imperative retains normal declarative order: 'Ne la lui raconte pas'."
        },
        {
            sentence: "Combien de croissants as-tu achetés ? — J'___ ai acheté quatre.",
            options: ["en", "y", "les", "des"],
            answer: "en",
            translation: "How many croissants did you buy? — I bought four of them.",
            rule: "'en' replaces quantities and nouns introduced by partitive or numbers."
        },
        {
            sentence: "Tu penses à ton avenir ? — Oui, j'___ pense constamment.",
            options: ["y", "en", "lui", "le"],
            answer: "y",
            translation: "Do you think about your future? — Yes, I think about it constantly.",
            rule: "'penser à + chose' replaces with 'y' (j'y pense)."
        },
        {
            sentence: "Tu as envoyé les invitations aux invités ? — Oui, je ___ ai envoyées.",
            options: ["les leur", "leur les", "les lui", "leur en"],
            answer: "les leur",
            translation: "Did you send the invitations to the guests? — Yes, I sent them to them.",
            rule: "COD plural 'les' precedes COI plural 'leur' (les leur)."
        },
        {
            sentence: "Est-ce qu'il reste du café ? — Non, il n'___ reste plus.",
            options: ["en", "y", "le", "de"],
            answer: "en",
            translation: "Is there any coffee left? — No, there is none left.",
            rule: "'en' replaces indefinite/partitive quantities (du café -> en)."
        },
        {
            sentence: "Tu peux me passer le sel ? — Tiens, je ___ passe.",
            options: ["te le", "le te", "me le", "lui le"],
            answer: "te le",
            translation: "Can you pass me the salt? — Here, I pass it to you.",
            rule: "2nd person 'te' precedes COD 'le'."
        }
    ];

    const AGREEMENT_ITEMS = [
        {
            sentence: "Elle est ___ à la réunion avec dix minutes de retard.",
            options: ["arrivée", "arrivé", "arrivés", "arrivées"],
            answer: "arrivée",
            translation: "She arrived at the meeting ten minutes late.",
            rule: "With auxiliary 'être', the past participle agrees in gender and number with the subject (Elle -> -ée)."
        },
        {
            sentence: "La robe que Sophie a ___ est magnifique.",
            options: ["achetée", "acheté", "achetés", "achetées"],
            answer: "achetée",
            translation: "The dress that Sophie bought is magnificent.",
            rule: "With 'avoir', past participle agrees with preceding direct object (la robe qu'elle a achetée -> feminine singular)."
        },
        {
            sentence: "Ils ont ___ trois livres ce matin.",
            options: ["lu", "lus", "lue", "lues"],
            answer: "lu",
            translation: "They read three books this morning.",
            rule: "With 'avoir', if the direct object follows the verb (trois livres), there is NO agreement."
        },
        {
            sentence: "Ces lettres ? Je les ai ___ hier soir.",
            options: ["écrites", "écrit", "écrite", "écrits"],
            answer: "écrites",
            translation: "These letters? I wrote them yesterday evening.",
            rule: "Preceding direct object pronoun 'les' refers to 'lettres' (feminine plural -> écrites)."
        },
        {
            sentence: "Mes sœurs sont ___ en vacances en Italie.",
            options: ["parties", "parti", "partie", "partis"],
            answer: "parties",
            translation: "My sisters left on holiday to Italy.",
            rule: "Auxiliary 'être' with feminine plural subject 'mes sœurs' -> parties."
        },
        {
            sentence: "Elle s'est ___ les mains avant de manger.",
            options: ["lavé", "lavée", "lavés", "lavées"],
            answer: "lavé",
            translation: "She washed her hands before eating.",
            rule: "Reflexive verb with following direct object ('les mains') -> no participle agreement (elle s'est lavé)."
        },
        {
            sentence: "Marie s'est ___ devant le miroir.",
            options: ["regardée", "regardé", "regardés", "regardées"],
            answer: "regardée",
            translation: "Marie looked at herself in the mirror.",
            rule: "Reflexive pronoun 's'' is preceding direct object (COD = Marie -> regardée)."
        },
        {
            sentence: "Des pommes ? J'en ai beaucoup ___ ce matin.",
            options: ["mangé", "mangée", "mangés", "mangées"],
            answer: "mangé",
            translation: "Apples? I ate many of them this morning.",
            rule: "With the pronoun 'en', the past participle NEVER agrees (en ai mangé)."
        },
        {
            sentence: "Quels monuments avez-vous ___ à Paris ?",
            options: ["visités", "visité", "visitée", "visitées"],
            answer: "visités",
            translation: "Which monuments did you visit in Paris?",
            rule: "Interrogative COD 'Quels monuments' precedes 'avoir' -> masculine plural agreement (-és)."
        },
        {
            sentence: "Nous sommes ___ fatigués après ce long trajet.",
            options: ["tombés", "tombé", "tombée", "tombées"],
            answer: "tombés",
            translation: "We fell tired after this long journey.",
            rule: "Auxiliary 'être' with plural subject 'nous' -> masculine plural -s."
        }
    ];

    const SUBJUNCTIVE_ITEMS = [
        {
            sentence: "Il faut absolument que tu ___ tes devoirs avant de sortir.",
            options: ["fasses", "fais", "feras", "fait"],
            answer: "fasses",
            translation: "You must absolutely do your homework before going out.",
            rule: "'Il faut que' expresses necessity/obligation and requires the subjunctive (tu fasses)."
        },
        {
            sentence: "Je suis certain qu'il ___ à l'heure au rendez-vous.",
            options: ["sera", "soit", "fût", "sois"],
            answer: "sera",
            translation: "I am certain that he will be on time for the meeting.",
            rule: "'Être certain que' expresses certainty and takes the indicative (futur: sera)."
        },
        {
            sentence: "Bien qu'il ___ froid, nous sommes allés nous promener.",
            options: ["fasse", "fait", "fera", "faisait"],
            answer: "fasse",
            translation: "Although it was cold, we went for a walk.",
            rule: "'Bien que' (concession) always triggers the subjunctive (il fasse)."
        },
        {
            sentence: "Je ne pense pas que ce film ___ intéressant.",
            options: ["soit", "est", "sera", "serait"],
            answer: "soit",
            translation: "I don't think this film is interesting.",
            rule: "'Penser que' in the negative (doubt/denial) takes the subjunctive (ce soit)."
        },
        {
            sentence: "Je pense que ce restaurant ___ délicieux.",
            options: ["est", "soit", "sois", "fût"],
            answer: "est",
            translation: "I think that this restaurant is delicious.",
            rule: "Affirmative 'Je pense que' expresses belief/fact and takes the indicative (est)."
        },
        {
            sentence: "J'aimerais beaucoup que vous ___ avec nous ce week-end.",
            options: ["veniez", "venez", "viendrez", "viendriez"],
            answer: "veniez",
            translation: "I would really like you to come with us this weekend.",
            rule: "Verbs of wish/desire ('aimer que', 'vouloir que') require the subjunctive (vous veniez)."
        },
        {
            sentence: "J'espère que tu ___ une excellente journée demain.",
            options: ["passeras", "passes", "passes", "sois"],
            answer: "passeras",
            translation: "I hope you have a great day tomorrow.",
            rule: "'Espérer que' takes the indicative (typically future: passeras), NEVER subjunctive."
        },
        {
            sentence: "Je te préviens pour que tu ___ au courant.",
            options: ["sois", "es", "seras", "été"],
            answer: "sois",
            translation: "I am telling you so that you are aware.",
            rule: "'Pour que' (purpose) always takes the subjunctive (tu sois)."
        },
        {
            sentence: "Il est possible qu'il ___ en retard à cause des embouteillages.",
            options: ["soit", "est", "sera", "serait"],
            answer: "soit",
            translation: "It is possible that he is late because of traffic jams.",
            rule: "'Il est possible que' expresses probability/uncertainty and takes the subjunctive."
        },
        {
            sentence: "Je doute qu'elle ___ la bonne réponse.",
            options: ["sache", "sait", "saura", "saurait"],
            answer: "sache",
            translation: "I doubt she knows the right answer.",
            rule: "'Douter que' expresses doubt and triggers the subjunctive (elle sache)."
        }
    ];

    let _container = null;
    let _activeTab = 'pronouns';
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
        if (tabId === 'agreement') return AGREEMENT_ITEMS;
        if (tabId === 'subjunctive') return SUBJUNCTIVE_ITEMS;
        return PRONOUN_ITEMS;
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

        const feedbackEl = document.getElementById('fr-quiz-feedback');
        if (!feedbackEl) return;

        feedbackEl.innerHTML = `
            <div class="wk-feedback-card ${isCorrect ? 'is-correct' : 'is-wrong'}">
                <div class="wk-feedback-title">${isCorrect ? '✓ Correct !' : '✗ Pas tout à fait'}</div>
                <div class="wk-feedback-rule"><strong>Règle :</strong> ${_esc(item.rule)}</div>
                <div class="wk-feedback-trans"><em>${_esc(item.translation)}</em></div>
                <button type="button" class="btn btn-primary wk-next-btn" id="fr-next-btn">Continuer</button>
            </div>
        `;

        document.querySelectorAll('.fr-opt-btn').forEach(btn => {
            btn.disabled = true;
            if (btn.dataset.opt === item.answer) {
                btn.classList.add('is-right');
            } else if (btn.dataset.opt === selected) {
                btn.classList.add('is-wrong');
            }
        });

        const nextBtn = document.getElementById('fr-next-btn');
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

        return `
            <div class="fr-studio-settings">
                <div class="wk-settings-header">
                    <h3>${_esc(tabMeta.label)}</h3>
                    <p class="text-muted">${_esc(tabMeta.desc)}</p>
                </div>
                <div class="fr-settings-counts">
                    <p>Choisissez le nombre de questions :</p>
                    <div class="btn-group" role="group">
                        <button type="button" class="btn btn-outline-primary" data-count="5">5</button>
                        <button type="button" class="btn btn-outline-primary" data-count="10">10</button>
                        <button type="button" class="btn btn-outline-primary" data-count="${pool.length}">Tout (${pool.length})</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _renderQuiz() {
        const item = _queue[_idx];
        const options = _shuffle(item.options);
        const promptSentence = item.sentence.replace('___', '<span class="fr-blank">____</span>');

        return `
            <div class="fr-quiz-container">
                <div class="fr-quiz-progress">
                    <span>Question ${_idx + 1} / ${_queue.length}</span>
                    <span class="fr-score-counter">Score: ${_score}</span>
                </div>
                <div class="fr-quiz-sentence">${promptSentence}</div>
                <div class="fr-quiz-options">
                    ${options.map(opt => `
                        <button type="button" class="btn btn-outline-secondary fr-opt-btn" data-opt="${_esc(opt)}">
                            ${_esc(opt)}
                        </button>
                    `).join('')}
                </div>
                <div id="fr-quiz-feedback"></div>
            </div>
        `;
    }

    function _renderSummary() {
        const total = _queue.length;
        const pct = Math.round((_score / total) * 100);

        return `
            <div class="fr-quiz-summary">
                <h3>Session terminée !</h3>
                <div class="fr-score-badge ${pct >= 80 ? 'high' : (pct >= 50 ? 'med' : 'low')}">
                    ${pct}% (${_score} / ${total})
                </div>
                ${_mistakes.length > 0 ? `
                    <div class="fr-mistakes-review">
                        <h4>Révision des points à revoir :</h4>
                        <ul class="fr-mistakes-list">
                            ${_mistakes.map(m => `
                                <li>
                                    <div class="fr-mistake-sentence">${_esc(m.item.sentence.replace('___', m.item.answer))}</div>
                                    <div class="fr-mistake-rule">${_esc(m.item.rule)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                ` : `<p class="text-success font-weight-bold">Félicitations ! Aucune erreur commise.</p>`}
                <div class="fr-summary-actions">
                    <button type="button" class="btn btn-primary" id="fr-restart-btn">Recommencer</button>
                </div>
            </div>
        `;
    }

    function _attachEvents() {
        if (!_container) return;

        // Nav tabs
        _container.querySelectorAll('[data-fr-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                _activeTab = btn.dataset.frTab;
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
        _container.querySelectorAll('.fr-opt-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                _onAnswer(btn.dataset.opt);
            });
        });

        // Restart
        const restartBtn = _container.querySelector('#fr-restart-btn');
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
            <div class="sp-studio-wrap fr-grammar-studio-wrap">
                <div class="sp-studio-nav" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="sp-studio-tab ${_activeTab === tab.id ? 'active' : ''}" data-fr-tab="${tab.id}" role="tab" aria-selected="${_activeTab === tab.id}">
                            ${tab.label}
                        </button>
                    `).join('')}
                </div>
                <div class="fr-studio-body">${bodyHtml}</div>
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
        render,
        stop
    };
})();

if (typeof module !== 'undefined' && module.exports) {
    module.exports = FrGrammarStudio;
}
