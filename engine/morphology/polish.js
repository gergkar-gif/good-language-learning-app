// ============================================
// POLISH MORPHOLOGY — runtime inflection & conjugation fallback
// ============================================
// Mirrors HungarianMorphology, SpanishMorphology, and ItalianMorphology for Polish.
// Provides:
// 1. Prepositional contractions & vocalizations (we, ze, ode, pode, przede, nade, dlań, doń, nań, zeń).
// 2. Mobile past clitic & conditional peeling (-m, -ś, -śmy, -ście, -bym, -byś, -by, -byśmy, -byście).
// 3. Regular conjugation reconstruction (Conjugations -am/-asz, -ę/-isz, -ę/-ysz, -ę/-esz, past in -ł-).
// 4. Irregular root & core verb analysis (być, mieć, móc, chcieć, wiedzieć, znać, iść, pójść, jechać,
//    brać, dać, wziąć, mówić, powiedzieć, robić, zrobić, jeść, pić).
// 5. Verbal prefix stripping & aspect pair stems (po-, wy-, za-, przy-, od-, do-, na-, u-, prze-, roz-).
// 6. Nominal & adjectival declension stem stripping across 7 cases.
// 7. Stem alternations (ó:o, ę:ą, fleeting-e in pies/psa, palatalizations k:c/cz, g:dz/ż, ch:sz, r:rz, t:ć, ł:l).
// 8. Reflexive particle stripping (się).

