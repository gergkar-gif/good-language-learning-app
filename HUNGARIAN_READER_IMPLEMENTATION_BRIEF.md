# Hungarian Reader: Initial Implementation Brief

## Purpose

Extend Parlour's existing Reader/Lexicon architecture to support Hungarian.

This is an initial implementation direction, not a rigid specification. Preserve the existing architecture where sensible, but improve the design if inspection of the codebase reveals a cleaner, lighter, or more robust approach.

The main requirement is that Hungarian should receive the same Reader experience as Spanish:

- tappable words
- dictionary lookup
- inflected-form → lemma resolution
- useful grammatical/morphological information
- phrase lookup
- pronunciation where available
- familiarity colouring
- Add to SRS / Add to Deck
- lazy loading
- no unnecessary runtime dependencies

## Existing Spanish architecture to reuse

The current Spanish implementation already provides the model.

`engine/lexicon.js` loads linguistic data lazily on first word lookup. The current data layers are broadly:

1. conjugated verb form → lemma + analysis
2. inflected noun/adjective/adverb form → lemma
3. lemma → English translation
4. lemma → frequency rank

`engine/reader.js` uses this Lexicon for word popups and resolves inflected forms to canonical lemmas before vocabulary/SRS actions.

The Library specification also explicitly expects the existing Reader to support morphology-aware lookup, phrase detection, pronunciation, familiarity colouring and SRS interaction.

Do not create a separate Hungarian Reader unless the existing architecture genuinely cannot support Hungarian.

## Wider scope: the generated-index gap is not just the Lexicon

Inspection (2026-08-18) found that `engine/lexicon.js` is not a special case — it's
one instance of a pattern that runs through every module built on generated
indexes. Each of these fetches a bare top-level path instead of going through
`Lang.content()`, the same way `lessons/`, `stories/` and `curriculum/`
already do:

