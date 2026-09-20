# Parlour CEFR Curriculum Roadmap

**Status**: Phases 1, 2, and 3 **COMPLETED** ✅  
**Remaining Phases**: Scheduled as **TO-BE-DONE LATER** ⏳

---

## How units get wired in (as of 2026-09-16)

Authoring a unit's lesson/grammar/exercise/vocabulary files is not enough
on its own — a level's unit titles, ordering, and lesson-stem groupings
are a separate, curated list, and a lesson file with nothing pointing at
it is invisible to the Learn tab (this happened to the Phase 2 imperfecto
content: it validated cleanly for a while before anyone wired it in).

For a level that already has an explicit table (Spanish A1/A2/B1,
Hungarian B1), add a new unit like this:

1. Author and validate the lesson/grammar/exercise/vocabulary files as
   usual (`python scripts/validate-content.py`).
2. Append one entry to `content/<lang>/curriculum/units/<level>.json`:
   `{"title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}`
   (add `"track": "core"` / `"latam"` / etc. only for a level that runs
   more than one parallel track). Schema:
   `content/<lang>/schemas/units.schema.json`.
3. Run `python build-manifest.py` (or just push — `sync-generated-content.yml`
   does this automatically for anything touching `content/**`) to
   regenerate `curriculum.json`, `decks.json`, and the story/grammar
   indexes.

No `build-manifest.py` edit needed — before 2026-09-16 this table lived
in a hardcoded Python dict there, which is exactly what made Phase 2's
imperfecto units hard to wire in after the fact. A level with no such
file (Hungarian A1/A2 today) instead auto-groups plain-numbered lesson
files from disk (`auto_group_units()` in `build-manifest.py`) — nothing
to hand-wire there either way.

---

## 🟢 Phase 1: Spanish A1 Core Gaps [COMPLETED]

| Unit ID | Unit Title | Key Grammatical / Functional Focus | Status |
|:---|:---|:---|:---|
| `unit.a1.gustar` | **What Do You Like? (Gustar)** | Inverted syntax, *me gusta* vs. *me gustan*, indirect object pronouns (*me, te, le, nos, les*), *gustar + infinitivo*, *encantar*, *interesar*. Story: *Las cosas que le gustan a Meg*. | ✅ **Live on master** |
| `unit.a1.reflexive` | **Daily Routine: Reflexive Verbs** | Paradigm (*me, te, se, nos, se*), routine verbs (*levantarse, ducharse, lavarse*), stem-changing reflexives (*despertarse [e→ie]*, *acostarse [o→ue]*, *vestirse [e→i]*), transitive vs. reflexive contrast (*lavar* vs *lavarse*), sequencing connectors (*primero, luego, después, antes de + inf*). Story: *Una mañana ocupada en Hanói*. | ✅ **Live on master** |
| `unit.a1.demonstrative` | **Demonstratives: This, That, and Over There** | Demonstrative adjectives/pronouns (*este/esta/estos/estas*, *ese/esa/esos/esas*, *aquel/aquella/aquellos/aquellas*), 3-tier spatial system (*aquí, ahí, allí*), neuter pronouns (*esto, eso, aquello*), market transactions. Story: *De compras en el mercado de Hanói*. | ✅ **Live on master** |
| `unit.a1.continuous` | **What Are You Doing? (Present Continuous)** | *Estar + gerundio* (*-ando*, *-iendo*), irregular gerunds (*leyendo, durmiendo, yendo, diciendo*), contrast with simple present (habits vs. current action), phone dialogues. Story: *Una llamada telefónica en Hanói*. | ✅ **Live on master** |
| `unit.a1.doler` | **What Hurts? (The Verb Doler)** | Inverted *doler* (*me duele* vs. *me duelen*), body parts (*cabeza, garganta, espalda, estómago, pies, ojos*), intensity (*mucho, un poco, nada*), health states with *estar* (*mareado, resfriado, cansado*), pharmacy remedies (*pastillas, jarabe*), contrast with *tener dolor de*. Story: *Un dolor de cabeza en Hanói*. | ✅ **Live on master** |
| `unit.a1.abilities` | **Skills & Abilities: Poder & Saber** | *Poder + infinitivo* (ability, permission, polite requests: *¿puedes ayudarme?*), *saber + infinitivo* (skills: *sé nadar*), *saber vs conocer*, obligatory **personal 'a'** (*conozco a Carlos, veo al profesor*), asking for favors. Story: *Nuevas habilidades en Hanói*. | ✅ **Live on master** |

