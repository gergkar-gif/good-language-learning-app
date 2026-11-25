# ES B2 latam batch 5–10 (2026-11-25)

Two Sonnet edit-in-place agents, three units each (A: El Salvador/Honduras, Nicaragua, Costa
Rica; B: Panama, Belize and the Guianas, Cuba). No usage-limit stop. Reviewer facts sent mid-run.

| Unit (app) | check-content before → after | unmet after (--with-hidden) |
|---|---|---|
| LatAm 5 el-salvador-honduras | 29 / 16 → 0 / 0 | 0 |
| LatAm 6 nicaragua | 33 / 13 → 0 / 0 | 0 |
| LatAm 7 costa-rica | 13 / 17 → 0 / 0 | 0 |
| LatAm 8 panama | 15 / 14 → 0 / 1 accepted | 0 (1 fixed by the reviewer: *conservar*) |
| LatAm 9 belize-guianas | 17 / 21 → 0 / 0 | 0 |
| LatAm 10 cuba | 7 / 21 → 0 / 0 | 0 |

Agent A 353,430 tokens (17 min), agent B 396,874 (21 min): ~125k a unit, against ~170k at two
per agent. Walk 36/36 with challenges. B2 46/72 frozen. Retired slugs in es-latam 566 → 435.

## What changed

- Units 5–6: seven lessons re-pointed from later core skills to known ones (reporting verbs →
  *dijo que*/*según*; contrast markers → *sin embargo*/*no obstante*; *de tal manera que* →
  *porque*/*por eso*; rhetorical devices → fronting; *aun cuando* → *a pesar de que*).
- Units 7–10 were topic-only (20 lessons with retired topic slugs and word-list screens): each lesson
  now teaches one known skill as a recap applied to the topic; every retired slug gone.
- 30 lesson texts rewritten; six combined readings restitched, retitled, English summaries.
- 30 lessons given checklists; 36 challenges.

## Facts corrected (reviewer-facts.md)

Misquoted or invented quotations cut: Romero's last homily (paraphrased), Sandino, Darío's "Oda a
Roosevelt", a Berta Cáceres slogan, Carpentier, Martí. Wrong: the isthmus "80 km" (about 50), the
Garifuna arrival "1802" (Settlement Day commemorates 1832), Nicaragua's bull sharks "unique".
Present-day, added from 2026 news: El Salvador's state of exception still renewed monthly
(government figure ~93,000 arrests, rights groups' criticism attributed), Honduras' president
Asfura since January 2026 after a disputed count, Costa Rica's president Laura Fernández since May
2026, Cuba's 2026 fuel crisis and blackouts. Unsupported figures cut: Antillean workers 150,000,
Belize "50 % Spanish", Cuban emigration "half a million / 5 %", electricity "98 %", and others.

## Reviewer edits

- *conservar* (unlisted) → *mantener* in panama-consolidation.ex05 and the panama-05 screen.
- cuba-04 screen recap: the verbs are A1, their past-tense meaning shift is B2 Unit 2 (reworded).
- Challenges: nicaragua-05 cited the UN where the text cites the IACHR; costarica-02 target
  reworded; cuba-consolidation repeated cuba-01 word for word (new target from the text).
- 12 `checklist-shared` errors from generated checklists (consolidation lines copying lesson lines;
  panama-05 and cuba-05 identical): **scripted** as `scripts/fix_shared_checklists.py`.

## Not verified

The agents' remaining claims are checked against the reviewer's knowledge only (list in
reviewer-facts.md). No native read; speaking steps and wrong-answer paths not walked.
