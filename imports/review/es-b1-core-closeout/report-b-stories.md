# Report B: Spanish B1 closeout stories (es-es + es-latam)

Method: every story rewritten from the old text in place (same paragraph count and events), es-es first, es-latam generated from the es-es text with `scripts/course_variants.convert` (enfadada>enojada, coche>carro, salón>sala, billete>boleto; checked by hand: "salones de la alta sociedad" kept in b1-39). Files saved in `content/es-es|es-latam/stories/classics/b1/`. Sources saved in `sources/`: `pazos-gutenberg-18005.txt` (Spanish, Gutenberg 18005), `alice-gutenberg-11.txt`, `dorian-gutenberg-174.txt`, `perrault-fairytales-en-gutenberg-29021.txt` (English translation, Gutenberg 29021). Spanish Wikisource had no page for Los pazos de Ulloa (and answered 429); Gutenberg's Spanish text was used.

Defects common to the 24 original texts and the adaptations (found on first read), all fixed:
- Template sentences spliced in and repeated, often word for word twice in a row (b1-13 "La opinión inicial de los periodistas..." twice, b1-15 had 14 sentences of filler in the last paragraph, b1-14 "Había decidido actualizar el dispositivo y quería seguir conectado durante el viaje", b1-27 "La conversación terminó sin una reacción negativa...").
- Comprehension questions far above B1 (stems and options such as "¿Cuál es la lección deontológica...", "epistemológica", "vampirizar", "emolumentos", "vehacula" [typo], "consistorio", "circunspecta") and questions/explanations that claimed things the text does not say (b1-12: "hermano vegetariano", "ultraprocesados", "viajar a la aldea de su abuela"; b1-24 "revisa y embala"; b1-39 etc.). All questions rewritten: 3 per story, plain B1, one clear right option, `correctIndex` varied, explanation quoting what the text says.
- Level: removed *antes de que* (b1-20, b1-37), *después de que* (b1-13), *como si* (b1-36-pazos), rare words (*inexorable, yugo, clarines, tisú, jergón, retruécanos*, etc.). Forms kept are B1-core ones (imperfect subjunctive after a past verb, *si* + imperfect subjunctive + conditional, *si hubiera ... habría*). No -se forms, no *ojalá*, no *vosotros* anywhere (checked by regex in both courses).
- Labels: for the 24 originals the `source` said "inspired by themes of Dickens / Rousseau / Adam Smith / Mill / Wells / Schopenhauer / Thoreau / Austen / Paine / Sinclair / Huxley / Voltaire / Aurelius / Aesop, Homer, Swift ..." although the texts have nothing from those works. I replaced the claim by "Original text written for Parlour; not an adaptation of any work." (b1-15 keeps an honest note: imaginary film, loose echo of the portrait theme of Dorian Gray; b1-23, 24, 33, 35 say which work they are not). No `author`/`work` fields exist on the originals.
- NOT changed (instruction 8): `type`. Note for the reviewer: in es-latam b1-13...b1-35 `type` is "classic", in es-es "original"; b1-12 is "original" in both. An original labelled "classic" in es-latam is inconsistent; your call.

## b1-12 La mesa de Elena (es-es = es-latam, identical)
Verdict: rewritten. Wrong: question 2 "con su hermano vegetariano" and "sustituyendo ultraprocesados" (text: a *hermana* proposes, nothing about ultraprocessed food); paragraph 3 had "Su hermano vegetariano prefería un plato casero y elegía cada alimento nutritivo con cuidado" contradicting the sister two sentences earlier; "Elena quería preparar un plato equilibrado y buscaba una solución práctica para mantenerlo" repeated. Changed: removed repeats and the brother, simplified; questions about fast food, the sister's proposal, the final idea. Label unchanged (already honest). Sources: none needed.

## b1-13 La luz sobre la ciudad
Verdict: rewritten. Wrong: five sentences repeated verbatim ("Posteriormente, otro periodista declaró..." x2, "Los investigadores intentaban..." x2), metalanguage in the last paragraph ("El verbo declarar introduce una afirmación..."), *después de que*. Changed: de-duplicated, "ayer por la noche" (events at nine), questions rewritten (old Q3 "lección deontológica"). Label: now "Original news-style text ... about an imaginary event" (old "premise of early science-fiction news reporting, not H. G. Wells"). Sources: none.

