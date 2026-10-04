# Grammar skill list: proposed frozen list (ROADMAP 125, step 2)

Status: **proposed 2026-10-04, waiting for the user's sign-off.** Once
approved, this becomes the frozen grammar skill list
([skill-tagging-spec.md](skill-tagging-spec.md) § "Frozen list"), and
any later addition, merge, split or rename has to be recorded on purpose.
Machine-readable: [grammar-skill-list.json](grammar-skill-list.json).
Families: [grammar-families-draft.md](grammar-families-draft.md).

## Summary

| | Spanish | Hungarian |
|---|---|---|
| grammar slugs today | 573 | 555 |
| skills in the proposed list | **184** | **203** |
| kept under their current slug | 136 | 148 |
| new names (old slugs become aliases) | 48 | 55 |
| old slugs merged into another skill | 333 | 366 |
| dropped as not grammar | 106 (1,425 exercises) | 41 (1,153 exercises) |
| skills under 6 exercises (⚠) | 8 | 9 |

Spanish exercise counts add es-es and es-latam together, so an exercise
shared by both courses counts twice.

## How the list was built

Every old grammar slug was handled by one of these rules, in order:

1. **Not grammar → dropped.** Country topics, policy topics, functions
   (greetings, café ordering) and catch-alls. Their exercises are retagged
   when each unit is read.
2. **Duplicates → one skill.** Same explanation under several names, e.g.
   `ir-infinitive` absorbs `ir-a-infinitivo`, `futuro-proximo` and
   `future-intention`.
3. **Topic copies → the generic skill.** E.g. HU's 17
   `c1-adv-proportional-…` skills become one `correlative-minel-annal`;
   es-latam's `amazonia-…`, `migracion-…`, `pluralismo-…` lesson skills
   join their grammar point.
4. **Uses of one form aren't separate skills.** Imperatives for directions,
   recipes and rules are the imperative; `condicional-planes` is
   `condicional-consejos`. One explanation fixes a wrong answer in any of
   them.
5. **Everything else is kept under its current slug.** A merged skill keeps
   the clearest old slug, or gets a new English name where every old one
   was topic-, level- or unit-bound (`c1-…`, `b2-…`). New names follow the
   house title style in `grammar-titles.json`.
6. **Level** is the lowest level any merged slug is used at today.

Skills under 6 exercises are flagged ⚠ and get exercises written during
the read-through (spec § "Coverage"), not merged away.

## Calls I made that you may want to overrule

1. **Spanish verbs of change are one skill** (`verbs-of-change`, 8 slugs
   merged). Textbooks teach *ponerse / volverse / hacerse / quedarse /
   llegar a ser / convertirse* as one comparison table. The alternative is
   two skills: temporary change (*ponerse, quedarse*) and lasting change
   (*hacerse, volverse, convertirse, llegar a ser*).
2. **HU personal pronouns with case endings are one skill**
   (`case-inflected-pronouns`: *nálam, tőlem, hozzám, rólam, bennem, rám,
   rajtam, velem*). The pattern is one explanation; picking the right case
   is tested by the case skills. The A1 dative series (*nekem, neked*)
   stays separate because it's taught first.
3. **HU verb government is split by case**: 8 skills (verbs taking
   *-ra/-re*, *-ban/-ben*, *-val/-vel*, *-hoz*, *-ról*, *-ért*, *-nak*,
   *-ból*), not one. Each case's verb list is learned separately.
4. **HU C1's ~190 topic skills collapse into a few discourse and register
   skills.** Two of them, `framing-markers` (18 old slugs, 140 exercises)
   and `evaluative-stance` (21 old slugs, 169 exercises), have no clear
   grammar point behind them. I expect to dissolve them when those units
   are read, retagging each exercise to whatever it really tests, instead
   of keeping two vague skills.
5. **HU *szeretnék* (A1) merges into the conditional** (`nek-conditional`,
   now level A1). It's the first conditional form learners meet, not a
   separate grammar point.
6. **Spanish slugs stay as they are, even when they're Spanish words**
   (`concesivas-aunque`, `subjuntivo-deseos`). Only new names are English.
   Renaming every Spanish-word slug to English would be consistent, but it
   adds churn with no gain: learners and authors see titles, not slugs.

## Spanish (es-es and es-latam, one list): 184 skills

### `word-formation`: word formation (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `nominalization` | nominalization in formal writing | B1 | 39 | `registro-nominalizacion-estilo-ensayistico`, `voz-y-registro-formal` |

### `nouns`: noun gender and number (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `gender` | noun gender | A1 | 34 |  |
| `plural` | plural formation of nouns and adjectives | A1 | 52 |  |

### `articles-demonstratives`: articles and demonstratives (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `articles` | definite and indefinite articles | A1 | 292 | `definite-article` |
| `demonstratives` | demonstratives este, ese and aquel | A1 | 239 | `aquel-aquella`, `ese-esa`, `este-esta` |
| `lo-neutro-abstraccion` | the neuter article lo for abstract qualities | A1 | 74 | `lo-adjetivo-que` |

### `possession`: possession (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `possessives` | possessive adjectives and pronouns | A1 | 70 |  |
| `tener` | uses of tener for possession, age, and sensations | A1 | 466 | `tener-expressions` |

### `numbers-quantity`: numbers and quantity (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `numbers` | cardinal and ordinal numbers | A1 | 72 | `compound-numbers` |

### `pronouns`: pronouns (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `pronombres-combinados` | double object pronouns and se lo | A1 | 292 |  |
| `subject-pronouns` | subject pronouns | A1 | 52 | `el-ella`, `pronouns` |
| `indefinidos-negativos` | indefinite pronouns and double negation | A2 | 116 |  |
| `objeto-directo` | direct object pronouns lo, la, los, and las | A2 | 198 |  |
| `objeto-indirecto` | indirect object pronouns me, te, le, nos, os, and les | A2 | 44 | `contraste-directo-indirecto` |

### `adjectives`: adjectives (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `adjective-agreement` | gender and number agreement of adjectives | A1 | 298 | `adjective-gender`, `adjective-plural` |

### `adverbs`: adverbs (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `intensificadores-y-grado` | intensifiers and expressions of degree | A1 | 34 |  |
| `frequency-adverbs` | adverbs of frequency | B1 | 38 | `habits-frequency` |

### `comparison`: comparison and manner (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `comparatives` | comparative constructions with más, menos, and tan | A2 | 530 |  |
| `cuanto-mas-tanto-mas` | proportional constructions with cuanto más... más and a medida que | B1 | 17 | `brasil-comparativas-proporcionales`, `integracion-modales-correspondencia` |
| `superlatives` | relative and absolute superlatives | B1 | 37 | `estructuras-ponderativas-pasion-popular` |
| `como-si` | como si + subjunctive | B2 | 3 ⚠ | `modales-hipoteticas-comparativas` |
| `manner-clauses` | manner clauses with según and como | B2 | 2 ⚠ | `modales-correlativas-avanzadas` |

### `prepositions-postpositions`: prepositions and postpositions (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `a-personal` | the personal a before animate direct objects | A1 | 32 |  |
| `preposiciones-movimiento` | prepositions of movement a, de, en and hacia | A1 | 64 |  |
| `por-vs-para` | the prepositions por and para | A2 | 127 | `para-purpose` |
| `prepositional-phrases` | formal prepositional phrases | B1 | 88 | `locuciones-preposicionales-formales`, `locuciones-prepositivas-conformidad-criterio`, `locuciones-prepositivas-espaciales`, `locuciones-prepositivas-pretexto-salvedad` |

### `verb-forms`: verb conjugation and the present (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `ar-verbs` | regular -ar verb conjugation | A1 | 66 |  |
| `er-ir-verbs` | regular -er and -ir verb conjugation | A1 | 78 | `comer` |
| `ir` | the verb ir and movement with a | A1 | 93 |  |
| `present-tense` | the present indicative | A1 | 418 | `habitual-present`, `regular-present` |
| `stem-changes` | stem-changing verbs in the present tense | A1 | 54 | `cambio-radical-reflexivos` |
| `vosotros-indicativo` | the vosotros verb conjugation *(es-es only)* | A2 | 42 |  |
| `voseo-rioplatense-reconocimiento` | recognizing rioplatense voseo in spoken and literary discourse *(es-latam only)* | B2 | 6 |  |

