# Hungarian Workshop: Implementation Handover

## 1. Overall approach

The Hungarian Workshop should **extend the existing Spanish Workshop architecture**, not replace it.

The Spanish implementation is the reference for Workshop navigation, activity loading, exercise rendering, answer checking, scoring/progress, familiarity/SRS integration, content loading, and general UI behaviour.

The Hungarian work should focus primarily on **new linguistic drillers**. Do not redesign the Workshop engine simply because Hungarian has different grammar.

---

## 2. Existing Workshop functions

These should carry over from Spanish with Hungarian content.

### Translation
Same mechanism. Hungarian content should progress more slowly and use shorter, highly controlled sentences at A1-A2.

### Listening
Same mechanism. Hungarian content can eventually exploit vowel length, vowel quality, suffixes/endings, verb endings and prefixes. These are content opportunities, not reasons to create a different Listening engine.

### Vocabulary
Same mechanism. Vocabulary should be **lemma-oriented** where morphology allows it.

For example:

`barátaimmal`

should ultimately connect to:

`barát`

rather than becoming an independent vocabulary item.

### Verb
The existing Verb Driller mechanism should be extended substantially for Hungarian.

---

# 3. New Hungarian Workshop functions

The Hungarian Workshop needs five additional conceptual functions:

1. **Verb**
2. **Case**
3. **Suffix**
4. **Prefix**
5. **Morphology**

These should be implemented as reusable Workshop activity types, with Hungarian data driving the exercises.

---

# 4. Verb Driller

Hungarian verbs need considerably more than a simple conjugation-table drill.

The learner should practise both **decoding** and **producing** verb forms.

### Core capabilities

**Recognition**

Given:

`olvastok`

identify:

- lemma: `olvas`
- tense: past
- person: 2nd plural
- conjugation: indefinite

**Selection**

> Én ___ magyarul.

- beszélek
- beszélsz
- beszél

→ `beszélek`

**Production**

Given:

> `beszélni` + 1SG + present

produce:

`beszélek`

**Transformation**

> te beszélsz → én ...

→ `beszélek`

### Hungarian-specific progression

The system should eventually support:

- person
- number
- present
- past
- indefinite conjugation
- definite conjugation
- common irregular verbs
- verb prefixes
- more complex forms

The learner should be trained to **decode the information contained in the verb**, rather than simply memorise tables.

---

# 5. Case Driller

The Case Driller answers:

> **What grammatical relationship does this form express?**

Examples:

`házban`

→ in the house

`házból`

→ from the house

`házhoz`

→ to the house

### Exercise types

- identify the case
- identify the meaning
- choose the appropriate case
- produce a case form from an English prompt
- recognise the case in context
- distinguish similar case meanings

The Case Driller is about **grammatical function and meaning**.

---

# 6. Suffix Driller

The Suffix Driller answers:

> **What do I attach to this word, and which form should I use?**

Examples:

`barát` + plural

→ `barátok`

`barát` + my

→ `barátom`

`ház` + in

→ `házban`

This is broader than the Case Driller.

Cases are one important type of suffix, but the Suffix Driller should also handle:

- plural
- possession
- case endings
- other productive suffixes as appropriate

## Vowel harmony belongs here

Vowel harmony should be a **core mechanic of the Suffix Driller**, rather than necessarily another top-level Workshop activity.

Examples:

`kocsma + -ban/-ben`

→ `kocsmában`

`város + -ban/-ben`

→ `városban`

`sör + -ban/-ben`

→ `sörben`

The learner should practise:

1. recognising the alternating forms;
2. selecting the correct form;
3. producing the complete word;
4. eventually explaining why that form is selected.

The system should support increasingly difficult vowel-harmony patterns.

---

# 7. Prefix Driller

Hungarian verb prefixes deserve their own activity.

The learner should understand both **meaning** and **behaviour**.

Examples:

`megy` → go

`elmegy` → leave / go away

`bemegy` → go in

`kimegy` → go out

`felmegy` → go up

### Exercise types

**Meaning → prefix**

> go in

→ `be-`

**Form → meaning**

> `bemegy`

→ go in

**Construction**

> `megy` + `be-`

→ `bemegy`