## b1-14 Un día sin conexión
Verdict: fixed/rewritten. Wrong: "Había decidido actualizar el dispositivo y quería seguir conectado durante el viaje" (masculine, a trip that is not in the story), the update sentence twice. Changed: de-duplicated; "prescindir" > "dejar de usar". Questions simplified. Label: old claim "inspired by Forster's The Machine Stops" dropped. Sources: none.

## b1-15 Una reseña cultural
Verdict: rewritten. Wrong: last paragraph was 12 template sentences ("Una buena reseña debe describir, comparar y evaluar antes de recomendar", "El personaje principal consigue interpretar sus experiencias de una manera diferente", two conclusions). Changed: removed filler, kept the review structure (story, acting, image/music, novel comparison, opinion). Label: film and "Clara Ruiz" are invented, said so; the Dorian Gray echo is stated as loose. Questions: story, music, recommendation (old Q3 asked about "método de una crítica rigurosa", not in the text). Sources: none.

## b1-16 El bosque y el río
Verdict: fixed. Wrong: "Debido a la sequía, el bosque necesita más cuidado" (stuck in paragraph 1, contradicted the order of events), "Debido a ..." x3 as template. Changed: removed template sentences, kept events. Questions rewritten (old: "retroceso de la vegetación ribereña", "consistorio"). Label: Walden claim dropped.

## b1-17 Una ciudad, muchas vidas
Verdict: fixed. Wrong: filler pairs ("También se habló de la ayuda disponible...", "Algunos vecinos preferían opinar sobre las medidas antes de decidirse" ), "Algunas personas disfrutaban de ciertos privilegios..." repeating the sentence before. Questions: old ones used "metrópoli, vulnerabilidad, brecha social, corresponsable". Label: Dickens claim dropped.

## b1-18 Una reunión pública
Verdict: fixed. Wrong: "También se explicó que una ley puede decidir cómo se organiza un servicio público" and "Era necesario proteger los servicios y valorar si cada política era eficaz" were disconnected filler; "La participación de la ciudadanía era importante para el debate." Changed: removed. Questions: old Q1 "reivindicación expresa ... delegado ... dársenas" etc. replaced. es-latam questions had differed (celular); now same as es-es. Label: Rousseau claim dropped.

## b1-19 Precios y decisiones
Verdict: fixed. Wrong: "Si la inversión produjera una ganancia, la familia podría ahorrar más" (nobody invests in the story), "Se observaba que..." passive filler. Questions rewritten (old "coyuntura, liquidez, crediticias"). Label: Adam Smith claim dropped.

## b1-20 El puente y sus problemas
Verdict: fixed. Wrong: *antes de que la avería empeorara*, *antes de que la situación se agrave* (B2), "La falta de mantenimiento había desencadenado varios fallos" twice. Changed to "Querían actuar ya, porque el puente podía estar peor..." and "actuar a tiempo". Questions rewritten (old "pasarela", "peritaje", "titularidad"; old Q1 said "miles de usuarios", not in text). Label: fable claim dropped.

## b1-21 Un debate en la comunidad
Verdict: fixed. Wrong: first paragraph ended "Su postura parecía razonable para quienes buscaban una solución práctica" (whose?), "Una perspectiva diferente puede ser convincente cuando presenta argumentos y evidencia suficientes" (spliced). Questions rewritten (old: "nitidez, lesiva, cuotas de comunidad ... cámaras" - an invented topic). Label: On Liberty claim dropped.

## b1-22 La máquina y el futuro
Verdict: fixed. Wrong: "La previsión del científico parecía razonable, pero posiblemente sería incorrecta", "Su supuesto era que la máquina funcionaría" and other template sentences; "Es posible que nadie llegue a saberlo". Questions: old asked about "ingenio mecánico", "epistemológica", with a distractor about a telegraph network; rewritten.

