REPORT (reader B): ES latam B1 Units 16, 17, 18. Nothing committed. Generator scripts (my own scratch) are in /home/user/parlour-read-b/.scratch/ (u16.py, u17.py, u18.py, ch16-18.py); they rewrite the files idempotently.

CHECK COUNTS (check-content errors/suspects, before -> after)
- U16 mexican-revolution 27/0 -> 0/0 ; U17 nationalism-state 21/2 -> 0/0 ; U18 great-depression 18/2 -> 0/0
- unmet words (with --with-hidden --challenges, after last edit): U16 5 (all names/inflection: Álvaro, Emiliano x2, Victoriano, *asesinado* = inflected form of listed *asesinar*); U17 2 (*Rivera* x2, a name); U18 0. Before: U16 about 150, U17/U18 over 100 each (old items).
- render_lesson: no "!!" in any of the 18 lessons. check_unit_refs --labels --bare: 0 in all three. check_es_c1_forms: no hit in my files (6 hits elsewhere, in b1-revolucioncubana-05, not mine). check_past_subjunctive: 0 in all three. Text lengths (words): U16 284/254/253/246/227; U17 248/257/239/239/224; U18 221/233/232/220/235.
- validate-content --changed: fails only on "locked tags changed" for the exercise files of the 18 lessons (their old tags were locked). Needs `lock_tags.py es-latam b1/<unit> --update --reason ...` by the reviewer; I did not run it (tags.lock.json is generated). Everything else passes.

