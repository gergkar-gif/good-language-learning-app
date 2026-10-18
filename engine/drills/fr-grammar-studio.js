// ============================================
// FRENCH GRAMMAR & MECHANICS STUDIO
// ============================================
// Dedicated French driller addressing the 5 core contrastive bottlenecks:
// 1. Passé composé vs Imparfait (completed events vs background, habit, and aspect shifts)
// 2. Partitive & Articles (du/de la/des vs de/d' after negation, quantities, and verbs)
// 3. Clitic Pronouns (me/te/se/nous/vous -> le/la/les -> lui/leur -> y -> en, plus imperatives)
// 4. Past Participle Agreement (accord du participe passé with être, avoir + preceding COD, and pronominals)
// 5. Subjunctive vs Indicative Triggers (doubt, necessity, emotion, and conjunctions vs certainty/hope)

const FrGrammarStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'past-aspect', label: 'Passé composé vs Imparfait', desc: 'Completed foreground actions vs ongoing background, habits, and aspect shifts' },
        { id: 'articles', label: 'Partitive & Articles', desc: 'Partitive du/de la/des vs de after negation, expressions of quantity, and verbs' },
        { id: 'pronouns', label: 'Clitic Pronouns', desc: 'Double object placement, y vs en, and affirmative vs negative imperatives' },
        { id: 'agreement', label: 'Participle Agreement', desc: 'Past participle agreement with être, preceding direct objects, and reflexive verbs' },
        { id: 'subjunctive', label: 'Subjunctive Triggers', desc: 'Subjunctive vs indicative after doubt, emotion, necessity, and conjunctions' }
    ];

    const PAST_ASPECT_ITEMS = [
        {
            sentence: "Je ___ tranquillement dans le salon quand le téléphone a sonné.",
            options: ["lisais", "ai lu", "lise", "lirai"],
            answer: "lisais",
            translation: "I was reading quietly in the living room when the phone rang.",
            rule: "An ongoing background action interrupted by a sudden event takes the imparfait ('lisais')."
        },
        {
            sentence: "Hier soir, nous ___ au restaurant pour fêter l'anniversaire de Claire.",
            options: ["sommes allés", "allions", "allons", "étions allés"],
            answer: "sommes allés",
            translation: "Last night, we went to the restaurant to celebrate Claire's birthday.",
            rule: "A single completed event at a specific past time ('hier soir') requires the passé composé."
        },
        {
            sentence: "Quand j'étais enfant, nous ___ chaque été en Bretagne chez mes grands-parents.",
            options: ["partions", "sommes partis", "partons", "partirons"],
            answer: "partions",
            translation: "When I was a child, we used to go to Brittany every summer to my grandparents' house.",
            rule: "Habitual or repeated actions in the past ('chaque été') take the imparfait."
        },
        {
            sentence: "Il ___ très froid ce matin-là et la neige couvrait les toits.",
            options: ["faisait", "a fait", "fait", "fasse"],
            answer: "faisait",
            translation: "It was very cold that morning and snow covered the rooftops.",
            rule: "Scene-setting descriptions and weather in a past narrative use the imparfait."
        },
        {
            sentence: "Tout à coup, le serveur ___ le plateau de verres sur le sol.",
            options: ["a fait tomber", "faisait tomber", "fait tomber", "fera tomber"],
            answer: "a fait tomber",
            translation: "Suddenly, the waiter dropped the tray of glasses on the floor.",
            rule: "Sudden, punctual actions ('tout à coup') that advance the plot take the passé composé."
        },
        {
            sentence: "Pendant que tu ___ le dîner, j'ai rangé toute la cuisine.",
            options: ["préparais", "as préparé", "prépares", "prépareras"],
            answer: "préparais",
            translation: "While you were preparing dinner, I tidied up the whole kitchen.",
            rule: "'Pendant que' introduces an ongoing background action in the imparfait."
        },
        {
            sentence: "J'___ pendant huit heures à Lyon avant de déménager à Bordeaux.",
            options: ["ai habité", "habitais", "habite", "habiterai"],
            answer: "ai habité",
            translation: "I lived in Lyon for a bounded period before moving to Bordeaux.",
            rule: "A state or action enclosed within a completed, bounded timeframe takes the passé composé."
        },
        {
            sentence: "À cette époque-là, nous ne ___ pas encore que le projet serait annulé.",
            options: ["savions", "avons su", "sachions", "saurons"],
            answer: "savions",
            translation: "At that time, we did not yet know that the project would be cancelled.",
            rule: "In the imparfait, 'savoir' means an ongoing state of knowing ('knew'); in the passé composé ('ai su') it means 'found out'."
        },
        {
            sentence: "Quand elle a ouvert la lettre, elle ___ la vérité immédiatement.",
            options: ["a su", "savait", "sache", "saura"],
            answer: "a su",
            translation: "When she opened the letter, she found out the truth immediately.",
            rule: "In the passé composé, 'savoir' shifts meaning to 'found out / learned at that moment'."
        },
        {
            sentence: "J'___ mon voisin pour la première fois lors de la fête du quartier.",
            options: ["ai connu", "connaissais", "connais", "connaisse"],
            answer: "ai connu",
            translation: "I met my neighbour for the first time at the neighbourhood party.",
            rule: "In the passé composé, 'connaître' means 'met for the first time' (whereas 'connaissais' means 'was acquainted with')."
        },
        {
            sentence: "Elle n'est pas venue travailler parce qu'elle ___ de la fièvre.",
            options: ["avait", "a eu", "ait", "aura"],
            answer: "avait",
            translation: "She didn't come to work because she had a fever.",
            rule: "Ongoing physical and mental states explaining the background cause take the imparfait."
        },
        {
            sentence: "Ce matin, je me suis réveillé, j'___ un café et je suis sorti.",
            options: ["ai pris", "prenais", "prends", "prenne"],
            answer: "ai pris",
            translation: "This morning, I woke up, had a coffee, and went out.",
            rule: "A sequence of completed actions in chronological order uses the passé composé for each step."
        },
        {
            sentence: "Autrefois, il n'y ___ pas autant de voitures dans cette rue.",
            options: ["avait", "a eu", "ait", "aura"],
            answer: "avait",
            translation: "In the past, there were not as many cars on this street.",
            rule: "'Autrefois' contrasts a past state of affairs with the present and takes the imparfait."
        },
        {
            sentence: "Le train ___ déjà à quai quand nous sommes arrivés à la gare.",
            options: ["était", "a été", "soit", "sera"],
            answer: "était",
            translation: "The train was already at the platform when we arrived at the station.",
            rule: "A pre-existing state ('was already there') when another event happens uses the imparfait."
        },
        {
            sentence: "Nous ___ lui parler, mais il a raccroché avant de nous écouter.",
            options: ["voulions", "avons voulu", "voulons", "veuillons"],
            answer: "voulions",
            translation: "We wanted to speak to him, but he hung up before listening to us.",
            rule: "'Voulions' expresses an ongoing desire/intention in the background."
        },
        {
            sentence: "Finalement, après trois essais, il ___ ouvrir la porte bloquée.",
            options: ["a pu", "pouvait", "peut", "puisse"],
            answer: "a pu",
            translation: "Finally, after three tries, he managed to open the jammed door.",
            rule: "In the passé composé, 'pouvoir' ('a pu') means 'managed to / succeeded in'."
        },
        {
            sentence: "Tous les vendredis soir, mes amis ___ jouer aux cartes au café du coin.",
            options: ["allaient", "sont allés", "vont", "aillent"],
            answer: "allaient",
            translation: "Every Friday evening, my friends used to go play cards at the corner café.",
            rule: "Recurring past routines ('tous les vendredis soir') take the imparfait."
        },
        {
            sentence: "L'année dernière, il ___ son permis de conduire du premier coup.",
            options: ["a obtenu", "obtenait", "obtient", "obtienne"],
            answer: "a obtenu",
            translation: "Last year, he got his driving licence on the first try.",
            rule: "A single completed achievement in the past uses the passé composé."
        },
        {
            sentence: "Les enfants ___ dans le jardin pendant que leurs parents discutaient.",
            options: ["jouaient", "ont joué", "jouent", "joueraient"],
            answer: "jouaient",
            translation: "The children were playing in the garden while their parents were chatting.",
            rule: "Two simultaneous ongoing actions in the past both take the imparfait."
        },
        {
            sentence: "Dès qu'elle ___ la nouvelle, elle nous a appelés.",
            options: ["a appris", "apprenait", "apprend", "apprenne"],
            answer: "a appris",
            translation: "As soon as she heard the news, she called us.",
            rule: "'Dès que' introducing a completed triggering event in the past takes the passé composé."
        }
    ];

    const ARTICLES_ITEMS = [
        {
            sentence: "Le matin, je prends toujours ___ café noir sans sucre.",
            options: ["du", "de", "le", "un"],
            answer: "du",
            translation: "In the morning, I always have some black coffee without sugar.",
            rule: "Unspecified quantities of masculine singular uncountable nouns after 'prendre' take the partitive 'du'."
        },
        {
            sentence: "Merci, mais je ne bois jamais ___ café après dix-sept heures.",
            options: ["de", "du", "le", "des"],
            answer: "de",
            translation: "Thank you, but I never drink coffee after 5 p.m.",
            rule: "After a negative verb ('ne... pas / jamais / plus'), partitive 'du/de la/des' and indefinite 'un/une' reduce to 'de'."
        },
        {
            sentence: "J'aime beaucoup ___ fromage de chèvre, surtout quand il est frais.",
            options: ["le", "du", "de", "un"],
            answer: "le",
            translation: "I really like goat cheese, especially when it is fresh.",
            rule: "Verbs of preference ('aimer', 'adorer', 'préférer', 'détester') always take the definite article ('le/la/les'), even in the negative."
        },
        {
            sentence: "Nous avons acheté beaucoup ___ fruits frais au marché ce matin.",
            options: ["de", "des", "du", "les"],
            answer: "de",
            translation: "We bought a lot of fresh fruit at the market this morning.",
            rule: "Expressions of quantity ('beaucoup de', 'trop de', 'peu de', 'assez de') are followed by 'de' (never 'des')."
        },
        {
            sentence: "Il reste encore ___ excellentes fraises au réfrigérateur.",
            options: ["d'", "des", "de la", "les"],
            answer: "d'",
            translation: "There are still some excellent strawberries left in the refrigerator.",
            rule: "In standard French, plural partitive 'des' reduces to 'de/d'' before a pre-nominal plural adjective ('d'excellentes fraises')."
        },
        {
            sentence: "Ce n'est pas ___ vin rouge, c'est du jus de raisin.",
            options: ["du", "de", "le", "un"],
            answer: "du",
            translation: "That isn't red wine, it's grape juice.",
            rule: "After 'ce n'est pas / ce ne sont pas', the partitive or indefinite article is retained ('du', not 'de') because the identity is contrasted."
        },
        {
            sentence: "Est-ce que tu joues ___ piano ou de la guitare ?",
            options: ["du", "au", "le", "de"],
            answer: "du",
            translation: "Do you play the piano or the guitar?",
            rule: "'Jouer de' is used for musical instruments ('jouer du piano'); 'jouer à' is used for sports and games."
        },
        {
            sentence: "Le dimanche après-midi, ils jouent souvent ___ tennis ensemble.",
            options: ["au", "du", "le", "en"],
            answer: "au",
            translation: "On Sunday afternoons, they often play tennis together.",
            rule: "'Jouer à' (à + le = au) is used with sports, board games, and team games."
        },
        {
            sentence: "Ma sœur fait ___ natation trois fois par semaine à la piscine municipale.",
            options: ["de la", "la", "à la", "une"],
            answer: "de la",
            translation: "My sister goes swimming three times a week at the municipal pool.",
            rule: "'Faire de' + partitive ('du / de la / de l'') is used for sports and activities."
        },
        {
            sentence: "Mais cet hiver, elle ne fait plus ___ sport à cause d'une blessure.",
            options: ["de", "du", "le", "au"],
            answer: "de",
            translation: "But this winter, she is no longer doing any sport because of an injury.",
            rule: "'Faire du sport' becomes 'ne plus faire de sport' under negation."
        },
        {
            sentence: "Nous avons ___ besoin d'une nouvelle imprimante pour le bureau.",
            options: ["— (no article)", "un", "du", "le"],
            answer: "— (no article)",
            translation: "We need a new printer for the office.",
            rule: "Fixed verbal expressions like 'avoir besoin de', 'avoir envie de', 'avoir peur de' take no article."
        },
        {
            sentence: "Pour cette recette, il faut ajouter une cuillère ___ huile d'olive.",
            options: ["d'", "de l'", "du", "l'"],
            answer: "d'",
            translation: "For this recipe, you must add a spoonful of olive oil.",
            rule: "Containers and measures of quantity ('une cuillère de', 'un verre de', 'un kilo de') take bare 'de/d''."
        },
        {
            sentence: "Il n'y a plus ___ eau minérale dans la bouteille.",
            options: ["d'", "de l'", "du", "l'"],
            answer: "d'",
            translation: "There is no mineral water left in the bottle.",
            rule: "After 'il n'y a pas / plus', the partitive 'de l'' reduces to 'd'' before a vowel."
        },
        {
            sentence: "Elle n'aime pas du tout ___ légumes trop cuits.",
            options: ["les", "des", "de", "aux"],
            answer: "les",
            translation: "She does not like overcooked vegetables at all.",
            rule: "With 'aimer', the definite article 'les' is kept even in a negative sentence ('elle n'aime pas les légumes')."
        },
        {
            sentence: "Avez-vous ___ monnaie pour le distributeur automatique ?",
            options: ["de la", "la", "une", "de"],
            answer: "de la",
            translation: "Do you have any change for the vending machine?",
            rule: "'La monnaie' (small change, feminine uncountable) takes the partitive 'de la' in an affirmative question."
        },
        {
            sentence: "La plupart ___ étudiants ont réussi l'examen final.",
            options: ["des", "de", "d'", "les"],
            answer: "des",
            translation: "Most of the students passed the final exam.",
            rule: "'La plupart' is the major exception to quantity expressions: it always takes 'des / du / de la', never bare 'de'."
        },
        {
            sentence: "J'ai parlé ___ nouveaux voisins qui viennent d'emménager.",
            options: ["aux", "des", "les", "à des"],
            answer: "aux",
            translation: "I spoke to the new neighbours who just moved in.",
            rule: "'Parler à + les' contracts to 'aux'."
        },
        {
            sentence: "De quoi avez-vous besoin ? — J'ai besoin ___ silence pour travailler.",
            options: ["de", "du", "le", "un"],
            answer: "de",
            translation: "What do you need? — I need silence to work.",
            rule: "After 'avoir besoin de', the partitive 'du' merges with 'de' -> 'avoir besoin de silence'."
        },
        {
            sentence: "Ils reviennent ___ Pays-Bas après une semaine de conférence.",
            options: ["des", "du", "de", "aux"],
            answer: "des",
            translation: "They are returning from the Netherlands after a week-long conference.",
            rule: "Plural country names with 'venir de / revenir de' take 'des' (de + les Pays-Bas)."
        },
        {
            sentence: "Cet été, nous allons passer deux semaines ___ Portugal.",
            options: ["au", "en", "à", "dans le"],
            answer: "au",
            translation: "This summer, we are going to spend two weeks in Portugal.",
            rule: "Masculine singular countries starting with a consonant take 'au' (feminine or vowel-initial countries take 'en')."
        }
    ];

    const PRONOUN_ITEMS = [
        {
            sentence: "Tu as donné le livre à Thomas ? — Oui, je ___ ai donné.",
            options: ["le lui", "lui le", "l'y", "le leur"],
            answer: "le lui",
            translation: "Did you give the book to Thomas? — Yes, I gave it to him.",
            rule: "3rd-person COD 'le' precedes 3rd-person COI 'lui' (le/la/les + lui/leur)."
        },
        {
            sentence: "Tu me prêtes ta voiture ? — D'accord, je ___ prête.",
            options: ["te la", "la te", "me la", "te l'"],
            answer: "te la",
            translation: "Will you lend me your car? — Okay, I'll lend it to you.",
            rule: "1st/2nd person pronouns (me/te/se/nous/vous) precede 3rd-person COD (le/la/les)."
        },
        {
            sentence: "Tu as parlé de ton voyage à tes parents ? — Oui, je ___ ai parlé.",
            options: ["leur en", "en leur", "les en", "lui en"],
            answer: "leur en",
            translation: "Did you speak about your trip to your parents? — Yes, I spoke to them about it.",
            rule: "COI 'leur' precedes the adverbial pronoun 'en' (lui/leur + en)."
        },
        {
            sentence: "Est-ce qu'elle va au cinéma ce soir ? — Oui, elle ___ va.",
            options: ["y", "en", "l'y", "lui"],
            answer: "y",
            translation: "Is she going to the cinema tonight? — Yes, she is going there.",
            rule: "'y' replaces locations introduced by 'à', 'en', 'dans', or 'sur' (au cinéma -> y)."
        },
        {
            sentence: "Donne ce document à Marie immédiatement ! — D'accord, je vais ___ donner.",
            options: ["le lui", "lui le", "la lui", "le leur"],
            answer: "le lui",
            translation: "Give this document to Marie immediately! — Okay, I am going to give it to her.",
            rule: "With a semi-auxiliary + infinitive ('aller donner'), object pronouns attach directly before the infinitive ('vais le lui donner')."
        },
        {
            sentence: "Rends-moi mon stylo ! — Oui, ___ tout de suite !",
            options: ["rends-le-moi", "rends-moi-le", "me le rends", "rends-lui-moi"],
            answer: "rends-le-moi",
            translation: "Return my pen! — Yes, return it to me right away!",
            rule: "In the affirmative imperative, COD ('le/la/les') comes first, followed by tonic COI ('moi/toi/lui/nous/vous/leur'): rends-le-moi."
        },
        {
            sentence: "Tu ne dois pas raconter cette histoire à Paul. — Ne ___ raconte pas.",
            options: ["la lui", "lui la", "le lui", "la leur"],
            answer: "la lui",
            translation: "You must not tell this story to Paul. — Don't tell it to him.",
            rule: "In the negative imperative, pronouns stay before the verb in standard order: 'Ne la lui raconte pas'."
        },
        {
            sentence: "Combien de croissants as-tu achetés ? — J'___ ai acheté quatre.",
            options: ["en", "y", "les", "des"],
            answer: "en",
            translation: "How many croissants did you buy? — I bought four of them.",
            rule: "'en' replaces nouns modified by numbers, quantities, or partitive articles."
        },
        {
            sentence: "Tu penses à ton examen de demain ? — Oui, j'___ pense constamment.",
            options: ["y", "en", "lui", "le"],
            answer: "y",
            translation: "Are you thinking about your exam tomorrow? — Yes, I think about it constantly.",
            rule: "'Penser à + inanimate thing' is replaced by 'y' ('j'y pense')."
        },
        {
            sentence: "Tu penses souvent à ta grand-mère ? — Oui, je pense souvent ___.",
            options: ["à elle", "y", "lui", "la"],
            answer: "à elle",
            translation: "Do you often think of your grandmother? — Yes, I often think of her.",
            rule: "With verbs like 'penser à', 's'intéresser à', or 'tenir à' followed by a PERSON, use 'à + disjunctive pronoun' ('à elle'), not 'y' or 'lui'."
        },
        {
            sentence: "Tu as envoyé les invitations aux invités ? — Oui, je ___ ai envoyées.",
            options: ["les leur", "leur les", "les lui", "leur en"],
            answer: "les leur",
            translation: "Did you send the invitations to the guests? — Yes, I sent them to them.",
            rule: "Plural COD 'les' precedes plural COI 'leur' ('les leur')."
        },
        {
            sentence: "Est-ce qu'il reste du café ? — Non, il n'___ reste plus.",
            options: ["en", "y", "le", "de"],
            answer: "en",
            translation: "Is there any coffee left? — No, there is none left.",
            rule: "'en' replaces indefinite/partitive quantities ('du café' -> 'en')."
        },
        {
            sentence: "Tu peux me passer le sel ? — Tiens, je ___ passe.",
            options: ["te le", "le te", "me le", "lui le"],
            answer: "te le",
            translation: "Can you pass me the salt? — Here, I'll pass it to you.",
            rule: "2nd-person COI 'te' precedes 3rd-person COD 'le' ('te le')."
        },
        {
            sentence: "Il reste encore des places pour le concert ? — Oui, prends-___ deux !",
            options: ["en", "les", "y", "des"],
            answer: "en",
            translation: "Are there still tickets left for the concert? — Yes, take two of them!",
            rule: "With a number ('deux'), the noun is replaced by 'en' ('prends-en deux')."
        },
        {
            sentence: "Tu vas à la boulangerie ? — Oui, vas-___ aussi si tu veux du pain chaud.",
            options: ["y", "en", "la", "le"],
            answer: "y",
            translation: "Are you going to the bakery? — Yes, go there too if you want warm bread.",
            rule: "In the affirmative imperative, 'va' regains its final '-s' before 'y' for liaison: 'vas-y'."
        },
        {
            sentence: "Ces pommes ont l'air délicieuses ; mange-___ une !",
            options: ["s-en", "en", "les", "la"],
            answer: "s-en",
            translation: "These apples look delicious; eat one of them!",
            rule: "First-group (-er) affirmative imperatives add '-s-' before 'en' or 'y' ('manges-en une')."
        },
        {
            sentence: "Paul m'a présenté à sa directrice ; il ___ a présenté hier.",
            options: ["m'à elle", "me lui", "m'y", "me l'"],
            answer: "m'à elle",
            translation: "Paul introduced me to his director; he introduced me to her yesterday.",
            rule: "When a 1st/2nd person pronoun ('me/te/nous/vous') is the COD, you cannot combine it with 'lui/leur'; use 'à + tonic pronoun' ('Il m'a présenté à elle')."
        },
        {
            sentence: "As-tu besoin de ce dictionnaire ? — Oui, j'___ ai besoin tout de suite.",
            options: ["en", "y", "le", "lui"],
            answer: "en",
            translation: "Do you need this dictionary? — Yes, I need it right away.",
            rule: "Verbal phrases with 'de' ('avoir besoin de', 'parler de', 'se souvenir de') replace inanimate objects with 'en'."
        },
        {
            sentence: "Tu te souviens de notre premier voyage à Rome ? — Oui, je ___ souviens très bien.",
            options: ["m'en", "en me", "m'y", "me le"],
            answer: "m'en",
            translation: "Do you remember our first trip to Rome? — Yes, I remember it very well.",
            rule: "Reflexive 'me' precedes 'en' ('se souvenir de' -> 'je m'en souviens')."
        },
        {
            sentence: "Il a promis à ses enfants de les emmener au zoo ; il ___ a promis.",
            options: ["le leur", "leur le", "les leur", "leur en"],
            answer: "le leur",
            translation: "He promised his children to take them to the zoo; he promised it to them.",
            rule: "Neutral 'le' replaces an entire clause or infinitive phrase ('de les emmener au zoo') and precedes 'leur'."
        }
    ];

    const AGREEMENT_ITEMS = [
        {
            sentence: "Elle est ___ à la réunion avec dix minutes de retard.",
            options: ["arrivée", "arrivé", "arrivés", "arrivées"],
            answer: "arrivée",
            translation: "She arrived at the meeting ten minutes late.",
            rule: "With auxiliary 'être', the past participle agrees in gender and number with the subject ('Elle' -> 'arrivée')."
        },
        {
            sentence: "La robe que Sophie a ___ pour le mariage est magnifique.",
            options: ["achetée", "acheté", "achetés", "achetées"],
            answer: "achetée",
            translation: "The dress that Sophie bought for the wedding is magnificent.",
            rule: "With 'avoir', the past participle agrees with a preceding direct object ('la robe que' -> feminine singular 'achetée')."
        },
        {
            sentence: "Ils ont ___ trois romans policiers pendant les vacances.",
            options: ["lu", "lus", "lue", "lues"],
            answer: "lu",
            translation: "They read three detective novels during the holidays.",
            rule: "With 'avoir', when the direct object follows the verb ('trois romans'), there is NO agreement."
        },
        {
            sentence: "Ces lettres ? Je les ai ___ hier soir avant de partir.",
            options: ["écrites", "écrit", "écrite", "écrits"],
            answer: "écrites",
            translation: "These letters? I wrote them yesterday evening before leaving.",
            rule: "Preceding direct object pronoun 'les' refers to 'ces lettres' (feminine plural -> 'écrites')."
        },
        {
            sentence: "Mes sœurs sont ___ en vacances dans le sud de la France.",
            options: ["parties", "parti", "partie", "partis"],
            answer: "parties",
            translation: "My sisters left on holiday to the south of France.",
            rule: "Auxiliary 'être' agrees with the feminine plural subject 'mes sœurs' -> 'parties'."
        },
        {
            sentence: "Elle s'est ___ les mains à l'eau froide avant de cuisiner.",
            options: ["lavé", "lavée", "lavés", "lavées"],
            answer: "lavé",
            translation: "She washed her hands with cold water before cooking.",
            rule: "When a reflexive verb is followed by a direct object body part ('les mains'), 'se' is an indirect object (COI), so there is NO agreement."
        },
        {
            sentence: "Marie s'est ___ longtemps dans le miroir de l'entrée.",
            options: ["regardée", "regardé", "regardés", "regardées"],
            answer: "regardée",
            translation: "Marie looked at herself for a long time in the hallway mirror.",
            rule: "Here 's'' is the direct object (Marie looked at herself), so the participle agrees -> 'regardée'."
        },
        {
            sentence: "Des pommes ? J'en ai beaucoup ___ cette semaine.",
            options: ["mangé", "mangée", "mangés", "mangées"],
            answer: "mangé",
            translation: "Apples? I ate a lot of them this week.",
            rule: "When the preceding object pronoun is 'en', the past participle stays invariable ('mangé')."
        },
        {
            sentence: "Quels musées avez-vous ___ pendant votre séjour à Lyon ?",
            options: ["visités", "visité", "visitée", "visitées"],
            answer: "visités",
            translation: "Which museums did you visit during your stay in Lyon?",
            rule: "Interrogative direct object 'Quels musées' precedes 'avoir', triggering masculine plural agreement ('visités')."
        },
        {
            sentence: "Nous nous sommes ___ pendant plus d'une heure au téléphone.",
            options: ["parlé", "parlés", "parlée", "parlées"],
            answer: "parlé",
            translation: "We spoke to each other for over an hour on the phone.",
            rule: "'Parler à quelqu'un' takes an indirect object (COI); therefore 'se parler', 'se téléphoner', and 'se sourire' NEVER agree in the past participle."
        },
        {
            sentence: "Ils se sont ___ dans un petit café près de la Sorbonne.",
            options: ["rencontrés", "rencontré", "rencontrée", "rencontrées"],
            answer: "rencontrés",
            translation: "They met each other in a small café near the Sorbonne.",
            rule: "'Rencontrer quelqu'un' is directly transitive (COD), so reciprocal 'se sont rencontrés' agrees with the plural subject."
        },
        {
            sentence: "Elle a ___ les valises au premier étage toute seule.",
            options: ["monté", "montée", "montés", "montées"],
            answer: "monté",
            translation: "She carried the suitcases up to the first floor all by herself.",
            rule: "Verbs like 'monter', 'descendre', 'sortir', and 'rentrer' take 'avoir' when used transitively with a following direct object ('les valises'), so no agreement."
        },
        {
            sentence: "Les fleurs que tu m'as ___ sentent merveilleusement bon.",
            options: ["offertes", "offert", "offerte", "offerts"],
            answer: "offertes",
            translation: "The flowers that you gave me smell wonderfully good.",
            rule: "Relative pronoun 'que' replaces 'les fleurs' (feminine plural COD before 'avoir') -> 'offertes'."
        },
        {
            sentence: "Combien de pages de ce rapport as-tu déjà ___ ?",
            options: ["lues", "lu", "lue", "lus"],
            answer: "lues",
            translation: "How many pages of this report have you already read?",
            rule: "'Combien de pages' is a preceding feminine plural direct object -> 'lues'."
        },
        {
            sentence: "Paul et Lucie se sont ___ des messages toute la soirée.",
            options: ["envoyé", "envoyés", "envoyée", "envoyées"],
            answer: "envoyé",
            translation: "Paul and Lucie sent each other messages all evening.",
            rule: "Because 'des messages' is the following direct object (COD), 'se' is the indirect object (to each other), so 'envoyé' does not agree."
        },
        {
            sentence: "Les messages qu'ils se sont ___ étaient très drôles.",
            options: ["envoyés", "envoyé", "envoyée", "envoyées"],
            answer: "envoyés",
            translation: "The messages that they sent each other were very funny.",
            rule: "Here the direct object ('les messages que') precedes the verb, so 'envoyés' agrees with 'les messages' (masculine plural)."
        },
        {
            sentence: "La voiture qu'elle a ___ réparer est enfin prête.",
            options: ["fait", "faite", "faits", "faites"],
            answer: "fait",
            translation: "The car that she had repaired is finally ready.",
            rule: "Causative 'faire + infinitive' ('a fait réparer') is strictly invariable: 'fait' NEVER agrees when followed by an infinitive."
        },
        {
            sentence: "Mes parents leur ont ___ dès leur arrivée à l'aéroport.",
            options: ["téléphoné", "téléphonés", "téléphonée", "téléphonées"],
            answer: "téléphoné",
            translation: "My parents phoned them as soon as they arrived at the airport.",
            rule: "'Leur' is an indirect object pronoun (COI); past participles with 'avoir' never agree with an indirect object."
        },
        {
            sentence: "Elles se sont ___ compte de leur erreur trop tard.",
            options: ["rendu", "rendues", "rendue", "rendus"],
            answer: "rendu",
            translation: "They realized their mistake too late.",
            rule: "In the idiom 'se rendre compte de', 'compte' acts as the following direct object, so 'rendu' remains invariable."
        },
        {
            sentence: "Quelle belle chanson ! Tu l'as ___ à la radio ce matin ?",
            options: ["entendue", "entendu", "entendus", "entendues"],
            answer: "entendue",
            translation: "What a lovely song! Did you hear it on the radio this morning?",
            rule: "Preceding COD 'l'' refers to 'une belle chanson' (feminine singular) -> 'entendue'."
        }
    ];

    const SUBJUNCTIVE_ITEMS = [
        {
            sentence: "Il faut absolument que tu ___ tes devoirs avant de sortir.",
            options: ["fasses", "fais", "feras", "fait"],
            answer: "fasses",
            translation: "You must absolutely do your homework before going out.",
            rule: "'Il faut que' expresses necessity and requires the subjunctive ('tu fasses')."
        },
        {
            sentence: "Je suis certain qu'il ___ à l'heure au rendez-vous demain.",
            options: ["sera", "soit", "fût", "sois"],
            answer: "sera",
            translation: "I am certain that he will be on time for the appointment tomorrow.",
            rule: "Affirmative expressions of certainty ('être certain que', 'être sûr que') take the indicative ('sera')."
        },
        {
            sentence: "Bien qu'il ___ froid, nous sommes allés marcher au bord du lac.",
            options: ["fasse", "fait", "fera", "faisait"],
            answer: "fasse",
            translation: "Although it was cold, we went walking by the lake.",
            rule: "Concessive conjunctions ('bien que', 'quoique') always require the subjunctive ('il fasse')."
        },
        {
            sentence: "Je ne pense pas que cette solution ___ la plus efficace.",
            options: ["soit", "est", "sera", "serait"],
            answer: "soit",
            translation: "I don't think that this solution is the most effective.",
            rule: "Verbs of opinion ('penser', 'croire', 'trouver') in the negative express doubt and trigger the subjunctive."
        },
        {
            sentence: "Je pense que ce petit restaurant ___ vraiment excellent.",
            options: ["est", "soit", "sois", "fût"],
            answer: "est",
            translation: "I think that this little restaurant is truly excellent.",
            rule: "Affirmative 'Je pense que / Je crois que' states a conviction as fact and takes the indicative ('est')."
        },
        {
            sentence: "J'aimerais beaucoup que vous ___ dîner chez nous samedi soir.",
            options: ["veniez", "venez", "viendrez", "viendriez"],
            answer: "veniez",
            translation: "I would really like you to come have dinner at our place Saturday evening.",
            rule: "Verbs of wish, desire, and preference ('aimer que', 'vouloir que', 'souhaiter que') take the subjunctive."
        },
        {
            sentence: "J'espère que tu ___ un excellent voyage au Japon.",
            options: ["feras", "fasses", "fais", "ferais"],
            answer: "feras",
            translation: "I hope you will have an excellent trip to Japan.",
            rule: "Affirmative 'espérer que' is a key exception: it takes the indicative (usually future 'feras'), NEVER the subjunctive."
        },
        {
            sentence: "Je te laisse les clés pour que tu ___ rentrer quand tu veux.",
            options: ["puisses", "peux", "pourras", "pouvais"],
            answer: "puisses",
            translation: "I am leaving you the keys so that you can come home whenever you want.",
            rule: "Conjunctions of purpose ('pour que', 'afin que') always trigger the subjunctive ('tu puisses')."
        },
        {
            sentence: "Il est possible qu'elle ___ un peu de retard à cause de la grève.",
            options: ["ait", "a", "aura", "aurait"],
            answer: "ait",
            translation: "It is possible that she may be a little late because of the strike.",
            rule: "'Il est possible que' expresses possibility rather than certainty and requires the subjunctive ('elle ait')."
        },
        {
            sentence: "Il est probable que le train ___ à l'heure malgré la pluie.",
            options: ["partira", "parte", "partît", "soit parti"],
            answer: "partira",
            translation: "It is probable that the train will leave on time despite the rain.",
            rule: "Affirmative 'Il est probable que' expresses high likelihood and takes the indicative ('partira'), unlike 'il est possible que'."
        },
        {
            sentence: "Je doute fort qu'il ___ toute la vérité sur cette affaire.",
            options: ["sache", "sait", "saura", "saurait"],
            answer: "sache",
            translation: "I strongly doubt that he knows the whole truth about this matter.",
            rule: "'Douter que' expresses doubt and requires the subjunctive ('il sache')."
        },
        {
            sentence: "Nous sommes ravis que tu ___ pu venir à notre fête.",
            options: ["aies", "as", "auras", "avais"],
            answer: "aies",
            translation: "We are delighted that you were able to come to our party.",
            rule: "Expressions of emotion ('être ravi que', 'être triste que', 'avoir peur que') require the subjunctive (past subjunctive 'tu aies pu')."
        },
        {
            sentence: "Appelle-moi avant qu'il ne ___ trop tard pour réserver.",
            options: ["soit", "est", "sera", "serait"],
            answer: "soit",
            translation: "Call me before it is too late to book.",
            rule: "'Avant que' (often accompanied by expletive 'ne') always triggers the subjunctive."
        },
        {
            sentence: "Nous partirons dès que tout le monde ___ prêt.",
            options: ["sera", "soit", "est", "serait"],
            answer: "sera",
            translation: "We will leave as soon as everyone is ready.",
            rule: "Temporal conjunctions ('quand', 'lorsque', 'dès que', 'après que') take the indicative (futur simple 'sera' for future events), never the subjunctive."
        },
        {
            sentence: "Je cherche un appartement qui ___ un balcon orienté au sud.",
            options: ["ait", "a", "aura", "avait"],
            answer: "ait",
            translation: "I am looking for an apartment (any such apartment) that has a south-facing balcony.",
            rule: "A relative clause describing a hypothetical or sought-after antecedent ('un appartement qui...') takes the subjunctive."
        },
        {
            sentence: "J'ai enfin trouvé un appartement qui ___ un grand balcon calme.",
            options: ["a", "ait", "aura", "eût"],
            answer: "a",
            translation: "I have finally found an apartment that has a large quiet balcony.",
            rule: "When the antecedent is known to exist ('j'ai trouvé un appartement qui...'), the relative clause takes the indicative ('a')."
        },
        {
            sentence: "C'est le meilleur film que nous ___ vu cette année.",
            options: ["ayons", "avons", "aurons", "avions"],
            answer: "ayons",
            translation: "It is the best film that we have seen this year.",
            rule: "Superlatives ('le meilleur', 'le plus...', 'le seul', 'le premier') expressing subjective judgment take the subjunctive in the relative clause."
        },
        {
            sentence: "Nous resterons au parc jusqu'à ce que le soleil se ___.",
            options: ["couche", "couchera", "coucherait", "couchait"],
            answer: "couche",
            translation: "We will stay in the park until the sun sets.",
            rule: "'Jusqu'à ce que' always requires the subjunctive."
        },
        {
            sentence: "Il semble que ce problème ___ plus complexe que prévu.",
            options: ["soit", "est", "sera", "était"],
            answer: "soit",
            translation: "It seems that this problem is more complex than expected.",
            rule: "'Il semble que' (without an indirect pronoun) expresses uncertainty and takes the subjunctive; 'Il me semble que' takes the indicative."
        },
        {
            sentence: "Il me semble que tu ___ tout à fait raison sur ce point.",
            options: ["as", "aies", "auras", "avais"],
            answer: "as",
            translation: "It seems to me that you are completely right on this point.",
            rule: "Affirmative 'Il me semble que' (with an indirect object pronoun) is treated like 'je pense que' and takes the indicative."
        }
    ];

    let _container = null;
    let _activeTab = 'past-aspect';
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
        if (tabId === 'past-aspect') return PAST_ASPECT_ITEMS;
        if (tabId === 'articles') return ARTICLES_ITEMS;
        if (tabId === 'pronouns') return PRONOUN_ITEMS;
        if (tabId === 'agreement') return AGREEMENT_ITEMS;
        if (tabId === 'subjunctive') return SUBJUNCTIVE_ITEMS;
        return PAST_ASPECT_ITEMS;
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

        const feedbackEl = document.getElementById('fr-quiz-feedback');
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
                <button type="button" class="vbtn vbtn-primary" id="fr-next-btn" style="min-width: 140px;">Continue</button>
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
        const drillInfoBtn = (typeof DrillInfo !== 'undefined') ? DrillInfo.buttonHtml('fr-grammar-studio') : '';

        return `
            <div class="gd-settings">
                <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px;">
                    <h2 class="gd-title" style="margin-bottom: 0;">French Grammar Studio</h2>
                    ${drillInfoBtn}
                </div>

                <div class="gd-tab-switcher" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="gd-tab-btn ${_activeTab === tab.id ? 'active' : ''}" data-fr-tab="${tab.id}" role="tab" aria-selected="${_activeTab === tab.id}">
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

                <button type="button" class="vbtn vbtn-primary vbtn-block" id="fr-start-btn" style="margin-top: 24px;">Start Practice</button>
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
                <button class="gd-change-skill" id="fr-exit-btn">← Exit</button>
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

                <div id="fr-quiz-feedback"></div>
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
                        <button type="button" class="vbtn vbtn-primary" id="fr-restart-btn">Practise Again</button>
                        <button type="button" class="vbtn vbtn-secondary" id="fr-choose-tab-btn">Change Topic</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _handleGlobalKey(e) {
        if (!_container || _state !== 'quiz') return;

        const nextBtn = document.getElementById('fr-next-btn');
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
            _container.querySelectorAll('[data-fr-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _activeTab = btn.dataset.frTab;
                    _render();
                });
            });

            _container.querySelectorAll('.gd-chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    _questionCount = parseInt(btn.dataset.count, 10);
                    _container.querySelectorAll('.gd-chip').forEach(b => b.classList.toggle('active', b === btn));
                });
            });

            const startBtn = _container.querySelector('#fr-start-btn');
            if (startBtn) {
                startBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }
        }

        if (_state === 'quiz') {
            const exitBtn = _container.querySelector('#fr-exit-btn');
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
            const restartBtn = _container.querySelector('#fr-restart-btn');
            if (restartBtn) {
                restartBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }

            const chooseTabBtn = _container.querySelector('#fr-choose-tab-btn');
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
        render,
        init: render,
        stop,
        _poolFor
    };
})();

if (typeof window !== 'undefined') {
    window.FrGrammarStudio = FrGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FrGrammarStudio;
}
