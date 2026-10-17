// ============================================
// ITALIAN MORPHOLOGY — runtime inflection & conjugation fallback
// ============================================
// Mirrors SpanishMorphology, HungarianMorphology, and FrenchMorphology for Italian.
// Provides:
// 1. Contraction decomposition (preposizioni articolate: del, dello, della, dell', dei, degli, delle,
//    al, allo, alla, all', ai, agli, alle, dal, nel, sul...).
// 2. Elision resolution (l', d', c', un', all', dell', quest', tant').
// 3. Regular conjugation reconstruction (1st group -are, 2nd group -ere, 3rd group -ire,
//    and inchoative -isc- pattern).
// 4. Irregular root & compound verb analysis (essere, avere, andare, fare, dare, stare,
//    dovere, potere, volere, venire, dire, sapere, uscire, bere, scegliere, salire, piacere).
// 5. Enclitic pronoun splitting (infinitives, gerunds, imperatives: vederlo, parlandogli, dimmi, andarsene).
// 6. Gender and number reconstruction for adjectives and nouns (-o/-a/-i/-e, -e/-i, irregular plurals).
// 7. Contextual definite article assignment (il, lo, la, l', i, gli, le).

const ItalianMorphology = (function () {
    'use strict';

    const CONTRACTIONS = {
        'del':   { lemma: 'di', pos: 'contraction', translation: 'of the, some (masculine)', analysis: 'di + il (masculine singular)' },
        'dello': { lemma: 'di', pos: 'contraction', translation: 'of the, some (masculine before z/s+cons)', analysis: 'di + lo (masculine singular)' },
        'della': { lemma: 'di', pos: 'contraction', translation: 'of the, some (feminine)', analysis: 'di + la (feminine singular)' },
        "dell'": { lemma: 'di', pos: 'contraction', translation: 'of the, some (elided)', analysis: "di + l' (singular before vowel)" },
        'dell':  { lemma: 'di', pos: 'contraction', translation: 'of the, some (elided)', analysis: "di + l' (singular before vowel)" },
        'dei':   { lemma: 'di', pos: 'contraction', translation: 'of the, some (masculine plural)', analysis: 'di + i (masculine plural)' },
        'degli': { lemma: 'di', pos: 'contraction', translation: 'of the, some (masculine plural)', analysis: 'di + gli (masculine plural)' },
        'delle': { lemma: 'di', pos: 'contraction', translation: 'of the, some (feminine plural)', analysis: 'di + le (feminine plural)' },

        'al':    { lemma: 'a', pos: 'contraction', translation: 'to the, at the (masculine)', analysis: 'a + il (masculine singular)' },
        'allo':  { lemma: 'a', pos: 'contraction', translation: 'to the, at the (masculine before z/s+cons)', analysis: 'a + lo (masculine singular)' },
        'alla':  { lemma: 'a', pos: 'contraction', translation: 'to the, at the (feminine)', analysis: 'a + la (feminine singular)' },
        "all'":  { lemma: 'a', pos: 'contraction', translation: 'to the, at the (elided)', analysis: "a + l' (singular before vowel)" },
        'all':   { lemma: 'a', pos: 'contraction', translation: 'to the, at the (elided)', analysis: "a + l' (singular before vowel)" },
        'ai':    { lemma: 'a', pos: 'contraction', translation: 'to the, at the (masculine plural)', analysis: 'a + i (masculine plural)' },
        'agli':  { lemma: 'a', pos: 'contraction', translation: 'to the, at the (masculine plural)', analysis: 'a + gli (masculine plural)' },
        'alle':  { lemma: 'a', pos: 'contraction', translation: 'to the, at the (feminine plural)', analysis: 'a + le (feminine plural)' },

        'dal':   { lemma: 'da', pos: 'contraction', translation: 'from the, by the (masculine)', analysis: 'da + il (masculine singular)' },
        'dallo': { lemma: 'da', pos: 'contraction', translation: 'from the, by the', analysis: 'da + lo (masculine singular)' },
        'dalla': { lemma: 'da', pos: 'contraction', translation: 'from the, by the (feminine)', analysis: 'da + la (feminine singular)' },
        "dall'": { lemma: 'da', pos: 'contraction', translation: 'from the, by the (elided)', analysis: "da + l' (singular before vowel)" },
        'dall':  { lemma: 'da', pos: 'contraction', translation: 'from the, by the (elided)', analysis: "da + l' (singular before vowel)" },
        'dai':   { lemma: 'da', pos: 'contraction', translation: 'from the, by the (masculine plural)', analysis: 'da + i (masculine plural)' },
        'dagli': { lemma: 'da', pos: 'contraction', translation: 'from the, by the (masculine plural)', analysis: 'da + gli (masculine plural)' },
        'dalle': { lemma: 'da', pos: 'contraction', translation: 'from the, by the (feminine plural)', analysis: 'da + le (feminine plural)' },

        'nel':   { lemma: 'in', pos: 'contraction', translation: 'in the (masculine)', analysis: 'in + il (masculine singular)' },
        'nello': { lemma: 'in', pos: 'contraction', translation: 'in the', analysis: 'in + lo (masculine singular)' },
        'nella': { lemma: 'in', pos: 'contraction', translation: 'in the (feminine)', analysis: 'in + la (feminine singular)' },
        "nell'": { lemma: 'in', pos: 'contraction', translation: 'in the (elided)', analysis: "in + l' (singular before vowel)" },
        'nell':  { lemma: 'in', pos: 'contraction', translation: 'in the (elided)', analysis: "in + l' (singular before vowel)" },
        'nei':   { lemma: 'in', pos: 'contraction', translation: 'in the (masculine plural)', analysis: 'in + i (masculine plural)' },
        'negli': { lemma: 'in', pos: 'contraction', translation: 'in the (masculine plural)', analysis: 'in + gli (masculine plural)' },
        'nelle': { lemma: 'in', pos: 'contraction', translation: 'in the (feminine plural)', analysis: 'in + le (feminine plural)' },

        'sul':   { lemma: 'su', pos: 'contraction', translation: 'on the (masculine)', analysis: 'su + il (masculine singular)' },
        'sullo': { lemma: 'su', pos: 'contraction', translation: 'on the', analysis: 'su + lo (masculine singular)' },
        'sulla': { lemma: 'su', pos: 'contraction', translation: 'on the (feminine)', analysis: 'su + la (feminine singular)' },
        "sull'": { lemma: 'su', pos: 'contraction', translation: 'on the (elided)', analysis: "su + l' (singular before vowel)" },
        'sull':  { lemma: 'su', pos: 'contraction', translation: 'on the (elided)', analysis: "su + l' (singular before vowel)" },
        'sui':   { lemma: 'su', pos: 'contraction', translation: 'on the (masculine plural)', analysis: 'su + i (masculine plural)' },
        'sugli': { lemma: 'su', pos: 'contraction', translation: 'on the (masculine plural)', analysis: 'su + gli (masculine plural)' },
        'sulle': { lemma: 'su', pos: 'contraction', translation: 'on the (feminine plural)', analysis: 'su + le (feminine plural)' }
    };

    const ELISIONS = {
        "c'": { lemma: 'ci', pos: 'pronoun', translation: 'there, us', analysis: 'locative/reflexive pronoun (elided)' },
        'c':  { lemma: 'ci', pos: 'pronoun', translation: 'there, us', analysis: 'locative/reflexive pronoun (elided)' },
        "l'": { lemma: 'il', pos: 'article', translation: 'the', analysis: 'definite article (elided)' },
        'l':  { lemma: 'il', pos: 'article', translation: 'the', analysis: 'definite article (elided)' },
        "d'": { lemma: 'di', pos: 'preposition', translation: 'of, from', analysis: 'preposition (elided)' },
        'd':  { lemma: 'di', pos: 'preposition', translation: 'of, from', analysis: 'preposition (elided)' },
        "m'": { lemma: 'mi', pos: 'pronoun', translation: 'me, myself', analysis: '1st person direct/indirect pronoun (elided)' },
        'm':  { lemma: 'mi', pos: 'pronoun', translation: 'me, myself', analysis: '1st person direct/indirect pronoun (elided)' },
        "t'": { lemma: 'ti', pos: 'pronoun', translation: 'you, yourself', analysis: '2nd person direct/indirect pronoun (elided)' },
        't':  { lemma: 'ti', pos: 'pronoun', translation: 'you, yourself', analysis: '2nd person direct/indirect pronoun (elided)' },
        "s'": { lemma: 'si', pos: 'pronoun', translation: 'oneself, himself, herself', analysis: '3rd person reflexive pronoun (elided)' },
        's':  { lemma: 'si', pos: 'pronoun', translation: 'oneself, himself, herself', analysis: '3rd person reflexive pronoun (elided)' },
        "v'": { lemma: 'vi', pos: 'pronoun', translation: 'you, to you, there', analysis: '2nd person plural / locative pronoun (elided)' },
        'v':  { lemma: 'vi', pos: 'pronoun', translation: 'you, to you, there', analysis: '2nd person plural / locative pronoun (elided)' },
        "un'": { lemma: 'una', pos: 'article', translation: 'a, an', analysis: 'feminine indefinite article (elided)' },
        'un':  { lemma: 'uno', pos: 'article', translation: 'a, an', analysis: 'masculine indefinite article (apocope)' }
    };

    const IRREGULAR_VERBS = {
        essere: {
            sono: 'Present, 1st person singular or 3rd person plural',
            sei: 'Present, 2nd person singular',
            'è': 'Present, 3rd person singular',
            siamo: 'Present, 1st person plural',
            siete: 'Present, 2nd person plural',
            stato: 'Past participle, masculine singular',
            stata: 'Past participle, feminine singular',
            stati: 'Past participle, masculine plural',
            state: 'Past participle, feminine plural',
            ero: 'Imperfect, 1st person singular',
            eri: 'Imperfect, 2nd person singular',
            era: 'Imperfect, 3rd person singular',
            eravamo: 'Imperfect, 1st person plural',
            eravate: 'Imperfect, 2nd person plural',
            erano: 'Imperfect, 3rd person plural',
            sarò: 'Future, 1st person singular',
            sarai: 'Future, 2nd person singular',
            sarà: 'Future, 3rd person singular',
            saremo: 'Future, 1st person plural',
            sarete: 'Future, 2nd person plural',
            saranno: 'Future, 3rd person plural',
            sarei: 'Conditional, 1st person singular',
            saresti: 'Conditional, 2nd person singular',
            sarebbe: 'Conditional, 3rd person singular',
            saremmo: 'Conditional, 1st person plural',
            sareste: 'Conditional, 2nd person plural',
            sarebbero: 'Conditional, 3rd person plural',
            sia: 'Subjunctive present, 1st/2nd/3rd person singular',
            siano: 'Subjunctive present, 3rd person plural',
            fossi: 'Subjunctive imperfect, 1st/2nd person singular',
            fosse: 'Subjunctive imperfect, 3rd person singular',
            fossimo: 'Subjunctive imperfect, 1st person plural',
            foste: 'Subjunctive imperfect, 2nd person plural',
            fossero: 'Subjunctive imperfect, 3rd person plural',
            fui: 'Past historic, 1st person singular',
            fosti: 'Past historic, 2nd person singular',
            fu: 'Past historic, 3rd person singular',
            fummo: 'Past historic, 1st person plural',
            furono: 'Past historic, 3rd person plural'
        },
        avere: {
            ho: 'Present, 1st person singular',
            hai: 'Present, 2nd person singular',
            ha: 'Present, 3rd person singular',
            abbiamo: 'Present, 1st person plural',
            avete: 'Present, 2nd person plural',
            hanno: 'Present, 3rd person plural',
            avuto: 'Past participle',
            avendo: 'Gerund',
            avevo: 'Imperfect, 1st person singular',
            avevi: 'Imperfect, 2nd person singular',
            aveva: 'Imperfect, 3rd person singular',
            avevamo: 'Imperfect, 1st person plural',
            avevate: 'Imperfect, 2nd person plural',
            avevano: 'Imperfect, 3rd person plural',
            avrò: 'Future, 1st person singular',
            avrai: 'Future, 2nd person singular',
            avrà: 'Future, 3rd person singular',
            avremo: 'Future, 1st person plural',
            avrete: 'Future, 2nd person plural',
            avranno: 'Future, 3rd person plural',
            avrei: 'Conditional, 1st person singular',
            avresti: 'Conditional, 2nd person singular',
            avrebbe: 'Conditional, 3rd person singular',
            avremmo: 'Conditional, 1st person plural',
            avreste: 'Conditional, 2nd person plural',
            avrebbero: 'Conditional, 3rd person plural',
            abbia: 'Subjunctive present, 1st/2nd/3rd person singular',
            abbiano: 'Subjunctive present, 3rd person plural',
            avessi: 'Subjunctive imperfect, 1st/2nd person singular',
            avesse: 'Subjunctive imperfect, 3rd person singular',
            avessimo: 'Subjunctive imperfect, 1st person plural',
            aveste: 'Subjunctive imperfect, 2nd person plural',
            avessero: 'Subjunctive imperfect, 3rd person plural'
        },
        andare: {
            vado: 'Present, 1st person singular',
            vai: 'Present, 2nd person singular',
            va: 'Present, 3rd person singular',
            andiamo: 'Present, 1st person plural',
            andate: 'Present, 2nd person plural',
            vanno: 'Present, 3rd person plural',
            andato: 'Past participle, masculine singular',
            andata: 'Past participle, feminine singular',
            andati: 'Past participle, masculine plural',
            andate: 'Past participle, feminine plural',
            andrò: 'Future, 1st person singular',
            andrai: 'Future, 2nd person singular',
            andrà: 'Future, 3rd person singular',
            andrei: 'Conditional, 1st person singular',
            vada: 'Subjunctive present, singular',
            vadano: 'Subjunctive present, 3rd person plural'
        },
        fare: {
            faccio: 'Present, 1st person singular',
            fai: 'Present, 2nd person singular',
            fa: 'Present, 3rd person singular',
            facciamo: 'Present, 1st person plural',
            fate: 'Present, 2nd person plural',
            fanno: 'Present, 3rd person plural',
            fatto: 'Past participle',
            facendo: 'Gerund',
            facevo: 'Imperfect, 1st person singular',
            facevi: 'Imperfect, 2nd person singular',
            faceva: 'Imperfect, 3rd person singular',
            farò: 'Future, 1st person singular',
            farai: 'Future, 2nd person singular',
            farà: 'Future, 3rd person singular',
            farei: 'Conditional, 1st person singular',
            faccia: 'Subjunctive present, singular',
            facciano: 'Subjunctive present, 3rd person plural',
            feci: 'Past historic, 1st person singular',
            fece: 'Past historic, 3rd person singular',
            fecero: 'Past historic, 3rd person plural'
        },
        potere: {
            posso: 'Present, 1st person singular',
            puoi: 'Present, 2nd person singular',
            può: 'Present, 3rd person singular',
            possiamo: 'Present, 1st person plural',
            potete: 'Present, 2nd person plural',
            possono: 'Present, 3rd person plural',
            potuto: 'Past participle',
            potrò: 'Future, 1st person singular',
            potrei: 'Conditional, 1st person singular',
            possa: 'Subjunctive present, singular',
            possano: 'Subjunctive present, 3rd person plural'
        },
        volere: {
            voglio: 'Present, 1st person singular',
            vuoi: 'Present, 2nd person singular',
            vuole: 'Present, 3rd person singular',
            vogliamo: 'Present, 1st person plural',
            volete: 'Present, 2nd person plural',
            vogliono: 'Present, 3rd person plural',
            voluto: 'Past participle',
            vorrò: 'Future, 1st person singular',
            vorrei: 'Conditional, 1st person singular',
            voglia: 'Subjunctive present, singular',
            vogliano: 'Subjunctive present, 3rd person plural'
        },
        dovere: {
            devo: 'Present, 1st person singular',
            debbo: 'Present, 1st person singular',
            devi: 'Present, 2nd person singular',
            deve: 'Present, 3rd person singular',
            dobbiamo: 'Present, 1st person plural',
            dovete: 'Present, 2nd person plural',
            devono: 'Present, 3rd person plural',
            dovuto: 'Past participle',
            dovrò: 'Future, 1st person singular',
            dovrei: 'Conditional, 1st person singular',
            debba: 'Subjunctive present, singular',
            debbano: 'Subjunctive present, 3rd person plural'
        },
        venire: {
            vengo: 'Present, 1st person singular',
            vieni: 'Present, 2nd person singular',
            viene: 'Present, 3rd person singular',
            veniamo: 'Present, 1st person plural',
            venite: 'Present, 2nd person plural',
            vengono: 'Present, 3rd person plural',
            venuto: 'Past participle',
            verrò: 'Future, 1st person singular',
            verrei: 'Conditional, 1st person singular',
            venga: 'Subjunctive present, singular',
            vengano: 'Subjunctive present, 3rd person plural'
        },
        dire: {
            dico: 'Present, 1st person singular',
            dici: 'Present, 2nd person singular',
            dice: 'Present, 3rd person singular',
            diciamo: 'Present, 1st person plural',
            dite: 'Present, 2nd person plural',
            dicono: 'Present, 3rd person plural',
            detto: 'Past participle',
            dicendo: 'Gerund',
            dicevo: 'Imperfect, 1st person singular',
            dirò: 'Future, 1st person singular',
            direi: 'Conditional, 1st person singular',
            dica: 'Subjunctive present, singular',
            dicano: 'Subjunctive present, 3rd person plural'
        },
        sapere: {
            so: 'Present, 1st person singular',
            sai: 'Present, 2nd person singular',
            sa: 'Present, 3rd person singular',
            sappiamo: 'Present, 1st person plural',
            sapete: 'Present, 2nd person plural',
            sanno: 'Present, 3rd person plural',
            saputo: 'Past participle',
            saprò: 'Future, 1st person singular',
            saprei: 'Conditional, 1st person singular',
            sappia: 'Subjunctive present, singular',
            sappiano: 'Subjunctive present, 3rd person plural'
        },
        stare: {
            sto: 'Present, 1st person singular',
            stai: 'Present, 2nd person singular',
            sta: 'Present, 3rd person singular',
            stiamo: 'Present, 1st person plural',
            state: 'Present, 2nd person plural',
            stanno: 'Present, 3rd person plural',
            stato: 'Past participle',
            stando: 'Gerund',
            stavo: 'Imperfect, 1st person singular',
            starò: 'Future, 1st person singular',
            starei: 'Conditional, 1st person singular',
            stia: 'Subjunctive present, singular',
            stiano: 'Subjunctive present, 3rd person plural'
        },
        dare: {
            do: 'Present, 1st person singular',
            dài: 'Present, 2nd person singular',
            dai: 'Present, 2nd person singular',
            dà: 'Present, 3rd person singular',
            da: 'Present, 3rd person singular',
            diamo: 'Present, 1st person plural',
            date: 'Present, 2nd person plural',
            danno: 'Present, 3rd person plural',
            dato: 'Past participle',
            dando: 'Gerund',
            davo: 'Imperfect, 1st person singular',
            darò: 'Future, 1st person singular',
            darei: 'Conditional, 1st person singular',
            dia: 'Subjunctive present, singular',
            diano: 'Subjunctive present, 3rd person plural'
        }
    };

    // Pronouns that attach enclitically to infinitives, gerunds, imperatives:
    // e.g. vederlo, parlargli, andarsene, dimmi, dandocelo
    const CLITICS = ['mi', 'ti', 'ci', 'vi', 'si', 'lo', 'la', 'li', 'le', 'gli', 'ne', 'melo', 'mela', 'meli', 'mele', 'telo', 'tela', 'teli', 'tele', 'celo', 'cela', 'celi', 'cele', 'velo', 'vela', 'veli', 'vele', 'glielo', 'gliela', 'glieli', 'gliele', 'gliene', 'sene', 'mene', 'tene', 'cene', 'vene'];

    function encliticStems(word) {
        if (!word || word.length < 5) return [];
        const stems = [];
        const lower = word.toLowerCase();

        for (const clitic of CLITICS) {
            if (lower.endsWith(clitic)) {
                const remainder = lower.slice(0, -clitic.length);
                if (remainder.length >= 3) {
                    // Infinitives drop trailing 'e' before clitic: parlare + lo -> parlarlo -> parlar + e = parlare
                    if (remainder.endsWith('ar') || remainder.endsWith('er') || remainder.endsWith('ir')) {
                        stems.push(remainder + 'e');
                    }
                    // Gerunds: parlando + lo = parlandolo -> parlando
                    if (remainder.endsWith('ando') || remainder.endsWith('endo')) {
                        stems.push(remainder);
                    }
                    // Doubled imperative consonants: dimmi -> di', fammi -> fa', dille -> di'
                    if (remainder.length >= 3 && remainder[remainder.length - 1] === clitic[0]) {
                        stems.push(remainder.slice(0, -1));
                    }
                    stems.push(remainder);
                }
            }
        }
        return stems;
    }

    function analyze(word, dictionary, verbExtra) {
        if (!word) return [];
        const results = [];
        const dict = dictionary || {};
        const lower = word.toLowerCase();

        // 1. Check irregular tables
        for (const [inf, table] of Object.entries(IRREGULAR_VERBS)) {
            if (table[lower]) {
                results.push({
                    lemma: inf,
                    mood: 'irregular',
                    tense: 'various',
                    analysis: table[lower]
                });
            }
        }
        if (results.length) return results;

        // 2. Regular verb endings analysis
        const ENDINGS = [
            // Presente
            { suffix: 'ano', mood: 'indicativo', tense: 'presente', person: '3-plural', drop: 3, add: 'are' },
            { suffix: 'ono', mood: 'indicativo', tense: 'presente', person: '3-plural', drop: 3, add: 'ere' },
            { suffix: 'ono', mood: 'indicativo', tense: 'presente', person: '3-plural', drop: 3, add: 'ire' },
            { suffix: 'iamo', mood: 'indicativo', tense: 'presente', person: '1-plural', drop: 4, add: ['are', 'ere', 'ire'] },
            { suffix: 'ate', mood: 'indicativo', tense: 'presente', person: '2-plural', drop: 3, add: 'are' },
            { suffix: 'ete', mood: 'indicativo', tense: 'presente', person: '2-plural', drop: 3, add: 'ere' },
            { suffix: 'ite', mood: 'indicativo', tense: 'presente', person: '2-plural', drop: 3, add: 'ire' },
            { suffix: 'isco', mood: 'indicativo', tense: 'presente', person: '1-singular', drop: 4, add: 'ire' },
            { suffix: 'isci', mood: 'indicativo', tense: 'presente', person: '2-singular', drop: 4, add: 'ire' },
            { suffix: 'isce', mood: 'indicativo', tense: 'presente', person: '3-singular', drop: 4, add: 'ire' },
            { suffix: 'iscono', mood: 'indicativo', tense: 'presente', person: '3-plural', drop: 6, add: 'ire' },
            { suffix: 'o', mood: 'indicativo', tense: 'presente', person: '1-singular', drop: 1, add: ['are', 'ere', 'ire'] },
            { suffix: 'i', mood: 'indicativo', tense: 'presente', person: '2-singular', drop: 1, add: ['are', 'ere', 'ire'] },
            { suffix: 'a', mood: 'indicativo', tense: 'presente', person: '3-singular', drop: 1, add: 'are' },
            { suffix: 'e', mood: 'indicativo', tense: 'presente', person: '3-singular', drop: 1, add: ['ere', 'ire'] },

            // Imperfetto
            { suffix: 'avo', mood: 'indicativo', tense: 'imperfetto', person: '1-singular', drop: 3, add: 'are' },
            { suffix: 'avi', mood: 'indicativo', tense: 'imperfetto', person: '2-singular', drop: 3, add: 'are' },
            { suffix: 'ava', mood: 'indicativo', tense: 'imperfetto', person: '3-singular', drop: 3, add: 'are' },
            { suffix: 'avamo', mood: 'indicativo', tense: 'imperfetto', person: '1-plural', drop: 5, add: 'are' },
            { suffix: 'avate', mood: 'indicativo', tense: 'imperfetto', person: '2-plural', drop: 5, add: 'are' },
            { suffix: 'avano', mood: 'indicativo', tense: 'imperfetto', person: '3-plural', drop: 5, add: 'are' },
            { suffix: 'evo', mood: 'indicativo', tense: 'imperfetto', person: '1-singular', drop: 3, add: 'ere' },
            { suffix: 'evi', mood: 'indicativo', tense: 'imperfetto', person: '2-singular', drop: 3, add: 'ere' },
            { suffix: 'eva', mood: 'indicativo', tense: 'imperfetto', person: '3-singular', drop: 3, add: 'ere' },
            { suffix: 'evamo', mood: 'indicativo', tense: 'imperfetto', person: '1-plural', drop: 5, add: 'ere' },
            { suffix: 'evate', mood: 'indicativo', tense: 'imperfetto', person: '2-plural', drop: 5, add: 'ere' },
            { suffix: 'evano', mood: 'indicativo', tense: 'imperfetto', person: '3-plural', drop: 5, add: 'ere' },
            { suffix: 'ivo', mood: 'indicativo', tense: 'imperfetto', person: '1-singular', drop: 3, add: 'ire' },
            { suffix: 'ivi', mood: 'indicativo', tense: 'imperfetto', person: '2-singular', drop: 3, add: 'ire' },
            { suffix: 'iva', mood: 'indicativo', tense: 'imperfetto', person: '3-singular', drop: 3, add: 'ire' },
            { suffix: 'ivamo', mood: 'indicativo', tense: 'imperfetto', person: '1-plural', drop: 5, add: 'ire' },
            { suffix: 'ivate', mood: 'indicativo', tense: 'imperfetto', person: '2-plural', drop: 5, add: 'ire' },
            { suffix: 'ivano', mood: 'indicativo', tense: 'imperfetto', person: '3-plural', drop: 5, add: 'ire' },

            // Futuro semplice
            { suffix: 'erò', mood: 'indicativo', tense: 'futuro_semplice', person: '1-singular', drop: 3, add: ['are', 'ere'] },
            { suffix: 'erai', mood: 'indicativo', tense: 'futuro_semplice', person: '2-singular', drop: 4, add: ['are', 'ere'] },
            { suffix: 'erà', mood: 'indicativo', tense: 'futuro_semplice', person: '3-singular', drop: 3, add: ['are', 'ere'] },
            { suffix: 'eremo', mood: 'indicativo', tense: 'futuro_semplice', person: '1-plural', drop: 5, add: ['are', 'ere'] },
            { suffix: 'erete', mood: 'indicativo', tense: 'futuro_semplice', person: '2-plural', drop: 5, add: ['are', 'ere'] },
            { suffix: 'eranno', mood: 'indicativo', tense: 'futuro_semplice', person: '3-plural', drop: 6, add: ['are', 'ere'] },
            { suffix: 'irò', mood: 'indicativo', tense: 'futuro_semplice', person: '1-singular', drop: 3, add: 'ire' },
            { suffix: 'irai', mood: 'indicativo', tense: 'futuro_semplice', person: '2-singular', drop: 4, add: 'ire' },
            { suffix: 'irà', mood: 'indicativo', tense: 'futuro_semplice', person: '3-singular', drop: 3, add: 'ire' },
            { suffix: 'iremo', mood: 'indicativo', tense: 'futuro_semplice', person: '1-plural', drop: 5, add: 'ire' },
            { suffix: 'irete', mood: 'indicativo', tense: 'futuro_semplice', person: '2-plural', drop: 5, add: 'ire' },
            { suffix: 'iranno', mood: 'indicativo', tense: 'futuro_semplice', person: '3-plural', drop: 6, add: 'ire' },

            // Participles & Gerunds
            { suffix: 'ato', mood: 'participle', tense: 'past', drop: 3, add: 'are' },
            { suffix: 'ata', mood: 'participle', tense: 'past', drop: 3, add: 'are' },
            { suffix: 'ati', mood: 'participle', tense: 'past', drop: 3, add: 'are' },
            { suffix: 'ate', mood: 'participle', tense: 'past', drop: 3, add: 'are' },
            { suffix: 'uto', mood: 'participle', tense: 'past', drop: 3, add: 'ere' },
            { suffix: 'uta', mood: 'participle', tense: 'past', drop: 3, add: 'ere' },
            { suffix: 'uti', mood: 'participle', tense: 'past', drop: 3, add: 'ere' },
            { suffix: 'ute', mood: 'participle', tense: 'past', drop: 3, add: 'ere' },
            { suffix: 'ito', mood: 'participle', tense: 'past', drop: 3, add: 'ire' },
            { suffix: 'ita', mood: 'participle', tense: 'past', drop: 3, add: 'ire' },
            { suffix: 'iti', mood: 'participle', tense: 'past', drop: 3, add: 'ire' },
            { suffix: 'ite', mood: 'participle', tense: 'past', drop: 3, add: 'ire' },
            { suffix: 'ando', mood: 'gerund', tense: 'present', drop: 4, add: 'are' },
            { suffix: 'endo', mood: 'gerund', tense: 'present', drop: 4, add: ['ere', 'ire'] }
        ];

        for (const e of ENDINGS) {
            if (lower.endsWith(e.suffix)) {
                const stem = lower.slice(0, -e.suffix.length);
                const candidates = Array.isArray(e.add) ? e.add : [e.add];
                for (const add of candidates) {
                    const candidate = stem + add;
                    if (dict[candidate] || (verbExtra && verbExtra[candidate])) {
                        results.push({
                            lemma: candidate,
                            mood: e.mood,
                            tense: e.tense,
                            person: e.person || null
                        });
                    }
                }
            }
        }

        return results;
    }

    function analyzeWord(word, dictionary) {
        if (!word) return [];
        const results = [];
        const dict = dictionary || {};
        const lower = word.toLowerCase();

        // 1. Plural -i -> singular -o or -e
        if (lower.endsWith('i') && lower.length > 2) {
            const stem = lower.slice(0, -1);
            if (dict[stem + 'o']) results.push({ lemma: stem + 'o', pos: 'adjective' });
            if (dict[stem + 'e']) results.push({ lemma: stem + 'e', pos: 'adjective' });
        }
        // 2. Feminine plural -e -> feminine singular -a (from masculine -o)
        if (lower.endsWith('e') && lower.length > 2) {
            const stem = lower.slice(0, -1);
            if (dict[stem + 'o']) results.push({ lemma: stem + 'o', pos: 'adjective' });
            if (dict[stem + 'e']) results.push({ lemma: stem + 'e', pos: 'adjective' });
        }
        // 3. Feminine singular -a -> masculine singular -o
        if (lower.endsWith('a') && lower.length > 2) {
            const stem = lower.slice(0, -1);
            if (dict[stem + 'o']) results.push({ lemma: stem + 'o', pos: 'adjective' });
        }

        return results;
    }

    // Contextual Italian definite article assignment:
    // il ragazzo, lo studente / lo zaino, l'amico, la ragazza, l'amica,
    // i ragazzi, gli studenti / gli amici, le ragazze / le amiche.
    function withArticle(word, gender, isPlural) {
        if (!word) return '';
        const w = word.trim().toLowerCase();
        const vowels = ['a', 'e', 'i', 'o', 'u'];
        const isVowel = vowels.includes(w[0]);
        const startsWithZ = w.startsWith('z');
        const startsWithSImpure = w.startsWith('s') && w.length > 1 && !vowels.includes(w[1]);
        const startsWithGn = w.startsWith('gn');
        const startsWithPs = w.startsWith('ps');
        const needsLoGli = startsWithZ || startsWithSImpure || startsWithGn || startsWithPs;

        if (gender === 'f') {
            if (isPlural) return `le ${word}`;
            if (isVowel) return `l'${word}`;
            return `la ${word}`;
        }

        // Masculine
        if (isPlural) {
            if (isVowel || needsLoGli) return `gli ${word}`;
            return `i ${word}`;
        } else {
            if (isVowel) return `l'${word}`;
            if (needsLoGli) return `lo ${word}`;
            return `il ${word}`;
        }
    }

    function article(lemma, entry) {
        if (!entry || entry.type !== 'noun') return null;
        const g = entry.gender || (lemma.endsWith('a') ? 'f' : 'm');
        const artWithWord = withArticle(lemma, g, false);
        if (artWithWord.startsWith("l'")) return "l'";
        const parts = artWithWord.split(' ');
        return parts[0] || null;
    }

    function acceptedArticles(lemma, entry) {
        const art = article(lemma, entry);
        if (!art) return null;
        if (art === "l'") {
            const g = (entry && entry.gender) || (lemma.endsWith('a') ? 'f' : 'm');
            return g === 'f' ? ["l'", "un'"] : ["l'", "un"];
        }
        if (art === 'la') return ['la', 'una'];
        if (art === 'lo') return ['lo', 'uno'];
        return ['il', 'un'];
    }

    return {
        contractions: CONTRACTIONS,
        elisions: ELISIONS,
        encliticStems: encliticStems,
        analyze: analyze,
        analyzeWord: analyzeWord,
        article: article,
        acceptedArticles: acceptedArticles,
        withArticle: withArticle
    };
})();

if (typeof window !== 'undefined') {
    window.ItalianMorphology = ItalianMorphology;
}
if (typeof Lexicon !== 'undefined' && typeof Lexicon.registerMorphology === 'function') {
    Lexicon.registerMorphology('it', ItalianMorphology);
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ItalianMorphology;
}
