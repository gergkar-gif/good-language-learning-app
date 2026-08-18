# Troubleshooting Backlog

Captured 2026-08-18 from a single user brain-dump session. Not yet triaged into
priority order — treat this as a raw intake list for the next troubleshooting
pass. Many items are recurring patterns flagged from specific A1/B1 lesson
steps; fixing the underlying generator/template issue will likely resolve many
step-specific entries at once.

## Cross-cutting UX / mechanics

- [ ] Switching language in Journey shouldn't jump back to the Home page. *(explicitly deferred by user — "save this fix for later")*
- [x] Dropdown selector styling is too "app"-y (plain white) — doesn't match the rest of the visual style. **Fixed 2026-08-18**: `.vb-select` (styles/verbs.css) used stale pre-Parlour fallback colors (`#FFFFFF`/`#8FB4BA`/`#2E2A26`); now uses `--bg`/`--border`/`--text` like the rest of the app. Verified live (computed bg is `#F5F1E8`, not white).
- [x] Word/answer selection highlight: currently orange on first click, which reads as "wrong." Change to a deep-blue border for selection; keep green for correct; use orange/red only for an actually incorrect answer. Applies to word-tap exercises and the writing exercise. **Fixed 2026-08-18**: `.lsn-option.selected` (components.css) and `.gd-option.selected` (workshop.css, the Workshop-driller equivalent) now use `--primary` navy border + light navy tint instead of `--accent` orange. `.correct` (green) and `.wrong` (orange/red) were already correct and untouched. Verified live via computed styles.
- [x] Exercises should have one "Check" button at the bottom that switches to "Continue" after the user checks their answer. **Fixed 2026-08-18**: removed every inline per-step "Check" button; the persistent footer button (`#lesson-next-btn`) now reads "Check" while a step is gated/unsolved and calls the step's check function, then flips to "Continue →" (or "Finish Lesson ✓" on the last step) once solved. Applies to multiple-choice, dialogue-complete, listening-choice, dictation, fill-blank, sentence-builder (Reset stays as a separate secondary button), sentence-order, and structured-writing. Matching and SRS steps are unchanged (they were never Check-gated). Verified live end-to-end (select → Check → graded → Continue).
- [ ] Green should consistently indicate a correct/good response app-wide. *(the lesson-exercise path already uses green for `.correct`; not yet audited elsewhere — e.g. Decks/SRS rating buttons, which intentionally use green only for "Easy" per visual-identity-v2 memory)*
- [x] After successfully solving a Spanish exercise, the English translation should always be shown (e.g. "Estudio español porque me gusta" → check → correct → show translation). **Partially fixed 2026-08-18**: plumbing added (`stepState.translation`, shown via `showTranslation()` on solve/reveal) for fill-blank and dictation steps, reading `step.english`/`step.translation` from content. **However — the content data doesn't exist yet**: across all of A1, 0 of 1,560 fill-blank and 0 of 522 dictation exercises carry an `english` field (checked programmatically). Sentence-builder already had this (949/1,076 items) and continues to work via its own existing mechanism. Populating translations for fill-blank/dictation is a real content-generation task (~2,000 items) — not done here.
- [x] Add a "back to previous exercise" button during lessons. **Fixed 2026-08-18**: added `#lesson-back-btn` (← Back) beside the Check/Continue button in the lesson footer; disabled on step 0. Going back re-renders that step fresh (ungraded again) rather than restoring a saved answer — there was no answer-history state to restore from. Verified live (disabled at step 0, enabled and functional mid-lesson).
- [x] Opening the lesson tree/map shouldn't require scrolling to find the current lesson — it should auto-scroll/open directly there. **Fixed 2026-08-18**: `renderCurriculum()` now scrolls the `.is-current` unit-path node or lesson-list row into view (centered) after every render. Verified live on both the unit path and a unit's lesson list by forcing progress deep into a level/unit and confirming the current item lands in the viewport without manual scrolling.
- [x] *(new mid-session request)* Enter key should do both Check and then Continue/Next, not just Check. **Already covered** by the single Check/Continue footer button above — Enter always clicks whatever the footer button currently is, so pressing it once checks the answer and pressing it again (same key, same target) advances to the next step. Verified live for both a fill-blank (type → Enter → Enter) and a multiple-choice (select → Enter → Enter) exercise.
- [ ] End-of-lesson remediation loop: exercises answered wrong on the first try should be re-served at the end of the lesson ("let's review so it sticks"); if missed again, repeat until correct.
- [ ] Grammar screens: audio playback is inconsistently placed. E.g. in a conjugation table you can listen to the pronouns (yo, tú, él) but not the conjugated forms themselves (trabajo, trabajas, trabaja). Sometimes only the English is voiced, not the Spanish. Needs a full audit across all grammar screens.
- [x] Spanish words embedded in grammar explanation prose should be styled in italics, e.g. *adiós*. **Fixed 2026-08-18**: added `escMd()` (engine/lessons.js) — parses `*word*`/`**word**` into `<em>word</em>` — and wired it into grammar `text`/`tip`/`examples`, and multiple-choice/dialogue-complete/listening-choice questions and options, and fill-blank sentences. This also fixes a live bug it uncovered: 11 exercise questions across 5 A1-U3 files (e.g. "¿Qué significa **joven**?") were showing literal double-asterisks because the old `esc()` had no markdown support.
- [ ] No exercise should ever use a proper name as the blank answer (e.g. "Carlos"), since it can't be inferred.
- [ ] Standard lesson progression should be: review (with appropriate clues) → new grammar → lesson vocabulary → exercises. (Currently vocabulary sometimes appears only at the end — see A1 U1 L1-S13 below.)
- [ ] "Tap the sentences in the right order" exercise type is broadly a poor fit for A1–A2 — sentences feel disjointed/arbitrary. Consider replacing this exercise type everywhere it appears (many instances logged below under A1 units 3, 5, 6, 9, 10).
- [ ] Recurring multiple-choice bug: several answer options are all grammatically valid, but only one is accepted. Logged repeatedly under A1 U9–U10; needs a systemic fix (accept-all-valid or redesign the prompt to disambiguate).
- [ ] Recurring fill-blank bug: answer could be literally any adjective/number/noun of the right category (e.g. "Ana es ___" accepting only "joven"), so the exercise is unguessable without a hint. Logged repeatedly across A1 U3–U9; needs either a constraining clue in the prompt or acceptance of any valid word of that category.
- [ ] Workshop → Grammar: some fill-the-gap exercises give away the answer within the exercise text itself.
- [ ] Workshop → Grammar: the "10 random exercises" set takes noticeably long to load.
- [ ] Grammar tips that reference Lingolia should include an actual link to the relevant Lingolia page (currently referenced by name only, e.g. A1 U4 L1 S5).
- [ ] Reading screens: consider a short heads-up before a reading that comprehension questions will follow.
- [ ] Reading screens: consider a short framing blurb along the lines of "it's okay if you don't understand everything — this exposes you to more natural language than crafted test sentences; take what you can for now" to set expectations.
- [ ] Lesson-complete summary card (accuracy %, time taken; later with sound effects) — nice-to-have for later.

