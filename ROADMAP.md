# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Active & Parked Priorities

2. **Keep new features cross-referencing `DESIGN.md`.** The 2026-09-23 visual-identity drift sweep (`ACHIEVED.md` items 72-75) is now fully closed out — `--bg-card` (real token, pure white in light mode, apparently a vestige of the briefly-adopted-then-reversed 2026-08-14 "soft card" phase) turned out to be used nowhere else in the entire app except the newer Level Test/Diagnostic/Home-onboarding features, all now fixed. The drift consistently came from features shipping their own CSS (and inline JS styles) without checking the doc first — a general periodic check for that would prevent the same class of drift recurring.

5. **Two new-learner notes still need a signal (added 2026-09-24).** The new-learner introduction (`ACHIEVED.md` item 87) planned two behaviour-triggered notes that weren't built, because nothing records what they'd trigger on: the **Verb Driller** note ("If a verb keeps catching you out, the Verb Driller practises just that", meant for the same verb missed three times across lessons) and the **Listening Driller** note ("Listening practice has its own space in the Workshop", meant for low listening scores). Lessons don't record which verb a miss was on, and there's no per-skill listening score. Either add those signals (e.g. note the lemma of a missed conjugation step in the learner model) or pick a different trigger. The copy is in `docs/feature-guidance-copy.md` (6a, 6b); the end-of-lesson "What's next" screen already suggests a grammar drill for a weak skill, which partly covers 6a.

104. **Workshop "Exam Preparation" section: citizenship tests now, full CEFR exam prep later (added 2026-09-28).** Workshop now has its own **Exam Preparation** section at the bottom, below Foundations (`engine/workshop.js`, drillers with `category: 'exams'`; commit `97868f02`). So far it holds only the **Hungarian Cultural Exam** (`engine/cultural-exam.js`, `content/hu/cultural-exam.json`), which used to sit under Studios. The section appears only when a course has at least one exam driller, so Spanish learners don't see it yet. Next, in order:
    - **Hungarian citizenship test.** Keep building out the existing module: the 6 official categories, explained artifacts, matching and 3 mock exams.
    - **CCSE (Spanish citizenship, Instituto Cervantes).** An es-es counterpart built on the same shell. The es-es B1 "Cultura y Ciudadanía" track already covers CCSE ground as lessons, but there's no exam-style practice module (question bank by CCSE task area, mock exams) like HU's.
    - **Full CEFR exam prep (later).** DELE/SIELE for Spanish, ECL/Origó for Hungarian, covering all four skills. It should build on the level-test reading section (§2, Reading Comprehension) and the Speaking/Writing Studio graders rather than start from scratch.

92. **Audit `imports/dictionary/spanish-en.json` for more wrong-primary-sense entries (added 2026-09-24).** Bug report #192 flagged the review card for "llamas" showing "a name of several localities in Asturias, Spain" instead of the taught verb sense — not corrupted/malformed data (the 2026-09-17 audit, ACHIEVED.md item 30, already covers that class), but a real Wiktionary entry that's simply the wrong headword for a common conjugated form that also exists as its own place-name/homograph entry. Fixed via `MANUAL_OVERRIDES` in `scripts/import_dictionary.py`, same mechanism as the 2026-09-18 HU "wrong-sense gloss" fixes (ACHIEVED.md, "HU Dictionary Wrong-Sense Gloss Fixes"), but ES has never had that HU audit's equivalent systematic pass over common words' primary senses — only this one-off fix. Worth a similar targeted audit of the ES dictionary's top N frequency-ranked headwords, since `Lexicon.define()` (used directly by SRS review cards) has no conjugation-aware disambiguation and will surface whatever sense the raw dictionary file happens to carry for that exact string.

107. **Expand the Hungarian B1/B2 classic adaptations to target length (added 2026-09-28).** The Hungarian literary classics in `content/hu/stories/classics/` are much shorter than the Library's word-count standards (the Spanish B1/B2 classics were expanded in commit `4aabea4b`):
    - **B1 classics (~400 words target).** 32 of 36 average ~225 words, with severe outliers under 120 words (*Édes Anna* `b1-10`: 114w, *Légy jó mindhalálig* `b1-11`: 98w, *Szindbád* `b1-12`: 91w). Expand to ~400 words, keeping B1 grammar and dialogue.
    - **B2 classics (~700 words target).** All 36 average ~288 words (e.g. *Pacsirta*, *A vörös postakocsi*, *Bánk bán*, *Ábel a rengetegben*, *Sorstalanság*, *Az ajtó*). The prose and dialogue are authentic, but they're 1-page vignettes; expand into ~700-word B2 adaptations with text-grounded comprehension questions.
    - **B1/B2 World/Civics shelf.** Consider expanding the short cultural vignettes too (currently ~130 words at B1, ~360 at B2).

