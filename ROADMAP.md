# Roadmap

Active development priorities, future feature ideas, and authoring guides.
Completed work is archived out to `ACHIEVED.md`.

---

## 1. Immediate Priority Queue

Active work in progress and prioritized backlog items:

26. **Vocabulary Driller: scoped session dead-end fixed** — Launching the driller pre-scoped to a specific word list whose words lack example sentences hit a dead end: "No example sentences for these words yet". UI fallback reworded to mount `RecommendationEngine.mountNextAction()` + "Back to Workshop". However, a systemic content gap remains: ~54% of Spanish and ~63% of Hungarian deck words have no corpus sentence the driller can use, plus ~40 Spanish deck entries keyed to a surface form (`soy`, `alto/alta`) that fail lemma matching. Needs a scoped content generation/backfill pass.
36. **Exercise-type variety: audit calibrated & scope narrowed to 45 A2 lessons** — **Audited 2026-09-18.** Scoping revealed that A1/A2 lessons were designed with dedicated functional blocks (`Practice` [4 core types] + `Dialogue` [dialogue-complete] + `Writing` [structured-writing] + `Listening` [listening-choice, dictation]), spanning 6 to 8 distinct types lesson-wide. `scripts/audit-lesson.py` calibrated to `MIN_PRACTICE_TYPES = 4` and now checks `MIN_LESSON_TYPES = 5` across blocks. All 132 A1 lessons and 100 A2 lessons pass. Remaining scope narrowed to just 45 lessons (the 9 named A2 units: `condicionalsimple`, `subjuntivobasico`, etc.) where Dialogue/Writing collapsed into generic `fill-blank`s, ready for targeted enrichment.
37. **New vocabulary frequently never appears in its own unit's story** — 55% of A1, 59% of A2, and a large share of B1 lesson-parts fail "every new word appears in the unit's story" — the single largest-volume content gap found. Needs a scoped story backfill pass per level, starting with A1.
38. **A2 lessons systemically show "2 goals vs 1 checklist item"** — 123/174 A2 lesson-parts exhibit this pattern. Check `guides/a2-lesson-guide.md` before batch-editing either side to determine if combining goals into one checklist line was intentional.
39. **ES teaching-order flags triaged: 731 total, 86% real** — `scripts/triage-teaching-order.py` splits flags into `real-gap-candidate` (626), `wrong-distractor-only` (100), and `english-leak` (5). B1 holds 537 candidates. In progress (separate agent).
40. **Hungarian teaching-order checker expansion** — `scripts/audit-lesson-hu.py` + `triage-teaching-order-hu.py` operational for agglutinative Hungarian morphology. Remaining: HU equivalents of Spanish structural audit rules (exercise variety, checklist phrasing, consolidation shape design).

---

## 2. Future Feature Ideas

Unscoped enhancements and candidate features:

- **CEFR Real-Exam Practice Mode (Queue Item 9)**: Source or generate actual CEFR-aligned exams with graded responses (under Grammar reference / Level test area).
- **Dual-Language Reading Setup (A1 Spanish)**: Integrate English-Spanish dual-language reading setup with originals, matching the setup in Hungarian.
- **Hungarian B1/B2 Citizenship Track (Units 6–36)**: Complete remaining 31 units per track (Core + Citizenship history sweep through EU accession and 4 civic units: Alaptörvény, government institutions, national symbols, holidays). Units 1–5 built; draft in `content/hu/b1-curriculum-draft.json`.
- **HU B1 Citizenship Track Word Count Trim**: 40 new words per unit across built units (`unit.b1.citizenship.01-05`) is too dense. Trim or pace vocabulary load across remaining units 6–36.
- **Sentence-Builder / Sentence-Order Mini-Game**: Short-format drill runner using unscrambling mechanics for clause structure practice.
- **Cloud Sync & Multi-Device Accounts**: Automatic background cloud sync (per learner-model step 7) preserving offline-first local storage without heavy frameworks.
- **CEFR Level Diagnostic Test**: Diagnostic placement exam to assess learner proficiency upon initial app entry.

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
