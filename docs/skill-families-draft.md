# Vocabulary topic families — draft for approval (ROADMAP 125, step 1)

Status: **draft, 2026-10-04. Not enforced and not in `skill-registry.json` yet.**
Once approved, each unit vocabulary skill (`a1-unit05-vocab`,
`b1-orszagma-vocab`, …) gets one or more of these as its `family` in the
registry. Grammar families are a separate list, still to be drafted.

## Sources checked

| Source | What it is | Why it counts |
|---|---|---|
| **CEFR (2001), §4.1, themes of communication** | 14 themes taken from the Threshold Level (1990). The CEFR gives them as an example classification, not a required list. | It's the framework itself. Short and coarse. |
| **Plan Curricular del Instituto Cervantes (PCIC), *Nociones específicas*** | 20 thematic notion areas, each itemised A1–C2. The PCIC sets them against the CEFR's personal, public, occupational and educational domains. | The CEFR-based reference for Spanish, used by DELE/SIELE. The most detailed of the three, and it covers every level. |
| **Hungarian érettségi, Hungarian as a foreign language, oral topics** | 10 topic areas for the school-leaving exam (intermediate ≈ B1, advanced ≈ B2). | The only official Hungarian-as-a-foreign-language topic list that could be retrieved. The ECL and Origó topic lists aren't published online (both exam centres' PDFs returned 404). |

The PCIC list is the backbone because it covers all levels and is the
most detailed. The other two are used to check for anything it leaves out.

## The proposed families

Families 1–20 are the PCIC's 20 notion areas, one to one. Families 21–25
are added because our units need them, and each one says where its
justification comes from.

| # | Family slug | Name | PCIC (*nociones específicas*) | CEFR / Threshold theme | Hungarian érettségi |
|---|---|---|---|---|---|
| 1 | `body` | the body and appearance | 1 Individuo: dimensión física | personal identification (in part); health and body care | 2 Ember és társadalom (in part) |
| 2 | `feelings-character` | feelings, senses and character | 2 Individuo: dimensión perceptiva y anímica | — | 2 Ember és társadalom (in part) |
| 3 | `personal-identity` | personal details and identity | 3 Identidad personal | personal identification | 1 Személyes vonatkozások |
| 4 | `relationships` | family, friends and social life | 4 Relaciones personales | relations with other people | 1 …család; 2 Ember és társadalom |
| 5 | `food-drink` | food and drink | 5 Alimentación | food and drink | 6 Életmód (in part) |
| 6 | `education` | school and learning | 6 Educación | education | 4 Az iskola |
| 7 | `work` | work and professions | 7 Trabajo | — | 5 A munka világa |
| 8 | `leisure` | free time, sport and going out | 8 Ocio | free time, entertainment | 7 Szabadidő, művelődés, szórakozás |
| 9 | `media` | news, media and communication | 9 Información y medios de comunicación | — | 9 Tudomány és technika (in part) |
| 10 | `housing` | home and housing | 10 Vivienda | house and home, environment | 3 Környezetünk (in part) |
| 11 | `services` | services: post, bank, offices | 11 Servicios | services | 2 Ember és társadalom (in part) |
| 12 | `shopping` | shopping and clothes | 12 Compras, tiendas y establecimientos | shopping | 2 Ember és társadalom (in part) |
| 13 | `health` | health and hygiene | 13 Salud e higiene | health and body care | 6 Életmód (in part) |
| 14 | `travel` | travel, accommodation and transport | 14 Viajes, alojamiento y transporte | travel | 8 Utazás, turizmus |
| 15 | `economy` | economy and money | 15 Economía e industria | — | 10 Gazdaság |
| 16 | `science-technology` | science and technology | 16 Ciencia y tecnología | — | 9 Tudomány és technika |
| 17 | `society-politics` | government, politics, law and society | 17 Gobierno, política y sociedad | — | 2 Ember és társadalom (in part) |
| 18 | `arts` | arts and culture | 18 Actividades artísticas | free time, entertainment (in part) | 7 …művelődés |
| 19 | `religion-philosophy` | religion and philosophy | 19 Religión y filosofía | — | — |
| 20 | `geography-nature` | geography, nature, weather and environment | 20 Geografía y naturaleza | weather | 3 Környezetünk |
| 21 | `daily-life` | daily routine | not a notion area | **daily life** | 6 Életmód |
| 22 | `town-places` | the town and getting around it | not a notion area (city vocabulary is spread over areas 10, 11 and 20) | **places** | 3 Környezetünk |
| 23 | `language` | language and language learning | not a notion area | **language** | — |
| 24 | `history` | history | not a notion area. PCIC covers it under *Referentes culturales*, not the notions. | — | — |
| 25 | `basics` | greetings, numbers and time | not a notion area. PCIC covers these as *Funciones* and *Nociones generales* (quantity, time), not as topics. | — | — |

