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
- [x] Green should consistently indicate a correct/good response app-wide. **Audited and fixed 2026-08-19**: found a real, self-contradicting split, not just a gap — tap-based options (`.lsn-option.correct`, `.gd-option.correct`) were already green, but typed inputs, sentence-builder's settled sentence, the lesson feedback text, the level test pass verdict, and a legacy quiz handler all still used navy, per a stale base.css comment that explicitly said green should stay narrow and *not* cover general lesson-exercise correctness — directly contradicted by the option rule sitting right next to it. Normalized everything to green and rewrote the comments to record this as the deliberate rule now. Verified live across 4 different exercise types. Decks/SRS rating buttons' narrow "Easy only" green was left as is — that's a different, still-correct use (mastery-tier feedback, not a right/wrong judgment).
- [x] After successfully solving a Spanish exercise, the English translation should always be shown (e.g. "Estudio español porque me gusta" → check → correct → show translation). **Partially fixed 2026-08-18**: plumbing added (`stepState.translation`, shown via `showTranslation()` on solve/reveal) for fill-blank and dictation steps, reading `step.english`/`step.translation` from content. **However — the content data doesn't exist yet**: across all of A1, 0 of 1,560 fill-blank and 0 of 522 dictation exercises carry an `english` field (checked programmatically). Sentence-builder already had this (949/1,076 items) and continues to work via its own existing mechanism. Populating translations for fill-blank/dictation is a real content-generation task (~2,000 items) — not done here.
- [x] Add a "back to previous exercise" button during lessons. **Fixed 2026-08-18**: added `#lesson-back-btn` (← Back) beside the Check/Continue button in the lesson footer; disabled on step 0. Going back re-renders that step fresh (ungraded again) rather than restoring a saved answer — there was no answer-history state to restore from. Verified live (disabled at step 0, enabled and functional mid-lesson).
- [x] Opening the lesson tree/map shouldn't require scrolling to find the current lesson — it should auto-scroll/open directly there. **Fixed 2026-08-18**: `renderCurriculum()` now scrolls the `.is-current` unit-path node or lesson-list row into view (centered) after every render. Verified live on both the unit path and a unit's lesson list by forcing progress deep into a level/unit and confirming the current item lands in the viewport without manual scrolling.
- [x] *(new mid-session request)* Enter key should do both Check and then Continue/Next, not just Check. **Already covered** by the single Check/Continue footer button above — Enter always clicks whatever the footer button currently is, so pressing it once checks the answer and pressing it again (same key, same target) advances to the next step. Verified live for both a fill-blank (type → Enter → Enter) and a multiple-choice (select → Enter → Enter) exercise.
- [x] End-of-lesson remediation loop: exercises answered wrong on the first try should be re-served at the end of the lesson ("let's review so it sticks"); if missed again, repeat until correct. **Built 2026-08-19**: any exercise missed at least once before being solved is queued and re-served, one at a time, right after the lesson's regular steps ("Quick review — 1 of N"); missing the redo too requeues it again. A step that exhausts all 3 tries and has its answer revealed does *not* requeue — that's the existing "never stuck on one item" safety valve, and looping it forever would defeat it. Recycle-block items are excluded (they have their own SM-2 schedule outside the lesson). Verified live end-to-end.
- [x] Grammar screens: audio playback is inconsistently placed. E.g. in a conjugation table you can listen to the pronouns (yo, tú, él) but not the conjugated forms themselves (trabajo, trabajas, trabaja). Sometimes only the English is voiced, not the Spanish. **Fixed 2026-08-18**: the shared `table()` renderer (engine/lessons.js) now also adds a listen button on column 2 whenever column 1 is a bare subject pronoun (or slash-combination of them), which is how every conjugation paradigm table is shaped — so the conjugated form itself is now audible, not just the pronoun. Sentence/translation reference tables (column 1 = a full Spanish sentence) are unaffected. Verified live on `trabajar`'s paradigm table and a non-conjugation reference table side by side. The "only English is voiced, not Spanish" half of this item is not yet separately audited.
- [x] Spanish words embedded in grammar explanation prose should be styled in italics, e.g. *adiós*. **Fixed 2026-08-18**: added `escMd()` (engine/lessons.js) — parses `*word*`/`**word**` into `<em>word</em>` — and wired it into grammar `text`/`tip`/`examples`, and multiple-choice/dialogue-complete/listening-choice questions and options, and fill-blank sentences. This also fixes a live bug it uncovered: 11 exercise questions across 5 A1-U3 files (e.g. "¿Qué significa **joven**?") were showing literal double-asterisks because the old `esc()` had no markdown support.
- [x] No exercise should ever use a proper name as the blank answer (e.g. "Carlos"), since it can't be inferred. **Fixed and swept 2026-08-19**: the one confirmed instance ("Soy ___." in A1 U1 L2) now accepts multiple names; a later exhaustive re-scan of every A1 fill-blank confirmed no other instances exist anywhere in the course.
- [x] Standard lesson progression should be: review (with appropriate clues) → new grammar → lesson vocabulary → exercises. **Fixed 2026-08-18**: found that all 100 A1 lessons with both a grammar and a vocabulary section had vocabulary sitting *after* the first block of practice exercises (order was goal, recycle, grammar, exercise-group, vocabulary, ...). Reordered every one so vocabulary comes right after grammar, before any exercises — this is the root cause behind most of the "word used before it's taught" reports throughout A1, not just A1 U1 L1-S13. Verified live.
- [x] "Tap the sentences in the right order" exercise type is broadly a poor fit for A1–A2 — sentences feel disjointed/arbitrary. **Fixed 2026-08-18**: converted all 23 A1 `sentence-order` exercises to multiple-choice ("which sentence starts this exchange?"), derived entirely from each item's existing sentences/solution data — no new authoring needed. Left B1's `sentence-order` exercises alone (historical-sequencing questions, not reported broken, still a live-and-used exercise type in the engine).
- [x] Recurring multiple-choice bug: several answer options are all grammatically valid, but only one is accepted. **Partially fixed 2026-08-18**: found and fixed the 4 instances in A1 U9 (café unit) — "Which is correct?" among tomo/tomas/toma-style person forms, and "tengo dos hermanos" vs. the also-valid "tienen dos hermanos" — by rewording each question to translate a specific English prompt, which disambiguates the intended subject without changing the options. Did not do an exhaustive sweep of A1 U10 or elsewhere for the same pattern.
- [x] Recurring fill-blank bug: answer could be literally any adjective/number/noun of the right category (e.g. "Ana es ___" accepting only "joven"), so the exercise is unguessable without a hint. **Fixed 2026-08-18** for the pattern actually found: 9 items across A1 U3/U3c/U8 where a ser+adjective or "quiero + number" blank had exactly one hardcoded answer with zero disambiguating context. Extended fill-blank to accept a curated list of valid answers (`stepState.acceptable` in engine/lessons.js) instead of one pinned string, keeping any grammar-agreement check (gender/number) intact. This was a targeted scan for one specific shape of the problem, not an exhaustive audit of every fill-blank/MC in A1.
- [x] Workshop → Grammar: some fill-the-gap exercises give away the answer within the exercise text itself. **Investigated 2026-08-19**: audited the dedicated bank (content/es/drills/grammar/a1-bank.json, 600 items, separate from the lesson exercise files fixed earlier) for the same pattern. Every candidate the scan flagged was a false positive — the established "(infinitivo)" hint convention, or a coincidental substring like "nos" appearing inside "Nosotros". Found and fixed 2 unrelated duplicate-option bugs while in there.
- [x] Workshop → Grammar: the "10 random exercises" set takes noticeably long to load. **Fixed 2026-08-19**: found the real cause — "Mixed" mode built its pool by fetching every lesson-exercise file referenced anywhere in the grammar index (668 distinct files across A1/A2/B1) before showing the first question, regardless of session size. Verified live: a 10-question Mixed session fired exactly 668 fetches. Capped it to sample 40 distinct files (still hundreds of exercises to draw from) — same session now fires exactly 40.
- [x] Grammar tips that reference Lingolia should include an actual link to the relevant Lingolia page (currently referenced by name only, e.g. A1 U4 L1 S5). **Fixed 2026-08-18**: found 5 grammar files (the adjective-agreement set, a1-03c-01 through 05) that mentioned "see Lingolia's ... reference" with no link. Added a verified working `external-link` section (`https://espanol.lingolia.com/en/grammar/adjectives`) to each.
- [x] Reading screens: consider a short heads-up before a reading that comprehension questions will follow. **Fixed 2026-08-18**, combined with the note below.
- [x] Reading screens: consider a short framing blurb along the lines of "it's okay if you don't understand everything — this exposes you to more natural language than crafted test sentences; take what you can for now" to set expectations. **Fixed 2026-08-18**: added one combined note above every in-lesson story step (engine/lessons.js `story()` renderer) covering both asks. Not yet added to the standalone Library reader, which has no comprehension test attached to it anyway (only in-lesson readings do).
- [ ] Lesson-complete summary card (accuracy %, time taken; later with sound effects) — nice-to-have for later. *(not done — explicitly deferred by user as "for later")*

