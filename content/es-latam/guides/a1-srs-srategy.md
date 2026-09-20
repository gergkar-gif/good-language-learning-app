# A1 Review Strategy

Rewritten 2026-08-07. The previous version described fixed intervals and said
grammar was "reviewed through lesson exercises"; the engine now schedules
words with SM-2, and lesson exercises never repeated, so grammar was in
practice never reviewed at all. This document describes both halves.

## Objective

Reinforce two different things, which need two different mechanisms:

| What | Mechanism | Where the learner meets it |
|------|-----------|----------------------------|
| **Words** | SRS deck, scheduled per card | The Decks section, any time |
| **Grammar and skills** | Recycled exercises from earlier lessons | A recycle block at the start of each lesson |

Reviewing words alone is not sufficient. A learner can know that `soy` means
"I am" and still be unable to say where they are from.

---

## 1. Vocabulary — the SRS deck

### Core principles

- Every new core word is offered to the learner's deck at the end of its lesson.
- The learner ticks which words to add; words already in the deck are skipped.
- Story-only words are **not** added automatically — they can be tapped and
  added from the reader by hand.
- A word can only exist once in the deck.
- Words are reviewed independently of lessons.

### Scheduling

Cards are scheduled with **SM-2** (`engine/srs.js`), not fixed intervals.
Each card carries an ease factor starting at 2.5 and clamped to 1.3–3.0.

| Rating | Ease | Next interval |
|--------|------|---------------|
| Again | −0.20 | 1 minute, interval and review count reset |
| Hard | −0.15 | interval × 1.2 |
| Good | unchanged | interval × ease |
| Easy | +0.15 | interval × ease × 1.3 |

The first two successful reviews use a fixed ramp (1 day, then 6) before the
ease factor takes over. Intervals are capped at 365 days.

Reviewing a card early earns a smaller step than letting it come due, and can
never shorten the schedule — so cramming does not inflate a deck.

### Graduation

A word is never finally "done". Successful reviews push it further out, up to
the yearly cap. `reviews >= 3` is what colours it as mastered in the reader.

---

## 2. Grammar and skills — recycled exercises

The problem this solves: a lesson's exercises are answered once and never seen
again. `ser` is taught in Lesson 1 and, without this, never deliberately
returns.

### The recycle block

Every lesson opens with a short **recycle block** — 2 to 3 exercises drawn
from *earlier* lessons — before any new material. It sits between the goal
screen and the first grammar screen, so the learner warms up on what they
already know before meeting anything new.

```
goal → recycle (2-3) → grammar → practice (6) → vocabulary → story
     → reading (4) → dialogue (3) → writing (2) → srs → checklist
```

The recycle block is **not** part of the lesson's own 15 exercises. It is
assembled at runtime from lessons the learner has already completed, so:

- Lesson 1 has nothing to recycle and shows no block.
- The block is scheduled per exercise, using the same SM-2 code as cards, so
  it surfaces what that learner actually got wrong rather than a fixed list.
- Nothing new has to be authored for it.

This replaces the authorial recycling in `a1-grammar.md`, where four lessons
are marked "(recycled)". That is worth keeping as a content-design signal, but
it is fixed at authoring time and blind to the individual learner.

### Which exercises can be recycled

An exercise is eligible if it carries a `teaches` tag naming the concepts it
tests. Exercises with no `teaches` tag are never recycled.

That rule exists mainly for **reading exercises**: they ask about one specific
story, so they only make sense to a learner who has just read it. Practice,
dialogue and writing exercises are skill-based and travel fine.

### The `teaches` tag

```json
{ "id": "a1-01-practice-blank", "type": "fill-blank",
  "teaches": ["ser"], … }
```

Values are lowercase hyphenated slugs, taken from the lesson's **Grammar**
column or **Vocabulary Theme** in `guides/a1.md`. Keep them consistent across
lessons — `ser` tagged in Lesson 1 is what lets Lesson 5 recycle it.

---

## Lesson requirements

Every core vocabulary item must:

- appear in the vocabulary list.
- appear in the original story.
- appear in at least one exercise.
- be offered to the SRS deck.

Every practice, dialogue and writing exercise must carry a `teaches` tag.
Reading exercises must not.

`scripts/audit-lesson.py` checks the vocabulary rules today. The `teaches`
rules are not yet enforced.

---

## Implementation status

| Piece | State |
|-------|-------|
| SM-2 card scheduling | built (`engine/srs.js`) |
| SRS step offering lesson words | built |
| `teaches` tag on exercises | schema supports it; tagged in lessons 1–2 |
| Per-exercise scheduling | **not built** |
| Recycle block in lessons | **not built** |