### `being-becoming`: being, becoming and existence (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `estar` | estar for location and temporary states | A1 | 292 | `descriptive`, `estar-sentirse-estados` |
| `hay` | existence with hay | A1 | 245 |  |
| `ser` | ser for identity, characteristics, and origin | A1 | 386 | `ser-origin` |
| `verbs-of-change` | verbs of change: ponerse, volverse, hacerse, quedarse, llegar a ser, convertirse | A1 | 204 | `seleccion-estilistica-verbos-cambio`, `sintesis-verbos-de-cambio`, `verbos-cambio`, `verbos-cambio-convertirse-transformarse` and 4 more |
| `resultar-adjective` | resultar + adjective | B1 | 38 | `evaluation` |

### `verb-patterns`: verb patterns and government (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `doler` | expressing pain and symptoms with doler | A1 | 90 | `doler-vs-tener` |
| `gustar` | verbs like gustar | A1 | 182 | `aptitud-academica`, `encantar-interesar`, `gusta-vs-gustan`, `gustar-infinitive`, `gustar-plural` |
| `saber-vs-conocer` | contrasting saber and conocer | A1 | 30 |  |
| `verbos-regimen-preposicional` | verbs with required prepositions | B1 | 154 | `change-experience`, `communication-patterns`, `regimen-preposicional-verbos-avanzados`, `verbos-regimen-preposicional-avanzado` |

### `past`: past tenses (14)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `alguna-vez` | talking about life experiences with alguna vez | A2 | 206 | `alguna-vez-nunca` |
| `imperfect` | the imperfect for descriptions and habits | A2 | 514 | `estados`, `imperfecto`, `imperfecto-habitual`, `imperfecto-past-description` |
| `past-participles` | regular and irregular past participles | A2 | 170 | `preterito-perfecto-participios` |
| `preterite-irregular-stems` | irregular preterite stems | A2 | 30 | `irregulares` |
| `preterite-vs-imperfect` | the preterite vs the imperfect | A2 | 215 | `contraste-pasados`, `estados-eventos`, `pret-indefinido-vs-imperfecto-narrativo` |
| `preterito-indefinido` | the preterite tense | A2 | 682 | `preterito-indefinido-narracion` |
| `preterito-perfecto` | the present perfect with haber + past participle | A2 | 724 | `change-comparison`, `present-perfect` |
| `preterito-perfecto-vs-indefinido` | contrasting the present perfect and the preterite | A2 | 302 |  |
| `secuencia-narrativa` | sequencing events in a narrative | A2 | 51 |  |
| `ya-todavia-no` | ya and todavía no with the present perfect | A2 | 766 | `todavia-no-perfecto`, `ya-perfecto` |
| `imperfect-vs-present-perfect` | the imperfect vs the present perfect for change over time | B1 | 76 | `change-over-time` |
| `pluscuamperfecto` | the pluperfect indicative with había + past participle | B1 | 164 | `pluscuamperfecto-retrospectiva` |
| `participios-irregulares-dobles` | irregular and double past participles in passive constructions | B2 | 5 ⚠ |  |
| `verbos-cambio-significado-pasado` | verbs with aspectual meaning shifts in past tenses | B2 | 7 |  |

### `future`: the future (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `ir-infinitive` | near future with ir a + infinitive | A1 | 724 | `future-intention`, `futuro-proximo`, `ir-a-infinitivo` |
| `futuro-simple` | the simple future tense | A2 | 444 | `future-predictions` |
| `future-probability` | the future and conditional of probability | B1 | 64 | `condicional-conjetura-pasado`, `estructuras-conjeturales-metafisicas`, `futuro-conjetura-presente-pasado`, `futuro-prospectiva-hipotesis-complejas` |
| `futuro-perfecto` | the future perfect with habrá + past participle | B1 | 3 ⚠ |  |

### `conditional`: conditions, hypotheses and wishes (13)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `condicional-consejos` | giving advice and making suggestions in the conditional | A2 | 98 | `condicional-planes` |
| `condicional-irregular` | irregular stems in the conditional | A2 | 22 |  |
| `condicional-regular` | regular forms of the conditional | A2 | 22 |  |
| `conditional-conjunctions` | conditional conjunctions with the subjunctive: con tal de que, a menos que, siempre que | B1 | 48 | `condicionales-a-condicion-con-tal`, `condicionales-como-no-advertencia`, `condicionales-con-tal-de-que`, `condicionales-exceptivas-a-no-ser-que` and 6 more |
| `hypothetical-structures` | hypothetical conditions with si + imperfect subjunctive | B1 | 455 | `condicionales-imperfecto-subjuntivo`, `future-conditional-subjunctive`, `imperfect-subjunctive-conditional`, `subjuntivo-imperfecto-hipotesis` |
| `pluscuamperfecto-subjuntivo-si` | counterfactual past conditions with si + pluperfect subjunctive | B1 | 62 | `condicional-contrafactico-pasado`, `condicionales-tercer-tipo-contrafactico`, `nordeste-condicionales-irreales` |
| `si-clauses` | conditional sentences with si | B1 | 218 | `condicionales-reales-si` |
| `apodosis-condicional-literaria` | stylistic variation in conditional apodosis clauses | B2 | 13 | `pluscuamperfecto-subjuntivo-apodosis` |
| `counterfactual-wishes` | past wishes with ojalá and quién + pluperfect subjunctive | B2 | 8 | `desiderativas-contrafacticas-ponderativas`, `subjuntivo-pluscuamperfecto-ojala` |
| `implicit-conditionals` | conditions without si: de + infinitive and the gerund | B2 | 25 | `condicional-de-infinitivo`, `condicionales-gerundio-de-infinitivo`, `condicionales-pasadas-haber-participio`, `subjuntivo-pluscuamperfecto-de-haber` |
| `inversiones-condicionales-de-haber` | rhetorical inversion and concessive conditions with pluperfect subjunctive | B2 | 9 | `integracion-condicionales-inversion-enfasis` |
| `mixed-conditionals` | mixed conditionals | B2 | 17 | `amazonia-condicionales-mixtas-complejas`, `condicionales-mixtas-pasado-presente`, `condicionales-mixtas-presente-pasado` |
| `regrets-reproaches` | regrets and reproaches about the past | B2 | 12 | `lamento-reproche-condicional`, `subjuntivo-pluscuamperfecto-alternativas` |

### `subjunctive`: the subjunctive (12)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `subjunctive-emotion` | the subjunctive after emotions and reactions | A2 | 58 | `afeccion-psicologica-subjuntivo`, `empatia-pesar-subjuntivo`, `exclamativas-evaluativas-subjuntivo`, `reaccion-afectiva-subjuntivo`, `subjuntivo-emociones` |
| `subjunctive-influence` | the subjunctive after advice, requests and commands | A2 | 381 | `recommendations-subjunctive`, `subjuntivo-influencia-mandato`, `subjuntivo-peticiones-propuestas` |
| `subjunctive-value-judgments` | the subjunctive after impersonal value judgments: es importante que | A2 | 541 | `evaluation-recommendation`, `evaluation-subjunctive`, `expresiones-impersonales-subjuntivo`, `futuro-diplomacia-compromiso-vinculante` and 6 more |
| `subjuntivo-deseos` | the present subjunctive for wishes and hopes | A2 | 59 |  |
| `subjuntivo-morfologia` | present subjunctive morphology | A2 | 62 |  |
| `conectores-con-subjuntivo` | connectors like sin que and de ahí que with the subjunctive | B1 | 70 | `cause-consequence-solutions` |
| `correlacion-temporal-subjuntivo` | the imperfect subjunctive in past subordinate clauses | B1 | 50 |  |
| `subjunctive-doubt` | the subjunctive after doubt and probability: quizás, dudo que | B1 | 242 | `duda-negacion-lexica`, `expresiones-probabilidad`, `indicative-subjunctive-contrast`, `matizacion-epistemica-subjuntivo` and 3 more |
| `subjuntivo-perfecto` | the present perfect subjunctive | B1 | 116 |  |
| `imperfect-subjunctive-forms` | imperfect subjunctive forms in -ra and -se | B2 | 13 | `subjuntivo-imperfecto-ra-se`, `subjuntivo-imperfecto-registro` |
| `pluperfect-subjunctive-forms` | pluperfect subjunctive forms: hubiera and hubiese | B2 | 13 | `subjuntivo-pluscuamperfecto-formas`, `subjuntivo-pluscuamperfecto-literario` |
| `subjuntivo-imperfecto-estilistico-ra` | stylistic indicative use of ra form in formal prose | B2 | 6 |  |

