# B1 Content Specification

This document defines the JSON shape every B1 lesson, grammar, exercise,
vocabulary and story file must have. It is the document to hand to a
generator (human or ChatGPT) alongside `B1_GUIDE.md` (curriculum design) and
`Parlour B1 Consolidated Unit List.md` (the 72-unit plan, both tracks) —
those two say *what* each unit teaches; this says *what file to write and in
what shape*.

It is grounded directly in the current schemas
(`content/es/schemas/*.schema.json`) and in the actual A1/A2 production
files, not in `a1-content-spec.md`, which describes an earlier one-file-per-
lesson layout the content has since moved on from. Where this spec disagrees
with `a1-content-spec.md`, this one is current — A1 itself no longer matches
its own spec document in several respects (see §8).

---

## 1. Unit → file layout

A unit is **six lesson files**: five teaching lessons and one consolidation.
This is the existing A1/A2 pattern, unchanged in shape for B1 — only the
per-lesson exercise and vocabulary counts grow (§4, §6).

```
content/es/lessons/b1/b1-{unit}-01.json   ...   b1-{unit}-05.json
content/es/lessons/b1/b1-{unit}-consolidation.json
```

Every lesson file has a matching exercise file, and every teaching lesson
(01–05) has a matching grammar file per grammar section (§5) and a matching
vocabulary file:

```
content/es/exercises/b1/b1-{unit}-01-ex.json   ... b1-{unit}-consolidation-ex.json
content/es/grammar/b1/b1-{unit}-01-{topic}-gr.json
content/es/vocabulary/b1/b1-{unit}-01-voc.json
```

The unit's one story lives in **lesson 05 only** (§7) — never repeated
across the other four teaching lessons, and never present in consolidation.

### 1a. The `{unit}` token differs by track

**Core Spanish** units are numbered `01`–`36`, matching their position in
the Consolidated Unit List (Part I).

**Latin America** units cannot also be numbered `01`–`36` — `lesson.b1.01.01`
would collide between "Core Unit 1, Lesson 1" and "Latin America Unit 1,
Lesson 1", because none of the id patterns in the schemas
(`lesson.schema.json`, `vocabulary.schema.json`, `exercises.schema.json`)
carry a track field. This is a real gap in the engine — there is no `track`
concept anywhere in `curriculum.json` or `journey.js` yet — and fixing it
properly is separate work. Until then, **Latin America units use a
lowercase word slug instead of a number** as `{unit}`, e.g.:

```
content/es/lessons/b1/b1-precolombina-01.json
content/es/lessons/b1/b1-conquista-01.json
content/es/lessons/b1/b1-independencia-01.json
```

This is legal today: the id patterns accept `[a-z]+` as an alternative to
`\d{2}[a-z]?` (the same escape hatch `a1-cafe-01` already uses). No hyphens
or digits inside the slug. Pick one short, distinctive word per Latin
America unit from its title in the Consolidated Unit List (Part II) — e.g.
Unit 1 "Pre-Columbian America" → `precolombina`, Unit 8 "La independencia" →
`independencia`. Keep a slug-to-unit-number lookup somewhere (a comment in
the unit list, or a small table in this file) so nothing has to be
reverse-engineered later; it does not need to be in this spec today, but
**do not generate content for a Latin America unit without first fixing its
slug**, since changing it later breaks every id, ref and SRS key derived
from it.

### 1b. ids

Every id follows the pattern already in the schema, substituting `b1` for
the level and the track's `{unit}` token from §1a:

| File | Pattern | Example (Core) | Example (Latin America) |
|---|---|---|---|
| Lesson | `lesson.b1.{unit}.{NN\|consolidation}` | `lesson.b1.01.01` | `lesson.b1.precolombina.01` |
| Vocabulary | `vocab.b1.{unit}.{NN\|consolidation}` | `vocab.b1.01.01` | `vocab.b1.precolombina.01` |
| Exercises file `lesson` field | `b1-{unit}-{NN\|consolidation}` | `b1-01-01` | `b1-precolombina-01` |
| Exercise id | `b1-{unit}-{NN}.exNN` | `b1-01-01.ex01` | `b1-precolombina-01.ex01` |
| Grammar | `grammar.b1.{unit}.{NN}.{topic}` | `grammar.b1.01.01.preterito-indefinido` | `grammar.b1.precolombina.01.geografia` |

### 1c. What a unit may assume is already known

