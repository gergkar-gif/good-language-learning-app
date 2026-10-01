# A1 Content Specification

> **Exercise metadata (required, validator-enforced):** every exercise needs a `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and, unless it is `reading`, a `teaches` array of canonical slugs from `content/<course>/indexes/skill-registry.json`. Vocabulary exercises take the unit's vocabulary-theme slug. Reuse existing skills; don't invent unit- or topic-specific slugs. Full rules: `AGENTS.md` § "Exercise metadata". Check with `python scripts/validate-content.py --changed`.

This document defines the minimum content required for an A1 **teaching**
lesson and for a unit's **consolidation** lesson.

**The real, enforced spec is `scripts/audit-lesson.py`, not this document.**
This file explains the rules in prose; the script is what actually checks
content and is the tie-breaker if the two ever disagree. Run
`python scripts/audit-lesson.py a1` before trusting either.

A1 is **26 units of 6 lesson files each** — five teaching lessons
(`a1-01-01.json` … `a1-01-05.json`) and one consolidation
(`a1-01-consolidation.json`) — 156 lessons total. Some unit slots are keyed
by a word slug instead of a two-digit number where the number would collide
with an old pre-restructure slot (e.g. `a1-cafe-01.json`, `a1-abilities-
01.json`); see `a1.md` for the full unit list and which slug belongs to
which unit. `content/es/lessons/a1/a1-01-01.json` is a reasonable structural
example to copy, but "reference implementation" should not be assumed —
check any candidate template against the audit script first, not just
against this doc (several shipped units, including consolidations, do not
currently pass — see the note under "Consolidation lessons" below).

---

## 1. Grammar

- 1 grammar explanation **per concept** — a lesson teaching two things gets
  one file each, and the engine renders one screen per file
- Maximum 300 words of prose per file (enforced: `GRAMMAR_MAX_WORDS`)
- 3–5 worked examples per file, when an `examples` part is present (enforced:
  `GRAMMAR_EXAMPLES`)
- A Lingolia reference (`external-link` part) is expected as the last part of
  the file; the script only warns if it's missing (e.g. a Latin America
  focus screen may legitimately skip it)
- Every bare Spanish word or phrase inside a `text`/`tip` part's prose must
  be wrapped in `*asterisks*` (`*hay*`, `*ir a* + infinitive`) — see
  `editorial-style-guide.md`'s Grammar section for the full rule. Don't wrap
  `examples`/`table` content (already italicized by CSS) and don't invent a
  Spanish word to wrap where the sentence is pure English.

The reference is written as a closing sentence, not a bare link. Give the
`external-link` part a `topic` that completes "Read more about ___ on
Lingolia.", and only the site name is hyperlinked:

```json
{ "type": "external-link", "topic": "the use of 'ser'", "site": "Lingolia",
  "url": "https://www.lingolia.com/en/grammar/verbs/irregular-verbs/ser" }
