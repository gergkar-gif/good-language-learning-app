# hu a1 `possession`: second-read fix list (2026-10-13)

After the pilot fix list and the `3rd-person-possessive` retag (c26691b9).
Second blind Sonnet read, the first with `docs/unit-agent-rules.md` in place
of the full docs (123k, 3.5 min), filtered and applied by Claude.

## Applied

- `a1-41-a-gr`: *anya*/*apa* note now "irregular in the 3rd person:
  *anyja*, *apja*, not *anyája*, *apája*".
- Lesson titles used plural possessed *dolgai/dolgaink/dolgaim* (A2) and
  unmet *dolog*: a1-41 "A kulcsa, a telefonja", a1-42 "A szobánk, a
  szobájuk", a1-45 "A saját szobám".
- `a1-45-a-gr`: "yours alone" → "your own, not shared".
- Story `a1-unit-09`: *Az autó a miénk. A kulcsa itt van.* (*kulcsa* reads as
  someone's key) → *A kulcs itt van.*
- `a1-43-controlled-4`: hint "yours" → "yours, one person".
- `a1-44-practice-6`, `a1-44-check-2`: `distractor_skills`
  `van-and-nincs-there-is-there-isn-t` moved from the tested skill's own
  form (*Van kulcsom.*, *Nincs szobánk.*) to the existence sentence (*Nincs
  kulcs.*, *Van egy szoba.*). The pilot fix list had this the wrong way round.
- Challenge scenarios a1-42, a1-44, a1-45, a1-45-consolidation now mention
  what the target talks about (room and friend, car, room and keys, key and
  bag).
- a1-45 checklist line 2 promised *saját* "with any owner" → "with my, our
  and their things".

## Not taken

- "*táskája* does not lengthen": false; *táskája*, *szobája* lengthen (the
  course spells them so 33 times).
- *-uk/-juk* items to `3rd-person-possessive`: the skill is titled
  -a/-e/-ja/-je (singular owner); keep `possessive-suffixes`.
- Story question *Kié az autó?* with *Az enyém* as a wrong option: the car is
  *a miénk*; *az enyém* is false for either speaker.
- `a1-43-practice-1` *kié* vs *hol/milyen* as vocabulary: no paradigm skill
  covers *kié*; keep.
- Shape repetition of "Which means" items; consolidation repeating a1-42
  dialogue: acceptable.
- `sajat` skill is A2 (`a2-25-b-gr`) though a1-45 teaches *saját*: items are
  tagged `possessive-suffixes` / `van-possessive-to-have`; a registry
  question for the user.