## Open design questions (decide before beta)

- [ ] How do we track a user's "known words"? Candidate: auto-add all words from a unit once completed — should the same apply to readings? Needs a real decision before beta.
- [ ] Accent sensitivity in answer-checking (e.g. está vs esta) — currently not enforced; decide whether/when to introduce.
- [ ] Name interchangeability in exercises — e.g. "Carlos presenta a Meg" and "Meg presenta a Carlos" should probably both validate when either could be correct.
- [ ] Can the dictionary/Library lookup handle inflected/reflexive forms like "conocerte"?

## B1 — Readings & structure

- [ ] The "Classics" reading category is mislabeled: most current entries are original texts, not adaptations of classic literature. Reclassify the originals out of "Classics," and separately produce ~15 actual classics — CEFR-leveled adaptations of literary works (e.g. a short-summary version of a Sherlock Holmes story).
- [ ] LATAM track lessons: integrate the reader's word-lookup / add-to-deck functionality directly into lesson body text (e.g. when the text discusses the Maya, users should be able to tap a word to see its meaning or add it to their deck), not just in standalone readings.
- [ ] Consider a "Show English translation" toggle button for B1 informative texts that reveals a full English version.
- [ ] B1 U1 L1 S7: the exercise question contains the answer.
- [ ] B1 U1 L1 S8: correct answer "ocurrió" is not being accepted.

