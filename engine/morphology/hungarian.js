// ============================================
// HUNGARIAN MORPHOLOGY — runtime suffix-stripping fallback
// ============================================
// Lexicon.js resolves most Hungarian words two ways first: a direct
// dictionary hit (the tapped word already is a lemma), or a hit in the
// static word-index built from Wiktionary's own declension tables (see
// scripts/import_hu_dictionary.py) for common lemmas' case/possessive
// forms. This module is the fallback for everything neither of those
// covers — most importantly case+possessive stacking ("házamban" = ház +
// possessive 1sg + inessive, which Wiktionary's tables never enumerate as
// a single combined form) and any verb form at all, since Hungarian verb
// conjugation is regular enough to strip rather than needing a precomputed
// table (see import_hu_dictionary.py's docstring for why the source
// dictionary's own conjugation tags were unusable).
//
// Approach: candidate suffix stripping, not generation. Hungarian's suffix
// allomorphs (vowel-harmony variants, sibilant-triggered variants,
// consonant-doubling before instrumental/translative) are enumerated as
// literal strings to try stripping from the end of the observed surface
// form, longest first. A candidate is only accepted if what's left
// resolves — directly in the dictionary, or in the static index (which
// lets a single case-suffix strip resolve a possessive-suffixed
// remainder, covering the stacking case above) — so wrong or coincidental
// allomorphs are filtered by outcome rather than needing correct harmony
// rules up front. This deliberately covers the common/regular case, not
// every irregular stem; see the "Known gaps" note at the end of the file.

