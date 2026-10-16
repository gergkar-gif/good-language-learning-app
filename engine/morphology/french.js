// ============================================
// FRENCH MORPHOLOGY — runtime inflection & conjugation fallback
// ============================================
// Mirrors SpanishMorphology and HungarianMorphology for French.
// Provides:
// 1. Contraction decomposition (du, des, au, aux).
// 2. Elision resolution (c', l', d', j', qu', n', s', m', t') and compound terms (aujourd'hui).
// 3. Regular conjugation reconstruction (1st group -er, 2nd group -ir, stem alterations).
// 4. Irregular root & compound verb analysis (être, avoir, aller, faire, pouvoir, vouloir,
//    devoir, savoir, venir, prendre, voir, mettre, dire, falloir).
// 5. Gender and number reconstruction for adjectives and nouns (-e, -ère, -euse, -trice, -s, -aux).

const FrenchMorphology = (function () {
    'use strict';

    const CONTRACTIONS = {
        'du':  { lemma: 'de', pos: 'contraction', translation: 'of the, from the, some', analysis: 'contraction of de + le (masculine singular)' },
        'des': { lemma: 'de', pos: 'contraction', translation: 'of the, from the, some (plural)', analysis: 'contraction of de + les (plural)' },
        'au':  { lemma: 'à',  pos: 'contraction', translation: 'to the, at the', analysis: 'contraction of à + le (masculine singular)' },
        'aux': { lemma: 'à',  pos: 'contraction', translation: 'to the, at the (plural)', analysis: 'contraction of à + les (plural)' }
    };

    const ELISIONS = {
        "c'": { lemma: 'ce', pos: 'pronoun', translation: 'this, that, it', analysis: 'demonstrative pronoun (elided)' },
        'c':  { lemma: 'ce', pos: 'pronoun', translation: 'this, that, it', analysis: 'demonstrative pronoun (elided)' },
        "j'": { lemma: 'je', pos: 'pronoun', translation: 'I', analysis: '1st person subject pronoun (elided)' },
        'j':  { lemma: 'je', pos: 'pronoun', translation: 'I', analysis: '1st person subject pronoun (elided)' },
        "l'": { lemma: 'le', pos: 'article', translation: 'the', analysis: 'definite article (elided)' },
        'l':  { lemma: 'le', pos: 'article', translation: 'the', analysis: 'definite article (elided)' },
        "d'": { lemma: 'de', pos: 'preposition', translation: 'of, from', analysis: 'preposition (elided)' },
        'd':  { lemma: 'de', pos: 'preposition', translation: 'of, from', analysis: 'preposition (elided)' },
        "qu'": { lemma: 'que', pos: 'conjunction', translation: 'that, which, what', analysis: 'relative pronoun / conjunction (elided)' },
        'qu':  { lemma: 'que', pos: 'conjunction', translation: 'that, which, what', analysis: 'relative pronoun / conjunction (elided)' },
        "n'": { lemma: 'ne', pos: 'adverb', translation: 'not', analysis: 'negative particle (elided)' },
        'n':  { lemma: 'ne', pos: 'adverb', translation: 'not', analysis: 'negative particle (elided)' },
        "s'": { lemma: 'se', pos: 'pronoun', translation: 'oneself, himself, herself', analysis: '3rd person reflexive pronoun (elided)' },
        's':  { lemma: 'se', pos: 'pronoun', translation: 'oneself, himself, herself', analysis: '3rd person reflexive pronoun (elided)' },
        "m'": { lemma: 'me', pos: 'pronoun', translation: 'me, to me, myself', analysis: '1st person object pronoun (elided)' },
        'm':  { lemma: 'me', pos: 'pronoun', translation: 'me, to me, myself', analysis: '1st person object pronoun (elided)' },
        "t'": { lemma: 'te', pos: 'pronoun', translation: 'you, to you, yourself', analysis: '2nd person object pronoun (elided)' },
        't':  { lemma: 'te', pos: 'pronoun', translation: 'you, to you, yourself', analysis: '2nd person object pronoun (elided)' },
        "jusqu'": { lemma: 'jusque', pos: 'preposition', translation: 'until, up to, as far as', analysis: 'preposition (elided)' },
        'jusqu':  { lemma: 'jusque', pos: 'preposition', translation: 'until, up to, as far as', analysis: 'preposition (elided)' },
        "lorsqu'": { lemma: 'lorsque', pos: 'conjunction', translation: 'when', analysis: 'conjunction (elided)' },
        'lorsqu':  { lemma: 'lorsque', pos: 'conjunction', translation: 'when', analysis: 'conjunction (elided)' },
        "puisqu'": { lemma: 'puisque', pos: 'conjunction', translation: 'since, because', analysis: 'conjunction (elided)' },
        'puisqu':  { lemma: 'puisque', pos: 'conjunction', translation: 'since, because', analysis: 'conjunction (elided)' },
        "quoiqu'": { lemma: 'quoique', pos: 'conjunction', translation: 'although, even though', analysis: 'conjunction (elided)' },
        'quoiqu':  { lemma: 'quoique', pos: 'conjunction', translation: 'although, even though', analysis: 'conjunction (elided)' }
    };

    const IRREGULAR_VERBS = {
        être: {
            forms: {
                suis: 'Present, 1st person singular',
                es: 'Present, 2nd person singular',
                est: 'Present, 3rd person singular',
                sommes: 'Present, 1st person plural',
                êtes: 'Present, 2nd person plural',
                sont: 'Present, 3rd person plural',
                été: 'Past participle',
                étais: 'Imperfect, 1st/2nd person singular',
                était: 'Imperfect, 3rd person singular',
                étions: 'Imperfect, 1st person plural',
                étiez: 'Imperfect, 2nd person plural',
                étaient: 'Imperfect, 3rd person plural',
                serai: 'Future, 1st person singular',
                seras: 'Future, 2nd person singular',
                sera: 'Future, 3rd person singular',
                serons: 'Future, 1st person plural',
                serez: 'Future, 2nd person plural',
                seront: 'Future, 3rd person plural',
                serais: 'Conditional, 1st/2nd person singular',
                serait: 'Conditional, 3rd person singular',
                serions: 'Conditional, 1st person plural',
                seriez: 'Conditional, 2nd person plural',
                seraient: 'Conditional, 3rd person plural',
                sois: 'Subjunctive/Imperative, singular',
                soit: 'Subjunctive, 3rd person singular',
                soyons: 'Subjunctive/Imperative, 1st person plural',
                soyez: 'Subjunctive/Imperative, 2nd person plural',
                soient: 'Subjunctive, 3rd person plural'
            }
        },
        avoir: {
            forms: {
                ai: 'Present, 1st person singular',
                as: 'Present, 2nd person singular',
                a: 'Present, 3rd person singular',
                avons: 'Present, 1st person plural',
                avez: 'Present, 2nd person plural',
                ont: 'Present, 3rd person plural',
                eu: 'Past participle',
                eue: 'Past participle, feminine singular',
                eus: 'Past participle, masculine plural',
                eues: 'Past participle, feminine plural',
                avais: 'Imperfect, 1st/2nd person singular',
                avait: 'Imperfect, 3rd person singular',
                avions: 'Imperfect, 1st person plural',
                aviez: 'Imperfect, 2nd person plural',
                avaient: 'Imperfect, 3rd person plural',
                aurai: 'Future, 1st person singular',
                auras: 'Future, 2nd person singular',
                aura: 'Future, 3rd person singular',
                aurons: 'Future, 1st person plural',
                aurez: 'Future, 2nd person plural',
                auront: 'Future, 3rd person plural',
                aurais: 'Conditional, 1st/2nd person singular',
                aurait: 'Conditional, 3rd person singular',
                aurions: 'Conditional, 1st person plural',
                auriez: 'Conditional, 2nd person plural',
                auraient: 'Conditional, 3rd person plural',
                aie: 'Subjunctive, 1st person singular',
                aies: 'Subjunctive, 2nd person singular',
                ait: 'Subjunctive, 3rd person singular',
                ayons: 'Subjunctive, 1st person plural',
                ayez: 'Subjunctive, 2nd person plural',
                aient: 'Subjunctive, 3rd person plural'
            }
        },
        aller: {
            forms: {
                vais: 'Present, 1st person singular',
                vas: 'Present, 2nd person singular',
                va: 'Present, 3rd person singular',
                allons: 'Present, 1st person plural',
                allez: 'Present, 2nd person plural',
                vont: 'Present, 3rd person plural',
                allé: 'Past participle',
                allée: 'Past participle, feminine singular',
                allés: 'Past participle, masculine plural',
                allées: 'Past participle, feminine plural',
                allais: 'Imperfect, 1st/2nd person singular',
                allait: 'Imperfect, 3rd person singular',
                irai: 'Future, 1st person singular',
                iras: 'Future, 2nd person singular',
                ira: 'Future, 3rd person singular',
                irons: 'Future, 1st person plural',
                irez: 'Future, 2nd person plural',
                iront: 'Future, 3rd person plural',
                irais: 'Conditional, 1st/2nd person singular',
                irait: 'Conditional, 3rd person singular',
                aille: 'Subjunctive, 1st/3rd person singular',
                ailles: 'Subjunctive, 2nd person singular',
                aillent: 'Subjunctive, 3rd person plural'
            }
        },
        faire: {
            forms: {
                fais: 'Present, 1st/2nd person singular',
                fait: 'Present, 3rd person singular / Past participle',
                faite: 'Past participle, feminine singular',
                faits: 'Past participle, masculine plural',
                faites: 'Present, 2nd person plural / Past participle, feminine plural',
                faisons: 'Present, 1st person plural',
                font: 'Present, 3rd person plural',
                faisais: 'Imperfect, 1st/2nd person singular',
                faisait: 'Imperfect, 3rd person singular',
                faisions: 'Imperfect, 1st person plural',
                faisiez: 'Imperfect, 2nd person plural',
                faisaient: 'Imperfect, 3rd person plural',
                ferai: 'Future, 1st person singular',
                feras: 'Future, 2nd person singular',
                fera: 'Future, 3rd person singular',
                ferons: 'Future, 1st person plural',
                ferez: 'Future, 2nd person plural',
                feront: 'Future, 3rd person plural',
                ferais: 'Conditional, 1st/2nd person singular',
                ferait: 'Conditional, 3rd person singular',
                fasse: 'Subjunctive, 1st/3rd person singular',
                fassent: 'Subjunctive, 3rd person plural'
            }
        },
        pouvoir: {
            forms: {
                peux: 'Present, 1st/2nd person singular',
                puis: 'Present, 1st person singular (formal)',
                peut: 'Present, 3rd person singular',
                pouvons: 'Present, 1st person plural',
                pouvez: 'Present, 2nd person plural',
                peuvent: 'Present, 3rd person plural',
                pu: 'Past participle',
                pouvais: 'Imperfect, 1st/2nd person singular',
                pouvait: 'Imperfect, 3rd person singular',
                pourrai: 'Future, 1st person singular',
                pourras: 'Future, 2nd person singular',
                pourra: 'Future, 3rd person singular',
                pourrons: 'Future, 1st person plural',
                pourrez: 'Future, 2nd person plural',
                pourront: 'Future, 3rd person plural',
                pourrais: 'Conditional, 1st/2nd person singular',
                pourrait: 'Conditional, 3rd person singular',
                puisse: 'Subjunctive, 1st/3rd person singular',
                puissent: 'Subjunctive, 3rd person plural'
            }
        },
        vouloir: {
            forms: {
                veux: 'Present, 1st/2nd person singular',
                veut: 'Present, 3rd person singular',
                voulons: 'Present, 1st person plural',
                voulez: 'Present, 2nd person plural',
                veulent: 'Present, 3rd person plural',
                voulu: 'Past participle',
                voulais: 'Imperfect, 1st/2nd person singular',
                voulait: 'Imperfect, 3rd person singular',
                voudrai: 'Future, 1st person singular',
                voudras: 'Future, 2nd person singular',
                voudra: 'Future, 3rd person singular',
                voudrons: 'Future, 1st person plural',
                voudrez: 'Future, 2nd person plural',
                voudront: 'Future, 3rd person plural',
                voudrais: 'Conditional, 1st/2nd person singular',
                voudrait: 'Conditional, 3rd person singular',
                veuille: 'Subjunctive, 1st/3rd person singular',
                veuillent: 'Subjunctive, 3rd person plural'
            }
        },
        devoir: {
            forms: {
                dois: 'Present, 1st/2nd person singular',
                doit: 'Present, 3rd person singular',
                devons: 'Present, 1st person plural',
                devez: 'Present, 2nd person plural',
                doivent: 'Present, 3rd person plural',
                dû: 'Past participle',
                due: 'Past participle, feminine singular',
                dus: 'Past participle, masculine plural',
                dues: 'Past participle, feminine plural',
                devais: 'Imperfect, 1st/2nd person singular',
                devait: 'Imperfect, 3rd person singular',
                devrai: 'Future, 1st person singular',
                devras: 'Future, 2nd person singular',
                devra: 'Future, 3rd person singular',
                devrons: 'Future, 1st person plural',
                devrez: 'Future, 2nd person plural',
                devront: 'Future, 3rd person plural',
                devrais: 'Conditional, 1st/2nd person singular',
                devrait: 'Conditional, 3rd person singular',
                doive: 'Subjunctive, 1st/3rd person singular',
                doivent_sub: 'Subjunctive, 3rd person plural'
            }
        },
        savoir: {
            forms: {
                sais: 'Present, 1st/2nd person singular',
                sait: 'Present, 3rd person singular',
                savons: 'Present, 1st person plural',
                savez: 'Present, 2nd person plural',
                savent: 'Present, 3rd person plural',
                su: 'Past participle',
                savais: 'Imperfect, 1st/2nd person singular',
                savait: 'Imperfect, 3rd person singular',
                saurai: 'Future, 1st person singular',
                sauras: 'Future, 2nd person singular',
                saura: 'Future, 3rd person singular',
                saurons: 'Future, 1st person plural',
                saurez: 'Future, 2nd person plural',
                sauront: 'Future, 3rd person plural',
                saurais: 'Conditional, 1st/2nd person singular',
                saurait: 'Conditional, 3rd person singular',
                sache: 'Subjunctive/Imperative, singular'
            }
        },
        venir: {
            forms: {
                viens: 'Present, 1st/2nd person singular',
                vient: 'Present, 3rd person singular',
                venons: 'Present, 1st person plural',
                venez: 'Present, 2nd person plural',
                viennent: 'Present, 3rd person plural',
                venu: 'Past participle',
                venue: 'Past participle, feminine singular',
                venus: 'Past participle, masculine plural',
                venues: 'Past participle, feminine plural',
                venais: 'Imperfect, 1st/2nd person singular',
                venait: 'Imperfect, 3rd person singular',
                viendrai: 'Future, 1st person singular',
                viendras: 'Future, 2nd person singular',
                viendra: 'Future, 3rd person singular',
                viendrons: 'Future, 1st person plural',
                viendrez: 'Future, 2nd person plural',
                viendront: 'Future, 3rd person plural',
                viendrais: 'Conditional, 1st/2nd person singular',
                viendrait: 'Conditional, 3rd person singular',
                vienne: 'Subjunctive, 1st/3rd person singular'
            }
        },
        prendre: {
            forms: {
                prends: 'Present, 1st/2nd person singular',
                prend: 'Present, 3rd person singular',
                prenons: 'Present, 1st person plural',
                prenez: 'Present, 2nd person plural',
                prennent: 'Present, 3rd person plural',
                pris: 'Past participle / Past Historic',
                prise: 'Past participle, feminine singular',
                prises: 'Past participle, feminine plural',
                prenais: 'Imperfect, 1st/2nd person singular',
                prenait: 'Imperfect, 3rd person singular',
                prendrai: 'Future, 1st person singular',
                prendras: 'Future, 2nd person singular',
                prendra: 'Future, 3rd person singular',
                prendrons: 'Future, 1st person plural',
                prendrez: 'Future, 2nd person plural',
                prendront: 'Future, 3rd person plural',
                prendrais: 'Conditional, 1st/2nd person singular',
                prendrait: 'Conditional, 3rd person singular',
                prenne: 'Subjunctive, 1st/3rd person singular'
            }
        },
        voir: {
            forms: {
                vois: 'Present, 1st/2nd person singular',
                voit: 'Present, 3rd person singular',
                voyons: 'Present, 1st person plural',
                voyez: 'Present, 2nd person plural',
                voient: 'Present, 3rd person plural',
                vu: 'Past participle',
                vue: 'Past participle, feminine singular',
                vus: 'Past participle, masculine plural',
                vues: 'Past participle, feminine plural',
                voyais: 'Imperfect, 1st/2nd person singular',
                voyait: 'Imperfect, 3rd person singular',
                verrai: 'Future, 1st person singular',
                verras: 'Future, 2nd person singular',
                verra: 'Future, 3rd person singular',
                verrons: 'Future, 1st person plural',
                verrez: 'Future, 2nd person plural',
                verront: 'Future, 3rd person plural',
                verrais: 'Conditional, 1st/2nd person singular',
                verrait: 'Conditional, 3rd person singular'
            }
        },
        mettre: {
            forms: {
                mets: 'Present, 1st/2nd person singular',
                met: 'Present, 3rd person singular',
                mettons: 'Present, 1st person plural',
                mettez: 'Present, 2nd person plural',
                mettent: 'Present, 3rd person plural',
                mis: 'Past participle',
                mise: 'Past participle, feminine singular',
                mises: 'Past participle, feminine plural',
                mettais: 'Imperfect, 1st/2nd person singular',
                mettait: 'Imperfect, 3rd person singular',
                mettrai: 'Future, 1st person singular',
                mettrais: 'Conditional, 1st/2nd person singular',
                mette: 'Subjunctive, 1st/3rd person singular'
            }
        },
        dire: {
            forms: {
                dis: 'Present, 1st/2nd person singular',
                dit: 'Present, 3rd person singular / Past participle',
                dite: 'Past participle, feminine singular',
                dits: 'Past participle, masculine plural',
                dites: 'Present, 2nd person plural / Past participle, feminine plural',
                disons: 'Present, 1st person plural',
                disent: 'Present, 3rd person plural',
                disais: 'Imperfect, 1st/2nd person singular',
                disait: 'Imperfect, 3rd person singular',
                dirai: 'Future, 1st person singular',
                dirais: 'Conditional, 1st/2nd person singular'
            }
        },
        falloir: {
            forms: {
                faut: 'Present, 3rd person singular',
                fallu: 'Past participle',
                fallait: 'Imperfect, 3rd person singular',
                faudra: 'Future, 3rd person singular',
                faudrait: 'Conditional, 3rd person singular',
                faille: 'Subjunctive, 3rd person singular'
            }
        }
    };

    // Compound prefixes that inherit an irregular root
    const COMPOUND_PREFIXES = [
        're', 'dé', 'de', 'ap', 'com', 'sur', 'per', 'pro', 'in', 'trans', 'ad', 'sou'
    ];

    function cleanFrenchWord(word) {
        if (!word) return '';
        let w = String(word).trim().toLowerCase();
        // preserve internal apostrophe for aujourd'hui
        if (w === "aujourd'hui" || w === "aujourd’hui") return "aujourd'hui";
        return w.replace(/[.,!?¡¿;:"()«»]/g, '').trim();
    }

    /**
     * Reconstruct regular 1st and 2nd group French verbs from inflected surface form.
     */
    function candidateVerbLemmas(form) {
        const cands = [];
        const seen = new Set();

        function addCand(stem, ending, analysis) {
            const lemma = stem + ending;
            const key = lemma + '|' + analysis;
            if (!seen.has(key)) {
                seen.add(key);
                cands.push({ lemma, analysis });
            }
        }

        // 1. Regular 1st Group (-er)
        if (form.endsWith('ons')) {
            let stem = form.slice(0, -3);
            if (stem.endsWith('ge')) stem = stem.slice(0, -1); // mangeons -> manger
            if (stem.endsWith('ç')) stem = stem.slice(0, -1) + 'c'; // commençons -> commencer
            addCand(stem, 'er', 'Present, 1st person plural');
        } else if (form.endsWith('ez')) {
            addCand(form.slice(0, -2), 'er', 'Present / Imperative, 2nd person plural');
        } else if (form.endsWith('ent')) {
            addCand(form.slice(0, -3), 'er', 'Present / Subjunctive, 3rd person plural');
        } else if (form.endsWith('es')) {
            addCand(form.slice(0, -2), 'er', 'Present / Subjunctive, 2nd person singular');
        } else if (form.endsWith('e')) {
            addCand(form.slice(0, -1), 'er', 'Present / Subjunctive, 1st/3rd person singular');
        }

        // Past participle (-é, -ée, -és, -ées)
        if (form.endsWith('ees') || form.endsWith('ées')) {
            addCand(form.slice(0, -3), 'er', 'Past participle, feminine plural');
        } else if (form.endsWith('ee') || form.endsWith('ée')) {
            addCand(form.slice(0, -2), 'er', 'Past participle, feminine singular');
        } else if (form.endsWith('es') || form.endsWith('és')) {
            addCand(form.slice(0, -2), 'er', 'Past participle, masculine plural');
        } else if (form.endsWith('e') || form.endsWith('é')) {
            addCand(form.slice(0, -1), 'er', 'Past participle, masculine singular');
        }

        // Imperfect (-ais, -ait, -ions, -iez, -aient)
        if (form.endsWith('aient')) {
            let stem = form.slice(0, -5);
            if (stem.endsWith('ge')) stem = stem.slice(0, -1);
            if (stem.endsWith('ç')) stem = stem.slice(0, -1) + 'c';
            addCand(stem, 'er', 'Imperfect, 3rd person plural');
        } else if (form.endsWith('ions')) {
            addCand(form.slice(0, -4), 'er', 'Imperfect, 1st person plural');
        } else if (form.endsWith('iez')) {
            addCand(form.slice(0, -3), 'er', 'Imperfect, 2nd person plural');
        } else if (form.endsWith('ait')) {
            let stem = form.slice(0, -3);
            if (stem.endsWith('ge')) stem = stem.slice(0, -1);
            if (stem.endsWith('ç')) stem = stem.slice(0, -1) + 'c';
            addCand(stem, 'er', 'Imperfect, 3rd person singular');
        } else if (form.endsWith('ais')) {
            let stem = form.slice(0, -3);
            if (stem.endsWith('ge')) stem = stem.slice(0, -1);
            if (stem.endsWith('ç')) stem = stem.slice(0, -1) + 'c';
            addCand(stem, 'er', 'Imperfect, 1st/2nd person singular');
        }

        // Future (-erai, -eras, -era, -erons, -erez, -eront)
        if (form.endsWith('eront')) addCand(form.slice(0, -5), 'er', 'Future, 3rd person plural');
        else if (form.endsWith('erez')) addCand(form.slice(0, -4), 'er', 'Future, 2nd person plural');
        else if (form.endsWith('erons')) addCand(form.slice(0, -5), 'er', 'Future, 1st person plural');
        else if (form.endsWith('eras')) addCand(form.slice(0, -4), 'er', 'Future, 2nd person singular');
        else if (form.endsWith('erai')) addCand(form.slice(0, -4), 'er', 'Future, 1st person singular');
        else if (form.endsWith('era')) addCand(form.slice(0, -3), 'er', 'Future, 3rd person singular');

        // Conditional (-erais, -erait, -erions, -eriez, -eraient)
        if (form.endsWith('eraient')) addCand(form.slice(0, -7), 'er', 'Conditional, 3rd person plural');
        else if (form.endsWith('eriez')) addCand(form.slice(0, -5), 'er', 'Conditional, 2nd person plural');
        else if (form.endsWith('erions')) addCand(form.slice(0, -6), 'er', 'Conditional, 1st person plural');
        else if (form.endsWith('erait')) addCand(form.slice(0, -5), 'er', 'Conditional, 3rd person singular');
        else if (form.endsWith('erais')) addCand(form.slice(0, -5), 'er', 'Conditional, 1st/2nd person singular');

        // 2. Regular 2nd Group (-ir)
        if (form.endsWith('issons')) addCand(form.slice(0, -6), 'ir', 'Present, 1st person plural');
        else if (form.endsWith('issez')) addCand(form.slice(0, -5), 'ir', 'Present, 2nd person plural');
        else if (form.endsWith('issent')) addCand(form.slice(0, -6), 'ir', 'Present, 3rd person plural');
        else if (form.endsWith('issant')) addCand(form.slice(0, -6), 'ir', 'Present participle');
        else if (form.endsWith('is')) addCand(form.slice(0, -2), 'ir', 'Present, 1st/2nd person singular / Past participle');
        else if (form.endsWith('it')) addCand(form.slice(0, -2), 'ir', 'Present, 3rd person singular');

        return cands;
    }

    /**
     * Fallback verb analyzer for Lexicon integration.
     */
    function analyze(word, dictionary) {
        const form = cleanFrenchWord(word);
        if (!form) return [];
        const results = [];
        const seen = new Set();
        const dict = dictionary || {};

        function addResult(lemma, analysis) {
            if (seen.has(lemma)) return;
            seen.add(lemma);
            results.push({ lemma, pos: 'verb', analysis });
        }

        // Check irregular root tables
        for (const [irrLemma, meta] of Object.entries(IRREGULAR_VERBS)) {
            if (meta.forms[form]) {
                addResult(irrLemma, meta.forms[form]);
            }
            // Compound verbs built on irregular root (e.g. apprendre -> prendre, devenir -> venir)
            for (const pref of COMPOUND_PREFIXES) {
                if (form.startsWith(pref) && meta.forms[form.slice(pref.length)]) {
                    const compoundLemma = pref + irrLemma;
                    if (dict[compoundLemma]) {
                        addResult(compoundLemma, meta.forms[form.slice(pref.length)]);
                    }
                }
            }
        }

        // Regular conjugation candidate stripping validated by dictionary outcome
        const cands = candidateVerbLemmas(form);
        const hasDict = dictionary && Object.keys(dictionary).length > 0;
        for (const cand of cands) {
            if (!hasDict) {
                addResult(cand.lemma, cand.analysis);
            } else if (dict[cand.lemma]) {
                const entry = dict[cand.lemma];
                if (!entry.type || entry.type === 'v' || entry.type === 'verb') {
                    addResult(cand.lemma, cand.analysis);
                }
            }
        }

        return results;
    }

    /**
     * Reconstruct candidate adjective / noun lemmas (gender and plural stripping).
     */
    function analyzeWord(word, dictionary) {
        const form = cleanFrenchWord(word);
        if (!form) return [];
        const results = [];
        const seen = new Set();
        const dict = dictionary || {};

        function tryLemma(lemma, pos, analysis) {
            if (lemma === form || seen.has(lemma)) return;
            const entry = dict[lemma];
            if (!entry) return;
            seen.add(lemma);
            results.push({
                lemma,
                pos: entry.type || pos || 'unknown',
                analysis
            });
        }

        // Plural -aux -> -al (animaux -> animal, journaux -> journal)
        if (form.endsWith('aux')) {
            tryLemma(form.slice(0, -3) + 'al', 'noun', 'masculine plural');
        }

        // Feminine plural -euses -> -eur / -eux
        if (form.endsWith('euses')) {
            tryLemma(form.slice(0, -5) + 'eux', 'adjective', 'feminine plural');
            tryLemma(form.slice(0, -5) + 'eur', 'adjective', 'feminine plural');
        } else if (form.endsWith('euse')) {
            tryLemma(form.slice(0, -4) + 'eux', 'adjective', 'feminine singular');
            tryLemma(form.slice(0, -4) + 'eur', 'adjective', 'feminine singular');
        }

        // Feminine -trices -> -teur
        if (form.endsWith('trices')) {
            tryLemma(form.slice(0, -6) + 'teur', 'noun', 'feminine plural');
        } else if (form.endsWith('trice')) {
            tryLemma(form.slice(0, -5) + 'teur', 'noun', 'feminine singular');
        }

        // Feminine -ières -> -ier
        if (form.endsWith('ieres') || form.endsWith('ières')) {
            tryLemma(form.slice(0, -5) + 'ier', 'adjective', 'feminine plural');
        } else if (form.endsWith('iere') || form.endsWith('ière')) {
            tryLemma(form.slice(0, -4) + 'ier', 'adjective', 'feminine singular');
        }

        // Feminine plural -es -> masculine base
        if (form.endsWith('es') && form.length > 3) {
            tryLemma(form.slice(0, -2), 'adjective', 'feminine plural');
            if (form.endsWith('lles')) tryLemma(form.slice(0, -4) + 'l', 'adjective', 'feminine plural');
            if (form.endsWith('nnes')) tryLemma(form.slice(0, -4) + 'n', 'adjective', 'feminine plural');
            if (form.endsWith('ttes')) tryLemma(form.slice(0, -4) + 't', 'adjective', 'feminine plural');
        }

        // Feminine singular -e -> masculine base
        if (form.endsWith('e') && form.length > 2) {
            tryLemma(form.slice(0, -1), 'adjective', 'feminine singular');
            // Double consonants: naturelle -> naturel, bonne -> bon, gentille -> gentil
            if (form.endsWith('lle')) tryLemma(form.slice(0, -3) + 'l', 'adjective', 'feminine singular');
            if (form.endsWith('nne')) tryLemma(form.slice(0, -3) + 'n', 'adjective', 'feminine singular');
            if (form.endsWith('tte')) tryLemma(form.slice(0, -3) + 't', 'adjective', 'feminine singular');
        }

        // Simple plural -s or -x -> singular base
        if (form.endsWith('s') && form.length > 2) {
            tryLemma(form.slice(0, -1), 'noun', 'plural');
        } else if (form.endsWith('x') && form.length > 2) {
            tryLemma(form.slice(0, -1), 'noun', 'plural');
        }

        return results;
    }

    /**
     * Primary French word lookup entry point for Lexicon.
     */
    function lookup(rawWord, ctx) {
        const word = String(rawWord || '').trim();
        if (!word) return { word: '', readings: [] };

        // 1. Direct elisions
        const cleanElision = word.toLowerCase();
        if (ELISIONS[cleanElision]) {
            const el = ELISIONS[cleanElision];
            return {
                word,
                readings: [{
                    lemma: el.lemma,
                    pos: el.pos,
                    translation: el.translation,
                    analysis: el.analysis
                }]
            };
        }

        // 2. Contractions
        const cleanKey = cleanFrenchWord(word);
        if (CONTRACTIONS[cleanKey]) {
            const ct = CONTRACTIONS[cleanKey];
            return {
                word,
                readings: [{
                    lemma: ct.lemma,
                    pos: ct.pos,
                    translation: ct.translation,
                    analysis: ct.analysis
                }]
            };
        }

        // 3. Compound adverbs like aujourd'hui
        if (cleanKey === "aujourd'hui" || cleanKey === "aujourd’hui") {
            return {
                word,
                readings: [{
                    lemma: "aujourd'hui",
                    pos: 'adverb',
                    translation: 'today',
                    analysis: 'adverb of time'
                }]
            };
        }

        const dict = (ctx && ctx.dictionary) || {};
        const wordIndex = (ctx && ctx.wordIndex) || {};
        const verbIndex = (ctx && ctx.verbIndex) || {};
        const readings = [];
        const seen = new Set();

        function addReading(lemma, pos, analysis) {
            const dedupe = lemma + '|' + (analysis || '');
            if (seen.has(dedupe)) return;
            seen.add(dedupe);
            const entry = dict[lemma] || {};
            readings.push({
                lemma,
                pos: entry.type || pos || 'unknown',
                gender: entry.gender,
                translation: entry.en || null,
                analysis: analysis || ''
            });
        }

        // A. Direct headword
        if (dict[cleanKey]) {
            addReading(cleanKey, dict[cleanKey].type, '');
        }

        // B. Inflected nouns/adjectives from wordIndex
        if (wordIndex[cleanKey]) {
            const entries = Array.isArray(wordIndex[cleanKey]) ? wordIndex[cleanKey] : [wordIndex[cleanKey]];
            entries.forEach(e => addReading(e.lemma, e.pos, (e.gender ? e.gender + ' ' : '') + (e.number || '')));
        }

        // C. Conjugated verbs from verbIndex
        if (verbIndex[cleanKey]) {
            const entries = Array.isArray(verbIndex[cleanKey]) ? verbIndex[cleanKey] : [verbIndex[cleanKey]];
            entries.forEach(e => addReading(e.lemma, 'verb', (e.tense || '') + ' ' + (e.person || '')));
        }

        // D. Runtime verb analysis fallback
        if (!readings.length) {
            const verbMatches = analyze(cleanKey, dict);
            verbMatches.forEach(v => addReading(v.lemma, 'verb', v.analysis));
        }

        // E. Runtime adjective/noun analysis fallback
        if (!readings.length || !readings.some(r => r.pos === 'adjective')) {
            const nounMatches = analyzeWord(cleanKey, dict);
            nounMatches.forEach(n => addReading(n.lemma, n.pos, n.analysis));
        }

        // Prioritize readings that have an actual English translation
        readings.sort((a, b) => (Boolean(b.translation) - Boolean(a.translation)));

        return { word, readings };
    }

    return {
        contractions: CONTRACTIONS,
        elisions: ELISIONS,
        cleanFrenchWord,
        candidateVerbLemmas,
        analyze,
        analyzeWord,
        lookup
    };
})();

if (typeof window !== 'undefined') {
    window.FrenchMorphology = FrenchMorphology;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FrenchMorphology;
}
