# Report, hu b1 Unit 52 kadar-era

Commands run: check-content (12 length-giveaway ERRORs, 6 vocab-unused suspects), render_lesson, audit-reader-coverage (6 stems), unmet-words (about 190 hits; most were fragments of glued blanks and are gone once the blanks are whole words). All fixes are in `fixes-kadar-era.json` (123 fixes); challenges in `challenges-kadar-era.json` (6); facts in `facts-kadar-era.md`.

## 1. Found by reading
Stories (fixes on the segment files only; the story files have no `questions`, the lessons' reading items are the ex04/ex06 style items):
- 01 para 1 "1961-ben ... a pártkongresszuson": the slogan was proclaimed at the Hazafias Népfront congress (Dec 1961), not a party congress. Fixed (check).
- 01: items ask for pufajkások, megtorló perek, the reprisals, but the story never mentions them. Added one hedged paragraph: reprisal trials, about 230 executed (estimate), Nagy Imre 1958, pufajkások took part (check).
- 01 "Kádár amnesztiarendeletet hozott": a decree of the Presidential Council. Fixed to "hoztak" (check).
- 01 last para "elfogadta a láthatatlan alkut" states a contested interpretation as fact. Now "Sok történész 'kádári alkunak' nevezi ... Mások szerint ez a kép túlságosan leegyszerűsített".
- 01 summary: "brutal bloodbath", "cynical compromise", "Kádár realized" (mind-reading). Rewritten.
- 02 "egyedülálló módon" (unique in the bloc) is too strong; "A reform legéletképesebb eleme a háztáji gazdaságok támogatása" is unsupported (household plots predate 1968); "a szomszédos országok üres boltjaival szemben" is false (Austria, Yugoslavia); "telivé" is odd. Fixed.
- 03 "irigyelt szigetévé", "bőséges élelmiszerellátást" overstated; "minden nyáron" overgeneralised; last sentence "elfedte ... a szabadság hiányát" is a judgement and "határok zártsága" is too strong for the 1970s. Fixed. Added the "legvidámabb barakk" nickname, which ex01/ex02 ask about but the story never gave.
- 04 "rafinált", "ügyesen sakkoztak", "bátor demokratikus ellenzék" (judgements); the Beszélő began in 1981, not the late 1970s (English summary says the same); "börtön vár ránk" overstated; "megtörve" is a -ve participle. Fixed.
- 05 "a fájdalmas valóság", "nem a gazdaság teljesítménye, hanem ... hitelek" is a disputed economic claim as fact (now "sok közgazdász szerint ... részben"). MNB president: "meghaladta a húszmilliárd dollárt" in 1982 is wrong (about 9 billion gross then; near 20 billion only at the end of the decade) (check). "a boltokban megjelent az infláció" odd. The 1988 Kádár monologue is an invented quotation with mind-reading: replaced by a delegate's line (characters list changed too). "megfáradt", "feltartóztathatatlanul" (-hatatlan, Unit 59) removed; added that Kádár became party chairman. Added 1982 IMF entry (ex03 asks for it).
- Grammar screens (all five) taught known forms as new or invented rules: 01 "negative existential predicates allow pragmatism" (false rule; aki is A2 Unit 4), 02 -hat/-het (A2 Unit 23), 03 comparatives and superlatives (A2 Units 13, 16; "kapható" is a -ható word), 04 past participles (B1 Unit 3) with a false "verbal aspect" claim and "elrejtve" (-va/-ve, Unit 57) in an example, 05 "révén" as a cause word (B1 Unit 28 teaches it as means), "fenntarthatatlan" (-hatatlan) in an example, and "forced to replace the aged Kádár" as a causal judgement. All rewritten as recaps with the unit numbers from the sheet.
- Items (all fill-blanks glued a suffix to a stem, rulebook § 2.5): L1 ex02, ex05, ex07; L2 ex02, ex05, ex07; L3 ex02, ex05, ex07; L4 ex02, ex05, ex07; L5 ex02, ex05, ex07; consolidation ex02, ex05, ex07. Rewritten as whole-word blanks. Also: L1 ex05 said the pufajkások carried out the whole reprisal (overstated); L2 ex02 said the reform made household farming possible (it predates 1968); L2 ex06 asks "why the háztáji was successful" (not in story); L3 ex07 compares with Bucharest (not in story); L4 ex06 asks about Szabad Európa Rádió (not in story); L5 ex01 "katasztrofálisan ... mesterségesen" (judgement), L5 ex08 "végérvényesen kifulladt"; consolidation ex04 asks which view "modern historiography" takes (a political judgement, the wrong options absurd).
- All eight builders per lesson have `english: "Build the sentence in the correct order."`; they now carry the real translation. L2 ex08 "megtöltötték a magyar boltok polcait" and L3 ex08 "minden család számára elérhető" overstated; changed.
- ex05 L2 original used preverb inversion (*dolgozták ki* after a focus), a B2 form: now "kidolgozták".
- Length give-aways (all 12 check-content ERRORs): L1 ex01, ex06; L2 ex01, ex04, ex06; L3 ex01; L4 ex04, ex06; L5 ex01, ex04; consolidation ex01, ex08. Fixed (shorter right answers, plausible wrong ones). L3 ex01 was reported 102 vs 57 on the lesson file I read; the fix covers it.
- Absurd wrong options (circus venues, coronation of Kádár, Soviet space programme, pyramid of "aranyhíd", 2004) replaced by plausible ones with one fault.

## 2. Metadata
- L1 ex05 (pufajkások) now `category: vocabulary`, `teaches: [b1-kadar-era-vocab]` (a word, not the plural form). L2 ex02 retagged `past-tense-indefinite`, L2 ex07 `potential-hat-het`, L3 ex02 `valik-verb`.
- vocab-unused: L1 "megtorló perek" now in ex05; L3 "Trabant gépkocsi" renamed "Trabant"; L5 "hitelfelvétel" used in ex02, "IMF-csatlakozás" renamed "Nemzetközi Valutaalap", "életszínvonal stagnálása" renamed "életszínvonal", "Kádár János leváltása" used in ex04, "gazdasági kifulladás" (loaded gloss "systemic bankruptcy") renamed "gazdasági nehézség".
- Unmet words added to the vocabulary file of the first lesson that uses them (12 + 13 + 10 + 16 + 7 entries). I could not run unmet-words on the fixed text, so entries were chosen from the original hits that remain plus new words I wrote; a few may be duplicates of earlier lists (parked) or miss a word.

## 3. Goals / checklists
- All five lessons' goal lines were the same template ("I can understand and discuss <title> ...", "I can master six target vocabulary items"), lines 2-4 identical across lessons, promising what is not practised. Rewritten lesson-specific; first line is the challenge's canDo.
- No lesson has a `checklist` section (the earlier citizenship units do) and the consolidation has no goal either: added a checklist copying the goals to each lesson and a goal + checklist to the consolidation (unsure: a structural addition).

## 4. Doubtful
- 01 Kádár dialogue, 04 Aczél dialogue: invented speeches of real people (kept; "in the spirit of"); the Nyers line about shoe prices (02) likewise (unsure).
- 03 "gulyáskommunizmus" origin (Khrushchev?) left unstated; "legnyitottabb" (one of the most open countries) is my wording (unsure).
- 05 debt figures (about 9 billion in 1982, nearly 20 billion by 1989) need a reference.
- The story's dialogue "speaker" for L5 is now "Pártküldött"; the combined story is rebuilt by the reviewer.
- Recap numbers used: A2 Unit 4 (aki), A2 Unit 23 (-hat/-het), A2 Units 13 and 16, B1 Units 3, 4, 5, 9, 31 (all named in the sheet); révén/amint avoided.

## 5. Dictionary
amnesztiarendeletet | amnesztiarendelet | noun | decree granting an amnesty |
kérdőjelezze | kérdőjelez | verb | to question, to put a question mark over |
pártkongresszuson | pártkongresszus | noun | party congress |
legéletképesebb | életképes | adjective | viable, able to survive |
maszek | maszek | noun | private-sector worker or craftsman (socialist-era informal word) |
tervutasításos | tervutasításos | adjective | based on binding plan directives (centrally planned) |
frizsiderszocializmus | frizsiderszocializmus | noun | "refrigerator socialism": a life centred on household goods |
nyugatnémet | nyugatnémet | adjective | West German |
bográcsgulyást | bográcsgulyás | noun | goulash cooked in a cauldron |
élelmiszerellátást | élelmiszerellátás | noun | food supply |
közszolgáltatásokat | közszolgáltatás | noun | public service |
allegóriákba | allegória | noun | allegory |
sokszorosítógépen | sokszorosítógép | noun | duplicating machine |
szervezkedik | szervezkedik | verb | to conspire, to organise (against the authorities) |
húszmilliárd | húszmilliárd | numeral | twenty billion |
dollárhitelek | dollárhitel | noun | loan in dollars |
fizetésképtelenné | fizetésképtelen | adjective | insolvent, unable to pay |
körülöttünk | körül | postposition | around |

Fix count Unit 52: 123 (28 on stories, 38 on goals/checklists/grammar, 48 on exercises, 9 on vocabulary files).