111. **ES-LATAM leftovers from the B2 Library shelf fix (added 2026-09-30).** The three combined readings built from segments (Guatemala, El Salvador & Honduras, Nicaragua) are thin: 15 short paragraphs, no narration, no comprehension questions, unlike the other 33. (The last four Latin America units' "B2 Regional: …" titles and the B1 "inspired by" readings were fixed — see ACHIEVED.md.)

113. **GitHub issue #132, "'m' shouldn't be in the dictionary as a separate entry" (investigated 2026-09, could not reproduce).** None of `story.a2.unit01`'s 35 words looks up as `m`, the Reader tokenizer covers every Hungarian diacritic, English narration isn't tappable, and `word-index.json` has no entry mapping to lemma `m`. The dictionary does hold about 205 abbreviation and unit-symbol entries like `m` (SI metre), but many of the same shape (`db`, `ft`, `h`, `am`, `p`) are genuine Hungarian shorthand, so filtering short entries wholesale would remove real vocabulary. Needs a repro detail: which word was tapped, or how `m` was reached.

115. **Reader coverage follow-ups (added 2026-10-01).** (1) Run `scripts/audit-reader-coverage.js` in CI as a report, not a gate, so a content change that adds many unreadable words shows up. (2) `imports/dictionary/coverage-ignore.json` is shared by Hungarian and Spanish; split it per language if a word ever needs ignoring in only one. (3) The weekly gloss review uses the desktop app's default model, because the scheduling tool has no model setting; set the app default to Opus 5.5 (or check the task's own settings) if that matters.

117. **B1+ choice exercises: easy giveaways, not two right answers (scoped 2026-10-01).** A1-A2 were audited for two acceptable answers (ACHIEVED.md, "One correct answer per choice exercise, A1-A2"). A scope of B1-C1 (9,872 choice exercises) found that problem is rare there: no duplicate options or multi-answer `correct`, no dictionary synonyms, and only 1 doubtful item in a random sample of 180 sentence/reply/dialogue questions (`b1-22-03.ex06`, "Which form follows «si» in this pattern?" without the pattern), against about 9% at A1-A2. The weakness at B1+ is the opposite: wrong options that can be ruled out without knowing the grammar. Spanish B1 has 486 of 3,597 (14%) where a wrong option is given away by a mismatched *ayer*/*mañana* ("Busqué una alternativa mañana."); B2 and Hungarian 3-5% by the same measure. Others are throwaways ("La comunicación existe.", "Tengo una decisión.") or, in Hungarian B2 dialogues and the ES-LATAM history tracks, absurd statements ("Fuss ki az épületből és ne gyere vissza soha többé."). If worth doing: replace them with near-miss distractors that test the target form (wrong mood, wrong tense with a matching time word, wrong case), starting with the Spanish B1 *ayer*/*mañana* set.

---

## 2. Future Feature Ideas

Unscoped enhancements, UX refinements, and candidate features grouped by domain (completed items archived to `ACHIEVED.md`):

### Reading Comprehension (CEFR) — key feature
Reading comprehension is one of the four skills every CEFR exam (DELE, SIELE, the Hungarian ECL/Origó exams) tests on its own, and it should be a first-class part of Parlour, not an optional extra at the end of a story.

**What exists (audited 2026-09-24):**
- **Library reader** — an unscored "Comprehension Check" block at the end of a story, rendered from `narration.pedagogical.comprehensionQuestions` (`engine/reader.js`, `renderStory()`). Coverage is patchy: ES A1 originals have 3 questions each (28 stories); the ES B1 Latin America readings have only 1 each; ES A2 (50 readings), ES B1 originals and classics, all of es-es beyond A1, and HU A1/A2 have **none**. HU B1 citizenship readings have 3 each. Answers aren't saved, scored or shown anywhere else.
- **Lessons** — a "Reading" exercise group after the lesson's story step: ES A1 16/27 story lessons, A2 27/27, B1 core 36 (297 exercises, nearly all `multiple-choice`; shared between es-latam and es-es). HU has these on only 12 B1 lessons, and none at A1/A2.
- **Level tests / diagnostic** (`content/<lang>/tests/`) — grammar and vocabulary sentence items plus writing and speaking tasks. **No reading section at all.** So nothing in the app actually measures reading at a CEFR level.

