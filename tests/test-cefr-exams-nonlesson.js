/**
 * Verifies CefrExam UI localization and exam JSON rendering for fr, it, pl, cs, sk.
 * Run: node tests/test-cefr-exams-nonlesson.js
 */
const assert = require('assert');
const fs = require('fs');

let currentLang = 'fr';
global.window = global;
global.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
global.document = {
    createElement: () => {
        let val = '';
        return {
            set textContent(s) {
                val = String(s == null ? '' : s)
                    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
            },
            get textContent() { return val; },
            get innerHTML() { return val; },
            set innerHTML(s) { val = s; },
            setAttribute() {},
            style: {}
        };
    },
    getElementById: () => null,
    addEventListener: () => {}
};
global.Lang = require('../engine/lang.js');
global.Lang.code = () => currentLang;
global.Lang.content = (p) => `content/${currentLang}/${p}`;
global.fetch = async (url) => {
    const clean = url.replace(/^\.\//, '');
    if (!fs.existsSync(clean)) return { ok: false, status: 404 };
    return { ok: true, status: 200, async json() { return JSON.parse(fs.readFileSync(clean, 'utf8')); } };
};

const CefrExam = require('../engine/cefr-exam.js');

function makeContainer() {
    const el = {
        innerHTML: '',
        querySelectorAll: () => [],
        querySelector: () => null
    };
    return el;
}

(async () => {
    const exams = [
        ['fr', CefrExam.DelfB1Exam, 'delf-b1-exam.json', 'Épreuves officielles'],
        ['it', CefrExam.CilsB1Exam, 'cils-b1-exam.json', 'Prove ufficiali'],
        ['pl', CefrExam.PlCertyfikatB1Exam, 'certyfikat-b1-exam.json', 'Zadania oficjalne'],
        ['cs', CefrExam.CsCceB1Exam, 'cce-b1-exam.json', 'Oficiální úlohy'],
        ['sk', CefrExam.SkEclB1Exam, 'ecl-b1-exam.json', 'Oficiálne úlohy']
    ];

    for (const [lang, mod, file, expectedTabLabel] of exams) {
        currentLang = lang;
        const raw = JSON.parse(fs.readFileSync(`content/${lang}/${file}`, 'utf8'));
        const c = makeContainer();
        await mod.render(c);

        assert(c.innerHTML.includes(expectedTabLabel), `${lang} expected "${expectedTabLabel}" tab label`);
        assert(!c.innerHTML.includes('[object Object]'), `${lang} hub contains [object Object]`);
        assert(!c.innerHTML.includes('Tareas oficiales'), `${lang} leaked Spanish UI string`);
        assert(!c.innerHTML.includes('Simulacro'), `${lang} leaked Spanish mock string`);

        // Structural contract check on every skill & tarea
        for (const sk of ['reading', 'listening', 'writing', 'speaking']) {
            const skill = raw.skills && raw.skills[sk];
            assert(skill && Array.isArray(skill.tareas) && skill.tareas.length > 0, `${lang} missing ${sk}.tareas`);
            for (const t of skill.tareas) {
                if (sk === 'reading') {
                    assert(['gapped-text', 'reading-mc', 'matching-notices', 'person-matching', 'cloze-mc'].includes(t.type), `${lang} bad reading type ${t.type}`);
                    for (const q of (t.questions || [])) {
                        assert(typeof q.question === 'string' && q.question, `${lang} ${t.id} missing question`);
                        assert(Array.isArray(q.options) && q.options.every(o => typeof o === 'string'), `${lang} ${t.id} non-string options`);
                        assert(Number.isInteger(q.correct) && q.correct >= 0 && q.correct < q.options.length, `${lang} ${t.id} bad correct`);
                    }
                }
                if (sk === 'listening') {
                    const list = t.items || t.questions || [];
                    assert(list.length > 0, `${lang} ${t.id} empty listening items/questions`);
                    if (t.items) {
                        for (const it of t.items) {
                            assert(it.audio && Array.isArray(it.audio.turns) && it.audio.turns.length > 0, `${lang} ${t.id}/${it.id} missing audio.turns`);
                            assert(typeof it.question === 'string' && it.question, `${lang} ${t.id}/${it.id} missing question`);
                            assert(Array.isArray(it.options) && it.options.every(o => typeof o === 'string'), `${lang} ${t.id}/${it.id} non-string options`);
                            assert(Number.isInteger(it.correct) && it.correct >= 0 && it.correct < it.options.length, `${lang} ${t.id}/${it.id} bad correct`);
                        }
                    } else {
                        assert(t.audio && Array.isArray(t.audio.turns) && t.audio.turns.length > 0, `${lang} ${t.id} missing audio.turns`);
                        for (const q of t.questions) {
                            assert(typeof q.question === 'string' && q.question, `${lang} ${t.id} missing question`);
                            assert(Array.isArray(q.options) && q.options.every(o => typeof o === 'string'), `${lang} ${t.id} non-string options`);
                            assert(Number.isInteger(q.correct) && q.correct >= 0 && q.correct < q.options.length, `${lang} ${t.id} bad correct`);
                        }
                    }
                }
                if (sk === 'writing') {
                    if (t.options) {
                        assert(Array.isArray(t.options) && t.options.length > 0 && t.options[0].optionLetter, `${lang} ${t.id} bad writing options`);
                    } else {
                        assert(typeof t.prompt === 'string' && t.prompt, `${lang} ${t.id} missing prompt`);
                    }
                    assert(t.maxWords, `${lang} ${t.id} missing maxWords`);
                }
                if (sk === 'speaking') {
                    assert(typeof t.prompt === 'string' && t.prompt, `${lang} ${t.id} missing prompt`);
                }
            }
        }
        assert(raw.strategies && Array.isArray(raw.strategies.structure) && Array.isArray(raw.strategies.connectors), `${lang} bad strategies shape`);
    }
    console.log('[PASS] CEFR B1 exam UI localization and JSON contracts verified for fr, it, pl, cs, sk.');
})();