---

## ✅ Phase 2: Spanish A2 — Pretérito Imperfecto [DONE 2026-09-16]

The Imperfecto is the second pillar of Spanish past-tense narration.

- [x] **Unit 21: The Imperfect Tense (`unit.a2.21`, stems `a2-imperfectobasico-*`)**
  - Regular *-ar* endings, regular *-er/-ir* endings, the 3 irregulars
    (*ser → era*, *ir → iba*, *ver → veía*), states/descriptions in the
    past, childhood-memory context. Shipped as 5 lessons + consolidation,
    not the originally-planned single unit — content grew during
    authoring/migration.
- [x] **Unit 22: Imperfect vs. Preterite (`unit.a2.22`, stems `a2-imperfectocontraste-*`)**
  - Background (Imperfecto) vs. foreground events (Indefinido),
    *mientras + imperfecto, [indefinido]*, weather/time/feelings in the
    past, narrative structure. 5 lessons + consolidation.

These landed as plain units 21/22 (appended after the existing 1-20),
not slotted into the story's grammar sequence at the point this phase
was originally scoped for — see "How units get wired in" below for why
that's now just a JSON append rather than a `build-manifest.py` edit.

---

## ✅ Phase 3: Spanish A2 — Imperativo & Clitic Pronouns [DONE 2026-09-17]

- [x] **Unit 23: Giving Instructions and Directions (`unit.a2.imperativoafirmativo`, stems `a2-imperativoafirmativo-*`)**
  - **Focus**: Regular *tú* imperatives (3rd person present), the 8 irregular *tú* imperatives (*ven, pon, sal, di, ten, haz, ve, sé*), formal *usted/ustedes* imperatives.
  - **Context**: Directions in a city, recipes, step-by-step instructions.
  - **Story**: *Las instrucciones de la abuela* (`a2-original-imperativoafirmativo`).
- [x] **Unit 24: Setting Rules and Warnings (`unit.a2.imperativonegativo`, stems `a2-imperativonegativo-*`)**
  - **Focus**: Negative *tú* commands (*no hables, no comas*), pronoun attachment to affirmative commands (*dime, siéntate, ponlo*) vs. placement before negative commands (*no me digas, no te sientes*). Accent shifts (*dímelo*).
  - **Story**: *Las reglas del hostel* (`a2-original-imperativonegativo`).
- [x] **Unit 25: Explaining Who and What: Pronouns (`unit.a2.pronombrescliticos`, stems `a2-pronombrescliticos-*`)**
  - **Focus**: Indirect object pronouns (*me, te, le, nos, les*) with verbs like *dar, decir, preguntar*, and combined double-object clitics (*se lo dije*, *le → se* rule).
  - **Story**: *Un favor entre amigos* (`a2-original-pronombrescliticos`).

---

## ✅ Phase 4: Spanish A2 — Modality, Subjunctive & Pragmatics [DONE 2026-09-17]

- [x] **Unit 26: Asking Politely and Giving Advice (`unit.a2.condicionalsimple`, stems `a2-condicionalsimple-*`)**
  - **Focus**: *-ría* endings for polite service requests (*me gustaría, ¿podría usted...?*) and giving advice (*deberías descansar, yo en tu lugar estudiaría*). 5 lessons + consolidation.
  - **Story**: *El dilema del café* (`a2-original-condicionalsimple`).
- [x] **Unit 27: Expressing Wishes and Feelings (`unit.a2.subjuntivobasico`, stems `a2-subjuntivobasico-*`)**
  - **Focus**: Introductory subjunctive triggers at A2: desires (*quiero que vengas*), feelings (*me alegra que estés aquí*), impersonal expressions (*es importante que estudies*), future time with *cuando* (*cuando llegues, llámame*). 5 lessons + consolidation.
  - **Story**: *Deseos para el viaje* (`a2-original-subjuntivobasico`).
