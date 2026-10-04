# Grammar families: draft for approval (ROADMAP 125, step 1)

Status: **family list approved 2026-10-04 (see "Decided" at the end); the skill mapping is a draft. Not in `skill-registry.json` yet.** One shared
list of grammar families for every language, the grammar half of the
format in [skill-tagging-spec.md](skill-tagging-spec.md). The vocabulary
half is [skill-families-draft.md](skill-families-draft.md). Every
existing grammar skill is mapped in
[grammar-families-mapping.md](grammar-families-mapping.md) (and `.json`).

## Sources checked

| Source | What it is | How it's used |
|---|---|---|
| **PCIC, *Gramática*** (Instituto Cervantes) | The CEFR-based grammar inventory for Spanish, A1–C2, in 15 chapters: 1 sustantivo, 2 adjetivo, 3 artículo, 4 demostrativos, 5 posesivos, 6 cuantificadores, 7 pronombre, 8 adverbio, 9 verbo, 10–12 sintagmas nominal/adjetival/verbal, 13 oración simple, 14 coordinación, 15 subordinación. | Backbone for word classes and the verb. Chapters 9 and 15 are too big for one map region each, so they're split by tense or mood and by clause type. |
| **English Grammar Profile** (Cambridge, from the Cambridge Learner Corpus) | The CEFR-aligned learner grammar for English, in 19 supercategories: adjectives, adverbs, clauses, conjunctions, determiners, discourse markers, focus, future, modality, negation, nouns, passives, past, prepositions, present, pronouns, questions, reported speech, verbs. | Cross-check from a second language. It adds what the PCIC leaves to other inventories: focus, discourse markers, modality, negation and questions as families of their own. |
| **The three courses' own grammar skills** (1,128 slugs) | What es-es, es-latam and hu actually teach. | Checks that the list covers Hungarian: cases, postpositions, preverbs, the definite conjugation, possessive suffixes, vowel harmony. **No external Hungarian-as-a-foreign-language grammar syllabus was retrieved.** The Hungarian families are inferred from the course itself and from general typology, so a Hungarian teacher's check is worth having. |

The Council of Europe *Reference Level Descriptions* were the intended
backbone, but they're per-language books (the PCIC *is* the Spanish one),
with no shared cross-language grammar list. The list below is that shared
list, built from the two.

## The proposed families

37 families in 5 display groups. The group is only for laying out the skill
map (ROADMAP 131). It lives on the family list, never on skills or
exercises. Counts are today's grammar skills per course, before the
merges below.