Core Unit *N* may assume everything taught by Core Units 1 through *N*−1
(per their rows in the Consolidated Unit List) plus all of A1 and A2 — and
nothing from Unit *N*+1 onward. This matters more than it looks: Unit 2,
"Experiences & Memories" (imperfecto for memories, indefinido for
experiences, pluscuamperfecto, connectors), covers almost the same
grammatical ground as Unit 1, "Telling Stories" (indefinido, imperfecto vs
indefinido, pluscuamperfecto, connectors). That overlap is fine — B1
consolidates narrative tenses across several units before moving on — but
it means a unit's own identity has to come from its vocabulary and its
Latin America counterpart's content, not from a grammar point no earlier
unit has already claimed. Don't write Unit 2 as Unit 1 with nouns swapped,
and don't reach forward and rely on a grammar point a later unit is
supposed to introduce first.

---

## 2. Section order (per lesson)

Fixed by `lesson.schema.json`'s `sections` description, and the only order
the engine understands — there are exactly eight section types
(`goal`, `recycle`, `grammar`, `exercise-group`, `vocabulary`, `story`,
`srs`, `checklist`); anything else silently renders nothing (see §8).

**Core teaching lesson (01–05):**

```
goal → recycle → grammar → exercise-group "Practice" → vocabulary
  → [story → exercise-group "Reading"]   (lesson 05 only)
  → exercise-group "Listening" → exercise-group "Dialogue"
  → exercise-group "Writing" → srs → checklist
```

**Latin America teaching lesson (01–05) — revised 2026-08-27, see §3:**

```
goal → recycle → story → vocabulary → grammar
  → exercise-group "Practice" (one light group) → srs → checklist
```

Latin America no longer shares Core's shape. The reading moves first (not
last, and not only in lesson 05 — every teaching lesson gets its own), and
the four exercise-group split (Practice/Reading/Listening/Dialogue/Writing)
collapses into one light group. See §3 for why and the full rationale.

**Consolidation lesson:**

```
goal → recycle → exercise-group "Review" → checklist
```

No grammar section, no vocabulary section, no srs section, no story — this
follows the settled A1 review-lesson rationale (`a1-content-spec.md` §4c):
nothing new is being taught, the block's words are already in Decks, and a
"review screen" would either repeat a screen already seen or become a new
grammar explanation, which is what the next lesson is for. A2's
consolidation lessons keep an `srs` section despite having no vocabulary —
that is drift, not a second convention; B1 consolidation should not carry
one.

---

## 3. Latin America lessons: reading-first, exercise-light (revised 2026-08-27)

**This section replaces the original Latin America design.** The original
version put one short (150–350 word) story in lesson 05 only, with the
other four teaching lessons carrying nothing but a Focus/grammar screen and
a full Core-sized exercise block (16–19 exercises across four groups). An
audit of the shipped content (starting with `lesson.b1.precolombina.02`,
"Grandes civilizaciones" — the Maya/Mexica/Inca lesson) found this
produced lessons that were structurally complete but hollow: the Focus
screen's 3–4 example sentences were the *entire* factual content of the
lesson — the same sentences were then reused verbatim as the story (when
the unit's one story happened to cover that lesson's topic at all) and
recombined into every exercise. A learner could finish "Grandes
civilizaciones" without learning one specific, memorable fact about the
Maya, Mexica or Inca beyond "they existed in different places and were
different from each other" — the lesson's entire vocabulary list was three
proper nouns that translate to themselves (`Maya → Maya`). Reasoning
through abstract-policy units (Neoliberalismo, Democratización) made this
worse, not better — with no named country, leader or date to anchor it,
those Focus screens could describe any country's economic policy in any
decade. See `TROUBLESHOOTING_BACKLOG.md`'s Latin America audit entries for
the full findings.

Direct user feedback drove the rebuild: *"if someone finishes the Maya
lesson, they should be able to have a five to fifteen minute conversation
about the Mayas... they should have some fun facts... the grammar comes
before the actual reading, so it doesn't really stick together... this
should be a primarily reading-focused lesson, and not just lesson, but a
whole track — reading and information heavy, and recall and exercise
light."*

**The new model, per teaching lesson (01–05), reading-first:**

1. **`story`** — every teaching lesson gets its own dedicated reading, not
   just lesson 05. Substantial: **400–700+ words**, real names, dates,
   places and numbers, not generic sentence templates ("a great political
   centre was built that dominated neighbouring territories" — with
   neither the centre nor the territories ever named — is exactly what
   this replaces). At least one explicit "¿Sabías que...?" (did you know)
   aside per reading, genuinely surprising, not a restatement of the main
   text. Directly address at least one thing historians still debate or a
   common misconception worth correcting (the Maya rebuild's example:
   correcting "they disappeared" — the languages and millions of
   descendants are still there). This is the lesson's centrepiece; it goes
   first because reading is the point, not a coda after the drilling.
2. **`vocabulary`** — real, transferable content words drawn from the
   reading (aim for 8–10, not 3), never proper nouns that translate to
   themselves. A word belongs here only if it does real work beyond this
   one lesson (`glifo`, `imperio`, `calendario` — not `Maya → Maya`).