### `imperative`: the imperative (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `imperativo-afirmativo` | affirmative informal and formal imperatives | A1 | 304 | `giving-directions`, `imperativo-afirmativo-regular`, `imperativo-direcciones`, `imperativo-normas`, `imperativo-recetas` |
| `imperativo-afirmativo-irregular` | irregular tú commands | A2 | 22 |  |
| `imperativo-formal-usted` | usted commands | A2 | 30 | `imperativo-negativo-formal` |
| `imperativo-negativo` | negative imperatives with the subjunctive | A2 | 40 | `imperativo-negativo-regular` |
| `imperativo-negativo-irregular` | irregular negative tú commands | A2 | 22 |  |
| `posicion-pronombres-imperativo` | pronoun placement with affirmative and negative imperatives | A2 | 12 |  |
| `vosotros-imperativo` | the vosotros imperative and pronoun placement *(es-es only)* | A2 | 16 |  |

### `aspect`: aspect, periphrases and verbal prefixes (16)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `progressive` | present progressive with estar + gerund | A1 | 134 | `conversacion-continuo`, `estar-ando`, `estar-iendo` |
| `acabar-de` | the periphrasis acabar de for recent actions | A2 | 41 | `acabar-de-infinitivo` |
| `llevar-tiempo-gerundio` | expressing duration with llevar and the gerund | A2 | 63 | `llevar-gerundio` |
| `perifrasis-verbales` | verbal periphrases for transitions and change | A2 | 59 |  |
| `seguir-gerundio` | continuity with seguir and continuar + gerund | A2 | 35 |  |
| `volver-a-infinitivo` | repetition with volver a + infinitive | A2 | 32 | `nordeste-perifrasis-reiterativas`, `perifrasis-volver-a` |
| `dejar-de-infinitivo` | cessation with dejar de + infinitive | B1 | 9 |  |
| `estar-a-punto-de` | imminent actions with estar a punto de + infinitive | B1 | 3 ⚠ |  |
| `gerundio-acciones-paralelas` | the gerund for parallel and simultaneous actions | B1 | 87 |  |
| `habitos-soler` | expressing habits with soler | B1 | 36 |  |
| `terminar-por-infinitivo` | culmination with acabar por and terminar por + infinitive | B1 | 9 |  |
| `gerund-periphrases` | ir, venir and andar + gerund | B2 | 33 | `perifrasis-andar-gerundio`, `perifrasis-ir-gerundio`, `perifrasis-venir-gerundio` |
| `inceptive-periphrases` | starting suddenly: echarse a, ponerse a, romper a | B2 | 18 | `perifrasis-echarse-a`, `perifrasis-ponerse-a`, `perifrasis-romper-a` |
| `perifrasis-dar-por-participio` | resultative periphrases with dar por plus participle | B2 | 6 |  |
| `perifrasis-llegar-a-infinitivo` | culminative periphrases with llegar a plus infinitive | B2 | 6 |  |
| `perifrasis-pasar-a` | transition periphrases with pasar a and sequential shifts | B2 | 7 |  |

### `modality`: obligation, ability, permission and probability (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `hay-que` | impersonal obligation with hay que | A1 | 44 | `perifrasis-haber-que-impersonal` |
| `querer-poder` | expressing wishes and ability with querer and poder | A1 | 28 |  |
| `saber-infinitivo` | saber + infinitive for abilities | A1 | 40 |  |
| `tener-que` | obligation with tener que + infinitive | A1 | 161 | `perifrasis-tener-que-infinitivo` |
| `deber-vs-tener-que` | deber vs tener que | B1 | 36 | `deber-tener-que-imperatives` |
| `perifrasis-deber-obligacion-conjetura` | modal distinction between deber and deber de plus infinitive | B2 | 6 |  |
| `perifrasis-haber-de-infinitivo` | formal modal periphrasis haber de plus infinitive | B2 | 10 | `interior-perifrasis-obligacion-atenuada`, `pluralismo-perifrasis-obligacion-estatutaria` |
| `perifrasis-modales-probabilidad-epistemica` | epistemic probability and conjecture with modal periphrases | B2 | 7 | `amazonia-perifrasis-probabilidad-retrospectiva` |

### `voice`: passive, impersonal, reflexive and causative (11)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `contraste-reflexivo` | reflexive vs non-reflexive verb meanings | A1 | 28 |  |
| `reflexives` | reflexive verbs and daily routines | A1 | 154 | `reflexive-verbs` |
| `pasiva-refleja` | the passive se construction | A2 | 455 | `migracion-pasivas-reflejas-generalizacion`, `pasiva-refleja-concordancia`, `pasiva-refleja-restricciones-agente` |
| `ser-passive` | the passive with ser + past participle | A2 | 240 | `paraguay-voz-pasiva-estilo`, `pasiva-analitica-geografia`, `pasiva-analitica-ser-participio`, `pasiva-complemento-agente-por` and 4 more |
| `se-impersonal` | impersonal constructions with se | B1 | 141 | `impersonal-constructions`, `impersonalidad-usos-costumbres`, `se-impersonal-avanzado`, `se-institucional-juridico` |
| `choosing-passive-type` | choosing between the ser, estar and se passives | B2 | 11 | `seleccion-estilistica-pasivas`, `sintesis-pasivas-analitica-estado` |
| `desambiguacion-valores-se` | pragmatic disambiguation of reflexive reciprocal and passive se | B2 | 10 | `brasil-voz-media-pronominal` |
| `impersonal-tercera-plural-uno` | third-person plural impersonals and indefinite uno | B2 | 5 ⚠ |  |
| `nominalizacion-despersonalizacion` | nominalization for depersonalization and agency omission | B2 | 10 | `registro-impersonalidad-distanciamiento-discursivo`, `sintesis-impersonalidad-distancia` |
| `pasiva-estado-estar-participio` | resultative state passive with estar and past participles | B2 | 6 |  |
| `se-pasivo-vs-impersonal` | distinguishing reflexive passive from impersonal se constructions | B2 | 12 | `sintesis-pasiva-refleja` |

### `non-finite`: infinitives, participles and gerunds (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `gerundios-irregulares` | irregular gerunds | A1 | 30 |  |
| `participios-absolutos-narrativos` | absolute participial clauses in narrative prose | B2 | 7 |  |

### `negation`: negation (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `negation` | negation and negative words | A1 | 6 |  |

### `questions`: questions (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `questions` | question words and interrogative sentences | A1 | 370 | `donde`, `entrevistas` |

### `word-order`: word order and focus (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `inversion-enfasis-fronting` | emphatic fronting and word order inversion | B2 | 18 | `focalizacion-discursiva-nortena` |
| `oraciones-hendidas-enfasis` | cleft sentences and focus constructions | B2 | 25 |  |

### `coordination`: joining clauses: and, but, or, not … but (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `connectors` | simple connectors like pero and sin | A1 | 22 |  |
| `correlativos-no-solo-sino` | correlative constructions no solo... sino también and tanto... como | B1 | 12 |  |
| `sino-vs-pero` | corrective conjunctions sino and sino que versus pero | B1 | 51 | `enfasis-contrastivo-sino` |

