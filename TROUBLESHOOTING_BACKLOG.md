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
- [x] Lesson-complete summary card (accuracy %, time taken; later with sound effects) — nice-to-have for later. **Built 2026-08-27**: `finishLesson()` now shows a summary screen (`renderLessonSummary()` in `engine/lessons.js`) instead of returning straight to the previous tab — "Congratulations!", the lesson's within-unit number and title (e.g. "Unit 1 · Lesson 1.5 — Hello", the same numbering the unit's own lesson list already uses), a new abstract frontispiece (`Art.svg('summit', ...)` in `engine/art.js`, matching the existing 5-class ink/accent illustration language exactly — one climb just made, distinct from My Journey's whole-journey `ascent`), then accuracy and time taken. Accuracy is correct-on-first-try across every graded interaction in the lesson (including the remediation redo pass), tracked via two counters incremented in the existing `solveStep()`/`failStep()` — not a new grading path. Time is wall-clock from `startLesson()` to `finishLesson()`, formatted as "3 min" / "1 hr 5 min". Both stats gracefully omit themselves (a pure-reading lesson has no graded steps to compute accuracy from). Verified live end-to-end with Playwright: correct 75% accuracy from a mixed pass/fail sequence, correct lesson numbering and title, "Done" button correctly returns to the originating tab. Sound effects **built 2026-08-27** too — see ROADMAP.md's "Audio" entry.

## Open design questions (decide before beta)

- [x] How do we track a user's "known words"? **Decided and built 2026-08-19**: a separate, unscheduled `knownWords` list distinct from the SRS deck. Populated three ways — an explicit Review/Know-it choice per word at the end of each lesson (replacing the old silent "untick what you know" checkbox), typing a word directly into a new Decks → My Dictionary view, or automatic graduation when an SRS card survives 5+ reviews and reaches a 180+ day interval. Known and reviewing are mutually exclusive by construction. Decks now shows both counts ("X reviewing" / "Y known") as the vocab-reach figures. Readings were *not* included in this pass — words tapped/looked up while reading still only join the SRS deck via the existing "add to deck" gesture, since looking a word up is arguably evidence against already knowing it; whether reading-encountered words should ever feed "known" is still open.
- [x] Accent sensitivity in answer-checking (e.g. está vs esta) — currently not enforced; decide whether/when to introduce. **Decided and built 2026-08-27**: introduced for Spanish, matching the standard Hungarian was already held to. Before flipping the switch, audited every interrogative/relative minimal pair (qué/que, cómo/como, dónde/donde, cuándo/cuando, cuál/cual, quién/quien) used as a fill-blank or sentence-builder answer across all of A1/A2/B1 (~100 instances) — found the content itself was already consistently correct everywhere (interrogative uses accented, relative/conjunction uses not), so the only thing actually lenient was the grading. Found a concrete case this was actively breaking: `a2-14-01-gr.json`'s own tip teaches "qué/dónde/cuándo/cómo carry an accent because they're asking, not relating," while the old lenient check accepted the unaccented form as equally correct for the same blank, silently disproving its own lesson. Fixed `engine/lessons.js`'s `normalise()` (used by fill-blank, sentence-builder, and dictation) to stop stripping accents for Spanish, matching Hungarian's existing behaviour — casing and punctuation stay lenient. Found and fixed the same accent-stripping duplicated in four other places that also grade Spanish typed input: `engine/drills/grammar-runner.js` (Workshop's Grammar Driller), `engine/verbs/table.js` and `engine/verbs/speed.js` (verb conjugation drilling — accent is often the only thing distinguishing person/tense, e.g. hablo/habló), and `engine/srs.js` (SRS typed review, which turned out to have been silently accent-lenient for Hungarian too despite its own comment claiming parity with lessons.js — a latent bug this happened to also fix). Left `engine/lexicon.js`'s accent-stripping alone — that one's for morphological stem-matching during word lookup (enclitic pronouns can shift where a stem's accent falls), a different and legitimate use, not grading leniency. Updated `exercises.schema.json`'s fill-blank description to match. Verified live in a running instance (Playwright against a local static server): `normalise('donde') !== normalise('dónde')` and `normalise('que') !== normalise('qué')`, while `normalise('Dónde') === normalise('dónde')` (casing) and `normalise('¿Dónde?') === normalise('dónde')` (punctuation) still hold.
- [x] Name interchangeability in exercises — e.g. "Carlos presenta a Meg" and "Meg presenta a Carlos" should probably both validate when either could be correct. **Investigated 2026-08-19, no live instance found**: searched every A1 "presenta a" exercise and every exercise pairing two character names with a symmetric relationship (son amigos/hermanos, se conocen, etc.) — none currently enforce a single name-order where the swap would be equally valid (the existing "presenta a" items are graded against genuinely ungrammatical distractors, not a name-swap). Note "Carlos presenta a Meg" and "Meg presenta a Carlos" aren't actually interchangeable anyway — they're opposite facts about who's introducing whom, not equivalent phrasings. The multi-answer infrastructure built this session (fill-blank `answers[]`, sentence-builder `solutions[]`) already covers this need for whenever a genuinely symmetric case is authored.
- [x] Can the dictionary/Library lookup handle inflected/reflexive forms like "conocerte"? **Answered and fixed 2026-08-19**: it could not — confirmed by scanning every reading in the course, which found 102 real infinitive+attached-pronoun forms ("conocerte", "ayudarte", "dármelo", etc.), none resolving. `Lexicon.lookup()` now strips one or two known enclitic pronouns and re-checks the verb index/dictionary for what's left, handling the accent-shift on double-clitic forms too ("dármelo" → "dar"). Verified live across single- and double-clitic examples, plus a genuinely ambiguous one (levantarme → both levantar and levantarse offered) and a regression check on an unrelated word.

## B1 — Readings & structure

- [x] The "Classics" reading category is mislabeled: most current entries are original texts, not adaptations of classic literature. Reclassify the originals out of "Classics," and separately produce ~15 actual classics — CEFR-leveled adaptations of literary works (e.g. a short-summary version of a Sherlock Holmes story). **Fixed 2026-08-18**: root cause was `build-manifest.py` assigning every story's type purely from its folder (`stories/classics/b1/`), ignoring the correct `"type": "original"`/`"type": "classic"` already set inside 24 of the 36 files in that folder. Fixed the generator to prefer each file's own type; B1 now correctly shows 12 → *(then)* 16 classics / 24 original. Also wrote 4 new B1 classic adaptations (Sherlock Holmes, Alice in Wonderland, The Picture of Dorian Gray, Cinderella) to bring the classics shelf to 16, past the 15 asked for.
- [x] LATAM track lessons: integrate the reader's word-lookup / add-to-deck functionality directly into lesson body text (e.g. when the text discusses the Maya, users should be able to tap a word to see its meaning or add it to their deck), not just in standalone readings. **Investigated 2026-08-27, already true — this item was stale**: every LatAm `story` step already renders through `engine/lessons.js`'s `story()`, which calls the exact same `Reader.makeClickable()` the standalone Library reader uses — every word in the lesson body is already tappable, with the same "+ Add to SRS Deck"/"+ Add to deck" actions. Verified live: tapped "golpe" inside `lesson.b1.conosur.05`'s embedded story and got a full popup (recognized it as part of the expression "golpe de Estado," showed both the expression and the standalone-word meaning, both add-to-deck buttons present and working). Whatever prompted this item may have predated the `story()` renderer picking up `Reader.makeClickable()`, or referred to something narrower (e.g. grammar-tip prose, which is in English and has nothing to look up) — no live gap found for the actual lesson-body reading itself.
- [ ] Consider a "Show English translation" toggle button for B1 informative texts that reveals a full English version. **Scoped 2026-08-27, not built**: the UI toggle itself would be trivial, but there's no English text anywhere to reveal — checked all 35 B1 `stories/world/*.json` files (the informative/cultural-history readings) and every one is Spanish-only, ~175 paragraphs total across conquest/colonial/Cold War/dictatorship-era topics. This is a real translation task on its own, not a quick UI fix — deferred rather than attempted as part of an "easy fixes" batch.
- [ ] **B1 LatAm track — fitness-for-purpose audit, 2026-08-27** (user: "I'm not sure that it's fit for purpose as it is"). **Decision made and generation approach fixed 2026-08-27**: rather than simplify/translate/split the existing content, the direction was to rebuild it — reading-first, exercise-light, escalating toward B2, deep enough that finishing a lesson supports "a five to fifteen minute conversation" about the topic. The new approach is written up in full in `content/es/guides/b1-content-spec.md` §3 (superseding its original Latin America section) and validated end-to-end on one lesson: `lesson.b1.precolombina.02` ("Grandes civilizaciones," the exact Maya/Mexica/Inca lesson this audit used as its example) was fully rewritten — new ~800-word story (real names, dates, places, four "¿Sabías que...?" facts, direct myth-correction that these civilisations "disappeared"), 10 real transferable vocabulary words (was 3 proper nouns), grammar section moved after the story with its 5 worked examples lifted verbatim from it, and exercises cut from 16 across four groups to 9 in one light group, 6 of them reading comprehension on the story's actual facts. Verified live: story renders first (before grammar), full length, tap-to-define still works on the new text; all 10 vocabulary words appear on their screen; grammar examples visibly match the story; a sampled exercise showed a real comprehension question with plausible distractors. `validate-content.py` and `audit-lesson.py` both pass structurally (the four now-dropped exercise groups — Reading/Listening/Dialogue/Writing — correctly report as gone; that's the intended new shape, not a regression). **Not yet done: the other four teaching lessons of this same unit, and all 35 other Latin America units** — this was deliberately scoped as one validated prototype before committing to rebuilding the remaining ~215 lessons at this depth, given the size of that undertaking. Original findings preserved below for reference.
  - **Scope**: LatAm is not a light cultural add-on — it's exactly as large as the Core grammar track, 36 units / 216 lessons each (`curriculum.json`). A learner doing both tracks in full does twice the B1 workload Core alone would be.
  - **Reading difficulty is measurably above the app's own B1 baseline, and flat across the whole 36-unit arc.** Measured avg words/sentence across all 35 `stories/world/b1/*.json` files: 16.1, vs. this app's own B1 "classics" adaptations (the fairest same-level in-app comparison, since B1 has no "everyday original" story category the way A1/A2 do) at 14.0, vs. A2's 11.5 and A1's 9.1 — and per-file breakdown shows no ramp: unit 1 (`b1-precolombina`, pre-Columbian societies) and unit 27 (`b1-conosur`, Cono Sur dictatorships) read at essentially the same register. Even the *first* LatAm reading assumes near-B2 reading stamina; there's no on-ramp.
  - **Zero translation support, but real word-level support does exist** (see the corrected item above) — so a learner isn't fully stranded, but there's no way to check whether they understood a whole sentence, only individual words, on text this dense.
  - **These readings are mandatory and graded**, not optional exposure, despite the in-lesson framing text calling them exactly that ("It's okay if you don't understand every word... Read for the general idea") — each is a required `story` step followed by a required graded "Reading" comprehension exercise group (e.g. `lesson.b1.conosur.05` has 4 MC comprehension questions gating that lesson's completion). The framing promises low-stakes exposure; the mechanics deliver a graded test.
  - **What's NOT wrong**: sampled grammar teaching (passive voice, impersonal se, gerund, formal connectors — genuinely B1-appropriate structures, well-explained, explicitly cross-referenced against Core's progression: "a step up from the active-voice sentences Core's earlier units use"), exercise construction (vocabulary matching, fill-blank, sentence-builder, listening, dialogue-complete, dictation — all well-built, correctly keyed, testing the actual grammar point), and historical accuracy/balance (sampled the Mexican Revolution and Cono Sur dictatorships specifically as topics where errors or bias would be easy to spot — both read as accurate, appropriately nuanced, no red flags). This is not a low-effort or careless content set; it's a calibration problem specifically in reading-text difficulty and total volume, not a quality problem.
  - Not yet decided: whether to simplify the reading prose to genuine B1 level, add real paragraph translations (a ~175-paragraph translation project, same one the toggle item above is blocked on), split LatAm into a shorter/optional track, or leave it as an intentionally-harder immersion track and just relabel/reframe it as such so the mismatch with "B1" isn't silent.
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
- [x] L3-S5: duplicate text shown twice on the same slide (e.g. "Me llamo Carlos" appears twice) — this is a recurring bug, not unit-specific. **Root cause found and fixed for this instance 2026-08-18**: the grammar file for this exact lesson (a1-01-03-questions-gr.json) had a `table` and an `examples` section repeating the same 3 sentence pairs verbatim on one screen. Swept all A1 grammar files for the same table/examples exact-duplicate pattern and fixed 5 files total (8 duplicate items removed). **Follow-up re-check 2026-08-27**: programmatically scanned every ES A1 grammar file for duplicates within a single `examples`/`items` list and across all section pairs in the same file (table rows vs. examples vs. anything else) — zero remaining instances of either shape.

