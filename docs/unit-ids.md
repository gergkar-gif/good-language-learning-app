# Unit ids: draft for review (ROADMAP 125)

Status: **draft, 2026-10-04, for review.** A permanent `id` for every
unit in es-es, es-latam and hu, and the vocabulary skill each one gets
([skill-tagging-spec.md](skill-tagging-spec.md) § "Vocabulary skills").
Machine-readable: [unit-ids.json](unit-ids.json). Nothing is written to
the curriculum files yet.

## Summary

- **539 units**: Spanish 243 (es-es and es-latam share every A1–A2 unit
  except *Vosotros*, and 40 core B1 units, so a shared unit has one id),
  Hungarian 296.
- **Vocabulary skill per unit**: `<level>-<id>-vocab`, e.g.
  `a1-greetings-introductions-vocab`. All 539 are unique within their
  language.
- **Old vocabulary slugs become aliases** of the unit they're really used
  in. 508 units take over one or more old slugs; **31 units have no
  vocabulary slug today** (24 Spanish A1–A2 units, 7 Hungarian A2 units)
  and get a new one. 13 units absorb several per-lesson slugs (es-latam
  B2 `b2-31-01-vocab` … `-05`, `brasil-interior-01-vocab` …).
- **`negation` and `hacer`** are grammar points registered as vocabulary.
  They don't belong to any unit and are dropped from the vocabulary list.

## How the ids were made

1. **Generated from the title**, then checked by hand. 271 ids are the
   automatic version; 268 were rewritten.
2. **Rules:** English, lowercase, hyphenated, ASCII; one to four words
   naming the unit's topic; unique within the level, across tracks. Proper
   nouns stay as they are (`honfoglalas`, `kormanyablak`, `cortes-generales`,
   `paks-nuclear`). No unit numbers, level or track names, or "Unit N".
   Years only where they *are* the name (`revolution-1956`, `trianon-1920`).
3. **Where the title is a grammar point**, the id names it
   (`present-continuous`, `translative-case`, `por-and-para`).
4. **Spanish-titled units get English ids** (`constitution-1978` for *La
   Constitución Española de 1978*), in line with the decision that new
   names are English.
5. **Two units with the same title** get a number: HU A2 *Talking About
   the Past I/II* → `the-past-1`, `the-past-2`.

## What I found on the way

- **The old slugs' numbers had already drifted from the units.**
  `a1-unit07-vocab` is used in Spanish A1 unit 8 (*At Home*),
  `a1-unit04-vocab` in unit 15 (*Around Town*), `a1-unit20-vocab` in unit 26.
  So ownership comes from where each slug is used, not from its number.
  This is exactly the problem unit-number slugs cause.
- **`a1-unit01-vocab`** (Spanish greetings) is on 533 exercises across many
  units. It's assigned to *Greetings & Introductions*, because its words are
  greetings; its uses elsewhere are the known mis-tags (ROADMAP 125, step 3).
- **HU A1 and A2 have no unit table.** Their units are blocks of 5 lesson
  files, with titles kept in `LANG_UNIT_TITLES` in `build-manifest.py`.
  Proposed for step 2: give them `curriculum/units/a1.json`/`a2.json` like
  every other level, with the same grouping, so every unit's id lives in
  one kind of place.

## Spanish (es-es and es-latam)

### A1 (26 units)

| es-es | es-latam | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|---|
| 1 | 1 |  | `greetings-introductions` | Greetings & Introductions | `a1-unit01-vocab` |
| 2 | 2 |  | `meeting-someone-new` | Meeting Someone New | `a1-unit02-vocab` |
| 3 | 3 |  | `naming-things` | Naming Things | *(none: new skill)* |
| 4 | 4 |  | `describing-people` | Describing People | `a1-unit03-vocab` |
| 5 | 5 |  | `family` | Family | `a1-unit05-vocab` |
| 6 | 6 |  | `daily-routine` | Daily Routine | `a1-unit06-vocab` |
| 7 | 7 |  | `daily-routine-reflexive-verbs` | Daily Routine: Reflexive Verbs | *(none: new skill)* |
| 8 | 8 |  | `home` | At Home | `a1-unit07-vocab` |
| 9 | 9 |  | `supermarket` | At the Supermarket | `a1-unit08-vocab` |
| 10 | 10 |  | `demonstratives` | Demonstratives: This, That, and Over There | *(none: new skill)* |
| 11 | 11 |  | `ordering-cafe` | Ordering at a Café | *(none: new skill)* |
| 12 | 12 |  | `birthdays-celebrations` | Birthdays & Celebrations | `a1-unit10-vocab` |
| 13 | 13 |  | `kitchen` | In the Kitchen | *(none: new skill)* |
| 14 | 14 |  | `numbers-time-schedules` | Numbers, Time & Schedules | `a1-unit12-vocab` |
| 15 | 15 |  | `around-town` | Around Town | `a1-unit04-vocab` |
| 16 | 16 |  | `directions` | Directions | *(none: new skill)* |
| 17 | 17 |  | `weather` | Weather | *(none: new skill)* |
| 18 | 18 |  | `work-obligations` | Work & Obligations | *(none: new skill)* |
| 19 | 19 |  | `present-continuous` | What Are You Doing? (Present Continuous) | *(none: new skill)* |
| 20 | 20 |  | `health` | Health | *(none: new skill)* |
| 21 | 21 |  | `what-hurts` | What Hurts? (The Verb Doler) | *(none: new skill)* |
| 22 | 22 |  | `likes-dislikes` | What Do You Like? (Gustar) | *(none: new skill)* |
| 23 | 23 |  | `hobbies-free-time` | Hobbies & Free Time | *(none: new skill)* |
| 24 | 24 |  | `skills-abilities` | Skills & Abilities: Poder & Saber | *(none: new skill)* |
| 25 | 25 |  | `future-plans` | Future Plans | *(none: new skill)* |
| 26 | 26 |  | `travel-getting-away` | Travel & Getting Away | `a1-unit20-vocab` |

### A2 (33 units)

| es-es | es-latam | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|---|
| 1 | 1 |  | `your-trip` | Talking About Your Trip | `a2-unit01-vocab` |
| 2 | 2 |  | `what-you-have-done` | Talking About What You Have Done | `a2-unit02-vocab` |
| 3 | 3 |  | `day-out` | Talking About a Day Out | `a2-unit03-vocab` |
| 4 | 4 |  | `following-instructions` | Following Instructions | `a2-unit04-vocab` |
| 5 | 5 |  | `giving-reasons-opinions` | Giving Reasons and Opinions | `a2-unit05-vocab` |
| 6 | 6 |  | `comparing-trips-memories` | Comparing Trips and Memories | `a2-unit06-vocab` |
| 7 | 7 |  | `how-long` | Talking About How Long | `a2-unit07-vocab` |
| 8 | 8 |  | `making-responding-invitations` | Making and Responding to Invitations | `a2-unit08-vocab` |
| 9 | 9 |  | `experiences` | Talking About Experiences | `a2-unit09-vocab` |
| 10 | 10 |  | `keeping-touch` | Keeping in Touch | `a2-unit10-vocab` |
| 11 | 11 |  | `what-happened` | Talking About What Happened | `a2-unit11-vocab` |
| 12 | 12 |  | `giving-receiving-things` | Giving and Receiving Things | `a2-unit12-vocab` |
| 13 | 13 |  | `describing-events-time` | Describing Events in Time | `a2-unit13-vocab` |
| 14 | 14 |  | `asking-what-happened` | Asking About What Happened | `a2-unit14-vocab` |
| 15 | 15 |  | `explaining-what-happened` | Explaining What Happened | `a2-unit15-vocab` |
| 16 | 16 |  | `plans` | Talking About Plans | `a2-unit16-vocab` |
| 17 | 17 |  | `review-experiences` | Reviewing A2 Experiences | `a2-unit17-vocab` |
| 18 | 18 |  | `travel-goodbyes` | Talking About Travel and Goodbyes | `a2-unit18-vocab` |
| 19 | 19 |  | `the-future` | Talking About the Future | `a2-unit19-vocab` |
| 20 | 20 |  | `looking-back-moving-forward` | Looking Back and Moving Forward | `a2-unit20-vocab` |
| 21 | 21 |  | `imperfect-tense` | The Imperfect Tense | *(none: new skill)* |
| 22 | 22 |  | `imperfect-vs-preterite` | Imperfect vs. Preterite | *(none: new skill)* |
| 23 | 23 |  | `giving-instructions-directions` | Giving Instructions and Directions | *(none: new skill)* |
| 24 | 24 |  | `setting-rules-warnings` | Setting Rules and Warnings | *(none: new skill)* |
| 25 | 25 |  | `pronouns` | Explaining Who and What: Pronouns | *(none: new skill)* |
| 26 | 26 |  | `asking-politely-giving-advice` | Asking Politely and Giving Advice | *(none: new skill)* |
| 27 | 27 |  | `expressing-wishes-feelings` | Expressing Wishes and Feelings | *(none: new skill)* |
| 28 | 28 |  | `connecting-ideas-habits` | Connecting Ideas and Habits | *(none: new skill)* |
| 29 | 29 |  | `studying-school-life` | Studying and School Life | *(none: new skill)* |
| 30 | 30 |  | `por-and-para` | Prepositions in Action: Por vs. Para | `a2-unit30-vocab` |
| 31 | 31 |  | `indefinites-double-negation` | Indefinites and Double Negation: Alguien, Nadie, Algo, Nada | `a2-unit31-vocab` |
| 32 | 32 |  | `duration-recent-actions` | Life in Duration and Recent Actions: Verbal Periphrases | `a2-unit32-vocab` |
| 33 |  |  | `vosotros` | Speaking to the Group: Vosotros in Spain | `a2-unit33-vocab` |

