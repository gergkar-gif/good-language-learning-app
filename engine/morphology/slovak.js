// ============================================
// SLOVAK MORPHOLOGY — runtime inflection & conjugation fallback
// ============================================
// Mirrors CzechMorphology, PolishMorphology, and HungarianMorphology for Slovak.
// Provides:
// 1. Prepositional contractions & vocalizations (vo, so, zo, ku, odo, podo, predo, nado, bezo, cezo).
// 2. Mobile past auxiliary clitics & conditional peeling (-s, som, si, sme, ste, by som, by si, by, by sme, by ste).
// 3. Regular conjugation reconstruction (Conjugations -ať/-ám, -ieť/-ím, -iť/-ím, -ovať/-ujem, -núť/-nem, past in -l-).
// 4. Irregular root & core verb analysis (byť, mať, môcť, chcieť, vedieť, ísť, prísť, odísť, jesť, piť, brať, vziať, dať, stáť, vidieť).
// 5. Verbal prefix stripping & aspect pair stems (po-, vy-, za-, pri-, od-, do-, na-, u-, pre-, roz-, s-, z-).
// 6. Nominal & adjectival declension stem stripping across 6 cases.
// 7. Qualitative & quantitative alternations (kôň:koňa, stôl:stola, nôž:noža, pes:psa, deň:dňa, otec:otca, mesto:miest).
// 8. Consonant palatalizations and soft stem alternations (chlapec:chlapci, človek:ľudia).
// 9. Reflexive particle stripping (sa, si).

