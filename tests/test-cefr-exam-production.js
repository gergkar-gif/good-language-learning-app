// CEFR mock exams: offline writing/speaking marks give nothing for empty,
// padded, copied or English answers, and full marks are still reachable.
const assert = require('assert');
global.localStorage = { _d: {}, getItem(k) { return this._d[k] || null; }, setItem(k, v) { this._d[k] = String(v); }, removeItem(k) { delete this._d[k]; } };
global.Lang = { current: () => 'es', code: () => 'es-es', key: k => 'test_' + k, content: p => p };
global.document = { getElementById: () => null, querySelector: () => null, querySelectorAll: () => [] };

const CefrExam = require('../engine/cefr-exam.js');
const exam = require('../content/es-es/dele-a2-exam.json');
const h = CefrExam.DeleA2Exam._testHooks;
const wt = exam.skills.writing.tareas[0];
const st = exam.skills.speaking.tareas[0];

assert.strictEqual(h.writing('', wt).totalScore, 0, 'empty writing scores 0');
assert.strictEqual(h.speaking('', st, 'blob:x').totalScore, 0, 'recording alone scores 0');
const padded = h.writing((wt.targetKeywords.join(' ') + ' y pero porque además ').repeat(15), wt);
assert(padded.totalScore <= 5, 'padded writing scores at most 5/25, got ' + padded.totalScore);
assert.strictEqual(h.writing(wt.prompt, wt).totalScore, 0, 'copied prompt scores 0');
const english = h.writing('I went to the beach with my friends and it was very nice because the weather was good. '.repeat(4), wt);
assert.strictEqual(english.totalScore, 0, 'English writing scores 0');

const genuine = 'Hola Marta:\n¿Qué tal estás? Te escribo porque el fin de semana pasado fui a Granada con mi familia. ' +
    'Hacía mucho calor, pero lo pasamos muy bien. Primero visitamos la Alhambra y después comimos en un restaurante pequeño del centro. ' +
    'Por la noche paseamos por el barrio del Albaicín, que me gustó muchísimo.\nAdemás, compré unos regalos para ti. ' +
    'Si quieres, podemos vernos el sábado y te enseño las fotos. Un abrazo, Pablo.';
const g = h.writing(genuine, wt);
assert(g.totalScore >= 15, 'genuine writing scores well, got ' + g.totalScore + ' ' + JSON.stringify(g.criteria));

// Official pass-rule checks: DELE 2-group (30/50 per group) & ECL 4-module (60% per module)
const deleFailGroup2 = h.evaluatePass({
    reading: { t1: { score: 10, maxScore: 10 } },
    writing: { t1: { score: 25, maxScore: 25 } },
    listening: { t1: { score: 4, maxScore: 10 } },
    speaking: { t1: { score: 10, maxScore: 25 } }
});
assert.strictEqual(deleFailGroup2.mode, 'dele-groups');
assert.strictEqual(deleFailGroup2.group1.passed, true, 'DELE Group 1 (50/50) passes');
assert.strictEqual(deleFailGroup2.group2.passed, false, 'DELE Group 2 (20/50) fails');
assert.strictEqual(deleFailGroup2.status, 'fail', 'DELE fails overall even when 4-skill avg is 70%');

const delePassBoth = h.evaluatePass({
    reading: { t1: { score: 8, maxScore: 10 } },
    writing: { t1: { score: 12, maxScore: 25 } }, // 20 + 12 = 32/50
    listening: { t1: { score: 6, maxScore: 10 } },
    speaking: { t1: { score: 15, maxScore: 25 } } // 15 + 15 = 30/50
});
assert.strictEqual(delePassBoth.status, 'pass', 'DELE passes when both groups >= 30/50');

const eclH = CefrExam.EclB1Exam._testHooks;
const eclFailOneMod = eclH.evaluatePass({
    reading: { t1: { score: 10, maxScore: 10 } },
    writing: { t1: { score: 25, maxScore: 25 } },
    listening: { t1: { score: 10, maxScore: 10 } },
    speaking: { t1: { score: 13, maxScore: 25 } } // 52% < 60%
});
assert.strictEqual(eclFailOneMod.mode, 'ecl-modular');
assert.strictEqual(eclFailOneMod.passedModules, 3);
assert.strictEqual(eclFailOneMod.status, 'fail', 'ECL fails complex pass when one module is below 60%');

const eclPassAll = eclH.evaluatePass({
    reading: { t1: { score: 6, maxScore: 10 } },
    writing: { t1: { score: 15, maxScore: 25 } },
    listening: { t1: { score: 6, maxScore: 10 } },
    speaking: { t1: { score: 15, maxScore: 25 } }
});
assert.strictEqual(eclPassAll.status, 'pass', 'ECL passes when all 4 modules >= 60%');

console.log('All CEFR exam production & pass-rule checks passed. (genuine: ' + g.totalScore + '/25)');
