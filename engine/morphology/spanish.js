// ============================================
// SPANISH MORPHOLOGY — runtime conjugation fallback
// ============================================
// Lexicon.js resolves most Spanish verb forms from a precomputed table
// (generated/indexes/verb-index.json, built by scripts/build_verb_index.py
// from imports/verbs/*.json — Fred Jehle's 656-verb conjugation database).
// That table is necessarily finite: any verb outside those 656 — a new
// vocabulary word the curriculum adds, or literally any Spanish verb a
// learner pastes into the Reader — has zero conjugated forms in it, so
// tap-to-dictionary silently fails for anything but (sometimes) the bare
// infinitive. This module is the fallback for that gap, mirroring
// HungarianMorphology's role for Hungarian: given a tapped surface form,
// reconstruct candidate (lemma, mood, tense, person) analyses instead of
// requiring every verb to be pre-catalogued.
//
// Approach: reconstruction, not generation. Regular Spanish conjugation is
// fully suffix-based and the same across every -ar/-er/-ir verb, so this
// strips a candidate ending, reverses the spelling-only changes Spanish
// orthography requires in that context (tocar -> toqué needs c -> qu
// reversed, llegar -> llegué needs g -> gu reversed, etc. — deterministic
// from the letters alone, no lexical knowledge needed), and also tries
// reversing a stressed-syllable stem change (pienso -> pensar, pido ->
// pedir) since that pattern is common but NOT deterministic from spelling
// (comer never diphthongizes to *cuemo). A candidate is only accepted if
// the reconstructed lemma actually resolves in the dictionary passed in —
// exactly HungarianMorphology's "validate by outcome" filter — so a wrong
// guess at which verbs stem-change is caught by the acceptance check, not
// by needing to know in advance.
//
// The ~22 core irregular verbs (ser, ir, tener, poder, hacer, decir...)
// and a dozen irregular past participles (abierto, escrito, resuelto...)
// can't be reconstructed this way at all — their forms are genuinely
// unpredictable from the infinitive — so their full paradigms are
// embedded directly below, extracted from imports/verbs/*.json (Jehle's
// own data, not guessed). A compound built on one of these roots
// (obtener, deshacer, convenir, describir...) inherits the root's
// irregularity: this module checks whether a tapped form's ending
// matches one of these roots' own conjugated forms and, if so, treats
// the leftover prefix as carried straight through — true for the large
// majority of Spanish compounds, though a few genuine exceptions exist
// (bendecir/maldecir don't fully inherit decir's irregularity in the
// participle/future/conditional) and aren't specially handled here.
//
// Verified against the full 656-verb Jehle corpus before being wired in:
// candidates_for() in the derivation script this was ported from recovers
// the correct lemma for 95%+ of every simple conjugated form in the
// dataset (30,575 distinct surface forms) with zero knowledge of which
// verb produced which form — the remaining ~5% is almost entirely a
// pre-existing, already-documented limitation (stress-accent shift on a
// pronoun-suffixed form, e.g. an imperative's stripped-off "-te", is not
// reversible by suffix-stripping alone — build_verb_index.py's own
// approx=True flag exists for exactly this) plus a handful of single-verb
// rarities (argüir's diaeresis, agorar's o -> üe). Not chased further, in
// the same spirit as HungarianMorphology's own "Known gaps" note.

