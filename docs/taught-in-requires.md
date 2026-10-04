# Where each skill is taught, and what it builds on: draft (ROADMAP 125)

Status: **draft, 2026-10-04, for review.** For every approved grammar
skill ([grammar-skill-list.md](grammar-skill-list.md)): `taught_in`, the
grammar screen that teaches it, and `requires`, its direct prerequisites
([skill-tagging-spec.md](skill-tagging-spec.md) § "Registry").
Machine-readable: [taught-in-requires.json](taught-in-requires.json).

## Summary

| | Spanish | Hungarian |
|---|---|---|
| skills | 184 | 203 |
| with a `taught_in` screen | 184 | 202 |
| prerequisite links | 214 | 213 |
| skills with no prerequisite (starting points) | 16 | 33 |
| level changed to the screen's level | 16 | 24 |

## How it was made

- **`taught_in`.** For each skill, the lessons whose exercises practise it,
  earliest first; within those, the grammar screen whose title and
  target-language examples best match the skill. Every pairing was then
  read by hand, and 45 were corrected (e.g. `ser-passive` had landed on a
  future-tense review, `negation` on a concession screen).
- **`requires`.** Written by hand: *direct* prerequisites only, at most
  three, each at the same level or lower, with no cycles (all checked).
  The test is "could you explain this skill to someone who doesn't know
  that one?" If not, it's a prerequisite.
- **Level is now the level of the screen that teaches the skill**, not
  the lowest level any exercise tags it. The spec defines level as where a
  skill is *introduced*, and the lowest tag is often a mis-tag.

## What it found

1. **40 skills are practised before they're taught** (16 Spanish, 24
   Hungarian), marked "practised from" below. Example: HU
   `adversative-contrast` (*azonban, viszont*) is on 38 A1 exercises, but
   its first screen is B1. The validator's "skill level ≤ exercise level"
   check will list every such exercise. During the read-through each one
   is either retagged (if it's a mis-tag) or gets an earlier screen (if
   learners really meet the form that early).
2. **12 Spanish skills are practised in both courses but explained in only
   one** (marked "es-es only" / "es-latam only"). Example:
   `relativo-posesivo-cuyo` is explained only in an es-es cultura lesson.
   Each needs a screen in the other course, or the registry allows a
   per-course `taught_in`.
3. **HU `nominalizing-processes`** (*-óban/-őben van*) has no screen at
   all. One needs to be written.
4. **There's no vowel-harmony skill in Hungarian.** HU A1 has a screen
   for it (`a1-05-vh-gr`), but the approved list has no skill, and it's
   the real prerequisite of every suffix. Here, `hungarian-vowels` stands
   in for it. Adding `vowel-harmony` would be a deliberate addition to the
   frozen list, so it needs your sign-off.

## Spanish

### `word-formation`: word formation

| skill | level | taught in | requires |
|---|---|---|---|
| `nominalization` | B2 (practised from B1) | `b2-35-01-a-gr`, *La nominalización en el ensayo y la prosa académica* (es-latam only) | *(none)* |

### `nouns`: noun gender and number

| skill | level | taught in | requires |
|---|---|---|---|
| `gender` | A1 | `a1-03-02-gender-gr`, *Noun gender* | *(none)* |
| `plural` | A1 | `a1-03c-03-plural-gr`, *Describing More Than One Person* | `gender` |

### `articles-demonstratives`: articles and demonstratives

| skill | level | taught in | requires |
|---|---|---|---|
| `articles` | A1 | `a1-03-01-indefinite-gr`, *Indefinite articles* | *(none)* |
| `demonstratives` | A1 | `a1-demonstrative-01-este-gr`, *Demonstratives: This & These* | *(none)* |
| `lo-neutro-abstraccion` | B1 (practised from A1) | `b1-40-03-gr`, *The Neuter Article Lo for Abstract Qualities* | `articles`, `adjective-agreement` |

### `possession`: possession

| skill | level | taught in | requires |
|---|---|---|---|
| `possessives` | A1 | `a1-05-02-possessives-gr`, *Possessive adjectives* | `subject-pronouns` |
| `tener` | A1 | `a1-05-01-tener-gr`, *Tener* | `present-tense` |

### `numbers-quantity`: numbers and quantity

| skill | level | taught in | requires |
|---|---|---|---|
| `numbers` | A1 | `a1-12-01-numbers-gr`, *Numbers* | *(none)* |

### `pronouns`: pronouns

| skill | level | taught in | requires |
|---|---|---|---|
| `subject-pronouns` | A1 | `a1-02-02-pronouns-ser-gr`, *Ser: third person* | *(none)* |
| `indefinidos-negativos` | A2 | `a2-indefinidosnegacion-01-gr`, *Indefinite Pronouns: Alguien and Nadie* | `negation` |
| `objeto-directo` | A2 | `a2-12-01-gr`, *Direct Object Pronouns with the Pretérito Indefinido* | `present-tense` |
| `objeto-indirecto` | A2 | `a2-pronombrescliticos-01-gr`, *Indirect Object Pronouns (me, te, le, nos, les)* | `objeto-directo` |
| `pronombres-combinados` | A2 (practised from A1) | `a2-pronombrescliticos-03-gr`, *Double Object Pronouns: Order (IO + DO)* | `objeto-directo`, `objeto-indirecto` |

### `adjectives`: adjectives

| skill | level | taught in | requires |
|---|---|---|---|
| `adjective-agreement` | A1 | `a1-03-04-adjectives-gr`, *Adjective agreement* | `gender`, `plural` |

### `adverbs`: adverbs

| skill | level | taught in | requires |
|---|---|---|---|
| `intensificadores-y-grado` | A1 | `a1-doler-03-intensidad-gr`, *Degrees of Pain & Health States* | `adjective-agreement` |
| `frequency-adverbs` | B1 | `b1-12-01-habits-and-frequency-gr`, *Habits and frequency* | `present-tense` |

### `comparison`: comparison and manner

