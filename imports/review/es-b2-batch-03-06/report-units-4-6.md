# Report: es-latam B2 Unit 4 (influence-will-value-judgments) and Unit 6 (emotional-reactions-affective-stance)

Nothing is committed. Both units were rewritten from scratch, Unit 4 first and then Unit 6. Every screen, lesson title, goal and checklist is now in English, and every question stem is in English. I built the JSON with scratch scripts, so each file keeps the existing `json.dumps(indent=2)` format. The files are in `/home/user/parlour-read-b`:
- screens in `content/es-latam/grammar/b2/b2-04-0{1..5}-a-gr.json` and `b2-06-0{1..5}-a-gr.json`
- vocabulary in `content/es-latam/vocabulary/b2/b2-04-0{1..5}-voc.json` and `b2-06-0{1..5}-voc.json`
- items in `content/es-latam/exercises/b2/b2-04-*-ex.json` and `b2-06-*-ex.json`, consolidation included
- lessons in `content/es-latam/lessons/b2/b2-04-*.json` and `b2-06-*.json`
- texts in `content/es-latam/stories/classics/b2/b2-04.json` and `b2-06.json`
- challenges in `/home/user/parlour-read-b/challenges-influence-will-value-judgments.json` and `/home/user/parlour-read-b/challenges-emotional-reactions-affective-stance.json`

`build-manifest.py` also regenerated `curriculum.json`, `word-lesson-index.json` and the decks and manifest files. The written report file only holds a pointer, because the full report is this message.

## Check counts

| Check | Unit 4 before | Unit 4 after | Unit 6 before | Unit 6 after |
|---|---|---|---|---|
| check-content errors | 3 | 0 | 8 | 0 |
| check-content suspects | 11 | 0 | 17 | 0 |
| unmet words | about 110 | 0 | 101 | 0 |

- **Unmet words:** the "after" counts also include the challenge targets. I tested them by merging my two challenge files into `content/es-latam/curriculum/challenges.json` for one run and then restored that file, so it is unchanged.
- **Other checks:** `check_unit_refs.py --labels --bare` reports 0 recaps for both units. `validate-content.py --changed` passes (es-latam 47 passed, 0 failed). All six lessons of each unit render with no `!!`.
- **Residual error:** none. The brief's "expected leftover" never appeared; both units show 0 errors.

## Unit 4: what changed per lesson

Every lesson has the same six items: `ex01` matching, `ex02` multiple-choice, `ex03` fill-blank, `ex04` sentence-builder, `ex05` dialogue, `ex06` dictation. Lesson titles, goals and checklists are rewritten in English. Lessons 02–05 got an `srs` section and a `checklist`, copied from the shape of `b2-02-01`.

- **b2-04-01, "Asking, Telling and Demanding".**
  - The screen recaps *aconsejar que* (B1 Unit 4) and *prohibir* (B1 Unit 38). It adds a gentle-to-strong table (*permitir, prohibir, impedir, insistir en que, ordenar, exigir*) and the present versus imperfect subjunctive after a past verb.
  - Vocabulary is *exigir* (kept, because it is in `requiredLemmas`), *insistir en*, *obligar a* and *el reglamento*.
  - Items are all new. `ex03` accepts `answers` [entregáramos, entregásemos] and is tagged `correlacion-temporal-subjuntivo`.
  - The intro text of the unit is rewritten in plain English.
- **b2-04-02, "Saying What Is Fair, Normal or Strange".**
  - It recaps A2 Unit 27 and B1 Unit 37 (*haya*). It adds *conviene, es justo/injusto/razonable, es lógico/normal/comprensible, es inaceptable/ridículo, es raro/increíble*.
  - The tip contrasts a fact (indicative) with a judgment (subjunctive).
  - Vocabulary is *razonable, inaceptable, ridículo, comprensible*.
  - `ex03` accepts estuviéramos/estuviésemos.
- **b2-04-03, "Reacting to News".** Short, as you asked. It recaps A2 Unit 27 and adds only *me alegra que*, *lamento que* and *me sorprende que*, plus *haya* for finished events. Vocabulary is *alegrar, lamentar, sorprender, agradecer*.
- **b2-04-04, "One Person or Two?".** This teaches `infinitive-vs-que-subjunctive`. It recaps *querer* and *preferir* from A2 Unit 27 (see "For the user" below), then covers same subject versus different subject for influence, value judgments and feelings. It adds one tip: with *permitir, prohibir, aconsejar, pedir* plus *me/te/le/nos/les* both patterns are correct. Vocabulary is *pretender* (glossed as a false friend of "to pretend"), *intentar, negarse a, renunciar a*.
- **b2-04-05, "Polite and Formal Recommendations".** Plain B2 only: *se recomienda que, se sugiere que, sería conveniente que, convendría que*. It recaps impersonal *se* (B1 Unit 6), *convendría* (B1 Unit 4) and the conditional for advice (A2 Unit 26). Vocabulary is *conveniente, la sugerencia, el visitante, el aviso*. All the diplomacy vocabulary (*dirimir, dictamen, concordia*) is gone.
- **b2-04-consolidation.**
  - The text was replaced (claims below).
  - It now has 10 items: two reading items (`ex02`, `ex09`), a sentence-order item, structured writing, and grammar items across the unit.
  - The old length-giveaway on `ex02` is gone.
  - The checklist is rewritten.