const SpanishMorphology = (function () {
    'use strict';


    // ---- Regular conjugation endings, verified against confirmed-regular
    // verbs (hablar/comer/vivir) across every mood/tense/person cell.
    // Compound tenses (haber + participle) are deliberately excluded —
    // Lexicon already resolves "he"/"había"/etc. as haber's own conjugated
    // forms and the participle separately, so a compound phrase like
    // "había hablado" is two already-resolvable words, not one to model
    // here.
    const REGULAR_ENDINGS = {
        ar: {
            'indicativo.presente':    { yo:'o',   tu:'as',   ud:'a',   nosotros:'amos',   vosotros:'áis',   uds:'an' },
            'indicativo.futuro':      { yo:'aré', tu:'arás', ud:'ará', nosotros:'aremos', vosotros:'aréis', uds:'arán' },
            'indicativo.imperfecto':  { yo:'aba', tu:'abas', ud:'aba', nosotros:'ábamos', vosotros:'abais', uds:'aban' },
            'indicativo.preterito':   { yo:'é',   tu:'aste', ud:'ó',   nosotros:'amos',   vosotros:'asteis', uds:'aron' },
            'indicativo.condicional': { yo:'aría', tu:'arías', ud:'aría', nosotros:'aríamos', vosotros:'aríais', uds:'arían' },
            'subjuntivo.presente':    { yo:'e',   tu:'es',   ud:'e',   nosotros:'emos',   vosotros:'éis',   uds:'en' },
            'subjuntivo.imperfecto':  { yo:'ara', tu:'aras', ud:'ara', nosotros:'áramos', vosotros:'arais', uds:'aran' },
            'subjuntivo.futuro':      { yo:'are', tu:'ares', ud:'are', nosotros:'áremos', vosotros:'areis', uds:'aren' },
            'subjuntivo.imperfectoAlt': { yo:'ase', tu:'ases', ud:'ase', nosotros:'ásemos', vosotros:'aseis', uds:'asen' }
        },
        er: {
            'indicativo.presente':    { yo:'o',  tu:'es',  ud:'e',  nosotros:'emos', vosotros:'éis', uds:'en' },
            'indicativo.futuro':      { yo:'eré', tu:'erás', ud:'erá', nosotros:'eremos', vosotros:'eréis', uds:'erán' },
            'indicativo.imperfecto':  { yo:'ía', tu:'ías', ud:'ía', nosotros:'íamos', vosotros:'íais', uds:'ían' },
            'indicativo.preterito':   { yo:'í',  tu:'iste', ud:'ió', nosotros:'imos', vosotros:'isteis', uds:'ieron' },
            'indicativo.condicional': { yo:'ería', tu:'erías', ud:'ería', nosotros:'eríamos', vosotros:'eríais', uds:'erían' },
            'subjuntivo.presente':    { yo:'a',  tu:'as',  ud:'a',  nosotros:'amos', vosotros:'áis', uds:'an' },
            'subjuntivo.imperfecto':  { yo:'iera', tu:'ieras', ud:'iera', nosotros:'iéramos', vosotros:'ierais', uds:'ieran' },
            'subjuntivo.futuro':      { yo:'iere', tu:'ieres', ud:'iere', nosotros:'iéremos', vosotros:'iereis', uds:'ieren' },
            'subjuntivo.imperfectoAlt': { yo:'iese', tu:'ieses', ud:'iese', nosotros:'iésemos', vosotros:'ieseis', uds:'iesen' }
        },
        ir: {
            'indicativo.presente':    { yo:'o',  tu:'es',  ud:'e',  nosotros:'imos', vosotros:'ís', uds:'en' },
            'indicativo.futuro':      { yo:'iré', tu:'irás', ud:'irá', nosotros:'iremos', vosotros:'iréis', uds:'irán' },
            'indicativo.imperfecto':  { yo:'ía', tu:'ías', ud:'ía', nosotros:'íamos', vosotros:'íais', uds:'ían' },
            'indicativo.preterito':   { yo:'í',  tu:'iste', ud:'ió', nosotros:'imos', vosotros:'isteis', uds:'ieron' },
            'indicativo.condicional': { yo:'iría', tu:'irías', ud:'iría', nosotros:'iríamos', vosotros:'iríais', uds:'irían' },
            'subjuntivo.presente':    { yo:'a',  tu:'as',  ud:'a',  nosotros:'amos', vosotros:'áis', uds:'an' },
            'subjuntivo.imperfecto':  { yo:'iera', tu:'ieras', ud:'iera', nosotros:'iéramos', vosotros:'ierais', uds:'ieran' },
            'subjuntivo.futuro':      { yo:'iere', tu:'ieres', ud:'iere', nosotros:'iéremos', vosotros:'iereis', uds:'ieren' },
            'subjuntivo.imperfectoAlt': { yo:'iese', tu:'ieses', ud:'iese', nosotros:'iésemos', vosotros:'ieseis', uds:'iesen' }
        }
    };

    const IMPERATIVE_ENDINGS = {
        ar: { afirmativo: { tu:'a', vosotros:'ad', ud:'e', uds:'en' }, negativo: { tu:'es', vosotros:'éis', ud:'e', uds:'en' } },
        er: { afirmativo: { tu:'e', vosotros:'ed', ud:'a', uds:'an' }, negativo: { tu:'as', vosotros:'áis', ud:'a', uds:'an' } },
        ir: { afirmativo: { tu:'e', vosotros:'id', ud:'a', uds:'an' }, negativo: { tu:'as', vosotros:'áis', ud:'a', uds:'an' } }
    };

    const PERSON_META = {
        yo: { person: 1, number: 'singular' }, tu: { person: 2, number: 'singular' },
        ud: { person: 3, number: 'singular' }, nosotros: { person: 1, number: 'plural' },
        vosotros: { person: 2, number: 'plural' }, uds: { person: 3, number: 'plural' }
    };

    // Extracted straight from imports/verbs/*.json (Jehle's own data) —
    // see the file header. Compound tenses omitted for the same reason
    // as REGULAR_ENDINGS above.
    const IRREGULAR_VERBS = 
    {
        "ser": {
            "indicativo": {
                "presente": {
                    "yo": "soy",
                    "tu": "eres",
                    "ud": "es",
                    "nosotros": "somos",
                    "vosotros": "sois",
                    "uds": "son"
                },
                "futuro": {
                    "yo": "seré",
                    "tu": "serás",
                    "ud": "será",
                    "nosotros": "seremos",
                    "vosotros": "seréis",
                    "uds": "serán"
                },
                "imperfecto": {
                    "yo": "era",
                    "tu": "eras",
                    "ud": "era",
                    "nosotros": "éramos",
                    "vosotros": "erais",
                    "uds": "eran"
                },
                "preterito": {
                    "yo": "fui",
                    "tu": "fuiste",
                    "ud": "fue",
                    "nosotros": "fuimos",
                    "vosotros": "fuisteis",
                    "uds": "fueron"
                },
                "condicional": {
                    "yo": "sería",
                    "tu": "serías",
                    "ud": "sería",
                    "nosotros": "seríamos",
                    "vosotros": "seríais",
                    "uds": "serían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "sea",
                    "tu": "seas",
                    "ud": "sea",
                    "nosotros": "seamos",
                    "vosotros": "seáis",
                    "uds": "sean"
                },
                "imperfecto": {
                    "yo": "fuera",
                    "tu": "fueras",
                    "ud": "fuera",
                    "nosotros": "fuéramos",
                    "vosotros": "fuerais",
                    "uds": "fueran"
                },
                "futuro": {
                    "yo": "fuere",
                    "tu": "fueres",
                    "ud": "fuere",
                    "nosotros": "fuéremos",
                    "vosotros": "fuereis",
                    "uds": "fueren"
                },
                "imperfectoAlt": {
                    "yo": "fuese",
                    "tu": "fueses",
                    "ud": "fuese",
                    "nosotros": "fuésemos",
                    "vosotros": "fueseis",
                    "uds": "fuesen"
                }
            },
            "afirmativo": {
                "tu": "sé",
                "vosotros": "sed",
                "ud": "sea",
                "uds": "sean"
            },
            "negativo": {
                "tu": "no seas",
                "vosotros": "no seáis",
                "ud": "no sea",
                "uds": "no sean"
            },
            "gerundio": "siendo",
            "participioPasado": "sido"
        },
        "estar": {
            "indicativo": {
                "presente": {
                    "yo": "estoy",
                    "tu": "estás",
                    "ud": "está",
                    "nosotros": "estamos",
                    "vosotros": "estáis",
                    "uds": "están"
                },
                "futuro": {
                    "yo": "estaré",
                    "tu": "estarás",
                    "ud": "estará",
                    "nosotros": "estaremos",
                    "vosotros": "estaréis",
                    "uds": "estarán"
                },
                "imperfecto": {
                    "yo": "estaba",
                    "tu": "estabas",
                    "ud": "estaba",
                    "nosotros": "estábamos",
                    "vosotros": "estabais",
                    "uds": "estaban"
                },
                "preterito": {
                    "yo": "estuve",
                    "tu": "estuviste",
                    "ud": "estuvo",
                    "nosotros": "estuvimos",
                    "vosotros": "estuvisteis",
                    "uds": "estuvieron"
                },
                "condicional": {
                    "yo": "estaría",
                    "tu": "estarías",
                    "ud": "estaría",
                    "nosotros": "estaríamos",
                    "vosotros": "estaríais",
                    "uds": "estarían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "esté",
                    "tu": "estés",
                    "ud": "esté",
                    "nosotros": "estemos",
                    "vosotros": "estéis",
                    "uds": "estén"
                },
                "imperfecto": {
                    "yo": "estuviera",
                    "tu": "estuvieras",
                    "ud": "estuviera",
                    "nosotros": "estuviéramos",
                    "vosotros": "estuvierais",
                    "uds": "estuvieran"
                },
                "futuro": {
                    "yo": "estuviere",
                    "tu": "estuvieres",
                    "ud": "estuviere",
                    "nosotros": "estuviéremos",
                    "vosotros": "estuviereis",
                    "uds": "estuvieren"
                },
                "imperfectoAlt": {
                    "yo": "estuviese",
                    "tu": "estuvieses",
                    "ud": "estuviese",
                    "nosotros": "estuviésemos",
                    "vosotros": "estuvieseis",
                    "uds": "estuviesen"
                }
            },
            "afirmativo": {
                "tu": "está",
                "vosotros": "estad",
                "ud": "esté",
                "uds": "estén"
            },
            "negativo": {
                "tu": "no estés",
                "vosotros": "no estéis",
                "ud": "no esté",
                "uds": "no estén"
            },
            "gerundio": "estando",
            "participioPasado": "estado"
        },
        "ir": {
            "indicativo": {
                "presente": {
                    "yo": "voy",
                    "tu": "vas",
                    "ud": "va",
                    "nosotros": "vamos",
                    "vosotros": "vais",
                    "uds": "van"
                },
                "futuro": {
                    "yo": "iré",
                    "tu": "irás",
                    "ud": "irá",
                    "nosotros": "iremos",
                    "vosotros": "iréis",
                    "uds": "irán"
                },
                "imperfecto": {
                    "yo": "iba",
                    "tu": "ibas",
                    "ud": "iba",
                    "nosotros": "íbamos",
                    "vosotros": "ibais",
                    "uds": "iban"
                },
                "preterito": {
                    "yo": "fui",
                    "tu": "fuiste",
                    "ud": "fue",
                    "nosotros": "fuimos",
                    "vosotros": "fuisteis",
                    "uds": "fueron"
                },
                "condicional": {
                    "yo": "iría",
                    "tu": "irías",
                    "ud": "iría",
                    "nosotros": "iríamos",
                    "vosotros": "iríais",
                    "uds": "irían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "vaya",
                    "tu": "vayas",
                    "ud": "vaya",
                    "nosotros": "vayamos",
                    "vosotros": "vayáis",
                    "uds": "vayan"
                },
                "imperfecto": {
                    "yo": "fuera",
                    "tu": "fueras",
                    "ud": "fuera",
                    "nosotros": "fuéramos",
                    "vosotros": "fuerais",
                    "uds": "fueran"
                },
                "futuro": {
                    "yo": "fuere",
                    "tu": "fueres",
                    "ud": "fuere",
                    "nosotros": "fuéremos",
                    "vosotros": "fuereis",
                    "uds": "fueren"
                },
                "imperfectoAlt": {
                    "yo": "fuese",
                    "tu": "fueses",
                    "ud": "fuese",
                    "nosotros": "fuésemos",
                    "vosotros": "fueseis",
                    "uds": "fuesen"
                }
            },
            "afirmativo": {
                "tu": "ve",
                "vosotros": "id",
                "ud": "vaya",
                "uds": "vayan"
            },
            "negativo": {
                "tu": "no vayas",
                "vosotros": "no vayáis",
                "ud": "no vaya",
                "uds": "no vayan"
            },
            "gerundio": "yendo",
            "participioPasado": "ido"
        },
        "haber": {
            "indicativo": {
                "presente": {
                    "yo": "",
                    "tu": "",
                    "ud": "hay",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "futuro": {
                    "yo": "",
                    "tu": "",
                    "ud": "habrá",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "imperfecto": {
                    "yo": "",
                    "tu": "",
                    "ud": "había",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "preterito": {
                    "yo": "",
                    "tu": "",
                    "ud": "hubo",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "condicional": {
                    "yo": "",
                    "tu": "",
                    "ud": "habría",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "",
                    "tu": "",
                    "ud": "haya",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "imperfecto": {
                    "yo": "",
                    "tu": "",
                    "ud": "hubiera",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "futuro": {
                    "yo": "",
                    "tu": "",
                    "ud": "hubiere",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                },
                "imperfectoAlt": {
                    "yo": "",
                    "tu": "",
                    "ud": "hubiese",
                    "nosotros": "",
                    "vosotros": "",
                    "uds": ""
                }
            },
            "afirmativo": {
                "tu": "",
                "ud": "haya",
                "uds": "",
                "vosotros": ""
            },
            "negativo": {
                "tu": "",
                "ud": "no haya",
                "uds": "",
                "vosotros": ""
            },
            "gerundio": "habiendo",
            "participioPasado": "habido"
        },
        "tener": {
            "indicativo": {
                "presente": {
                    "yo": "tengo",
                    "tu": "tienes",
                    "ud": "tiene",
                    "nosotros": "tenemos",
                    "vosotros": "tenéis",
                    "uds": "tienen"
                },
                "futuro": {
                    "yo": "tendré",
                    "tu": "tendrás",
                    "ud": "tendrá",
                    "nosotros": "tendremos",
                    "vosotros": "tendréis",
                    "uds": "tendrán"
                },
                "imperfecto": {
                    "yo": "tenía",
                    "tu": "tenías",
                    "ud": "tenía",
                    "nosotros": "teníamos",
                    "vosotros": "teníais",
                    "uds": "tenían"
                },
                "preterito": {
                    "yo": "tuve",
                    "tu": "tuviste",
                    "ud": "tuvo",
                    "nosotros": "tuvimos",
                    "vosotros": "tuvisteis",
                    "uds": "tuvieron"
                },
                "condicional": {
                    "yo": "tendría",
                    "tu": "tendrías",
                    "ud": "tendría",
                    "nosotros": "tendríamos",
                    "vosotros": "tendríais",
                    "uds": "tendrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "tenga",
                    "tu": "tengas",
                    "ud": "tenga",
                    "nosotros": "tengamos",
                    "vosotros": "tengáis",
                    "uds": "tengan"
                },
                "imperfecto": {
                    "yo": "tuviera",
                    "tu": "tuvieras",
                    "ud": "tuviera",
                    "nosotros": "tuviéramos",
                    "vosotros": "tuvierais",
                    "uds": "tuvieran"
                },
                "futuro": {
                    "yo": "tuviere",
                    "tu": "tuvieres",
                    "ud": "tuviere",
                    "nosotros": "tuviéremos",
                    "vosotros": "tuviereis",
                    "uds": "tuvieren"
                },
                "imperfectoAlt": {
                    "yo": "tuviese",
                    "tu": "tuvieses",
                    "ud": "tuviese",
                    "nosotros": "tuviésemos",
                    "vosotros": "tuvieseis",
                    "uds": "tuviesen"
                }
            },
            "afirmativo": {
                "tu": "ten",
                "vosotros": "tened",
                "ud": "tenga",
                "uds": "tengan"
            },
            "negativo": {
                "tu": "no tengas",
                "vosotros": "no tengáis",
                "ud": "no tenga",
                "uds": "no tengan"
            },
            "gerundio": "teniendo",
            "participioPasado": "tenido"
        },
        "hacer": {
            "indicativo": {
                "presente": {
                    "yo": "hago",
                    "tu": "haces",
                    "ud": "hace",
                    "nosotros": "hacemos",
                    "vosotros": "hacéis",
                    "uds": "hacen"
                },
                "futuro": {
                    "yo": "haré",
                    "tu": "harás",
                    "ud": "hará",
                    "nosotros": "haremos",
                    "vosotros": "haréis",
                    "uds": "harán"
                },
                "imperfecto": {
                    "yo": "hacía",
                    "tu": "hacías",
                    "ud": "hacía",
                    "nosotros": "hacíamos",
                    "vosotros": "hacíais",
                    "uds": "hacían"
                },
                "preterito": {
                    "yo": "hice",
                    "tu": "hiciste",
                    "ud": "hizo",
                    "nosotros": "hicimos",
                    "vosotros": "hicisteis",
                    "uds": "hicieron"
                },
                "condicional": {
                    "yo": "haría",
                    "tu": "harías",
                    "ud": "haría",
                    "nosotros": "haríamos",
                    "vosotros": "haríais",
                    "uds": "harían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "haga",
                    "tu": "hagas",
                    "ud": "haga",
                    "nosotros": "hagamos",
                    "vosotros": "hagáis",
                    "uds": "hagan"
                },
                "imperfecto": {
                    "yo": "hiciera",
                    "tu": "hicieras",
                    "ud": "hiciera",
                    "nosotros": "hiciéramos",
                    "vosotros": "hicierais",
                    "uds": "hicieran"
                },
                "futuro": {
                    "yo": "hiciere",
                    "tu": "hicieres",
                    "ud": "hiciere",
                    "nosotros": "hiciéremos",
                    "vosotros": "hiciereis",
                    "uds": "hicieren"
                },
                "imperfectoAlt": {
                    "yo": "hiciese",
                    "tu": "hicieses",
                    "ud": "hiciese",
                    "nosotros": "hiciésemos",
                    "vosotros": "hicieseis",
                    "uds": "hiciesen"
                }
            },
            "afirmativo": {
                "tu": "haz",
                "vosotros": "haced",
                "ud": "haga",
                "uds": "hagan"
            },
            "negativo": {
                "tu": "no hagas",
                "vosotros": "no hagáis",
                "ud": "no haga",
                "uds": "no hagan"
            },
            "gerundio": "haciendo",
            "participioPasado": "hecho"
        },
        "poder": {
            "indicativo": {
                "presente": {
                    "yo": "puedo",
                    "tu": "puedes",
                    "ud": "puede",
                    "nosotros": "podemos",
                    "vosotros": "podéis",
                    "uds": "pueden"
                },
                "futuro": {
                    "yo": "podré",
                    "tu": "podrás",
                    "ud": "podrá",
                    "nosotros": "podremos",
                    "vosotros": "podréis",
                    "uds": "podrán"
                },
                "imperfecto": {
                    "yo": "podía",
                    "tu": "podías",
                    "ud": "podía",
                    "nosotros": "podíamos",
                    "vosotros": "podíais",
                    "uds": "podían"
                },
                "preterito": {
                    "yo": "pude",
                    "tu": "pudiste",
                    "ud": "pudo",
                    "nosotros": "pudimos",
                    "vosotros": "pudisteis",
                    "uds": "pudieron"
                },
                "condicional": {
                    "yo": "podría",
                    "tu": "podrías",
                    "ud": "podría",
                    "nosotros": "podríamos",
                    "vosotros": "podríais",
                    "uds": "podrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "pueda",
                    "tu": "puedas",
                    "ud": "pueda",
                    "nosotros": "podamos",
                    "vosotros": "podáis",
                    "uds": "puedan"
                },
                "imperfecto": {
                    "yo": "pudiera",
                    "tu": "pudieras",
                    "ud": "pudiera",
                    "nosotros": "pudiéramos",
                    "vosotros": "pudierais",
                    "uds": "pudieran"
                },
                "futuro": {
                    "yo": "pudiere",
                    "tu": "pudieres",
                    "ud": "pudiere",
                    "nosotros": "pudiéremos",
                    "vosotros": "pudiereis",
                    "uds": "pudieren"
                },
                "imperfectoAlt": {
                    "yo": "pudiese",
                    "tu": "pudieses",
                    "ud": "pudiese",
                    "nosotros": "pudiésemos",
                    "vosotros": "pudieseis",
                    "uds": "pudiesen"
                }
            },
            "afirmativo": {
                "tu": "puede",
                "vosotros": "poded",
                "ud": "pueda",
                "uds": "puedan"
            },
            "negativo": {
                "tu": "no puedas",
                "vosotros": "no podáis",
                "ud": "no pueda",
                "uds": "no puedan"
            },
            "gerundio": "pudiendo",
            "participioPasado": "podido"
        },
        "poner": {
            "indicativo": {
                "presente": {
                    "yo": "pongo",
                    "tu": "pones",
                    "ud": "pone",
                    "nosotros": "ponemos",
                    "vosotros": "ponéis",
                    "uds": "ponen"
                },
                "futuro": {
                    "yo": "pondré",
                    "tu": "pondrás",
                    "ud": "pondrá",
                    "nosotros": "pondremos",
                    "vosotros": "pondréis",
                    "uds": "pondrán"
                },
                "imperfecto": {
                    "yo": "ponía",
                    "tu": "ponías",
                    "ud": "ponía",
                    "nosotros": "poníamos",
                    "vosotros": "poníais",
                    "uds": "ponían"
                },
                "preterito": {
                    "yo": "puse",
                    "tu": "pusiste",
                    "ud": "puso",
                    "nosotros": "pusimos",
                    "vosotros": "pusisteis",
                    "uds": "pusieron"
                },
                "condicional": {
                    "yo": "pondría",
                    "tu": "pondrías",
                    "ud": "pondría",
                    "nosotros": "pondríamos",
                    "vosotros": "pondríais",
                    "uds": "pondrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "ponga",
                    "tu": "pongas",
                    "ud": "ponga",
                    "nosotros": "pongamos",
                    "vosotros": "pongáis",
                    "uds": "pongan"
                },
                "imperfecto": {
                    "yo": "pusiera",
                    "tu": "pusieras",
                    "ud": "pusiera",
                    "nosotros": "pusiéramos",
                    "vosotros": "pusierais",
                    "uds": "pusieran"
                },
                "futuro": {
                    "yo": "pusiere",
                    "tu": "pusieres",
                    "ud": "pusiere",
                    "nosotros": "pusiéremos",
                    "vosotros": "pusiereis",
                    "uds": "pusieren"
                },
                "imperfectoAlt": {
                    "yo": "pusiese",
                    "tu": "pusieses",
                    "ud": "pusiese",
                    "nosotros": "pusiésemos",
                    "vosotros": "pusieseis",
                    "uds": "pusiesen"
                }
            },
            "afirmativo": {
                "tu": "pon",
                "vosotros": "poned",
                "ud": "ponga",
                "uds": "pongan"
            },
            "negativo": {
                "tu": "no pongas",
                "vosotros": "no pongáis",
                "ud": "no ponga",
                "uds": "no pongan"
            },
            "gerundio": "poniendo",
            "participioPasado": "puesto"
        },
        "querer": {
            "indicativo": {
                "presente": {
                    "yo": "quiero",
                    "tu": "quieres",
                    "ud": "quiere",
                    "nosotros": "queremos",
                    "vosotros": "queréis",
                    "uds": "quieren"
                },
                "futuro": {
                    "yo": "querré",
                    "tu": "querrás",
                    "ud": "querrá",
                    "nosotros": "querremos",
                    "vosotros": "querréis",
                    "uds": "querrán"
                },
                "imperfecto": {
                    "yo": "quería",
                    "tu": "querías",
                    "ud": "quería",
                    "nosotros": "queríamos",
                    "vosotros": "queríais",
                    "uds": "querían"
                },
                "preterito": {
                    "yo": "quise",
                    "tu": "quisiste",
                    "ud": "quiso",
                    "nosotros": "quisimos",
                    "vosotros": "quisisteis",
                    "uds": "quisieron"
                },
                "condicional": {
                    "yo": "querría",
                    "tu": "querrías",
                    "ud": "querría",
                    "nosotros": "querríamos",
                    "vosotros": "querríais",
                    "uds": "querrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "quiera",
                    "tu": "quieras",
                    "ud": "quiera",
                    "nosotros": "queramos",
                    "vosotros": "queráis",
                    "uds": "quieran"
                },
                "imperfecto": {
                    "yo": "quisiera",
                    "tu": "quisieras",
                    "ud": "quisiera",
                    "nosotros": "quisiéramos",
                    "vosotros": "quisierais",
                    "uds": "quisieran"
                },
                "futuro": {
                    "yo": "quisiere",
                    "tu": "quisieres",
                    "ud": "quisiere",
                    "nosotros": "quisiéremos",
                    "vosotros": "quisiereis",
                    "uds": "quisieren"
                },
                "imperfectoAlt": {
                    "yo": "quisiese",
                    "tu": "quisieses",
                    "ud": "quisiese",
                    "nosotros": "quisiésemos",
                    "vosotros": "quisieseis",
                    "uds": "quisiesen"
                }
            },
            "afirmativo": {
                "tu": "quiere",
                "vosotros": "quered",
                "ud": "quiera",
                "uds": "quieran"
            },
            "negativo": {
                "tu": "no quieras",
                "vosotros": "no queráis",
                "ud": "no quiera",
                "uds": "no quieran"
            },
            "gerundio": "queriendo",
            "participioPasado": "querido"
        },
        "saber": {
            "indicativo": {
                "presente": {
                    "yo": "sé",
                    "tu": "sabes",
                    "ud": "sabe",
                    "nosotros": "sabemos",
                    "vosotros": "sabéis",
                    "uds": "saben"
                },
                "futuro": {
                    "yo": "sabré",
                    "tu": "sabrás",
                    "ud": "sabrá",
                    "nosotros": "sabremos",
                    "vosotros": "sabréis",
                    "uds": "sabrán"
                },
                "imperfecto": {
                    "yo": "sabía",
                    "tu": "sabías",
                    "ud": "sabía",
                    "nosotros": "sabíamos",
                    "vosotros": "sabíais",
                    "uds": "sabían"
                },
                "preterito": {
                    "yo": "supe",
                    "tu": "supiste",
                    "ud": "supo",
                    "nosotros": "supimos",
                    "vosotros": "supisteis",
                    "uds": "supieron"
                },
                "condicional": {
                    "yo": "sabría",
                    "tu": "sabrías",
                    "ud": "sabría",
                    "nosotros": "sabríamos",
                    "vosotros": "sabríais",
                    "uds": "sabrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "sepa",
                    "tu": "sepas",
                    "ud": "sepa",
                    "nosotros": "sepamos",
                    "vosotros": "sepáis",
                    "uds": "sepan"
                },
                "imperfecto": {
                    "yo": "supiera",
                    "tu": "supieras",
                    "ud": "supiera",
                    "nosotros": "supiéramos",
                    "vosotros": "supierais",
                    "uds": "supieran"
                },
                "futuro": {
                    "yo": "supiere",
                    "tu": "supieres",
                    "ud": "supiere",
                    "nosotros": "supiéremos",
                    "vosotros": "supiereis",
                    "uds": "supieren"
                },
                "imperfectoAlt": {
                    "yo": "supiese",
                    "tu": "supieses",
                    "ud": "supiese",
                    "nosotros": "supiésemos",
                    "vosotros": "supieseis",
                    "uds": "supiesen"
                }
            },
            "afirmativo": {
                "tu": "sabe",
                "vosotros": "sabed",
                "ud": "sepa",
                "uds": "sepan"
            },
            "negativo": {
                "tu": "no sepas",
                "vosotros": "no sepáis",
                "ud": "no sepa",
                "uds": "no sepan"
            },
            "gerundio": "sabiendo",
            "participioPasado": "sabido"
        },
        "salir": {
            "indicativo": {
                "presente": {
                    "yo": "salgo",
                    "tu": "sales",
                    "ud": "sale",
                    "nosotros": "salimos",
                    "vosotros": "salís",
                    "uds": "salen"
                },
                "futuro": {
                    "yo": "saldré",
                    "tu": "saldrás",
                    "ud": "saldrá",
                    "nosotros": "saldremos",
                    "vosotros": "saldréis",
                    "uds": "saldrán"
                },
                "imperfecto": {
                    "yo": "salía",
                    "tu": "salías",
                    "ud": "salía",
                    "nosotros": "salíamos",
                    "vosotros": "salíais",
                    "uds": "salían"
                },
                "preterito": {
                    "yo": "salí",
                    "tu": "saliste",
                    "ud": "salió",
                    "nosotros": "salimos",
                    "vosotros": "salisteis",
                    "uds": "salieron"
                },
                "condicional": {
                    "yo": "saldría",
                    "tu": "saldrías",
                    "ud": "saldría",
                    "nosotros": "saldríamos",
                    "vosotros": "saldríais",
                    "uds": "saldrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "salga",
                    "tu": "salgas",
                    "ud": "salga",
                    "nosotros": "salgamos",
                    "vosotros": "salgáis",
                    "uds": "salgan"
                },
                "imperfecto": {
                    "yo": "saliera",
                    "tu": "salieras",
                    "ud": "saliera",
                    "nosotros": "saliéramos",
                    "vosotros": "salierais",
                    "uds": "salieran"
                },
                "futuro": {
                    "yo": "saliere",
                    "tu": "salieres",
                    "ud": "saliere",
                    "nosotros": "saliéremos",
                    "vosotros": "saliereis",
                    "uds": "salieren"
                },
                "imperfectoAlt": {
                    "yo": "saliese",
                    "tu": "salieses",
                    "ud": "saliese",
                    "nosotros": "saliésemos",
                    "vosotros": "salieseis",
                    "uds": "saliesen"
                }
            },
            "afirmativo": {
                "tu": "sal",
                "vosotros": "salid",
                "ud": "salga",
                "uds": "salgan"
            },
            "negativo": {
                "tu": "no salgas",
                "vosotros": "no salgáis",
                "ud": "no salga",
                "uds": "no salgan"
            },
            "gerundio": "saliendo",
            "participioPasado": "salido"
        },
        "traer": {
            "indicativo": {
                "presente": {
                    "yo": "traigo",
                    "tu": "traes",
                    "ud": "trae",
                    "nosotros": "traemos",
                    "vosotros": "traéis",
                    "uds": "traen"
                },
                "futuro": {
                    "yo": "traeré",
                    "tu": "traerás",
                    "ud": "traerá",
                    "nosotros": "traeremos",
                    "vosotros": "traeréis",
                    "uds": "traerán"
                },
                "imperfecto": {
                    "yo": "traía",
                    "tu": "traías",
                    "ud": "traía",
                    "nosotros": "traíamos",
                    "vosotros": "traíais",
                    "uds": "traían"
                },
                "preterito": {
                    "yo": "traje",
                    "tu": "trajiste",
                    "ud": "trajo",
                    "nosotros": "trajimos",
                    "vosotros": "trajisteis",
                    "uds": "trajeron"
                },
                "condicional": {
                    "yo": "traería",
                    "tu": "traerías",
                    "ud": "traería",
                    "nosotros": "traeríamos",
                    "vosotros": "traeríais",
                    "uds": "traerían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "traiga",
                    "tu": "traigas",
                    "ud": "traiga",
                    "nosotros": "traigamos",
                    "vosotros": "traigáis",
                    "uds": "traigan"
                },
                "imperfecto": {
                    "yo": "trajera",
                    "tu": "trajeras",
                    "ud": "trajera",
                    "nosotros": "trajéramos",
                    "vosotros": "trajerais",
                    "uds": "trajeran"
                },
                "futuro": {
                    "yo": "trajere",
                    "tu": "trajeres",
                    "ud": "trajere",
                    "nosotros": "trajéremos",
                    "vosotros": "trajereis",
                    "uds": "trajeren"
                },
                "imperfectoAlt": {
                    "yo": "trajese",
                    "tu": "trajeses",
                    "ud": "trajese",
                    "nosotros": "trajésemos",
                    "vosotros": "trajeseis",
                    "uds": "trajesen"
                }
            },
            "afirmativo": {
                "tu": "trae",
                "vosotros": "traed",
                "ud": "traiga",
                "uds": "traigan"
            },
            "negativo": {
                "tu": "no traigas",
                "vosotros": "no traigáis",
                "ud": "no traiga",
                "uds": "no traigan"
            },
            "gerundio": "trayendo",
            "participioPasado": "traído"
        },
        "valer": {
            "indicativo": {
                "presente": {
                    "yo": "valgo",
                    "tu": "vales",
                    "ud": "vale",
                    "nosotros": "valemos",
                    "vosotros": "valéis",
                    "uds": "valen"
                },
                "futuro": {
                    "yo": "valdré",
                    "tu": "valdrás",
                    "ud": "valdrá",
                    "nosotros": "valdremos",
                    "vosotros": "valdréis",
                    "uds": "valdrán"
                },
                "imperfecto": {
                    "yo": "valía",
                    "tu": "valías",
                    "ud": "valía",
                    "nosotros": "valíamos",
                    "vosotros": "valíais",
                    "uds": "valían"
                },
                "preterito": {
                    "yo": "valí",
                    "tu": "valiste",
                    "ud": "valió",
                    "nosotros": "valimos",
                    "vosotros": "valisteis",
                    "uds": "valieron"
                },
                "condicional": {
                    "yo": "valdría",
                    "tu": "valdrías",
                    "ud": "valdría",
                    "nosotros": "valdríamos",
                    "vosotros": "valdríais",
                    "uds": "valdrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "valga",
                    "tu": "valgas",
                    "ud": "valga",
                    "nosotros": "valgamos",
                    "vosotros": "valgáis",
                    "uds": "valgan"
                },
                "imperfecto": {
                    "yo": "valiera",
                    "tu": "valieras",
                    "ud": "valiera",
                    "nosotros": "valiéramos",
                    "vosotros": "valierais",
                    "uds": "valieran"
                },
                "futuro": {
                    "yo": "valiere",
                    "tu": "valieres",
                    "ud": "valiere",
                    "nosotros": "valiéremos",
                    "vosotros": "valiereis",
                    "uds": "valieren"
                },
                "imperfectoAlt": {
                    "yo": "valiese",
                    "tu": "valieses",
                    "ud": "valiese",
                    "nosotros": "valiésemos",
                    "vosotros": "valieseis",
                    "uds": "valiesen"
                }
            },
            "afirmativo": {
                "tu": "vale",
                "vosotros": "valed",
                "ud": "valga",
                "uds": "valgan"
            },
            "negativo": {
                "tu": "no valgas",
                "vosotros": "no valgáis",
                "ud": "no valga",
                "uds": "no valgan"
            },
            "gerundio": "valiendo",
            "participioPasado": "valido"
        },
        "venir": {
            "indicativo": {
                "presente": {
                    "yo": "vengo",
                    "tu": "vienes",
                    "ud": "viene",
                    "nosotros": "venimos",
                    "vosotros": "venís",
                    "uds": "vienen"
                },
                "futuro": {
                    "yo": "vendré",
                    "tu": "vendrás",
                    "ud": "vendrá",
                    "nosotros": "vendremos",
                    "vosotros": "vendréis",
                    "uds": "vendrán"
                },
                "imperfecto": {
                    "yo": "venía",
                    "tu": "venías",
                    "ud": "venía",
                    "nosotros": "veníamos",
                    "vosotros": "veníais",
                    "uds": "venían"
                },
                "preterito": {
                    "yo": "vine",
                    "tu": "viniste",
                    "ud": "vino",
                    "nosotros": "vinimos",
                    "vosotros": "vinisteis",
                    "uds": "vinieron"
                },
                "condicional": {
                    "yo": "vendría",
                    "tu": "vendrías",
                    "ud": "vendría",
                    "nosotros": "vendríamos",
                    "vosotros": "vendríais",
                    "uds": "vendrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "venga",
                    "tu": "vengas",
                    "ud": "venga",
                    "nosotros": "vengamos",
                    "vosotros": "vengáis",
                    "uds": "vengan"
                },
                "imperfecto": {
                    "yo": "viniera",
                    "tu": "vinieras",
                    "ud": "viniera",
                    "nosotros": "viniéramos",
                    "vosotros": "vinierais",
                    "uds": "vinieran"
                },
                "futuro": {
                    "yo": "viniere",
                    "tu": "vinieres",
                    "ud": "viniere",
                    "nosotros": "viniéremos",
                    "vosotros": "viniereis",
                    "uds": "vinieren"
                },
                "imperfectoAlt": {
                    "yo": "viniese",
                    "tu": "vinieses",
                    "ud": "viniese",
                    "nosotros": "viniésemos",
                    "vosotros": "vinieseis",
                    "uds": "viniesen"
                }
            },
            "afirmativo": {
                "tu": "ven",
                "vosotros": "venid",
                "ud": "venga",
                "uds": "vengan"
            },
            "negativo": {
                "tu": "no vengas",
                "vosotros": "no vengáis",
                "ud": "no venga",
                "uds": "no vengan"
            },
            "gerundio": "viniendo",
            "participioPasado": "venido"
        },
        "ver": {
            "indicativo": {
                "presente": {
                    "yo": "veo",
                    "tu": "ves",
                    "ud": "ve",
                    "nosotros": "vemos",
                    "vosotros": "veis",
                    "uds": "ven"
                },
                "futuro": {
                    "yo": "veré",
                    "tu": "verás",
                    "ud": "verá",
                    "nosotros": "veremos",
                    "vosotros": "veréis",
                    "uds": "verán"
                },
                "imperfecto": {
                    "yo": "veía",
                    "tu": "veías",
                    "ud": "veía",
                    "nosotros": "veíamos",
                    "vosotros": "veíais",
                    "uds": "veían"
                },
                "preterito": {
                    "yo": "vi",
                    "tu": "viste",
                    "ud": "vio",
                    "nosotros": "vimos",
                    "vosotros": "visteis",
                    "uds": "vieron"
                },
                "condicional": {
                    "yo": "vería",
                    "tu": "verías",
                    "ud": "vería",
                    "nosotros": "veríamos",
                    "vosotros": "veríais",
                    "uds": "verían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "vea",
                    "tu": "veas",
                    "ud": "vea",
                    "nosotros": "veamos",
                    "vosotros": "veáis",
                    "uds": "vean"
                },
                "imperfecto": {
                    "yo": "viera",
                    "tu": "vieras",
                    "ud": "viera",
                    "nosotros": "viéramos",
                    "vosotros": "vierais",
                    "uds": "vieran"
                },
                "futuro": {
                    "yo": "viere",
                    "tu": "vieres",
                    "ud": "viere",
                    "nosotros": "viéremos",
                    "vosotros": "viereis",
                    "uds": "vieren"
                },
                "imperfectoAlt": {
                    "yo": "viese",
                    "tu": "vieses",
                    "ud": "viese",
                    "nosotros": "viésemos",
                    "vosotros": "vieseis",
                    "uds": "viesen"
                }
            },
            "afirmativo": {
                "tu": "ve",
                "vosotros": "ved",
                "ud": "vea",
                "uds": "vean"
            },
            "negativo": {
                "tu": "no veas",
                "vosotros": "no veáis",
                "ud": "no vea",
                "uds": "no vean"
            },
            "gerundio": "viendo",
            "participioPasado": "visto"
        },
        "dar": {
            "indicativo": {
                "presente": {
                    "yo": "doy",
                    "tu": "das",
                    "ud": "da",
                    "nosotros": "damos",
                    "vosotros": "dais",
                    "uds": "dan"
                },
                "futuro": {
                    "yo": "daré",
                    "tu": "darás",
                    "ud": "dará",
                    "nosotros": "daremos",
                    "vosotros": "daréis",
                    "uds": "darán"
                },
                "imperfecto": {
                    "yo": "daba",
                    "tu": "dabas",
                    "ud": "daba",
                    "nosotros": "dábamos",
                    "vosotros": "dabais",
                    "uds": "daban"
                },
                "preterito": {
                    "yo": "di",
                    "tu": "diste",
                    "ud": "dio",
                    "nosotros": "dimos",
                    "vosotros": "disteis",
                    "uds": "dieron"
                },
                "condicional": {
                    "yo": "daría",
                    "tu": "darías",
                    "ud": "daría",
                    "nosotros": "daríamos",
                    "vosotros": "daríais",
                    "uds": "darían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "dé",
                    "tu": "des",
                    "ud": "dé",
                    "nosotros": "demos",
                    "vosotros": "deis",
                    "uds": "den"
                },
                "imperfecto": {
                    "yo": "diera",
                    "tu": "dieras",
                    "ud": "diera",
                    "nosotros": "diéramos",
                    "vosotros": "dierais",
                    "uds": "dieran"
                },
                "futuro": {
                    "yo": "diere",
                    "tu": "dieres",
                    "ud": "diere",
                    "nosotros": "diéremos",
                    "vosotros": "diereis",
                    "uds": "dieren"
                },
                "imperfectoAlt": {
                    "yo": "diese",
                    "tu": "dieses",
                    "ud": "diese",
                    "nosotros": "diésemos",
                    "vosotros": "dieseis",
                    "uds": "diesen"
                }
            },
            "afirmativo": {
                "tu": "da",
                "vosotros": "dad",
                "ud": "dé",
                "uds": "den"
            },
            "negativo": {
                "tu": "no des",
                "vosotros": "no deis",
                "ud": "no dé",
                "uds": "no den"
            },
            "gerundio": "dando",
            "participioPasado": "dado"
        },
        "caer": {
            "indicativo": {
                "presente": {
                    "yo": "caigo",
                    "tu": "caes",
                    "ud": "cae",
                    "nosotros": "caemos",
                    "vosotros": "caéis",
                    "uds": "caen"
                },
                "futuro": {
                    "yo": "caeré",
                    "tu": "caerás",
                    "ud": "caerá",
                    "nosotros": "caeremos",
                    "vosotros": "caeréis",
                    "uds": "caerán"
                },
                "imperfecto": {
                    "yo": "caía",
                    "tu": "caías",
                    "ud": "caía",
                    "nosotros": "caíamos",
                    "vosotros": "caíais",
                    "uds": "caían"
                },
                "preterito": {
                    "yo": "caí",
                    "tu": "caíste",
                    "ud": "cayó",
                    "nosotros": "caímos",
                    "vosotros": "caísteis",
                    "uds": "cayeron"
                },
                "condicional": {
                    "yo": "caería",
                    "tu": "caerías",
                    "ud": "caería",
                    "nosotros": "caeríamos",
                    "vosotros": "caeríais",
                    "uds": "caerían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "caiga",
                    "tu": "caigas",
                    "ud": "caiga",
                    "nosotros": "caigamos",
                    "vosotros": "caigáis",
                    "uds": "caigan"
                },
                "imperfecto": {
                    "yo": "cayera",
                    "tu": "cayeras",
                    "ud": "cayera",
                    "nosotros": "cayéramos",
                    "vosotros": "cayerais",
                    "uds": "cayeran"
                },
                "futuro": {
                    "yo": "cayere",
                    "tu": "cayeres",
                    "ud": "cayere",
                    "nosotros": "cayéremos",
                    "vosotros": "cayereis",
                    "uds": "cayeren"
                },
                "imperfectoAlt": {
                    "yo": "cayese",
                    "tu": "cayeses",
                    "ud": "cayese",
                    "nosotros": "cayésemos",
                    "vosotros": "cayeseis",
                    "uds": "cayesen"
                }
            },
            "afirmativo": {
                "tu": "cae",
                "vosotros": "caed",
                "ud": "caiga",
                "uds": "caigan"
            },
            "negativo": {
                "tu": "no caigas",
                "vosotros": "no caigáis",
                "ud": "no caiga",
                "uds": "no caigan"
            },
            "gerundio": "cayendo",
            "participioPasado": "caído"
        },
        "oír": {
            "indicativo": {
                "presente": {
                    "yo": "oigo",
                    "tu": "oyes",
                    "ud": "oye",
                    "nosotros": "oímos",
                    "vosotros": "oís",
                    "uds": "oyen"
                },
                "futuro": {
                    "yo": "oiré",
                    "tu": "oirás",
                    "ud": "oirá",
                    "nosotros": "oiremos",
                    "vosotros": "oiréis",
                    "uds": "oirán"
                },
                "imperfecto": {
                    "yo": "oía",
                    "tu": "oías",
                    "ud": "oía",
                    "nosotros": "oíamos",
                    "vosotros": "oíais",
                    "uds": "oían"
                },
                "preterito": {
                    "yo": "oí",
                    "tu": "oíste",
                    "ud": "oyó",
                    "nosotros": "oímos",
                    "vosotros": "oísteis",
                    "uds": "oyeron"
                },
                "condicional": {
                    "yo": "oiría",
                    "tu": "oirías",
                    "ud": "oiría",
                    "nosotros": "oiríamos",
                    "vosotros": "oiríais",
                    "uds": "oirían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "oiga",
                    "tu": "oigas",
                    "ud": "oiga",
                    "nosotros": "oigamos",
                    "vosotros": "oigáis",
                    "uds": "oigan"
                },
                "imperfecto": {
                    "yo": "oyera",
                    "tu": "oyeras",
                    "ud": "oyera",
                    "nosotros": "oyéramos",
                    "vosotros": "oyerais",
                    "uds": "oyeran"
                },
                "futuro": {
                    "yo": "oyere",
                    "tu": "oyeres",
                    "ud": "oyere",
                    "nosotros": "oyéremos",
                    "vosotros": "oyereis",
                    "uds": "oyeren"
                },
                "imperfectoAlt": {
                    "yo": "oyese",
                    "tu": "oyeses",
                    "ud": "oyese",
                    "nosotros": "oyésemos",
                    "vosotros": "oyeseis",
                    "uds": "oyesen"
                }
            },
            "afirmativo": {
                "tu": "oye",
                "vosotros": "oíd",
                "ud": "oiga",
                "uds": "oigan"
            },
            "negativo": {
                "tu": "no oigas",
                "vosotros": "no oigáis",
                "ud": "no oiga",
                "uds": "no oigan"
            },
            "gerundio": "oyendo",
            "participioPasado": "oído"
        },
        "decir": {
            "indicativo": {
                "presente": {
                    "yo": "digo",
                    "tu": "dices",
                    "ud": "dice",
                    "nosotros": "decimos",
                    "vosotros": "decís",
                    "uds": "dicen"
                },
                "futuro": {
                    "yo": "diré",
                    "tu": "dirás",
                    "ud": "dirá",
                    "nosotros": "diremos",
                    "vosotros": "diréis",
                    "uds": "dirán"
                },
                "imperfecto": {
                    "yo": "decía",
                    "tu": "decías",
                    "ud": "decía",
                    "nosotros": "decíamos",
                    "vosotros": "decíais",
                    "uds": "decían"
                },
                "preterito": {
                    "yo": "dije",
                    "tu": "dijiste",
                    "ud": "dijo",
                    "nosotros": "dijimos",
                    "vosotros": "dijisteis",
                    "uds": "dijeron"
                },
                "condicional": {
                    "yo": "diría",
                    "tu": "dirías",
                    "ud": "diría",
                    "nosotros": "diríamos",
                    "vosotros": "diríais",
                    "uds": "dirían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "diga",
                    "tu": "digas",
                    "ud": "diga",
                    "nosotros": "digamos",
                    "vosotros": "digáis",
                    "uds": "digan"
                },
                "imperfecto": {
                    "yo": "dijera",
                    "tu": "dijeras",
                    "ud": "dijera",
                    "nosotros": "dijéramos",
                    "vosotros": "dijerais",
                    "uds": "dijeran"
                },
                "futuro": {
                    "yo": "dijere",
                    "tu": "dijeres",
                    "ud": "dijere",
                    "nosotros": "dijéremos",
                    "vosotros": "dijereis",
                    "uds": "dijeren"
                },
                "imperfectoAlt": {
                    "yo": "dijese",
                    "tu": "dijeses",
                    "ud": "dijese",
                    "nosotros": "dijésemos",
                    "vosotros": "dijeseis",
                    "uds": "dijesen"
                }
            },
            "afirmativo": {
                "tu": "di",
                "vosotros": "decid",
                "ud": "diga",
                "uds": "digan"
            },
            "negativo": {
                "tu": "no digas",
                "vosotros": "no digáis",
                "ud": "no diga",
                "uds": "no digan"
            },
            "gerundio": "diciendo",
            "participioPasado": "dicho"
        },
        "andar": {
            "indicativo": {
                "presente": {
                    "yo": "ando",
                    "tu": "andas",
                    "ud": "anda",
                    "nosotros": "andamos",
                    "vosotros": "andáis",
                    "uds": "andan"
                },
                "futuro": {
                    "yo": "andaré",
                    "tu": "andarás",
                    "ud": "andará",
                    "nosotros": "andaremos",
                    "vosotros": "andaréis",
                    "uds": "andarán"
                },
                "imperfecto": {
                    "yo": "andaba",
                    "tu": "andabas",
                    "ud": "andaba",
                    "nosotros": "andábamos",
                    "vosotros": "andabais",
                    "uds": "andaban"
                },
                "preterito": {
                    "yo": "anduve",
                    "tu": "anduviste",
                    "ud": "anduvo",
                    "nosotros": "anduvimos",
                    "vosotros": "anduvisteis",
                    "uds": "anduvieron"
                },
                "condicional": {
                    "yo": "andaría",
                    "tu": "andarías",
                    "ud": "andaría",
                    "nosotros": "andaríamos",
                    "vosotros": "andaríais",
                    "uds": "andarían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "ande",
                    "tu": "andes",
                    "ud": "ande",
                    "nosotros": "andemos",
                    "vosotros": "andéis",
                    "uds": "anden"
                },
                "imperfecto": {
                    "yo": "anduviera",
                    "tu": "anduvieras",
                    "ud": "anduviera",
                    "nosotros": "anduviéramos",
                    "vosotros": "anduvierais",
                    "uds": "anduvieran"
                },
                "futuro": {
                    "yo": "anduviere",
                    "tu": "anduvieres",
                    "ud": "anduviere",
                    "nosotros": "anduviéremos",
                    "vosotros": "anduviereis",
                    "uds": "anduvieren"
                },
                "imperfectoAlt": {
                    "yo": "anduviese",
                    "tu": "anduvieses",
                    "ud": "anduviese",
                    "nosotros": "anduviésemos",
                    "vosotros": "anduvieseis",
                    "uds": "anduviesen"
                }
            },
            "afirmativo": {
                "tu": "anda",
                "vosotros": "andad",
                "ud": "ande",
                "uds": "anden"
            },
            "negativo": {
                "tu": "no andes",
                "vosotros": "no andéis",
                "ud": "no ande",
                "uds": "no anden"
            },
            "gerundio": "andando",
            "participioPasado": "andado"
        },
        "caber": {
            "indicativo": {
                "presente": {
                    "yo": "quepo",
                    "tu": "cabes",
                    "ud": "cabe",
                    "nosotros": "cabemos",
                    "vosotros": "cabéis",
                    "uds": "caben"
                },
                "futuro": {
                    "yo": "cabré",
                    "tu": "cabrás",
                    "ud": "cabrá",
                    "nosotros": "cabremos",
                    "vosotros": "cabréis",
                    "uds": "cabrán"
                },
                "imperfecto": {
                    "yo": "cabía",
                    "tu": "cabías",
                    "ud": "cabía",
                    "nosotros": "cabíamos",
                    "vosotros": "cabíais",
                    "uds": "cabían"
                },
                "preterito": {
                    "yo": "cupe",
                    "tu": "cupiste",
                    "ud": "cupo",
                    "nosotros": "cupimos",
                    "vosotros": "cupisteis",
                    "uds": "cupieron"
                },
                "condicional": {
                    "yo": "cabría",
                    "tu": "cabrías",
                    "ud": "cabría",
                    "nosotros": "cabríamos",
                    "vosotros": "cabríais",
                    "uds": "cabrían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "quepa",
                    "tu": "quepas",
                    "ud": "quepa",
                    "nosotros": "quepamos",
                    "vosotros": "quepáis",
                    "uds": "quepan"
                },
                "imperfecto": {
                    "yo": "cupiera",
                    "tu": "cupieras",
                    "ud": "cupiera",
                    "nosotros": "cupiéramos",
                    "vosotros": "cupierais",
                    "uds": "cupieran"
                },
                "futuro": {
                    "yo": "cupiere",
                    "tu": "cupieres",
                    "ud": "cupiere",
                    "nosotros": "cupiéremos",
                    "vosotros": "cupiereis",
                    "uds": "cupieren"
                },
                "imperfectoAlt": {
                    "yo": "cupiese",
                    "tu": "cupieses",
                    "ud": "cupiese",
                    "nosotros": "cupiésemos",
                    "vosotros": "cupieseis",
                    "uds": "cupiesen"
                }
            },
            "afirmativo": {
                "tu": "cabe",
                "vosotros": "cabed",
                "ud": "quepa",
                "uds": "quepan"
            },
            "negativo": {
                "tu": "no quepas",
                "vosotros": "no quepáis",
                "ud": "no quepa",
                "uds": "no quepan"
            },
            "gerundio": "cabiendo",
            "participioPasado": "cabido"
        },
        "satisfacer": {
            "indicativo": {
                "presente": {
                    "yo": "satisfago",
                    "tu": "satisfaces",
                    "ud": "satisface",
                    "nosotros": "satisfacemos",
                    "vosotros": "satisfacéis",
                    "uds": "satisfacen"
                },
                "futuro": {
                    "yo": "satisfaré",
                    "tu": "satisfarás",
                    "ud": "satisfará",
                    "nosotros": "satisfaremos",
                    "vosotros": "satisfaréis",
                    "uds": "satisfarán"
                },
                "imperfecto": {
                    "yo": "satisfacía",
                    "tu": "satisfacías",
                    "ud": "satisfacía",
                    "nosotros": "satisfacíamos",
                    "vosotros": "satisfacíais",
                    "uds": "satisfacían"
                },
                "preterito": {
                    "yo": "satisfice",
                    "tu": "satisficiste",
                    "ud": "satisfizo",
                    "nosotros": "satisficimos",
                    "vosotros": "satisficisteis",
                    "uds": "satisficieron"
                },
                "condicional": {
                    "yo": "satisfaría",
                    "tu": "satisfarías",
                    "ud": "satisfaría",
                    "nosotros": "satisfaríamos",
                    "vosotros": "satisfaríais",
                    "uds": "satisfarían"
                }
            },
            "subjuntivo": {
                "presente": {
                    "yo": "satisfaga",
                    "tu": "satisfagas",
                    "ud": "satisfaga",
                    "nosotros": "satisfagamos",
                    "vosotros": "satisfagáis",
                    "uds": "satisfagan"
                },
                "imperfecto": {
                    "yo": "satisficiera",
                    "tu": "satisficieras",
                    "ud": "satisficiera",
                    "nosotros": "satisficiéramos",
                    "vosotros": "satisficierais",
                    "uds": "satisficieran"
                },
                "futuro": {
                    "yo": "satisficiere",
                    "tu": "satisficieres",
                    "ud": "satisficiere",
                    "nosotros": "satisficiéremos",
                    "vosotros": "satisficiereis",
                    "uds": "satisficieren"
                },
                "imperfectoAlt": {
                    "yo": "satisficiese",
                    "tu": "satisficieses",
                    "ud": "satisficiese",
                    "nosotros": "satisficiésemos",
                    "vosotros": "satisficieseis",
                    "uds": "satisficiesen"
                }
            },
            "afirmativo": {
                "tu": "satisfaz",
                "vosotros": "satisfaced",
                "ud": "satisfaga",
                "uds": "satisfagan"
            },
            "negativo": {
                "tu": "no satisfagas",
                "vosotros": "no satisfagáis",
                "ud": "no satisfaga",
                "uds": "no satisfagan"
            },
            "gerundio": "satisfaciendo",
            "participioPasado": "satisfecho"
        }
    };

    // Verbs that are otherwise fully regular except for one irregular
    // past participle. A compound of one of these (descubrir, devolver,
    // reescribir...) inherits it via the same suffix-match mechanism
    // used for IRREGULAR_VERBS below.
    const IRREGULAR_PARTICIPLES = {
        abrir: 'abierto', cubrir: 'cubierto', escribir: 'escrito',
        morir: 'muerto', resolver: 'resuelto', romper: 'roto',
        volver: 'vuelto', freír: 'frito', imprimir: 'impreso',
        proveer: 'provisto'
    };

    // ---- Spelling-only reversals ----
    // Spanish keeps a consonant's SOUND constant across an ending's vowel
    // by changing its spelling — these are fully determined by the letters
    // present, never by which specific verb it is, so they apply to any
    // candidate stem regardless of whether that verb is in IRREGULAR_VERBS.
    // nextClass is 'e' for endings starting e/é/i/í, 'a_o' for endings
    // starting a/á/o/ó (or no vowel, e.g. imperative "-d"/"-id").
    function orthographicReversals(stem, nextClass) {
        const cands = new Set([stem]);
        if (nextClass === 'e') {
            if (stem.endsWith('qu')) cands.add(stem.slice(0, -2) + 'c');   // tocar: toqu- -> toc-
            if (stem.endsWith('gu') && !stem.endsWith('gü')) cands.add(stem.slice(0, -2) + 'g'); // llegar: llegu- -> lleg-
            if (stem.endsWith('c')) cands.add(stem.slice(0, -1) + 'z');    // cruzar: cruc- -> cruz-
        } else {
            if (stem.endsWith('j')) cands.add(stem.slice(0, -1) + 'g');    // coger/dirigir: -j- -> -g-
            if (stem.endsWith('zc')) cands.add(stem.slice(0, -2) + 'c');   // conocer: conozc- -> conoc-
            else if (stem.endsWith('z')) cands.add(stem.slice(0, -1) + 'c'); // vencer: venz- -> venc-
            if (stem.endsWith('ig')) cands.add(stem.slice(0, -2) + 'igu'); // distinguir: disting- -> distingu-
            if (stem.endsWith('uy')) cands.add(stem.slice(0, -2) + 'u');   // construir: construy- -> constru-
        }
        return cands;
    }

    // ---- Stressed-syllable stem-change reversal ----
    // e->ie (pensar), o->ue (contar), e->i (pedir, -ir only), plus the
    // accent-only raising on -iar/-uar verbs (envío -> enviar, actúo ->
    // actuar). Not deterministic from spelling (comer never diphthongizes)
    // — offered as a candidate regardless and filtered by whether the
    // reconstructed lemma actually resolves.
    const VOWEL_CLUSTER = /[aeiouáéíóú]+(?!.*[aeiouáéíóú])/;
    function stemVowelReversals(stem) {
        const cands = new Set([stem]);
        const m = VOWEL_CLUSTER.exec(stem);
        if (!m) return cands;
        const cluster = m[0];
        const start = m.index;
        const end = start + cluster.length;
        const before = stem.slice(0, start);
        const after = stem.slice(end);
        const repl = { ie: 'e', ue: 'o', i: 'e', í: 'i', ú: 'u' }[cluster];
        if (repl) cands.add(before + repl + after);
        return cands;
    }

    // Reverse-index: every simple conjugated form of every IRREGULAR_VERBS
    // root -> the root(s) it belongs to (built once, module load time).
    const _irregularFormToRoots = (function () {
        const index = {};
        function add(form, root) {
            if (!form) return;
            const key = form.toLowerCase();
            (index[key] = index[key] || new Set()).add(root);
        }
        Object.keys(IRREGULAR_VERBS).forEach(root => {
            const d = IRREGULAR_VERBS[root];
            ['indicativo', 'subjuntivo'].forEach(mood => {
                Object.keys(d[mood] || {}).forEach(tense => {
                    const persons = d[mood][tense];
                    Object.keys(persons).forEach(p => add(persons[p], root));
                });
            });
            ['afirmativo', 'negativo'].forEach(pol => {
                const persons = d[pol] || {};
                Object.keys(persons).forEach(p => add((persons[p] || '').replace(/^no /, ''), root));
            });
            add(d.gerundio, root);
            add(d.participioPasado, root);
            add(root, root);
        });
        return index;
    })();

    const _participleFormToRoot = (function () {
        const index = {};
        Object.keys(IRREGULAR_PARTICIPLES).forEach(root => {
            index[IRREGULAR_PARTICIPLES[root].toLowerCase()] = root;
        });
        return index;
    })();

    // A compounding prefix is a short run of letters — guards against an
    // accidental substring match (e.g. a form that merely happens to end
    // in "ir" shouldn't be treated as a compound of the irregular verb
    // "ir" unless the whole rest of the word really is that short).
    const COMPOUND_PREFIX = /^[a-zà-ÿñ]{0,6}$/;

    function reflexiveVariants(lemma) {
        return /^(ar|er|ir)$/.test(lemma.slice(-2)) ? [lemma, lemma + 'se'] : [lemma];
    }

    /** Every plausible (lemma, analysis) reconstruction for a tapped
     * surface form — unfiltered candidates, same spirit as Hungarian's
     * ladder-building. Caller (analyze()) is what actually validates each
     * one against the dictionary. */
    function candidateLemmas(form) {
        const out = new Set();

        // Compound-irregular inheritance.
        Object.keys(_irregularFormToRoots).forEach(irregularForm => {
            if (form === irregularForm || (form.endsWith(irregularForm) && form.length > irregularForm.length)) {
                const prefix = form.slice(0, form.length - irregularForm.length);
                if (COMPOUND_PREFIX.test(prefix)) {
                    _irregularFormToRoots[irregularForm].forEach(root => out.add(prefix + root));
                }
            }
        });
        Object.keys(_participleFormToRoot).forEach(irregularForm => {
            if (form === irregularForm || (form.endsWith(irregularForm) && form.length > irregularForm.length)) {
                const prefix = form.slice(0, form.length - irregularForm.length);
                if (COMPOUND_PREFIX.test(prefix)) out.add(prefix + _participleFormToRoot[irregularForm]);
            }
        });

        // Regular reconstruction across all three conjugation classes.
        ['ar', 'er', 'ir'].forEach(cls => {
            const endtab = REGULAR_ENDINGS[cls];
            Object.keys(endtab).forEach(cell => {
                const persons = endtab[cell];
                Object.keys(persons).forEach(person => {
                    const end = persons[person];
                    if (end && form.endsWith(end) && form.length > end.length) {
                        const rawStem = form.slice(0, form.length - end.length);
                        const nextClass = /^[eéií]/.test(end) ? 'e' : 'a_o';
                        orthographicReversals(rawStem, nextClass).forEach(s1 => {
                            stemVowelReversals(s1).forEach(s2 => out.add(s2 + cls));
                        });
                        out.add(rawStem + cls);
                    }
                });
            });
            Object.keys(IMPERATIVE_ENDINGS[cls]).forEach(pol => {
                const persons = IMPERATIVE_ENDINGS[cls][pol];
                Object.keys(persons).forEach(person => {
                    const end = persons[person];
                    if (end && form.endsWith(end) && form.length > end.length) {
                        const rawStem = form.slice(0, form.length - end.length);
                        const nextClass = /^[eéií]/.test(end) ? 'e' : 'a_o';
                        orthographicReversals(rawStem, nextClass).forEach(s1 => {
                            stemVowelReversals(s1).forEach(s2 => out.add(s2 + cls));
                        });
                        out.add(rawStem + cls);
                    }
                });
            });
            const gerundEnd = cls === 'ar' ? 'ando' : 'iendo';
            if (form.endsWith(gerundEnd) && form.length > gerundEnd.length) {
                const rawStem = form.slice(0, form.length - gerundEnd.length);
                // -ir stem-changing verbs mute their stem vowel in the
                // gerund too (pedir -> pidiendo, dormir -> durmiendo), the
                // same reversal the finite/imperative loops above already
                // apply — without it, every stem-changing -ir verb's
                // gerund (a very common form) never reconstructed to its
                // real lemma at all ("pidiendo" only ever produced the
                // non-word candidate "pidir", never "pedir").
                orthographicReversals(rawStem, 'a_o').forEach(s1 => {
                    stemVowelReversals(s1).forEach(s2 => out.add(s2 + cls));
                });
                out.add(rawStem + cls);
            }
            const participleEnd = cls === 'ar' ? 'ado' : 'ido';
            if (form.endsWith(participleEnd) && form.length > participleEnd.length) {
                out.add(form.slice(0, form.length - participleEnd.length) + cls);
            }
        });

        out.add(form);
        Array.from(out).forEach(c => { if (/^(ar|er|ir)$/.test(c.slice(-2))) out.add(c + 'se'); });
        return out;
    }

    // ---- Analysis metadata for an accepted candidate ----
    function analysisFor(lemma, form, dictionary) {
        // Is `form` itself a bare infinitive (possibly the reflexive variant)?
        if (form === lemma || form + 'se' === lemma || form === lemma.replace(/se$/, '')) {
            return { lemma: lemma, form: 'infinitive' };
        }
        const irregular = IRREGULAR_VERBS[lemma] || IRREGULAR_VERBS[lemma.replace(/se$/, '')];
        if (irregular) {
            if (irregular.gerundio && irregular.gerundio.toLowerCase() === form) return { lemma: lemma, form: 'gerund' };
            if (irregular.participioPasado && irregular.participioPasado.toLowerCase() === form) return { lemma: lemma, form: 'participle' };
            for (const mood of ['indicativo', 'subjuntivo']) {
                const tenses = irregular[mood] || {};
                for (const tense of Object.keys(tenses)) {
                    const persons = tenses[tense];
                    for (const p of Object.keys(persons)) {
                        if ((persons[p] || '').toLowerCase() === form) {
                            const meta = PERSON_META[p] || {};
                            return { lemma: lemma, mood: mood, tense: tense, person: meta.person, number: meta.number };
                        }
                    }
                }
            }
            for (const pol of ['afirmativo', 'negativo']) {
                const persons = irregular[pol] || {};
                for (const p of Object.keys(persons)) {
                    if ((persons[p] || '').replace(/^no /, '').toLowerCase() === form) {
                        const meta = PERSON_META[p] || {};
                        return { lemma: lemma, mood: 'imperative', polarity: pol, person: meta.person, number: meta.number };
                    }
                }
            }
        }
        const participleRoot = lemma.replace(/se$/, '');
        if (IRREGULAR_PARTICIPLES[participleRoot] && IRREGULAR_PARTICIPLES[participleRoot].toLowerCase() === form) {
            return { lemma: lemma, form: 'participle' };
        }
        // Regular reconstruction: recompute which cell this lemma+form pair
        // corresponds to by regenerating candidate endings the same way
        // candidateLemmas() did, this time keeping the (mood,tense,person).
        const cls = lemma.slice(-2) === 'se' ? lemma.slice(-4, -2) : lemma.slice(-2);
        const bareLemma = lemma.replace(/se$/, '');
        const stem = bareLemma.slice(0, -2);
        const gerundEnd = cls === 'ar' ? 'ando' : 'iendo';
        if (form === stem + gerundEnd || form === (stemVowelForward(stem)) + gerundEnd) return { lemma: lemma, form: 'gerund' };
        const participleEnd = cls === 'ar' ? 'ado' : 'ido';
        if (form === stem + participleEnd) return { lemma: lemma, form: 'participle' };

        for (const cell of Object.keys(REGULAR_ENDINGS[cls] || {})) {
            const persons = REGULAR_ENDINGS[cls][cell];
            for (const person of Object.keys(persons)) {
                if (formMatchesCell(form, stem, persons[person])) {
                    const [mood, tense] = cell.split('.');
                    const meta = PERSON_META[person] || {};
                    return { lemma: lemma, mood: mood, tense: tense, person: meta.person, number: meta.number };
                }
            }
        }
        for (const pol of ['afirmativo', 'negativo']) {
            const persons = IMPERATIVE_ENDINGS[cls][pol];
            for (const person of Object.keys(persons)) {
                if (formMatchesCell(form, stem, persons[person])) {
                    const meta = PERSON_META[person] || {};
                    return { lemma: lemma, mood: 'imperative', polarity: pol, person: meta.person, number: meta.number };
                }
            }
        }
        return { lemma: lemma, mood: null, tense: null };
    }

    // A stem may need spelling/vowel changes forward (the same
    // orthographic + stem-change rules, applied in the generation
    // direction) to actually match `form` for a given ending — this
    // mirrors orthographicReversals/stemVowelReversals but forward, only
    // used here to confirm which cell produced an already-accepted form.
    function formMatchesCell(form, stem, end) {
        if (!end) return false;
        if (form === stem + end) return true;
        const nextClass = /^[eéií]/.test(end) ? 'e' : 'a_o';
        for (const s of orthographicReversals(stem, nextClass)) {
            if (form === s + end) return true;
        }
        for (const s of stemVowelForwardCandidates(stem)) {
            if (form === s + end) return true;
            for (const s2 of orthographicReversals(s, nextClass)) {
                if (form === s2 + end) return true;
            }
        }
        return false;
    }
    function stemVowelForwardCandidates(stem) {
        const cands = new Set([stem]);
        const m = VOWEL_CLUSTER.exec(stem);
        if (!m) return cands;
        const cluster = m[0];
        const start = m.index, end = start + cluster.length;
        const before = stem.slice(0, start), after = stem.slice(end);
        const repl = { e: 'ie', o: 'ue', i: 'í', u: 'ú' }[cluster];
        if (repl) cands.add(before + repl + after);
        if (cluster === 'e') cands.add(before + 'i' + after);
        return cands;
    }
    function stemVowelForward(stem) {
        const c = Array.from(stemVowelForwardCandidates(stem));
        return c.length > 1 ? c[1] : stem;
    }

    /** Public entry point. Mirrors HungarianMorphology.analyze()'s role:
     * given a tapped surface form and the loaded Spanish dictionary
     * (lemma -> entry), return every reconstruction whose lemma actually
     * resolves as a real verb — shaped exactly like a generated/indexes/
     * verb-index.json entry, so Lexicon.js's existing describeVerb()/add()
     * handling needs no changes to consume it. */
    function analyze(word, dictionary) {
        if (!word || !dictionary) return [];
        const form = word.toLowerCase();
        const results = [];
        const seen = new Set();
        candidateLemmas(form).forEach(lemma => {
            if (seen.has(lemma)) return;
            const entry = dictionary[lemma];
            const isVerb = entry && (entry.type === 'verb' || entry.type === 'v');
            if (!isVerb && !IRREGULAR_VERBS[lemma] && !IRREGULAR_VERBS[lemma.replace(/se$/, '')]) return;
            seen.add(lemma);
            results.push(analysisFor(lemma, form, dictionary));
        });
        return results;
    }

    // ============================================
    // Noun / adjective inflection fallback
    // ============================================
    // generated/indexes/word-index.json (built by scripts/build_word_index.py
    // from doozan/spanish_data's es_allforms.csv) covers inflected forms for
    // whatever lemmas that external corpus happens to carry — a different,
    // smaller lemma set than imports/dictionary/spanish-en.json (Wiktionary).
    // A dictionary word the corpus doesn't have — or, same as the verb case,
    // literally anything a learner pastes in — has zero plural/gender forms
    // in the table. This is that gap's fallback: given a tapped surface
    // form, reverse the (fully regular, deterministic-from-spelling) plural
    // and gender suffixes and accept a candidate only if it resolves as a
    // real noun/adjective in the dictionary passed in.
    //
    // Spanish plural/gender marking, unlike verb stem-changes, is NOT
    // lexically arbitrary — every noun and adjective follows the same small
    // set of suffix rules — so no irregular-word table is needed here at
    // all, just the suffix reversal plus the written-accent shift that
    // reversal can trigger (imagen -> imágenes adds a syllable so the
    // stress, which stays on the same syllable, needs a mark to override
    // the plural's own default stress rule; nación -> naciones loses its
    // mark for the mirror-image reason). Rather than modelling Spanish
    // syllable-stress rules to compute exactly where that mark goes, this
    // generates every plausible placement (added, removed, or stripped
    // entirely) and lets the dictionary decide — same "accept only what
    // resolves" filter as everywhere else in this module.
    //
    // Verified against the same es_allforms.csv this module's own gap is
    // measured against (141,812 real noun/adjective surface forms): this
    // reconstruction recovers the correct lemma for 99.45% of them knowing
    // nothing about which word produced which form. The remaining ~0.5% is
    // mostly corpus noise (a handful of reflexive-verb forms mistagged as
    // nouns) plus genuine one-off irregulars (gais -> gay, obturatriz ->
    // obturador) not chased further.
    const ACCENT_MAP = { a: 'á', e: 'é', i: 'í', o: 'ó', u: 'ú' };
    const UNACCENT_MAP = { á: 'a', é: 'e', í: 'i', ó: 'o', ú: 'u' };
    const PLAIN_VOWELS = /[aeiou]/;
    const ANY_VOWEL = /[aeiouáéíóú]/;

    function stripAllAccents(s) {
        return s.replace(/[áéíóú]/g, c => UNACCENT_MAP[c]);
    }

    // Every way to add-or-remove one accent mark on `stem`'s last vowel,
    // plus the fully-unaccented form (covers a mark sitting further back,
    // e.g. imágenes -> imagen, which isn't on the truncation-adjacent vowel).
    function accentVariants(stem) {
        const out = new Set([stem, stripAllAccents(stem)]);
        let idx = -1;
        for (let i = stem.length - 1; i >= 0; i--) {
            if (ANY_VOWEL.test(stem[i])) { idx = i; break; }
        }
        if (idx === -1) return out;
        const ch = stem[idx];
        if (UNACCENT_MAP[ch]) {
            out.add(stem.slice(0, idx) + UNACCENT_MAP[ch] + stem.slice(idx + 1));
        } else if (PLAIN_VOWELS.test(ch)) {
            out.add(stem.slice(0, idx) + ACCENT_MAP[ch] + stem.slice(idx + 1));
            const base = stripAllAccents(stem);
            out.add(base.slice(0, idx) + ACCENT_MAP[ch] + base.slice(idx + 1));
        }
        return out;
    }

    // Returns { plural: Set, gender: Set } rather than one flat set because
    // the two need different acceptance rules in analyzeWord(): pluralising
    // is a live inflectional category for every noun and adjective, but
    // grammatical gender is only a live category for ADJECTIVES (every
    // adjective genuinely has both an -o and an -a form of the same word).
    // For nouns, gender is a fixed lexical fact, not an inflection — "casa"
    // (house) and "caso" (case) are two unrelated words that merely share
    // the same o/a shape, not the same noun in two genders. Reconstructing
    // "caso" as a candidate for "casa" and accepting it because it happens
    // to also be a real dictionary noun would be a false reading, not a
    // gap-filling one, so gender-derived candidates are only trusted when
    // they land on an adjective.
    function candidateWordLemmas(form) {
        const plural = new Set([form]);
        if (form.endsWith('s') && form.length > 2) {
            plural.add(form.slice(0, -1));                 // café(s), casa(s), jefe(s), crisis(unchanged)
        }
        if (form.endsWith('es') && form.length > 3) {
            const stem = form.slice(0, -2);
            accentVariants(stem).forEach(v => plural.add(v));  // nación<-naciones, imagen<-imágenes
            if (stem.endsWith('c')) plural.add(stem.slice(0, -1) + 'z');  // luz<-luces
        }
        if (form.endsWith('ces') && form.length > 4) {
            plural.add(form.slice(0, -3) + 'z');
        }

        // Gender: try o<->a on every plural-stage candidate, plus stripping
        // a trailing -a entirely (feminine -ora/-ona/-ina/-esa -> masculine
        // -or/-ón/-ín/-és, with the same accent-placement guesswork).
        const gender = new Set();
        plural.forEach(c => {
            if (c.endsWith('a')) {
                gender.add(c.slice(0, -1) + 'o');
                accentVariants(c.slice(0, -1)).forEach(v => gender.add(v));
            } else if (c.endsWith('o')) {
                gender.add(c.slice(0, -1) + 'a');
            }
        });
        return { plural: plural, gender: gender };
    }

    const WORD_POS = { noun: 'n', adjective: 'adj' };

    /** Public entry point for non-verb inflection. Given a tapped surface
     * form and the loaded Spanish dictionary, returns every reconstruction
     * whose lemma resolves as a real noun or adjective — shaped exactly
     * like a generated/indexes/word-index.json entry ({lemma, pos}), so
     * Lexicon.js's existing describeWord()/add() handling needs no changes
     * to consume it. Verbs are out of scope here — analyze() above and the
     * static verb-index already cover that ground. */
    function analyzeWord(word, dictionary) {
        if (!word || !dictionary) return [];
        const form = word.toLowerCase();
        const results = [];
        const seen = new Set();
        const cands = candidateWordLemmas(form);
        function tryLemma(lemma, adjectiveOnly) {
            if (lemma === form || seen.has(lemma)) return;
            const entry = dictionary[lemma];
            if (!entry) return;
            if (adjectiveOnly && entry.type !== 'adjective') return;
            const pos = WORD_POS[entry.type];
            if (!pos) return;
            seen.add(lemma);
            results.push({ lemma: lemma, pos: pos });
        }
        cands.plural.forEach(lemma => tryLemma(lemma, false));
        cands.gender.forEach(lemma => tryLemma(lemma, true));
        return results;
    }

    return { analyze: analyze, analyzeWord: analyzeWord };
})();
