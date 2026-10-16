# Reader report: Spanish A1 Unit 1 `greetings-introductions` (es-es & es-latam, ROADMAP 153)

## 1. Found by reading

- `a1-01-01.ex05`: `"question": "Someone says \"Hola\". Which response is appropriate?"`, `"options": ["Hola", "Adiós", "Hasta mañana"]` — `answer-in-prompt` (`Hola` in both prompt and right option) and two wrong options failing the same way (both farewells). → `"question": "Someone greets you in the morning with \"Hola\". Which response is appropriate?"`, `"options": ["Buenos días", "Buenas noches", "Hasta mañana"]` (wrong time of day vs farewell).
- `a1-01-01.ex09`: `"question": "It is 8 p.m. Which greeting fits best?"`, `"options": ["Buenas noches", "Buenos días", "Buenas tardes"]` — in Spain (`es-es`), 8 p.m. is often still *Buenas tardes* (sunset/dinner time), leaving two plausible answers. → `"It is 11 p.m. Which greeting fits best?"`.
- `a1-01-01.ex10`: `"sentence": "___, Carlos."`, `"hint": "works any time of day"`, `"answer": "Hola"` — *adiós* and *gracias* also work any time of day. → `"hint": "general greeting"`.
- `a1-01-01.ex11`: `Ana: Hola. / Carlos: _____`, `"options": ["Hola.", "Adiós.", "Buenas noches."]` — with no time of day given, `"Buenas noches."` is also a valid greeting reply to `"Hola."` (as `a1-01-01.ex16` teaches). → `"options": ["Hola.", "Adiós.", "Por favor."]`.
- `a1-01-02.ex01` & `a1-01-02.ex08`: `["nombre", "name"]` and `["también", "also"]` appeared in both matching exercises of `a1-01-02` while `chico`, `chica` and `señora` in `a1-01-02-voc.json` went unused (`vocab-unused`). → `ex01` pairs `soy`, `yo`, `chico`, `chica`; `ex08` pairs `me llamo`, `nombre`, `persona`, `señora`.
- `a1-01-02.ex02`: `"options": ["Soy Carlos.", "Eres Carlos.", "Carlos soy."]` — *eres* is used before `a1-01-04-origin-gr` teaches it, and `"Carlos soy."` is grammatical inverted word order. → `"options": ["Soy Carlos.", "Yo Carlos.", "Me soy Carlos."]`.
- `a1-01-02.ex06`: `"question": "Which sentence is a simple way to identify yourself?"`, `"options": ["Soy Meg.", "Meg soy yo.", "Yo Meg."]` — `"Meg soy yo."` is grammatical in Spanish ("I am the one who is Meg"). → `"question": "Which sentence means \"I am a student\"?"`, `"options": ["Soy estudiante.", "Yo estudiante.", "Me llamo estudiante."]`.
- `a1-01-02.ex07` & `a1-01-02.ex10`: together with `a1-01-02.ex03` (`"Yo ___ Carlos."`), three fill-blanks in one lesson had the identical shape `"Yo ___ <Name>."` (`"Yo ___ Ana."`, `"Yo ___ Meg."`, Rule 2.7). → `ex07`: `"Yo también ___ estudiante."` (`"I am also a student."`); `ex10`: `"Buenas tardes, ___ Meg."` (`"Good afternoon, I am Meg."`).
- `a1-01-02.ex09`: `"question": "Which form of ser should you use for yourself?"`, `"options": ["soy", "es", "son"]` — *es* and *son* are not taught until Unit 2 (`a1-02-02-pronouns-ser-gr`). → `"question": "Which sentence correctly uses \"yo\" and \"soy\"?"`, `"options": ["Yo soy Meg.", "Yo también Meg.", "Me soy Meg."]`.
- `a1-01-02.ex11`: `Carlos: Hola. Soy Carlos. / Meg: _____`, `"options": ["Hola. Soy Meg.", "Buenas noches.", "Adiós, Carlos."]` — `"Buenas noches."` can greet Carlos if it is evening. → `"options": ["Hola. Soy Meg.", "Por favor, Carlos.", "Adiós, Carlos."]`.
- `a1-01-02.ex12`: `"options": ["Hola. Soy Carlos.", "Hasta mañana.", "Gracias."]` — `length-giveaway` (17 vs 13 chars). → `"options": ["Hola. Soy Carlos.", "Hasta mañana, Ana.", "Por favor, señora Ana."]`.
- `a1-01-02.ex13`: `Meg: Soy Meg. / Carlos: Yo soy Carlos. _____`, `"options": ["También soy estudiante.", "Buenos días.", "Hasta luego."]` — `length-giveaway` (23 vs 12 chars), and Meg's turn did not mention being a student so Carlos's *También soy estudiante* had no antecedent. → `Meg: "Soy Meg. Soy estudiante."`, `"options": ["También soy estudiante.", "Yo también me llamo Meg.", "Adiós, hasta mañana."]`.
- `a1-01-03.ex01` & `a1-01-03.ex07`: `["¿y tú?", "and you?"]` was duplicated in both matching exercises of `a1-01-03` while `mucho` and `conocer` in `a1-01-03-voc.json` went unused (`vocab-unused`). → `ex01` replaces `¿y tú?` with `["mucho", "much / a lot"]`; `ex07` replaces `["te", "you"]` (already drilled in `ex03`, `ex06`, `ex10`) with `["conocer", "to meet / know"]`.
- `a1-01-03.ex02`: `"options": ["¿Cómo te llamas?", "¿Quién soy?", "¿Qué es?"]` — `length-giveaway` (16 vs 11 chars) and `"¿Qué es?"` uses *es* (Unit 2). → `"options": ["¿Cómo te llamas?", "¿Quién te llamas?", "¿Qué te llamas?"]`.
- `a1-01-03.ex13`: `Ana: Hola. ¿Cómo te llamas? / Meg: Me llamo Meg. _____`, `"options": ["¿Y tú?", "Buenos días.", "Por favor."]` — `tell-punctuation` (`first-letter case`): only the right option was a question starting with `¿`. → `"options": ["¿Y tú?", "¿Quién soy?", "¿Cómo me llamo?"]`.
- `a1-01-04.ex10`: `"question": "Which form of ser goes with tú when asking where someone is from?"`, `"options": ["eres", "soy", "es"]` — *es* is not taught until Unit 2. → `"options": ["eres", "soy", "llamas"]`.
- `a1-01-04.ex13`: `Ana: ¿De dónde eres? / Carlos: Soy de Hungría. / Ana: _____`, `"options": ["Yo soy de Vietnam.", "Eres de Vietnam.", "Buenas noches."]` — `"Buenas noches."` fails by meaning alone on an item tagged `ser`. → `"options": ["Yo soy de Vietnam.", "Eres de Vietnam.", "Yo soy Vietnam."]` (missing *de*).
- `a1-01-05.ex05`: `conocer` and `primero` in `a1-01-05-voc.json` were unused (`vocab-unused`). → added `["conocer", "to meet / know"]` and `["primero", "first"]` to `ex05` (6 pairs).
- `a1-01-05.ex07` & `a1-01-05.ex08`: repeated the exact sentence-builders of `a1-01-03.ex06` (`¿Cómo te llamas?`) and `a1-01-04.ex06` (`Soy de Hungría.`) with shuffled tile order, while `también` in `a1-01-05-voc.json` was unused (`vocab-unused`). → `ex07`: `["Hola,", "me", "llamo", "Meg."]`; `ex08`: `["Yo", "también", "soy", "de", "España."]`.
- `a1-01-05.ex09`: `"options": ["South Africa.", "Hungary.", "Spain."]` — `length-giveaway` (13 vs 8 chars). → `"options": ["She is from South Africa.", "She is from Hungary.", "She is from Vietnam."]`.
- `a1-01-05.ex14`: `"options": ["Mucho gusto.", "Adiós.", "Hasta mañana."]` — both wrong options fail the same way (both are farewells, Rule 2.2). → `"options": ["Mucho gusto.", "Por favor.", "Hasta mañana."]`.
- `a1-01-consolidation.ex01`: `"pairs": [["Hola", "hello"], ["¿Cómo te llamas?", "what's your name?"], ["¿De dónde eres?", "where are you from?"], ["Mucho gusto", "nice to meet you"]]` — inconsistent casing (`Hola` and `Mucho gusto` capitalised without periods; English questions lowercase). → `[["hola", "hello"], ["¿Cómo te llamas?", "What's your name?"], ["¿De dónde eres?", "Where are you from?"], ["mucho gusto", "nice to meet you"]]`.
- `a1-01-consolidation.ex03`: `"options": ["Soy Carlos.", "Es Carlos.", "Eres Carlos."]` — *es* is not taught in Unit 1 (Unit 2). → `"options": ["Soy Carlos.", "Yo Carlos.", "Eres Carlos."]`.
- `a1-01-consolidation.ex05`: `"question": "Which question asks someone where they are from?"` — `reported-question` suspect. → `"question": "How do you ask someone \"Where are you from?\""`.
- `a1-01-consolidation.ex06`: `"sentence": "Soy ___ Vietnam."` — `consolidation-copy` of `a1-01-04.ex03`. → `"sentence": "Yo soy ___ España."`, `"english": "I am from Spain."`.
- `a1-01-consolidation.ex07` & `a1-01-consolidation.ex08`: repeated the exact sentence-builders of `a1-01-03.ex06` (`¿Cómo te llamas?`) and `a1-01-04.ex06` (`Soy de Hungría.`). → `ex07`: `["Hola,", "¿cómo", "te", "llamas?"]`; `ex08`: `["Yo", "soy", "de", "Vietnam."]`.
- `a1-01-consolidation.ex09`: `"question": "Which reply fits \"Hola\"?"`, `"options": ["Hola.", "Soy de Vietnam.", "¿Cómo te llamas?"]` — `answer-in-prompt` (`Hola` in prompt and right option), and `"¿Cómo te llamas?"` could plausibly follow a greeting. → `"question": "Someone greets you in the morning with \"Hola.\" Which reply fits?"`, `"options": ["Buenos días.", "Soy de Vietnam.", "Hasta mañana."]`.