- [x] **Unit 28: Connecting Ideas and Habits (`unit.a2.perifrasisverbales`, stems `a2-perifrasisverbales-*`)**
  - **Focus**: Verbal periphrases (*empezar a + inf*, *dejar de + inf*, *seguir + gerundio*, *volver a + inf*, *llevar + tiempo + gerundio*) and discourse connectors (*sin embargo, por lo tanto, además, en primer lugar*). 5 lessons + consolidation.
  - **Story**: *Nuevos hábitos en Valencia* (`a2-original-perifrasisverbales`).
- [x] **Unit 29: Studying and School Life (`unit.a2.educacionyestudios`, stems `a2-educacionyestudios-*`)**
  - **Focus**: School subjects, academic strengths/weaknesses (*se me da bien / me cuesta*), university life, exams and classroom interaction. 5 lessons + consolidation.
  - **Story**: *El primer día en la facultad* (`a2-original-educacionyestudios`).

---

## ✅ Phase 5: Hungarian A1 — Core Case Integrations [DONE 2026-09-17]

- [x] **Unit 31: Coming from Places: Origin Cases (`unit.a1.31`, stems `a1-151` to `a1-155` + `a1-155-consolidation`)**
  - **Focus**: Elative case *-ból/-ből* (out of 3D enclosed spaces), delative case *-ról/-ről* (off surfaces and from Hungarian cities: *Budapestről, Szegedről*), delative for topics (*Miről beszélünk? A munkáról beszélek*), and 3-way source case contrast (*-ból/-ből, -ról/-ről, -tól/-től*). 5 lessons + consolidation.
  - **Story**: *Honnan jöttök?* (`a1-unit-31`).
- [x] **Unit 32: Languages & Manner: The Essive-Modal (`unit.a1.32`, stems `a1-156` to `a1-160` + `a1-160-consolidation`)**
  - **Focus**: Essive-modal *-ul/-ül* for language adverbials (*magyarul, angolul, németül, spanyolul*), verbs of comprehension/learning (*tanul, ért, olvas, ír*), fluency and degree adverbs (*egy kicsit, jól, folyékonyan, már, még, csak*), and manner adverbs (*rosszul, egyedül, például*). 5 lessons + consolidation.
  - **Story**: *Nyelvgyakorlás a kávézóban* (`a1-unit-32`).
- [x] **Unit 33: Where Things Are: Postpositions (`unit.a1.33`, stems `a1-161` to `a1-165` + `a1-165-consolidation`)**
  - **Focus**: Core postpositions with bare nominative nouns: *alatt* (under), *felett/fölött* (above), *mellett* (next to), *előtt* (in front of / before), *mögött* (behind), *között* (between/among), *után* (after in space/time), and *alatt* (during). 5 lessons + consolidation.
  - **Story**: *Hol van a jegy?* (`a1-unit-33`).

---

## ✅ Phase 6: Hungarian A2 — Inflected Personal Pronouns [DONE 2026-09-17]

- [x] **Unit 33: Declined Pronouns: Internal & Surface Cases (`unit.a2.33`, stems `a2-161` to `a2-165` + `a2-165-consolidation`)**
  - **Focus**: Inessive (*bennem, benned, benne, bennünk, bennetek, bennük*), Superessive (*rajtam, rajtad, rajta, rajtunk, rajtatok, rajtuk*), Sublative (*rám, rád, rá, ránk, rátok, rájuk*), governing verbs (*bízik, csalódik, segít, számít, múlik*). 5 lessons + consolidation.
  - **Story**: *Egy fontos vizsga előtt* (`a2-unit-33`).
