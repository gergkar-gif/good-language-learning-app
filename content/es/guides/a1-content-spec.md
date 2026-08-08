# A1 Content Specification

This document defines the minimum content required for every A1 **teaching**
lesson — lessons 1 to 17.

Lessons 18, 19 and 20 are **review lessons** and are deliberately out of scope.
They introduce no new words and no new grammar, so almost none of the rules
below apply to them: they need their own format, which has not been designed
yet. `scripts/audit-lesson.py` skips them rather than reporting failures
against rules that were never meant for them.

`content/es/lessons/a1/a1-01.json` is the reference implementation. It passes
`scripts/audit-lesson.py`, `scripts/validate-content.py` and
`build-manifest.py`, and later lessons should copy its shape.

---

## 1. Grammar

- 1 grammar explanation **per concept** — a lesson teaching two things (Lesson 1 is greetings *and* `ser`) gets one file each, and the engine renders one screen per file
- Maximum 300 words of prose per file
- 3–5 worked examples per file
- 1 Lingolia reference per file, as the **last** part of the file

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

Exact per-lesson targets live in `a1-vocabulary-themes.md` (that document is authoritative). Roughly:

- Lesson 1–2: 10 words
- Lesson 3–4: 12 words
- Lesson 5–6: 15 words
- Lesson 7–8: 18 words
- Lesson 9–17: 20 words
- Lesson 18–20: Review only

Every word must come from the Core Lexicon.

---

## 3. Original Story

Required.

Target length: **100–250 words**, flat across all of A1.

Revised 2026-08-07. The previous version escalated the target across the level
(100–150 rising to 400–600), but the twenty stories that exist range from 106
to 225 words with no upward trend — lessons 13–17 are among the shortest. The
escalating bands described a curriculum nobody had written, and holding the
stories to them would have meant rewriting eleven of them and roughly
quadrupling the last three. A1 texts stay short deliberately: a beginner
reading tap-to-translate does not benefit from length.

Length may grow again at A2 and above, where it should be set from the stories
that actually get written.

Only previously introduced grammar may be used.

---

## 4. Exercises

Exactly 15 exercises, grouped into four blocks. Revised 2026-08-07 from the
previous 9; the blocks below are the `exercise-group` sections in the lesson
file, in this order.

| Block | Count | Where it sits |
|-------|------:|---------------|
| Practice | 6 | After the grammar screens, before the vocabulary list |
| Reading | 4 | After the story |
| Dialogue | 3 | After reading |
| Writing | 2 | Last, before SRS |

The Practice block must span **at least 5 distinct exercise types** — a block
of six that is four matchings and two fill-blanks does not qualify. Available
types are in `a1-exercises.md`; the machine-readable list is
`content/es/schemas/exercises.schema.json`.

Practice draws on the vocabulary that is formally presented in the next
section, so those six exercises are the learner's first contact with the
words.

---

## 4b. Split lessons

A slot whose grammar is too much for one sitting is split into **parts** —
`a1-03a`, `a1-03b`, `a1-03c` — added 2026-08-08, when Lesson 3 turned out to
need three grammar screens (articles, `presentar`, `ser` + adjective) before a
single exercise. Three short classes teach that better than one long one.

The parts share the slot, so Lesson 4 is still Lesson 4: the lesson row number
comes from the filename (`label` in `curriculum.json`), not from the row's
position in the list.

A part is a whole lesson — its own goals, one grammar screen, its own
vocabulary and SRS step, its own checklist — but a shorter one:

| Block | Per part | Where it sits |
|-------|---------:|---------------|
| Practice | 4 | After the grammar screen, before the vocabulary list |
| Reading | 4 | **Only in the part that carries the story** |
| Dialogue | 1 | After reading |
| Writing | 1 | Last, before SRS |

And across the unit:

- The slot's word target is **split evenly** between the parts (Lesson 3: 12 → 4 + 4 + 4). Give each part the words its own grammar screen uses.
- **Exactly one part carries the story**, normally the last, so the text is read once, when the learner knows all of the slot's words. The other parts' words must still appear in that story.
- Practice spans **3+ distinct types** per part rather than 5, since a part has four exercises rather than six.
- 2–4 checklist items per part, still one-to-one with its goals, still beginning "I can".
- Each part gets its own row in `a1.md`, keyed `3a`, `3b`, `3c` — `audit-lesson.py` matches title, goal and grammar against it exactly as for a whole lesson.

---

## 5. Classic Story

| Lessons | Required |
|---------|----------|
| 1–9 | No |
| 10 | Yes |
| 11–20 | Yes |

Target length:

100–300 words.

---

## 6. World Text

| Lessons | Required |
|---------|----------|
| 1–10 | No |
| 11–20 | Yes |

Target length:

75–200 words.

---

## 7. SRS

Every core vocabulary item is automatically added to the learner's SRS deck.

---

## 8. Can-do Checklist

Exactly four checklist items.

Each must begin with:

> I can...
