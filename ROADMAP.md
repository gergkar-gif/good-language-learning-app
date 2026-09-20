# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Active & Parked Priorities

1. **Progressive Authoring of Spain CCSE Track (`content/es-es`, Units 3–36):**
   - **Completed**: Unit 1 (*La Constitución Española de 1978*) and Unit 2 (*La Corona y la Jefatura del Estado*) are fully authored, schema-validated, and generating SRS decks and translation indexes.
   - **Roadmapped / Parked for Future Cycles**: Units 3 through 36 (covering Cortes Generales, Gobierno, Poder Judicial, Organización Territorial, Derechos Fundamentales, Geografía, Historia, Cultura, y Sociedad Española).
   - **Authoring Norm**: When resuming, every unit must follow the established three-pillar standard: B1 level pedagogical clarity, 100% factual accuracy (aligned with Instituto Cervantes CCSE syllabus), and *The Rest Is History* (TRIH)-style engaging, humanized narrative storytelling with companion stories in `stories/world/b1/`.
   - `scripts/validate-content.py` maintains `SKIP_STEM_MARKERS = {"es-es": "-ccse-"}` for scaffolded stubs until all units are authored.

---

## 2. Future Feature Ideas

Unscoped enhancements and candidate features:

- **Google Sign-In & Multi-Device Sync**: Introduce 1-tap Google Sign-In alongside the email magic link. Enables fast login without waiting for email delivery, verifies email via OpenID Connect token in Cloudflare Worker, and maps seamlessly to the existing D1 SQL database and JWT session architecture.
- **Automatic Background Cloud Sync**: Shipped 2026-09-20 (see ACHIEVED.md queue item 58).
- **Peninsular Adaptations & Active *Vosotros* Practice**: Shipped 2026-09-20 (see ACHIEVED.md queue item 57).
- **Onboarding & New-User Experience**: Shipped 2026-09-20 (casual philosophy, encounter-based coach notes, 6-room modal, power imports, deferred sync prompt — see ACHIEVED.md queue item 56).
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