### `relative-clauses`: relative clauses (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `relativas-preposicion-el-que` | relative clauses with prepositions and el que or lo que | B1 | 84 | `describing-problems`, `futuro-relativos-complejos-tratados`, `paraguay-subordinadas-adjetivas`, `pluralismo-relativas-preposicionales-institucionales`, `relativos-preposicionales-complejos` |
| `relativas-subjuntivo` | relative clauses with an indefinite or negated antecedent + subjunctive | B1 | 83 | `amazonia-relativas-locativas-complejas`, `relativas-antecedente-inespecifico`, `relativas-antecedente-negativo`, `relativas-modo-indicativo-subjuntivo` and 4 more |
| `relative-clauses` | relative clauses with que and quien | B1 | 321 | `brasil-oraciones-relativas-especificativas`, `comparison-relative-clauses`, `description-relative-clauses`, `relativas-criterios-institucionales`, `relativas-especificativas` |
| `relativo-posesivo-cuyo` | possessive relative clauses with cuyo, cuya, cuyos, and cuyas | B1 | 22 | `relativos-posesivos-cuyo` |
| `relativas-universales-quiera` | universal relatives with cualquiera and quienquiera | B2 | 16 | `cuantificadores-universales-cuanto`, `migracion-relativas-indefinidas-distributivas` |

### `complement-clauses`: that-clauses and opinions (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `infinitive-vs-que-subjunctive` | infinitive vs que + subjunctive: same or different subject | A2 | 17 | `dos-sujetos-subjuntivo`, `infinitivo-vs-subjuntivo-correferencia` |
| `giving-opinions` | giving opinions with creo que and me parece que | B1 | 248 | `defending-opinions`, `explaining-trends-opinions`, `expresar-opiniones-preferencias` |
| `opinion-verbs-mood` | creo que + indicative vs no creo que + subjunctive | B1 | 336 | `creencia-negada-subjuntivo`, `opinion-subjunctive`, `subjunctive-negated-opinion`, `subjuntivo-opiniones-no-creo-que` |
| `el-hecho-de-que-subjuntivo` | subjunctive with the thematic frame el hecho de que | B2 | 8 |  |

### `time-clauses`: time clauses and expressions (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `antes-despues-infinitive` | antes de and después de + infinitive | A2 | 247 | `antes-de`, `antes-despues-infinitivo`, `despues-de` |
| `cuando-mientras` | simultaneous and sequential past actions with cuando and mientras | A2 | 217 | `conectores-temporales-pasado`, `interior-oraciones-temporales-avanzadas`, `mientras-durativas-simultaneidad` |
| `cuando-subjuntivo` | temporal clauses with cuando, en cuanto, and hasta que + subjunctive | A2 | 66 | `cada-vez-que-habitualidad`, `hasta-que-limite-temporal`, `migracion-clausulas-temporales-limite`, `temporales-prospeccion-subjuntivo` |
| `desde-desde-hace` | expressing duration with desde, desde hace, and hace... que | A2 | 203 |  |
| `antes-despues-de-que` | clauses with antes de que and despues de que | B2 | 16 | `temporales-antes-despues-que` |

### `cause-purpose-result`: cause, purpose and result (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `por-que-y-porque` | asking why and giving reasons with por qué and porque | A1 | 294 |  |
| `porque-y-por-eso` | connecting reasons and results with porque and por eso | A2 | 851 | `cause-consequence`, `consequence` |
| `formal-cause-connectors` | formal cause connectors: debido a, a raíz de, dado que | B1 | 81 | `amazonia-causales-explicativas-continuativas`, `conectores-causales-complejos`, `conectores-causales-formales`, `locuciones-prepositivas-causa-origen` and 5 more |
| `purpose-connectors` | prepositional phrases of purpose | B1 | 29 | `finales-con-vistas-a-miras-a`, `locuciones-prepositivas-finalidad-sacrificio` |
| `subjuntivo-de-finalidad-para-que` | purpose clauses with para que + subjunctive | B1 | 98 | `amazonia-oraciones-finales-institucionales`, `finales-negativas-para-que-no`, `finales-subjuntivo-a-fin-de-que`, `finalidad-a-fin-de-que` and 3 more |
| `consecutivas-de-tal-manera` | consecutive clauses of intensity and manner | B2 | 14 | `integracion-consecutivas-intensivas`, `interior-subordinadas-consecutivas-intensivas` |
| `consequence-markers` | consequence markers: por lo tanto, así que, por consiguiente | B2 | 8 | `marcadores-consecutivos-coloquiales`, `marcadores-consecutivos-formales`, `marcadores-ilativos-deductivos` |

### `concession`: concession (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `concesivas-aunque` | concessive clauses with aunque and a pesar de que | A2 | 118 | `concesivas-aunque-modo`, `conectores-causales-concesivos` |
| `a-pesar-de` | a pesar de (que) and pese a | B1 | 31 | `concesivas-a-pesar-de-por-mas-que`, `concesivas-enfaticas-pesar-de-que`, `concesivas-pese-a` |
| `contrast-concession-connectors` | connectors of contrast and concession: sin embargo, no obstante | B1 | 342 | `conectores-concesivos-adversativos`, `contrast-concession`, `interior-construcciones-concesivas-subjuntivo`, `marcadores-restriccion-concesiva`, `paraguay-concesivas-avanzadas`, `pluralismo-concesivas-oposicion-reivindicativa` |
| `concesivas-aun-cuando` | concessive clauses with aun cuando and the subjunctive | B2 | 23 | `concesivas-aun-cuando-riesgo`, `concesivas-politicas-aun-cuando`, `concesivas-riesgo-contingencia` |
| `concesivas-por-mas-que` | concessive clauses with por mas que and subjunctive | B2 | 31 | `concesivas-intensivas-cuantificadas`, `concesivas-intensivas-por-mas-que`, `concesivas-por-adj-que` |
| `concesivas-si-bien` | formal concessive clauses with si bien and the indicative | B2 | 20 | `concesivas-historicas-si-bien`, `futuro-concesivas-ponderacion-riesgos`, `migracion-concesivas-factuales-complejas` |
| `reduplicated-subjunctive` | reduplicated subjunctive: sea como sea, digan lo que digan | B2 | 16 | `concesivas-redundantes-duplicadas`, `concesivas-reduplicativas-relativas`, `subjuntivo-reduplicado-indiferencia` |

### `reported-speech`: reported speech (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `estilo-indirecto` | reported speech and tense shifting | B1 | 171 | `direct-indirect-speech`, `discurso-indirecto-tiempos-pasados`, `estilo-indirecto-testimonios` |
| `estilo-indirecto-informacion` | reported statements and citing sources with según | B1 | 168 |  |
| `estilo-indirecto-ordenes` | reporting orders and requests with the subjunctive | B1 | 73 | `discurso-indirecto-peticiones-subjuntivo` |
| `discurso-indirecto-deicticos` | shifting temporal and spatial deictic markers in narratives | B2 | 6 |  |
| `discurso-indirecto-interrogativas` | reporting questions and interrogative clauses in the past | B2 | 6 |  |
| `discurso-indirecto-libre` | free indirect discourse in narrative prose | B2 | 7 |  |
| `reporting-verbs` | reporting verbs: afirmar, advertir, negar, reprochar | B2 | 39 | `verbos-atribucion-denuncia`, `verbos-comunicacion-advertencia-recordatorio`, `verbos-comunicacion-aseverativos`, `verbos-comunicacion-disputa-refutacion`, `verbos-comunicacion-reproche-critica`, `verbos-comunicacion-subjetividad-conjetura` |

### `discourse-markers`: discourse markers and stance (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `ordering-markers` | ordering markers: primero, además, por un lado | A2 | 270 | `connectors-process-description`, `contrast`, `discourse-connectors`, `marcadores-continuidad`, `marcadores-distribucion`, `marcadores-ordenacion` |
| `argument-markers` | markers for building and closing an argument | B1 | 286 | `conectores-argumentativos`, `connected-opinion-writing`, `marcadores-conclusion`, `marcadores-reflexion-intelectual` |
| `contrast-markers` | contrast and counter-argument markers in discourse | B2 | 47 | `brasil-conectores-contraste`, `conectores-contraargumentativos-debate`, `conectores-contraste-discursivo`, `interior-conectores-contraargumentativos-formales` and 5 more |
| `hedging` | hedging and epistemic distance | B2 | 12 | `distanciamiento-epistemico-atenuacion`, `pragmatica-atenuacion-modalidad-epistemica`, `voz-modalizacion-epistemica-compleja` |
| `marcadores-digresion` | markers of digression and incidental commentary | B2 | 5 ⚠ |  |
| `reformulation-markers` | reformulation markers: es decir, o sea, mejor dicho | B2 | 26 | `marcadores-reformulacion-distanciamiento`, `marcadores-reformulacion-ejemplificativa`, `marcadores-reformulacion-explicativa`, `marcadores-reformulacion-recapitulativa`, `marcadores-reformulacion-rectificativa` |
| `refutacion-no-es-que-sino` | discursive refutation with no es que and sino que | B2 | 11 |  |
| `stance-adverbs` | focus and stance adverbs: precisamente, francamente | B2 | 17 | `adverbios-intensificadores`, `brasil-adverbios-foco` |

