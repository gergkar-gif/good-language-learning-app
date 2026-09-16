# Parlour CEFR Curriculum Roadmap

**Status**: Phase 1 (Spanish A1 Core Gaps) **COMPLETED** ✅  
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

## ⏳ Phase 3: Spanish A2 — Imperativo & Clitic Pronouns [TO-BE-DONE LATER]

- [ ] **Unit 3.1: Imperativo I — Affirmative Commands (`unit.a2.imperativo1`)**
  - **Focus**: Regular *tú* imperatives (3rd person present), the 8 irregular *tú* imperatives (*ven, pon, sal, di, ten, haz, ve, sé*), formal *usted/ustedes* imperatives.
  - **Context**: Directions in a city, recipes, step-by-step instructions.
  - **Story**: *Las instrucciones de la abuela*.
- [ ] **Unit 3.2: Imperativo II — Negative Commands & Clitic Attachment (`unit.a2.imperativo2`)**
  - **Focus**: Negative *tú* commands (*no hables, no comas*), pronoun attachment to affirmative commands (*dime, siéntate, ponlo*) vs. placement before negative commands (*no me digas, no te sientes*). Accent shifts (*dímelo*).
  - **Story**: *Las reglas del hostel*.
- [ ] **Unit 3.3: Indirect Object & Combined Clitic Pronouns (`unit.a2.clitics`)**
  - **Focus**: Indirect object pronouns (*me, te, le, nos, les*) with verbs like *dar, decir, preguntar*, and combined double-object clitics (*se lo dije*, *le → se* rule).

---

## ⏳ Phase 4: Spanish A2 — Modality, Subjunctive & Pragmatics [TO-BE-DONE LATER]

- [ ] **Unit 4.1: Condicional Simple — Politeness & Advice (`unit.a2.condicional`)**
  - **Focus**: *-ría* endings for polite service requests (*me gustaría, ¿podría usted...?*) and giving advice (*deberías descansar, yo que tú tomaría agua*).
- [ ] **Unit 4.2: Presente de Subjuntivo — Desires & Feelings (`unit.a2.subjuntivo`)**
  - **Focus**: Introductory triggers at A2: desires (*quiero que vengas*), impersonal expressions (*es importante que estudies*), future time with *cuando* (*cuando llegues, llámame*).
- [ ] **Unit 4.3: Verbal Periphrases & Discourse Connectors (`unit.a2.periphrases`)**
  - **Focus**: *seguir + gerundio* (continuation), *empezar a + inf* (inception), *dejar de + inf* (cessation), connectors (*sin embargo, por lo tanto, aunque, además*).
- [ ] **Unit 4.4: Thematic Domain — Education & Schooling (`unit.a2.education`)**
  - **Focus**: School subjects, university, classroom items, studying and learning vocabulary.

---

## ⏳ Phase 5: Hungarian A1 — Core Case Integrations [TO-BE-DONE LATER]

- [ ] **Unit 5.1: Hungarian Elative (*-ból/-ből*) & Delative (*-ról/-ről*) Consolidation**
  - **Focus**: Spatial origin cases: coming out of places (*a szobából*), coming off / speaking about (*Budapestről, a munkáról beszélünk*).
- [ ] **Unit 5.2: Hungarian Essive-Modal (*-ul/-ül*)**
  - **Focus**: Language adverbials (*magyarul, angolul, spanyolul*) with explicit vowel harmony rules.
- [ ] **Unit 5.3: Postpositions (*alatt, felett, mellett, előtt, után*)**
  - **Focus**: Core spatial and temporal postpositions used with bare nominative nouns.

---

## ⏳ Phase 6: Hungarian A2 — Inflected Personal Pronouns [TO-BE-DONE LATER]

- [ ] **Unit 6.1: Inflected Personal Pronouns I — Internal & External Cases (`unit.hu.pronouns1`)**
  - **Focus**: Inessive (*bennem, benned, benne, bennünk, bennetek, bennük*), Superessive (*rajtam, rajtad, rajta, rajtunk, rajtatok, rajtuk*), Sublative (*rám, rád, rá, ránk, rátok, rájuk*).
- [ ] **Unit 6.2: Inflected Personal Pronouns II — Approach & Proximity Cases (`unit.hu.pronouns2`)**
  - **Focus**: Adessive (*nálam, nálad, nála, nálunk, nálatok, náluk* — "at my place"), Allative (*hozzám, hozzád, hozzá, hozzánk, hozzátok, hozzájuk* — "coming to me"), Ablative (*tőlem, tőled, tőle, tőlünk, tőletek, tőlük* — "from me").

---

## ⏳ Phase 7: Hungarian A2 — Advanced Grammar & Culture [TO-BE-DONE LATER]

- [ ] **Unit 7.1: Change-of-State Cases (*-vá/-vé* Translative-Factitive)**
  - **Focus**: *orvossá válik* (becomes a doctor), *széppé teszi* (makes it beautiful).
- [ ] **Unit 7.2: Role / Capacity Case (*-ként* Essive-Formal)**
  - **Focus**: *tanárként dolgozom* (I work as a teacher).
- [ ] **Unit 7.3: Sociocultural Pragmatics (*Tetszikelés* & Hungarian Customs)**
  - **Focus**: Deferential polite construction (*Hogy tetszik lenni?*), Hungarian Eastern name order (*Kovács Péter*), Name Days (*Névnap*), toasting etiquette (*Egészségedre!*).

---

## ⏳ Phase 8: Comprehensive CEFR Assessment Tests [TO-BE-DONE LATER]

- [ ] Update `content/es/tests/a1-test.json`: Add questions testing `gustar`, reflexives, demonstratives, continuous, `doler`, and `poder/saber`.
- [ ] Update `content/es/tests/a2-test.json`: Add questions testing Imperfecto, Imperativo, Indirect Objects, Conditional, and Subjunctive.
- [ ] Update `content/hu/tests/a1-test.json` & `a2-test.json`: Align questions with newly integrated case paradigms.

---

## 💡 Strategic & Product Ideas [TO-BE-DONE LATER]

*Most of these are product/design-level ideas. No priority order — capture for future sprints.*

- [ ] **Reverse-engineer competitor apps for feature ideas** — systematically audit apps like Duolingo, Babbel, Clozemaster, Conjuguemos, Busuu etc. for UX patterns, exercise types, and engagement hooks worth adapting.
- [ ] **Listening Lab — extended audio-passage comprehension** — the existing Listening Driller (`engine/drills/listening.js`) is single-sentence/TTS-based only; this is a longer-form mode adapting the Conjuguemos model for paragraphs and short dialogues at A2–B1, not a from-scratch listening feature.
- [ ] **Cyberpunk hero page load animation** — on page load, the hero section "powers up" element by element (think a machine booting, cyberpunk aesthetic). Stagger reveals of logo, tagline, CTA buttons, stat cards, etc.
- [ ] **User-configurable feature visibility (especially Workshop)** — let users choose which modules/features are shown in their dashboard. Too many options at once creates friction; a simple onboarding toggle or settings page can hide unused sections.
- [ ] **IP / attribution audit for content-engine resources** — review all third-party content used (word lists, texts, images, audio). Where Creative Commons material is used, add a dedicated acknowledgments page or footer alongside AI-use disclosure.
- [ ] **Language expansion roadmap** — finish Spanish & Hungarian content → V4 release milestone → Eastern European languages (e.g. Polish, Czech, Romanian) → Vietnamese.