const PolishMorphology = (function () {
    'use strict';

    // Prepositional vocalizations & historical pronominal enclitics (-ń)
    const CONTRACTIONS = {
        'we':    { lemma: 'w', pos: 'preposition', translation: 'in, into', analysis: 'vocalized form of w (before consonant clusters)' },
        'ze':    { lemma: 'z', pos: 'preposition', translation: 'with, from, out of', analysis: 'vocalized form of z (before consonant clusters)' },
        'ode':   { lemma: 'od', pos: 'preposition', translation: 'from', analysis: 'vocalized form of od' },
        'pode':  { lemma: 'pod', pos: 'preposition', translation: 'under', analysis: 'vocalized form of pod' },
        'przede': { lemma: 'przed', pos: 'preposition', translation: 'in front of, before', analysis: 'vocalized form of przed' },
        'nade':  { lemma: 'nad', pos: 'preposition', translation: 'above, over', analysis: 'vocalized form of nad' },
        'beze':  { lemma: 'bez', pos: 'preposition', translation: 'without', analysis: 'vocalized form of bez' },
        'przeze': { lemma: 'przez', pos: 'preposition', translation: 'through, by', analysis: 'vocalized form of przez' },

        // Pronominal enclitics (-ń = niego / go after prepositions)
        'dlań':  { lemma: 'dla', pos: 'contraction', translation: 'for him', analysis: 'dla + on (niego)' },
        'doń':   { lemma: 'do', pos: 'contraction', translation: 'to him', analysis: 'do + on (niego)' },
        'nań':   { lemma: 'na', pos: 'contraction', translation: 'on him / onto him', analysis: 'na + on (niego)' },
        'zeń':   { lemma: 'z', pos: 'contraction', translation: 'from him / out of him', analysis: 'z + on (niego)' },
        'oń':    { lemma: 'o', pos: 'contraction', translation: 'about him', analysis: 'o + on (niego)' },
        'poń':   { lemma: 'po', pos: 'contraction', translation: 'after him', analysis: 'po + on (niego)' },
        'zań':   { lemma: 'za', pos: 'contraction', translation: 'behind him / for him', analysis: 'za + on (niego)' },
        'podń':  { lemma: 'pod', pos: 'contraction', translation: 'under him', analysis: 'pod + on (niego)' },
        'weń':   { lemma: 'w', pos: 'contraction', translation: 'into him / in him', analysis: 'w + on (niego)' }
    };

    // Core irregular verbs lookup map
    const IRREGULAR_VERBS = {
        być: {
            forms: {
                jestem: 'Present, 1st person singular',
                jesteś: 'Present, 2nd person singular',
                jest: 'Present, 3rd person singular',
                jesteśmy: 'Present, 1st person plural',
                jesteście: 'Present, 2nd person plural',
                są: 'Present, 3rd person plural',
                będę: 'Future, 1st person singular',
                będziesz: 'Future, 2nd person singular',
                będzie: 'Future, 3rd person singular',
                będziemy: 'Future, 1st person plural',
                będziecie: 'Future, 2nd person plural',
                będą: 'Future, 3rd person plural',
                byłem: 'Past, 1st person singular (masculine)',
                byłam: 'Past, 1st person singular (feminine)',
                byłeś: 'Past, 2nd person singular (masculine)',
                byłaś: 'Past, 2nd person singular (feminine)',
                był: 'Past, 3rd person singular (masculine)',
                była: 'Past, 3rd person singular (feminine)',
                było: 'Past, 3rd person singular (neuter)',
                byliśmy: 'Past, 1st person plural (virile)',
                byłyśmy: 'Past, 1st person plural (non-virile)',
                byliście: 'Past, 2nd person plural (virile)',
                byłyście: 'Past, 2nd person plural (non-virile)',
                byli: 'Past, 3rd person plural (virile)',
                były: 'Past, 3rd person plural (non-virile)',
                bądź: 'Imperative singular',
                bądźmy: 'Imperative 1st person plural',
                bądźcie: 'Imperative 2nd person plural',
                byłbym: 'Conditional, 1st person singular (masculine)',
                byłabym: 'Conditional, 1st person singular (feminine)',
                byłby: 'Conditional, 3rd person singular (masculine)',
                byłaby: 'Conditional, 3rd person singular (feminine)',
                bylibyśmy: 'Conditional, 1st person plural (virile)',
                byłybyśmy: 'Conditional, 1st person plural (non-virile)'
            }
        },
        mieć: {
            forms: {
                mam: 'Present, 1st person singular',
                masz: 'Present, 2nd person singular',
                ma: 'Present, 3rd person singular',
                mamy: 'Present, 1st person plural',
                macie: 'Present, 2nd person plural',
                mają: 'Present, 3rd person plural',
                miałem: 'Past, 1st person singular (masculine)',
                miałam: 'Past, 1st person singular (feminine)',
                miałeś: 'Past, 2nd person singular (masculine)',
                miałaś: 'Past, 2nd person singular (feminine)',
                miał: 'Past, 3rd person singular (masculine)',
                miała: 'Past, 3rd person singular (feminine)',
                miało: 'Past, 3rd person singular (neuter)',
                mieliśmy: 'Past, 1st person plural (virile)',
                miałyśmy: 'Past, 1st person plural (non-virile)',
                mieliście: 'Past, 2nd person plural (virile)',
                miałyście: 'Past, 2nd person plural (non-virile)',
                mieli: 'Past, 3rd person plural (virile)',
                miały: 'Past, 3rd person plural (non-virile)',
                miej: 'Imperative singular'
            }
        },
        móc: {
            forms: {
                mogę: 'Present, 1st person singular',
                możesz: 'Present, 2nd person singular',
                może: 'Present, 3rd person singular',
                możemy: 'Present, 1st person plural',
                możecie: 'Present, 2nd person plural',
                mogą: 'Present, 3rd person plural',
                mogłem: 'Past, 1st person singular (masculine)',
                mogłam: 'Past, 1st person singular (feminine)',
                mógł: 'Past, 3rd person singular (masculine)',
                mogła: 'Past, 3rd person singular (feminine)',
                mogło: 'Past, 3rd person singular (neuter)',
                mogliśmy: 'Past, 1st person plural (virile)',
                mogłyśmy: 'Past, 1st person plural (non-virile)',
                mogli: 'Past, 3rd person plural (virile)',
                mogły: 'Past, 3rd person plural (non-virile)'
            }
        },
        chcieć: {
            forms: {
                chcę: 'Present, 1st person singular',
                chcesz: 'Present, 2nd person singular',
                chce: 'Present, 3rd person singular',
                chcemy: 'Present, 1st person plural',
                chcecie: 'Present, 2nd person plural',
                chcą: 'Present, 3rd person plural',
                chciałem: 'Past, 1st person singular (masculine)',
                chciałam: 'Past, 1st person singular (feminine)',
                chciał: 'Past, 3rd person singular (masculine)',
                chciała: 'Past, 3rd person singular (feminine)',
                chciało: 'Past, 3rd person singular (neuter)',
                chcieliśmy: 'Past, 1st person plural (virile)',
                chciałyśmy: 'Past, 1st person plural (non-virile)',
                chcieli: 'Past, 3rd person plural (virile)',
                chciały: 'Past, 3rd person plural (non-virile)'
            }
        },
        wiedzieć: {
            forms: {
                wiem: 'Present, 1st person singular',
                wiesz: 'Present, 2nd person singular',
                wie: 'Present, 3rd person singular',
                wiemy: 'Present, 1st person plural',
                wiecie: 'Present, 2nd person plural',
                wiedzą: 'Present, 3rd person plural',
                wiedziałem: 'Past, 1st person singular (masculine)',
                wiedziałam: 'Past, 1st person singular (feminine)',
                wiedział: 'Past, 3rd person singular (masculine)',
                wiedziała: 'Past, 3rd person singular (feminine)',
                wiedzieli: 'Past, 3rd person plural (virile)',
                wiedziały: 'Past, 3rd person plural (non-virile)',
                wiedz: 'Imperative singular'
            }
        },
        iść: {
            forms: {
                idę: 'Present, 1st person singular',
                idziesz: 'Present, 2nd person singular',
                idzie: 'Present, 3rd person singular',
                idziemy: 'Present, 1st person plural',
                idziecie: 'Present, 2nd person plural',
                idą: 'Present, 3rd person plural',
                szedłem: 'Past, 1st person singular (masculine)',
                szłam: 'Past, 1st person singular (feminine)',
                szedłeś: 'Past, 2nd person singular (masculine)',
                szłaś: 'Past, 2nd person singular (feminine)',
                szedł: 'Past, 3rd person singular (masculine)',
                szła: 'Past, 3rd person singular (feminine)',
                szło: 'Past, 3rd person singular (neuter)',
                szliśmy: 'Past, 1st person plural (virile)',
                szłyśmy: 'Past, 1st person plural (non-virile)',
                szliście: 'Past, 2nd person plural (virile)',
                szłyście: 'Past, 2nd person plural (non-virile)',
                szli: 'Past, 3rd person plural (virile)',
                szły: 'Past, 3rd person plural (non-virile)',
                idź: 'Imperative singular'
            }
        },
        pójść: {
            forms: {
                pójdę: 'Future/Present, 1st person singular',
                pójdziesz: 'Future/Present, 2nd person singular',
                pójdzie: 'Future/Present, 3rd person singular',
                pójdziemy: 'Future/Present, 1st person plural',
                pójdziecie: 'Future/Present, 2nd person plural',
                pójdą: 'Future/Present, 3rd person plural',
                poszedłem: 'Past, 1st person singular (masculine)',
                poszłam: 'Past, 1st person singular (feminine)',
                poszedł: 'Past, 3rd person singular (masculine)',
                poszła: 'Past, 3rd person singular (feminine)',
                poszło: 'Past, 3rd person singular (neuter)',
                poszliśmy: 'Past, 1st person plural (virile)',
                poszłyśmy: 'Past, 1st person plural (non-virile)',
                poszli: 'Past, 3rd person plural (virile)',
                poszły: 'Past, 3rd person plural (non-virile)',
                pójdź: 'Imperative singular'
            }
        },
        jechać: {
            forms: {
                jadę: 'Present, 1st person singular',
                jedziesz: 'Present, 2nd person singular',
                jedzie: 'Present, 3rd person singular',
                jedziemy: 'Present, 1st person plural',
                jedziecie: 'Present, 2nd person plural',
                jadą: 'Present, 3rd person plural',
                jechałem: 'Past, 1st person singular (masculine)',
                jechałam: 'Past, 1st person singular (feminine)',
                jechał: 'Past, 3rd person singular (masculine)',
                jechała: 'Past, 3rd person singular (feminine)',
                jechali: 'Past, 3rd person plural (virile)',
                jechały: 'Past, 3rd person plural (non-virile)',
                jedź: 'Imperative singular'
            }
        },
        jeść: {
            forms: {
                jem: 'Present, 1st person singular',
                jesz: 'Present, 2nd person singular',
                je: 'Present, 3rd person singular',
                jemy: 'Present, 1st person plural',
                jecie: 'Present, 2nd person plural',
                jedzą: 'Present, 3rd person plural',
                jadłem: 'Past, 1st person singular (masculine)',
                jadłam: 'Past, 1st person singular (feminine)',
                jadł: 'Past, 3rd person singular (masculine)',
                jadła: 'Past, 3rd person singular (feminine)',
                jedli: 'Past, 3rd person plural (virile)',
                jadły: 'Past, 3rd person plural (non-virile)',
                jedz: 'Imperative singular'
            }
        }
    };

    // Polish verbal prefixes
    const VERB_PREFIXES = [
        'przy', 'prze', 'roz', 'pod', 'nad', 'od', 'do', 'wy', 'za', 'po', 'na', 'u', 'w', 'z', 's'
    ];

    function cleanPolishWord(word) {
        if (!word) return '';
        return String(word)
            .toLowerCase()
            .trim()
            .replace(/^[«„"'\s]+|[»"'.,!?;:\s]+$/g, '');
    }

    /**
     * Peels Polish mobile clitics from a word (verbs, particles, conjunctions):
     * e.g. "czytałem" -> "czytał" (-em)
     * e.g. "poszłam" -> "poszła" (-am)
     * e.g. "zrobilibyście" -> "zrobili" (-byście)
     * e.g. "gdzieś" -> "gdzie" (-ś)
     * e.g. "coście" -> "co" (-ście)
     */
    function peelClitics(rawWord) {
        const w = cleanPolishWord(rawWord);
        const candidates = [];

        // 1. Conditional endings with person markers: -bym, -byś, -by, -byśmy, -byście
        const condMatch = w.match(/^(.*?)(byśmy|byście|bym|byś|by)$/);
        if (condMatch && condMatch[1].length >= 3) {
            candidates.push({ stem: condMatch[1], clitic: condMatch[2], type: 'conditional' });
        }

        // 2. Past tense person markers:
        // Feminine singular: -łam -> stem -ła + m, -łaś -> stem -ła + ś
        if (w.endsWith('łam') && w.length >= 4) {
            candidates.push({ stem: w.slice(0, -1), clitic: 'm', type: 'past' });
        } else if (w.endsWith('łaś') && w.length >= 4) {
            candidates.push({ stem: w.slice(0, -1), clitic: 'ś', type: 'past' });
        }

        // Masculine singular: -łem -> stem -ł + em, -łeś -> stem -ł + eś
        if (w.endsWith('łem') && w.length >= 4) {
            candidates.push({ stem: w.slice(0, -2), clitic: 'em', type: 'past' });
        } else if (w.endsWith('łeś') && w.length >= 4) {
            candidates.push({ stem: w.slice(0, -2), clitic: 'eś', type: 'past' });
        }

        // Plural: -liśmy / -łyśmy -> stem -li/-ły + śmy; -liście / -łyście -> stem -li/-ły + ście
        if ((w.endsWith('liśmy') || w.endsWith('łyśmy')) && w.length >= 6) {
            candidates.push({ stem: w.slice(0, -3), clitic: 'śmy', type: 'past' });
        } else if ((w.endsWith('liście') || w.endsWith('łyście')) && w.length >= 7) {
            candidates.push({ stem: w.slice(0, -4), clitic: 'ście', type: 'past' });
        }

        // Generic fallback past/clitic regex (stem length >= 2 for clitics like 'coście', 'bośmy')
        const pastMatch = w.match(/^(.*?)(iśmy|yśmy|iście|yście|śmy|ście|em|am|eś|aś)$/);
        if (pastMatch && pastMatch[1].length >= 2) {
            candidates.push({ stem: pastMatch[1], clitic: pastMatch[2], type: 'past' });
        }

        // 3. Emphatic / indefinite clitics: -że, -ż, -kolwiek, -ś
        if (w.endsWith('że') && w.length >= 4) {
            candidates.push({ stem: w.slice(0, -2), clitic: 'że', type: 'emphatic' });
        } else if (w.endsWith('ż') && w.length >= 3) {
            candidates.push({ stem: w.slice(0, -1), clitic: 'ż', type: 'emphatic' });
        } else if (w.endsWith('kolwiek') && w.length >= 9) {
            candidates.push({ stem: w.slice(0, -7), clitic: 'kolwiek', type: 'indefinite' });
        }

        return candidates;
    }

    /**
     * Candidate verb lemmas reconstructed from surface form
     */
    function candidateVerbLemmas(cleanWord) {
        const lemmas = new Set();
        let w = cleanWord;

        // Strip reflexive particle 'się' if glued or passed
        w = w.replace(/\s+się$/, '').replace(/^się\s+/, '');

        // 1. Direct irregular match
        for (const [irrLemma, data] of Object.entries(IRREGULAR_VERBS)) {
            if (w === irrLemma || (data.forms && data.forms[w])) {
                lemmas.add(irrLemma);
            }
        }

        // 2. Mobile clitic candidates
        const cliticMatches = peelClitics(w);
        for (const m of cliticMatches) {
            const s = m.stem;
            // e.g. "czytał" -> "czytać"
            if (s.endsWith('ł') || s.endsWith('ła') || s.endsWith('ło') || s.endsWith('li') || s.endsWith('ły')) {
                const base = s.replace(/(ł|ła|ło|li|ły)$/, '');
                lemmas.add(base + 'ć');
                lemmas.add(base + 'eć');
                lemmas.add(base + 'ać');
            }
            if (s === 'poszedł' || s === 'poszła' || s === 'poszli' || s === 'poszły') {
                lemmas.add('pójść');
            }
            if (s === 'szedł' || s === 'szła' || s === 'szli' || s === 'szły') {
                lemmas.add('iść');
            }
        }

        // 3. Past tense direct forms (e.g. czytał, poszła)
        if (w.endsWith('ł')) {
            lemmas.add(w.slice(0, -1) + 'ć');
        } else if (w.endsWith('ła') || w.endsWith('ło') || w.endsWith('ły')) {
            lemmas.add(w.slice(0, -2) + 'ć');
        } else if (w.endsWith('li')) {
            lemmas.add(w.slice(0, -2) + 'ć');
            lemmas.add(w.slice(0, -2) + 'eć');
        }

        // 4. Present tense regular patterns
        // -am, -asz, -a, -amy, -acie, -ają -> -ać (czytać, przepraszać)
        if (w.endsWith('ają')) lemmas.add(w.slice(0, -3) + 'ać');
        else if (w.endsWith('acie')) lemmas.add(w.slice(0, -4) + 'ać');
        else if (w.endsWith('amy')) lemmas.add(w.slice(0, -3) + 'ać');
        else if (w.endsWith('asz')) lemmas.add(w.slice(0, -3) + 'ać');
        else if (w.endsWith('am') && w.length >= 4) lemmas.add(w.slice(0, -2) + 'ać');

        // -uję, -ujesz, -uje, -ujemy, -ujecie, -ują -> -ować (pracować, dziękować)
        if (w.endsWith('ują')) lemmas.add(w.slice(0, -3) + 'ować');
        else if (w.endsWith('ujecie')) lemmas.add(w.slice(0, -6) + 'ować');
        else if (w.endsWith('ujemy')) lemmas.add(w.slice(0, -5) + 'ować');
        else if (w.endsWith('ujesz')) lemmas.add(w.slice(0, -5) + 'ować');
        else if (w.endsWith('uje')) lemmas.add(w.slice(0, -3) + 'ować');
        else if (w.endsWith('uję')) lemmas.add(w.slice(0, -3) + 'ować');

        // -isz, -i, -imy, -icie -> -ić (mówić, robić)
        if (w.endsWith('imy')) lemmas.add(w.slice(0, -3) + 'ić');
        else if (w.endsWith('icie')) lemmas.add(w.slice(0, -4) + 'ić');
        else if (w.endsWith('isz')) lemmas.add(w.slice(0, -3) + 'ić');
        else if (w.endsWith('ysz')) lemmas.add(w.slice(0, -3) + 'yć');

        // 5. Infinitive with prefix stripping (e.g. przeczytać -> czytać, napisać -> pisać)
        for (const cand of Array.from(lemmas)) {
            for (const pref of VERB_PREFIXES) {
                if (cand.startsWith(pref) && cand.length - pref.length >= 4) {
                    lemmas.add(cand.slice(pref.length));
                }
            }
        }

        return Array.from(lemmas);
    }

    /**
     * Stem alternations and nominal/adjectival declension analysis
     */
    function candidateNounAdjLemmas(cleanWord) {
        const lemmas = new Set();
        const w = cleanWord;

        lemmas.add(w);

        // 1. Vowel alternations
        // ó -> o (stole, stołu, stołem -> stół)
        if (w.includes('o')) {
            const oToOacute = w.replace(/o([^o]*)$/, 'ó$1');
            lemmas.add(oToOacute);
        }

        // 2. Fleeting 'e' resolution (psa, psu, psem -> pies; dnia, dniem -> dzień)
        if (w.startsWith('ps')) lemmas.add('pies');
        if (w.startsWith('dn')) lemmas.add('dzień');
        if (w.startsWith('chłopc')) lemmas.add('chłopiec');
        if (w.startsWith('ojc')) lemmas.add('ojciec');

        // 3. Consonant palatalizations before locative/dative -e or virile -i/-y
        // Polsce -> Polska, drodze -> droga, musze -> mucha, biurze -> biuro
        if (w.endsWith('ce') && w.length >= 4) {
            lemmas.add(w.slice(0, -2) + 'ka');
            lemmas.add(w.slice(0, -2) + 'ek');
        }
        if (w.endsWith('dze') && w.length >= 4) {
            lemmas.add(w.slice(0, -3) + 'ga');
            lemmas.add(w.slice(0, -3) + 'g');
        }
        if (w.endsWith('sze') && w.length >= 4) {
            lemmas.add(w.slice(0, -3) + 'cha');
            lemmas.add(w.slice(0, -3) + 'ch');
        }
        if (w.endsWith('rze') && w.length >= 4) {
            lemmas.add(w.slice(0, -3) + 'ro');
            lemmas.add(w.slice(0, -3) + 'r');
            lemmas.add(w.slice(0, -3) + 'ra');
        }
        if (w.endsWith('cie') && w.length >= 4) {
            lemmas.add(w.slice(0, -3) + 't');
            lemmas.add(w.slice(0, -3) + 'ta');
            lemmas.add(w.slice(0, -3) + 'to');
        }
        if (w.endsWith('dzie') && w.length >= 4) {
            lemmas.add(w.slice(0, -4) + 'd');
            lemmas.add(w.slice(0, -4) + 'da');
        }
        if (w.endsWith('le') && w.length >= 3) {
            lemmas.add(w.slice(0, -2) + 'ł');
            lemmas.add(w.slice(0, -2) + 'ła');
            lemmas.add(w.slice(0, -2) + 'ło');
        }

        // 4. Standard Case Endings stripping
        // Instrumental -em (m/n), -ą (f)
        if (w.endsWith('em') && w.length >= 4) {
            lemmas.add(w.slice(0, -2));
            lemmas.add(w.slice(0, -2) + 'a');
            lemmas.add(w.slice(0, -2) + 'o');
            // stół from stołem
            if (w.slice(0, -2).includes('o')) {
                lemmas.add(w.slice(0, -2).replace(/o([^o]*)$/, 'ó$1'));
            }
        }
        if (w.endsWith('ą') && w.length >= 3) {
            lemmas.add(w.slice(0, -1) + 'a'); // książką -> książka
        }

        // Genitive/Accusative -a, -u, -y, -i, -ów
        if (w.endsWith('ów') && w.length >= 4) {
            lemmas.add(w.slice(0, -2));
        }
        if (w.endsWith('a') && w.length >= 3) {
            lemmas.add(w.slice(0, -1));
            // stołu -> stół, stoła -> stół
            if (w.slice(0, -1).includes('o')) {
                lemmas.add(w.slice(0, -1).replace(/o([^o]*)$/, 'ó$1'));
            }
        }
        if (w.endsWith('u') && w.length >= 3) {
            lemmas.add(w.slice(0, -1));
            if (w.slice(0, -1).includes('o')) {
                lemmas.add(w.slice(0, -1).replace(/o([^o]*)$/, 'ó$1'));
            }
        }
        if (w.endsWith('y') && w.length >= 3) {
            lemmas.add(w.slice(0, -1) + 'a');
            lemmas.add(w.slice(0, -1));
        }
        if (w.endsWith('i') && w.length >= 3) {
            lemmas.add(w.slice(0, -1) + 'a');
            lemmas.add(w.slice(0, -1));
        }

        // Locative plural -ach
        if (w.endsWith('ach') && w.length >= 5) {
            lemmas.add(w.slice(0, -3));
            lemmas.add(w.slice(0, -3) + 'a');
            lemmas.add(w.slice(0, -3) + 'o');
        }

        // Adjective endings: -ego, -emu, -ym, -im, -ych, -ich, -ymi, -imi
        if (w.endsWith('ego') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'y');
            lemmas.add(w.slice(0, -3) + 'i');
        }
        if (w.endsWith('emu') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'y');
            lemmas.add(w.slice(0, -3) + 'i');
        }
        if (w.endsWith('ych') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'y');
        }
        if (w.endsWith('ich') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'i');
        }
        if (w.endsWith('ymi') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'y');
        }
        if (w.endsWith('imi') && w.length >= 5) {
            lemmas.add(w.slice(0, -3) + 'i');
        }

        // Comparative / Superlative: naj- prefix
        if (w.startsWith('naj') && w.length >= 6) {
            lemmas.add(w.slice(3));
        }

        // Apply vowel shifts (o -> ó) across all derived nominal stems
        // e.g. stoł -> stół, pokoj -> pokój, samochod -> samochód, ogrod -> ogród
        for (const cand of Array.from(lemmas)) {
            if (cand.includes('o')) {
                lemmas.add(cand.replace(/o([^o]*)$/, 'ó$1'));
            }
        }

        return Array.from(lemmas);
    }

    /**
     * Determines whether to use vocalized preposition form ("w" vs "we", "z" vs "ze"):
     * e.g. "we Wrocławiu", "ze mną", "ze szkoły"
     */
    function withPreposition(prep, nounWord) {
        if (!nounWord) return prep;
        const p = String(prep).toLowerCase().trim();
        const nw = String(nounWord).toLowerCase().trim();

        if (p === 'w' || p === 'we') {
            // Takes 'we' before words starting with w/f + consonant: e.g. we Wrocławiu, we Francji
            if (/^[wf][b-df-hj-np-tv-zżźćńś]/i.test(nw) || nw === 'mnie') return 'we ' + nounWord;
            return 'w ' + nounWord;
        }

        if (p === 'z' || p === 'ze') {
            // Takes 'ze' before words starting with s/z/ś/ź/ż/sz/cz + consonant: e.g. ze szkoły, ze mną
            if (/^(s|z|ś|ź|ż|sz|cz)[b-df-hj-np-tv-zżźćńś]/i.test(nw) || nw === 'mną' || nw === 'mnie') return 'ze ' + nounWord;
            return 'z ' + nounWord;
        }

        if (p === 'od' || p === 'ode') {
            if (nw === 'mnie') return 'ode mnie';
            return 'od ' + nounWord;
        }

        if (p === 'pod' || p === 'pode') {
            if (nw === 'mnie') return 'pode mną';
            return 'pod ' + nounWord;
        }

        return p + ' ' + nounWord;
    }

    function _getDictEntry(dict, key) {
        if (!dict || !key) return null;
        if (dict[key]) return { entry: dict[key], lemma: key };
        const lower = key.toLowerCase();
        if (dict[lower]) return { entry: dict[lower], lemma: lower };
        const cap = lower.charAt(0).toUpperCase() + lower.slice(1);
        if (dict[cap]) return { entry: dict[cap], lemma: cap };
        return null;
    }

    /**
     * Analyze a verb form and return matching lemmas
     */
    function analyze(cleanWord, dict) {
        const matches = [];
        const seen = new Set();
        const d = dict || {};

        // 1. Direct irregular matches
        for (const [irrLemma, data] of Object.entries(IRREGULAR_VERBS)) {
            if (data.forms && data.forms[cleanWord]) {
                if (!seen.has(irrLemma)) {
                    seen.add(irrLemma);
                    matches.push({
                        lemma: irrLemma,
                        pos: 'verb',
                        analysis: data.forms[cleanWord],
                        confidence: 0.98
                    });
                }
            }
        }

        // 2. Candidate verb derivation
        const candidates = candidateVerbLemmas(cleanWord);
        for (const cand of candidates) {
            if (seen.has(cand.toLowerCase())) continue;
            const res = _getDictEntry(d, cand);
            if (res && (res.entry.type === 'verb' || !res.entry.type)) {
                seen.add(cand.toLowerCase());
                matches.push({
                    lemma: res.lemma,
                    pos: 'verb',
                    analysis: 'inflected verb form',
                    confidence: 0.85
                });
            }
        }

        return matches;
    }

    /**
     * Analyze a noun or adjective form and return matching lemmas
     */
    function analyzeWord(cleanWord, dict) {
        const matches = [];
        const seen = new Set();
        const d = dict || {};

        const candidates = candidateNounAdjLemmas(cleanWord);
        for (const cand of candidates) {
            if (seen.has(cand.toLowerCase())) continue;
            const res = _getDictEntry(d, cand);
            if (cand === cleanWord && !res) continue;

            if (res) {
                seen.add(cand.toLowerCase());
                matches.push({
                    lemma: res.lemma,
                    pos: res.entry.type || 'noun',
                    gender: res.entry.gender || null,
                    analysis: 'inflected form',
                    confidence: 0.8
                });
            }
        }

        return matches;
    }

    /**
     * Main Reader / Lexicon runtime lookup entry point
     */
    function lookup(word, dict, wordIndex, verbIndex) {
        const cleanKey = cleanPolishWord(word);
        if (!cleanKey) return { word: word, readings: [] };

        const readings = [];
        const seenReadings = new Set();
        const d = dict || {};
        const wi = wordIndex || {};
        const vi = verbIndex || {};

        function addReading(lemma, pos, analysis, translation) {
            const tr = translation || (d[lemma] && d[lemma].en) || '';
            const key = lemma + '|' + (pos || '') + '|' + (analysis || '');
            if (!seenReadings.has(key)) {
                seenReadings.add(key);
                readings.push({
                    lemma: lemma,
                    pos: pos || 'unknown',
                    analysis: analysis || '',
                    translation: tr
                });
            }
        }

        // 1. Contractions and vocalized forms
        if (CONTRACTIONS[cleanKey]) {
            const c = CONTRACTIONS[cleanKey];
            addReading(c.lemma, c.pos, c.analysis, c.translation);
        }

        // 2. Exact match in dictionary
        if (d[cleanKey]) {
            addReading(cleanKey, d[cleanKey].type, '', d[cleanKey].en);
        }

        // 3. Precomputed word-index match
        if (wi[cleanKey]) {
            const entries = Array.isArray(wi[cleanKey]) ? wi[cleanKey] : [wi[cleanKey]];
            entries.forEach(e => {
                const ana = [e.case, e.number, e.gender].filter(Boolean).join(' ');
                addReading(e.lemma, e.pos, ana);
            });
        }

        // 4. Precomputed verb-index match
        if (vi[cleanKey]) {
            const entries = Array.isArray(vi[cleanKey]) ? vi[cleanKey] : [vi[cleanKey]];
            entries.forEach(e => {
                const ana = [e.tense, e.person, e.number, e.gender].filter(Boolean).join(' ');
                addReading(e.lemma, 'verb', ana);
            });
        }

        // 5. Runtime irregular verb match
        for (const [irrLemma, data] of Object.entries(IRREGULAR_VERBS)) {
            if (data.forms && data.forms[cleanKey]) {
                addReading(irrLemma, 'verb', data.forms[cleanKey]);
            }
        }

        // 6. Runtime verb morphology fallback
        if (!readings.length) {
            const vMatches = analyze(cleanKey, d);
            vMatches.forEach(v => addReading(v.lemma, v.pos, v.analysis));
        }

        // 7. Runtime noun/adjective morphology fallback
        if (!readings.length) {
            const nMatches = analyzeWord(cleanKey, d);
            nMatches.forEach(n => addReading(n.lemma, n.pos, n.analysis));
        }

        // Sort by quality: definitions first
        readings.sort((a, b) => Boolean(b.translation) - Boolean(a.translation));

        return { word: word, readings: readings };
    }

    return {
        contractions: CONTRACTIONS,
        irregularVerbs: IRREGULAR_VERBS,
        cleanPolishWord: cleanPolishWord,
        peelClitics: peelClitics,
        candidateVerbLemmas: candidateVerbLemmas,
        candidateNounAdjLemmas: candidateNounAdjLemmas,
        withPreposition: withPreposition,
        analyze: analyze,
        analyzeWord: analyzeWord,
        lookup: lookup
    };
})();

if (typeof window !== 'undefined') {
    window.PolishMorphology = PolishMorphology;
}
try {
    if (typeof globalThis !== 'undefined' && globalThis.Lexicon && typeof globalThis.Lexicon.registerMorphology === 'function') {
        globalThis.Lexicon.registerMorphology('pl', PolishMorphology);
    } else if (typeof Lexicon !== 'undefined' && typeof Lexicon.registerMorphology === 'function') {
        Lexicon.registerMorphology('pl', PolishMorphology);
    }
} catch (e) {}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = PolishMorphology;
}
