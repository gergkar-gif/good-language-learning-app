# Parlour Listening: Design Specification

## 1. Two levels of listening

The listening system should eventually have two distinct experiences.

### Listening Driller

Short, controlled listening practice.

- Mainly A1-A2
- Some controlled B1
- Short words, phrases and sentences
- TTS can be used where appropriate
- Focus on decoding and basic comprehension

### Listening Lab

More advanced, authentic listening.

- B1-C1
- Increasingly authentic material
- Interviews
- News
- Podcasts
- Documentaries
- Video
- Existing listening exercises
- Multiple speakers and accents
- Natural speech rate and reductions

The progression should be:

**A1-A2:** predominantly controlled  
**B1:** mixture of controlled and authentic  
**B2-C1:** predominantly authentic

---

## 2. Listening Driller v1

Keep the first implementation light.

### Exercise types

#### 1. Listen → Meaning

Audio:

> *Tengo hambre.*

What does it mean?

- I'm thirsty.
- I'm hungry.
- I'm tired.
- I'm cold.

#### 2. Listen → Spanish

Audio plays and the learner selects the matching Spanish sentence.

#### 3. Listen → Type

Audio plays and the learner types what they heard.

Normalise capitalisation, punctuation and accents. Do not accept arbitrary wording substitutions.

#### 4. Listen → Missing Word

Audio plays, then:

> Mañana trabajo desde _____.

The learner supplies the missing word.

This can be added after the first three if we want to keep v1 particularly small.

---

## 3. Audio behaviour

Audio is the primary information source.

Initial state:

**▶ Play**

After playing:

**↻ Replay**

Rules:

- unlimited replay
- do not penalise replaying
- do not show the transcript before answering
- reveal the transcript after the answer
- no playback-speed controls initially

---

## 4. Listening content

Listening items should have explicit audio and transcript data.

Conceptually:

```text
Listening item
├── id
├── level
├── text/transcript
├── audio
├── translation
├── lemmas
└── type
```

Possible content types:

- word
- phrase
- sentence
- short dialogue

Do not start with long passages in the Driller.

The existing curriculum should provide much of the initial controlled content.

---

## 5. Exercise generation

One listening item should be capable of producing several exercise forms.

For example:

> **Quiero comprar una camisa.**

can produce:

- Listen → Meaning
- Listen → Spanish
- Listen → Type
- Listen → Missing Word

This avoids maintaining four separate exercise banks.

---

## 6. Distractors

Distractors must be linguistically plausible.

For:

> *Quiero comprar una camisa.*

better options include:

- Quiero comprar unos zapatos.
- Quiero buscar una camisa.
- Quiero vender una camisa.

The exercise should test listening, not obvious elimination.

---

## 7. Advanced authentic listening

This should eventually be a separate **Listening Lab**.

A Listening Lab item might contain:

```text
Listening item
├── audio/video
├── transcript
├── source information
├── level
├── duration
├── speaker information
├── comprehension questions
└── target vocabulary
```

Example:

> **Spain's housing crisis**  
> B2 · 4:32 · Authentic interview

Questions can cover:

- main idea
- specific information
- speaker intent
- meaning of an expression in context

The learner should have to understand sustained natural speech.

---

## 8. Source strategy for B1+

We should not assume TTS is sufficient for advanced listening.

Authentic material may come from:

- licensed material
- permissioned material
- public-domain material
- Parlour-produced recordings
- permitted external embeds
- existing educational listening resources

Where appropriate, embed external video/audio rather than downloading and re-hosting it.

The content pipeline needs to respect source licensing and usage conditions.

---

## 9. Levels

The Workshop should eventually support:

- All
- A1
- A2
- B1
- B2
- C1

Reuse the existing CEFR level system rather than creating another taxonomy.

---

## 10. Session structure

The Listening Driller should reuse the existing Workshop session pattern.

### Session

- By Count
- Timed

### Count

- 5
- 10
- 15
- 20
- 30

### Timer

- 1 min
- 2 min
- 3 min
- 5 min

Follow the existing Workshop UI rather than creating a new session system.

---

## 11. Results

Basic results:

> **8 / 10 correct**  
> **80% accuracy**

Potential future listening-specific statistic:

> **Average replays: 1.6**

Replay count should not affect correctness.

---

## 12. Architecture

Reuse the existing Workshop/drill architecture.

Conceptually:

```text
ListeningDriller
       ↓
ListeningRunner
       ↓
audio playback
response handling
feedback
       ↓
existing Workshop session system
```

Do not force audio exercises into the existing `GrammarRunner`.

Listening-specific logic should remain separate while sharing existing session/UI infrastructure.

---

## 13. Engineering principle

Keep the first version **light and quick**.

Do not initially build:

- sophisticated adaptive listening algorithms
- complicated speech recognition
- speed-adjustment systems
- huge exercise databases
- advanced accent modelling
- long-form authentic listening infrastructure
- complex automatic question generation

Build the controlled Listening Driller first.

Then build the **Listening Lab/content pipeline** separately when ready for authentic B1-C1 material.

---

## Core product principle

**Listening Driller teaches the learner to decode spoken Spanish.**

**Listening Lab teaches the learner to understand real spoken Spanish.**

The two should complement each other rather than pretending that the same content technology can do both jobs.
