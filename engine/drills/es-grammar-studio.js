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
// - At least 30 carefully authored questions per drill tab (150 total)

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
        },
        {
            sentence: "Mis abuelos maternos ___ de un pueblo pequeño en las montañas.",
            options: ["son", "están", "sean", "estén"],
            answer: "son",
            translation: "My maternal grandparents are from a small town in the mountains.",
            rule: "Geographic origin and nationality are expressed with 'ser de'."
        },
        {
            sentence: "Mi hermana mayor ___ arquitecta en una empresa internacional.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "My older sister is an architect at an international company.",
            rule: "Professions, trades, and occupations use 'ser'."
        },
        {
            sentence: "Hoy ___ martes y ya pasan de las tres de la tarde.",
            options: ["es", "está", "son", "están"],
            answer: "es",
            translation: "Today is Tuesday and it is already past three in the afternoon.",
            rule: "Days of the week and dates with singular subjects use 'ser'."
        },
        {
            sentence: "Esta mesa antigua del comedor ___ de madera de roble macizo.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "This antique dining table is made of solid oak wood.",
            rule: "Material composition of an object takes 'ser de'."
        },
        {
            sentence: "Ese paraguas negro no es mío; ___ de Lucía.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "That black umbrella is not mine; it belongs to Lucía.",
            rule: "Ownership and possession are expressed with 'ser de'."
        },
        {
            sentence: "¿Cuánto ___ todo junto, por favor? — Cincuenta euros en total.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "How much is everything together, please? — Fifty euros in total.",
            rule: "Asking for or stating the definitive total price uses 'ser'."
        },
        {
            sentence: "Las manzanas en el mercado hoy ___ a dos euros el kilo.",
            options: ["están", "son", "estén", "sean"],
            answer: "están",
            translation: "The apples at the market today are at two euros per kilo.",
            rule: "Fluctuating or daily variable market prices take 'estar a'."
        },
        {
            sentence: "Felipe no vino a trabajar hoy porque ___ con fiebre en cama.",
            options: ["está", "es", "esté", "sea"],
            answer: "está",
            translation: "Felipe didn't come to work today because he is in bed with a fever.",
            rule: "Temporary illnesses and health conditions take 'estar'."
        },
        {
            sentence: "Mis tíos ___ casados desde hace veinticinco años.",
            options: ["están", "son", "estén", "sean"],
            answer: "están",
            translation: "My aunt and uncle have been married for twenty-five years.",
            rule: "Marital or civil status (casado, soltero, divorciado) standardly takes 'estar'."
        },
        {
            sentence: "Ese médico del hospital ___ una persona muy buena y compasiva.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "That hospital doctor is a very good and compassionate person.",
            rule: "'Ser bueno' expresses moral goodness, high quality, or virtue."
        },
        {
            sentence: "El café recién preparado ___ muy bueno esta mañana.",
            options: ["está", "es", "esté", "sea"],
            answer: "está",
            translation: "The freshly brewed coffee tastes very good this morning.",
            rule: "'Estar bueno' applied to food or drinks refers to delicious taste at the moment."
        },
        {
            sentence: "Fumar tabaco ___ sumamente malo para la salud de los pulmones.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "Smoking tobacco is extremely bad for lung health.",
            rule: "'Ser malo' denotes that something is inherently detrimental, harmful, or poor quality."
        },
        {
            sentence: "No bebas esa leche del refrigerador; creo que ya ___ mala.",
            options: ["está", "es", "esté", "sea"],
            answer: "está",
            translation: "Don't drink that milk from the refrigerator; I think it has gone bad.",
            rule: "'Estar malo' applied to food means spoiled or sour; applied to people it means sick."
        },
        {
            sentence: "Ese empresario internacional ___ inmensamente rico.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "That international businessman is immensely wealthy.",
            rule: "'Ser rico' means to possess great wealth or financial resources."
        },
        {
            sentence: "La paella que cocinaste para todos ___ verdaderamente rica.",
            options: ["está", "es", "esté", "sea"],
            answer: "está",
            translation: "The paella you cooked for everyone tastes truly delicious.",
            rule: "'Estar rico' evaluates the culinary flavor of food."
        },
        {
            sentence: "Las manzanas de esta variedad especial ___ verdes por naturaleza.",
            options: ["son", "están", "sean", "estén"],
            answer: "son",
            translation: "Apples of this special variety are naturally green in color.",
            rule: "Permanent, characteristic colors of objects use 'ser'."
        },
        {
            sentence: "No comas esos plátanos todavía; todavía ___ muy verdes.",
            options: ["están", "son", "estén", "sean"],
            answer: "están",
            translation: "Don't eat those bananas yet; they are still very unripe.",
            rule: "'Estar verde' applied to fruit means unripe or not ready to eat."
        },
        {
            sentence: "La fiesta de bienvenida ___ en el jardín del club social.",
            options: ["es", "está", "sea", "esté"],
            answer: "es",
            translation: "The welcome party takes place in the social club garden.",
            rule: "Events, celebrations, and gatherings take place using 'ser', not 'estar'."
        },
        {
            sentence: "En este momento todos nosotros ___ preparando los informes finales.",
            options: ["estamos", "somos", "estemos", "seamos"],
            answer: "estamos",
            translation: "Right now all of us are preparing the final reports.",
            rule: "The progressive aspect (estar + gerundio) strictly uses auxiliary 'estar'."
        },
        {
            sentence: "El tratado de paz ___ firmado por ambos presidentes en Ginebra.",
            options: ["fue", "estuvo", "era", "había"],
            answer: "fue",
            translation: "The peace treaty was signed by both presidents in Geneva.",
            rule: "The true passive voice expressing an action with an agent uses 'ser + participio'."
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
        },
        {
            sentence: "El tren de alta velocidad sale a las ocho con destino ___ Valencia.",
            options: ["para", "por", "hacia", "sobre"],
            answer: "para",
            translation: "The high-speed train leaves at eight bound for Valencia.",
            rule: "Physical destination or directional destination takes 'para'."
        },
        {
            sentence: "Vivimos tranquilamente en esa pequeña ciudad ___ más de diez años.",
            options: ["por", "para", "en", "con"],
            answer: "por",
            translation: "We lived peacefully in that small city for more than ten years.",
            rule: "Duration of an action over a period of time uses 'por'."
        },
        {
            sentence: "¿Hay alguna farmacia de turno abierta ___ aquí cerca?",
            options: ["por", "para", "en", "de"],
            answer: "por",
            translation: "Is there a 24-hour pharmacy open around here nearby?",
            rule: "Approximate location or spatial vicinity takes 'por'."
        },
        {
            sentence: "Fui rápidamente a la biblioteca ___ un diccionario que me faltaba.",
            options: ["por", "para", "hacia", "sobre"],
            answer: "por",
            translation: "I went quickly to the library to fetch a dictionary I was missing.",
            rule: "Going in search of or to fetch something takes 'ir por'."
        },
        {
            sentence: "Compré esta chaqueta de cuero marrón ___ solo cuarenta euros.",
            options: ["por", "para", "con", "en"],
            answer: "por",
            translation: "I bought this brown leather jacket for only forty euros.",
            rule: "Cost, price, or financial transaction takes 'por'."
        },
        {
            sentence: "El límite de velocidad en esta vía es de cien kilómetros ___ hora.",
            options: ["por", "para", "de", "en"],
            answer: "por",
            translation: "The speed limit on this road is one hundred kilometers per hour.",
            rule: "Unit rates, frequencies, and percentages take 'por'."
        },
        {
            sentence: "Muchas gracias ___ haberme ayudado con todas esas cajas pesadas.",
            options: ["por", "para", "de", "con"],
            answer: "por",
            translation: "Thank you very much for having helped me with all those heavy boxes.",
            rule: "Expressing gratitude for a cause or action takes 'gracias por'."
        },
        {
            sentence: "El monumento conmemorativo fue diseñado ___ un arquitecto famoso.",
            options: ["por", "para", "de", "con"],
            answer: "por",
            translation: "The commemorative monument was designed by a famous architect.",
            rule: "The performing agent in a passive construction takes 'por'."
        },
        {
            sentence: "Este vaso de cristal fino es exclusivamente ___ vino blanco.",
            options: ["para", "por", "de", "con"],
            answer: "para",
            translation: "This fine crystal glass is exclusively for white wine.",
            rule: "The specific intended utility or suitability of an object takes 'para'."
        },
        {
            sentence: "___ mí, la tranquilidad y la salud son más valiosas que el dinero.",
            options: ["Para", "Por", "Según", "Hacia"],
            answer: "Para",
            translation: "In my opinion, peace of mind and health are more valuable than money.",
            rule: "Personal opinion or subjective viewpoint takes 'para mí'."
        },
        {
            sentence: "El agua ya está hirviendo en la tetera; está lista ___ servir el té.",
            options: ["para", "por", "con", "en"],
            answer: "para",
            translation: "The water is already boiling in the kettle; it is ready to serve the tea.",
            rule: "Readiness for a specific intended purpose ('listo para') takes 'para'."
        },
        {
            sentence: "Todavía quedan varios puntos importantes ___ discutir en la agenda.",
            options: ["por", "para", "de", "con"],
            answer: "por",
            translation: "There are still several important points yet to be discussed on the agenda.",
            rule: "Pending actions that remain to be done take 'quedar por + infinitivo'."
        },
        {
            sentence: "Después de catorce horas de viaje, ___ fin llegamos a la posada.",
            options: ["por", "para", "en", "al"],
            answer: "por",
            translation: "After fourteen hours of travel, at last we arrived at the inn.",
            rule: "The fixed temporal idiom 'por fin' (at last / finally) takes 'por'."
        },
        {
            sentence: "Un adulto debería dormir ___ lo menos siete horas cada noche.",
            options: ["por", "para", "a", "de"],
            answer: "por",
            translation: "An adult should sleep at least seven hours each night.",
            rule: "The restrictive idiom 'por lo menos' (at least) takes 'por'."
        },
        {
            sentence: "Se me olvidaron las llaves y, ___ colmo, comenzó a llover a cántaros.",
            options: ["para", "por", "de", "en"],
            answer: "para",
            translation: "I forgot my keys and, to top it all off, it started pouring rain.",
            rule: "The idiom 'para colmo' (to make matters worse / to top it off) takes 'para'."
        },
        {
            sentence: "___ desgracia, se agotaron todas las entradas para el concierto.",
            options: ["Por", "Para", "De", "Con"],
            answer: "Por",
            translation: "Unfortunately, all tickets for the concert sold out.",
            rule: "The adverbial expression 'por desgracia' (unfortunately) takes 'por'."
        },
        {
            sentence: "El profesor entregó dos hojas de ejercicios ___ cada alumno del grupo.",
            options: ["por", "para", "en", "con"],
            answer: "por",
            translation: "The teacher handed out two exercise sheets per student in the group.",
            rule: "Distributive allocation takes 'por' (per individual)."
        },
        {
            sentence: "Ella trabaja desde hace tres años como abogada ___ el Ministerio de Justicia.",
            options: ["para", "por", "hacia", "sobre"],
            answer: "para",
            translation: "She has worked for three years as a lawyer for the Ministry of Justice.",
            rule: "Employment by or service to an organization takes 'trabajar para'."
        },
        {
            sentence: "Para llegar al museo histórico, tienes que cruzar ___ la plaza principal.",
            options: ["por", "para", "hacia", "con"],
            answer: "por",
            translation: "To get to the historical museum, you have to cross through the main square.",
            rule: "Passage across or transit through an area takes 'por'."
        },
        {
            sentence: "Aquel viaje por los Andes quedará grabado en mi memoria ___ siempre.",
            options: ["para", "por", "de", "con"],
            answer: "para",
            translation: "That journey through the Andes will remain etched in my memory forever.",
            rule: "The permanent temporal expression 'para siempre' (forever) takes 'para'."
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
        },
        {
            sentence: "Cuando yo ___ diez años, vivía en una granja pequeña con mis abuelos.",
            options: ["tenía", "tuve", "había tenido", "tuviera"],
            answer: "tenía",
            translation: "When I was ten years old, I lived on a small farm with my grandparents.",
            rule: "Stating age in the past provides background context and uses the imperfect ('tenía')."
        },
        {
            sentence: "El antiguo profesor era alto, delgado y siempre ___ unas gafas oscuras.",
            options: ["llevaba", "llevó", "ha llevado", "lleve"],
            answer: "llevaba",
            translation: "The former teacher was tall, slender, and always wore dark glasses.",
            rule: "Describing physical characteristics or habitual clothing in the past takes the imperfect ('llevaba')."
        },
        {
            sentence: "Ayer revisé mi estado bancario y ___ que me habían cobrado una suscripción errónea.",
            options: ["supe", "sabía", "he sabido", "supiera"],
            answer: "supe",
            translation: "Yesterday I checked my bank statement and found out they had charged me an erroneous subscription.",
            rule: "'Saber' in the preterite means to discover or find out at a specific moment ('supe')."
        },
        {
            sentence: "Le ofrecí llevar su maleta pesada hasta la entrada, pero él no ___ aceptar.",
            options: ["quiso", "quería", "ha querido", "quisiera"],
            answer: "quiso",
            translation: "I offered to carry his heavy suitcase to the entrance, but he refused to accept.",
            rule: "'No quiso' in the preterite expresses an active refusal to do something."
        },
        {
            sentence: "El verano pasado yo ___ viajar a Italia, pero no tenía presupuesto suficiente.",
            options: ["quería", "quise", "he querido", "quisiera"],
            answer: "quería",
            translation: "Last summer I wanted to travel to Italy, but I didn't have enough budget.",
            rule: "An ongoing mental wish or intention without a completed outcome uses the imperfect ('quería')."
        },
        {
            sentence: "Durante tres años continuos yo ___ en esa misma oficina antes de mudarme.",
            options: ["trabajé", "trabajaba", "he trabajado", "trabajara"],
            answer: "trabajé",
            translation: "For three continuous years I worked in that same office before moving.",
            rule: "Actions with explicitly stated beginning and ending boundaries use the preterite ('trabajé')."
        },
        {
            sentence: "Mientras mi madre preparaba la cena en la cocina, mi padre ___ la prensa del día.",
            options: ["leía", "leyó", "ha leído", "leyera"],
            answer: "leía",
            translation: "While my mother was preparing dinner in the kitchen, my father was reading the day's press.",
            rule: "Two simultaneous ongoing actions linked by 'mientras' both take the imperfect ('leía')."
        },
        {
            sentence: "Todos los domingos por la mañana nosotros ___ a pasear por el malecón.",
            options: ["salíamos", "salimos", "hemos salido", "saliéramos"],
            answer: "salíamos",
            translation: "Every Sunday morning we used to go out for a walk along the boardwalk.",
            rule: "Customary habitual actions repeated on a regular schedule use the imperfect ('salíamos')."
        },
        {
            sentence: "En cuanto sonó la campana del timbre, los estudiantes ___ a salir al patio.",
            options: ["empezaron", "empezaban", "han empezado", "empezaran"],
            answer: "empezaron",
            translation: "As soon as the bell rang, the students began to go out to the courtyard.",
            rule: "The sudden punctual initiation of an action takes the preterite ('empezaron')."
        },
        {
            sentence: "A las doce en punto de la noche, la música del festival ___ por completo.",
            options: ["terminó", "terminaba", "ha terminado", "terminara"],
            answer: "terminó",
            translation: "At twelve o'clock sharp at night, the festival music finished completely.",
            rule: "The definitive termination of an event at a fixed moment takes the preterite ('terminó')."
        },
        {
            sentence: "Te ___ por teléfono tres veces seguidas esta mañana, pero no respondiste.",
            options: ["llamé", "llamaba", "he llamado", "llamara"],
            answer: "llamé",
            translation: "I called you on the phone three consecutive times this morning, but you didn't answer.",
            rule: "Actions repeated a specific counted number of times use the preterite ('llamé')."
        },
        {
            sentence: "Yo caminaba tranquilamente por la acera cuando de repente ___ un ruido ensordecedor.",
            options: ["oí", "oía", "he oído", "oyera"],
            answer: "oí",
            translation: "I was walking peacefully on the sidewalk when suddenly I heard a deafening noise.",
            rule: "A sudden sensory perception interrupting an ongoing activity takes the preterite ('oí')."
        },
        {
            sentence: "Nuestra casa de campo ___ en lo alto de una colina con vista al valle.",
            options: ["estaba", "estuvo", "ha estado", "estuviera"],
            answer: "estaba",
            translation: "Our country house was on top of a hill overlooking the valley.",
            rule: "Static geographical location in a past descriptive narrative takes the imperfect ('estaba')."
        },
        {
            sentence: "Ayer por la tarde ___ una discusión acalorada con el director del proyecto.",
            options: ["tuve", "tenía", "he tenido", "tuviera"],
            answer: "tuve",
            translation: "Yesterday afternoon I had a heated argument with the project director.",
            rule: "'Tener' in the preterite denotes experiencing an event or incident at a specific time ('tuve')."
        },
        {
            sentence: "En aquella época difícil, nosotros ___ que levantarnos a las cinco cada mañana.",
            options: ["teníamos", "tuvimos", "hemos tenido", "tuviéramos"],
            answer: "teníamos",
            translation: "In that difficult era, we had to get up at five every morning.",
            rule: "Continuous, habitual obligation over an extended period uses the imperfect ('teníamos')."
        },
        {
            sentence: "Ella siempre almorzaba en casa, pero el martes pasado ___ en una cafetería.",
            options: ["almorzó", "almorzaba", "ha almorzado", "almorzara"],
            answer: "almorzó",
            translation: "She always had lunch at home, but last Tuesday she had lunch at a cafeteria.",
            rule: "An exceptional, singular event that breaks a past habit takes the preterite ('almorzó')."
        },
        {
            sentence: "El día de nuestra boda en la playa fue perfecto; no ___ en absoluto.",
            options: ["llovió", "llovía", "ha llovido", "lloviera"],
            answer: "llovió",
            translation: "Our wedding day on the beach was perfect; it didn't rain at all.",
            rule: "Summary evaluation of weather over an entire completed day takes the preterite ('llovió')."
        },
        {
            sentence: "Al ver el obstáculo en la carretera, el chofer ___ el pedal de freno de golpe.",
            options: ["pisó", "pisaba", "ha pisado", "pisara"],
            answer: "pisó",
            translation: "Upon seeing the obstacle on the road, the driver stepped on the brake pedal abruptly.",
            rule: "An immediate instinctive reaction to a trigger takes the preterite ('pisó')."
        },
        {
            sentence: "De niño, yo siempre ___ mucha hambre al terminar las clases de natación.",
            options: ["tenía", "tuve", "he tenido", "tuviera"],
            answer: "tenía",
            translation: "As a child, I always used to be very hungry upon finishing swimming lessons.",
            rule: "A recurrent physical sensation in childhood takes the imperfect ('tenía')."
        },
        {
            sentence: "La restauración completa del puente histórico ___ en mayo del año pasado.",
            options: ["concluyó", "concluía", "ha concluido", "concluyera"],
            answer: "concluyó",
            translation: "The complete restoration of the historic bridge concluded in May of last year.",
            rule: "Historical milestones with an explicit completion date take the preterite ('concluyó')."
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
        },
        {
            sentence: "¿Has visto mi sombrero nuevo por la casa? — No, todavía no ___ he visto.",
            options: ["lo", "le", "la", "se"],
            answer: "lo",
            translation: "Have you seen my new hat around the house? — No, I haven't seen it yet.",
            rule: "A masculine singular direct object noun ('el sombrero') is replaced by 'lo'."
        },
        {
            sentence: "¿Compraste la fruta fresca en la tienda? — Sí, ya ___ compré toda.",
            options: ["la", "le", "lo", "las"],
            answer: "la",
            translation: "Did you buy the fresh fruit at the store? — Yes, I already bought all of it.",
            rule: "A feminine singular direct object noun ('la fruta') is replaced by 'la'."
        },
        {
            sentence: "¿Invitaste a tus primos a la celebración? — Sí, ___ invité ayer por teléfono.",
            options: ["los", "les", "se", "lo"],
            answer: "los",
            translation: "Did you invite your cousins to the celebration? — Yes, I invited them yesterday by phone.",
            rule: "Direct object replacing masculine plural people ('a tus primos') is 'los'."
        },
        {
            sentence: "¿Terminaron las tareas de matemáticas? — Sí, ya ___ terminamos todas.",
            options: ["las", "les", "los", "se"],
            answer: "las",
            translation: "Did you finish the math homework? — Yes, we already finished all of it.",
            rule: "Direct object replacing feminine plural things ('las tareas') is 'las'."
        },
        {
            sentence: "A mí no ___ gusta nada madrugar los domingos por la mañana.",
            options: ["me", "te", "le", "se"],
            answer: "me",
            translation: "I don't like getting up early on Sunday mornings at all.",
            rule: "Verbs like 'gustar' require an indirect object pronoun matching the experiencer ('a mí' -> 'me')."
        },
        {
            sentence: "A mis padres ___ encantan los paseos tranquilos por la naturaleza.",
            options: ["les", "los", "se", "le"],
            answer: "les",
            translation: "My parents love quiet walks through nature.",
            rule: "Third-person plural experiencers ('a mis padres') take the indirect pronoun 'les'."
        },
        {
            sentence: "___ di las gracias al médico por toda su paciencia y dedicación.",
            options: ["Le", "Lo", "Se", "Me"],
            answer: "Le",
            translation: "I thanked the doctor for all his patience and dedication.",
            rule: "Spanish standardly requires the redundant indirect object pronoun 'le' with explicit recipients."
        },
        {
            sentence: "Esa canción tradicional es hermosa; ¿puedes ___ otra vez?",
            options: ["cantárnosla", "cantárnoslo", "nos la cantar", "cantarnos la"],
            answer: "cantárnosla",
            translation: "That traditional song is beautiful; can you sing it to us again?",
            rule: "Attaching 'nos' + 'la' to an infinitive requires an accent on the stressed vowel: 'cantárnosla'."
        },
        {
            sentence: "¿Quién nos explicará las instrucciones? — El profesor ___ explicará mañana.",
            options: ["nos las", "las nos", "se las", "nos los"],
            answer: "nos las",
            translation: "Who will explain the instructions to us? — The teacher will explain them to us tomorrow.",
            rule: "Indirect 'nos' precedes feminine plural direct object 'las' before a conjugated verb."
        },
        {
            sentence: "Si necesitas esa regla de medir sobre la mesa, ___ ahora mismo.",
            options: ["tómala", "la toma", "tómatela", "tómalo"],
            answer: "tómala",
            translation: "If you need that ruler on the table, take it right now.",
            rule: "Affirmative command 'toma' attaches the direct object 'la' with a written accent: 'tómala'."
        },
        {
            sentence: "Señor Gómez, si tiene el contrato firmado, por favor ___ a la oficina.",
            options: ["tráiganoslo", "nos lo traiga", "tráiganosla", "tráigalo nos"],
            answer: "tráiganoslo",
            translation: "Mr. Gómez, if you have the signed contract, please bring it to us at the office.",
            rule: "Formal imperative 'traiga' attaches 'nos' + 'lo' with an accent: 'tráiganoslo'."
        },
        {
            sentence: "¿Te devolvió Ana los libros prestados? — Sí, ya ___ ha devuelto todos.",
            options: ["me los", "los me", "se los", "te los"],
            answer: "me los",
            translation: "Did Ana return the borrowed books to you? — Yes, she has already returned them to me.",
            rule: "Indirect pronoun 'me' precedes direct pronoun 'los' before auxiliary 'ha devuelto'."
        },
        {
            sentence: "Estaba buscando mis llaves perdidas y mi hermana estaba ___ en el jardín.",
            options: ["buscándomelas", "buscándoselas", "me las buscando", "buscándomelos"],
            answer: "buscándomelas",
            translation: "I was looking for my lost keys and my sister was looking for them for me in the garden.",
            rule: "Attaching 'me' + 'las' to a gerund adds an accent over the stem vowel: 'buscándomelas'."
        },
        {
            sentence: "Ese libro es un regalo sorpresa para papá; por favor, no ___ compres todavía.",
            options: ["se lo", "lo se", "te lo", "le lo"],
            answer: "se lo",
            translation: "That book is a surprise gift for dad; please don't buy it for him yet.",
            rule: "Negative command places indirect 'se' (from 'le') before direct 'lo': 'no se lo compres'."
        },
        {
            sentence: "El paquete postal llegó ayer por la tarde y yo se lo entregué ___ personalmente.",
            options: ["a ella", "ella", "para ella", "de ella"],
            answer: "a ella",
            translation: "The postal package arrived yesterday afternoon and I delivered it to her personally.",
            rule: "Because 'se' is ambiguous, the prepositional phrase 'a ella' clarifies the recipient."
        },
        {
            sentence: "¿Por qué caminas con dificultad? ¿___ duele la pierna derecha?",
            options: ["Te", "La", "Se", "Le"],
            answer: "Te",
            translation: "Why are you walking with difficulty? Does your right leg hurt?",
            rule: "Body parts causing pain with 'doler' take an indirect object pronoun ('te duele la pierna')."
        },
        {
            sentence: "Ponte la chaqueta antes de salir al frío. — Sí, ya ___ pongo ahora mismo.",
            options: ["me la", "la me", "se la", "te la"],
            answer: "me la",
            translation: "Put on your jacket before going out into the cold. — Yes, I am putting it on right now.",
            rule: "Reflexive/pronominal 'me' precedes direct object 'la': 'me la pongo'."
        },
        {
            sentence: "Quiero enviar este archivo a los clientes. — Puedes ___ de inmediato.",
            options: ["enviárselo", "enviárlelo", "se lo enviar", "enviártelo"],
            answer: "enviárselo",
            translation: "I want to send this file to the clients. — You can send it to them right away.",
            rule: "Attached to the infinitive, 'les lo' dissimilates into 'se lo': 'enviárselo'."
        },
        {
            sentence: "Señora Pérez, ese informe contiene varios errores; por favor, no ___ envíe todavía.",
            options: ["se lo", "lo se", "le lo", "se la"],
            answer: "se lo",
            translation: "Mrs. Pérez, that report contains several errors; please don't send it to them yet.",
            rule: "Negative formal command places 'se' + 'lo' before the verb: 'no se lo envíe'."
        },
        {
            sentence: "Carlos y su hermano se respetan mucho y ___ ayudan mutuamente en todo.",
            options: ["se", "les", "los", "nos"],
            answer: "se",
            translation: "Carlos and his brother respect each other very much and help each other in everything.",
            rule: "Reciprocal actions between plural subjects take the reflexive reciprocal pronoun 'se'."
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
        },
        {
            sentence: "Aunque ___ bastante frío hoy en la calle, saldré a dar un paseo.",
            options: ["hace", "haga", "haría", "haya"],
            answer: "hace",
            translation: "Although it is quite cold on the street today, I will go out for a walk.",
            rule: "Concessive 'aunque' introducing an acknowledged factual reality takes the indicative ('hace')."
        },
        {
            sentence: "Mis padres quieren que yo ___ una carrera universitaria completa.",
            options: ["estudie", "estudio", "estudiaré", "estudiaba"],
            answer: "estudie",
            translation: "My parents want me to study a complete university degree.",
            rule: "Verbs of volition, wish, or demand ('querer que') trigger the subjunctive ('estudie')."
        },
        {
            sentence: "¡Ojalá que mañana ___ un día despejado para poder navegar!",
            options: ["sea", "es", "será", "era"],
            answer: "sea",
            translation: "Hopefully tomorrow will be a clear day so we can sail!",
            rule: "The wish particle 'ojalá' always triggers the subjunctive mood ('sea')."
        },
        {
            sentence: "Me alegro mucho de que tú ___ mucho mejor de tu resfriado.",
            options: ["estés", "estás", "estarás", "estabas"],
            answer: "estés",
            translation: "I am very glad that you are feeling much better from your cold.",
            rule: "Verbs expressing emotion, feeling, or psychological reaction trigger the subjunctive ('estés')."
        },
        {
            sentence: "Temo que nosotros no ___ llegar a tiempo para el comienzo de la función.",
            options: ["podamos", "podemos", "podremos", "podríamos"],
            answer: "podamos",
            translation: "I fear that we won't be able to arrive in time for the beginning of the show.",
            rule: "Verbs of fear or apprehension ('temer que') require the subjunctive ('podamos')."
        },
        {
            sentence: "El médico me recomendó que ___ al menos dos litros de agua al día.",
            options: ["beba", "bebo", "beberé", "bebía"],
            answer: "beba",
            translation: "The doctor recommended that I drink at least two liters of water a day.",
            rule: "Verbs of advice, recommendation, or suggestion trigger the subjunctive ('beba')."
        },
        {
            sentence: "El reglamento del museo prohíbe que los visitantes ___ fotos con flash.",
            options: ["tomen", "toman", "tomarán", "tomaban"],
            answer: "tomen",
            translation: "The museum rules prohibit visitors from taking photos with flash.",
            rule: "Verbs of prohibition ('prohibir que') require the subjunctive mood ('tomen')."
        },
        {
            sentence: "No estoy completamente seguro de que ellos ___ la dirección correcta.",
            options: ["tengan", "tienen", "tendrán", "tenían"],
            answer: "tengan",
            translation: "I am not completely sure that they have the correct address.",
            rule: "Expressions of uncertainty ('no estar seguro de que') take the subjunctive ('tengan')."
        },
        {
            sentence: "Estoy completamente seguro de que ellos ___ la dirección correcta.",
            options: ["tienen", "tengan", "tuvieran", "tuviesen"],
            answer: "tienen",
            translation: "I am completely sure that they have the correct address.",
            rule: "Expressions of absolute certainty ('estar seguro de que') take the indicative ('tienen')."
        },
        {
            sentence: "Te presto estas notas para que ___ repasar antes del examen final.",
            options: ["puedas", "puedes", "podrás", "podías"],
            answer: "puedas",
            translation: "I lend you these notes so that you can review before the final exam.",
            rule: "Purpose clauses introduced by 'para que' always require the subjunctive ('puedas')."
        },
        {
            sentence: "Salieron de la reunión en completo silencio sin que nadie los ___.",
            options: ["viera", "vio", "veía", "verá"],
            answer: "viera",
            translation: "They left the meeting in complete silence without anyone seeing them.",
            rule: "Conjunctions of negative circumstance ('sin que') always require the subjunctive ('viera')."
        },
        {
            sentence: "Iremos a caminar por el bosque esta tarde a menos que ___ a llover.",
            options: ["empiece", "empieza", "empezará", "empezaba"],
            answer: "empiece",
            translation: "We will go walking in the forest this afternoon unless it begins to rain.",
            rule: "Conditional conjunctions ('a menos que') always take the subjunctive ('empiece')."
        },
        {
            sentence: "Debemos organizar toda la sala antes de que ___ los primeros invitados.",
            options: ["lleguen", "llegan", "llegarán", "llegaban"],
            answer: "lleguen",
            translation: "We must organize the entire living room before the first guests arrive.",
            rule: "Temporal 'antes de que' always requires the subjunctive, regardless of tense."
        },
        {
            sentence: "Te ayudaré con la mudanza después de que ___ mis exámenes finales.",
            options: ["termine", "termino", "terminaré", "terminaba"],
            answer: "termine",
            translation: "I will help you with the move after I finish my final exams.",
            rule: "Temporal 'después de que' referring to a future event triggers the subjunctive ('termine')."
        },
        {
            sentence: "Esperaremos pacientemente en la estación hasta que ___ el próximo tren.",
            options: ["venga", "viene", "vendrá", "venía"],
            answer: "venga",
            translation: "We will wait patiently at the station until the next train arrives.",
            rule: "Temporal 'hasta que' pointing to an anticipated future moment triggers the subjunctive ('venga')."
        },
        {
            sentence: "Ayer nos quedamos esperando en la sala hasta que ___ el médico de guardia.",
            options: ["llegó", "llegara", "llegue", "llegase"],
            answer: "llegó",
            translation: "Yesterday we stayed waiting in the room until the on-call doctor arrived.",
            rule: "Temporal 'hasta que' describing an actual completed past fact takes the indicative ('llegó')."
        },
        {
            sentence: "En esta pequeña empresa no hay nadie que ___ hablar alemán.",
            options: ["sepa", "sabe", "sabrá", "sabía"],
            answer: "sepa",
            translation: "In this small company there is no one who knows how to speak German.",
            rule: "Negated existence in the main clause ('no hay nadie que') requires the subjunctive ('sepa')."
        },
        {
            sentence: "Es una verdadera lástima que tú no ___ acompañarnos al viaje.",
            options: ["puedas", "puedes", "podrás", "podías"],
            answer: "puedas",
            translation: "It is a real shame that you cannot accompany us on the trip.",
            rule: "Impersonal expressions conveying emotional evaluation ('es una lástima que') take the subjunctive."
        },
        {
            sentence: "Es completamente verdad que la práctica constante ___ la perfección.",
            options: ["hace", "haga", "hiciera", "hiciese"],
            answer: "hace",
            translation: "It is completely true that constant practice makes perfection.",
            rule: "Impersonal expressions stating truth or fact ('es verdad que') take the indicative ('hace')."
        },
        {
            sentence: "El profesor de química exige que todos los alumnos ___ puntuales al laboratorio.",
            options: ["sean", "son", "serán", "fueron"],
            answer: "sean",
            translation: "The chemistry teacher demands that all students be punctual to the laboratory.",
            rule: "Verbs of demand or insistence ('exigir que') trigger the subjunctive mood ('sean')."
        }
    ];

    let _container = null;
    let _activeTab = 'ser-estar';
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
        _score = 0;
        _mistakes = [];
    }

    function _startSession(count) {
        const pool = _poolFor(_activeTab);
        const shuffled = _shuffle(pool);
        const targetCount = (count && count > 0) ? count : _questionCount;
        _queue = shuffled.slice(0, Math.min(targetCount, pool.length));
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
                <button type="button" class="vbtn vbtn-primary" id="es-next-btn" style="min-width: 140px;">Continue</button>
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
            <div class="gd-settings">
                <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px;">
                    <h2 class="gd-title" style="margin-bottom: 0;">Spanish Grammar Studio</h2>
                    ${drillInfoBtn}
                </div>

                <div class="gd-tab-switcher" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="gd-tab-btn ${_activeTab === tab.id ? 'active' : ''}" data-es-tab="${tab.id}" role="tab" aria-selected="${_activeTab === tab.id}">
                            ${tab.label}
                        </button>
                    `).join('')}
                </div>

                <p class="gd-hint" style="margin-bottom: 22px;">${_esc(tabMeta.desc)}</p>

                <div class="gd-setting">
                    <label>Number of questions</label>
                    <div class="gd-count-chips">
                        ${[5, 10, 20, 30].map(n => `
                            <button type="button" class="gd-chip ${_questionCount === n ? 'active' : ''}" data-count="${n}">
                                ${n === 30 ? 'All (30)' : n}
                            </button>
                        `).join('')}
                    </div>
                </div>

                <button type="button" class="vbtn vbtn-primary vbtn-block" id="es-start-btn" style="margin-top: 24px;">Start Practice</button>
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
                <button class="gd-change-skill" id="es-exit-btn">← Exit</button>
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

                <div id="es-quiz-feedback"></div>
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
                        <button type="button" class="vbtn vbtn-primary" id="es-restart-btn">Practise Again</button>
                        <button type="button" class="vbtn vbtn-secondary" id="es-choose-tab-btn">Change Topic</button>
                    </div>
                </div>
            </div>
        `;
    }

    function _handleGlobalKey(e) {
        if (!_container || _state !== 'quiz') return;

        // If feedback Continue button is active, Enter or Space advances
        const nextBtn = document.getElementById('es-next-btn');
        if (nextBtn) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                nextBtn.click();
            }
            return;
        }

        // 1-4 keys to select option
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

        // Settings events
        if (_state === 'settings') {
            _container.querySelectorAll('[data-es-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _activeTab = btn.dataset.esTab;
                    _render();
                });
            });

            _container.querySelectorAll('.gd-chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    _questionCount = parseInt(btn.dataset.count, 10);
                    _container.querySelectorAll('.gd-chip').forEach(b => b.classList.toggle('active', b === btn));
                });
            });

            const startBtn = _container.querySelector('#es-start-btn');
            if (startBtn) {
                startBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }
        }

        // Quiz events
        if (_state === 'quiz') {
            const exitBtn = _container.querySelector('#es-exit-btn');
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

        // Summary events
        if (_state === 'summary') {
            const restartBtn = _container.querySelector('#es-restart-btn');
            if (restartBtn) {
                restartBtn.addEventListener('click', () => {
                    _startSession(_questionCount);
                });
            }

            const chooseTabBtn = _container.querySelector('#es-choose-tab-btn');
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
        stop,
        _poolFor
    };
})();

if (typeof window !== 'undefined') {
    window.EsGrammarStudio = EsGrammarStudio;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EsGrammarStudio;
}
