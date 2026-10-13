# hu a1 `frequency-word-order`: fix list (2026-10-13)

First read of the old unit (90k, verdict-first) said regenerate; Sonnet
regenerated it (181k); blind read of the new unit (121k, 3 min), filtered
and applied by Claude.

## Applied

- `a1-84-check-2`: answer key pointed at "Ebéd mindig után pihenek.";
  `correct` 0 → 1 ("Ebéd után mindig pihenek.").
- `a1-85-b-gr`: "Only the “I” form of an *-ik* verb is different." → "Only
  the “I” and “he/she” forms …" (contradicted a1-85-a); *-öm* added to the
  *-om/-em* rule.
- Wrong options that broke the person in *soha* items now break the *soha*
  point: `a1-82-introduce-2` "Soha nem főzünk." → "Néha nem főzök.";
  `a1-82-dialogue-1` "Nem, soha nem főzünk." → "Nem, néha nem főzök.";
  `a1-84-practice-2` "Este soha nem főzünk." → "Este néha nem főzök.";
  `a1-85-consolidation-13` "Nem, soha nem főzök." → "Nem, néha nem főz."
- `a1-84-production-1` solution to the screen's order: *Délután általában
  sétálunk a parkban.*
- `a1-82-production-1` (*Minden este főzök.*): no skill covers *minden* →
  unit vocabulary.
- Story: "Te is sportolsz?" (nothing for *is* to add to) → "Te sportolsz?";
  English added to the four comprehension questions.
- `a1-85-consolidation` challenge target: "…, szombaton szoktam sportolni."
  → "…, de szoktam sportolni." (and the English).

## Not taken

- `distractor_skills` on the person-form options: replaced instead.
- "Ebédután" non-word option: a single-fault option; keep.
- Story Saturday rest vs cooking; `characters` list: minor.
- a1-84-production-2, a1-85-consolidation-19 structured-writing tags: not
  graded.
- a1-85-a-gr *lakik/laksz* simplification; repeated consolidation dialogue:
  keep.