### `politeness-address`: politeness and forms of address (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `polite-softening` | softening requests: conditional, quisiera, indirect requests | A1 | 51 | `condicional-cortesia`, `condicionales-parenteticas-cortesia`, `cortesia-atenuacion-condicional`, `pragmatica-actos-habla-directivos-formales`, `subjuntivo-imperfecto-cortesia` |
| `sociolinguistica-tratamiento-cortesia` | forms of address and honorific deference in formal discourse | B2 | 3 ⚠ |  |

### `register-style`: register, style and rhetoric (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `essay-style` | essay style: structure, rhythm and density | B2 | 8 | `registro-densidad-lexica-sintesis`, `voz-cadencia-ritmo-sintactico`, `voz-organizadores-macroestructurales-ensayo` |
| `formal-register` | formal and institutional register | B2 | 13 | `generalizaciones-eticas-juridicas`, `registro-formulas-protocolarias-correspondencia`, `sociolinguistica-adecuacion-cambio-registro`, `voz-integracion-registro-estilo` |
| `rhetorical-devices` | rhetorical devices and metaphor | B2 | 13 | `nordeste-adjetivacion-estilo`, `recursos-retoricos-poesia`, `voz-metaforas-conceptuales-retorica` |

### Dropped: not grammar (106)

Their exercises are retagged when each unit is read: to the unit vocabulary skill, or to a grammar skill where the answer tests a form. Full list with reasons: [grammar-families-mapping.md](grammar-families-mapping.md) § "Not grammar skills".

- **dissolve** (1): `paraguay-adverbiales-lugar`
- **function-or-vocabulary** (13): `age-dates`, `cafe-interaction`, `clarification-explanation`, `doctor-interaction`, `full-directions`, `greetings`, `identity-description`, `introductions`, `invitaciones-y-pedidos`, `names`, `pedir-favores`, `time-dates` …
- **topic** (92): `abolicion-ejercito-pacto-civil`, `belice-multilinguismo-garifuna`, `biodiversidad-costarricense-geografia`, `bolivia-altiplano-sintesis-regional`, `bolivia-altiplano-titicaca-geografia`, `bolivia-carnaval-oruro-folclore`, `bolivia-chiquitos-misiones-selva`, `bolivia-coca-acullico-cosmovision`, `bolivia-estado-plurinacional-constitucion`, `bolivia-guerra-chaco-nacionalismo`, `bolivia-lapaz-elalto-cholets-cholitas`, `bolivia-oriente-sintesis-regional` …

## Hungarian: 203 skills

### `sounds-spelling`: sounds, spelling and stress (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `hungarian-consonant-sounds` | Hungarian consonant sounds | A1 | 15 |  |
| `hungarian-vowels` | short and long Hungarian vowels | A1 | 21 |  |

### `word-formation`: word formation (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `having-s` | forming adjectives with -s/-os/-es/-ös | A2 | 9 |  |
| `nominalization` | verbal nouns in -ás/-és | A2 | 127 | `b2-nominalization-chains`, `c1-action-nominalization`, `c1-nominal-compound-geopolitical-syntax`, `c1-nominal-compression` |
| `noun-compounds` | possessive and compound nouns | B1 | 5 ⚠ |  |
| `spatial-belonging-beli` | forming relational adjectives in -beli | B1 | 11 |  |
| `verbal-adjectives-hatatlan-hetetlen` | negative potential adjectives in -hatatlan/-hetetlen | B1 | 5 ⚠ |  |
| `sag-seg-nouns` | abstract nouns in -ság/-ség | C1 | 14 | `c1-deadjectival-abstraction` |

### `nouns`: noun gender and number (1)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `plural-nouns-k` | plural nouns with -k | A1 | 121 |  |

### `articles-demonstratives`: articles and demonstratives (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `definite-article-a-az` | the definite articles a and az | A1 | 34 | `the-definite-article-a-az` |
| `demonstratives-ez-az` | demonstratives ez and az | A1 | 157 | `ez-az-this-that`, `ezt-azt-this-one-that-one` |
| `indefinite-article-egy` | the indefinite article egy | A1 | 12 | `naming-objects-with-egy` |

### `possession`: possession (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `kinship-possessives` | family and kinship nouns with possessive suffixes | A1 | 71 |  |
| `possessive-pronouns-enyem` | possessive pronouns like enyém and tiéd | A1 | 22 |  |
| `possessive-suffixes` | possessive suffixes across persons | A1 | 215 | `possessive-m-om-em-om-my-family` |
| `van-possessive-to-have` | van with possessive suffixes for having | A1 | 149 |  |
| `3rd-person-possessive` | the third-person possessive -a/-e/-ja/-je | A2 | 26 |  |
| `acc-poss` | accusative -t on possessed nouns | A2 | 25 |  |
| `plural-possessive` | plural possessed nouns in -i | A2 | 99 | `plural-possessed-nouns` |
| `sajat` | emphatic possession with saját | A2 | 10 | `sajat-elet` |

### `numbers-quantity`: numbers and quantity (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `cardinal-numbers` | cardinal numbers | A1 | 37 | `numbers-11-100` |
| `containers-and-measures` | quantifiers and measure nouns | A1 | 69 |  |
| `fractions` | fractions: fél, negyed, harmad | A1 | 45 | `fel-and-negyed-halves-and-quarters` |
| `singular-after-numbers` | singular nouns after numbers and quantifiers | A1 | 176 | `plural-nouns-after-quantifiers`, `sok-egy-singular-noun` |
| `ordinal-numbers` | ordinal numbers in -dik | A2 | 14 |  |
| `sokat-eleget` | quantity adverbs sokat, keveset and eleget | A2 | 4 ⚠ |  |
| `szor-szer-multiplicatives` | how many times: -szor/-szer/-ször | A2 | 6 | `frequency-eszik-iszik` |
| `b2-proportional-rates` | proportional multiples and quantitative rate expressions in Hungarian | B2 | 89 |  |

### `pronouns`: pronouns (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `good-for-me-nekem-jo` | dative pronouns nekem, neked and neki | A1 | 121 |  |
| `personal-pronouns` | subject pronouns | A1 | 21 |  |
| `subject-pronouns-omission` | subject pronouns and pronoun omission | A1 | 129 | `subject-omission` |
| `case-inflected-pronouns` | personal pronouns with case endings: nálam, tőled, rá | A2 | 108 | `ablative-pronouns`, `adessive-pronouns`, `allative-pronouns`, `delative-pronouns-trio` and 4 more |

### `adjectives`: adjectives (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `adjective-order-before-the-noun` | adjectives before the noun | A1 | 121 |  |
| `plural-predicate-adjectives-k` | plural predicate adjectives in -ak/-ek | A1 | 26 |  |

### `adverbs`: adverbs (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `an-en-adverb` | manner adverbs in -an/-en | A1 | 56 |  |
| `direction-adverbs-jobbra-balra` | direction adverbs jobbra, balra and egyenesen | A1 | 39 |  |
| `egyutt-together` | adverbial együtt with plural verbs | A1 | 9 |  |
| `itt-ott-here-there` | location with itt and ott | A1 | 20 |  |
| `mindig-and-gyakran-frequency-adverbs` | frequency adverbs mindig, gyakran, néha and ritkán | A1 | 68 |  |
| `nagyon-very` | degree adverbs nagyon, elég and túl | A1 | 16 |  |
| `sequencing-elobb-aztan-utana-vegul` | sequencing events with először, aztán and végül | A1 | 137 |  |
| `scalar-adverbs` | scalar and degree adverbs in formal prose | C1 | 130 | `c1-adv-comparative-cybernetic-cognition`, `c1-adv-comparative-democratic-compromise`, `c1-adv-comparative-intertextuality-scalar`, `c1-adv-comparative-paradigmatic-shift` and 15 more |

