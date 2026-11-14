# ES B2 batch 27–30 (2026-11-13)

Two Sonnet edit-in-place agents, two units each (A: Units 28 structuring/sequencing and
29 reformulation/precision markers; B: Units 27 prepositional regimes and 30 contrast/
restriction markers). Started 21:04 UTC; a container restart came after both agents had
finished, before their diffs were saved; both worktrees survived and the diffs were
saved and committed first. One `taught_in` move signed off before the batch
(`contrast-markers` to b2-30-01, `decisions.md`).

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| 27 prepositional-regimes-locutions | 1 / 19 → 0 / 0 | 1 kept (*consiste*: the lesson's own lemma *consistir en*) |
| 28 discourse-markers-structuring-sequencing | 6 / 18 → 0 / 3 accepted | 0 |
| 29 discourse-markers-reformulation-precision | 8 / 21 → 0 / 1 accepted | 0 |
| 30 discourse-markers-contrast-restriction | 8 / 17 → 0 / 1 accepted | 0 |

Agent A 336,404 tokens (19 min), agent B 328,070 (18 min): ~166k a unit. Walk 24/24.
B2 30/72 frozen. Accept list: `accept.txt`.

## Texts

- Unit 27, Quiroga's "Anaconda" (chapters I–VI): retelling checked against the full
  Wikisource text (`sources/`). The old file had Anaconda presiding, a "Lanceolata"
  killed and Anaconda caged for Buenos Aires: none of it in these chapters. `work` now
  "Anaconda (1921)". Reviewer: two tense slips (*Es una yarará*, *Allí vive Terrífica*).
- Unit 29, Machado's *Dom Casmurro* (chapters I–III): retelling checked against the
  Portuguese Project Gutenberg text (#55752). Every claim matched (the train, the
  nickname, the Matacavalos house, the four medallions, the *História dos Subúrbios*,
  the November 1857 scene). Reviewer: "Capitu acababa de cumplir catorce" → "había
  cumplido catorce la semana anterior" (*fez quatorze á semana passada*).
- Unit 28 (Roa Bastos, *Hijo de hombre*) and Unit 30 (Da Cunha, *Os sertões*): texts
  about the work. Both agents' versions were padded with talk about the text ("Este texto
  trata de…, vamos a dar tres pasos", "Pues bien, quien conozca estos datos sabrá, antes
  de abrir el libro…", "a quien usted ya conoce por otros textos de este curso", a
  paragraph telling the reader which book to choose). The reviewer rewrote both within
  `reviewer-facts.md` (178 and 198 words; the facts are thin). The 1959 date one critic
  gives is now in the Roa Bastos text, attributed as in the facts file.

## Reviewer edits

- Unit 30 consolidation challenge: the target used none of the unit's markers; now
  *Un corresponsal suele escribir artículos; Da Cunha, en cambio, escribió un libro…*
- Vocabulary: *el gobernante* (b2-28-03), *el corresponsal* (b2-30-01, accepted as
  `vocab-unused` there: the unit text and the consolidation challenge use it).
- Unmet words over all 30 frozen core units: the five kept cases plus *consiste*.

## New check

`story-meta` (check-content suspect, B2 and up, Spanish classic texts): talk about the
text, the course or the reader. Tested on the agents' Unit 28 and 30 versions (caught)
and the rewrites (clean). It finds **43 sentences in 18 frozen texts** (Units 2, 4, 6–18,
20, 23, 26) and 6 in Unit 33 (next batch). Not all are defects: "el lector tiene que
reunir las piezas" (Rulfo's fragments, b2-02) and the diary point in b2-11 describe the
book's form. The rest are reading advice, "en este texto vamos a hablar de…", invented
claims about readers ("Muchos lectores prefieren…", b2-04) and pointers to "otros
textos de este curso" (b2-13, b2-20). **Queued for the core close-out:** trim them,
refreeze the units; list: `python scripts/check-content.py es-latam b2 | grep story-meta`.

## For the user

- Nothing to decide in this batch. Items in 28-03 (*pues bien, en cuanto a, por lo que
  se refiere a*) carry the unit vocabulary skill: those markers have no grammar skill.

## Follow-up the same night: frozen texts cleaned

The `story-meta` list was worked through at once instead of waiting for the close-out,
while the batch 31–36 agents ran (and then sat out a usage limit). The check was widened
(*un lector*, *cada lector*, *muchos/algunos lectores*, *muchos críticos*, *quien hubiera
leído*, *quienquiera que lea*), which added 16 sentences in Units 1–10, 18 and 21. All
cut or rewritten as facts; 22 units refrozen; walk 132/132. Kept on purpose: none (the
Rulfo "pieces" line was rephrased without the reader).