### B1 (112 units)

| es-es | es-latam | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|---|
| 1 | 1 | core | `telling-stories` | Telling Stories | `b1-unit01-vocab` |
| 2 |  | cultura | `constitution-1978` | La Constitución Española de 1978 | `b1-constitucion-vocab` |
| 3 | 2 | core | `experiences-memories` | Experiences & Memories | `b1-unit02-vocab` |
| 5 | 3 | core | `plans-ambitions` | Plans & Ambitions | `b1-unit03-vocab` |
| 4 |  | cultura | `crown-head-of-state` | La Corona y la Jefatura del Estado | `b1-monarquia-vocab` |
| 7 | 4 | core | `giving-advice` | Giving Advice | `b1-unit04-vocab` |
| 9 | 5 | core | `relationships` | Relationships | `b1-unit05-vocab` |
| 6 |  | cultura | `cortes-generales` | Las Cortes Generales: Congreso y Senado | `b1-cortes-vocab` |
| 11 | 6 | core | `work-professional-life` | Work & Professional Life | `b1-unit06-vocab` |
| 13 | 7 | core | `education-learning` | Education & Learning | `b1-unit07-vocab` |
| 8 |  | cultura | `government-administration` | El Gobierno y la Administración del Estado | `b1-gobierno-vocab` |
| 15 | 8 | core | `travel-mobility` | Travel & Mobility | `b1-unit08-vocab` |
| 17 | 9 | core | `health-wellbeing` | Health & Wellbeing | `b1-unit09-vocab` |
| 10 |  | cultura | `judiciary-constitutional-court` | El Poder Judicial y el Tribunal Constitucional | `b1-judicial-vocab` |
| 19 | 10 | core | `home-housing` | Home & Housing | `b1-unit10-vocab` |
| 21 | 11 | core | `cities-communities` | Cities & Communities | `b1-unit11-vocab` |
| 12 |  | cultura | `regional-local-institutions` | Las Instituciones Autonómicas y Locales | `b1-autonomias-vocab` |
| 23 | 12 | core | `food-lifestyle` | Food & Lifestyle | `b1-unit12-vocab` |
| 25 | 13 | core | `media-information` | Media & Information | `b1-unit13-vocab` |
| 14 |  | cultura | `elections-participation` | Elecciones y Participación Ciudadana | `b1-participacion-vocab` |
| 27 | 14 | core | `technology-communication` | Technology & Communication | `b1-unit14-vocab` |
| 29 | 15 | core | `culture-entertainment` | Culture & Entertainment | `b1-unit15-vocab` |
| 16 |  | cultura | `armed-forces-security` | Fuerzas Armadas y Cuerpos de Seguridad | `b1-seguridad-vocab` |
| 31 | 16 | core | `environment` | The Environment | `b1-unit16-vocab` |
| 33 | 17 | core | `society-inequality` | Society & Inequality | `b1-unit17-vocab` |
| 18 |  | cultura | `spain-in-the-eu` | España en la Unión Europea | `b1-unioneuropea-vocab` |
| 35 | 18 | core | `politics-public-life` | Politics & Public Life | `b1-unit18-vocab` |
| 37 | 19 | core | `money-economy` | Money & the Economy | `b1-unit19-vocab` |
| 20 |  | cultura | `state-symbols` | Símbolos del Estado: Bandera, Escudo e Himno | `b1-simbolos-vocab` |
| 39 | 20 | core | `problems-solutions` | Problems & Solutions | `b1-unit20-vocab` |
| 41 | 21 | core | `opinions-arguments` | Opinions & Arguments | `b1-unit21-vocab` |
| 22 |  | cultura | `co-official-languages` | El Castellano y las Lenguas Cooficiales | `b1-lenguas-vocab` |
| 43 | 22 | core | `possibilities-predictions` | Possibilities & Predictions | `b1-unit22-vocab` |
| 45 | 23 | core | `making-decisions` | Making Decisions | `b1-unit23-vocab` |
| 24 |  | cultura | `instituto-cervantes` | Difusión Cultural: El Instituto Cervantes | `b1-cervantes-vocab` |
| 47 | 24 | core | `how-things-work` | Explaining How Things Work | `b1-unit24-vocab` |
| 49 | 25 | core | `change-development` | Change & Development | `b1-unit25-vocab` |
| 26 |  | cultura | `fundamental-rights` | Derechos y Libertades Fundamentales | `b1-derechos-vocab` |
| 51 | 26 | core | `work-ambition-balance` | Work, Ambition & Balance | `b1-unit26-vocab` |
| 53 | 27 | core | `social-life-communication` | Social Life & Communication | `b1-unit27-vocab` |
| 28 |  | cultura | `gender-equality` | Igualdad de Género y No Discriminación | `b1-igualdad-vocab` |
| 55 | 28 | core | `rules-rights-responsibilities` | Rules, Rights & Responsibilities | `b1-unit28-vocab` |
| 57 | 29 | core | `migration-identity` | Migration & Identity | `b1-unit29-vocab` |
| 30 |  | cultura | `civic-duties-taxes` | Deberes Ciudadanos y Sistema Tributario | `b1-deberes-vocab` |
| 59 | 30 | core | `culture-language-society` | Culture, Language & Society | `b1-unit30-vocab` |
| 61 | 31 | core | `future-society` | The Future of Society | `b1-unit31-vocab` |
| 32 |  | cultura | `constitutional-guarantees-ombudsman` | Garantías Constitucionales y Defensor del Pueblo | `b1-garantias-vocab` |
| 63 | 32 | core | `connecting-ideas` | Connecting Ideas | `b1-unit32-vocab` |
| 65 | 33 | core | `reported-speech` | Reported Speech | `b1-unit33-vocab` |
| 34 |  | cultura | `physical-geography` | Geografía Física: Relieve, Costas y Ríos | `b1-geografia-vocab` |
| 67 | 34 | core | `complex-opinions` | Complex Opinions | `b1-unit34-vocab` |
| 69 | 35 | core | `hypotheticals-possibilities` | Hypotheticals & Possibilities | `b1-unit35-vocab` |
| 36 |  | cultura | `northern-regions` | Comunidades del Norte y la Cornisa Cantábrica | `b1-norte-vocab` |
| 71 | 36 | core | `independent-spanish` | Independent Spanish | `b1-unit36-vocab` |
|  | 37 | latam | `pre-columbian-america` | Pre-Columbian America | `b1-precolombina-vocab` |
| 38 |  | cultura | `mediterranean-regions` | Comunidades del Mediterráneo e Islas Baleares | `b1-mediterraneo-vocab` |
|  | 38 | latam | `indigenous-civilizations` | Indigenous Civilizations | `b1-civilizaciones-vocab` |
|  | 39 | latam | `arrival-of-europeans` | The Arrival of the Europeans | `b1-llegadaeuropeos-vocab` |
| 40 |  | cultura | `central-southern-regions` | Comunidades del Centro, Sur y Canarias | `b1-centrosur-vocab` |
|  | 40 | latam | `conquest` | The Conquest | `b1-conquista-vocab` |
|  | 41 | latam | `colonial-society` | Colonial Society | `b1-sociedadcolonial-vocab` |
| 42 |  | cultura | `ceuta-melilla-municipalities` | Ceuta, Melilla y Municipios de España | `b1-ciudadesautonomas-vocab` |
|  | 42 | latam | `colonial-economy` | Colonial Economy | `b1-economiacolonial-vocab` |
|  | 43 | latam | `race-class-power` | Race, Class & Power | `b1-razaclasepoder-vocab` |
| 44 |  | cultura | `history-hispania-golden-age` | Historia: De Hispania al Siglo de Oro | `b1-historiaantigua-vocab` |
|  | 44 | latam | `independence` | Independence | `b1-independencia-vocab` |
|  | 45 | latam | `new-republics` | The New Republics | `b1-nuevasrepublicas-vocab` |
| 46 |  | cultura | `contemporary-history-transition` | Historia Contemporánea y Transición a la Democracia | `b1-historiacontemporanea-vocab` |
|  | 46 | latam | `caudillismo` | Caudillismo | `b1-caudillismo-vocab` |
|  | 47 | latam | `nation-nationalism` | Nation & Nationalism | `b1-nacionnacionalismo-vocab` |
| 48 |  | cultura | `spanish-literature` | Literatura Española: De Cervantes a la Generación del 27 | `b1-literatura-vocab` |
|  | 48 | latam | `liberalism-modernization` | Liberalism & Modernization | `b1-liberalismomodernizacion-vocab` |
|  | 49 | latam | `export-economies` | Export Economies | `b1-economiasexportacion-vocab` |
| 50 |  | cultura | `painting-sculpture` | Pintura y Escultura: Velázquez, Goya, Picasso y Dalí | `b1-arte-vocab` |
|  | 50 | latam | `social-change` | Social Change | `b1-cambiosocial-vocab` |
|  | 51 | latam | `revolution` | Revolution | `b1-revolucion-vocab` |
| 52 |  | cultura | `music-dance-cinema` | Música, Danza y Cine Español | `b1-musicacine-vocab` |
|  | 52 | latam | `mexican-revolution` | The Mexican Revolution | `b1-revolucionmexicana-vocab` |
|  | 53 | latam | `nationalism-state` | Nationalism & the State | `b1-nacionalismo-vocab` |
| 54 |  | cultura | `festivals-traditions` | Fiestas Nacionales, Autonómicas y Tradiciones | `b1-fiestas-vocab` |
|  | 54 | latam | `great-depression` | The Great Depression | `b1-grandepresion-vocab` |
|  | 55 | latam | `populism` | Populism | `b1-populismo-vocab` |
| 56 |  | cultura | `spanish-gastronomy` | Gastronomía Española y Dieta Mediterránea | `b1-gastronomia-vocab` |
|  | 56 | latam | `industrialization` | Industrialization | `b1-industrializacion-vocab` |
|  | 57 | latam | `cuban-revolution` | The Cuban Revolution | `b1-revolucioncubana-vocab` |
| 58 |  | cultura | `national-health-system` | El Sistema Nacional de Salud y la Tarjeta Sanitaria | `b1-sanidad-vocab` |
|  | 58 | latam | `cold-war` | The Cold War | `b1-guerrafria-vocab` |
|  | 59 | latam | `united-states-latin-america` | The United States & Latin America | `b1-eeuu-vocab` |
| 60 |  | cultura | `education-system` | El Sistema Educativo Español | `b1-educacion-vocab` |
|  | 60 | latam | `military-governments` | Military Governments | `b1-gobiernosmilitares-vocab` |
|  | 61 | latam | `political-repression` | Political Repression | `b1-represionpolitica-vocab` |
| 62 |  | cultura | `labour-market-social-security` | Mercado Laboral y Seguridad Social | `b1-empleo-vocab` |
|  | 62 | latam | `central-america-revolution-conflict` | Central America: Revolution & Conflict | `b1-centroamerica-vocab` |
|  | 63 | latam | `southern-cone-dictatorships` | The Southern Cone Dictatorships | `b1-conosur-vocab` |
| 64 |  | cultura | `housing-registration` | Vivienda, Registro y Empadronamiento | `b1-vivienda-vocab` |
|  | 64 | latam | `debt-crisis` | The Debt Crisis | `b1-crisisdeuda-vocab` |
|  | 65 | latam | `neoliberalism` | Neoliberalism | `b1-neoliberalismo-vocab` |
| 66 |  | cultura | `identity-documents` | Documentación: DNI, NIE y Registro Civil | `b1-documentacion-vocab` |
|  | 66 | latam | `democratization` | Democratization | `b1-democratizacion-vocab` |
|  | 67 | latam | `indigenous-movements` | Indigenous Movements | `b1-movimientosindigenas-vocab` |
| 68 |  | cultura | `transport-emergencies` | Transporte, Comunicaciones y Emergencias 112 | `b1-transporte-vocab` |
|  | 68 | latam | `regional-integration` | Regional Integration | `b1-integracionregional-vocab` |
|  | 69 | latam | `end-cold-war` | The End of the Cold War | `b1-finalguerrafria-vocab` |
| 70 |  | cultura | `consumer-banking-services` | Consumo, Horarios y Servicios Bancarios | `b1-consumobanca-vocab` |
|  | 70 | latam | `latin-america-1990s` | Latin America in the 1990s | `b1-latamnoventa-vocab` |
|  | 71 | latam | `legacy-20th-century` | The Legacy of the 20th Century | `b1-legadosigloveinte-vocab` |
| 72 |  | cultura | `ccse-mock-exam` | Simulacro General de Examen CCSE | `b1-simulacro-vocab` |
|  | 72 | latam | `latin-america-toward-2000` | Latin America Toward 2000 | `b1-americalatinadosmil-vocab` |
| 73 | 73 | core | `present-perfect-subjunctive` | The Past in the Mind: Present Perfect Subjunctive | `b1-unit37-vocab` |
| 74 | 74 | core | `sequence-of-tenses` | Time & Perspective: Sequence of Tenses & Reported Speech | `b1-unit38-vocab` |
| 75 | 75 | core | `verbs-of-becoming` | The Nuances of Change: Spanish Verbs of Becoming | `b1-unit39-vocab` |
| 76 | 76 | core | `connectors-prepositional-regimes` | Advanced Connectors & Prepositional Regimes | `b1-unit40-vocab` |