- [x] **Unit 34: Declined Pronouns: Proximity & Motion (`unit.a2.34`, stems `a2-166` to `a2-170` + `a2-170-consolidation`)**
  - **Focus**: Adessive (*nálam, nálad, nála, nálunk, nálatok, náluk* — "at my place"), Allative (*hozzám, hozzád, hozzá, hozzánk, hozzátok, hozzájuk* — "coming to me"), Ablative (*tőlem, tőled, tőle, tőlünk, tőletek, tőlük* — "from me"), Delative (*rólam, rólad, róla, rólunk, rólatok, róluk* — "about me"), hosting & visiting etiquette. 5 lessons + consolidation.
  - **Story**: *Vendégség a barátoknál* (`a2-unit-34`).

---

## ✅ Phase 7: Hungarian A2 — Advanced Grammar & Culture [DONE 2026-09-17]

- [x] **Unit 35: Change of State: The Translative Case (`unit.a2.35`, stems `a2-171` to `a2-175` + `a2-175-consolidation`)**
  - **Focus**: Translative-Factitive *-vá/-vé* morphology and consonant assimilation (*orvossá, széppé, fává, vízzé*), verbs of becoming (*válik*), verbs of making/transforming (*tesz*), natural state changes (*jéggé fagy, vízzé olvad*), and idioms (*valósággá válik, divattá válik, kővé dermed*). 5 lessons + consolidation.
  - **Story**: *Az új műhely* (`a2-unit-35`).
- [x] **Unit 36: Roles & Capacities: The Essive-Formal (`unit.a2.36`, stems `a2-176` to `a2-180` + `a2-180-consolidation`)**
  - **Focus**: The invariant suffix *-ként*, professions (*tanárként, orvosként*), stages of life (*gyerekként, felnőttként*), function/purpose (*ajándékként, emlékként, megoldásként*), temporal & distributive rate adverbs (*időnként, helyenként, óránként, fejenként*), and contrast with *-nak/-nek* and nominative. 5 lessons + consolidation.
  - **Story**: *Önkéntesként a táborban* (`a2-unit-36`).
- [x] **Unit 37: Sociocultural Pragmatics & Customs (`unit.a2.37`, stems `a2-181` to `a2-185` + `a2-185-consolidation`)**
  - **Focus**: Deferential politeness (*tetszikelés*: *Hogy tetszik lenni? Mit tetszik kérni?*), public formulas (*tessék, kérem, parancsoljon, legyen szíves*), Hungarian Eastern name order (*Kovács Péter*), honorifics (*tanár úr, doktornő, néni, bácsi, -né*), Name Days (*Névnap*, *Boldog névnapot!*), toasting etiquette (*Egészségedre!* with mandatory eye contact), and home visiting hospitality (guest slippers, gifts, *Jó étvágyat!*). 5 lessons + consolidation.
  - **Story**: *Névnap a nagymamánál* (`a2-unit-37`).

---

## ✅ Phase 8: Comprehensive CEFR Assessment Tests [DONE 2026-09-17]

- [x] **Multi-Modal CEFR Test Architecture & Engine Upgrade (`engine/leveltest.js`, `styles/components.css`)**:
  - Expanded test engine beyond simple dropdown cloze to authentic CEFR 3-part level assessments:
    - **Part 1: Language in Context**: Contextual Cloze (`dropdown`), Active Recall Text-Input (`text-input`), and Pragmatic Communicative Choice (`choice`).
    - **Part 2: Short Written Production (`writingTask`)**: Integrated writing prompt with target length meter, live keyword/target badge feedback, and CEFR rubric checks.
    - **Part 3: Short Spoken Production (`speakingTask`)**: Live voice recording with SpeechRecognition live transcription, audio playback, and accessible typed/dictation fallback.
  - Schema updated (`content/{es,hu}/schemas/test.schema.json`) supporting 20–40 items, `oneOf` question definitions, and optional productive tasks.
- [x] **Update `content/es/tests/a1-test.json`**:
  - 22 varied questions testing `ser/estar`, reflexives, `gustar`, demonstratives, time, prepositions, communicative dining/ordering, and greetings.
  - Part 2 Writing Task: *Un día en mi vida* (min. 30 words with daily routine reflexives & preferences).
  - Part 3 Speaking Task: *Presentación personal* (min. 15s oral introduction).
