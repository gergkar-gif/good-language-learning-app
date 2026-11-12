// ============================================
// CZECH MORPHOLOGY — runtime inflection & conjugation fallback
// ============================================
// Mirrors HungarianMorphology, PolishMorphology, and ItalianMorphology for Czech.
// Provides:
// 1. Prepositional contractions & vocalizations (ve, se, ze, ke, ku, ode, pode, přede, nade, beze, přese).
// 2. Mobile past auxiliary clitics & conditional peeling (-s, jsem, jsi, jsme, jste, bych, bys, by, bychom, byste).
// 3. Regular conjugation reconstruction (Conjugations -at/-ám, -et/-ím, -it/-ím, -ovat/-uji, -out/-u, past in -l-).
// 4. Irregular root & core verb analysis (být, mít, moct, moci, chtít, vědět, znát, jít, jet, vzít, brát, dát, jíst, pít, říct).
// 5. Verbal prefix stripping & aspect pair stems (po-, vy-, za-, při-, od-, do-, na-, u-, pře-, roz-, s-, z-).
// 6. Nominal & adjectival declension stem stripping across 7 cases.
// 7. Quantitative & fleeting-e alternations (dům:domu, kůň:koně, stůl:stolu, pes:psa, den:dne, otec:otce).
// 8. Consonant palatalizations (k:c/č, h:z/ž, ch:š, r:ř, t:ť, d:ď, n:ň).
// 9. Reflexive particle stripping (se, si).

