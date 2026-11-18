# ES C1 core: level plan (step 1, for sign-off)

## Decided by the user (2026-11-18)

- Start C1 now; the core does not depend on the culture/latam tracks.
- Lesson shape: the ES B2 size (5 teaching lessons of ~8 exercises:
  Introduce 1, Controlled 2, Practice 2, Dialogue 1, Production 1,
  Check 1; Reading 3 on lesson 05; consolidation 12).
- Mostly identical files in es-latam and es-es; vocabulary and small
  differences where relevant (*computadora/ordenador*, *carro/coche*,
  leísmo noted as the Spain norm, …). Written in es-latam first, then
  planted in es-es with the differences listed per unit.
- About 20 new C1 skills; the other units are topic units.
- Unit texts: original genre texts (column, essay, interview, report, …).

## Candidate check (against `skills/es.json` and the core screens)

Dropped: *lo + adj + que* (B1 core b1-40-04 teaches it); verbal idioms
and support-verb collocations (choosing the word is vocabulary by the
tagging rules; the units stay, tagged vocabulary); mitigation strategies
(overlaps B2 `hedging`, `imperfecto-de-cortesia`). Added: *como* +
subjunctive conditions, the concessive future, *de lo que* comparatives
(none taught in core). *sentir que* has a tip on b2-06-02 (recapped, not
retaught). *el cual* appears only on hidden-track screens; B1
`relativas-preposicion-el-que` is its prerequisite. *dequeísmo* appears
only on a hidden latam screen (b2-salvadorhonduras-02).

## New skills (20)

| Slug | Family | Title (house style) | taught_in | requires |
|---|---|---|---|---|
| infinitivo-compuesto-nominal | non-finite | the perfect and nominal infinitive like el haber firmado | c1-01-02-a-gr | nominalizacion-despersonalizacion |
| dequeismo-queismo | complement-clauses | de que and que after verbs, nouns and adjectives | c1-02-01-a-gr | – |
| gerundio-normativo | non-finite | correct uses of the gerund in formal writing | c1-02-03-a-gr | gerundio-acciones-paralelas |
| derivacion-nominal-verbal | word-formation | noun and verb derivation in specialised language | c1-03-01-a-gr | – |
| condicional-de-rumor | conditional | the conditional for unconfirmed reports in the press | c1-04-01-a-gr | future-probability |
| estilo-titular | register-style | headline style with verbless and infinitive clauses | c1-04-03-a-gr | – |
| futuro-subjuntivo-reconocimiento | subjunctive | the future subjunctive in legal and fixed texts | c1-06-02-a-gr | imperfect-subjunctive-forms |
| relativos-el-cual | relative-clauses | formal relatives with el cual and lo cual | c1-07-01-a-gr | relativas-preposicion-el-que |
| concordancia-ad-sensum | numbers-quantity | agreement with collective nouns and quantity phrases | c1-08-01-a-gr | – |
| comparativas-de-lo-que | comparison | comparisons with de lo que and del que | c1-08-03-a-gr | superlatives |
| dislocacion-clitica | word-order | fronted objects picked up by a clitic pronoun | c1-11-01-a-gr | inversion-enfasis-fronting |
| verbos-doble-modo | subjunctive | verbs whose meaning changes with the indicative or subjunctive | c1-12-01-a-gr | subjunctive-influence, subjunctive-emotion |
| se-aspectual | pronouns | aspectual se with verbs like comerse and leerse | c1-17-01-a-gr | – |
| marcadores-conversacionales | discourse-markers | spoken discourse markers like pues, vamos and hombre | c1-18-01-a-gr | reformulation-markers |
| como-condicional-subjuntivo | conditional | conditions and warnings with como and the subjunctive | c1-19-01-a-gr | conditional-conjunctions |
| futuro-concesivo | future | the concessive future and conditional like será caro, pero | c1-20-01-a-gr | future-probability |
| con-lo-que-para-lo-que | concession | evaluative con lo que and para lo que | c1-20-03-a-gr | – |
| ni-que-exclamativo | subjunctive | ironic exclamations with ni que and the imperfect subjunctive | c1-21-01-a-gr | imperfect-subjunctive-forms |
| sufijos-apreciativos | word-formation | evaluative suffixes for tone and attitude | c1-22-01-a-gr | superlatives |
| leismo-laismo-reconocimiento | pronouns | recognising leísmo and laísmo | c1-25-01-a-gr | pronombres-combinados |

Plus 36 vocabulary skills `c1-<unit id>-vocab`. `requires` slugs are
checked by the validator when the entries go in.

## Unit table (36, all `track: "core"`)

New skill in **bold** with its lesson; the other lessons recap B1/B2
skills at C1 density in the unit's topic. Per-lesson detail for each unit
goes in its batch notes; Units 1–2 (pilot) are given in full below.

