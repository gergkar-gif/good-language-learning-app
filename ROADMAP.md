# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Active & Parked Priorities

1. **Progressive Authoring of Spain CCSE Track (`content/es-es`, Units 7–36):**
   - **Completed**:
     - Unit 1: *La Constitución Española de 1978*
     - Unit 2: *La Corona y la Jefatura del Estado*
     - Unit 3: *Las Cortes Generales: Congreso y Senado*
     - Unit 4: *El Gobierno y la Administración del Estado*
     - Unit 5: *El Poder Judicial y el Tribunal Constitucional*
     - Unit 6: *Las Instituciones Autonómicas y Locales*
     (Fully authored with B1 pedagogical texts, grammar modules, vocabulary, exercises with English translations, and generating SRS decks).
   - **Roadmapped / Parked for Future Cycles**: Units 7 through 36 (covering Elecciones, Fuerzas Armadas, Unión Europea, Símbolos, Derechos Fundamentales, Geografía, Historia, Cultura, y Sociedad Española).
   - **Authoring Norm**: When resuming, every unit must follow the established three-pillar standard: B1 level pedagogical clarity, 100% factual accuracy (aligned with Instituto Cervantes CCSE syllabus), and *The Rest Is History* (TRIH)-style engaging, humanized narrative storytelling with companion stories in `stories/world/b1/`.
   - `scripts/validate-content.py` maintains `SKIP_STEM_MARKERS = {"es-es": "-ccse-"}` for scaffolded stubs until all units are authored.
   - **2026-09-23 grading bug fixed**: the first multiple-choice question in every Unit 1 (Constitución) and Unit 2 (Monarquía) lesson, plus both in Unit 2's consolidation, used an `"answer": "<text>"` field instead of the `"correct": <index>` field every other exercise in the app uses — `shuffledOptions()` in `engine/lessons.js` reads `step.correct`, got `undefined`, and marked every choice wrong regardless of what the learner picked. Fixed by converting all 12 exercises to `"correct": <index>` (`content/es-es/exercises/b1/b1-ccse-constitucion-*-ex.json`, `b1-ccse-monarquia-*-ex.json`). Worth spot-checking Units 3-6 exercise files for the same `answer`-vs-`correct` drift if this recurs.

2. **Keep new features cross-referencing `design principles.md`.** The 2026-09-23 visual-identity drift sweep (`ACHIEVED.md` items 72-75) is now fully closed out — `--bg-card` (real token, pure white in light mode, apparently a vestige of the briefly-adopted-then-reversed 2026-08-14 "soft card" phase) turned out to be used nowhere else in the entire app except the newer Level Test/Diagnostic/Home-onboarding features, all now fixed. The drift consistently came from features shipping their own CSS (and inline JS styles) without checking the doc first — a general periodic check for that would prevent the same class of drift recurring.




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
  - Exercises must conform to `exercises.schema.json` with a valid `category`.
  - For recycle and recommendation systems to work, reuse consistent slug vocabulary in the `teaches` array (e.g. `"ser"`, not `"ser-verb"`).
  - **Sentence Translations (`english`)**: Every `fill-blank`, `dictation`, and `sentence-builder` exercise must carry an `english` field providing the English translation of the sentence (displayed via `showTranslation()` once solved or revealed).