## Open design questions (decide before beta)

- [x] How do we track a user's "known words"? **Decided and built 2026-08-19**: a separate, unscheduled `knownWords` list distinct from the SRS deck. Populated three ways — an explicit Review/Know-it choice per word at the end of each lesson (replacing the old silent "untick what you know" checkbox), typing a word directly into a new Decks → My Dictionary view, or automatic graduation when an SRS card survives 5+ reviews and reaches a 180+ day interval. Known and reviewing are mutually exclusive by construction. Decks now shows both counts ("X reviewing" / "Y known") as the vocab-reach figures. Readings were *not* included in this pass — words tapped/looked up while reading still only join the SRS deck via the existing "add to deck" gesture, since looking a word up is arguably evidence against already knowing it; whether reading-encountered words should ever feed "known" is still open.
- [ ] Accent sensitivity in answer-checking (e.g. está vs esta) — currently not enforced; decide whether/when to introduce.
- [x] Name interchangeability in exercises — e.g. "Carlos presenta a Meg" and "Meg presenta a Carlos" should probably both validate when either could be correct. **Investigated 2026-08-19, no live instance found**: searched every A1 "presenta a" exercise and every exercise pairing two character names with a symmetric relationship (son amigos/hermanos, se conocen, etc.) — none currently enforce a single name-order where the swap would be equally valid (the existing "presenta a" items are graded against genuinely ungrammatical distractors, not a name-swap). Note "Carlos presenta a Meg" and "Meg presenta a Carlos" aren't actually interchangeable anyway — they're opposite facts about who's introducing whom, not equivalent phrasings. The multi-answer infrastructure built this session (fill-blank `answers[]`, sentence-builder `solutions[]`) already covers this need for whenever a genuinely symmetric case is authored.
- [x] Can the dictionary/Library lookup handle inflected/reflexive forms like "conocerte"? **Answered and fixed 2026-08-19**: it could not — confirmed by scanning every reading in the course, which found 102 real infinitive+attached-pronoun forms ("conocerte", "ayudarte", "dármelo", etc.), none resolving. `Lexicon.lookup()` now strips one or two known enclitic pronouns and re-checks the verb index/dictionary for what's left, handling the accent-shift on double-clitic forms too ("dármelo" → "dar"). Verified live across single- and double-clitic examples, plus a genuinely ambiguous one (levantarme → both levantar and levantarse offered) and a regression check on an unrelated word.

