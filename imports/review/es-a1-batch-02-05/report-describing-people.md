# Review report: es-es A1 Unit 4 describing-people and Unit 5 family

Fix files: fixes-describing-people.json (48 fixes), fixes-family.json (30). Challenges: challenges-describing-people.json, challenges-family.json (6 each). I applied both fix lists to a scratch copy: all fixes apply, check-content gives 0 errors for both units (Unit 5 keeps 2 consolidation-copy suspects, left alone as instructed). The audit found no "literal compound guess" or "not in the dictionary" words for a1-21 (lesson a1-03c-05's story) or a1-05, so group 5 is empty.

## UNIT 4 describing-people

### 1. Found by reading
- a1-03c-01-g03, a1-03c-02-g02, a1-03c-02-g03, a1-03c-03-g02, a1-03c-03-g03, a1-03c-04-g02, a1-03c-04-g03: blanks glued to a stem ("simpátic__", "trabajad__", "rubi__", "jóven__", "amabl__"). 03-g03 even prints the misspelling "jóven". Fix: blank the whole word ("Meg es ____." plus a hint naming the masculine base, e.g. "simpático"); where "friendly" also fits amable, `answers` lists both.
- a1-03c-01-g02, 05-g02, 05-g03, c-g03, c-g04, c-g06: `english` pins one adjective ("Ana is young.") but 6 to 7 answers are accepted. Fix: `answers` limited to the one the English fits (friendly: simpáticos or amables).
- a1-03c-01-d01: wrong option "Tiene treinta años." uses unmet tener, treinta, años (numbers are a1-10-02). It also fails the same way as "Es de Hungría." Fix: options "Es joven y simpática." / "Es de Hungría." / "Es joven y simpático.", teaches adjective-agreement.
- a1-03c-01-d03: "Carlos: ¿Cómo es Meg? / Meg: Es simpática." Meg answers about herself in the third person. Fix: "Ana: ¿Cómo es Meg? / Carlos: _____".
- a1-03c-03-d01: "Meg: ¿Cómo son Ana y Meg?" Meg asks about herself in the third person. Fix: asker is Lauren.
- a1-03c-02-d03: "Meg: ¿Cómo es Carlos? / Carlos: Soy trabajador." Carlos is asked in the third person and answers in the first. "Somos trabajadores." is unmet and fails differently. Fix: "Meg: ¿Cómo eres, Carlos?" with Soy trabajador. / Soy trabajadora. / Soy trabajadores.
- a1-03c-01-g07: option "Andreas es baja." fails agreement, not ser, so the item tests two skills. Fix: "Andreas eres bajo."
- a1-03c-02-d01: "Es divertido y amables." has two faults (gender and number). Fix: "Es divertido y amable."
- a1-03c-02-v03: length-giveaway ERROR (10 vs 6). Fix: options trabajador / divertido / simpático.
- a1-03c-03-v04: "Which word means good-looking?" offers bonito ("pretty / nice"), a near-synonym, so two answers fit. Fix: replace with pequeño.
- a1-03c-c-d02 and a1-03c-c-d04 (suspect *húngaro*): "Soy húngaro alto." has two faults; "Es húngaro de." is a non-word. Fix: "Soy en Hungría." and "Es en Hungría." (same fault as c-g05).
- a1-03c-05-r01: "Who is Daniela? A Spanish teacher." The story a1-21 never says that (the man next to her is the teacher). Fix: "What is Daniela like?" with Tall, young and friendly.
- a1-03c-05-r02: "Who is described as calm and organized?" Nobody is. Fix: "Who is described as funny and sociable?" (Lauren).
- a1-03c-05-r03: "Who does Meg describe? Her sisters" Meg also describes Daniela and the teacher. Fix: "Who are Lauren and Kaylee?"
- a1-03c-05-r04: "What does Kaylee do? She talks a lot and jokes." The story says she is shy. Fix: "What is Kaylee like?" with Shy, with a lovely smile.
- a1-03c-05-g06: "Meg y Daniela son ____ (older)." English inside the Spanish line (check-content missed the trailing bracket). It also contradicts the story, where Daniela is "joven". Fix: "El profesor es un hombre ____." with `english` "The teacher is an older man."; options mayor / mayora / mayores.
- a1-03c-05-d01: Carlos is asked about Meg's family and answers; "la mujer rubia" fits both Lauren and Kaylee; "Es un hombre." is ruled out by the prompt. Fix: "Carlos: ¿Quién es la mujer alta y joven? / Meg: Es Daniela." with Son Daniela. / Soy Daniela. as wrong options.
- a1-03c-05-d03: "Meg: Es una mujer seria." about Daniela, but the story says simpática and amable. Fix: "Es una mujer alta." and its wrong options.
- Open structured-writing prompts with one fixed answer, unguessable from the prompt: a1-03c-01-w01, 01-w02, 02-w01, 02-w02 ("Describe a woman with a feminine adjective." for "Lauren es divertida."), 03-w01, 03-w02, 04-w01, 05-w01. Fix: each prompt pins the sentence ("Say that Lauren is funny."). a1-03c-c-w01 and c-w02 ask "Say your name" and "Say where you are from" but the answers are Carlos's and Meg's. Fix: "Say that your name is Carlos.", "Say that you are from South Africa."
- Grammar screens present known material as new: a1-03c-01 ("Use ser + an adjective…", tip "Gender and plural agreement are the focus of the next lessons"), 03c-02 (gender agreement, taught in a1-03-04) and 03c-03 (the plural -s rule). Fix: open with "You know … from Unit 3" and recap wording.
- a1-03c-03 grammar: *jóvenes* gains an accent without explanation, and the rule does not cover *trabajadores* (needed by c-g04). Fix: the rule now says *joven* or *trabajador* take *-es* and *jóvenes* adds an accent to keep the stress.

### 2. Metadata
- a1-03c-01-d01: `teaches` changed to adjective-agreement (the options now differ in gender).
- Check by hand (not wrong, see group 4): a1-03c-02-d01, d04, 01-d03 use "Son …" wrong options in agreement-tagged items; those faults are the verb's number, not adjective agreement.
- a1-03c-05-g06 (rewritten): `teaches` plural → adjective-agreement; a1-03c-05-d01: `teaches` → ser.
- All fill-blank items rewritten above keep their `teaches`.

### 3. Goals / checklists
- a1-03c-consolidation (check-content ERROR checklist-shared): "I can use articles with familiar nouns." is also in a1-03-consolidation. Fix: "I can use un and una with words for people." (goal and checklist; it is also the challenge canDo).
- a1-03c-05: first line "I can describe someone's appearance and personality." is a near-duplicate of a1-03c-01's "…appearance or personality." Fix: "I can describe a person with two or more adjectives." (goal and checklist).
- a1-03c-05 goal "appearance": *pelo* and *ojos* are listed but never practised beyond the vocabulary items (see group 4).

### 4. Doubtful
- a1-03c-c-d03 is an exact copy of a1-03c-04-d03 (same prompt, same options). Left alone as a consolidation copy (6a says vary the words) (unsure).
- a1-03c-c-v01 matches "Carlos" with "Carlos" (a name to itself); left alone (character name).
- a1-03c-01 vocabulary re-lists five words from Unit 3 (alto, bajo, joven, simpático, serio), and 03c-02, 03c-03 re-list amable, trabajador, guapo, pequeño. Parked, not a defect, but lesson 01 teaches nothing new in vocabulary.
- Items with "Son …" wrong options in lessons tagged adjective-agreement (01-d03, 02-d01, 02-d02, 02-d04, 04-g04): they break the verb's number as well as the tested skill. Not fixed (unsure).
- Several lessons have 3 or more "X es ____." items of the same shape (01: g01, g05, g06; 02: g01, g05, g06; 03: g01, g07; 04: g01, g05, g06). Not fixed.
- a1-03c-05-d01 and the others use *Son Daniela* / *Soy Daniela* as person faults; both fail the same way (unsure).
- a1-03a/a1-03 story note: in story a1-03 Daniela's `narration.speakers` entry says gender "male" although she is a woman; this may give her a male voice (not in my units, outside my files, unsure).
- Structured-writing is graded against one stored answer; I pinned each prompt but did not check the grader's tolerance (unsure).
- The Lingolia external-link lines sit on 5 screens with the same URL; left alone.
- No past tense, no numbers beyond treinta (fixed), no gusta, no regular verb conjugation, no vosotros in Unit 4. Nothing needed `variant`.

### 5. Dictionary
(none: the audit of a1-21, the story inside a1-03c-05, reports 0 "literal compound guess" and 0 "not in the dictionary")

## UNIT 5 family

### 1. Found by reading
- a1.05.05.ex14/ex15/ex16: the reading questions do not match story a1-05. ex14 "con quién habla Carlos por videollamada" and ex15 "la videollamada con la madre de Carlos… Su padre, Andreas y Ana" invent a video call; ex16 makes "Que es muy amable" correct, but Meg says "divertida y unida". They also drew the unmet-word suspects *trabajo* and *solo*. Fix: "¿cuántos hermanos tiene Carlos?" (Un hermano y una hermana.), "¿cómo es el padre de Carlos?" (Tranquilo y amable.), "Que es muy divertida."
- a1.05.02 grammar: second section "Introducing someone: *este* / *esta*" teaches the demonstratives (A1 Unit 10, `demonstratives` later) as new. The same chunk "Esta es mi madre" is in a1-05-03 grammar and speaking, a1-05-05 grammar and speaking, and the writing items a1.05.02.ex15, a1.05.05.ex18, ex19 and consolidation ex17. Fix: recap *él es* / *ella es* from Unit 2 plus a possessive ("Ella es mi madre", "Él es mi padre") everywhere, with the writing prompts pinned ("Say that she is your mother.").
- a1.05.02.ex09: "__ padres viven en Hungría." *viven* is regular -ir conjugation (Unit 6). Fix: "__ padres son de Hungría. (yo)".
- a1.05.05.ex05: "__ padres están juntos en la foto." *están* is estar (Unit 8). Fix: "__ padres tienen una foto juntos. (tú)".
- a1.05.01.ex10: "Mi padre __ dos hijos." and ex12 "¿Cuántos hijos tiene tu madre?" use mi and tu before a1-05-02. ex12's answer "Tiene dos hijos" also contradicts the story (Carlos's mother has three children). Fix: ex10 "Meg __ dos hermanas."; ex12 "Meg: ¿Cuántos hermanos tienes? / Carlos: Tengo dos hermanos." (a brother and a sister).
- a1.05.01.ex06: "Carlos y Ana __ tres hijos." Carlos has no children in the story. Fix: "Ana y Andreas …".
- a1.05.05.ex04: "Tengo dos __. (brothers)" English inside the Spanish line. Fix: "Carlos tiene un hermano y una hermana. Tiene dos __." (hermanos / hermanas / familia).
- a1.05.05.ex03: length-giveaway ERROR (9 vs 5). Fix: options presentar / conocer / familia.
- a1.05.consolidation.ex10: "__ padre es húngaro." unmet *húngaro*. Fix: "__ padre es de Hungría."
- a1.05.consolidation.ex14: "¿Cómo se llama tu madre? / Se llama Ana." reflexive *llamarse* (Unit 6, suspect *llama*). Fix: "Carlos: ¿Quién es Daniela? / Meg: Es mi amiga." (Soy mi amiga. / Tengo mi amiga.).
- a1.05.03.ex10: matching "su esposa" = "his / her wife" is wrong English. Fix: "his wife".
- a1.05.03.ex15: "Say that your cousin is kind." → "Mi primo es amable.": primo and prima both fit. Fix: "your male cousin".
- a1.05.05 grammar: "Es mi …" glossed "This is my…" (it is "He / she is my…"); example "Tengo dos hermanos. Mi hermano es joven." is incoherent (two brothers, then "my brother"), and it is also the first speaking line and the old lesson challenge. Fix: "Tengo un hermano. Mi hermano es joven."
- a1.05.04 grammar presents *ser* + adjective agreement as new (A1 Units 3–4). Fix: opens "You know … from Units 1 to 4".
- Numbers: *dos* is listed only at a1-08-02 and *tres* in no vocabulary list, yet both are used from a1-05-01 (ex04, ex05, ex06, ex08, ex10, ex15…, a1.05.consolidation.ex05, ex11, grammar examples). Fix: add dos and tres to the a1-05-01 vocabulary (unsure: the alternative is to replace every use with un/una; I judged counting siblings essential). No ages or larger numbers occur in the unit.

