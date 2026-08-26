# Parlour Library: Design Specification

## Purpose

The Library should become Parlour's reading environment, with three clear sections:

1. **Parlour**: curated readings supplied by Parlour
2. **Saved**: Parlour readings saved by the learner
3. **My Texts**: texts pasted/imported by the learner

All three should use the same existing Reader.

The Library is for reading and language exposure. It should not become a second lesson system or SRS system.

---

## 1. Library structure

### Parlour

Curated readings organised primarily by CEFR level:

- A1
- A2
- B1
- B2
- C1

Within each level, group readings as:

- **Original**: written specifically for Parlour learners
- **Classical**: selected/adapted material from Spanish-language classics
- **World**: material originating elsewhere and appropriately translated/adapted

Level indicates linguistic accessibility. Category indicates the nature/source of the reading.

Keep the existing collapsible reading-room model.

### Saved

A personal collection of Parlour readings selected by the learner.

Saving should store the canonical reading ID, not duplicate the reading.

Actions:

- Open
- Remove from Saved

A save action should also be available from inside an open reading.

### My Texts

User-owned texts brought into Parlour.

Examples:

- Wikipedia articles
- Spanish news articles
- essays
- stories
- personal texts
- any other Spanish text

They should use the same Reader as Parlour readings.

---

## 2. Main navigation

The Library should have three primary tabs:

**Parlour | Saved | My Texts**

Keep the interface compact and editorial.

---

## 3. Parlour reading cards

Cards should show only useful information, for example:

**Una mañana diferente**

`A1 · Original · 6 min`

Later, useful familiarity information may be shown, such as:

`82% familiar`

Do not overload cards with metadata.

---

## 4. My Texts creation flow

The creation flow should be deliberately simple.

### Add text

**Title**

Required.

**Paste your text**

Large text area.

**Analyse text**

Primary action.

There should be **no source field**.

Do not ask the learner for:

- source
- URL
- author
- publication
- category
- CEFR level

The learner is simply bringing a text into their reading library.

---

## 5. Text analysis

After pasting a text, Parlour should analyse it before saving/opening it.

Useful information can include:

**Estimated level: B2**

**1,247 words**

**~8 min reading time**

### Vocabulary coverage

**82% familiar**

And, where the underlying data supports it:

- recognised vocabulary
- unfamiliar vocabulary
- vocabulary already in the learner's decks
- vocabulary currently due for review

For example:

> 412 recognised words  
> 96 words not yet learned  
> 31 words already in your decks  
> 18 words due for review

Do not invent precision that the analysis cannot support.

---

## 6. Estimated level

My Texts may display an estimated CEFR level.

Example:

`Estimated level: B2`

This is informational, not restrictive.

A learner must be able to read a text regardless of its estimated level.

If reliable automatic estimation is not available, use:

`Level: Unassessed`

Do not represent a user text as an official Parlour B2 reading.

It remains a **My Text**.

---

## 7. My Text cards

Keep these clean.

Example:

**La Revolución Mexicana**

`B2 · 1,247 words · ~8 min`

`82% familiar`

Actions:

- Read
- Edit
- Delete

Do not display source labels, URLs or unnecessary metadata.

---

## 8. Reader integration

A My Text must use the existing Reader.

Do **not** build a separate My Text reader.

It should retain the existing Reader behaviour:

- readable typography
- paragraph structure
- tappable words
- dictionary lookup
- morphology analysis
- phrase detection
- pronunciation where available
- familiarity colouring
- SRS interaction
- Add to Deck

The existing Reader already provides word lookup, phrase detection, morphology-aware readings, pronunciation, familiarity colouring and SRS interaction. Reuse these systems.

---

## 9. Vocabulary interaction

When reading a My Text, tapping a word should produce the existing word popup.

For example:

**comenzó**

`comenzar · verb · preterite`

`began`

The existing Reader resolves inflected forms to canonical lemmas. Preserve this.

---

## 10. Add to My Deck

Library and Decks should integrate.

From a vocabulary popup:

**Add to deck +**

Then show existing My Decks and:

**+ Create new deck**

This should work from:

- Parlour readings
- Saved readings
- My Texts

The selected word should be added as the canonical lexical item.

Do not create duplicate SRS cards.

---

## 11. Vocabulary analysis view

