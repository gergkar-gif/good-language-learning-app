// ============================================
// POLISH GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated Polish driller addressing the 5 core contrastive bottlenecks:
// 1. Biernik vs Dopełniacz & Genitive of Negation (Mam czas vs Nie mam czasu, animate vs inanimate masculine)
// 2. Narzędnik & Miejscownik (Professions/instruments with narzędnik vs prepositions w/na/o/po/przy with miejscownik)
// 3. Dokonany vs Niedokonany Aspect (Completed vs habitual/processive verb pairs)
// 4. Rodzaj Męskoosobowy vs Niemęskoosobowy Plurals (Virile -i/-y vs non-virile -e, past agreement byli vs były)
// 5. Clitic vs Stressed Pronouns & Clitic Peeling (cię/ciebie, mi/mnie, go/jego, clitic endings -m, -ś, -śmy)

const PlGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'cases_negation', label: 'Biernik vs Dopełniacz', desc: 'Accusative objects, animate masculine genitive-accusative shift, and mandatory Genitive of Negation' },
        { id: 'instrumental_locative', label: 'Narzędnik & Miejscownik', desc: 'Instrumental for identity, professions, tools & z/ze; Locative after prepositions w, na, o, po, przy' },
        { id: 'aspect', label: 'Aspekt (Dokonany / Niedokonany)', desc: 'Imperfective processes and habits vs perfective completed results and single events' },
        { id: 'virile_plural', label: 'Męskoosobowy vs Niemęskoosobowy', desc: 'Virile masculine personal plurals (oni, byli, studenci) vs non-virile (one, były, kobiety/samochody)' },
        { id: 'clitics_pronouns', label: 'Zaimki & Końcówki ruchome', desc: 'Short enclitic vs long emphatic pronouns (cię/ciebie, mi/mnie) and mobile past clitic endings' }
    ];

    const CASES_NEGATION_ITEMS = [
        {
            sentence: 'Mam ___ na przeczytanie tej interesującej książki.',
            options: ['czas', 'czasu', 'czasem', 'czasie'],
            answer: 'czas',
            translation: 'I have time to read this interesting book.',
            rule: 'Positive transitive verbs (mieć) take the direct object in the Accusative (biernik): inanimate masculine czas remains czas.'
        },
        {
            sentence: 'Niestety dzisiaj w ogóle nie mam ___.',
            options: ['czasu', 'czas', 'czasem', 'czasie'],
            answer: 'czasu',
            translation: 'Unfortunately today I have no time at all.',
            rule: 'The Genitive of Negation (dopełniacz) is mandatory after negated verbs: nie mam + Genitive (czas -> czasu).'
        },
        {
            sentence: 'Codziennie rano piję czarną ___.',
            options: ['kawę', 'kawy', 'kawa', 'kawą'],
            answer: 'kawę',
            translation: 'Every morning I drink black coffee.',
            rule: 'Feminine singular nouns in the Accusative end in -ę (kawa -> kawę).'
        },
        {
            sentence: 'Lekarz powiedział, że nie powinienem pić ___.',
            options: ['kawy', 'kawę', 'kawa', 'kawie'],
            answer: 'kawy',
            translation: 'The doctor said that I should not drink coffee.',
            rule: 'Negated verb phrase (nie pić) requires the direct object in Genitive: kawa -> kwy.'
        },
        {
            sentence: 'Widzę na ulicy twojego nowego ___.',
            options: ['psa', 'pies', 'psem', 'psie'],
            answer: 'psa',
            translation: 'I see your new dog on the street.',
            rule: 'Masculine animate nouns (animals and humans) take Genitive-form endings in the Accusative: pies -> psa.'
        },
        {
            sentence: 'Na parkingu przed biurem widzę twój nowy ___.',
            options: ['samochód', 'samochodu', 'samochodem', 'samochodzie'],
            answer: 'samochód',
            translation: 'In the parking lot in front of the office I see your new car.',
            rule: 'Masculine inanimate nouns retain the Nominative shape in the Accusative: samochód -> samochód.'
        },
        {
            sentence: 'Czy znasz tego młodego ___?',
            options: ['studenta', 'student', 'studentem', 'studencie'],
            answer: 'studenta',
            translation: 'Do you know this young student?',
            rule: 'Masculine personal direct objects take -a in the Accusative: student -> studenta.'
        },
        {
            sentence: 'Nie znam tego nowego ___.',
            options: ['studenta', 'student', 'studentem', 'studencie'],
            answer: 'studenta',
            translation: 'I do not know this new student.',
            rule: 'Both Accusative animate masculine and Genitive of Negation take -a for personal nouns (student -> studenta).'
        },
        {
            sentence: 'Kupuję w księgarni tę ciekawą ___.',
            options: ['książkę', 'książki', 'książka', 'książką'],
            answer: 'książkę',
            translation: 'I am buying this interesting book at the bookstore.',
            rule: 'Feminine noun and demonstrative in Accusative take -ę: tę ciekawą książkę.'
        },
        {
            sentence: 'Nie kupiłem tej drogiej ___.',
            options: ['książki', 'książkę', 'książka', 'książką'],
            answer: 'książki',
            translation: 'I did not buy this expensive book.',
            rule: 'Genitive of Negation on feminine nouns takes -y / -i: książka -> książki.'
        },
        {
            sentence: 'Bardzo lubię polską ___ i tradycyjne zupy.',
            options: ['kuchnię', 'kuchni', 'kuchnia', 'kuchnią'],
            answer: 'kuchnię',
            translation: 'I really like Polish cuisine and traditional soups.',
            rule: 'Accusative feminine takes -ę: kuchnia -> kuchnię.'
        },
        {
            sentence: 'On nie lubi zimnej ___.',
            options: ['zimy', 'zimę', 'zima', 'zimą'],
            answer: 'zimy',
            translation: 'He does not like cold winter.',
            rule: 'Negated verb (nie lubi) triggers Genitive on direct object: zima -> zimy.'
        },
        {
            sentence: 'Szukam mojego czarnego ___.',
            options: ['portfela', 'portfel', 'portfelem', 'portfelu'],
            answer: 'portfela',
            translation: 'I am looking for my black wallet.',
            rule: 'Verbs of seeking and desiring (szukać, potrzebować) always govern the Genitive even in positive sentences: portfel -> portfela.'
        },
        {
            sentence: 'Potrzebuję pilnie twojej ___.',
            options: ['pomocy', 'pomoc', 'pomocą', 'pomocu'],
            answer: 'pomocy',
            translation: 'I urgently need your help.',
            rule: 'The verb potrzebować governs the Genitive: pomoc -> pomocy.'
        },
        {
            sentence: 'Słucham wieczorem spokojnej ___.',
            options: ['muzyki', 'muzykę', 'muzyka', 'muzyką'],
            answer: 'muzyki',
            translation: 'In the evening I listen to calm music.',
            rule: 'Słuchać governs the Genitive in Polish: muzyka -> muzyki.'
        },
        {
            sentence: 'Nie pamiętam tego trudnego ___.',
            options: ['słowa', 'słowo', 'słowem', 'słowie'],
            answer: 'słowa',
            translation: 'I do not remember this difficult word.',
            rule: 'Negation of neuter noun direct object takes Genitive -a: słowo -> słowa.'
        },
        {
            sentence: 'Chcę kupić świeży chleb i biały ___.',
            options: ['ser', 'sera', 'serem', 'serze'],
            answer: 'ser',
            translation: 'I want to buy fresh bread and white cheese.',
            rule: 'Inanimate masculine food nouns in positive Accusative keep the Nominative form: ser -> ser.'
        },
        {
            sentence: 'W lodówce nie ma już żółtego ___.',
            options: ['sera', 'ser', 'serem', 'serze'],
            answer: 'sera',
            translation: 'There is no yellow cheese left in the fridge.',
            rule: 'Existential negation (nie ma) always takes the Genitive: ser -> sera.'
        },
        {
            sentence: 'Poproszę jedno małe ___ z pianką.',
            options: ['piwo', 'piwa', 'piwem', 'piwie'],
            answer: 'piwo',
            translation: 'One small beer with foam, please.',
            rule: 'Neuter nouns in the Accusative retain the Nominative ending (-o / -e): piwo -> piwo.'
        },
        {
            sentence: 'Lekarz zabronił mu pić zimnego ___.',
            options: ['piwa', 'piwo', 'piwem', 'piwie'],
            answer: 'piwa',
            translation: 'The doctor forbade him from drinking cold beer.',
            rule: 'Negated/inhibited object in Genitive: piwo -> piwa.'
        }
    ];

    const INSTRUMENTAL_LOCATIVE_ITEMS = [
        {
            sentence: 'Mój ojciec z zawodu jest znanym ___.',
            options: ['lekarzem', 'lekarz', 'lekarza', 'lekarzu'],
            answer: 'lekarzem',
            translation: 'My father by profession is a well-known doctor.',
            rule: 'Predicative nouns following być (to be) expressing profession or role take the Instrumental (narzędnik): lekarz -> lekarzem.'
        },
        {
            sentence: 'Moja starsza siostra jest utalentowaną ___.',
            options: ['nauczycielką', 'nauczycielka', 'nauczycielki', 'nauczycielce'],
            answer: 'nauczycielką',
            translation: 'My older sister is a talented teacher.',
            rule: 'Feminine singular nouns in the Instrumental end in -ą: nauczycielka -> nauczycielką.'
        },
        {
            sentence: 'Często jeżdżę do pracy miejskim ___.',
            options: ['autobusem', 'autobus', 'autobusu', 'autobusie'],
            answer: 'autobusem',
            translation: 'I often travel to work by city bus.',
            rule: 'Means of transport used as an instrument take the Instrumental without preposition: autobus -> autobusem.'
        },
        {
            sentence: 'Idę dziś do kina z moim nowym ___.',
            options: ['kolegą', 'kolega', 'koledze', 'kolegę'],
            answer: 'kolegą',
            translation: 'I am going to the cinema today with my new friend.',
            rule: 'Preposition z / ze (with - accompaniment) requires the Instrumental: z kolegą.'
        },
        {
            sentence: 'Mieszkam w pięknym, starym ___.',
            options: ['Krakowie', 'Kraków', 'Krakowa', 'Krakowem'],
            answer: 'Krakowie',
            translation: 'I live in beautiful, old Krakow.',
            rule: 'Static location with preposition w (in) requires the Locative (miejscownik): Kraków -> Krakowie.'
        },
        {
            sentence: 'Książka leży na drewnianym ___.',
            options: ['stole', 'stół', 'stołu', 'stołem'],
            answer: 'stole',
            translation: 'The book is lying on the wooden table.',
            rule: 'Location on a surface with na takes Locative with consonant alternation ł:l and ó:o (stół -> stole).'
        },
        {
            sentence: 'Rozmawialiśmy długo o nowym ___.',
            options: ['filmie', 'film', 'filmu', 'filmem'],
            answer: 'filmie',
            translation: 'We spoke for a long time about the new film.',
            rule: 'Topic with preposition o (about) requires the Locative: film -> filmie.'
        },
        {
            sentence: 'Po udanym ___ poszliśmy do restauracji.',
            options: ['koncercie', 'koncert', 'koncertu', 'koncertem'],
            answer: 'koncercie',
            translation: 'After a successful concert we went to a restaurant.',
            rule: 'Temporal preposition po (after) requires the Locative: koncert -> koncercie.'
        },
        {
            sentence: 'Spotkajmy się przy głównym ___ kolejowym.',
            options: ['dworcu', 'dworzec', 'dworca', 'dworcem'],
            answer: 'dworcu',
            translation: 'Let us meet by the main railway station.',
            rule: 'Preposition przy (by/near) takes the Locative; masculine nouns ending in -ec take -u: dworzec -> dworcu.'
        },
        {
            sentence: 'Jesteśmy teraz w małym, przytulnym ___.',
            options: ['pokoju', 'pokój', 'pokojem', 'pokoju'],
            answer: 'pokoju',
            translation: 'We are now in a small, cosy room.',
            rule: 'Locative with w for pokój takes -u: w pokoju.'
        },
        {
            sentence: 'Ona interesuje się polską ___ i kinem.',
            options: ['historią', 'historia', 'historii', 'historię'],
            answer: 'historią',
            translation: 'She is interested in Polish history and cinema.',
            rule: 'The reflexive verb interesować się takes the Instrumental without preposition: historia -> historią.'
        },
        {
            sentence: 'Mój brat został wybitnym ___.',
            options: ['architektem', 'architekt', 'architekta', 'architekcie'],
            answer: 'architektem',
            translation: 'My brother became an outstanding architect.',
            rule: 'The verb zostać (to become) governs the Instrumental for the resulting identity: architektem.'
        },
        {
            sentence: 'Piszemy to ćwiczenie czarnym ___.',
            options: ['długopisem', 'długopis', 'długopisu', 'długopisie'],
            answer: 'długopisem',
            translation: 'We are writing this exercise with a black pen.',
            rule: 'Instrument of an action takes the bare Instrumental: długopis -> długopisem.'
        },
        {
            sentence: 'W mojej rodzinnej ___ nie ma teatru.',
            options: ['wsi', 'wieś', 'wsią', 'wsiu'],
            answer: 'wsi',
            translation: 'In my home village there is no theatre.',
            rule: 'Feminine noun wieś in Locative with w becomes wsi.'
        },
        {
            sentence: 'O czym myślisz? Myślę o mojej ___.',
            options: ['rodzinie', 'rodzina', 'rodziny', 'rodziną'],
            answer: 'rodzinie',
            translation: 'What are you thinking about? I am thinking about my family.',
            rule: 'Preposition o + Locative on feminine -a ending stems takes -e with d:dz consonant shift (rodzina -> rodzinie).'
        },
        {
            sentence: 'Herbata z cytryną i białym ___.',
            options: ['cukrem', 'cukier', 'cukru', 'cukrze'],
            answer: 'cukrem',
            translation: 'Tea with lemon and white sugar.',
            rule: 'Preposition z (with ingredient/accompaniment) takes Instrumental: cukier -> cukrem.'
        },
        {
            sentence: 'Pies leży pod drewnianym ___.',
            options: ['stołem', 'stół', 'stole', 'stołu'],
            answer: 'stołem',
            translation: 'The dog is lying under the wooden table.',
            rule: 'Static position under an object (pod) requires the Instrumental: pod stołem.'
        },
        {
            sentence: 'Czekam na ciebie na drugim ___.',
            options: ['piętrze', 'piętro', 'piętra', 'piętrem'],
            answer: 'piętrze',
            translation: 'I am waiting for you on the second floor.',
            rule: 'Building floors take na + Locative: piętro -> piętrze (consonant shift r -> rz).'
        },
        {
            sentence: 'Przed naszym starym ___ rośnie wielkie drzewo.',
            options: ['domem', 'dom', 'domu', 'domie'],
            answer: 'domem',
            translation: 'In front of our old house grows a big tree.',
            rule: 'Preposition przed (in front of - static location) requires the Instrumental: przed domem.'
        },
        {
            sentence: 'W całym tym dużym ___ zgasło światło.',
            options: ['mieście', 'miasto', 'miasta', 'miastem'],
            answer: 'mieście',
            translation: 'In this entire large city the light went out.',
            rule: 'Locative of miasto takes -e with st:ść consonant shift (w mieście).'
        }
    ];

    const ASPECT_ITEMS = [
        {
            sentence: 'Wczoraj przez cały wieczór ___ ciekawą książkę.',
            options: ['czytałem', 'przeczytałem', 'przeczytam', 'będę przeczytać'],
            answer: 'czytałem',
            translation: 'Yesterday for the entire evening I was reading an interesting book.',
            rule: 'Duration expressions (przez cały wieczór) focus on the ongoing process and require the imperfective aspect (czytałem).'
        },
        {
            sentence: 'W końcu wczoraj ___ całą tę książkę od deski do deski.',
            options: ['przeczytałem', 'czytałem', 'czytam', 'będę czytać'],
            answer: 'przeczytałem',
            translation: 'Finally yesterday I finished reading this whole book from cover to cover.',
            rule: 'Completion of a result (w końcu, całą książkę) requires the perfective aspect (przeczytałem).'
        },
        {
            sentence: 'Zawsze rano ___ kawę przed wyjściem do pracy.',
            options: ['piję', 'wypiję', 'wypijam', 'będę wypić'],
            answer: 'piję',
            translation: 'Always in the morning I drink coffee before leaving for work.',
            rule: 'Habitual repeated actions (zawsze, często, rano) use the imperfective aspect (piję).'
        },
        {
            sentence: 'Poczekaj chwilę, szybko ___ tę herbatę i możemy iść.',
            options: ['wypiję', 'piję', 'piłem', 'będę pił'],
            answer: 'wypiję',
            translation: 'Wait a moment, I will quickly finish drinking this tea and we can go.',
            rule: 'Future single completed action uses the perfective present-future form (wypiję).'
        },
        {
            sentence: 'Co robiłeś, kiedy zadzwoniłem? Właśnie ___ obiad.',
            options: ['gotowałem', 'ugotowałem', 'ugotuję', 'będę ugotować'],
            answer: 'gotowałem',
            translation: 'What were you doing when I called? I was just cooking dinner.',
            rule: 'Ongoing background activity interrupted by another event takes imperfective past (gotowałem).'
        },
        {
            sentence: 'Na dzisiejszą kolację ___ pyszny żurek.',
            options: ['ugotowałem', 'gotowałem', 'gotuję', 'ugotuję'],
            answer: 'ugotowałem',
            translation: 'For today dinner I cooked a delicious sour rye soup.',
            rule: 'A completed finished achievement with a result produced takes perfective past (ugotowałem).'
        },
        {
            sentence: 'Często ___ do dziadków w weekendy.',
            options: ['pisałem', 'napisałem', 'napiszę', 'będę napisać'],
            answer: 'pisałem',
            translation: 'I often used to write to my grandparents on weekends.',
            rule: 'Repeated historical habit (często w weekendy) takes imperfective past (pisałem).'
        },
        {
            sentence: 'Usiadłem przy biurku i w godzinę ___ cały ważny raport.',
            options: ['napisałem', 'pisałem', 'piszę', 'będę pisać'],
            answer: 'napisałem',
            translation: 'I sat at the desk and in an hour I wrote the entire important report.',
            rule: 'Action completed within a time limit (w godzinę) takes perfective past (napisałem).'
        },
        {
            sentence: 'Jutro przez trzy godziny będziemy ___ nowe słówka.',
            options: ['powtarzać', 'powtórzyć', 'powtórzyli', 'powtórzymy'],
            answer: 'powtarzać',
            translation: 'Tomorrow for three hours we will be reviewing new words.',
            rule: 'Compound future with być (będziemy) can only take imperfective infinitives or participles (powtarzać), never perfective.'
        },
        {
            sentence: 'Jutro rano na pewno ___ ten trudny egzamin.',
            options: ['zdam', 'będę zdawać', 'zdawałem', 'zdawać'],
            answer: 'zdam',
            translation: 'Tomorrow morning I will definitely pass this difficult exam.',
            rule: 'Definite completed outcome in the future takes synthetic perfective future (zdam).'
        },
        {
            sentence: 'Tomasz długo ___ kluczy, aż wreszcie je znalazł.',
            options: ['szukał', 'znalazł', 'znajdował', 'poszukał'],
            answer: 'szukał',
            translation: 'Tomasz searched for the keys for a long time until he finally found them.',
            rule: 'Ongoing extended effort (długo) takes imperfective szukać (szukał); successful result takes perfective znaleźć (znalazł).'
        },
        {
            sentence: 'Gdy wszedłem do pokoju, oni ___ o polityce.',
            options: ['rozmawiali', 'porozmawiali', 'będą rozmawiać', 'rozmawiać'],
            answer: 'rozmawiali',
            translation: 'When I entered the room, they were talking about politics.',
            rule: 'Continuous activity in progress at a specific past point in time requires imperfective (rozmawiali).'
        },
        {
            sentence: 'Musimy koniecznie ___ ten problem przed spotkaniem.',
            options: ['rozwiązać', 'rozwiązywać', 'rozwiązaliśmy', 'rozwiążemy'],
            answer: 'rozwiązać',
            translation: 'We must definitely solve this problem before the meeting.',
            rule: 'Achieving a definitive resolution requires perfective infinitive: rozwiązać.'
        },
        {
            sentence: 'Marek codziennie ___ o szóstej rano.',
            options: ['wstaje', 'wstanie', 'wstał', 'będzie wstać'],
            answer: 'wstaje',
            translation: 'Marek gets up at six in the morning every day.',
            rule: 'Daily routine (codziennie) in the present requires imperfective aspect (wstaje).'
        },
        {
            sentence: 'Jutro wyjątkowo ___ wcześniej, żeby zdążyć na pociąg.',
            options: ['wstanę', 'wstaję', 'wstawałem', 'będę wstać'],
            answer: 'wstanę',
            translation: 'Tomorrow exceptionally I will get up earlier to catch the train.',
            rule: 'Single specific event in the future requires perfective future (wstanę).'
        },
        {
            sentence: 'Czy możesz mi pomóc? Zaraz ___ tę paczkę.',
            options: ['otworzę', 'otwierałem', 'będę otwierać', 'otwierać'],
            answer: 'otworzę',
            translation: 'Can you help me? I will open this package right away.',
            rule: 'Immediate future completion (zaraz) uses perfective future (otworzę).'
        },
        {
            sentence: 'W lecie zawsze ___ okno na całą noc.',
            options: ['otwieram', 'otworzę', 'otworzyłem', 'otworzywszy'],
            answer: 'otwieram',
            translation: 'In the summer I always open the window for the entire night.',
            rule: 'Habitual repeated practice (zawsze) takes imperfective (otwieram).'
        },
        {
            sentence: 'Nareszcie ___ całą prawdę o tej sprawie.',
            options: ['zrozumiałem', 'rozumiałem', 'rozumiem', 'będę rozumieć'],
            answer: 'zrozumiałem',
            translation: 'At last I understood the whole truth about this matter.',
            rule: 'Sudden culmination/insight (nareszcie) takes perfective past (zrozumiałem).'
        },
        {
            sentence: 'Kiedy byłem mały, w ogóle nie ___ języka angielskiego.',
            options: ['rozumiałem', 'zrozumiałem', 'zrozumiem', 'zrozumieć'],
            answer: 'rozumiałem',
            translation: 'When I was little, I did not understand the English language at all.',
            rule: 'Long-term state of capability in the past uses imperfective (rozumiałem).'
        },
        {
            sentence: 'Czy ___ już wszystkie rachunki za ten miesiąc?',
            options: ['zapłaciłeś', 'płaciłeś', 'płacisz', 'będziesz zapłacić'],
            answer: 'zapłaciłeś',
            translation: 'Have you already paid all the bills for this month?',
            rule: 'Result achieved with respect to the present (już) takes perfective past (zapłaciłeś).'
        }
    ];

    const VIRILE_PLURAL_ITEMS = [
        {
            sentence: 'Wszyscy nowi ___ zdali wczoraj trudny egzamin.',
            options: ['studenci', 'studentki', 'studentów', 'studentach'],
            answer: 'studenci',
            translation: 'All the new male/mixed students passed the difficult exam yesterday.',
            rule: 'Virile masculine personal nominative plural takes personal endings like -i/-y with consonant softening (student -> studenci).'
        },
        {
            sentence: 'Wczoraj w teatrze ___ moi dobrzy koledzy.',
            options: ['byli', 'były', 'było', 'był'],
            answer: 'byli',
            translation: 'Yesterday at the theatre were my good colleagues.',
            rule: 'Past tense of być with masculine personal subjects (koledzy) takes the virile plural form byli (vs non-virile były).'
        },
        {
            sentence: 'Moje koleżanki ze studiów ___ wczoraj w bibliotece.',
            options: ['były', 'byli', 'było', 'był'],
            answer: 'były',
            translation: 'My female colleagues from studies were in the library yesterday.',
            rule: 'Groups of women, children, animals, or objects take the non-virile past plural ending -ły (były).'
        },
        {
            sentence: 'Ci znani polscy ___ pracują nad nowym filmem.',
            options: ['aktorzy', 'aktorki', 'aktorów', 'aktorami'],
            answer: 'aktorzy',
            translation: 'These famous Polish actors are working on a new film.',
            rule: 'Masculine personal plural takes virile demonstrative (ci) and personal noun form: aktorzy.'
        },
        {
            sentence: 'Tamte szybkie ___ czekały na zielone światło.',
            options: ['samochody', 'samochodów', 'samochodzi', 'samochodzie'],
            answer: 'samochody',
            translation: 'Those fast cars were waiting for the green light.',
            rule: 'Inanimate objects (samochody) belong to the non-virile gender: demonstrative tamte, noun in -y, past czekały.'
        },
        {
            sentence: 'Dwaj młodzi ___ rozmawiali głośno w kawiarni.',
            options: ['panowie', 'panów', 'pani', 'panom'],
            answer: 'panowie',
            translation: 'Two young gentlemen were talking loudly in the café.',
            rule: 'Virile numeral construction dwaj takes masculine personal plural panowie.'
        },
        {
            sentence: 'Dwie młode ___ rozmawiały przy stoliku obok.',
            options: ['kobiety', 'kobiet', 'kobietom', 'kobietami'],
            answer: 'kobiety',
            translation: 'Two young women were talking at the table next door.',
            rule: 'Non-virile feminine numeral dwie takes regular plural kobiety.'
        },
        {
            sentence: 'Wszyscy nasi ___ przyjechali na święta.',
            options: ['rodzice', 'rodziców', 'rodzicami', 'rodzicom'],
            answer: 'rodzice',
            translation: 'All our parents arrived for the holidays.',
            rule: 'Masculine personal subject (rodzice) takes virile modifiers: wszyscy nasi, verb przyjechali.'
        },
        {
            sentence: 'Nasze małe ___ bawiły się w ogrodzie.',
            options: ['dzieci', 'dzieciom', 'dziećmi', 'dzieciach'],
            answer: 'dzieci',
            translation: 'Our little children were playing in the garden.',
            rule: 'Dzieci (children) behaves grammatically as non-virile plural: nasze małe dzieci bawiły się (ending -ły).'
        },
        {
            sentence: 'Do sali weszli trzej znani ___.',
            options: ['profesorowie', 'profesorki', 'profesorów', 'profesorem'],
            answer: 'profesorowie',
            translation: 'Three renowned professors entered the hall.',
            rule: 'Virile numeral trzej takes masculine personal ending -owie: profesorowie, verb weszli.'
        },
        {
            sentence: 'Trzy stare ___ stały na skraju drogi.',
            options: ['drzewa', 'drzew', 'drzewom', 'drzewami'],
            answer: 'drzewa',
            translation: 'Three old trees stood on the edge of the road.',
            rule: 'Neuter nouns in plural take non-virile numeral trzy, noun drzewa, and past stały.'
        },
        {
            sentence: 'Nasi nowi polscy ___ są bardzo sympatyczni.',
            options: ['sąsiedzi', 'sąsiadki', 'sąsiadów', 'sąsiadami'],
            answer: 'sąsiedzi',
            translation: 'Our new Polish neighbours are very friendly.',
            rule: 'Masculine personal plural of sąsiad has stem vowel shift and consonant shift: sąsiedzi, adj sympatyczni.'
        },
        {
            sentence: 'Tamte nowe ___ były bardzo drogie.',
            options: ['telefony', 'telefonów', 'telefoni', 'telefonach'],
            answer: 'telefony',
            translation: 'Those new phones were very expensive.',
            rule: 'Inanimate masculine nouns in plural are non-virile: telefony, adjective drogie, verb były.'
        },
        {
            sentence: 'Czy widziałeś tych dwóch młodych ___?',
            options: ['chłopców', 'chłopcy', 'chłopcom', 'chłopcami'],
            answer: 'chłopców',
            translation: 'Did you see those two young boys?',
            rule: 'In the Accusative plural, virile masculine personal nouns take Genitive-identical endings in -ów (chłopców).'
        },
        {
            sentence: 'Kupiłem wczoraj te dwa nowe ___.',
            options: ['komputery', 'komputerów', 'komputerach', 'komputerom'],
            answer: 'komputery',
            translation: 'I bought these two new computers yesterday.',
            rule: 'In the Accusative plural, non-virile nouns retain the Nominative form: komputery (te dwa nowe komputery).'
        },
        {
            sentence: 'Polscy ___ walczyli dzielnie o wolność ojczyzny.',
            options: ['żołnierze', 'żołnierzy', 'żołnierzem', 'żołnierzom'],
            answer: 'żołnierze',
            translation: 'Polish soldiers fought bravely for the homeland freedom.',
            rule: 'Masculine personal żołnierz takes plural żołnierze and virile past walczyli.'
        },
        {
            sentence: 'Te wysokie ___ rosną w parku od stu lat.',
            options: ['dęby', 'dębów', 'dębi', 'dębach'],
            answer: 'dęby',
            translation: 'These tall oak trees have been growing in the park for a hundred years.',
            rule: 'Inanimate masculine trees are non-virile: te wysokie dęby.'
        },
        {
            sentence: 'Gdzie ___ wczoraj wieczorem, panowie?',
            options: ['byliście', 'byłyście', 'byliśmy', 'byłyśmy'],
            answer: 'byliście',
            translation: 'Where were you yesterday evening, gentlemen?',
            rule: 'Second-person plural referring to men (panowie) takes virile ending -liście: byliście.'
        },
        {
            sentence: 'Gdzie ___ wczoraj wieczorem, drogie panie?',
            options: ['byłyście', 'byliście', 'byłyśmy', 'byliśmy'],
            answer: 'byłyście',
            translation: 'Where were you yesterday evening, dear ladies?',
            rule: 'Second-person plural referring exclusively to women takes non-virile ending -łyście: byłyście.'
        },
        {
            sentence: 'Wszyscy moi dobrzy ___ pomogli mi przy przeprowadzce.',
            options: ['przyjaciele', 'przyjaciółki', 'przyjaciół', 'przyjaciołom'],
            answer: 'przyjaciele',
            translation: 'All my good friends helped me with the move.',
            rule: 'Irregular masculine personal plural of przyjaciel is przyjaciele, with virile past pomogli.'
        }
    ];

    const CLITICS_PRONOUNS_ITEMS = [
        {
            sentence: 'Bardzo ___ lubię i chcę ci pomóc.',
            options: ['cię', 'ciebie', 'tobie', 'tobą'],
            answer: 'cię',
            translation: 'I like you very much and want to help you.',
            rule: 'In neutral mid-sentence positions without emphasis, Polish uses the short clitic pronoun cię, not the emphatic ciebie.'
        },
        {
            sentence: 'To właśnie ___ widziałem wczoraj w kinie, a nie kogoś innego!',
            options: ['ciebie', 'cię', 'tobie', 'tobą'],
            answer: 'ciebie',
            translation: 'It was precisely you whom I saw yesterday at the cinema, not someone else!',
            rule: 'Under contrastive emphasis, focus (właśnie), or at the beginning of a clause, the full stressed form ciebie is required.'
        },
        {
            sentence: 'Czekam na ___ już ponad pół godziny.',
            options: ['ciebie', 'cię', 'tobie', 'tobą'],
            answer: 'ciebie',
            translation: 'I have been waiting for you for over half an hour already.',
            rule: 'After prepositions (na, do, dla, od), stressed pronoun forms must be used: na ciebie, never na cię.'
        },
        {
            sentence: 'Czy możesz ___ pożyczyć tę książkę?',
            options: ['mi', 'mnie', 'mną', 'mnieć'],
            answer: 'mi',
            translation: 'Can you lend me this book?',
            rule: 'In neutral non-initial indirect object position, the short clitic dative mi is standard.'
        },
        {
            sentence: 'Daj to ___ , a nie jemu!',
            options: ['mnie', 'mi', 'mną', 'mnieć'],
            answer: 'mnie',
            translation: 'Give that to me, and not to him!',
            rule: 'In contrastive dative phrases (...a nie jemu), the full stressed pronoun mnie is mandatory.'
        },
        {
            sentence: 'Nie widziałem ___ od zeszłego tygodnia.',
            options: ['go', 'jego', 'niego', 'jemu'],
            answer: 'go',
            translation: 'I have not seen him since last week.',
            rule: 'In neutral mid-sentence positions, the short clitic accusative/genitive go is used for third-person singular masculine.'
        },
        {
            sentence: 'Czekamy na ___ przed wejściem do teatru.',
            options: ['niego', 'jego', 'go', 'on'],
            answer: 'niego',
            translation: 'We are waiting for him in front of the theatre entrance.',
            rule: 'After prepositions, third-person pronouns prepend the n- prefix: na niego, do niego, z nim.'
        },
        {
            sentence: 'Wczoraj rano poszła___ do biblioteki uniwersyteckiej.',
            options: ['m', 'śmy', 'ś', 'ście'],
            answer: 'm',
            translation: 'Yesterday morning I (female) went to the university library.',
            rule: 'First-person singular past clitic ending for female speaker attaches to the l-participle poszła + m = poszłam.'
        },
        {
            sentence: 'Gdzie wczoraj poszli___ po lekcjach?',
            options: ['ście', 'śmy', 'm', 'ś'],
            answer: 'ście',
            translation: 'Where did you (plural virile) go yesterday after classes?',
            rule: 'Second-person plural past ending attaches to virile participle poszli + ście = poszliście.'
        },
        {
            sentence: 'Gdzie___ wczoraj był?',
            options: ['ś', 'm', 'ście', 'śmy'],
            answer: 'ś',
            translation: 'Where were you (singular masculine) yesterday?',
            rule: 'Mobile past clitics can peel off the verb and attach to question words or conjunctions: Gdzieś był? = Gdzie byłeś?'
        },
        {
            sentence: 'Co___ wczoraj zrobili na obiad?',
            options: ['ście', 'śmy', 'm', 'ś'],
            answer: 'ście',
            translation: 'What did you (plural) make for dinner yesterday?',
            rule: 'Mobile clitic -ście attaches to question word: Coście zrobili? = Co zrobiliście?'
        },
        {
            sentence: 'Gdyby___ miał więcej czasu, pojechałbym w góry.',
            options: ['m', 'ś', 'śmy', 'ście'],
            answer: 'm',
            translation: 'If I had more time, I would go to the mountains.',
            rule: 'Conditional clitic -bym / -by- attaches to conjunction gdyby + m = gdybym.'
        },
        {
            sentence: 'Znam ___ od wielu lat i bardzo ją szanuję.',
            options: ['ją', 'niej', 'niejże', 'jej'],
            answer: 'ją',
            translation: 'I have known her for many years and respect her very much.',
            rule: 'Feminine third-person direct object in Accusative is ją.'
        },
        {
            sentence: 'Zadzwoniłem do ___ wczoraj wieczorem.',
            options: ['niej', 'ją', 'jej', 'ona'],
            answer: 'niej',
            translation: 'I phoned her yesterday evening.',
            rule: 'After preposition do (takes Genitive), feminine pronoun adds n- prefix: do niej.'
        },
        {
            sentence: 'Pomogłem ___ w rozwiązaniu trudnego zadania.',
            options: ['mu', 'jemu', 'nim', 'jego'],
            answer: 'mu',
            translation: 'I helped him solve the difficult exercise.',
            rule: 'Unstressed indirect object dative for he is clitic mu: pomogłem mu.'
        },
        {
            sentence: 'Właśnie ___ chcę podziękować za wszystko.',
            options: ['jemu', 'mu', 'niego', 'nim'],
            answer: 'jemu',
            translation: 'It is precisely him that I want to thank for everything.',
            rule: 'Stressed/emphatic dative pronoun after właśnie is jemu.'
        },
        {
            sentence: 'Idziemy dzisiaj z ___ na spacer do parku.',
            options: ['nimi', 'ich', 'im', 'oni'],
            answer: 'nimi',
            translation: 'We are going for a walk to the park with them today.',
            rule: 'Preposition z + Instrumental plural pronoun adds n- prefix: z nimi.'
        },
        {
            sentence: 'Dlaczego nic ___ o tym nie powiedziałeś?',
            options: ['nam', 'nas', 'nami', 'my'],
            answer: 'nam',
            translation: 'Why did you not say anything to us about this?',
            rule: 'Dative of my (we) is nam: powiedzieć komuś -> nam.'
        },
        {
            sentence: 'Czekają na ___ na lotnisku.',
            options: ['nas', 'nam', 'nami', 'my'],
            answer: 'nas',
            translation: 'They are waiting for us at the airport.',
            rule: 'Preposition na + Accusative for we is nas: czekać na nas.'
        },
        {
            sentence: 'Zawsze chętnie ___ pomagamy.',
            options: ['wam', 'was', 'wami', 'wy'],
            answer: 'wam',
            translation: 'We always gladly help you (plural).',
            rule: 'Pomagać takes dative: wam (to you all).'
        }
    ];

    let _container = null;
    let _activeTab = 'cases_negation';
    let _state = 'settings'; // 'settings' | 'quiz' | 'summary'
    let _questionCount = 10;
    let _queue = [];
    let _currentIndex = 0;
    let _score = 0;
    let _mistakes = [];
    let _keyHandlerAttached = false;

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

    function _poolFor(tabId) {
        if (tabId === 'cases_negation') return CASES_NEGATION_ITEMS;
        if (tabId === 'instrumental_locative') return INSTRUMENTAL_LOCATIVE_ITEMS;
        if (tabId === 'aspect') return ASPECT_ITEMS;
        if (tabId === 'virile_plural') return VIRILE_PLURAL_ITEMS;
        if (tabId === 'clitics_pronouns') return CLITICS_PRONOUNS_ITEMS;
        return CASES_NEGATION_ITEMS;
    }

    function _startSession(count) {
        const pool = _poolFor(_activeTab);
        _queue = _shuffle(pool).slice(0, Math.min(count, pool.length));
        _currentIndex = 0;
        _score = 0;
        _mistakes = [];
        _state = 'quiz';
        _render();
    }

    function _onAnswer(selected) {
        const item = _queue[_currentIndex];
        const isCorrect = selected === item.answer;

        if (isCorrect) {
            _score++;
        } else {
            _mistakes.push({ item: item, selected: selected });
        }

        const fbContainer = _container.querySelector('#pl-quiz-feedback');
        if (!fbContainer) return;

        const optionBtns = _container.querySelectorAll('.gd-option');
        optionBtns.forEach(btn => {
            btn.disabled = true;
            if (btn.dataset.opt === item.answer) {
                btn.classList.add('correct');
            } else if (btn.dataset.opt === selected && !isCorrect) {
                btn.classList.add('incorrect');
            }
        });

        fbContainer.innerHTML = `
            <div class="gd-feedback-panel ${isCorrect ? 'gd-correct' : 'gd-incorrect'}" style="margin-top: 18px; padding: 14px 16px; border-radius: var(--radius-md); background: ${isCorrect ? 'var(--success-bg, rgba(46,125,50,0.08))' : 'var(--danger-bg, rgba(211,47,47,0.08))'}; border-left: 4px solid ${isCorrect ? 'var(--success, #2e7d32)' : 'var(--danger, #d32f2f)'};">
                <div style="font-weight: 600; font-size: 15px; color: ${isCorrect ? 'var(--success, #2e7d32)' : 'var(--danger, #d32f2f)'}; margin-bottom: 4px;">
                    ${isCorrect ? 'Dobrze! (Correct)' : 'Niepoprawnie (Incorrect)'}
                </div>
                <div style="font-size: 14px; color: var(--text); margin-bottom: 6px;">
                    <strong>Translation:</strong> ${_esc(item.translation)}
                </div>
                <div style="font-size: 13.5px; color: var(--muted); line-height: 1.45;">
                    <strong>Grammar rule:</strong> ${_esc(item.rule)}
                </div>
                <div style="margin-top: 12px; text-align: right;">
                    <button type="button" class="vbtn vbtn-primary" id="pl-next-btn">
                        ${_currentIndex + 1 < _queue.length ? 'Następne pytanie (Next) &rarr;' : 'Zobacz wynik (View Results) &rarr;'}
                    </button>
                </div>
            </div>
        `;

        const nextBtn = fbContainer.querySelector('#pl-next-btn');
        if (nextBtn) {
            nextBtn.focus();
            nextBtn.addEventListener('click', () => {
                _currentIndex++;
                if (_currentIndex < _queue.length) {
                    _render();
                } else {
                    _state = 'summary';
                    _render();
                }
            });
        }
    }

    function _renderSettings() {
        const pool = _poolFor(_activeTab);
        const tabMeta = TABS.find(t => t.id === _activeTab) || TABS[0];

        return `
            <div class="gd-settings">
                <div class="gd-tabs-bar" style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">
                    ${TABS.map(t => `
                        <button type="button" class="gd-tab-btn ${t.id === _activeTab ? 'active' : ''}" data-tab="${t.id}" style="padding: 8px 14px; border-radius: var(--radius-sm); border: 1px solid ${t.id === _activeTab ? 'var(--accent)' : 'var(--border)'}; background: ${t.id === _activeTab ? 'var(--wash)' : 'transparent'}; font-weight: ${t.id === _activeTab ? '600' : '400'}; cursor: pointer;">
                            ${_esc(t.label)}
                        </button>
                    `).join('')}
                </div>

                <div class="gd-tab-desc-box" style="margin-bottom: 24px; padding: 14px 16px; background: var(--wash, rgba(16,42,71,0.03)); border-radius: var(--radius-md);">
                    <h3 style="font-size: 1.1rem; margin: 0 0 6px 0; color: var(--text);">${_esc(tabMeta.label)}</h3>
                    <p style="margin: 0; font-size: 14px; color: var(--muted);">${_esc(tabMeta.desc)}</p>
                    <div style="margin-top: 8px; font-size: 13px; color: var(--secondary);">Available exercises in this topic: ${pool.length}</div>
                </div>

                <div class="gd-config-group" style="margin-bottom: 24px;">
                    <label style="display: block; font-weight: 600; font-size: 14px; margin-bottom: 10px;">Number of questions:</label>
                    <div class="gd-count-chips" style="display: flex; gap: 10px;">
                        ${[5, 10, 15, 20].map(cnt => `
                            <button type="button" class="gd-chip ${cnt === _questionCount ? 'active' : ''}" data-count="${cnt}" style="padding: 6px 14px; border-radius: 16px; border: 1px solid var(--border); background: ${cnt === _questionCount ? 'var(--accent)' : 'var(--card)'}; color: ${cnt === _questionCount ? '#fff' : 'var(--text)'}; cursor: pointer;">
                                ${cnt}
                            </button>
                        `).join('')}
                    </div>
                </div>

                <div class="gd-start-actions">
                    <button type="button" class="vbtn vbtn-primary" id="pl-start-btn" style="padding: 10px 24px; font-size: 15px; font-weight: 600;">
                        Start Practice &rarr;
                    </button>
                </div>
            </div>
        `;
    }

    function _renderQuiz() {
        const item = _queue[_currentIndex];
        const tabMeta = TABS.find(t => t.id === _activeTab) || TABS[0];
        const progress = Math.round(((_currentIndex) / _queue.length) * 100);

        const promptSentence = _esc(item.sentence).replace('___', '<span class="gd-blank" style="display: inline-block; min-width: 60px; border-bottom: 2px solid var(--accent); color: var(--accent); font-weight: 600; text-align: center;">&nbsp;?&nbsp;</span>');
        const options = item.options.slice();

        return `
            <div class="gd-hud" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 0 4px;">
                <button type="button" class="vbtn-link" id="pl-exit-btn" style="font-size: 13px; color: var(--muted); cursor: pointer; background: none; border: none;">&larr; Exit to Topics</button>
                <div style="font-size: 13px; font-weight: 600; color: var(--secondary);">Question ${_currentIndex + 1} of ${_queue.length}</div>
            </div>

            <div class="gd-progress-track" style="height: 4px; background: var(--border); border-radius: 2px; margin-bottom: 24px; overflow: hidden;">
                <div class="gd-progress-fill" style="height: 100%; width: ${progress}%; background: var(--accent); transition: width 0.25s ease;"></div>
            </div>

            <div class="gd-hud-meta" style="margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                <span class="gd-hud-skill-tag" style="font-size: 12px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: var(--muted);">${_esc(tabMeta.label)}</span>
                <span style="font-size: 13px; font-weight: 500; color: var(--secondary); font-variant-numeric: tabular-nums;">Score: ${_score}</span>
            </div>

            <div class="gd-exercise" style="max-width: 540px; margin: 0 auto; padding: 0 16px;">
                <p class="gd-question" style="font-family: var(--font-display, Georgia, serif); font-size: 1.25rem; line-height: 1.5; color: var(--text); margin: 18px 0 22px;">
                    ${promptSentence}
                </p>

                <div class="gd-options" style="display: flex; flex-direction: column; gap: 8px;">
                    ${options.map((opt, i) => `
                        <button type="button" class="gd-option" data-opt="${_esc(opt)}" style="display: flex; align-items: center; gap: 12px; padding: 12px 16px; border: 1px solid var(--border); border-radius: var(--radius-md); background: var(--card); text-align: left; cursor: pointer; font-size: 15px;">
                            <span class="lsn-key-hint" style="display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px; border-radius: 50%; background: var(--wash); font-size: 12px; font-weight: 600; color: var(--muted);">${i + 1}</span>
                            <span>${_esc(opt)}</span>
                        </button>
                    `).join('')}
                </div>

                <div id="pl-quiz-feedback"></div>
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
                    <div style="font-size: 2.4rem; font-family: var(--font-display, Georgia, serif); font-weight: 600; color: ${pct >= 80 ? 'var(--success, #2e7d32)' : (pct >= 50 ? 'var(--ochre, #855A08)' : 'var(--danger, #d32f2f)')}; margin: 12px 0;">
                        ${pct}%
                    </div>
                    <p class="gd-clean-desc" style="margin-bottom: 24px;">You answered ${_score} of ${total} questions correctly.</p>

                    ${_mistakes.length > 0 ? `
                        <div style="text-align: left; margin: 24px 0 20px; border-top: 1px solid var(--border); padding-top: 18px;">
                            <h4 style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 12px;">Points to review</h4>
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                ${_mistakes.map(m => `
                                    <div style="padding: 12px 14px; background: var(--wash, rgba(16,42,71,0.03)); border-left: 3px solid var(--danger, #d32f2f); border-radius: var(--radius-sm);">
                                        <div style="font-weight: 500; font-size: 14.5px; color: var(--text); margin-bottom: 4px;">${_esc(m.item.sentence.replace('___', m.item.answer))}</div>
                                        <div style="font-size: 13px; color: var(--muted);">${_esc(m.item.rule)}</div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : `
                        <p style="font-weight: 600; color: var(--success, #2e7d32); margin-bottom: 20px;">Świetnie! No mistakes made.</p>
                    `}

                    <div class="gd-clean-actions" style="margin-top: 24px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                        <button type="button" class="vbtn vbtn-primary" id="pl-restart-btn">Practise Again</button>
                        <button type="button" class="vbtn vbtn-secondary" id="pl-choose-tab-btn">Change Topic</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _handleGlobalKey(e) {
        if (!_container || _state !== 'quiz') return;

        const nextBtn = document.getElementById('pl-next-btn');
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
            _container.querySelectorAll('.gd-tab-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    _activeTab = btn.dataset.tab;
                    _render();
                });
            });

            _container.querySelectorAll('.gd-chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    _questionCount = parseInt(btn.dataset.count, 10);
                    _container.querySelectorAll('.gd-chip').forEach(b => b.classList.toggle('active', b === btn));
                });
            });

            const startBtn = _container.querySelector('#pl-start-btn');
            if (startBtn) {
                startBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }
        }

        if (_state === 'quiz') {
            const exitBtn = _container.querySelector('#pl-exit-btn');
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
            const restartBtn = _container.querySelector('#pl-restart-btn');
            if (restartBtn) {
                restartBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }

            const chooseTabBtn = _container.querySelector('#pl-choose-tab-btn');
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

    function stop() {
        if (_keyHandlerAttached && typeof document !== 'undefined') {
            document.removeEventListener('keydown', _handleGlobalKey);
            _keyHandlerAttached = false;
        }
        _state = 'settings';
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
    window.PlGrammarStudio = PlGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PlGrammarStudio;
}