**Decisions to make:**
- **Keep 21–25 as families, or fold them in?** `daily-life` could go
  into `leisure` + `housing`, and `town-places` into
  `geography-nature`. `history` and `basics` don't fit anywhere else
  without stretching a family. My recommendation: keep all five. 21–23 are
  CEFR themes in their own right, 24 holds about 65 units (most of
  the es-latam Latin America and HU B1 citizenship tracks), and 25 is what A1 units 1–3
  actually teach.
- **One family or a list per unit?** Many B2/C1 units span two
  (*Medicine, Ethics & Responsibility* = `health` + `religion-philosophy`).
  Recommendation: a list, at most two, the main one first.

## What the cross-check shows about our units

This is from reading every unit title in all three courses (637 units), not yet a unit-by-unit mapping.

1. **Well covered at A1–B1:** families 3–8, 10, 12–14 and 20–22 all have
   units at every level. The shared B1 core list (*Relationships*,
   *Work & Professional Life*, *Health & Wellbeing*, …) lines up almost
   one-to-one with the PCIC areas.
2. **Gaps against the standards:**
   - **`religion-philosophy` (PCIC 19).** No Spanish unit at any level.
     In Hungarian it appears only from B2 (*Political Philosophy*) and C1.
     PCIC itemises this area from A1, at a basic level (festivals,
     beliefs).
   - **`services` (PCIC 11, CEFR "services").** Hungarian A2 has *Post
     Office*, *Banking*, *Pharmacy*. Spanish Core has no services unit at
     any level. Only the es-es citizenship track touches it
     (*Consumo… Servicios Bancarios*, *Sistema Nacional de Salud*).
   - **Clothes (inside `shopping`).** Hungarian A1 has *Clothes &
     Appearance*. Spanish A1/A2 have no clothes unit.
   - **`education` at A1.** Spanish meets it only at A2 (*Studying and
     School Life*). Hungarian has it at A2 and B1.
3. **Units named after a function or grammar point, not a topic.** Most
   Spanish A2 units (*Talking About What Happened*, *The Imperfect Tense*,
   *Por vs. Para*, …) and several A1/B1 ones (*Demonstratives*,
   *Reported Speech*, *Connecting Ideas*) don't name a topic. Their family has to come from what their vocabulary list
   actually contains, so each needs reading, not a guess from the title.
4. **The topic list is set by level in the standards, not just by name.**
   PCIC assigns each item a level, and *Economía e industria* at A2 is
   prices and shops, not fiscal policy. The family says *what area* a word
   belongs to, and the level still comes from the unit. That's
   consistent with how the registry already stores `level`.

## Next steps once this list is approved

1. Map each unit vocabulary skill to its families: about 290 Hungarian
   ones and about 114 per Spanish course. The grammar-named units
   (finding 3) need their vocabulary lists read. Review it as a table
   before it goes into the registry.
2. Draft the grammar families the same way, checked against the PCIC
   *Gramática* inventory for Spanish. For Hungarian, use the grammar
   points the érettségi and ECL/Origó specifications name, as far as they
   can be found.
3. Decide whether the gaps in finding 2 become content items in the
   ROADMAP.

## Sources

- CEFR (2001), §4.1. The 14 Threshold Level themes are summarised at
  [IH Cairo, "Common European Framework of Reference"](https://ihcairoeg.com/about-ih-cairo/cefr/)
  and in [this ECML training worksheet](https://www.ecml.at/Portals/1/3MTP/ECEP/training-kit/PageEN/D/Worksheet_B_Plurilingualism_multilingualism.doc).
  The Council of Europe's own PDF (rm.coe.int) refused automated
  fetching, so the list wasn't checked against the original text.
- [Instituto Cervantes, PCIC, *Nociones específicas*: introduction](https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/09_nociones_especificas_introduccion.htm)
- [Jelky András Iparművészeti Szakgimnázium, oral érettségi topics, Hungarian as a foreign language, 2024/2025](https://jelky.hu/fix/erettsegi/magyarmintidegennyelv2025.pdf),
  with subtopics as listed in
  [Semmelweis Egyetem Bókay János Gimnázium, foreign-language érettségi topics](https://semmelweis.hu/bokay/files/2022/10/ELO-IDEGEN-NYELV-ERETTSEGI-TEMAKOROK.pdf)