### Unit 2
- [x] 2.1: "amigo"/"amiga" used before being taught. **Confirmed and fixed 2026-08-27**: `a1-02-01-ex.json`'s "Introduce Carlos."/"Introduce Meg." structured-writing prompts expected "Carlos es mi amigo."/"Meg es mi amiga." — but amigo/amiga isn't taught until the next lesson, `a1-02-02`. Reworded both prompts/answers to use `presentar` ("Carlos presenta a Meg." / "Meg presenta a Carlos."), which is this lesson's own taught vocabulary and mirrors its grammar screen's own example sentence.
- [x] S21: writing-exercise prompt "identify a male person" is awkwardly phrased. **Re-verified 2026-08-27**: confirmed already resolved by the earlier "all 6 instances" fix — no `identify a male/female` phrasing remains anywhere in A1.
- [x] L5(?)-S19: reading references photos that aren't actually shown. **Confirmed real and fixed 2026-08-27**: `a1-02-05-ex.json`'s reading-comprehension question for `stories/original/a1/a1-03.json` ("Los amigos de Meg") had "They talk about their families and show photos." as the correct answer — the story never mentions photos. Reworded to "They meet Meg's friends and talk about why Carlos is learning Spanish," which is what actually happens. Also caught and fixed a second mismatch in the same file while checking this one: a sibling question asked "where do Carlos and Meg **first** meet," but this story's opening line says Carlos *returns* to the language exchange with Meg — they'd already met before this reading. Reworded to drop the false "first."