3. **`grammar`** — comes *after* the reading, not before, and its worked
   examples are **sentences lifted verbatim from that lesson's own
   story**, not a separately-authored set. This is what makes the grammar
   and the reading "stick together" rather than being two disconnected
   pieces of content that happen to share a lesson: a learner meets the
   construction once, in context, doing real work, then sees it named and
   explained using the exact sentence they already read. The grammar point
   itself is still one of the four extension points below (voz pasiva, se
   pasiva/impersonal, gerundio, formal connectors) — that framework was
   sound and is unchanged; only where its examples come from changes.
4. **`exercise-group` "Practice" — one light group, roughly 6–9 exercises**,
   not 16–19 across four groups. Majority (5–6 of them) should be
   `category: "reading"` comprehension questions that test whether the
   learner actually understood and retained the reading's specific facts —
   "¿Por qué dicen los historiadores que los mayas nunca formaron un solo
   imperio?" with a real answer requiring comprehension, not "¿Cuál
   afirmación corresponde al tema?" with the correct option being a
   sentence the learner was just shown verbatim (§5a already banned this
   pattern; it matters even more now that reading is the centrepiece it's
   meant to test). The rest (2–3) are grammar-pattern practice built from
   the *same* sentences the story and Focus screen already used — a
   `fill-blank` or `sentence-builder` reconstructing a sentence the
   learner has now met three times (reading, grammar example, exercise),
   which is real spaced reinforcement, not three unrelated exposures to
   the same idea. One `matching` for the new vocabulary is fine; keep it
   to two matching blocks of ≤5 pairs each if the word list runs to 8–10,
   rather than one crowded block.
5. `srs` → `checklist`, unchanged.

**Difficulty must actually escalate across the level, not just get
longer.** The original story-length bands (§7) scaled word count from
150–250 up to 250–350 across the 36 units, but register stayed flat —
sampled units from early, middle and late in the sequence read at
essentially the same sentence complexity. The user's direction is explicit
that this track can run **closer to B2 than strict B1**, and should get
harder as it goes: 

| Units | Register target |
|---|---|
| 1–12 (early) | Solid B1 — the register floor in §5a, not pushed further |
| 13–24 (mid) | B1, leaning B1+: denser subordination, more formal connectors used more often |
| 25–36 (late) | B1+ leaning B2: longer sentences, more formal/abstract vocabulary, faster pacing |

This is a register and density change, not a grammar-inventory change —
late units should not require grammar Core/Latin America hasn't taught;
they should read like a more demanding treatment of material the learner
is, by that point, actually ready for.

**Status as of 2026-08-28: Units 1-6 (all thirty teaching lessons)
rebuilt to this model** (`lesson.b1.precolombina.01-05`,
`lesson.b1.civilizaciones.01-05`, `lesson.b1.llegadaeuropeos.01-05`,
`lesson.b1.conquista.01-05`, `lesson.b1.sociedadcolonial.01-05`,
`lesson.b1.economiacolonial.01-05` — each with its own dedicated story,
not a story shared across the unit; grammar, vocabulary, exercises and
lesson-flow all rewritten in every lesson; see their files for a worked
example of every rule above, including the one-story-per-lesson shape
§7's Latin America override describes). All 30 other Latin America units
still follow the original model and need the same rebuild. Treat this
section, not the original text below it, as current — the
grammar-extension-point list and the thematic-pairing table (§3a) are
unaffected and still apply as written.

### 3.0 The Focus/grammar screen's own content rules

The schema has no "historical context" or "content" section type — only
`grammar`, which is generic underneath (`text`, `table`, `examples`, `tip`,
`external-link` parts; none of the field names are grammar-specific). Latin
America teaching lessons use the `grammar` section type, now positioned
after the story per the model above:

- `text` — brief framing of the grammar point itself (≤150 words — shorter
  than the old ≤300-word budget, since the historical content now lives in
  the story, not here)
- `examples` — 3–5 sentences **lifted verbatim from that lesson's own
  story** (not separately authored) that demonstrate the point
- `tip` — a distinction or usage note about the grammar point
- `external-link` — optional; when used, `site` should name the actual
  source (a museum, archive or reference work) rather than defaulting to
  Lingolia, which has nothing relevant to link to for this track

**The Focus screen also carries one grammar-extension point per unit.**
Core's B1 sequence is built around personal narration and everyday
functions and never needs the structures formal historical writing leans
on. Rather than re-teach a tense Core has already covered, each Latin
America unit should introduce or deepen **one** of these, chosen for
whatever fits the unit's actual content:

- **voz pasiva** (*fue conquistado por, fueron gobernados por*) — the
  passive Core's personal-narrative units never need
- **se pasiva / impersonal** (*se estableció, se exportaba, se firmó el
  tratado*) — the depersonalised historical-event construction
- **gerundio for background/parallel action** in narration (*gobernando
  el país, la economía crecía*) — distinct from Core's imperfecto, which
  covers background description but not two actions running in parallel
- **formal register connectors** historical/academic prose uses that
  Core's conversational register skips (*a raíz de, a lo largo de, en el
  marco de, como consecuencia de*)