## A1 — Unit-by-unit findings

### Unit 1
- [ ] L1-S3: por favor, gracias, hola, adiós used before being taught.
- [ ] L1-S8: "hasta luego" used before being taught.
- [ ] L1-S10: "bien" used before being taught.
- [ ] L1-S12: nonsensical prompt "….(hola), por favor" — this phrasing pattern recurs elsewhere too.
- [ ] L1-S13: lesson vocabulary currently only appears at this step; should move to the start of the lesson (right after grammar) — this alone would fix several of the above "used before taught" issues.
- [ ] L2-S12: "Soy …" exercise — verify whether it accepts any name.
- [ ] L3-S5: duplicate text shown twice on the same slide (e.g. "Me llamo Carlos" appears twice) — this is a recurring bug, not unit-specific.

### Unit 2
- [ ] 2.1: "amigo"/"amiga" used before being taught.
- [ ] S21: writing-exercise prompt "identify a male person" is awkwardly phrased.
- [ ] L5(?)-S19: reading references photos that aren't actually shown.

### Unit 3
- [ ] L1-S22: "name one male/female friend" prompt is awkward, needs rephrasing.
- [ ] L3(?)-S4: "which form of ser is used in 'de dónde eres'" — bad exercise, the answer ("eres") is embedded in the question.
- [ ] L3-S13: "Carlos es simpát…" — answer is currently "simpático" but should just be the completion "ico".
- [ ] L4-S13: "Es un chico…" answer "alto" — could be any adjective, exercise is unguessable.
- [ ] The reading duplicates the previous unit's reading; the earlier unit's reading was already too advanced for that point, and even here it's still a bit too complex for Unit 3.
- [ ] S19: "Son unos amigos…." answer "simpáticos" — same "could be any adjective" problem, needs a hint at minimum.
- [ ] Review-S17: "tap the sentences in the right order" exercise doesn't fit this context.

### Unit 4, Lesson 1
- [ ] S3: answer should also accept "cómo te llamas".
- [ ] S5: grammar explanation / example differentiation is good, but the tip references Lingolia without linking to the actual page — apply the Lingolia-link fix here too.
- [ ] S7: "joven" is incorrectly wrapped in asterisks — check for this formatting bug elsewhere too.
- [ ] S9: "Ana es ….." answer "joven" — could be any adjective.
- [ ] S10: "Meg es simpátic…" — answer should just be the completion "a".

### Unit 4, Lesson 2
- [ ] S3: review question asks the user to recall reading details — review sections should always test grammar, never reading recall.
- [ ] S9: "Ana es trabaja…" — answer "trabajadora" should just be the completion "ora"; this pattern (giving the full word instead of the completion) recurs in multiple places and should be fixed globally.

### Unit 4, Lesson 3
- [ ] S3: review again wants reading recall — replace this exercise type wherever it appears.
- [ ] S5: grammar explanation presents singular/plural as if they were a vocab translation pair, which is confusing.

### Unit 4, Lesson 4
- [ ] S22: writing-exercise prompt "identify a woman and describe her" is wonky; consider rephrasing to something like "Say that Ana is a tall woman."

### Unit 4, Lesson 5
- [ ] S9: "Carlos es un hombre alto y ….." answer "serio" — could be any adjective.
- [ ] S10: same issue, recurring.
- [ ] S17: reading is a third repeat of the same text — every unit needs a distinct reading.

