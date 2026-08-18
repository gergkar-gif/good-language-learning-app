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
- [x] Grammar screens: audio playback is inconsistently placed. E.g. in a conjugation table you can listen to the pronouns (yo, tú, él) but not the conjugated forms themselves (trabajo, trabajas, trabaja). Sometimes only the English is voiced, not the Spanish. **Fixed 2026-08-18**: the shared `table()` renderer (engine/lessons.js) now also adds a listen button on column 2 whenever column 1 is a bare subject pronoun (or slash-combination of them), which is how every conjugation paradigm table is shaped — so the conjugated form itself is now audible, not just the pronoun. Sentence/translation reference tables (column 1 = a full Spanish sentence) are unaffected. Verified live on `trabajar`'s paradigm table and a non-conjugation reference table side by side. The "only English is voiced, not Spanish" half of this item is not yet separately audited.
- [x] Spanish words embedded in grammar explanation prose should be styled in italics, e.g. *adiós*. **Fixed 2026-08-18**: added `escMd()` (engine/lessons.js) — parses `*word*`/`**word**` into `<em>word</em>` — and wired it into grammar `text`/`tip`/`examples`, and multiple-choice/dialogue-complete/listening-choice questions and options, and fill-blank sentences. This also fixes a live bug it uncovered: 11 exercise questions across 5 A1-U3 files (e.g. "¿Qué significa **joven**?") were showing literal double-asterisks because the old `esc()` had no markdown support.
- [ ] No exercise should ever use a proper name as the blank answer (e.g. "Carlos"), since it can't be inferred. *(One confirmed instance — "Soy ___." in A1 U1 L2 — fixed below by accepting multiple names. Not swept exhaustively across the rest of A1.)*
- [x] Standard lesson progression should be: review (with appropriate clues) → new grammar → lesson vocabulary → exercises. **Fixed 2026-08-18**: found that all 100 A1 lessons with both a grammar and a vocabulary section had vocabulary sitting *after* the first block of practice exercises (order was goal, recycle, grammar, exercise-group, vocabulary, ...). Reordered every one so vocabulary comes right after grammar, before any exercises — this is the root cause behind most of the "word used before it's taught" reports throughout A1, not just A1 U1 L1-S13. Verified live.
- [x] "Tap the sentences in the right order" exercise type is broadly a poor fit for A1–A2 — sentences feel disjointed/arbitrary. **Fixed 2026-08-18**: converted all 23 A1 `sentence-order` exercises to multiple-choice ("which sentence starts this exchange?"), derived entirely from each item's existing sentences/solution data — no new authoring needed. Left B1's `sentence-order` exercises alone (historical-sequencing questions, not reported broken, still a live-and-used exercise type in the engine).
- [x] Recurring multiple-choice bug: several answer options are all grammatically valid, but only one is accepted. **Partially fixed 2026-08-18**: found and fixed the 4 instances in A1 U9 (café unit) — "Which is correct?" among tomo/tomas/toma-style person forms, and "tengo dos hermanos" vs. the also-valid "tienen dos hermanos" — by rewording each question to translate a specific English prompt, which disambiguates the intended subject without changing the options. Did not do an exhaustive sweep of A1 U10 or elsewhere for the same pattern.
- [x] Recurring fill-blank bug: answer could be literally any adjective/number/noun of the right category (e.g. "Ana es ___" accepting only "joven"), so the exercise is unguessable without a hint. **Fixed 2026-08-18** for the pattern actually found: 9 items across A1 U3/U3c/U8 where a ser+adjective or "quiero + number" blank had exactly one hardcoded answer with zero disambiguating context. Extended fill-blank to accept a curated list of valid answers (`stepState.acceptable` in engine/lessons.js) instead of one pinned string, keeping any grammar-agreement check (gender/number) intact. This was a targeted scan for one specific shape of the problem, not an exhaustive audit of every fill-blank/MC in A1.
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

- [x] The "Classics" reading category is mislabeled: most current entries are original texts, not adaptations of classic literature. Reclassify the originals out of "Classics," and separately produce ~15 actual classics — CEFR-leveled adaptations of literary works (e.g. a short-summary version of a Sherlock Holmes story). **Fixed 2026-08-18**: root cause was `build-manifest.py` assigning every story's type purely from its folder (`stories/classics/b1/`), ignoring the correct `"type": "original"`/`"type": "classic"` already set inside 24 of the 36 files in that folder. Fixed the generator to prefer each file's own type; B1 now correctly shows 12 → *(then)* 16 classics / 24 original. Also wrote 4 new B1 classic adaptations (Sherlock Holmes, Alice in Wonderland, The Picture of Dorian Gray, Cinderella) to bring the classics shelf to 16, past the 15 asked for.
- [ ] LATAM track lessons: integrate the reader's word-lookup / add-to-deck functionality directly into lesson body text (e.g. when the text discusses the Maya, users should be able to tap a word to see its meaning or add it to their deck), not just in standalone readings.
- [ ] Consider a "Show English translation" toggle button for B1 informative texts that reveals a full English version.
- [ ] B1 U1 L1 S7: the exercise question contains the answer.
- [ ] B1 U1 L1 S8: correct answer "ocurrió" is not being accepted.

