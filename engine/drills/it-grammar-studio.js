// ============================================
// ITALIAN GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated Italian driller addressing the 5 core contrastive bottlenecks:
// 1. Preposizioni Articolate & Semplici (di, a, da, in, su + definite articles vs bare prepositions)
// 2. Essere vs Avere in Passato Prossimo & Participle Agreement (motion/state/reflexive vs transitive)
// 3. Pronomi Diretti, Indiretti e Combinati (mi/ti/lo/la/gli/le/ci/vi/ne & glielo/me la/ce ne)
// 4. Particelle Ci vs Ne (locative, existential, and idiomatic ci vs partitive and topic ne)
// 5. Congiuntivo vs Indicativo Triggers (opinion, doubt, hope, necessity, and conjunctions)

const ItGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'prepositions', label: 'Preposizioni', desc: 'Articulated prepositions (del, al, dal, nel, sul) and simple prepositional contrasts' },
        { id: 'auxiliary', label: 'Essere vs Avere', desc: 'Passato prossimo auxiliary selection, transitive/intransitive shifts, and agreement' },
        { id: 'pronouns', label: 'Pronomi & Combinati', desc: 'Direct, indirect, and combined object pronouns (glielo, me la, ce ne) with agreement' },
        { id: 'ci_ne', label: 'Ci vs Ne', desc: 'Locative, existential, and idiomatic ci vs partitive and topic ne' },
        { id: 'subjunctive', label: 'Congiuntivo', desc: 'Subjunctive vs indicative after opinion, doubt, hope, necessity, and conjunctions' }
    ];

    const PREPOSITION_ITEMS = [
        {
            sentence: "Vado ___ stazione a prendere un amico che arriva da Torino.",
            options: ["alla", "al", "dalla", "nella"],
            answer: "alla",
            translation: "I am going to the station to pick up a friend arriving from Turin.",
            rule: "'Stazione' is feminine singular beginning with a consonant: a + la = alla."
        },
        {
            sentence: "Il libro di storia è ___ tavolo in salotto.",
            options: ["sul", "nel", "al", "del"],
            answer: "sul",
            translation: "The history book is on the table in the living room.",
            rule: "Location on a surface: su + il tavolo = sul."
        },
        {
            sentence: "La camera da letto principale si trova ___ secondo piano.",
            options: ["al", "nel", "sul", "dal"],
            answer: "al",
            translation: "The main bedroom is located on the second floor.",
            rule: "Building floors take 'a': a + il secondo piano = al secondo piano."
        },
        {
            sentence: "Metto sempre un cucchiaino di zucchero ___ caffè.",
            options: ["nel", "sul", "al", "del"],
            answer: "nel",
            translation: "I always put a teaspoon of sugar in the coffee.",
            rule: "Inside a container or liquid: in + il caffè = nel."
        },
        {
            sentence: "Questo è il cane ___ zia di Marco.",
            options: ["della", "dalla", "alla", "nella"],
            answer: "della",
            translation: "This is the dog of Marco's aunt.",
            rule: "Possession with a feminine singular noun: di + la zia = della."
        },
        {
            sentence: "Torno adesso ___ ufficio del direttore.",
            options: ["dall'", "dallo", "dal", "dell'"],
            answer: "dall'",
            translation: "I am returning right now from the director's office.",
            rule: "Origin from a singular noun starting with a vowel: da + l'ufficio = dall'."
        },
        {
            sentence: "Le chiavi di casa sono ___ zaino di Luca.",
            options: ["nello", "nel", "sullo", "dallo"],
            answer: "nello",
            translation: "The house keys are in Luca's backpack.",
            rule: "Masculine nouns beginning with z- or s+consonant take 'lo': in + lo zaino = nello zaino."
        },
        {
            sentence: "Telefoniamo ogni domenica ___ nostri nonni.",
            options: ["ai", "agli", "dei", "dai"],
            answer: "ai",
            translation: "We call our grandparents every Sunday.",
            rule: "Indirect object to a regular masculine plural noun: a + i nostri nonni = ai."
        },
        {
            sentence: "Il professore distribuisce i fogli ___ studenti.",
            options: ["agli", "ai", "degli", "dagli"],
            answer: "agli",
            translation: "The professor distributes the sheets to the students.",
            rule: "Before masculine plural nouns starting with s+consonant, z-, or a vowel, use 'gli': a + gli studenti = agli."
        },
        {
            sentence: "Parliamo spesso ___ nostre vacanze in Sicilia.",
            options: ["delle", "dalle", "alle", "nelle"],
            answer: "delle",
            translation: "We often talk about our holidays in Sicily.",
            rule: "Topic with 'parlare di': di + le nostre vacanze = delle."
        },
        {
            sentence: "Domani pomeriggio devo andare ___ dentista per un controllo.",
            options: ["dal", "al", "nel", "del"],
            answer: "dal",
            translation: "Tomorrow afternoon I have to go to the dentist for a check-up.",
            rule: "Going to a person or professional's practice/home takes 'da' (da + il dentista = dal dentista), never 'a'."
        },
        {
            sentence: "Quest'estate andremo in vacanza ___ Stati Uniti per tre settimane.",
            options: ["negli", "nei", "agli", "in"],
            answer: "negli",
            translation: "This summer we will go on holiday to the United States for three weeks.",
            rule: "Plural country names require the articulated preposition: in + gli Stati Uniti = negli Stati Uniti."
        },
        {
            sentence: "Abito ___ Italia da cinque anni, precisamente ___ Firenze.",
            options: ["in / a", "a / in", "nell' / a", "in / in"],
            answer: "in / a",
            translation: "I have lived in Italy for five years, specifically in Florence.",
            rule: "Unmodified countries and regions take 'in' ('in Italia'); cities and towns take 'a' ('a Firenze')."
        },
        {
            sentence: "Preferisco viaggiare ___ treno piuttosto che ___ aereo.",
            options: ["in / in", "con il / a", "al / all'", "su / su"],
            answer: "in / in",
            translation: "I prefer travelling by train rather than by plane.",
            rule: "General means of transport without an article take simple 'in' ('in treno', 'in macchina', 'in aereo')."
        },
        {
            sentence: "Stasera mangiamo una pizza ___ mio fratello.",
            options: ["da", "a", "in", "da il"],
            answer: "da",
            translation: "Tonight we are eating a pizza at my brother's place.",
            rule: "'At someone's home' is expressed with 'da' + person; singular family members with a possessive take no article ('da mio fratello')."
        },
        {
            sentence: "Questo tavolo antico è fatto ___ legno massiccio.",
            options: ["di", "da", "in", "del"],
            answer: "di",
            translation: "This antique table is made of solid wood.",
            rule: "Material composition is expressed with simple 'di' ('di legno', 'di vetro', 'd'oro')."
        },
        {
            sentence: "Ho comprato una camicia ___ righe blu e bianche.",
            options: ["a", "di", "con", "in"],
            answer: "a",
            translation: "I bought a shirt with blue and white stripes.",
            rule: "Patterns and styles on clothing or food take 'a' ('a righe', 'a quadretti', 'a fiori')."
        },
        {
            sentence: "Non ho niente ___ bere in frigorifero, dobbiamo fare la spesa.",
            options: ["da", "di", "a", "per"],
            answer: "da",
            translation: "I have nothing to drink in the fridge; we need to go grocery shopping.",
            rule: "After 'qualcosa / niente / molto / poco', purpose before an infinitive takes 'da' ('niente da bere', 'qualcosa da mangiare')."
        },
        {
            sentence: "Oggi c'è qualcosa ___ nuovo in ufficio?",
            options: ["di", "da", "a", "del"],
            answer: "di",
            translation: "Is there anything new at the office today?",
            rule: "After 'qualcosa / niente / nulla', a masculine singular adjective is introduced by 'di' ('qualcosa di nuovo', 'niente di speciale')."
        },
        {
            sentence: "Gli occhiali da sole sono rimasti ___ sedia in giardino.",
            options: ["sulla", "nella", "alla", "dalla"],
            answer: "sulla",
            translation: "The sunglasses were left on the chair in the garden.",
            rule: "su + la sedia = sulla sedia."
        }
    ];

    const AUXILIARY_ITEMS = [
        {
            sentence: "Ieri sera Francesca ___ a casa prima di mezzanotte.",
            options: ["è tornata", "ha tornato", "è tornato", "ha tornata"],
            answer: "è tornata",
            translation: "Yesterday evening Francesca returned home before midnight.",
            rule: "'Tornare' is an intransitive verb of directed motion and takes 'essere'; the participle agrees with Francesca ('è tornata')."
        },
        {
            sentence: "I ragazzi ___ una pizza margherita in centro.",
            options: ["hanno mangiato", "sono mangiati", "hanno mangiati", "sono mangiato"],
            answer: "hanno mangiato",
            translation: "The boys ate a margherita pizza downtown.",
            rule: "Transitive verbs take 'avere'; when the direct object follows, the past participle stays in '-o' ('mangiato')."
        },
        {
            sentence: "Noi (ragazze) ___ a Roma per tutto il fine settimana.",
            options: ["siamo rimaste", "abbiamo rimasto", "siamo rimasti", "abbiamo rimaste"],
            answer: "siamo rimaste",
            translation: "We (girls) stayed in Rome for the whole weekend.",
            rule: "'Rimanere / restare / stare' take 'essere', and the past participle agrees with the feminine plural subject ('siamo rimaste')."
        },
        {
            sentence: "A che ora ___ stamattina, Marco e Matteo?",
            options: ["vi siete svegliati", "avete svegliato", "vi siete svegliato", "avete svegliati"],
            answer: "vi siete svegliati",
            translation: "What time did you wake up this morning, Marco and Matteo?",
            rule: "All reflexive verbs ('svegliarsi', 'alzarsi', 'vestirsi') take 'essere' in compound tenses with subject agreement."
        },
        {
            sentence: "I bambini ___ tutta la notte senza svegliarsi.",
            options: ["hanno dormito", "sono dormiti", "hanno dormiti", "sono dormito"],
            answer: "hanno dormito",
            translation: "The children slept all night without waking up.",
            rule: "Intransitive bodily/activity verbs like 'dormire', 'ridere', 'piangere', and 'viaggiare' take 'avere' ('hanno dormito')."
        },
        {
            sentence: "Abbiamo ___ per tre ore lungo la costa toscana.",
            options: ["camminato", "camminati", "siamo camminati", "camminate"],
            answer: "camminato",
            translation: "We walked for three hours along the Tuscan coast.",
            rule: "Non-directional movement verbs expressing manner of motion ('camminare', 'passeggiare', 'nuotare', 'ballare') take 'avere'."
        },
        {
            sentence: "La lezione di letteratura ___ alle nove in punto.",
            options: ["è cominciata", "ha cominciato", "è cominciato", "ha cominciata"],
            answer: "è cominciata",
            translation: "The literature lesson began at nine sharp.",
            rule: "When 'cominciare / iniziare / finire' are used intransitively (no direct object), they take 'essere' with subject agreement."
        },
        {
            sentence: "Il professore ___ la lezione con una domanda interessante.",
            options: ["ha cominciato", "è cominciato", "ha cominciata", "è cominciata"],
            answer: "ha cominciato",
            translation: "The professor began the lesson with an interesting question.",
            rule: "When 'cominciare / finire' have a direct object ('la lezione'), they are transitive and take 'avere'."
        },
        {
            sentence: "Maria ___ le scale di corsa perché era in ritardo.",
            options: ["ha salito", "è salita", "ha salita", "è salito"],
            answer: "ha salito",
            translation: "Maria went up the stairs at a run because she was late.",
            rule: "'Salire' and 'scendere' take 'avere' when used transitively with a direct object ('le scale'), and 'essere' when intransitive ('è salita sull'autobus')."
        },
        {
            sentence: "Appena è arrivato il treno, tutti i passeggeri ___.",
            options: ["sono saliti", "hanno salito", "sono salito", "hanno saliti"],
            answer: "sono saliti",
            translation: "As soon as the train arrived, all the passengers boarded.",
            rule: "Used intransitively without a direct object, 'salire' and 'scendere' take 'essere' ('sono saliti')."
        },
        {
            sentence: "Ti ___ i dolci che ho preparato ieri sera?",
            options: ["sono piaciuti", "hanno piaciuto", "è piaciuto", "sono piaciuto"],
            answer: "sono piaciuti",
            translation: "Did you like the pastries that I made last night?",
            rule: "'Piacere', 'sembrare', 'succedere', 'mancare', and 'bastare' take 'essere' and agree with the grammatical subject ('i dolci' -> 'sono piaciuti')."
        },
        {
            sentence: "Quanto ___ queste scarpe di pelle?",
            options: ["sono costate", "hanno costato", "sono costati", "è costata"],
            answer: "sono costate",
            translation: "How much did these leather shoes cost?",
            rule: "'Costare' and 'durare' standardly take 'essere' and agree with the subject ('queste scarpe' -> 'sono costate')."
        },
        {
            sentence: "Non ___ uscire ieri perché pioveva fortissimo.",
            options: ["sono potuto", "ho potuto", "sono potuta", "ho potuta"],
            answer: "sono potuto",
            translation: "I wasn't able to go out yesterday because it was raining heavily.",
            rule: "Modal verbs ('potere', 'dovere', 'volere') take the auxiliary required by the following infinitive ('uscire' takes 'essere' -> 'sono potuto uscire')."
        },
        {
            sentence: "Lucia non ___ finire il lavoro prima di cena.",
            options: ["ha potuto", "è potuta", "ha potuta", "è potuto"],
            answer: "ha potuto",
            translation: "Lucia was not able to finish the work before dinner.",
            rule: "Because the infinitive 'finire (il lavoro)' is transitive and takes 'avere', the modal 'potere' takes 'avere' ('ha potuto finire')."
        },
        {
            sentence: "Durante l'inverno scorso ___ moltissimo sulle Alpi.",
            options: ["è nevicato", "ha nevicato", "sono nevicati", "è nevicata"],
            answer: "è nevicato",
            translation: "During last winter it snowed a great deal in the Alps.",
            rule: "Impersonal weather verbs ('piovere', 'nevicare') take 'essere' (or 'avere' in modern usage) with an invariable masculine singular participle ('-o')."
        },
        {
            sentence: "Elena ___ le mani prima di sedersi a tavola.",
            options: ["si è lavata", "ha lavato", "si ha lavato", "si è lavate"],
            answer: "si è lavata",
            translation: "Elena washed her hands before sitting down at the table.",
            rule: "Unlike French, Italian reflexive verbs with a body-part object STILL take 'essere' and agree with the subject ('Elena si è lavata le mani')."
        },
        {
            sentence: "I prezzi degli affitti in centro ___ molto quest'anno.",
            options: ["sono aumentati", "hanno aumentato", "sono aumentato", "hanno aumentati"],
            answer: "sono aumentati",
            translation: "Rental prices downtown have increased a lot this year.",
            rule: "'Aumentare', 'diminuire', 'cambiare', and 'migliorare' take 'essere' when the subject changes state intransitively."
        },
        {
            sentence: "Il proprietario ___ l'affitto del nostro appartamento.",
            options: ["ha aumentato", "è aumentato", "ha aumentata", "è aumentati"],
            answer: "ha aumentato",
            translation: "The landlord increased the rent of our apartment.",
            rule: "When 'aumentare / cambiare / migliorare' take a direct object ('l'affitto'), they are transitive and take 'avere'."
        },
        {
            sentence: "Che cosa ___ ieri alla riunione di condominio?",
            options: ["è successo", "ha successo", "è successa", "ha succeduto"],
            answer: "è successo",
            translation: "What happened yesterday at the building meeting?",
            rule: "'Succedere' (to happen) takes 'essere' and its irregular past participle is 'successo' ('è successo')."
        },
        {
            sentence: "Mio nonno ___ in un piccolo paese vicino a Bologna.",
            options: ["è nato", "ha nato", "è nata", "ha nascosto"],
            answer: "è nato",
            translation: "My grandfather was born in a small town near Bologna.",
            rule: "'Nascere', 'crescere', 'diventare', and 'morire' are change-of-state verbs and always take 'essere' ('è nato')."
        }
    ];

    const PRONOUN_ITEMS = [
        {
            sentence: "Hai visto l'ultimo film di Sorrentino? — Sì, ___ visto ieri sera.",
            options: ["l'ho", "lo ho", "gli ho", "li ho"],
            answer: "l'ho",
            translation: "Did you see Sorrentino's latest film? — Yes, I saw it yesterday evening.",
            rule: "Singular direct object pronouns 'lo' and 'la' elide to 'l'' before forms of 'avere' starting with h- or a vowel ('l'ho visto')."
        },
        {
            sentence: "Hai comprato le mele al mercato? — Sì, ___ comprate stamattina.",
            options: ["le ho", "l'ho", "li ho", "la ho"],
            answer: "le ho",
            translation: "Did you buy the apples at the market? — Yes, I bought them this morning.",
            rule: "Plural direct object pronouns 'li' and 'le' NEVER elide before 'ho/hai/ha', and the past participle must agree ('le ho comprate')."
        },
        {
            sentence: "Hai parlato con Maria? — Sì, ___ telefonato dieci minuti fa.",
            options: ["le ho", "l'ho", "gli ho", "la ho"],
            answer: "le ho",
            translation: "Did you speak with Maria? — Yes, I phoned her ten minutes ago.",
            rule: "Indirect object 'to her' is 'le' ('telefonare a qualcuno'); indirect object pronouns NEVER trigger past participle agreement ('le ho telefonato')."
        },
        {
            sentence: "Hai restituito il dizionario a Marco? — Sì, ___ restituito ieri.",
            options: ["gliel'ho", "lo gli ho", "gli l'ho", "me l'ho"],
            answer: "gliel'ho",
            translation: "Did you return the dictionary to Marco? — Yes, I returned it to him yesterday.",
            rule: "Indirect 'gli/le' + direct 'lo' fuses into a single word 'glielo', which elides before 'ho' -> 'gliel'ho restituito'."
        },
        {
            sentence: "Mi presti la tua bicicletta? — Certo, ___ presto volentieri.",
            options: ["te la", "la ti", "me la", "te lo"],
            answer: "te la",
            translation: "Will you lend me your bicycle? — Of course, I'll gladly lend it to you.",
            rule: "Indirect pronouns 'mi, ti, ci, vi, si' change their vowel to '-e' ('me, te, ce, ve, se') before 'lo, la, li, le, ne'."
        },
        {
            sentence: "Hai mandato i contratti agli avvocati? — Sì, ___ mandati stamattina.",
            options: ["glieli ho", "li loro ho", "li gli ho", "glielo ho"],
            answer: "glieli ho",
            translation: "Did you send the contracts to the lawyers? — Yes, I sent them to them this morning.",
            rule: "In combined pronouns, 'gli-' serves for 'to him', 'to her', and 'to them': gli + li = 'glieli', with participle agreement ('mandati')."
        },
        {
            sentence: "Porti queste chiavi a tua sorella? — Va bene, ___ porto subito.",
            options: ["gliele", "le le", "le gli", "glielo"],
            answer: "gliele",
            translation: "Are you taking these keys to your sister? — Okay, I'll take them to her right away.",
            rule: "Indirect 'le' (to her) becomes 'glie-' before direct 'le' (queste chiavi) -> 'gliele porto'."
        },
        {
            sentence: "Chi ti ha regalato quell'orologio? — ___ ha regalato mio zio.",
            options: ["Me l'ha", "Te l'ha", "Mi l'ha", "Se l'ha"],
            answer: "Me l'ha",
            translation: "Who gave you that watch? — My uncle gave it to me.",
            rule: "mi (to me) + lo (it) -> 'me lo', which elides before 'ha' -> 'Me l'ha regalato'."
        },
        {
            sentence: "Hai salutato i tuoi cugini? — Sì, ___ salutati prima di partire.",
            options: ["li ho", "l'ho", "le ho", "gli ho"],
            answer: "li ho",
            translation: "Did you say goodbye to your cousins? — Yes, I greeted them before leaving.",
            rule: "'Salutare' takes a direct object in Italian; masculine plural 'li' triggers agreement ('li ho salutati')."
        },
        {
            sentence: "Ci puoi spiegare questa regola? — Sì, ___ spiego subito.",
            options: ["ve la", "ce la", "vi la", "ve lo"],
            answer: "ve la",
            translation: "Can you explain this rule to us? — Yes, I will explain it to you right away.",
            rule: "Indirect 'vi' (to you all) becomes 've' before feminine singular 'la' ('la regola'): 've la spiego'."
        },
        {
            sentence: "Signora Rossi, ___ posso fare una domanda?",
            options: ["Le", "La", "Gli", "Vi"],
            answer: "Le",
            translation: "Mrs Rossi, may I ask you a question?",
            rule: "Formal singular 'you' takes 3rd-person feminine pronouns regardless of the addressee's gender: indirect 'Le' (to you), direct 'La' (you)."
        },
        {
            sentence: "Dottor Bianchi, ___ ringrazio molto per la Sua disponibilità.",
            options: ["La", "Le", "Lo", "Gli"],
            answer: "La",
            translation: "Dr Bianchi, I thank you very much for your availability.",
            rule: "'Ringraziare' takes a direct object; formal 'you' (even addressing a man) uses direct object 'La' ('La ringrazio')."
        },
        {
            sentence: "Quante fette di torta hai portato ai bambini? — ___ portate quattro.",
            options: ["Gliene ho", "Gliele ho", "Ne gli ho", "Ce ne ho"],
            answer: "Gliene ho",
            translation: "How many slices of cake did you bring to the children? — I brought four of them to them.",
            rule: "gli (to them) + ne (of them, with number 'quattro') fuses into 'gliene', with feminine plural participle agreement ('portate')."
        },
        {
            sentence: "Se hai freddo, ___ la giacca pesante!",
            options: ["mettiti", "ti metti", "metti ti", "mettitela"],
            answer: "mettiti",
            translation: "If you are cold, put on your heavy jacket!",
            rule: "In the informal affirmative imperative ('tu', 'noi', 'voi'), clitic pronouns attach to the end of the verb ('mettiti')."
        },
        {
            sentence: "Questo segreto è importante: ___ a nessuno!",
            options: ["non dirlo", "non lo dici", "non dillo", "dirlo non"],
            answer: "non dirlo",
            translation: "This secret is important: don't tell it to anyone!",
            rule: "The negative 'tu' imperative is formed with 'non + infinitive'; pronouns either attach to the infinitive ('non dirlo') or precede it ('non lo dire')."
        },
        {
            sentence: "Dimmi la verità: ___ subito!",
            options: ["dimmela", "dimmi la", "me la di'", "dilmela"],
            answer: "dimmela",
            translation: "Tell me the truth: tell it to me right away!",
            rule: "Short monosyllabic imperatives ('da'', 'di'', 'fa'', 'sta'', 'va'') double the initial consonant of attached pronouns (except 'gli'): di' + me + la = 'dimmela'."
        },
        {
            sentence: "Se vedi Luca, ___ questo pacco da parte mia.",
            options: ["dagli", "daggli", "gli dai", "dallo"],
            answer: "dagli",
            translation: "If you see Luca, give him this package from me.",
            rule: "Unlike 'dammi / dille / dacci', the pronoun 'gli' NEVER doubles its initial consonant after 'da'' -> 'dagli'."
        },
        {
            sentence: "Hai comprato il regalo per Giulia? — Non ancora, ma voglio ___ oggi.",
            options: ["comprarglielo", "lo comprarle", "comprarlelo", "comprarlo gli"],
            answer: "comprarglielo",
            translation: "Did you buy the gift for Giulia? — Not yet, but I want to buy it for her today.",
            rule: "With modal + infinitive, combined pronouns attach to the infinitive without its final '-e': comprare + glielo = 'comprarglielo'."
        },
        {
            sentence: "Ti serve ancora questo coltello? — No, non ___ serve più.",
            options: ["mi", "me", "ti", "lo"],
            answer: "mi",
            translation: "Do you still need this knife? — No, I don't need it anymore.",
            rule: "'Servire' (to be needed by) works like 'piacere' with an indirect object pronoun ('mi serve', not 'me' when no second pronoun follows)."
        },
        {
            sentence: "Vi ricordate di quella vacanza? — Sì, ___ ricordiamo benissimo.",
            options: ["ce ne", "ci ne", "ve ne", "ce la"],
            answer: "ce ne",
            translation: "Do you remember that holiday? — Yes, we remember it very well.",
            rule: "'Ricordarsi di' combines reflexive 'ci' + 'ne' into 'ce ne' ('ce ne ricordiamo')."
        }
    ];

    const CI_NE_ITEMS = [
        {
            sentence: "Vai spesso a Firenze per lavoro? — Sì, ___ vado quasi ogni settimana.",
            options: ["ci", "ne", "lo", "li"],
            answer: "ci",
            translation: "Do you often go to Florence for work? — Yes, I go there almost every week.",
            rule: "'Ci' is the locative pronoun replacing a destination or location introduced by 'a', 'in', or 'su' ('a Firenze' -> 'ci vado')."
        },
        {
            sentence: "Quanti caffè bevi al giorno? — Di solito ___ bevo due.",
            options: ["ne", "ci", "li", "lo"],
            answer: "ne",
            translation: "How many coffees do you drink a day? — Usually I drink two of them.",
            rule: "'Ne' is the partitive pronoun required whenever a noun is omitted after a number or quantity ('due [di caffè]' -> 'ne bevo due')."
        },
        {
            sentence: "Che cosa sai di questo progetto? — Purtroppo non ___ so ancora niente.",
            options: ["ne", "ci", "lo", "la"],
            answer: "ne",
            translation: "What do you know about this project? — Unfortunately I don't know anything about it yet.",
            rule: "'Ne' replaces prepositional phrases introduced by 'di' ('sapere di / parlare di qualcosa' -> 'non ne so niente')."
        },
        {
            sentence: "Credi all'oroscopo? — No, non ___ credo affatto.",
            options: ["ci", "ne", "lo", "gli"],
            answer: "ci",
            translation: "Do you believe in horoscopes? — No, I don't believe in them at all.",
            rule: "'Ci' replaces inanimate complements introduced by 'a' ('credere a', 'pensare a', 'tenere a', 'abituarsi a')."
        },
        {
            sentence: "Quante valigie avete portato? — ___ portate soltanto due.",
            options: ["Ne abbiamo", "Ci abbiamo", "Le abbiamo", "Ne siamo"],
            answer: "Ne abbiamo",
            translation: "How many suitcases did you bring? — We brought only two of them.",
            rule: "With partitive 'ne', the past participle agrees in gender and number with the noun replaced ('valigie' -> 'ne abbiamo portate due')."
        },
        {
            sentence: "Riesci a riparare la stampante? — No, non ___ riesco proprio.",
            options: ["ci", "ne", "lo", "la"],
            answer: "ci",
            translation: "Can you manage to fix the printer? — No, I really can't manage it.",
            rule: "'Riuscire a + infinito' replaces the 'a + infinito' clause with 'ci' ('non ci riesco')."
        },
        {
            sentence: "Sei mai stato in Giappone? — No, non ___ sono mai stato, ma vorrei andarci.",
            options: ["ci", "ne", "lo", "li"],
            answer: "ci",
            translation: "Have you ever been to Japan? — No, I have never been there, but I would like to go there.",
            rule: "Locative 'in Giappone' is replaced by 'ci' ('non ci sono mai stato')."
        },
        {
            sentence: "Hai bisogno di una mano con le buste? — Grazie, non ___ ho bisogno.",
            options: ["ne", "ci", "la", "lo"],
            answer: "ne",
            translation: "Do you need a hand with the bags? — Thanks, I don't need it.",
            rule: "'Avere bisogno di', 'avere voglia di', and 'avere paura di' replace the 'di' complement with 'ne'."
        },
        {
            sentence: "Quanto tempo ___ vuole per arrivare in aeroporto in taxi?",
            options: ["ci", "ne", "si", "lo"],
            answer: "ci",
            translation: "How much time does it take to get to the airport by taxi?",
            rule: "Idiomatic 'volerci' ('ci vuole' + singular / 'ci vogliono' + plural) means 'it takes / is required'."
        },
        {
            sentence: "Vuoi ancora un po' di formaggio? — No grazie, non ___ voglio più.",
            options: ["ne", "ci", "lo", "del"],
            answer: "ne",
            translation: "Do you want some more cheese? — No thanks, I don't want any more of it.",
            rule: "Partial or unspecified quantities ('un po' di...', 'più', 'abbastanza') use partitive 'ne'."
        },
        {
            sentence: "Vuoi tutto il formaggio rimasto? — Sì, ___ prendo tutto.",
            options: ["lo", "ne", "ci", "li"],
            answer: "lo",
            translation: "Do you want all the remaining cheese? — Yes, I'll take all of it.",
            rule: "With 'tutto / tutta / tutti / tutte' (the entirety, not a part), Italian uses the direct object pronoun ('lo prendo tutto'), NEVER 'ne'."
        },
        {
            sentence: "Pensi ancora al colloquio di ieri? — Cerco di non pensar___ più.",
            options: ["ci", "ne", "lo", "gli"],
            answer: "ci",
            translation: "Are you still thinking about yesterday's interview? — I'm trying not to think about it anymore.",
            rule: "'Pensare a' takes enclitic '-ci' on the infinitive ('pensarci')."
        },
        {
            sentence: "A che ora sei uscito dall'ufficio ieri? — ___ sono uscito verso le sette.",
            options: ["Ne", "Ci", "Da lì", "Lo"],
            answer: "Ne",
            translation: "What time did you leave the office yesterday? — I left there around seven.",
            rule: "'Ne' replaces motion away from a place introduced by 'da' ('uscire da / tornare da un luogo' -> 'ne sono uscito')."
        },
        {
            sentence: "Non sento bene con questo rumore: non ___ sento da questo orecchio!",
            options: ["ci", "ne", "lo", "mi"],
            answer: "ci",
            translation: "I can't hear well with this noise: I can't hear out of this ear!",
            rule: "Idiomatic sensory ability uses 'vederci' (to be able to see) and 'sentirci' (to be able to hear)."
        },
        {
            sentence: "La festa è un po' noiosa; che ne dici, ___ andiamo?",
            options: ["ce ne", "ci ne", "ne ci", "se ne"],
            answer: "ce ne",
            translation: "The party is a bit boring; what do you say, shall we leave?",
            rule: "The pronominal verb 'andarsene' (to go away / leave a place) combines 'ci' + 'ne' into 'ce ne andiamo'."
        },
        {
            sentence: "Conosci tutti gli invitati? — No, ___ conosco soltanto tre o quattro.",
            options: ["ne", "li", "ci", "gli"],
            answer: "ne",
            translation: "Do you know all the guests? — No, I only know three or four of them.",
            rule: "Even with people, when a subset quantity is specified ('tre o quattro'), 'ne' is required instead of 'li'."
        },
        {
            sentence: "Scusi, ___ messo due ore per arrivare a causa del traffico.",
            options: ["ci ho", "ne ho", "c'è", "mi sono"],
            answer: "ci ho",
            translation: "Excuse me, it took me two hours to get here because of traffic.",
            rule: "Idiomatic 'metterci' (for a person to take a certain amount of time to do something) uses 'ci' + 'avere' ('ci ho messo due ore')."
        },
        {
            sentence: "Valeva davvero la pena di fare tutto questo viaggio? — Sì, ___ valeva la pena.",
            options: ["ne", "ci", "lo", "la"],
            answer: "ne",
            translation: "Was it really worth making this whole trip? — Yes, it was worth it.",
            rule: "The idiom 'valere la pena di...' replaces the 'di' clause with 'ne' ('ne vale la pena')."
        },
        {
            sentence: "Ti intendi di vini italiani? — Sì, ___ intendo abbastanza.",
            options: ["me ne", "mi ci", "me lo", "ne mi"],
            answer: "me ne",
            translation: "Do you know much about Italian wines? — Yes, I know a fair bit about them.",
            rule: "'Intendersi di qualcosa' (to be an expert/knowledgeable about) takes 'mi + ne' -> 'me ne intendo'."
        },
        {
            sentence: "Non capisco il senso di questa frase: non ___ capisco proprio niente.",
            options: ["ci", "ne", "lo", "la"],
            answer: "ci",
            translation: "I don't understand the meaning of this sentence: I really don't understand anything in it.",
            rule: "In the colloquial idiom 'non capirci niente' (to make neither head nor tail of it), Italian uses 'ci'."
        }
    ];

    const SUBJUNCTIVE_ITEMS = [
        {
            sentence: "Penso che Marco ___ perfettamente ragione in questo caso.",
            options: ["abbia", "ha", "avrà", "avrebbe"],
            answer: "abbia",
            translation: "I think that Marco is completely right in this case.",
            rule: "Unlike French and Spanish, Italian verbs of personal opinion ('pensare che', 'credere che', 'ritenere che') require the congiuntivo even in the affirmative!"
        },
        {
            sentence: "So che Marco ___ ragione, me l'ha confermato l'avvocato.",
            options: ["ha", "abbia", "avesse", "abbiano"],
            answer: "ha",
            translation: "I know that Marco is right; the lawyer confirmed it to me.",
            rule: "Verbs of objective knowledge and certainty ('sapere che', 'essere sicuro che', 'vedere che') take the indicativo ('ha')."
        },
        {
            sentence: "Spero che voi ___ passare una bellissima vacanza al mare.",
            options: ["possiate", "potete", "possate", "potreste"],
            answer: "possiate",
            translation: "I hope that you can spend a wonderful holiday by the sea.",
            rule: "Unlike French 'espérer que', Italian 'sperare che' expresses subjective hope and takes the congiuntivo ('voi possiate')."
        },
        {
            sentence: "Usciamo a fare una passeggiata, benché ___ piuttosto freddo.",
            options: ["faccia", "fa", "farà", "facesse"],
            answer: "faccia",
            translation: "Let's go out for a walk, although it is rather cold.",
            rule: "Concessive conjunctions ('benché', 'sebbene', 'nonostante', 'malgrado') require the congiuntivo ('faccia')."
        },
        {
            sentence: "Anche se ___ tardi, ti accompagnerò volentieri alla stazione.",
            options: ["è", "sia", "fosse", "sarà"],
            answer: "è",
            translation: "Even though it is late, I will gladly accompany you to the station.",
            rule: "Contrast 'benché + congiuntivo' with 'anche se': when 'anche se' states a real fact ('even though it is late'), it takes the indicativo ('è')."
        },
        {
            sentence: "È necessario che tutti i partecipanti ___ il modulo entro venerdì.",
            options: ["firmino", "firmano", "firmeranno", "firmassero"],
            answer: "firmino",
            translation: "It is necessary that all participants sign the form by Friday.",
            rule: "Impersonal expressions of necessity or evaluation ('è necessario che', 'bisogna che', 'è importante che') take the congiuntivo."
        },
        {
            sentence: "Ti chiamo sul cellulare prima che il treno ___.",
            options: ["parta", "parte", "partirà", "partisse"],
            answer: "parta",
            translation: "I'll call you on your mobile before the train leaves.",
            rule: "'Prima che' ALWAYS requires the congiuntivo ('parta')."
        },
        {
            sentence: "Dubito fortemente che loro ___ tutta la verità sull'incidente.",
            options: ["dicano", "dicono", "diranno", "dicessero"],
            answer: "dicano",
            translation: "I strongly doubt that they are telling the whole truth about the accident.",
            rule: "'Dubitare che' expresses doubt and triggers the congiuntivo ('loro dicano')."
        },
        {
            sentence: "Credo che questo appartamento ___ troppo piccolo per quattro persone.",
            options: ["sia", "è", "sarà", "fosse"],
            answer: "sia",
            translation: "I believe that this apartment is too small for four people.",
            rule: "'Credere che' expresses subjective opinion and requires the congiuntivo ('sia')."
        },
        {
            sentence: "Secondo me, questo appartamento ___ perfetto per le nostre esigenze.",
            options: ["è", "sia", "fosse", "siano"],
            answer: "è",
            translation: "In my opinion, this apartment is perfect for our needs.",
            rule: "'Secondo me' has no subordinating 'che', so the main clause remains in the indicativo ('è')."
        },
        {
            sentence: "Ho l'impressione che tu non mi ___ ascoltando con attenzione.",
            options: ["stia", "stai", "stessi", "starai"],
            answer: "stia",
            translation: "I have the impression that you are not listening to me carefully.",
            rule: "'Avere l'impressione che' and 'sembrare che' express subjective impression and take the congiuntivo ('tu stia')."
        },
        {
            sentence: "Benché ieri ___ brutto tempo, siamo andati lo stesso in montagna.",
            options: ["facesse", "faceva", "faccia", "ha fatto"],
            answer: "facesse",
            translation: "Although the weather was bad yesterday, we went to the mountains anyway.",
            rule: "'Benché' referring to an ongoing past state takes the congiuntivo imperfetto ('facesse')."
        },
        {
            sentence: "Pensavo che Laura ___ già partita per Milano.",
            options: ["fosse", "era", "sia", "è"],
            answer: "fosse",
            translation: "I thought that Laura had already left for Milan.",
            rule: "When the main verb of opinion is in the past ('Pensavo che...'), sequence of tenses requires the congiuntivo imperfetto/trapassato ('fosse partita')."
        },
        {
            sentence: "Se ___ più tempo libero, studierei anche il portoghese.",
            options: ["avessi", "avrei", "avevo", "abbia"],
            answer: "avessi",
            translation: "If I had more free time, I would also study Portuguese.",
            rule: "In a type-2 conditional sentence ('periodo ipotetico della possibilità'), the 'se' clause takes the congiuntivo imperfetto ('se avessi') and the main clause takes the condizionale ('studierei')."
        },
        {
            sentence: "Ti prego di abbassare la voce affinché il bambino ___ dormire.",
            options: ["possa", "può", "potrà", "potesse"],
            answer: "possa",
            translation: "Please lower your voice so that the child can sleep.",
            rule: "Conjunctions of purpose ('affinché', 'perché' meaning 'so that') require the congiuntivo ('possa')."
        },
        {
            sentence: "Non sono venuto alla festa perché ___ molto stanco.",
            options: ["ero", "fossi", "sia", "sarei"],
            answer: "ero",
            translation: "I didn't come to the party because I was very tired.",
            rule: "When 'perché' means 'because' (cause, not purpose), it takes the indicativo ('ero')."
        },
        {
            sentence: "Cerco una segretaria che ___ parlare fluentemente il tedesco.",
            options: ["sappia", "sa", "saprà", "sapesse"],
            answer: "sappia",
            translation: "I am looking for a secretary (any such secretary) who knows how to speak German fluently.",
            rule: "A relative clause modifying an indefinite, sought-after antecedent ('cerco una persona che...') takes the congiuntivo."
        },
        {
            sentence: "Conosco una segretaria che ___ parlare tre lingue straniere.",
            options: ["sa", "sappia", "saprebbe", "sapesse"],
            answer: "sa",
            translation: "I know a secretary who knows how to speak three foreign languages.",
            rule: "When the antecedent is a specific, known person ('conosco una segretaria che...'), the relative clause takes the indicativo ('sa')."
        },
        {
            sentence: "Ti presto l'auto a patto che tu ___ con molta prudenza.",
            options: ["guidi", "guida", "guiderai", "guidassi"],
            answer: "guidi",
            translation: "I'll lend you the car provided that you drive very carefully.",
            rule: "Conditional conjunctions ('purché', 'a patto che', 'a condizione che') always require the congiuntivo ('tu guidi' for 1st-conj. -are)."
        },
        {
            sentence: "Non so esattamente a che ora ___ l'ultimo autobus stasera.",
            options: ["passi", "passa", "passasse", "passerebbe"],
            answer: "passi",
            translation: "I don't know exactly what time the last bus comes by tonight.",
            rule: "Indirect questions introduced by 'non sapere', 'chiedersi', or 'domandarsi' standardly take the congiuntivo ('a che ora passi')."
        }
    ];

    let _container = null;
    let _activeTab = 'prepositions';
    let _questionCount = 10;
    let _queue = [];
    let _idx = 0;
    let _score = 0;
    let _mistakes = [];
    let _state = 'settings'; // 'settings' | 'quiz' | 'summary'
    let _keyHandlerAttached = false;

    function _esc(s) {
        if (!s) return '';
        const d = document.createElement('div');
        d.textContent = s;
        return d.innerHTML;
    }

    function _poolFor(tabId) {
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
            const tmp = copy[i];
            copy[i] = copy[j];
            copy[j] = tmp;
        }
        return copy;
    }

    function stop() {
        _state = 'settings';
        _queue = [];
        _idx = 0;
        if (_keyHandlerAttached && typeof document !== 'undefined') {
            document.removeEventListener('keydown', _handleGlobalKey);
            _keyHandlerAttached = false;
        }
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

        const feedbackEl = document.getElementById('it-quiz-feedback');
        if (!feedbackEl) return;

        feedbackEl.innerHTML = `
            <div class="gd-feedback ${isCorrect ? 'gd-feedback-correct' : 'gd-feedback-wrong'}" style="margin-top: 18px; padding: 14px 16px; border-radius: var(--radius-sm); border: 1px solid ${isCorrect ? 'var(--success)' : 'var(--danger)'}; background: ${isCorrect ? 'var(--success-bg, rgba(47,122,77,0.08))' : 'var(--danger-bg, rgba(178,58,34,0.08))'};">
                <div style="font-weight: 600; font-size: 15px; margin-bottom: 6px; color: ${isCorrect ? 'var(--success)' : 'var(--danger)'};">
                    ${isCorrect ? '✓ Correct' : '✗ Not quite'}
                </div>
                <div style="font-size: 14px; line-height: 1.45; color: var(--text); margin-bottom: 6px;">
                    <strong>Rule:</strong> ${_esc(item.rule)}
                </div>
                <div style="font-size: 13.5px; font-style: italic; color: var(--muted); margin-bottom: 14px;">
                    ${_esc(item.translation)}
                </div>
                <button type="button" class="vbtn vbtn-primary" id="it-next-btn" style="min-width: 140px;">Continue</button>
            </div>
        `;

        document.querySelectorAll('.gd-option').forEach(btn => {
            btn.disabled = true;
            if (btn.dataset.opt === item.answer) {
                btn.classList.add('correct');
            } else if (btn.dataset.opt === selected) {
                btn.classList.add('wrong');
            }
        });

        const nextBtn = document.getElementById('it-next-btn');
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
        const drillInfoBtn = (typeof DrillInfo !== 'undefined') ? DrillInfo.buttonHtml('it-grammar-studio') : '';

        return `
            <div class="gd-settings">
                <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px;">
                    <h2 class="gd-title" style="margin-bottom: 0;">Italian Grammar Studio</h2>
                    ${drillInfoBtn}
                </div>

                <div class="gd-tab-switcher" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="gd-tab-btn ${_activeTab === tab.id ? 'active' : ''}" data-it-tab="${tab.id}" role="tab" aria-selected="${_activeTab === tab.id}">
                            ${tab.label}
                        </button>
                    `).join('')}
                </div>

                <p class="gd-hint" style="margin-bottom: 22px;">${_esc(tabMeta.desc)}</p>

                <div class="gd-setting">
                    <label>Number of questions</label>
                    <div class="gd-count-chips">
                        ${[5, 10, 15, pool.length].map(n => `
                            <button type="button" class="gd-chip ${_questionCount === n ? 'active' : ''}" data-count="${n}">
                                ${n === pool.length ? `All (${pool.length})` : n}
                            </button>
                        `).join('')}
                    </div>
                </div>

                <button type="button" class="vbtn vbtn-primary vbtn-block" id="it-start-btn" style="margin-top: 24px;">Start Practice</button>
            </div>
        `;
    }

    function _renderQuiz() {
        const item = _queue[_idx];
        const tabMeta = TABS.find(t => t.id === _activeTab) || TABS[0];
        const options = _shuffle(item.options);
        const progressPct = Math.round(((_idx) / Math.max(1, _queue.length)) * 100);
        const promptSentence = item.sentence.replace('___', '<span class="gd-blank" style="display: inline-block; min-width: 48px; border-bottom: 2px solid var(--primary); color: var(--primary); font-weight: 600; text-align: center; padding: 0 4px;">_____</span>');

        return `
            <div class="driller-progress-track" aria-hidden="true">
                <div class="driller-progress-bar" style="width: ${progressPct}%;"></div>
            </div>
            <div class="gd-hud">
                <span class="gd-hud-score">Question ${_idx + 1} of ${_queue.length}</span>
                <button class="gd-change-skill" id="it-exit-btn">← Exit</button>
            </div>
            <div class="gd-hud-subline">
                <span class="gd-hud-skill-tag">${_esc(tabMeta.label)}</span>
                <span style="font-size: 13px; font-weight: 500; color: var(--secondary); font-variant-numeric: tabular-nums;">Score: ${_score}</span>
            </div>

            <div class="gd-exercise" style="max-width: 540px; margin: 0 auto; padding: 0 16px;">
                <p class="gd-question" style="font-family: var(--font-display, Georgia, serif); font-size: 1.25rem; line-height: 1.5; color: var(--text); margin: 18px 0 22px;">
                    ${promptSentence}
                </p>

                <div class="gd-options">
                    ${options.map((opt, i) => `
                        <button type="button" class="gd-option" data-opt="${_esc(opt)}">
                            <span class="lsn-key-hint">${i + 1}</span>
                            <span>${_esc(opt)}</span>
                        </button>
                    `).join('')}
                </div>

                <div id="it-quiz-feedback"></div>
            </div>
        `;
    }

    function _renderSummary() {
        const total = _queue.length;
        const pct = Math.round((_score / total) * 100);

        return `
            <div class="gd-settings">
                <div class="gd-clean-state" style="padding: 36px 24px; text-align: center;">
                    <h3 class="gd-clean-title" style="font-size: 1.4rem; margin-bottom: 8px;">Practice Complete</h3>
                    <div style="font-size: 2.4rem; font-family: var(--font-display, Georgia, serif); font-weight: 600; color: ${pct >= 80 ? 'var(--success)' : (pct >= 50 ? 'var(--ochre, #855A08)' : 'var(--danger)')}; margin: 12px 0;">
                        ${pct}%
                    </div>
                    <p class="gd-clean-desc" style="margin-bottom: 24px;">You answered ${_score} of ${total} questions correctly.</p>

                    ${_mistakes.length > 0 ? `
                        <div style="text-align: left; margin: 24px 0 20px; border-top: 1px solid var(--border); padding-top: 18px;">
                            <h4 style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 12px;">Points to review</h4>
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                ${_mistakes.map(m => `
                                    <div style="padding: 12px 14px; background: var(--wash, rgba(16,42,71,0.03)); border-left: 3px solid var(--danger); border-radius: var(--radius-sm);">
                                        <div style="font-weight: 500; font-size: 14.5px; color: var(--text); margin-bottom: 4px;">${_esc(m.item.sentence.replace('___', m.item.answer))}</div>
                                        <div style="font-size: 13px; color: var(--muted);">${_esc(m.item.rule)}</div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : `
                        <p style="font-weight: 600; color: var(--success); margin-bottom: 20px;">Outstanding! No mistakes made.</p>
                    `}

                    <div class="gd-clean-actions" style="margin-top: 24px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                        <button type="button" class="vbtn vbtn-primary" id="it-restart-btn">Practise Again</button>
                        <button type="button" class="vbtn vbtn-secondary" id="it-choose-tab-btn">Change Topic</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _handleGlobalKey(e) {
        if (!_container || _state !== 'quiz') return;

        const nextBtn = document.getElementById('it-next-btn');
        if (nextBtn) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                nextBtn.click();
            }
            return;
        }

        if (['1', '2', '3', '4'].includes(e.key)) {
            const index = parseInt(e.key, 10) - 1;
            const optionBtns = _container.querySelectorAll('.gd-option');
            if (optionBtns && optionBtns[index] && !optionBtns[index].disabled) {
                e.preventDefault();
                optionBtns[index].click();
            }
        }
    }

    function _attachEvents() {
        if (!_container) return;

        if (typeof DrillInfo !== 'undefined') {
            DrillInfo.attach(_container);
        }

        if (!_keyHandlerAttached && typeof document !== 'undefined') {
            document.addEventListener('keydown', _handleGlobalKey);
            _keyHandlerAttached = true;
        }

        if (_state === 'settings') {
            _container.querySelectorAll('[data-it-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _activeTab = btn.dataset.itTab;
                    _render();
                });
            });

            _container.querySelectorAll('.gd-chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    _questionCount = parseInt(btn.dataset.count, 10);
                    _container.querySelectorAll('.gd-chip').forEach(b => b.classList.toggle('active', b === btn));
                });
            });

            const startBtn = _container.querySelector('#it-start-btn');
            if (startBtn) {
                startBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }
        }

        if (_state === 'quiz') {
            const exitBtn = _container.querySelector('#it-exit-btn');
            if (exitBtn) {
                exitBtn.addEventListener('click', () => {
                    _state = 'settings';
                    _render();
                });
            }

            _container.querySelectorAll('.gd-option').forEach(btn => {
                btn.addEventListener('click', () => {
                    _onAnswer(btn.dataset.opt);
                });
            });
        }

        if (_state === 'summary') {
            const restartBtn = _container.querySelector('#it-restart-btn');
            if (restartBtn) {
                restartBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }

            const chooseTabBtn = _container.querySelector('#it-choose-tab-btn');
            if (chooseTabBtn) {
                chooseTabBtn.addEventListener('click', () => {
                    _state = 'settings';
                    _render();
                });
            }
        }
    }

    function _render() {
        if (!_container) return;

        if (_state === 'settings') {
            _container.innerHTML = _renderSettings();
        } else if (_state === 'quiz') {
            _container.innerHTML = _renderQuiz();
        } else if (_state === 'summary') {
            _container.innerHTML = _renderSummary();
        }

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
        _poolFor,
        render,
        init: render,
        stop
    };
})();

if (typeof window !== 'undefined') {
    window.ItGrammarStudio = ItGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ItGrammarStudio;
}
