# Parlour Planning and Claude Handoff

## Co-production workflow

Parlour is being developed through a co-production workflow between the project owner, ChatGPT, and Claude Code.

**ChatGPT:** planning, research, curriculum and grammar design, content generation/QA, UX decisions, and turning discussions into implementation specifications.

**Claude Code:** implementation and testing. It should inspect the existing codebase, implement the specifications below, preserve the existing architecture unless a change is explicitly required, test its changes, and avoid inventing requirements.

Workflow:
1. Discuss/design with ChatGPT.
2. Consolidate decisions into this document.
3. Give Claude Code a focused implementation task.
4. Claude implements and tests.
5. Review the result with ChatGPT.
6. Update this document when decisions change.

This is a living handoff, not a conversation transcript.

## Token efficiency

Claude Code usage is limited, so work efficiently. Prefer focused implementation over extended discussion. Inspect only files relevant to the current task, avoid repeatedly rereading the whole codebase, batch related changes where practical, and keep responses concise. Do not spend tokens explaining routine changes unless there is an important problem, ambiguity or architectural decision.

# Current A1 revision requirements

## Curriculum
- Structure: **Level → Unit → Lesson → Exercise**.
- A1 consists of thematic/functional units.
- Each unit has **6–7 lessons**.
- Lessons should genuinely take roughly **5–10 minutes**.
- Remove the lesson-duration indicator from the interface for now.
- Each unit contains **2 review lessons**.
- Review lessons contain **no new grammar, vocabulary, reading or other new material**. They focus on grammar/vocabulary retrieval and checking.
- Maximum **20 new vocabulary items per unit**, preferably close to 20.
- Vocabulary should recur naturally, but should not be mechanically presented three times in every lesson.
- Earlier grammar/vocabulary should periodically return through review lessons.
- Readings must only be used after the learner has enough language to understand them.

## LatAm Spanish
- The course is **Latin American Spanish**.
- Remove `vosotros` from readings, grammar explanations, examples and normal course content.
- `vosotros` may remain in the dedicated verb drill as optional recognition.
- Use `ustedes` for plural 'you'.
- Keep vocabulary/examples broadly suitable for Latin American learners.

## Exercise behaviour

### Multiple choice
- Randomise answer-option order.
- Never allow the correct answer to be predictably positioned at the top.

### Sentence Builder
The interaction should resemble a tile-based construction model such as Duolingo:
- Learner sees Spanish word tiles.
- Learner can move tiles freely to construct the sentence.
- **Do not show the English translation before completion.**
- After the learner completes/submits the Spanish sentence, display the **English translation** as feedback.
- Clearly indicate whether the constructed sentence is correct.
- Do not unnecessarily constrain tile movement.

### Word Match
Use natural casing:
- `la leche → milk`
- `el café → coffee`
- `Good day! → Buen día!`
Do not capitalise ordinary vocabulary items merely because they appear at the beginning of a card. Capitalise actual sentences normally.

### Sentence-order exercises
- Maximum **2 per unit**.
- They must produce useful, natural sentences.
- Avoid artificial sentences whose only purpose is demonstrating word order.
- Existing sentence-order exercises need particularly strict QA because nonsensical examples recur.

### Conjugation prompts
Never ask for a specific conjugation if the subject/person is not clear. Make the subject explicit or otherwise unambiguous.

### Multiple valid answers
Where more than one answer is grammatically valid, accept the valid alternatives. This applies to interchangeable names/nouns and similar cases.

## Teaching/content principles
- Grammar explanations should be short, explicit and natural.
- Explain why a structure works, not just what form to memorise.
- Avoid awkward phrases such as `run on`; prefer natural wording such as `uses`, `is used to`, `means`, etc.
- Parlour should explain grammar more explicitly and gradually than fast implicit-learning apps.
- Concepts unfamiliar to English speakers should receive enough explanation before drilling.
- Context should be integrated into lessons/exercises, not become a separate tab/system.
- Exercises should progress: **recognise → manipulate → construct → retrieve → use**.
- Vary exercise types rather than repeatedly testing the same grammar in one format.