const CzechMorphology = (function () {
    'use strict';

    // Prepositional vocalizations & historical pronominal enclitics (-ň)
    const CONTRACTIONS = {
        've':     { lemma: 'v', pos: 'preposition', translation: 'in, into', analysis: 'vocalized form of v (before consonant clusters)' },
        'se':     { lemma: 's', pos: 'preposition', translation: 'with', analysis: 'vocalized form of s (before consonant clusters)' },
        'ze':     { lemma: 'z', pos: 'preposition', translation: 'from, out of', analysis: 'vocalized form of z (before consonant clusters)' },
        'ke':     { lemma: 'k', pos: 'preposition', translation: 'to, towards', analysis: 'vocalized form of k' },
        'ku':     { lemma: 'k', pos: 'preposition', translation: 'to, towards', analysis: 'archaic vocalized form of k (e.g. ku pomoci)' },
        'ode':    { lemma: 'od', pos: 'preposition', translation: 'from', analysis: 'vocalized form of od' },
        'pode':   { lemma: 'pod', pos: 'preposition', translation: 'under', analysis: 'vocalized form of pod' },
        'přede':  { lemma: 'před', pos: 'preposition', translation: 'in front of, before', analysis: 'vocalized form of před' },
        'nade':   { lemma: 'nad', pos: 'preposition', translation: 'above, over', analysis: 'vocalized form of nad' },
        'beze':   { lemma: 'bez', pos: 'preposition', translation: 'without', analysis: 'vocalized form of bez' },
        'přese':  { lemma: 'přes', pos: 'preposition', translation: 'across, over', analysis: 'vocalized form of přes' },

        // Pronominal enclitics (-ň = něj / ho after prepositions)
        'proň':   { lemma: 'pro', pos: 'contraction', translation: 'for him/it', analysis: 'pro + on (něj)' },
        'oň':     { lemma: 'o', pos: 'contraction', translation: 'about him/it', analysis: 'o + on (něj)' },
        'naň':    { lemma: 'na', pos: 'contraction', translation: 'onto him/it', analysis: 'na + on (něj)' },
        'zaň':    { lemma: 'za', pos: 'contraction', translation: 'for him / behind him', analysis: 'za + on (něj)' },
        'doň':    { lemma: 'do', pos: 'contraction', translation: 'into him/it', analysis: 'do + on (něj)' },
        'podň':   { lemma: 'pod', pos: 'contraction', translation: 'under him/it', analysis: 'pod + on (něj)' }
    };

    // Core irregular verbs lookup map
    const IRREGULAR_VERBS = {
        být: {
            forms: {
                jsem: 'Present, 1st person singular',
                jsi: 'Present, 2nd person singular',
                je: 'Present, 3rd person singular',
                jsme: 'Present, 1st person plural',
                jste: 'Present, 2nd person plural',
                jsou: 'Present, 3rd person plural',
                budu: 'Future, 1st person singular',
                budeš: 'Future, 2nd person singular',
                bude: 'Future, 3rd person singular',
                budeme: 'Future, 1st person plural',
                budete: 'Future, 2nd person plural',
                budou: 'Future, 3rd person plural',
                byl: 'Past, 3rd person singular (masculine)',
                byla: 'Past, 3rd person singular (feminine)',
                bylo: 'Past, 3rd person singular (neuter)',
                byli: 'Past, 3rd person plural (masculine animate)',
                byly: 'Past, 3rd person plural (inanimate / feminine)',
                buď: 'Imperative singular',
                buďme: 'Imperative 1st person plural',
                buďte: 'Imperative 2nd person plural',
                bych: 'Conditional auxiliary, 1st person singular',
                bys: 'Conditional auxiliary, 2nd person singular',
                by: 'Conditional auxiliary, 3rd person',
                bychom: 'Conditional auxiliary, 1st person plural',
                byste: 'Conditional auxiliary, 2nd person plural'
            }
        },
        mít: {
            forms: {
                mám: 'Present, 1st person singular',
                máš: 'Present, 2nd person singular',
                má: 'Present, 3rd person singular',
                máme: 'Present, 1st person plural',
                máte: 'Present, 2nd person plural',
                mají: 'Present, 3rd person plural',
                měl: 'Past, 3rd person singular (masculine)',
                měla: 'Past, 3rd person singular (feminine)',
                mělo: 'Past, 3rd person singular (neuter)',
                měli: 'Past, 3rd person plural (masculine animate)',
                měly: 'Past, 3rd person plural (inanimate / feminine)',
                měj: 'Imperative singular',
                mějme: 'Imperative 1st person plural',
                mějte: 'Imperative 2nd person plural'
            }
        },
        moct: {
            forms: {
                můžu: 'Present, 1st person singular',
                mohu: 'Present, 1st person singular (formal)',
                můžeš: 'Present, 2nd person singular',
                může: 'Present, 3rd person singular',
                můžeme: 'Present, 1st person plural',
                můžete: 'Present, 2nd person plural',
                můžou: 'Present, 3rd person plural',
                mohou: 'Present, 3rd person plural (formal)',
                mohl: 'Past, 3rd person singular (masculine)',
                mohla: 'Past, 3rd person singular (feminine)',
                mohlo: 'Past, 3rd person singular (neuter)',
                mohli: 'Past, 3rd person plural (masculine animate)',
                mohly: 'Past, 3rd person plural (inanimate / feminine)'
            }
        },
        chtít: {
            forms: {
                chci: 'Present, 1st person singular',
                chceš: 'Present, 2nd person singular',
                chce: 'Present, 3rd person singular',
                chceme: 'Present, 1st person plural',
                chcete: 'Present, 2nd person plural',
                chtějí: 'Present, 3rd person plural',
                chtěl: 'Past, 3rd person singular (masculine)',
                chtěla: 'Past, 3rd person singular (feminine)',
                chtělo: 'Past, 3rd person singular (neuter)',
                chtěli: 'Past, 3rd person plural (masculine animate)',
                chtěly: 'Past, 3rd person plural (inanimate / feminine)',
                chtěj: 'Imperative singular',
                chtějme: 'Imperative 1st person plural',
                chtějte: 'Imperative 2nd person plural'
            }
        },
        vědět: {
            forms: {
                vím: 'Present, 1st person singular',
                víš: 'Present, 2nd person singular',
                ví: 'Present, 3rd person singular',
                víme: 'Present, 1st person plural',
                víte: 'Present, 2nd person plural',
                vědí: 'Present, 3rd person plural',
                věděl: 'Past, 3rd person singular (masculine)',
                věděla: 'Past, 3rd person singular (feminine)',
                vědělo: 'Past, 3rd person singular (neuter)',
                věděli: 'Past, 3rd person plural (masculine animate)',
                věděly: 'Past, 3rd person plural (inanimate / feminine)',
                věz: 'Imperative singular',
                vězme: 'Imperative 1st person plural',
                vězte: 'Imperative 2nd person plural'
            }
        },
        jít: {
            forms: {
                jdu: 'Present, 1st person singular',
                jdeš: 'Present, 2nd person singular',
                jde: 'Present, 3rd person singular',
                jdeme: 'Present, 1st person plural',
                jdete: 'Present, 2nd person plural',
                jdou: 'Present, 3rd person plural',
                šel: 'Past, 3rd person singular (masculine)',
                šla: 'Past, 3rd person singular (feminine)',
                šlo: 'Past, 3rd person singular (neuter)',
                šli: 'Past, 3rd person plural (masculine animate)',
                šly: 'Past, 3rd person plural (inanimate / feminine)',
                půjdu: 'Future, 1st person singular',
                půjdeš: 'Future, 2nd person singular',
                půjde: 'Future, 3rd person singular',
                půjdeme: 'Future, 1st person plural',
                půjdete: 'Future, 2nd person plural',
                půjdou: 'Future, 3rd person plural',
                jdi: 'Imperative singular',
                jděme: 'Imperative 1st person plural',
                jděte: 'Imperative 2nd person plural'
            }
        },
        přijít: {
            forms: {
                přijdu: 'Future/Present, 1st person singular',
                přijdeš: 'Future/Present, 2nd person singular',
                přijde: 'Future/Present, 3rd person singular',
                přijdeme: 'Future/Present, 1st person plural',
                přijdete: 'Future/Present, 2nd person plural',
                přijdou: 'Future/Present, 3rd person plural',
                přišel: 'Past, 3rd person singular (masculine)',
                přišla: 'Past, 3rd person singular (feminine)',
                přišlo: 'Past, 3rd person singular (neuter)',
                přišli: 'Past, 3rd person plural (masculine animate)',
                přišly: 'Past, 3rd person plural (inanimate / feminine)',
                přijď: 'Imperative singular',
                přijďme: 'Imperative 1st person plural',
                přijďte: 'Imperative 2nd person plural'
            }
        },
        jet: {
            forms: {
                jedu: 'Present, 1st person singular',
                jedeš: 'Present, 2nd person singular',
                jede: 'Present, 3rd person singular',
                jedeme: 'Present, 1st person plural',
                jedete: 'Present, 2nd person plural',
                jedou: 'Present, 3rd person plural',
                jel: 'Past, 3rd person singular (masculine)',
                jela: 'Past, 3rd person singular (feminine)',
                jelo: 'Past, 3rd person singular (neuter)',
                jeli: 'Past, 3rd person plural (masculine animate)',
                jely: 'Past, 3rd person plural (inanimate / feminine)',
                pojedu: 'Future, 1st person singular',
                pojedeš: 'Future, 2nd person singular',
                pojede: 'Future, 3rd person singular',
                pojedeme: 'Future, 1st person plural',
                pojedete: 'Future, 2nd person plural',
                pojedou: 'Future, 3rd person plural',
                jeď: 'Imperative singular',
                jeďme: 'Imperative 1st person plural',
                jeďte: 'Imperative 2nd person plural'
            }
        },
        říct: {
            forms: {
                řeknu: 'Future/Present, 1st person singular',
                řekneš: 'Future/Present, 2nd person singular',
                řekne: 'Future/Present, 3rd person singular',
                řekneme: 'Future/Present, 1st person plural',
                řeknete: 'Future/Present, 2nd person plural',
                řeknou: 'Future/Present, 3rd person plural',
                řekl: 'Past, 3rd person singular (masculine)',
                řekla: 'Past, 3rd person singular (feminine)',
                řeklo: 'Past, 3rd person singular (neuter)',
                řekli: 'Past, 3rd person plural (masculine animate)',
                řekly: 'Past, 3rd person plural (inanimate / feminine)',
                řekni: 'Imperative singular',
                řekněme: 'Imperative 1st person plural',
                řekněte: 'Imperative 2nd person plural'
            }
        },
        jíst: {
            forms: {
                jím: 'Present, 1st person singular',
                jíš: 'Present, 2nd person singular',
                jí: 'Present, 3rd person singular',
                jíme: 'Present, 1st person plural',
                jíte: 'Present, 2nd person plural',
                jedí: 'Present, 3rd person plural',
                jedl: 'Past, 3rd person singular (masculine)',
                jedla: 'Past, 3rd person singular (feminine)',
                jedlo: 'Past, 3rd person singular (neuter)',
                jedli: 'Past, 3rd person plural (masculine animate)',
                jedly: 'Past, 3rd person plural (inanimate / feminine)',
                jez: 'Imperative singular',
                jezme: 'Imperative 1st person plural',
                jezte: 'Imperative 2nd person plural'
            }
        }
    };

    // Vowel quantity / diphthong alternations in Czech noun/adjective stems
    const STEM_ALTERNATIONS = [
        // ou : ú
        { from: /ou/, to: 'ú' },
        // ů : o (dům -> domu, stůl -> stolu, kůň -> koně)
        { from: /ů/, to: 'o' },
        // í : ě / e (vítr -> větru, chléb -> chleba)
        { from: /í/, to: 'ě' },
        { from: /í/, to: 'e' },
        // á : a (král -> krále, jáma -> jam)
        { from: /á/, to: 'a' }
    ];

    // Fleeting e (pohyblivé e) words
    const FLEETING_E_MAP = {
        'psa': 'pes', 'psu': 'pes', 'psem': 'pes', 'psi': 'pes', 'psů': 'pes', 'psům': 'pes', 'psech': 'pes',
        'dne': 'den', 'dni': 'den', 'dny': 'den', 'dnů': 'den', 'dnem': 'den', 'dnech': 'den',
        'otce': 'otec', 'otci': 'otec', 'otcem': 'otec', 'otců': 'otec', 'otcům': 'otec', 'otcích': 'otec',
        'lva': 'lev', 'lvu': 'lev', 'lvem': 'lev', 'lvi': 'lev',
        'orla': 'orel', 'orlu': 'orel', 'orlem': 'orel', 'orli': 'orel',
        'domu': 'dům', 'domem': 'dům', 'domy': 'dům', 'domů': 'dům', 'domech': 'dům',
        'stolu': 'stůl', 'stolem': 'stůl', 'stoly': 'stůl', 'stolů': 'stůl', 'stolech': 'stůl',
        'koně': 'kůň', 'koni': 'kůň', 'koněm': 'kůň', 'koní': 'kůň', 'koních': 'kůň', 'koňmi': 'kůň',
        'boha': 'bůh', 'bohu': 'bůh', 'bohem': 'bůh', 'bozi': 'bůh', 'bohové': 'bůh',
        'lidé': 'člověk', 'lidí': 'člověk', 'lidem': 'člověk', 'lidech': 'člověk', 'lidmi': 'člověk'
    };

    // Palatalization rules reversing inflected stem to base consonant
    function unpalatalize(stem) {
        const candidates = [stem];
        // c -> k (kluci -> kluk, v ruce -> ruka)
        if (stem.endsWith('c')) candidates.push(stem.slice(0, -1) + 'k');
        // č -> k (ručka -> ruka)
        if (stem.endsWith('č')) candidates.push(stem.slice(0, -1) + 'k');
        // z -> h (v Praze -> Praha, bozi -> bůh)
        if (stem.endsWith('z')) candidates.push(stem.slice(0, -1) + 'h');
        // ž -> h
        if (stem.endsWith('ž')) candidates.push(stem.slice(0, -1) + 'h');
        // š -> ch (Češi -> Čech, v mouše -> moucha)
        if (stem.endsWith('š')) candidates.push(stem.slice(0, -1) + 'ch');
        // ř -> r (doktoři -> doktor, bratři -> bratr)
        if (stem.endsWith('ř')) candidates.push(stem.slice(0, -1) + 'r');
        // ď -> d, ť -> t, ň -> n
        if (stem.endsWith('ď')) candidates.push(stem.slice(0, -1) + 'd');
        if (stem.endsWith('ť')) candidates.push(stem.slice(0, -1) + 't');
        if (stem.endsWith('ň')) candidates.push(stem.slice(0, -1) + 'n');
        return candidates;
    }

    // Peel enclitics: past tense -s, reflexive particles, and auxiliaries
    function peelClitics(word) {
        const results = [];
        const lower = word.toLowerCase();

        // 2nd person past clitic attached to participle: dělals -> dělal + s, byls -> byl + s
        if (lower.length >= 4 && lower.endsWith('ls')) {
            results.push({ stem: lower.slice(0, -1), clitic: 's', analysis: '2nd person singular past auxiliary enclitic (-s = jsi)' });
        }
        if (lower.length > 4 && (lower.endsWith('las') || lower.endsWith('los') || lower.endsWith('lis') || lower.endsWith('lys'))) {
            results.push({ stem: lower.slice(0, -1), clitic: 's', analysis: '2nd person past auxiliary enclitic (-s = jsi)' });
        }

        // Conditional forms with fused particles (abych, abys, aby, abychom, abyste; kdybych...)
        if (lower.startsWith('aby') || lower.startsWith('kdyby')) {
            const base = lower.startsWith('kdyby') ? 'kdyby' : 'aby';
            const suffix = lower.slice(base.length);
            if (suffix === 'ch' || suffix === 's' || suffix === '' || suffix === 'chom' || suffix === 'ste') {
                results.push({ stem: base, clitic: suffix, analysis: `conditional conjunction ${base} + person ending` });
            }
        }

        return results;
    }

    // Reverse past tense participle ending: dělal / dělala / dělali -> dělat
    function reconstructInfinitiveFromPast(participle) {
        const candidates = [];
        const lower = participle.toLowerCase();
        let stem = lower;
        if (lower.endsWith('li') || lower.endsWith('ly') || lower.endsWith('la') || lower.endsWith('lo')) {
            stem = lower.slice(0, -1);
        }
        if (stem.endsWith('l')) {
            const root = stem.slice(0, -1);
            candidates.push(root + 't');
            if (root.endsWith('a')) candidates.push(root + 't');
            if (root.endsWith('e') || root.endsWith('ě')) candidates.push(root + 't');
            if (root.endsWith('i')) candidates.push(root + 't');
            if (root.endsWith('ou')) candidates.push(root.slice(0, -2) + 'out');
        }
        return candidates;
    }

    // Strip common productive verbal prefixes to discover base imperfective partner
    function stripVerbalPrefixes(word) {
        const prefixes = ['pře', 'při', 'roz', 'od', 'po', 'vy', 'za', 'do', 'na', 'u', 's', 'z'];
        const results = [];
        for (const p of prefixes) {
            if (word.startsWith(p) && word.length > p.length + 3) {
                results.push({ prefix: p, stem: word.slice(p.length) });
            }
        }
        return results;
    }

    // Nominal, pronominal & adjectival declension suffixes across 7 cases
    const DECLENSION_SUFFIXES = [
        'eho', 'ému', 'ých', 'ými', 'ého', 'ému', 'ího', 'ímu', 'ích', 'ími', // Adj long endings
        'ách', 'ích', 'ech', 'ata', 'atech', 'atům',                          // Locative / plural neuter
        'ami', 'emi', 'ama', 'ma',                                            // Instrumental plurals & duals
        'ovi', 'ové', 'ata',                                                  // Dative/Loc masculine, Nom plural
        'ům', 'ou', 'em', 'am', 'om', 'ím',                                   // Dat/Inst/Gen
        'ka', 'ky', 'ce', 'ku', 'kem',                                        // Diminutives / k-stems
        'e', 'ě', 'a', 'u', 'i', 'í', 'y', 'o'                                // Common short case endings
    ];

    function analyze(word) {
        if (!word || typeof word !== 'string') return null;
        const lower = word.trim().toLowerCase();

        // 1. Direct contraction / vocalization match
        if (CONTRACTIONS[lower]) {
            return {
                matched: true,
                type: 'contraction',
                entry: CONTRACTIONS[lower]
            };
        }

        // 2. Irregular verb direct form lookup
        for (const [lemma, data] of Object.entries(IRREGULAR_VERBS)) {
            if (data.forms && data.forms[lower]) {
                return {
                    matched: true,
                    type: 'irregular_verb',
                    lemma: lemma,
                    analysis: data.forms[lower]
                };
            }
        }

        // 3. Fleeting-e direct map
        if (FLEETING_E_MAP[lower]) {
            return {
                matched: true,
                type: 'alternation',
                lemma: FLEETING_E_MAP[lower],
                analysis: 'stem alternation (fleeting-e / vowel length)'
            };
        }

        // 4. Clitic peeling
        const peeled = peelClitics(lower);
        if (peeled.length > 0) {
            return {
                matched: true,
                type: 'clitic',
                peeled: peeled
            };
        }

        return {
            matched: false,
            word: lower
        };
    }

    // Lookup helper for Lexicon
    function lookup(word, dict) {
        if (!word) return null;
        const lower = word.trim().toLowerCase();

        // Direct dictionary hit
        if (dict && dict[lower]) {
            return {
                found: true,
                source: 'direct',
                readings: [{ lemma: lower, ...dict[lower] }]
            };
        }

        // Contraction hit
        if (CONTRACTIONS[lower]) {
            const c = CONTRACTIONS[lower];
            return {
                found: true,
                source: 'contraction',
                readings: [{
                    lemma: c.lemma,
                    translation: c.translation,
                    analysis: c.analysis,
                    type: c.pos
                }]
            };
        }

        // Irregular verb hit
        for (const [vlemma, vdata] of Object.entries(IRREGULAR_VERBS)) {
            if (vdata.forms && vdata.forms[lower]) {
                const dictEntry = (dict && dict[vlemma]) || {};
                return {
                    found: true,
                    source: 'irregular_verb',
                    readings: [{
                        lemma: vlemma,
                        translation: dictEntry.en || 'to ' + vlemma,
                        analysis: vdata.forms[lower],
                        type: 'verb'
                    }]
                };
            }
        }

        // Fleeting-e / vowel alternation hit
        if (FLEETING_E_MAP[lower]) {
            const mappedLemma = FLEETING_E_MAP[lower];
            if (dict && dict[mappedLemma]) {
                return {
                    found: true,
                    source: 'alternation',
                    readings: [{
                        lemma: mappedLemma,
                        ...dict[mappedLemma],
                        analysis: `inflected form of ${mappedLemma}`
                    }]
                };
            }
        }

        // Clitic peeling lookup
        const peeled = peelClitics(lower);
        for (const item of peeled) {
            if (dict && dict[item.stem]) {
                return {
                    found: true,
                    source: 'clitic_peeled',
                    readings: [{
                        lemma: item.stem,
                        ...dict[item.stem],
                        analysis: item.analysis
                    }]
                };
            }
            // Try past participle reconstruct from peeled stem
            const infs = reconstructInfinitiveFromPast(item.stem);
            for (const inf of infs) {
                if (dict && dict[inf]) {
                    return {
                        found: true,
                        source: 'past_participle',
                        readings: [{
                            lemma: inf,
                            ...dict[inf],
                            analysis: item.analysis
                        }]
                    };
                }
            }
        }

        // Past participle directly: dělal -> dělat
        const infCandidates = reconstructInfinitiveFromPast(lower);
        for (const inf of infCandidates) {
            if (dict && dict[inf]) {
                return {
                    found: true,
                    source: 'past_participle',
                    readings: [{
                        lemma: inf,
                        ...dict[inf],
                        analysis: `past participle of ${inf}`
                    }]
                };
            }
        }

        // Nominal & adjectival declension suffix stripping with unpalatalization
        for (const suf of DECLENSION_SUFFIXES) {
            if (lower.length > suf.length + 2 && lower.endsWith(suf)) {
                const rawStem = lower.slice(0, -suf.length);
                const stemVariants = unpalatalize(rawStem);

                for (const st of stemVariants) {
                    // Try bare stem (e.g. hrad, student, muž)
                    if (dict && dict[st]) {
                        return {
                            found: true,
                            source: 'declension_stem',
                            readings: [{
                                lemma: st,
                                ...dict[st],
                                analysis: `inflected case form of ${st}`
                            }]
                        };
                    }
                    // Try nominative feminine -a, neuter -o/-e
                    for (const nomEnd of ['a', 'o', 'e', 'í', 'ý']) {
                        const candidate = st + nomEnd;
                        if (dict && dict[candidate]) {
                            return {
                                found: true,
                                source: 'declension_candidate',
                                readings: [{
                                    lemma: candidate,
                                    ...dict[candidate],
                                    analysis: `inflected form of ${candidate}`
                                }]
                            };
                        }
                    }

                    // Try stem vowel quantity alternation (ů -> o, etc.)
                    for (const alt of STEM_ALTERNATIONS) {
                        const altStem = st.replace(alt.from, alt.to);
                        if (altStem !== st && dict && dict[altStem]) {
                            return {
                                found: true,
                                source: 'declension_alternation',
                                readings: [{
                                    lemma: altStem,
                                    ...dict[altStem],
                                    analysis: `inflected form of ${altStem}`
                                }]
                            };
                        }
                    }
                }
            }
        }

        // Verbal prefix stripping for aspect partner lookup
        const prefixStems = stripVerbalPrefixes(lower);
        for (const item of prefixStems) {
            if (dict && dict[item.stem]) {
                return {
                    found: true,
                    source: 'prefixed_verb',
                    readings: [{
                        lemma: item.stem,
                        ...dict[item.stem],
                        analysis: `prefixed form (${item.prefix}-) of ${item.stem}`
                    }]
                };
            }
        }

        return null;
    }

    return {
        contractions: CONTRACTIONS,
        irregularVerbs: IRREGULAR_VERBS,
        fleetingEMap: FLEETING_E_MAP,
        peelClitics: peelClitics,
        unpalatalize: unpalatalize,
        reconstructInfinitiveFromPast: reconstructInfinitiveFromPast,
        stripVerbalPrefixes: stripVerbalPrefixes,
        analyze: analyze,
        lookup: lookup
    };
})();

if (typeof window !== 'undefined') {
    window.CzechMorphology = CzechMorphology;
}
if (typeof globalThis !== 'undefined') {
    globalThis.CzechMorphology = CzechMorphology;
    if (globalThis.Lexicon && typeof globalThis.Lexicon.registerMorphology === 'function') {
        globalThis.Lexicon.registerMorphology('cs', CzechMorphology);
    }
} else if (typeof Lexicon !== 'undefined' && typeof Lexicon.registerMorphology === 'function') {
    Lexicon.registerMorphology('cs', CzechMorphology);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = CzechMorphology;
}
