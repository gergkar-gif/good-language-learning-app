# Parlour Decks: Design Specification

## Purpose

This document consolidates the design discussion for the next iteration
of Parlour's Decks system.

It is intended as an implementation specification for Claude Code.

The existing Decks architecture should be extended rather than replaced.
Preserve the existing engine/content separation and the existing
one-card-per-vocabulary-item SRS model.

------------------------------------------------------------------------

# 1. Core conceptual model

Parlour should distinguish three separate concepts:

### Vocabulary

A canonical lexical item in the Parlour lexicon.

Example:

`aeropuerto`

The vocabulary item can have:

-   translation
-   part of speech
-   pronunciation
-   lexical metadata
-   curriculum relationships
-   topic relationships
-   frequency information
-   other existing dictionary data

There should be one canonical vocabulary item rather than separate
copies for different decks.

### Deck membership

A deck is a collection of vocabulary items.

A vocabulary item may belong to many decks.

For example, `aeropuerto` might belong to:

-   A1 Unit 8
-   Travel
-   Spanish for Mexico
-   Difficult Words

These are memberships, not separate vocabulary objects.

### SRS state

The learner has one SRS card/state for a vocabulary item.

For example:

`aeropuerto` - reviews: 4 - interval: 18 days - next review: 30 August

This SRS state is independent of deck membership.

If `aeropuerto` belongs to five decks, it still has one review schedule.

## Fundamental rule

> Decks organise cards. Cards own memory.

Do not introduce deck-level SRS schedules.

------------------------------------------------------------------------

# 2. My Decks vs Parlour Decks

The Decks section should have two major categories:

## My Decks

These are user-created and user-owned collections.

Examples:

-   Spanish for Mexico
-   Words I Keep Forgetting
-   Politics
-   Restaurant Vocabulary
-   My B1 Verbs
-   Spanish for Seoul

Properties:

-   unlimited number of decks
-   unlimited words per deck
-   editable
-   user can rename decks
-   user can delete decks
-   user can add words
-   user can remove words
-   a word can belong to multiple My Decks
-   removing a word from a deck must NOT delete its SRS history
-   deleting a deck must NOT delete the vocabulary or SRS cards
    themselves

A My Deck is a collection, not an independent SRS system.

## Parlour Decks

These are curated, read-only collections supplied by Parlour.

Examples:

-   A1 Unit 1
-   A1 Unit 2
-   A1: Travel
-   A1: Food
-   A2: Daily Life
-   B1: Politics

The learner cannot edit their membership.

They can:

-   browse them
-   review them
-   add their words to a My Deck

Parlour Decks should be generated from the existing
curriculum/vocabulary data where appropriate.

------------------------------------------------------------------------

# 3. The curriculum vocabulary limit is NOT a deck limit

The existing curriculum requirement of approximately 20 new vocabulary
items per unit remains a curriculum/content constraint.

It should NOT restrict user-created decks.

For example:

-   A1 Unit 4 may contain 20 new words.
-   A user-created "Spanish for Mexico" deck may contain 70 words.
-   Another user-created deck may contain 500 words.

There should be no 20-word limit on My Decks.

The existing daily new-word cap is a separate concern.

## Important distinction

> Deck membership ≠ SRS activation.

A user can add 100 words to a My Deck without necessarily being required
to learn 100 new words that day.

The SRS scheduler can continue to control the learner's active
review/new-card workload.

Do not confuse deck size with the daily new-word limit.

------------------------------------------------------------------------

# 4. Why the current one-card-per-word model should remain

The existing architecture already implements the important principle
that a vocabulary item has one SRS card, while decks provide different
ways of selecting those cards.

This should be preserved.

Example:

`aeropuerto`

belongs to:

-   Parlour Deck: A1 Travel
-   Parlour Deck: A1 Unit 8
-   My Deck: Spanish for Mexico
-   My Deck: Airport Vocabulary

There is still only one SRS card.

If the learner reviews `aeropuerto` through "Spanish for Mexico" and
presses Good, its single SRS schedule is updated.

The same updated card is then reflected everywhere else.

## Do NOT implement

Do not create:

-   one SRS schedule per deck
-   one duplicate card per deck
-   deck-specific SM-2 intervals
-   deck-specific review histories

That would cause the same vocabulary item to have competing schedules
and duplicate reviews.

------------------------------------------------------------------------

# 5. My Deck creation flow

The preferred interaction should take inspiration from Quizlet's simple
set-creation flow.

From:

**Decks → My Decks → Create Deck**

the learner should be able to:

1.  Enter a deck name.
2.  Optionally enter a description.
3.  Add vocabulary.
4.  Save the deck.