**Reading section in level tests & diagnostic — built (2026-09-27):**
- New question types added to `engine/leveltest.js` & `engine/diagnostic.js`: `reading-mc`, `true-false-not-stated`, `gapped-text`
- `readingSection` schema added to `test.schema.json` (all 3 courses)
- Reading sections authored and validated for 9 level test files: A1/A2/B1 × es-es/es-latam/hu
- Diagnostic placement test (`engine/diagnostic.js`) now features an adaptive reading comprehension section on every tier (A1, A2, B1 × es-es, es-latam, hu), evaluated seamlessly with core questions and surfaced in tier debrief
- Scores saved to `Lang.key('readingScores')` across both level tests and diagnostic placement
- **Fix + "nearly there" band (2026-09-28):** the diagnostic's reading section was never actually shown — `_renderTesting` scored the tier as soon as the last core question was answered, so reading always counted 0/2 and the best possible tier score was 10/12 (83%), under the 85% pass mark. Nobody could pass A1, so everyone was placed in A1 (surfaced by a learner who scored 8/10). Fixed, plus a middle band: 70% to 84% on a tier (`borderlineRatio`, optional per test file) places one level up with a "Review <tier> first" option and a "Nearly there" badge. The preface now shows the real per-tier question count (12, not 10) and the pass/band percentages from the data.
- **Library Comprehension Scoring (Phase 5):** `engine/reader.js` and `engine/library.js` now score and persist reading comprehension checks to `Lang.key('storyComprehension')`, surface completion feedback upon answering, and display a `Quiz N/M ✓` badge on both home shelves and saved cards

**Future items:**
1. Backfilling comprehension questions across remaining Library readings (A2/B1 classics & originals).
2. Connecting reading skills directly into the Can-Do Journey passport.


### Artifacts — real-world texts you're now ready for
Added 2026-09-24. Every so often, depending on the learner's level, Parlour presents an **artifact**: a real text, image or object from the real world — a restaurant menu, a traffic sign or instruction, a book title, a train ticket, a shop notice. The point is the moment of *"I can actually read this now"*: proof that the learning works on something that really exists, not on material written for learners.

Open questions for when this is scoped:
- **Matching an artifact to the learner** — tag each artifact with the words and grammar needed to understand it and show it once the learner has them (the lesson `teaches` tags and the % familiar data could decide this), rather than by CEFR level alone.
- **When it appears** — e.g. after finishing a unit, on Home, or as its own occasional card; frequent enough to motivate, rare enough to stay special.
- **What the learner does with it** — just read it (tap words as in the Reader), or answer one or two "what does this say?" questions (ties into the Reading Comprehension section above).
- **A collection** — artifacts already met could be kept (e.g. in Journey or the Library), a visible record of real things the learner can now read.
- **Sourcing** — real images need clear rights (own photos, public-domain or openly licensed ones, credited in `CREDITS.md`); a recreated menu or sign is a fallback, but loses some of the "this is real" point.