## A1 — Unit-by-unit findings

*Note added 2026-08-18: the unit/lesson/step numbers below were captured from one playthrough and content has been actively restructured since (by this session and others) — some references may no longer point at the exact step they did. Where a fix below says "found via corpus-wide sweep" it means the underlying bug pattern was searched for across all of A1 rather than at the specific cited location, so it should be caught regardless of renumbering.*

### Unit 1
- [x] L1-S3: por favor, gracias, hola, adiós used before being taught. **Fixed 2026-08-18** — see the "lesson progression" fix above (vocabulary moved ahead of exercises app-wide).
- [x] L1-S8: "hasta luego" used before being taught. **Fixed 2026-08-18**, same cause as above.
- [x] L1-S10: "bien" used before being taught. **Fixed 2026-08-18**, same cause as above.
- [ ] L1-S12: nonsensical prompt "….(hola), por favor" — this phrasing pattern recurs elsewhere too. *(not found/fixed this pass)*
- [x] L1-S13: lesson vocabulary currently only appears at this step; should move to the start of the lesson (right after grammar) — this alone would fix several of the above "used before taught" issues. **Fixed 2026-08-18** — this was the exact diagnosis; implemented app-wide across all 100 A1 lessons.
- [x] L2-S12: "Soy …" exercise — verify whether it accepts any name. **Answered and fixed 2026-08-18**: it did not (only "Meg"). Fill-blank now supports multiple accepted answers; this one accepts "Meg" or "Carlos".
- [ ] L3-S5: duplicate text shown twice on the same slide (e.g. "Me llamo Carlos" appears twice) — this is a recurring bug, not unit-specific. **Root cause found and fixed for this instance 2026-08-18**: the grammar file for this exact lesson (a1-01-03-questions-gr.json) had a `table` and an `examples` section repeating the same 3 sentence pairs verbatim on one screen. Swept all A1 grammar files for the same table/examples exact-duplicate pattern and fixed 5 files total (8 duplicate items removed). Not yet checked for the same duplication happening via other section-type combinations (e.g. within a single `examples` or `dialogue` list).

### Unit 2
- [ ] 2.1: "amigo"/"amiga" used before being taught. *(should now be caught by the vocabulary-reorder fix if it was a vocabulary-ordering issue — not individually reverified)*
- [ ] S21: writing-exercise prompt "identify a male person" is awkwardly phrased. *(not fixed this pass — same phrasing recurs in U7 below)*
- [ ] L5(?)-S19: reading references photos that aren't actually shown. *(not fixed this pass)*

### Unit 3
- [ ] L1-S22: "name one male/female friend" prompt is awkward, needs rephrasing. *(not fixed this pass)*
- [x] L3(?)-S4: "which form of ser is used in 'de dónde eres'" — bad exercise, the answer ("eres") is embedded in the question. **Fixed 2026-08-18**: reworded to "Which form of ser goes with tú when asking where someone is from?"
- [x] L3-S13: "Carlos es simpát…" — answer is currently "simpático" but should just be the completion "ico". **Fixed 2026-08-18**, along with 6 other instances of the same bug (full word stored instead of the missing suffix) found by scanning every fill-blank whose sentence shows a partial word stem before the blank.
- [x] L4-S13: "Es un chico…" answer "alto" — could be any adjective, exercise is unguessable. **Fixed 2026-08-18**: now accepts a curated list of correctly-agreeing adjectives instead of only "alto".
- [ ] The reading duplicates the previous unit's reading; the earlier unit's reading was already too advanced for that point, and even here it's still a bit too complex for Unit 3. *(not fixed this pass — needs new reading content, not just a data patch)*
- [x] S19: "Son unos amigos…." answer "simpáticos" — same "could be any adjective" problem, needs a hint at minimum. **Fixed 2026-08-18**, same multi-answer fix.
- [x] Review-S17: "tap the sentences in the right order" exercise doesn't fit this context. **Fixed 2026-08-18** — see the sentence-order → multiple-choice conversion above (all 23 A1 instances).