Across the unit:
- Wrong options differ from the right one by one fault.
- Where a wrong option is a real form of another skill I added `distractor_skills`: `present-tense`, `imperfect`, `futuro-simple`, `preterito-perfecto`, `condicional-regular`, `subjuntivo-deseos`, `subjunctive-emotion`.
- Fill-blanks blank a whole word and carry `english`.
- No hint gives away the answer.
- No multiple-choice item has `hint` or `english`.
- The dialogue wrong options are the same reply with one form fault, not unrelated sentences.

## Unit 6: what changed per lesson

- **b2-06-01, "More Verbs That Work Like Gustar".**
  - The screen recaps *gustar* (A1 Unit 22), *molestar* (A2 Unit 27) and *sorprender* (B2 Unit 4). It adds *molestar/fastidiar, preocupar/asustar, encantar/entristecer* with *que* + subjunctive.
  - It explains that the verb stays singular, with the plural-noun exception, and that the same person gets an infinitive.
  - Vocabulary is *preocupar, asustar, fastidiar, entristecer*.
  - The unit intro is rewritten.
- **b2-06-02, "Sorry, Sad or Afraid".**
  - It covers *sentir, lamentar, temer que*, with the person who feels as the subject, recapping *Quiero comer* / *Quiero que comas* from B2 Unit 4.
  - It adds *sentir que* "to be sorry" (subjunctive) versus "to feel that" (indicative), and a condolence tip.
  - Vocabulary is *temer, consolar, el pésame, apenado*.
  - `ex03` is `correlacion-temporal-subjuntivo`, with `answers` llegara/llegase.
- **b2-06-03, "Reacting with Exclamations".**
  - It covers *¡Qué pena que…!, ¡Qué lástima que…!, ¡Qué bien/bueno que…!, ¡Qué horrible/barbaridad que…!*.
  - The tip says *¡Menos mal que…!* takes the indicative, because it expresses relief that something good did happen.
  - Vocabulary is *menos mal, la barbaridad, el susto, horrible*.
- **b2-06-04, "The Fact That…".**
  - This teaches `el-hecho-de-que-subjuntivo`. It covers fact first and comment after, with the comment agreeing with singular *el hecho*, *no significa que*, and the imperfect subjunctive after a past verb.
  - It explains why the subjunctive is used and mentions that you may read the indicative when a writer stresses the fact.
  - I avoided indicative distractors in its items, because the indicative is sometimes acceptable there. The wrong options use *el hecho que* without *de*, and plural *molestan*.
  - Vocabulary is *el hecho, el retraso, significar, disculpar*.
- **b2-06-05.** The title "vehemencia ética … manifiesto social" is gone; it is now "Reacting to News and Social Problems". The point is fact first (indicative), reaction second (subjunctive), plus the rule that no *que* is needed after a noun (*Me preocupa la contaminación* / *Me preocupan los precios*). Vocabulary is *la desigualdad, la pobreza, el desempleo, la contaminación*.
- **b2-06-consolidation.** New text (claims below), 10 items, new checklist. *como si* is used nowhere.

Intros in b2-06-02 to b2-06-04 are shortened and rewritten in English. Lesson 05 has none, as before.

## Texts: every factual claim

**Unit 4, `b2-04.json`, "Carlos Fuentes y las tres voces de Artemio Cruz": 326 words, 6 paragraphs.**
- Fuentes was a Mexican novelist and essayist: certain (your list).
- He wrote novels and also essays, "textos en los que un autor piensa sobre un tema": certain. This is a gloss of the word "ensayo", not a fact.
- Born 1928, died 2012 in Mexico City: certain (your list). The birthplace is not named.
- He was the son of a diplomat and grew up in several countries: certain (your list).
- The novel was published in 1962: certain.
- The protagonist is an old, rich and powerful man who is dying. He remembers his life: the years of the Revolution, then the power he had later. "Es una novela sobre una vida larga y sobre el poder": certain (your list), and the last line is an interpretation drawn from it.
- It does not tell the life in order, and it jumps in time: certain.
- It moves between yo, tú and él, all of them Artemio Cruz: certain.
- "Fuentes quería que el lector siguiera la vida … desde tres lados y no en línea recta": medium. It is an inference about intent from the structure, and the brief asked for the "Fuentes quería que el lector…" pattern. Soften or cut it if you think it is beyond the list.
- "Por eso el lector no siempre sabe en qué momento de la vida está": medium. This is a reasonable consequence of the time jumps, not a stated fact.
- Reading advice (*es importante que, conviene que, es mejor que, Quien quiere entender…*): this is advice, not fact.
- "Muchos lectores prefieren que una historia vaya de principio a fin": medium. It is a general remark about readers, not about Fuentes. Cut it if you want strictly nothing beyond the list.
- No scene, dialogue or quotation. The pluperfect subjunctive is not used.