### B2 (72 units)

| es-es | es-latam | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|---|
|  | 1 | core | `nuance-precision-emphasis` | Nuance, Precision & Emphasis | `b2-unit01-vocab` |
|  | 2 | latam | `mexico-central` | Mexico I: Central Mexico & the Valley of Anáhuac | `b2-mexicocentro-vocab` |
|  | 3 | core | `narrative-time-aspect` | Narrative Time & Aspect | `b2-unit02-vocab` |
|  | 4 | latam | `mexico-north` | Mexico II: The North, the Border & Industrial Modernity | `b2-mexiconorte-vocab` |
|  | 5 | core | `hypothesizing-probability` | Hypothesizing & Probability | `b2-unit03-vocab` |
|  | 6 | latam | `mexico-south` | Mexico III: The South, Indigenous Pueblos & Biodiversity | `b2-mexicosur-vocab` |
|  | 7 | core | `influence-will-value-judgments` | Influence, Will & Value Judgments | `b2-unit04-vocab` |
|  | 8 | latam | `guatemala` | Guatemala: Mayan Heritage, Highland Communities & Modern Transitions | `b2-guatemala-vocab` |
|  | 9 | core | `doubt-denial-epistemic-stance` | Doubt, Denial & Epistemic Stance | `b2-unit05-vocab` |
|  | 10 | latam | `el-salvador-honduras` | El Salvador & Honduras: Copán, Memory, Migration & Resilience | `b2-salvadorhonduras-vocab` |
|  | 11 | core | `emotional-reactions-affective-stance` | Emotional Reactions & Affective Stance | `b2-unit06-vocab` |
|  | 12 | latam | `nicaragua` | Nicaragua: Land of Lakes, Volcanoes & Poetry | `b2-nicaragua-vocab` |
|  | 13 | core | `temporal-clauses-future` | Temporal Subordination & Future Prospections | `b2-unit07-vocab` |
|  | 14 | latam | `costa-rica` | Costa Rica: Demilitarization, Biodiversity & Democratic Welfare | `b2-costarica-vocab` |
|  | 15 | core | `concession-counter-argument` | Concession & Counter-Argument | `b2-unit08-vocab` |
|  | 16 | latam | `panama` | Panama: The Interoceanic Crossroads & Afro-Antillean Identity | `b2-panama-vocab` |
|  | 17 | core | `conditionals-potential-scenarios` | Conditionals I: Potential Scenarios | `b2-unit09-vocab` |
|  | 18 | latam | `belize-guianas` | Belize, Suriname & The Guianas: Multilingual Frontiers | `b2-guyanas-vocab` |
|  | 19 | core | `conditionals-counterfactuals-regrets` | Conditionals II: Counterfactuals & Regrets | `b2-unit10-vocab` |
|  | 20 | latam | `cuba` | Cuba: Island of Paradox, Revolution, Cinema & Music | `b2-cuba-vocab` |
|  | 21 | core | `mixed-restrictive-conditionals` | Mixed Conditionals & Restrictive Conditions | `b2-unit11-vocab` |
|  | 22 | latam | `dominican-republic` | Dominican Republic: The First European Settlement, Merengue & Transnational Identity | `b2-dominicana-vocab` |
|  | 23 | core | `purpose-clauses` | Finality, Purpose & Institutional Goals | `b2-unit12-vocab` |
|  | 24 | latam | `puerto-rico` | Puerto Rico: Boricua Identity, Sovereignty & Cultural Defiance | `b2-puertorico-vocab` |
|  | 25 | core | `relatives-unknown-antecedents` | Relative Clauses with Unidentified Antecedents | `b2-unit13-vocab` |
|  | 26 | latam | `colombia-andes` | Colombia I: The Andean Core, Coffee & Realism | `b2-colombiaandina-vocab` |
|  | 27 | core | `universal-indefinite-relatives` | Universal & Indefinite Relatives | `b2-unit14-vocab` |
|  | 28 | latam | `colombia-caribbean-pacific` | Colombia II: The Caribbean, Pacific, Afro-Colombian Heritage & Peace | `b2-colombiaperiferias-vocab` |
|  | 29 | core | `imperfect-subjunctive-forms-nuances` | The Imperfect Subjunctive: Forms & Nuances | `b2-15-vocab` |
|  | 30 | latam | `venezuela-oil-caracas` | Venezuela I: The Oil Century, Modernism & Caracas | `b2-venezuelapetroleo-vocab` |
|  | 31 | core | `pluperfect-subjunctive` | The Pluperfect Subjunctive in Independence | `b2-16-vocab` |
|  | 32 | latam | `venezuela-llanos-diaspora` | Venezuela II: The Llanos, Tepuis & Modern Diaspora | `b2-venezuelasabana-vocab` |
|  | 33 | core | `reported-speech-past-frames` | Reported Speech in Past Frames | `b2-17-vocab` |
|  | 34 | latam | `ecuador` | Ecuador: Plurinationalism, The Equatorial Andes & The Galápagos | `b2-ecuador-vocab` |
|  | 35 | core | `rhetorical-reporting-verbs` | Rhetorical Reporting Verbs | `b2-18-vocab` |
|  | 36 | latam | `peru-cusco-andes` | Peru I: Cusco, Tawantinsuyu & Andean Worldview | `b2-peruandino-vocab` |
|  | 37 | core | `passive-se` | The Passive with 'Se' | `b2-19-vocab` |
|  | 38 | latam | `peru-coast-lima` | Peru II: The Pacific Coast, Lima & The Gastronomic Vanguard | `b2-perucosta-vocab` |
|  | 39 | core | `analytical-resultative-passives` | Analytical & Resultative Passives | `b2-20-vocab` |
|  | 40 | latam | `bolivia-altiplano` | Bolivia I: The High Altiplano, Potosí & The Indigenous Majority State | `b2-boliviaaltiplano-vocab` |
|  | 41 | core | `impersonality-strategic-distance` | Impersonality & Strategic Distance | `b2-21-vocab` |
|  | 42 | latam | `bolivia-lowlands` | Bolivia II: The Lowlands, Eastern Amazonia & The Lithium Frontier | `b2-boliviaoriente-vocab` |
|  | 43 | core | `verbs-becoming-transformation` | Verbs of Becoming & Transformation | `b2-22-vocab` |
|  | 44 | latam | `chile-central` | Chile I: The Central Valley, Valparaíso & The Great Poets | `b2-chilecentro-vocab` |
|  | 45 | core | `inceptive-iterative-periphrases` | Inceptive & Iterative Periphrases | `b2-unit23-vocab` |
|  | 46 | latam | `chile-atacama-patagonia` | Chile II: The Extreme Geographies: Atacama, Patagonia & Mapuche Wallmapu | `b2-chileextremos-vocab` |
|  | 47 | core | `durative-progressive-periphrases` | Durative & Progressive Periphrases | `b2-24-vocab` |
|  | 48 | latam | `argentina-buenos-aires` | Argentina I: Buenos Aires, Tango & Porteño Culture | `b2-argentinaba-vocab` |
|  | 49 | core | `terminative-resultative-periphrases` | Terminative & Resultative Periphrases | `b2-25-vocab` |
|  | 50 | latam | `argentina-pampas-patagonia` | Argentina II: The Pampas, Patagonia & Regional Terroirs | `b2-argentinaregiones-vocab` |
|  | 51 | core | `modal-periphrases-conjecture-duty` | Modal Periphrases of Conjecture & Duty | `b2-26-vocab` |
|  | 52 | latam | `argentina-politics` | Argentina III: Politics, Passion, Peronism & The Human Rights Movement | `b2-argentinasociedad-vocab` |
|  | 53 | core | `prepositional-regimes-locutions` | Advanced Prepositional Regimes & Prepositional Locutions | `b2-27-vocab` |
|  | 54 | latam | `uruguay` | Uruguay: Secularism, Candombe & Progressive Institutions | `b2-uruguay-vocab` |
|  | 55 | core | `discourse-markers-structuring-sequencing` | Discourse Markers I: Structuring & Sequencing | `b2-28-vocab` |
|  | 56 | latam | `paraguay` | Paraguay: Guaraní Bilingualism, Jesuit Missions & The Chaco | `b2-paraguay-vocab` |
|  | 57 | core | `discourse-markers-reformulation-precision` | Discourse Markers II: Reformulation & Precision | `b2-29-vocab` |
|  | 58 | latam | `brazil-rio-sao-paulo` | Brazil I: The Cultural Engines: Rio, São Paulo & Modernism | `b2-brasilsudeste-vocab` |
|  | 59 | core | `discourse-markers-contrast-restriction` | Discourse Markers III: Contrast & Restriction | `b2-30-vocab` |
|  | 60 | latam | `brazil-northeast` | Brazil II: The Northeast, Afro-Brazilian Soul & The Sertão | `b2-brasilnordeste-vocab` |
|  | 61 | core | `discourse-markers-consequence-causality` | Discourse Markers IV: Consequence & Causality | `b2-31-01-vocab`, `b2-31-02-vocab`, `b2-31-03-vocab`, `b2-31-04-vocab`, `b2-31-05-vocab` |
|  | 62 | latam | `brazil-amazonia-brasilia` | Brazil III: Amazonia, Brasília & The Geopolitics of the Interior | `brasil-interior-01-vocab`, `brasil-interior-02-vocab`, `brasil-interior-03-vocab`, `brasil-interior-04-vocab`, `brasil-interior-05-vocab` |
|  | 63 | core | `advanced-concessives` | Subordinación adverbial I: Concesivas avanzadas y modales | `b2-32-01-vocab`, `b2-32-02-vocab`, `b2-32-03-vocab`, `b2-32-04-vocab`, `b2-32-05-vocab` |
|  | 64 | latam | `amazon-basin` | Amazonía Pancontinental: La cuenca compartida y el bioma sin fronteras | `amazonia-pan-01-vocab`, `amazonia-pan-02-vocab`, `amazonia-pan-03-vocab`, `amazonia-pan-04-vocab`, `amazonia-pan-05-vocab` |
|  | 65 | core | `complex-conditionals` | B2.33 Subordinación adverbial II: Condicionales complejas y contrafácticas | `b2-33-01-vocab`, `b2-33-02-vocab`, `b2-33-03-vocab`, `b2-33-04-vocab`, `b2-33-05-vocab` |
|  | 66 | latam | `regional-integration-corridors` | Integración regional, corredores bioceánicos y energía compartida | `integracion-01-vocab`, `integracion-02-vocab`, `integracion-03-vocab`, `integracion-04-vocab`, `integracion-05-vocab` |
|  | 67 | core | `dialect-variation-register` | B2.34 Sociolingüística y variación dialectal II: Léxico, registros y pragmática | `b2-34-01-vocab`, `b2-34-02-vocab`, `b2-34-03-vocab`, `b2-34-04-vocab`, `b2-34-05-vocab` |
|  | 68 | latam | `south-american-migration` | Migraciones suramericanas y diáspora: Desplazamientos, refugio y comunidades transnacionales | `migracion-01-vocab`, `migracion-02-vocab`, `migracion-03-vocab`, `migracion-04-vocab`, `migracion-05-vocab` |
|  | 69 | core | `formal-registers` | B2.35 Registros formales, ensayísticos y de prensa | `b2-35-01-vocab`, `b2-35-02-vocab`, `b2-35-03-vocab`, `b2-35-04-vocab`, `b2-35-05-vocab` |
|  | 70 | latam | `legal-pluralism` | Pluralismo jurídico, autodeterminación y derechos indígenas en el siglo XXI | `pluralismo-01-vocab`, `pluralismo-02-vocab`, `pluralismo-03-vocab`, `pluralismo-04-vocab`, `pluralismo-05-vocab` |
|  | 71 | core | `own-voice-synthesis` | B2.36 Síntesis B2: La voz propia en español | `b2-36-01-vocab`, `b2-36-02-vocab`, `b2-36-03-vocab`, `b2-36-04-vocab`, `b2-36-05-vocab` |
|  | 72 | latam | `latin-america-global` | América Latina en el escenario global: Identidad, multilateralismo y porvenir | `futuro-01-vocab`, `futuro-02-vocab`, `futuro-03-vocab`, `futuro-04-vocab`, `futuro-05-vocab` |

