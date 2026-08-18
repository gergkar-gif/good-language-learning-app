# Multi-Language Readiness Audit

A sweep of the whole app (2026-08-18) for places still assuming the course is
Spanish, beyond the Lexicon/generated-index gap already documented in
`HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md`. That brief covers *data* — this
covers everything else: UI copy, feature gating, storage.

## Fixed in this pass

**Workshop's Verb Driller now hides itself for a course it can't serve.**
`imports/verbs/verb-list.js` is a plain global script with zero language
scoping — before this fix, a Hungarian learner opening Verb Driller would
have silently drilled *Spanish* conjugation under a Hungarian course. Wrong
content, not just missing content, which is worse than the other four
drillers (their generated indexes fail gracefully to an honest empty pool
today). `engine/workshop.js`'s `DRILLERS` array now carries an optional
`langs` field; `Verb Driller` is `langs: ['es']` and is filtered out of the
picker (and defensively re-checked in `render()`) for any other course. The
other four stay visible — once the generated-index relocation in the Reader
brief lands, they start serving real per-language content with no further
gating needed here.

**Hardcoded "Spanish" UI copy**, swapped for `Lang.name()` (or, for
`page-header.js`, upgraded `subtitle` to support a function the same way
`title` already did, then made Lessons' subtitle one):

| File | What said "Spanish" |
|---|---|
| `engine/page-header.js` | Lessons tab subtitle ("Your Spanish course.") |
| `engine/workshop.js` | Listening Driller's own sub-label |
| `engine/drills/translation.js` | Direction dropdown options, prompt label |
| `engine/drills/listening.js` | Settings-screen hint text |
| `engine/drills/vocabulary.js` | Settings-screen hint text |
| `engine/decks.js` | "Search in Spanish or English…" placeholder |
| `engine/library.js` | My Texts paste placeholder + blurb |

Two placeholder examples (a deck-name example, a My-Texts title example)
referenced specifically Spanish topics ("Spanish for Mexico", "La Revolución
Mexicana") — these aren't really *about* the course language, just flavour
text that happened to lean Spanish, so they were swapped for
language-neutral examples ("Travel essentials", "A Short History") rather
than made dynamic.

## Confirmed already correct — not bugs

- **Storage.** Every per-course key (`progress`, `myDecks`, `savedReadings`,
  `myTexts`, `readStories`, `recycleSchedule`, level-test results) goes
  through `Lang.key()`. XP/streak (`spanishApp_xp`) and the review
  direction/mode toggles (`app_reviewDirection`, `app_reviewMode`) are
  deliberately global across courses — that's documented, existing policy
  (a study habit and a study-style preference respectively, not course
  data), not an oversight.
- **Voice/speech.** Already fully routed through `Lang.voices()` — confirmed
  live, a Hungarian session picks a real Hungarian system voice
  ("Microsoft Szabolcs") with no code changes needed.
- **Content paths for lessons/stories/curriculum/decks.** All go through
  `Lang.content()` already.
- No other explicit `=== 'es'` branches exist anywhere outside `engine/lang.js`
  itself and the one documented fallback in `engine/curriculum.js`
  (`loadCurriculumData()`'s empty-content recovery).

## Still open (tracked elsewhere, not duplicated here)

- **Generated indexes** (`grammar-index.json`, `translation-index.json`,
  the Lexicon's four files) are hardcoded to top-level paths, not
  `Lang.content()`-scoped. This is the big one — see
  `HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md`'s "Wider scope" section.
- **`engine/verbs/`** needs an actual rewrite for Hungarian's
  definite/indefinite conjugation, not a data swap — see
  [[multi-language-plan]]. `Content.verb()` in `engine/content-loader.js`
  deliberately still hardcodes `imports/verbs/`; leave it until that rewrite
  happens.
- **`scripts/audit-lesson.py`** is Spanish linguistics in Python (article
  regex, a Spanish stemmer, a proper-noun list) — a content-authoring tool,
  not runtime, so it's out of scope for "is the app open to multiple
  languages" but will need its own Hungarian-aware version (or an
  acknowledgment that Hungarian content isn't auditable the same way) before
  Hungarian content authoring can lean on it the way Spanish does.
- **Cosmetic:** `engine/srs.js` names its review-state variable
  `reviewExpectedSpanish`. Purely internal, not user-facing, but worth a
  rename to something language-neutral next time that file is touched.

## Net effect

Every remaining gap the app has for a second language is now one of exactly
three kinds, each already tracked: the generated-index/Lexicon data layer
(Reader brief), the verb-conjugation engine (needs a rewrite, not scoping),
and the Python content-authoring tooling (not runtime). Nothing else in the
running app assumes Spanish anymore.