## b1-23 Dos caminos
Verdict: rewritten (characters). Wrong: "Ulises y sus compañeros" in an invented episode that is not in the Odyssey (the story is a decision lesson with mountains/coast); that presents an invention as a classic. Changed: Ulises is now an invented guide, Julia, with a group of travellers; label says it is not the Odyssey. Duplicates removed ("Tenían que elegir entre dos opciones", "La ruta de las montañas tenía una ventaja clara..." repeating the paragraph before). Questions rewritten (old distractors "oráculo", "remeros").

## b1-24 La máquina de la isla
Verdict: rewritten (character). Wrong: "Gulliver" in an invented episode, not from Gulliver's Travels. Changed: invented traveller Mateo, label says not Gulliver's Travels. "pulsaba una palanca" > "bajaba una palanca"; template last sentence removed. Questions rewritten ("radioactivos", "alberca", "embala" removed).

## b1-25 El mundo en transformación
Verdict: fixed. Wrong: filler "También pensaba que era necesario mejorar algunos sistemas...", "En comparación con antes, ...", label claiming Schopenhauer (text has no Schopenhauer content; "un filósofo" is unnamed). Label replaced. Questions rewritten (old "tesis central", "celeridad", "enclaves").

## b1-26 Una idea diferente del éxito
Verdict: fixed. Wrong: "Durante años pensó en dedicarse a una profesión diferente, pero no quería medir su vida solo por el éxito o el fracaso" (garbled), "Es mejor tener una carrera interesante si no ocupa..." (garbled), the last paragraph's "Aprendió a aprovechar mejor el tiempo..." repeating. Questions rewritten (old "encrucijada existencial", "emolumentos", "vampirizar"). Label: Thoreau claim dropped.

## b1-27 Un mensaje mal interpretado
Verdict: fixed. Wrong: **Carlos** is a course character (Hungarian, Budapest) used here as an unnamed friend of Elena and Marta; renamed Pablo (rulebook: a story character with a course name gets a full name, renaming is simpler and avoids any link). "Elena decidió comunicarse indirectamente ... aunque prefería hablar directamente" contradicted the ending; now she decides to phone when the subject is delicate. Filler removed. Questions rewritten (old Q1 invented "un familiar tomó el teléfono", "teclado"). es-latam: *enojada*. Label: Pride and Prejudice claim dropped.

## b1-28 Una regla difícil
Verdict: fixed. Wrong: "estaba prohibido ignorarla", "Los ciudadanos tenían que cumplir la regla", "En la práctica, el cumplimiento era obligatorio para todos los comerciantes", "En esos casos, iba a estar permitido entrar..." (four sentences saying the same). Questions rewritten (old "ordenanza, peatonalización, viandante"). es-latam: *carro*. Label: Paine claim dropped.