## B1 — Readings & structure

- [x] The "Classics" reading category is mislabeled: most current entries are original texts, not adaptations of classic literature. Reclassify the originals out of "Classics," and separately produce ~15 actual classics — CEFR-leveled adaptations of literary works (e.g. a short-summary version of a Sherlock Holmes story). **Fixed 2026-08-18**: root cause was `build-manifest.py` assigning every story's type purely from its folder (`stories/classics/b1/`), ignoring the correct `"type": "original"`/`"type": "classic"` already set inside 24 of the 36 files in that folder. Fixed the generator to prefer each file's own type; B1 now correctly shows 12 → *(then)* 16 classics / 24 original. Also wrote 4 new B1 classic adaptations (Sherlock Holmes, Alice in Wonderland, The Picture of Dorian Gray, Cinderella) to bring the classics shelf to 16, past the 15 asked for.
- [ ] LATAM track lessons: integrate the reader's word-lookup / add-to-deck functionality directly into lesson body text (e.g. when the text discusses the Maya, users should be able to tap a word to see its meaning or add it to their deck), not just in standalone readings.
- [ ] Consider a "Show English translation" toggle button for B1 informative texts that reveals a full English version.
- [x] B1 U1 L1 S7: the exercise question contains the answer. **Fixed 2026-08-18**: "Elige la opción que mejor encaja en 'De repente apareció un hombre.'" quoted its own correct option verbatim. Reworded to "¿Qué oración describe algo que pasó de repente?"
- [x] B1 U1 L1 S8: correct answer "ocurrió" is not being accepted. **Investigated 2026-08-18, did not reproduce**: tested ocurrió/ocurrio/Ocurrió live against the actual exercise and all three were accepted correctly. Possibly already fixed by an unrelated earlier change, or content has shifted since this was reported (step numbers for this lesson don't match S7/S8 in current content — see the note at the top of this file).

## A1 — Unit-by-unit findings

*Note added 2026-08-18: the unit/lesson/step numbers below were captured from one playthrough and content has been actively restructured since (by this session and others) — some references may no longer point at the exact step they did. Where a fix below says "found via corpus-wide sweep" it means the underlying bug pattern was searched for across all of A1 rather than at the specific cited location, so it should be caught regardless of renumbering.*

### Unit 1
- [x] L1-S3: por favor, gracias, hola, adiós used before being taught. **Fixed 2026-08-18** — see the "lesson progression" fix above (vocabulary moved ahead of exercises app-wide).
- [x] L1-S8: "hasta luego" used before being taught. **Fixed 2026-08-18**, same cause as above.
- [x] L1-S10: "bien" used before being taught. **Fixed 2026-08-18**, same cause as above.
- [x] L1-S12: nonsensical prompt "….(hola), por favor" — this phrasing pattern recurs elsewhere too. **Fixed 2026-08-19**: found it — "Complete: ___, por favor." (answer "Hola") produced "Hola, por favor," which isn't an idiom. Dropped ", por favor" so it reads "Complete the greeting: ___.", matching a sibling exercise in the same file.
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
- [x] The reading duplicates the previous unit's reading; the earlier unit's reading was already too advanced for that point, and even here it's still a bit too complex for Unit 3. **Fixed 2026-08-18/19**: confirmed `stories/original/a1/a1-03.json` ("Los amigos de Meg") was assigned as the reading for three separate lessons. Wrote a new story reusing only already-taught vocabulary (`a1-21.json`, "Cómo es cada uno") and reassigned one lesson to it. For the third lesson (a1-03c-05), found its reading-comprehension questions (a1-03c-05-r01..r04) didn't match a1-03.json's content at all (referenced a baby and a character "Andreas") — traced that content to a completely different, unrelated story (a1-16.json, already correctly used by the health unit) and rewrote the 3 mismatched questions to actually test a1-03.json instead of reassigning the story again. The "too complex for this level" half of the original complaint wasn't independently assessed.
- [x] S19: "Son unos amigos…." answer "simpáticos" — same "could be any adjective" problem, needs a hint at minimum. **Fixed 2026-08-18**, same multi-answer fix.
- [x] Review-S17: "tap the sentences in the right order" exercise doesn't fit this context. **Fixed 2026-08-18** — see the sentence-order → multiple-choice conversion above (all 23 A1 instances).

### Unit 4, Lesson 1
- [ ] S3: answer should also accept "cómo te llamas". *(not found in current content at this location — may have moved; not fixed)*
- [ ] S5: grammar explanation / example differentiation is good, but the tip references Lingolia without linking to the actual page — apply the Lingolia-link fix here too. *(not fixed this pass)*
- [ ] S7: "joven" is incorrectly wrapped in asterisks — check for this formatting bug elsewhere too. *(the asterisk-rendering bug itself is fixed app-wide via escMd(); the specific "joven" instance reported here wasn't located in current content to confirm — may already be resolved as a side effect)*
- [ ] S9: "Ana es ….." answer "joven" — could be any adjective. *(not found at this exact location in current content — the identical "Ana es ____ → joven" item was found and fixed under a different current file/unit; see Unit 3 above)*
- [ ] S10: "Meg es simpátic…" — answer should just be the completion "a". *(likewise not found at this exact location — the equivalent bug pattern was fixed wherever the corpus-wide scan found it)*

### Unit 4, Lesson 2
- [x] S3: review question asks the user to recall reading details — review sections should always test grammar, never reading recall. **Root cause fixed 2026-08-18**: `Recycle.collectPool()` (engine/recycle.js) already only pulls exercises carrying a `teaches` tag — reading-comprehension items were never supposed to be eligible. Found 5 reading-category exercises across A1 U1/U2 that mistakenly carried a `teaches` tag anyway (e.g. "In the story, where do Carlos and Meg first meet?") and stripped it, matching the code's own documented intent. This should resolve the pattern everywhere it occurs, not just at this one location.
- [x] S9: "Ana es trabaja…" — answer "trabajadora" should just be the completion "ora"; this pattern (giving the full word instead of the completion) recurs in multiple places and should be fixed globally. **Fixed 2026-08-18** — see the Unit 3 fix above; this was one of the 7 instances found and corrected in a corpus-wide sweep.

### Unit 4, Lesson 3
- [x] S3: review again wants reading recall — replace this exercise type wherever it appears. **Fixed 2026-08-18**, same root-cause fix as U4L2 S3 above.
- [x] S5: grammar explanation presents singular/plural as if they were a vocab translation pair, which is confusing. **Fixed 2026-08-18**: found the actual bug — the grammar table's header row (`["singular", "plural"]`) was stored as an ordinary data row, so it rendered as if "singular" were a Spanish word being taught with "plural" as its translation. Swept all A1 grammar tables for the same accidental-header-row shape and fixed 2 instances (this one, plus a `["masculine", "feminine"]` header in a nearby file). Two other tables using "singular"/"plural" as row *labels* next to real examples were left alone — that's an intentional, different, and correct pattern.

### Unit 4, Lesson 4
- [x] S22: writing-exercise prompt "identify a woman and describe her" is wonky; consider rephrasing to something like "Say that Ana is a tall woman." **Fixed 2026-08-18**: reworded to "Say that Ana is a kind woman" (matching the exercise's actual model answer, which uses "kind," not "tall").

### Unit 4, Lesson 5
- [x] S9: "Carlos es un hombre alto y ….." answer "serio" — could be any adjective. **Fixed 2026-08-18** — see the Unit 3 multi-answer fix above.
- [x] S10: same issue, recurring. **Fixed 2026-08-18**, same fix.
- [ ] S17: reading is a third repeat of the same text — every unit needs a distinct reading. *(Fixed the confirmed instance of this — see "Unit 3" reading-duplication note below — but this specific U4L5 reference wasn't independently re-verified given the unit-numbering drift noted at the top of this file.)*

### Unit 5
- [ ] L2: uses "este"/"esta" without explaining them — double-check whether these were introduced earlier. *(not checked this pass)*
- [x] L5-S2: sentence-ordering exercise doesn't make sense — ties into the broader "replace all sentence-ordering exercises" item above. **Fixed 2026-08-18** — all A1 sentence-order exercises converted, see the item above.
- [x] Consolidation-S15: sentence-ordering exercise is nonsensical. **Fixed 2026-08-18**, same fix.

### Unit 6, Lesson 1
- [x] S10: "Yo …. en casa" answer "trabajo" — could be anything. **Fixed 2026-08-19**: found 14 instances of this exact pattern across all of A1 U6 (not just S10) — open verb blanks like "Yo __ en casa" and "¿Qué __ en casa?" with one hardcoded answer when 3-7 already-taught verbs fit equally well, plus two exercises that used the identical sentence "Yo __ en casa." with two different single answers (trabajo vs. cocino) — a direct conflict. Extended all of them to accept a curated list of correctly-conjugated verbs drawn from the unit's own vocabulary. One item ("¿__ trabajas?" → "Cuándo") was testing a specific just-taught word rather than open grammar, so it got an "(when)" hint instead.
- [x] S15: "Yo … por la tarde" with options trabajo/camino/estudio — only "camino" is marked correct with no clear reason why. This recurs throughout the unit (e.g. "¿Qué … en casa?" answer "comes") — needs a unit-wide pass. **Fixed 2026-08-19**, same unit-wide fix as S10 above.

### Unit 6, Lesson 6
- [ ] S13: "sentences in the right order" exercise is really a "build the sentence" exercise — same issue appears in the Consolidation section (S15). Review and fix everywhere this pattern occurs. *(the actual `sentence-order` type is fixed everywhere in A1 — checked this file's exercises directly and found no `sentence-order`-typed items in it at all, so if this report is accurate the exercise must be classified differently than expected; not independently identified or fixed this pass)*

### Unit 7
- [x] "Identify a male person" awkward phrasing recurs — writing-exercise prompts need clearer phrasing generally. **Fixed 2026-08-18**: found and reworded all 6 "Identify a [male/female] person/friend" structured-writing prompts across A1 (not just this unit) to natural task phrasing, e.g. "Talk about a man, using él."
- [x] Reading: Meg and Carlos are shown living together despite having just met (also implied earlier via a video call) — they aren't dating yet at this point in the story; should be revised to something like one of them visiting the other's apartment. **Fixed 2026-08-18**: confirmed in stories/original/a1/a1-07.json ("El nuevo apartamento") — it was explicitly "el apartamento de Carlos y Meg" with plural possessives throughout (nuestros libros, nos gusta, ¿os gusta vivir aquí?). Rewrote it as Carlos's own apartment, with Meg re-cast as one of the visiting friends rather than a co-resident.
- [x] Consolidation-S16: "which is correct?" — "tienen dos hermanos" should also be marked correct, not only "tengo dos hermanos". **Fixed 2026-08-18** — see the café-unit fixes above (this was the same item, found under A1 U9 consolidation rather than U7).

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
- [x] "Aquí está mi …" answer "grupo" — no way for the user to infer this answer. **Fixed 2026-08-18**: "grupo" is the lesson's own target vocabulary word (tested for recognition immediately before this item), but the blank still had zero in-sentence context pointing at it specifically. Added the same "(english word)" parenthetical hint convention already used for verb-infinitive blanks elsewhere: "Complete: Aquí está mi ___. (group)"
- [x] S11: "Quiero … tomates" answer "tres" — arbitrary, unguessable. **Fixed 2026-08-18**: now accepts dos through diez.
- [x] S12: same problem, "Necesito … kilo de arroz". **Checked 2026-08-19**: found it ("Necesito __ kilo de arroz." → "un") — but the blank is an article, not a number, and "un kilo" really is the only natural completion here (unlike the manzanas/tomates items). Not the same bug; left as is.
- [x] S13: build-the-sentence exercise — the relative order of "dos manzanas" and "una botella de agua" shouldn't be enforced as a strict sequence. **Fixed 2026-08-19**: added multi-order support to sentence-builder (`solutions`, an array of accepted tile orders, alongside the existing single `solution`) and applied it here with both clause orders. Verified live — both now solve the step.

### Unit 9, Consolidation
- [x] S8: "Necesito … leche" multiple-choice — exercise is broken (the intended correct answer "leche" doesn't work with the structure). **Fixed 2026-08-18**: the question text repeated "leche" that was also in every option, producing "Necesito leche leche" if picked — shortened the question to "Necesito __." so the options complete it cleanly.
- [x] S17: all three answer options are correct. **Fixed 2026-08-18** ("Which sentence means 'I have two siblings'?", disambiguating from the also-valid "tienen dos hermanos").

### Unit 10, Lesson 1
- [x] S10: sentence-ordering exercise doesn't work well. **Fixed 2026-08-18** — covered by the app-wide `sentence-order` → multiple-choice conversion; U10 already shows "Which sentence starts this exchange?" in its place.
- [x] "Which sentence correctly connects the ideas…" is a poor review-exercise format. **Checked 2026-08-19**: found the likely match ("¿Cuál combina la edad y la fecha correctamente?", testing "Tengo veinticinco años y mi cumpleaños es el doce de mayo." against two options with real grammar errors — wrong verb "soy" for age, wrong preposition, a nonsense swap). Unlike the other "which is correct" bugs, this one only has a single defensible answer — not actually broken, just a plain grammar-correctness question. Left as is.
- [x] Users are asked to state their age in an exercise but have only been taught numbers up to 3 at that point. **Confirmed 2026-08-19, and it's worse than reported**: by the point numbers are taught at all (A1 U8), only uno/dos/tres are introduced — the full 1-20 system isn't taught until **Unit 12**, two units *after* Unit 10 already leans on ages like "veinticinco" (25) and dates like "el doce de mayo." This is a curriculum-sequencing problem (Numbers is taught after Ages/Dates, not before), not a small content patch — belongs with the item below rather than a standalone fix.
- [ ] Unit 10 overall needs a full review: too much writing, too little active practice. Prioritize teaching how to conjugate "saber" and basic connectors (y, con, sin, pero) over incidental vocabulary like "vela" and "globo". *(not addressed — needs a product decision on curriculum reordering/rebalancing, not a content fix. The numbers-sequencing finding above should factor into that review.)*

## HU A1 — Unit-by-unit findings

*Merged in from `HUNGARIAN_A1_CONTENT_BACKLOG.md` 2026-08-26, which is now
deleted — that doc's cross-cutting fixes, curriculum-wide gaps, and Units
1-4 were all resolved during the session that captured them (2026-08-21)
plus this session's teaches-tag/consolidation/duplicate-dialogue audit;
only Unit 5's line items and the Unit 13 finding below were still open.
Several of Unit 5's original items turned out to already be resolved as a
side effect of this session's other work (the lesson-goal rewrite for
a1-21 through a1-35, the Vowel Harmony page inserted into a1-22, and the
consolidation rebuild to 20 exercises) and were dropped rather than
carried over.*

- [x] Unit 13 (`unit.a1.13`, "Everyday Actions" — `a1-61` through `a1-65`,
  "I Work, I Study" / "Everyday Verbs" / "Who Does What?" / "Talking About
  Activities" / "Verb Review"): grammar content was byte-for-byte identical
  across all five lessons despite each having a distinct title and
  vocabulary — the same duplication-without-customization bug already
  found and fixed in HU Units 2 and 4. **Fixed 2026-08-26**: rewrote both
  grammar screens ("Present Tense: -ok/-ek/-ök" and "Subject omission") for
  `a1-62` through `a1-65` to use each lesson's own new verbs (beszélni/
  hallgatni/nézni, főzni, keresni/várni/sétálni, tanítani/kérni/válaszolni)
  instead of all five repeating a1-61's dolgozom/tanulok/olvasok examples.
  Avoided each lesson's own irregular -ik verbs not taught until much later
  in the course (enni→eszem, inni→iszom, aludni→alszom, játszani→játszom,
  utazni→utazom — a1-63's own vocab is inni/aludni/főzni/venni, so only
  főzni is a safe regular verb; borrowed already-established `írok` for its
  second grammar example the same way the exercise-level fix did). a1-61
  itself needed no change — its examples already matched its own vocab.
  Verified live: all four lessons' grammar screens now show distinct,
  vocab-matched examples with no console errors; `validate-content.py hu`
  unaffected (still the same 3 pre-existing failures). **Follow-up, same
  day**: the user checked and found the lesson *goals* were also
  byte-identical across all five lessons (missed in the first pass, which
  only looked at grammar) — same bug, different field. Rewrote all five
  lessons' top-level `goal`, goal-section `items`, and checklist `items`
  (kept identical to each other within a lesson, as required) to name
  each lesson's own verbs instead of the generic shared text. Regenerated
  curriculum.json/decks.json afterward. Verified live. **Second follow-up,
  same day**: the user caught that two of the five rewritten goals
  (a1-63's "I can name more everyday actions: inni, aludni, venni." and
  a1-65's "I can name a few more everyday verbs: ...") were themselves
  the exact word-drill pattern this whole class of fix exists to
  eliminate — a bare vocabulary list, not a communicative framing.
  Reworded both to describe what the words let you talk about instead of
  just naming them ("I can talk about basic daily needs, like drinking,
  sleeping, and buying things."). Also caught and fixed a real editing
  bug from the first pass: a `replace_all` edit missed each lesson's
  top-level `goal` field (4-space indented) because the search string
  was copied from the 8-space-indented section copies — the two fields
  had silently diverged until this pass. All three locations verified
  identical again after the fix.

### HU Unit 5
- [ ] L1 (a1-21, "What Is This?"):
  - [ ] S4: tip merely restates what was already said above.
  - [ ] S5: explain in the tip that 'micsoda' is made from mi (what) +
    csoda (wonder).
  - [ ] S11: 'micsoda' is translated as "what thing."
  - [ ] S17: replace the "sentences in the right order" exercise with
    another type.
- [ ] L2 (a1-22, "Objects"):
  - [ ] S4: "van egy könyv itt" is very unnatural — "van itt egy könyv" is
    better.
- [ ] L4 (a1-24, "Where Is It?"):
  - [ ] S4: what is "zero copula"? (clarify/explain)
  - [ ] S9: "van egy telefon …" — wrong word order, should be "… van egy
    telefon."
  - [ ] S12: "itt nincs lámpa" is more natural.
    - [ ] Maybe explain 'nincs' as the merging of 'nem van'.
  - [ ] S18: "nincs itt szék" means "there is no chair here."
- [ ] L5 (a1-25, "Summary"):
  - [ ] S10: "itt van egy lakás" is more natural.
  - [ ] S15: "itt nincs kulcs" and "itt van egy lakás" are more natural.
  - [ ] Story ends very abruptly — should be rounded off.
- [ ] Consolidation (a1-25-consolidation): S2 — two options can be correct.
  *(the consolidation was fully rebuilt 2026-08-26 with different, reused-
  from-the-unit's-lessons exercises, so this old "S2" position almost
  certainly doesn't point at the same exercise anymore — would need a
  fresh look at the current consolidation to find whatever the equivalent
  issue is, if it still exists at all)*

### Deferred — future feature, not a bug
- [ ] HU audio: replace TTS with real recorded sound files. *(explicitly
  deferred by the user, 2026-08-21 — "future feature, not in this pass")*

### Found this pass, not originally reported
- [x] Exhaustive re-scan for the name-blank pattern (any fill-blank whose answer is a proper name): confirmed only the one instance already fixed (A1 U1 L2, "Soy ___.") exists anywhere in A1 — no further instances found.
- [x] Exhaustive re-scan for duplicate options within a single exercise (beyond the café-unit "sí, ahora mismo" case already found): 3 more instances — "Queremos una botella de agua." listed twice in one multiple-choice item, all three options identically "diecinueve" in a numbers item, and "Está a la izquierda." listed twice in a directions dialogue. All fixed with distinct, plausible-but-wrong distractors.
- [x] a1-03c-05's reading questions didn't match their attached story at all — see "Unit 3" reading-duplication entry above for the full fix.