## 2. Metadata

- No `teaches` or `distractor_skills` tags needed changing; all 106 exercises in `es-es` and `es-latam` already match `docs/unit-agent-rules.md` § 3 and `indexes/tags.lock.json`.

## 3. Goals, checklists, challenges

- Goals and checklists across `a1-01-01` … `a1-01-05` and `a1-01-consolidation` are distinct per lesson, have no comma splices or voice defects, and match what each lesson practises.
- Added six curated challenges (`a1-01-01`, `a1-01-02`, `a1-01-03`, `a1-01-04`, `a1-01-05`, `a1-01-consolidation`) to `content/es-es/curriculum/challenges.json` and `content/es-latam/curriculum/challenges.json` via `scripts/add_challenges.py` from `imports/review/es-a1-batch-01/challenges-greetings-introductions.json`. Each uses Carlos and Meg in the language-exchange setting, cues without Spanish words, 3-sentence targets using only words met by that lesson, and `canDo` copied verbatim from the lesson's first checklist line.

## 4. Doubtful

- `content/es-es/stories/original/a1/a1-01.json` (and `es-latam`):
  - Paragraph 2 (`Meg`): `"¡Hola! Buenos días, señor. Buenas tardes si ya es tarde aquí."` — stiff phrasing written to include both *buenos días* and *buenas tardes*. Left untouched because the story file carries pre-timed audio narration segments (`narration.segments`, `durationSeconds: 84.47`).
  - Paragraphs 11–12 (`Meg` / `Carlos`): `"¿Quién eres en Hanói, Carlos? ¿Eres chico estudiante o trabajas?"` / `"Soy un chico estudiante. Ahora estudio español. ¿Y tú, chica?"` — unnatural *chico estudiante* and vocative *chica* between strangers who just used *señor*, written to force `chico` and `chica` into the story. Left untouched for the same audio-timing reason; flagged for reviewer decision.
  - The 3 embedded `pedagogical.comprehensionQuestions` in `a1-01.json` differ in wording between `es-es` and `es-latam` and do not carry `questionEnglish` / `optionsEnglish` (note: lesson `a1-01-05` uses `ex09`–`ex11` in `a1-01-05-ex.json` for its Reading section, which are in English).

