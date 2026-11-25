// Level tests: writing and speaking are feedback, not marks, and the offline
// quick check cannot be bought by padding the answer with target phrases.
const assert = require('assert');
const path = require('path');

global.localStorage = {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = String(v); },
    removeItem(k) { delete this._data[k]; }
};
global.Lang = { current: () => 'es', code: () => 'es-es', key: k => 'test_' + k, content: p => p };
global.document = { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [] };

const Check = require('../engine/production-check.js');
const LevelTest = require('../engine/leveltest.js');
const a2 = require(path.join(__dirname, '..', 'content', 'es-es', 'tests', 'a2-test.json'));
const task = a2.writingTask;
const kw = task.targetKeywords;

// 1. Stuffing the target phrases earns nothing beyond the repeat cap.
const stuffed = Check.analyse((kw.join(' ') + ' ').repeat(12) + '.', task, { modality: 'written' });
assert(stuffed.effectiveWords <= kw.length * Check.MAX_REPEATS, 'repeats capped');
assert(stuffed.score <= 1, 'stuffed answer scores at most 1/3, got ' + stuffed.score);

// 2. Substrings are not matches: "era" is not in "primera", "sino" not in "casino".
assert.deepStrictEqual(Check.matchPhrases('la primera vez en el casino', ['era', 'sino']), []);
assert.deepStrictEqual(Check.matchPhrases('Cuando era niño, decidí...', ['era', 'decidí', 'cuando']), ['era', 'decidí', 'cuando']);
// Long targets may take an ending (Hungarian stems); short ones may not.
assert.deepStrictEqual(Check.matchPhrases('Sok tapasztalatom van, és kötelességünk segíteni.', ['tapasztalat', 'kötelesség', 'és']), ['tapasztalat', 'kötelesség', 'és']);
assert.deepStrictEqual(Check.matchPhrases('siempre sido', ['si']), []);

// 3. An English answer scores nothing.
const english = Check.analyse('I went to the beach with my friends and it was very nice because the weather was good and we were happy there for the whole weekend.', task, {});
assert(english.notTargetLanguage && english.score === 0, 'English answer scores 0');

// 4. Copying the test's own text does not count.
const copied = Check.analyse(a2.readingSection.passage, task, { sourceTexts: [a2.readingSection.passage] });
assert(copied.effectiveWords < 6 && copied.score === 0, 'copied passage scores 0, got ' + copied.score);

// 5. A genuine answer still gets full marks from the quick check.
const genuine = 'Hola Marta: el sábado fui a la sierra con mi hermano. Hacía sol y era un día perfecto. ' +
    'Mientras subíamos por el camino, vimos un ciervo enorme cerca del río. Después decidí bajar por otra ruta ' +
    'más tranquila. Si vas, te recomiendo salir temprano y llevar mucha agua. Un abrazo, Pablo.';
const g = Check.analyse(genuine, task, { sourceTexts: [a2.readingSection.passage, task.prompt] });
assert.strictEqual(g.score, 3, 'genuine answer 3/3, got ' + g.score + ' ' + JSON.stringify(g.notes));

// 6. The level-test score ignores writing and speaking entirely.
const allRight = {};
a2.questions.forEach(q => { allRight[q.id] = q.type === 'text-input' ? q.answer : q.options[q.correct]; });
const noProd = LevelTest._testHooks.markSitting(a2, { answers: allRight });
const gamed = LevelTest._testHooks.markSitting(a2, {
    answers: allRight,
    writing: (kw.join(' ') + ' ').repeat(20) + '.',
    speaking: (a2.speakingTask.targetKeywords.join(' ') + ' ').repeat(20)
});
assert.strictEqual(gamed.total, noProd.total, 'production adds nothing to the total');
assert.strictEqual(gamed.correct, noProd.correct, 'production adds nothing to the marks');
assert.strictEqual(gamed.total, a2.questions.length + a2.readingSection.questions.length + a2.listeningSection.questions.length);
assert.strictEqual(gamed.writing.counted, false);
assert.strictEqual(gamed.speaking.counted, false);

console.log('All level-test production checks passed.');