### Unit 5
- [ ] L2: uses "este"/"esta" without explaining them — double-check whether these were introduced earlier.
- [ ] L5-S2: sentence-ordering exercise doesn't make sense — ties into the broader "replace all sentence-ordering exercises" item above.
- [ ] Consolidation-S15: sentence-ordering exercise is nonsensical.

### Unit 6, Lesson 1
- [ ] S10: "Yo …. en casa" answer "trabajo" — could be anything.
- [ ] S15: "Yo … por la tarde" with options trabajo/camino/estudio — only "camino" is marked correct with no clear reason why. This recurs throughout the unit (e.g. "¿Qué … en casa?" answer "comes") — needs a unit-wide pass.

### Unit 6, Lesson 6
- [ ] S13: "sentences in the right order" exercise is really a "build the sentence" exercise — same issue appears in the Consolidation section (S15). Review and fix everywhere this pattern occurs.

### Unit 7
- [ ] "Identify a male person" awkward phrasing recurs — writing-exercise prompts need clearer phrasing generally.
- [ ] Reading: Meg and Carlos are shown living together despite having just met (also implied earlier via a video call) — they aren't dating yet at this point in the story; should be revised to something like one of them visiting the other's apartment.
- [ ] Consolidation-S16: "which is correct?" — "tienen dos hermanos" should also be marked correct, not only "tengo dos hermanos".

### Unit 8
- [ ] Unclear whether "quiero"/"necesito" are actually explained before use — they're covered later in the same unit. Consider swapping the order of Lessons 1 and 3 (to be discussed after further analysis).
- [ ] L2-S9: "Quiero … manzanas" answer "dos" — could be anything.

### Unit 9, Lesson 1
- [ ] S18: "which is correct?" — all three options are grammatically correct, but only "tomo leche" is accepted.

### Unit 9, Lesson 2
- [ ] S18: same "which is correct" problem as above.

### Unit 9, Lesson 3
- [ ] Querer was already taught earlier — the lesson should acknowledge this explicitly ("we've seen this before, now let's use it in a café context") rather than reintroducing it cold.
- [ ] S17: same "which is correct" problem, all three options valid.

### Unit 9, Lesson 4
- [ ] S2: sentence-ordering exercise "Carlos presenta a Meg. Meg es su amiga" produces a nonsensical result.

### Unit 9, Lesson 5
- [ ] S9: "what comes first?" exercise is weak, needs changing.
- [ ] Vocabulary: "rico" is glossed only as "rich" — it can also mean "delicious," and that sense is missing.
- [ ] S18: "where does the café encounter take place?" — the question contains its own answer ("in a café").
- [ ] S20: "what does the customer eat?" is marked as "a sandwich," but both characters actually eat tacos.
- [ ] S25: two duplicate "sí, ahora mismo" reply options.

### Unit 9, Lesson ~8.5
- [ ] "Aquí está mi …" answer "grupo" — no way for the user to infer this answer.
- [ ] S11: "Quiero … tomates" answer "tres" — arbitrary, unguessable.
- [ ] S12: same problem, "Necesito … kilo de arroz".
- [ ] S13: build-the-sentence exercise — the relative order of "dos manzanas" and "una botella de agua" shouldn't be enforced as a strict sequence.

### Unit 9, Consolidation
- [ ] S8: "Necesito … leche" multiple-choice — exercise is broken (the intended correct answer "leche" doesn't work with the structure).
- [ ] S17: all three answer options are correct.

### Unit 10, Lesson 1
- [ ] S10: sentence-ordering exercise doesn't work well.
- [ ] "Which sentence correctly connects the ideas…" is a poor review-exercise format.
- [ ] Users are asked to state their age in an exercise but have only been taught numbers up to 3 at that point.
- [ ] Unit 10 overall needs a full review: too much writing, too little active practice. Prioritize teaching how to conjugate "saber" and basic connectors (y, con, sin, pero) over incidental vocabulary like "vela" and "globo".