### `comparison`: comparison and manner (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `comparative-bb` | comparative adjectives in -bb with mint | A2 | 68 |  |
| `olyan-mint` | comparisons of equality with olyan... mint | A2 | 8 |  |
| `superlative` | superlative adjectives with leg-...-bb | A2 | 9 |  |
| `correlative-minel-annal` | proportional comparisons with minél... annál | B1 | 260 | `b2-proportional-correlatives`, `c1-adv-proportional-academic-exclusion-isolation`, `c1-adv-proportional-academic-mobility`, `c1-adv-proportional-advertising-distortion` and 16 more |
| `kepest` | comparing with -hoz/-hez/-höz képest | B1 | 18 | `comparing-experiences-synthesis` |
| `mintha` | as if: mintha | B2 | 94 | `b2-resultative-similes`, `c1-adv-manner-comparative-similes` |

### `cases`: noun cases (20)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `ban-ben-in` | the -ban/-ben case | A1 | 256 | `inessive-location-chunks` |
| `delative-rol-rel` | the delative -ról/-ről | A1 | 30 |  |
| `elative-bol-bel` | the elative -ból/-ből | A1 | 59 |  |
| `how-the-accusative-t-works` | the accusative -t | A1 | 308 | `accusative-quantities-and-measures`, `accusative-without-a-linking-vowel`, `more-than-one-thing-the-plural-accusative-ket` |
| `kor-time` | telling time with -kor | A1 | 73 | `at-seven-o-clock-the-suffix-kor`, `telling-time-ora-and-mikor` |
| `movement-with-ba-be` | movement into with -ba/-be | A1 | 149 |  |
| `on-en-on` | the superessive -n/-on/-en/-ön | A1 | 154 | `days-superessive` |
| `ra-re` | movement onto with -ra/-re | A1 | 78 |  |
| `ul-ul-essive-modal` | languages and manner with -ul/-ül | A1 | 84 | `essive-modal-languages` |
| `val-vel` | the instrumental -val/-vel and assimilation | A1 | 93 | `travelling-by-the-suffix-val-vel` |
| `distributive-nkent` | the distributive suffix -nként | A2 | 26 |  |
| `essive-formal-kent` | the essive-formal suffix -ként | A2 | 98 |  |
| `hoz-suffix` | the allative -hoz/-hez/-höz | A2 | 16 |  |
| `nal-nel` | location at with -nál/-nél | A2 | 12 | `at-someones-place` |
| `nta-productive` | distributive time expressions in -nta/-nte | A2 | 6 |  |
| `terminative-case-ig` | the terminative -ig | A2 | 21 |  |
| `three-locatives` | three-way spatial case contrasts | A2 | 50 |  |
| `tol-tol` | from: -tól/-től, and -tól ... -ig | A2 | 20 | `from-to-tol-ig`, `from-tol-tol` |
| `translative-morphology` | the translative -vá/-vé and assimilation | A2 | 54 |  |
| `kent-vs-mint` | contrasting -ként and mint | B1 | 5 ⚠ |  |

### `prepositions-postpositions`: prepositions and postpositions (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `postpositions-basic` | postpositions: alatt, fölött, mellett, előtt, mögött, között, után | A1 | 188 | `postpositions-alatt-felett`, `postpositions-kozott-utan`, `postpositions-mellett-elott-mogott` |
| `inflected-postpositions` | personal inflected forms of postpositions | A2 | 100 | `interior-postpositions` |
| `keresztul` | the postposition keresztül with -n/-on/-en/-ön | A2 | 14 |  |
| `postpositions-altal-reven` | postpositions of means által, révén and helyett | A2 | 54 |  |
| `postposition-fele` | directional postpositions felé and felől | B1 | 6 |  |
| `b2-relational-compounds` | compound relational postpositions for social and economic analysis | B2 | 89 | `b2-relational-postpositions` |
| `b2-spatial-postpositions` | advanced spatial and directional postpositions in Hungarian | B2 | 96 | `c1-adv-spatial-geometric-connectors` |

### `verb-forms`: verb conjugation and the present (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `definite-vs-indefinite-conjugation` | definite vs indefinite verb conjugation | A1 | 143 | `definite-indefinite` |
| `ik-verbs-dolgozom-not-dolgozok` | present conjugation of -ik verbs | A1 | 63 |  |
| `megy-jon` | motion verbs megy and jön | A1 | 99 | `going-somewhere-the-irregular-verb-megy`, `going-the-irregular-verb-megy` |
| `present-tense-routine-language` | present tense verb conjugation | A1 | 241 | `present-tense-ok-ek-ok` |
| `eszik-iszik` | irregular verbs eszik, iszik and alszik | A2 | 9 |  |
| `lak-lek-suffix` | the -lak and -lek verbal suffix for you | A2 | 75 |  |

### `being-becoming`: being, becoming and existence (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `nem-vs-nincs-two-kinds-of-negation` | nem vs nincs | A1 | 17 |  |
| `van-and-nincs-there-is-there-isn-t` | van and nincs for existence | A1 | 264 | `existential-questions-van-itt`, `van-vannak-locative` |
| `van-zero-copula` | van and the zero copula | A1 | 331 | `predicate-adjectives-zero-copula`, `the-present-forms-of-lenni`, `vagyok-vagy-and-where-van-goes` |
| `valik-verb` | válik and tesz with -vá/-vé | A2 | 93 |  |

### `verb-patterns`: verb patterns and government (10)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `erdekel-construction` | expressing likes and interest with szeret, ízlik and érdekel | A1 | 84 |  |
| `verb-government-val-vel` | verbs governing -val/-vel | A1 | 61 | `egyetert-val-vel` |
| `faj-construction` | expressing pain and symptoms with fáj and van | A2 | 18 |  |
| `verb-government-ban-ben` | verbs and adjectives governing -ban/-ben | A2 | 35 |  |
| `verb-government-nak-nek` | verbs governing the dative -nak/-nek | A2 | 20 | `ad-dative-accusative`, `professional-qualifications` |
| `verb-government-ra-re` | verbs and adjectives governing -ra/-re | A2 | 61 | `szuksegem-van` |
| `verb-government-bol-bol` | verbs governing -ból/-ből | B1 | 6 | `bol-bol-all` |
| `verb-government-ert` | verbs and nouns governing -ért | B1 | 32 | `compromise-connectors` |
| `verb-government-hoz-hez` | verbs and adjectives governing -hoz/-hez/-höz | B1 | 33 | `modszer-usage` |
| `verb-government-rol-rel` | verbs governing -ról/-ről | B1 | 13 | `reflexive-support-verbs` |

### `past`: past tenses (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `definite-past` | definite past tense conjugation | A2 | 74 |  |
| `irregular-past` | irregular past forms: ment, jött, evett, ivott | A2 | 19 | `megy-jon-eszik-iszik-past` |
| `mar-experiential` | past experience with már and még soha nem | A2 | 70 |  |
| `past-tense-indefinite` | indefinite past tense conjugation | A2 | 137 | `past-tense-questions` |
| `van-past` | past tense forms volt and voltak | A2 | 16 |  |
| `historical-routines` | habitual past with szokás volt + infinitive | B1 | 3 ⚠ |  |

### `future`: the future (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `fog-infinitive` | future tense with fog + infinitive | A1 | 81 |  |
| `majd-adverb` | present tense for future plans with majd | A2 | 23 |  |

### `conditional`: conditions, hypotheses and wishes (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `nek-conditional` | present conditional in -na/-ne/-ná/-né | A1 | 206 | `szeretnek-the-conditional-ending-nek` |
| `ha-clause` | conditional sentences with ha and amennyiben | A2 | 5 ⚠ |  |
| `hypothetical-ha-conditional` | hypothetical clauses with ha and the conditional | A2 | 75 | `ha-lennek-helyedben` |
| `irregular-nek-conditional` | irregular conditional forms lenne, menne and enne | A2 | 5 ⚠ |  |
| `barcsak-wish` | wishes with bárcsak and szeretném, ha + conditional | B1 | 31 |  |
| `mixed-conditionals` | mixed conditionals and mintha clauses | B1 | 10 |  |
| `past-conditional-volna` | past counterfactual conditional with volna | B1 | 183 | `b2-speculative-conditionals`, `c1-complex-hypothetical-counterfactuals`, `c1-complex-hypothetical-linguistic-counterfactuals`, `c1-counterfactual-syntax`, `c1-syntax-invisible-constitution-doctrine`, `c1-syntax-republic-of-science-deduction` |
| `felteve-hogy-kiveve-ha` | conditions and exceptions: feltéve, hogy and kivéve, ha | C1 | 17 | `c1-legal-conditions`, `c1-restrictive-exceptive-adverbials` |

