# HU A1–A2 against public CEFR syllabi: gap proposal (2026-10-14)

Before HU A2 enters the unit pipeline (ROADMAP 153(a)), the A1–A2 skill list
(`skills/hu.json`: A1 65 grammar / 33 vocabulary, A2 60 / 44) was checked
against public Hungarian A1–A2 syllabi. Every candidate was then checked in
`content/hu/grammar/a1|a2` (screen titles and bodies) and in the A1–A2
exercises, so a point that is taught but tagged elsewhere is not reported as
missing. **Signed off by the user 2026-10-14:** all nine grammar skills added (done) and the three new units and the V4 fold-in approved. Each skill has
an entry in `skills/frozen-hu.json`.

## Sources

- University of Vienna Sprachenzentrum, Hungarian A1/1–A2/3 (MagyarOK-based):
  https://sprachenzentrum.univie.ac.at/en/hungarian
- University of Veterinary Medicine Budapest, Hungarian A1/1 and A1/2 (to A2):
  https://univet.hu/en/education/courses/hungarian-a1-1/ ,
  https://univet.hu/en/education/courses/hungarian-a1-2/
- University of Novi Sad, Hungarian A2.1:
  https://ff.uns.ac.rs/en/fis/karton_predmeta/15MJ002
- Duolingo HU course, sections labelled CEFR A1 / A2:
  https://www.duolingodata.com/dat/hufen110v2.html
- Council of Europe Waystage / Threshold topic list (the language-neutral
  A2/B1 theme list: personal identification, house and home, daily life,
  free time, travel, relations with others, health, education, shopping,
  food and drink, services, places, language, weather, environment).
- No official Hungarian A2 grammar list exists online: ECL has no grammar
  paper and its public A2 page is language-neutral; the Hungarian
  *Küszöbszint* is B1.

## Already covered (checked, no action)

Cases incl. -nál/-nél, -hoz, -tól/-ig, -kor, -ért, -ként, -nként, -vá/-vé;
days/months/seasons/dates (screens `a1-78…80`, `a2-03`, `a2-06-b`, `a2-07-b`,
`a2-62`; tagged `on-en-on` / `ban-ben-in` / vocabulary, which fits);
definite/indefinite present and past, *volt*, *fog*, imperative, conditional,
-hat/-het, prefixes, infinitive and inflected infinitive, *kell/szabad/tilos/
tud/akar/szokott*, ordinals, comparative/superlative, -s adjectives, -an/-en
adverbs, case-inflected and accusative pronouns (*engem, téged*), relative
clauses, *hogy*-clauses, *óta* and *múlva*, -lak/-lek, *egymás*, *magam*.
Themes: all 14 Waystage themes have at least one unit except the ones below.

## Grammar gaps (no screen anywhere in A1–A2, used in content untaught)

| # | point | evidence | proposed skill | level, family | taught_in (new screen) | requires |
|---|---|---|---|---|---|---|
| G1 | indefinite / universal / negative series: *valaki, valami, valahol, mindenki, minden, mindenhol, senki, semmi, sehol* (+ *nem*) | Duolingo A2 ×2 units; 79 A1–A2 exercises use the words, tagged on vocabulary; no screen at any level (B2 has only *bárki/akármi*) | `indefinite-pronouns` | A2, pronouns | `problems-requests` (next to `a2-160-a` *Valami elromlott*) | `soha-needs-nem-negative-concord` |
| G2 | demonstrative agreement with case: *ebben a házban, azzal a busszal, az előtt a ház előtt* | Duolingo A2 ×3 units; 29 exercises use it; no screen | `demonstrative-case-agreement` | A2, articles-demonstratives | `neighbourhood-city` | `demonstratives-ez-az`, `ban-ben-in` |
| G3 | adjectives in -i: *budapesti, mai, reggeli, magyarországi* | Vienna A2/1; used on 28 A2 screens, never explained | `i-adjectives` | A2, word-formation | `neighbourhood-city` or `time-dates-schedules` | `vowel-harmony` |
| G4 | possessor in -nak/-nek: *Péternek a kocsija, annak a fiúnak a kutyája* | Vienna A1/2 "possessive structures"; no screen | `dative-possessor` | A2, possession | `plural-possessed` | `3rd-person-possessive` |
| G5 | anaphoric possessive -é: *Kié? Péteré, a szomszédé* | standard A1–A2 point; *Kié?* appears on 3 A1 screens unexplained | `anaphoric-possessive-e` | A2, possession | `plural-possessed` | `possessive-pronouns-enyem` |
| G6 | family/group plural -ék: *Péterék, Kovácsék* | standard A2 point; no screen | `ek-group-plural` | A2, nouns | `family-life` | `plural-nouns-k` |
| G7 | "ago": *két éve, két évvel ezelőtt* + past | Duolingo A2; no screen. (Checked 2026-10-14: the 21 A2 items with *két éve / két napja* are present-tense "for X years" and rightly on `ota-duration`; "ago" + past is untaught.) | `ago-ezelott` | A2, time-clauses | `the-past-1` | `past-tense-indefinite`, `ota-duration` |
| G8 | collective numerals: *ketten, hárman, Hányan vagytok?* | Duolingo A2 "how many"; no screen, no use | `collective-numerals-an` | A2, numbers-quantity | `friends-relationships` | `cardinal-numbers` |
| G9 | basic connectors *és, de, vagy, hanem, pedig* | taught on `a1-100-b-gr` and `a1-69-b-gr` but there is no skill, so their items sit on vocabulary | `basic-connectors` | A1, coordination | `a1-100-b-gr` (exists) | none |

Kept as they are (level difference, not a gap): indirect speech, -ó/-ő agent
nouns and -ás/-és nouns appear at A2 in the Vienna syllabus but are B1 skills
here (`reported-speech-statements`, `present-participle`, `nominalization`;
the 2026-10-07 proposal already kept -ás/-és at B1). *mégis/mégsem* and
*tehát* stay with the B1 connector skills. -zik verbs (*reggelizik,
teniszezik*) stay vocabulary (plain -ik conjugation).

## Vocabulary theme gaps

| # | theme | evidence | A1–A2 today |
|---|---|---|---|
| V1 | nature, countryside and animals (pets, farm animals, landscape, Hungarian geography: Balaton, Duna, Alföld) | Waystage "environment"; Duolingo A1 "animals"; Vienna A2/1 "country vs city" | a dog and a cat on two A1 postposition screens; no animals at A2; landscape words only in passing |
| V2 | phone, internet and technology (texting, apps, e-mail, passwords, "it doesn't work") | Duolingo A1 "technology"; Vienna A1/1 "technical problems" | a few words on 6 A2 screens |
| V3 | holidays and celebrations (birthday, name day, Christmas, Easter, national days, wishes like *Boldog születésnapot!*) | Duolingo A1 "celebrations"; Vienna A2/3 "hosting guests, Hungarian culture" | one name-day screen (`a2-184-a`); no Christmas, Easter or national days |
| V4 | emergencies and the police (112, theft, lost property, accident) | Waystage "services" | 112 on pharmacy screens; no police or lost-property language |

Each new theme is a new unit and a new vocabulary skill
(`a2-<unit>-vocab`). V4 could instead be folded into `problems-requests` and
`pharmacy` (no new skill).
