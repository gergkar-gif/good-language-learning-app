// ============================================
// LANGUAGE
// ============================================
// Which course the learner is studying. Everything that is per-course — the
// content path, the saved progress, the SRS deck, the voice the app speaks
// with — hangs off this, so adding Hungarian is a matter of filling
// content/hu/ rather than hunting hardcoded paths through the engine.
//
// Deliberately NOT scoped by language: XP and the daily streak. Those record
// that the learner sat down and studied, which is a habit rather than a
// property of one course; splitting them would reset a streak every time
// somebody switched language.
//
// Content ids stay language-relative — a Hungarian lesson is 'lesson.a1.03'
// exactly as the Spanish one is. They never collide, because everything that
// stores them against a learner goes through key(), and everything that
// fetches them goes through content().

const Lang = (function () {
    'use strict';

    const DEFAULT = 'es-latam';
    const SETTING_KEY = 'app_language';

    // Voice tags per course, best first.
    const VOICES = {
        'es-latam': ['es-MX', 'es-US', 'es-419', 'es-CO', 'es-AR', 'es-ES', 'es'],
        'es-es':    ['es-ES', 'es'],
        hu:         ['hu-HU', 'hu'],
        fr:         ['fr-FR', 'fr-CA', 'fr']
    };

    // Course-level names for pickers and track settings
    const COURSE_NAMES = {
        'es-latam': 'Spanish (Latin America)',
        'es-es':    'Spanish (Spain)',
        hu:         'Hungarian',
        fr:         'French'
    };

    // Natural language names for learner-facing prompts, exercises, and drills
    const LANGUAGE_NAMES = {
        'es-latam': 'Spanish',
        'es-es':    'Spanish',
        hu:         'Hungarian',
        fr:         'French'
    };

    // Courses with real content behind them — what the language picker
    // (My Journey) offers. content/fr is still an empty folder (scaffolded
    // per multi-language-plan) so it stays out.
    const AVAILABLE = ['es-latam', 'es-es', 'hu'];

    // Can-do cue copy shared by both Spanish courses; only the city differs.
    const ES_CAN_DO_CUES = {
        monthsExamples: 'enero, febrero, marzo...',
        monthInEvent: 'State when an event or your birthday is using "en" (e.g. "En octubre..." or "En diciembre...")',
        daysExamples: 'lunes, martes...',
        dayInEvent: 'Say which day you do an activity (e.g. los lunes, los viernes)',
        cafeGreeting: 'Polite greeting (Hola / Buenas tardes)',
        cafeOrder: 'Order a drink or snack (e.g. "Un café con leche, por favor")',
        cafeBill: 'Conclude politely or ask for the bill ("La cuenta, por favor" / "Muchas gracias")',
        restaurantGreeting: 'Greeting and request a table ("Una mesa para dos, por favor")',
        restaurantOrder: 'Order food and drinks ("De primero queremos... y de segundo...")',
        restaurantBill: 'Ask for the bill ("La cuenta, por favor")',
        directionsInterruption: 'Polite opening (Disculpe / Perdón)',
        directionsAsk: 'Ask for directions (e.g. "¿Dónde está la estación de tren?")',
        directionsThanks: 'Thank the person (Muchas gracias)'
    };

    // Comprehensive language profiles — centralizing orthography, speech
    // locales, connectors, and exam labels so engine modules never need
    // hardcoded if-lang branches.
    const PROFILES = {
        'es-latam': {
            code: 'es-latam',
            baseCode: 'es',
            name: 'Spanish',
            courseName: 'Spanish (Latin America)',
            voices: ['es-MX', 'es-US', 'es-419', 'es-CO', 'es-AR', 'es-ES', 'es'],
            sttLocale: 'es-MX',
            contentFallback: 'es-es',
            tests: ['A1', 'A2', 'B1', 'B2'],
            diacritics: { a: ['á'], e: ['é'], i: ['í'], o: ['ó'], u: ['ú', 'ü'], n: ['ñ'] },
            openers: { '?': '¿', '!': '¡' },
            numberWords: {
                '1': ['uno', 'una', 'un'], '2': ['dos'], '3': ['tres'], '4': ['cuatro'], '5': ['cinco'],
                '6': ['seis'], '7': ['siete'], '8': ['ocho'], '9': ['nueve'], '10': ['diez']
            },
            speechAbbreviations: { 'pa': 'para', 'pal': 'parael', 'al': 'ael', 'del': 'deel' },
            examLabels: {
                trueFalseNotStated: ['Verdadero', 'Falso', 'No se menciona en el texto']
            },
            paradigm: {
                hasVosotros: false,
                persons: {
                    yo: { key: 'yo', label: 'yo' },
                    tu: { key: 'tu', label: 'tú' },
                    ud: { key: 'ud', label: 'él / ella' },
                    nosotros: { key: 'nosotros', label: 'nosotros' },
                    vosotros: { key: 'vosotros', label: 'vosotros' },
                    uds: { key: 'uds', label: 'ellos / ustedes' }
                },
                defaultPersons: ['yo', 'tu', 'ud', 'nosotros', 'uds'],
                vosotrosPersons: ['yo', 'tu', 'ud', 'nosotros', 'vosotros', 'uds'],
                tenses: [
                    { value: 'indicativo.presente',    label: 'Present' },
                    { value: 'indicativo.preterito',   label: 'Preterite' },
                    { value: 'indicativo.imperfecto',  label: 'Imperfect' },
                    { value: 'indicativo.futuro',      label: 'Future' },
                    { value: 'indicativo.condicional', label: 'Conditional' },
                    { value: 'subjuntivo.presente',    label: 'Present Subjunctive' },
                    { value: 'subjuntivo.imperfecto',  label: 'Imperfect Subjunctive' },
                    { value: 'subjuntivo.futuro',      label: 'Future Subjunctive' },
                    { value: 'all',                    label: 'All Tenses' }
                ]
            },
            canDoCues: Object.assign({}, ES_CAN_DO_CUES, { city: 'Mexico City' }),
            discourseConnectors: {
                A1: ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo'],
                A2: ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo', 'por eso', 'después', 'entonces'],
                B1: ['en primer lugar', 'por ejemplo', 'en mi opinión', 'además', 'por eso'],
                B2: ['en primer lugar', 'por ejemplo', 'en mi opinión', 'desde mi perspectiva', 'además', 'por consiguiente', 'no obstante', 'sin embargo', 'en definitiva', 'cabe destacar']
            }
        },
        'es-es': {
            code: 'es-es',
            baseCode: 'es',
            name: 'Spanish',
            courseName: 'Spanish (Spain)',
            voices: ['es-ES', 'es'],
            sttLocale: 'es-ES',
            contentFallback: 'es-latam',
            tests: ['A1', 'A2', 'B1'],
            diacritics: { a: ['á'], e: ['é'], i: ['í'], o: ['ó'], u: ['ú', 'ü'], n: ['ñ'] },
            openers: { '?': '¿', '!': '¡' },
            numberWords: {
                '1': ['uno', 'una', 'un'], '2': ['dos'], '3': ['tres'], '4': ['cuatro'], '5': ['cinco'],
                '6': ['seis'], '7': ['siete'], '8': ['ocho'], '9': ['nueve'], '10': ['diez']
            },
            speechAbbreviations: { 'pa': 'para', 'pal': 'parael', 'al': 'ael', 'del': 'deel' },
            canDoCues: Object.assign({}, ES_CAN_DO_CUES, { city: 'Madrid' }),
            examLabels: {
                trueFalseNotStated: ['Verdadero', 'Falso', 'No se menciona en el texto']
            },
            discourseConnectors: {
                A1: ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo'],
                A2: ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo', 'por eso', 'después', 'entonces'],
                B1: ['en primer lugar', 'por ejemplo', 'en mi opinión', 'además', 'por eso'],
                B2: ['en primer lugar', 'por ejemplo', 'en mi opinión', 'desde mi perspectiva', 'además', 'por consiguiente', 'no obstante', 'sin embargo', 'en definitiva', 'cabe destacar']
            }
        },
        hu: {
            code: 'hu',
            baseCode: 'hu',
            name: 'Hungarian',
            courseName: 'Hungarian',
            voices: ['hu-HU', 'hu'],
            sttLocale: 'hu-HU',
            tests: ['A1', 'A2', 'B1', 'C1'],
            diacritics: { a: ['á'], e: ['é'], i: ['í'], o: ['ó', 'ö', 'ő'], u: ['ú', 'ü', 'ű'] },
            openers: {},
            numberWords: {
                '1': ['egy'], '2': ['ketto', 'ket'], '3': ['harom'], '4': ['negy'], '5': ['ot'],
                '6': ['hat'], '7': ['het'], '8': ['nyolc'], '9': ['kilenc'], '10': ['tiz']
            },
            speechAbbreviations: { 'db': 'darab' },
            examLabels: {
                trueFalseNotStated: ['Igaz', 'Hamis', 'A szöveg nem tartalmaz ilyen információt']
            },
            canDoCues: {
                city: 'Budapest',
                monthsExamples: 'január, február, március...',
                monthInEvent: 'State when an event or your birthday is using -ban / -ben (e.g. "Októberben..." or "Decemberben...")',
                daysExamples: 'hétfő, kedd...',
                dayInEvent: 'Say which day you have an activity or day off (e.g. hétfőn, pénteken)',
                cafeGreeting: 'Polite greeting (Jó napot / Szia)',
                cafeOrder: 'Order a drink or snack (e.g. "Kérek egy kávét és egy tejet")',
                cafeBill: 'Conclude politely or ask for the bill ("Kérem a számlát" / "Köszönöm")',
                restaurantGreeting: 'Greeting and ask for a table or menu',
                restaurantOrder: 'Order food and drink politely ("Kérek egy...")',
                restaurantBill: 'Ask about the bill or thank the staff',
                directionsInterruption: 'Polite interruption (Elnézést / Bocsánat)',
                directionsAsk: 'Ask where a place is (e.g. "Hol van a pályaudvar?")',
                directionsThanks: 'Polite thank you (Köszönöm szépen)'
            },
            discourseConnectors: {
                A1: ['és', 'mert', 'is', 'de', 'szintén', 'szerintem'],
                A2: ['és', 'mert', 'is', 'de', 'szintén', 'szerintem', 'ezért', 'például', 'aztán'],
                B1: ['véleményem szerint', 'szerintem', 'úgy gondolom', 'először is', 'például', 'ugyanakkor', 'azonban', 'ezért', 'másrészt', 'egyrészt'],
                B2: ['véleményem szerint', 'úgy vélem', 'meglátásom szerint', 'elsőként', 'például', 'ugyanakkor', 'mindazonáltal', 'ennek következtében', 'másrészt', 'egyrészt', 'összességében']
            },
            informalTextingNote: "When Hungarian people text, accents are often left out — these exchanges simulate that, so don't be surprised if they're missing."
        }
    };

    let current = DEFAULT;
    try {
        const stored = localStorage.getItem(SETTING_KEY);
        current = (stored === 'es') ? 'es-latam' : (stored || DEFAULT);
    } catch (error) {
        // Private browsing with storage disabled: the default is fine.
    }

    function code() {
        return current;
    }

    function defaultCode() {
        return DEFAULT;
    }

    function paradigm(targetCode) {
        const p = profile(targetCode);
        return (p && p.paradigm) ? p.paradigm : null;
    }

    function profile(targetCode) {
        const c = targetCode || current;
        if (PROFILES[c]) return PROFILES[c];
        const base = c.split('-')[0];
        if (PROFILES[base]) return PROFILES[base];
        return {
            code: c,
            baseCode: base,
            name: LANGUAGE_NAMES[c] || c,
            courseName: COURSE_NAMES[c] || c,
            voices: VOICES[c] || [c],
            sttLocale: c,
            tests: ['A1', 'A2'],
            diacritics: {},
            openers: {},
            examLabels: { trueFalseNotStated: ['True', 'False', 'Not Stated'] },
            discourseConnectors: { A1: [], A2: [], B1: [], B2: [] }
        };
    }

    function registerProfile(cfg) {
        if (!cfg || !cfg.code) return;
        PROFILES[cfg.code] = Object.assign({}, profile(cfg.code), cfg);
        if (cfg.voices) VOICES[cfg.code] = cfg.voices;
        if (cfg.name) LANGUAGE_NAMES[cfg.code] = cfg.name;
        if (cfg.courseName) COURSE_NAMES[cfg.code] = cfg.courseName;
        if (cfg.isAvailable && !AVAILABLE.includes(cfg.code)) AVAILABLE.push(cfg.code);
    }

    function sttLocale(targetCode) {
        return profile(targetCode).sttLocale || (targetCode || current);
    }

    // Digit -> spoken number words, for matching "dos" against "2" in speech.
    function numberWords(targetCode) {
        return profile(targetCode).numberWords || {};
    }

    // Spoken contractions the recogniser may return ('pa' for 'para').
    function speechAbbreviations(targetCode) {
        return profile(targetCode).speechAbbreviations || {};
    }

    // A sibling course whose content can stand in for a missing file
    // (es-latam borrows es-es). null when the course has none.
    function contentFallback(targetCode) {
        return profile(targetCode).contentFallback || null;
    }

    function diacritics(targetCode) {
        return profile(targetCode).diacritics || {};
    }

    function openers(targetCode) {
        return profile(targetCode).openers || {};
    }

    function examLabels(targetCode) {
        return profile(targetCode).examLabels || {};
    }

    function discourseConnectors(level, targetCode) {
        const p = profile(targetCode);
        const lvl = (level || 'B1').toUpperCase();
        return (p.discourseConnectors && p.discourseConnectors[lvl]) || [];
    }

    function canDoCues(targetCode) {
        const p = profile(targetCode);
        return p.canDoCues || profile('es-latam').canDoCues || {};
    }

    // Natural language name for exercises and prompts ('Spanish', 'Hungarian')
    function name() {
        return LANGUAGE_NAMES[current] || current;
    }

    function languageNameFor(otherCode) {
        return LANGUAGE_NAMES[otherCode] || COURSE_NAMES[otherCode] || otherCode;
    }

    // The display name for any course code, not just the current one —
    // for rendering a picker over all of them.
    function nameFor(otherCode) {
        return COURSE_NAMES[otherCode] || otherCode;
    }

    function courseName() {
        return COURSE_NAMES[current] || current;
    }

    function available() {
        return AVAILABLE.slice();
    }

    function voices() {
        return VOICES[current] || [current];
    }

    // A path inside the current course: content('lessons/a1/a1-01.json').
    function content(path) {
        return `content/${current}/${path}`;
    }

    // A localStorage key scoped to the current course. Spanish lesson 3 and
    // Hungarian lesson 3 share an id, so without this, finishing one would
    // mark the other complete and both decks would pour into one pile.
    function key(name) {
        return `${current}:${name}`;
    }

    // Universal target text accessor that accepts any exercise/pair/card item shape
    function targetText(item) {
        if (!item) return '';
        if (typeof item === 'string') return item;
        const base = current.split('-')[0];
        return item.target || item.lemma || item[current] || item[base] || item.hungarian || item.spanish || item.sentence || '';
    }

    // Universal lemma accessor that accepts any dictionary/word/card item shape
    function targetLemma(item) {
        if (!item) return '';
        if (typeof item === 'string') return item;
        const base = current.split('-')[0];
        return item.target || item.lemma || item[current] || item[base] || item.hungarian || item.spanish || item.word || '';
    }

    // Migrate older keys to course-scoped names without losing learner progress.
    function migrateLegacyKeys() {
        try {
            // 1. Unscoped legacy keys -> es:
            const legacy = {
                'spanishApp_srsDeck': 'es:srsDeck',
                'spanishMastery_progress': 'es:progress',
                'spanishApp_readStories': 'es:readStories'
            };
            for (const [from, to] of Object.entries(legacy)) {
                const value = localStorage.getItem(from);
                if (value !== null && localStorage.getItem(to) === null) {
                    localStorage.setItem(to, value);
                }
            }

            // 2. es: -> es-latam:
            const esToLatam = {
                'es:srsDeck': 'es-latam:srsDeck',
                'es:progress': 'es-latam:progress',
                'es:readStories': 'es-latam:readStories'
            };
            for (const [from, to] of Object.entries(esToLatam)) {
                const value = localStorage.getItem(from);
                if (value !== null && localStorage.getItem(to) === null) {
                    localStorage.setItem(to, value);
                }
            }

            // 3. Stored language setting migration
            if (localStorage.getItem(SETTING_KEY) === 'es') {
                localStorage.setItem(SETTING_KEY, 'es-latam');
            }
        } catch (error) {
            console.warn('Language: could not migrate saved data', error);
        }
    }

    function set(next) {
        if (!next || next === current) return;
        current = next;
        try {
            localStorage.setItem(SETTING_KEY, next);
            if (localStorage.getItem('parlour_first_open_completed') === 'true') {
                localStorage.setItem(`${next}:diagnosticOnboardingDismissed`, 'true');
            }
        } catch (error) {
            console.warn('Language: could not save the chosen course', error);
        }
        document.dispatchEvent(new CustomEvent('language-changed', { detail: next }));
    }

    migrateLegacyKeys();

    return {
        code,
        current: code,
        defaultCode,
        name,
        nameFor,
        languageNameFor,
        courseName,
        available,
        voices,
        content,
        key,
        set,
        profile,
        registerProfile,
        sttLocale,
        numberWords,
        speechAbbreviations,
        contentFallback,
        diacritics,
        openers,
        examLabels,
        discourseConnectors,
        canDoCues,
        targetText,
        targetLemma,
        paradigm
    };
})();
