# B2 test review (es-latam/tests/b2-test.json)

Screens opened for every `teaches` slug that carried a doubt (no-es-que, por-mas-que, aun-cuando, si-bien, consecutivas, cortesia, deber, contrast, hendida, reproches, quienquiera, se-impersonal, mixed, hubiera-sin-si, antes/despues, saber/supe, el-hecho, de+infinitivo, estar+participio, voseo).

## Defects

### 1. b2-por-mas-que: wrong option "insistes" is accepted Spanish
Screen b2-08-03-a-gr says the indicative is read when the effort really happens ("Por más que insistió, no consiguió nada"), subjunctive "when you look ahead or speak in general". DPD/NGLE accept *por más que* + indicative for a known, real fact: "Por más que insistes, no voy a cambiar de idea" (you are insisting now) is natural. The sentence has no cue that rules out a present indicative. Make the wrong option clearly wrong by pointing to the future and using a past form.
- Sentence: old `"sentence": "Por más que _____, no voy a cambiar de idea."` new `"sentence": "Por más que _____ mañana, no voy a cambiar de idea."`
- Option: old `"insistes",` new `"insististe",`
(Result: insistas / insististe / insistirás / insistieras; "insistieras" is also off with "no voy a", fine as a distractor.)

### 2. b2-aun-cuando: wrong option "llueve" is arguably accepted
Screen b2-08-04-a-gr: aun cuando follows the aunque rule, indicative for a fact, subjunctive for a possibility. "El museo abrirá el domingo aun cuando llueve" can be read as a habitual/known fact (it rains there often; the museum opens anyway), which the norm accepts. Not clearly wrong. Replace with a past form that cannot fit a future main clause.
- old `"llueve",` new `"llovió",`

### 3. ls-b2-06: evidence is not the transcript word for word
Transcript line: "Ahora bien, el perro va a echar de menos el jardín." The evidence is a paraphrase plus a quote.
- old `"evidence": "La conversación no lo dice; solo que el perro va a echar de menos el jardín."` new `"evidence": "Ahora bien, el perro va a echar de menos el jardín."`

### 4. ls-b2-01 and ls-b2-03: evidence differs from the transcript in the first letter's case
Transcript has "pasaba casi dos horas al día en el tráfico" and "vamos a buscar una que esté cerca del nuevo apartamento" (mid-sentence, lower case). Only matters if the check is exact string search.
- old `"evidence": "Pasaba casi dos horas al día en el tráfico."` new `"evidence": "pasaba casi dos horas al día en el tráfico."`
- old `"evidence": "Vamos a buscar una que esté cerca del nuevo apartamento."` new `"evidence": "vamos a buscar una que esté cerca del nuevo apartamento."`

### 5. speakingTask targetKeywords: too narrow for the prompt (low)
The prompt asks for what "habría cambiado" and what "deberías haber hecho". A good answer may use "debí haber", "tendría que haber", "habría". Current list leans on "ojalá" (not requested in the prompt) and "ahora". Add forms the prompt invites.
- old `"debería haber",` new `"debería haber",\n      "tendría que haber",\n      "habría",`
(Indent to match the file; line 500.)

## Noted, not changed (your call)
- b2-no-es-que, option "quiero": the screen teaches subjunctive after "no es que"; the indicative is attested colloquially but the norm (DPD, NGLE) prefers the subjunctive. Kept as a valid wrong option; I judge it safe at the screen's strength.
- b2-deber, option "debemos de": the screen itself says books call it a mistake while speakers mix it; DPD censures *deber de* for duty. Valid at the screen's strength.
- b2-se-impersonal, "buscan": screen calls it a common mistake; widespread but non-normative. Valid.
- Weak distractors, nonsense forms no learner would pick: b2-reproche ("deberías habiendo", "deberías hubiera"), b2-volver-a ("otra vez"), b2-ir-gerundio ("estoy a", "ando a"), b2-quienquiera ("Dondequiera"). Not defects of correctness; they lower discrimination.
- Region: "apartamento", "escuela", "sueldos" read fine in Spain too (piso/colegio more usual there but understood). No real-world facts stated.

## Checked, no defect
b2-hendida, b2-saber-supe, b2-imperfecto-cortesia, b2-que-subjuntivo, b2-no-es-que, b2-el-hecho, b2-antes-de-que, b2-despues-de-que, b2-si-bien, b2-reduplicado, b2-reproche, b2-de-infinitivo, b2-hubiera-sin-si, b2-mixta, b2-relativa-subjuntivo, b2-quienquiera, b2-como-si, b2-ojala-pasado, b2-pregunta-indirecta, b2-se-impersonal, b2-estar-participio, b2-volver-a, b2-ir-gerundio, b2-dar-por, b2-deber, b2-haber-de, b2-consecutiva, b2-al-contrario, b2-voseo; rs-b2-01 to rs-b2-06 (passage, answers and TFNS values correct); ls-b2-02, ls-b2-04, ls-b2-05 (evidence exact); writingTask (task and keywords fine).