The initial editor should be simple and compact.

Conceptually:

  Spanish       English
  ------------- ---------------
  aeropuerto    airport
  boleto        ticket
  alojamiento   accommodation
  reservar      to book

There should be an obvious:

**+ Add word**

control.

------------------------------------------------------------------------

# 6. Adding vocabulary to a My Deck

There should be two ways to populate a deck.

## A. While editing/creating a deck

The user can:

-   search Parlour's vocabulary
-   select a result
-   have its known translation and metadata automatically populated
-   manually enter a word when appropriate

If a manually entered word already exists in the Parlour lexicon,
attempt to resolve it to the canonical lexical item rather than creating
a duplicate vocabulary object.

The user should be able to edit the displayed translation if the UI
permits custom definitions, but the default should come from the
existing lexicon.

## B. Add to deck from anywhere

Vocabulary appearing throughout Parlour should have an:

**Add to deck +**

action where appropriate.

This can be used from:

-   Lessons
-   Library / Reader
-   Parlour Decks
-   Workshop where vocabulary is exposed

Clicking it should present:

**Add to deck**

-   existing My Deck 1
-   existing My Deck 2
-   existing My Deck 3
-   **+ Create new deck**

This should make vocabulary collection a natural part of using Parlour.

The user should not have to visit the Decks page every time they
encounter a useful word.

------------------------------------------------------------------------

# 7. Editing a My Deck

Opening a My Deck should provide actions such as:

-   Review
-   Edit deck
-   Add words

The edit view should use essentially the same vocabulary editor as
creation.

The user should be able to:

-   rename the deck
-   edit its description
-   add words
-   remove words
-   save changes
-   delete the deck

Removing a vocabulary item from a deck only removes the membership.

It must not:

-   delete the lexical item
-   delete the user's SRS card
-   reset review history
-   alter other decks containing the same word

Likewise, deleting a My Deck must not delete its words or SRS state.

------------------------------------------------------------------------

# 8. Parlour Deck organisation

The current implementation exposes Lesson, Topic and Frequency decks as
peer groups.

This should be reconsidered.

The user-facing structure should distinguish curated Parlour collections
from personal collections.

A possible structure is:

## Parlour Decks

### Course

**A1** - Unit 1 - Unit 2 - Unit 3 - etc.

**A2** - Unit 1 - Unit 2 - etc.

### Topics

-   Family
-   Food
-   Travel
-   Work
-   Politics
-   etc.

Other curated collections can exist where they serve a clear purpose.

The exact hierarchy should remain compact.

## Frequency

Frequency should primarily be treated as vocabulary metadata/filtering
rather than necessarily as a major visible deck hierarchy.

Avoid turning the interface into:

-   1--100
-   101--200
-   201--300
-   etc.

Frequency information can instead help users find or construct useful
study collections.

------------------------------------------------------------------------

# 9. Review behaviour

There should be two distinct review entry points.

## Global review

From the homepage:

> What vocabulary is due for review?

The homepage should use the existing SRS system to retrieve due cards
across the learner's entire active SRS collection.

This should produce a global review session.

The user does not need to select a deck first.

## Deck review

From a specific deck:

> What vocabulary in this collection do I want to review?

The existing scoped review mechanism can be used.

A deck review should select the relevant vocabulary items and feed them
into the same underlying SRS cards.

There must still be only one SRS state per vocabulary item.

------------------------------------------------------------------------

# 10. Homepage implication

The current SRS architecture already contains the machinery needed for a
global due-review queue.

The homepage can therefore expose something like:

## Today's review

**12 words due**

\[Start review\]

The global review session should draw from the learner's due SRS cards.

The homepage does not need to understand deck-specific scheduling.

Decks provide organisation and filtering. SRS provides the memory
schedule.

The homepage answers:

> What do I need to review?

Decks answer:

> Which vocabulary collection do I want to study?

------------------------------------------------------------------------

# 11. Deck status information

A deck can show useful statistics derived from the shared SRS cards.

Possible states include:

-   total words
-   new
-   learning
-   due
-   reviewed
-   possibly mature/long-interval

Avoid claiming that a card is "mastered" based on an arbitrary number of
reviews unless the underlying system has a defensible definition of
mastery.

The existing implementation currently treats `reviews >= 3` as
"mastered". This should be reviewed before making that terminology
prominent in the new UI.

A safer UI vocabulary is:

-   New
-   Learning
-   Due
-   Reviewed

or similar.

------------------------------------------------------------------------

# 12. What we are explicitly NOT building now

Keep the first implementation focused.

Do NOT add:

