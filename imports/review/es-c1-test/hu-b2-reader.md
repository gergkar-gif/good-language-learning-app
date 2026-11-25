# HU B2 test review (content/hu/tests/b2-test.json)

Defects (strings are copied from the file; the file is JSON, so each old string is unique in it).

## 1. hu-b2-mukodteto: second right answer (medium)
"Elvittem az autót a szerelőhöz, és ott megjavítottam." is grammatical and sensible (I fixed it myself at the garage), so "megjavítottam" is a second right answer. It is only pragmatically odd. b2-10-01-a-gr teaches -tat/-tet "has repaired", so the sentence must exclude the self-did reading.
Old: "sentence": "Elvittem az autót a szerelőhöz, és ott _____."
New: "sentence": "Nem értek az autókhoz, ezért elvittem a szerelőhöz, és ott _____ az autót."
Check: after the change "megjavítottam" contradicts the first clause and the wrong forms stay wrong. "megjavíttam" and "megjavítattam" are not standard (screen tip: double -tt-).

## 2. hu-b2-akkor-sem: ambiguous verb form (low to medium)
"hagyjuk el" is both 1pl definite indicative and the hortative ("let's leave"). So "A szülőföldünket akkor is hagyjuk el, ha nehézségekkel kell szembenéznünk" can be read as a grammatical hortative with its own meaning ("let us leave it even if..."). b2-27-01-a-gr teaches "sem" after a refusal. The item reuses the screen's own example, but the verb form lets "is" through. Use the screen's other example, whose verb has distinct indicative and subjunctive forms (mondunk / mondjunk).
Old: "sentence": "A szülőföldünket akkor _____ hagyjuk el, ha nehézségekkel kell szembenéznünk."
New: "sentence": "A szülőföldünkről akkor _____ mondunk le, ha a gazdasági válság elvándorlásra kényszerítene."
Caveat: "akkor is mondunk le" stays a grammatical additive sentence ("we also give up then"). I judge it wrong here only because the screen teaches "sem" for refusals and the sentence is a refusal frame. If you want it airtight, say so and the item should be made a choice item on meaning.

## 3. hu-b2-ikerszo: wrong option nobody picks (low)
"limotlomot" is a typo-like nonsense form, so it is not a real distractor. b2-34-01-a-gr's tip is that only the second element inflects. A real wrong form is the plural after "sok", which the standard rejects ("sok" takes the singular).
Old: "options": ["limlomot", "limlom", "limotlomot", "limlomnak"]
New: "options": ["limlomot", "limlom", "limlomokat", "limlomnak"]

## 4. ls-hu-b2-03: evidence not word for word (low)
The transcript has lowercase "az": "...mert az új iskola a folyó mentén van, és oda biciklivel járhat."
Old: "evidence": "Az új iskola a folyó mentén van, és oda biciklivel járhat."
New: "evidence": "az új iskola a folyó mentén van, és oda biciklivel járhat."

## 5. hu-b2-rovasara and hu-b2-szoros: real-world claim as fact (low, optional)
"A gyors iparosítás a mezőgazdaság rovására ment végbe, ezért sok falu elszegényedett." is a general historical claim stated as true, copied from the screen's example. "a lakások ára a kétszeresére nőtt" is similar but vague. If the no-real-world-claims rule is applied strictly, make the first one local:
Old: "A gyors iparosítás a mezőgazdaság _____ ment végbe, ezért sok falu elszegényedett."
New: "A kisváros fejlesztése a környező falvak _____ ment végbe, ezért sok falu elszegényedett."
Check: "rovására" still right. "javára", "szempontjából" and "érdekében" are still wrong, and "ezért" only fits the detriment reading.

## Notes, not defects
- Writing keyword "javára" is a bit unnatural for the task, but the other five are natural and the prompt names three. Speaking "annyira" and "mintha" are optional; "régen", "viszont" and "során" are enough for the two-keyword rule.
- rs-hu-b2-06 (not stated: the engineer still lives there): the text only says he lived there "gyerekkora óta" (past tense). Defensible as 2.
- ls-hu-b2-02: "Azonnal" appears only in a wrong option. It is mild and not worth changing.

## Checked, no defect
hu-b2-kontrasztiv-topik, hu-b2-fokusz, hu-b2-tagadas, hu-b2-igeneves-szerkezet, hu-b2-sag-seg, hu-b2-megengedo, hu-b2-gyakorito, hu-b2-kataforikus, hu-b2-hiszen, hu-b2-alany-nelkul, hu-b2-mindazonaltal, hu-b2-tul, hu-b2-soran, hu-b2-amely-mellett, hu-b2-meg-ha-is, hu-b2-beilleszkedik, hu-b2-celszeru, hu-b2-mintha, hu-b2-annyira-hogy, hu-b2-nem-mas-mint, hu-b2-mint-eset; rs-hu-b2-01 to 06; ls-hu-b2-01, 02, 04, 05, 06; hu-b2-writing; hu-b2-speaking. hu-b2-rovasara and hu-b2-szoros: only the optional note in point 5.