### `subjunctive`: the subjunctive (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `hogy-jon-jen` | subjunctive clauses with hogy + -jon/-jen/-jön | A2 | 65 | `c1-subjunctive-regulatory-mandates` |
| `mit-csinaljak` | deliberative subjunctive questions like mit csináljak | A2 | 4 ⚠ |  |
| `optative-subjunctive` | wishes and deliberation with the subjunctive: hadd, csak ... -jon | C1 | 8 | `c1-subjunctive-deliberative-optatives` |

### `imperative`: the imperative (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `imperative-indefinite` | indefinite imperative forms | A1 | 62 | `imperative-general` |
| `imperative-definite` | definite imperative verb forms | A2 | 8 |  |
| `junk-suggestion` | first-person plural suggestions in -junk/-jünk | A2 | 18 |  |

### `aspect`: aspect, periphrases and verbal prefixes (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `directional-preverbs` | directional preverbs: fel-, le-, be-, ki-, át- | A1 | 46 | `be-ki-meaning`, `fel-le-meaning`, `fel-le-szall` |
| `szokott-infinitive-habitual-actions` | habitual actions with szokott + infinitive | A1 | 21 |  |
| `jar-iskolaba` | habitual attendance with jár | A2 | 6 |  |
| `meg-meaning` | aspectual and separable verbal prefixes | A2 | 111 |  |
| `nominalizing-processes` | progressive state in -óban/-őben van | B1 | 5 ⚠ |  |
| `b2-figurative-preverbs` | figurative preverb contrasts for integration, motion, and change | B2 | 88 |  |
| `b2-frequentative-verbs` | frequentative and iterative verb forms in Hungarian | B2 | 83 |  |

### `modality`: obligation, ability, permission and probability (10)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `akar-tervez-infinitive` | wanting and planning: akar, tervez + infinitive | A1 | 32 | `tervez-infinitive` |
| `kell-infinitive` | obligation with kell and muszáj + infinitive | A1 | 44 |  |
| `lehet-infinitive` | impersonal possibility with lehet + infinitive | A1 | 59 |  |
| `kellene` | giving advice with kellene, érdemes and ajánlott | A2 | 23 |  |
| `potential-hat-het` | the potential suffix -hat/-het | A2 | 25 |  |
| `szabad-infinitive` | permission and prohibition with szabad and tilos | A2 | 41 |  |
| `tud-infinitive-skills` | personal ability with tud + infinitive | A2 | 21 |  |
| `formal-obligation` | formal obligation: köteles, kénytelen, -andó/-endő | B1 | 343 | `b2-legal-normative-register`, `c1-adv-juridical-normative-obligation`, `c1-complex-modal-contingency`, `c1-infinitive-predicative-necessity` and 27 more |
| `kellett-volna` | should have: kellett volna, lehetett volna | B1 | 101 | `b2-past-modals`, `past-obligation-kellett-volna` |
| `epistemic-modality` | must be, might be: epistemic modality | C1 | 22 | `c1-deontic-epistemic-distinction`, `c1-modal-probabilistic-modifiers`, `c1-modal-speculative-futurism` |

### `voice`: passive, impersonal, reflexive and causative (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `egymas` | reciprocal pronouns with egymás | A2 | 158 | `b2-reciprocal-distributive` |
| `mediopassive-verbs-odik` | mediopassive and reflexive verbs in -ódik and -ik | A2 | 130 | `b2-reflexive-middle`, `passive-avoidance-odik` |
| `causative-verbal-derivations` | causative verbs in -tat/-tet | B1 | 98 | `b2-causative-agents`, `c1-complex-sociological-causatives` |
| `agentless-constructions` | saying what happened without naming the doer | B2 | 127 | `b2-agent-backgrounding`, `c1-adv-passive-substitute-phrases`, `c1-passive-avoidance`, `c1-passive-computational-impersonals`, `c1-passive-institutional-impersonals` |

### `non-finite`: infinitives, participles and gerunds (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `building-the-infinitive-the-suffix-ni` | forming the infinitive in -ni | A1 | 47 |  |
| `inflected-infinitives` | inflected infinitives with personal endings | A2 | 99 | `kell-szemelyes-infinitivus` |
| `participle-actions` | adverbial participles in -va/-ve | A2 | 157 | `b2-adverbial-participles`, `c1-adv-circumstantial-participial-clauses`, `c1-hypothetical-counterfactual-participles`, `c1-participle-passive-resultative-state`, `c1-participle-temporal-anteriority` |
| `future-participle-ando` | future passive participles in -andó/-endő | B1 | 124 | `b2-obligatory-participle`, `c1-normative-participles` |
| `past-participle-adjective` | past participles in -t/-ott/-ett/-ött as modifiers | B1 | 50 |  |
| `present-participle` | present participles in -ó/-ő | B1 | 14 |  |
| `participial-clauses` | participial clauses before the noun | B2 | 222 | `b2-participial-clauses`, `c1-dense-participles`, `c1-participle-algorithmic-determinism`, `c1-participle-architectural-epithets` and 13 more |

### `negation`: negation (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `negation-with-nem` | negation with nem | A1 | 140 |  |
| `soha-needs-nem-negative-concord` | double negation with soha nem | A1 | 19 |  |

### `questions`: questions (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `ki-and-mi` | questions with ki and mi | A1 | 164 | `asking-how-the-question-word-mivel` |
| `quantity-choice-questions-mennyi-melyik` | questions with milyen, mennyi and melyik | A1 | 132 | `mennyi-vs-hany`, `milyen-asking-what-someone-is-like` |
| `spatial-questions-hol-hova` | spatial questions with hol, hova and honnan | A1 | 170 | `asking-where-something-is-hol-van`, `hova-movement` |
| `yes-no-questions` | yes/no questions and negation | A1 | 113 |  |
| `rhetorical-questions` | rhetorical questions | C1 | 7 | `c1-rhetorical-hypothetical-questions` |

### `word-order`: word order and focus (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `basic-hungarian-word-order` | focus position before the verb | A1 | 125 | `word-order-focus-and-is` |
| `is-placing-also-too` | word order with is | A1 | 19 |  |
| `prefix-word-order` | separation and placement of verbal prefixes | A2 | 65 | `fog-negation` |
| `b2-cleft-identification` | cleft identificational clauses in philosophical and academic prose | B2 | 95 | `c1-adv-syntactic-focus-clefting` |
| `b2-contrastive-topic` | contrastive topic framing and perspective shifts in Hungarian | B2 | 41 | `c1-polemical-topicalization` |
| `b2-focus-inversion` | focus word order and preverb inversion in Hungarian | B2 | 70 | `c1-adv-contrastive-focus-inversion` |

### `coordination`: joining clauses: and, but, or, not … but (2)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `adversative-contrast` | adversative connectors azonban, viszont and ezzel szemben | A1 | 38 |  |
| `egyreszt-masreszt` | paired connectors egyrészt... másrészt and nem csak... hanem | A1 | 112 | `c1-correlative-balance` |

### `relative-clauses`: relative clauses (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `relative-clauses-aki-ami-amely` | relative clauses with aki, ami and amely | A2 | 120 | `aki-vonatkozoi-mellekmondat`, `ami-clause`, `c1-correlative-rights` |
| `ahol-amikor` | relative adverbs ahol and amikor | B1 | 12 | `c1-complex-locative-correlatives` |
| `vonatkozoi-nevmas-esetei` | case-inflected relative pronouns | B1 | 6 |  |
| `b2-relative-postpositions` | complex relative clauses with postpositions and possessive chains | B2 | 88 |  |

