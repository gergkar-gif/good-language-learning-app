# HU B1 citizenship batch 08-14: reviewer's notes (Claude, 2026-10-28)

Units 8 `saint-stephen`, 10 `arpad-dynasty` (reader A), 12 `mongol-invasion`, 14 `angevin-kings` (reader B).
Both readers stopped at the 5-hour Sonnet limit before writing a file and were resumed after the reset.

## Counts

| Unit | proposed | auto | review | rejected | Claude changed / added |
|---|---|---|---|---|---|
| 8 saint-stephen | 101 | 20 | 80 | 1 | 1 changed (Aug 20 term), 1 dropped (consolidation title), 1 rewritten, 3 added |
| 10 arpad-dynasty | 87 | 10 | 73 | 4 | 1 rewritten, 3 checklist lines by hand, 2 Croatia/heir fixes, 3 *amely* recaps, 1 length fix |
| 12 mongol-invasion | 72 | 13 | 58 | 1 | 2 changed ("second founder"), 1 rewritten (`answers`), 2 challenges |
| 14 angevin-kings | 77 | 14 | 62 | 1 | 1 rewritten (JSON quote), 2 added (*-ható*, verbal noun), 1 challenge |

Merged and applied: 335. Then 10 item fixes (`extra2-4.json`), 77 vocabulary entries
(`unmet-added.txt` → `vocab-added*.json`), 2 lesson-file lines (arpadhaz-03 grammar title and
goal line 5, edited directly: the line occurs three times in the file), 24 challenges
(4 edited before adding), 52 dictionary glosses (`dictionary.txt`, `dictionary-2.txt`).

