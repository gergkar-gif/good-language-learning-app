# HU C1 core batch 9–16 (2026-11-14)

Units (app numbering, core track): 9 bioethics, 10 contracts-negotiation, 11 human-rights-law, 12 civic-resistance (reader A); 13 macroeconomics, 14 energy-transition, 15 artificial-intelligence, 16 public-sphere (reader B). Method of batch 1–8; four units per reader; extras staged with `scripts/stage_extras.py` (0 fields needed carrying: the readers repeated every field, as the focus file asked).

## Cost

| Reader | Tokens | Minutes | Fixes |
|---|---|---|---|
| A (Units 9–12) | 383,237 (360,621 + follow-up) | 17.7 + 2.1 | 449 + 54 extra |
| B (Units 13–16) | 422,476 (399,799 + follow-up) | 19.2 + 2.2 | 441 + 50 extra |

About 100k reader tokens a unit (batch 1–8: ~90k).

## Results

- check-content 66 errors / 80 suspects (setup.md) → 0 errors; 40 `vocab-unused` stems accepted (`accept.txt`).
- 898 fixes applied: merged-1 791, merged-2 99, reviewer lists rev-*.json 8. 39 words listed.
- Unmet words after applying: 68 → 31, all lookup misses (*-hat/-het* forms, comparatives, suffixed forms). Frozen Units 1–8: 17, no regression.
- 48 challenges, 57 dictionary glosses.
- All 175 retired tags in the batch retagged; C1 retired 500 → 332.
- Locked, frozen 8/8, walk 48/48 with challenges.

## Registry (user, 2026-11-14)

- `evaluative-stance` is now taught in c1-12-02, which first teaches stance framing. c1-26-04 teaches obligation; its items are to be retagged when that batch runs.
- c1-09-02 and c1-15-04 teach probability adverbs, not `epistemic-modality`. Their 15 items are retagged to `epistemic-hedging`.

## Facts (reviewer-facts.md)

- **Bibó (Unit 16).** No quotation marks are left; both lines are paraphrased. The known line is worded differently, and the source page refused the fetch.
- **Neumann (Unit 15).** The paraphrase shown as a quotation is unquoted; the "foresaw neural networks" and "bio-cybernetics" claims are cut.
- **Márai (Unit 10).** The contract and honour view is now the text's reading, not the content of *Sértődöttek*.
- **Konrád (Unit 12).** The text is framed as his ideas ("Konrád szerint").
- **Fekete (Unit 14).** The text is about *Tüskevár* only; the Kis-Balaton judgement and the unconfirmed "öreg halász" are cut.
- **Németh (Unit 9).** The unconfirmed 1940 is dropped and the praise softened.
- **All eight `source` fields** say "original text about".
- **ICC (Unit 11).** Hungary reversed its Rome Statute withdrawal on 27 May 2026 and is still a party. No item says otherwise.
- **Present-day law.**
  - The Ptk. liability-exclusion and force-majeure claims are consistent with the code.
  - The end-of-life screen matches current law (refusal of life-sustaining treatment allowed under conditions; euthanasia illegal; Karsai v Hungary, ECtHR 2024).
  - The debt rule (Fundamental Law Art. 36) was not touched by the 16th and 17th amendments of 2026.

## Reviewer changes

- **Unit 9.** *legnagyobb biztonságot* (safety, where certainty was meant) rewritten; a "right to a dignified death" stated as fact is now framed as what many people speak of.
- **Unit 13.** *enyhén stagnált* rewritten twice; a *mindig* contradicting the story (and a tell) removed.
- **Unit 14.** The *amennyiben* recap now names B2 Unit 7; "öreg halász" cut; "Az olvasó számára" cut from the story.
- **Unit 15.** *kivéve, ha* comma restored in 14 places; one elliptical blank rewritten; "Az olvasó azt veheti észre" cut.
- **Unit 16.** *ellenségkép-gyártás* gloss fixed (it is not "scapegoating"); "Az olvasó számára" cut; *következésquéppen* typo in a reader extra fixed.
- **Rejected extras rewritten by hand.** Three items (c1-10-02 ×2, c1-12-consolidation-2); a fourth, c1-12-03-check-8, was clean and stayed.
- **Two missed retags:** c1-11-04-controlled-2 and c1-12-05-controlled-2.
- **Two recap units corrected:** *céljából*, *eltekintve*.
- **Challenges.** 7 targets rewritten so each uses its lesson's form and met words; 2 more for unmet words.

## Not verified

- Speaking steps, spoken answers, wrong-answer paths, real audio, a native speaker's eye.
- The exact Bibó wording (paraphrased instead).

## For the user

Open from batch 1–8: prune or keep the unused list words; Unit 2 has no skill of its own; the `author` labels. Units 13, 15 and 16 also teach no registry skill: their new points are vocabulary and frames.

**Before batch 17–24:** c1-22-01, the registered screen for `epistemic-modality`, teaches hedging phrases (*könnyen meglehet, hogy*, *nem zárható ki*). C1 core may have no lesson that teaches *kellett, hogy legyen*.
