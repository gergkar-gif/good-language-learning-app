/**
 * tests/test-verb-engine-nonlesson.js
 * Verifies VerbsTable, VerbsSpeed, and all verb datasets across fr, it, pl, cs, sk.
 */
'use strict';

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..');

function makeSandbox() {
    const elements = {};
    const makeEl = (tag) => ({
        tagName: (tag || 'div').toUpperCase(),
        className: '',
        dataset: {},
        style: {},
        value: '',
        readOnly: false,
        disabled: false,
        textContent: '',
        _listeners: {},
        classList: {
            _set: new Set(),
            add(...cs) { cs.forEach(c => this._set.add(c)); },
            remove(...cs) { cs.forEach(c => this._set.delete(c)); },
            contains(c) { return this._set.has(c); }
        },
        addEventListener(ev, fn) {
            (this._listeners[ev] = this._listeners[ev] || []).push(fn);
        },
        click() { (this._listeners.click || []).forEach(fn => fn()); },
        focus() {},
        querySelector() { return null; },
        querySelectorAll() { return []; }
    });

    const sandbox = {
        console,
        Math,
        Date,
        setTimeout: (fn) => { sandbox._lastTimeout = fn; return 1; },
        clearTimeout() {},
        setInterval: () => 1,
        clearInterval() {},
        window: { matchMedia: () => ({ matches: true }) },
        document: {
            getElementById(id) { return elements[id] || null; }
        },
        VerbsStats: {
            init() {},
            record(ok) { sandbox._recorded.push(ok); }
        },
        _recorded: [],
        _elements: elements,
        _makeEl: makeEl,
        Lang: { paradigm: () => ({ persons: {
            ty: { label: 'ty' }, my: { label: 'my' }, wy: { label: 'wy' },
            ja: { label: 'ja' }, io: { label: 'io' }, il: { label: 'il' }
        } }) },
        UI: { escape: s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;') }
    };
    sandbox.window.document = sandbox.document;
    return sandbox;
}

// 1. Test VerbsTable: empty person omission & slash variant + strict accent grading
(function testVerbsTable() {
    const sb = makeSandbox();
    vm.runInNewContext(fs.readFileSync(path.join(ROOT, 'engine/verbs/table.js'), 'utf8') + '\nthis.VerbsTable = VerbsTable;', sb);

    const rows = [];
    const feedback = sb._makeEl('div');
    const checkBtn = sb._makeEl('button');
    const nextBtn = sb._makeEl('button');
    const root = {
        _html: '',
        set innerHTML(html) {
            this._html = html;
            rows.length = 0;
            const inputRe = /<div class="vtable-row">[\s\S]*?<input[^>]*data-person="([^"]+)" data-correct="([^"]*)"[\s\S]*?<span class="vtable-correction[^>]*><\/span>/g;
            let m;
            while ((m = inputRe.exec(html)) !== null) {
                const inp = sb._makeEl('input');
                inp.dataset.person = m[1];
                inp.dataset.correct = m[2];
                const corr = sb._makeEl('span');
                rows.push({
                    input: inp,
                    corr,
                    querySelector(sel) { return sel === '.vtable-input' ? inp : (sel === '.vtable-correction' ? corr : null); }
                });
            }
        },
        get innerHTML() { return this._html; },
        querySelectorAll(sel) {
            if (sel === '.vtable-row') return rows;
            if (sel === '.vtable-input') return rows.map(r => r.input);
            return [];
        },
        querySelector(sel) {
            if (sel === '[data-action="check"]') return checkBtn;
            if (sel === '[data-action="next"]') return nextBtn;
            if (sel === '.vtable-feedback') return feedback;
            if (sel === '.vtable-input') return rows[0] ? rows[0].input : null;
            return null;
        }
    };

    // Imperative with missing ja/on/oni should render ONLY ty, my, wy
    sb.VerbsTable.render(root, {
        verb: { infinitivo: 'robić', tryb: { rozkazujacy: { ty: 'rób', my: 'róbmy', wy: 'róbcie' } } },
        tensePath: 'tryb.rozkazujacy',
        tenseLabel: 'Tryb rozkazujący',
        persons: ['ja', 'ty', 'on', 'my', 'wy', 'oni'],
        meaning: 'to do, to make',
        onNext() {}
    });
    assert.deepStrictEqual(rows.map(r => r.input.dataset.person), ['ty', 'my', 'wy'], 'VerbsTable must omit absent imperative persons');

    // Polish slash alternative (robiłam for robiłem/robiłam) & strict accents
    sb.VerbsTable.render(root, {
        verb: { infinitivo: 'robić', indicativo: { przeszly: { ja: 'robiłem/robiłam', ty: 'robiłeś/robiłaś', on: 'robił' } } },
        tensePath: 'indicativo.przeszly',
        tenseLabel: 'Past',
        persons: ['ja', 'ty', 'on'],
        meaning: 'to do',
        onNext() {}
    });
    rows[0].input.value = 'robiłam';
    rows[1].input.value = 'robiles'; // missing diacritics -> must fail
    rows[2].input.value = 'robił';
    checkBtn.click();
    assert(rows[0].input.classList.contains('vtable-correct'), 'VerbsTable should accept female slash variant');
    assert(rows[1].input.classList.contains('vtable-wrong'), 'VerbsTable must reject missing accents');
    assert(rows[2].input.classList.contains('vtable-correct'), 'VerbsTable should accept exact match');

    // Italian single-char slash ending (sono andato/a)
    sb.VerbsTable.render(root, {
        verb: { infinitivo: 'andare', indicativo: { passato_prossimo: { io: 'sono andato/a' } } },
        tensePath: 'indicativo.passato_prossimo',
        tenseLabel: 'Passato prossimo',
        persons: ['io'],
        meaning: 'to go',
        onNext() {}
    });
    rows[0].input.value = 'sono andata';
    checkBtn.click();
    assert(rows[0].input.classList.contains('vtable-correct'), 'VerbsTable should accept sono andata for sono andato/a');
})();

// 2. Test VerbsSpeed: falls back from absent person on imperative & accepts slash variants
async function testVerbsSpeed() {
    const sb = makeSandbox();
    const robicVerb = JSON.parse(fs.readFileSync(path.join(ROOT, 'imports/verbs/pl/robić.json'), 'utf8'));
    sb.Content = { verb: () => Promise.resolve(robicVerb) };
    // Force _pickRandom to first choose index 0 ('ja' - absent from imperative) then fallback valid person
    sb.Math = Object.create(Math);
    sb.Math.random = () => 0;

    vm.runInNewContext(fs.readFileSync(path.join(ROOT, 'engine/verbs/speed.js'), 'utf8') + '\nthis.VerbsSpeed = VerbsSpeed;', sb);

    const qEl = sb._makeEl('div');
    const scoreEl = sb._makeEl('span');
    const feedbackEl = sb._makeEl('div');
    const submitBtn = sb._makeEl('button');
    const ansInput = sb._makeEl('input');
    sb._elements['vspeed-answer'] = ansInput;
    Object.defineProperty(qEl, 'innerHTML', {
        set(html) {
            qEl._html = html;
            if (html.includes('vspeed-answer')) {
                ansInput._listeners = {};
                submitBtn._listeners = {};
            }
        },
        get() { return qEl._html || ''; }
    });
    qEl.querySelector = (sel) => sel === '[data-action="submit"]' ? submitBtn : null;

    const root = {
        innerHTML: '',
        querySelector(sel) {
            if (sel === '.vspeed-question') return qEl;
            if (sel === '.vspeed-score-value') return scoreEl;
            if (sel === '.vspeed-feedback') return feedbackEl;
            if (sel === '[data-action="submit"]') return submitBtn;
            return null;
        }
    };

    sb.VerbsSpeed.render(root, {
        tense: 'tryb.rozkazujacy',
        tenseLabel: 'Imperative',
        tenseOptions: [{ value: 'tryb.rozkazujacy', label: 'Imperative' }],
        persons: ['ja', 'ty', 'on', 'my', 'wy', 'oni'],
        verbList: ['robić'],
        autoStart: true
    });

    await new Promise(r => setTimeout(r, 10));
    assert(!qEl.innerHTML.includes('No questions available'), 'VerbsSpeed must not show empty error on imperative');
    assert(qEl.innerHTML.includes('ROBIĆ'), 'VerbsSpeed must render valid imperative person question');
    ansInput.value = 'rób'; // ty = Index 0 of validPersons ['ty', 'my', 'wy']
    submitBtn.click();
    assert.strictEqual(scoreEl.textContent, 1, 'VerbsSpeed must score correct fallback person');
    sb.VerbsSpeed.reset();
}

// 3. Validate all 941 verb datasets across fr, it, pl, cs, sk
const SPECS = {
    fr: { varName: 'ALL_FRENCH_VERBS', listFile: 'imports/verbs/fr/verb-list-fr.js', root: 'indicatif', tenses: ['present', 'imparfait', 'futur_simple', 'conditionnel_present', 'passe_compose', 'plus_que_parfait'], persons: ['je', 'tu', 'il', 'nous', 'vous', 'ils'], defective: new Set(['falloir', 'pleuvoir', 'faillir']) },
    it: { varName: 'ALL_ITALIAN_VERBS', listFile: 'imports/verbs/it/verb-list-it.js', root: 'indicativo', tenses: ['presente', 'passato_prossimo', 'imperfetto', 'futuro_semplice', 'condizionale_presente', 'passato_remoto'], persons: ['io', 'tu', 'lui', 'noi', 'voi', 'loro'], defective: new Set() },
    pl: { varName: 'ALL_POLISH_VERBS', listFile: 'imports/verbs/pl/verb-list-pl.js', root: 'indicativo', tenses: ['presente', 'przeszly', 'przyszly'], persons: ['ja', 'ty', 'on', 'my', 'wy', 'oni'], defective: new Set() },
    cs: { varName: 'ALL_CZECH_VERBS', listFile: 'imports/verbs/cs/verb-list-cs.js', root: 'indicativo', tenses: ['presente', 'minuly', 'budouci'], persons: ['ja', 'ty', 'on', 'my', 'vy', 'oni'], defective: new Set() },
    sk: { varName: 'ALL_SLOVAK_VERBS', listFile: 'imports/verbs/sk/verb-list-sk.js', root: 'indicativo', tenses: ['presente', 'minuly', 'budouci'], persons: ['ja', 'ty', 'on', 'my', 'vy', 'oni'], defective: new Set() }
};

let totalVerified = 0;
for (const [lang, spec] of Object.entries(SPECS)) {
    const sb = {};
    vm.runInNewContext(fs.readFileSync(path.join(ROOT, spec.listFile), 'utf8') + `\nthis.${spec.varName} = ${spec.varName};`, sb);
    const list = sb[spec.varName];
    assert(Array.isArray(list) && list.length >= 100, `${lang} verb list too short`);

    for (const v of list) {
        const fp = path.join(ROOT, `imports/verbs/${lang}/${v}.json`);
        assert(fs.existsSync(fp), `${lang} missing verb JSON: ${v}`);
        const d = JSON.parse(fs.readFileSync(fp, 'utf8'));
        const en = d.english && d.english.infinitivo;
        assert(en && en.length >= 3 && en !== `to ${v}`, `${lang}/${v} invalid english.infinitivo: ${en}`);
        if (spec.defective.has(v)) { totalVerified++; continue; }
        for (const t of spec.tenses) {
            const td = d[spec.root] && d[spec.root][t];
            assert(td, `${lang}/${v} missing ${spec.root}.${t}`);
            for (const p of spec.persons) {
                const form = td[p];
                assert(form && !form.split('/')[0].includes('-'), `${lang}/${v} invalid ${t}.${p}: "${form}"`);
                if (lang === 'fr' && t !== 'futur_simple') {
                    assert.notStrictEqual(form, v, `fr/${v} ${t}.${p} leaked infinitive`);
                }
            }
        }
        totalVerified++;
    }
}

testVerbsSpeed().then(() => {
    console.log(`[PASS] VerbsTable, VerbsSpeed, and ${totalVerified} verb datasets verified across fr, it, pl, cs, sk.`);
}).catch((err) => {
    console.error(err);
    process.exit(1);
});