This is one extra worked example or a short second `text` paragraph
introducing the structure — not a second grammar lesson. The Focus screen
stays primarily historical content; treat the grammar point as a layer on
top, sized so the whole file still fits the ≤300-word prose budget and
3–5 worked examples from §5. Pick a different one of the four across a
unit's five lessons rather than reusing the same structure five times.

Latin America lessons still recycle Core grammar in their exercises beyond
the one point above (a `fill-blank` about a colonial economy can still
exercise the imperfecto), and `recycle` in a Latin America lesson pulls
from **both** tracks' completed lessons — nothing in `engine/recycle.js`
restricts it by track, and the two tracks are meant to reinforce each
other.

---

## 3a. Thematic pairing with Core

Core is a functional/communicative syllabus (Telling Stories, Relationships,
Work, Travel...); Latin America is a chronological history course
(Pre-Columbian → Conquest → Colonial era → Independence → 20th century).
The two do **not** share a unit-by-unit theme order — Core unit *N* and
Latin America unit *N* are unrelated by default, and forcing them to align
would break one syllabus's internal logic (you can't teach independence
before colonization just to match Core's unit numbering).

Instead: **where a Latin America unit's topic genuinely overlaps a Core
unit's theme, regardless of unit number, deliberately expand that Core
unit's vocabulary** — reuse its domain, go further into it, don't
re-teach the same words. **Where no real overlap exists, fall back to
plain cumulative** (check `decks.json` per §4a as usual; no topical
matching to chase).

| Latin America unit | Paired Core unit | Latin America unit | Paired Core unit |
|---|---|---|---|
| 1. Pre-Columbian America | *cumulative only* | 19. Populismo | 18. Politics & Public Life |
| 2. Civilizaciones indígenas | *cumulative only* | 20. Industrialización | 19. Money & the Economy |
| 3. La llegada de los europeos | *cumulative only* | 21. La Revolución cubana | *cumulative only* |
| 4. La conquista | *cumulative only* | 22. La Guerra Fría | 18. Politics & Public Life |
| 5. La sociedad colonial | 17. Society & Inequality | 23. Estados Unidos y América Latina | 18. Politics & Public Life |
| 6. Economía colonial | 19. Money & the Economy | 24. Gobiernos militares | 28. Rules, Rights & Responsibilities |
| 7. Raza, clase y poder | 17. Society & Inequality | 25. Represión política | 28. Rules, Rights & Responsibilities |
| 8. La independencia | 18. Politics & Public Life | 26. Centroamérica: Revolución y conflicto | *cumulative only* |
| 9. Las nuevas repúblicas | 18. Politics & Public Life | 27. Las dictaduras del Cono Sur | 28. Rules, Rights & Responsibilities |
| 10. Caudillismo | 18. Politics & Public Life | 28. La crisis de la deuda | 19. Money & the Economy |
| 11. Nación y nacionalismo | 28. Rules, Rights & Responsibilities | 29. Neoliberalismo | 19. Money & the Economy |
| 12. Liberalismo y modernización | 25. Change & Development | 30. Democratización | 28. Rules, Rights & Responsibilities |
| 13. Las economías de exportación | 19. Money & the Economy | 31. Movimientos indígenas | 29. Migration & Identity |
| 14. Cambio social | 25. Change & Development | 32. Integración regional | 30. Culture, Language & Society |
| 15. Revolución | *cumulative only* | 33. El final de la Guerra Fría | 18. Politics & Public Life |
| 16. La Revolución mexicana | *cumulative only* | 34. América Latina en los años 90 | *cumulative only* |
| 17. Nacionalismo y Estado | 28. Rules, Rights & Responsibilities | 35. El legado del siglo XX | *cumulative only* |
| 18. La Gran Depresión | 19. Money & the Economy | 36. América Latina hacia el año 2000 | *cumulative only* |

A single Core unit gets paired against several Latin America units on
purpose (Politics & Public Life and Money & the Economy each recur eight
times) — that's expected, not a sign to spread pairings more evenly. Each
of those Latin America units adds its own specific layer (nationalism
vocabulary, populism vocabulary, Cold War vocabulary...) on top of the
same Core baseline; they are not competing to "own" the pairing.

---

## 4. Vocabulary

Per unit, across the six lessons: **16 new words**, split `4 / 3 / 3 / 3 / 3
/ 0` across lessons 01–05 and consolidation. This is now baked into the
Consolidated Unit List's per-lesson `New words:` counts for both tracks —
copy them directly rather than re-deriving a split.