-   public deck sharing
-   collaborative decks
-   cloud synchronisation
-   deck importing/exporting
-   social deck discovery
-   complex deck hierarchies
-   deck-specific SRS algorithms
-   deck-specific scheduling
-   complicated filtering systems
-   elaborate drag-and-drop editing
-   another independent vocabulary database

These can be considered later if actually needed.

The immediate goal is:

> Create deck → add words → edit deck → review deck.

And:

> Any useful vocabulary → Add to deck.

------------------------------------------------------------------------

# 13. Relationship to the existing architecture

The existing repository already has:

-   `engine/decks.js`
-   `engine/srs.js`
-   `engine/lexicon.js`
-   persistent SRS data
-   deck-scoped review
-   canonical vocabulary lookup
-   `content/es/decks/decks.json`

The implementation should extend these systems rather than replace them.

The existing principle in `engine/decks.js` that decks are views onto a
shared SRS card collection should remain the architectural foundation.

The existing SRS system should remain responsible for:

-   card state
-   review scheduling
-   intervals
-   ease
-   due status
-   review history

The Decks system should become responsible for:

-   deck definitions
-   personal deck persistence
-   deck membership
-   deck editing
-   deck creation/deletion
-   deck browsing
-   deck-scoped selection for review

The Lexicon should remain responsible for resolving vocabulary and
supplying known lexical data.

------------------------------------------------------------------------

# 14. Implementation principle

Do not redesign the entire Decks/SRS architecture.

Build the user-created deck layer around the architecture that already
exists.

The key separation is:

``` text
Lexicon
    ↓
Vocabulary item
    ↓
    ├── Parlour Deck memberships
    ├── My Deck memberships
    └── one SRS card/state
```

The same SRS card can therefore be reached from:

-   the homepage global review
-   a Parlour Deck
-   a My Deck
-   potentially future filtered study sessions

without creating duplicate memory schedules.

------------------------------------------------------------------------

# 15. UX principle

The experience should take the useful simplicity of:

-   Anki's separation of cards and decks
-   Quizlet's straightforward set creation/editing
-   the older Memrise model of user-created vocabulary collections

without copying their complexity wholesale.

Parlour should feel like a serious language-learning tool.

Keep the UI:

-   clean
-   compact
-   restrained
-   obvious
-   low-friction

The learner should be able to create a useful personal deck in seconds,
add words to it naturally while using Parlour, and review it through the
existing SRS engine.

------------------------------------------------------------------------

# 16. Proposed implementation sequence

Do not implement everything at once.

Recommended sequence:

### Phase 1: Personal deck data model

Implement persistent My Deck definitions and membership.

Support:

-   create
-   read
-   update
-   delete
-   add word
-   remove word

Preserve existing SRS cards.

### Phase 2: My Deck UI

Build:

-   My Decks index
-   Create Deck
-   Edit Deck
-   Deck detail
-   Review Deck

### Phase 3: Lexicon picker

Build vocabulary search/selection for adding words.

Reuse existing Lexicon resolution.

### Phase 4: Global "Add to deck"

Expose the deck picker from vocabulary contexts throughout the app.

### Phase 5: Parlour Deck UI revision

Refine the existing curated deck presentation around the My Decks /
Parlour Decks distinction.

### Phase 6: Homepage integration

Use the existing global due-card system to expose the review queue on
the homepage.

------------------------------------------------------------------------

# 17. Acceptance criteria

The feature is successful when a learner can:

1.  Create a My Deck with any number of words.
2.  Create any number of My Decks.
3.  Add an existing Parlour vocabulary item to a My Deck.
4.  Add a vocabulary item to multiple My Decks.
5.  Add a word to a deck directly from another part of Parlour.
6.  Remove a word from one deck without affecting its SRS state.
7.  Delete a deck without affecting its vocabulary or SRS state.
8.  Review a specific deck using the existing SRS cards.
9.  Review all due cards globally from the homepage.
10. See consistent SRS state for a vocabulary item regardless of which
    deck it was reviewed from.
11. Continue to respect the daily new-word limit for actual SRS
    learning.
12. Have no artificial 20-word limit on personal decks.
13. Keep Parlour Decks read-only.
14. Preserve existing learner SRS data during migration.

The curriculum's vocabulary limits remain curriculum limits and must not
be repurposed as personal deck limits.

------------------------------------------------------------------------

# Final architectural principle

The Decks feature should be understood as a **vocabulary collection
system sitting on top of the existing SRS system**, not as a second
spaced-repetition system.

**Parlour curates vocabulary.**

**Users organise vocabulary into their own collections.**

**SRS remembers the learner's relationship with each word.**

**The homepage surfaces what is due.**
