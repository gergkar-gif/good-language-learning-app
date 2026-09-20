# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Immediate Priority Queue

1. **Finish the Spain CCSE track (`content/es-es`, `*-ccse-*` files).** Added 2026-09-20 as an
   unfinished scaffold: 210 of its 216 B1 lessons are empty stubs (`sections: []`) yet already wired
   into `curriculum/units/b1.json`, so the Spain course shows empty lessons. The 6 lessons with content
   (Constitución 01-05 + consolidation) use ids/fields the schemas reject (`lesson.b1.ccse.constitucion.01`,
   lowercase `level`, `track`, vocab `word`/`gender` instead of `lemma`, exercise files without `lesson`).
   The Sync generated content workflow was failing on every push because of this, so
   `scripts/validate-content.py` now skips `-ccse-` files in `es-es` (`SKIP_STEM_MARKERS`) and prints the
   skipped count. Remove that skip once the track is built to schema — or park the empty units out of the
   curriculum until then.

Candidate next items are listed in Section 2 below.

---

## 2. Future Feature Ideas

Unscoped enhancements and candidate features:

- **Cloud Sync & Multi-Device Accounts**: Automatic background cloud sync (per learner-model step 7) preserving offline-first local storage without heavy frameworks.
- **Onboarding & New-User Experience**: Discuss onboarding, introducing Parlour philosophy/methodology, and initial setup processes for new users.
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
