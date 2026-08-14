# Latin America unit generation brief

A short, reusable brief for generating one Latin America unit's 23 content
files (6 lessons, 6 exercise files, 5 grammar/Focus files, 5 vocabulary
files, 1 story). Read this first — it points at the docs that carry the
actual rules rather than repeating them, so it stays a few minutes' read
even though the rules behind it don't fit in a few minutes.

## 1. Read these, in this order

1. `content/es/guides/b1-content-spec.md` **§1-§2** — file layout and
   section order. Same for both tracks.
2. `content/es/guides/b1-content-spec.md` **§3** — the Focus screen shape,
   and the one grammar-extension point every unit now needs (voz pasiva,
   se pasiva/impersonal, gerundio for parallel action, or formal
   connectors — pick one per lesson, vary across the unit's five).
3. `content/es/guides/b1-content-spec.md` **§3a** — the Core↔Latin America
   pairing table. Look up this unit's number; if it has a paired Core
   unit, deliberately expand that Core unit's vocabulary domain (§4) with
   words the paired unit doesn't already teach. If it says
   *cumulative only*, skip straight to checking `decks.json`.
4. `content/es/guides/b1-content-spec.md` **§5a** — the register floor.
   At least half the Spanish in the Focus screen's examples, the story,
   every Dialogue exercise, structured-writing answers, and Consolidation
   must combine two clauses (a connector, a relative clause, a
   comparison) — not a run of isolated simple declaratives. This is what
   Unit 1 got wrong the first time; read the before/after examples there.
5. `content/es/guides/b1-content-spec.md` **§9**, items 12-17 especially —
   these are bugs that actually shipped in *every* batch so far
   (missing `teaches` tags, `exerciseRefs` pointing at the wrong
   category, missing Reading blocks, only 2 worked examples instead of
   3-5, zero grammar taught). Check for all of them before calling a unit
   done.
6. `content/es/guides/Parlour B1 Consolidated Unit List.md`, **Part II**
   — find the unit by number for its six lesson titles, each lesson's
   `Focus:` line (the subject of that lesson's Focus screen), and the
   per-lesson word counts (`New words:`).

## 2. Use Unit 1 as the worked example

`content/es/lessons/b1/b1-precolombina-*.json`, `content/es/grammar/b1/
b1-precolombina-*-gr.json`, `content/es/exercises/b1/b1-precolombina-*-ex.json`,
`content/es/vocabulary/b1/b1-precolombina-*-voc.json`, and
`content/es/stories/world/b1/b1-precolombina.json` were rewritten against
this exact brief and pass both validators cleanly. When in doubt about
tone, sentence complexity, how a grammar-extension point should read
alongside historical content, or the teaches/exerciseRefs wiring, match
what Unit 1 actually does rather than re-deriving it from the spec text
alone.

## 3. Before handing back a unit

Run both of these yourself and include the literal output:

```bash
python scripts/validate-content.py
python scripts/audit-lesson.py b1-{unit-slug}
```

A unit isn't done because `validate-content.py` is green — most of §9's
pitfalls (12-16 especially) pass schema validation while still being
wrong. `audit-lesson.py` catches the rest, and a couple of things
(exerciseRefs-vs-category, the register floor) need a manual read since
no script checks them.

## 4. Output

One zip per unit, named `parlour_b1_unit{NN}_latam.zip` (unit number, not
name — e.g. `parlour_b1_unit5_latam.zip` for "La sociedad colonial"),
containing the 23 files at their real repo-relative paths so they extract
straight into place.
