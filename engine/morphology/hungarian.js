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
        ['ott', 'past', 3, 'sg'], ['ett', 'past', 3, 'sg'], ['ött', 'past', 3, 'sg'], ['t', 'past', 3, 'sg'],
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
        aludtatok: ['alszik', 'past', 2, 'pl'], aludtak: ['alszik', 'past', 3, 'pl']
    };

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
        if (a.person) bits.push(describePossessive(a.person, a.ownerNumber, a.number));
        if (a.case) bits.push(CASE_LABELS[a.case] || a.case);
        else if (!a.person && a.number === 'pl') bits.push('plural');
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

    /**
     * Step-by-step build-up of a Hungarian word for the Reader popup —
     * "barátaimmal" -> [barát: friend, barátaim: my friends, barátaimmal:
     * with my friends] — so a learner sees how the pieces stack rather
     * than just a compact "my, plural, instrumental" label.
     *
     * Deliberately traces the SAME decomposition analyze() actually found
     * (same case/possessive tables, same order) rather than independently
     * generating forms — every step shown is a form the resolution
     * genuinely passed through, not a synthesized comparison that could be
     * wrong about which suffix allomorph the word actually needs. Returns
     * [] when there's nothing to stack (the word already is the lemma, or
     * it's a verb form — conjugation doesn't stack the way case/possessive
     * do, so there's no ladder worth showing).
     */
    function ladder(word, dictionary, wordIndex) {
        if (!word || dictionary[word]) return [];
        const gloss = lemma => (typeof Lexicon !== 'undefined' && Lexicon.shortGloss)
            ? Lexicon.shortGloss(dictionary[lemma].en) : dictionary[lemma].en;
        // "to hotel" reads wrong in English; "with my friends" doesn't need
        // it since the possessive already makes the noun definite — only
        // the bare-noun-plus-case branch needs an article added.
        const withArticle = (base, type) => type === 'noun' ? 'the ' + base : base;

        for (const [suffix, caseCode] of CASE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const prep = CASE_PREPOSITION[caseCode];

            if (dictionary[remainder]) {
                const base = withArticle(gloss(remainder), dictionary[remainder].type);
                return [
                    { form: remainder, translation: gloss(remainder) },
                    { form: word, translation: prep ? prep + ' ' + base : base + ' (' + caseName(caseCode) + ')' }
                ];
            }

            const indexHit = (wordIndex[remainder] || [])[0];
            if (indexHit && dictionary[indexHit.lemma]) {
                const base = gloss(indexHit.lemma);
                const possPhrase = possessivePhrase(base, indexHit.person, indexHit.ownerNumber, indexHit.number);
                return [
                    { form: indexHit.lemma, translation: base },
                    { form: remainder, translation: possPhrase },
                    { form: word, translation: prep ? prep + ' ' + possPhrase : possPhrase + ' (' + caseName(caseCode) + ')' }
                ];
            }

            // One layer deeper: a possessive suffix under the case, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative) — same
            // reach as analyze()'s own deeper chain, so the ladder covers
            // exactly what the resolved reading actually found.
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                if (deeper === null || !dictionary[deeper]) continue;
                const base = gloss(deeper);
                const possPhrase = possessivePhrase(base, person, ownerNumber, possessedNumber);
                return [
                    { form: deeper, translation: base },
                    { form: remainder, translation: possPhrase },
                    { form: word, translation: prep ? prep + ' ' + possPhrase : possPhrase + ' (' + caseName(caseCode) + ')' }
                ];
            }
        }

        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null || !dictionary[remainder]) continue;
            const base = gloss(remainder);
            return [
                { form: remainder, translation: base },
                { form: word, translation: possessivePhrase(base, person, ownerNumber, possessedNumber) }
            ];
        }

        return [];
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

        function addFromLemma(lemma, pos, analysisText) {
            const entry = dictionary[lemma];
            if (!entry) return false;
            const key = lemma + '|' + analysisText;
            if (seen.has(key)) return true;
            seen.add(key);
            results.push({
                lemma: lemma, pos: entry.type || pos || '',
                translation: entry.en, analysis: analysisText
            });
            return true;
        }

        // 0. suppletive verbs — checked first since these can't be
        // reached by stripping a suffix off the dictionary lemma at all
        const irregular = IRREGULAR_VERBS[word];
        if (irregular) {
            const [lemma, tense, person, number] = irregular;
            addFromLemma(lemma, 'verb', [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', '));
        }

        // A remainder left after stripping a case suffix — check whether
        // it's a bare lemma, or itself a possessive form from the static
        // index (this is what resolves "házamban": strip "-ban", and
        // "házam" is already in word-index as ház + possessive 1sg).
        function resolveRemainder(remainder, caseLabel) {
            let hit = false;
            if (dictionary[remainder]) {
                hit = addFromLemma(remainder, dictionary[remainder].type, caseLabel) || hit;
            }
            (wordIndex[remainder] || []).forEach(a => {
                const bits = [];
                if (a.person) bits.push(describePossessive(a.person, a.ownerNumber, a.number));
                if (caseLabel) bits.push(caseLabel);
                hit = addFromLemma(a.lemma, a.pos, bits.join(', ') || describe(a)) || hit;
            });
            return hit;
        }

        // 1. case suffix, optionally stacked over a possessive/plural form
        for (const [suffix, caseCode] of CASE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const caseLabel = CASE_LABELS[caseCode];
            if (resolveRemainder(remainder, caseLabel)) continue;
            // one more layer down: plural marker under the case suffix
            // ("házakban" = ház + plural + inessive)
            for (const plSuffix of PLURAL_SUFFIXES) {
                const deeper = strip(remainder, plSuffix);
                if (deeper !== null && dictionary[deeper]) {
                    addFromLemma(deeper, dictionary[deeper].type, caseLabel + ', plural');
                }
            }
            // ...or a possessive suffix under the case suffix, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative,
            // where "eredményének" itself was never common enough to be
            // pre-baked but "eredmény" the lemma still is)
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                if (deeper !== null && dictionary[deeper]) {
                    addFromLemma(deeper, dictionary[deeper].type,
                        describePossessive(person, ownerNumber, possessedNumber) + ', ' + caseLabel);
                }
            }
        }

        // 2. possessive suffix alone (no case) — for lemmas outside the
        // static index's frequency cutoff
        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null || !dictionary[remainder]) continue;
            addFromLemma(remainder, dictionary[remainder].type,
                describePossessive(person, ownerNumber, possessedNumber));
        }

        // 3. plural marker alone — nouns mainly, but pronouns/determiners
        // pluralize the same way ("az" -> "azok", "ami" -> "amik")
        const PLURALIZABLE = { noun: 1, pronoun: 1, determiner: 1, adjective: 1, article: 1 };
        for (const suffix of PLURAL_SUFFIXES) {
            const remainder = strip(word, suffix);
            const entry = remainder !== null ? dictionary[remainder] : null;
            if (entry && PLURALIZABLE[entry.type]) {
                addFromLemma(remainder, entry.type, 'plural');
            }
        }

        // 4. verb personal ending, present or past. "-ik" is tried as an
        // alternate lemma form since many verb dictionary headwords
        // include it (dolgozik) while the stem alone (dolgoz) is not a
        // separate entry.
        for (const [suffix, tense, person, number] of VERB_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const label = [TENSE_LABELS[tense], PERSON_LABELS[person][number]].join(', ');
            if (dictionary[remainder] && dictionary[remainder].type === 'verb') {
                addFromLemma(remainder, 'verb', label);
            }
            const ikForm = remainder + 'ik';
            if (dictionary[ikForm] && dictionary[ikForm].type === 'verb') {
                addFromLemma(ikForm, 'verb', label);
            }
        }

        return results;
    }

    return { analyze: analyze, describe: describe, ladder: ladder };
})();