const HungarianMorphology = (function () {
    'use strict';

    // Case, possessive and (nominal) plural marking only ever attach to
    // these parts of speech in Hungarian — never a verb. Without this
    // guard, a verb whose bare stem happens to be one letter shorter than
    // its conjugated form ("él" = to live) gets mis-parsed as that stem
    // plus a case/possessive/plural suffix ("élt" -> "él" + accusative
    // "-t", rather than "él" + past-tense "-t") purely because the
    // dictionary lookup succeeded without checking what kind of word it
    // found. Checked at every nominal-suffix dictionary hit below, in both
    // analyze() and ladder().
    const CASEABLE_POS = {
        noun: 1, pronoun: 1, adjective: 1, numeral: 1, determiner: 1, article: 1,
        // A closed class of postpositions personally-inflect the same way
        // ("köztük" = "among them", "belőle" = "out of him/her/it") —
        // rarer than noun/pronoun inflection but real, not a false match.
        postposition: 1
    };
    function isNominal(entry) { return !!entry && !!CASEABLE_POS[entry.type]; }

    // Dictionary entries are arrays of senses (see import_hu_dictionary.py
    // — "él" is both noun "edge" and verb "to live", kept as two entries
    // rather than one arbitrarily discarded). These three pick the ONE
    // sense a given grammatical context actually wants, rather than every
    // caller re-deriving "is this the sense I mean" itself:
    //   nominalSense — for case/possessive/plural suffix contexts, which
    //     can only ever apply to a nominal sense
    //   verbSense    — for conjugation-suffix contexts
    //   anySense     — no grammatical evidence either way (a bare-lemma
    //     direct hit); takes whichever sense sorted first at build time
    //     (see that script's docstring on ordering)
    function nominalSense(dictEntry) {
        if (!dictEntry) return null;
        const senses = Array.isArray(dictEntry) ? dictEntry : [dictEntry];
        return senses.find(isNominal) || null;
    }
    function verbSense(dictEntry) {
        if (!dictEntry) return null;
        const senses = Array.isArray(dictEntry) ? dictEntry : [dictEntry];
        return senses.find(s => s.type === 'verb') || null;
    }
    function anySense(dictEntry) {
        if (!dictEntry) return null;
        return Array.isArray(dictEntry) ? (dictEntry[0] || null) : dictEntry;
    }

    const CASE_LABELS = {
        nom: 'nominative', acc: 'accusative', dat: 'dative',
        ins: 'instrumental', cfi: 'causal-final', tra: 'translative',
        ter: 'terminative', esf: 'essive-formal', esm: 'essive-modal',
        ine: 'inessive ("in")', sup: 'superessive ("on")', ade: 'adessive ("at")',
        ill: 'illative ("into")', sub: 'sublative ("onto")', all: 'allative ("to")',
        ela: 'elative ("out of")', del: 'delative ("off/about")', abl: 'ablative ("from")'
    };

    // The English preposition a case roughly translates as, for building a
    // plain-English phrase in the popup's step-by-step breakdown (see
    // ladder() below) — plainer than CASE_LABELS' linguistic names, which
    // are for the one-line "noun · inessive" summary instead.
    const CASE_PREPOSITION = {
        dat: 'to', ins: 'with', cfi: 'for', tra: 'into', ter: 'up to',
        esf: 'as', ine: 'in', sup: 'on', ade: 'at', ill: 'into',
        sub: 'onto', all: 'to', ela: 'out of', del: 'off', abl: 'from'
    };

    // Longest-first within each case so "-ként" isn't shadowed by a
    // shorter suffix that happens to be a substring of it.
    const CASE_SUFFIXES = [
        ['ként', 'esf'],
        ['ban', 'ine'], ['ben', 'ine'],
        ['ból', 'ela'], ['ből', 'ela'],
        ['ról', 'del'], ['ről', 'del'],
        ['tól', 'abl'], ['től', 'abl'],
        ['nál', 'ade'], ['nél', 'ade'],
        ['hoz', 'all'], ['hez', 'all'], ['höz', 'all'],
        ['nak', 'dat'], ['nek', 'dat'],
        ['ért', 'cfi'],
        ['val', 'ins'], ['vel', 'ins'],
        ['vá', 'tra'], ['vé', 'tra'],
        ['ba', 'ill'], ['be', 'ill'],
        ['ra', 'sub'], ['re', 'sub'],
        ['ig', 'ter'],
        ['on', 'sup'], ['en', 'sup'], ['ön', 'sup'],
        ['at', 'acc'], ['ot', 'acc'], ['et', 'acc'], ['öt', 'acc'], ['t', 'acc']
    ]
        // Instrumental (-val/-vel) and translative (-vá/-vé) assimilate
        // their v to match the stem's final consonant when the stem ends
        // in one ("ház" + val -> "házzal", not "házval") — so the surface
        // suffix is [that consonant] + a/e(+l), which naturally reproduces
        // the doubled letter because the stem already supplied the first
        // copy. Generated rather than hand-enumerated so every consonant
        // gets the same treatment; digraphs (sz, zs, cs, ...) count as one
        // consonant here since that's the unit Hungarian assimilation
        // treats them as.
        .concat((() => {
            const consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'r', 's', 't', 'z', 'cs', 'gy', 'ly', 'ny', 'sz', 'ty', 'zs'];
            const generated = [];
            consonants.forEach(c => {
                generated.push([c + 'al', 'ins'], [c + 'el', 'ins'], [c + 'á', 'tra'], [c + 'é', 'tra']);
            });
            return generated;
        })())
        .sort((a, b) => b[0].length - a[0].length);

    // Possessive suffixes (nominative case only — a stacked case has
    // already been stripped by the time these are tried). Tagged with
    // [suffix, person, ownerNumber, possessedNumber].
    const POSSESSIVE_SUFFIXES = [
        // possessed-plural ("my houses", not just "my house") — longer,
        // tried first
        ['jaim', 1, 'sg', 'pl'], ['jeim', 1, 'sg', 'pl'], ['aim', 1, 'sg', 'pl'], ['eim', 1, 'sg', 'pl'],
        ['jaid', 2, 'sg', 'pl'], ['jeid', 2, 'sg', 'pl'], ['aid', 2, 'sg', 'pl'], ['eid', 2, 'sg', 'pl'],
        ['jai', 3, 'sg', 'pl'], ['jei', 3, 'sg', 'pl'], ['ai', 3, 'sg', 'pl'], ['ei', 3, 'sg', 'pl'],
        ['jaink', 1, 'pl', 'pl'], ['jeink', 1, 'pl', 'pl'], ['aink', 1, 'pl', 'pl'], ['eink', 1, 'pl', 'pl'],
        ['jaitok', 2, 'pl', 'pl'], ['jeitek', 2, 'pl', 'pl'], ['aitok', 2, 'pl', 'pl'], ['eitek', 2, 'pl', 'pl'],
        ['jaik', 3, 'pl', 'pl'], ['jeik', 3, 'pl', 'pl'], ['aik', 3, 'pl', 'pl'], ['eik', 3, 'pl', 'pl'],
        // possessed-singular
        ['am', 1, 'sg', 'sg'], ['em', 1, 'sg', 'sg'], ['om', 1, 'sg', 'sg'], ['öm', 1, 'sg', 'sg'], ['m', 1, 'sg', 'sg'],
        ['ad', 2, 'sg', 'sg'], ['ed', 2, 'sg', 'sg'], ['od', 2, 'sg', 'sg'], ['öd', 2, 'sg', 'sg'], ['d', 2, 'sg', 'sg'],
        // "-a/-e" lengthens to "-á/-é" when a case suffix follows
        // ("eredménye" -> "eredményé-nek") — see the case-suffix loop
        // below, which strips a case first and tries these against what's
        // left, so both the plain and lengthened forms are listed here
        ['ja', 3, 'sg', 'sg'], ['je', 3, 'sg', 'sg'], ['já', 3, 'sg', 'sg'], ['jé', 3, 'sg', 'sg'],
        ['a', 3, 'sg', 'sg'], ['e', 3, 'sg', 'sg'], ['á', 3, 'sg', 'sg'], ['é', 3, 'sg', 'sg'],
        ['unk', 1, 'pl', 'sg'], ['ünk', 1, 'pl', 'sg'], ['nk', 1, 'pl', 'sg'],
        ['otok', 2, 'pl', 'sg'], ['etek', 2, 'pl', 'sg'], ['ötök', 2, 'pl', 'sg'], ['tok', 2, 'pl', 'sg'], ['tek', 2, 'pl', 'sg'],
        ['juk', 3, 'pl', 'sg'], ['jük', 3, 'pl', 'sg'], ['uk', 3, 'pl', 'sg'], ['ük', 3, 'pl', 'sg']
    ].sort((a, b) => b[0].length - a[0].length);

    const PLURAL_SUFFIXES = ['ak', 'ok', 'ek', 'ök', 'k'];

    // Present/past indefinite personal endings. A verb's dictionary lemma
    // already covers bare 3sg present (tanul, olvas) and -ik lemmas cover
    // their own 3sg present (dolgozik) with no stripping needed, so those
    // aren't listed here — this table is only what needs a strip.
    // [suffix, tense, person, number]
    const VERB_SUFFIXES = [
        // present, 1sg — includes -ik verbs' -om/-em/-öm alongside the
        // regular -ok/-ek/-ök, since we validate by outcome rather than
        // knowing in advance whether the stem is an -ik verb
        ['ok', 'pres', 1, 'sg'], ['ek', 'pres', 1, 'sg'], ['ök', 'pres', 1, 'sg'],
        ['om', 'pres', 1, 'sg'], ['em', 'pres', 1, 'sg'], ['öm', 'pres', 1, 'sg'],
        // present, 2sg — plain -sz and the sibilant-stem -ol/-el/-öl variant
        ['asz', 'pres', 2, 'sg'], ['esz', 'pres', 2, 'sg'], ['sz', 'pres', 2, 'sg'],
        ['ol', 'pres', 2, 'sg'], ['el', 'pres', 2, 'sg'], ['öl', 'pres', 2, 'sg'],
        // present, 1pl / 2pl / 3pl
        ['unk', 'pres', 1, 'pl'], ['ünk', 'pres', 1, 'pl'],
        ['otok', 'pres', 2, 'pl'], ['etek', 'pres', 2, 'pl'], ['tok', 'pres', 2, 'pl'], ['tek', 'pres', 2, 'pl'],
        ['nak', 'pres', 3, 'pl'], ['nek', 'pres', 3, 'pl'],
        // present, definite conjugation (the object is a specific "it"/
        // "them" — "olvasom a könyvet" vs indefinite "olvasok"). 1sg is
        // the same surface form as the -ik-verb indefinite already listed
        // above, so isn't repeated here.
        ['od', 'pres', 2, 'sg'], ['ed', 'pres', 2, 'sg'], ['öd', 'pres', 2, 'sg'],
        ['ja', 'pres', 3, 'sg'], ['i', 'pres', 3, 'sg'],
        ['juk', 'pres', 1, 'pl'], ['jük', 'pres', 1, 'pl'],
        ['játok', 'pres', 2, 'pl'], ['itek', 'pres', 2, 'pl'],
        ['ják', 'pres', 3, 'pl'], ['ik', 'pres', 3, 'pl'],
        // past — -t-/-ott-/-ett-/-ött- + personal ending; 3sg has no
        // further ending beyond the tense marker itself. Consonant
        // clusters that can't take a bare -t- (stems already ending in a
        // consonant that clashes with it) need the same -ott-/-ett-/-ött-
        // linking vowel in every person, not just 3sg indefinite
        // ("felfüggesztettek", not "felfüggesztek") — so both the plain
        // and linking-vowel forms are listed for 1pl/2pl/3pl.
        ['tam', 'past', 1, 'sg'], ['tem', 'past', 1, 'sg'],
        ['tál', 'past', 2, 'sg'], ['tél', 'past', 2, 'sg'],
        ['ott', 'past', 3, 'sg'], ['ett', 'past', 3, 'sg'], ['ött', 'past', 3, 'sg'],
        // bare doubled -tt: long-vowel stems take this instead of the
        // -ott/-ett/-ött linking vowel ("nő" -> "nőtt", not "nőött";
        // "fő" -> "főtt", "lő" -> "lőtt")
        ['tt', 'past', 3, 'sg'], ['t', 'past', 3, 'sg'],
        ['tunk', 'past', 1, 'pl'], ['tünk', 'past', 1, 'pl'],
        ['ottunk', 'past', 1, 'pl'], ['ettünk', 'past', 1, 'pl'], ['öttünk', 'past', 1, 'pl'],
        ['tatok', 'past', 2, 'pl'], ['tetek', 'past', 2, 'pl'],
        ['ottatok', 'past', 2, 'pl'], ['ettetek', 'past', 2, 'pl'], ['öttetek', 'past', 2, 'pl'],
        ['tak', 'past', 3, 'pl'], ['tek', 'past', 3, 'pl'],
        ['ottak', 'past', 3, 'pl'], ['ettek', 'past', 3, 'pl'], ['öttek', 'past', 3, 'pl'],
        // past, definite conjugation — 3sg/3pl get the same linking-vowel
        // treatment as indefinite above ("gyűjtötte", not "gyűjtte";
        // "hamisították", not "hamisítták")
        ['tad', 'past', 2, 'sg'], ['ted', 'past', 2, 'sg'],
        ['ta', 'past', 3, 'sg'], ['te', 'past', 3, 'sg'],
        ['otta', 'past', 3, 'sg'], ['ette', 'past', 3, 'sg'], ['ötte', 'past', 3, 'sg'],
        ['tuk', 'past', 1, 'pl'], ['tük', 'past', 1, 'pl'],
        ['tátok', 'past', 2, 'pl'], ['tétek', 'past', 2, 'pl'],
        ['ták', 'past', 3, 'pl'], ['ték', 'past', 3, 'pl'],
        ['ották', 'past', 3, 'pl'], ['ették', 'past', 3, 'pl'], ['ötték', 'past', 3, 'pl']
    ].sort((a, b) => b[0].length - a[0].length);

    const PERSON_LABELS = {
        1: { sg: '1st person singular', pl: '1st person plural' },
        2: { sg: '2nd person singular', pl: '2nd person plural' },
        3: { sg: '3rd person singular', pl: '3rd person plural' }
    };
    const TENSE_LABELS = { pres: 'Present', past: 'Past' };

    // Suppletive verbs — their stem changes shape under conjugation in a
    // way no suffix strip can undo (van -> vagyok, not "vanok"). Too
    // common to leave unresolved (van/lenni is the copula "to be"), too
    // irregular to derive: a hardcoded form -> [lemma, tense, person,
    // number] table, same treatment Spanish gives its own wholly
    // irregular verbs. [suffix table entries don't apply here — these are
    // full surface forms, not stems + endings.]
    const IRREGULAR_VERBS = {
        vagyok: ['van', 'pres', 1, 'sg'], vagy: ['van', 'pres', 2, 'sg'],
        van: ['van', 'pres', 3, 'sg'], vagyunk: ['van', 'pres', 1, 'pl'],
        vagytok: ['van', 'pres', 2, 'pl'], vannak: ['van', 'pres', 3, 'pl'],
        voltam: ['van', 'past', 1, 'sg'], voltál: ['van', 'past', 2, 'sg'],
        volt: ['van', 'past', 3, 'sg'], voltunk: ['van', 'past', 1, 'pl'],
        voltatok: ['van', 'past', 2, 'pl'], voltak: ['van', 'past', 3, 'pl'],

        megyek: ['megy', 'pres', 1, 'sg'], mész: ['megy', 'pres', 2, 'sg'],
        megyünk: ['megy', 'pres', 1, 'pl'], mentek: ['megy', 'pres', 2, 'pl'],
        mennek: ['megy', 'pres', 3, 'pl'],
        mentem: ['megy', 'past', 1, 'sg'], mentél: ['megy', 'past', 2, 'sg'],
        ment: ['megy', 'past', 3, 'sg'], mentünk: ['megy', 'past', 1, 'pl'],
        mentetek: ['megy', 'past', 2, 'pl'],

        jövök: ['jön', 'pres', 1, 'sg'], jössz: ['jön', 'pres', 2, 'sg'],
        jövünk: ['jön', 'pres', 1, 'pl'], jöttök: ['jön', 'pres', 2, 'pl'],
        jönnek: ['jön', 'pres', 3, 'pl'],
        jöttem: ['jön', 'past', 1, 'sg'], jöttél: ['jön', 'past', 2, 'sg'],
        jött: ['jön', 'past', 3, 'sg'], jöttünk: ['jön', 'past', 1, 'pl'],
        jöttetek: ['jön', 'past', 2, 'pl'], jöttek: ['jön', 'past', 3, 'pl'],

        eszem: ['eszik', 'pres', 1, 'sg'], eszel: ['eszik', 'pres', 2, 'sg'],
        eszünk: ['eszik', 'pres', 1, 'pl'], esztek: ['eszik', 'pres', 2, 'pl'],
        esznek: ['eszik', 'pres', 3, 'pl'],
        ettem: ['eszik', 'past', 1, 'sg'], ettél: ['eszik', 'past', 2, 'sg'],
        evett: ['eszik', 'past', 3, 'sg'], ettünk: ['eszik', 'past', 1, 'pl'],
        ettetek: ['eszik', 'past', 2, 'pl'], ettek: ['eszik', 'past', 3, 'pl'],

        iszom: ['iszik', 'pres', 1, 'sg'], iszol: ['iszik', 'pres', 2, 'sg'],
        iszunk: ['iszik', 'pres', 1, 'pl'], isztok: ['iszik', 'pres', 2, 'pl'],
        isznak: ['iszik', 'pres', 3, 'pl'],
        ittam: ['iszik', 'past', 1, 'sg'], ittál: ['iszik', 'past', 2, 'sg'],
        ivott: ['iszik', 'past', 3, 'sg'], ittunk: ['iszik', 'past', 1, 'pl'],
        ittatok: ['iszik', 'past', 2, 'pl'], ittak: ['iszik', 'past', 3, 'pl'],

        alszom: ['alszik', 'pres', 1, 'sg'], alszol: ['alszik', 'pres', 2, 'sg'],
        alszunk: ['alszik', 'pres', 1, 'pl'], alusztok: ['alszik', 'pres', 2, 'pl'],
        alszanak: ['alszik', 'pres', 3, 'pl'],
        aludtam: ['alszik', 'past', 1, 'sg'], aludtál: ['alszik', 'past', 2, 'sg'],
        aludt: ['alszik', 'past', 3, 'sg'], aludtunk: ['alszik', 'past', 1, 'pl'],
        aludtatok: ['alszik', 'past', 2, 'pl'], aludtak: ['alszik', 'past', 3, 'pl'],

        // vesz/tesz/hisz/visz/lesz — present tense is regular (handled by
        // VERB_SUFFIXES stripping), but the past stem shortens irregularly
        // (vesz -> vett-, not "veszt-"), same treatment as the suppletive
        // verbs above. 1sg is the same surface form for definite and
        // indefinite past ("vettem" either way), so only needs one entry;
        // "meg-" combines with several of these constantly (megvette,
        // megvettem, megtette) — see stripKnownPrefix() below for why that
        // still resolves even though these entries only cover the bare form.
        vettem: ['vesz', 'past', 1, 'sg'], vettél: ['vesz', 'past', 2, 'sg'], vetted: ['vesz', 'past', 2, 'sg'],
        vett: ['vesz', 'past', 3, 'sg'], vette: ['vesz', 'past', 3, 'sg'],
        vettünk: ['vesz', 'past', 1, 'pl'], vettük: ['vesz', 'past', 1, 'pl'],
        vettetek: ['vesz', 'past', 2, 'pl'], vettétek: ['vesz', 'past', 2, 'pl'],
        vettek: ['vesz', 'past', 3, 'pl'], vették: ['vesz', 'past', 3, 'pl'],

        tettem: ['tesz', 'past', 1, 'sg'], tettél: ['tesz', 'past', 2, 'sg'], tetted: ['tesz', 'past', 2, 'sg'],
        tett: ['tesz', 'past', 3, 'sg'], tette: ['tesz', 'past', 3, 'sg'],
        tettünk: ['tesz', 'past', 1, 'pl'], tettük: ['tesz', 'past', 1, 'pl'],
        tettetek: ['tesz', 'past', 2, 'pl'], tettétek: ['tesz', 'past', 2, 'pl'],
        tettek: ['tesz', 'past', 3, 'pl'], tették: ['tesz', 'past', 3, 'pl'],

        hittem: ['hisz', 'past', 1, 'sg'], hittél: ['hisz', 'past', 2, 'sg'], hitted: ['hisz', 'past', 2, 'sg'],
        hitt: ['hisz', 'past', 3, 'sg'], hitte: ['hisz', 'past', 3, 'sg'],
        hittünk: ['hisz', 'past', 1, 'pl'], hittük: ['hisz', 'past', 1, 'pl'],
        hittetek: ['hisz', 'past', 2, 'pl'], hittétek: ['hisz', 'past', 2, 'pl'],
        hittek: ['hisz', 'past', 3, 'pl'], hitték: ['hisz', 'past', 3, 'pl'],

        vittem: ['visz', 'past', 1, 'sg'], vittél: ['visz', 'past', 2, 'sg'], vitted: ['visz', 'past', 2, 'sg'],
        vitt: ['visz', 'past', 3, 'sg'], vitte: ['visz', 'past', 3, 'sg'],
        vittünk: ['visz', 'past', 1, 'pl'], vittük: ['visz', 'past', 1, 'pl'],
        vittetek: ['visz', 'past', 2, 'pl'], vittétek: ['visz', 'past', 2, 'pl'],
        vittek: ['visz', 'past', 3, 'pl'], vitték: ['visz', 'past', 3, 'pl'],

        // lesz ("to become") is intransitive — no definite conjugation
        lettem: ['lesz', 'past', 1, 'sg'], lettél: ['lesz', 'past', 2, 'sg'],
        lett: ['lesz', 'past', 3, 'sg'], lettünk: ['lesz', 'past', 1, 'pl'],
        lettetek: ['lesz', 'past', 2, 'pl'], lettek: ['lesz', 'past', 3, 'pl']
    };

    // Separable verbal prefixes — fully productive, and change a verb's
    // meaning in ways too idiomatic to translate mechanically in every
    // case ("eszik" = to eat, "megeszik" = to eat up/finish eating). Only
    // the sense is noted here, not a composed translation. Longest-first
    // so "elő-" isn't shadowed by "el-" matching its own first two letters.
    const VERB_PREFIXES = [
        ['vissza', 'back'], ['össze', 'together'],
        ['meg', 'completive — often "up"/"through"/"done"'],
        ['elő', 'ahead/forward'], ['után', 'after'],
        ['el', 'away'], ['ki', 'out'], ['be', 'in'],
        ['le', 'down'], ['fel', 'up'], ['föl', 'up'],
        ['át', 'across/through'], ['rá', 'onto'], ['ide', 'here'], ['oda', 'there']
    ].sort((a, b) => b[0].length - a[0].length);

    // A prefixed verb often isn't its own dictionary headword even though
    // the bare verb is ("eszik" is listed, "megeszik" usually isn't) — see
    // the "meg-" fallback in analyze() below, which strips a known prefix
    // and re-checks the bare stem (including IRREGULAR_VERBS) when the
    // prefixed form alone doesn't resolve. Requires at least 2 letters left
    // after the prefix so "el" alone (a real word, "the") isn't mistaken
    // for "e" + "l".
    function stripKnownPrefix(word) {
        for (const [prefix, sense] of VERB_PREFIXES) {
            if (word.startsWith(prefix) && word.length - prefix.length >= 2) {
                return { prefix: prefix, sense: sense, stem: word.slice(prefix.length) };
            }
        }
        return null;
    }

    function strip(word, suffix) {
        return word.length > suffix.length && word.endsWith(suffix)
            ? word.slice(0, -suffix.length)
            : null;
    }

    // "my house" / "our friends" / etc, from a POSSESSIVE_SUFFIXES match.
    function describePossessive(person, ownerNumber, possessedNumber) {
        const owner = { 1: { sg: 'my', pl: 'our' }, 2: { sg: 'your', pl: 'your (pl.)' },
            3: { sg: 'his/her', pl: 'their' } }[person][ownerNumber];
        return possessedNumber === 'pl' ? owner + ', plural' : owner;
    }

    // Friendly label for a static word-index entry (see
    // scripts/import_hu_dictionary.py's { lemma, pos, case?, number?,
    // person?, ownerNumber? } shape) — shared by Lexicon.js when it
    // resolves a form directly from the static index, and by analyze()
    // above for its own remainders, so both paths describe a form the
    // same way.
    function describe(a) {
        const bits = [];
        if (a.person) {
            // describePossessive() already reports possessed-plural itself
            // ("my, plural") — number here is the possessed noun's number,
            // not a separate fact to restate.
            bits.push(describePossessive(a.person, a.ownerNumber, a.number));
            if (a.case) bits.push(CASE_LABELS[a.case] || a.case);
        } else {
            // A plain noun form can be BOTH cased and plural at once
            // ("házak" = nominative plural) — these aren't mutually
            // exclusive, so both get reported when both are present
            // rather than the case silently swallowing the plural.
            if (a.case) bits.push(CASE_LABELS[a.case] || a.case);
            if (a.number === 'pl') bits.push('plural');
        }
        return bits.join(', ');
    }

    // Crude English pluralization for a ladder phrase's noun ("friend" ->
    // "friends"). Good enough for the common case; irregular English
    // plurals (child/children) are a known, accepted miss rather than a
    // reason to ship a full pluralization table for what's a teaching aid.
    function naivePluralize(noun) {
        if (/[sxz]$/i.test(noun) || /[cs]h$/i.test(noun)) return noun + 'es';
        if (/[^aeiou]y$/i.test(noun)) return noun.slice(0, -1) + 'ies';
        return noun + 's';
    }

    // "my friend" / "our friends" / etc, as a natural phrase rather than
    // describePossessive()'s compact "my, plural" label — used by ladder()
    // below, where the point is to read like English, not like a tag.
    function possessivePhrase(gloss, person, ownerNumber, possessedNumber) {
        const owner = { 1: { sg: 'my', pl: 'our' }, 2: { sg: 'your', pl: 'your' },
            3: { sg: 'his/her', pl: 'their' } }[person][ownerNumber];
        const noun = possessedNumber === 'pl' ? naivePluralize(gloss) : gloss;
        return owner + ' ' + noun;
    }

    function caseName(caseCode) { return CASE_LABELS[caseCode] || caseCode; }

    // Splits a possessive suffix into its own sub-morphemes for the
    // popup's per-suffix breakdown table — "-aim" isn't atomic, it's the
    // plural-possessed marker "-ai-" ("houses/friends", not "house/friend")
    // plus the 1st-person owner marker "-m" ("my"). Only 1st/2nd person
    // plural-possessed forms split cleanly this way; 3rd person singular
    // owner has no separate trailing person letter at all ("barátai" =
    // "his/her friends" is fully carried by "-ai" alone), so that one stays
    // a single row rather than a fake second one with nothing in it.
    function splitPossessiveSuffix(suffixStr, person, ownerNumber, possessedNumber) {
        const wholeLabel = describePossessive(person, ownerNumber, possessedNumber);
        if (possessedNumber !== 'pl') return [{ suffix: suffixStr, label: wholeLabel }];
        const m = suffixStr.match(/^(j?[ae]i)(.*)$/);
        if (!m || !m[2]) return [{ suffix: suffixStr, label: wholeLabel }];
        const personLabel = { 1: { sg: 'my', pl: 'our' }, 2: { sg: 'your', pl: 'your' },
            3: { sg: 'his/her', pl: 'their' } }[person][ownerNumber];
        return [
            { suffix: m[1], label: 'plural/possessive' },
            { suffix: m[2], label: personLabel }
        ];
    }

    // The preposition-or-caseName label for a case suffix, for the
    // breakdown table's per-suffix row ("-mal" -> "with").
    function caseSuffixLabel(caseCode) { return CASE_PREPOSITION[caseCode] || caseName(caseCode); }

    // Plain-language reason for a verb-suffix allomorph that isn't the
    // "default" ending — this is what actually makes "nőtt" explainable
    // rather than just recognisable: a learner who sees the breakdown
    // table's "-tt" row wants to know why it isn't "-ett", not just that
    // it means "past, 3rd person". Returns null for the ordinary case,
    // where there's nothing surprising to explain.
    function verbSuffixWhy(suffix) {
        if (suffix === 'tt') {
            return 'Stems ending in a long vowel double the "t" directly instead of adding a linking vowel.';
        }
        if (/^(ott|ett|ött)/.test(suffix)) {
            return 'A linking vowel (o/e/ö) is inserted so "-t" doesn’t collide with the stem’s own final consonant.';
        }
        if (suffix === 'ol' || suffix === 'el' || suffix === 'öl') {
            return 'Stems ending in a hissing sound (s, sz, z) take "-ol/-el/-öl" here instead of "-sz", which would be awkward to say.';
        }
        return null;
    }

    // Same idea for a case suffix: instrumental/translative assimilate
    // their "v" to match the stem's final consonant ("ház" + val ->
    // "házzal", not "házval") — see CASE_SUFFIXES' own generated block
    // above for how those variants are built. Anything other than the
    // plain -val/-vel/-vá/-vé form is one of them.
    const PLAIN_VA_VE = { val: 1, vel: 1, vá: 1, vé: 1 };
    function caseSuffixWhy(suffix, caseCode) {
        if ((caseCode === 'ins' || caseCode === 'tra') && !PLAIN_VA_VE[suffix]) {
            return '-val/-vel (and -vá/-vé) change their "v" to match the sound right before them.';
        }
        return null;
    }

    /**
     * Step-by-step build-up of a Hungarian word for the Reader popup.
     * Returns { chain, breakdown }: chain is the cumulative forms
     * ("barátaimmal" -> [barát: friend, barátaim: my friends,
     * barátaimmal: with my friends]); breakdown is the individual
     * suffixes added along the way ([-ai: plural/possessive, -m: my,
     * -mal: with]) — the popup shows the chain as a compact arrow list
     * and the breakdown as a small table underneath.
     *
     * Deliberately traces the SAME decomposition analyze() actually found
     * (same case/possessive tables, same order) rather than independently
     * generating forms — every step shown is a form the resolution
     * genuinely passed through, not a synthesized comparison that could be
     * wrong about which suffix allomorph the word actually needs. Returns
     * { chain: [], breakdown: [] } when there's nothing to stack (the word
     * already is the lemma, or it's a verb form — conjugation doesn't
     * stack the way case/possessive do, so there's no ladder to show).
     *
     * A form can be ambiguous between an unrelated verb and a noun+suffix
     * reading — "lakom" is both "lakik" ("I dwell", present 1sg) and "lak"
     * + possessive ("my dwelling"). This function only ever searches
     * case/possessive tables, so left to itself it always finds the noun
     * reading, even when frequency ranking picked the verb as primary.
     * targetLemma pins the search to that winning reading: a candidate
     * whose base lemma doesn't match is skipped rather than accepted, so
     * the ladder never contradicts the reading the popup shows above it.
     * Pass null/omit to take whatever's found first (only safe when
     * there's no such ambiguity to worry about).
     */
    function ladder(word, dictionary, wordIndex, targetLemma) {
        const empty = { chain: [], breakdown: [] };
        if (!word || dictionary[word]) return empty;
        // sense is an already-resolved nominalSense() object, never a raw
        // (possibly multi-sense) dictionary entry — same reasoning as
        // analyze()'s addFromLemma above.
        const gloss = sense => (typeof Lexicon !== 'undefined' && Lexicon.shortGloss)
            ? Lexicon.shortGloss(sense.en) : sense.en;
        // "to hotel" reads wrong in English; "with my friends" doesn't need
        // it since the possessive already makes the noun definite — only
        // the bare-noun-plus-case branch needs an article added.
        const withArticle = (base, type) => type === 'noun' ? 'the ' + base : base;
        const matches = lemma => !targetLemma || lemma === targetLemma;

        for (const [suffix, caseCode] of CASE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const prep = CASE_PREPOSITION[caseCode];
            const caseBreakdown = { suffix: suffix, label: caseSuffixLabel(caseCode) };
            const caseWhy = caseSuffixWhy(suffix, caseCode);
            if (caseWhy) caseBreakdown.why = caseWhy;

            const remainderSense = nominalSense(dictionary[remainder]);
            if (remainderSense && matches(remainder)) {
                const plainGloss = gloss(remainderSense);
                const base = withArticle(plainGloss, remainderSense.type);
                return {
                    chain: [
                        { form: remainder, translation: plainGloss },
                        { form: word, translation: prep ? prep + ' ' + base : base + ' (' + caseName(caseCode) + ')' }
                    ],
                    breakdown: [caseBreakdown]
                };
            }

            // a.person is required — this branch assumes a possessive form
            // (feeds possessivePhrase() below), and a plain case-only
            // word-index entry for the same remainder (no .person) would
            // otherwise match first and crash possessivePhrase on a
            // missing person.
            const indexHit = (wordIndex[remainder] || [])
                .find(a => a.person && nominalSense(dictionary[a.lemma]) && matches(a.lemma));
            if (indexHit) {
                const base = gloss(nominalSense(dictionary[indexHit.lemma]));
                const possPhrase = possessivePhrase(base, indexHit.person, indexHit.ownerNumber, indexHit.number);
                return {
                    chain: [
                        { form: indexHit.lemma, translation: base },
                        { form: remainder, translation: possPhrase },
                        { form: word, translation: prep ? prep + ' ' + possPhrase : possPhrase + ' (' + caseName(caseCode) + ')' }
                    ],
                    breakdown: splitPossessiveSuffix(
                        remainder.slice(indexHit.lemma.length), indexHit.person, indexHit.ownerNumber, indexHit.number
                    ).concat(caseBreakdown)
                };
            }

            // One layer deeper: a possessive suffix under the case, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative) — same
            // reach as analyze()'s own deeper chain, so the ladder covers
            // exactly what the resolved reading actually found.
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                const deeperSense = deeper !== null ? nominalSense(dictionary[deeper]) : null;
                if (!deeperSense || !matches(deeper)) continue;
                const base = gloss(deeperSense);
                const possPhrase = possessivePhrase(base, person, ownerNumber, possessedNumber);
                return {
                    chain: [
                        { form: deeper, translation: base },
                        { form: remainder, translation: possPhrase },
                        { form: word, translation: prep ? prep + ' ' + possPhrase : possPhrase + ' (' + caseName(caseCode) + ')' }
                    ],
                    breakdown: splitPossessiveSuffix(possSuffix, person, ownerNumber, possessedNumber).concat(caseBreakdown)
                };
            }
        }

        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            const sense = remainder !== null ? nominalSense(dictionary[remainder]) : null;
            if (!sense || !matches(remainder)) continue;
            const base = gloss(sense);
            return {
                chain: [
                    { form: remainder, translation: base },
                    { form: word, translation: possessivePhrase(base, person, ownerNumber, possessedNumber) }
                ],
                breakdown: splitPossessiveSuffix(suffix, person, ownerNumber, possessedNumber)
            };
        }

        // Plain plural, no case or possessive ("aratók" = arató + -k,
        // "reapers") — the simplest stack there is, but easy to miss since
        // it doesn't go through either loop above; without this, every
        // plain plural noun/adjective/pronoun fell through to no ladder
        // at all despite being exactly the kind of stacking this exists
        // to show.
        for (const suffix of PLURAL_SUFFIXES) {
            const remainder = strip(word, suffix);
            const sense = remainder !== null ? nominalSense(dictionary[remainder]) : null;
            if (!sense || !matches(remainder)) continue;
            const base = gloss(sense);
            return {
                chain: [
                    { form: remainder, translation: base },
                    { form: word, translation: naivePluralize(base) }
                ],
                breakdown: [{ suffix: suffix, label: 'plural' }]
            };
        }

        // Verb conjugation ("nőtt" = nő + -tt, past tense) — this is the
        // case that actually motivated adding "why" notes at all: a
        // suffix like "-tt" or "-ott" isn't obvious from the label alone,
        // and a learner asking "why is it nőtt, not nőett?" deserves a
        // real answer, not just "past tense". Skipped for IRREGULAR_VERBS
        // matches on purpose — a suppletive stem (van -> voltam) has no
        // clean stem+ending split worth drawing a chain for.
        for (const [suffix, tense, person, number] of VERB_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            let sense = verbSense(dictionary[remainder]);
            let lemma = remainder;
            if (!sense) {
                sense = verbSense(dictionary[remainder + 'ik']);
                lemma = remainder + 'ik';
            }
            if (!sense || !matches(lemma)) continue;
            const base = gloss(sense);
            const label = [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', ');
            const breakdown = { suffix: suffix, label: label };
            const why = verbSuffixWhy(suffix);
            if (why) breakdown.why = why;
            return {
                chain: [
                    { form: lemma, translation: base },
                    { form: word, translation: base + ' (' + label + ')' }
                ],
                breakdown: [breakdown]
            };
        }

        return empty;
    }

    /**
     * Try to resolve a Hungarian surface form the dictionary and static
     * word-index didn't recognise directly. dictionary and wordIndex are
     * Lexicon's already-loaded data (passed in rather than imported, so
     * this module has no load-order dependency on Lexicon).
     *
     * Returns a list of candidate readings (same shape Lexicon.lookup()
     * already produces for Spanish: { lemma, pos, translation, analysis }),
     * or an empty list if nothing resolves.
     */
    function analyze(word, dictionary, wordIndex) {
        const results = [];
        const seen = new Set();

        // sense is an already-resolved single sense object (from
        // nominalSense()/verbSense()/anySense() above) — never a raw
        // dictionary entry, so this never has to guess which of a
        // multi-sense lemma's readings applies; the caller already decided
        // that from grammatical context (case suffix -> nominal sense,
        // conjugation suffix -> verb sense).
        function addFromLemma(lemma, sense, analysisText) {
            if (!sense) return false;
            const key = lemma + '|' + analysisText;
            if (seen.has(key)) return true;
            seen.add(key);
            results.push({ lemma: lemma, pos: sense.type, translation: sense.en, analysis: analysisText });
            return true;
        }

        // A prefixed verb whose exact prefixed form isn't its own
        // dictionary headword ("megeszik" isn't listed even though "eszik"
        // is) — reconstructs the citation form (prefix + baseLemma) and
        // borrows the base verb's translation, noting the prefix's rough
        // sense separately rather than composing a translation that could
        // be wrong about exactly how the prefix shifted the meaning.
        function addPrefixedVerb(prefix, sense, baseLemma, analysisText) {
            const baseSense = verbSense(dictionary[baseLemma]);
            if (!baseSense) return false;
            const lemma = prefix + baseLemma;
            const key = lemma + '|' + analysisText;
            if (seen.has(key)) return true;
            seen.add(key);
            results.push({
                lemma: lemma, pos: 'verb',
                translation: baseSense.en + ' (+ ' + prefix + '-: ' + sense + ')',
                analysis: analysisText
            });
            return true;
        }

        // 0. suppletive verbs — checked first since these can't be
        // reached by stripping a suffix off the dictionary lemma at all
        const irregular = IRREGULAR_VERBS[word];
        if (irregular) {
            const [lemma, tense, person, number] = irregular;
            addFromLemma(lemma, verbSense(dictionary[lemma]),
                [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', '));
        } else {
            const pfx = stripKnownPrefix(word);
            const stemIrregular = pfx && IRREGULAR_VERBS[pfx.stem];
            if (stemIrregular) {
                const [baseLemma, tense, person, number] = stemIrregular;
                addPrefixedVerb(pfx.prefix, pfx.sense, baseLemma,
                    [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', '));
            }
        }

        // A remainder left after stripping a case suffix — check whether
        // it's a bare lemma, or itself a possessive form from the static
        // index (this is what resolves "házamban": strip "-ban", and
        // "házam" is already in word-index as ház + possessive 1sg).
        function resolveRemainder(remainder, caseLabel) {
            let hit = false;
            const sense = nominalSense(dictionary[remainder]);
            if (sense) {
                hit = addFromLemma(remainder, sense, caseLabel) || hit;
            }
            // a.person required — this branch exists to catch a possessive
            // form stacked under a case ("házamban" = "házam" + "-ban";
            // "házam" carries a.person). A plain case-only word-index entry
            // for the same remainder ("nőt" = "nő" + accusative) isn't a
            // possessive form at all — accepting it here would read "nőtt"
            // as "nő" plus a nonsensical double accusative instead of
            // giving the past-tense verb reading ("nő" the verb, "to grow")
            // a chance to be found instead.
            (wordIndex[remainder] || []).forEach(a => {
                if (!a.person) return;
                const aSense = nominalSense(dictionary[a.lemma]);
                if (!aSense) return;
                const bits = [describePossessive(a.person, a.ownerNumber, a.number)];
                if (caseLabel) bits.push(caseLabel);
                hit = addFromLemma(a.lemma, aSense, bits.join(', ')) || hit;
            });
            return hit;
        }

        // 1. verb personal ending, present or past — tried before any
        // nominal suffix. Where a bare stem is ambiguous between a nominal
        // case reading and a verb conjugation reading of the SAME lemma
        // spelling ("élt" = "él" the noun "edge" + accusative "-t", or
        // "él" the verb "to live" + past "-t" — both grammatically real),
        // there's no per-sense frequency data to break the tie with, only
        // lemma-level frequency, which is identical either way. Trying
        // verb suffixes first — so a verb reading is already in `results`
        // before a same-lemma case reading could out-rank it on a tied
        // score — resolved every such collision found while building this
        // ("nőtt", "élt", "örült"): the verb sense was the one a learner
        // actually needed. "-ik" is tried as an alternate lemma form since
        // many verb dictionary headwords include it (dolgozik) while the
        // stem alone (dolgoz) is not a separate entry.
        for (const [suffix, tense, person, number] of VERB_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const label = [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', ');
            const remainderSense = verbSense(dictionary[remainder]);
            if (remainderSense) {
                addFromLemma(remainder, remainderSense, label);
            }
            const ikForm = remainder + 'ik';
            const ikSense = verbSense(dictionary[ikForm]);
            if (ikSense) {
                addFromLemma(ikForm, ikSense, label);
            }

            // Neither the bare remainder nor its -ik form is a headword —
            // try peeling a known prefix off it too ("megettem" strips
            // "-em" or the irregular table catches it whole, but
            // "megettél" needs "-él" stripped first, leaving "megett",
            // which still needs "meg-" stripped to reach the dictionary's
            // "eszik"/base-stem coverage).
            if (!remainderSense && !ikSense) {
                const pfx = stripKnownPrefix(remainder);
                if (pfx) {
                    if (verbSense(dictionary[pfx.stem])) {
                        addPrefixedVerb(pfx.prefix, pfx.sense, pfx.stem, label);
                    }
                    const pfxIk = pfx.stem + 'ik';
                    if (verbSense(dictionary[pfxIk])) {
                        addPrefixedVerb(pfx.prefix, pfx.sense, pfxIk, label);
                    }
                }
            }
        }

        // 2. case suffix, optionally stacked over a possessive/plural form
        for (const [suffix, caseCode] of CASE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const caseLabel = CASE_LABELS[caseCode];
            if (resolveRemainder(remainder, caseLabel)) continue;
            // one more layer down: plural marker under the case suffix
            // ("házakban" = ház + plural + inessive)
            for (const plSuffix of PLURAL_SUFFIXES) {
                const deeper = strip(remainder, plSuffix);
                const deeperSense = deeper !== null ? nominalSense(dictionary[deeper]) : null;
                if (deeperSense) {
                    addFromLemma(deeper, deeperSense, caseLabel + ', plural');
                }
            }
            // ...or a possessive suffix under the case suffix, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative,
            // where "eredményének" itself was never common enough to be
            // pre-baked but "eredmény" the lemma still is)
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                const deeperSense = deeper !== null ? nominalSense(dictionary[deeper]) : null;
                if (deeperSense) {
                    addFromLemma(deeper, deeperSense,
                        describePossessive(person, ownerNumber, possessedNumber) + ', ' + caseLabel);
                }
            }
        }

        // 3. possessive suffix alone (no case) — for lemmas outside the
        // static index's frequency cutoff
        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            const sense = remainder !== null ? nominalSense(dictionary[remainder]) : null;
            if (!sense) continue;
            addFromLemma(remainder, sense, describePossessive(person, ownerNumber, possessedNumber));
        }

        // 4. plural marker alone — nouns mainly, but pronouns/determiners
        // pluralize the same way ("az" -> "azok", "ami" -> "amik"). Labelled
        // "nominative, plural", not just "plural" — this strips the bare
        // marker straight off the nominative stem with no case suffix
        // involved, and matching the word-index's own label for the exact
        // same fact (see describe() above) means the two agree and dedupe
        // as one reading instead of showing as two near-identical ones.
        for (const suffix of PLURAL_SUFFIXES) {
            const remainder = strip(word, suffix);
            const sense = remainder !== null ? nominalSense(dictionary[remainder]) : null;
            if (sense) {
                addFromLemma(remainder, sense, 'nominative, plural');
            }
        }

        return results;
    }

    return {
        analyze: analyze, describe: describe, ladder: ladder, isNominal: isNominal,
        nominalSense: nominalSense, verbSense: verbSense, anySense: anySense
    };
})();