PER LESSON (skill before -> after; screen; items)
Common to all 18 lessons: title, goal, `grammar` label, goal and checklist items rewritten in English (goal items = checklist items, "I can ..."); vocabulary lists rewritten (8 words, 9 in U16-03 [10: +devolución, asesinar], U16-01 [+norte], U17-02 [+indigenismo], U17-04 [+protesta], U18-03 [+afectado]); screen rewritten in English (recap + 4 new topic examples + tip); every exercise rewritten (same ids/types/counts, per-lesson file); reading questions in English with Spanish options; dialogue speakers Meg/Carlos only; dialogue-complete now `category dialogue` + unit vocab tag, structured-writing `category writing` (as the frozen B1/B2 models). Grammar files and ids keep their old (misleading) file names, because renaming would not show in `git diff` (e.g. b1-revolucionmexicana-02-subjuntivo-peticion-gr.json now holds reported speech).
U16
- -01 perifrasis-verbales -> same (*llevar* + gerund). Screen recap "from A2 Unit 28" names *seguir* + gerund, *empezar a* (not *acabar de*: checker says it first appears A2 Unit 32). Items: ex04 fb, ex06 builder (grammar); ex02/03/05 reading; ex07 dialogue; ex08 listening.
- -02 subjunctive-influence -> estilo-indirecto (B1 Unit 13): screen on *dijo que* + imperfect / pluperfect / conditional; ex04 *habían*, ex06 builder (Creelman sentence). No subjunctive.
- -03 (no tag) -> preterite-vs-imperfect: ex04 fb *formó*, ex06 builder (*era ... cuando proclamó*); were vocabulary-tagged.
- -04 relativas-preposicion-el-que (same; screen recap B1 Units 5 and 20): ex04 *en* el que, ex06 builder.
- -05 correlativos-no-solo-sino (later) -> ser-passive (B1 Unit 18): ex04 *repartidas*, ex06 builder.
- consolidation: tags now perifrasis-verbales (ex03, ex15), estilo-indirecto (ex04, ex12), preterite-vs-imperfect (ex05 with ds 2 pluscuamperfecto, ex06), ser-passive (ex13, ex16), vocab elsewhere. Old *se-impersonal, concesivas-aunque, formal-cause-connectors, ordering-markers* removed (not this unit's skills).
U17
- -01 preterito-perfecto -> pasiva-refleja (B1 Unit 6): ex04 *crearon*, ex06 builder.
- -02 a-pesar-de (same): ex04 *pesar*, ex06 builder.
- -03 futuro-perfecto -> cuanto-mas-tanto-mas (B1 Unit 2, both *a medida que* and *cuanto más*): ex04 *medida*, ex06 builder.
- -04 (no tag; was vocab) -> se-impersonal (B1 Unit 6): ex04 *se*, ex06 builder.
- -05 verbs-of-change (same): ex04 *convirtió*, ex06 builder; no *llegar a ser*.
- consolidation: pasiva-refleja ex03 and ex06 (sentence-order), a-pesar-de ex04, cuanto-mas ex05, se-impersonal ex12, verbs-of-change ex13 and ex16, pasiva ex15.
U18
- -01 perifrasis-verbales -> pluscuamperfecto (B1 Unit 1): ex04 *habían*, ex06 builder.
- -02 cuando-subjuntivo -> contrast-concession-connectors (B1 Unit 1): ex04 blank "Sin ___" = *embargo*, ex06 builder (blank is one word, since the connectors are two words).
- -03 superlatives (same): ex04 *peor*, ex06 builder.
- -04 prepositional-phrases (same; only *mediante* is taught on the B1 Unit 24 screens, so only *mediante* is used in items): ex04 *Mediante*, ex06 builder.
- -05 (no tag; was vocab) -> argument-markers (B1 Unit 13 *en resumen*, *lo más importante es que*; *por un lado ... por otro lado*, which the checker places first in B1 Unit 23, so the recap says "from B1 Unit 23", not the sheet's A2 Unit 28): ex04 *En*, ex06 builder.
- consolidation (14 items, types kept): ex02 pluscuamperfecto (ds 1 preterito-perfecto, 2 preterito-indefinido), ex04 superlatives, ex05 sentence-order contrast, ex06 argument-markers, ex13 prepositional-phrases, ex14 pluscuamperfecto; ex03 vocab fill-blank.
All skills are in the sheet's Known list; no skill used from "later"; no imperfect subjunctive anywhere.

FACTS (one per line; sure unless marked)
U16-01: Díaz president 1876, out 1880-1884 (sure); "más de treinta años" in 1910 (sure); Centenary celebrations Sept 1910 and Díaz turned 80 then (15 Sept, sure); railways and foreign investment mainly US and Britain (sure); oil wells from about 1900 (fairly sure, not dated); "los científicos" advisers (sure); laws that allowed survey and sale of land, villages lost land (sure); "hacia 1910 la mayoría de los campesinos no tenía tierra propia" attributed to "varios historiadores" (sure, no figure); debt peonage "en algunas regiones" (sure).
U16-02: Creelman interview 1908, Díaz said Mexico was ready for democracy and would accept an opposition party (paraphrase, fairly sure of the second half: unsure); Madero hacendado of Coahuila, book on the presidential succession, antireelection party, slogan *Sufragio efectivo, no reelección* (sure); candidate 1910, jailed in June before the election (sure); escaped to Texas, Plan de San Luis said the elections were a fraud and called for arms on 20 Nov 1910 (sure); Orozco and Villa took Ciudad Juárez May 1911 (sure); Díaz resigned May 1911, went to France (sure); Madero took office Nov 1911 (sure); "decía que había que respetar la ley" (characterisation, unsure); Huerta coup Feb 1913, Madero killed days later (sure).
U16-03: Zapata a peasant of Morelos, sugar haciendas (sure); backed Madero 1911, Plan de Ayala Nov 1911 demanded return of land, did not recognise Madero (sure); Villa in Chihuahua, fought with Madero 1911, formed División del Norte after Madero's death 1913 (sure), used trains (sure), won Zacatecas June 1914 (sure); Carranza governor of Coahuila, Constitutionalist Army, Huerta left July 1914 (sure); Villa and Zapata met at Xochimilco Dec 1914, troops entered the capital, no government, left within weeks (fairly sure on "pocas semanas"); Obregón beat Villa at Celaya 1915 (sure); Zapata killed in an ambush 1919, Villa assassinated 1923 (sure); neither was president (sure).
U16-04: Congress at Querétaro end of 1916, Constitution dated 5 Feb 1917 (sure); replaced the 1857 Constitution (sure); Art. 27: land and subsoil belong to the nation, State may divide haciendas and return land to villages, oil and minerals are the nation's (sure); Art. 123: 8-hour day, unions, strike (sure); Art. 3: public education lay, religious corporations not allowed to run primary schools (fairly sure on the second half: unsure); "según muchos historiadores una de las primeras del mundo con derechos sociales" (attributed; sure it is a standard claim); still the Constitution today (sure, dated "hoy").
U16-05: death toll disputed, "algunas estimaciones hablan de hasta un millón" (attributed; sure); Obregón assassinated 1928 right after re-election (sure); PNR founded 1929 by Calles, later PRI (sure); PRI won every presidential election until 2000 (sure, counts the PNR/PRM years); Cárdenas 1934-1940, haciendas shared out, ejidos (sure, no figure); oil expropriation 18 March 1938, workers had asked for better pay and the companies had not accepted a Supreme Court decision (sure); Pemex created shortly after (June 1938, sure).
U17-01: customs the main income c. 1900 (sure); German and French military missions in Chile, Peru, Argentina (fairly sure; Bolivia dropped); central banks in the 1920s "como Chile y México" (sure: both 1925); income tax introduced "en algunos países" (sure); ministries of education, health, labour (sure, general).
U17-02: Vasconcelos from 1921 invited painters (sure); Rivera, Orozco, Siqueiros (sure); indigenismo also state policy, critics today say communities stayed poor (attributed); Mariátegui 1928 *Siete ensayos de interpretación de la realidad peruana*, indigenous problem = land problem (sure); Semana de Arte Moderna Feb 1922, Teatro Municipal, São Paulo; Oswald de Andrade, Mário de Andrade, Anita Malfatti (sure).
U17-03: SEP 1921, Vasconcelos first secretary (sure); cultural missions train local teachers and teach agriculture, hygiene, trades (fairly sure); taught in Spanish in regions with indigenous languages (sure); Argentina law of 1884, primary compulsory, free, lay (sure); Uruguay Varela reform 1870s (sure, 1877); "el maestro rural fue la cara más visible del Estado" attributed to many historians (sure it is standard).
U17-04: censuses Argentina 1895 and 1914 (sure); civil registers (general); Rio de Janeiro 1904 smallpox vaccination law and protests (sure); compulsory military service Chile 1900, Argentina 1901 (sure); local leaders negotiated and kept power (general).
U17-05: Vargas in power 1930, Estado Novo 1937-1945, authoritarian, Congress closed (sure); historians judge differently (attributed).
U18-01: crash October 1929, 24 and 29 October (sure); people bought shares with borrowed money (sure); US banks closed, unemployment (sure); US tariff law of 1930 (sure); US/European banks had lent heavily to Latin American governments in the 1920s, then stopped (sure).
U18-02: export products by country (Brazil coffee, Cuba sugar, Argentina meat and wheat, Chile nitrate and copper; sure); League of Nations report names Chile worst hit (attributed, per reviewer-facts); Chilean mines closed (sure); Brazil bought coffee and burned part, price stayed low (sure); several governments stopped paying their foreign debts (sure).
U18-03: "la peor crisis económica hasta entonces" (sure, as the old text); customs the main tax income (sure); fewer imports, port and mining areas hit (fairly sure); tariffs raised (sure); no figures given.
U18-04: import substitution, name given later by economists (sure); tariffs and import permits (sure); São Paulo, Buenos Aires, Mexico City (sure); Brazil state steel company created 1941 (sure: CSN); Mexico oil from 1938 (sure); Chile corporation 1939 (CORFO, fairly sure); CEPAL created 1948, Prebisch (sure); critics: industries expensive and inefficient (attributed).
U18-05: Uriburu coup Sept 1930 in Argentina, Vargas revolution Oct 1930, end of the República Velha (sure); "en otros países también cayeron gobiernos" (sure, general); historians' summary (attributed).

OLD CLAIMS CUT OR CORRECTED (old -> new)
U16-01: Terrazas "millones de hectáreas", yaquis deported to Yucatán, "palacios de mármol", Limantour as leader, "ancianos tecnócratas" -> cut (unchecked or ornament); "34 años" -> "más de treinta".
U16-02: the quotation *Madero ha soltado al tigre...* -> cut (quote from memory); Díaz said Mexico was "maduro para la alternancia democrática" -> paraphrase; Madero "espiritista", Ypiranga, Tratados de Ciudad Juárez -> cut; "mantuvo intactos ... tribunales agrarios" -> cut (no such courts); "debilitando fatalmente su gobierno" -> cut.
U16-03: Huerta killing Pino Suárez, Torreón, "trenes blindados, hospitales móviles, caballería pesada", photo in the presidential chair, "trincheras y ametralladoras" at Celaya -> cut or simplified; "devolución inmediata de campos comunales" -> "devolución de las tierras a los pueblos".
U16-04: Teatro Iturbide, Múgica and the "jacobinos", "por primera vez en la historia del derecho universal" (-> attributed, "una de las primeras"), night work ban and weekly rest in Art. 123 (-> cut), "restituir tierras ejidales" -> simplified.
U16-05: "más de un millón" as a fact -> disputed estimates; "más de veinte millones de hectáreas ... La Laguna y Yucatán" -> cut (figure); "educación socialista", "fundando PEMEX" -> cut / "se creó Pemex"; "México evitó los golpes de sus vecinos" -> two attributed views.
U17-01: "Estados han emprendido" (present perfect), Bolivia missions, "concursos", "aduanas interiores abolidas", "timbre fiscal" -> cut or generalised.
U17-02: Tarsila do Amaral in the Semana (she was in Paris, unsure) and the *Manifiesto Antropófago* in 1922 (it is Oswald's, 1928) -> cut; Valcárcel, gamonalismo, ayllu -> cut; narrator judgements ("paradoja", "mitología homogeneizadora") -> critics' view, attributed.
U17-03: "miles de maestros a caballo", "seguramente habrán alcanzado", "varias veces superior" -> cut; ley 1420 -> "una ley de 1884".
U17-04: "clausuró definitivamente la era de las guerras civiles", "por primera vez" conscription -> cut; dates added.
U17-05: "Estado gendarme", "vigoroso Estado-nación ... vendaval de 1929" -> cut.
U18-01: Smoot-Hawley by name -> "una ley de 1930"; "numerosos países recesión", "final abrupto de una era dorada" -> cut.
U18-02: coffee lost "más del sesenta por ciento", copper and nitrate fell "más del ochenta por ciento", "decenas de miles de mineros en Atacama", coffee burned "en locomotoras" -> cut (figures/detail unchecked).
U18-03: exports fell "más del sesenta por ciento 1929-1932", "mayor contracción jamás" -> no figure.
U18-04: quotas, preferential exchange rates, beer, Medellín -> cut; ISI: dated 1941/1939/1938/1948 only.
U18-05: "ola de golpes en 1930 en Argentina, Brasil, Perú, Bolivia y Chile" (Chile's fell in 1931) -> Argentina and Brazil only; "era del populismo clásico" -> cut (later unit).

SPANISH I AM UNSURE OF (unsure)
- U16-02 "Madero, que era prudente, decía que había que respetar la ley" (characterisation); "aceptaría un partido de oposición" (paraphrase of Creelman).
- U16-04 "A las corporaciones religiosas tampoco se les permitía dirigir escuelas primarias" (Art. 3 content); "El artículo 123 hablaba del trabajo. Fijaba..." (imperfect for a document: natural? fine).
- U17-02 "que quería integrar a las comunidades indígenas en la vida nacional" (attribution of the policy's aim).
- U17-04 "Con el ferrocarril se viajaba más rápido, y con el telégrafo se enviaban mensajes en pocos minutos."
- U18-01 "los precios de muchos productos bajaron" (general); U18-03 "los productos que los países exportaban se volvieron más baratos que los que importaban" (terms of trade, general).

FOR THE USER
1. Locked tags: validate --changed fails on the 18 exercise files until `lock_tags.py ... --update --reason` is run by the reviewer.
2. Grammar file names and ids still carry the old topics (e.g. ...-02-subjuntivo-peticion-gr, ...-grandepresion-01-acabar-de-gr); renaming was left for you because a plain move would not appear in `git diff`.
3. U17 has orphan grammar files b1-nacionnacionalismo-0X-focus-gr.json and a story set b1-nacionnacionalismo-*.json (alias unit "nacion-nationalism"; untouched).
4. Names counted as unmet words (Álvaro, Emiliano, Victoriano, Rivera) and *asesinado* (inflection of listed *asesinar*) remain; the checker flags them, the brief allows them.
5. Reviewer to rebuild the combined readings b1-revolucionmexicana.json, etc. (not edited). Lesson `grammar` labels set to short English labels.
6. U18-05's *por un lado ... por otro lado* is recapped "from B1 Unit 23" (the first screen where the checker finds it), not A2 Unit 28 as the sheet says.
7. U16 uses *sigue siendo hoy la ley fundamental de México* and *hasta el año 2000* (present-day claims; dated "hoy"; check at read).