### Library & Reading Experience
Brainstormed 2026-09-24 (quick fixes from the same pass shipped — see ACHIEVED.md, "Library Track Shelf, Shelf Ordering & Card Polish"). Next up: prototype 4.
1. ~~**"% familiar" on every card**~~ — built 2026-09-24, see ACHIEVED.md ("Library: % Familiar, Continue Reading & Series Progress"). Follow-ups: use the figure in recommendations ("12 of its words are in your deck"); decide whether My Texts' figure should also count content words only (it still counts every word).
2. ~~**Continue reading + series progress**~~ — built 2026-09-24, see ACHIEVED.md (same entry). Follow-up: reading positions are local to the device — add `storyProgress` to cloud sync (`engine/sync.js`) if resuming across devices matters.
3. **Pre-reading word preview** — an optional "5 words worth knowing" screen before a story. Preview only; nothing is added to SRS automatically (spec §17).
4. **Book-spine view** — a compact toggle that draws a shelf as book spines: height from reading length, colour from shelf type, a ribbon when read. Fixes the long scroll (B1 Classics is ~20 rows of cards on a phone) and fits the Parlour visual language.
5. **Timeline covers for the history track** — each card's cover is one segment of a single continuous line (the two-tone disc-on-a-line motif used for node art), so the whole shelf reads as a timeline. An optional `era` field on the reading (c. 1500, 1810, 1910) would add dates.
6. **Covers that mean something** — cover shape derived from the story's topic, not a hash of its id, so "travel" or "history" becomes recognisable at a glance.
7. **Filter chips** — Unread · Has audio · Under 5 min · Within reach, alongside the search box.
8. **"Drill this story"** (Clozemaster-style) — after finishing, a ~10-item cloze drill built from the story's own sentences via the Workshop shell. Related to the deferred idea of a post-lesson mini-game covering any weak Workshop driller.
9. **Questions during the story** (Duolingo Stories-style) — interleave a check between paragraphs, not only at the end. Ties into the Reading Comprehension item above.
10. **Save a sentence** — long-press a sentence to add it to a deck as a sentence card (sentence mining), not just single words.
11. **Listen through a shelf** (LingQ playlists) — play a shelf's narrated readings back-to-back; 244 ES readings already have audio.
12. **Citizenship exam-readiness view** (HU B1 track) — per-topic status across the track, e.g. "Constitution: read ✓, quiz 4/5". Depends on comprehension scoring (Reading Comprehension item 3).
### Listening Comprehension & Audio Modules
- **CEFR-Leveled Long-Form Listening Practice**: Introduce dedicated ~2-minute pre-recorded or multi-voice TTS audio modules (interviews, dialogues, monologues) accompanied by comprehension questions. Scale content strictly across CEFR levels: from A1 (simple descriptions of someone's day) to C1 (academic debates between three people on social housing, false friends, and complex idioms).
- **Listening Lab**: the existing Listening Driller (`engine/drills/listening.js`) is single-sentence and TTS-based only. A Listening Lab would be the longer-form mode, adapting the Conjuguemos model for paragraphs and short dialogues at A2–B1 — likely the first step towards the long-form practice above, not a from-scratch listening feature.


### Curriculum, Content & Extended Tracks
- **Exam-Focused Writing & Speech Units**: Introduce new units that expressly teach writing, particular aspects of speech, and turns of phrase for exams.
- **Cultural Track Recommendations**: Curated cultural recommendations integrated into the cultural track.
- **Cultural Track Slang**: Slang and colloquial expressions on the cultural track.
- **ProfeDeELE Exercise Sourcing**: Source reading and other exercises from [ProfeDeELE](https://www.profedeele.es/actividad/independencia-de-mexico/).
- **B2+ Civic Education & History Engine**: From B2 onward, build up a dedicated civic education and history engine.

### Platform, Audio & Administrative
- **New App Sounds**: Audio effects and sound palette refresh.
- **Teacher-Facing Version & Portal**: Separate teacher log-in and teacher-facing management/monitoring version.
- **Legal & Trademark**: Legal compliance, trademark registration, and administrative/bureaucratic requirements.
- **IP / Attribution Audit for Content Resources**: Review all third-party content used (word lists, texts, images, audio). Where Creative Commons material is used, add an acknowledgments page or footer (alongside `CREDITS.md`) next to an AI-use disclosure.
- **User-Configurable Feature Visibility (especially Workshop)**: Let learners choose which modules are shown. Too many options at once creates friction; an onboarding toggle or a settings page could hide unused sections.
- **Hero Load Animation**: On page load, the hero section "powers up" element by element, like a machine booting (originally pitched as a cyberpunk aesthetic, so check it against `DESIGN.md` first). Stagger reveals of logo, tagline, buttons, stat cards. Progressive enhancement only, per "Core First" below.
- **Language Expansion Order**: Finish Spanish & Hungarian content → V4 release milestone → Eastern European languages (e.g. Polish, Czech, Romanian) → Vietnamese. How to set up a new course is in §3 ("New courses").

### Ideas from other language apps (APK scan, 2026-09-24)
Found by pulling the UI strings out of the 12 language-app APKs in `apps for ux-ui inspiration/`. The per-app inventories are in `feature-inventories/` there. Only ideas that fit Parlour and aren't already built are listed. Items 1–2 were gaps confirmed in our code, and both are now fixed. This scan was a first pass at a wider idea: a systematic audit of competitor apps (Duolingo, Babbel, Clozemaster, Conjuguemos, Busuu, etc.) for UX patterns, exercise types and engagement hooks, going beyond UI strings to actually using them.
1. ~~**Resume a lesson where you left off**~~ — built 2026-09-24, see ACHIEVED.md ("Resume a Lesson Where You Left Off").
2. ~~**Credit vocabulary when a learner tests out**~~ — built 2026-09-24, see ACHIEVED.md ("Vocabulary Credit When Testing Out"). Follow-up: words are credited as fully known. A weaker "assumed known" status could be used instead if placed learners find the Reader too generous.
3. **Word-level error hints on typed answers** (Duolingo: "You missed a word" / "You used the wrong word"; LingoDeer: "Check the word form" / "Check the word order" / "There's something extra"). `generateAnswerDiff()` already separates accent slips from typos, letter by letter. Add a word-level layer for multi-word answers. Use `Lexicon` / the HU morphology engine to spot "right word, wrong form", the most common error in a course built on conjugations and suffixes. That makes the 2nd and 3rd tries (lesson gating rule) more useful.
4. **"Can't listen right now"** (EWA: "Can't speak now" snooze for 1 hour or 1 day; LingoDeer silent mode: "don't forget to redo lesson with audio"). We have only the speaking half (`lessonSkipSpeaking()`). Add the same for listening and dictation steps. Also send snoozed steps to recycle for later: snoozed speaking steps are currently dropped from `missedSteps` in `nextLessonStep()`.
5. **Hands-free audio review** (Babbel Audio Recaps, "listen while driving, cooking, jogging"; LingoDeer Listen Along with loop, pause between items and translation modes; Language Transfer's "engage, pause, think"; Clozemaster Radio). Play a unit's sentences as English → pause to answer aloud → target language. The content is already there: every fill-blank, dictation and sentence-builder carries `english`, and ParlourTTS voices it. Could share a player with Library item 11 (listen through a shelf). Risk: mobile browsers may pause audio with silent gaps once the screen locks, so test on real phones first (Media Session API or stitched audio).
6. **Minimal-pairs listening** (Duolingo SelectMinimalPairs / SelectPronunciation). A new Listening Driller type: hear one word, pick which of two it was. For HU: vowel and consonant length (kor/kór, szel/szél, megy/meggy). For ES: stress and r/rr (hablo/habló, esta/está, pero/perro). Needs a small hand-made pair list per language, plus a check that the Chirp3-HD voices keep each distinction. HU already has recorded human pairs (hat/hát, szel/szél, irt/írt, kor/kór, tör/tőr, hurok/húrok) in `content/hu/audio/sounds/` (`ACHIEVED.md` item 105), and `tools/sound-recorder/` can record more.
7. **Retype the answer after a reveal** (Quizlet setting "Retype correct answers"). After the 3rd miss reveals the answer, a typed step asks for it once more before Continue. This changes the lesson gating rule, so decide whether it's always on or optional.
8. **Describe-a-photo task** (Busuu: "Describe what you see in the Busuu Photo of the Week!"). A Speaking/Writing Studio prompt type graded by the existing grader. Photo description is a DELE oral task format (check the current A2/B1 spec). It has the same image-rights question as Artifacts above.
9. **Share into Parlour** (WordWise and Clozemaster quick capture; LingQ import by URL). Add a Web Share Target to `manifest.webmanifest` so text or a link shared from any app opens in My Texts, filled in. Only works for the installed PWA on Android Chrome, not iOS.
10. **Smaller ones.** Custom review that leaves the SRS schedule alone (LingoDeer: "Your actions in Custom Review won't impact your SRS schedule"); first check what Decks' Learn/Match already do. Grammar topics grouped weak / medium / strong from the learner model (Busuu grammar review). "Words read" and listening time in Journey (LingQ stats). These are counted, not estimated, so they fit Journey's rule.

Left out on purpose, so they aren't proposed again: hearts and energy, leagues, duels and leaderboards, gems, shops and paid streak repair, double-XP days, home-screen widgets (not possible for a PWA), community correction (needs moderation), AI mnemonic images, script tracing.

---

## 3. Necessary Authoring Guides & Architecture Principles

### Standing Architecture Principles

- **Core First, Enhancement Second**: Set 2026-09-10 as a permanent constraint on all future work:
  - The core learning experience — lessons, vocabulary, grammar, exercises, SRS, progress, XP, local saving, and cloud sync — must always work regardless of device quality or connection speed. Keep it lightweight: no large frameworks, no heavy assets, no animations or constant network requests as dependencies of the core.
  - Progressive enhancement: richer animations, media, and interactive elements load only when supported and must never become dependencies of the core.
- **Offline First**: The app shell and visited content are precached via Service Worker (`sw.js`) and PWA manifest (`manifest.webmanifest`). Local state updates immediately in `localStorage`; background sync must never block UI.
- **Roadmap Logging Discipline**: Every new feature, architectural enhancement, content addition, and meaningful fix must be logged directly upon completion (active items in `ROADMAP.md`, completed work archived to `ACHIEVED.md`).

### Modularity & Content Authoring Rules

- **Wiring a Unit into the Learn Tab** (as of 2026-09-16):
  - Authoring a unit's lesson/grammar/exercise/vocabulary files is not enough on its own. A level's unit titles, ordering and lesson-stem groupings are a separate, curated list, and a lesson file with nothing pointing at it is invisible to the Learn tab (this happened to the Phase 2 imperfecto content: it validated cleanly for a while before anyone wired it in).
  - For a level with an explicit table (Spanish A1/A2/B1, Hungarian B1): (1) author and validate the files as usual (`python scripts/validate-content.py`); (2) append one entry to `content/<lang>/curriculum/units/<level>.json`: `{"title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}` (add `"track": "core"` / `"latam"` / etc. only for a level that runs more than one parallel track; schema: `content/<lang>/schemas/units.schema.json`); (3) run `python build-manifest.py` (or just push — `sync-generated-content.yml` does this for anything touching `content/**`) to regenerate `curriculum.json`, `decks.json` and the story/grammar indexes.
  - `curriculum.json` is generated — never edit it by hand. No `build-manifest.py` edit is needed either: before 2026-09-16 this table lived in a hardcoded Python dict there, which is what made Phase 2's units hard to wire in after the fact.
  - A level with no such file (Hungarian A1/A2 today) auto-groups plain-numbered lesson files from disk (`auto_group_units()` in `build-manifest.py`), so there's nothing to hand-wire.
- **Adding a New Exercise Type**:
  - `engine/lessons.js`'s `stepRenderers` dispatches dynamically by step `type` (`stepRenderers[part.type](part)`).
  - A new type requires one new function in `engine/lessons.js` and one new branch in `content/<lang>/schemas/exercises.schema.json`. Existing renderers remain untouched.
- **Exercise Schemas & Teaches Tags**:
  - Exercises must conform to `exercises.schema.json` with a valid 6-value `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and a non-empty `teaches` array (for non-`reading` exercises) registered in `content/<lang>/indexes/skill-registry.json` (`es-es`: 200 grammar skills / 326 total; `es-latam`: 219 grammar skills / 347 total; `hu`: 216 grammar skills / 365 total).
  - **Aliases & Category/Kind alignment**: Retired or consolidated skill slugs stay in `"aliases": [...]` under their canonical skill in `skill-registry.json` (`scripts/validate-content.py` rejects alias slugs in `teaches` and `LearnerModel` migrates stored `productionEvidence` on load). Every `category: "vocabulary"` exercise must use a `kind: "vocabulary"` unit theme slug (e.g. `a1-unit01-vocab`) and never a `kind: "grammar"` skill (`scripts/validate-content.py` enforces this and validates that every canonical skill and alias matches `^[a-z0-9]+(-[a-z0-9]+)*$`; `scripts/build_grammar_index.py` warns if any grammar skill exceeds `150` grammar exercises or `25` aliases).
  - **Skill names (`indexes/grammar-titles.json`)**: every `teaches` slug used on a `category: "grammar"` exercise needs a name in `content/<lang>/indexes/grammar-titles.json`. Learners see it mid-sentence ("You made a few mistakes with stem-changing reflexive verbs lately."), so write it lowercase-first in plain CEFR-inventory English, with target-language forms unquoted ("estar + gerund", "ser vs estar"). No colons, dashes, slashes between phrases, unit numbers, or parentheses. A tag should name a grammar point, not a topic or story. Non-grammar skills are named `"reading"`. Both `scripts/validate-content.py` and `scripts/build_grammar_index.py --strict` enforce this (ACHIEVED.md items 89, 91, 93, 99, 100).
  - **New courses (added 2026-09-25)**: these rules apply to every course, including future ones (Polish, Czech, Slovak, French, German). A new `content/<code>/` copies the reference schemas from `content/es-es/schemas/` and gets its own `skill-registry.json` and `grammar-titles.json` before any content is written; see AGENTS.md § "Adding a new course". Once a course folder holds any lesson or exercise file, `scripts/validate-content.py` fails if its schemas or tag registry are missing, rather than silently skipping it as it used to. The build and audit scripts discover every folder under `content/`, so no hard-coded course list needs editing.
  - **Sentence Translations (`english`)**: Every `fill-blank`, `dictation`, and `sentence-builder` exercise must carry an `english` field providing the English translation of the sentence (displayed via `showTranslation()` once solved or revealed).
