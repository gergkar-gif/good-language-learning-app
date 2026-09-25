# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Active & Parked Priorities

2. **Keep new features cross-referencing `design principles.md`.** The 2026-09-23 visual-identity drift sweep (`ACHIEVED.md` items 72-75) is now fully closed out — `--bg-card` (real token, pure white in light mode, apparently a vestige of the briefly-adopted-then-reversed 2026-08-14 "soft card" phase) turned out to be used nowhere else in the entire app except the newer Level Test/Diagnostic/Home-onboarding features, all now fixed. The drift consistently came from features shipping their own CSS (and inline JS styles) without checking the doc first — a general periodic check for that would prevent the same class of drift recurring.

4. **Explain an elective track to learners who start mid-track (added 2026-09-24).** The B1 elective tracks (es-es Cultura y Ciudadanía, es-latam Latin America, hu Citizenship) now open with a welcome screen in their first lesson (see ACHIEVED.md, "Welcome Screens for the B1 Elective Tracks"). But the elective nudge (`engine/recommendationEngine.js`, `_electiveCandidate()`) can send a learner straight to a later unit, and they never see that screen. Proposed: a one-line `description` on each track in `curriculum.json`'s `tracks` array (through `build-manifest.py`, since that file is generated), shown on the nudge card.

5. **Two new-learner notes still need a signal (added 2026-09-24).** The new-learner introduction (`ACHIEVED.md` item 87) planned two behaviour-triggered notes that weren't built, because nothing records what they'd trigger on: the **Verb Driller** note ("If a verb keeps catching you out, the Verb Driller practises just that", meant for the same verb missed three times across lessons) and the **Listening Driller** note ("Listening practice has its own space in the Workshop", meant for low listening scores). Lessons don't record which verb a miss was on, and there's no per-skill listening score. Either add those signals (e.g. note the lemma of a missed conjugation step in the learner model) or pick a different trigger. The copy is in `docs/feature-guidance-copy.md` (6a, 6b); the end-of-lesson "What's next" screen already suggests a grammar drill for a weak skill, which partly covers 6a.

101. **Fill-blank hints that repeat the answer — 80 more instances beyond the fixed 59 (added 2026-09-25).** Bug report #193 flagged `b1-precolombina-01.ex04`: the inline parenthetical at the end of `sentence` (e.g. `"...la papa se convirtió... (mientras que)"`) literally repeated the answer instead of hinting at it. Fixed that exercise plus the same pattern across ~59 other ES-LATAM B1 history-track exercises (mostly each lesson's `ex04`) by replacing the Spanish repeat with a short English gloss derived from the exercise's own `english` field (commit `8d125e09`). While auditing, found 80 more fill-blanks with the identical bug (`sentence`'s trailing `(...)` case-insensitively equals `answer`, no `[...]` bracket translation already in the sentence) that weren't fixed in this pass: about half are in the same history track's remaining lessons/consolidations (missed because they use `teaches` tags the audit script didn't classify as connector-related, e.g. plain vocabulary recall like `"(institución)"`), the other half are in the numeric `b1-02`…`b1-09` grammar-topic units, a different exercise family from the history track. Left untouched: 38 further matches that pair the parenthetical with an existing `[English sentence]` bracket already in `sentence` (e.g. `b1-06-05.ex03`) — that looks like a distinct, likely-intentional dual-hint convention, not the same bug, and wasn't in scope for #193. Before the next pass: re-run the audit (search `content/es-latam/exercises/**/*.json` for `fill-blank` where the trailing paren equals `answer` case-insensitively and `sentence` has no `[`), fix each with an `english`-derived gloss the same way, and separately check whether `es-es` and `hu` content have the same pattern (not yet audited).

92. **Audit `imports/dictionary/spanish-en.json` for more wrong-primary-sense entries (added 2026-09-24).** Bug report #192 flagged the review card for "llamas" showing "a name of several localities in Asturias, Spain" instead of the taught verb sense — not corrupted/malformed data (the 2026-09-17 audit, ACHIEVED.md item 30, already covers that class), but a real Wiktionary entry that's simply the wrong headword for a common conjugated form that also exists as its own place-name/homograph entry. Fixed via `MANUAL_OVERRIDES` in `scripts/import_dictionary.py`, same mechanism as the 2026-09-18 HU "wrong-sense gloss" fixes (ACHIEVED.md, "HU Dictionary Wrong-Sense Gloss Fixes"), but ES has never had that HU audit's equivalent systematic pass over common words' primary senses — only this one-off fix. Worth a similar targeted audit of the ES dictionary's top N frequency-ranked headwords, since `Lexicon.define()` (used directly by SRS review cards) has no conjugation-aware disambiguation and will surface whatever sense the raw dictionary file happens to carry for that exact string.

