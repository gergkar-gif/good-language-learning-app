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

    // Hungarian's low vowel lengthening: a stem ending in short "a"/"e"
    // lengthens to "á"/"é" before almost every suffix ("intelligencia" ->
    // "intelligenciával", not "intelligenciaval") — a spelling change, not
    // just a sound one, so stripping a suffix by string length alone can
    // leave a remainder ("intelligenciá") that doesn't literally match its
    // own dictionary headword ("intelligencia"). Confirmed live: the word-
    // index already resolves these correctly (it's built from Wiktionary's
    // own pre-inflected declension tables, so the lengthened spelling is
    // baked in), but analyze()/ladder()'s own string-stripping — needed
    // for anything outside the word-index's frequency cutoff, or for the
    // ladder's independent re-derivation — didn't know to shorten back.
    function delengthen(form) {
        if (form.endsWith('á')) return form.slice(0, -1) + 'a';
        if (form.endsWith('é')) return form.slice(0, -1) + 'e';
        return null;
    }

    // nominalSense(dictionary[remainder]), with the delengthened spelling
    // tried as a fallback when the literal remainder isn't a headword.
    // Returns { lemma, sense } (lemma is whichever spelling actually
    // resolved — not necessarily `remainder` itself) or null.
    function resolveNominal(dictionary, remainder) {
        if (remainder == null) return null;
        let sense = nominalSense(dictionary[remainder]);
        if (sense) return { lemma: remainder, sense: sense };
        const shortened = delengthen(remainder);
        if (shortened) {
            sense = nominalSense(dictionary[shortened]);
            if (sense) return { lemma: shortened, sense: sense };
        }
        return null;
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
        // present, 1pl / 2pl / 3pl. 2pl's front-rounded variants ("üt" ->
        // "üttök", "küld" -> "küldötök") and 3pl's cluster-final linking-
        // vowel variant ("ért" -> "értenek", "mond" -> "mondanak") were
        // missing here until conjugate() below was round-trip tested
        // against this table (2026-08-19) and caught real words it
        // couldn't decode.
        ['unk', 'pres', 1, 'pl'], ['ünk', 'pres', 1, 'pl'],
        ['otok', 'pres', 2, 'pl'], ['etek', 'pres', 2, 'pl'], ['ötök', 'pres', 2, 'pl'],
        ['tok', 'pres', 2, 'pl'], ['tek', 'pres', 2, 'pl'], ['tök', 'pres', 2, 'pl'],
        ['nak', 'pres', 3, 'pl'], ['nek', 'pres', 3, 'pl'], ['anak', 'pres', 3, 'pl'], ['enek', 'pres', 3, 'pl'],
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
        // and linking-vowel forms are listed for 1sg/2sg/1pl/2pl/3pl (the
        // 1sg/2sg linking variants — "értettem", "javítottál" — were
        // missing until conjugate()'s past-tense generator was round-trip
        // tested against this table and caught real words it couldn't
        // decode, 2026-08-20, same pattern as the earlier 2pl/3pl fix
        // above).
        ['tam', 'past', 1, 'sg'], ['tem', 'past', 1, 'sg'],
        ['ottam', 'past', 1, 'sg'], ['ettem', 'past', 1, 'sg'], ['öttem', 'past', 1, 'sg'],
        ['tál', 'past', 2, 'sg'], ['tél', 'past', 2, 'sg'],
        ['ottál', 'past', 2, 'sg'], ['ettél', 'past', 2, 'sg'], ['öttél', 'past', 2, 'sg'],
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
    ]
    // Conditional and imperative personal endings (2026-08-29 follow-up —
    // see conjugate()'s own generation-side comment for the full
    // derivation and confidence notes; this table only needs the literal
    // strings, decoded by strip-and-validate like everything else here).
    // Both moods harmonize back/front only (2-way, "a/e"), collapsing
    // front-rounded into front-unrounded — unlike present/past tense's
    // 3-way back/front-unrounded/front-rounded split for several cells
    // (e.g. -ok/-ek/-ök) — EXCEPT imperative 3sg, which keeps the
    // indicative's own 3-way -on/-en/-ön grade (cross-checked against
    // "maradjon"/"beszéljen" already in content/hu/grammar, and "jöjjön"
    // found live in content/hu — see IRREGULAR_VERBS below for jön's
    // suppletive imperative stem). A linking vowel ("a" back / "e" front,
    // same 2-way pattern) is needed before either marker on a
    // cluster-final stem, same test as _needsLinkingVowel already uses
    // for present tense — so both the bare and linking-vowel variant of
    // every cell are listed here, exactly like VERB_SUFFIXES above
    // already does for present/past.
    //
    // Conditional indefinite 1sg ("-nék") is invariant regardless of
    // harmony — well-attested (cross-checked against content/hu/grammar's
    // own "szeretnék"/"szeretnél"/"szeretne"/"szeretnétek" cards, all
    // front-harmony, plus an independent back-harmony check against
    // "várnék/várnál/várna/várnánk/várnátok/várnának"). Conditional
    // definite 1pl/2pl are genuinely identical strings to indefinite
    // (a real Hungarian syncretism, not a gap) so aren't repeated below.
    // Front-harmony conditional indefinite-1sg and definite-3pl are ALSO
    // genuinely homophonous in real Hungarian ("kérnék" = both "I would
    // ask" and "they would ask it") — both readings are listed below on
    // purpose, not a mistake.
    .concat([
        // -- conditional, indefinite --
        ['nék', 'cond', 1, 'sg'],
        ['anék', 'cond', 1, 'sg'], ['enék', 'cond', 1, 'sg'],
        ['nál', 'cond', 2, 'sg'], ['nél', 'cond', 2, 'sg'],
        ['anál', 'cond', 2, 'sg'], ['enél', 'cond', 2, 'sg'],
        ['na', 'cond', 3, 'sg'], ['ne', 'cond', 3, 'sg'],
        ['ana', 'cond', 3, 'sg'], ['ene', 'cond', 3, 'sg'],
        ['nánk', 'cond', 1, 'pl'], ['nénk', 'cond', 1, 'pl'],
        ['anánk', 'cond', 1, 'pl'], ['enénk', 'cond', 1, 'pl'],
        ['nátok', 'cond', 2, 'pl'], ['nétek', 'cond', 2, 'pl'],
        ['anátok', 'cond', 2, 'pl'], ['enétek', 'cond', 2, 'pl'],
        ['nának', 'cond', 3, 'pl'], ['nének', 'cond', 3, 'pl'],
        ['anának', 'cond', 3, 'pl'], ['enének', 'cond', 3, 'pl'],
        // -- conditional, definite --
        ['nám', 'cond', 1, 'sg'], ['ném', 'cond', 1, 'sg'],
        ['anám', 'cond', 1, 'sg'], ['eném', 'cond', 1, 'sg'],
        ['nád', 'cond', 2, 'sg'], ['néd', 'cond', 2, 'sg'],
        ['anád', 'cond', 2, 'sg'], ['enéd', 'cond', 2, 'sg'],
        ['ná', 'cond', 3, 'sg'], ['né', 'cond', 3, 'sg'],
        ['aná', 'cond', 3, 'sg'], ['ené', 'cond', 3, 'sg'],
        ['nák', 'cond', 3, 'pl'], ['nék', 'cond', 3, 'pl'],
        ['anák', 'cond', 3, 'pl'], ['enék', 'cond', 3, 'pl'],
        // -- imperative, indefinite (see conjugate()'s own comment for
        // which stem classes this reliably covers vs declines) --
        //
        // Unlike the conditional's "n" marker just above, "j" attaches
        // directly to a stem's final consonant with NO linking vowel
        // ever, even when that stem is already cluster-final — confirmed
        // by "küldj" (send!, from cluster-final "küld") behaving the same
        // as "várj" (wait!, from single-consonant-final "vár"), both
        // bare stem + j with nothing inserted between them. So, unlike
        // every other suffix table in this file, there's no bare/linking-
        // vowel pair to list per cell here — just one row each.
        ['jak', 'imp', 1, 'sg'], ['jek', 'imp', 1, 'sg'],
        ['j', 'imp', 2, 'sg'],
        ['jon', 'imp', 3, 'sg'], ['jen', 'imp', 3, 'sg'], ['jön', 'imp', 3, 'sg'],
        ['junk', 'imp', 1, 'pl'], ['jünk', 'imp', 1, 'pl'],
        ['jatok', 'imp', 2, 'pl'], ['jetek', 'imp', 2, 'pl'],
        ['janak', 'imp', 3, 'pl'], ['jenek', 'imp', 3, 'pl'],
        // sibilant-final stems (s and z — see _isSibilantFinal, which
        // also covers the "sz" digraph, NOT handled here; see the gap
        // note below): "j" assimilates into a doubled copy of the stem's
        // own final consonant ("olvas" -> "olvass-", "néz" -> "nézz-"),
        // same gemination mechanic _conjugatePresentDefinite already uses
        // for definite present's own "j"-initial endings. Because the
        // doubled letter is just a literal extra copy of the stem's own
        // final character, every cell — including 2sg, which for a
        // regular non-sibilant stem is bare "-j" with no vowel at all
        // ("Várj!") — decodes as plain suffix-stripping like everything
        // else in this table: "olvass" minus "s" leaves "olvas", the
        // real headword, no special-case code needed.
        ['son', 'imp', 3, 'sg'], ['sen', 'imp', 3, 'sg'],
        ['sunk', 'imp', 1, 'pl'], ['sünk', 'imp', 1, 'pl'],
        ['satok', 'imp', 2, 'pl'], ['setek', 'imp', 2, 'pl'],
        ['sanak', 'imp', 3, 'pl'], ['senek', 'imp', 3, 'pl'],
        ['sak', 'imp', 1, 'sg'], ['sek', 'imp', 1, 'sg'], ['s', 'imp', 2, 'sg'],
        ['zon', 'imp', 3, 'sg'], ['zen', 'imp', 3, 'sg'],
        ['zunk', 'imp', 1, 'pl'], ['zünk', 'imp', 1, 'pl'],
        ['zatok', 'imp', 2, 'pl'], ['zetek', 'imp', 2, 'pl'],
        ['zanak', 'imp', 3, 'pl'], ['zenek', 'imp', 3, 'pl'],
        ['zak', 'imp', 1, 'sg'], ['zek', 'imp', 1, 'sg'], ['z', 'imp', 2, 'sg'],
        // "-ít"-suffixed stems (tanít, javít, gyógyít, ...) and t-final
        // stems preceded by a SONORANT (ért, tart, bánt, ... — reusing
        // PAST_TYPE_I_SONORANTS' r/l/n/ny/j/ly, same extrapolation
        // _imperativeMarker's own comment flags) need NO extra rows
        // here either: unlike s/z stems, these don't assimilate at
        // all — the imperative is just the bare stem (with its own "t"
        // untouched) + the SAME plain "s" endings above ("taníts",
        // "tarts", not "taníss"/"tarss") — so the 's'/'son'/'sunk'/...
        // rows just above already decode "tanítson"/"tartson" -> the
        // real headword by stripping only their own literal suffix, no
        // separate entry needed. (An earlier version of this table had
        // redundant, and for 2sg actively wrong, "ts"-prefixed rows
        // here — caught before shipping by checking "taníts" minus "ts"
        // would leave "taní", not the real headword "tanít".)
        //
        // -- imperative, DEFINITE (2026-08-29 follow-up — see
        // _conjugateImperativeDefinite's own comment for the full
        // derivation) — 2sg takes a SINGULAR (non-doubled) version of
        // whatever marker the stem would otherwise double: bare "-d" for
        // a regular or plain-sibilant stem ("várd"/"olvasd"/"nézd"/
        // "mondd" — the sibilant classes still leave one copy of their
        // own final consonant in place, same as everywhere else in this
        // table), but "-sd" for the "-ít"/sonorant-t class specifically,
        // which keeps its own unassimilated "t" ("tartsd", not "tartd" —
        // an easy trap, since it LOOKS like it should pattern with
        // "mondd"'s bare-d but doesn't; caught by this follow-up's own
        // external check after first shipping the wrong "tartd" guess).
        ['jam', 'imp', 1, 'sg'], ['jem', 'imp', 1, 'sg'],
        ['d', 'imp', 2, 'sg'], ['sd', 'imp', 2, 'sg'],
        ['ja', 'imp', 3, 'sg'], ['je', 'imp', 3, 'sg'],
        ['juk', 'imp', 1, 'pl'], ['jük', 'imp', 1, 'pl'],
        ['játok', 'imp', 2, 'pl'], ['jétek', 'imp', 2, 'pl'],
        ['ják', 'imp', 3, 'pl'], ['jék', 'imp', 3, 'pl'],
        // Same sibilant-gemination logic as indefinite above, just with
        // the definite endings' own vowel — leaves one copy of the
        // stem's own final s/z in the remainder either way ("olvassa"
        // minus "sa" -> "olvas"; "nézze" minus "ze" -> "néz"). Also
        // covers the "-ít"/sonorant-t class for free, same as indefinite.
        ['sam', 'imp', 1, 'sg'], ['sem', 'imp', 1, 'sg'],
        ['sa', 'imp', 3, 'sg'], ['se', 'imp', 3, 'sg'],
        ['suk', 'imp', 1, 'pl'], ['sük', 'imp', 1, 'pl'],
        ['sátok', 'imp', 2, 'pl'], ['sétek', 'imp', 2, 'pl'],
        ['sák', 'imp', 3, 'pl'], ['sék', 'imp', 3, 'pl'],
        ['zam', 'imp', 1, 'sg'], ['zem', 'imp', 1, 'sg'],
        ['za', 'imp', 3, 'sg'], ['ze', 'imp', 3, 'sg'],
        ['zuk', 'imp', 1, 'pl'], ['zük', 'imp', 1, 'pl'],
        ['zátok', 'imp', 2, 'pl'], ['zétek', 'imp', 2, 'pl'],
        ['zák', 'imp', 3, 'pl'], ['zék', 'imp', 3, 'pl']
        //
        // Genuinely NOT covered by plain suffix-stripping — decoded
        // instead by _decodeTReplacedImperative() below, called
        // separately from analyze() itself, since these need the
        // remainder's tail RECONSTRUCTED (a "t" put back), not just
        // accepted-or-rejected as-is: single-t-after-vowel stems OUTSIDE
        // the "-ít"/sonorant class (fizet, nevet, siet, lát, ...), whose
        // imperative replaces the stem's own "t" with a doubled "ss"
        // ("fizess", not "fizets"), and t-after-SIBILANT stems (választ,
        // fest, ...), whose imperative drops the "t" and geminates the
        // sibilant instead ("válassz", "fess") — both cross-checked
        // externally this follow-up (see _imperativeMarker's own
        // comment for sources). Still declined entirely, in both
        // directions: the "sz" digraph on its own (a genuine sz-final
        // stem's imperative, not one whose "sz" came from an absorbed
        // "t") — the most common sz-final verbs (eszik, iszik) are
        // already covered via IRREGULAR_VERBS, so this is a narrow gap.
    ])
    .sort((a, b) => b[0].length - a[0].length);

    const PERSON_LABELS = {
        1: { sg: '1st person singular', pl: '1st person plural' },
        2: { sg: '2nd person singular', pl: '2nd person plural' },
        3: { sg: '3rd person singular', pl: '3rd person plural' }
    };
    const TENSE_LABELS = { pres: 'Present', past: 'Past', cond: 'Conditional', imp: 'Imperative' };

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
        lettetek: ['lesz', 'past', 2, 'pl'], lettek: ['lesz', 'past', 3, 'pl'],

        // Conditional (2026-08-29 follow-up) — every suppletive verb above
        // takes a THIRD stem here, distinct from both its present and past
        // stems: drop "-ni" from the verb's infinitive (van's is "lenni",
        // shared with lesz, but van itself uses its own historical "vol-"
        // instead — "volna" being one of the most common words in the
        // language) and attach the regular conditional endings from the
        // MOOD_SUFFIXES table above. Concatenating that stem with an
        // n-initial ending naturally produces the doubled "nn" spelling
        // seen throughout (men+nék=mennék, en+nék=ennék, ...) — it's just
        // orthography, not a separate doubling rule to encode. Indefinite
        // only, same scope present tense already keeps for these same
        // lemmas: vesz/tesz/hisz/visz's conditional definite forms exist
        // in real Hungarian (e.g. "venném" = "I would buy it") but are
        // genuinely homophonous with OTHER cells for these same verbs
        // (front-harmony definite-3pl and indefinite-1sg coincide, see the
        // MOOD_SUFFIXES comment above) — a single flat surfaceForm->tag
        // map can't hold two different tags under one key the way the
        // regular suffix table can (multiple rows, same string), so
        // rather than silently pick a wrong winner, definite forms for
        // this whole group are left out here entirely.
        volnék: ['van', 'cond', 1, 'sg'], volnál: ['van', 'cond', 2, 'sg'],
        volna: ['van', 'cond', 3, 'sg'], volnánk: ['van', 'cond', 1, 'pl'],
        volnátok: ['van', 'cond', 2, 'pl'], volnának: ['van', 'cond', 3, 'pl'],

        mennék: ['megy', 'cond', 1, 'sg'], mennél: ['megy', 'cond', 2, 'sg'],
        menne: ['megy', 'cond', 3, 'sg'], mennénk: ['megy', 'cond', 1, 'pl'],
        mennétek: ['megy', 'cond', 2, 'pl'], mennének: ['megy', 'cond', 3, 'pl'],

        jönnék: ['jön', 'cond', 1, 'sg'], jönnél: ['jön', 'cond', 2, 'sg'],
        jönne: ['jön', 'cond', 3, 'sg'], jönnénk: ['jön', 'cond', 1, 'pl'],
        jönnétek: ['jön', 'cond', 2, 'pl'], jönnének: ['jön', 'cond', 3, 'pl'],

        ennék: ['eszik', 'cond', 1, 'sg'], ennél: ['eszik', 'cond', 2, 'sg'],
        enne: ['eszik', 'cond', 3, 'sg'], ennénk: ['eszik', 'cond', 1, 'pl'],
        ennétek: ['eszik', 'cond', 2, 'pl'], ennének: ['eszik', 'cond', 3, 'pl'],

        innék: ['iszik', 'cond', 1, 'sg'], innál: ['iszik', 'cond', 2, 'sg'],
        inna: ['iszik', 'cond', 3, 'sg'], innánk: ['iszik', 'cond', 1, 'pl'],
        innátok: ['iszik', 'cond', 2, 'pl'], innának: ['iszik', 'cond', 3, 'pl'],

        // alszik's conditional stem "alud-" is the SAME stem its past
        // tense already uses (aludtam etc. above) — not a coincidence,
        // both are alszik's one non-present stem — but still needs its
        // own entries here since "alud" alone isn't the dictionary
        // headword "alszik", so plain suffix-stripping can't reach it.
        aludnék: ['alszik', 'cond', 1, 'sg'], aludnál: ['alszik', 'cond', 2, 'sg'],
        aludna: ['alszik', 'cond', 3, 'sg'], aludnánk: ['alszik', 'cond', 1, 'pl'],
        aludnátok: ['alszik', 'cond', 2, 'pl'], aludnának: ['alszik', 'cond', 3, 'pl'],

        lennék: ['lesz', 'cond', 1, 'sg'], lennél: ['lesz', 'cond', 2, 'sg'],
        lenne: ['lesz', 'cond', 3, 'sg'], lennénk: ['lesz', 'cond', 1, 'pl'],
        lennétek: ['lesz', 'cond', 2, 'pl'], lennének: ['lesz', 'cond', 3, 'pl'],

        vennék: ['vesz', 'cond', 1, 'sg'], vennél: ['vesz', 'cond', 2, 'sg'],
        venne: ['vesz', 'cond', 3, 'sg'], vennénk: ['vesz', 'cond', 1, 'pl'],
        vennétek: ['vesz', 'cond', 2, 'pl'], vennének: ['vesz', 'cond', 3, 'pl'],

        tennék: ['tesz', 'cond', 1, 'sg'], tennél: ['tesz', 'cond', 2, 'sg'],
        tenne: ['tesz', 'cond', 3, 'sg'], tennénk: ['tesz', 'cond', 1, 'pl'],
        tennétek: ['tesz', 'cond', 2, 'pl'], tennének: ['tesz', 'cond', 3, 'pl'],

        hinnék: ['hisz', 'cond', 1, 'sg'], hinnél: ['hisz', 'cond', 2, 'sg'],
        hinne: ['hisz', 'cond', 3, 'sg'], hinnénk: ['hisz', 'cond', 1, 'pl'],
        hinnétek: ['hisz', 'cond', 2, 'pl'], hinnének: ['hisz', 'cond', 3, 'pl'],

        vinnék: ['visz', 'cond', 1, 'sg'], vinnél: ['visz', 'cond', 2, 'sg'],
        vinne: ['visz', 'cond', 3, 'sg'], vinnénk: ['visz', 'cond', 1, 'pl'],
        vinnétek: ['visz', 'cond', 2, 'pl'], vinnének: ['visz', 'cond', 3, 'pl'],

        // Imperative (2026-08-29 follow-up) — a FOURTH stem per verb again
        // (van has none of its own at all: Hungarian has no direct "be!"
        // command built on van — it borrows lesz's légy/legyen family for
        // exactly that meaning, so van itself contributes no entries
        // here). eszik/iszik/vesz/tesz/hisz/visz share an irregular 2sg
        // shape too — an extra "-él"/"-ál" rather than the bare "-j"
        // every regular verb takes (see MOOD_SUFFIXES above) — the same
        // palatal-final stems (egy-, igy-, vegy-, tegy-, higgy-, vigy-)
        // that can't cleanly take a bare "j" the way "vár"/"küld" can.
        // légy (lesz, 2sg) is irregular even by THIS group's own pattern
        // (not "legyél") — kept as its own entry rather than derived.
        menjek: ['megy', 'imp', 1, 'sg'], menj: ['megy', 'imp', 2, 'sg'],
        menjen: ['megy', 'imp', 3, 'sg'], menjünk: ['megy', 'imp', 1, 'pl'],
        menjetek: ['megy', 'imp', 2, 'pl'], menjenek: ['megy', 'imp', 3, 'pl'],

        jöjjek: ['jön', 'imp', 1, 'sg'], jöjj: ['jön', 'imp', 2, 'sg'],
        jöjjön: ['jön', 'imp', 3, 'sg'], jöjjünk: ['jön', 'imp', 1, 'pl'],
        jöjjetek: ['jön', 'imp', 2, 'pl'], jöjjenek: ['jön', 'imp', 3, 'pl'],

        egyek: ['eszik', 'imp', 1, 'sg'], egyél: ['eszik', 'imp', 2, 'sg'],
        egyen: ['eszik', 'imp', 3, 'sg'], együnk: ['eszik', 'imp', 1, 'pl'],
        egyetek: ['eszik', 'imp', 2, 'pl'], egyenek: ['eszik', 'imp', 3, 'pl'],

        igyak: ['iszik', 'imp', 1, 'sg'], igyál: ['iszik', 'imp', 2, 'sg'],
        igyon: ['iszik', 'imp', 3, 'sg'], igyunk: ['iszik', 'imp', 1, 'pl'],
        igyatok: ['iszik', 'imp', 2, 'pl'], igyanak: ['iszik', 'imp', 3, 'pl'],

        // alszik's imperative is fully regular off its "alud-" stem (bare
        // "-j", like any other single-consonant-after-vowel stem) — still
        // needs explicit entries for the same reason its conditional does
        // above ("alud" isn't the headword).
        aludjak: ['alszik', 'imp', 1, 'sg'], aludj: ['alszik', 'imp', 2, 'sg'],
        aludjon: ['alszik', 'imp', 3, 'sg'], aludjunk: ['alszik', 'imp', 1, 'pl'],
        aludjatok: ['alszik', 'imp', 2, 'pl'], aludjanak: ['alszik', 'imp', 3, 'pl'],

        legyek: ['lesz', 'imp', 1, 'sg'], légy: ['lesz', 'imp', 2, 'sg'],
        legyen: ['lesz', 'imp', 3, 'sg'], legyünk: ['lesz', 'imp', 1, 'pl'],
        legyetek: ['lesz', 'imp', 2, 'pl'], legyenek: ['lesz', 'imp', 3, 'pl'],

        vegyek: ['vesz', 'imp', 1, 'sg'], vegyél: ['vesz', 'imp', 2, 'sg'],
        vegyen: ['vesz', 'imp', 3, 'sg'], vegyünk: ['vesz', 'imp', 1, 'pl'],
        vegyetek: ['vesz', 'imp', 2, 'pl'], vegyenek: ['vesz', 'imp', 3, 'pl'],

        tegyek: ['tesz', 'imp', 1, 'sg'], tegyél: ['tesz', 'imp', 2, 'sg'],
        tegyen: ['tesz', 'imp', 3, 'sg'], tegyünk: ['tesz', 'imp', 1, 'pl'],
        tegyetek: ['tesz', 'imp', 2, 'pl'], tegyenek: ['tesz', 'imp', 3, 'pl'],

        higgyek: ['hisz', 'imp', 1, 'sg'], higgyél: ['hisz', 'imp', 2, 'sg'],
        higgyen: ['hisz', 'imp', 3, 'sg'], higgyünk: ['hisz', 'imp', 1, 'pl'],
        higgyetek: ['hisz', 'imp', 2, 'pl'], higgyenek: ['hisz', 'imp', 3, 'pl'],

        vigyek: ['visz', 'imp', 1, 'sg'], vigyél: ['visz', 'imp', 2, 'sg'],
        vigyen: ['visz', 'imp', 3, 'sg'], vigyünk: ['visz', 'imp', 1, 'pl'],
        vigyetek: ['visz', 'imp', 2, 'pl'], vigyenek: ['visz', 'imp', 3, 'pl']
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

    // Hungarian's "-kodik/-kedik/-ködik" derivational suffix attaches to a
    // verb stem to intensify or add reciprocity to its action ("osztozik"
    // "to share" -> "osztozkodik" "to share out, to keep sharing with each
    // other") — productive enough that the derived form usually isn't its
    // own dictionary headword even when the base verb is. `stem` here has
    // already had its personal verb ending stripped (VERB_SUFFIXES), so
    // this only needs to peel the bare "kod/ked/köd" tail, mirroring how
    // the "-ik" fallback just above it peels a different verb-class tail.
    const FREQUENTATIVE_TAILS = ['kod', 'ked', 'köd'];
    function stripFrequentative(stem) {
        for (const tail of FREQUENTATIVE_TAILS) {
            const shortened = strip(stem, tail);
            if (shortened !== null) return shortened;
        }
        return null;
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
    //
    // `pos`, when passed, gates this to nouns only — an adjective or
    // participle gloss doesn't pluralize in English ("fresh" stays
    // "fresh"), so a non-noun pos returns the gloss unchanged instead of
    // producing "freshs". Also trims a trailing "…" (Lexicon.shortGloss()
    // truncates long multi-sense glosses with one) and pluralizes only the
    // FIRST comma-separated sense, dropping the rest — pluralizing the
    // whole string used to tack "s" straight onto the ellipsis
    // ("unprovoked…s") or, when the LAST of several senses got the "s",
    // read as a singular/plural mismatch mid-phrase ("sour cream,
    // smetanas"). Callers that don't have a pos to pass (pos omitted)
    // still get this cleanup, just without the noun-only gate.
    function naivePluralize(gloss, pos) {
        if (pos && pos !== 'noun') return gloss;
        const noun = String(gloss || '').split(',')[0].replace(/[…\s]+$/, '').trim();
        if (!noun) return gloss;
        if (/[sxz]$/i.test(noun) || /[cs]h$/i.test(noun)) return noun + 'es';
        if (/[^aeiou]y$/i.test(noun)) return noun.slice(0, -1) + 'ies';
        return noun + 's';
    }

    // "my friend" / "our friends" / etc, as a natural phrase rather than
    // describePossessive()'s compact "my, plural" label — used by ladder()
    // below, where the point is to read like English, not like a tag.
    function possessivePhrase(gloss, person, ownerNumber, possessedNumber, pos) {
        const owner = { 1: { sg: 'my', pl: 'our' }, 2: { sg: 'your', pl: 'your' },
            3: { sg: 'his/her', pl: 'their' } }[person][ownerNumber];
        const noun = possessedNumber === 'pl' ? naivePluralize(gloss, pos) : gloss;
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
        if (possessedNumber !== 'pl') return [{ suffix: suffixStr, label: wholeLabel, concept: 'possessive' }];
        const m = suffixStr.match(/^(j?[ae]i)(.*)$/);
        if (!m || !m[2]) return [{ suffix: suffixStr, label: wholeLabel, concept: 'possessive' }];
        const personLabel = { 1: { sg: 'my', pl: 'our' }, 2: { sg: 'your', pl: 'your' },
            3: { sg: 'his/her', pl: 'their' } }[person][ownerNumber];
        return [
            { suffix: m[1], label: 'plural/possessive', concept: 'possessive' },
            { suffix: m[2], label: personLabel, concept: 'possessive' }
        ];
    }

    // The preposition-or-caseName label for a case suffix, for the
    // breakdown table's per-suffix row ("-mal" -> "with").
    function caseSuffixLabel(caseCode) { return CASE_PREPOSITION[caseCode] || caseName(caseCode); }

    // The bare English preposition for a case, or null when the case has
    // none (nominative, accusative, essive-modal — grammatical cases with
    // no locational/instrumental English equivalent). Unlike
    // caseSuffixLabel() above, this never falls back to the case name, so
    // callers building a natural-English phrase ("to mugs", not "dative
    // mugs") can tell the two situations apart instead of treating a
    // missing preposition as if it were one.
    function casePreposition(caseCode) { return CASE_PREPOSITION[caseCode] || null; }

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

    // Content parts only — a function word (postposition, conjunction,
    // particle, pronoun, determiner, article, interjection) makes for a
    // nonsense split ("vala" isn't a compound of two real short words
    // just because both halves happen to also be spellable words).
    const COMPOUND_PART_POS = { noun: 1, verb: 1, adjective: 1, adverb: 1, numeral: 1 };
    const MIN_COMPOUND_PART = 3;

    // Hungarian compounding is fully productive (gyümölcs + lé ->
    // gyümölcslé, "fruit juice") and routinely produces words no
    // dictionary — however large — will ever fully enumerate. When
    // nothing else resolves a word at all, try splitting it into two
    // known dictionary words and offer their combined meaning as a
    // literal, word-by-word guess. This is deliberately the LAST resort
    // (only ever reached when analyze() and ladder() both come up empty
    // for a word) and is never treated as if it were a real dictionary
    // definition of the whole compound — callers must label it as a
    // literal/compositional guess, not present it as authoritative.
    // Scans left-to-right and takes the first valid split rather than
    // every possible one: Hungarian compounds are normally exactly two
    // meaningful parts, and the leftmost split is the one a reader
    // parsing the word left-to-right would find first too.
    function splitCompound(word, dictionary) {
        for (let i = MIN_COMPOUND_PART; i <= word.length - MIN_COMPOUND_PART; i++) {
            const left = word.slice(0, i);
            const right = word.slice(i);
            const leftSense = anySense(dictionary[left]);
            const rightSense = anySense(dictionary[right]);
            if (leftSense && rightSense && COMPOUND_PART_POS[leftSense.type] && COMPOUND_PART_POS[rightSense.type]) {
                return { left: left, leftSense: leftSense, right: right, rightSense: rightSense };
            }
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

        // Verb conjugation is checked FIRST, before any nominal suffix —
        // matching analyze()'s and lexicon.js's own tie-break order (see
        // their comments on "nőtt"/"élt"/"örült"). Without this agreement,
        // a lemma spelling with a spurious/rare nominal sense could win the
        // ladder even when ranking correctly picked the verb reading as
        // primary — exactly what happened with "kérem": "kér" carries an
        // obscure noun sense (a historical tribe name) alongside its
        // everyday verb sense "to ask for", and the CASE/POSSESSIVE loops
        // below would happily explain "-em" as "my [tribe]" before ever
        // reaching the correct "present, 1st person singular" verb
        // explanation, even though readings[0] was already the verb.
        // ("nőtt" = nő + -tt, past tense) is the case that motivated the
        // "why" notes at all: a suffix like "-tt" or "-ott" isn't obvious
        // from the label alone, and a learner asking "why is it nőtt, not
        // nőett?" deserves a real answer, not just "past tense". Skipped
        // for IRREGULAR_VERBS matches on purpose — a suppletive stem
        // (van -> voltam) has no clean stem+ending split worth drawing a
        // chain for.
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

        for (const [suffix, caseCode] of CASE_SUFFIXES) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            const prep = CASE_PREPOSITION[caseCode];
            // `concept` is the same key content/hu/reference/cases.json uses
            // (a case code, or 'plural'/'possessive' elsewhere in this
            // function) — purely additive, existing consumers only read
            // .suffix/.label/.why. Lets a caller like hu-morphology.js's
            // Workshop driller look up a general reference for whichever
            // suffix layer a question is actually about.
            const caseBreakdown = { suffix: suffix, label: caseSuffixLabel(caseCode), concept: caseCode };
            const caseWhy = caseSuffixWhy(suffix, caseCode);
            if (caseWhy) caseBreakdown.why = caseWhy;

            const resolved = resolveNominal(dictionary, remainder);
            if (resolved && matches(resolved.lemma)) {
                const plainGloss = gloss(resolved.sense);
                const base = withArticle(plainGloss, resolved.sense.type);
                return {
                    chain: [
                        { form: resolved.lemma, translation: plainGloss },
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
                const indexHitSense = nominalSense(dictionary[indexHit.lemma]);
                const base = gloss(indexHitSense);
                const possPhrase = possessivePhrase(base, indexHit.person, indexHit.ownerNumber, indexHit.number, indexHitSense.type);
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

            // One layer deeper: a plural marker under the case
            // ("megjelenteknek" = megjelent + plural "-ek" + dative
            // "-nek") — same reach as analyze()'s own deeper chain (see
            // its "one more layer down: plural marker under the case
            // suffix" comment), which is what actually resolves this kind
            // of word; without the matching branch here, it translated
            // correctly but showed no breakdown at all.
            for (const plSuffix of PLURAL_SUFFIXES) {
                const deeper = strip(remainder, plSuffix);
                const deeperResolved = resolveNominal(dictionary, deeper);
                if (!deeperResolved || !matches(deeperResolved.lemma)) continue;
                const base = gloss(deeperResolved.sense);
                const pluralPhrase = naivePluralize(base, deeperResolved.sense.type);
                return {
                    chain: [
                        { form: deeperResolved.lemma, translation: base },
                        { form: remainder, translation: pluralPhrase },
                        { form: word, translation: prep ? prep + ' ' + pluralPhrase : pluralPhrase + ' (' + caseName(caseCode) + ')' }
                    ],
                    breakdown: [{ suffix: plSuffix, label: 'plural', concept: 'plural' }, caseBreakdown]
                };
            }

            // One layer deeper: a possessive suffix under the case, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative) — same
            // reach as analyze()'s own deeper chain, so the ladder covers
            // exactly what the resolved reading actually found.
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                const deeperResolved = resolveNominal(dictionary, deeper);
                if (!deeperResolved || !matches(deeperResolved.lemma)) continue;
                const base = gloss(deeperResolved.sense);
                const possPhrase = possessivePhrase(base, person, ownerNumber, possessedNumber, deeperResolved.sense.type);
                return {
                    chain: [
                        { form: deeperResolved.lemma, translation: base },
                        { form: remainder, translation: possPhrase },
                        { form: word, translation: prep ? prep + ' ' + possPhrase : possPhrase + ' (' + caseName(caseCode) + ')' }
                    ],
                    breakdown: splitPossessiveSuffix(possSuffix, person, ownerNumber, possessedNumber).concat(caseBreakdown)
                };
            }
        }

        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            const resolved = resolveNominal(dictionary, remainder);
            if (!resolved || !matches(resolved.lemma)) continue;
            const base = gloss(resolved.sense);
            return {
                chain: [
                    { form: resolved.lemma, translation: base },
                    { form: word, translation: possessivePhrase(base, person, ownerNumber, possessedNumber, resolved.sense.type) }
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
            const resolved = resolveNominal(dictionary, remainder);
            if (!resolved || !matches(resolved.lemma)) continue;
            const base = gloss(resolved.sense);
            return {
                chain: [
                    { form: resolved.lemma, translation: base },
                    { form: word, translation: naivePluralize(base, resolved.sense.type) }
                ],
                breakdown: [{ suffix: suffix, label: 'plural', concept: 'plural' }]
            };
        }

        return empty;
    }

    // Decodes the two imperative t-final classes _imperativeMarker's own
    // comment describes as needing "the remainder's tail reconstructed",
    // not just accepted-or-rejected: t-after-vowel stems (fizet -> the
    // "t" replaced by doubled "ss") and t-after-sibilant stems (választ
    // -> the "t" dropped, the sibilant doubled instead). Both classes
    // leave a word whose ending literally isn't a valid suffix of the
    // real headword — no strip of it can ever land back on "fizet" or
    // "választ" — so unlike everything else in this file, this doesn't
    // try suffixes from a table; it tries STRIPPING the marker+ending
    // combination, then PUTTING A "t" (and, for the sibilant case, the
    // sibilant that "t" replaced) BACK before checking the dictionary.
    //
    // AFTER_MARKER lists what comes after the doubled letters for every
    // cell this covers, independent of which doubling produced them
    // (mirrors the "rest" pieces _conjugateImperativeDefinite computes,
    // plus indefinite's own endings) — GEMINATIONS lists every doubled
    // spelling this session found real Hungarian producing and what to
    // reconstruct in its place. Trying every (ending, doubling) pair
    // against real dictionary data is exactly this file's usual
    // "generate candidates, keep whichever resolves" approach; it's just
    // that resolving here means transforming the remainder, not merely
    // accepting it.
    const T_REPLACED_AFTER_MARKER = [
        // [afterMarker, person, number, definite]
        ['', 2, 'sg', false],
        ['ak', 1, 'sg', false], ['ek', 1, 'sg', false],
        ['on', 3, 'sg', false], ['en', 3, 'sg', false], ['ön', 3, 'sg', false],
        ['unk', 1, 'pl', false], ['ünk', 1, 'pl', false],
        ['atok', 2, 'pl', false], ['etek', 2, 'pl', false],
        ['anak', 3, 'pl', false], ['enek', 3, 'pl', false],
        ['am', 1, 'sg', true], ['em', 1, 'sg', true],
        ['a', 3, 'sg', true], ['e', 3, 'sg', true],
        ['uk', 1, 'pl', true], ['ük', 1, 'pl', true],
        ['átok', 2, 'pl', true], ['étek', 2, 'pl', true],
        ['ák', 3, 'pl', true], ['ék', 3, 'pl', true]
    ];
    // [doubledSpelling, reconstructedTail] — "ss" is genuinely ambiguous
    // between the vowel-preceded-t class (reconstructs as bare "t") and
    // the s-preceded-t class (reconstructs as "st"), so both are tried;
    // whichever one resolves against the dictionary wins, same as every
    // other genuine ambiguity in this file.
    const T_REPLACED_GEMINATIONS = [['ss', 't'], ['ss', 'st'], ['zz', 'zt'], ['ssz', 'szt']];
    // Definite 2sg is its own special case, not covered by the loop
    // below: _singularizeMarker's own comment explains why it takes a
    // SINGULAR marker rather than doubling like every other cell, so the
    // reconstruction here tries putting "t" back after only ONE copy of
    // "s"/"z" (not two) — "fizesd" -> "fizet" (single "s" removed,
    // replaced by "t"), "válaszd" -> "választ" (nothing removed at all;
    // the "sz" was never doubled at this cell to begin with, so "t" is
    // simply appended after it).
    const T_REPLACED_2SG_DEFINITE = [['sd', 't'], ['sd', 'st'], ['zd', 'zt'], ['szd', 'szt']];
    function decodeTReplacedImperative(word) {
        const candidates = [];
        for (const [afterMarker, person, number, definite] of T_REPLACED_AFTER_MARKER) {
            for (const [doubled, tail] of T_REPLACED_GEMINATIONS) {
                const remainder = strip(word, doubled + afterMarker);
                if (remainder === null) continue;
                candidates.push({ lemma: remainder + tail, person: person, number: number, definite: definite });
            }
        }
        for (const [suffix, tail] of T_REPLACED_2SG_DEFINITE) {
            const remainder = strip(word, suffix);
            if (remainder === null) continue;
            candidates.push({ lemma: remainder + tail, person: 2, number: 'sg', definite: true });
        }
        return candidates;
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

        // A "-kodik/-kedik/-ködik"-derived verb whose exact form isn't its
        // own dictionary headword ("osztozkodik" isn't listed even though
        // "osztozik" is) — same reconstruct-and-borrow approach as
        // addPrefixedVerb above, just for a suffix instead of a prefix.
        function addFrequentativeVerb(lemma, baseSense, analysisText) {
            const key = lemma + '|' + analysisText;
            if (seen.has(key)) return true;
            seen.add(key);
            results.push({
                lemma: lemma, pos: 'verb',
                translation: baseSense.en + ' (mutually, with each other)',
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
            const resolved = resolveNominal(dictionary, remainder);
            if (resolved) {
                hit = addFromLemma(resolved.lemma, resolved.sense, caseLabel) || hit;
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

                // ...or a "-kodik/-kedik/-ködik" derivational tail
                // ("osztozkodnak" strips "-nak" to "osztozkod", which
                // isn't a headword itself, but peeling "-kod" too leaves
                // "osztoz", whose "-ik" form "osztozik" is).
                const freqStem = stripFrequentative(remainder);
                if (freqStem) {
                    const freqSense = verbSense(dictionary[freqStem]) || verbSense(dictionary[freqStem + 'ik']);
                    if (freqSense) {
                        addFrequentativeVerb(remainder + 'ik', freqSense, label);
                    }
                }
            }
        }

        // 1b. imperative forms of a t-final stem whose "t" was replaced
        // or absorbed during assimilation ("fizess" -> "fizet",
        // "válassz" -> "választ") — see decodeTReplacedImperative()'s
        // own comment for why this needs its own reconstruction step
        // rather than a plain suffix-table row like everything above.
        for (const c of decodeTReplacedImperative(word)) {
            const sense = verbSense(dictionary[c.lemma]);
            if (!sense) continue;
            const label = [TENSE_LABELS.imp, PERSON_LABELS[c.person][c.number]].join(', ');
            addFromLemma(c.lemma, sense, label);
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
                const deeperResolved = resolveNominal(dictionary, deeper);
                if (deeperResolved) {
                    addFromLemma(deeperResolved.lemma, deeperResolved.sense, caseLabel + ', plural');
                }
            }
            // ...or a possessive suffix under the case suffix, for a
            // lemma outside the static index's frequency cutoff
            // ("eredményének" = eredmény + possessive 3sg + dative,
            // where "eredményének" itself was never common enough to be
            // pre-baked but "eredmény" the lemma still is)
            for (const [possSuffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
                const deeper = strip(remainder, possSuffix);
                const deeperResolved = resolveNominal(dictionary, deeper);
                if (deeperResolved) {
                    addFromLemma(deeperResolved.lemma, deeperResolved.sense,
                        describePossessive(person, ownerNumber, possessedNumber) + ', ' + caseLabel);
                }
            }
        }

        // 3. possessive suffix alone (no case) — for lemmas outside the
        // static index's frequency cutoff
        for (const [suffix, person, ownerNumber, possessedNumber] of POSSESSIVE_SUFFIXES) {
            const remainder = strip(word, suffix);
            const resolved = resolveNominal(dictionary, remainder);
            if (!resolved) continue;
            addFromLemma(resolved.lemma, resolved.sense, describePossessive(person, ownerNumber, possessedNumber));
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
            const resolved = resolveNominal(dictionary, remainder);
            if (resolved) {
                addFromLemma(resolved.lemma, resolved.sense, 'nominative, plural');
            }
        }

        // Last resort: nothing above resolved this word at all. Try
        // splitting it into two known dictionary words and offer their
        // combined meaning as a literal, word-by-word guess — see
        // splitCompound()'s own comment for why this only ever runs here,
        // never ahead of an actual morphological reading. analysis is
        // deliberately the literal string 'literal translation' (checked
        // by engine/reader.js to render this distinctly, with a caveat,
        // rather than as an ordinary grammatical label) and compoundParts
        // carries the split itself for that same rendering.
        if (!results.length) {
            const split = splitCompound(word, dictionary);
            if (split) {
                const shorten = sense => (typeof Lexicon !== 'undefined' && Lexicon.shortGloss)
                    ? Lexicon.shortGloss(sense.en) : sense.en;
                const leftGloss = shorten(split.leftSense);
                const rightGloss = shorten(split.rightSense);
                results.push({
                    lemma: word, pos: split.rightSense.type,
                    translation: leftGloss + ' + ' + rightGloss,
                    analysis: 'literal translation',
                    compoundParts: [
                        { form: split.left, translation: leftGloss },
                        { form: split.right, translation: rightGloss }
                    ]
                });
            }
        }

        return results;
    }

    // ------------------------------------------------------------------
    // GENERATION (2026-08-19, for Workshop drillers)
    // ------------------------------------------------------------------
    // Everything above this point only ever strips a suffix and validates
    // the remainder by outcome (dictionary/word-index lookup) — it never
    // has to independently know which vowel-harmony variant is "correct"
    // for a given stem, because trying all of them and keeping whichever
    // one resolves does that job for free. Generation can't lean on that
    // trick: a driller asking "what's the 2pl present of tanul" needs one
    // answer, not a set of candidates to validate against data that (for
    // verbs) mostly doesn't exist — see import_hu_dictionary.py's own
    // comment on why conjugated verb forms were deliberately left out of
    // word-index.json. So this does need real vowel-harmony logic.
    //
    // Scope: present + past indicative, plus conditional and imperative
    // (2026-08-29, in two follow-up passes — Hungarian has no separate
    // subjunctive; it reuses the imperative form for subjunctive-like
    // clauses, e.g. "azt akarom, hogy menjen" = "I want him to go" using
    // the imperative "menjen"), indefinite + definite for both moods.
    //
    // The first pass had no external access at all (every linguistics
    // reference site tried — Wiktionary, Wikipedia, cooljugator.com,
    // several Hungarian-grammar blogs — was blocked by this session's
    // network egress) and leaned on this repo's own vetted content/hu/
    // grammar cards plus one live grep hit; it also declined imperative
    // definite conjugation entirely and every t-final stem outside the
    // "-ít" derivational class, having found conflicting half-remembered
    // patterns it couldn't verify. A second follow-up (still 2026-08-29)
    // got search-engine access (WebFetch to the actual reference pages
    // stayed blocked throughout, but WebSearch's own snippets — quoting
    // an academic paper on teaching the Hungarian imperative to
    // foreigners, and Rounds' "Hungarian: An Essential Grammar" among
    // others — carried enough real conjugated forms to work from) and
    // used it to fill in both of those gaps: the full t-final
    // classification (see _imperativeMarker's own comment) and the full
    // imperative DEFINITE paradigm (see _conjugateImperativeDefinite's
    // own comment) — including catching and fixing two mistakes an
    // unverified first guess had made (imperative definite 2sg using the
    // WRONG, doubled marker; front-harmony's 3sg/2pl/3pl wrongly assumed
    // to reuse present indicative's own endings when real Hungarian uses
    // a different, uniformly "j"-initial set instead) via round-trip
    // testing against real, externally-attested forms, not just internal
    // self-consistency. What's STILL declined after both passes — the
    // "sz" digraph's imperative gemination specifically — is narrower
    // than what shipped after the first pass, not broader; see the
    // "Known gaps" note at the end of this file for the precise
    // remaining scope. Given how much of even the present-tense
    // indefinite logic above turned out to need fixing despite "high
    // confidence" from memory alone, and that this whole area only had
    // search-snippet access rather than a full source document to read
    // straight through, treat all of this — not just the parts admitted
    // above — as worth an eventual native-speaker spot-check.

    const BACK_VOWELS = 'aáoóuú';
    const FRONT_ROUNDED_VOWELS = 'öőüű';
    // e/é/i/í are "neutral" in Hungarian vowel harmony — they carry no
    // harmonic pull of their own and are TRANSPARENT to it, so a stem's
    // harmony class is set by the nearest non-neutral vowel, which isn't
    // necessarily the stem's last vowel: "szólít" (to call/address) is
    // back-harmony (szólítok, szólítunk, szólítanak) because of its "ó",
    // even though the closer, final vowel is the neutral "í" — a bug
    // caught live (2026-08-19) when this returned "szólítnek" as "correct"
    // and a manual test typed the identical string and was marked wrong
    // (the exercise's own displayed "correct" answer was already wrong,
    // not a separate grading bug).
    //
    // When EVERY vowel in the stem is neutral, real Hungarian splits by
    // WHICH neutral vowel: stems with an e/é anywhere reliably default to
    // front (kér, ért, beszél, néz, fizet, ken — all verified by round-trip
    // testing) — but stems with ONLY i/í are unreliable. That same
    // live-testing session also caught "hív" -> "hívnek" as wrong (real
    // Hungarian: hívok/hívnak, back) sitting right next to "ír" in the
    // pool, which means this isn't one or two isolated exceptions to patch
    // — pure i/í stems are back-harmony often enough that guessing "front"
    // for an unlisted one is a real, repeated risk of teaching wrong
    // Hungarian, not a rare edge case. So rather than keep extending a
    // lexical list one caught mistake at a time, an i/í-only stem NOT on
    // the known-front list below returns null (uncertain) and
    // conjugate()/callers skip the verb entirely instead of guessing.
    // Every entry on both lists below is independently confirmed against
    // cooljugator.com/hu.wiktionary.org (2026-08-20), not just carried
    // over from whatever reasoning first added it — that re-check caught
    // "hisz" and "visz" listed as back-harmony here when they're actually
    // front (hiszek/viszek, not hiszok/viszok), and two more unverifiable
    // entries ("izzik", "intik" — the latter doesn't even resolve as a
    // real dictionary lemma) were dropped rather than left in on trust.
    // The lesson: this whole file's linguistic tables get cross-validated
    // some other way (round-trip through analyze(), or word-index.json)
    // except these two lists, which is exactly why they're where mistakes
    // slipped through twice now — worth remembering before extending
    // either list again without checking a source.
    const BACK_HARMONY_NEUTRAL_STEMS = ['ír', 'sír', 'nyír', 'bízik', 'iszik', 'hív', 'szid', 'nyit'];
    const FRONT_HARMONY_II_ONLY_STEMS = ['illik', 'hisz', 'visz'];
    function _harmonyClass(stem) {
        if (BACK_HARMONY_NEUTRAL_STEMS.includes(stem)) return 'back';
        if (FRONT_HARMONY_II_ONLY_STEMS.includes(stem)) return 'front-unrounded';

        let sawEE = false, sawII = false;
        for (let i = stem.length - 1; i >= 0; i--) {
            const ch = stem[i];
            if (BACK_VOWELS.includes(ch)) return 'back';
            if (FRONT_ROUNDED_VOWELS.includes(ch)) return 'front-rounded';
            if (ch === 'e' || ch === 'é') sawEE = true;
            else if (ch === 'i' || ch === 'í') sawII = true;
            // neutral - transparent, keep scanning past it either way
        }
        if (sawEE) return 'front-unrounded';
        if (sawII) return null; // i/í-only and not on either list - unreliable, don't guess
        return 'front-unrounded'; // no vowels at all - shouldn't happen for a real word
    }

    // s/sz/z-final stems take -ol/-el/-öl instead of -asz/-esz (or bare
    // -sz) at 2sg — "olvasol" not "olvasasz"/"olvassz" — to avoid the
    // sibilant clashing with the -sz ending. -ik verbs take -ol/-el/-öl at
    // 2sg unconditionally, as a property of that verb class, independent
    // of whether the stem happens to be sibilant-final too.
    function _isSibilantFinal(stem) {
        return stem.endsWith('sz') || stem.endsWith('s') || stem.endsWith('z');
    }

    // Whether a consonant-initial ending (-sz, -tok/-tek/-tök, -nak/-nek)
    // needs a linking vowel before it, or attaches bare: bare when the
    // stem ends in a single consonant after a vowel ("tanul" -> "tanulsz",
    // "tanultok"), a linking vowel when it ends in a consonant CLUSTER
    // ("ért" -> "értesz", "értetek" — the r+t cluster can't take the
    // ending directly). Digraphs (sz, cs, zs, gy, ly, ny, ty) count as one
    // consonant, same unit CASE_SUFFIXES' assimilation logic already
    // treats them as. Unlike everything else in this file, this couldn't
    // be cross-validated against real data the way the noun suffix tables
    // are via word-index.json, since conjugated verb forms aren't in that
    // index (see the comment above conjugate()) — instead it was round-trip
    // tested by generating all persons/numbers for a growing set of verbs
    // spanning every harmony class, sibilant-final, cluster-final and
    // vowel-final stems, and feeding each generated form back through
    // analyze() to confirm it resolves to the same lemma (2026-08-19).
    // That testing caught and fixed a missing front-rounded/cluster-linking
    // 2pl and 3pl branch in VERB_SUFFIXES itself (which also means the
    // Reader can now decode forms like "üttök"/"értenek" it couldn't
    // before) — but round-trip testing only proves internal consistency
    // with VERB_SUFFIXES, not correctness against real Hungarian, and it
    // was live manual testing (not this harness) that caught the harmony
    // function returning a flatly wrong "correct" answer for "ír" and
    // "hív" both (see _harmonyClass's own comment on why i/í-only stems
    // now come back null rather than a guess). Still worth a
    // native-speaker spot-check before leaning on it hard for anything
    // beyond the verb classes that testing actually covered.
    const CONSONANT_UNITS = ['cs', 'gy', 'ly', 'ny', 'sz', 'ty', 'zs',
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z'];
    const VOWELS = 'aáeéiíoóöőuúüű';

    // The stem's final consonant "unit" (a digraph like sz/ny/gy counts as
    // one), or null for a vowel-final stem. Shared by _needsLinkingVowel
    // below and by the past-tense/definite-conjugation logic further down,
    // which both need to know what the stem ends in.
    function _finalConsonantUnit(stem) {
        for (const c of CONSONANT_UNITS) {
            if (stem.endsWith(c)) return c;
        }
        return null;
    }

    function _needsLinkingVowel(stem) {
        const unit = _finalConsonantUnit(stem);
        if (!unit) return false; // vowel-final stem, no clash possible
        const before = stem.slice(0, -unit.length).slice(-1);
        return before !== '' && !VOWELS.includes(before);
    }

    function _countVowels(word) {
        let n = 0;
        for (const ch of word) if (VOWELS.includes(ch)) n++;
        return n;
    }

    function _conjugatePresentIndefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        if (person === 3 && number === 'sg') return lemma; // harmony-independent, safe even when harmony is uncertain

        const harmony = _harmonyClass(stem);
        if (harmony === null) return null; // i/í-only stem not on either known list - don't guess
        const linking = _needsLinkingVowel(stem);

        if (person === 1 && number === 'sg') {
            if (isIkVerb) return stem + { back: 'om', 'front-unrounded': 'em', 'front-rounded': 'öm' }[harmony];
            return stem + { back: 'ok', 'front-unrounded': 'ek', 'front-rounded': 'ök' }[harmony];
        }
        if (person === 2 && number === 'sg') {
            if (isIkVerb || _isSibilantFinal(stem)) return stem + { back: 'ol', 'front-unrounded': 'el', 'front-rounded': 'öl' }[harmony];
            if (linking) return stem + { back: 'asz', 'front-unrounded': 'esz', 'front-rounded': 'esz' }[harmony];
            return stem + 'sz';
        }
        if (person === 1 && number === 'pl') return stem + { back: 'unk', 'front-unrounded': 'ünk', 'front-rounded': 'ünk' }[harmony];
        if (person === 2 && number === 'pl') {
            if (linking) return stem + { back: 'otok', 'front-unrounded': 'etek', 'front-rounded': 'ötök' }[harmony];
            return stem + { back: 'tok', 'front-unrounded': 'tek', 'front-rounded': 'tök' }[harmony];
        }
        if (person === 3 && number === 'pl') {
            if (linking) return stem + { back: 'anak', 'front-unrounded': 'enek', 'front-rounded': 'enek' }[harmony];
            return stem + { back: 'nak', 'front-unrounded': 'nek', 'front-rounded': 'nek' }[harmony];
        }

        return null;
    }

    // ---- PAST TENSE, INDEFINITE ----
    // Cross-checked against two independent sources (hungarianreference.com
    // and Wikipedia's Hungarian verbs article, both 2026-08-20) that
    // independently describe the same three-way split, given different
    // names but identical behaviour:
    //   Type I  ("soft"/sonorant stems)   — never take a linking vowel
    //   Type II (everything not I or III) — linking vowel ONLY in 3sg
    //                                        ("mos" -> mostam/mostál/
    //                                        mosott/mostunk/mostatok/
    //                                        mostak" — every other person
    //                                        stays bare)
    //   Type III ("hard" -t / clusters)   — linking vowel in every person
    // This is a genuinely different rule from present tense's single-vs-
    // cluster test above (_needsLinkingVowel) — a sibilant-final stem like
    // "mos" is single-consonant (no linking needed for present -sz/-tok/
    // -nak) but IS Type II here (3sg past does need it) — so this is its
    // own classification, not a reuse of that one.
    const PAST_TYPE_I_SONORANTS = ['r', 'l', 'n', 'ny', 'j', 'ly'];
    // "-ad/-ed" is a specific derivational suffix on a handful of common
    // verbs (marad "stay", ébred "wake") that's fully bare in the past
    // ("maradt", not "maradott") despite ending in a plain "d" that would
    // otherwise land in Type II ("adott", for the unrelated verb "ad" "to
    // give") — a lexical fact about which verbs carry that suffix, not
    // something derivable from the surface letters alone. Not exhaustive.
    const PAST_TYPE_I_LEXICAL = ['marad', 'ébred', 'fárad'];
    function _pastLinkingClass(stem) {
        if (PAST_TYPE_I_LEXICAL.includes(stem)) return 'never';
        const unit = _finalConsonantUnit(stem);
        // Type I only holds for a sonorant preceded by a VOWEL ("gondol" ->
        // gondolt) — the same single-consonant-after-vowel test
        // _needsLinkingVowel already makes for present tense. A sonorant
        // preceded by another consonant ("ugr" in "ugrik", "csukl" in
        // "csuklik") is a cluster and needs the linking vowel in every
        // person just like any other cluster-final stem — this used to be
        // missed entirely (checked only whether the FINAL letter was a
        // sonorant, not what came before it), fabricating non-words like
        // "ugrtam" instead of the real "ugrottam".
        const clusterFinal = _needsLinkingVowel(stem);
        if (unit && PAST_TYPE_I_SONORANTS.includes(unit) && !clusterFinal) return 'never';
        if (stem.endsWith('ít')) return 'always';
        if (_countVowels(stem) === 1 && stem.endsWith('t') && stem !== 'lát') return 'always';
        if (clusterFinal && !stem.endsWith('d')) return 'always';
        return 'only-3sg-indefinite';
    }

    // Personal endings past tense, WITHOUT the leading -t-/-tt- (or
    // -Vtt-) tense marker — that marker is prepended separately below,
    // once for the bare case and once (as "ott"/"ett"/"ött", already
    // including its own "tt") for the linking case. 3sg's core is empty:
    // the tense marker alone ("várt", "mosott") IS the whole word.
    const PAST_PERSONAL_CORE = {
        1: { sg: { back: 'am', 'front-unrounded': 'em', 'front-rounded': 'em' },
             pl: { back: 'unk', 'front-unrounded': 'ünk', 'front-rounded': 'ünk' } },
        2: { sg: { back: 'ál', 'front-unrounded': 'él', 'front-rounded': 'él' },
             pl: { back: 'atok', 'front-unrounded': 'etek', 'front-rounded': 'etek' } },
        3: { sg: { back: '', 'front-unrounded': '', 'front-rounded': '' },
             pl: { back: 'ak', 'front-unrounded': 'ek', 'front-rounded': 'ek' } }
    };

    function _conjugatePastIndefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;

        const core = PAST_PERSONAL_CORE[person] && PAST_PERSONAL_CORE[person][number]
            && PAST_PERSONAL_CORE[person][number][harmony];
        if (core === undefined) return null;

        const cls = _pastLinkingClass(stem);
        const linking = (cls === 'always') || (cls === 'only-3sg-indefinite' && person === 3 && number === 'sg');
        if (linking) {
            const linkVowel = { back: 'o', 'front-unrounded': 'e', 'front-rounded': 'ö' }[harmony];
            return stem + linkVowel + 'tt' + core;
        }
        const lastChar = stem[stem.length - 1];
        const bareMarker = VOWELS.includes(lastChar) ? 'tt' : 't'; // "nő" -> "nőtt", not "nőt"
        return stem + bareMarker + core;
    }

    // ---- PRESENT TENSE, DEFINITE ----
    // Endings and the sibilant-assimilation rule cross-checked against
    // hungarianreference.com and a Hungarian grammar summary PDF
    // (2026-08-20): "olvas"+"ja" -> "olvassa", "néz"+"jük" -> "nézzük",
    // "vesz"+"jük" -> "vesszük" — every one of those three worked
    // examples matched this rule exactly, which is the closest this file
    // gets to real cross-validation for anything past/definite (verb
    // forms aren't in word-index.json to round-trip against the way noun
    // suffixes are).
    function _conjugatePresentDefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;

        // 1sg definite has no distinct form at all — it's the same
        // -om/-em/-öm shape indefinite -ik-verbs already use, for every
        // verb, not just -ik ones (a genuine Hungarian collapse, not a
        // coincidence limited to one verb class).
        if (person === 1 && number === 'sg') return stem + { back: 'om', 'front-unrounded': 'em', 'front-rounded': 'öm' }[harmony];
        if (person === 2 && number === 'sg') return stem + { back: 'od', 'front-unrounded': 'ed', 'front-rounded': 'öd' }[harmony];

        const ENDINGS = {
            3: { sg: { back: 'ja', 'front-unrounded': 'i', 'front-rounded': 'i' },
                 pl: { back: 'ják', 'front-unrounded': 'ik', 'front-rounded': 'ik' } },
            1: { pl: { back: 'juk', 'front-unrounded': 'jük', 'front-rounded': 'jük' } },
            2: { pl: { back: 'játok', 'front-unrounded': 'itek', 'front-rounded': 'itek' } }
        };
        const ending = ENDINGS[person] && ENDINGS[person][number] && ENDINGS[person][number][harmony];
        if (ending === undefined) return null;

        // A leading "j" assimilates into a doubled copy of the stem's own
        // final consonant when that consonant is a sibilant (s/sz/z) —
        // endings that don't start with "j" (front -i/-itek/-ik) are
        // unaffected. Hungarian geminates a DIGRAPH by doubling only its
        // first letter, not the whole digraph — "vesz" -> "vesszük" (ssz),
        // not "veszszük" (szsz) — a real bug caught here (2026-08-20) by
        // checking generated forms against the exact worked examples
        // ("vesz"+"jük"->"vesszük") the sibilant-assimilation rule itself
        // was sourced from, rather than trusting the first formula that
        // looked plausible.
        if (ending.charAt(0) === 'j' && _isSibilantFinal(stem)) {
            const unit = _finalConsonantUnit(stem);
            const geminated = unit.length === 1 ? unit + unit : unit[0] + unit;
            return stem.slice(0, -unit.length) + geminated + ending.slice(1);
        }
        return stem + ending;
    }

    // ---- PAST TENSE, DEFINITE ----
    // Endings again cross-checked against hungarianreference.com and
    // Wikipedia's worked "mos" table: definite 3sg "mosta" stays bare even
    // though indefinite 3sg "mosott" needs linking for the exact same
    // stem — Type II's "linking only in 3sg" rule is specific to
    // INDEFINITE conjugation, so definite 3sg/3pl only get the linking
    // form for Type III stems. 2sg/1pl/2pl definite have no documented
    // linking variant at all (even for Type III stems) in either source
    // consulted — generated bare uniformly here; flagged as a known gap
    // below rather than guessed.
    function _conjugatePastDefinite(lemma, person, number) {
        // 1sg is identical to indefinite for every verb ("vettem" either
        // way) — delegate instead of duplicating the logic.
        if (person === 1 && number === 'sg') return _conjugatePastIndefinite(lemma, person, number);

        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;

        if (person === 2 && number === 'sg') return stem + { back: 'tad', 'front-unrounded': 'ted', 'front-rounded': 'ted' }[harmony];
        if (person === 1 && number === 'pl') return stem + { back: 'tuk', 'front-unrounded': 'tük', 'front-rounded': 'tük' }[harmony];
        if (person === 2 && number === 'pl') return stem + { back: 'tátok', 'front-unrounded': 'tétek', 'front-rounded': 'tétek' }[harmony];

        const linking = _pastLinkingClass(stem) === 'always';
        if (person === 3 && number === 'sg') {
            return linking
                ? stem + { back: 'otta', 'front-unrounded': 'ette', 'front-rounded': 'ötte' }[harmony]
                : stem + { back: 'ta', 'front-unrounded': 'te', 'front-rounded': 'te' }[harmony];
        }
        if (person === 3 && number === 'pl') {
            return linking
                ? stem + { back: 'ották', 'front-unrounded': 'ették', 'front-rounded': 'ötték' }[harmony]
                : stem + { back: 'ták', 'front-unrounded': 'ték', 'front-rounded': 'ték' }[harmony];
        }
        return null;
    }

    // ---- CONDITIONAL, INDEFINITE (2026-08-29 follow-up) ----
    // Marker is "n" + á/é + personal ending. Unlike present/past's 3-way
    // back/front-unrounded/front-rounded split, both conditional and
    // imperative harmonize back/front ONLY (2-way — front-rounded stems
    // take the exact same endings as front-unrounded ones, e.g. "küld"'s
    // conditional is "küldenék", not "küldönnék") — cross-checked against
    // content/hu/grammar's own "szeretnék/szeretnél/szeretne/szeretnétek"
    // cards (front) and an independent check against "várnék/várnál/
    // várna/várnánk/várnátok/várnának" (back); see MOOD_SUFFIXES above for
    // the full derivation this rests on. A cluster-final stem needs a
    // linking vowel ("a" back / "e" front) before the "n", same test
    // _needsLinkingVowel already makes for present tense's own -sz/-tok/
    // -nak. 1sg's ending is invariant "-nék" regardless of harmony
    // (várnék AND kérnék both end in é) — only ITS linking vowel, when
    // needed, varies by harmony, not the marker itself.
    function _conjugateConditionalIndefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;
        const front = harmony !== 'back';
        const link = _needsLinkingVowel(stem) ? (front ? 'e' : 'a') : '';

        if (person === 1 && number === 'sg') return stem + link + 'nék';
        if (person === 2 && number === 'sg') return stem + link + (front ? 'nél' : 'nál');
        if (person === 3 && number === 'sg') return stem + link + (front ? 'ne' : 'na');
        if (person === 1 && number === 'pl') return stem + link + (front ? 'nénk' : 'nánk');
        if (person === 2 && number === 'pl') return stem + link + (front ? 'nétek' : 'nátok');
        if (person === 3 && number === 'pl') return stem + link + (front ? 'nének' : 'nának');
        return null;
    }

    // ---- CONDITIONAL, DEFINITE ----
    // Same marker/linking-vowel rule as indefinite above. 1pl/2pl are a
    // genuine Hungarian syncretism — the SAME surface form serves both
    // definite and indefinite ("olvasnánk" = both "we would read" and
    // "we would read it") — so those two cells just delegate to the
    // indefinite generator rather than duplicate its logic.
    function _conjugateConditionalDefinite(lemma, person, number) {
        if ((person === 1 || person === 2) && number === 'pl') {
            return _conjugateConditionalIndefinite(lemma, person, number);
        }
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;
        const front = harmony !== 'back';
        const link = _needsLinkingVowel(stem) ? (front ? 'e' : 'a') : '';

        if (person === 1 && number === 'sg') return stem + link + (front ? 'ném' : 'nám');
        if (person === 2 && number === 'sg') return stem + link + (front ? 'néd' : 'nád');
        if (person === 3 && number === 'sg') return stem + link + (front ? 'né' : 'ná');
        // Front-harmony definite 3pl ("kérnék") is genuinely homophonous
        // with front-harmony indefinite 1sg — a real Hungarian syncretism
        // (see MOOD_SUFFIXES's own comment), not a bug: both really do
        // generate the identical string here.
        if (person === 3 && number === 'pl') return stem + link + (front ? 'nék' : 'nák');
        return null;
    }

    // ---- IMPERATIVE marker computation (shared by indefinite + definite) ----
    // (2026-08-29, refined follow-up — the original version of this file
    // declined every t-final stem outside the "-ít" class, having found
    // two conflicting half-remembered patterns with no way to verify
    // which; a later pass got external access and resolved it, cross-
    // checked against multiple independent sources: a Hungarian-for-
    // foreigners academic paper (Durst, "A magyar felszólító mód
    // tanítása külföldieknek", Szeged) giving "ért" -> "érts" and "tart"
    // -> "tartsam", a search-engine snippet quoting "fizet" -> "fizess"/
    // "fizessek"/"fizessen", and another quoting "választ" -> "válassz").
    //
    // The "j" marker assimilates into the stem's own final consonant(s)
    // in four different ways depending on what the stem ends in:
    //   - a sibilant (s/z; the "sz" digraph is its own case, see below):
    //     "j" geminates into a doubled copy of that consonant, digraph-
    //     aware the same way _conjugatePresentDefinite's own sibilant
    //     assimilation already is ("olvas" -> "olvass-", "néz" -> "nézz-")
    //   - "t" preceded by a SONORANT (r/l/n/ny/j/ly — reusing
    //     PAST_TYPE_I_SONORANTS from the past-tense classifier above,
    //     which this session's external check didn't directly re-verify
    //     for this new purpose but which "tart"/"ért" both fit) OR by
    //     the "-ít" derivational suffix specifically (tanít, javít, ...):
    //     the stem is left completely unchanged (its own "t" stays) and
    //     a bare "s" is appended ("tart" -> "tarts-", "tanít" ->
    //     "taníts-")
    //   - "t" preceded by a SIBILANT (választ, fest, ...): the "t" is
    //     dropped and the PRECEDING sibilant geminates instead, same
    //     digraph-aware doubling as the plain-sibilant case above, just
    //     computed one letter further back ("választ" -> "válassz-",
    //     "fest" -> "fess-")
    //   - "t" preceded by any OTHER vowel (fizet, lát, nevet, siet, ...):
    //     the "t" is dropped and replaced outright with a doubled "ss"
    //     ("fizet" -> "fizess-", "lát" -> "láss-")
    // Declined (returns null) rather than guessed: the "sz" digraph
    // specifically (a genuine sz-final stem's "j" geminates as an
    // inserted "s" before the existing "sz", giving "...ssz" — the most
    // common sz-final verbs, eszik/iszik, are already covered via
    // IRREGULAR_VERBS, so this is a narrow remaining gap).
    //
    // Returns { base, marker } — base is the stem to actually attach an
    // ending to (the original stem, unless the sibilant-preceded-"t"
    // case shortened it by dropping the "t"), or null if undecidable.
    function _imperativeMarker(stem) {
        if (stem.endsWith('ít')) return { base: stem, marker: 's' };
        if (stem.endsWith('sz')) return null; // sz-digraph gemination — declined
        if (stem.endsWith('t')) {
            const before = stem.slice(0, -1);
            const beforeUnit = _finalConsonantUnit(before);
            if (beforeUnit && PAST_TYPE_I_SONORANTS.includes(beforeUnit)) {
                return { base: stem, marker: 's' }; // sonorant-preceded: keep "t", add "s"
            }
            if (beforeUnit && _isSibilantFinal(before)) {
                // sibilant-preceded: drop "t", double the sibilant instead
                const geminated = beforeUnit.length === 1 ? beforeUnit + beforeUnit : beforeUnit[0] + beforeUnit;
                return { base: before.slice(0, -beforeUnit.length), marker: geminated };
            }
            return { base: before, marker: 'ss' }; // vowel-preceded: "t" replaced by doubled "ss"
        }
        if (_isSibilantFinal(stem)) {
            const unit = _finalConsonantUnit(stem);
            return { base: stem.slice(0, -unit.length), marker: unit + unit };
        }
        return { base: stem, marker: 'j' };
    }

    // Imperative definite 2sg specifically uses a SINGULAR (non-doubled)
    // version of _imperativeMarker's own marker, not the doubled form
    // every other cell does — a correction this follow-up's OWN external
    // check caught after first assuming (wrongly) that 2sg definite never
    // touches the stem at all: "fizesd" (from "fizet"), not "fizessd" or
    // "fizetd", and "tartsd" (from "tart"), not "tartd" — both confirmed
    // by search-engine snippets. Regular stems (marker "j") still take
    // NO marker at all here ("várd"/"olvasd"/"nézd"/"mondd" all confirmed
    // with nothing inserted before the "d") — "j" is the one marker this
    // cell drops outright rather than singularizing.
    function _singularizeMarker(marker) {
        if (marker === 'j') return '';
        if (marker === 'ss' || marker === 'zz') return marker.charAt(0);
        if (marker === 'ssz') return 'sz';
        return marker; // already singular ("s", from the "-ít"/sonorant-t class)
    }

    // ---- IMPERATIVE, INDEFINITE ----
    // Unlike every other mood/tense here, "j" (or whatever it assimilates
    // into, see _imperativeMarker above) attaches to ANY stem directly
    // with NO linking vowel EVER, even a pre-existing consonant cluster
    // ("küldj", not "küldej") — see the "küldj"/"maradj" cross-check in
    // MOOD_SUFFIXES's own comment above. Endings harmonize back/front
    // 2-way (like conditional) for every person except 3sg, which keeps
    // present tense's own 3-way -on/-en/-ön grade — cross-checked against
    // "maradjon"/"beszéljen" (already in content/hu/grammar) and
    // "jöjjön" (found live in content/hu).
    function _conjugateImperativeIndefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;
        const front = harmony !== 'back';

        const m = _imperativeMarker(stem);
        if (!m) return null;
        const { base, marker } = m;

        if (person === 2 && number === 'sg') return base + marker;
        if (person === 1 && number === 'sg') return base + marker + (front ? 'ek' : 'ak');
        if (person === 3 && number === 'sg') return base + marker + { back: 'on', 'front-unrounded': 'en', 'front-rounded': 'ön' }[harmony];
        if (person === 1 && number === 'pl') return base + marker + (front ? 'ünk' : 'unk');
        if (person === 2 && number === 'pl') return base + marker + (front ? 'etek' : 'atok');
        if (person === 3 && number === 'pl') return base + marker + (front ? 'enek' : 'anak');
        return null;
    }

    // ---- IMPERATIVE, DEFINITE ----
    // 1sg and 2sg have their own dedicated endings, distinct from every
    // other mood's definite pattern and from imperative's own indefinite
    // endings:
    //   - 1sg is "-jam"/"-jem" (2-way, invariant like conditional's own
    //     1sg) — cross-checked against "várjam", "tartsam" and
    //     "szeressem" (Rounds, "Hungarian: An Essential Grammar", via a
    //     search-engine snippet quoting its conjugation table) — note
    //     "tartsam"/"szeressem" both go through the SAME t-final
    //     assimilation _imperativeMarker computes for indefinite, just
    //     with "am"/"em" appended after the marker instead of a bare "j"
    //   - 2sg is a bare "-d", with NO harmony variation and NO linking
    //     vowel ever, attaching directly regardless of the stem's own
    //     final consonant — cross-checked against "olvasd" (s-final),
    //     "nézd" (z-final, from the common phrase "Nézd meg!") and
    //     "mondd" (d-final — the doubled "dd" is just the stem's own "d"
    //     plus this ending's "d" concatenating, not a special rule)
    //
    // 3sg/1pl/2pl/3pl: BACK harmony reuses present INDICATIVE's own
    // definite endings verbatim ("ja"/"juk"/"játok"/"ják" — "várja" means
    // both "he waits for it" and "let him wait for it", the same "j"-
    // initial morpheme doing double duty, confirmed by a search-engine
    // snippet quoting "olvassa"/"olvassuk" as BOTH the present-indicative
    // and imperative-definite forms of "olvasni"). FRONT harmony does
    // NOT reuse present indicative's own front endings, though —
    // present's front 3sg/2pl/3pl ("-i"/"-itek"/"-ik") are non-"j"-
    // initial, but imperative regularizes to a fully "j"-initial front
    // set instead ("-je"/"-jétek"/"-jék") that present tense never uses
    // at all: "nézze"/"kérje" (3sg), NOT "nézi"/"kéri" (which are the
    // present-indicative forms of the same verbs) — cross-checked
    // against two independent search-engine snippets ("nézze meg"/
    // "kérje" for 3sg; "kérjétek"/"kérjék"/"nézzék" for 2pl/3pl). This
    // also means, unlike back harmony, this function can never delegate
    // to _conjugatePresentDefinite even for a fully regular front stem.
    //
    // Either way, present indicative's OWN definite conjugation does NOT
    // apply _imperativeMarker's t-final assimilation ("tartja" stays
    // "tartja" in the present tense — confirmed by memory, not an
    // external source this session — but becomes "tartsa" in the
    // imperative, per the "tartsam" evidence above), so this recomputes
    // the ending itself regardless of harmony, applying the marker where
    // one exists and stripping the ending's own leading "j" when it
    // would otherwise double up with an already-assimilated marker.
    function _conjugateImperativeDefinite(lemma, person, number) {
        const isIkVerb = lemma.endsWith('ik');
        const stem = isIkVerb ? lemma.slice(0, -2) : lemma;
        const harmony = _harmonyClass(stem);
        if (harmony === null) return null;
        const front = harmony !== 'back';

        const m = _imperativeMarker(stem);
        if (!m) return null;
        const { base, marker } = m;

        if (person === 2 && number === 'sg') return base + _singularizeMarker(marker) + 'd';
        if (person === 1 && number === 'sg') return base + marker + (front ? 'em' : 'am');

        const ENDING = {
            3: { sg: front ? 'je' : 'ja', pl: front ? 'jék' : 'ják' },
            1: { pl: front ? 'jük' : 'juk' },
            2: { pl: front ? 'jétek' : 'játok' }
        };
        const ending = ENDING[person] && ENDING[person][number];
        if (ending === undefined) return null;

        if (marker === 'j') return base + ending; // regular stem: no separate marker, present's own "j"-initial ending already carries it
        const rest = ending.charAt(0) === 'j' ? ending.slice(1) : ending;
        return base + marker + rest;
    }

    // IRREGULAR_VERBS' keys aren't tagged with definiteness — most entries
    // don't need to be (van/megy/jön etc. are intransitive, no definite
    // object to agree with), but vesz/tesz/hisz/visz's past tense lists
    // BOTH an indefinite and a definite surface form under the SAME
    // [lemma, tense, person, number] tag ("vettél" indefinite and "vetted"
    // definite both tag as ['vesz','past',2,'sg']), since that ambiguity
    // never mattered for decode (either one resolves to the same lemma).
    // Generation has to pick one, so when more than one candidate matches,
    // this disambiguates by the same definite personal-ending shapes
    // _conjugatePastDefinite uses above.
    const IRREGULAR_LEMMAS = new Set(Object.values(IRREGULAR_VERBS).map(tags => tags[0]));
    const IRREGULAR_DEFINITE_HINT = {
        2: { sg: 'ted', pl: 'tétek' }, 3: { sg: 'te', pl: 'ték' }, 1: { pl: 'tük' }
    };
    // van/megy/jön/alszik are intransitive (no object to agree with, so
    // "definite past" isn't a real thing for them, same as already-excluded
    // present). eszik/iszik ARE transitive and DO have real, distinct
    // definite past forms (ette, itta, ...) — but this table only carries
    // their indefinite-shaped forms, so returning that single candidate for
    // a definite request would silently hand back the wrong answer, same
    // class of risk present tense already guards against for them.
    const PAST_DEFINITE_EXCLUDED = new Set(['van', 'megy', 'jön', 'alszik', 'lesz', 'eszik', 'iszik']);
    function _irregularForm(lemma, tense, person, number, definite) {
        const candidates = Object.entries(IRREGULAR_VERBS)
            .filter(([, tags]) => tags[0] === lemma && tags[1] === tense && tags[2] === person && tags[3] === number);
        if (!candidates.length) return null; // known-irregular stem, but this cell isn't covered - don't guess

        if (candidates.length === 1) {
            // 1sg is excluded from both guards below: Hungarian genuinely
            // uses the same 1sg form for definite and indefinite regardless
            // of tense or transitivity (vesz/tesz/hisz/visz's own table only
            // lists one 1sg past entry each for exactly this reason), so
            // returning it for a "definite" request isn't a wrong answer,
            // just a non-distinguishing one.
            //
            // PRESENT: none of van/megy/jön/eszik/iszik/alszik's present
            // entries were written with definiteness in mind, and eszik/
            // iszik ARE transitive with real, different definite forms this
            // table doesn't have — so a definite request there returns null
            // rather than silently handing back the indefinite form as if
            // it answered the question asked.
            if (tense === 'pres' && definite && !(person === 1 && number === 'sg')) return null;
            // PAST: same reasoning, scoped to the lemmas above — vesz/tesz/
            // hisz/visz's genuinely-ambiguous cells reach the multi-candidate
            // branch below instead and aren't affected by this guard.
            if (tense === 'past' && definite && PAST_DEFINITE_EXCLUDED.has(lemma) && !(person === 1 && number === 'sg')) return null;
            // CONDITIONAL/IMPERATIVE: IRREGULAR_VERBS carries indefinite-
            // only entries for every lemma in both moods (see their own
            // block comments above) — no 1sg exception either, since
            // unlike present/past tense, this file's conditional/
            // imperative generators produce genuinely DIFFERENT definite
            // vs. indefinite 1sg forms for regular verbs (nám vs. nék),
            // so there's no shared "same form either way" cell to spare
            // from this guard.
            if ((tense === 'cond' || tense === 'imp') && definite) return null;
            return candidates[0][0];
        }

        const hint = IRREGULAR_DEFINITE_HINT[person] && IRREGULAR_DEFINITE_HINT[person][number];
        const defMatch = hint ? candidates.find(([form]) => form.endsWith(hint)) : null;
        if (definite) return defMatch ? defMatch[0] : null;
        const indefMatch = defMatch ? candidates.find(c => c[0] !== defMatch[0]) : candidates[0];
        return indefMatch ? indefMatch[0] : null;
    }

    // vesz/tesz/hisz/visz are only irregular in the PAST tense — their
    // present tense is fully regular (per IRREGULAR_VERBS' own comment,
    // "handled by VERB_SUFFIXES stripping") and simply has no 'pres'
    // entries at all. So "is this lemma irregular" isn't quite the right
    // question for dispatch below; "does this lemma have ANY entries for
    // THIS tense" is — if not, falling through to the regular generator
    // is correct (that's exactly why those entries don't exist), whereas
    // a lemma that DOES have entries for this tense but not this exact
    // person/number (van/megy/jön missing 3sg present, since it's just
    // the bare lemma) must NOT fall through, since the regular pattern
    // would be guaranteed wrong for a genuinely irregular stem.
    function _hasIrregularEntriesForTense(lemma, tense) {
        return Object.values(IRREGULAR_VERBS).some(tags => tags[0] === lemma && tags[1] === tense);
    }

    // conjugate(lemma, {tense, person, number, definite}) -> surface form,
    // or null for a combination this scope doesn't cover (see the scope
    // note above this section, and each helper's own comment).
    function conjugate(lemma, opts) {
        const tense = (opts && opts.tense) || 'pres';
        const person = (opts && opts.person) || 3;
        const number = (opts && opts.number) || 'sg';
        const definite = !!(opts && opts.definite);
        if (tense !== 'pres' && tense !== 'past' && tense !== 'cond' && tense !== 'imp') return null;

        // Universal, true for every verb regardless of regularity: present
        // indefinite 3sg is just the bare lemma, no suffix at all. Checked
        // before the irregular-lemma branch below because IRREGULAR_VERBS
        // never bothers listing this cell for van/megy/jön (it doesn't
        // diverge from the pattern), which would otherwise make
        // _irregularForm wrongly report it as "not covered".
        if (tense === 'pres' && person === 3 && number === 'sg' && !definite) return lemma;

        if (IRREGULAR_LEMMAS.has(lemma) && _hasIrregularEntriesForTense(lemma, tense)) {
            return _irregularForm(lemma, tense, person, number, definite);
        }

        // lesz ("to become") is intransitive but is only irregular in the
        // PAST tense (present is fully regular — leszek, leszel, lesz, ...
        // — so it has no 'pres' entries in IRREGULAR_VERBS at all), which
        // means the branch above never runs for it in present tense and
        // dispatch falls straight to the regular generator below. Unlike
        // _irregularForm, that generator has no concept of transitivity and
        // would happily fabricate non-word "definite" forms (leszem, leszi,
        // ...) for a verb with no object to agree with. lesz is the one
        // lemma in this scope irregular in only one tense while needing a
        // definite exclusion in the other, so it needs its own guard here
        // rather than fitting the IRREGULAR_LEMMAS-gated check above.
        if (lemma === 'lesz' && tense === 'pres' && definite && !(person === 1 && number === 'sg')) return null;

        // van has NO imperative of its own in real Hungarian at all — a
        // direct "be!" command borrows lesz's légy/legyen family instead
        // (see IRREGULAR_VERBS' own comment on this) — so IRREGULAR_VERBS
        // has zero 'imp' entries for van, and _hasIrregularEntriesForTense
        // above correctly returns false for it. Without this guard,
        // dispatch would fall through to the regular generator below,
        // which has no way to know "van" isn't a normal single-consonant
        // stem and would fabricate non-words ("vanj", "vanjon", ...) —
        // caught live by round-trip testing this follow-up against every
        // irregular lemma, not just the ones with SOME entries for a
        // tense (the failure mode the lesz guard above already covers).
        if (lemma === 'van' && tense === 'imp') return null;

        if (tense === 'pres') {
            return definite ? _conjugatePresentDefinite(lemma, person, number) : _conjugatePresentIndefinite(lemma, person, number);
        }
        if (tense === 'cond') {
            return definite ? _conjugateConditionalDefinite(lemma, person, number) : _conjugateConditionalIndefinite(lemma, person, number);
        }
        if (tense === 'imp') {
            return definite ? _conjugateImperativeDefinite(lemma, person, number) : _conjugateImperativeIndefinite(lemma, person, number);
        }
        return definite ? _conjugatePastDefinite(lemma, person, number) : _conjugatePastIndefinite(lemma, person, number);
    }

    return {
        analyze: analyze, describe: describe, ladder: ladder, isNominal: isNominal,
        nominalSense: nominalSense, verbSense: verbSense, anySense: anySense,
        conjugate: conjugate,
        naivePluralize: naivePluralize,
        caseName: caseName, caseSuffixLabel: caseSuffixLabel, casePreposition: casePreposition,
        casesList: function () {
            return Object.keys(CASE_LABELS).map(code => ({
                code: code, label: CASE_LABELS[code], preposition: CASE_PREPOSITION[code] || null
            }));
        },
        personLabel: function (person, number) { return PERSON_LABELS[person][number]; },
        tenseLabel: function (tense) { return TENSE_LABELS[tense]; },
        prefixList: function () {
            return VERB_PREFIXES.map(([prefix, sense]) => ({ prefix: prefix, sense: sense }));
        }
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
//   - low vowel lengthening (delengthen()/resolveNominal(), 2026-08-19
//     follow-up) only tries ONE step back (á->a, é->e) on the immediate
//     remainder — covers "intelligenciával" but not a lengthened stem
//     buried under two stacked suffixes at once
//   - the "-kodik/-kedik/-ködik" frequentative/reciprocal verb suffix
//     (stripFrequentative()/addFrequentativeVerb(), 2026-08-19 follow-up)
//     is tried only as a last resort after a bare remainder and its "-ik"
//     form both fail, and only ever composes a generic "(mutually, with
//     each other)" gloss onto the base verb's translation — right for
//     "osztozkodik", not guaranteed for every verb this suffix attaches to
//   - within-POS dictionary sense selection is capped at 3 per (lemma,
//     pos) (MAX_SENSES_PER_POS in import_hu_dictionary.py, 2026-08-19
//     follow-up) — a lemma with a 4th genuinely distinct sense under the
//     same POS still silently drops it, same failure mode "kormány" hit
//     before the cap was raised from 1
//
// conjugate()'s gaps (2026-08-20 follow-up, present+past/definite+
// indefinite generation — see the comment above conjugate() for what WAS
// cross-checked and how):
//   - sibilant-assimilated definite present forms ("olvassa", "mos+ja"
//     with the leading j replaced by a geminated stem consonant) generate
//     correctly but analyze() can't decode them back — the assimilation
//     doesn't leave the stem as a clean prefix of the surface form for
//     simple suffix-stripping to recover (see _conjugatePresentDefinite's
//     own comment), so this is the one class of generated form this
//     session couldn't round-trip-verify, only external-source-verify
//     (olvassa/nézzük/vesszük/veszem-veszed-veszi-vesszük-veszitek-veszik
//     all matched cooljugator.com exactly)
//   - definite past 2sg/1pl/2pl (-tad/-ted, -tuk/-tük, -tátok/-tétek)
//     are generated bare for every stem, even Type III ("always linking")
//     ones — neither source consulted documented a linking variant for
//     these three cells the way they did for 3sg/3pl, but that could be
//     the sources' own gap rather than Hungarian's; unconfirmed either way
//   - eszik/iszik have no past-tense DEFINITE forms in IRREGULAR_VERBS
//     (only the shared indefinite-shaped ones) — same category of gap as
//     vesz/tesz/hisz/visz already being explicitly disambiguated, just not
//     done yet for these two (real forms would be "ette"/"itta" etc., not
//     derivable from IRREGULAR_DEFINITE_HINT as-is since it only covers
//     front-harmony endings and iszik's are back-harmony). **Partially
//     fixed 2026-08-27**: conjugate() no longer hands back the indefinite-
//     shaped form for a definite request (that was actively wrong, e.g.
//     the driller presenting "evett" as the graded-correct definite
//     answer) — PAST_DEFINITE_EXCLUDED in _irregularForm now returns null
//     for eszik/iszik definite past instead, same as it already did for
//     alszik/van/megy/jön, which are truly intransitive. The real definite
//     forms still aren't authored; this only stops the wrong guess.
//   - the "-ad/-ed" past-tense lexical exception list (PAST_TYPE_I_LEXICAL:
//     marad, ébred, fárad) is a hand-picked few, not the full closed set
//   - _pastLinkingClass's Type-I sonorant list (r, l, n, ny, j, ly) is
//     cross-sourced but only spot-checked against "vár". **Fixed
//     2026-08-27**: the list itself wasn't the problem — the classifier
//     was checking only whether the stem's FINAL letter was a sonorant,
//     not whether that sonorant was preceded by a vowel (true Type I,
//     e.g. "gondol" -> gondolt) or by another consonant (a cluster,
//     e.g. "ugr" in "ugrik", which needs the linking vowel in every
//     person like any other cluster-final stem: ugrottam, not ugrtam).
//     Now gated on the same single-consonant-after-vowel test
//     (_needsLinkingVowel) present tense already uses. The list itself is
//     still only spot-checked per-consonant against "vár".
//
// Conditional and imperative moods (2026-08-29, two follow-up passes —
// see the "Scope" comment above conjugate() for what each pass had access
// to and fixed, and each generation function's own comment for its exact
// coverage):
//   - imperative DEFINITE conjugation IS now modelled (second pass) —
//     1sg/3sg/1pl/2pl/3pl reuse the same t-final/sibilant assimilation
//     _imperativeMarker computes for indefinite, plus their own dedicated
//     endings; 2sg takes a SINGULAR version of that same marker via
//     _singularizeMarker. The very first version of this second pass got
//     2sg wrong twice before shipping — assumed no marker at all
//     ("tartd"), then caught by an external check specifically for that
//     cell and fixed to the real "tartsd" — and separately assumed
//     front-harmony 3sg/2pl/3pl could reuse present indicative's own
//     "i"/"itek"/"ik" endings, when real Hungarian actually regularizes
//     imperative's front endings to their own uniformly "j"-initial set
//     ("nézze"/"kérje", not "nézi"/"kéri" — those are present tense).
//     Both mistakes were caught by cross-checking generated output
//     against real, externally-sourced forms, not just internal round-
//     trip self-consistency, which is exactly why that step mattered.
//   - imperative's t-final classification is now the full 4-way split
//     (see _imperativeMarker's own comment: "-ít"/sonorant-preceded keeps
//     the stem's own "t" and adds "s"; sibilant-preceded drops the "t"
//     and doubles the sibilant instead; every other vowel-preceded stem
//     replaces "t" with a doubled "ss") rather than the first pass's
//     "-ít" class only. The two harder classes (sibilant-preceded and
//     vowel-preceded) needed genuinely new DECODE logic too, not just a
//     table row — see decodeTReplacedImperative()'s own comment for why
//     "fizess"/"válassz"-shaped words need their tail reconstructed
//     rather than simply stripped.
//   - still declined, narrower than before: the "sz" digraph specifically
//     (a genuine sz-final stem geminates as an inserted "s" before the
//     existing "sz", not decodable by this table's plain suffix-
//     stripping, nor by decodeTReplacedImperative's reconstruction, which
//     is for a DIFFERENT situation — an absorbed "t", not a bare sz-final
//     stem with no "t" involved at all) — a narrow gap since the most
//     common sz-final verbs (eszik, iszik) are already covered via
//     IRREGULAR_VERBS
//   - IRREGULAR_VERBS' conditional/imperative entries for the 11
//     suppletive verbs are still indefinite-only, even where vesz/tesz/
//     hisz/visz genuinely have distinct definite forms in real Hungarian
//     ("venném" = "I would buy it") — left out because front-harmony
//     definite-3pl and indefinite-1sg are genuinely homophonous for these
//     moods (see MOOD_SUFFIXES's own comment), and a flat surfaceForm->tag
//     map can't hold two different tags under one key the way the regular
//     suffix table can (multiple rows sharing a string); rather than pick
//     a silently-arbitrary winner, both cells are simply not authored
//   - separately, and NOT specific to conditional/imperative: Lexicon.
//     lookup() (engine/lexicon.js, not this file) tries a direct
//     dictionary hit before ever calling this module's analyze(), and a
//     direct hit wins outright with no merging — so a generated
//     imperative form that happens to ALSO be an unrelated existing
//     headword ("fess" the adjective "stylish", "lásd"/"nézze" as fixed
//     interjections) will only ever show that unrelated reading in the
//     Reader, never the verb one, even though analyze() itself decodes
//     the verb reading correctly when called directly (confirmed live
//     this pass: "kérje"/"kérjétek"/"kérjék"/"nézzék"/"tartsd"/"fizesd"/
//     "válaszd"/"tartsam"/"szeressem"/"válassz"/"érts"/"bánts" all showed
//     correctly through the real Reader; only the three coincidental-
//     collision words didn't). This is an existing, general Lexicon
//     architecture choice that predates this file's own work and applies
//     to any suffix-stripping result, not something specific to the
//     imperative — flagged here since it's newly OBSERVABLE now that
//     imperative coverage produces more short, word-like forms likely to
//     collide, not because this file caused it.
//   - all of this was cross-checked via WebSearch snippets rather than
//     reading a full external reference document straight through (every
//     linguistics site's own page stayed blocked via WebFetch all
//     session) — a native-speaker spot-check would still be worth doing
//     before leaning on it as hard as present/past tense.