### `complement-clauses`: that-clauses and opinions (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `hogy-clauses` | that-clauses with hogy | A2 | 38 |  |
| `szerintem` | stating opinions with szerintem and azt hiszem, hogy | A2 | 35 |  |
| `b2-cataphoric-clauses` | cataphoric demonstrative anchors with complement clauses in Hungarian | B2 | 88 |  |

### `time-clauses`: time clauses and expressions (5)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `mig-egyidejuseg` | simultaneous events with míg and miközben | A1 | 132 | `b2-simultaneity-conjunctions` |
| `temporal-postpositions` | time postpositions előtt, után and közben | A1 | 30 |  |
| `ota-duration` | duration up to the present with óta and -ja/-je | A2 | 32 |  |
| `miutan-mielott` | time clauses with miután, mielőtt and amint | B1 | 42 | `miutan-mielott-clauses` |
| `b2-temporal-framing` | temporal framing postpositions and anteriority clauses in Hungarian | B2 | 111 | `c1-adv-temporal-succession-chains`, `c1-adv-temporal-successive-aspect`, `c1-complex-adverbials` |

### `cause-purpose-result`: cause, purpose and result (6)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `mert-because` | causal clauses with mert, mivel and ezért | A1 | 88 |  |
| `azert-hogy-purpose` | purpose clauses with azért, hogy + subjunctive | B1 | 68 |  |
| `causal-postpositions` | causal postpositions miatt and következtében | B1 | 156 | `b2-causal-purposive-chains`, `c1-adv-clinical-epidemiological-causality`, `c1-adv-environmental-causal-chains`, `c1-causal-constitutional-precedent-ratio`, `c1-correlative-causal-adverbials` |
| `formal-purpose` | formal purpose: érdekében, céljából | B1 | 62 | `c1-modal-teleological-alliance-commitments`, `c1-modal-teleological-canon-formation`, `c1-modal-teleological-checks-balances`, `c1-modal-teleological-historical-catharsis` and 5 more |
| `nehogy-purpose` | negative purpose and warnings with nehogy + subjunctive | B1 | 108 | `b2-nehogy-subjunctive` |
| `annyira-hogy` | result clauses: annyira ..., hogy; olyan ..., hogy | B2 | 88 | `b2-consecutive-degree` |

### `concession`: concession (4)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `concessive-annak-ellenere` | concessive clauses with bár, habár and annak ellenére, hogy | B1 | 113 | `c1-adv-adversative-concessive-clauses`, `c1-adv-adversative-ecological-concessives`, `c1-adv-concessive-spatial-correlatives`, `c1-adv-economic-concession-markers` and 3 more |
| `concessive-postpositions` | concessive postpositions ellenére and dacára | B1 | 10 |  |
| `concessive-indefinites` | whoever, whatever: bárki, akármi + is | B2 | 108 | `b2-concessive-indefinites`, `c1-subjunctive-concessives` |
| `even-if-ha-is` | even if: ha ... is, még ha | B2 | 88 | `b2-concessive-conditionals` |

### `reported-speech`: reported speech (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `reported-speech-statements` | reported statements with azt mondta, hogy | A2 | 56 |  |
| `indirect-questions` | indirect questions with hogy and -e | B1 | 20 |  |
| `reported-commands` | reported commands and requests with hogy + subjunctive | B1 | 16 |  |

### `discourse-markers`: discourse markers and stance (8)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `evidentials` | hearsay and source: állítólag, szerint, úgy tűnik | A2 | 154 | `b2-evidential-framing`, `c1-assertive-evidential-markers`, `c1-evidentiality-markers`, `c1-modal-epistemic-distancing`, `evidential-allitolag` |
| `additive-connectors` | discourse connectors and argument signposts | B1 | 18 |  |
| `contrastive-discourse-markers` | contrast and counter-argument in discourse | B2 | 212 | `b2-polemical-connectors`, `c1-adv-adversative-modal-shift`, `c1-adv-adversative-rhetorical-refutation`, `c1-adv-contrastive-academic-adversatives` and 12 more |
| `discourse-particles` | discourse particles: hiszen, ugyan, csak, bezzeg | B2 | 131 | `b2-discourse-particles`, `c1-adv-emphatic-scalar-particles`, `c1-adv-evaluative-polarization-particles`, `c1-discourse-limiting-particles`, `c1-ironic-particles` |
| `conclusive-markers` | concluding and summing up: összességében, végső soron | C1 | 172 | `c1-adv-conclusive-canon-pluralism`, `c1-adv-conclusive-cultural-renewal-synthesis`, `c1-adv-conclusive-democratic-horizon`, `c1-adv-conclusive-democratic-safeguards` and 15 more |
| `epistemic-hedging` | hedging and degrees of certainty | C1 | 172 | `c1-adv-epistemic-discursive-truth`, `c1-adv-epistemic-methodological-evaluation`, `c1-adv-epistemic-probability-markers`, `c1-adv-epistemic-tacit-knowledge` and 18 more |
| `evaluative-stance` | evaluative stance adverbials | C1 | 156 | `c1-adv-academic-expulsion-critique`, `c1-adv-constitutional-norm-control`, `c1-adv-grassroots-municipal-autonomy-critique`, `c1-adv-human-dignity-absoluteness` and 15 more |
| `framing-markers` | framing a problem in commentary | C1 | 140 | `c1-discourse-academic-asset-stripping-framing`, `c1-discourse-canon-indoctrination-framing`, `c1-discourse-civil-disobedience-framing`, `c1-discourse-constitutional-crisis-framing` and 14 more |

### `politeness-address`: politeness and forms of address (3)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `formal-address-on` | formal address with ön and polite formulas | A1 | 73 | `tetszik-politeness` |
| `kerek-vs-szeretnek` | polite requests with kérek and szeretnék | A1 | 133 |  |
| `diplomatic-softening` | diplomatic softening and polite dissent | B2 | 126 | `b2-diplomatic-conditionals`, `c1-diplomatic-hedging-conditional`, `c1-negotiation-hedging`, `c1-stylistic-politeness`, `c1-subtle-disclaimer` |

### `register-style`: register, style and rhetoric (7)

| skill | title | level | exercises | merged in (become aliases) |
|---|---|---|---|---|
| `twin-words-colloquial` | twin words and colloquial register | B2 | 88 | `b2-twin-words-register` |
| `essay-oratory-style` | essay and oratory style | C1 | 44 | `c1-essayistic-register`, `c1-essayistic-synthesis`, `c1-persuasive-oratory` |
| `litotes-understatement` | understatement, litotes and irony | C1 | 15 | `c1-antiphrasis-understatement` |
| `metaphor` | metaphor and figurative meaning | C1 | 41 | `c1-cognitive-metaphor`, `c1-conceptual-blending`, `c1-embodied-spatial-metaphor` |
| `official-register` | official and contractual register | C1 | 17 | `c1-bureaucratic-distancing`, `c1-contractual-stipulations` |
| `rhetorical-argument` | antithesis, refutation and reductio | C1 | 45 | `c1-antithesis-structuring`, `c1-reductio-argumentation`, `c1-rhetorical-antithetical-parallelism`, `c1-rhetorical-refutation` |
| `satire-parody` | satire and parody | C1 | 34 | `c1-parodic-inversion`, `c1-satirical-discourse` |

### Dropped: not grammar (41)

Their exercises are retagged when each unit is read: to the unit vocabulary skill, or to a grammar skill where the answer tests a form. Full list with reasons: [grammar-families-mapping.md](grammar-families-mapping.md) § "Not grammar skills".

- **catch-all** (1): `b2-mastery-synthesis`
- **dissolve** (2): `b2-abstract-case-government`, `c1-adv-nominal-appositive-structures`
- **function-or-vocabulary** (7): `contractual-tenancy-clauses`, `financial-transactions-pragmatics`, `light-verb-collocations`, `medical-triage-instructions`, `official-administrative-procedures`, `public-service-interactions`, `weather-verbs-esik-sut`
- **topic** (31): `c1-administrative-remedy`, `c1-biomedical-discourse`, `c1-circular-economy-syntax`, `c1-civic-transparency`, `c1-collective-responsibility`, `c1-constitutional-discourse`, `c1-corporate-governance`, `c1-cultural-semiotics`, `c1-dissent-deliberation`, `c1-ecological-system-dynamics`, `c1-energy-transition-clauses`, `c1-ethical-quandaries` …
