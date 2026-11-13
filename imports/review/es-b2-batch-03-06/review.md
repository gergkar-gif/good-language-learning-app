# ES B2 batch 3–6 (2026-11-13)

Two Sonnet edit-in-place agents, two units each, paired by topic overlap (A: Units 3
probability + 5 doubt; B: Units 4 influence + 6 emotion), so each recap across the
pair was written by the agent that wrote what it recaps.

| Unit (app) | check-content before → after | unmet before → after |
|---|---|---|
| 3 hypothesizing-probability | 6 / 18 → 0 / 0 | 67 → 0 |
| 4 influence-will-value-judgments | 3 / 11 → 0 / 0 | ~110 → 0 |
| 5 doubt-denial-epistemic-stance | 10 / 18 → 0 / 0 | 79 → 0 |
| 6 emotional-reactions-affective-stance | 8 / 17 → 0 / 0 | 101 → 0 |

Agent A 375,044 tokens (19 min), agent B 339,242 (18 min): ~180k a unit, against
~300k at one unit per agent in the pilot. Walk 24/24. B2 6/72 frozen.

## Texts (all four authors in copyright; texts about the work)

García Márquez, *Crónica de una muerte anunciada*; Fuentes, *La muerte de Artemio
Cruz*; Paz, *El laberinto de la soledad*; Galeano, *Las venas abiertas de América
Latina*. Every claim checked against `reviewer-facts.md`; ideas presented as the
authors' views; the readers' guesses labelled as such.

## Reviewer edits

- Fuentes text: "Fuentes quería que el lector…" (a claim about his intent) → "la
  novela pide que el lector siga…"; a repeated "Fuentes murió en 2012" removed.
- Galeano text: narrator "nos molesta" → "me molesta" (one voice).
- b2-04-04 screen: *pedir* removed from the verbs that allow an infinitive with another
  subject (*te pido que vengas* is the norm).
- Challenge b2-06-01: "me preocupa que no termine el informe" (same subject, against
  the unit's own rule) → "me preocupa no terminar el informe a tiempo".
- Two consolidation checklist lines shared across the agents' units
  (`checklist-shared`): the author named in each.

## Read and kept (agents' "unsure" lines)

Mood claims on screens (postposed *quizás* + indicative, *a lo mejor* indicative only,
*seguramente* usually indicative, *no niego que* both moods, *¡Menos mal que…!* +
indicative, indicative possible after *el hecho de que*): all correct. Wrong options
teaching the standard form (*No es que estoy…*, *Siento de que…*, *Me alegra de…*).

## For the user

- `infinitive-vs-que-subjunctive` (taught b2-04-04) overlaps A2 Unit 27's two-subject
  rule for wishes (`subjuntivo-deseos`): the screen recaps A2 and extends it to
  influence, judgments and feelings. No registry change made.
- *¡Menos mal que…!* + indicative has no skill; its two items are tagged
  `subjunctive-emotion`.