---

## 2. Future Feature Ideas

Unscoped enhancements, UX refinements, and candidate features grouped by domain (completed items archived to `ACHIEVED.md`):

### Reading Comprehension (CEFR) — key feature
Reading comprehension is one of the four skills every CEFR exam (DELE, SIELE, the Hungarian ECL/Origó exams) tests on its own, and it should be a first-class part of Parlour, not an optional extra at the end of a story.

**What exists (audited 2026-09-24):**
- **Library reader** — an unscored "Comprehension Check" block at the end of a story, rendered from `narration.pedagogical.comprehensionQuestions` (`engine/reader.js`, `renderStory()`). Coverage is patchy: ES A1 originals have 3 questions each (28 stories); the ES B1 Latin America readings have only 1 each; ES A2 (50 readings), ES B1 originals and classics, all of es-es beyond A1, and HU A1/A2 have **none**. HU B1 citizenship readings have 3 each. Answers aren't saved, scored or shown anywhere else.
- **Lessons** — a "Reading" exercise group after the lesson's story step: ES A1 16/27 story lessons, A2 27/27, B1 core 36 (297 exercises, nearly all `multiple-choice`; shared between es-latam and es-es). HU has these on only 12 B1 lessons, and none at A1/A2.
- **Level tests / diagnostic** (`content/<lang>/tests/`) — grammar and vocabulary sentence items plus writing and speaking tasks. **No reading section at all.** So nothing in the app actually measures reading at a CEFR level.

**Proposed:**
1. **A reading section in every level test** (A1/A2/B1 tests), plus a reading tier in the diagnostic, in exam-style formats: several short texts matched to people/situations, multiple choice on one longer text, a gapped text (sentences removed), and true/false/not-stated. This is the gap that most undermines the "you are B1" claim.
2. **A standard question set on every Library reading**: 3–5 questions per reading covering gist, detail, inference and vocabulary-in-context. Fill the gaps listed above (ES A2, ES B1 originals/classics, es-es, HU A1/A2), and bring the ES B1 track readings from 1 to 3–5. Questions in English at A1, in the target language from A2 onward (exam convention).
3. **Score it and remember it**: save each comprehension result, show it on the card ("Read ✓ · 4/5"), and feed a reading-skill score into the learner model/Journey alongside grammar and vocabulary.
4. **New question renderers** (one function in `engine/lessons.js` + one schema branch each, per the rule below): true/false/not-stated, match headings to paragraphs, gapped text (put the removed sentence back), order the paragraphs, match people to texts. Reusable in lessons, the Library and tests.
5. **A Reading Driller in Workshop**: timed practice in exam formats on unseen texts at your level, sharing the Count/Timed shell with the other drillers.
6. **Cross-link with Listening**: the same question renderers should serve the long-form listening modules below, so both comprehension skills are built once.


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