## Hungarian

### A1 (33 units)

| # | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|
| 1 |  | `reading-hungarian` | Learning to Read Hungarian | `a1-unit01-vocab` |
| 2 |  | `greetings-basic-interaction` | Greetings & Basic Interaction | `a1-unit02-vocab` |
| 3 |  | `introducing-yourself` | Introducing Yourself | `a1-unit03-vocab` |
| 4 |  | `numbers-personal-information` | Numbers & Personal Information | `a1-unit04-vocab` |
| 5 |  | `objects-locations` | Objects & Locations | `a1-unit05-vocab` |
| 6 |  | `family` | Family | `a1-unit06-vocab` |
| 7 |  | `describing-people` | Describing People | `a1-unit07-vocab` |
| 8 |  | `plurals-quantities` | Plurals & Quantities | `a1-unit08-vocab` |
| 9 |  | `possession` | Possession | `a1-unit09-vocab` |
| 10 |  | `foundations-review` | Foundations Review | `a1-unit10-vocab` |
| 11 |  | `where-things-are` | Where Things Are | `a1-unit11-vocab` |
| 12 |  | `going-places` | Going Places | `a1-unit12-vocab` |
| 13 |  | `everyday-actions` | Everyday Actions | `a1-unit13-vocab` |
| 14 |  | `questions-negation` | Questions & Negation | `a1-unit14-vocab` |
| 15 |  | `daily-routine` | Daily Routine | `a1-unit15-vocab` |
| 16 |  | `time-dates` | Time & Dates | `a1-unit16-vocab` |
| 17 |  | `frequency-word-order` | Frequency & Word Order | `a1-unit17-vocab` |
| 18 |  | `home` | At Home | `a1-unit18-vocab` |
| 19 |  | `food-drink` | Food & Drink | `a1-unit19-vocab` |
| 20 |  | `everyday-hungarian-review` | Everyday Hungarian Review | `a1-unit20-vocab` |
| 21 |  | `buying-food` | Buying Food | `a1-unit21-vocab` |
| 22 |  | `market` | At the Market | `a1-unit22-vocab` |
| 23 |  | `cafe` | At the Café | `a1-unit23-vocab` |
| 24 |  | `restaurant` | At the Restaurant | `a1-unit24-vocab` |
| 25 |  | `shopping` | Shopping | `a1-unit25-vocab` |
| 26 |  | `clothes-appearance` | Clothes & Appearance | `a1-unit26-vocab` |
| 27 |  | `city` | The City | `a1-unit27-vocab` |
| 28 |  | `transport-directions` | Transport & Directions | `a1-unit28-vocab` |
| 29 |  | `hobbies-free-time` | Hobbies & Free Time | `a1-unit29-vocab` |
| 30 |  | `friends-making-plans` | Friends & Making Plans | `a1-unit30-vocab` |
| 31 |  | `origin-cases` | Coming from Places: Origin Cases | `a1-unit31-vocab` |
| 32 |  | `languages-manner` | Languages & Manner: The Essive-Modal | `a1-unit32-vocab` |
| 33 |  | `postpositions` | Where Things Are: Postpositions | `a1-unit33-vocab` |