### Unit 3
- [x] L1-S22: "name one male/female friend" prompt is awkward, needs rephrasing. **Re-verified 2026-08-27**: already resolved by the earlier "all 6 instances" fix — current Unit 3 prompts read naturally ("Say that someone is a male friend.", "Describe two male friends.").
- [x] L3(?)-S4: "which form of ser is used in 'de dónde eres'" — bad exercise, the answer ("eres") is embedded in the question. **Fixed 2026-08-18**: reworded to "Which form of ser goes with tú when asking where someone is from?"
- [x] L3-S13: "Carlos es simpát…" — answer is currently "simpático" but should just be the completion "ico". **Fixed 2026-08-18**, along with 6 other instances of the same bug (full word stored instead of the missing suffix) found by scanning every fill-blank whose sentence shows a partial word stem before the blank.
- [x] L4-S13: "Es un chico…" answer "alto" — could be any adjective, exercise is unguessable. **Fixed 2026-08-18**: now accepts a curated list of correctly-agreeing adjectives instead of only "alto".
- [x] The reading duplicates the previous unit's reading; the earlier unit's reading was already too advanced for that point, and even here it's still a bit too complex for Unit 3. **Fixed 2026-08-18/19**: confirmed `stories/original/a1/a1-03.json` ("Los amigos de Meg") was assigned as the reading for three separate lessons. Wrote a new story reusing only already-taught vocabulary (`a1-21.json`, "Cómo es cada uno") and reassigned one lesson to it. For the third lesson (a1-03c-05), found its reading-comprehension questions (a1-03c-05-r01..r04) didn't match a1-03.json's content at all (referenced a baby and a character "Andreas") — traced that content to a completely different, unrelated story (a1-16.json, already correctly used by the health unit) and rewrote the 3 mismatched questions to actually test a1-03.json instead of reassigning the story again. The "too complex for this level" half of the original complaint wasn't independently assessed.
- [x] S19: "Son unos amigos…." answer "simpáticos" — same "could be any adjective" problem, needs a hint at minimum. **Fixed 2026-08-18**, same multi-answer fix.
- [x] Review-S17: "tap the sentences in the right order" exercise doesn't fit this context. **Fixed 2026-08-18** — see the sentence-order → multiple-choice conversion above (all 23 A1 instances).