## Grammar → Workshop
After teaching a verb conjugation pattern, provide a clear route into Workshop practice where the architecture supports it:
- direct recommendation/link to the relevant Workshop drill
- simpler dedicated drill for regular verb conjugation where appropriate
- use the same underlying grammar-skill IDs across lessons, exercises, Workshop and grammar reference.

## Readings
- Early readings are too long/complex for the level. Make them shorter and simpler.
- Reduce repetitive use of `sonreír` and `sonrisa`.
- The Carlos and Meg narrative should visibly develop, including the relationship progression.
- Reading-dependent exercises must appear **after** the relevant reading.
- Avoid using vocabulary/grammar not yet taught.

## Decks
- Decks should be collapsible by group.
- Grouping may also be hierarchical by level where appropriate.
- Keep the interface compact.

# Specific lesson corrections

- **L1 S2:** delete Lingolia sentence.
- **L2 S2:** delete Lingolia sentence; rewrite/delete `because the article is the easiest`.
- **L2 S11:** `taco` appears as `peg` in reader. Correct.
- **L2 S19:** remove/rewrite `say por favor` writing prompt.
- **L3a S2:** remove Lingolia sentence.
- **L3a S11:** `I can say who someone is...` is not taught. Remove or align.
- **L3c S5:** Lauren and Kaylee should be interchangeable where grammar permits.
- **L5 S5:** investigate why `nuestro` is required; accept/use `mi/tu/su` etc. where grammatically valid.
- **L5 S9:** ordering exercise is too soon. Replace/move.
- **L6 S2:** final `both are...` sentence does not make sense. Rewrite.
- **L7 S7/S9:** reading-dependent exercises appear before the reading. Fix.
- **L8 S2:** rewrite awkward `the difference...` sentence.
- **L8 S8:** `arroz` and `verduras` should be interchangeable where grammar permits.
- **L8 S9:** reading-dependent exercise appears before reading. Fix.
- **L9 S9:** reading-dependent exercise appears before reading. Fix.
- **L10:** delete `soplar las velas` and `pedir un deseo`; not appropriate at this A1 stage.
- **L10 S8:** exercise is too difficult. Simplify.
- **L10 S9:** reading-dependent exercise appears before reading. Fix.
- **L11 S3:** rewrite awkward `the common verbs...` sentence.
- **L11 S9:** replace nonsensical sentence-order exercise.
- **L12 S9:** replace awkward sentence-order exercise.
- **L13 S9:** replace nonsensical sentence-order exercise.
- **L14 S8:** unclear exercise. Review/rewrite.
- **L15 S3:** rewrite awkward grammar explanation.
- **L15 S9:** replace nonsensical sentence-order exercise.
- **L16 S6:** audit subject clarity. Do not require a specific conjugation when the subject/person is not indicated.
- **L16 S9:** replace nonsensical sentence-order exercise.
- **L17 S9:** replace nonsensical sentence-order exercise.
- **L18:** delete reading; make review hardcore grammar/vocabulary drilling and checking with no new material.
- **L18 S12:** replace poor sentence-order exercise.
- **L19:** delete reading and S14 exercise.
- **L20:** delete reading and S13 exercise.

# Design direction
- Parlour should feel like a serious language-learning tool rather than a gamified children's app.
- Keep the interface clean and restrained.
- Avoid emoji-like lesson icons; use the established simple editorial/SVG visual language.
- Do not add interface elements merely because another language-learning app has them.
- Core navigation: **Learn → Library → Workshop → Decks → Journey**.
- Library is primarily for reading.
- Workshop is for active manipulation and production.
- Decks are for review.
- Grammar reference is a permanent lookup resource, not another lesson sequence.

# Immediate implementation priority

1. Fix global exercise behaviour: multiple-choice randomisation, Sentence Builder free tile movement, post-completion English translation, Word Match casing.
2. Fix curriculum/content rules: unit/lesson structure, review lessons, vocabulary limits, LatAm-only course content, lesson-duration indicator removal.
3. Fix exercise dependency and quality issues.
4. Fix the listed lesson-specific problems.
5. Review readings for A1 level, length, repetition and narrative continuity.
6. Implement Decks collapsibility.
7. Add Grammar → Workshop drill recommendations where supported by the existing architecture.

Do not expand scope beyond these requirements without discussing the proposed change first.