| # | Family | Name | Group | PCIC chapter | EGP supercategory | es-es | es-latam | hu |
|---|---|---|---|---|---|---|---|---|
| 1 | `sounds-spelling` | sounds, spelling and stress | Sounds and words | — (separate PCIC inventories: Pronunciación, Ortografía) | — (outside the EGP) | 0 | 0 | 2 |
| 2 | `word-formation` | word formation | Sounds and words | 1, 2 (formación de palabras) | nouns, adjectives (in part) | 1 | 2 | 10 |
| 3 | `nouns` | noun gender and number | Nouns and noun phrases | 1 El sustantivo | nouns | 2 | 2 | 1 |
| 4 | `articles-demonstratives` | articles and demonstratives | Nouns and noun phrases | 3 El artículo, 4 Los demostrativos | determiners | 7 | 7 | 6 |
| 5 | `possession` | possession | Nouns and noun phrases | 5 Los posesivos | determiners, pronouns (in part) | 2 | 2 | 10 |
| 6 | `numbers-quantity` | numbers and quantity | Nouns and noun phrases | 6 Los cuantificadores | determiners (quantifiers) | 2 | 2 | 8 |
| 7 | `pronouns` | pronouns | Nouns and noun phrases | 7 El pronombre | pronouns | 7 | 7 | 12 |
| 8 | `adjectives` | adjectives | Nouns and noun phrases | 2 El adjetivo, 11 Sintagma adjetival | adjectives | 3 | 3 | 2 |
| 9 | `adverbs` | adverbs | Nouns and noun phrases | 8 El adverbio | adverbs | 2 | 3 | 14 |
| 10 | `comparison` | comparison and manner | Nouns and noun phrases | 2, 8 (gradación), 15 (comparativas, modales) | adjectives, adverbs (comparison) | 2 | 8 | 33 |
| 11 | `cases` | noun cases | Nouns and noun phrases | — (Spanish has no cases) | — (English has no cases) | 0 | 0 | 27 |
| 12 | `prepositions-postpositions` | prepositions and postpositions | Nouns and noun phrases | 12 Sintagma verbal (complementos), B2+ sintagma preposicional | prepositions | 4 | 7 | 11 |
| 13 | `verb-forms` | verb conjugation and the present | Verbs | 9 El verbo | present, verbs | 10 | 10 | 9 |
| 14 | `being-becoming` | being, becoming and existence | Verbs | 9 El verbo (ser, estar, haber), 12 | verbs | 9 | 15 | 8 |
| 15 | `verb-patterns` | verb patterns and government | Verbs | 12 Sintagma verbal | verbs | 14 | 15 | 13 |
| 16 | `past` | past tenses | Verbs | 9 El verbo (pasado) | past | 22 | 25 | 7 |
| 17 | `future` | the future | Verbs | 9 El verbo (futuro) | future time | 7 | 9 | 3 |
| 18 | `conditional` | conditions, hypotheses and wishes | Verbs | 9 (condicional), 15 (condicionales) | clauses (conditional), modality (in part) | 12 | 41 | 18 |
| 19 | `subjunctive` | the subjunctive | Verbs | 9 El verbo (subjuntivo) | — (no productive subjunctive in English) | 14 | 33 | 4 |
| 20 | `imperative` | the imperative | Verbs | 9 El verbo (imperativo) | verbs | 14 | 14 | 3 |
| 21 | `aspect` | aspect, periphrases and verbal prefixes | Verbs | 9 (perífrasis), 12 | verbs, present and past (aspect) | 10 | 27 | 9 |
| 22 | `modality` | obligation, ability, permission and probability | Verbs | 9 (perífrasis modales) | modality | 6 | 16 | 44 |
| 23 | `voice` | passive, impersonal, reflexive and causative | Verbs | 9, 12, 13 (pasiva, impersonal) | passives | 6 | 30 | 13 |
| 24 | `non-finite` | infinitives, participles and gerunds | Verbs | 9 El verbo (formas no personales) | verbs, clauses (non-finite) | 1 | 2 | 21 |
| 25 | `negation` | negation | Sentences | 13 La oración simple | negation | 0 | 1 | 2 |
| 26 | `questions` | questions | Sentences | 13 La oración simple (interrogativas) | questions | 3 | 3 | 11 |
| 27 | `word-order` | word order and focus | Sentences | 13 La oración simple (orden) | focus | 0 | 3 | 10 |
| 28 | `coordination` | joining clauses: and, but, or, not … but | Sentences | 14 Coordinación | conjunctions | 2 | 4 | 3 |
| 29 | `relative-clauses` | relative clauses | Sentences | 15 Subordinación (adjetivas) | clauses (relative) | 7 | 26 | 8 |
| 30 | `complement-clauses` | that-clauses and opinions | Sentences | 15 Subordinación (sustantivas) | clauses (that-clauses) | 7 | 11 | 3 |
| 31 | `time-clauses` | time clauses and expressions | Sentences | 15 Subordinación (temporales) | clauses (time), conjunctions | 6 | 15 | 11 |
| 32 | `cause-purpose-result` | cause, purpose and result | Sentences | 15 Subordinación (causales, finales, consecutivas) | clauses, conjunctions | 6 | 32 | 22 |
| 33 | `concession` | concession | Sentences | 15 Subordinación (concesivas) | clauses, conjunctions | 3 | 27 | 13 |
| 34 | `reported-speech` | reported speech | Sentences | 15 (estilo indirecto) | reported speech | 4 | 16 | 3 |
| 35 | `discourse-markers` | discourse markers and stance | Text and register | — (PCIC Tácticas y estrategias pragmáticas) | discourse markers | 5 | 34 | 118 |
| 36 | `politeness-address` | politeness and forms of address | Text and register | — (PCIC Tácticas pragmáticas: cortesía) | modality (in part) | 1 | 7 | 6 |
| 37 | `register-style` | register, style and rhetoric | Text and register | — (PCIC Géneros discursivos) | — (outside the EGP) | 0 | 9 | 18 |

A language uses the families it needs: Spanish has no `cases`; Polish,
Czech, Slovak and German will. A family only one language needs requires
the user's sign-off.

## Choosing a family: the rules

A skill gets exactly one grammar family. These rules make that choice
reproducible for any author and any language:

1. **The family is what the skill's one explanation is about.** If a
   skill needs two families, it fails the one-explanation test and should
   be split (spec § "Grammar skills: how fine").