### Unit 4, Lesson 1
*Content has drifted from what was reported — today's `a1-04-01` teaches `hay`, not names/origin/adjectives. Re-checked each item against the whole A1 corpus rather than this specific lesson.*
- [x] S3: answer should also accept "cómo te llamas". **Re-checked 2026-08-27**: read every exercise referencing "¿Cómo te llamas?" across A1 (11 exercises, 6 files) — none are free-text productions of the question itself where an alternate accepted phrasing would matter; it's always one fixed option among multiple-choice/dialogue-complete/matching/sentence-builder items, already correct everywhere. No live instance of this bug found.
- [x] S5: grammar explanation / example differentiation is good, but the tip references Lingolia without linking to the actual page. **Re-checked 2026-08-27**: programmatically scanned every A1 grammar file for a "Lingolia" mention without an accompanying link — zero remaining. Already fully resolved.
- [x] S7: "joven" is incorrectly wrapped in asterisks. **Re-checked 2026-08-27**: found the exact reported instance — `a1-03c-01-ex.json`'s "¿Qué significa **joven**?" — and confirmed it's not a bug: this is the same file the 2026-08-18 escMd() fix names as its own example of a previously-broken pattern it fixed. The double-asterisk markdown is now the *correct* authoring convention (parsed to italics at render time), not leftover breakage.
- [x] S9/S10: "Ana es ….." / "Meg es simpátic…" — could be any adjective / answer should be a suffix only. **Re-checked 2026-08-27**: both patterns were already fixed under Unit 3 (see above); reran the corpus-wide scans for both bug shapes (single hardcoded adjective answer, and full-word-instead-of-completion) across every A1 fill-blank — zero remaining instances of either.

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
- [x] L2: uses "este"/"esta" without explaining them — double-check whether these were introduced earlier. **Confirmed real and fixed 2026-08-27**: searched every A1 vocabulary/grammar file for a dedicated este/esta explanation — there was none, anywhere in A1. Yet `a1-05-02-ex.json`'s own structured-writing exercise requires freely producing "Esta es mi madre."/"Este es mi padre." (tagged `teaches: possessives`, but that tag never covered este/esta), and `a1-05-03-possessives-tener-gr.json`'s grammar screen uses "Esta es mi madre." as an unexplained example. Added a new "Introducing someone: este / esta" section to `a1-05-02-possessives-gr.json` (the earliest lesson that needs it) explaining the masculine/feminine agreement pattern before the exercise that requires producing it. **Residual, lower-severity issue not fixed this pass**: `este`/`esta` also appear unglossed in five A1 *readings* (`a1-04.json`, `a1-11.json`, `a1-14.json`, `a1-16.json`, `a1-20.json`), one of which (`a1-04`) is read before this new grammar screen. Reading-only exposure to a word slightly ahead of its formal teaching point is a much softer issue than requiring production of it (tap-to-translate covers comprehension), and fixing it would mean rewriting several stories — left as a follow-up, not done here.
- [x] L5-S2: sentence-ordering exercise doesn't make sense — ties into the broader "replace all sentence-ordering exercises" item above. **Fixed 2026-08-18** — all A1 sentence-order exercises converted, see the item above.
- [x] Consolidation-S15: sentence-ordering exercise is nonsensical. **Fixed 2026-08-18**, same fix.

### Unit 6, Lesson 1
- [x] S10: "Yo …. en casa" answer "trabajo" — could be anything. **Fixed 2026-08-19**: found 14 instances of this exact pattern across all of A1 U6 (not just S10) — open verb blanks like "Yo __ en casa" and "¿Qué __ en casa?" with one hardcoded answer when 3-7 already-taught verbs fit equally well, plus two exercises that used the identical sentence "Yo __ en casa." with two different single answers (trabajo vs. cocino) — a direct conflict. Extended all of them to accept a curated list of correctly-conjugated verbs drawn from the unit's own vocabulary. One item ("¿__ trabajas?" → "Cuándo") was testing a specific just-taught word rather than open grammar, so it got an "(when)" hint instead.
- [x] S15: "Yo … por la tarde" with options trabajo/camino/estudio — only "camino" is marked correct with no clear reason why. This recurs throughout the unit (e.g. "¿Qué … en casa?" answer "comes") — needs a unit-wide pass. **Fixed 2026-08-19**, same unit-wide fix as S10 above.

### Unit 6, Lesson 6
- [x] S13: "sentences in the right order" exercise is really a "build the sentence" exercise. **Re-checked 2026-08-27**: read every exercise in `a1-06-consolidation-ex.json` (18 items, "Lesson 6" = the consolidation) — no `sentence-order` type, and nothing shaped like a mislabeled sentence-order/build task; all multiple-choice/fill-blank/matching/dialogue-complete/structured-writing items are properly formed grammar/vocab questions. No live instance found.

### Unit 7
- [x] "Identify a male person" awkward phrasing recurs — writing-exercise prompts need clearer phrasing generally. **Fixed 2026-08-18**: found and reworded all 6 "Identify a [male/female] person/friend" structured-writing prompts across A1 (not just this unit) to natural task phrasing, e.g. "Talk about a man, using él."
- [x] Reading: Meg and Carlos are shown living together despite having just met (also implied earlier via a video call) — they aren't dating yet at this point in the story; should be revised to something like one of them visiting the other's apartment. **Fixed 2026-08-18**: confirmed in stories/original/a1/a1-07.json ("El nuevo apartamento") — it was explicitly "el apartamento de Carlos y Meg" with plural possessives throughout (nuestros libros, nos gusta, ¿os gusta vivir aquí?). Rewrote it as Carlos's own apartment, with Meg re-cast as one of the visiting friends rather than a co-resident.
- [x] Consolidation-S16: "which is correct?" — "tienen dos hermanos" should also be marked correct, not only "tengo dos hermanos". **Fixed 2026-08-18** — see the café-unit fixes above (this was the same item, found under A1 U9 consolidation rather than U7).

### Unit 8
- [x] Unclear whether "quiero"/"necesito" are actually explained before use — they're covered later in the same unit. **Re-checked 2026-08-27**: current lesson order already teaches querer in `a1-08-03` ("What Do You Want?") and necesito in `a1-08-04` ("What Do You Need?"); confirmed neither word appears anywhere in `a1-08-01`/`a1-08-02` before that. Already fixed, presumably as part of an earlier reordering pass — no live instance of this bug remains.
- [x] L2-S9: "Quiero … manzanas" answer "dos" — could be anything. **Fixed 2026-08-18**: now accepts dos through diez instead of only "dos".

### Unit 9 (café unit), Lesson 1
- [x] S18: "which is correct?" — all three options are grammatically correct, but only "tomo leche" is accepted. **Fixed 2026-08-18**: reworded to "Which sentence means 'I drink milk'?", which disambiguates the intended subject without touching the options.

