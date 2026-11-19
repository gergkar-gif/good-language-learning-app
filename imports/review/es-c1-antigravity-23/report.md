# ES C1 Core Unit 23 (`idiom-figurative`) — Writer Report

Self-read: 8 fixes (`imports/review/es-c1-antigravity-23/self-read.md`, `imports/review/es-c1-antigravity-23/self-read-fixes.json`).

## What was written
- **Unit type:** Topic unit (no new C1 grammar skill; notes drafted at `imports/review/es-c1-plan/notes/idiom-figurative.md` per `notes/README.md`).
- **Skills covered:**
  - Lesson 01 (vocabulary-led): `c1-idiom-figurative-vocab` (`c1-23-01-a-gr`) — everyday figurative idioms (*el modismo, meter la pata, dar en el clavo, echar una mano, quedarse de piedra, no tener pelos en la lengua*).
  - Lesson 02 (recap): `verbos-regimen-preposicional` (`c1-23-02-a-gr`, recapping B1 Unit 29) — figurative prepositional verbs (*dar con, caer en la cuenta, cargar con, tropezar con, encajar, romper con*).
  - Lesson 03 (recap): `manner-clauses` (`c1-23-03-a-gr`, recapping B2 Unit 32) — proverbial and figurative manner frames (*como anillo al dedo, como quien no quiere la cosa, tal como suena, figurado, proverbial, el dicho*).
  - Lesson 04 (recap): `inversion-enfasis-fronting` (`c1-23-04-a-gr`, recapping B2 Unit 1) — emphatic fronting with figurative phrases (*a ciegas, el hilo, romper el hielo, enredar, desenredar, la trampa*).
  - Lesson 05 (recap + story): `gerundio-acciones-paralelas` (`c1-23-05-a-gr`, recapping B1 Unit 2) — figurative gerunds in storytelling (*tirar la toalla, hacer la vista gorda, esquivar, la dueña, la tertulia, el marcapáginas*).
  - Consolidation (`c1-23-consolidation`): 12 exercises across 6 distinct `teaches` tags (the 5 unit skills + `imperfect-subjunctive-forms` for *como si* + pluperfect subjunctive).
- **Content files:** 6 lessons, 5 grammar screens, 5 vocab files (30 new lemmas total, 6 per lesson), 6 exercise files (55 exercises locked), 1 story (`content/es-latam/stories/original/c1/c1-23.json`, *El marcapáginas olvidado*, 426 words, invented neighbourhood bookshop-café reading circle with Carlos and Meg, zero real-world factual claims), and 6 challenges in `content/es-latam/curriculum/challenges.json`.

## Norm claims
- `c1-23-04-a-gr`: After a fronted negative phrase (*ni una palabra*), Spanish drops *no* before the verb (*Ni una palabra soltó*, never *Ni una palabra no soltó*) and places an explicit subject after the verb.
- `c1-23-05-a-gr`: In formal Spanish, the gerund expresses an action simultaneous with or framing the main verb; avoid the *gerundio de posterioridad* for a clearly later result (join sequential events with *y* + finite verb).
- `es-latam` only: no `vosotros` / `os` anywhere, no Spain-only vocabulary, no unintroduced later-unit grammar (`leismo-laismo-reconocimiento` not used).

## Checks after self-read
- `python scripts/check-content.py es-latam c1 idiom-figurative`: **0 error(s), 0 suspect(s)**
- `python scripts/check-content.py --changed`: **no new errors**
- `node scripts/unmet-words.js es-latam --stems c1-23-01,c1-23-02,c1-23-03,c1-23-04,c1-23-05,c1-23-consolidation --with-hidden`: **`[]` (0 unmet words)**
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s) before their screen**
- `python scripts/check_unit_refs.py es-latam c1 idiom-figurative --bare --named`: 3 recap notices checked by hand (all three verbs *acostumbrarse a*, *adaptarse a*, *darse cuenta de* appear verbatim on `b1-29-03-change-experience-gr`; simultaneous gerund appears verbatim on `b1-02-02-indefinido-experiencias-gr`).
- `node scripts/audit-reader-coverage.js es-latam --story c1-23 --top 0`: **0 not in dictionary, 0 literal compound guesses, 0 lookup throws** (426 tokens, 249 unique words)
- `python scripts/validate-content.py --changed`: **24/24 es-latam passed, 0 failed**
- `python scripts/lock_tags.py es-latam c1/idiom-figurative --update --reason "self-read"`: **55 exercise(s) locked**

---

## 4-Unit Block Summary (Units 20–23)

| Unit | ID | New skill(s) | Self-read fixes | `check-content` | `unmet-words` | `audit-reader-coverage` | Schema |
|---|---|---|---|---|---|---|---|
| 20 | `concession-evaluation` | `futuro-concesivo`, `con-lo-que-para-lo-que` | 18 | 0 err / 0 susp | 0 | 0 / 0 / 0 | 24/24 |
| 21 | `irony-humour` | `ni-que-exclamativo` | 8 | 0 err / 0 susp | 0 | 0 / 0 / 0 | 24/24 |
| 22 | `tone-attitude` | `sufijos-apreciativos` | 9 | 0 err / 0 susp | 0 | 0 / 0 / 0 | 24/24 |
| 23 | `idiom-figurative` | *(topic unit; notes drafted)* | 8 | 0 err / 0 susp | 0 | 0 / 0 / 0 | 24/24 |

**For the user:** All four units (20–23) are committed and pushed to `master` with 0 errors, 0 suspects, 0 unmet words, and 0 dictionary misses. Stopping here after 4 units per `RUN.md`; start a fresh chat to continue from Unit 24.