| # | id | Title | New skill (lesson) | Text genre |
|---|---|---|---|---|
| 1 | academic-argument | Academic Argument & Precision | **infinitivo-compuesto-nominal** (02) | academic essay |
| 2 | written-norm | Norm & Correctness in Writing | **dequeismo-queismo** (01), **gerundio-normativo** (03) | style-guide column |
| 3 | science-communication | Science & Specialised Language | **derivacion-nominal-verbal** (01) | popular-science article |
| 4 | press-news | The Press & Unconfirmed News | **condicional-de-rumor** (01), **estilo-titular** (03) | news report |
| 5 | opinion-editorial | Opinion & Editorial Stance | – | editorial |
| 6 | legal-language | Law & Legal Language | **futuro-subjuntivo-reconocimiento** (02) | model regulation with commentary |
| 7 | public-administration | Institutions & Administration | **relativos-el-cual** (01) | official report |
| 8 | data-demography | Demography & the Language of Data | **concordancia-ad-sensum** (01), **comparativas-de-lo-que** (03) | data report |
| 9 | economy-markets | Economy & Markets | – | analysis column |
| 10 | work-labour | Work & the Labour Market | – | interview |
| 11 | debate-information | Debate & Information Structure | **dislocacion-clitica** (01) | debate transcript |
| 12 | interpretation-meaning | Interpretation & Meaning | **verbos-doble-modo** (01) | essay |
| 13 | health-bioethics | Health & Bioethics | – | bioethics essay |
| 14 | environment-climate | Environment & Climate Policy | – | policy report |
| 15 | ai-digital-ethics | AI & Digital Ethics | – | op-ed |
| 16 | cities-housing | Cities & Housing | – | feature report |
| 17 | everyday-aspect | Everyday Speech & Aspect | **se-aspectual** (01) | short story with dialogue |
| 18 | conversation-markers | Conversation & Spoken Markers | **marcadores-conversacionales** (01) | interview transcript |
| 19 | warnings-conditions | Warnings, Conditions & Threats | **como-condicional-subjuntivo** (01) | story |
| 20 | concession-evaluation | Concession & Evaluation in Speech | **futuro-concesivo** (01), **con-lo-que-para-lo-que** (03) | column |
| 21 | irony-humour | Irony & Humour | **ni-que-exclamativo** (01) | satirical column |
| 22 | tone-attitude | Tone & Attitude in Words | **sufijos-apreciativos** (01) | *crónica* |
| 23 | idiom-figurative | Idiom & Figurative Language | – (vocabulary) | story |
| 24 | negotiation-mediation | Negotiation & Mediation | – | mediation transcript |
| 25 | language-variation | Language Variation | **leismo-laismo-reconocimiento** (01) | essay on varieties |
| 26 | education-university | Education & the University | – | debate article |
| 27 | history-memory | History & Memory | – | essay |
| 28 | migration-identity | Migration & Identity | – | testimony (*crónica*) |
| 29 | human-rights | Human Rights & Justice | – | report |
| 30 | politics-democracy | Politics & Democracy | – | speech |
| 31 | art-criticism | Art & Criticism | – | exhibition review |
| 32 | literary-analysis | Literature & Literary Analysis | – | essay on a genre, not one work |
| 33 | philosophy-ethics | Philosophy & Ethics | – | dialogue essay |
| 34 | globalisation-geopolitics | Globalisation & Geopolitics | – | analysis |
| 35 | public-speaking | Public Speaking & Rhetoric | – | speech with commentary |
| 36 | own-voice-c1 | Synthesis: Your Own Voice | – | capstone essay |

## Pilot units in full

**Unit 1 academic-argument**
- 01 essay architecture at C1 density (recap `essay-style`, `contrast-markers`)
- 02 **infinitivo-compuesto-nominal** (*el haber firmado*, *tras haberlo leído*, *al no haber respondido*)
- 03 dense nominal style (recap `nominalizacion-despersonalizacion`)
- 04 precision and reformulation in argument (recap `reformulation-markers`)
- 05 qualifying academic claims (recap `hedging`) + text: academic essay, 400–600 words

**Unit 2 written-norm**
- 01 **dequeismo-queismo** (*pienso que* / *me alegro de que*, *estoy seguro de que*)
- 02 *se* passive vs impersonal agreement in formal writing (recap `se-pasivo-vs-impersonal`)
- 03 **gerundio-normativo** (no gerund of posteriority, no adjectival gerund: *una caja conteniendo*)
- 04 sequence of tenses in formal reports (recap `correlacion-temporal-subjuntivo`)
- 05 double participles in formal use (recap `participios-irregulares-dobles`) + text: style-guide column

## After sign-off

Add the 20 grammar skills and 36 vocabulary skills to `skills/es.json` and
`skills/frozen-es.json`, write `curriculum/units/c1.json` in both
courses (hidden until the level checklist), run
`build_skill_registry.py`, then the tooling (step 2) and the pilot.
