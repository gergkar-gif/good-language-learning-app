# HU B2 core batch: Units 5, 7, 9 (reader A) and 11, 13, 15 (reader B), 2026-10-30 → 2026-11-04

Both readers stopped at the weekly Sonnet limit (2026-10-30) with Units 5, 11 and 13
written and Unit 7 half done; resumed after the reset (2026-11-03). Reader B was then
resumed once more to rewrite the C1 lessons of Units 13 and 15 (extra lists).

## Cost

| Reader | Units | tokens | notes |
|---|---|---|---|
| A | 5, 7, 9 | 413,177 (resumed run) | first run's usage lost with the limit |
| B | 11, 13, 15 | 340,419 (resumed) + 398,629 (C1 rewrites) | first run's usage lost |

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 5 `language-style-word-formation` | 9 / 2 | 74 | 55 | 0 | 3 perfective *elolvas-* with *miközben/során* → *olvas-*; the story's unconfirmed Krúdy parody → Kosztolányi, an overclaim softened; 2 reading items and 1 consolidation item to met words; 4 items retagged `sag-seg-nouns` | 0 / 0 |
| 7 `performance-drama-persuasion` | 8 / 0 | 88 | 65 | 3 (length, *soha* tell, punctuation tell; rewritten) | 14 items retagged `concessive-indefinites`; 3 unmet words (*kényelmetlen*, *újságírók*, *ellenfeleid*) | 0 / 0 |
| 9 `roots-tradition-collective-memory` | 13 / 0 | 81 | 62 | 0 | *megy* "to walk" → "to go", a two-fault option, a length give-away, 13 arrow hints (several gave the answer: *rak -> rakosgat*), *magányosan* | 0 / 0 |
| 11 `aesthetics-vision-creative-obsession` | 18 / 0 | 77 | 63 | 1 (consolidation copy; rewritten) | a two-fault option, a second right answer (*A kép van kiállítva*), 16 arrow hints, *soha* tell, *háttér*, *külső* | 0 / 0 |
| 13 `scientific-discovery-hypothesis` | 16 / 0 | 85 + 86 extra | 66 + 39 | 1 extra (article blank; rewritten) | an answer order, the vocabulary title, *félelem* | 0 / 0 |
| 15 `medicine-ethics-responsibility` | 19 / 0 | 70 + 51 extra | 52 + 24 | 1 (length; rewritten) | 5 options (a second right answer *senki sem tehetett*, a person fault, colloquial *ha … marad*, *Lehet, sejtették*, *bárki észrevette volna*), *mégsem*; *etikai* listed on b2-08-03 | 0 / 0 |

Applied in two stages (437 fixes, then the 137 C1 rewrites written against the
stage-1 text). 36 challenges, 201 dictionary entries (187 lemmas, 14 surface forms),
no checklist missing, no glued blanks; check-content 0 / 0 on all six; B2 overall
976 → 803 errors. Walk 36/36 with challenges. All six frozen (B2 8/72).

## Decisions

- **No C1 forms (user's rule), rewritten:** Unit 13 lesson 01 was built on *feltéve,
  hogy* (C1 `felteve-hogy-kiveve-ha`) and used *attól függően, hogy* / *aszerint, hogy*
  (cataphoric, Unit 35): now *amennyiben*, *abban az esetben, ha*, *ha … akkor*, a noun
  with *-tól függően*, *X szerint*. Unit 15 lesson 04 taught the epistemic past modals
  (C1 `epistemic-modality`): now *biztosan*, *valószínűleg*, *talán*, *lehet, hogy*,
  *kétlem, hogy*, with *kellett/lehetett volna* for a missed chance.
- **Decided by the user (2026-11-03):** `concessive-indefinites` `taught_in` moved to
  b2-04-04-a-gr (Unit 7, from Unit 17); `sag-seg-nouns` moved to B2, taught in
  b2-03-01-a-gr (Unit 5, from C1 c1-06-02). Unit 17's and C1's screens recap them
  when their batch runs.
- **Judged by Claude, kept:** *arra kért, hogy* / *azt követelte, hogy* (B1 reported
  commands, Unit 53), *oly módon, hogy* (formal *úgy, hogy*), *mindent összevetve*,
  *őszintén szólva* (set phrases, not the C1 concluding markers), *-ván/-vén* (literary
  variant of the B1 *-va/-ve*), Unit 5 lesson 04's unpacking of nominal style (it
  teaches the reverse of the C1 official register), counterfactual *tudhatta volna*
  ("could have known", not the epistemic reading).
- **Two classics relabelled** (`reviewer-facts.md`): b2-06 (Csáth) and b2-08 (Németh)
  are original stories, not scenes from the books; screens, goals and items that
  presented them as the books' plots were reworded by reader B.

## Recurring, scripted

- **Arrow hints** ("összevet -> -va/-ve", "rak -> rakosgat 3sg past"): 89 in 34 B2 files.
  `check-content` `hint-suffix` now covers B2 and the arrow form when it names an
  ending; this batch's 29 were rewritten to the base verb (with a role label where
  needed). 55 arrow hints are left in other B2 units (1 names an ending; the rest name
  a form, "elhagy -> hagyják"): readers fix them unit by unit.
