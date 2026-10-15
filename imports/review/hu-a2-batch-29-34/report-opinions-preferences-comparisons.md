# Reader report: hu a2 units 29, 30, 31

Units: `opinions-preferences-comparisons` (a2-141..145, a2-145-consolidation, story a2-unit-29), `review-work-past-opinions` (a2-146..150, a2-150-consolidation, story a2-unit-30), `problems-requests` (a2-151..155, a2-155-consolidation, story a2-unit-31).

Files written (nothing else touched):
- `/home/user/parlour-read-a/fixes-opinions-preferences-comparisons.json` (21 fixes), `/home/user/parlour-read-a/challenges-opinions-preferences-comparisons.json` (6)
- `/home/user/parlour-read-a/fixes-review-work-past-opinions.json` (24 fixes), `/home/user/parlour-read-a/challenges-review-work-past-opinions.json` (6)
- `/home/user/parlour-read-a/fixes-problems-requests.json` (27 fixes), `/home/user/parlour-read-a/challenges-problems-requests.json` (6)

Check: I applied the three fix files to a scratch copy of the repo (not the real one). All 25 check-content ERRORs (6 + 10 + 9) are gone and no new ERROR appears; `render_lesson.js` shows no `!!`. `validate-content.py` then fails only on "locked tags changed" for 10 exercises in 9 files, which is expected: after applying, run `python scripts/lock_tags.py hu a2/<unit id> --update --reason "..."` for a2-142-practice-1, a2-144-check-1, a2-148-practice-1, a2-149-dialogue-2, a2-149-practice-5, a2-150-dialogue-1, a2-152-practice-1, a2-153-check-2, a2-155-consolidation-3, a2-155-dialogue-2. Each fix carries `why`; `"sure": false` marks the uncertain ones. Grammar and lesson files don't round-trip through JSON, so those fixes are exact-text `old`/`new`; exercise fixes use `set` on the id.

Scans done on all three units: no -vá/-vé, -ként, -lak/-lek, no indefinite pronoun before a2-151 (only *valami/valamit*, met since A1), no -ódik before a2-155, no cases or plural possessed taught later, no `distractor_skills` problems other than those listed. Unit 30 introduces no new grammar.

---------------------------------------------------------------------
## UNIT 29: opinions-preferences-comparisons
---------------------------------------------------------------------

### 1. Found by reading
- a2-141-a-gr (screen "azt hiszem"): presents *azt hiszem* as new ("now you know exactly how it's built") and says "no *hogy* is needed", but a2-58-b already taught "azt hiszem, hogy" (skill `szerintem`). The tip repeats "itself drops *hogy*". Fix: open with "You know *azt hiszem* … you already use it with *hogy*; in everyday speech *hogy* is often dropped"; tip made consistent. (a2-145-a-gr even writes "Azt hiszem, hogy X", contradicting 141.)
- a2-141-b-gr: "It sits at the front or end of a sentence exactly like *szerintem*" but its own example puts *gondolom* mid-sentence ("Fáradt vagy, gondolom, hosszú napod volt"). Fix: front, middle or end; say *szerintem* and *azt hiszem* are already known (only *gondolom* is new in 141).
- a2-141-intro-2: option *hall* is unmet (a2-169). Fix: *néz*.
- a2-141-controlled-4: "Fáradtnak látszol, ____ hosszú napod volt." *látszol* is unmet (b2). Fix: "Fáradt vagy, ____, hosszú napod volt." (the screen example); english changed.
- a2-141-practice-1 (ERROR length-giveaway 10 vs 4): stem "never needs hogy" is false (see first item). Fix: "Which phrase opens an opinion with the verb hisz, "to believe"?" with azt hiszem / szerintem / gondolom.
- a2-141-check-1: identical to a2-141-intro-1 (same stem, same options). Fix: ask "idea" (ötlet / vélemény / talán).
- a2-142-a-gr: "put *inkább* right in front of the verb" but in *Inkább teát iszom* it stands before the object. Fix: "right before the thing or action you choose". (unsure)
- a2-142-practice-1: "Which word goes right in front of the verb to say what you'd rather do?" repeats that claim, is tagged vocabulary, and duplicates intro-1. Fix: "Inkább teát iszom, ____ kávét" (mint / mert / és), grammar, `inkabb-mint`.
- a2-143-intro-1 (ERROR 13 vs 9): wrong option *különbség* replaced by *megbeszélés* (met, 11).
- a2-143-dialogue-2: wrong option "Mindkettő jó, egyiket sem szeretem." contradicts itself and *egyiket* is unmet (b1). Fix: "Mindkettő jó, egyformán szeretem azt." (one fault: singular for two restaurants). (unsure)
- a2-143-a-gr tip: "*a másik* is a stand-in for *mint*". It stands in for the repeated noun. Fix.
- a2-143-b-gr: "add the -n/-an/-en ending … you get *egyformán*": *egyforma* ends in -a, so the ending is -n and the vowel lengthens (not "egyformaan"). Fix. (unsure)
- a2-143-b-gr example "Mindkettő jó könyv, egyformán tetszettek." *tetszik* is first taught at a2-181. Fix: "…egyformán szeretem őket." (+ English).
- a2-144-check-1: same stem and options as a2-144-practice-1. Fix: "I agree with Károly" (Egyetértek Károllyal / Károlytól / Károlyra), `verb-government-val-vel`.
- a2-145-dialogue-2 (ERROR tell-absolute): *egyáltalán* is first taught at a2-188 and the wrong reply contradicts itself. Fix: "Azért gondolom, mert rosszabb." (*rosszabb* is met).
- a2-145-consolidation-8 (ERROR 48 vs 31): right option shortened to "Azt hiszem, ez jobb, mint a másik." (34 vs 31).
- a2-145-consolidation-7 (sentence-order): "Károly szerint …" (noun + *szerint*) is never taught and *sokkal* is in no vocabulary list. Fix: "Károly azt hiszi, hogy …" and drop *sokkal*; order unchanged. (unsure)
- a2-141 / a2-145-consolidation (ERROR checklist-shared): first line identical. Fix: consolidation goal and checklist line 1 now "I can give my opinion with szerintem, azt hiszem or gondolom."

