// Unit test: what an exercise says aloud once settled (engine/exercise-audio.js,
// ROADMAP 122). Cases are real exercises from the content audit.

const assert = require('assert');
const A = require('../../engine/exercise-audio.js');

// Fill-blank: the whole sentence, hints and glosses gone.
assert.strictEqual(A.fillBlank('A Carlos le ___ (gustar) leer.', 'gusta', 'es'), 'A Carlos le gusta leer.');
assert.strictEqual(A.fillBlank('Necesitamos una ___ eficaz. (solución) [We need an effective solution.]', 'solución', 'es'),
    'Necesitamos una solución eficaz.');
assert.strictEqual(A.fillBlank('____ nem tudok jönni. (unfortunately)', 'Sajnos', 'hu'), 'Sajnos nem tudok jönni.');
// A suffix blank fills in place.
assert.strictEqual(A.fillBlank('Az emberi méltóság érték az alkotmányunk_____. (in our constitution)', 'ban', 'hu'),
    'Az emberi méltóság érték az alkotmányunkban.');
// An English lead-in is dropped.
assert.strictEqual(A.fillBlank('Complete the greeting: Buenos ___.', 'días', 'es'), 'Buenos días.');
assert.strictEqual(A.fillBlank('Complete: ¿De dónde ___?', 'eres', 'es'), '¿De dónde eres?');
// "He" and "has" are Spanish here, not English.
assert.strictEqual(A.fillBlank('¿Has __ bien? (llegar)', 'llegado', 'es'), '¿Has llegado bien?');
// Two blanks, one answer: silent.
assert.strictEqual(A.fillBlank('A hunok birodalma gyorsan ___. (collapsed) _____', 'összeomlott', 'hu'), '');

// Choice: the target-language answer, or the completed sentence.
assert.strictEqual(A.forChoice('Nosotros nos __ a las once de la noche.', 'acostamos', 'es'),
    'Nosotros nos acostamos a las once de la noche.');
assert.strictEqual(A.forChoice('A friend calls and asks: "¿Dónde estás?" You answer: "__ de mi casa."', 'Estoy saliendo', 'es'),
    'Estoy saliendo de mi casa.');
assert.strictEqual(A.forChoice('Which means “fourth”?', 'negyedik', 'hu'), 'negyedik');
assert.strictEqual(A.forChoice('Ki volt az utolsó Árpád-házi király?', 'III. András.', 'hu'), 'III. András.');
// English answer: say the target word the question asks about.
assert.strictEqual(A.forChoice('¿Qué significa "paciente"?', 'patient', 'es'), 'paciente');
assert.strictEqual(A.forChoice('What does *acostarse* mean?', 'to go to bed', 'es'), 'acostarse');
assert.strictEqual(A.forChoice('¿Qué significa en inglés el término «Castilla y León»?', 'Castile and León', 'es'), 'Castilla y León');
// English answers and explanations stay silent, even when they quote target words.
assert.strictEqual(A.forChoice('Who does Ana meet for coffee?', 'Her friend Marta.', 'es'), '');
assert.strictEqual(A.forChoice("Why is 'csoportonként' preferred in: 'A diákokat ____ értékelték'?",
    'Because the distributive suffix -onként conveys evaluation broken down cohort by cohort.', 'hu'), '');
assert.strictEqual(A.forChoice('Which of the following is NOT followed by a case suffix?', 'nouns followed by postpositions', 'hu'), '');
// A bare suffix isn't a word.
assert.strictEqual(A.forChoice('Which ending goes with «nosotros»?', '-emos', 'es'), '');

console.log('exercise-audio: all assertions passed');