### Unit 9, Lesson 2
- [x] S18: same "which is correct" problem as above. **Fixed 2026-08-18**, same treatment ("Which sentence means 'I eat rice'?").

### Unit 9, Lesson 3
- [x] Querer was already taught earlier — the lesson should acknowledge this explicitly ("we've seen this before, now let's use it in a café context") rather than reintroducing it cold. **Confirmed and fixed 2026-08-27**: `a1-cafe-03-querer-gr.json` had the exact same conjugation table as `a1-08-03-querer-gr.json` (Unit 8) with no acknowledgment of the repeat. Reworded the intro text to "You've already met querer... here's a quick recap, now put to use in a café" and relabeled the table "Querer in the present (recap)".
- [x] S17: same "which is correct" problem, all three options valid. **Fixed 2026-08-18** ("Which sentence means 'I want a salad'?").

### Unit 9, Lesson 4
- [x] S2: sentence-ordering exercise "Carlos presenta a Meg. Meg es su amiga" produces a nonsensical result. **Fixed 2026-08-18** — this exact item was one of the 23 sentence-order exercises converted to multiple-choice ("Which sentence starts this exchange?").

### Unit 9, Lesson 5
- [x] S9: "what comes first?" exercise is weak, needs changing. **Confirmed and fixed 2026-08-27**: found it in `a1-cafe-05-ex.json` — "What comes first in a basic café interaction?" tested pure common-sense sequencing in English ("A greeting" vs. "The bill" vs. "That's all"), not any actual Spanish. Reworded to "Which phrase starts a café interaction, before you order?" with the three phrases themselves as options (Buenas tardes. / La cuenta, por favor. / Eso es todo.) — all already established vocabulary elsewhere in the same file — so it now tests real language recognition while keeping the same sequencing intent.
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
- [x] Users are asked to state their age in an exercise but have only been taught numbers up to 3 at that point. **Confirmed 2026-08-19, and it's worse than reported**: by the point numbers are taught at all (A1 U8), only uno/dos/tres are introduced — the full 1-20 system isn't taught until **Unit 12**, two units *after* Unit 10 already leans on ages like "veinticinco" (25) and dates like "el doce de mayo." **Fixed 2026-08-27** without moving the full Numbers unit (that would be the larger reordering decision below): programmatically found every number word actually used anywhere in Unit 10's exercises/grammar/vocab (cuatro through diez, doce, veinte, veinticinco, veintiocho, treinta) and added them to `a1-10-02-voc.json` (the earliest lesson that needs them), plus a compact "Numbers for talking about age" table and a tip on the veinte+cinco→veinticinco fusion pattern in `a1-10-02-edad-gr.json`. This makes everything Unit 10 currently uses actually decodable at the point it's used; Unit 12 remains the place for the full systematic 1-100 treatment.
- [x] Unit 10 overall needs a full review: too much writing, too little active practice. Prioritize teaching how to conjugate "saber" and basic connectors (y, con, sin, pero) over incidental vocabulary like "vela" and "globo". **Audited and rebalanced 2026-08-27**:
  - **Quantified the "too little active practice" complaint**: every one of Unit 10's 6 lesson files had only 7-12 exercises, versus the 16-19 that all 113 other A1 lesson files use — confirmed programmatically, not just by impression. Lessons 01-04 were the worst, at under half the normal count.
  - **Confirmed saber/pero/con/sin were completely absent**: not one exercise, grammar screen, or vocab entry anywhere in A1 (or even A2) taught any of them — despite the unit's own reading (`stories/original/a1/a1-10.json`) already using both "pero" and "sabe" unglossed ("Es el cumpleaños de Meg, pero ella no sabe que sus amigos preparan una sorpresa.").
  - **Fixed both problems together** rather than trading vela/globo away for saber/connectors (there was room to add, not just reallocate): added a "Joining more sentences: pero, con, sin" section to `a1-10-04-integracion-gr.json` (the lesson already introduces "y" for joining sentences, so this extends the same idea) and a "Saber: to know" section to `a1-10-05-celebracion-gr.json`, explicitly quoting the reading's own sentence, contrasted with the already-taught conocer. Also caught and fixed two smaller gaps surfaced while building this: "favorito/favorita" and actual colour words were used in the original ex07 ("Ask someone their favourite colour" → "¿Cuál es tu color favorito?") despite never being taught, and the months matching exercise only taught 4 of 12 months despite being the dedicated "Dates & Months" lesson — added the full set to `a1-10-02-voc.json`/`a1-10-03-voc.json`.
  - **Brought every lesson up to the 16-19 exercise norm** (01: 7→16, 02: 7→16, 03: 7→16, 04: 7→17, 05: 11→17, consolidation: 12→18 — 100 exercises total, up from 51), all newly-referenced correctly in each lesson's `exerciseRefs`, all new content built only from vocabulary already taught by that point (verified programmatically — no new "used before taught" instances introduced). Updated each lesson's goals/checklist to mention the new content, and regenerated `curriculum.json`/`decks.json` to match.
  - Validated: `python scripts/validate-content.py es` → 2596 passed, 0 failed throughout.

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

### HU A1 Readings — narrative/language audit (all 30 stories)

