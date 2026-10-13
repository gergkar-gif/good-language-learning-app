# hu a1 `plurals-quantities`: second fix list (2026-10-13)

After the pilot fix list (883cafc1). Second blind Sonnet read (161k, 5 min)
filtered by Claude against the files.

## Applied (apply every item)

1. **Remove `distractor_skills` index `"0"`** (ungrammatical *a nagyok
   asztalok*-type options; the pilot fix list was wrong to add them) in
   `a1-38-introduce-2`, `a1-38-controlled-4`, `a1-38-check-2`,
   `a1-39-practice-1`, `a1-40-consolidation-13`, `a1-38-dialogue-1`. Keep
   index `"1"` where its option is well-formed (*az asztalok nagyok*);
   drop the whole field where nothing remains.
2. `a1-37-a-gr`: replace the ö/ü passage that calls *könyv* an exception
   with: "Words whose vowels are *ö* or *ü* take *-ök* or *-ek*: learn each
   as you meet it (*sör → sörök*, *könyv → könyvek*)." Keep *könyvök* out
   of every option.
3. `a1-39-a-gr`: add one sentence: "*régi* is an exception to 'after a
   vowel just add *-k*': it takes *-ek*: *régiek*."
4. `a1-36-a-gr` first text: lead with *asztal → asztalok*, *szék → székek*
   instead of *könyv → könyvek* (könyv's linking vowel is explained in
   a1-37).
5. *is* ("too") is not taught before a1-80: `a1-36-a-gr` example *Az
   asztalok is itt vannak.* → *Az asztalok itt vannak.* (English "The tables
   are here."); story `a1-unit-08` *Az asztalok is itt vannak.* → *Az
   asztalok ott vannak.*, *A család is itt van.* → *A család itt van.*
   (adjust their English lines if they say "too"). Re-render a1-36 and
   check the speaking step built from the example.
6. *kell* glossed "is needed / must" (`a1-40-voc`, `a1-40-a-gr`) → "is
   needed".
7. `a1-38-dialogue-1`: Meg's question → *A kicsi székek itt vannak?* so the
   right reply *Nem, a kicsi székek ott vannak.* answers it.
8. Story `a1-unit-08`: narration "Meg counts the chairs" → "Meg looks at the
   chairs"; `a1-40-reading-1`: drop "only" from "only a few".

## Not taken

- `egyutt-together` on *vannak* items: *vannak* is taught on that skill's
  screen (a1-30-b-gr); keep.
- Adjective fill-blanks tagged `adjective-order-before-the-noun`: the
  learner can type *nagyok*, so a wrong answer shows the form; keep.
- *Négy székek vannak* as two faults: one agreement idea; keep.
- *kicsiek* in `answers`: the screen teaches *kicsik*; keep.
- Builder alternative orders (parked); near-duplicate items; two-option
  items; a1-37-b tip wording; a1-36-a table "a könyv van".