Every word must:
- appear in the vocabulary file for its lesson (`vocabulary.schema.json`
  shape: `lemma`, `translation`, `pos`)
- appear in the lesson's exercises (at least one)
- appear in the unit's story if the word belongs to lesson 05, or — for
  words from lessons 01–04 — appear somewhere in the unit's story too,
  since it is the one text the whole unit shares (this is the existing
  A1 `audit-lesson.py` rule, applied per-unit rather than per-lesson: a
  part without its own story is still checked against the unit's story)

Latin America vocabulary should deliberately overlap with Core: a word
taught in a Core unit does not need to be re-taught in a Latin America unit
to be used by it, but a term specific to the historical content (*régimen*,
*dictadura*, *desaparecido*) is new vocabulary for that Latin America
lesson regardless of how many Core units come before or after it. When
§3a's pairing table gives the unit a paired Core theme, prefer choosing new
words that extend that Core unit's domain (Core's "Money & the Economy"
taught the everyday economic vocabulary; a paired Latin America unit adds
the historical/institutional layer — *deuda externa*, *exportación*,
*devaluación* — rather than words unconnected to that domain). When the
table marks a unit cumulative-only, just pick whatever the historical
content actually needs.

### 4a. Check against what the course has already taught

Before choosing a unit's 16 words, check
`content/es/decks/decks.json` — its top-level `words` object is every
lemma taught anywhere in the course so far (A1, A2, and every already-built
B1 unit), generated straight from the vocabulary files by
`build-manifest.py`. It exists for the Decks tab, but it is also the
easiest way to answer "has this word already been taught?" without fetching
every vocabulary file individually.

This isn't a hypothetical: Unit 1's Lesson 5 already taught *recuerdo*
("memory"). Unit 2, "Experiences & Memories," would reach for that exact
word by instinct. Reusing an already-taught word isn't wrong — the course
wants recycling — but it must be a **choice**, not an accident: a word
already in `decks.json` doesn't count toward the unit's 16 new words, and
doesn't need its own vocabulary-file entry, matching-pair, or fresh
introduction. Only count and introduce words that are genuinely new.

---

## 5. Grammar (Core) / Focus (Latin America)

One file per teaching lesson (lessons 01–05; consolidation has none).

- ≤300 words of prose across all `text`/`tip` parts
- 3–5 worked examples (`examples` part)
- one `external-link` recommended, not mandatory (a missing one is a
  warning, not a failure — same as the existing A1 rule)
- one concept per file. A unit whose grammar needs more room than one
  700-word-lesson screen can comfortably hold should be split the way A1
  splits an overloaded lesson into parts (`a1-content-spec.md` §4b) —
  prefer narrowing what lesson 3, say, tries to teach over cramming two
  grammar screens into one lesson

---

## 5a. Register floor: hitting the target isn't enough

Unit 1's first draft passed every structural rule in this document — right
word counts, right section order, right exercise-block split — and still
read as A2, sometimes A1, because nothing here said how *complex* a sentence
had to be, only what grammar point or topic it had to touch. That gap is
now closed.

**Isolated grammar drills are exempt.** A `fill-blank` or `sentence-builder`
in the Practice block that isolates one clause to test one form
(`"Ayer __ algo inesperado. (ocurrir)"`) is correct pedagogy, not a defect —
narrowing to one thing is the point of a drill.

**Everything that models how the language is actually used is not exempt.**
That means the Grammar/Focus screen's `examples`, the story, every
`Dialogue`-block exercise, `structured-writing` answers, and Consolidation's
`Review` block. In each of these, **at least half the Spanish must combine
two clauses** — a connector (*mientras, aunque, ya que, sin embargo, porque,
cuando, lo que*), a relative clause, or a comparison — not a run of isolated
simple declaratives. A Focus screen's four examples should not read like
four vocabulary flashcards stitched into sentences.

This is exactly what went wrong in Latin America Unit 1's Focus screens.
Concretely, from `b1-precolombina-01-geography-and-historical-context-gr.json`:

> ✗ *"La selva ofrecía recursos diversos."* — subject, verb, object. Nothing
> a learner couldn't produce at A2.
>
> ✓ *"La selva, que cubría gran parte del territorio, ofrecía recursos que
> las comunidades aprovechaban de formas distintas."* — same content, two
> relative clauses, and it now actually needs B1 syntax to parse.

And from the exercise file, where the dialogue-complete block used the
identical two-line template in every lesson without ever supplying a reason:

> ✗ *"¿Qué sabes sobre este tema?" → [fact] → "¿Por qué?" → [same fact
> repeated]* — the "why" question goes unanswered.
>
> ✓ *"¿Por qué es importante este período?" → "Porque explica cómo se
> formaron las sociedades que los europeos encontraron después."* — a real
> causal connector, doing real work.