### Ideas from other language apps (APK scan, 2026-09-24)
Found by pulling the UI strings out of the 12 language-app APKs in `apps for ux-ui inspiration/`. The per-app inventories are in `feature-inventories/` there. Only ideas that fit Parlour and aren't already built are listed. Items 1–2 were gaps confirmed in our code, and both are now fixed.
1. ~~**Resume a lesson where you left off**~~ — built 2026-09-24, see ACHIEVED.md ("Resume a Lesson Where You Left Off").
2. ~~**Credit vocabulary when a learner tests out**~~ — built 2026-09-24, see ACHIEVED.md ("Vocabulary Credit When Testing Out"). Follow-up: words are credited as fully known. A weaker "assumed known" status could be used instead if placed learners find the Reader too generous.
3. **Word-level error hints on typed answers** (Duolingo: "You missed a word" / "You used the wrong word"; LingoDeer: "Check the word form" / "Check the word order" / "There's something extra"). `generateAnswerDiff()` already separates accent slips from typos, letter by letter. Add a word-level layer for multi-word answers. Use `Lexicon` / the HU morphology engine to spot "right word, wrong form", the most common error in a course built on conjugations and suffixes. That makes the 2nd and 3rd tries (lesson gating rule) more useful.
4. **"Can't listen right now"** (EWA: "Can't speak now" snooze for 1 hour or 1 day; LingoDeer silent mode: "don't forget to redo lesson with audio"). We have only the speaking half (`lessonSkipSpeaking()`). Add the same for listening and dictation steps. Also send snoozed steps to recycle for later: snoozed speaking steps are currently dropped from `missedSteps` in `nextLessonStep()`.
5. **Hands-free audio review** (Babbel Audio Recaps, "listen while driving, cooking, jogging"; LingoDeer Listen Along with loop, pause between items and translation modes; Language Transfer's "engage, pause, think"; Clozemaster Radio). Play a unit's sentences as English → pause to answer aloud → target language. The content is already there: every fill-blank, dictation and sentence-builder carries `english`, and ParlourTTS voices it. Could share a player with Library item 11 (listen through a shelf). Risk: mobile browsers may pause audio with silent gaps once the screen locks, so test on real phones first (Media Session API or stitched audio).
6. **Minimal-pairs listening** (Duolingo SelectMinimalPairs / SelectPronunciation). A new Listening Driller type: hear one word, pick which of two it was. For HU: vowel and consonant length (kor/kór, szel/szél, megy/meggy). For ES: stress and r/rr (hablo/habló, esta/está, pero/perro). Needs a small hand-made pair list per language, plus a check that the Chirp3-HD voices keep each distinction.
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

- **Adding Lessons to an Existing Unit**:
  - `content/<lang>/curriculum/curriculum.json` holds each unit as `{id, label, title, lessons: [...]}`.
  - Adding lessons is an array edit (new lesson JSON file with a unique ID + entry in `lessons`), not a rewrite.
  - Regenerate derived indexes afterward via `python build-manifest.py`.
- **Adding a New Exercise Type**:
  - `engine/lessons.js`'s `stepRenderers` dispatches dynamically by step `type` (`stepRenderers[part.type](part)`).
  - A new type requires one new function in `engine/lessons.js` and one new branch in `content/<lang>/schemas/exercises.schema.json`. Existing renderers remain untouched.
- **Exercise Schemas & Teaches Tags**:
  - Exercises must conform to `exercises.schema.json` with a valid 6-value `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and a non-empty `teaches` array (for non-`reading` exercises) registered in `content/<lang>/indexes/skill-registry.json` (`es-es`: 200 grammar skills / 326 total; `es-latam`: 219 grammar skills / 347 total; `hu`: 216 grammar skills / 365 total).
  - **Aliases & Category/Kind alignment**: Retired or consolidated skill slugs stay in `"aliases": [...]` under their canonical skill in `skill-registry.json` (`scripts/validate-content.py` rejects alias slugs in `teaches` and `LearnerModel` migrates stored `productionEvidence` on load). Every `category: "vocabulary"` exercise must use a `kind: "vocabulary"` unit theme slug (e.g. `a1-unit01-vocab`) and never a `kind: "grammar"` skill (`scripts/validate-content.py` enforces this and validates that every canonical skill and alias matches `^[a-z0-9]+(-[a-z0-9]+)*$`; `scripts/build_grammar_index.py` warns if any grammar skill exceeds `150` grammar exercises or `25` aliases).
  - **Skill names (`indexes/grammar-titles.json`)**: every `teaches` slug used on a `category: "grammar"` exercise needs a name in `content/<lang>/indexes/grammar-titles.json`. Learners see it mid-sentence ("You made a few mistakes with stem-changing reflexive verbs lately."), so write it lowercase-first in plain CEFR-inventory English, with target-language forms unquoted ("estar + gerund", "ser vs estar"). No colons, dashes, slashes between phrases, unit numbers, or parentheses. A tag should name a grammar point, not a topic or story. Non-grammar skills are named `"reading"`. Both `scripts/validate-content.py` and `scripts/build_grammar_index.py --strict` enforce this (ACHIEVED.md items 89, 91, 93, 99, 100).
  - **Sentence Translations (`english`)**: Every `fill-blank`, `dictation`, and `sentence-builder` exercise must carry an `english` field providing the English translation of the sentence (displayed via `showTranslation()` once solved or revealed).