```

> Read more about the use of 'ser' on [Lingolia](https://www.lingolia.com/en/grammar/verbs/irregular-verbs/ser).

---

## 2. Core Vocabulary

Per-unit shipped totals live in `a1-vocabulary-themes.md` (that document is
authoritative and regenerated from the real vocabulary files). Units range
from 20 to 55 new words, spread across that unit's 5 teaching lessons — the
audit script does **not** enforce a fixed per-lesson word count for A1
(there is no A1 entry in its `PLAN_LOADERS`), so treat any specific
lesson-by-lesson number as a rough planning guide, not a hard target.

Every word must come from the Core Lexicon. Every new word must appear in
that lesson's own exercises (enforced by the audit script). Words are
contextualized in the unit's original story where natural, without forcing an
unnatural 100% concordance into a 100–250 word text.

---

## 3. Original Story

Required for the lesson that carries the unit's story — usually one lesson
per unit, not all five (a unit's other lessons rely on the same story for
word-coverage checking, via `unit_story_ref`'s fallback, but only the
lesson with its own `story` section gets a "Reading" exercise block). Six
units currently have no story wired into any lesson yet at all — see
`a1.md`'s note on the "—" rows.

Target length: **100–250 words**, flat across all of A1. A1 texts stay
short deliberately: a beginner reading tap-to-translate does not benefit
from length. Length may grow again at A2 and above, where it should be set
from the stories that actually get written.

Only previously introduced grammar may be used.

---

## 4. Exercises

A teaching lesson's exercises are grouped into `exercise-group` sections,
checked structurally by the audit script in this order:

| Block | Required when | What's checked |
|-------|---------------|-----------------|
| Practice | Always | Spans **4+ distinct exercise types** (typically matching, multiple-choice, fill-blank, sentence-builder) |
| Reading | Only on the lesson carrying the unit's story | Its exercises carry no `teaches` tag (they're about the story just read, not testing a recyclable point) |
| Dialogue | Always | — |
| Writing | Always | — |

A1 has no Listening block — that was introduced at A2 (see
`listening-plan` in project memory) and predates A1.

**There is no fixed total or per-block count enforced for A1** (unlike A2
and B1, which have a per-lesson plan document the script checks counts
against). Shipped lessons currently run **12–19 exercises total**: Practice
typically 8–16, Reading 1–5 (only on lessons that have one), Dialogue 2–4,
Writing 1–3. Treat these as the current shape, not a target to hit exactly.

Available exercise types are in `a1-exercises.md`; the machine-readable
definitions are `content/es/schemas/exercises.schema.json`.

**`fill-blank` hints.** When a blank is genuinely unrecoverable without a
nudge (the missing word can't be inferred from the sentence alone — a
brand-new noun, an ambiguous verb person/tense, a fixed register choice),
append a short parenthetical hint to the end of `sentence`, e.g. `"Ayer __
en el festival. (bailar)"` or `"¿Y ___? (and you?)"`. Don't add one just
because a blank is hard — only when it's genuinely unguessable; most
blanks shouldn't have one. **This is scheduled to change**: a dedicated
`hint` field is planned (see `ROADMAP.md` → Workshop → "Fill-blank
exercises should carry a real, typed `hint` field") so the hint can render
styled and distinct from the sentence instead of being silently part of
the same string. Once that field exists in `exercises.schema.json`, use it
instead of the trailing-parenthetical convention — this note will be
updated at that point.

---

## 5. Consolidation lessons

Every unit's 6th lesson is a consolidation — no new grammar, no new
vocabulary, nothing to add to SRS. The audit script enforces one specific
shape for A1 (`CONSOLIDATION_SHAPE["a1"] == "single"`):

- **No** `grammar`, `vocabulary`, or `srs` section.
- Exactly one `exercise-group` titled exactly **"Review"**.
- That group spans **5+ distinct exercise types**.
- **Every** exercise in it carries a `teaches` tag (this is what makes a
  review auditable — it's the only place grammar from Lesson 2 and Lesson
  14 can turn up in consecutive exercises).
- The union of `teaches` tags across the group covers **8+ distinct
  points** — the check that a review actually ranges across the unit
  instead of drilling one thing repeatedly.

**Not yet true of every shipped consolidation.** As of this writing only 6
of the 26 consolidation files (`a1-01`, `a1-02`, `a1-03`, `a1-03c`, `a1-04`,
`a1-10`) actually use this "Review" shape. The other 20 instead ship the
same Practice/Dialogue/Writing blocks as a teaching lesson (the shape A2
drifted to, called `"split"` in the audit script) — which means they fail
the "has a 'Review' exercise group" check. This is a real content gap, not
a documentation question; it's tracked as its own roadmap item rather than
fixed here.

---

## 6. Classic Story & World Text

Not yet started for A1. `content/es/stories/classics/a1/` and
`content/es/stories/world/a1/` don't exist — see `a1.md`'s Reading
Progression section. Any per-lesson target here would be aspirational, so
none is given; set real targets from the stories once they're actually
planned.

---

## 7. SRS

Every core vocabulary item is automatically added to the learner's SRS deck
via the lesson's `srs` section. Consolidation lessons have no `srs` section
— there are no new words to offer, and the unit's words are already in the
learner's deck.

---

## 8. Can-do Checklist

One checklist item per goal item (`goal.items` and `checklist.items` must be
the same length — enforced). Each checklist item must literally start with
**"I can"** (enforced). No fixed count is enforced, but shipped lessons
typically carry 2–4.
