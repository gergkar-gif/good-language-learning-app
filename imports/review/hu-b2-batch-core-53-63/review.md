# HU B2 core batch: Units 53, 55, 57 (reader A) and 59, 61, 63 (reader B), 2026-11-04

No usage limit hit. Reader A 438,701 tokens (61 tool uses, 26 min), reader B 446,836 (72,
26 min): ~148k a unit. A worker restart mid-review lost nothing (review lists were on disk).

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 53 `borders-kinship-transborder-identity` | 14 / 0 | 117 | 79 | 0 | 6 second right answers (*akkor is, ha*; bare *Ha* with *volna is*; both orders of *eltekintve attól, hogy*); a reading question; *országhatár*, *szülőfalu* listed | 0 / 0 |
| 55 `exile-emigration-global-networks` | 9 / 0 | 85 | 65 | 1 (*munkahelyben*, a non-form; rewritten) | *kivándoroltak* as a second answer; *különösen, ha* comma; 4 words listed | 0 / 0 |
| 57 `diplomacy-alliances-sovereignty` | 8 / 0 | 107 | 74 | 1 (a *mindenki* tell; rewritten) | model answer *kívánatosnak tartaná még egy találkozót* (definite verb, indefinite object) rewritten; "Közép-Európa nagy része"; **Abády Balázs → Abády Bálint** (story, challenges); story relabelled; 10 words listed | 0 / 1 accepted |
| 59 `civic-participation-advocacy-public` | 8 / 1 | 82 | 65 | 0 | *panasszal él* "often" (not always) with *miatt*; **Tóth Piroska → Horváth Piroska**, not a fiancée; a challenge that reused her name for a neighbour renamed; *hátrál* listed | 0 / 0 |
| 61 `gastronomy-conviviality-cultural-rituals` | 19 / 1 | 122 | 79 | 1 (length; rewritten) | *ropogóssá* (attested) and two indicative-after-*mintha* wrong options replaced; story typo *felsejlettek*; source title corrected and relabelled; 15 words listed | 0 / 1 accepted |
| 63 `competition-mastery-peak-performance` | 9 / 0 | 99 | 80 | 3 (2 length, 1 ds on its own skill; rewritten) | **13 fill-blanks now take *annyira* beside *olyannyira* and *olyan* beside *oly mértékben*** (second right answers); my own rewrite brought *sportszerűség* before its lesson (replaced); story relabelled; 15 words listed | 0 / 0 |

612 fixes applied (606 from the readers' lists, 6 rewrites), 36 challenges (2 changed: a
reused story name, *oly mértékben nagy*), 47 words listed, 152 dictionary entries (136 lemmas,
16 surface forms). Accepted at freeze: `vocab-unused` b2-29-05 *pontosít* and b2-31-05
*húsleves* (consolidation only). Walk 36/36 with challenges. No new B2 validator warning.
B2 32/72 frozen.

## For the user (nothing blocks; defaults applied)

- **Resultative *-ra/-re* (*puhára párol, ropogósra pirít*) has no registry skill.** Unit 61's
  lesson 01 and ~12 later items test it; reader B tagged them `ra-re` (title "movement onto"),
  the nearest form skill. The `mintha` order defect named in the focus file turned out to be
  a tagging fault: the 10 b2-31-01 items tagged `mintha` never used it. Kept on `ra-re` (the
  skill list is frozen); a resultative skill would need your sign-off.
- **Unit 59 teaches no registry skill** (formal verb government with known endings), like
  Units 47–51.
- **Esterházy Péter (d. 2016) speaks invented lines** in the Unit 63 story; now labelled
  "Adaptation inspired by". Reader B suggests a fictional name instead. Left as it is.

## Recurring, not yet scripted

- **Second right answers in fill-blanks when the skill has two forms** (*olyannyira / annyira*,
  *oly / olyan mértékben*, *Még ha / Ha … is*, word-order twins of *eltekintve attól, hogy*):
  21 items this batch, all passed by check_fixes (it can't know the alternatives). Logged in
  rulebook § 6b; a check would need a per-skill list of equivalent forms.

## Judged by Claude

- Facts and classics: `reviewer-facts.md` (Bánffy's protagonist, Piroska's surname, the Krúdy
  title, the Esterházy scene, the beer-clinking legend, now hedged by reader B).
- *-ig* wrong options (*puháig, ropogósig, sűrűig*) kept: recipes use *-ra* (*puhára főzzük*,
  *ropogósra sütjük*), and no recipe in a search used the *-ig* forms; *ropogóssá* does occur
  (*ropogóssá válik*), so that option was replaced.
- Recaps: all 5 flags false positives (multi-word *függetlenül attól, hogy* is b2-09-04, B2
  Unit 17; *kellene* A2 Unit 18; *-ra/-re* verbs B1 Unit 3; *amennyiben* B2 Unit 13;
  preverbs A1 Unit 28).
- Unmet words after applying: 87; 47 listed, 30 lookup misses or deliberate wrong forms left.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