| File | Hardcoded path | Feature |
|---|---|---|
| `engine/lexicon.js` | `verb-index.json`, `word-index.json`, `spanish-en.json`, `frequency.json` | Reader word-tap lookup (this brief's original scope) |
| `engine/drills/grammar.js` | `generated/indexes/grammar-index.json` | Workshop Grammar Driller's skill pool |
| `engine/drills/translation.js` | `generated/indexes/translation-index.json` | Workshop Translation Driller |
| `engine/drills/listening.js` | `generated/indexes/translation-index.json` | Workshop Listening Driller |
| `engine/drills/vocabulary.js` | `generated/indexes/translation-index.json` | Workshop Vocabulary Driller (Context mode) |

All four Workshop files sit downstream of `scripts/build_grammar_index.py`
and `scripts/build_translation_index.py`, which themselves only ever scan
`content/es/`. So this is one fix, not five: make the generated-index
location itself language-scoped — most consistent with the rest of the app
would be moving them under `content/<lang>/indexes/...` (matching how
`content/hu/curriculum/` and `content/hu/decks/` already work from the
course-picker work), updating the four build scripts to write there
per-language, and swapping these fetch call sites to `Lang.content(...)`.

**Deliberately out of scope:** `engine/content-loader.js`'s `Content.verb()`
also hardcodes `imports/verbs/`, but that's an existing, documented
exception — Hungarian's definite/indefinite verb conjugation has no Spanish
analogue, so `engine/verbs/` needs an actual rewrite regardless of any data
scoping (see multi-language-plan). Don't fold it into this pass.

This means Phase 3 ("integrate with existing Lexicon... make the Lexicon
language-aware without duplicating the Reader") should really be scoped as
*make every generated-index consumer language-aware*, not just the Lexicon —
otherwise Hungarian gets a working Reader but a Workshop that's silently
still serving Spanish content, or serving nothing, under every driller.

## Hungarian requirement

Hungarian needs richer morphology than Spanish.

A learner may encounter forms such as:

- `házban`
- `házamban`
- `barátaimmal`
- `hotelhez`
- `olvastam`

The Reader should ideally recognise the surface form and resolve it to a useful lexical entry rather than treating the form as an unknown word.

For example, a future popup might represent:

`házamban`

- lemma: `ház`
- meaning: `house`
- morphology: possessive 1sg + inessive

Or:

`olvastam`

- lemma: `olvas`
- meaning: `read`
- morphology: past, indicative, 1st person singular

The exact presentation is for the implementer to determine. The important point is that the system should expose morphology in a way useful to a learner, rather than merely returning a technical parser dump.

## Lightweight runtime principle

Do NOT put a full Hungarian NLP stack into the browser.

In particular, do not assume that Parlour should ship:

- Python
- HuSpaCy
- emMorph
- large NLP models
- a permanent morphology API
- embeddings
- an LLM
- a full syntactic parser
- a large corpus

These may be useful during development/content generation, but they should not become runtime requirements unless there is a compelling reason.

The preferred model is:

    heavy linguistic tooling
            ↓
       build/preprocessing
            ↓
    compact Parlour indexes
            ↓
       browser Reader

The learner should receive the processed data, not the machinery used to generate it.

## Candidate Hungarian linguistic resources

The following resources were identified during research and should be evaluated rather than blindly integrated.

### emMorph / emMorphPy

GitHub:
https://github.com/nytud/emmorphpy

Potential use:

- generate or validate Hungarian morphological analyses
- lemma resolution
- detailed grammatical features
- preprocessing source data for Parlour indexes

emMorphPy is Python-based and therefore is more appropriate as a build/content-processing dependency than as a browser dependency.

Check the licences of emMorphPy and its underlying linguistic resources individually before redistributing derived data.

### Magyar Ispell / Hunspell

Potential use:

- stemming
- morphological analysis
- Hungarian lexical coverage
- potentially generating/validating inflected forms

Possible GitHub sources include:

https://github.com/laszlonemeth/magyarispell
https://github.com/hunspell/hunspell

Do not add Hunspell WASM to the app automatically. First determine whether generated static indexes are sufficient. A runtime WASM dependency should only be introduced if it provides a clear benefit that cannot be achieved more simply.

### HuSpaCy

GitHub:
https://github.com/huspacy/huspacy

Potential use:

- tokenisation
- lemmatisation
- POS tagging
- morphology
- preprocessing and validation of curated texts

Again, this should normally be a content/build-time tool rather than a browser dependency.

### Hungarian frequency data

A Hungarian Webcorpus-derived frequency dataset was identified here:

https://github.com/petyaracz/hungarian-word-frequencies

Potential use:

- lemma frequency
- vocabulary familiarity/coverage calculations
- ranking ambiguous readings
- future reading difficulty estimation

Do not import an unnecessarily large corpus into the browser. Extract the compact frequency information Parlour actually needs.

## Proposed initial data model

The exact filenames and schema are deliberately open to improvement.

A starting point would be language-specific generated indexes such as:

    generated/indexes/
        hu-word-index.json
        hu-verb-index.json
        hu-frequency.json

and a Hungarian dictionary/lexicon source containing:

    lemma
    English translation
    part of speech
    optional gender/other lexical information where relevant
    optional phrase information

The important distinction is:

### Surface-form indexes

These answer:

> What is this word form?

For example:

    hotelhez → hotel
    házamban → ház
    olvastam → olvas

### Dictionary

This answers:

> What does the lemma mean?

For example:

    hotel → hotel
    ház → house
    olvas → read

### Morphological analysis

This answers:

> What grammatical information explains this particular form?

For example:

    házamban
    → possessive 1sg + inessive

The implementation may combine these into fewer files if that is smaller or cleaner. The four-layer separation is a starting model based on the existing Spanish Lexicon, not a requirement.

## Important: do not generate every possible Hungarian form blindly

Hungarian morphology is highly productive. A naïve exhaustive form dictionary could become unnecessarily large.

Investigate whether the best approach is:

1. compact generated form indexes for common/attested forms;
2. compact morphological rules;
3. a hybrid;
4. or another approach discovered during implementation.

The target is good Reader behaviour with a small memory/download footprint, not linguistic completeness at any cost.

**Coverage cannot be scoped to the curriculum's own vocabulary.** Library's
My Texts feature (see [[parlour-library-my-texts-feature]]) lets a learner
paste and read *any* text — not just Parlour's own stories — and it runs
through this same Reader. A Hungarian lexicon sized only to the ~30-lesson
A1 word list would work for lesson content and then return "not in the
dictionary yet" for most of whatever a learner actually pastes in, which
defeats the point of My Texts existing at all. The dictionary/lemma layer
in particular needs essentially full coverage (the same shape as
`imports/dictionary/spanish-en.json`'s ~110k Spanish entries, not a few
hundred). Where the curriculum *can* legitimately constrain scope is the
morphological *depth* surfaced by default early on (which cases/tenses get
a friendly label vs. a raw tag) — not which words are recognised at all.

## Reader behaviour

The existing Reader should remain the main UI.

When a learner taps a Hungarian word:

1. normalise the surface form;
2. look it up in the Hungarian Lexicon;
3. resolve possible lemmas/readings;
4. show the most useful reading first;
5. show alternatives where ambiguity is real;
6. expose useful morphology;
7. provide the English meaning;
8. resolve the canonical lemma for SRS/Deck operations.

For example:

    barátaimmal

should ideally not become a new SRS item simply because the learner tapped that exact surface form.

The canonical lexical item should normally be the lemma:

    barát

The precise policy for what is stored in SRS should follow the existing Spanish implementation unless Hungarian-specific requirements justify a change.

## Ambiguity

Do not silently discard legitimate analyses.

If a Hungarian surface form can have multiple plausible analyses, the Lexicon should be capable of returning multiple readings, as the Spanish implementation already does for ambiguous forms.

However, the UI should prioritise the most likely/useful reading rather than dumping every technical analysis on the learner.

Frequency, lexical information, context and curriculum knowledge may be useful for ranking. The implementer can determine the simplest reliable method.

## Phrase detection

Reuse the existing phrase-detection mechanism.

Hungarian will eventually need multi-word expressions too. Do not replace the existing Reader with a Hungarian-specific phrase system unless necessary.

## Familiarity and SRS

Reuse existing Reader/SRS behaviour.

The Reader should continue to distinguish:

- unknown
- seen
- known
- mastered

or whatever the current implementation uses.

Tapping an inflected Hungarian form should resolve to the canonical lexical item where possible.

`Add to Deck` should likewise use the resolved lexical item.

Do not automatically create SRS cards for every unknown form.

## Lazy loading

Follow the existing Spanish pattern.

Hungarian linguistic indexes should not block application startup.

Ideally:

    app startup
        ↓
    no Hungarian lexicon loaded

    first Hungarian word tap
        ↓
    load required Hungarian indexes
        ↓
    cache in memory
        ↓
    subsequent lookups are local

If the implementer finds a substantially smaller or more efficient loading strategy, use it.

## Build pipeline

A likely workflow is:

    Hungarian linguistic resources
             ↓
    build/preprocessing script
             ↓
    compact JSON indexes
             ↓
    content/hu or generated Hungarian assets
             ↓
    existing Lexicon/Reader

The build process should be deterministic and repeatable.

It should ideally make it possible to regenerate the Hungarian indexes when:

- the dictionary changes
- the curriculum expands
- morphology coverage improves
- translations are corrected
- frequency data is updated

Do not require the browser to perform linguistic preprocessing.

## Validation

Before considering the first implementation complete, create a small Hungarian test set containing at least:

### Simple lemmas

- ház
- hotel
- barát
- olvas

### Case forms

Include examples using several cases, such as:

- `házban`
- `hotelhez`
- other forms appropriate to the available A1 material

### Possessive forms

Include examples such as:

- `házam`
- `házamban`
- `barátaim`

### Verb forms

Include examples such as:

- `olvasok`
- `olvasol`
- `olvastam`

### Ambiguous or potentially difficult forms

Include forms where the underlying resource reports more than one analysis.

For every test form, verify:

- surface form is recognised;
- lemma is correct;
- POS is sensible;
- morphology is sensible;
- English meaning is available where expected;
- SRS/Deck uses the canonical lexical item;
- unknown forms fail gracefully.

## Do not over-engineer the first version

The first goal is not a complete Hungarian morphological engine.

The first goal is:

> Make the existing Parlour Reader work properly for Hungarian using the smallest practical amount of runtime data.

Start by inspecting the current Spanish implementation and the build pipeline. Then prototype the Hungarian data generation against a small test set.

If one resource produces sufficiently good static indexes, prefer that over combining several systems.

If a hybrid approach is materially better, use it.

If the proposed JSON structure can be reduced without losing functionality, reduce it.

If an existing Parlour abstraction can be extended cleanly instead of creating Hungarian-specific code, extend it.

## Suggested implementation sequence

### Phase 1: inspect and prototype

- inspect `engine/lexicon.js`
- inspect Reader integration
- inspect current Spanish generated indexes
- inspect build scripts
- inspect how language-specific content paths are resolved
- test candidate Hungarian resources against a small form set

### Phase 2: generate minimal Hungarian indexes

Produce the smallest useful dataset that supports:

- lemma lookup
- translation
- basic POS
- common inflected forms
- useful morphology
- frequency ranking if practical

### Phase 3: integrate with existing Lexicon

Make the Lexicon language-aware without duplicating the Reader.

### Phase 4: test in the actual Reader

Test:

- word popup
- lemma resolution
- ambiguous forms
- phrase lookup
- pronunciation
- familiarity
- Add to SRS
- Add to Deck
- lazy loading
- course switching between Spanish and Hungarian

### Phase 5: measure

Check:

- generated file sizes
- network transfer on first lookup
- memory usage after loading
- lookup speed
- coverage on the Hungarian test set

Only then decide whether additional machinery such as runtime Hunspell/WASM is justified.

## Success criterion

A learner reading a Hungarian text should be able to tap a form such as:

    házamban

and get a useful explanation connected to:

    ház = house

rather than:

    "Not in the dictionary yet."

At the same time, adding Hungarian support should not turn Parlour into a heavy NLP application.

The preferred outcome is a **small, static, language-specific linguistic data layer sitting behind the existing Reader architecture**.

The above is an initial direction. The implementer should inspect the repository, test the resources, measure the resulting data, and change the design where doing so produces a simpler or better result.