**Unit 6, `b2-06.json`, "Eduardo Galeano y Las venas abiertas de América Latina": 322 words, 6 paragraphs.**
- Galeano was a Uruguayan journalist and writer, born in Montevideo in 1940 and died in the same city in 2015: certain (your list).
- The book was published in 1971: certain.
- "Según Galeano, este libro cuenta la historia de la explotación económica de América Latina", starting with the Spanish and Portuguese conquest: certain, attributed to Galeano. The text names silver, sugar, rubber, oil "y otras riquezas que salieron de la región": certain (your list).
- "Es una historia larga, que empieza hace siglos": certain (the conquest was a long time ago).
- "Es la visión de Galeano … otros autores pueden pensar de otra manera": a caution, not a fact. It is safe.
- Galeano was a journalist and the book has a journalist's style, written for a wide public, "no solo para los especialistas": certain apart from the "no solo" gloss, which is low-risk.
- "Es posible que a un lector nuevo le sorprenda que … se lea casi como un reportaje": hypothetical, not a claim about real readers.
- In the 1970s several military dictatorships in South America banned it: certain. The sentence "El hecho de que lo prohibieran no cambia lo que dice el libro" is neutral.
- First-person opinions in the text voice (*A mí me parece una pena… nos molesta… Me encanta… me preocupa…*): opinions of the narrator, not claims about Galeano or readers.
- "El hecho de que el libro presente esa visión no significa que sea la única explicación posible": a hedge.
- No quotation and no near-quotation. Galeano's feelings are not claimed: I dropped *Le indignaba que…*, because that would be mind-reading.

## Spanish I am unsure of (marked as unsure)

- (unsure) `b2-04-04.ex02` wrong option *Me alegra de estar aquí*: non-standard (the standard form is *Me alegro de estar aquí*), so it is wrong, but a reviewer may want a different distractor.
- (unsure) `b2-06-02.ex02` wrong option *Siento de que estés enfermo*: an intentional *dequeísmo* error.
- (unsure) `b2-04-04` example *Mi hermano pretende que le prestemos el carro* ("expects us to lend him"): correct but slightly marked.
- (unsure) 06-03 tip: *¡Menos mal que…!* takes the indicative. I am fairly confident, but I did not source it.
- (unsure) 06-04 tip: the indicative after *el hecho de que* "may be read when the writer stresses the fact". I hedged it ("at B2 use the subjunctive").
- `b2-04-05` *Convendría que revisáramos…* and *Sería conveniente que… + imperfect subjunctive* are standard.

## For the user

- **`infinitive-vs-que-subjunctive` is not fully new in 04-04.** A2 Unit 27 (`subjuntivo-deseos`, the screen "The Two-Subject Rule with Wishes") already teaches the same rule for wishes: *Quiero comer* / *Quiero que comas*. The 04-04 screen recaps it honestly ("You know *querer* and *preferir* from A2 Unit 27") and extends it to influence, judgments and feelings, with the *permitir/prohibir + me* exception. If you want this skill to be "new", the A2 screen needs to change.
- **`el-hecho-de-que-subjuntivo`** is taught only in 06-04 for the core track. A hidden-track screen, `b1-revolucionmexicana-03-el-hecho-de-que`, also exists; I did not treat it as met.
- **No listed skill covers *¡Menos mal que…!* + indicative.** The related items (06-03 `ex06` dictation and the 06-03 tip) are tagged `subjunctive-emotion`, which is not a perfect fit.
- **Tags:** items on the correlation of tenses after a past main verb are tagged `correlacion-temporal-subjuntivo` (04-01 `ex03`, 04-02 `ex03`, 06-02 `ex03`). I did not run `lock_tags.py`.
- **Two wrong options of the same mood fault.** In a few multiple-choice items both wrong options are the indicative (or a different non-subjunctive tense) in different tenses, for example 04-01 `ex05` and 04-03 `ex02`. The mood contrast has few single-fault alternatives. If you read this as "two options failing the same way", say so and I will swap one for a morphology error.
- **Challenges:** the old generic `b2-04-*` and `b2-06-*` entries in `content/es-latam/curriculum/challenges.json` are untouched; merge mine over them. Scenario facts are minimal: Carlos works in an office in Budapest, Meg is a student in Budapest. The only things I invented are small situations (noise in the office, a library closing on Saturdays, a cinema closing, a friend who is often late, a dinner Meg cannot attend, visitors coming to the office). All of them are marked in the scenario text.
- **Nothing I could not fix.**
- **Skills used before their screen:** none flagged by the checks. B1 Unit 37 (*haya*) and B1 Unit 38 (imperfect subjunctive after a past verb) are used as known.