const SlovakMorphology = (function () {
    'use strict';

    // Prepositional vocalizations & pronominal enclitics (-ň, -ňho)
    const CONTRACTIONS = {
        'vo':     { lemma: 'v', pos: 'preposition', translation: 'in, into', analysis: 'vocalized form of v (before consonant clusters)' },
        'so':     { lemma: 's', pos: 'preposition', translation: 'with', analysis: 'vocalized form of s (before consonant clusters)' },
        'zo':     { lemma: 'z', pos: 'preposition', translation: 'from, out of', analysis: 'vocalized form of z (before consonant clusters)' },
        'ku':     { lemma: 'k', pos: 'preposition', translation: 'to, towards', analysis: 'vocalized form of k (before k, g, or clusters)' },
        'odo':    { lemma: 'od', pos: 'preposition', translation: 'from', analysis: 'vocalized form of od' },
        'podo':   { lemma: 'pod', pos: 'preposition', translation: 'under', analysis: 'vocalized form of pod' },
        'predo':  { lemma: 'pred', pos: 'preposition', translation: 'in front of, before', analysis: 'vocalized form of pred' },
        'nado':   { lemma: 'nad', pos: 'preposition', translation: 'above, over', analysis: 'vocalized form of nad' },
        'bezo':   { lemma: 'bez', pos: 'preposition', translation: 'without', analysis: 'vocalized form of bez' },
        'cezo':   { lemma: 'cez', pos: 'preposition', translation: 'across, through', analysis: 'vocalized form of cez' },

        // Pronominal enclitics (-ň / -ňho = neho / ho after prepositions)
        'preň':   { lemma: 'pre', pos: 'contraction', translation: 'for him/it', analysis: 'pre + on (neho)' },
        'preňho': { lemma: 'pre', pos: 'contraction', translation: 'for him', analysis: 'pre + on (neho)' },
        'oň':     { lemma: 'o', pos: 'contraction', translation: 'about him/it', analysis: 'o + on (neho)' },
        'oňho':   { lemma: 'o', pos: 'contraction', translation: 'about him', analysis: 'o + on (neho)' },
        'naň':    { lemma: 'na', pos: 'contraction', translation: 'onto him/it', analysis: 'na + on (neho)' },
        'naňho':  { lemma: 'na', pos: 'contraction', translation: 'onto him', analysis: 'na + on (neho)' },
        'zaň':    { lemma: 'za', pos: 'contraction', translation: 'for/behind him/it', analysis: 'za + on (neho)' },
        'zaňho':  { lemma: 'za', pos: 'contraction', translation: 'for him', analysis: 'za + on (neho)' },
        'doň':    { lemma: 'do', pos: 'contraction', translation: 'into him/it', analysis: 'do + on (neho)' },
        'doňho':  { lemma: 'do', pos: 'contraction', translation: 'into him', analysis: 'do + on (neho)' },
        'podň':   { lemma: 'pod', pos: 'contraction', translation: 'under him/it', analysis: 'pod + on (neho)' },
        'uňho':   { lemma: 'u', pos: 'contraction', translation: 'at his place', analysis: 'u + on (neho)' },

        // Short personal pronoun enclitics
        'ma':     { lemma: 'ja', pos: 'pronoun', translation: 'me', analysis: 'Accusative/Genitive short form of ja' },
        'ťa':     { lemma: 'ty', pos: 'pronoun', translation: 'you', analysis: 'Accusative/Genitive short form of ty' },
        'sa':     { lemma: 'seba', pos: 'pronoun', translation: 'oneself', analysis: 'Reflexive accusative pronoun' },
        'mi':     { lemma: 'ja', pos: 'pronoun', translation: 'to me', analysis: 'Dative short form of ja' },
        'ti':     { lemma: 'ty', pos: 'pronoun', translation: 'to you', analysis: 'Dative short form of ty' },
        'si':     { lemma: 'seba', pos: 'pronoun', translation: 'to oneself', analysis: 'Reflexive dative pronoun' },
        'mu':     { lemma: 'on', pos: 'pronoun', translation: 'to him', analysis: 'Dative short form of on/ono' },
        'ho':     { lemma: 'on', pos: 'pronoun', translation: 'him/it', analysis: 'Accusative/Genitive short form of on/ono' }
    };

    // Core irregular verbs lookup map
    const IRREGULAR_VERBS = {
        byť: {
            forms: {
                som: 'Present, 1st person singular',
                si: 'Present, 2nd person singular',
                je: 'Present, 3rd person singular',
                sme: 'Present, 1st person plural',
                ste: 'Present, 2nd person plural',
                sú: 'Present, 3rd person plural',
                budem: 'Future, 1st person singular',
                budeš: 'Future, 2nd person singular',
                bude: 'Future, 3rd person singular',
                budeme: 'Future, 1st person plural',
                budete: 'Future, 2nd person plural',
                budú: 'Future, 3rd person plural',
                bol: 'Past, 3rd person singular (masculine)',
                bola: 'Past, 3rd person singular (feminine)',
                bolo: 'Past, 3rd person singular (neuter)',
                boli: 'Past, 3rd person plural (all genders)',
                buď: 'Imperative singular',
                buďme: 'Imperative 1st person plural',
                buďte: 'Imperative 2nd person plural'
            }
        },
        mať: {
            forms: {
                mám: 'Present, 1st person singular',
                máš: 'Present, 2nd person singular',
                má: 'Present, 3rd person singular',
                máme: 'Present, 1st person plural',
                máte: 'Present, 2nd person plural',
                majú: 'Present, 3rd person plural',
                mal: 'Past, 3rd person singular (masculine)',
                mala: 'Past, 3rd person singular (feminine)',
                malo: 'Past, 3rd person singular (neuter)',
                mali: 'Past, 3rd person plural',
                maj: 'Imperative singular',
                majme: 'Imperative 1st person plural',
                majte: 'Imperative 2nd person plural'
            }
        },
        môcť: {
            forms: {
                môžem: 'Present, 1st person singular',
                môžeš: 'Present, 2nd person singular',
                môže: 'Present, 3rd person singular',
                môžeme: 'Present, 1st person plural',
                môžete: 'Present, 2nd person plural',
                môžu: 'Present, 3rd person plural',
                mohol: 'Past, 3rd person singular (masculine)',
                mohla: 'Past, 3rd person singular (feminine)',
                mohlo: 'Past, 3rd person singular (neuter)',
                mohli: 'Past, 3rd person plural'
            }
        },
        chcieť: {
            forms: {
                chcem: 'Present, 1st person singular',
                chceš: 'Present, 2nd person singular',
                chce: 'Present, 3rd person singular',
                chceme: 'Present, 1st person plural',
                chcete: 'Present, 2nd person plural',
                chcú: 'Present, 3rd person plural',
                chcel: 'Past, 3rd person singular (masculine)',
                chcela: 'Past, 3rd person singular (feminine)',
                chcelo: 'Past, 3rd person singular (neuter)',
                chceli: 'Past, 3rd person plural',
                chci: 'Imperative singular',
                chcime: 'Imperative 1st person plural',
                chcite: 'Imperative 2nd person plural'
            }
        },
        vedieť: {
            forms: {
                viem: 'Present, 1st person singular',
                vieš: 'Present, 2nd person singular',
                vie: 'Present, 3rd person singular',
                vieme: 'Present, 1st person plural',
                viete: 'Present, 2nd person plural',
                vedia: 'Present, 3rd person plural',
                vedel: 'Past, 3rd person singular (masculine)',
                vedela: 'Past, 3rd person singular (feminine)',
                vedelo: 'Past, 3rd person singular (neuter)',
                vedeli: 'Past, 3rd person plural',
                vedz: 'Imperative singular',
                vedzme: 'Imperative 1st person plural',
                vedzte: 'Imperative 2nd person plural'
            }
        },
        ísť: {
            forms: {
                idem: 'Present, 1st person singular',
                ideš: 'Present, 2nd person singular',
                ide: 'Present, 3rd person singular',
                ideme: 'Present, 1st person plural',
                idete: 'Present, 2nd person plural',
                idú: 'Present, 3rd person plural',
                išiel: 'Past, 3rd person singular (masculine)',
                šla: 'Past, 3rd person singular (feminine)',
                išla: 'Past, 3rd person singular (feminine)',
                šlo: 'Past, 3rd person singular (neuter)',
                išlo: 'Past, 3rd person singular (neuter)',
                šli: 'Past, 3rd person plural',
                išli: 'Past, 3rd person plural',
                pôjdem: 'Future, 1st person singular',
                pôjdeš: 'Future, 2nd person singular',
                pôjde: 'Future, 3rd person singular',
                pôjdeme: 'Future, 1st person plural',
                pôjdete: 'Future, 2nd person plural',
                pôjdu: 'Future, 3rd person plural',
                choď: 'Imperative singular',
                poďme: 'Imperative 1st person plural',
                choďte: 'Imperative 2nd person plural'
            }
        },
        prísť: {
            forms: {
                prídem: 'Future/Present, 1st person singular',
                prídeš: 'Future/Present, 2nd person singular',
                príde: 'Future/Present, 3rd person singular',
                prídeme: 'Future/Present, 1st person plural',
                prídete: 'Future/Present, 2nd person plural',
                prídu: 'Future/Present, 3rd person plural',
                prišiel: 'Past, 3rd person singular (masculine)',
                prišla: 'Past, 3rd person singular (feminine)',
                prišlo: 'Past, 3rd person singular (neuter)',
                prišli: 'Past, 3rd person plural',
                príď: 'Imperative singular',
                príďme: 'Imperative 1st person plural',
                príďte: 'Imperative 2nd person plural'
            }
        },
        odísť: {
            forms: {
                odídem: 'Future/Present, 1st person singular',
                odídeš: 'Future/Present, 2nd person singular',
                odíde: 'Future/Present, 3rd person singular',
                odídeme: 'Future/Present, 1st person plural',
                odídete: 'Future/Present, 2nd person plural',
                odídu: 'Future/Present, 3rd person plural',
                odišiel: 'Past, 3rd person singular (masculine)',
                odišla: 'Past, 3rd person singular (feminine)',
                odišlo: 'Past, 3rd person singular (neuter)',
                odišli: 'Past, 3rd person plural',
                odíď: 'Imperative singular',
                odíďme: 'Imperative 1st person plural',
                odíďte: 'Imperative 2nd person plural'
            }
        },
        jesť: {
            forms: {
                jem: 'Present, 1st person singular',
                ješ: 'Present, 2nd person singular',
                je: 'Present, 3rd person singular',
                jeme: 'Present, 1st person plural',
                jete: 'Present, 2nd person plural',
                jedia: 'Present, 3rd person plural',
                jedol: 'Past, 3rd person singular (masculine)',
                jedla: 'Past, 3rd person singular (feminine)',
                jedlo: 'Past, 3rd person singular (neuter)',
                jedli: 'Past, 3rd person plural',
                jedz: 'Imperative singular',
                jedzme: 'Imperative 1st person plural',
                jedzte: 'Imperative 2nd person plural'
            }
        },
        piť: {
            forms: {
                pijem: 'Present, 1st person singular',
                piješ: 'Present, 2nd person singular',
                pije: 'Present, 3rd person singular',
                pijeme: 'Present, 1st person plural',
                pijete: 'Present, 2nd person plural',
                pijú: 'Present, 3rd person plural',
                pil: 'Past, 3rd person singular (masculine)',
                pila: 'Past, 3rd person singular (feminine)',
                pilo: 'Past, 3rd person singular (neuter)',
                pili: 'Past, 3rd person plural',
                pi: 'Imperative singular',
                pime: 'Imperative 1st person plural',
                pite: 'Imperative 2nd person plural'
            }
        },
        brať: {
            forms: {
                beriem: 'Present, 1st person singular',
                berieš: 'Present, 2nd person singular',
                berie: 'Present, 3rd person singular',
                berieme: 'Present, 1st person plural',
                beriete: 'Present, 2nd person plural',
                berú: 'Present, 3rd person plural',
                bral: 'Past, 3rd person singular (masculine)',
                brala: 'Past, 3rd person singular (feminine)',
                bralo: 'Past, 3rd person singular (neuter)',
                brali: 'Past, 3rd person plural',
                ber: 'Imperative singular',
                berme: 'Imperative 1st person plural',
                berte: 'Imperative 2nd person plural'
            }
        },
        vziať: {
            forms: {
                vezmem: 'Future/Present, 1st person singular',
                vezmeš: 'Future/Present, 2nd person singular',
                vezme: 'Future/Present, 3rd person singular',
                vezmeme: 'Future/Present, 1st person plural',
                vezmete: 'Future/Present, 2nd person plural',
                vezmú: 'Future/Present, 3rd person plural',
                vzal: 'Past, 3rd person singular (masculine)',
                vzala: 'Past, 3rd person singular (feminine)',
                vzalo: 'Past, 3rd person singular (neuter)',
                vzali: 'Past, 3rd person plural',
                vezmi: 'Imperative singular',
                vezmime: 'Imperative 1st person plural',
                vezmite: 'Imperative 2nd person plural'
            }
        },
        dať: {
            forms: {
                dám: 'Future/Present, 1st person singular',
                dáš: 'Future/Present, 2nd person singular',
                dá: 'Future/Present, 3rd person singular',
                dáme: 'Future/Present, 1st person plural',
                dáte: 'Future/Present, 2nd person plural',
                dajú: 'Future/Present, 3rd person plural',
                dal: 'Past, 3rd person singular (masculine)',
                dala: 'Past, 3rd person singular (feminine)',
                dalo: 'Past, 3rd person singular (neuter)',
                dali: 'Past, 3rd person plural',
                daj: 'Imperative singular',
                dajme: 'Imperative 1st person plural',
                dajte: 'Imperative 2nd person plural'
            }
        },
        stáť: {
            forms: {
                stojím: 'Present, 1st person singular',
                stojíš: 'Present, 2nd person singular',
                stojí: 'Present, 3rd person singular',
                stojíme: 'Present, 1st person plural',
                stojíte: 'Present, 2nd person plural',
                stoja: 'Present, 3rd person plural',
                stál: 'Past, 3rd person singular (masculine)',
                stála: 'Past, 3rd person singular (feminine)',
                stálo: 'Past, 3rd person singular (neuter)',
                stáli: 'Past, 3rd person plural',
                stoj: 'Imperative singular',
                stojme: 'Imperative 1st person plural',
                stojte: 'Imperative 2nd person plural'
            }
        },
        vidieť: {
            forms: {
                vidím: 'Present, 1st person singular',
                vidíš: 'Present, 2nd person singular',
                vidí: 'Present, 3rd person singular',
                vidíme: 'Present, 1st person plural',
                vidíte: 'Present, 2nd person plural',
                vidia: 'Present, 3rd person plural',
                videl: 'Past, 3rd person singular (masculine)',
                videla: 'Past, 3rd person singular (feminine)',
                videlo: 'Past, 3rd person singular (neuter)',
                videli: 'Past, 3rd person plural',
                viď: 'Imperative singular',
                viďme: 'Imperative 1st person plural',
                viďte: 'Imperative 2nd person plural'
            }
        },
        povedať: {
            forms: {
                poviem: 'Future/Present, 1st person singular',
                povieš: 'Future/Present, 2nd person singular',
                povie: 'Future/Present, 3rd person singular',
                povieme: 'Future/Present, 1st person plural',
                poviete: 'Future/Present, 2nd person plural',
                povedia: 'Future/Present, 3rd person plural',
                povedal: 'Past, 3rd person singular (masculine)',
                povedala: 'Past, 3rd person singular (feminine)',
                povedalo: 'Past, 3rd person singular (neuter)',
                povedali: 'Past, 3rd person plural',
                povedz: 'Imperative singular',
                povedzme: 'Imperative 1st person plural',
                povedzte: 'Imperative 2nd person plural'
            }
        }
    };

    // Vowel quantity / diphthong alternations in Slovak stems
    const STEM_ALTERNATIONS = [
        // ô : o (stôl -> stola, kôň -> koňa, nôž -> noža, dôvod -> dôvodu)
        { from: /ô/, to: 'o' },
        // ie : e (chlieb -> chleba, vietor -> vetra, trieda -> tried)
        { from: /ie/, to: 'e' },
        // á : a (jamy -> jama, vrana -> vrán)
        { from: /á/, to: 'a' },
        // í : i
        { from: /í/, to: 'i' },
        // ú : u
        { from: /ú/, to: 'u' }
    ];

    // Fleeting vowels (vkladné samohlásky e/o/ie)
    const FLEETING_VOWELS_MAP = {
        'psa': 'pes', 'psu': 'pes', 'psom': 'pes', 'psy': 'pes', 'psov': 'pes', 'psoch': 'pes', 'psami': 'pes',
        'dňa': 'deň', 'dňu': 'deň', 'dňom': 'deň', 'dni': 'deň', 'dní': 'deň', 'dňoch': 'deň', 'dňami': 'deň',
        'otca': 'otec', 'otcovi': 'otec', 'otcom': 'otec', 'otcovia': 'otec', 'otcov': 'otec', 'otcoch': 'otec', 'otcami': 'otec',
        'chlapca': 'chlapec', 'chlapcovi': 'chlapec', 'chlapcom': 'chlapec', 'chlapci': 'chlapec', 'chlapcov': 'chlapec', 'chlapcoch': 'chlapec', 'chlapcami': 'chlapec',
        'orla': 'orol', 'orlovi': 'orol', 'orlom': 'orol', 'orly': 'orol', 'orlov': 'orol',
        'cukru': 'cukor', 'cukrom': 'cukor',
        'stola': 'stôl', 'stolu': 'stôl', 'stolom': 'stôl', 'stoly': 'stôl', 'stoloch': 'stôl', 'stolmi': 'stôl',
        'koňa': 'kôň', 'koňovi': 'kôň', 'koňom': 'kôň', 'kone': 'kôň', 'koňoch': 'kôň', 'koňmi': 'kôň',
        'noža': 'nôž', 'nožu': 'nôž', 'nožom': 'nôž', 'nože': 'nôž', 'nožoch': 'nôž', 'nožmi': 'nôž',
        'dôvodu': 'dôvod', 'dôvodom': 'dôvod', 'dôvody': 'dôvod', 'dôvodoch': 'dôvod',
        'chleba': 'chlieb', 'chlebu': 'chlieb', 'chlebom': 'chlieb', 'chleby': 'chlieb',
        'okien': 'okno', 'oknám': 'okno', 'oknami': 'okno', 'oknách': 'okno',
        'miest': 'mesto', 'mestám': 'mesto', 'mestami': 'mesto', 'mestách': 'mesto',
        'ľudia': 'človek', 'ľudí': 'človek', 'ľuďom': 'človek', 'ľuďoch': 'človek', 'ľuďmi': 'človek'
    };

    // Peel enclitics: past tense -s, conditional conjunctions
    function peelClitics(word) {
        const results = [];
        const lower = word.toLowerCase();

        // 2nd person past clitic: robils -> robil + s, bols -> bol + s
        if (lower.length >= 4 && lower.endsWith('ls')) {
            results.push({ stem: lower.slice(0, -1), clitic: 's', analysis: '2nd person singular past auxiliary enclitic (-s = si)' });
        }
        if (lower.length > 4 && (lower.endsWith('las') || lower.endsWith('los') || lower.endsWith('lis'))) {
            results.push({ stem: lower.slice(0, -1), clitic: 's', analysis: '2nd person past auxiliary enclitic (-s = si)' });
        }

        // Conditional forms with fused conjunctions (abys, aby som, keby...)
        if (lower.startsWith('aby') || lower.startsWith('keby')) {
            const base = lower.startsWith('keby') ? 'keby' : 'aby';
            const suffix = lower.slice(base.length);
            if (suffix === 's' || suffix === '') {
                results.push({ stem: base, clitic: suffix, analysis: `conditional conjunction ${base} + person ending` });
            }
        }

        return results;
    }

    // Reverse past tense participle ending: robil / robila / robili -> robiť
    function reconstructInfinitiveFromPast(participle) {
        const candidates = [];
        const lower = participle.toLowerCase();
        let stem = lower;
        if (lower.endsWith('li') || lower.endsWith('la') || lower.endsWith('lo')) {
            stem = lower.slice(0, -1);
        }
        if (stem.endsWith('l')) {
            const root = stem.slice(0, -1);
            candidates.push(root + 'ť');
            if (root.endsWith('a')) candidates.push(root + 'ť');
            if (root.endsWith('ie')) candidates.push(root + 'ť');
            if (root.endsWith('i')) candidates.push(root + 'ť');
            if (root.endsWith('nú')) candidates.push(root.slice(0, -2) + 'núť');
        }
        return candidates;
    }

    // Strip common productive verbal prefixes to discover base imperfective partner
    function stripVerbalPrefixes(word) {
        const prefixes = ['pre', 'pri', 'roz', 'od', 'po', 'vy', 'za', 'do', 'na', 'u', 's', 'z', 'o', 'ob', 'pod'];
        const results = [];
        for (const p of prefixes) {
            if (word.startsWith(p) && word.length > p.length + 3) {
                results.push({ prefix: p, stem: word.slice(p.length) });
            }
        }
        return results;
    }

    // Nominal, pronominal & adjectival declension suffixes across 6 Slovak cases
    const DECLENSION_SUFFIXES = [
        'ieho', 'iemu', 'ieho', 'iach', 'iami',                               // Soft adj endings
        'ého', 'ému', 'ých', 'ými', 'ého', 'ému', 'ích', 'ími',               // Hard adj endings
        'ovi', 'ovia', 'och', 'ami', 'mi',                                    // Animate masculine plural/dative
        'om', 'ou', 'ov', 'ím', 'am', 'ám',                                   // Case endings
        'ia', 'ie', 'iu', 'ov', 'ev',                                         // Plurals & Genitives
        'e', 'a', 'u', 'i', 'í', 'y', 'o', 'á'                                // Short case endings
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

        // 3. Fleeting vowels direct map
        if (FLEETING_VOWELS_MAP[lower]) {
            return {
                matched: true,
                type: 'alternation',
                lemma: FLEETING_VOWELS_MAP[lower],
                analysis: 'stem alternation (fleeting vowel / diphthong ô:o)'
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
                        translation: dictEntry.en || `to ${vlemma}`,
                        analysis: vdata.forms[lower],
                        type: 'verb'
                    }]
                };
            }
        }

        // Fleeting vowel / stem alternation map
        if (FLEETING_VOWELS_MAP[lower]) {
            const lemma = FLEETING_VOWELS_MAP[lower];
            const dictEntry = (dict && dict[lemma]) || {};
            return {
                found: true,
                source: 'alternation',
                readings: [{
                    lemma: lemma,
                    translation: dictEntry.en || lemma,
                    type: dictEntry.type || 'noun',
                    analysis: 'stem alternation (fleeting vowel e/o/ie or diphthong ô:o)'
                }]
            };
        }

        // Clitic peeling
        const clitics = peelClitics(lower);
        for (const c of clitics) {
            if (dict && dict[c.stem]) {
                return {
                    found: true,
                    source: 'clitic',
                    readings: [{
                        lemma: c.stem,
                        translation: dict[c.stem].en,
                        analysis: c.analysis,
                        type: dict[c.stem].type
                    }]
                };
            }
        }

        // Past tense reconstruction
        const pastReconstructed = reconstructInfinitiveFromPast(lower);
        for (const cand of pastReconstructed) {
            if (dict && dict[cand]) {
                return {
                    found: true,
                    source: 'past_participle',
                    readings: [{
                        lemma: cand,
                        translation: dict[cand].en,
                        type: 'verb',
                        analysis: 'past tense form'
                    }]
                };
            }
        }

        // Declension stem stripping with vowel quantity alternations
        for (const sfx of DECLENSION_SUFFIXES) {
            if (lower.length > sfx.length + 2 && lower.endsWith(sfx)) {
                const stem = lower.slice(0, -sfx.length);
                const stemVariants = [stem];

                // Check stem alternations (e.g. o -> ô, e -> ie)
                if (stem.includes('o')) {
                    stemVariants.push(stem.replace(/o/g, 'ô'));
                }
                if (stem.includes('e')) {
                    stemVariants.push(stem.replace(/e/g, 'ie'));
                }

                for (const svar of stemVariants) {
                    // Try bare root (masculine noun / short form)
                    if (dict && dict[svar]) {
                        return {
                            found: true,
                            source: 'declension',
                            readings: [{
                                lemma: svar,
                                translation: dict[svar].en,
                                type: dict[svar].type,
                                analysis: `inflected form (-${sfx})`
                            }]
                        };
                    }
                    // Try with standard noun endings (-a, -o, -e)
                    for (const baseEnd of ['a', 'o', 'e', 'ť']) {
                        const candidate = svar + baseEnd;
                        if (dict && dict[candidate]) {
                            return {
                                found: true,
                                source: 'declension',
                                readings: [{
                                    lemma: candidate,
                                    translation: dict[candidate].en,
                                    type: dict[candidate].type,
                                    analysis: `inflected form (-${sfx})`
                                }]
                            };
                        }
                    }
                    // Try adjective ending -ý / -í / -y
                    for (const adjEnd of ['ý', 'í', 'y']) {
                        const candidate = svar + adjEnd;
                        if (dict && dict[candidate]) {
                            return {
                                found: true,
                                source: 'adjective_declension',
                                readings: [{
                                    lemma: candidate,
                                    translation: dict[candidate].en,
                                    type: 'adjective',
                                    analysis: `adjective case ending (-${sfx})`
                                }]
                            };
                        }
                    }
                }
            }
        }

        // Verbal prefix stripping
        const stripped = stripVerbalPrefixes(lower);
        for (const item of stripped) {
            if (dict && dict[item.stem]) {
                return {
                    found: true,
                    source: 'prefixed_verb',
                    readings: [{
                        lemma: item.stem,
                        translation: dict[item.stem].en,
                        type: 'verb',
                        analysis: `prefixed form (${item.prefix}- + ${item.stem})`
                    }]
                };
            }
        }

        return { found: false, word: lower };
    }

    return {
        analyze: analyze,
        lookup: lookup,
        peelClitics: peelClitics,
        reconstructInfinitiveFromPast: reconstructInfinitiveFromPast,
        stripVerbalPrefixes: stripVerbalPrefixes,
        contractions: CONTRACTIONS,
        irregularVerbs: IRREGULAR_VERBS,
        fleetingVowels: FLEETING_VOWELS_MAP
    };
})();

// Export globally and for CommonJS tests
if (typeof window !== 'undefined') {
    window.SlovakMorphology = SlovakMorphology;
}
if (typeof global !== 'undefined') {
    global.SlovakMorphology = SlovakMorphology;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SlovakMorphology;
}