### 2. Metadata
- a2-142-practice-1: `vocabulary` + vocab tag for a word-order/pattern question; now `grammar` + `inkabb-mint` (in the same fix).
- a2-144-check-1: new item teaches `verb-government-val-vel` (was `prefix-word-order`).
- (unsure) a2-142-controlled-4 fills *Jobban* (vocabulary tag) while the builder a2-142-practice-4 for the same sentence is `comparative-bb`; pick one.

### 3. Goals / checklists
- Consolidation line 1 reworded (above); `canDo` of the consolidation challenge is the reworded line.
- a2-141 goal line 1 ("introduce an opinion with szerintem, azt hiszem, or gondolom") is mostly recap of a2-58-b; left, but only *gondolom* is new. (unsure)

### 4. Doubtful
- *gyorsabb* (a2-144-dialogue-2, consolidation-9), *finomabb* (consolidation-10), *izgalmasabb* (consolidation-8/12): lemmas *gyors*, *finom*, *izgalmas* are met and -bb is known (a2-64-b), so I treated these suspects as met forms and changed nothing.
- a2-141-dialogue-2: wrong option *Szerinted nagyon jó ötlet.* fails by person (szerinted), not by the form tested. (unsure)
- a2-144-practice-1 / check-1: *Nem egyetértek.* is heard in everyday Hungarian; a native might not call it wrong. (unsure)
- Story a2-unit-29 uses *miatt* (B1 `causal-postpositions`) in "Melyik munka miatt vagy izgatottabb?"; stories are exempt, noted only. Q1 explanation calls Károly Meg's "partnere"; the story never says so. (unsure)
- All six lessons' in-lesson challenge screens still show the generic fallback ("Put your Hungarian skills into practice…", titles cut off mid-phrase such as "Introduce an opinion with"); the new challenges file replaces them.

---------------------------------------------------------------------
## UNIT 30: review-work-past-opinions (review unit)
---------------------------------------------------------------------

