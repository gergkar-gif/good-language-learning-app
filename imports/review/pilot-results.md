# Pilot results: regenerate vs fix (ROADMAP 149 step 3, 2026-10-10)

Three arms on HU A1. Units 8–15 turned out to be template stubs (every
lesson's two grammar screens are the same two placeholder screens), so all
three arms start from stubs. Each arm's result gets the same blind Sonnet
read (the second-read prompt from `docs/unit-second-read.md`), filtered by
Claude into real defects.

| | A: Sonnet regenerates | B: Sonnet read → fix list → Sonnet fixer | C: Antigravity regenerates |
|---|---|---|---|
| Unit | 8 `plurals-quantities` | 9 `possession` | 11 `where-things-are` |
| Work time | 16 min | read 7.5 min + fixer 23 min (+ Claude's filtering) | … |
| Sonnet tokens | 251k | read 159k + fixer 298k = 457k | 0 |
| Checker after | 0 errors, 0 suspects | 0 errors, 0 suspects | … |
| Blind read (tokens) | 153k, 4.5 min | ~150k | … |
| Real defects found by the blind read | ~21, none serious | ~14, none serious | … |

## Arm A: defects the blind read found (filtered)

All are rule-fit or metadata; no Hungarian errors, no unmet words.

- Grammar screens (3): `a1-37-a-gr` ö/ü note hides that *könyv* → *könyvek*
  is an exception; `a1-38-b-gr` tip compares with Spanish/French (the learner
  knows only English); `a1-40-b-gr` third example has no *mind*.
- Answer copied from the question (2): `a1-37-dialogue-1`,
  `a1-40-consolidation-14` (*A székek nagyok?* → *Igen, nagyok.*).
- Wrong option breaks the noun's number, not the tested adjective position
  (5): `a1-38-introduce-2`, `-controlled-4`, `-check-2`, `a1-39-practice-1`,
  `a1-40-consolidation-13`.
- Missing `distractor_skills` `plural-predicate-adjectives-k` on *a nagyok
  asztalok*-type options (6): `a1-38-introduce-2`, `-controlled-4`,
  `-dialogue-1`, `-check-2`, `a1-39-practice-1`, `a1-40-consolidation-13`.
- Wording (3): `a1-38-dialogue-1` (unprompted *kicsi*), `a1-40-reading-3`
  ("asks"), `a1-38` challenge scenario (asks *where*, target says
  *together*).
- `a1-40-consolidation` challenge practises checklist line 2, `canDo` is
  line 1 (1).

Not taken: the i/í simplification, *vannak* echoed from the question stem,
*gyerekek* in a1-36, re-listed vocabulary (frozen units do the same),
near-duplicate items, `egyutt-together` scope, recall-hint tags.

Arm A's own notes: comprehension questions written in English (older stories
use Hungarian); some 2-option items; non-word harmony options (*könyvok*),
single-fault.

## Arm B notes

The unit was a stub, so the fix list was a rewrite plan (new screens, story,
most exercises); the fixer rewrote under the existing ids and kept the old
consolidation shape (6/6/4/4, 4 `teaches` tags). It taught the 3rd-person
possessive (*kulcsa*, *telefonja*) on `a1-41-a-gr` as the list asked, though
the registry has `3rd-person-possessive` at A2 (`a2-12`): a registry
question for the user.

## Arm B: defects the blind read found (filtered)

No wrong forms or answers.

- Grammar screen wording (4): `a1-41-a-gr` calls *anyja*/*apja* exceptions to
  the wrong rule (they don't lengthen); no linking-vowel sentence in a1-41
  (*kulcs → kulcsom*); `a1-43-a-gr` "leave the noun out" (it replaces
  *kulcsom*, not the noun); a1-45 drops *egy* with *saját* unexplained.
- Exercises (3): `a1-43-practice-2` hint "your" also fits *címetek* ("your,
  one person"); `a1-44-practice-5` *Kié a táska?* ruled out by *Igen*; odd
  pair *A nevünk szép.* in `a1-42-practice-3`.
- Metadata (3): `a1-45-consolidation-12` vs `a1-45-writing-1` (same
  sentence, different skill); `a1-44-check-2` option 2 entry; "Which means
  'mine'?" items `grammar` while the matching twins are vocabulary.
- Challenge English (4): a1-41 "her" ambiguous (name Anna); a1-42 says
  "your" for *szobánk* (our); a1-43 and the consolidation say "yours" where
  the target is *az enyém* (mine).

Not taken: *tiéd* gloss, an easy but correct a1-45-practice-5, the polarity
`distractor_skills` entry, single-answer structured writing (not graded),
substitution items rendering as "[object Object]" (to check in
`render_lesson.js`, not content).
