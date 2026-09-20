# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Immediate Priority Queue

All active queue items have shipped. See `ACHIEVED.md` for completed work.
Candidate next items are listed in Section 2 below.

---

## 2. Future Feature Ideas

Unscoped enhancements and candidate features:

- **Cloud Sync & Multi-Device Accounts**: Automatic background cloud sync (per learner-model step 7) preserving offline-first local storage without heavy frameworks.
- **CEFR Level Diagnostic Test**: Diagnostic placement exam to assess learner proficiency upon initial app entry.
- **Exam-Focused Writing & Speech Units**: Introduce new units that expressly teach writing, particular aspects of speech, and turns of phrase for exams.
- **New App Sounds**: Audio effects and sound palette refresh.
- **Cultural Track Recommendations**: Curated cultural recommendations integrated into the cultural track.
- **Cultural Track Slang**: Slang and colloquial expressions on the cultural track.
- **ProfeDeELE Exercise Sourcing**: Source reading and other exercises from [ProfeDeELE](https://www.profedeele.es/actividad/independencia-de-mexico/).
- **Legal & Trademark**: Legal compliance, trademark registration, and administrative/bureaucratic requirements.
- **B2+ Civic Education & History Engine**: From B2 onward, build up a dedicated civic education and history engine.
- **Teacher-Facing Version & Portal**: Separate teacher log-in and teacher-facing management/monitoring version.

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