### A2 (44 units)

| # | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|
| 1 |  | `daily-life-routines` | Daily Life & Routines | `a2-unit11-vocab` |
| 2 |  | `time-dates-schedules` | Time, Dates & Schedules | `a2-unit12-vocab` |
| 3 |  | `family-life` | Family & Family Life | `a2-unit13-vocab` |
| 4 |  | `people-personality` | People & Personality | `a2-unit14-vocab` |
| 5 |  | `friends-relationships` | Friends & Relationships | `a2-unit15-vocab` |
| 6 |  | `home-housing` | Home & Housing | `a2-unit16-vocab` |
| 7 |  | `neighbourhood-city` | Neighbourhood & City | `a2-unit17-vocab` |
| 8 |  | `shopping-prices` | Shopping & Prices | `a2-unit18-vocab` |
| 9 |  | `food-eating-habits` | Food & Eating Habits | `a2-unit19-vocab` |
| 10 |  | `cooking` | Cooking | `a2-unit20-vocab` |
| 11 |  | `leisure-hobbies` | Leisure & Hobbies | `a2-unit21-vocab` |
| 12 |  | `culture-going-out` | Culture & Going Out | `a2-unit22-vocab` |
| 13 |  | `weather-seasons` | Weather & Seasons | `a2-unit23-vocab` |
| 14 |  | `transport-getting-around` | Transport & Getting Around | `a2-unit24-vocab` |
| 15 |  | `travel-holidays` | Travel & Holidays | `a2-unit25-vocab` |
| 16 |  | `hotels-accommodation` | Hotels & Accommodation | `a2-unit26-vocab` |
| 17 |  | `health-body` | Health & the Body | `a2-unit27-vocab` |
| 18 |  | `healthy-living-advice` | Healthy Living & Advice | `a2-unit28-vocab` |
| 19 |  | `school-language-learning` | School & Language Learning | `a2-unit29-vocab` |
| 20 |  | `review-life-leisure-health` | Review 1: Life, Leisure & Health | `a2-unit30-vocab` |
| 21 |  | `work-professions` | Work & Professions | `a2-unit31-vocab` |
| 22 |  | `verb-prefixes` | Verb Prefixes | `a2-unit32-vocab` |
| 23 |  | `ability-possibility-permission` | Ability, Possibility & Permission | `a2-unit33-vocab` |
| 24 |  | `the-past-1` | Talking About the Past I | `a2-unit34-vocab` |
| 25 |  | `the-past-2` | Talking About the Past II | `a2-unit35-vocab` |
| 26 |  | `telling-stories` | Telling Stories | `a2-unit36-vocab` |
| 27 |  | `future-plans` | Future Plans | `a2-unit37-vocab` |
| 28 |  | `suggestions-conditional` | Suggestions & Conditional | `a2-unit38-vocab` |
| 29 |  | `opinions-preferences-comparisons` | Opinions, Preferences & Comparisons | `a2-unit39-vocab` |
| 30 |  | `review-work-past-opinions` | Review 2: Work, Past & Opinions | `a2-unit40-vocab` |
| 31 |  | `problems-requests` | Problems, Requests & Everyday Communication | `a2-unit41-vocab` |
| 32 |  | `living-in-hungarian` | Living in Hungarian | `a2-unit42-vocab` |
| 33 |  | `pronouns-internal-surface-cases` | Declined Pronouns: Internal & Surface Cases | *(none: new skill)* |
| 34 |  | `pronouns-proximity-motion` | Declined Pronouns: Proximity & Motion | *(none: new skill)* |
| 35 |  | `translative-case` | Change of State: The Translative Case | `a2-unit45-vocab` |
| 36 |  | `essive-formal` | Roles & Capacities: The Essive-Formal | `a2-unit46-vocab` |
| 37 |  | `sociocultural-pragmatics-customs` | Sociocultural Pragmatics & Customs | `a2-unit47-vocab` |
| 38 |  | `lak-lek-suffix` | The -lak/-lek Verbal Suffix | *(none: new skill)* |
| 39 |  | `plural-possessed` | Possessions in the Plural: The Plural Possessed | *(none: new skill)* |
| 40 |  | `inflected-postpositions` | Inflected Postpositions: Personal Relations | *(none: new skill)* |
| 41 |  | `inflected-infinitives-necessity` | Inflected Infinitives & Necessity | *(none: new skill)* |
| 42 |  | `post-office` | Post Office, Mail & Parcel Lockers | *(none: new skill)* |
| 43 |  | `banking` | Banking, Payments & ATM Services | `a2-unit43-vocab` |
| 44 |  | `pharmacy` | Pharmacy, Medication & Medical Triage | `a2-unit44-vocab` |

### B1 (75 units)

| # | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|
| 1 | core | `longer-stories` | Telling a Longer Story | `b1-01-vocab` |
| 2 | citizenship | `hungary-today-land-symbols` | Hungary Today: Land & Symbols | `b1-orszagma-vocab` |
| 3 | core | `experiences-memories` | Experiences & Memories | `b1-02-vocab` |
| 4 | citizenship | `carpathian-basin-before-magyars` | The Carpathian Basin Before the Magyars | `b1-karpatmedence-vocab` |
| 5 | core | `plans-ambitions` | Plans & Ambitions | `b1-03-vocab` |
| 6 | citizenship | `honfoglalas` | The Honfoglalás (895) | `b1-honfoglalas-vocab` |
| 7 | core | `giving-advice` | Giving Advice | `b1-04-vocab` |
| 8 | citizenship | `saint-stephen` | Saint Stephen & the Founding of the State (1000) | `b1-istvankiraly-vocab` |
| 9 | core | `relationships` | Relationships | `b1-05-vocab` |
| 10 | citizenship | `arpad-dynasty` | The Árpád Dynasty | `b1-arpadhaz-vocab` |
| 11 | core | `work-professional-life` | Work & Professional Life | `b1-06-vocab` |
| 12 | citizenship | `mongol-invasion` | The Mongol Invasion (1241–42) | `b1-tatarjaras-vocab` |
| 13 | core | `education-learning` | Education & Learning | `b1-07-vocab` |
| 14 | citizenship | `angevin-kings` | The Angevin & Later Medieval Kings | `b1-anjouk-vocab` |
| 15 | core | `travel-mobility` | Travel & Mobility | `b1-08-vocab` |
| 16 | citizenship | `matthias-corvinus` | Matthias Corvinus & the Renaissance Court | `b1-matyas-vocab` |
| 17 | core | `health-wellbeing` | Health & Wellbeing | `b1-09-vocab` |
| 18 | citizenship | `mohacs-1526` | The Battle of Mohács (1526) | `b1-mohacs-vocab` |
| 19 | core | `home-housing` | Home & Housing | `b1-10-vocab` |
| 20 | citizenship | `three-part-hungary` | Three Parts of Hungary | `b1-haromresz-vocab` |
| 21 | core | `cities-communities` | Cities & Communities | `b1-11-vocab` |
| 22 | citizenship | `transylvania-golden-age` | Transylvania's Golden Age | `b1-erdelyaranykora-vocab` |
| 23 | core | `food-lifestyle` | Food & Lifestyle | `b1-12-vocab` |
| 24 | citizenship | `driving-out-ottomans` | Driving Out the Ottomans | `b1-torokkiuzese-vocab` |
| 25 | core | `media-information` | Media & Information | `b1-13-vocab` |
| 26 | citizenship | `rakoczi-war` | Rákóczi's War of Independence (1703–11) | `b1-rakoczi-vocab` |
| 27 | core | `technology-communication` | Technology & Communication | `b1-14-vocab` |
| 28 | citizenship | `18th-century-rebuilding` | The 18th Century: Rebuilding | `b1-mariaterezia-vocab` |
| 29 | core | `culture-entertainment` | Culture & Entertainment | `b1-15-vocab` |
| 30 | citizenship | `reform-age` | The Reform Age | `b1-reformkor-vocab` |
| 31 | core | `environment` | The Environment | `b1-16-vocab` |
| 32 | citizenship | `revolution-1848` | The 1848–49 Revolution | `b1-forradalom-vocab` |
| 33 | core | `society-inequality` | Society & Inequality | `b1-17-vocab` |
| 34 | citizenship | `kossuth-petofi-national-cause` | Kossuth, Petőfi & the National Cause | `b1-nemzetiugy-vocab` |
| 35 | core | `politics-public-life` | Politics & Public Life | `b1-18-vocab` |
| 36 | citizenship | `compromise-1867` | The Compromise of 1867 | `b1-kiegyezes-vocab` |
| 37 | core | `money-economy` | Money & the Economy | `b1-19-vocab` |
| 38 | citizenship | `austria-hungary` | Austria-Hungary | `b1-monarchia-vocab` |
| 39 | core | `problems-solutions` | Problems & Solutions | `b1-20-vocab` |
| 40 | citizenship | `world-war-1` | World War I & Collapse | `b1-vilaghaboru-vocab` |
| 41 | core | `opinions-arguments` | Opinions & Arguments | `b1-21-vocab` |
| 42 | citizenship | `trianon-1920` | The Treaty of Trianon (1920) | `b1-trianon-vocab` |
| 43 | core | `possibilities-predictions` | Possibilities & Predictions | `b1-22-vocab` |
| 44 | citizenship | `interwar-years` | The Interwar Years | `b1-horthykorszak-vocab` |
| 45 | core | `making-decisions` | Making Decisions | `b1-23-vocab` |
| 46 | citizenship | `world-war-2` | World War II in Hungary | `b1-masodikvh-vocab` |
| 47 | core | `how-things-work` | Processes & How Things Work | `b1-24-vocab` |
| 48 | citizenship | `rakosi-era` | The Communist Takeover & Rákosi Era | `b1-rakosikorszak-vocab` |
| 49 | core | `change-development` | Change & Development | `b1-25-vocab` |
| 50 | citizenship | `revolution-1956` | The 1956 Revolution | `b1-otvenhat-vocab` |
| 51 | core | `work-ambition-balance` | Work, Ambition & Balance | `b1-26-vocab` |
| 52 | citizenship | `kadar-era` | The Kádár Era & Goulash Communism | `b1-kadarkorszak-vocab` |
| 53 | core | `social-life-communication` | Social Life & Communication | `b1-27-vocab` |
| 54 | citizenship | `regime-change` | The Regime Change: From Communism to Democracy | `b1-rendszervaltas-vocab` |
| 55 | core | `rules-rights-responsibilities` | Rules, Rights & Responsibilities | `b1-28-vocab` |
| 56 | citizenship | `modern-democratic-hungary` | Modern Democratic Hungary & Euro-Atlantic Integration | `b1-demokracia-vocab` |
| 57 | core | `migration-identity` | Migration & Identity | `b1-29-vocab` |
| 58 | citizenship | `national-symbols` | National Symbols | `b1-nemzetijelkepek-vocab` |
| 59 | core | `culture-language-society` | Culture, Language & Society | `b1-30-vocab` |
| 60 | citizenship | `national-holidays-remembrance-days` | National Holidays & Remembrance Days | `b1-nemzetiunnepek-vocab` |
| 61 | core | `future-society` | The Future of Society | `b1-31-vocab` |
| 62 | citizenship | `fundamental-law` | The Constitution: Alaptörvény | `b1-alaptorveny-vocab` |
| 63 | core | `connecting-ideas` | Connecting Ideas | `b1-32-vocab` |
| 64 | citizenship | `government-institutions-today` | Government & Institutions Today | `b1-allamszervezet-vocab` |
| 65 | core | `reported-speech` | Reported Speech | `b1-33-vocab` |
| 66 | citizenship | `local-governments-public-administration` | Local Governments & Public Administration | `b1-onkormanyzat-vocab` |
| 67 | core | `complex-opinions` | Complex Opinions | `b1-34-vocab` |
| 68 | citizenship | `hungarian-culture-science-heritage` | Hungarian Culture, Science & Heritage | `b1-nemzetiertekek-vocab` |
| 69 | citizenship | `literary-musical-canon` | European & Hungarian Literary and Musical Canon | `b1-europaiorokseg-vocab` |
| 70 | core | `hypotheticals-possibilities` | Hypotheticals & Possibilities | `b1-35-vocab` |
| 71 | citizenship | `hungarians-abroad` | Hungarians Across the World & International Relations | `b1-magyarsag-vocab` |
| 72 | core | `independent-hungarian` | Independent Hungarian | `b1-36-vocab` |
| 73 | citizenship | `being-hungarian-citizen` | Being a Hungarian Citizen | `b1-allampolgarsag-vocab` |
| 74 | citizenship | `kormanyablak` | Public Administration & Kormányablak | `b1-kormanyablak-vocab` |
| 75 | citizenship | `tenancy-contracts` | Residential Tenancy & Housing Contracts | `b1-alberlet-vocab` |

### B2 (72 units)

| # | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|
| 1 | core | `nuance-focus-emphasis-narrative` | Nuance, Focus & Emphasis in Narrative | `b2-01-vocab` |
| 2 | culture | `nyugat-coffeehouses` | The Coffeehouse Republic: Nyugat & Print Culture | `b2-kavehazikultura-vocab` |
| 3 | core | `memory-nostalgia-sensory-description` | Memory, Nostalgia & Sensory Description | `b2-02-vocab` |
| 4 | culture | `fin-de-siecle-budapest` | Fin-de-Siècle Budapest & Hungarian Secession | `b2-szecesszio-vocab` |
| 5 | core | `language-style-word-formation` | Language, Style & Word Formation | `b2-03-vocab` |
| 6 | culture | `language-reform` | The Language Reform & the Politics of Hungarian | `b2-nyelvujitas-vocab` |
| 7 | core | `performance-drama-persuasion` | Performance, Drama & Persuasion | `b2-04-vocab` |
| 8 | culture | `national-theatre` | The National Stage: Theatre, Censorship & Politics | `b2-szinhazmuveszet-vocab` |
| 9 | core | `roots-tradition-collective-memory` | Roots, Tradition & Collective Memory | `b2-05-vocab` |
| 10 | culture | `bartok-kodaly` | Bartók, Kodály & the Ethnomusicological Revolution | `b2-bartokkodaly-vocab` |
| 11 | core | `aesthetics-vision-creative-obsession` | Aesthetics, Vision & Creative Obsession | `b2-06-vocab` |
| 12 | culture | `visual-arts-modernism` | Light, Myth & Modernism: Hungarian Visual Arts | `b2-festeszet-vocab` |
| 13 | core | `scientific-discovery-hypothesis` | Scientific Discovery & Hypothesis | `b2-07-vocab` |
| 14 | culture | `the-martians` | The 'Martians' of Budapest: Physics & Computing | `b2-marslakok-vocab` |
| 15 | core | `medicine-ethics-responsibility` | Medicine, Ethics & Responsibility | `b2-08-vocab` |
| 16 | culture | `medical-pioneers` | Semmelweis, Szent-Györgyi & Medical Pioneers | `b2-semmelweis-vocab` |
| 17 | core | `logic-paradox-abstract-reasoning` | Logic, Paradox & Abstract Reasoning | `b2-09-vocab` |
| 18 | culture | `mathematics-chess` | Non-Euclidean Worlds: Hungarian Mathematics & Chess | `b2-matematikasakk-vocab` |
| 19 | core | `mentorship-discipline-intellectual-growth` | Mentorship, Discipline & Intellectual Growth | `b2-10-vocab` |
| 20 | culture | `elite-education` | The Fasori & Eötvös Tradition: Elite Education | `b2-gimnaziumok-vocab` |
| 21 | core | `unconscious-dreams-inner-conflict` | The Unconscious, Dreams & Inner Conflict | `b2-11-vocab` |
| 22 | culture | `psychoanalysis` | The Budapest School of Psychoanalysis & the Mind | `b2-pszichoanalizis-vocab` |
| 23 | core | `ingenuity-design` | Ingenuity, Design & Practical Problem-Solving | `b2-12-vocab` |
| 24 | culture | `kempelen-to-rubik` | From Kempelen's Chess Turk to Rubik's Cube | `b2-talalmanyok-vocab` |
| 25 | core | `irony-satire` | Irony, Satire & Reading Between the Lines | `b2-13-vocab` |
| 26 | culture | `pesti-humor` | The Pesti Humor: Cabaret, Satire & Survival | `b2-pestihumor-vocab` |
| 27 | core | `visual-storytelling-perspective-time` | Visual Storytelling, Perspective & Time | `b2-14-vocab` |
| 28 | culture | `hungarian-cinema` | Allegory on Screen: A Century of Hungarian Cinema | `b2-magyarfilm-vocab` |
| 29 | core | `censorship-ambiguity-indirect-expression` | Censorship, Ambiguity & Indirect Expression | `b2-15-vocab` |
| 30 | culture | `three-ts-censorship` | The Three Ts: Censorship, Aczél's Cultural Policy & Samizdat | `b2-szamizdat-vocab` |
| 31 | core | `ideological-debates-public-polemics` | Ideological Debates & Public Polemics | `b2-16-vocab` |
| 32 | culture | `urbanists-populists` | Great Intellectual Debates: Urbanists vs. Populists | `b2-urbanusnepi-vocab` |
| 33 | core | `information-overload-rumor-verification` | Information Overload, Rumor & Verification | `b2-17-vocab` |
| 34 | culture | `public-sphere-history` | From the Town Crier to the Digital Public Sphere | `b2-mediatortenet-vocab` |
| 35 | core | `rhetoric-framing-mass-persuasion` | Rhetoric, Framing & Mass Persuasion | `b2-18-vocab` |
| 36 | culture | `monuments-political-memory` | Public Memory, Monuments & Political Rhetoric | `b2-politikairetorika-vocab` |
| 37 | core | `landscape-belonging-regional-character` | Landscape, Belonging & Regional Character | `b2-19-vocab` |
| 38 | culture | `regional-identities` | Alföld, Dunántúl & Felföld: Regional Identities | `b2-tajegysegek-vocab` |
| 39 | core | `social-mobility-class-opportunity` | Social Mobility, Class & Opportunity | `b2-20-vocab` |
| 40 | culture | `village-change` | The Changing Hungarian Village: From Tanya to Today | `b2-falutortenet-vocab` |
| 41 | core | `economic-cycles-crisis-adaptation` | Economic Cycles, Crisis & Adaptation | `b2-21-vocab` |
| 42 | culture | `goulash-to-single-market` | From Goulash Socialism to the European Single Market | `b2-gazdasagiatmenet-vocab` |
| 43 | core | `demographics-generations-life-course` | Demographics, Generations & the Life Course | `b2-22-vocab` |
| 44 | culture | `family-policy` | Demographics, Family Policy & Generational Shifts | `b2-demografia-vocab` |
| 45 | core | `urban-space-architecture-coexistence` | Urban Space, Architecture & Coexistence | `b2-23-vocab` |
| 46 | culture | `housing-estates-renewal` | Courtyards, Panel Estates & Urban Renewal | `b2-lakhatas-vocab` |
| 47 | core | `ecology-infrastructure-stewardship` | Ecology, Infrastructure & Stewardship | `b2-24-vocab` |
| 48 | culture | `danube-dams` | The Blue Danube: Ecology, Dams & Civic Awakening | `b2-kornyezetpolitika-vocab` |
| 49 | core | `law-justice-constitutional-principles` | Law, Justice & Constitutional Principles | `b2-25-vocab` |
| 50 | culture | `constitutional-history` | From the Historical Constitution to Constitutional Review | `b2-alkotmanytortenet-vocab` |
| 51 | core | `pluralism-heritage-minority-perspectives` | Pluralism, Heritage & Minority Perspectives | `b2-26-vocab` |
| 52 | culture | `nationalities` | Thirteen Nationalities & Shared Cultural Heritage | `b2-nemzetisegek-vocab` |
| 53 | core | `borders-kinship-transborder-identity` | Borders, Kinship & Transborder Identity | `b2-27-vocab` |
| 54 | culture | `hungarians-carpathian-basin` | Hungarian Communities Across the Carpathian Basin Today | `b2-hatarontul-vocab` |
| 55 | core | `exile-emigration-global-networks` | Exile, Emigration & Global Networks | `b2-28-vocab` |
| 56 | culture | `emigre-waves` | Global Hungarians: Émigré Waves & Returnees | `b2-diaszpora-vocab` |
| 57 | core | `diplomacy-alliances-sovereignty` | Diplomacy, Alliances & Sovereignty | `b2-29-vocab` |
| 58 | culture | `visegrad-geopolitics` | Central European Geopolitics & Visegrád Cooperation | `b2-kulpolitika-vocab` |
| 59 | core | `civic-participation-advocacy-public` | Civic Participation, Advocacy & Public Institutions | `b2-30-vocab` |
| 60 | culture | `ombudsman-civic-rights` | Public Administration, Ombudsman & Civic Rights | `b2-jogvedelem-vocab` |
| 61 | core | `gastronomy-conviviality-cultural-rituals` | Gastronomy, Conviviality & Cultural Rituals | `b2-31-vocab` |
| 62 | culture | `paprika-tokaj` | Paprika, Tokaj & Terroir: A Cultural History of Hungarian Cuisine | `b2-borkultura-vocab` |
| 63 | core | `competition-mastery-peak-performance` | Competition, Mastery & Peak Performance | `b2-32-vocab` |
| 64 | culture | `sport-national-identity` | From Alfréd Hajós to the Aranycsapat: Sport & National Identity | `b2-sporttortenet-vocab` |
| 65 | core | `political-philosophy` | Political Philosophy, Freedom & Historical Hysteria | `b2-33-vocab` |
| 66 | culture | `political-thought` | Central European Political Thought: Széchenyi, Eötvös, Polányi, Bibó | `b2-eszmetortenet-vocab` |
| 67 | core | `slang-register` | Slang, Register Shifting & Living Language | `b2-34-vocab` |
| 68 | culture | `youth-culture` | Beats, Festivals & Living Slang: Youth Culture Since the 1960s | `b2-ifjusagikultura-vocab` |
| 69 | core | `technology-futurism-human-agency` | Technology, Futurism & Human Agency | `b2-35-vocab` |
| 70 | culture | `knowledge-economy` | Hungary in the 21st-Century Knowledge Economy | `b2-tudomanyjovo-vocab` |
| 71 | core | `mastery-voice` | Mastery & Voice: Upper-Intermediate Synthesis | `b2-36-vocab` |
| 72 | culture | `speaking-hungarian-today` | Synthesis: What It Means to Speak and Understand Hungarian Today | `b2-magyaridentitas-vocab` |

### C1 (72 units)

