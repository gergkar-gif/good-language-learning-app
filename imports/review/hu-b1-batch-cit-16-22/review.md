# HU B1 citizenship batch 16-22: reviewer's notes (Claude, 2026-10-28)

Units 16 `matthias-corvinus`, 18 `mohacs-1526` (reader A), 20 `three-part-hungary`,
22 `transylvania-golden-age` (reader B). No usage limit hit.

## Counts

| Unit | proposed | auto | review | rejected | Claude changed / added |
|---|---|---|---|---|---|
| 16 matthias-corvinus | 98 | 33 | 65 | 0 | 5 changed (tax reform, hedges removed), 2 added (age), 4 length fixes |
| 18 mohacs-1526 | 102 | 38 | 62 | 2 (restored: false rejections) | 1 added (place of Louis II's death disputed), 1 recap |
| 20 three-part-hungary | 160 | 62 | 97 | 1 (rewritten) | 3 changed (Pozsony from 1536, two metalanguage stems), 2 added (szokás volt item, 04.ex04 stem) |
| 22 transylvania-golden-age | 174 | 73 | 100 | 1 (rewritten) | 2 changed (a verbal-noun option, a metalanguage stem), 1 recap |

Merged and applied: 537; then 9 more item and screen fixes (`extra2-4.json`), 96 vocabulary
entries (`unmet-added.txt`), 24 challenges (2 edited), 74 dictionary glosses.

Reader tokens: A 380,427 (47 tool calls, 25 min), B 438,979 (58, 31 min): ~190k and ~220k a unit.

## Changes to the readers' fixes

- Unit 16: Matthias's tax. Reader A hedged the *füstadó* as unconfirmed; Hungarian sources
  confirm the 1467 reform: the *kapuadó* (lucrum camerae) replaced by the royal treasury tax,
  levied per household ("per smoke", *füstpénz*). The segment now says so, and the three items
  and the screen lose "egyes források szerint".
- Unit 16: Matthias was elected at 14 (born 23 Feb 1443, elected 24 Jan 1458), not "alig
  tizenöt"; segment 01, ex08 and the challenge now say *tizennégy*.
- Unit 18: one line added to segment 04 naming the dispute over where Louis II drowned (Csele
  brook in the tradition; a Danube side branch according to Pap Norbert and colleagues, 2019).
- Unit 18: two lesson `grammar` field fixes were rejected only because a `vocab-unused` finding
  carries the lesson id; restored (`restored-mohacs-1526.json`).
- Unit 20: "Miután Buda török kézre került, Pozsony lett ... fővárosa" → Pozsony was the diets'
  seat from 1536, the capital after 1541, the coronation city 1563–1830.
- Hungarian grammar terms in question stems (*megengedő kötőszó*, *névutó*, *ige*, *múltbeli
  szokásos cselekvés*) replaced by "Melyik szó illik a mondatba" or an English meaning line
  (04.ex04: *kötelező* and *tilos* were grammatical too, with nothing to pin the meaning).
- Unit 22, 04.ex06: wrong option *Kimondták Erdély egyesítését* (verbal noun) → *Erdélyt a
  Hódoltsághoz csatolták.*
- Recaps found by `check_unit_refs.py`: *révén* "from A2 Unit 18" and *amint* "from B1 Unit 1"
  copy skill titles whose screens never show the word (first taught in B1 Units 28 and 24), so
  both are now presented as new and listed. *leg-* "from A2 Unit 16" is the known false positive.
- `historical-routines` fell to 5 exercises after reader B rightly retagged an adverb item; the
  consolidation's *másfél* blank became a *szokás volt* item (6 again).

## Facts checked on the web

Wikipedia is outside this container's network policy; web search results instead.

- Matthias's tax reform, 1467: https://openaccess.ludovika.hu/nke/catalog/download/327/3114/7230?inline=1,
  https://epa.oszk.hu/03100/03122/00010/pdf/EPA03122_rubicon_2016-4_058-059.pdf,
  https://eduline.hu/erettsegi-felveteli/tortenelem_erettsegi_2014_masodik_resz_mego_W8BK7E
- The Corvina library: about 216 surviving corvinas; the original estimated at 2,000–3,000
  volumes ("becslések szerint több ezer" kept): https://oszk.hu/node/1844,
  https://crln.acrl.org/index.php/crlnews/article/view/20023/23952
- Louis II: body found in the third week of October near the Csele's mouth, buried at
  Székesfehérvár; the identification and the place of death are disputed:
  https://hvg.hu/kultura/20150901_Hogyan_halt_meg_Mohacs_mezejen_Lajos_kira,
  https://444.hu/2019/08/28/a-kutatok-szerint-biztos-hogy-ii-lajos-kiraly-nem-a-csele-patakba-fulladt
- Not searched, standard facts I am sure of: Matthias crowned 1464 at Székesfehérvár, took
  Vienna 1485, died there 1490; Beatrix of Naples (Aragon line); Kinizsi; the Black Army
  disbanded in the 1490s; Dózsa 1514; Suleiman sultan 1520, Belgrade 1521; Mohács 29 Aug 1526,
  ~25,000 against at least ~50–60,000; Tomori fell; two kings elected in 1526; Buda taken by a
  ruse on 29 Aug 1541; the principality from 1570 (Speyer); Torda January 1568, the four
  received religions later; Dávid Ferenc died in Déva castle 1579; Bethlen 1613–1629, college
  1622, elected king at Besztercebánya 1620, Nikolsburg 31 Dec 1621, seven counties for life;
  Vizsoly Bible 1590; Szenczi Molnár's psalms, Herborn 1607; Buda retaken 1686; Karlowitz 1699
  with the Temesköz excepted; Debrecen "kálvinista Róma".

**Disputed, for the user:** none needed a decision. Named in one line: the place of Louis II's
death, Hungary as "first outside Italy" for the Renaissance, the Torda law as one of the first
European laws of religious tolerance, why Bethlen was not crowned.

## After applying

- `unmet-words.js`: 96 words listed on their first lessons (`unmet-added.txt`); the remaining
  hits are names and forms the lookup can't reduce (*álló*, *gyűlő*, *követheti*, split verbs).
- `check_unit_refs.py`: 2 wrong recaps fixed (above), 1 known false positive.
- `check-content`: 0 errors; 17 `vocab-unused` suspects accepted at freeze (`accept.json`).
- `validate-content --changed` passes; `--warnings` identical to the baseline after the
  `historical-routines` item.
- Walk 24/24 with challenges.
- New `scripts/add_vocab_words.py` (the list → fixes step, refusing a pos the schema rejects
  and a multi-word lemma not tagged `expression`); three of my multi-word entries retagged.