| skill | level | taught in | requires |
|---|---|---|---|
| `comparatives` | A2 | `a2-06-01-gr`, *Comparative Structures* | `adjective-agreement` |
| `cuanto-mas-tanto-mas` | B1 | `b1-eeuu-03-cuanto-mas-gr`, *Cuanto más... (tanto) más: relaciones que crecen juntas* | `comparatives` |
| `superlatives` | B1 | `b1-gastronomia-01-superlativo-relativo-proporcion-gr`, *El superlativo relativo y las construcciones de proporción (* (es-es only) | `comparatives` |
| `como-si` | B2 | `b2-32-05-a-gr`, *Subordinadas modales hipotéticas con subjuntivo* | `imperfect-subjunctive-forms` |
| `manner-clauses` | B2 | `b2-32-04-a-gr`, *Subordinadas modales correlativas avanzadas* | `relative-clauses` |

### `prepositions-postpositions`: prepositions and postpositions

| skill | level | taught in | requires |
|---|---|---|---|
| `a-personal` | A1 | `a1-abilities-04-a-personal-gr`, *The Personal 'a' with People* | `present-tense` |
| `preposiciones-movimiento` | A1 | `a1-directions-02-movement-prepositions-gr`, *Prepositions of movement* | `ir` |
| `por-vs-para` | A2 | `a2-porpara-01-gr`, *The Preposition Para: Purpose and Recipient* | *(none)* |
| `prepositional-phrases` | B1 | `b1-cortes-05-mediante-y-a-traves-de-gr`, *Instrumentos normativos: uso de «mediante» en lenguaje legal* (es-es only) | `por-vs-para` |

### `verb-forms`: verb conjugation and the present

| skill | level | taught in | requires |
|---|---|---|---|
| `ar-verbs` | A1 | `a1-06-02-ar-verbs-gr`, *Regular -AR verbs* | `present-tense` |
| `er-ir-verbs` | A1 | `a1-06-03-er-ir-verbs-gr`, *Regular -ER and -IR verbs* | `ar-verbs` |
| `ir` | A1 | `a1-directions-01-movement-location-gr`, *Movement and location* | `present-tense` |
| `present-tense` | A1 | `a1-06-01-present-introduction-gr`, *The regular present tense* | `subject-pronouns` |
| `stem-changes` | A1 | `a1-reflexive-02-cambio-radical-gr`, *Stem-Changing Reflexive Verbs* | `er-ir-verbs` |
| `vosotros-indicativo` | A2 | `a2-vosotrospeninsular-01-gr`, *Present Indicative of Vosotros: You All in Spain* | `present-tense` |
| `voseo-rioplatense-reconocimiento` | B2 | `b2-argentinaba-02-a-gr`, *Reconocimiento y comprensión del voseo rioplatense* | `present-tense` |

### `being-becoming`: being, becoming and existence

| skill | level | taught in | requires |
|---|---|---|---|
| `estar` | A1 | `a1-07-03-estar-location-gr`, *Estar for location* | `ser` |
| `hay` | A1 | `a1-07-04-hay-estar-gr`, *Hay vs estar* | `estar` |
| `ser` | A1 | `a1-01-04-origin-gr`, *Ser for origin* | `subject-pronouns` |
| `resultar-adjective` | B1 | `b1-15-02-evaluation-gr`, *Evaluation* | `ser`, `gustar` |
| `verbs-of-change` | B1 (practised from A1) | `b1-39-01-gr`, *Ponerse + Adjective for Involuntary Emotional and Physical C* | `reflexives`, `estar` |

### `verb-patterns`: verb patterns and government

| skill | level | taught in | requires |
|---|---|---|---|
| `doler` | A1 | `a1-doler-01-duele-gr`, *The Verb Doler: Singular vs. Plural* | `gustar` |
| `gustar` | A1 | `a1-gustar-01-me-gusta-gr`, *The verb gustar: Basics* | `present-tense` |
| `saber-vs-conocer` | A1 | `a1-abilities-03-saber-conocer-gr`, *Saber vs. Conocer* | `present-tense` |
| `verbos-regimen-preposicional` | B1 | `b1-40-01-gr`, *Verbs Requiring Inherent Prepositions* | `present-tense` |

### `past`: past tenses

| skill | level | taught in | requires |
|---|---|---|---|
| `alguna-vez` | A2 | `a2-09-05-gr`, *Talking About Experiences* | `preterito-perfecto` |
| `imperfect` | A2 | `a2-imperfectobasico-01-gr`, *Imperfecto: -AR Verb Endings* | `present-tense` |
| `past-participles` | A2 | `a2-01-01-participles-gr`, *Talking About What You've Done* | `ar-verbs`, `er-ir-verbs` |
| `preterite-irregular-stems` | A2 | `a2-11-02-gr`, *Common Irregular Pretérito Indefinido* | `preterito-indefinido` |
| `preterite-vs-imperfect` | A2 | `a2-imperfectocontraste-01-gr`, *Imperfecto vs Indefinido — The Core Contrast* | `preterito-indefinido`, `imperfect` |
| `preterito-indefinido` | A2 | `a2-11-01-gr`, *Regular Pretérito Indefinido* | `present-tense` |
| `preterito-perfecto` | A2 | `a2-01-01-participles-gr`, *Talking About What You've Done* | `past-participles` |
| `preterito-perfecto-vs-indefinido` | A2 | `a2-17-03-gr`, *Pretérito Perfecto or Indefinido?* | `preterito-perfecto`, `preterito-indefinido` |
| `secuencia-narrativa` | A2 | `a2-11-04-gr`, *Sequencing Completed Events* | `preterito-indefinido` |
| `ya-todavia-no` | A2 | `a2-02-03-gr`, *Questions with Ya and Todavía No* | `preterito-perfecto` |
| `imperfect-vs-present-perfect` | B1 | `b1-11-02-change-over-time-gr`, *Change over time* | `imperfect`, `preterito-perfecto` |
| `pluscuamperfecto` | B1 | `b1-01-03-pluscuamperfecto-gr`, *Before That* | `imperfect`, `past-participles` |
| `participios-irregulares-dobles` | B2 | `b2-20-04-a-gr`, *Participios irregulares y formas dobles en español* | `past-participles`, `ser-passive` |
| `verbos-cambio-significado-pasado` | B2 | `b2-02-03-a-gr`, *Verbos con cambio de significado según el aspecto* | `preterite-vs-imperfect` |

### `future`: the future

| skill | level | taught in | requires |
|---|---|---|---|
| `ir-infinitive` | A1 | `a1-future-01-ir-a-infinitive-gr`, *Ir a + infinitive* | `ir` |
| `futuro-simple` | A2 | `a2-19-01-gr`, *Regular Futuro Simple Endings* | `ir-infinitive` |
| `future-probability` | B1 | `b1-22-01-future-for-probability-gr`, *Future for probability* | `futuro-simple`, `condicional-regular` |
| `futuro-perfecto` | B1 | `b1-nacionalismo-03-futuro-perfecto-gr`, *Futuro perfecto: conjeturas sobre lo ya ocurrido* | `futuro-simple`, `past-participles` |

### `conditional`: conditions, hypotheses and wishes

| skill | level | taught in | requires |
|---|---|---|---|
| `condicional-consejos` | A2 | `a2-condicionalsimple-04-gr`, *Giving Advice with the Conditional* | `condicional-regular` |
| `condicional-irregular` | A2 | `a2-condicionalsimple-02-gr`, *Conditional Simple: Irregular Stems* | `condicional-regular` |
| `condicional-regular` | A2 | `a2-condicionalsimple-01-gr`, *Conditional Simple: Regular Endings* | `futuro-simple` |
| `conditional-conjunctions` | B1 | `b1-cortes-03-en-caso-de-que-subjuntivo-gr`, *Condicionales jurídicas: «en caso de que + subjuntivo»* (es-es only) | `subjuntivo-morfologia` |
| `hypothetical-structures` | B1 | `b1-14-04-hypothetical-structures-gr`, *Hypothetical structures* | `si-clauses`, `condicional-regular` |
| `si-clauses` | B1 | `b1-08-04-conditional-structures-gr`, *Conditional structures* | `futuro-simple` |
| `apodosis-condicional-literaria` | B2 | `b2-10-02-a-gr`, *El pluscuamperfecto de subjuntivo en la apódosis* | `pluscuamperfecto-subjuntivo-si` |
| `counterfactual-wishes` | B2 | `b2-33-05-a-gr`, *Estructuras optativas contrafácticas con ojalá y quién pudie* | `subjuntivo-deseos`, `pluperfect-subjunctive-forms` |
| `implicit-conditionals` | B2 | `b2-16-03-a-gr`, *Estructuras condicionales contrafácticas con 'de haber + par* | `pluscuamperfecto-subjuntivo-si` |
| `inversiones-condicionales-de-haber` | B2 | `b2-10-05-a-gr`, *Construcciones concesivo-condicionales e inversión retórica* | `pluscuamperfecto-subjuntivo-si` |
| `mixed-conditionals` | B2 | `b2-11-01-a-gr`, *Condicionales mixtas: condición en pasado y repercusión en p* | `pluscuamperfecto-subjuntivo-si` |
| `pluscuamperfecto-subjuntivo-si` | B2 (practised from B1) | `b2-nicaragua-03-a-gr`, *Períodos hipotéticos contrafácticos en el pasado con pluscua* (es-latam only) | `hypothetical-structures`, `pluscuamperfecto` |
| `regrets-reproaches` | B2 | `b2-10-03-a-gr`, *Fórmulas de lamento, queja y reproche en el pasado* | `pluscuamperfecto-subjuntivo-si` |

### `subjunctive`: the subjunctive

| skill | level | taught in | requires |
|---|---|---|---|
| `subjunctive-emotion` | A2 | `a2-subjuntivobasico-05-gr`, *Verbs of Emotion with the Subjunctive* | `subjuntivo-morfologia` |
| `subjunctive-value-judgments` | A2 | `a2-subjuntivobasico-03-gr`, *Impersonal Expressions with Subjunctive* | `subjuntivo-morfologia` |
| `subjuntivo-deseos` | A2 | `a2-subjuntivobasico-02-gr`, *The Two-Subject Rule with Wishes* | `subjuntivo-morfologia` |
| `subjuntivo-morfologia` | A2 | `a2-subjuntivobasico-01-gr`, *Present Subjunctive: Concept & Morphology* | `present-tense` |
| `conectores-con-subjuntivo` | B1 | `b1-36-03-cause-consequence-solutions-gr`, *Cause, consequence and solutions* | `subjuntivo-morfologia` |
| `correlacion-temporal-subjuntivo` | B1 | `b1-38-01-gr`, *Tense Sequence with Subjunctive in the Past* | `subjunctive-influence`, `preterito-indefinido` |
| `subjunctive-doubt` | B1 | `b1-34-02-subjunctive-doubt-possibility-gr`, *Subjunctive with doubt and possibility* | `subjuntivo-morfologia` |
| `subjunctive-influence` | B1 (practised from A2) | `b1-04-03-subjuntivo-recomendaciones-gr`, *I Recommend That...* | `subjuntivo-morfologia` |
| `subjuntivo-perfecto` | B1 | `b1-37-01-gr`, *Formation of the Present Perfect Subjunctive* | `subjuntivo-morfologia`, `preterito-perfecto` |
| `imperfect-subjunctive-forms` | B2 | `b2-15-01-a-gr`, *Las dos desinencias del imperfecto de subjuntivo: -ra y -se* | `preterito-indefinido`, `subjuntivo-morfologia` |
| `pluperfect-subjunctive-forms` | B2 | `b2-16-01-a-gr`, *El pretérito pluscuamperfecto de subjuntivo: estructura y al* | `imperfect-subjunctive-forms`, `past-participles` |
| `subjuntivo-imperfecto-estilistico-ra` | B2 | `b2-15-05-a-gr`, *El uso estilístico de -ra con valor de indicativo en la pros* | `imperfect-subjunctive-forms`, `pluscuamperfecto` |

### `imperative`: the imperative

| skill | level | taught in | requires |
|---|---|---|---|
| `imperativo-afirmativo` | A1 | `a1-kitchen-04-imperatives-gr`, *Basic affirmative imperatives* | `present-tense` |
| `imperativo-afirmativo-irregular` | A2 | `a2-imperativoafirmativo-02-gr`, *The 8 Irregular Affirmative Commands (tú)* | `imperativo-afirmativo` |
| `imperativo-formal-usted` | A2 | `a2-imperativoafirmativo-03-gr`, *Formal Commands (usted / ustedes)* | `imperativo-afirmativo`, `subjuntivo-morfologia` |
| `imperativo-negativo` | A2 | `a2-imperativonegativo-01-gr`, *Negative Commands (tú) — Regular Verbs* | `imperativo-afirmativo`, `subjuntivo-morfologia` |
| `imperativo-negativo-irregular` | A2 | `a2-imperativonegativo-02-gr`, *Irregular Negative Commands (tú)* | `imperativo-negativo` |
| `posicion-pronombres-imperativo` | A2 | `a2-imperativonegativo-04-gr`, *Pronoun Placement with Commands* | `imperativo-negativo`, `objeto-directo` |
| `vosotros-imperativo` | A2 | `a2-vosotrospeninsular-02-gr`, *Affirmative Imperative of Vosotros: Group Commands in Spain* | `imperativo-afirmativo`, `vosotros-indicativo` |

### `aspect`: aspect, periphrases and verbal prefixes

| skill | level | taught in | requires |
|---|---|---|---|
| `progressive` | A1 | `a1-continuous-01-ando-gr`, *Present Continuous: -AR Verbs* | `estar` |
| `acabar-de` | A2 | `a2-perifrasisduracion-01-gr`, *Recent Actions: Acabar de + Infinitivo* | `present-tense` |
| `llevar-tiempo-gerundio` | A2 | `a2-perifrasisduracion-02-gr`, *Duration of Actions: Llevar + Tiempo + Gerundio* | `progressive` |
| `perifrasis-verbales` | A2 | `a2-perifrasisverbales-05-gr`, *Narrating Transitions with Periphrases* | `acabar-de` |
| `seguir-gerundio` | A2 | `a2-perifrasisverbales-02-gr`, *Continuity Periphrases: Seguir and Llevar* | `progressive` |
| `dejar-de-infinitivo` | B1 | `b1-industrializacion-03-no-dejar-de-gr`, *No dejar de + infinitivo: un proceso que no se detiene* | `perifrasis-verbales` |
| `estar-a-punto-de` | B1 | `b1-revolucioncubana-04-a-punto-de-gr`, *A punto de + infinitivo: al borde de que algo ocurra* | `estar` |
| `gerundio-acciones-paralelas` | B1 | `b1-precolombina-04-daily-life-gerund-gr`, *Gerundio para acción paralela* | `progressive` |
| `habitos-soler` | B1 | `b1-09-03-habitos-soler-gr`, *Habitual structures and soler* | `present-tense` |
| `gerund-periphrases` | B2 | `b2-mexiconorte-01-a-gr`, *La perífrasis aspectual ir + gerundio* | `progressive`, `seguir-gerundio` |
| `inceptive-periphrases` | B2 | `b2-23-01-a-gr`, *Perífrasis inceptivas: Echarse a + infinitivo* | `perifrasis-verbales` |
| `perifrasis-dar-por-participio` | B2 | `b2-25-05-a-gr`, *Juicios resultativos: Dar por + participio / adjetivo* | `past-participles` |
| `perifrasis-llegar-a-infinitivo` | B2 | `b2-25-04-a-gr`, *Alcance de hitos: Llegar a + infinitivo* | `perifrasis-verbales` |
| `perifrasis-pasar-a` | B2 | `b2-23-05-a-gr`, *Perífrasis secuenciales: Pasar a + infinitivo* | `perifrasis-verbales` |
| `terminar-por-infinitivo` | B2 (practised from B1) | `b2-25-03-a-gr`, *Desenlace gradual: Terminar por + infinitivo y Terminar + ge* | `perifrasis-verbales` |
| `volver-a-infinitivo` | B2 (practised from A2) | `b2-23-04-a-gr`, *Perífrasis iterativas: Volver a + infinitivo* (es-latam only) | `present-tense` |

### `modality`: obligation, ability, permission and probability

| skill | level | taught in | requires |
|---|---|---|---|
| `hay-que` | A1 | `a1-work-03-hay-que-gr`, *Hay que* | `hay` |
| `querer-poder` | A1 | `a1-abilities-01-poder-gr`, *Poder + Infinitivo* | `stem-changes` |
| `saber-infinitivo` | A1 | `a1-abilities-02-saber-gr`, *Saber + Infinitivo for Skills* | `present-tense` |
| `tener-que` | A1 | `a1-work-02-tener-que-gr`, *Tener que* | `tener` |
| `deber-vs-tener-que` | B1 | `b1-04-01-deber-tener-que-imperatives-gr`, *You Should...* | `tener-que` |
| `perifrasis-deber-obligacion-conjetura` | B2 | `b2-26-01-a-gr`, *Perífrasis modales: Deber vs. Deber de + infinitivo* | `deber-vs-tener-que` |
| `perifrasis-haber-de-infinitivo` | B2 | `b2-26-02-a-gr`, *Modalidad culta: Haber de + infinitivo* | `perifrasis-deber-obligacion-conjetura` |
| `perifrasis-modales-probabilidad-epistemica` | B2 | `b2-amazoniapan-04-a-gr`, *Perífrasis de probabilidad y conjetura retrospectiva* | `perifrasis-deber-obligacion-conjetura`, `future-probability` |

### `voice`: passive, impersonal, reflexive and causative

| skill | level | taught in | requires |
|---|---|---|---|
| `contraste-reflexivo` | A1 | `a1-reflexive-04-contraste-gr`, *Reflexive vs. Non-Reflexive Actions* | `reflexives` |
| `reflexives` | A1 | `a1-06-04-reflexive-verbs-gr`, *Reflexive Verbs* | `present-tense` |
| `pasiva-refleja` | B1 (practised from A2) | `b1-constitucion-01-se-pasiva-constitucional-gr`, *Pasiva refleja con «se» en textos constitucionales* (es-es only) | `reflexives` |
| `se-impersonal` | B1 | `b1-07-02-impersonal-constructions-gr`, *Impersonal constructions* | `pasiva-refleja` |
| `ser-passive` | B1 (practised from A2) | `b1-civilizaciones-01-mayas-passive-gr`, *Voz pasiva y se pasiva en textos históricos* (es-latam only) | `ser`, `past-participles` |
| `choosing-passive-type` | B2 | `b2-20-05-a-gr`, *Selección estilística entre pasivas en la prosa formal* | `ser-passive`, `pasiva-estado-estar-participio`, `pasiva-refleja` |
| `desambiguacion-valores-se` | B2 | `b2-19-05-a-gr`, *Desambiguación pragmática de las funciones de se* | `se-pasivo-vs-impersonal`, `contraste-reflexivo` |
| `impersonal-tercera-plural-uno` | B2 | `b2-21-01-a-gr`, *La tercera persona del plural impersonal y el pronombre inde* | `se-impersonal` |
| `nominalizacion-despersonalizacion` | B2 | `b2-21-03-a-gr`, *La nominalización como recurso de despersonalización y conci* | `nominalization`, `se-impersonal` |
| `pasiva-estado-estar-participio` | B2 | `b2-20-03-a-gr`, *La pasiva de estado con estar y participio* | `ser-passive`, `estar` |
| `se-pasivo-vs-impersonal` | B2 | `b2-19-02-a-gr`, *Diferenciación: pasiva refleja vs se impersonal* | `se-impersonal`, `pasiva-refleja` |

### `non-finite`: infinitives, participles and gerunds

| skill | level | taught in | requires |
|---|---|---|---|
| `gerundios-irregulares` | A1 | `a1-continuous-03-irregulares-gr`, *Irregular & Stem-Changing Gerunds* | `progressive` |
| `participios-absolutos-narrativos` | B2 | `b2-argentinaba-03-a-gr`, *Construcciones de participio absoluto en el relato literario* | `past-participles` |

### `negation`: negation

| skill | level | taught in | requires |
|---|---|---|---|
| `negation` | A2 (practised from A1) | `a2-indefinidosnegacion-05-gr`, *Integrated Negative System in Spanish* | *(none)* |

### `questions`: questions

| skill | level | taught in | requires |
|---|---|---|---|
| `questions` | A1 | `a1-01-03-questions-gr`, *Asking someone's name* | *(none)* |

### `word-order`: word order and focus

| skill | level | taught in | requires |
|---|---|---|---|
| `inversion-enfasis-fronting` | B2 | `b2-01-03-a-gr`, *La anteposición enfática y la inversión verbo-sujeto* | *(none)* |
| `oraciones-hendidas-enfasis` | B2 | `b2-01-01-a-gr`, *Las oraciones hendidas: lo que... es* | `relative-clauses`, `lo-neutro-abstraccion` |

### `coordination`: joining clauses: and, but, or, not … but

| skill | level | taught in | requires |
|---|---|---|---|
| `connectors` | A1 | `a1-10-04-integracion-gr`, *Putting It Together* | *(none)* |
| `correlativos-no-solo-sino` | B1 | `b1-cambiosocial-05-no-solo-sino-tambien-gr`, *Correlativos formales: no solo... sino también* | `sino-vs-pero` |
| `sino-vs-pero` | B1 | `b1-40-02-gr`, *Contrasts: Pero, Sino, and Sino que* | `connectors`, `negation` |

### `relative-clauses`: relative clauses

| skill | level | taught in | requires |
|---|---|---|---|
| `relativas-preposicion-el-que` | B1 | `b1-20-01-describing-problems-gr`, *Describing problems* | `relative-clauses` |
| `relative-clauses` | B1 | `b1-10-01-relative-clauses-gr`, *Relative clauses* | *(none)* |
| `relativo-posesivo-cuyo` | B1 | `b1-gobierno-04-cuya-funcion-es-gr`, *Relativos posesivos en definiciones institucionales: «cuyo /* (es-es only) | `relative-clauses` |
| `relativas-subjuntivo` | B2 (practised from B1) | `b2-13-03-a-gr`, *Contraste de modo en relativas: Indicativo (específico) vs S* (es-latam only) | `relative-clauses`, `subjuntivo-morfologia` |
| `relativas-universales-quiera` | B2 | `b2-14-04-a-gr`, *Cuantificadores relativos universales: cuanto, todo aquel qu* | `relativas-subjuntivo` |

### `complement-clauses`: that-clauses and opinions

| skill | level | taught in | requires |
|---|---|---|---|
| `giving-opinions` | B1 | `b1-15-01-preferences-and-opinions-gr`, *Preferences and opinions* | *(none)* |
| `opinion-verbs-mood` | B1 | `b1-07-03-opinion-indicative-subjunctive-gr`, *Opinion + indicative/subjunctive* | `giving-opinions`, `subjuntivo-morfologia` |
| `el-hecho-de-que-subjuntivo` | B2 | `b2-06-04-a-gr`, *Subjuntivo e indicativo con 'el hecho de que'* | `opinion-verbs-mood` |
| `infinitive-vs-que-subjunctive` | B2 (practised from A2) | `b2-04-04-a-gr`, *Infinitivo frente a subjuntivo: Correferencia del sujeto* (es-latam only) | `subjunctive-influence` |

### `time-clauses`: time clauses and expressions

| skill | level | taught in | requires |
|---|---|---|---|
| `antes-despues-infinitive` | A2 | `a2-04-02-gr`, *Después de + Infinitive* | *(none)* |
| `cuando-mientras` | A2 | `a2-13-02-gr`, *Mientras with Simultaneous Past Actions* | `imperfect`, `preterito-indefinido` |
| `desde-desde-hace` | A2 | `a2-07-04-gr`, *Duration with Friendship and Languages* | `present-tense` |
| `cuando-subjuntivo` | B1 (practised from A2) | `b1-gobierno-05-hasta-que-subjuntivo-gr`, *Límite temporal futuro: «hasta que + presente de subjuntivo»* (es-es only) | `cuando-mientras`, `subjuntivo-morfologia` |
| `antes-despues-de-que` | B2 | `b2-guatemala-02-a-gr`, *Subordinadas temporales con antes de que y después de que* | `antes-despues-infinitive`, `cuando-subjuntivo` |

### `cause-purpose-result`: cause, purpose and result

| skill | level | taught in | requires |
|---|---|---|---|
| `por-que-y-porque` | A1 | `a1-02-03-porque-gr`, *Por qué and porque* | `questions` |
| `porque-y-por-eso` | A2 | `a2-15-03-gr`, *Cause and Consequence* | `por-que-y-porque` |
| `formal-cause-connectors` | B1 | `b1-independencia-04-republicas-gr`, *Conectores formales: a raíz de, en el marco de* | `porque-y-por-eso` |
| `subjuntivo-de-finalidad-para-que` | B1 | `b1-32-04-purpose-gr`, *Purpose* | `por-vs-para`, `subjuntivo-morfologia` |
| `consecutivas-de-tal-manera` | B2 | `b2-nicaragua-01-a-gr`, *Oraciones consecutivas de intensidad y modo: de tal manera q* | `porque-y-por-eso` |
| `consequence-markers` | B2 | `b2-31-02-a-gr`, *Marcadores consecutivos coloquiales e ilativos* | `porque-y-por-eso` |
| `purpose-connectors` | B2 (practised from B1) | `b2-27-03-a-gr`, *Locuciones prepositivas de finalidad y sacrificio: en aras d* | `subjuntivo-de-finalidad-para-que` |

### `concession`: concession

| skill | level | taught in | requires |
|---|---|---|---|
| `concesivas-aunque` | A2 | `a2-perifrasisverbales-04-gr`, *Causal & Concessive Connectors* | `connectors` |
| `a-pesar-de` | B1 | `b1-industrializacion-05-pese-a-que-gr`, *Pese a que + subjuntivo: un logro con límites* | `concesivas-aunque` |
| `contrast-concession-connectors` | B1 | `b1-21-02-contrast-and-concession-gr`, *Contrast and concession* | `connectors` |
| `concesivas-aun-cuando` | B2 | `b2-nicaragua-04-a-gr`, *Concesivas de registro formal: aun cuando, si bien y a sabie* | `concesivas-aunque` |
| `concesivas-por-mas-que` | B2 | `b2-mexicosur-02-a-gr`, *Oraciones concesivas intensivas con por más que* | `concesivas-aunque` |
| `concesivas-si-bien` | B2 | `b2-guatemala-03-a-gr`, *Concesivas formales en el discurso histórico: si bien, a pes* | `concesivas-aunque` |
| `reduplicated-subjunctive` | B2 | `b2-08-05-a-gr`, *Estructuras concesivas reduplicativas con subjuntivo* | `concesivas-aunque`, `subjuntivo-morfologia` |

### `reported-speech`: reported speech

| skill | level | taught in | requires |
|---|---|---|---|
| `estilo-indirecto` | B1 | `b1-13-02-reported-speech-foundations-gr`, *Reported speech foundations* | `preterito-indefinido`, `imperfect` |
| `estilo-indirecto-informacion` | B1 | `b1-13-01-reporting-information-gr`, *Reporting information* | `estilo-indirecto` |
| `estilo-indirecto-ordenes` | B1 | `b1-38-02-gr`, *Reporting Commands and Requests in the Past* | `estilo-indirecto`, `subjunctive-influence` |
| `discurso-indirecto-deicticos` | B2 | `b2-17-04-a-gr`, *Traslación de deícticos temporales, espaciales y demostrativ* | `estilo-indirecto` |
| `discurso-indirecto-interrogativas` | B2 | `b2-17-02-a-gr`, *Preguntas indirectas y traslación interrogativa en pasado* | `estilo-indirecto` |
| `discurso-indirecto-libre` | B2 | `b2-17-05-a-gr`, *El discurso indirecto libre en la prosa narrativa hispanoame* | `estilo-indirecto` |
| `reporting-verbs` | B2 | `b2-salvadorhonduras-02-a-gr`, *Verbos de atribución y reporte en la denuncia social y ambie* | `estilo-indirecto` |

### `discourse-markers`: discourse markers and stance

| skill | level | taught in | requires |
|---|---|---|---|
| `ordering-markers` | A2 | `a2-perifrasisverbales-03-gr`, *Discourse Connectors: Contrast & Addition* | `connectors` |
| `argument-markers` | B1 | `b1-15-05-connected-opinion-writing-gr`, *Connected opinion writing* | `ordering-markers` |
| `contrast-markers` | B2 | `b2-brasilsudeste-01-a-gr`, *Contrastive Discourse Markers in Urban Analysis* | `contrast-concession-connectors` |
| `hedging` | B2 | `b2-21-05-a-gr`, *Distanciamiento epistémico y fórmulas de atenuación asertiva* | `subjunctive-doubt` |
| `marcadores-digresion` | B2 | `b2-28-02-a-gr`, *Discourse Markers of Digression & Incidental Remarks* | `ordering-markers` |
| `reformulation-markers` | B2 | `b2-29-01-a-gr`, *Explanatory Reformulation Discourse Markers* | `ordering-markers` |
| `refutacion-no-es-que-sino` | B2 | `b2-05-03-a-gr`, *Estructuras de refutación discursiva con 'no es que' + subju* | `sino-vs-pero`, `subjunctive-doubt` |
| `stance-adverbs` | B2 | `b2-brasilsudeste-04-a-gr`, *Focusing Adverbs & Scalar Markers in Cultural Writing* | `intensificadores-y-grado` |

### `politeness-address`: politeness and forms of address

| skill | level | taught in | requires |
|---|---|---|---|
| `polite-softening` | A2 (practised from A1) | `a2-condicionalsimple-03-gr`, *The Conditional of Politeness (Cortesía)* | *(none)* |
| `sociolinguistica-tratamiento-cortesia` | B2 | `b2-34-01-a-gr`, *Formas de tratamiento, voseo y cortesía en el español americ* | `polite-softening` |

### `register-style`: register, style and rhetoric

| skill | level | taught in | requires |
|---|---|---|---|
| `essay-style` | B2 | `b2-35-05-a-gr`, *Densidad léxica, períodos sintácticos complejos y síntesis a* | `argument-markers` |
| `formal-register` | B2 | `b2-14-05-a-gr`, *Generalizaciones categóricas en el discurso jurídico y ético* | `nominalization` |
| `rhetorical-devices` | B2 | `b2-36-04-a-gr`, *Metáforas conceptuales y recursos retóricos en el discurso p* | *(none)* |

## Hungarian

### `sounds-spelling`: sounds, spelling and stress

| skill | level | taught in | requires |
|---|---|---|---|
| `hungarian-consonant-sounds` | A1 | `a1-01-b-gr`, *Hungarian Consonant Sounds* | *(none)* |
| `hungarian-vowels` | A1 | `a1-01-a-gr`, *Hungarian Vowels* | *(none)* |

### `word-formation`: word formation

| skill | level | taught in | requires |
|---|---|---|---|
| `having-s` | A2 | `a2-16-b-gr`, *-s: "Having X"* | `adjective-order-before-the-noun` |
| `nominalization` | B1 (practised from A2) | `b1-16-04-b-gr`, *Nominalization with -ás/-és: újrahasznosítás, energiatakarék* | `present-tense-routine-language` |
| `noun-compounds` | B1 | `b1-16-02-b-gr`, *Environmental Compound Nouns in Hungarian* | `3rd-person-possessive` |
| `spatial-belonging-beli` | B1 | `b1-11-02-gr`, *Expressing Origin & Spatial Belonging: The -beli Suffix* | `having-s`, `ban-ben-in` |
| `verbal-adjectives-hatatlan-hetetlen` | B1 | `b1-30-02-b-gr`, *Privative Potential Participles: -hatatlan / -hetetlen* | `potential-hat-het`, `present-participle` |
| `sag-seg-nouns` | C1 | `c1-06-02-a-gr`, *Deadjectival and Nominal Abstract Compounds in Philosophical* | `nominalization` |

### `nouns`: noun gender and number

| skill | level | taught in | requires |
|---|---|---|---|
| `plural-nouns-k` | A1 | `a1-22-b-gr`, *Plural Nouns: -k* | `hungarian-vowels` |

### `articles-demonstratives`: articles and demonstratives

| skill | level | taught in | requires |
|---|---|---|---|
| `definite-article-a-az` | A1 | `a1-23-b-gr`, *The Definite Article: a / az* | *(none)* |
| `demonstratives-ez-az` | A1 | `a1-03-b-gr`, *Ez, az, egy* | *(none)* |
| `indefinite-article-egy` | A1 | `a1-22-a-gr`, *Naming Objects with egy* | *(none)* |

### `possession`: possession

| skill | level | taught in | requires |
|---|---|---|---|
| `kinship-possessives` | A1 | `a1-26-b-gr`, *Possessive: -m / -om / -em / -öm — My Family* | `possessive-suffixes` |
| `possessive-pronouns-enyem` | A1 | `a1-43-a-gr`, *Possessive suffixes* | `possessive-suffixes` |
| `possessive-suffixes` | A1 | `a1-26-b-gr`, *Possessive: -m / -om / -em / -öm — My Family* | `hungarian-vowels` |
| `van-possessive-to-have` | A1 | `a1-27-b-gr`, *Van + Possessive = 'To Have'* | `possessive-suffixes`, `van-and-nincs-there-is-there-isn-t` |
| `3rd-person-possessive` | A2 | `a2-12-a-gr`, *His/Her: the 3rd-Person Possessive Suffix* | `possessive-suffixes` |
| `acc-poss` | A2 | `a2-104-b-gr`, *Bemutatom a munkatársamat: Accusative + Possessive Together* | `how-the-accusative-t-works`, `3rd-person-possessive` |
| `plural-possessive` | A2 | `a2-191-b-gr`, *Stem Changes with Plural Possessed Nouns* | `3rd-person-possessive` |
| `sajat` | A2 | `a2-25-b-gr`, *saját élet: A Life of Her Own* | `possessive-suffixes` |

### `numbers-quantity`: numbers and quantity

| skill | level | taught in | requires |
|---|---|---|---|
| `cardinal-numbers` | A1 | `a1-16b-gr`, *Numbers 11–100* | *(none)* |
| `containers-and-measures` | A1 | `a1-93-b-gr`, *Containers and Measures* | `singular-after-numbers` |
| `fractions` | A1 | `a1-76-b-gr`, *Fél and negyed — halves and quarters* | `cardinal-numbers` |
| `singular-after-numbers` | A1 | `a1-30-a-gr`, *sok / egy + Singular Noun* | `cardinal-numbers` |
| `ordinal-numbers` | A2 | `a2-07-a-gr`, *Ordinal Numbers: First, Second, Third...* | `cardinal-numbers` |
| `sokat-eleget` | A2 | `a2-86-a-gr`, *Sokat, Eleget – How Much You Do Something* | `how-the-accusative-t-works` |
| `szor-szer-multiplicatives` | A2 | `a2-04-a-gr`, *How Many Times: -szor/-szer/-ször* | `cardinal-numbers` |
| `b2-proportional-rates` | B2 | `b2-21-01-a-gr`, *Multiplicative Suffixes and Proportional Expressions* | `szor-szer-multiplicatives` |

### `pronouns`: pronouns

| skill | level | taught in | requires |
|---|---|---|---|
| `good-for-me-nekem-jo` | A1 | `a1-148-a-gr`, *Good For Me: nekem + jó* | `personal-pronouns` |
| `personal-pronouns` | A1 | `a1-02-a-gr`, *Én, te, ő* | *(none)* |
| `subject-pronouns-omission` | A1 | `a1-61-b-gr`, *Subject omission* | `personal-pronouns`, `present-tense-routine-language` |
| `case-inflected-pronouns` | A2 | `a2-163-a-gr`, *Sublative Personal Pronouns: rám, rád, rá...* | `good-for-me-nekem-jo`, `three-locatives` |

### `adjectives`: adjectives

| skill | level | taught in | requires |
|---|---|---|---|
| `adjective-order-before-the-noun` | A1 | `a1-34-b-gr`, *Adjective Order: Before the Noun* | *(none)* |
| `plural-predicate-adjectives-k` | A1 | `a1-31-b-gr`, *Plural Predicate Adjectives: -k* | `plural-nouns-k`, `van-zero-copula` |

### `adverbs`: adverbs

| skill | level | taught in | requires |
|---|---|---|---|
| `direction-adverbs-jobbra-balra` | A1 | `a1-140-a-gr`, *Directions: egyenesen, jobbra, balra* | *(none)* |
| `egyutt-together` | A1 | `a1-30-b-gr`, *együtt — Together* | `present-tense-routine-language` |
| `itt-ott-here-there` | A1 | `a1-24-b-gr`, *Itt / Ott — Here / There* | *(none)* |
| `mindig-and-gyakran-frequency-adverbs` | A1 | `a1-82-a-gr`, *néha and ritkán — the low end of the scale* | `present-tense-routine-language` |
| `nagyon-very` | A1 | `a1-35-a-gr`, *nagyon — Very* | *(none)* |
| `an-en-adverb` | A2 (practised from A1) | `a2-94-a-gr`, *Manner Adverbs: -an/-en* | `adjective-order-before-the-noun` |
| `sequencing-elobb-aztan-utana-vegul` | A2 (practised from A1) | `a2-02-b-gr`, *Sequencing: előbb, aztán, utána, végül* | *(none)* |
| `scalar-adverbs` | C1 | `c1-19-05-a-gr`, *Scalar Evaluative Adverbials Calibrating Magnitude and Traje* | `comparative-bb`, `an-en-adverb` |

### `comparison`: comparison and manner

| skill | level | taught in | requires |
|---|---|---|---|
| `comparative-bb` | A2 | `a2-64-b-gr`, *Comparative Adjectives: -bb* | `adjective-order-before-the-noun` |
| `olyan-mint` | A2 | `a2-18-b-gr`, *olyan, mint: "Like/Such As"* | `comparative-bb` |
| `superlative` | A2 | `a2-76-b-gr`, *Superlative: leg- + Comparative* | `comparative-bb` |
| `correlative-minel-annal` | B1 | `b1-matyas-02-gr`, *Correlative Comparisons: minél ..., annál ...* | `comparative-bb` |
| `kepest` | B1 | `b1-02-05-gr`, *Comparing Experiences: képest, egyre, and the Full Toolkit* | `comparative-bb`, `hoz-suffix` |
| `mintha` | B2 | `b2-31-02-a-gr`, *Hypothetical Sensory Comparisons: mintha + Conditional* | `nek-conditional` |

### `cases`: noun cases

| skill | level | taught in | requires |
|---|---|---|---|
| `ban-ben-in` | A1 | `a1-23-a-gr`, *-ban / -ben — In* | `hungarian-vowels` |
| `delative-rol-rel` | A1 | `a1-152-a-gr`, *Off the Surface: The Delative Suffix -ról/-ről* | `elative-bol-bel` |
| `elative-bol-bel` | A1 | `a1-151-a-gr`, *Out of a Space: The Elative Suffix -ból/-ből* | `ban-ben-in` |
| `how-the-accusative-t-works` | A1 | `a1-102-a-gr`, *How the Accusative -t Works* | *(none)* |
| `kor-time` | A1 | `a1-147-b-gr`, *At Seven O'Clock: the Suffix -kor* | `cardinal-numbers` |
| `movement-with-ba-be` | A1 | `a1-56-a-gr`, *Movement with -ba/-be* | `ban-ben-in` |
| `ul-ul-essive-modal` | A1 | `a1-159-a-gr`, *Manner Adverbs with -ul/-ül: Rosszul, Egyedül, Például* | *(none)* |
| `val-vel` | A1 | `a1-136-a-gr`, *Travelling By: the Suffix -val/-vel* | `hungarian-vowels` |
| `essive-formal-kent` | A2 | `a2-176-a-gr`, *The Essive-Formal Suffix: -ként (As / In the Capacity Of)* | *(none)* |
| `hoz-suffix` | A2 | `a2-31-a-gr`, *-hoz/-hez/-höz: "To/Toward"* | `nal-nel` |
| `nal-nel` | A2 | `a2-13-b-gr`, *-nál/-nél: "At Someone's Place"* | `ban-ben-in` |
| `nta-productive` | A2 | `a2-54-b-gr`, *hétvégente and Other New -nta/-nte Words* | `cardinal-numbers` |
| `on-en-on` | A2 (practised from A1) | `a2-26-a-gr`, *On the Second Floor: -on/-en/-ön* | `hungarian-vowels` |
| `ra-re` | A2 (practised from A1) | `a2-29-a-gr`, *-ra/-re: Onto* | `on-en-on`, `movement-with-ba-be` |
| `three-locatives` | A2 | `a2-28-b-gr`, *A Room, Case by Case* | `ban-ben-in`, `on-en-on`, `nal-nel` |
| `tol-tol` | A2 | `a2-05-a-gr`, *From ... To ...: -tól/-től ... -ig* | `nal-nel` |
| `translative-morphology` | A2 | `a2-171-b-gr`, *Consonant Assimilation in -vá / -vé* | `val-vel` |
| `distributive-nkent` | B1 (practised from A2) | `b1-17-02-a-gr`, *The Distributive Suffix: -nként ('per, by, at intervals')* | `cardinal-numbers` |
| `kent-vs-mint` | B1 | `b1-17-01-b-gr`, *Distinction Between -ként and mint* | `essive-formal-kent`, `olyan-mint` |
| `terminative-case-ig` | B1 (practised from A2) | `b1-08-03-gr`, *The Terminative Case: -ig in Space & Time* | `tol-tol` |

### `prepositions-postpositions`: prepositions and postpositions

| skill | level | taught in | requires |
|---|---|---|---|
| `postpositions-basic` | A1 | `a1-89-a-gr`, *mellett, előtt, mögött — postpositions* | *(none)* |
| `inflected-postpositions` | A2 | `a2-196-a-gr`, *Inflected Spatial Postpositions: előtt, mögött, mellett* | `postpositions-basic`, `possessive-suffixes` |
| `keresztul` | A2 | `a2-22-b-gr`, *keresztül: "Through"* | `on-en-on`, `postpositions-basic` |
| `postpositions-altal-reven` | A2 | `a2-88-a-gr`, *Helyett – Doing This Instead of That* | `postpositions-basic` |
| `postposition-fele` | B1 | `b1-08-01-a-gr`, *Postpositions of Motion: keresztül, át, felé, felől* | `postpositions-basic` |
| `b2-relational-compounds` | B2 | `b2-20-05-a-gr`, *Writing Sociological Analysis: Synthesis of Compound Relatio* | `postpositions-altal-reven` |
| `b2-spatial-postpositions` | B2 | `b2-19-01-a-gr`, *Spatial Postpositions: Boundaries, Lines, and Proximity* | `inflected-postpositions` |

### `verb-forms`: verb conjugation and the present

| skill | level | taught in | requires |
|---|---|---|---|
| `definite-vs-indefinite-conjugation` | A1 | `a1-102-def-gr`, *Definite vs Indefinite Conjugation* | `present-tense-routine-language`, `how-the-accusative-t-works` |
| `ik-verbs-dolgozom-not-dolgozok` | A1 | `a1-85-b-gr`, *-ik verbs: dolgozom, not dolgozok* | `present-tense-routine-language` |
| `megy-jon` | A1 | `a1-136-b-gr`, *Going: the Irregular Verb megy* | `present-tense-routine-language` |
| `present-tense-routine-language` | A1 | `a1-61-a-gr`, *Present Tense: -ok/-ek/-ök* | `personal-pronouns` |
| `eszik-iszik` | A2 | `a2-41-a-gr`, *eszik and iszik: Two Special Verbs* | `ik-verbs-dolgozom-not-dolgozok` |
| `lak-lek-suffix` | A2 | `a2-187-b-gr`, *-lak / -lek with Plural 'You' (Titeket)* | `definite-vs-indefinite-conjugation` |

### `being-becoming`: being, becoming and existence

| skill | level | taught in | requires |
|---|---|---|---|
| `nem-vs-nincs-two-kinds-of-negation` | A1 | `a1-28-b-gr`, *nem vs. nincs — Two Kinds of Negation* | `negation-with-nem`, `van-and-nincs-there-is-there-isn-t` |
| `van-and-nincs-there-is-there-isn-t` | A1 | `a1-24-a-gr`, *Van and Nincs — There Is / There Isn't* | `van-zero-copula` |
| `van-zero-copula` | A1 | `a1-02-b-gr`, *Vagyok, vagy — and where van goes* | `personal-pronouns` |
| `valik-verb` | A2 | `a2-172-a-gr`, *The Verb 'válik' + -vá/-vé (To Become)* | `translative-morphology` |

### `verb-patterns`: verb patterns and government

| skill | level | taught in | requires |
|---|---|---|---|
| `erdekel-construction` | A1 | `a1-95-b-gr`, *Sharing and Expressing Preferences* | `good-for-me-nekem-jo` |
| `faj-construction` | A2 | `a2-82-b-gr`, *Lázam Van – "Have" with Symptoms* | `possessive-suffixes` |
| `verb-government-ert` | A2 (practised from B1) | `a2-38-b-gr`, *-ért and kerül: Asking and Telling Prices* | *(none)* |
| `verb-government-nak-nek` | A2 | `a2-59-a-gr`, *ajánl valakinek valamit: Recommending Something* | `good-for-me-nekem-jo` |
| `verb-government-val-vel` | A2 (practised from A1) | `a2-144-a-gr`, *egyetért valakivel: To Agree With Someone* | `val-vel` |
| `verb-government-ban-ben` | B1 (practised from A2) | `b1-11-05-gr`, *Civic Participation & Verb Governments: részt vesz vmiben, h* | `ban-ben-in` |
| `verb-government-bol-bol` | B1 | `b1-orszagma-03-bol-bol-all-gr`, *Describing Structure & Heraldry: -ból/-ből áll and Compositi* | `elative-bol-bel` |
| `verb-government-hoz-hez` | B1 | `b1-07-03-gr`, *Verbs of Study & Attention: összpontosít, jegyzetel* | `hoz-suffix` |
| `verb-government-ra-re` | B1 (practised from A2) | `b1-02-04-b-gr`, *visszatekint + -ra/-re: Looking Back AT Something* | `ra-re` |
| `verb-government-rol-rel` | B1 | `b1-05-03-a-gr`, *gondoskodik, támaszkodik, ragaszkodik: Verbs of Support* | `delative-rol-rel` |

### `past`: past tenses

| skill | level | taught in | requires |
|---|---|---|---|
| `definite-past` | A2 | `a2-118-b-gr`, *Definite vs Indefinite in the Past* | `past-tense-indefinite`, `definite-vs-indefinite-conjugation` |
| `irregular-past` | A2 | `a2-120-b-gr`, *eszik and iszik: Past Tense* | `past-tense-indefinite` |
| `past-tense-indefinite` | A2 | `a2-116-a-gr`, *Past Tense: Regular Verbs (Indefinite)* | `present-tense-routine-language` |
| `van-past` | A2 | `a2-119-a-gr`, *van in the Past: voltam, voltál, volt...* | `van-zero-copula` |
| `historical-routines` | B1 | `b1-haromresz-04-gr`, *Describing Historical Routines & Habitual Past: rendszeresen* | `past-tense-indefinite`, `building-the-infinitive-the-suffix-ni` |
| `mar-experiential` | B1 (practised from A2) | `b1-02-01-b-gr`, *még (soha) nem + Past Tense: What Hasn't Happened Yet* | `past-tense-indefinite` |

### `future`: the future

| skill | level | taught in | requires |
|---|---|---|---|
| `fog-infinitive` | A2 (practised from A1) | `a2-131-a-gr`, *fog + Infinitive: The General Future* | `building-the-infinitive-the-suffix-ni` |
| `majd-adverb` | A2 | `a2-95-a-gr`, *Present Tense for Future Plans* | `present-tense-routine-language` |

### `conditional`: conditions, hypotheses and wishes

| skill | level | taught in | requires |
|---|---|---|---|
| `nek-conditional` | A1 | `a1-112-a-gr`, *Szeretnék: The Conditional Ending -nék* | `present-tense-routine-language` |
| `ha-clause` | A2 | `a2-65-a-gr`, *If It Rains...: ha + Present Tense* | `present-tense-routine-language` |
| `irregular-nek-conditional` | A2 | `a2-137-b-gr`, *Ennék, Innék, Mennék – Some Everyday -nék Verbs* | `nek-conditional` |
| `barcsak-wish` | B1 | `b1-03-01-b-gr`, *szeretném, ha + Conditional: Saying What You Wish Would Happ* | `nek-conditional` |
| `hypothetical-ha-conditional` | B1 (practised from A2) | `b1-04-01-b-gr`, *Ha (én) a helyedben lennék...: Spelling Out the Full Hypothe* | `ha-clause`, `nek-conditional` |
| `mixed-conditionals` | B1 | `b1-35-02-a-gr`, *Mixed Conditionals: Past Condition Leading to Present Result* | `past-conditional-volna` |
| `past-conditional-volna` | B1 | `b1-rakoczi-02-gr`, *Complex Counterfactual Conditionals: ha... akkor... volna* | `hypothetical-ha-conditional`, `past-tense-indefinite` |
| `felteve-hogy-kiveve-ha` | C1 | `c1-07-03-a-gr`, *Restrictive Conditions: Kizárólag abban az esetben, Amennyib* | `ha-clause` |

### `subjunctive`: the subjunctive

| skill | level | taught in | requires |
|---|---|---|---|
| `mit-csinaljak` | A2 | `a2-87-b-gr`, *Mit Csináljak? – Asking What To Do* | `imperative-indefinite` |
| `hogy-jon-jen` | B1 (practised from A2) | `b1-03-03-b-gr`, *hogy + -jon/-jen: Wanting Something To Happen* | `imperative-indefinite`, `hogy-clauses` |
| `optative-subjunctive` | C1 | `c1-mestersegesintelligencia-04-a-gr`, *Deliberative and Optative Subjunctive in Medical Decision Ma* | `hogy-jon-jen` |

### `imperative`: the imperative

| skill | level | taught in | requires |
|---|---|---|---|
| `imperative-definite` | A2 | `a2-49-a-gr`, *The Imperative with a Definite Object* | `imperative-indefinite`, `definite-vs-indefinite-conjugation` |
| `imperative-indefinite` | A2 (practised from A1) | `a2-48-a-gr`, *The Imperative: Giving a Command* | `present-tense-routine-language` |
| `junk-suggestion` | A2 | `a2-136-a-gr`, *Menjünk? – Turning "Let's..." Into a Suggestion* | `imperative-indefinite` |

### `aspect`: aspect, periphrases and verbal prefixes

| skill | level | taught in | requires |
|---|---|---|---|
| `directional-preverbs` | A1 | `a1-139-a-gr`, *Getting On and Off: fel- and le-* | `movement-with-ba-be` |
| `szokott-infinitive-habitual-actions` | A1 | `a1-81-b-gr`, *szokott + infinitive: habitual actions* | `building-the-infinitive-the-suffix-ni` |
| `jar-iskolaba` | A2 | `a2-91-a-gr`, *jár: Attending School or University* | `present-tense-routine-language` |
| `meg-meaning` | A2 | `a2-109-a-gr`, *meg-: megcsinál and the Idea of 'Completely Done'* | `directional-preverbs` |
| `nominalizing-processes` | B1 | **none: screen to write** | `nominalization` |
| `b2-figurative-preverbs` | B2 | `b2-28-01-a-gr`, *Figurative Preverbs of Integration and Alienation: beilleszk* | `meg-meaning` |
| `b2-frequentative-verbs` | B2 | `b2-05-01-a-gr`, *Frequentative and Attenuative Verbs with -gat/-get* | `meg-meaning` |

### `modality`: obligation, ability, permission and probability

| skill | level | taught in | requires |
|---|---|---|---|
| `akar-tervez-infinitive` | A1 | `a1-147-a-gr`, *Wanting To Meet: akar + Infinitive* | `building-the-infinitive-the-suffix-ni` |
| `kell-infinitive` | A1 | `a1-118-b-gr`, *Kell: An Impersonal Need* | `building-the-infinitive-the-suffix-ni` |
| `lehet-infinitive` | A1 | `a1-149-b-gr`, *Maybe? lehet and Being Free: ráér* | `building-the-infinitive-the-suffix-ni` |
| `kellene` | A2 | `a2-87-a-gr`, *Kellene – Giving Soft Advice* | `kell-infinitive`, `nek-conditional` |
| `potential-hat-het` | A2 | `a2-115-b-gr`, *-hat/-het: A One-Word Preview* | `present-tense-routine-language` |
| `szabad-infinitive` | A2 | `a2-114-b-gr`, *Nem szabad: A Strong Prohibition* | `kell-infinitive` |
| `tud-infinitive-skills` | A2 | `a2-111-a-gr`, *tud + Infinitive: A Wider Range of Skills* | `building-the-infinitive-the-suffix-ni` |
| `formal-obligation` | B1 | `b1-10-03-gr`, *Tenancy Rights & Contractual Conditions: köteles, jogosult, * | `kell-infinitive`, `future-participle-ando` |
| `kellett-volna` | B1 | `b1-20-02-a-gr`, *Unfulfilled Past Obligation: kellett volna + infinitive ('sh* | `kellene`, `past-tense-indefinite` |
| `epistemic-modality` | C1 | `c1-22-01-a-gr`, *Epistemic Speculative Modal Structures Exploring Future Ling* | `kell-infinitive`, `potential-hat-het` |

### `voice`: passive, impersonal, reflexive and causative

| skill | level | taught in | requires |
|---|---|---|---|
| `egymas` | A2 | `a2-23-b-gr`, *egymással: "With Each Other"* | `personal-pronouns` |
| `mediopassive-verbs-odik` | B1 (practised from A2) | `b1-06-02-a-gr`, *Passive-Avoidance: Verbs in -ódik / -ődik* | `present-tense-routine-language` |
| `agentless-constructions` | B2 | `b2-15-01-a-gr`, *Natural Agent-Backgrounding: 3rd-Person Plural and Middle Ve* | `mediopassive-verbs-odik` |
| `causative-verbal-derivations` | B2 (practised from B1) | `b2-10-04-a-gr`, *Lexicalized vs. Productive Causatives: tanít vs. taníttat, é* | `definite-vs-indefinite-conjugation` |

### `non-finite`: infinitives, participles and gerunds

| skill | level | taught in | requires |
|---|---|---|---|
| `building-the-infinitive-the-suffix-ni` | A1 | `a1-143-b-gr`, *Building the Infinitive: the Suffix -ni* | `present-tense-routine-language` |
| `inflected-infinitives` | A2 | `a2-201-b-gr`, *The Dative Person with Inflected Infinitives* | `building-the-infinitive-the-suffix-ni`, `possessive-suffixes`, `kell-infinitive` |
| `future-participle-ando` | B1 | `b1-14-01-a-gr`, *The Future / Obligatory Participle in -andó / -endő* | `present-participle` |
| `participle-actions` | B1 (practised from A2) | `b1-nemzetiugy-01-gr`, *Adverbial Participle -va/-ve in Historical Descriptions* | `past-tense-indefinite` |
| `past-participle-adjective` | B1 | `b1-02-03-a-gr`, *The Past Participle as an Adjective: elkészített étel* | `past-tense-indefinite` |
| `present-participle` | B1 | `b1-06-01-a-gr`, *The Present Participle as Adjective: -ó / -ő* | `present-tense-routine-language` |
| `participial-clauses` | B2 | `b2-szecesszio-02-a-gr`, *Passive & Anterior Pre-Nominal Participles (-t/-tt) with ált* | `present-participle`, `past-participle-adjective` |

### `negation`: negation

| skill | level | taught in | requires |
|---|---|---|---|
| `negation-with-nem` | A1 | `a1-04-b-gr`, *Nem* | *(none)* |
| `soha-needs-nem-negative-concord` | A1 | `a1-82-b-gr`, *soha needs nem: negative concord* | `negation-with-nem` |

### `questions`: questions

| skill | level | taught in | requires |
|---|---|---|---|
| `ki-and-mi` | A1 | `a1-03-a-gr`, *Ki? and Mi?* | *(none)* |
| `quantity-choice-questions-mennyi-melyik` | A1 | `a1-31-a-gr`, *milyen? — Asking What Someone Is Like* | `ki-and-mi` |
| `spatial-questions-hol-hova` | A1 | `a1-13-a-gr`, *Hol?* | `ki-and-mi` |
| `yes-no-questions` | A1 | `a1-04-a-gr`, *Yes/No Questions* | *(none)* |
| `rhetorical-questions` | C1 | `c1-16-02-a-gr`, *Rhetorical and Deliberative Interrogative Structures in Poli* | `yes-no-questions`, `nek-conditional` |

### `word-order`: word order and focus

| skill | level | taught in | requires |
|---|---|---|---|
| `basic-hungarian-word-order` | A1 | `a1-20-b-gr`, *Basic Hungarian word order* | *(none)* |
| `is-placing-also-too` | A1 | `a1-83-a-gr`, *is — placing "also / too"* | `basic-hungarian-word-order` |
| `prefix-word-order` | A2 | `a2-110-a-gr`, *Prefix + Verb Together: The Neutral Word Order* | `directional-preverbs`, `basic-hungarian-word-order` |
| `b2-cleft-identification` | B2 | `b2-33-01-a-gr`, *Cleft Identification and Emphatic Focus: az nem más, mint & * | `b2-focus-inversion`, `relative-clauses-aki-ami-amely` |
| `b2-contrastive-topic` | B2 | `b2-kavehazikultura-01-a-gr`, *Framing Contrastive Topics: ami X-et illeti and viszont* | `basic-hungarian-word-order` |
| `b2-focus-inversion` | B2 | `b2-01-02-a-gr`, *Preverb-Verb Inversion Under Focus and Negation* | `prefix-word-order` |

### `coordination`: joining clauses: and, but, or, not … but

| skill | level | taught in | requires |
|---|---|---|---|
| `egyreszt-masreszt` | A2 (practised from A1) | `a2-21-b-gr`, *nem csak..., hanem... is: "Not Only, But Also"* | *(none)* |
| `adversative-contrast` | B1 (practised from A1) | `b1-32-03-a-gr`, *Adversative Contrast Markers: Azonban, Viszont & Mindazonált* | *(none)* |

### `relative-clauses`: relative clauses

| skill | level | taught in | requires |
|---|---|---|---|
| `relative-clauses-aki-ami-amely` | A2 | `a2-19-a-gr`, *aki: "Who"* | `ki-and-mi`, `how-the-accusative-t-works` |
| `ahol-amikor` | B1 | `b1-arpadhaz-04-ahol-amikor-gr`, *ahol and amikor: Relative Clauses of Place and Time* | `relative-clauses-aki-ami-amely` |
| `vonatkozoi-nevmas-esetei` | B1 | `b1-arpadhaz-03-vonatkozoi-nevmas-esetei-gr`, *Case Forms of aki: akit, akinek, akik* | `relative-clauses-aki-ami-amely` |
| `b2-relative-postpositions` | B2 | `b2-23-02-a-gr`, *Possessive Relative Chains: amelynek a tetején* | `vonatkozoi-nevmas-esetei`, `inflected-postpositions` |

### `complement-clauses`: that-clauses and opinions

| skill | level | taught in | requires |
|---|---|---|---|
| `hogy-clauses` | A2 | `a2-88-b-gr`, *Azt Javaslom, Hogy... – Giving Advice with hogy* | *(none)* |
| `szerintem` | A2 | `a2-141-b-gr`, *gondolom: Three Ways to Open an Opinion* | `hogy-clauses` |
| `b2-cataphoric-clauses` | B2 | `b2-18-01-a-gr`, *Cataphoric Demonstrative Anchors with Complement Clauses* | `hogy-clauses`, `demonstratives-ez-az` |

### `time-clauses`: time clauses and expressions

| skill | level | taught in | requires |
|---|---|---|---|
| `temporal-postpositions` | A1 | `a1-164-a-gr`, *Before and After in Time: Előtt vs Után* | `postpositions-basic` |
| `ota-duration` | A2 | `a2-83-b-gr`, *Két Napja – "For X Days" with -ja/-je* | `3rd-person-possessive` |
| `mig-egyidejuseg` | B1 (practised from A1) | `b1-karpatmedence-03-mig-egyidejuseg-gr`, *míg — Simultaneous Events* | *(none)* |
| `miutan-mielott` | B1 | `b1-01-03-b-gr`, *The Turning Point: miután and mielőtt Together* | `past-tense-indefinite` |
| `b2-temporal-framing` | B2 | `b2-22-01-a-gr`, *Temporal Framing Postpositions: folyamán, során, múltával, k* | `temporal-postpositions`, `miutan-mielott` |

### `cause-purpose-result`: cause, purpose and result

| skill | level | taught in | requires |
|---|---|---|---|
| `mert-because` | A1 | `a1-119-b-gr`, *Mert: Because* | *(none)* |
| `azert-hogy-purpose` | B1 | `b1-03-04-a-gr`, *azért, hogy + -jon/-jen: Purpose Clauses* | `hogy-jon-jen` |
| `causal-postpositions` | B1 | `b1-mohacs-01-gr`, *Causality & Historical Preconditions: miatt, következtében, * | `mert-because`, `postpositions-basic` |
| `formal-purpose` | B1 | `b1-erdelyaranykora-04-gr`, *Diplomatic Intentions & Alliances: annak érdekében, hogy...* | `azert-hogy-purpose` |
| `nehogy-purpose` | B1 | `b1-03-04-b-gr`, *nehogy + -jon/-jen: So That Something Doesn't Happen* | `azert-hogy-purpose` |
| `annyira-hogy` | B2 | `b2-32-01-a-gr`, *Consecutive Clauses of Degree: olyannyira ..., hogy & oly mé* | `hogy-clauses` |

### `concession`: concession

| skill | level | taught in | requires |
|---|---|---|---|
| `concessive-annak-ellenere` | B1 | `b1-05-04-a-gr`, *annak ellenére, hogy: Despite the Fact That* | `hogy-clauses` |
| `concessive-postpositions` | B1 | `b1-29-01-b-gr`, *Concession with Postpositions: ellenére, dacára* | `concessive-annak-ellenere` |
| `concessive-indefinites` | B2 | `b2-09-01-a-gr`, *Concessive Generalizations: bárhogyan ... is* | `concessive-annak-ellenere` |
| `even-if-ha-is` | B2 | `b2-27-01-a-gr`, *Emphatic Concessive Conditionals: még akkor is, ha... and ak* | `ha-clause`, `is-placing-also-too` |

### `reported-speech`: reported speech

| skill | level | taught in | requires |
|---|---|---|---|
| `indirect-questions` | B1 | `b1-13-02-a-gr`, *Indirect Questions in Reporting: azt kérdezte, hogy... -e* | `reported-speech-statements` |
| `reported-commands` | B1 | `b1-27-03-a-gr`, *Indirect Imperatives: Subjunctive in Dependent Clauses* | `reported-speech-statements`, `hogy-jon-jen` |
| `reported-speech-statements` | B1 (practised from A2) | `b1-13-01-a-gr`, *Reported Speech in News: azt mondta, hogy... and Tense Reten* | `hogy-clauses`, `past-tense-indefinite` |

### `discourse-markers`: discourse markers and stance

| skill | level | taught in | requires |
|---|---|---|---|
| `additive-connectors` | B1 | `b1-32-01-b-gr`, *Additive Discourse Connectors: Ráadásul, Továbbá & Mindemell* | *(none)* |
| `evidentials` | B1 (practised from A2) | `b1-13-03-a-gr`, *Expressing Doubt & Verification: úgy tűnik, állítólag, kétsé* | *(none)* |
| `contrastive-discourse-markers` | B2 | `b2-16-02-a-gr`, *Adversative Transitions & Counter-Thesis Architecture* | `adversative-contrast` |
| `discourse-particles` | B2 | `b2-13-02-a-gr`, *Shared Knowledge and Pragmatic Complicity: hiszen, ugyebár, * | *(none)* |
| `conclusive-markers` | C1 | `c1-visegrad-05-a-gr`, *Discourse Summation Particles and Definitive Conclusions in * | `additive-connectors` |
| `epistemic-hedging` | C1 | `c1-01-04-a-gr`, *Epistemic Stance Markers: Ennek fényében, Mindebből következ* | `evidentials` |
| `evaluative-stance` | C1 | `c1-26-04-a-gr`, *Deliberative Modal Structures Articulating Public Sphere Dia* | *(none)* |
| `framing-markers` | C1 | `c1-tarsadalmireteg-01-a-gr`, *Spatial Disparity Discourse Markers Characterizing Territori* | *(none)* |

### `politeness-address`: politeness and forms of address

| skill | level | taught in | requires |
|---|---|---|---|
| `formal-address-on` | A1 | `a1-124-a-gr`, *Polite Questions: Addressing Someone as Ön* | `present-tense-routine-language` |
| `kerek-vs-szeretnek` | A1 | `a1-94-a-gr`, *Making Requests* | `nek-conditional` |
| `diplomatic-softening` | B2 | `b2-29-01-a-gr`, *Diplomatic Conditionals and Polite Hedging: célszerű lenne, * | `nek-conditional`, `formal-address-on` |

### `register-style`: register, style and rhetoric

| skill | level | taught in | requires |
|---|---|---|---|
| `twin-words-colloquial` | B2 | `b2-34-01-a-gr`, *Expressive Twin-Words and Reduplications: gizgaz, limlom, cs* | *(none)* |
| `essay-oratory-style` | C1 | `c1-01-05-a-gr`, *Synthesizing C1 Argumentation: Period, Cadence, and Ethical * | `conclusive-markers` |
| `litotes-understatement` | C1 | `c1-05-02-a-gr`, *Understatement, Antiphrasis, and Litotes in Satirical Regist* | `negation-with-nem` |
| `metaphor` | C1 | `c1-nyelvfilozofia-04-a-gr`, *Cognitive Metaphors and Spatial Conceptualization in Hungari* | *(none)* |
| `official-register` | C1 | `c1-08-03-a-gr`, *Agent Deletion and Formal Distancing in Administrative Decis* | `agentless-constructions`, `formal-obligation` |
| `rhetorical-argument` | C1 | `c1-01-03-a-gr`, *Rhetorical Antithesis: Ezzel szemben, Ellenben, and Csakhogy* | `contrastive-discourse-markers` |
| `satire-parody` | C1 | `c1-pestiironia-02-a-gr`, *Literary Parody, Stylistic Mimicry, and Philosophical Wit* | `litotes-understatement` |
