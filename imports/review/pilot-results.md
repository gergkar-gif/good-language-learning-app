# Pilot results: regenerate vs fix (ROADMAP 149 step 3, 2026-10-10)

Three arms on HU A1. Units 8–15 turned out to be template stubs (every
lesson's two grammar screens are the same two placeholder screens), so all
three arms start from stubs. Each arm's result gets the same blind Sonnet
read (the second-read prompt from `docs/unit-second-read.md`), filtered by
Claude into real defects.

| | A: Sonnet regenerates | B: Sonnet read → fix list → Sonnet fixer | C: Antigravity regenerates |
|---|---|---|---|
| Unit | 8 `plurals-quantities` | 9 `possession` | 11 `where-things-are` |
| Work time | 16 min | read 7.5 min + fixer 23 min (+ Claude's filtering) | 30 min (07:04–07:34) |
| Sonnet tokens | 251k | read 159k + fixer 298k = 457k | 0 |
| Checker after | 0 errors, 0 suspects | 0 errors, 0 suspects | 0 errors, 0 suspects |
| Blind read (tokens) | 153k, 4.5 min | 144k, 5 min | 140k, 4 min |
| Real defects found by the blind read | ~21, none serious | ~14, none serious | ~45, several serious |

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

## Arm C: defects the blind read found (checked)

- **Answers that teach a misspelling (4):** `a1-51-check-2`, `a1-52-check-2`,
  `a1-54-check-2`, `a1-55-check-2` put the blank on the bare stem
  (*hálószoba____*, answer *ban*), so the learner builds *hálószobaban*,
  *irodaban*, *utcaban*, *táskaban* (the vowel lengthens: *-ában*). The
  checker can't see this yet.
- **Unmet wrong options (~25 items, 33 options):** *-ba/-be*
  (`movement-with-ba-be`, taught a1-56) in nearly every choice item, plus
  *konyhán*, *utcánál*, *könyvtáron*, *teremen*, *nappalin*.
- **Grammar screens kept as stubs:** the same two screens in all five
  lessons; their rules are wrong or misleading (*fürdőszoba* takes *-ban*
  against "front vowels take -ben"; *i* listed as a *-ben* vowel; "*van*
  goes last" next to *Hol van a táska?*; an "anchor word" tip whose anchors
  are both *-ban* words). *-ben* rests on one noun (*terem*); no screen says
  that final *-a/-e* lengthens (*szobában*).
- ***utcában*** for "on the street" (natural: *utcán*) in the story and four
  items; a shop "in the street", an office "in the house".
- Two right answers (`a1-55-consolidation-7`, *egy iroda*); word salad
  (`a1-54-practice-4`, `a1-55-practice-4`); non-sequitur replies
  (`a1-51-dialogue-2`, `a1-52-dialogue-2`, consolidation-12); ungrammatical
  options tagged `ki-and-mi` (`a1-51-introduce-2`, `a1-55-introduce-2`).
- Challenges a1-51, a1-55: someone else answers in the scenario, the learner
  says both; a1-54 goal line promises "on the street".

Antigravity followed the brief, which said to keep the grammar screens
(written before the stubs were found); Sonnet in arm A rewrote them
unprompted.

## Verdict

- **Sonnet regeneration (A) is the best route for stub units:** half the
  time and tokens of the fix route (B) at the same quality, and no read
  needed before it. Each regenerated unit still gets one blind read and a
  small fix pass (about 20 small items) before freezing.
- **The fix route (B)** is right for units with real content (units 4–7):
  there it fixed 20–30 defects without rewriting.
- **Antigravity regeneration (C)** costs no Claude tokens and was fast
  (30 min), but left about twice as many defects, several serious (a taught
  misspelling, wrong rules on screen, an untaught case in a third of the
  options). Getting it to A's level would take a read and a fix pass on top,
  about arm B's cost.
- **New check:** a fill-blank whose blank is glued to a stem
  (`hálószoba____` + `ban`) should look up the joined word with the Reader's
  lexicon and flag a non-word.