## 5. Not fixed, and why

- None: 0 errors and 0 suspects remain in both `es-es` and `es-latam` (`imports/review/es-a1-batch-01/accept.json` is `[]`).
- `audit-reader-coverage.js es-es --story a1-01 --top 0` reported 0 missing words, 0 literal compound guesses, and 0 lookup errors.

## 6. Numbers

- **Before (`es-es`):** 4 errors (`length-giveaway`: `a1-01-02.ex12`, `a1-01-02.ex13`, `a1-01-03.ex02`, `a1-01-05.ex09`), 13 suspects (`answer-in-prompt` ×2, `tell-punctuation` ×1, `reported-question` ×1, `consolidation-copy` ×1, `vocab-unused` ×8).
- **Before (`es-latam`):** 4 errors, 13 suspects (identical).
- **After (`es-es`):** 0 errors, 0 suspects.
- **After (`es-latam`):** 0 errors, 0 suspects.
- **Fixes applied in `es-es`:** 32 (4 auto, 28 review, 0 rejected).
- **Fixes mirrored to `es-latam`:** 32 (4 auto, 28 review, 0 unmatched).
- **Fixes written by hand for `es-latam`:** 0 (all 6 exercise files were byte-for-byte identical; the 3 differing unit files — `a1-01-01-sounds-gr.json` and `stories/original/a1/a1-01.json` — had no exercise diffs).
- **Words added to vocabulary lists:** 0 (0 `unmet-word` findings).
- **Start time:** 2026-10-16 09:08 +07:00
- **Finish time:** 2026-10-16 09:51 +07:00