After analysing a My Text, the learner should be able to inspect its vocabulary.

Useful categories:

### Familiar

Words for which the learner has meaningful SRS familiarity.

### New

Words not currently represented in the learner's SRS collection.

### In decks

Words already belonging to one or more My Decks.

### Due

Words currently due for review.

Where practical, allow selection of vocabulary and:

**Add selected words to deck**

The learner chooses an existing My Deck or creates a new one.

Do **not** automatically add every unfamiliar word to SRS.

---

## 12. My Text persistence

My Texts should persist using the app's existing client-side storage architecture.

A record should minimally contain:

- stable ID
- title
- text content
- created date
- modified date
- optional cached analysis data

Do not store unnecessary metadata.

In particular, do not require a source field.

Analysis results are derived data and should be recalculable.

---

## 13. Editing

The learner should be able to edit:

- title
- text

After editing, the text can be re-analysed.

Do not build version history initially.

---

## 14. Deleting

Deleting a My Text should remove only the user-owned text.

It must not:

- delete Lexicon vocabulary
- delete SRS cards
- delete My Deck membership
- affect Parlour readings
- affect Saved readings

---

## 15. Explicitly out of scope

Do not add:

- source fields
- URLs
- author/publication metadata
- required manual CEFR classification
- automatic text rewriting/adaptation
- automatic addition of unfamiliar words to SRS
- public/social user texts
- separate My Text Reader
- unnecessary gamification

---

## 16. Relationship to Decks

The two systems should mirror each other.

### Library

**Parlour** = curated readings  
**Saved** = learner-selected Parlour readings  
**My Texts** = learner-provided readings

### Decks

**Parlour Decks** = curated vocabulary collections  
**My Decks** = learner-created vocabulary collections

The overall product model is:

> Parlour provides curated material. The learner can save, collect and bring in their own material.

---

## 17. Relationship to SRS

Library does not own SRS.

SRS remains a separate layer.

A text can contain:

- familiar words
- unfamiliar words
- words already in decks
- words currently due for review

Reading a text should not automatically flood the SRS system with unfamiliar vocabulary.

The learner decides which vocabulary is worth retaining.

---

## 18. Recommended implementation sequence

### Phase 1
Refine Library into:

- Parlour
- Saved
- My Texts

Preserve the existing reading-room behaviour.

### Phase 2
Implement Saved persistence.

### Phase 3
Implement My Texts:

- Add
- title
- text
- save
- list
- open
- edit
- delete

using the existing Reader.

### Phase 4
Add text analysis:

- word count
- estimated reading time
- vocabulary coverage
- recognised/unrecognised vocabulary
- deck/SRS statistics where reliable

### Phase 5
Add vocabulary selection and Add to Deck.

### Phase 6
Make Add to Deck available consistently from reading contexts throughout the app.

---

## 19. Acceptance criteria

A learner should be able to:

1. Browse Parlour readings by CEFR level.
2. Browse Original, Classical and World readings.
3. Save a Parlour reading.
4. Find saved readings under Saved.
5. Remove a reading from Saved.
6. Create a My Text with only a title and pasted text.
7. Analyse the text.
8. See useful text statistics.
9. See an estimated level when reliable, otherwise Unassessed.
10. Open the My Text in the normal Parlour Reader.
11. Tap words and receive existing dictionary/morphology behaviour.
12. Add vocabulary from the text to a My Deck.
13. Inspect unfamiliar vocabulary.
14. Select vocabulary and add it to a My Deck.
15. Edit a My Text.
16. Delete a My Text.
17. Preserve SRS state when texts are edited or deleted.
18. Keep My Texts clearly separate from curated Parlour readings.
19. Avoid source fields and unnecessary metadata.
20. Avoid automatically flooding SRS with unfamiliar vocabulary.
21. Use the same Reader for Parlour, Saved and My Texts.

---

## 20. Product principle

The Library should become the place where the learner **reads whatever they want to read in Spanish**.

Parlour supplies a structured, levelled reading library.

Saved lets the learner keep the Parlour readings they care about.

My Texts lets the learner bring real Spanish they encounter elsewhere into the same reading environment.

The core loop is:

> **Find or bring in a text → read it → understand words → save useful vocabulary to My Decks → let SRS remember it.**