Reader tokens (from the resumed runs' notices only): A 306,602, B 344,038.

## Changes to the readers' fixes

- Unit 8, segment 04: Aug 20 is *Magyarország hivatalos állami ünnepe* (Alaptörvény J cikk),
  not *nemzeti ünnepe*.
- Unit 8 / Unit 10 consolidation titles ("Unit 4 / Unit 5 Consolidation"): kept. Citizenship
  consolidations are numbered within the track (Unit 8 is the track's 4th unit), as in every
  other citizenship unit.
- Unit 12, segment 04 and its question: "a történészek ... második honalapítónak nevezik" →
  "gyakran második honalapítónak nevezik" (a popular label, not a historians' verdict).
- Rejected and rewritten: two consolidation items repeating the question "Melyik mondat
  helyes?" of the item before (question made specific); `answers` beside `answer` on
  tatarjaras-consolidation.ex12 (`answer` removed); unescaped quotes on b1-anjouk-03-gr; three
  arpadhaz-03 checklist fixes whose old text didn't match.
- Unit 10, consolidation ex14: "László ... Horvátországot Magyarországhoz csatolta" → "1091-ben
  elfoglalta Horvátország nagy részét" (Kálmán was crowned king of Croatia in 1102); "örökös
  nélkül" → "fiú nélkül" (András III had a daughter).
- *amely* recaps: reader A wrote "you know *amely* from A2 Unit 4" on arpadhaz-01, -02 and -03,
  but *amely* is taught on b1-arpadhaz-02 (the close-out found the same on six core screens);
  arpadhaz-01's original "you'll meet this next lesson" was right and is restored in substance.
  Unit 8's screen example used *amely* before Unit 10: now *ami*.
- Forms before their unit, found by `unmet-words.js` after applying: *megnyitás* (verbal noun)
  in istvankiraly-03.ex05, *honfoglaló* (present participle, Unit 11) in the Unit 8
  consolidation, *adható* (Unit 61) in anjouk-03.ex06, *megerősítését* in the anjouk
  consolidation ex14 question (rewritten with *erősítették meg*).
- Challenges: tatarjaras-04 and anjouk-04 targets now do what their `canDo` says (why the
  Mongols left, hedged; Sigismund as king and emperor); "IV. Béla" in the consolidation target
  written as "Béla király" (the sentence counter reads "IV." as a sentence end).

## Facts checked on the web (the readers' "check" lines)

Wikipedia is not reachable from this container (`en.wikipedia.org` is outside the network
policy); Perplexity and Firecrawl failed. Checked with web search results instead.

- Golden Bull: issued by Andrew II in spring 1222 at the Székesfehérvár assembly; the barons
  forced him; right of resistance (jus resistendi). Kept, with Zsoldos's caveat that place, date
  and circumstances are debated (not added to the text). Sources:
  https://www.britannica.com/print/article/237527, https://discovery-pp.ucl.ac.uk/id/eprint/1457439/6/II.087-108.pdf,
  https://eshop.posta.hu/storefront/en/stamps/fdc/the-golden-bull-is-800-years-old-fdc/prod2022210060012.html,
  https://real.mtak.hu/162885
- Coronation: 25 December 1000 or 1 January 1001, crown from Sylvester II by tradition; place
  not stated by the sources found, so "a hagyomány szerint Esztergomban" stays hedged.
  https://newworldencyclopedia.org/entry/Stephen_I_of_Hungary
- Ten dioceses: two archbishoprics (Esztergom, Kalocsa) and eight bishoprics (Veszprém, Pécs,
  Győr, Eger, Vác, Csanád, Bihar, Erdély). https://real-eod.mtak.hu/5154/1/000901313.pdf,
  https://tortenelem.fazekas.hu/erettsegi/tomor/11_magyar_allamalapitas.pdf
- Kálmán's decree "De strigis vero quae non sunt, nulla amplius quaestio fiat": no
  investigations or trials about *strigae*, "which do not exist"; the segment's wording matches.
  https://en.wikipedia.org/wiki/Witch_trials_in_Hungary (search excerpt),
  https://journals.lib.pte.hu/index.php/speciminanova/article/download/6798/6409/12311
- Croatia: Ladislaus I king of Croatia from 1091; Coloman crowned at Biograd 1102 (fix above).
  https://en.wikipedia.org/wiki/Croatia_in_personal_union_with_Hungary (search excerpt)
- Imre died 2 September 1031, killed by a boar while hunting (Altaich annals: 1033): "a
  hagyomány szerint vadászat közben" kept. Andrew III's mother Tomasina Morosini was Venetian.
  Géza kept worshipping pagan gods ("a régi hitet sem hagyta el teljesen" kept).
  https://en.wikipedia.org/wiki/Andrew_III_of_Hungary (search excerpt),
  https://www.constantinesletters.ukf.sk/images/issues/2025_v18_iss2/CL_v18_iss2_057to067.pdf
- Not searched, standard facts I am sure of: Géza died 997; István died 15 August 1038;
  canonised 1083 with Imre and Gellért, László 1192; Orseolo Péter and Aba Sámuel 1038–1046;
  Muhi 11 April 1241, Mongols withdraw 1242, Ögödei's death as the usual (disputed) reason;
  second Mongol invasion 1285 repelled; Pannonhalma founded 996; the Holy Crown returned by the
  US in 1978 and in Parliament since 2000; Árpád dynasty extinct 14 January 1301; gold florin
  1325, Körmöcbánya mint 1328; Visegrád congress 1335 (Hungary, Bohemia, Poland); V4 founded at
  Visegrád 1991; *ősiség* 1351; Order of the Dragon 1408; Council of Constance 1414–1418;
  Sigismund crowned emperor 1433; Hunyadi governor 1446–1453; Belgrade 1456 (river blockade
  broken 14 July, assault repelled 21–22 July, Hunyadi died of plague in August); Calixtus III's
  noon-bell bull preceded the victory; Belgrade fell 1521 (65 years).

**Disputed, for the user:** none needed a decision. The coronation date and place, the
Intelmek's authorship, the Mongols' reason for leaving and the noon bell's link to Belgrade are
each named as disputed or as tradition in one line.

## After applying

- `unmet-words.js`: 85 hits; 77 words added to the first lesson's list (`unmet-added.txt`), 4
  forms before their unit rewritten, the rest lookup misses (split verbs *küldi szét*,
  *telepedtek le*, *fogadták el*; comparatives *közelebb*, *legbátrabb*; names; *1335-ös*).
- `check_unit_refs.py`: its unit filter skipped every citizenship screen (topic suffix in the
  file name); fixed, and it found the two *amely* recaps above. Units 2, 4, 6 rechecked: clean.
- `check-content`: 0 errors on all four units; 10 `vocab-unused` suspects accepted at freeze
  (`accept.json`).
- `validate-content --changed` passes; `--warnings` identical to the baseline.
- Walk 24/24 with challenges.