### 1. Found by reading
- a2-146-intro-1 (ERROR 9 vs 5): options now munkatárs / szomszéd / feladat. a2-150-consolidation-1 (same ERROR, replay of the same item) gets the same options.
- a2-146-a-gr: "adding a possessive suffix to who you have to do something with *kell* + a personal infinitive" is garbled and wrong (the infinitive takes a personal ending). Fix: "putting a personal ending on the infinitive after *kell* (*Kell dolgoznom*)".
- a2-146-dialogue-2 (ERROR 39 vs 21): wrong option now "Nem, ma nem bemegyek, otthon dolgozom." (same tail, one fault).
- a2-147-dialogue-1 (ERROR 32 vs 24): right option shortened to "Igen, jól tudok zongorázni." (27 vs 24).
- a2-147-writing-1: *jogosítványom* is first taught at a2-210. Fix: "Nem tudok zongorázni, mert sosem tanultam." (unsure). Same word in the a2-147-a-gr table row ("Petra nem tud vezetni, mert nincs jogosítványa."): replaced by *zongorázni … még sosem tanult* (+ English). (unsure)
- a2-148-dialogue-2 (ERROR 38 vs 22): wrong option now "Egy koncerten leszünk, nagyon jó lesz."
- a2-148-a-gr table row "vettem egy kabátot / megvettem a kabátot = I bought a coat / the coat" teaches *meg-* as a definiteness marker; 1st-person *vettem* is the same for both objects and *meg-* is perfective (rulebook § 6). Fix: "vettél egy kabátot / vetted a kabátot".
- a2-148-practice-1 (ERROR 18 vs 13): "I ate up the soup (a definite, finished object)" tests *meg-*, not definite conjugation (*ettem* is identical for both). Fix: "(the whole soup, finished)", options Megettem a levest. / Ettem egy levest. / Eszem a levest. (18/17/15), tag `meg-meaning`. (unsure)
- a2-149-practice-1: "already-fixed plan" also fits *Tervezünk sokat pihenni* (a plan). Fix: "Which sentence uses the present tense for something already arranged?" (unsure)
- a2-149-practice-5 (ERRORs length 12 vs 8, tell-absolute *soha*): options biztosan / valószínűleg / mindenesetre (all met).
- a2-149-dialogue-2: wrong option *Inkább teát iszom.* is a natural way to decline "Menjünk moziba ma este?", so a second reply could be right. Fix: "Jó ötlet, mentünk!" (one fault: past for the suggestion). (unsure)
- a2-150-check-1 (ERROR 11 vs 4): *azért, mert* vs *mert* / *hogy*. Fix: three whole sentences of similar length (Azért nem megyek, mert fáradt vagyok. / Nem megyek, mert … / Nem megyek, ezért fáradt vagyok.). (unsure)
- a2-150-check-2 (ERRORs 32 vs 21 and tell-opener *szerintem*): wrong options now "Szerintem ez egy olcsó étterem." and "Azt hiszem, ez a jobb étterem." (opinion without reason; all 30-32 chars).
- a2-150-dialogue-1: *drágább* is unmet and "Szerintem ez drágább, mert olcsóbb." is nonsense twice over. Fix: "Szerintem ez jobb, mint olcsóbb." (*mint* for *mert*). (unsure)
- Review framing: every grammar screen is titled "Bringing … together" (good), but bodies of a2-147-a/b, 148-a/b, 149-a/b, 150-a read as fresh teaching. Added "You know … from Unit N" openers. (unsure how strict)

