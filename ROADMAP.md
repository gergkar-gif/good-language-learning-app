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

2. **2026-09-23 Communicative Challenge reshuffle (Tier 1)**: The challenge card had it backwards — the bold headline was the generic CEFR task description (e.g. "Ask for a coffee and water politely"), while the actual sentence to produce was buried inside the "Points to include" bullet list. For Tier 1 (A1, single-target) challenges, the card now leads with "Say this in {language}:" plus the English sentence to translate; the CanDo/task framing moved to the post-solve success message ("Well done! With this, you've completed a CEFR A1 requirement: '...'"). Added an `english` field to the challenge step shape (`engine/lessons.js`, `content/*/schemas/lesson.schema.json`, `content/es-latam/curriculum/challenges.json`) carrying that source sentence. Tier 2/3 (situational, multi-cue, no single target sentence) were intentionally left unchanged — worth revisiting later whether they need the same canDo-framing-moved-to-completion treatment for consistency.

3. **Keep new features cross-referencing `design principles.md`.** The 2026-09-23 visual-identity drift sweep (`ACHIEVED.md` items 72-75) is now fully closed out — `--bg-card` (real token, pure white in light mode, apparently a vestige of the briefly-adopted-then-reversed 2026-08-14 "soft card" phase) turned out to be used nowhere else in the entire app except the newer Level Test/Diagnostic/Home-onboarding features, all now fixed. The drift consistently came from features shipping their own CSS (and inline JS styles) without checking the doc first — a general periodic check for that would prevent the same class of drift recurring.




---

## 2. Future Feature Ideas

Unscoped enhancements, UX refinements, and candidate features grouped by domain (completed items archived to `ACHIEVED.md`):


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
