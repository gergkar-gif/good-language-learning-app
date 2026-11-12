// ============================================
// SLOVAK GRAMMAR STUDIO
// ============================================
// Interactive Slovak grammar driller featuring 5 focused training tabs:
//   1. 6 slovenských pádov (Nominatív to Inštrumentál, animacy, no vocative)
//   2. Rytmický zákon a dvojhlásky (Rhythmic law, diphthongs ia, ie, iu, ô, alternations)
//   3. Vid a slovesné predpony (Imperfective vs Perfective, future tense, motion verbs)
//   4. Minulý čas a podmieňovací spôsob (Auxiliary clitics, unified plural -li, conditional)
//   5. Mäkké a tvrdé spoluhlásky a predložky (Softening d-t-n-l before e/i, vocalized prepositions)
//
// Zero emojis across all UI, badges, and exercises.

const SkGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'cases', label: '6 slovenských pádov', desc: 'Nominatív through Inštrumentál, masculine animacy (chlap vs dub/stroj), address in Nominative' },
        { id: 'rhythmic_law', label: 'Rytmický zákon a dvojhlásky', desc: 'Vowel shortening after long syllables/diphthongs (biely vs pekný), diphthongs (ô, ia, ie), kôň/koňa' },
        { id: 'aspect', label: 'Vid a slovesné predpony', desc: 'Nedokonavý vs dokonavý, future tense (budem písať vs napíšem), motion prefixes (prísť, odísť)' },
        { id: 'past_conditionals', label: 'Minulý čas a kondicionál', desc: 'Auxiliary clitics (som, si, sme, ste), unified plural in -li, conditional (by som, by si, by)' },
        { id: 'consonants_prepositions', label: 'Spoluhlásky a predložky', desc: 'Softening of d-t-n-l before e/i, vocalized prepositions (vo, so, zo, ku), Slovak-Czech contrasts' }
    ];

    const CASES_ITEMS = [
        {
            sentence: 'Ahoj ___, ako sa dnes máš?',
            options: ['Peter', 'Petře', 'Petra', 'Petrom'],
            answer: 'Peter',
            translation: 'Hi Peter, how are you today?',
            rule: 'Modern standard Slovak does not use a separate Vocative case: direct address uses the Nominative (Ahoj Peter!).'
        },
        {
            sentence: 'Dobrý deň, pán ___!',
            options: ['Kováč', 'Kováčovi', 'Kováča', 'Kováčom'],
            answer: 'Kováč',
            translation: 'Good day, Mr. Kováč!',
            rule: 'Direct polite address in Slovak uses the Nominative form: pán Kováč.'
        },
        {
            sentence: 'Vidím na ulici tvojho nového ___.',
            options: ['psa', 'pes', 'psom', 'psu'],
            answer: 'psa',
            translation: 'I see your new dog on the street.',
            rule: 'Masculine animate nouns follow the "chlap" paradigm in Accusative singular, taking the Genitive ending -a: pes -> psa.'
        },
        {
            sentence: 'Kúpil som nový drevený ___ do obývačky.',
            options: ['stôl', 'stola', 'stolom', 'stole'],
            answer: 'stôl',
            translation: 'I bought a new wooden table for the living room.',
            rule: 'Masculine inanimate nouns follow the "dub" paradigm in Accusative singular, keeping the Nominative form: stôl.'
        },
        {
            sentence: 'Idem do Bratislavy k môjmu dobrému ___.',
            options: ['kamarátovi', 'kamarát', 'kamarátom', 'kamarátu'],
            answer: 'kamarátovi',
            translation: 'I am going to Bratislava to visit my good friend.',
            rule: 'The preposition "k" governs the Dative case; animate masculine nouns take the ending -ovi: kamarátovi.'
        },
        {
            sentence: 'Hovorili sme o našom novom ___ v práci.',
            options: ['projekte', 'projekt', 'projektu', 'projektom'],
            answer: 'projekte',
            translation: 'We spoke about our new project at work.',
            rule: 'The preposition "o" governs the Locative (6. pád): inanimate masculine foreign nouns in hard consonants take -e: projekte.'
        },
        {
            sentence: 'Píšeme úlohu obyčajnou modrou ___.',
            options: ['ceruzkou', 'ceruzka', 'ceruzku', 'ceruzke'],
            answer: 'ceruzkou',
            translation: 'We are writing the assignment with an ordinary blue pencil.',
            rule: 'Means/instrument uses the Instrumental (7. pád); feminine nouns ending in -a take -ou: ceruzkou.'
        },
        {
            sentence: 'Na lúke sa páslo veľa bielych ___.',
            options: ['oviec', 'ovce', 'ovciach', 'ovcami'],
            answer: 'oviec',
            translation: 'Many white sheep were grazing on the meadow.',
            rule: 'After quantifier "veľa", feminine nouns take Genitive plural with fleeting vowel lengthening: ovca -> oviec.'
        },
        {
            sentence: 'V našom meste máme niekoľko krásnych ___.',
            options: ['námestí', 'námestie', 'námestia', 'námestiam'],
            answer: 'námestí',
            translation: 'In our town we have several beautiful squares.',
            rule: 'Neuter nouns following the "vysvedčenie" paradigm take the Genitive plural ending in -í: námestie -> námestí.'
        },
        {
            sentence: 'Cestovali sme vlakom s našimi ___.',
            options: ['deťmi', 'dieťaťom', 'deťoch', 'deti'],
            answer: 'deťmi',
            translation: 'We traveled by train with our children.',
            rule: 'The preposition "s" governs the Instrumental; plural of dieťa in the Instrumental is deťmi.'
        }
    ];

    const RHYTHMIC_LAW_ITEMS = [
        {
            sentence: 'V diaľke vidím jeden ___ dom.',
            options: ['biely', 'bielý', 'bieli', 'bielo'],
            answer: 'biely',
            translation: 'In the distance I see a white house.',
            rule: 'Rhythmic Law (Rytmický zákon): the diphthong "ie" counts as long, so the adjective ending shortens from -ý to -y: biely (not bielý).'
        },
        {
            sentence: 'Dnes je vonku naozaj ___ deň.',
            options: ['krásny', 'krásný', 'krásne', 'krásnom'],
            answer: 'krásny',
            translation: 'Today is truly a beautiful day outside.',
            rule: 'Because the root has long "á", the adjective ending is shortened to -y: krásny (in contrast to Czech krásný).'
        },
        {
            sentence: 'Každý večer rád ___ slovenské knihy.',
            options: ['čítam', 'čítám', 'čítať', 'čítajú'],
            answer: 'čítam',
            translation: 'Every evening I like to read Slovak books.',
            rule: 'Rhythmic law in verbs: long "í" in stem shortens the 1st person ending -ám to -am: čítam (Czech has čítám / čtu).'
        },
        {
            sentence: 'V stajni stojí vysoký čierny ___.',
            options: ['kôň', 'koňa', 'koňom', 'koni'],
            answer: 'kôň',
            translation: 'A tall black horse stands in the stable.',
            rule: 'The Nominative singular features the diphthong "ô": kôň; in oblique cases it alternates with "o": koňa, koňovi.'
        },
        {
            sentence: 'Položte tie knihy na veľký drevený ___.',
            options: ['stôl', 'stola', 'stolu', 'stolom'],
            answer: 'stôl',
            translation: 'Place those books on the large wooden table.',
            rule: 'Nominative/Accusative inanimate has the diphthong "ô": stôl; oblique cases alternate with "o": stola, na stole.'
        },
        {
            sentence: 'Krájam chlieb ostrým ___.',
            options: ['nožom', 'nôžom', 'nožom', 'nôž'],
            answer: 'nožom',
            translation: 'I cut bread with a sharp knife.',
            rule: 'Diphthong "ô" in nôž alternates to short "o" in inflected cases: nožom (Instrumental).'
        },
        {
            sentence: 'V zime nosím teplú ___ čiapku.',
            options: ['bielu', 'bielú', 'bielej', 'bielom'],
            answer: 'bielu',
            translation: 'In winter I wear a warm white cap.',
            rule: 'Accusative feminine adjective after diphthong "ie" shortens -ú to -u: bielu čiapku.'
        },
        {
            sentence: 'Zajtra ráno do práce určite ___.',
            options: ['zavolám', 'zavolam', 'zavolajú', 'zavolať'],
            answer: 'zavolám',
            translation: 'Tomorrow morning I will definitely call work.',
            rule: 'When the preceding syllable is short (vo-), the suffix retains its long vowel -ám: zavolám.'
        },
        {
            sentence: 'Poobede pravidelne ___ novým zákazníkom.',
            options: ['píšem', 'píšém', 'písať', 'píšeme'],
            answer: 'píšem',
            translation: 'In the afternoon I regularly write to new customers.',
            rule: 'Verbs with long root vowel "í" take short ending -em: píšem.'
        },
        {
            sentence: 'Na stole leží peceň čerstvého ___.',
            options: ['chleba', 'chlieba', 'chlebu', 'chlieb'],
            answer: 'chleba',
            translation: 'A loaf of fresh bread lies on the table.',
            rule: 'Stem diphthong "ie" in chlieb alternates with short "e" in the Genitive singular: chleba.'
        }
    ];

    const ASPECT_ITEMS = [
        {
            sentence: 'Včera som celý večer ___ túto zaujímavú knihu.',
            options: ['čítal', 'prečítal', 'prečítam', 'dočítam'],
            answer: 'čítal',
            translation: 'Yesterday I was reading this interesting book all evening.',
            rule: 'Duration over a period of time ("celý večer") requires the imperfective aspect: čítal.'
        },
        {
            sentence: 'Túto knihu som už celú ___ a môžem ti ju požičať.',
            options: ['prečítal', 'čítal', 'čítam', 'budem čítať'],
            answer: 'prečítal',
            translation: 'I have already read this book completely and can lend it to you.',
            rule: 'A completed event with a finished result ("už celú") requires the perfective aspect: prečítal.'
        },
        {
            sentence: 'Zajtra ráno určite ___ ten dôležitý list.',
            options: ['napíšem', 'budem napísať', 'písal som', 'písať'],
            answer: 'napíšem',
            translation: 'Tomorrow morning I will definitely write that important letter.',
            rule: 'Perfective verbs form their future tense using present endings: napíšem (never with budem).'
        },
        {
            sentence: 'Budúci rok sa ___ po slovensky každý deň.',
            options: ['budem učiť', 'naučím sa', 'učil som sa', 'doučím sa'],
            answer: 'budem učiť',
            translation: 'Next year I will be learning Slovak every day.',
            rule: 'Continuous or habitual future action ("každý deň") requires imperfective compound future: budem učiť.'
        },
        {
            sentence: 'Každé ráno ___ do práce pešo.',
            options: ['chodím', 'ídem', 'pôjdem', 'prišiel som'],
            answer: 'chodím',
            translation: 'Every morning I walk to work on foot.',
            rule: 'Repeated or habitual movement requires the indeterminate motion verb: chodiť (chodím).'
        },
        {
            sentence: 'Práve teraz ___ do obchodu kúpiť mlieko.',
            options: ['idem', 'chodím', 'pôjdem', 'išiel som'],
            answer: 'idem',
            translation: 'Right now I am going to the shop to buy milk.',
            rule: 'Movement in progress in one direction right now requires the determinate motion verb: ísť (idem).'
        },
        {
            sentence: 'Vlak z Košíc ___ na stanicu presne načas.',
            options: ['prišiel', 'odišiel', 'išiel', 'prešiel'],
            answer: 'prišiel',
            translation: 'The train from Košice arrived at the station on time.',
            rule: 'Prefix pri- indicates arrival / reaching a destination: prišiel (arrived).'
        },
        {
            sentence: 'Ráno sme sa rozlúčili a Peter hneď ___ domov.',
            options: ['odišiel', 'prišiel', 'došiel', 'prešiel'],
            answer: 'odišiel',
            translation: 'In the morning we said goodbye and Peter left for home right away.',
            rule: 'Prefix od- indicates departure / leaving a place: odišiel (departed).'
        },
        {
            sentence: 'Opatrne sme ___ cez rušnú cestu.',
            options: ['prešli', 'prišli', 'odišli', 'zašli'],
            answer: 'prešli',
            translation: 'We carefully crossed the busy street.',
            rule: 'Prefix pre- indicates moving across an obstacle or surface: prejsť (prešli cez cestu).'
        },
        {
            sentence: 'Môžeš mi, prosím, ___ s tou ťažkou taškou?',
            options: ['pomôcť', 'pomáhať', 'pomáham', 'pomôžem'],
            answer: 'pomôcť',
            translation: 'Can you please help me with that heavy bag?',
            rule: 'A single, completed favour after modal "môžeš" takes the perfective infinitive: pomôcť.'
        }
    ];

    const PAST_CONDITIONALS_ITEMS = [
        {
            sentence: 'Včera večer ___ unavený po dlhej ceste.',
            options: ['som bol', 'bol', 'bol som', 'som bola'],
            answer: 'som bol',
            translation: 'Yesterday evening I was tired after the long journey.',
            rule: 'Past tense auxiliary "som" occupies second position (Wackernagel law): Včera večer som bol...'
        },
        {
            sentence: 'Ty ___ včera v kine na tom novom filme?',
            options: ['si bol', 'bol', 'bol si', 'si bola'],
            answer: 'si bol',
            translation: 'Were you at the cinema yesterday watching that new movie?',
            rule: '2nd person singular past auxiliary is "si" in second position: Ty si bol...'
        },
        {
            sentence: 'Všetci študenti ___ na prednáške veľmi pozorní.',
            options: ['boli', 'byli', 'byly', 'bola'],
            answer: 'boli',
            translation: 'All the students were very attentive at the lecture.',
            rule: 'In Slovak, plural past participles are unified with -li for ALL genders (študenti boli, ženy boli, deti boli).'
        },
        {
            sentence: 'Keby som mal viac času, ___ na Slovensko častejšie.',
            options: ['cestoval by som', 'by som cestoval', 'cestoval som', 'budem cestovať'],
            answer: 'cestoval by som',
            translation: 'If I had more time, I would travel to Slovakia more often.',
            rule: 'Present conditional is formed with the l-participle + conditional auxiliary: cestoval by som.'
        },
        {
            sentence: 'Čo ___ na mojom mieste?',
            options: ['by si urobil', 'urobil si', 'by urobil', 'urobil bys'],
            answer: 'by si urobil',
            translation: 'What would you do in my place?',
            rule: '2nd person conditional auxiliary "by si" sits in the second position of the clause: Čo by si urobil?'
        },
        {
            sentence: 'Veľmi radi ___ vám pomohli s opravou auta.',
            options: ['by sme', 'bychom', 'sme', 'by'],
            answer: 'by sme',
            translation: 'We would very gladly help you with fixing the car.',
            rule: '1st person plural conditional in Slovak is "by sme" (Czech has bychom).'
        },
        {
            sentence: 'Kde ___ minulý týždeň na dovolenke?',
            options: ['ste boli', 'boli ste', 'ste bol', 'boli jste'],
            answer: 'ste boli',
            translation: 'Where were you last week on vacation?',
            rule: '2nd person plural past auxiliary is "ste" with unified plural participle "boli": ste boli.'
        },
        {
            sentence: 'Prišiel som, ___ ti zablahoželal k narodeninám.',
            options: ['aby som', 'abych', 'že som', 'keby som'],
            answer: 'aby som',
            translation: 'I came in order to congratulate you on your birthday.',
            rule: 'Purpose clause with conditional conjunction: aby som (in contrast to Czech abych).'
        },
        {
            sentence: 'Keby ___ viac peňazí, kúpili by sme si nový dom.',
            options: ['sme mali', 'mali by sme', 'sme mali by', 'mali sme'],
            answer: 'sme mali',
            translation: 'If we had more money, we would buy a new house.',
            rule: 'In conditional clauses after "keby", the clitic "sme" follows keby: keby sme mali...'
        },
        {
            sentence: 'Už ___ videl Bratislavský hrad?',
            options: ['si', 'jsi', 'som', 'ste'],
            answer: 'si',
            translation: 'Have you already seen Bratislava Castle?',
            rule: '2nd person singular past auxiliary in Slovak is "si" (Czech has jsi).'
        }
    ];

    const CONSONANTS_PREPOSITIONS_ITEMS = [
        {
            sentence: 'Malé ___ sa hrali v parku na ihrisku.',
            options: ['deti', 'dety', 'ďeti', 'ďeťi'],
            answer: 'deti',
            translation: 'Small children were playing in the park on the playground.',
            rule: 'Consonants d, t, n, l soften before e, i without writing carons: "deti" is pronounced [ďeťi].'
        },
        {
            sentence: 'Cestujeme na výlet ___ vlaku.',
            options: ['vo', 'v', 've', 'do'],
            answer: 'vo',
            translation: 'We are traveling on a trip by train.',
            rule: 'Preposition "v" vocalizes to "vo" before consonant clusters beginning with v/f: vo vlaku.'
        },
        {
            sentence: 'Išiel som do kina ___ sestrou.',
            options: ['so', 's', 'se', 'zo'],
            answer: 'so',
            translation: 'I went to the cinema with my sister.',
            rule: 'Preposition "s" vocalizes to "so" before s, z, š, ž clusters: so sestrou.'
        },
        {
            sentence: 'Peter zobral knihu ___ stola.',
            options: ['zo', 'z', 'ze', 'od'],
            answer: 'zo',
            translation: 'Peter took the book from the table.',
            rule: 'Preposition "z" vocalizes to "zo" before s, z, š, ž clusters: zo stola.'
        },
        {
            sentence: 'Poď rýchlo ___ mne, chcem ti niečo ukázať.',
            options: ['ku', 'k', 'ke', 'do'],
            answer: 'ku',
            translation: 'Come quickly to me, I want to show you something.',
            rule: 'Preposition "k" vocalizes to "ku" before k, g and m- clusters: ku mne.'
        },
        {
            sentence: 'Na Slovensku sa bežne ___ po slovensky.',
            options: ['hovorí', 'mluví', 'priepovedá', 'vypráva'],
            answer: 'hovorí',
            translation: 'In Slovakia, people commonly speak Slovak.',
            rule: 'Standard Slovak uses "hovoriť" (to speak), whereas Czech uses "mluvit".'
        },
        {
            sentence: 'Celé popoludnie som v lese zbieral sladké ___.',
            options: ['čučoriedky', 'borůvky', 'jahody', 'maliny'],
            answer: 'čučoriedky',
            translation: 'All afternoon I was picking sweet blueberries in the forest.',
            rule: 'Slovak word for blueberry is "čučoriedka" (in Czech it is "borůvka").'
        },
        {
            sentence: 'Na strome sedí malá mačka a na streche stojí biely ___.',
            options: ['bocian', 'čáp', 'vták', 'orol'],
            answer: 'bocian',
            translation: 'A small cat sits on the tree and a white stork stands on the roof.',
            rule: 'Slovak word for stork is "bocian" (in Czech it is "čáp").'
        },
        {
            sentence: 'Už pol hodiny ___ svoje kľúče od bytu.',
            options: ['hľadám', 'hledám', 'hľadať', 'hľadajú'],
            answer: 'hľadám',
            translation: 'For half an hour already I have been searching for my apartment keys.',
            rule: 'Slovak verb has soft l with caron and long á: hľadám (Czech has hledám).'
        },
        {
            sentence: 'Dnes sme pili čerstvú pomarančovú ___.',
            options: ['šťavu', 'džús', 'limonádu', 'vodu'],
            answer: 'šťavu',
            translation: 'Today we drank fresh orange juice.',
            rule: 'Standard Slovak term for fruit juice is "šťava" (pomarančová šťava).'
        }
    ];

    let _activeTab = 'cases';
    let _currentIndex = 0;
    let _score = 0;
    let _answered = false;
    let _container = null;

    function _poolFor(tabId) {
        switch (tabId) {
            case 'cases': return CASES_ITEMS;
            case 'rhythmic_law': return RHYTHMIC_LAW_ITEMS;
            case 'aspect': return ASPECT_ITEMS;
            case 'past_conditionals': return PAST_CONDITIONALS_ITEMS;
            case 'consonants_prepositions': return CONSONANTS_PREPOSITIONS_ITEMS;
            default: return CASES_ITEMS;
        }
    }

    function render(containerId) {
        const root = document.getElementById(containerId);
        if (!root) return;
        _container = root;
        _renderShell();
    }

    function _renderShell() {
        if (!_container) return;

        let navHtml = '<div class="grammar-tabs-nav" role="tablist">';
        TABS.forEach(t => {
            const activeClass = t.id === _activeTab ? ' is-active' : '';
            navHtml += `<button class="grammar-tab-btn${activeClass}" role="tab" data-tab="${t.id}">${t.label}</button>`;
        });
        navHtml += '</div>';

        const curTabMeta = TABS.find(t => t.id === _activeTab) || TABS[0];
        const descHtml = `<div class="grammar-tab-desc"><p>${curTabMeta.desc}</p></div>`;

        _container.innerHTML = `
            <div class="grammar-studio-wrapper slovak-theme">
                <div class="grammar-studio-header">
                    <h2>Slovak Grammar Studio</h2>
                    <p class="subtitle">Majstrovstvo slovenskej gramatiky · 5 špecializovaných modulov</p>
                </div>
                ${navHtml}
                ${descHtml}
                <div id="sk-grammar-card-mount" class="grammar-card-mount"></div>
            </div>
        `;

        _container.querySelectorAll('.grammar-tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const targetTab = e.currentTarget.getAttribute('data-tab');
                if (targetTab !== _activeTab) {
                    _activeTab = targetTab;
                    _currentIndex = 0;
                    _score = 0;
                    _answered = false;
                    _renderShell();
                }
            });
        });

        _renderCard();
    }

    function _renderCard() {
        const mount = document.getElementById('sk-grammar-card-mount');
        if (!mount) return;

        const pool = _poolFor(_activeTab);
        if (_currentIndex >= pool.length) {
            mount.innerHTML = `
                <div class="grammar-completion-card">
                    <h3>Výborne! Modul dokončený!</h3>
                    <p class="final-score">Dosiahnuté skóre: <strong>${_score}</strong> z <strong>${pool.length}</strong></p>
                    <button id="sk-grammar-restart-btn" class="action-btn">Zopakovať modul</button>
                </div>
            `;
            document.getElementById('sk-grammar-restart-btn').addEventListener('click', () => {
                _currentIndex = 0;
                _score = 0;
                _answered = false;
                _renderCard();
            });
            return;
        }

        const item = pool[_currentIndex];
        const displaySentence = item.sentence.replace('___', '<span class="gap-placeholder">______</span>');

        let optionsHtml = '<div class="grammar-options-grid">';
        item.options.forEach((opt, idx) => {
            optionsHtml += `<button class="grammar-opt-btn" data-opt="${opt}">${opt}</button>`;
        });
        optionsHtml += '</div>';

        mount.innerHTML = `
            <div class="grammar-exercise-card">
                <div class="card-progress">Otázka ${_currentIndex + 1} z ${pool.length} · Skóre: ${_score}</div>
                <div class="sentence-prompt">${displaySentence}</div>
                <div class="sentence-translation">${item.translation}</div>
                ${optionsHtml}
                <div id="sk-grammar-feedback" class="grammar-feedback" style="display: none;"></div>
                <div class="card-actions" style="margin-top: 15px; display: none;" id="sk-grammar-next-wrap">
                    <button id="sk-grammar-next-btn" class="action-btn">Ďalej</button>
                </div>
            </div>
        `;

        _answered = false;
        mount.querySelectorAll('.grammar-opt-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                if (_answered) return;
                _answered = true;
                const picked = e.currentTarget.getAttribute('data-opt');
                const isCorrect = picked === item.answer;
                if (isCorrect) _score++;

                e.currentTarget.classList.add(isCorrect ? 'is-correct' : 'is-wrong');

                if (!isCorrect) {
                    mount.querySelectorAll('.grammar-opt-btn').forEach(b => {
                        if (b.getAttribute('data-opt') === item.answer) {
                            b.classList.add('is-correct');
                        }
                    });
                }

                const fb = document.getElementById('sk-grammar-feedback');
                fb.style.display = 'block';
                fb.className = `grammar-feedback ${isCorrect ? 'is-success' : 'is-error'}`;
                fb.innerHTML = `
                    <div class="feedback-status">${isCorrect ? 'Správne!' : 'Nesprávne'}</div>
                    <div class="feedback-rule">${item.rule}</div>
                `;

                document.getElementById('sk-grammar-next-wrap').style.display = 'block';
            });
        });

        const nextBtn = document.getElementById('sk-grammar-next-btn');
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                _currentIndex++;
                _renderCard();
            });
        }
    }

    function stop() {
        _container = null;
    }

    return {
        TABS: TABS,
        render: render,
        stop: stop,
        _poolFor: _poolFor
    };
})();

// Export globally and for CommonJS tests
if (typeof window !== 'undefined') {
    window.SkGrammarStudio = SkGrammarStudio;
}
if (typeof global !== 'undefined') {
    global.SkGrammarStudio = SkGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SkGrammarStudio;
}
