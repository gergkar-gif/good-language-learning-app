# Parlour Vocabulary Driller: Implementation Specification

## Purpose

Redesign the current Vocabulary Driller so that it does not duplicate My Decks/SRS.

**My Decks** handles direct vocabulary memory and spaced repetition.

**Vocabulary Driller** handles vocabulary in context, training the learner to recognise, infer and retrieve vocabulary from actual Spanish.

Keep the implementation light and quick. Do not build a sophisticated adaptive testing engine.

## Core principle

Every exercise must have **one clear intended answer, with enough context for the learner to recover it**.

Bad:

> Yo quiero un ______.

Good:

> Después de trabajar doce horas, estaba completamente ______.

**English:** exhausted

→ agotado

If an exercise is ambiguous, do not show it.

## Exercise types

### 1. Contextual inference

> Después de trabajar doce horas, estaba completamente **agotado**.

What does *agotado* mean here?

→ exhausted

This should be the defining Driller exercise.

### 2. Contextual recall

> Después de trabajar doce horas, estaba completamente ______.

**English:** exhausted

→ agotado

This requires retrieval while retaining meaningful context.

### 3. Meaning discrimination

> El director **planteó** una solución durante la reunión.

What does *planteó* mean here?

- proposed
- cancelled
- discovered
- prevented

→ proposed

Distractors should be plausible but clearly wrong in context.

### 4. Same word, different context

> Me senté en un **banco** del parque.

→ bench

Then:

> Fui al **banco** después del trabajo.

→ bank

Use this especially for genuinely polysemous words.

### 5. Contextual choice

> No tenía dinero suficiente, así que tuvo que ______ la compra.

- cancelar
- celebrar
- esconder
- mejorar

→ cancelar

The context should make one answer clearly appropriate.

### 6. Morphological inference

> Cuando llegaron a casa, estaban completamente **agotadas**.

What does *agotadas* mean?

→ exhausted

The underlying vocabulary item is *agotado*. The learner should recognise vocabulary despite grammatical changes.

## Do NOT include

Do not implement:

- contextual correction
- contextual translation
- direct flashcard recall
- elaborate adaptive modes
- complex difficulty modelling

Direct flashcard recall belongs in My Decks/SRS.

## Contexts are the important asset

We do not need thousands of hand-authored exercises.

Use a small number of good contextual examples for vocabulary items.

Example:

```text
agotado

translation: exhausted

contexts:
- Después del partido, Juan estaba agotado.
- Después de trabajar doce horas, estaba completamente agotado.
```

One good context can produce several exercise forms, such as inference, contextual recall and contextual choice.

Prefer reusing good existing contexts rather than maintaining a huge exercise database.

## Where contexts should come from

Prefer existing Parlour content:

- lesson dialogues
- lesson stories
- existing example sentences
- Parlour readings
- other existing curriculum content

The curriculum and Library can therefore become the source of contextual vocabulary examples.

Contexts must be natural Spanish and must genuinely support the intended meaning.

## Difficulty

Keep difficulty simple.

The target vocabulary can be at the learner's level while the surrounding sentence can be somewhat harder.

Example for an A2 learner:

> Aunque llevaba toda la noche trabajando, Juan seguía **agotado** al día siguiente.

The learner does not need to understand every word. The target must remain inferable.

Use only a simple distinction if needed:

- accessible context
- moderately challenging context
- difficult context

Do not build a complex adaptive difficulty engine.

## Quality rule

The most important quality rule is:

> **Never show an exercise where the answer is not reasonably recoverable.**

Reject:

> Yo quiero un ______.

Prefer:

> Después de trabajar doce horas, estaba completamente ______.

The system does not need an elaborate automated quality-control engine. Conservative content selection is preferable.

## Relationship to Parlour

### Learn

Teaches vocabulary and grammar.

### Vocabulary Driller

Teaches the learner to **recognise, infer and retrieve vocabulary in context**.

### My Decks

Provides direct recall and long-term SRS.

### Library

Provides sustained reading and exposure to language.

The intended loop is:

> **Learn a word → encounter it in context → practise contextual inference/retrieval → add it to a My Deck if useful → SRS maintains long-term recall.**

## Engineering principle

Keep the feature **light and quick**.

Do not build:

- a giant exercise database
- a complex adaptive testing engine
- deck-specific SRS
- elaborate difficulty algorithms
- unnecessary exercise types
- complicated authoring infrastructure

Prefer a small number of well-designed exercise types using good existing vocabulary contexts.

The goal is **fewer, better exercises**, not maximum exercise volume.

## Acceptance criteria

The redesigned Driller should:

1. Never present deliberately under-specified sentence blanks.
2. Always have a clear intended answer.
3. Primarily test vocabulary through context.
4. Include the six exercise types above.
5. Leave direct flashcard recall to My Decks/SRS.
6. Use existing Parlour content as contextual material where possible.
7. Support contexts somewhat above the learner's level when the target remains inferable.
8. Handle inflected forms of known vocabulary.
9. Support multiple contexts for words with multiple meanings.
10. Remain lightweight in both engineering and UI.
11. Prefer a small number of high-quality contexts over a massive exercise bank.
12. Reuse the existing vocabulary/lexicon infrastructure rather than creating another vocabulary system.