// Known gaps (v1, deliberately deferred rather than blocking the first
// version — see HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md). Measured
// against a real Hungarian news article (2026-08-19): 232/276 running
// words resolved (84%); nearly all of the remaining misses are proper
// nouns/acronyms (correctly not matching) or lemmas the dictionary
// itself doesn't have yet (see import_hu_dictionary.py's docstring on
// dictionary size), not suffix-stripping failures. VERB_PREFIXES/
// stripKnownPrefix() (2026-08-19 follow-up) covers the 15 most common
// separable prefixes (meg-, el-, ki-, be-, le-, fel-, össze-, át-,
// vissza-, rá-, ide-, oda-, elő-, után-); rarer ones (agyon-, félre-,
// tovább-, ...) aren't covered. Remaining real analyser gaps:
//   - suppletive verbs beyond IRREGULAR_VERBS above (van/megy/jön/eszik/
//     iszik/alszik/vesz/tesz/hisz/visz/lesz cover the most curriculum-
//     critical ones; Hungarian has a few more with less common irregular
//     stems)
//   - stem-vowel deletion before a vowel-initial suffix ("tükör" ->
//     "tükr-öm", not "tüköröm") — affects a closed, learnable set of
//     nouns (tükör, majom, bokor, álom, torok, ...) but isn't derivable
//     from the surface form alone the way suffix-stripping is; would need
//     a small lexical list of which nouns do this
//   - the noun -> adjective "-i" suffix ("kiértékelés" -> "kiértékelési",
//     "the evaluation's") isn't in POSSESSIVE_SUFFIXES or CASE_SUFFIXES
//     since it's neither — a third suffix category not yet modelled