- [x] **Update `content/es/tests/a2-test.json`**:
  - 24 varied questions testing Pretérito Perfecto, Imperfecto morphology & narrative contrast, Imperativo (tú/formal, affirmative/negative, clitic placement), indirect objects, Condicional de cortesía, Subjuntivo presente, and direction giving.
  - Part 2 Writing Task: *Un fin de semana inolvidable* (min. 45 words contrasting narrative pasts and giving recommendations).
  - Part 3 Speaking Task: *Mensaje de voz con recomendaciones* (min. 20s voice message with practical travel advice).
- [x] **Update `content/hu/tests/a1-test.json`**:
  - 26 varied questions testing basic conjugation, Origin cases (*-ból/-ből*), Essive-modal language case (*-ul/-ül*), spatial/temporal postpositions (*előtt/után/mellett*), *szeret* + infinitive, indefinite conjugations, and public greetings/shopping.
  - Part 2 Writing Task: *Magyarul tanulok* (min. 25 words introducing languages and daily habits).
  - Part 3 Speaking Task: *Bemutatkozás élőszóban* (min. 15s oral introduction).
- [x] **Create `content/hu/tests/a2-test.json`**:
  - 26 varied questions testing inflected personal pronouns (*nálam, hozzánk, vele, nekem*), Translative-Factitive assimilation (*-vá/-vé, orvossá*), Essive-Formal (*-ként*), deferential *tetszik*, preverbs aspect & word order, definite vs indefinite conjugations, past tense, and cultural Name Day (*Névnap*) greetings & hospitality formulas.
  - Part 2 Writing Task: *Köszönőlevél vendéglátásért vagy meghívó* (min. 40 words with inflected pronouns and gratitude).
  - Part 3 Speaking Task: *Névnapi köszöntő és programajánló* (min. 20s spoken greeting and invitation).
- [x] **Create `content/hu/tests/b1-test.json`**:
  - 28 varied questions testing conditional mood (present/past *volna*), participles (*-ó/-ő, -t/-tt, -andó/-endő, -va/-ve, -ván/-vén*), potential suffix (*-hat/-het*), causative & frequentative morphology (*-tat/-tet, -ogat/-eget*), reflexive verbs (*-kodik*), complex connectors (*bár, noha, holott*), indirect speech & indirect question particle (*-e*), preverb inversion & auxiliaries, and citizenship & administrative topics.
  - Part 2 Writing Task: *Hivatalos megkeresés és javaslattétel* (min. 60 words formal proposal/enquiry with conditional forms and connectors).
  - Part 3 Speaking Task: *Állásinterjú vagy szakmai tervek bemutatása* (min. 30s spoken career overview and future plans).

---

## 💡 Strategic & Product Ideas [TO-BE-DONE LATER]

*Most of these are product/design-level ideas. No priority order — capture for future sprints.*

- [ ] **Reverse-engineer competitor apps for feature ideas** — systematically audit apps like Duolingo, Babbel, Clozemaster, Conjuguemos, Busuu etc. for UX patterns, exercise types, and engagement hooks worth adapting.
- [ ] **Listening Lab — extended audio-passage comprehension** — the existing Listening Driller (`engine/drills/listening.js`) is single-sentence/TTS-based only; this is a longer-form mode adapting the Conjuguemos model for paragraphs and short dialogues at A2–B1, not a from-scratch listening feature.
- [ ] **Cyberpunk hero page load animation** — on page load, the hero section "powers up" element by element (think a machine booting, cyberpunk aesthetic). Stagger reveals of logo, tagline, CTA buttons, stat cards, etc.
- [ ] **User-configurable feature visibility (especially Workshop)** — let users choose which modules/features are shown in their dashboard. Too many options at once creates friction; a simple onboarding toggle or settings page can hide unused sections.
- [ ] **IP / attribution audit for content-engine resources** — review all third-party content used (word lists, texts, images, audio). Where Creative Commons material is used, add a dedicated acknowledgments page or footer alongside AI-use disclosure.
- [ ] **Language expansion roadmap** — finish Spanish & Hungarian content → V4 release milestone → Eastern European languages (e.g. Polish, Czech, Romanian) → Vietnamese.