// Known gaps (v1, deliberately deferred rather than blocking the first
// version — see HUNGARIAN_READER_IMPLEMENTATION_BRIEF.md). Measured
// against a real Hungarian news article (2026-08-19): 232/276 running
// words resolved (84%); nearly all of the remaining misses are proper
// nouns/acronyms (correctly not matching) or lemmas the dictionary
// itself doesn't have yet (see import_hu_dictionary.py's docstring on
// dictionary size), not suffix-stripping failures. Two real analyser
// gaps remain, both narrower than they first look:
//   - suppletive verbs beyond IRREGULAR_VERBS above (van/megy/jön/eszik/
//     iszik/alszik cover the most curriculum-critical ones; Hungarian has
//     a few more with less common irregular stems)
//   - stem-vowel deletion before a vowel-initial suffix ("tükör" ->
//     "tükr-öm", not "tüköröm") — affects a closed, learnable set of
//     nouns (tükör, majom, bokor, álom, torok, ...) but isn't derivable
//     from the surface form alone the way suffix-stripping is; would need
//     a small lexical list of which nouns do this
//   - the noun -> adjective "-i" suffix ("kiértékelés" -> "kiértékelési",
//     "the evaluation's") isn't in POSSESSIVE_SUFFIXES or CASE_SUFFIXES
//     since it's neither — a third suffix category not yet modelled