## b1-29 Más de un hogar
Verdict: fixed. Wrong: "Su sentido de pertenencia todavía era fuerte..." (non sequitur), "Antes de llegar, había pensado mucho en emigrar" after the arrival, "Aquella doble identidad ya no le parecía un problema" repeating. Questions rewritten (old: "desarraigo", "consanguínea", "visado ... escondido de las autoridades" - invented). Label: The Jungle claim dropped (Sinclair's novel is about Lithuanian immigrants in Chicago; this text is not about it).

## b1-30 Muchas maneras de hablar (es-es = es-latam)
Verdict: fixed. Wrong: "También hablaron de la expresión y de la pronunciación" (vague), repeated "Para él, pertenecer a más de una comunidad..." and "El intercambio de ideas...". Questions rewritten (old "dialecto canónico", "gutarales", "vehacula" typo). Label (already "not a reproduction of any source text") kept in meaning.

## b1-31 Una sociedad por venir
Verdict: fixed. Wrong: template tail sentences in each paragraph ("La tendencia de este desarrollo...", "Cada posibilidad parecía probable...", "La previsión era una necesidad..."). Questions rewritten (old "sociolaboral prospectivo", "autómatas", "refugios subterráneos" invented). Label: Brave New World claim dropped (the story has nothing of Huxley's plot).

## b1-32 El camino de la ciudad
Verdict: rewritten. Wrong: five paragraphs ended in an exercise-style sentence ("La causa principal era..., y una razón importante...", "El objetivo de las reuniones era ... y la finalidad del proyecto era ...", "El argumento final se basaba en estas razones y consecuencias"). Removed. Questions rewritten (old "estrago climático", "derruye" [wrong verb], "gótica ... iglesia" invented). Label: Candide claim dropped.

## b1-33 Los testimonios
Verdict: fixed. Wrong: "El detective tomó nota de cada mensaje y comentario", "El detective tuvo que cambiar algunos detalles al reconstruir la conversación" (nonsense), paragraph 3 mixed up which witness said what (a witness who "vivía allí", another "había estado fuera"). Rewritten so the woman saw a man near the entrance and the second witness, inside, heard a door but saw nobody; the detective needs more information. Questions rewritten (old "pecuniarias", "inmueble"). Label: now says it is not a Sherlock Holmes story.

## b1-34 Una opinión cuidadosa
Verdict: fixed. Wrong: "Marco pensó que estaba seguro de que algunas ideas eran útiles" (ungrammatical logic), "presentó un argumento con varios matices, sin dejar ningún matiz sin explicar". "Marco" is not Marcus Aurelius; label now says original. Questions rewritten (old "circunspecta", "dogmatismos", "dialógica").

## b1-35 El camino de Alicia
Verdict: fixed. Wrong: nothing in the text is from Alice's Adventures except the name; label said "around themes associated with Alice". Now: "Original ... not an adaptation of Alice's Adventures in Wonderland". Small fixes ("Si pudiera elegir entre varias alternativas" while she can still choose). Questions rewritten (old "libre albedrío", "acaecido", "de boca" provisions invented).

## b1-37 Sherlock Holmes y el hombre desconocido
Verdict: rewritten. Wrong: label "Adapted from the public-domain detective stories of Sir Arthur Conan Doyle" but the scene (a sea captain deduced from his hands and sextant, a stolen chest) is not from any Holmes story I could identify; text at C1 ("método inductivo", "desglosar", "bergantín", "cabos de esparto", "pigmentación cobriza"), em-dash dialogue presented as the author's. Changed: relabelled "Pastiche escrito para Parlour a la manera de las historias de Sherlock Holmes de Arthur Conan Doyle; la escena es inventada y no es un texto suyo." (same model as b1-21-paliques; `author`/`work` left as the model), rewritten at B1, same four beats. Questions rewritten (old "destreza intelectual", "cuadrante" etc.). es-latam: *sala*, *boleto*. Sources: none (no Holmes text read); (unverified) that no Holmes story contains this scene; (unverified) "221B Baker Street", "John Watson", the 1892 date of the book, all known facts not checked against a text.

## b1-38 Alicia y la merienda de locos
Verdict: fixed (level, plot details). Source: Gutenberg 11, chapter 7 "A Mad Tea-Party" (English, read in full). Wrong: "gafas redondas" (invented), "sillón de mimbre" (invented; it is "a large arm-chair"), "el Señor Tiempo ... concierto de canciones en primavera" (it is a concert of the Queen of Hearts, last March), Alice leaves because "Then you shouldn't talk", not because the Hatter and the Hare try to put the Dormouse into the teapot (she sees that as she walks away). Level: C1 ("tertulia, retruécanos, peregrina razón, embutir"). Changed: rewritten at B1, events restored to the chapter (table under a tree, "no room", wine that does not exist, "your hair wants cutting", raven/writing-desk riddle with no answer, the watch that tells the day of the month, the quarrel with Time, always six o'clock, moving round as the cups get used, Dormouse pinched awake, Alice leaves, teapot). Label now says chapter 7 and that dialogue is retold, not Carroll's wording (riddle in «» is my Spanish rendering of the English line). Questions rewritten. (unverified) the 1865 date in `work` (not in the Gutenberg text).

## b1-39 El retrato que cambiaba
Verdict: rewritten. Source: Gutenberg 174 (English). Wrong: "desearía con toda su alma envejecer él jamás" (garbled wish; in the book he says he would give everything, "my soul", for the picture to age and him to stay young); no ending (the novel ends with Dorian stabbing the portrait with the knife that killed Basil, and the servants finding the portrait young and a dead, withered man whom they know only by his rings); "cortinaje de terciopelo carmesí" (the book: a purple satin coverlet), "buhardilla" (the old schoolroom, top of the house); C1 vocabulary. Changed: rewritten at B1 with the real ending (Basil's murder, the knife, the rings). The closing sentence is phrased as "Muchos lectores ven ... una advertencia" instead of stating the moral as Wilde's. Questions rewritten. (unverified) the 1890 date in `work` (not in the Gutenberg text).

## b1-40 Cenicienta y el zapato de cristal
Verdict: rewritten. Source: Gutenberg 29021 (Samber's English translation of Perrault, read in full; 1697 confirmed by its introduction). Wrong: "tras la muerte de su amado padre" (in Perrault the father is alive, he remarried), "baile de tres días" (one ball, Cinderella goes on two nights), "heraldos ... clarines" and "cocina comunal" (invented), "tisú de plata" (cloth of gold and silver), the fairy's rule "antes de que las campanas" (*antes de que*), the moral "la nobleza de alma siempre prevalece" (Perrault's moral is that grace is worth more than beauty). Changed: father alive, second night, six mice/rat/six lizards, forgiveness and the sisters housed in the palace, Perrault's real moral. Questions rewritten (old: "premisa dramática", "inexorable"). es-latam: *carro*.

## b1-36-pazosdeulloa La llegada a los Pazos de Ulloa (es-es only)
Verdict: rewritten. Source: Gutenberg 18005, Spanish text of chapter I (read in full). Wrong: dialogue invented as the author's ("Buenas tardes, hermano", "señor cura", "castaños" in the peón's directions), "salud delicada y rostro bondadoso", "administrador y capellán", "monteros armados" and "criados rústicos" and "Pedro Moscoso" (not in chapter I), the whole second half missing: the peón actually says to go to the pinar, left, right by a shortcut to the crucero ("Un bocadito"), and at the crucero two shots sound and Julián meets the marqués (a hunter), Primitivo and the abad; Julián was recommended by the marqués's uncle, el señor de la Lage, and says he is "servidor y capellán". Changed: p0 now follows the source ("miembros delicados, sin barba, parece casi un niño", hat pulled down, afraid of the horse, bad rider); the two dialogue lines follow the source's content, the question being a copy of the source sentence; "Un bocadito" copied from the source; last paragraph tells the real end of the scene (crucero, Pazos seen from afar, shots, marqués, uncle's letter, he laughs). `summary` rewritten; `characters` gained "El marqués de Ulloa"; label says dialogues are retold except the quoted question and "Un bocadito". Questions rewritten. Not done: Primitivo and the abad are left out of the retelling (said "tres cazadores"). (unverified) "Pedro Moscoso" was removed, not checked beyond the novel's later chapters (it is in the novel, line 1014, but not in chapter I).

## 5. Dictionary (audit-reader-coverage, es-es and es-latam, each story rewritten, --top 0)
"literal compound guess": none. "not in the dictionary" (all names, no common word):
sherlock | Sherlock | name | Sherlock Holmes's first name (b1-37, both courses)
gray | Gray | name | Dorian Gray's surname (b1-39, both courses)
hallward | Hallward | name | Basil Hallward's surname (b1-39, both courses)
lage | Lage | name | "el señor de la Lage", the marqués's uncle (b1-36-pazosdeulloa, es-es)

## Checks
- All 57 edited story files valid JSON; `validate-content.py --changed`: es-es 30 passed, es-latam 29 passed; `check-content.py --changed`: no new errors.
- `python3 build-manifest.py` ran clean (regenerated the manifests and decks; expected diff noise in `content/*/stories/manifest.json` and `decks.json`).
- `check-content.py es-es b1` and `es-latam b1`: no finding names any of these story files (the only story-path findings are `stories/world/b1/...` course-variant suspects).
- Regex scan of all 57 files: no *-se* subjunctive, *como si*, *antes de que*, *después de que*, *ojalá*, *vosotros/os* forms, no sentence repeated twice.
- Left alone on purpose: `id`, `level`, `type`, `lesson`, `estimatedMinutes`, narration timing; es-latam `type` mismatch (see above).