### 2. Metadata
- a1.05.consolidation.ex14: `teaches` → a1-family-vocab (it was a1-greetings-introductions-vocab for a question now about family vocabulary).
- a1.05.05.ex10 "I have two sisters": wrong option "Tengo dos hermanos." fails by noun meaning, not by the tener form the item is tagged with (unsure, not changed).
- a1.05.03.ex07 (Tú / Tu / Su, `subject-pronouns`): "Tu" is a well-formed possessive but the sentence "¿Tu tienes hermanos?" is ungrammatical, so I added no `distractor_skills` (unsure).
- `distractor_skills` on a1.05.05.ex06 and consolidation ex03, ex06, ex15 mark an ungrammatical sentence ("Mis padres tiene …") (unsure, left).

### 3. Goals / checklists
- No check-content findings. Goal wording "retrieve family vocabulary and grammar" (consolidation, also its canDo) is vague but unique.

### 4. Doubtful
- Story a1-05, line "¿Y quiénes son los abuelos del jardín?": no garden is set, unnatural. Proposed "¿Y quiénes son los abuelos?" (the audio narration would need regenerating, so not put in the fixes) (unsure).
- Vocabulary: "hijo = son", but *hijos* ("children") is used in the lesson 01 examples and in 03 exercises. Fix proposed: gloss "son / child" (unsure).
- a1.05.consolidation speaking steps: read-repeat and prompt-speak both say "Yo tengo dos hermanos." (same sentence twice, from ex05). Not fixed: speaking is engine-generated (unsure).
- Two consolidation-copy suspects (consolidation ex04 = 02.ex03, ex05 = 01.ex04) left as instructed.
- Vocabulary re-listing (madre, padre, hermano, hermana, familia, foto, presentar, amable, divertido) is parked.
- The `vosotros` items (01-ex16, tener table) are fine in es-es; none of my fixes is es-es specific, so no `variant` keys. es-latam gets the same fixes (it has no vosotros item to mirror).
- a1.05.01 ex15 and ex17 "Nosotros __ …" fine. No past tenses, gusta, or ages found.
- Hint lines like "Meg answers about her own grandmother" are English in `hint` (allowed).

### 5. Dictionary
(none: the audit of a1-05 reports 0 "literal compound guess" and 0 "not in the dictionary")