### Unit 4, Lesson 1
- [ ] S3: answer should also accept "cómo te llamas". *(not found in current content at this location — may have moved; not fixed)*
- [ ] S5: grammar explanation / example differentiation is good, but the tip references Lingolia without linking to the actual page — apply the Lingolia-link fix here too. *(not fixed this pass)*
- [ ] S7: "joven" is incorrectly wrapped in asterisks — check for this formatting bug elsewhere too. *(the asterisk-rendering bug itself is fixed app-wide via escMd(); the specific "joven" instance reported here wasn't located in current content to confirm — may already be resolved as a side effect)*
- [ ] S9: "Ana es ….." answer "joven" — could be any adjective. *(not found at this exact location in current content — the identical "Ana es ____ → joven" item was found and fixed under a different current file/unit; see Unit 3 above)*
- [ ] S10: "Meg es simpátic…" — answer should just be the completion "a". *(likewise not found at this exact location — the equivalent bug pattern was fixed wherever the corpus-wide scan found it)*

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
- [ ] Unclear whether "quiero"/"necesito" are actually explained before use — they're covered later in the same unit. Consider swapping the order of Lessons 1 and 3 (to be discussed after further analysis). *(not addressed — a curriculum-sequencing decision, not a data fix)*
- [x] L2-S9: "Quiero … manzanas" answer "dos" — could be anything. **Fixed 2026-08-18**: now accepts dos through diez instead of only "dos".

### Unit 9 (café unit), Lesson 1
- [x] S18: "which is correct?" — all three options are grammatically correct, but only "tomo leche" is accepted. **Fixed 2026-08-18**: reworded to "Which sentence means 'I drink milk'?", which disambiguates the intended subject without touching the options.

### Unit 9, Lesson 2
- [x] S18: same "which is correct" problem as above. **Fixed 2026-08-18**, same treatment ("Which sentence means 'I eat rice'?").

### Unit 9, Lesson 3
- [ ] Querer was already taught earlier — the lesson should acknowledge this explicitly ("we've seen this before, now let's use it in a café context") rather than reintroducing it cold. *(not fixed — needs new lesson-copy authoring)*
- [x] S17: same "which is correct" problem, all three options valid. **Fixed 2026-08-18** ("Which sentence means 'I want a salad'?").

### Unit 9, Lesson 4
- [x] S2: sentence-ordering exercise "Carlos presenta a Meg. Meg es su amiga" produces a nonsensical result. **Fixed 2026-08-18** — this exact item was one of the 23 sentence-order exercises converted to multiple-choice ("Which sentence starts this exchange?").

### Unit 9, Lesson 5
- [ ] S9: "what comes first?" exercise is weak, needs changing. *(not fixed this pass)*
- [x] Vocabulary: "rico" is glossed only as "rich" — it can also mean "delicious," and that sense is missing. **Fixed 2026-08-18**: dictionary entry now reads "rich; delicious (of food)".
- [x] S18: "where does the café encounter take place?" — the question contains its own answer ("in a café"). **Fixed 2026-08-18**: reworded to "Where does this conversation take place?"
- [x] S20: "what does the customer eat?" is marked as "a sandwich," but both characters actually eat tacos. **Fixed 2026-08-18**: verified against the actual reading (both Carlos and Meg order tacos, no sandwich anywhere in the story) and corrected the answer to "Tacos."
- [x] S25: two duplicate "sí, ahora mismo" reply options. **Fixed 2026-08-18**: replaced the duplicate with "Sí, mañana." as a distinct (and clearly wrong-for-context) distractor.

### Unit 9, Lesson ~8.5
- [ ] "Aquí está mi …" answer "grupo" — no way for the user to infer this answer. *(not found/fixed this pass)*
- [x] S11: "Quiero … tomates" answer "tres" — arbitrary, unguessable. **Fixed 2026-08-18**: now accepts dos through diez.
- [ ] S12: same problem, "Necesito … kilo de arroz". *(not found in current content at this exact phrasing — not fixed)*
- [ ] S13: build-the-sentence exercise — the relative order of "dos manzanas" and "una botella de agua" shouldn't be enforced as a strict sequence. *(not fixed — would need a sentence-builder grading change to accept reordered clauses)*

### Unit 9, Consolidation
- [x] S8: "Necesito … leche" multiple-choice — exercise is broken (the intended correct answer "leche" doesn't work with the structure). **Fixed 2026-08-18**: the question text repeated "leche" that was also in every option, producing "Necesito leche leche" if picked — shortened the question to "Necesito __." so the options complete it cleanly.
- [x] S17: all three answer options are correct. **Fixed 2026-08-18** ("Which sentence means 'I have two siblings'?", disambiguating from the also-valid "tienen dos hermanos").

### Unit 10, Lesson 1
- [ ] S10: sentence-ordering exercise doesn't work well.
- [ ] "Which sentence correctly connects the ideas…" is a poor review-exercise format.
- [ ] Users are asked to state their age in an exercise but have only been taught numbers up to 3 at that point.
- [ ] Unit 10 overall needs a full review: too much writing, too little active practice. Prioritize teaching how to conjugate "saber" and basic connectors (y, con, sin, pero) over incidental vocabulary like "vela" and "globo".