### 2. Metadata
- a2-148-practice-1: `definite-past` -> `meg-meaning` (above). (unsure)
- a2-149-practice-5: `a2-review-work-past-opinions-vocab` -> `a2-future-plans-vocab` (*valószínűleg* is a2-131..135 vocabulary; review items keep the skill they review). (unsure) Same question for a2-149-controlled-1 and a2-149-practice-3 (matching of fogok, tervezek, majd, kellene, tagged with this unit's vocab skill while a2-146..148 tag earlier-unit vocab skills); left as is.
- a2-149-dialogue-2: `a2-suggestions-conditional-vocab` -> `junk-suggestion` (wrong option now differs by a form). (unsure)
- a2-150-dialogue-1: vocab -> `mert-because` (wrong option differs by *mint*/*mert*). (unsure)

### 3. Goals / checklists
- Nothing wrong in goal or checklist lines (the unit-30 consolidation lines differ from the lessons').

### 4. Doubtful
- *kilenckor* / *ötkor* (consolidation-10, a2-146 builder): forms of met *kilenc/öt* + `kor-time` (a1-147-b); not changed.
- check-content `consolidation-copy` suspects (a2-150-consolidation-1, -9): replays, left.
- `vocab-unused`: büntetés (147), elveszít, nevet, szerencsére (148; szerencsére is used in consolidation-8), javaslat, helyzet (149), vélemény (150) are listed but never practised in their lesson. All re-list earlier words, so parked.
- a2-147-controlled-4 "Itt nem ____ dohányozni": *lehet* also fits; the hint "by rule" pins *szabad*. (unsure)
- Story a2-unit-30: *izgultam a jelentkezés miatt* uses *miatt* (B1 `causal-postpositions`); stories are exempt. Audit: 2 words not in the dictionary (see 5), no compound guesses.
- No B1-family grammar is presented or drilled in the lessons.

---------------------------------------------------------------------
## UNIT 31: problems-requests
---------------------------------------------------------------------

### 1. Found by reading
- a2-151-dialogue-1 (ERROR 47 vs 35): right option "Nem működik a klíma, és hiányzik egy párna." (43).
- a2-152-dialogue-2 (ERROR 45 vs 24): right option "Szükségem van segítségre." (25 vs 24), the screen phrase.
- a2-152-b-gr: "the same way *birtokom van* patterns work" (*birtokom* never taught) and "just like *szükséges* expressions you've seen before" (never seen). Fix: "the same way *van egy autóm* works" and "as in *segítségre* and *pénzre*".
- a2-153-intro-1 (ERROR 13 vs 7): options visszatérítés / elégedetlen / minőség.
- a2-153-dialogue-1 (ERROR 51 vs 36, suspect *sajnálom* in no vocabulary list): right option "Lehet cserélni vagy visszatérítést kérni." (41).
- a2-153-dialogue-2 (ERROR 37 vs 21): wrong option "A probléma az, hogy nagyon jó a minősége." (same frame, one fault).
- a2-154: *hív* is in no vocabulary list before a2-154 (the list has only *hívás*); suspects *hívok*, *hívtam*, *hívott*, and *hívni* runs through the lesson. Fix: *telefonálni* (in the lesson vocabulary) in a2-154-a-gr (title, table, example; the speaking screen takes the example), a2-154-practice-1, -2, -3, a2-154-dialogue-2, a2-154-writing-1, a2-155-consolidation-11.
- a2-154-practice-1 (ERROR 19 vs 14): options "Holnap fogok telefonálni." / "Holnap telefonálok." / "Tegnap telefonáltam." (25 vs 20).
- a2-154-dialogue-2 (ERROR 24 vs 14): "Mikor fog telefonálni a fogorvos?" with "Holnap reggel fog telefonálni." / "Tegnap reggel már telefonált." (30 vs 29).
- a2-154-a-gr presents the dedicated future tense as new ("Hungarian also has a dedicated future tense") and *fog* as "a completely regular verb"; fog + infinitive was taught in a2-131. Fix: "You know two ways to talk about the future from Unit 27 …".
- a2-155-consolidation-9 (ERROR 58 vs 36): right option "Hibás, ezért kérek egy visszatérítést." (38).
- a2-155-dialogue-2 (ERROR tell-absolute *mindig*): the wrong reply "Igen, még mindig nem működik semmi." contradicts its own "Igen". Fix: "Igen, a recepciós azonnal megoldódott." (one fault: -ódik verb with an agent, which is the lesson's contrast).

### 2. Metadata
- a2-155-dialogue-2: `yes-no-questions` -> `mediopassive-verbs-odik` (with the new wrong option).
- a2-153-check-2 and a2-155-consolidation-3: `distractor_skills` {"2": "hogy-clauses"} sits on the option *hogy*, which makes the sentence ungrammatical; rulebook says none. Removed. (unsure)
- a2-152-practice-1: *tudnak* is a well-formed present form of `tud-infinitive-skills`; add {"2": "tud-infinitive-skills"}. (unsure)

### 3. Goals / checklists
- a2-151: the goal screen lists two lines, the checklist three. Added the third line to the goals and reworded it: "I can talk about someone, everyone and no one, using valaki, mindenki and senki with nem." (old text "…did something, using valaki, mindenki and senki nem." is a fragment and says more than the lesson practises). First line (the challenge `canDo`) unchanged.

### 4. Doubtful
- a2-153-dialogue-2: "A probléma az, hogy hibás a minősége" sounds odd (*rossz a minősége* is natural); *rossz* is in no vocabulary list either, so left. (unsure)
- a2-151-c-gr: says "Without *nem* the sentence is wrong" and then offers *sem*; table "minden-" family includes *mindig*, which is not a *minden-* word (the tip only explains *soha*). Lesson 151 now has three grammar screens (the sheet places `indefinite-pronouns` at a2-151-c-gr, so intended).
- a2-155-a-gr never states the -ódik/-ődik pattern (megold -> megoldódik); it presents the one verb pair, so the skill `mediopassive-verbs-odik` is taught by a single example. (unsure)
- a2-152: all of the conditional (tudna, tudnál, -nék) is known (a1-112, a2-137..139); the screen says "You already know", so left.
- Story a2-unit-31: no defects found; *Ott lehetek négy órakor* gives the one compound guess (5).
- Same-family B1 grammar (causal postpositions, nehogy, volna …) is not presented or drilled in any of the three units.

---------------------------------------------------------------------
## 5. Dictionary
---------------------------------------------------------------------
Literal compound guesses (audit, `--top 0`): unit 29 story none, unit 30 story none, unit 31 story one.

órakor | órakor | adverb | at ... o'clock (óra + -kor) |

Not compound guesses, but reported by the unit 30 audit as "not in the dictionary" (2):

barátnőivel | barátnő | noun | with her girlfriends (plural possessed -i + -vel) |
károllyal | Károly | noun | with Károly (name + -val) |
