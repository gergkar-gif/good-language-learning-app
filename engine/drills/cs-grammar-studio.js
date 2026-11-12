// ============================================
// CZECH GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated Czech driller addressing the 5 core contrastive bottlenecks:
// 1. 7 českých pádů (7 Cases): Nominativ through Instrumentál, everyday Vocative (Petře!), masculine animacy (psa/stůl).
// 2. Aspekt (Dokonavý a nedokonavý): Imperfective habit/process vs perfective completed action, future tense (budu psát vs napíšu).
// 3. Slovesa pohybu: Determinate vs indeterminate (jít/chodit, jet/jezdit) and directional prefixes (přijít, odejít, odjet, dojet).
// 4. Minulý čas a podmiňovací způsob: Auxiliary clitics (jsem, jsi, -s), conditionals (bych, bys, by), Wackernagel 2nd position.
// 5. Spisovná vs Obecná čeština & Zvuky: Standard vs colloquial awareness, vowel quantity (dům/domu), fleeting-e (pes/psa), palatalizations.

const CsGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'cases', label: '7 českých pádů', desc: 'Nominativ through Instrumentál, Vocative address (Petře!), masculine animacy (psa vs stůl)' },
        { id: 'aspect', label: 'Aspekt (Dokonavý / Nedokonavý)', desc: 'Imperfective process/habit vs perfective completed event, future tense (budu číst vs přečtu)' },
        { id: 'motion_verbs', label: 'Slovesa pohybu', desc: 'Determinate vs indeterminate (jít/chodit, jet/jezdit) and directional prefixes (přijít, odejít, odjet)' },
        { id: 'past_conditionals', label: 'Minulý čas a kondicionál', desc: 'Past auxiliary clitics (jsem, jsi, -s), conditional (bych, bys, by), Wackernagel 2nd position' },
        { id: 'spoken_czech', label: 'Spisovná vs Obecná čeština', desc: 'Standard vs colloquial Czech, vowel quantity (dům/domu), fleeting-e (pes/psa), palatalizations' }
    ];

    const CASES_ITEMS = [
        {
            sentence: 'Ahoj ___, jak se dnes máš?',
            options: ['Petře', 'Petr', 'Petra', 'Petrem'],
            answer: 'Petře',
            translation: 'Hi Petr, how are you today?',
            rule: 'Direct address requires the Vocative (5. pád): hard masculine stems in -r take -e with palatalization (Petr -> Petře).'
        },
        {
            sentence: 'Dobrý den, pane ___!',
            options: ['profesore', 'profesor', 'profesora', 'profesorem'],
            answer: 'profesore',
            translation: 'Good day, Professor!',
            rule: 'Masculine title address uses the Vocative in -e: pan profesor -> pane profesore.'
        },
        {
            sentence: 'Ahoj ___, ráda tě zase vidím!',
            options: ['Jano', 'Jana', 'Janu', 'Janě'],
            answer: 'Jano',
            translation: 'Hi Jana, nice to see you again!',
            rule: 'Feminine names in -a form the Vocative with -o: Jana -> Jano.'
        },
        {
            sentence: 'Vidím na ulici tvého nového ___.',
            options: ['psa', 'pes', 'psem', 'psu'],
            answer: 'psa',
            translation: 'I see your new dog on the street.',
            rule: 'Masculine animate direct objects take the Genitive ending in the Accusative: pes -> psa.'
        },
        {
            sentence: 'Koupil jsem si včera nový pracovní ___.',
            options: ['stůl', 'stolu', 'stolem', 'stoly'],
            answer: 'stůl',
            translation: 'Yesterday I bought a new work table.',
            rule: 'Masculine inanimate direct objects retain the Nominative form in the Accusative: stůl remains stůl.'
        },
        {
            sentence: 'Mluvili jsme o tom novém ___ filmu.',
            options: ['českém', 'český', 'českého', 'českým'],
            answer: 'českém',
            translation: 'We talked about that new Czech film.',
            rule: 'Preposition "o" (about) governs the Locative (6. pád): o novém českém filmu.'
        },
        {
            sentence: 'Kávu piju vždycky bez ___.',
            options: ['cukru', 'cukr', 'cukrem', 'cukruje'],
            answer: 'cukru',
            translation: 'I always drink coffee without sugar.',
            rule: 'Preposition "bez" (without) strictly requires the Genitive (2. pád): bez cukru.'
        },
        {
            sentence: 'Pojedeme na dovolenou s našimi dobrými ___.',
            options: ['přáteli', 'přátelé', 'přátel', 'přátelích'],
            answer: 'přáteli',
            translation: 'We will go on holiday with our good friends.',
            rule: 'Preposition "s" (with) requires the Instrumental (7. pád): s dobrými přáteli.'
        },
        {
            sentence: 'Pracuje jako zkušený programátor v mezinárodní ___.',
            options: ['firmě', 'firma', 'firmu', 'firmou'],
            answer: 'firmě',
            translation: 'He works as an experienced programmer in an international company.',
            rule: 'Preposition "v" (in - static location) requires the Locative (6. pád): v mezinárodní firmě.'
        },
        {
            sentence: 'Jdu zítra do ___ na nákup.',
            options: ['obchodu', 'obchod', 'obchodě', 'obchodem'],
            answer: 'obchodu',
            translation: 'Tomorrow I am going to the shop for groceries.',
            rule: 'Preposition "do" (into/to - motion toward) requires the Genitive (2. pád): do obchodu.'
        },
        {
            sentence: 'Dám ten dopis tvé ___.',
            options: ['sestře', 'sestra', 'sestru', 'sestrou'],
            answer: 'sestře',
            translation: 'I will give that letter to your sister.',
            rule: 'Indirect objects (giving to someone) take the Dative (3. pád): dát sestře.'
        },
        {
            sentence: 'Bydlíme v krásném starém ___.',
            options: ['domě', 'dům', 'domu', 'domem'],
            answer: 'domě',
            translation: 'We live in a beautiful old house.',
            rule: 'Locative singular of dům is v domě (vowel shift ů -> o plus -ě).'
        },
        {
            sentence: 'Potkal jsem včera svého bývalého ___.',
            options: ['kolegu', 'kolega', 'kolegou', 'kolegovi'],
            answer: 'kolegu',
            translation: 'Yesterday I met my former colleague.',
            rule: 'Masculine animate nouns ending in -a take -u in the Accusative: kolega -> kolegu.'
        },
        {
            sentence: 'Petr se stal známým ___.',
            options: ['lékařem', 'lékař', 'lékaře', 'lékaři'],
            answer: 'lékařem',
            translation: 'Petr became a well-known doctor.',
            rule: 'The verb stát se (to become) requires the predicate in the Instrumental (7. pád): lékařem.'
        },
        {
            sentence: 'Děti si hrají na dětském ___.',
            options: ['hřišti', 'hřiště', 'hřištěm', 'hřišť'],
            answer: 'hřišti',
            translation: 'Children are playing on the playground.',
            rule: 'Neuter nouns in -ště take -i in the Locative: na hřišti.'
        },
        {
            sentence: 'Požádal jsem o pomoc pana ___.',
            options: ['Novotného', 'Novotný', 'Novotnému', 'Novotným'],
            answer: 'Novotného',
            translation: 'I asked Mr. Novotný for help.',
            rule: 'Surnames of adjectival declension (Novotný) decline like adjectives: Accusative animate Novotného.'
        },
        {
            sentence: 'Na stole leží pět velkých ___.',
            options: ['jablek', 'jablka', 'jablko', 'jablcích'],
            answer: 'jablek',
            translation: 'On the table lie five large apples.',
            rule: 'Numerals from 5 upwards govern the Genitive plural: pět jablek (with fleeting-e).'
        },
        {
            sentence: 'Podej mi prosím kousek ___.',
            options: ['chleba', 'chléb', 'chlebem', 'chlebě'],
            answer: 'chleba',
            translation: 'Please pass me a piece of bread.',
            rule: 'Partitive genitive after quantity nouns (kousek): kousek chleba (or chlebu).'
        },
        {
            sentence: 'Mluvíme o ___ městě Praze.',
            options: ['hlavním', 'hlavní', 'hlavního', 'hlavnímě'],
            answer: 'hlavním',
            translation: 'We are talking about the capital city Prague.',
            rule: 'Soft adjectives (hlavní) have the Locative ending -ím: o hlavním městě.'
        },
        {
            sentence: 'Učitel vysvětluje novou látku celému ___.',
            options: ['ročníku', 'ročník', 'ročníkem', 'ročníka'],
            answer: 'ročníku',
            translation: 'The teacher explains the new material to the whole year group.',
            rule: 'Dative singular of masculine inanimate nouns ends in -u: celému ročníku.'
        }
    ];

    const ASPECT_ITEMS = [
        {
            sentence: 'Každý den ráno ___ hodinu noviny.',
            options: ['čtu', 'přečtu', 'přečetl', 'dočtu'],
            answer: 'čtu',
            translation: 'Every day in the morning I read the newspaper for an hour.',
            rule: 'Habitual or repeated actions require the Imperfective aspect: čtu (from číst).'
        },
        {
            sentence: 'Dnes večer určitě ___ celou tuto knihu.',
            options: ['přečtu', 'čtu', 'budu číst', 'čítávám'],
            answer: 'přečtu',
            translation: 'This evening I will definitely finish reading this whole book.',
            rule: 'Completed future results use the present tense of the Perfective verb: přečtu.'
        },
        {
            sentence: 'Zítra v pět hodin odpoledne ___ ten důležitý úkol.',
            options: ['budu dělat', 'udělám', 'udělal', 'dodělám'],
            answer: 'budu dělat',
            translation: 'Tomorrow at five in the afternoon I will be doing that important task.',
            rule: 'Process in progress at a specific future moment uses compound imperfective future: budu dělat.'
        },
        {
            sentence: 'Až přijdeš domů, už to všechno ___.',
            options: ['udělám', 'dělám', 'budu dělat', 'dělávám'],
            answer: 'udělám',
            translation: 'By the time you come home, I will already have done it all.',
            rule: 'Completed accomplishment before or by a future point requires perfective udělám.'
        },
        {
            sentence: 'Včera jsem dvě hodiny ___ e-maily.',
            options: ['psal', 'napsal', 'dopsal', 'vepsal'],
            answer: 'psal',
            translation: 'Yesterday I spent two hours writing emails.',
            rule: 'Duration expressions (dvě hodiny) focus on process and require imperfective psal.'
        },
        {
            sentence: 'Konečně jsem ten dopis pro úřad ___.',
            options: ['napsal', 'psal', 'psávám', 'zapisoval'],
            answer: 'napsal',
            translation: 'I finally wrote the letter for the authority.',
            rule: 'Finished, completed achievement (konečně) takes perfective napsal.'
        },
        {
            sentence: 'Pravidelně ___ v supermarketu u nádraží.',
            options: ['nakupuji', 'nakoupím', 'nakoupil', 'skoupím'],
            answer: 'nakupuji',
            translation: 'I regularly shop at the supermarket near the station.',
            rule: 'Regular, repeated habitual action (pravidelně) requires imperfective nakupuji / nakupuju.'
        },
        {
            sentence: 'Zítra ráno tam půjdu a rychle ___ všechno potřebné.',
            options: ['nakoupím', 'nakupuji', 'budu nakupovat', 'kupovávám'],
            answer: 'nakoupím',
            translation: 'Tomorrow morning I will go there and quickly buy everything needed.',
            rule: 'Single completed future action takes perfective nakoupím.'
        },
        {
            sentence: 'Číšník přinesl účet a my jsme hned ___.',
            options: ['zaplatili', 'platili', 'budeme platit', 'přeplatili'],
            answer: 'zaplatili',
            translation: 'The waiter brought the bill and we paid immediately.',
            rule: 'Sequential completed action in a narrative takes perfective zaplatili.'
        },
        {
            sentence: 'Když jsem žil v Praze, za nájem jsem ___ deset tisíc korun měsíčně.',
            options: ['platil', 'zaplatil', 'doplatil', 'připlatil'],
            answer: 'platil',
            translation: 'When I lived in Prague, I paid ten thousand crowns a month for rent.',
            rule: 'Habitual repeated monthly payments require imperfective platil.'
        },
        {
            sentence: 'Kdy obvykle ___ do postele?',
            options: ['chodíš', 'jdeš', 'přijdeš', 'dojdeš'],
            answer: 'chodíš',
            translation: 'When do you usually go to bed?',
            rule: 'Regular habit (obvykle) requires iterative/indeterminate imperfective chodíš.'
        },
        {
            sentence: 'Počkej na mě, právě teď ___ za tebou!',
            options: ['jdu', 'chodím', 'půjdu', 'dojdu'],
            answer: 'jdu',
            translation: 'Wait for me, right now I am coming over to you!',
            rule: 'Specific single ongoing movement right now requires determinate imperfective jdu.'
        },
        {
            sentence: 'Petr mi slíbil, že mi zítra ráno ___.',
            options: ['zavolá', 'volá', 'bude volat', 'přivolává'],
            answer: 'zavolá',
            translation: 'Petr promised me that he will call me tomorrow morning.',
            rule: 'Single completed communicative act in future takes perfective zavolá.'
        },
        {
            sentence: 'Celé odpoledne jsem se snažil pracovat, ale někdo mi neustále ___.',
            options: ['volal', 'zavolal', 'odvolal', 'přivolal'],
            answer: 'volal',
            translation: 'I was trying to work all afternoon, but someone kept calling me.',
            rule: 'Repeated annoying interruptions (neustále) take imperfective volal.'
        },
        {
            sentence: 'Už jsi někdy ___ pravé české pivo v Plzni?',
            options: ['pil', 'vypil', 'napil', 'píval'],
            answer: 'pil',
            translation: 'Have you ever drunk real Czech beer in Plzeň?',
            rule: 'General experiential questions (ever in your life?) use imperfective pil.'
        },
        {
            sentence: 'Byl tak žíznivý, že na jedno napití ___ celou sklenici vody.',
            options: ['vypil', 'pil', 'popíjel', 'pije'],
            answer: 'vypil',
            translation: 'He was so thirsty that in one gulp he drank up the whole glass of water.',
            rule: 'Total consumption / exhaustion of an object takes perfective vypil.'
        },
        {
            sentence: 'Profesor celý semestr ___ studenty českou historii.',
            options: ['učil', 'naučil', 'vyučil', 'poučil'],
            answer: 'učil',
            translation: 'The professor taught the students Czech history the whole semester.',
            rule: 'Duration of teaching activity takes processive imperfective učil.'
        },
        {
            sentence: 'Za tři měsíce intenzivního kurzu se skvěle ___ česky.',
            options: ['naučil', 'učil', 'učíval', 'vyučoval'],
            answer: 'naučil',
            translation: 'In three months of an intensive course he learned Czech brilliantly.',
            rule: 'Result of learning (achieved state) takes perfective naučil se.'
        },
        {
            sentence: 'Musíme ___ okno, protože je v místnosti velký hluk.',
            options: ['zavřít', 'zavírat', 'uzavírat', 'přivírat'],
            answer: 'zavřít',
            translation: 'We must close the window because there is a lot of noise in the room.',
            rule: 'Single completed act of closing takes perfective zavřít.'
        },
        {
            sentence: 'V noci se v tomto hotelu vchodové dveře vždycky v jedenáct ___.',
            options: ['zavírají', 'zavřou', 'zavřely', 'uzavřou'],
            answer: 'zavírají',
            translation: 'At night in this hotel the entrance door always closes at eleven.',
            rule: 'Routine scheduled rule (vždycky) takes imperfective zavírají.'
        }
    ];

    const MOTION_ITEMS = [
        {
            sentence: 'Kam právě teď ___ tak rychle?',
            options: ['jdeš', 'chodíš', 'přijdeš', 'pojdeš'],
            answer: 'jdeš',
            translation: 'Where are you going so fast right now?',
            rule: 'Single ongoing movement on foot in progress right now takes determinate jít: jdeš.'
        },
        {
            sentence: 'Do práce obvykle ___ pěšky, ale dnes jedu tramvají.',
            options: ['chodím', 'jdu', 'půjdu', 'dojdu'],
            answer: 'chodím',
            translation: 'I usually walk to work, but today I am taking the tram.',
            rule: 'Habitual repeated walking (obvykle) requires indeterminate chodit: chodím.'
        },
        {
            sentence: 'Dnes ráno ___ do Brna autem na pracovní schůzku.',
            options: ['jedu', 'jezdím', 'půjdu', 'chodím'],
            answer: 'jedu',
            translation: 'This morning I am driving to Brno for a business meeting.',
            rule: 'Single ongoing vehicular motion requires determinate jet: jedu.'
        },
        {
            sentence: 'Každé léto ___ na dovolenou k moři do Chorvatska.',
            options: ['jezdíme', 'jedeme', 'půjdeme', 'dojedeme'],
            answer: 'jezdíme',
            translation: 'Every summer we go on holiday to the sea in Croatia.',
            rule: 'Annual repeated trip by vehicle takes indeterminate jezdit: jezdíme.'
        },
        {
            sentence: 'Vlak z Vídně ___ do Prahy přesně na čas.',
            options: ['přijel', 'odjel', 'vyjel', 'zajel'],
            answer: 'přijel',
            translation: 'The train from Vienna arrived in Prague right on time.',
            rule: 'Prefix při- denotes arrival at a destination: přijel.'
        },
        {
            sentence: 'Rychlík do Berlína právě ___ z prvního nástupiště.',
            options: ['odjel', 'přijel', 'dojel', 'najel'],
            answer: 'odjel',
            translation: 'The express train to Berlin has just departed from platform one.',
            rule: 'Prefix od- denotes departure away from an origin: odjel.'
        },
        {
            sentence: 'Konečně jsme po dlouhé cestě v pořádku ___ domů.',
            options: ['dojeli', 'odjeli', 'vyjeli', 'přejeli'],
            answer: 'dojeli',
            translation: 'We finally reached home safely after a long trip.',
            rule: 'Prefix do- signifies reaching the final destination: dojet.'
        },
        {
            sentence: 'Kdy zítra ráno ___ z hotelu na letiště?',
            options: ['vyrazíme', 'přirazíme', 'dorazíme', 'odrazíme'],
            answer: 'vyrazíme',
            translation: 'When tomorrow morning do we set off from the hotel to the airport?',
            rule: 'Setting off on a journey uses vyrazit.'
        },
        {
            sentence: 'Byl unavený, a tak ___ z kanceláře dřív.',
            options: ['odešel', 'přišel', 'došel', 'našel'],
            answer: 'odešel',
            translation: 'He was tired, so he left the office earlier.',
            rule: 'Prefix od- on foot expresses leaving: odejít (odešel).'
        },
        {
            sentence: 'Hosté už ___ na oslavu a sedí v obývacím pokoji.',
            options: ['přišli', 'odešli', 'došli', 'prošli'],
            answer: 'přišli',
            translation: 'The guests have already arrived at the party and are sitting in the living room.',
            rule: 'Arrival on foot takes přijít (přišli).'
        },
        {
            sentence: 'Včera nám ___ mléko, musím skočit do obchodu.',
            options: ['došlo', 'přišlo', 'odešlo', 'vyšlo'],
            answer: 'došlo',
            translation: 'Yesterday we ran out of milk, I need to pop to the shop.',
            rule: 'Idiom dojít (došlo mléko) means to run out of something.'
        },
        {
            sentence: 'Pomohl babičce ___ těžké tašky do třetího patra.',
            options: ['vynést', 'snést', 'odnést', 'zanést'],
            answer: 'vynést',
            translation: 'He helped grandmother carry the heavy bags up to the third floor.',
            rule: 'Carrying upward (to 3rd floor) uses prefix vy-: vynést.'
        },
        {
            sentence: 'Pošťák každý den ___ dopisy a balíky.',
            options: ['roznáší', 'nese', 'vynáší', 'odnáší'],
            answer: 'roznáší',
            translation: 'The postman delivers letters and parcels every day.',
            rule: 'Distributing to multiple places uses prefix roz-: roznášet.'
        },
        {
            sentence: 'Rodiče ___ ráno děti autem do školy.',
            options: ['vozí', 'vezou', 'nosí', 'vedou'],
            answer: 'vozí',
            translation: 'Parents drive their children to school by car in the morning.',
            rule: 'Repeated transport by vehicle uses vozit (vozí).'
        },
        {
            sentence: 'Učitel ___ žáky na exkurzi do Národního muzea.',
            options: ['vede', 'veze', 'nosí', 'vodí'],
            answer: 'vede',
            translation: 'The teacher is leading the pupils on an excursion to the National Museum.',
            rule: 'Leading people on foot currently in progress uses determinate vést (vede).'
        },
        {
            sentence: 'Musíme ___ přes tuto rušnou křižovatku.',
            options: ['přejít', 'přijít', 'odejít', 'dojít'],
            answer: 'přejít',
            translation: 'We have to cross this busy intersection.',
            rule: 'Prefix pře- indicates crossing from one side to the other: přejít.'
        },
        {
            sentence: 'Během cesty do Brna jsme se na chvíli ___ v Kolíně.',
            options: ['zastavili', 'postavili', 'vystavili', 'odstavili'],
            answer: 'zastavili',
            translation: 'During the journey to Brno we stopped for a while in Kolín.',
            rule: 'Stopping during movement uses zastavit se.'
        },
        {
            sentence: 'Kdy konečně ___ ten nový film v kině?',
            options: ['vyjde', 'dojde', 'zajde', 'přejde'],
            answer: 'vyjde',
            translation: 'When will that new movie finally come out in the cinema?',
            rule: 'Coming out / publication / release uses vyjít (vyjde).'
        },
        {
            sentence: 'Rád ___ o víkendu po horách.',
            options: ['chodím', 'jdu', 'půjdu', 'dojdu'],
            answer: 'chodím',
            translation: 'I like walking around the mountains at the weekend.',
            rule: 'Recreational repeated hiking uses indeterminate chodit.'
        },
        {
            sentence: 'Autobus ___ z Prahy v osm hodin ráno a v devět je v Plzni.',
            options: ['odjíždí', 'přijíždí', 'dojíždí', 'projíždí'],
            answer: 'odjíždí',
            translation: 'The bus departs from Prague at eight in the morning and is in Plzeň at nine.',
            rule: 'Regular scheduled departure by vehicle uses odjíždět.'
        }
    ];

    const PAST_COND_ITEMS = [
        {
            sentence: 'Včera ___ tě v tramvaji, ale nevšiml sis mě.',
            options: ['jsem viděl', 'viděl jsem', 'viděl bych', 'jsem byl viděl'],
            answer: 'jsem viděl',
            translation: 'Yesterday I saw you on the tram, but you did not notice me.',
            rule: 'Wackernagel law: auxiliary clitic jsem belongs in second syntactic position (Včera jsem tě viděl).'
        },
        {
            sentence: 'Ty ___ tam včera nebyl?',
            options: ['jsi', 'jsem', 'byl', 'budeš'],
            answer: 'jsi',
            translation: 'You were not there yesterday?',
            rule: '2nd person singular past auxiliary is jsi: Ty jsi tam nebyl.'
        },
        {
            sentence: 'Kde ___ včera celý večer?',
            options: ['byls', 'byl jsi', 'byl', 'bylste'],
            answer: 'byls',
            translation: 'Where were you yesterday all evening?',
            rule: 'In informal Czech, auxiliary jsi contracts onto the past participle as -s (byl + s = byls).'
        },
        {
            sentence: 'My ___ o tom vůbec nevěděli.',
            options: ['jsme', 'jste', 'byli', 'jsou'],
            answer: 'jsme',
            translation: 'We did not know about it at all.',
            rule: '1st person plural past tense requires auxiliary jsme.'
        },
        {
            sentence: 'Kdybych měl víc peněz, ___ do Japonska.',
            options: ['jel bych', 'bych jel', 'bychom jeli', 'bychom jet'],
            answer: 'jel bych',
            translation: 'If I had more money, I would go to Japan.',
            rule: 'Conditional 1st person singular uses l-participle + bych: jel bych.'
        },
        {
            sentence: 'My ___ vám rádi pomohli, ale nemáme čas.',
            options: ['bychom', 'byjsme', 'byste', 'by'],
            answer: 'bychom',
            translation: 'We would gladly help you, but we do not have time.',
            rule: 'Standard Czech conditional 1st person plural is strictly bychom (byjsme is a non-standard colloquial error).'
        },
        {
            sentence: 'Vy ___ to dokázali vyřešit bez naší pomoci?',
            options: ['byste', 'byste byli', 'bychom', 'by jste'],
            answer: 'byste',
            translation: 'Would you be able to solve it without our help?',
            rule: '2nd person plural conditional particle is written together as byste.'
        },
        {
            sentence: 'Kdyby Petr víc studoval, ___ tu zkoušku.',
            options: ['udělal by', 'udělal bys', 'udělal bych', 'udělal'],
            answer: 'udělal by',
            translation: 'If Petr studied more, he would pass the exam.',
            rule: '3rd person conditional uses participle + invariant by: udělal by.'
        },
        {
            sentence: 'Chtěl jsem, ___ mi s tím pomohl.',
            options: ['abys', 'aby', 'abych', 'abyste'],
            answer: 'abys',
            translation: 'I wanted you to help me with that.',
            rule: 'Conjunction aby with 2nd person singular contracts to abys.'
        },
        {
            sentence: 'Přišel jsem včas, ___ nezmeškal začátek filmu.',
            options: ['abych', 'abys', 'aby', 'abychom'],
            answer: 'abych',
            translation: 'I arrived on time so that I would not miss the start of the movie.',
            rule: 'Purpose clause with 1st person subject uses abych.'
        },
        {
            sentence: 'Včera ___ se nám ten výlet moc líbil.',
            options: ['se nám', 'nám se', 'nám', 'se'],
            answer: 'se nám',
            translation: 'Yesterday we liked that trip very much.',
            rule: 'Clitic cluster ordering: reflexive se precedes dative pronoun nám.'
        },
        {
            sentence: 'Proč ___ mi to neřekl dřív?',
            options: ['jsi', 'jsem', 'jste', 'jsme'],
            answer: 'jsi',
            translation: 'Why didn’t you tell me earlier?',
            rule: '2nd person singular past auxiliary in 2nd position after question word: Proč jsi mi to neřekl.'
        },
        {
            sentence: 'Děti včera celý den ___ na zahradě.',
            options: ['si hrály', 'si hráli', 'hrály si', 'hráli'],
            answer: 'si hrály',
            translation: 'Yesterday the children played in the garden all day.',
            rule: 'Subject děti is grammatically feminine plural in past agreement: hrály si.'
        },
        {
            sentence: 'Muži unaveně ___ po těžké práci.',
            options: ['odpočívali', 'odpočívaly', 'odpočívalo', 'odpočívat'],
            answer: 'odpočívali',
            translation: 'The men rested tiredly after hard work.',
            rule: 'Masculine animate plural subject takes -i in the past participle: muži odpočívali.'
        },
        {
            sentence: 'Ženy včera dlouho ___ v parku.',
            options: ['diskutovaly', 'diskutovali', 'diskutovala', 'diskutovalo'],
            answer: 'diskutovaly',
            translation: 'The women discussed in the park for a long time yesterday.',
            rule: 'Feminine plural subject takes -y in the past participle: ženy diskutovaly.'
        },
        {
            sentence: 'Auta na parkovišti celou noc ___.',
            options: ['stála', 'stály', 'stáli', 'stál'],
            answer: 'stála',
            translation: 'The cars stood in the car park all night.',
            rule: 'Neuter plural subject (auta) takes -a in the past participle: auta stála.'
        },
        {
            sentence: '___ jsem se s ním včera odpoledne.',
            options: ['Sešel', 'Jsem sešel', 'Sešel jsem', 'Sešel se'],
            answer: 'Sešel',
            translation: 'I met with him yesterday afternoon.',
            rule: 'Auxiliary jsem cannot start a sentence; verb participle leads: Sešel jsem se.'
        },
        {
            sentence: 'Kdybych to věděl, ___ ti to.',
            options: ['byl bych řekl', 'řekl bych', 'byl bych ti řekl', 'řekl jsem'],
            answer: 'řekl bych',
            translation: 'If I had known, I would have told you.',
            rule: 'Present/general conditional expression in modern Czech: řekl bych.'
        },
        {
            sentence: '___ si ještě jeden šálek čaje?',
            options: ['Dal byste', 'Dáte', 'Dával byste', 'Dáte si'],
            answer: 'Dal byste',
            translation: 'Would you have another cup of tea?',
            rule: 'Polite offer uses conditional: Dal byste si (vy-form).'
        },
        {
            sentence: 'Byli bychom rádi, ___ s námi zůstali na večeři.',
            options: ['kdybyste', 'kdybychom', 'kdyby', 'kdybys'],
            answer: 'kdybyste',
            translation: 'We would be glad if you stayed with us for dinner.',
            rule: 'Conditional conjunction with 2nd person plural vy: kdybyste.'
        }
    ];

    const SPOKEN_CZECH_ITEMS = [
        {
            sentence: 'Spisovně: "To je dobré pivo." V obecné češtině: "To je ___ pivo."',
            options: ['dobrý', 'dobrej', 'dobrá', 'dobrou'],
            answer: 'dobrej',
            translation: 'Standard: "That is good beer." Common Czech: "To je dobrý/dobrej pivo."',
            rule: 'Colloquial Common Czech often replaces standard -ý with -ej (dobrej) or standard neuter -é with -ý/-ej.'
        },
        {
            sentence: 'Spisovně: "Oni pracují v továrně." V běžné mluvě často uslyšíte: "Oni ___ v továrně."',
            options: ['pracujou', 'pracují', 'pracuj', 'pracoval'],
            answer: 'pracujou',
            translation: 'Standard: "They work in the factory." Colloquial: "Oni pracujou v továrně."',
            rule: 'In 3rd person plural, colloquial Czech predominantly uses -ou instead of standard -í: pracujou.'
        },
        {
            sentence: 'Spisovně: "V kolik hodin to začíná?" Hovorově v Praze: "V kolik hodin to ___?"',
            options: ['začíná', 'začínaj', 'začne', 'začínat'],
            answer: 'začíná',
            translation: 'At what time does it begin?',
            rule: 'Standard and spoken forms coincide here, showing that not every verb alters.'
        },
        {
            sentence: 'V Praze na ulici často uslyšíte prothetické v-: místo "okno" lidé řeknou "___".',
            options: ['vokno', 'okno', 'ukno', 'hokno'],
            answer: 'vokno',
            translation: 'In Prague people often say "vokno" instead of standard "okno".',
            rule: 'Prothetic v- before initial o- is a hallmark of Common Czech (vokno, von, vodejít).'
        },
        {
            sentence: 'Spisovně: "Byl jsem tam s děvčaty." Hovorově: "Byl jsem tam s ___."',
            options: ['holkama', 'holkami', 'děvčata', 'holkách'],
            answer: 'holkama',
            translation: 'Standard: "I was there with girls." Colloquial: "Byl jsem tam s holkama."',
            rule: 'Universal colloquial Instrumental plural ending is -ama/-ema: s holkama, s klukama.'
        },
        {
            sentence: 'Podstatné jméno "dům" má v 2. pádě jednotného čísla tvar "___".',
            options: ['domu', 'důmu', 'důma', 'domem'],
            answer: 'domu',
            translation: 'The noun "dům" has the form "domu" in Genitive singular.',
            rule: 'Vowel shortening/alternation ů -> o occurs across oblique cases: dům -> domu, stůl -> stolu.'
        },
        {
            sentence: 'Podstatné jméno "kůň" má v 2. pádě tvar "___".',
            options: ['koně', 'kůně', 'koňa', 'koněm'],
            answer: 'koně',
            translation: 'The noun "kůň" has the form "koně" in Genitive.',
            rule: 'Vowel alternation ů -> o: kůň -> koně.'
        },
        {
            sentence: 'Podstatné jméno "pes" má v 2. pádě tvar "___" (pohyblivé e).',
            options: ['psa', 'pesa', 'psem', 'psovi'],
            answer: 'psa',
            translation: 'The noun "pes" has the form "psa" in Genitive (fleeting e).',
            rule: 'Fleeting e (pohyblivé e) drops out when endings are added: pes -> psa, den -> dne.'
        },
        {
            sentence: 'Podstatné jméno "otec" má v 4. pádě tvar "___".',
            options: ['otce', 'otece', 'otca', 'otcem'],
            answer: 'otce',
            translation: 'The noun "otec" has the form "otce" in Accusative.',
            rule: 'Fleeting e drops out: otec -> otce.'
        },
        {
            sentence: 'Podstatné jméno "den" má v 7. pádě jednotného čísla tvar "___".',
            options: ['dnem', 'denem', 'dnemu', 'dny'],
            answer: 'dnem',
            translation: 'The noun "den" has the form "dnem" in Instrumental singular.',
            rule: 'Fleeting e drops out: den -> dnem.'
        },
        {
            sentence: 'Město "Praha" má v 6. pádě (o kom, o čem) tvar "v ___".',
            options: ['Praze', 'Prazě', 'Prahe', 'Prahu'],
            answer: 'Praze',
            translation: 'The city "Praha" has the form "v Praze" in Locative.',
            rule: 'Consonant palatalization h -> z before -e in Locative: Praha -> v Praze.'
        },
        {
            sentence: 'Slovo "ruka" má v 6. pádě tvar "v ___".',
            options: ['ruce', 'ruke', 'ručce', 'rukou'],
            answer: 'ruce',
            translation: 'The word "ruka" has the form "v ruce" in Locative.',
            rule: 'Consonant palatalization k -> c before -e: ruka -> v ruce.'
        },
        {
            sentence: 'Slovo "moucha" má v 6. pádě tvar "o ___".',
            options: ['mouše', 'mouche', 'mouce', 'mouši'],
            answer: 'mouše',
            translation: 'The word "moucha" has the form "o mouše" in Locative.',
            rule: 'Consonant palatalization ch -> š before -e: moucha -> o mouše.'
        },
        {
            sentence: 'Slovo "Čech" má v 1. pádě množného čísla tvar "___".',
            options: ['Češi', 'Čechové', 'Češiť', 'Čechy'],
            answer: 'Češi',
            translation: 'The word "Čech" has the plural form "Češi".',
            rule: 'Consonant palatalization ch -> š before -i in animate plurals: Čech -> Češi.'
        },
        {
            sentence: 'Slovo "kluk" má v 1. pádě množného čísla tvar "___".',
            options: ['kluci', 'klukové', 'kluky', 'klučové'],
            answer: 'kluci',
            translation: 'The word "kluk" has the plural form "kluci".',
            rule: 'Consonant palatalization k -> c before -i: kluk -> kluci.'
        },
        {
            sentence: 'Slovo "doktor" má v 1. pádě množného čísla tvar "___".',
            options: ['doktoři', 'doktory', 'doktore', 'doktorové'],
            answer: 'doktoři',
            translation: 'The word "doktor" has the plural form "doktoři".',
            rule: 'Consonant palatalization r -> ř before -i: doktor -> doktoři.'
        },
        {
            sentence: 'Slovo "bůh" má v 1. pádě množného čísla tvar "___" nebo "bohové".',
            options: ['bozi', 'bohy', 'bůhové', 'bozové'],
            answer: 'bozi',
            translation: 'The word "bůh" has the plural form "bozi" or "bohové".',
            rule: 'Palatalization h -> z and vowel shift ů -> o: bůh -> bozi.'
        },
        {
            sentence: 'Hovorově: "Včera jsem viděl jednoho ___ chlápka."',
            options: ['divnýho', 'divného', 'divnej', 'divném'],
            answer: 'divnýho',
            translation: 'Colloquial: "Yesterday I saw a strange guy."',
            rule: 'Common Czech replaces standard adjectival Genitive/Accusative -ého with -ýho (divnýho).'
        },
        {
            sentence: 'Spisovně: "mléko", hovorově v Čechách často: "___".',
            options: ['mlíko', 'mléko', 'mlouko', 'mlýko'],
            answer: 'mlíko',
            translation: 'Standard: "mléko", colloquial: "mlíko".',
            rule: 'Vowel shift é -> í in spoken Czech (mléko -> mlíko, polévka -> polívka).'
        },
        {
            sentence: 'Spisovně: "Vezměte si kabát." Hovorově v Praze uslyšíte: "___ si kabát."',
            options: ['Vemte', 'Vezměte', 'Brávejte', 'Vezmete'],
            answer: 'Vemte',
            translation: 'Standard: "Vezměte si kabát." Colloquial: "Vemte si kabát."',
            rule: 'Colloquial imperative shortening: vezměte -> vemte.'
        }
    ];

    let _activeTab = 'cases';
    let _currentIndex = 0;
    let _score = { correct: 0, total: 0 };
    let _container = null;

    function _poolFor(tabId) {
        switch (tabId) {
            case 'cases': return CASES_ITEMS;
            case 'aspect': return ASPECT_ITEMS;
            case 'motion_verbs': return MOTION_ITEMS;
            case 'past_conditionals': return PAST_COND_ITEMS;
            case 'spoken_czech': return SPOKEN_CZECH_ITEMS;
            default: return CASES_ITEMS;
        }
    }

    function render(container, options) {
        _container = container;
        if (options && options.tab) {
            _activeTab = options.tab;
        }
        _currentIndex = 0;
        _score = { correct: 0, total: 0 };
        _renderStudio();
    }

    function _renderStudio() {
        if (!_container) return;
        const pool = _poolFor(_activeTab);
        const item = pool[_currentIndex % pool.length];

        let html = `
            <div class="grammar-studio cs-grammar-studio">
                <div class="studio-header">
                    <h2>🇨🇿 Czech Grammar Studio</h2>
                    <p class="studio-sub">Master Czech cases, verbal aspect, motion verbs, clitics, and spoken nuances.</p>
                </div>
                <div class="studio-tabs">
        `;

        for (const t of TABS) {
            const active = t.id === _activeTab ? 'active' : '';
            html += `<button class="studio-tab-btn ${active}" data-tab="${t.id}">${t.label}</button>`;
        }

        html += `
                </div>
                <div class="studio-content">
                    <div class="studio-progress">
                        <span>Question ${_currentIndex + 1} of ${pool.length}</span>
                        <span>Score: ${_score.correct} / ${_score.total}</span>
                    </div>
                    <div class="studio-card">
                        <div class="drill-sentence">${item.sentence}</div>
                        <div class="drill-translation">"${item.translation}"</div>
                        <div class="drill-options">
        `;

        for (let i = 0; i < item.options.length; i++) {
            const opt = item.options[i];
            html += `<button class="drill-opt-btn" data-opt="${opt}">${opt}</button>`;
        }

        html += `
                        </div>
                        <div class="drill-feedback" style="display: none;"></div>
                    </div>
                </div>
            </div>
        `;

        _container.innerHTML = html;
        _bindEvents();
    }

    function _bindEvents() {
        if (!_container) return;
        const tabBtns = _container.querySelectorAll('.studio-tab-btn');
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                _activeTab = btn.getAttribute('data-tab');
                _currentIndex = 0;
                _score = { correct: 0, total: 0 };
                _renderStudio();
            });
        });

        const optBtns = _container.querySelectorAll('.drill-opt-btn');
        const feedback = _container.querySelector('.drill-feedback');
        const pool = _poolFor(_activeTab);
        const item = pool[_currentIndex % pool.length];

        optBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const chosen = btn.getAttribute('data-opt');
                const isCorrect = chosen === item.answer;
                _score.total++;
                if (isCorrect) _score.correct++;

                optBtns.forEach(b => {
                    b.disabled = true;
                    if (b.getAttribute('data-opt') === item.answer) {
                        b.classList.add('correct');
                    } else if (b.getAttribute('data-opt') === chosen) {
                        b.classList.add('incorrect');
                    }
                });

                if (feedback) {
                    feedback.style.display = 'block';
                    feedback.className = `drill-feedback ${isCorrect ? 'fb-correct' : 'fb-incorrect'}`;
                    feedback.innerHTML = `
                        <div class="fb-title">${isCorrect ? '✓ Správně!' : '✗ Špatně'}</div>
                        <div class="fb-rule">${item.rule}</div>
                        <button class="drill-next-btn">Další otázka →</button>
                    `;
                    const nextBtn = feedback.querySelector('.drill-next-btn');
                    if (nextBtn) {
                        nextBtn.addEventListener('click', () => {
                            _currentIndex++;
                            _renderStudio();
                        });
                    }
                }
            });
        });
    }

    function stop() {
        if (_container) {
            _container.innerHTML = '';
        }
    }

    return {
        TABS: TABS,
        render: render,
        stop: stop,
        _poolFor: _poolFor
    };
})();

if (typeof window !== 'undefined') {
    window.CsGrammarStudio = CsGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CsGrammarStudio;
}