| # | track | unit id | title | old vocabulary slugs (become aliases) |
|---|---|---|---|---|
| 1 | core | `argument-cohesion` | The Architecture of Argument & Logical Cohesion | `c1-01-vocab` |
| 2 | culture | `language-worldview` | Language as Worldview: Humboldt, Kosztolányi & Cognitive Linguistics | `c1-nyelvfilozofia-vocab` |
| 3 | core | `syntactic-compression` | Syntactic Compression & Dense Participial Modification | `c1-02-vocab` |
| 4 | culture | `hungarian-essay` | The Golden Age of the Hungarian Essay | `c1-esszemuveszet-vocab` |
| 5 | core | `hedging-evidentials` | Epistemic Hedging, Probability & Evidential Stance | `c1-03-vocab` |
| 6 | culture | `paradigm-shifts` | Epistemology & Scientific Paradigm Shifts | `c1-tudomanyelmelet-vocab` |
| 7 | core | `polemics-refutation` | The Mechanics of Polemics & Rhetorical Refutation | `c1-04-vocab` |
| 8 | culture | `public-debate` | The Art of Hungarian Public Debate | `c1-vitakultura-vocab` |
| 9 | core | `irony-understatement` | Irony, Understatement & Sarcastic Register Shifting | `c1-05-vocab` |
| 10 | culture | `urban-satire` | Urban Satire as Political Defense | `c1-pesti-ironia-vocab`, `c1-pestiironia-vocab` |
| 11 | core | `metaphor-idiom` | Metaphor, Idiomatic Resonance & Conceptual Blending | `c1-06-vocab` |
| 12 | culture | `hungarian-metaphors` | The Metaphorical Landscape of Hungarian | `c1-metaforak-vocab` |
| 13 | core | `legal-language` | Legal Syntactic Architecture & Normative Modality | `c1-07-vocab` |
| 14 | culture | `rule-of-law` | The Rule of Law & Constitutional Evolution | `c1-jogallamisag-vocab` |
| 15 | core | `passive-avoidance` | Institutional Impersonalization & Passive Avoidance | `c1-08-vocab` |
| 16 | culture | `transparency-redress` | Public Administration, Transparency & Civic Redress | `c1-kozszolgalat-vocab` |
| 17 | core | `bioethics` | Bioethics, Human Dignity & Moral Quandaries | `c1-09-vocab` |
| 18 | culture | `patient-rights` | Ethics in Medicine, Biotechnology & Patient Rights | `c1-bioetika-vocab` |
| 19 | core | `contracts-negotiation` | Contractual Precision, Ambiguity & Negotiation Register | `c1-10-vocab` |
| 20 | culture | `corporate-law` | Commercial Negotiation & Corporate Law in Hungary | `c1-szerzodesek-vocab` |
| 21 | core | `human-rights-law` | Human Rights, Minority Protections & International Law | `c1-11-vocab` |
| 22 | culture | `minority-protections` | Universal Human Rights & Minority Protections | `c1-emberijogok-vocab` |
| 23 | core | `civic-resistance` | Civic Resistance, Dissent & Legal Philosophy | `c1-12-vocab` |
| 24 | culture | `civil-disobedience` | Civil Disobedience & Democratic Checks | `c1-polgariengedetlenseg-vocab` |
| 25 | core | `macroeconomics` | Macroeconomic Architecture, Fiscal Policy & Monetary Stance | `c1-13-vocab` |
| 26 | culture | `forint-eurozone` | Monetary Sovereignty, the Forint & the Eurozone Dilemma | `c1-monetaris-vocab` |
| 27 | core | `energy-transition` | Ecological System Dynamics, Energy Transition & Green Taxonomy | `c1-14-vocab` |
| 28 | culture | `paks-nuclear` | Nuclear Energy, the Paks Dilemma & Renewables in the Carpathian Basin | `c1-energetika-vocab` |
| 29 | core | `artificial-intelligence` | Artificial Intelligence, Cognitive Systems & Algorithmic Reason | `c1-15-vocab` |
| 30 | culture | `ai-ethics` | AI Ethics, Neural Networks & Technological Sovereignty | `c1-mestersegesintelligencia-vocab` |
| 31 | core | `public-sphere` | Public Sphere, Rhetorical Framing & Deliberative Communication | `c1-16-vocab` |
| 32 | culture | `media-pluralism` | Media Pluralism, Algorithmic Filters & Information Integrity | `c1-mediakritika-vocab` |
| 33 | core | `regional-geopolitics` | Regional Geopolitics, Diplomatic Strategy & Transnational Coalitions | `c1-17-vocab` |
| 34 | culture | `visegrad-group` | The Visegrád Group (V4), Regional Alliances & European Cohesion | `c1-visegrad-vocab` |
| 35 | core | `digital-sovereignty` | Digital Sovereignty, Algorithmic Surveillance & Information Security | `c1-18-vocab` |
| 36 | culture | `cyber-warfare` | Cyber Warfare, Critical Infrastructure Protection & Citizen Resilience | `c1-kiberbiztonsag-vocab` |
| 37 | core | `social-stratification` | Sociological Stratification, Class Structures & Social Mobility | `c1-19-vocab` |
| 38 | culture | `centre-periphery` | Center vs. Periphery: Spatial Inequalities & Rural Transformations | `c1-tarsadalmireteg-vocab` |
| 39 | core | `drying-alfold` | Ecological Fragility, The Drying Alföld & Environmental Causality | `c1-20-vocab` |
| 40 | culture | `water-management` | Water Management, Drought Crises & Wetland Restoration | `c1-vizgazdalkodas-vocab` |
| 41 | core | `labour-economics` | Labor Economics, Technological Displacement & Collective Bargaining | `c1-21-vocab` |
| 42 | culture | `dual-labour-market` | The Dual Labor Market: Guest Workers, Gig Economy & Wage Convergence | `c1-munkaeropiac-vocab` |
| 43 | core | `computational-linguistics` | Computational Linguistics, Algorithmic Thought & Small-Language Survival | `c1-22-vocab` |
| 44 | culture | `small-language-ai` | Artificial Intelligence, Digital Sovereignty & Small-Language Ecology | `c1-mestersegesnyelv-vocab` |
| 45 | core | `urban-preservation` | Spatial Urban Geometry, Historic Preservation & Architectural Semiotics | `c1-23-vocab` |
| 46 | culture | `urban-sprawl` | Urbanism in Crisis: Agglomeration Sprawl, Transit & Brownfield Renewal | `c1-varosfejlesztes-vocab` |
| 47 | core | `academic-autonomy` | Epistemology of Research, Academic Autonomy & Scientific Discovery | `c1-24-vocab` |
| 48 | culture | `university-model-change` | The University in Turmoil: Model Change, Autonomy & The European Horizon | `c1-felsooktatas-vocab` |
| 49 | core | `separation-of-powers` | Constitutionalism, Separation of Powers & The Hierarchy of Legal Norms | `c1-25-vocab` |
| 50 | culture | `constitutional-breakdown` | Constitutional Breakdown: The Fundamental Law, Decrees & Institutional Capture | `c1-alkotmanyjog-vocab` |
| 51 | core | `press-freedom` | Media Ecology, Freedom of the Press & The Public Sphere | `c1-26-vocab` |
| 52 | culture | `media-capture` | Media Capture: The KESMA Empire, State Propaganda & Digital Resistance | `c1-mediaszabadsag-vocab` |
| 53 | core | `epidemiology` | Clinical Empiricism, Epidemiology & Medical Ethics | `c1-27-vocab` |
| 54 | culture | `healthcare-crisis` | Healthcare in Crisis: Doctor Wage Reforms, Nurse Shortages & Chamber Control | `c1-egeszsegugy-vocab` |
| 55 | core | `railway-modernization` | Transport Geography, Railway Modernization & Modal Infrastructure | `c1-28-vocab` |
| 56 | culture | `railway-decay` | Railway Decay vs. Highway Megaprojects: The MÁV Crisis, Branch Closures & Concessions | `c1-kozlekedespolitika-vocab` |
| 57 | core | `museums-monuments` | Museology, Monument Preservation & National Cultural Memory | `c1-29-vocab` |
| 58 | culture | `cultural-policy` | Cultural Policy Hegemony, the PKÜ Monopoly & the Plight of Independent Theatres | `c1-kulturalisorokseg-vocab` |
| 59 | core | `east-west-geopolitics` | Geopolitics, East vs. West & The Carpathian Basin Horizon | `c1-30-vocab` |
| 60 | culture | `pendulum-politics` | Pendulum Politics, Strategic Neutrality & Euro-Atlantic Crisis | `c1-geopolitika-vocab` |
| 61 | core | `historical-trauma` | Philosophy of History, Historical Trauma & Post-Communist Memory | `c1-31-vocab` |
| 62 | culture | `historical-revisionism` | The House of Terror, 1956 Revisionism & Historical Revisionism | `c1-emlekezetpolitika-vocab` |
| 63 | core | `fundamental-rights` | Constitutional Jurisprudence & Fundamental Rights | `c1-32-vocab` |
| 64 | culture | `judicial-independence` | The Dismantling of Independent Judiciary & Rule of Law Breakdown | `c1-biroifuggetlenseg-vocab` |
| 65 | core | `literary-modernism` | Hungarian Literary Modernism, Poetic Semiotics & Textual Hermeneutics | `c1-33-vocab` |
| 66 | culture | `literary-canon` | The Battle for the Literary Canon: NAT, Textbooks & Blacklists | `c1-irodalmielet-vocab` |
| 67 | core | `philosophy-of-science` | Philosophy of Science, Epistemic Rigor & Discovery | `c1-34-vocab` |
| 68 | culture | `mta-ceu` | The Stripping of MTA Research Institutes & The CEU Expulsion | `c1-tudomanyosszabadsag-vocab` |
| 69 | core | `digital-ethics` | Information Theory, Digital Ethics & Algorithmic Society | `c1-35-vocab` |
| 70 | culture | `pegasus-scandal` | The Pegasus Surveillance Scandal & State Cyber-Espionage | `c1-megfigyeles-vocab` |
| 71 | core | `democratic-tradition` | The Architecture of Liberty: Deák, Eötvös, Bibó & The Democratic Tradition | `c1-36-vocab` |
| 72 | culture | `civil-society` | The Democratic Minimum: Civil Society, Resistance & The European Horizon | `c1-magyarjovo-vocab` |