Three more patterns from the same draft to specifically avoid, because each
one technically satisfies its exercise type's schema while testing nothing:

- **Multiple-choice that asks the learner to recognise a sentence they were
  just shown** (`"¿Cuál afirmación corresponde al tema «geography»?"`, with
  the correct option being the example sentence verbatim) is not a
  comprehension question. Write one that requires understanding the content,
  not matching strings.
- **`sentence-order` items need an actual sequence** — temporal, causal, or
  logical — that a learner can reason through. Three unrelated facts in
  arbitrary order (*"La cordillera atravesaba grandes territorios." / "Las
  comunidades se adaptaban a su entorno." / "Existían diferencias
  regionales."*) has no correct answer beyond the one the file happens to
  declare.
- **`dialogue-complete` wrong options must be plausible near-misses in the
  same register**, not absurd non-sequiturs (*"No lo sé mañana."*, *"Mañana
  había ocurrido."* — the latter isn't even grammatical). A wrong option a
  learner could imagine a real speaker saying is what makes the right one
  worth choosing.

---

## 6. Exercises

Nine exercise types render in a lesson today: `matching`,
`multiple-choice`, `fill-blank`, `sentence-builder`, `sentence-order`,
`dialogue-complete`, `structured-writing`, `listening-choice`, `dictation`.
**`error-correction` is defined in the schema but not yet rendered by
`engine/lessons.js`** — it only works in Workshop's Grammar Driller. Do not
put it in a lesson's `exerciseRefs`; it will be requested and silently
skipped.

Every `fill-blank` whose answer is an open verb choice (not a fixed phrase
with only one possible completion) needs a parenthetical hint baked into
`sentence`, e.g. `"Ayer __ en el festival. (bailar)"` — otherwise the
correct answer is unrecoverable from context. This was missed across
`a2-17-01` through `a2-17-consolidation` and only caught when a learner hit
it in the Grammar Driller; check for it explicitly at B1's volume rather
than relying on a later audit to catch it again.

**`teaches` slugs must match across units, not just be internally
consistent within one file.** `generated/indexes/grammar-index.json` (built
by `scripts/build_grammar_index.py`) groups every exercise in the course by
its `teaches` slug to build Workshop's Grammar Driller pool — a grammar
point that recurs across units only pools together if every occurrence
uses the exact same slug. Before inventing a new slug, check that index for
one that already means the same thing (Unit 1 already uses
`preterito-indefinido`, `pluscuamperfecto`, `narrative-connectors`, and
others — reuse them rather than writing a near-duplicate like
`pluscuamperfecto-narrativo`).

### Block split, per lesson

**Core only.** Latin America's exercise block is lighter and shaped
differently — one "Practice" group of 6–9 exercises, majority reading
comprehension — per §3's revised model, not the table below.

| Lesson | Practice | Reading | Listening | Dialogue | Writing | Total |
|---|---:|---:|---:|---:|---:|---:|
| 01 | 9 | — | 2 | 3 | 2 | 16 |
| 02 | 9 | — | 2 | 3 | 2 | 16 |
| 03 | 9 | — | 2 | 3 | 2 | 16 |
| 04 | 9 | — | 2 | 3 | 2 | 16 |
| 05 | 8 | 4 | 2 | 3 | 2 | 19 |
| consolidation | — (single "Review" block) | | | | | 18 |

These totals sit inside the ranges already fixed per lesson in the
Consolidated Unit List (15–17 / 15–18 / 16–18 / 16–18 / 18–20 / 18) — the
table above is the concrete split to author against so 72 units come out
consistent rather than each improvising a different mix.

- **Practice must span at least 6 distinct exercise types** (raised from
  A1's 5, since B1 draws on a wider grammar range per lesson and there are
  9 usable types to draw from).
- **Reading** exists only in lesson 05, asks about the unit's shared story,
  and its exercises carry no `teaches` tag (same rule as A1: a reading
  question is about one specific text, not a recyclable concept).
- **Listening** exercises are `listening-choice` or `dictation`, spread
  across every teaching lesson rather than concentrated in one — this is
  what actually delivers `B1_GUIDE.md` §14's listening progression (clear
  short recordings early, natural multi-speaker speech late), since there
  is no single "Listening class" slot in the six-lesson unit.
- **Consolidation's "Review" block is one exercise-group of 18**, not a
  Practice/Reading/Dialogue/Writing split — following A1's `audit_review()`
  design rather than A2's (which just repeats the teaching-lesson split).
  A1's reasoning holds at B1's scale better than A2's: every Review exercise
  must carry `teaches`, the block must span **at least 6 distinct types**,
  and the union of `teaches` tags across the block must cover **at least 6
  distinct points** — that last rule is what stops a "consolidation" being
  eighteen drills of the same one thing. This number was originally set to
  10 (matching A1 scaled up), which Units 1-3 hit comfortably — but only by
  splitting each lesson's grammar point into several near-duplicate slugs
  (`imperfecto` *and* `imperfecto-habitual`, `narrative-connectors` *and*
  `connectors`), which directly contradicts the slug-reuse rule this
  section itself asks for. A five-lesson unit genuinely has about five
  grammar points plus vocabulary — six distinct points, tagged honestly, is
  the real ceiling without either fragmenting slugs or reaching into other
  units' content (which the Review block does not do). Units 4-10 hit 6-7
  once retagged properly; treat 10 as never having been achievable
  cleanly.

---

## 7. Story

**Core:** one per unit, referenced only from lesson 05's `story` section,
followed immediately by the "Reading" exercise-group, as below.

**Latin America (revised 2026-08-27, see §3):** one story **per teaching
lesson** (five per unit, not one), each 400–700+ words, referenced first
in that lesson's own section list — not last, and not confined to lesson
05. File under `content/es/stories/world/b1/`, one file per lesson (e.g.
`b1-precolombina-02-civilizaciones.json` for `lesson.b1.precolombina.02`),
`type: "world"`. The length band table below and the "one per unit" framing
are Core-only; see §3 for Latin America's word count and register-escalation
rules.

- **Core** stories are adapted extracts from the real works already named
  in the Consolidated Unit List (*Don Quijote*, *The Odyssey*, etc.) — file
  under `content/es/stories/classics/b1/`, `type: "classic"`.
- **Latin America** stories are adapted historical/documentary material
  (chronicles, testimonies, speeches, reports), written specifically for
  the lesson rather than adapted from a single source document — file
  under `content/es/stories/world/b1/`, `type: "world"`.

Neither track uses `type: "original"` at B1 — `B1_GUIDE.md` §1 is explicit
that "literary, historical and world texts replace original Parlour
stories" from this level on.

Length band, escalating across the level per `B1_GUIDE.md` §13's
early/mid/late progression (this specific banding is new — no B1 target
existed before this document):

| Units | Words |
|---|---|
| 1–12 (early B1) | 150–250 |
| 13–24 (mid B1) | 200–300 |
| 25–36 (late B1) | 250–350 |

Only previously-taught grammar and vocabulary may appear in the text — same
rule as A1, unchanged at B1: a story is where the learner reads what they
already know, not a preview of what's coming.

---

## 8. What this spec deliberately does not inherit from A1

`a1-content-spec.md` describes A1 as it existed on 2026-08-09: one file per
lesson (`a1-01.json`), with lessons 18–20 as a separate "review" format.
Since then A1 itself was restructured into the six-lessons-per-unit shape
this document describes (`a1-01-01.json` … `a1-01-consolidation.json`).

`scripts/audit-lesson.py` has been rewritten (2026-08-13) to discover units
from that id shape directly rather than from a hardcoded old-format regex,
and to check each lesson against this document for B1, `a2-lesson-guide.md`
for A2, and structurally only (no plan document exists at lesson grain) for
A1. Running `python scripts/audit-lesson.py b1-{unit}` once a unit is
written is the actual gate — see the script's own docstring for exactly
what is and isn't checked per level. Two things worth knowing before relying
on it at volume:

- **Latin America units aren't cross-checked against the plan yet.** The
  Consolidated Unit List numbers Latin America units 1–36 the same as Core,
  but lesson files use word-slug ids (§1a) that the plan document has no way
  to key by. Title/word/exercise-count checks are silently skipped for
  Latin America lessons until a slug-to-unit-number mapping exists — the
  structural checks (section order, exercise-block presence, type diversity,
  word coverage, checklist form) still run and still matter.
- **The teaching-order check ("asked for before it was taught") is a coarse
  heuristic** — it stems Spanish tokens rather than parsing morphology, so
  irregular participles and gerunds (`escrito`, `visto`, `viendo`) routinely
  read as "unseen" even when the infinitive was taught, because the stem
  doesn't match. Treat its output as a worth-a-look list, not a hard
  contract, until that's tightened.

---

## 9. Known generation pitfalls

Unit 1's first draft failed `validate-content.py` on 27 of 46 files and
needed a second full fix pass after that — every item below is a bug that
actually shipped, not a hypothetical. A generator that avoids all eleven
gets much closer to a clean pass on the first try.

1. **Every lesson file needs a top-level `"level": "B1"` field.** The
   schema requires it; the first draft omitted it from all twelve lesson
   files in the unit.
2. **`recycle` is `{"type": "recycle"}`, optionally with `title`/`count` —
   never an `items` field.** Present (and wrong) in every lesson file.
3. **`srs` is `{"type": "srs"}`, optionally with `title` — never a `ref`
   field.** Present (and wrong) in every teaching lesson.
4. **Grammar files are `{"id", "title", "sections"}` only — no top-level
   `"lesson"` field.** Present (and wrong) in every grammar file, both
   tracks.
5. **`external-link` parts take `type`, `topic`, `url`, and optionally
   `site` — never `title`.** Present (and wrong) in every Core grammar
   file.
6. **`dialogue-complete`'s `options` array must contain only plain
   strings.** A `[word, translation, pos]` vocabulary triple was pasted
   into `options[0]` in five separate exercise files instead of a real
   alternative line of dialogue.
7. **`fill-blank` sentences place the blank *inside* the sentence, where
   the target word belongs — never appended after an already-complete
   sentence.** `"La cordillera atravesaba grandes territorios __.
   (cordillera)"` is nonsense; it has to be `"La __ atravesaba grandes
   territorios. (cordillera)"`. This exact pattern shipped in ten
   exercises across the Latin America track (`ex03` and `ex08` in every
   lesson).
8. **When a lesson's exercise file has a block inserted partway through**
   (Reading, only in lesson `.05`, sitting between Practice and
   Listening), **every exercise id after that block must be renumbered
   sequentially.** Reusing an earlier id (a second `ex10`/`ex11`/`ex12`
   after the real Reading block's own `ex10`–`ex12`) silently shadows the
   real exercise when the file is read as an id-keyed map — both tracks'
   lesson-`.05` files had exactly this bug, and it also produced a false
   failure on rule #10 below, since the shadowing entry happened to carry
   a `teaches` tag the real Reading exercise didn't.
9. **No exercise's full content (every field except `id`) may be
   identical to another exercise's in the same unit.** Two variants of
   this shipped: one exercise reused verbatim across all five (or all
   four) teaching lessons of a unit with only its `id` changed, and pairs
   of adjacent lessons sharing one exercise's exact sentence.
10. **Reading-block exercises carry no `teaches` tag** (§6) — but per
    pitfall #8, this can *look* satisfied while actually being violated by
    a shadowed duplicate id. Check the ids are unique before checking the
    tags.
11. **Run `python scripts/validate-content.py` and
    `python scripts/audit-lesson.py b1-{unit}` yourself and paste the
    literal terminal output alongside the files.** Every one of the ten
    pitfalls above was claimed "validated" in the first submission, and
    none of it had actually been checked.

The pitfalls below surfaced across later Core batches (Units 4-36) and
are just as real, even though `validate-content.py` stays green through
every one of them — they only show up in `audit-lesson.py` or a manual
check, so don't skip those just because the schema check passed.

12. **Every non-Reading exercise needs a `teaches` tag.** One whole batch
    (ten units) shipped with zero exercises tagged anywhere — not
    fragmented, not blanket, just absent. Tag every Practice/Listening/
    Dialogue/Writing exercise in a teaching lesson with that lesson's own
    slug; tag consolidation's exercises by cycling through the unit's
    lesson slugs plus one unit-level vocabulary slug.
13. **`teaches` slugs are per-lesson, not one blanket tag for the whole
    unit.** A blanket tag breaks Grammar Driller pooling
    (`grammar-index.json`) and fails the same "review ranges over 6+
    points" audit rule as fragmenting one grammar point into several
    near-duplicate slugs (§6) — both are wrong in opposite directions.
14. **Each `exercise-group`'s `exerciseRefs` must match the actual
    `category` of the exercises it points at.** One whole batch had every
    lesson's Listening/Dialogue/Writing groups off by one at each category
    boundary — e.g. Listening's last ref was actually a
    `dialogue-complete` exercise, Writing was missing its first item.
    `category` is schema-declared "informational; the lesson decides
    placement," so this never fails `validate-content.py` — check it by
    hand, or rebuild every group's refs directly from each exercise's own
    `category` rather than trusting the generated arrays.
15. **Lesson `.05`'s `Reading` exercise-group must actually exist and be
    non-empty.** Several batches omitted it completely, silently letting
    Listening/Dialogue/Writing absorb the freed exercise slots instead of
    flagging a missing block.
16. **Grammar/Focus screens need 3-5 worked examples (§5), not 2.** One
    whole batch shipped with exactly 2 examples in every file — it passes
    every other check and only fails this one specific audit rule, so it's
    easy to miss without actually reading the audit output line by line.
17. **(Latin America only) Every Focus screen needs exactly one
    grammar-extension point from §3's list, and it should vary across the
    unit's five lessons rather than reusing the same one five times.**
    Unit 1's first draft, and every Latin America Focus screen generated
    before the §3 rewrite, taught zero grammar at all — historical content
    only. That's the single biggest thing to get right generating Latin
    America units, since nothing in `validate-content.py` catches its
    absence.