*User-requested audit 2026-08-26: read every `content/hu/stories/original/a1/a1-unit-01..30.json` end to end, checking for (1) raw Hungarian words leaking into the English narration text, (2) nonsensical content, (3) violations of the established canon (Meg moves to Hungary to live with her boyfriend Károly; Anna = his older sister, András = his younger brother, Mariann = their mutual friend/Hungarian teacher, Kaylee & Lauren = Meg's twin sisters in Johannesburg).*

- [x] **Mixed-language narration** — Units 5 and 7's English narration paragraphs had untranslated Hungarian nouns/adjectives dropped in mid-sentence (e.g. "They look around the szoba together," "The férfi is Károly's barát... nagyon erős"), exactly the "narration is English scaffolding, dialogue is Hungarian" rule broken. **Fixed**: reworded all 10 affected narration paragraphs (4 in Unit 5, 6 in Unit 7) to plain English; the Hungarian target-language content stays in the dialogue lines where it belongs. No other unit had this pattern — confirmed by re-reading every narration paragraph in the other 28 files.
- [x] **Vocabulary dumps disguised as dialogue** — two distinct instances of the same underlying bug (raw word lists stuffed into a `dialogue` paragraph, breaking character voice and reading as pure nonsense):
  - Units 13-15 each ended with Károly reciting 6-20 consecutive "A szó: X." ("The word: X.") lines — not something anyone would say aloud. **Fixed**: deleted all 32 lines across the three files; each story already had a natural closing exchange immediately before the dump (e.g. Unit 15's "A nap véget ér." / "Igen. Jó éjszakát.").
  - Units 21, 23, 24, 25, 26, 27, 28, 29, 30 each ended with a final "Károly" line that was just a bare, ungrammatical string of nouns (e.g. "kenyér alma víz.", "farmer.", "meghív találkozó találkozik hétvége szeretne."). **Fixed**: deleted all 9 lines; each story already had a natural closing line before it.
  - Units 21-24 additionally had a paragraph tagged `dialogue, speaker: Meg` where Meg narrates her own actions in third person ("Meg vesz kenyeret, almát..." — "Meg buys bread, apples...") — nobody talks about themselves that way. **Fixed**: converted these 4 paragraphs to proper English `narration` (matching the rest of the course's recap style) instead of fake self-referential dialogue.
- [x] **Canon violation: Meg and Károly treating each other as strangers** — Units 1 and 10 both had Meg and her live-in boyfriend ask each other's name and confirm identity ("És te? Károly vagy?" / "Igen, Károly vagyok." in Unit 1; "Meg vagyok. Mi a neved?" / "Károly vagyok." in Unit 10), despite both stories' own narration stating they're already living together. **Fixed**: Unit 1 now has Meg introduce herself to Anna (whom she's genuinely meeting for the first time in that scene) instead of to Károly. Unit 10 drops the self-introduction and instead has Károly say "Budapesten lakom. Veled élek." ("I live in Budapest. I live with you.") — reinforcing the cohabitation premise instead of contradicting it.
- [x] **Unit 9 non-sequiturs** — "Is your family in Budapest?" was answered with "Yes. My name is Meg, and I know your address" (doesn't address the question, and needlessly restates her own name to her boyfriend); later Károly randomly asks Meg's name again mid-conversation about whose book is whose. **Fixed**: the family question now gets a real answer that also plants a piece of established canon — "Nem, a családom Dél-Afrikában van." ("No, my family is in South Africa.") — and the redundant "Mi a neved?" exchange was cut, merging the surrounding lines into a coherent possessives conversation.
- [x] **Canon underuse** — none of the 30 readings mentioned Anna's one-year-old baby, András working as a teacher, or Meg's twin sisters Kaylee and Lauren by name/location (Johannesburg); Unit 6 only gestured at "her two younger sisters happen to be twins" without naming them. **Fixed 2026-08-26**: added these as English narration asides (no new Hungarian dialogue vocabulary needed, so no "used before taught" risk) — Unit 6 ("Family") now notes the baby held by Anna in the family photo and names Meg's twin sisters and their home city ("Her two younger sisters, Kaylee and Lauren, are twins — they still live in Johannesburg."); Unit 13 ("What You Do") now has a narration line distinguishing András's day job as a schoolteacher from Mariann's Hungarian tutoring, followed by Károly's dialogue line "András is tanít." — reusing only vocabulary ("is", "tanít") already established earlier in that same unit. Verified both files are valid JSON and pass `validate-content.py hu` (same 3 pre-existing, unrelated failures as before).
- [x] Verified all 18 edited files still pass `python3 scripts/validate-content.py hu` (837 passed; the same pre-existing 3 unrelated exercise-file failures noted elsewhere in this doc are untouched) and are valid JSON. `manifest.json`/`curriculum.json`/`decks.json` weren't regenerated — none of these edits touched titles, ids, lesson numbers, or character lists, only paragraph text, so the manifest stays byte-identical except its own contents-derived fields.

### HU Unit 5 — resolved 2026-08-26
*Re-audited by content (not step number, since numbering had drifted per the note at the top of this file) rather than the original S-numbers.*
- [x] L1 (a1-21, "What Is This?"):
  - [x] S4/S5 (micsoda tip): already resolved as a side effect of an earlier pass — the tip now explains the mi+csoda (wonder) etymology and no longer just restates the text above it (verified current `a1-21-b-gr.json`).
  - [x] S11: `micsoda` was glossed as "what thing" in `a1-21-voc.json` and in the generated `decks.json` — wrong sense for an emphatic "what on earth" word. **Fixed**: both now say "what on earth," matching the grammar screen's own explanation.
  - [x] S17: already resolved — all A1 `sentence-order` exercises were converted to multiple-choice in an earlier pass; none remain in `a1-21-ex.json`.
- [x] L2 (a1-22, "Objects"): S4 — `a1-22-a-gr.json`'s own example read "Van egy könyv itt." (locative stranded at the end). **Fixed**: reordered to "Itt van egy könyv."
- [x] L4 (a1-24, "Where Is It?"):
  - [x] S4 (zero copula): already clarified inline — the grammar text names it explicitly and contrasts it directly ("Ez egy könyv, not Ez van egy könyv").
  - [x] S9: found the real instance — exercise `a1-24-controlled-1` was "Van egy telefon ____. (here)" answer "itt," producing "Van egy telefon itt." **Fixed**: rebuilt as a sentence-builder tile exercise for "Itt van egy telefon." (avoids the capitalization ambiguity a leading fill-in blank would create).
  - [x] S12 + S18 + L5's S10/S15: **all the same underlying bug** — this whole grammar point (`van`/`nincs` + `itt`/`ott`) was inconsistent about whether the locative leads or trails, and `a1-24-b-gr.json`'s own tip already stated the intended rule ("itt/ott usually leads the sentence... Itt van a könyv, not Van itt a könyv") while several examples and exercises across `a1-24`, `a1-25`, and `a1-25-consolidation` contradicted it. **Fixed by standardizing the whole itt/ott+van/nincs pattern on locative-first** across `a1-24-a-gr.json` and `a1-24-b-gr.json`'s examples, `a1-24-ex.json` (controlled-1, controlled-4, practice-3, practice-6 — which also had a mismatched English prompt, "The chair isn't here" for an indefinite "Nincs itt szék," now "There's no chair here" — and writing-2), `a1-25-ex.json`'s practice-3 matching pairs, and `a1-25-consolidation-ex.json`'s consolidation-11 fill-blank. Also added a requested tip explaining `nincs` as a fusion of `nem` + `van`.
  - [x] Story ending abruptly (the Unit 5 reading is `story.a1.unit05`, "What Is This?", covering lessons a1-21 through a1-25): confirmed it stopped cold on an unanswered "Micsoda ez?" **Fixed**: added Károly's reply and a closing narration beat.
- [x] Consolidation (a1-25-consolidation): re-checked the current (rebuilt) consolidation directly rather than trusting the stale "S2" position — found the same locative-order bug in consolidation-11 (folded into the fix above) and confirmed all 6 multiple-choice items have exactly one defensible correct answer with no overlap.

### HU A1 — curriculum coverage audit (2026-08-27)
*Requested: triangulate the 150-lesson HU A1 curriculum against external
CEFR A1/Hungarian-pedagogy standards and confirm it covers what an A1
course should. `WebFetch` was unavailable in this session (blocked by the
network egress policy for every domain tested, including generic ones like
google.com) — findings below combine `WebSearch` snippets with established
CEFR/Hungarian-pedagogy knowledge, but every concrete claim about *this*
course's content was verified directly against the content files (grep),
not inferred. User confirmed the deliberate scope decision below; no fixes
applied this pass — logged for prioritization later.*

- [x] Past/future tense: confirmed genuinely absent (zero `múlt idő`/`jövő
  idő` grammar files) — **intentional**, matches the user's stated plan to
  cover it in A2 and is standard practice (the A1→A2 boundary is commonly
  marked by narrating past events). Not a gap.
- [x] **Decided 2026-08-27: all of the gaps below are deliberately deferred
  to A2, not A1 bugs to fix.** Cross-checked against
  `content/hu/a2-curriculum-draft.json` (the existing A2 planning doc) and
  found it already covers nearly everything this audit flagged — `tud`,
  `szabad`, `akar`, `lehet` are all in `verb_system`; `-hoz/-hez/-höz`,
  `-tól/-től`, `-nál/-nél`, `-ig` are all in `noun_and_case_system`;
  `Comparative`/`Superlative` are in `adjectives_and_comparison`; there's a
  whole "Weather & Seasons" unit (21). Added the three real gaps found *in
  the draft itself*: the productive dative `-nak/-nek` suffix was missing
  from `noun_and_case_system` (only the memorized `nekem` chunk exists in
  A1); "Nationalities and countries" was missing from `thematic_coverage`
  (worth pairing with Meg's South African background, already in the
  readings' canon); and the generic "Numbers" entry in `other_structures`
  was expanded into a note that numbers 11+ need to land early in A2 since
  A1 already uses them unglossed (ages, phone numbers) despite only
  formally teaching 0–10 — this is the one item here that's a live
  used-before-taught bug today, not just a sequencing preference, so it
  shouldn't wait for A2 to be prioritized within that level once work
  starts.
- [x] Areas confirmed to already meet or exceed typical A1 depth (no
  action needed): vowel harmony, zero-copula, van/nincs existentials, the
  full possessive-suffix "have" construction, plural `-k`, a wide spread of
  spatial cases already taught (`-ban/-ben`, `-ba/-be`, `-ra/-re`, `-n`,
  `-val/-vel`, `-kor`), postpositions (`mellett/előtt/mögött/között`), and
  notably **both indefinite and definite conjugation** — many slimmer A1
  courses skip definite conjugation almost entirely.

### HU Workshop drillers — audit and fix (2026-08-27)
Full audit of every Hungarian Workshop driller (Grammar, Vocabulary,
Listening, Translation, plus the 4 HU-specific ones: Verb, Suffix, Prefix,
Morphology), driven live via Playwright through 100+ rounds total, not just
a code read. 7 real findings, all fixed and re-verified live:
- [x] **Grammar Driller 100% dead for Hungarian**: `content/hu/indexes/
  grammar-index.json` referenced exercise IDs that no longer existed
  (renamed at some point after the index was last built) — 25/25 entries
  failed to resolve, so "Mixed" showed "0+ items" and Start immediately said
  "No exercises found." **Fixed**: reran `scripts/build_grammar_index.py hu
  es` — HU now has 20 skills / 162 resolvable entries (was 5/25, all stale);
  ES was unaffected (already 0 mismatches, just a routine refresh from new
  content). Also fixed the "Mixed — 0+ items" label itself
  (`engine/drills/grammar.js`) to count lesson-exercise entries too, not
  just the (for HU, nonexistent) hand-authored bank — was misleadingly
  showing "0+" even once the driller worked. Verified live: real questions
  now render ("Which means 'I have a son'?").
- [x] **Vocabulary Driller completely empty for Hungarian**: it needs 5+
  word sentences to build any exercise (`MIN_CONTEXT_WORDS` in
  `engine/drills/vocabulary.js`); `translation-index.json` had only 28
  pairs, longest 3 words. Root cause turned out to be the same as the next
  finding — a stale index, not a code bug in vocabulary.js. Fixed by the
  translation-index regeneration below; verified live afterward with a real
  question ("What does 'haza' mean in both?").
- [x] **`translation-index.json` stale and buggy**: only 28 pairs (should
  reflect current content), several of which were phoneme-pronunciation
  notes ("sz" → "s sound") pulled verbatim from a grammar screen's example
  block rather than real sentences, and sentence-builder-derived pairs had
  a punctuation-spacing bug ("Tegnap tanultam ." with a stray space before
  the period) from joining tiles with a plain `" ".join()`. **Fixed**:
  `scripts/build_translation_index.py` now joins a punctuation-only tile
  directly onto the previous word instead of space-separating it; reran
  for both languages. HU jumped from 28 → 734 pairs (135 of them 5+ words)
  — the phoneme-note entries disappeared because their source content had
  already been rewritten since the index was last built, confirming this
  was pure staleness, not a content-authoring gap. ES: 3019 → 3034 pairs
  (routine refresh). Verified live: 10 sampled Translation Driller
  sentences, all correctly punctuated, no phoneme notes.
- [x] **Past-tense conjugation bug — fabricated non-words graded as
  correct**: `engine/morphology/hungarian.js`'s `_pastLinkingClass()`
  classified any stem ending in a sonorant (r/l/n/ny/j/ly) as never needing
  a linking vowel, without checking whether that sonorant was preceded by a
  vowel (true Type I, "gondol" → "gondolt") or by another consonant (a
  cluster, "ugr" in "ugrik", which needs the linking vowel in every person
  like any other cluster-final stem). Verb Driller was presenting "ugrta"
  as the graded-correct 3sg past of "ugrik" — the real word is "ugrott".
  **Fixed**: gated the sonorant check on the same single-consonant-after-
  vowel test present tense already uses. Verified live: `ugrik`/`csuklik`
  now correctly generate `ugrottam.../csuklottam...`; controls (`gondol`,
  `vándorol`, `mos`) unchanged.
- [x] **Definite-conjugation guard missing for past tense**: present tense
  already excludes intransitive irregular verbs (van/megy/jön/alszik) from
  the "definite conjugation" pool (they have no real definite form), but
  past tense didn't — the driller's Past+Definite mode presented plain
  past-tense forms for these as if a distinct definite conjugation existed.
  Worse, `lesz` ("to become") is irregular only in the PAST table, so it
  never even reached the present-tense guard and got fully fabricated
  non-word "definite present" forms (leszem, leszi, ...). `eszik`/`iszik`
  are genuinely transitive with real distinct definite past forms
  (ette/itta) the table just doesn't have, so they were silently returning
  the wrong (indefinite-shaped) answer. **Fixed**: extended the guard to
  past tense for van/megy/jön/alszik/lesz (return null, matching present's
  treatment) and to eszik/iszik (return null rather than the wrong guess —
  the real definite forms still aren't authored, this only stops teaching
  a wrong one). Added a `lesz`-specific present-tense guard since it can't
  reach the shared irregular-lemma dispatch path. Verified live: the Verb
  Driller's Past+Definite pool correctly dropped from 563 to 556 verbs
  (exactly the 7 excluded lemmas), 10 rounds ran clean.
- [x] **Prefix Driller: `fel-`/`föl-` ambiguous question**: both are real
  dialectal variants meaning "up", but decoy selection only excluded the
  exact target prefix string, not other prefixes sharing its sense — so
  "Which prefix means 'up'?" could show both as options with only one
  marked correct (~1 in 35 questions, by simulation). **Fixed**:
  `_decoyPrefixes()` in `engine/drills/hu-prefix.js` now also excludes
  candidates whose sense matches the target's. Verified live: 7 sampled
  "up" questions, zero show both options (unrelated fel/föl co-occurrence
  as two decoys for a different question is fine and still happens, since
  neither is "correct" there).
- [x] **Naive English pluralization producing broken text**: bare `gloss +
  's'` (two independent copies: `engine/drills/hu-suffix.js` inline, and
  `naivePluralize()`/`possessivePhrase()` in `engine/morphology/
  hungarian.js`, shared by the Morphology Driller and the Reader's word
  popup) pluralized adjectives ("with freshs"), doubled/tripled a gloss
  already ending in "s" ("effectivenesss"), and appended "s" straight onto
  a truncated gloss's ellipsis ("unprovoked…s") or only the LAST of several
  comma-separated senses ("sour cream, smetanas"). Sampled ~30 live
  questions per driller; roughly a quarter to a third were affected.
  **Fixed**: `naivePluralize(gloss, pos)` now takes an optional POS and
  returns the gloss unchanged for anything but a noun, and pluralizes only
  the first comma-separated sense after trimming a trailing "…". Threaded
  the POS through all 5 call sites in hungarian.js (now exported so
  hu-suffix.js can reuse it instead of its cruder inline version, which
  also fixes the double/triple-"s" case that inline version didn't guard
  against). Verified live: 0/55 hu-suffix.js questions and 0/40
  hu-morphology.js questions matched the broken patterns afterward
  (previously reproducible on ~25-33% of samples).

### Deferred — future feature, not a bug
- [ ] HU audio: replace TTS with real recorded sound files. *(explicitly
  deferred by the user, 2026-08-21 — "future feature, not in this pass")*

### Found this pass, not originally reported
- [x] Exhaustive re-scan for the name-blank pattern (any fill-blank whose answer is a proper name): confirmed only the one instance already fixed (A1 U1 L2, "Soy ___.") exists anywhere in A1 — no further instances found.
- [x] Exhaustive re-scan for duplicate options within a single exercise (beyond the café-unit "sí, ahora mismo" case already found): 3 more instances — "Queremos una botella de agua." listed twice in one multiple-choice item, all three options identically "diecinueve" in a numbers item, and "Está a la izquierda." listed twice in a directions dialogue. All fixed with distinct, plausible-but-wrong distractors.
- [x] a1-03c-05's reading questions didn't match their attached story at all — see "Unit 3" reading-duplication entry above for the full fix.