### Later functionality

The Driller should eventually handle prefix movement:

`Bemegyek.`

versus:

`Megyek be.`

This does not necessarily need to be part of the first implementation, but the underlying model should not prevent it.

---

# 8. Morphology Driller

The Morphology Driller teaches the learner to **take Hungarian words apart and construct them**.

Example:

`barátaimmal`

The learner might identify:

- `barát` = friend
- plural/possessive material
- `-m` = my
- `-val/-vel` = with

The exact linguistic segmentation should come from the Hungarian morphological data, not from hard-coded assumptions.

### Exercise types

**Decomposition**

> What is the base/lemma?

`barátaimmal`

→ `barát`

**Recognition**

> What does this component contribute?

**Construction**

> `barát` + plural + my + with

→ `barátaimmal`

**Analysis**

Given a surface form, identify its grammatical components.

This is also the main bridge between the **Reader** and the **Workshop**.

---

# 9. Relationship between the five functions

They should not duplicate one another.

| Function | Core question |
|---|---|
| **Verb** | Who/when/how is the verb marked? |
| **Case** | What grammatical relationship does this form express? |
| **Suffix** | What do I attach, and which form? |
| **Prefix** | What does this prefix do to the verb? |
| **Morphology** | How is this whole word constructed? |

There will inevitably be some overlap, but each activity should have a distinct learning objective.

---

# 10. Shared Hungarian linguistic data

The five drillers should **not each contain their own grammatical rules**.

They should consume shared Hungarian linguistic data.

Conceptually:

```text
                Hungarian linguistic data
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
        Reader        Workshop       Lessons
                         │
        ┌────────────────┼────────────────┐
        ↓        ↓       ↓       ↓       ↓
      Verb     Case   Suffix   Prefix  Morphology
```

The same morphological representation that allows the Reader to understand:

`barátaimmal`

should allow the Morphology Driller to generate an exercise from it.

Likewise, the same suffix data used by the Reader should eventually drive the Suffix and Case drillers.

---

# 11. Data-driven rather than hard-coded

The new drillers should be built around structured content/data.

Conceptually:

```json
{
  "id": "ban_ben",
  "type": "suffix",
  "meaning": "in",
  "forms": ["ban", "ben"],
  "harmony": "vowel"
}
```

The exact schema should be determined after inspecting the existing Workshop/content architecture. Do not assume this example schema must be used.

The important principle is:

> **The engine knows how to generate an activity. Hungarian content/data tells it what to practise.**

---

# 12. What should NOT be built as a separate Hungarian feature

Avoid creating a separate Workshop activity for every Hungarian grammatical phenomenon.

Initially, these should remain part of existing mechanisms:

- general sentence building → existing Sentence Builder
- basic word order → Translation/Sentence Builder
- pronunciation/spelling → Listening and lesson exercises
- general vocabulary → Vocabulary Driller
- general translation → Translation Driller

Only create a new top-level activity when it represents a genuinely distinct learning task.

---

# 13. Recommended Workshop structure

### Core Workshop

- Translation
- Listening
- Vocabulary
- Verb

### Hungarian-specific Workshop

- Case
- Suffix
- Prefix
- Morphology

Vowel harmony is primarily a **Suffix Driller mechanic**, not necessarily a fifth separate Workshop tile.

---

# 14. Implementation priority

1. **Verb**: most important and likely to require the most careful design.
2. **Suffix**: provides the foundation for vowel harmony, plural, possession and case forms.
3. **Case**: builds on the suffix infrastructure but focuses on grammatical meaning.
4. **Prefix**: important for Hungarian verbs and should share data with the Verb system.
5. **Morphology**: connects the above systems and the Reader, and can become richer as the linguistic data improves.

---

# 15. Core architectural principle

Do not build five isolated Hungarian mini-games.

Build:

**one reusable Workshop engine**

plus:

**shared Hungarian linguistic data**

plus:

**Hungarian-specific activity definitions and exercise generators.**

The Spanish Workshop tells us **how the Workshop works**.

The Hungarian implementation should determine **what additional linguistic operations the Workshop needs to practise**.

The goal is a Workshop that feels native to Hungarian without creating a separate Hungarian application architecture.