2. **Meaning beats form for relations between events.** A skill defined
   by meaning (cause, purpose, result, concession, time) goes to that
   clause family, whatever the form: conjunction, postposition (*miatt*),
   prepositional phrase (*a raíz de*), infinitive (*antes de* + inf.) or
   participle. A skill defined by a form with no such meaning goes to the
   form family (`cases`, `prepositions-postpositions`, `non-finite`).
3. **Mood families are for mood choice driven by a trigger class**
   (verbs of influence, emotion, doubt, value judgments; *ojalá*), and
   for the mood's own forms. When the trigger is a conjunction or clause
   type, the clause family wins: *para que* + subj. → `cause-purpose-result`,
   *cuando* + subj. → `time-clauses`, relative + subj. → `relative-clauses`,
   *no creo que* → `complement-clauses`.
4. **Conditions and counterfactuals go to `conditional`**, including
   *si* + imperfect subjunctive, conditional verb forms, mixed
   conditionals and counterfactual wishes (*ojalá hubiera*, *bárcsak*).
   Present-tense wishes (*ojalá* + present subj.) stay in `subjunctive`.
5. **Modal meaning goes to `modality`** even when it's built from a
   conditional form (*kellene*, *kellett volna*, *debería*) or a
   periphrasis (*tener que*, *haber de*, *deber de*).
6. **Personal pronouns with case endings** (*nálam*, *rólam*, *velem*)
   go to `pronouns`. A case's own form and meaning → `cases`. A case or
   preposition a verb requires (*vár valakire*, *pensar en*) →
   `verb-patterns`.
7. **Verbal prefixes**: their meaning (direction, aspect) → `aspect`;
   their position (separation, inversion) → `word-order`.
8. **Grading words** (*más … que*, *-bb*, *minél … annál*, *como si*,
   *mintha*) → `comparison`.
9. **Not grammar at all** (a communicative function, a topic's words, a
   synthesis bucket) → no grammar family. The skill is reclassified, and
   each exercise is retagged by what it tests.

## What the mapping found

These are worklists for step 2 (the registry), where the frozen list is
settled. None of them is changed yet.

- **144 skills registered as grammar aren't grammar** (es-es 13, es-latam
  105, hu 39), carrying 2,479 exercises. Most are es-latam B2 country
  units (`bolivia-potosi-cerro-rico-plata`, `peru-gastronomia-nikkei-chifa`)
  and HU C1 policy topics (`c1-nuclear-governance`,
  `c1-fiscal-counterbalancing`). The rest are functions (`greetings`,
  `cafe-interaction`, `weather`) and one catch-all (`b2-mastery-synthesis`,
  88 exercises).
- **244 grammar skills are tied to one unit's topic** (hu 196, es-latam
  48), carrying 1,666 exercises: real grammar points under a topic name.
  HU C1 is the worst: 17 versions of the proportional correlative
  (`c1-adv-proportional-nurse-shortage`, `…-veto-diplomacy`, …), 20 of
  deontic modal statements (`c1-modal-deontic-…`), 18 of conclusive
  particles and 16 of participial clauses. Each collapses into one generic skill, with the old slugs kept
  as aliases.
- **55 duplicate groups** (143 skills) teach the same thing under two to
  five slugs, e.g. `ir-infinitive` / `ir-a-infinitivo` / `futuro-proximo` /
  `future-intention`, and `demonstratives-ez-az` / `ez-az-this-that`.
- **19 skills name two separate things** (e.g. `comparison-relative-clauses`,
  `lo-adjetivo-que`, `yes-no-questions` "and negation") and need splitting
  or narrowing.
- **The skill count will drop a lot.** 1,128 grammar slugs today. Once
  the not-grammar, topic and duplicate skills are resolved, it's likely
  well under half that, before the one-explanation test is applied to
  the rest.
- **Hungarian C1 has 292 grammar skills at about 9 exercises each**,
  roughly one skill per lesson. After merging, each generic skill will
  have dozens of exercises, so the 6-exercise minimum isn't the issue
  there. A map cell per lesson-topic would be.

## Decided (2026-10-04)

1. **Keep all 37 families.** The four clause families stay separate, so
   no map region gets too large.
2. **`register-style` skills are `kind: grammar`**, in their own family.
   No third kind.
3. **Keep the five display groups** as the skill map's top layer. They're
   stored only on the family list.

The skill-by-skill mapping still needs review: the flags in
[grammar-families-mapping.md](grammar-families-mapping.md) are settled
skill by skill in step 2.
