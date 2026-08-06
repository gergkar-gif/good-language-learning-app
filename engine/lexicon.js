// ============================================
// LEXICON — word lookup (lemma + grammar + translation)
// ============================================
// Three data layers, loaded together on first use:
//   generated/indexes/verb-index.json  conjugated form -> lemma + full analysis
//   generated/indexes/word-index.json  inflected noun/adj/adv -> lemma
//   imports/dictionary/spanish-en.json lemma -> English translation
//
// These total several MB, so they are fetched lazily the first time a
// learner taps a word rather than on app startup.

const Lexicon = (function () {
    'use strict';

    let _verbIndex = null;
    let _wordIndex = null;
    let _dictionary = null;
    let _frequency = null;   // lemma -> rank (lower is more common)
    let _loadPromise = null;

    const TENSE_LABELS = {
        presente: 'Present', preterito: 'Preterite', imperfecto: 'Imperfect',
        futuro: 'Future', condicional: 'Conditional'
    };
    const MOOD_LABELS = {
        indicativo: 'Indicative', subjuntivo: 'Subjunctive', imperative: 'Imperative'
    };
    const FORM_LABELS = {
        infinitive: 'Infinitive', gerund: 'Gerund', participle: 'Past participle'
    };
    const POS_LABELS = {
        n: 'noun', adj: 'adjective', adv: 'adverb', pron: 'pronoun',
        prep: 'preposition', conj: 'conjunction', interj: 'interjection',
        art: 'article', num: 'numeral', determiner: 'determiner', part: 'particle'
    };
    const PERSON_LABELS = {
        '1-singular': '1st person singular', '2-singular': '2nd person singular',
        '3-singular': '3rd person singular', '1-plural': '1st person plural',
        '2-plural': '2nd person plural', '3-plural': '3rd person plural'
    };

    function load() {
        if (_loadPromise) return _loadPromise;

        _loadPromise = Promise.all([
            fetch('generated/indexes/verb-index.json').then(r => r.ok ? r.json() : {}),
            fetch('generated/indexes/word-index.json').then(r => r.ok ? r.json() : {}),
            fetch('imports/dictionary/spanish-en.json').then(r => r.ok ? r.json() : {}),
            fetch('generated/indexes/frequency.json').then(r => r.ok ? r.json() : [])
        ]).then(([verbs, words, dict, freq]) => {
            _verbIndex = verbs;
            _wordIndex = words;
            _dictionary = dict;
            _frequency = new Map(freq.map((lemma, i) => [lemma, i]));
            console.log('Lexicon loaded:',
                Object.keys(verbs).length, 'verb forms,',
                Object.keys(words).length, 'word forms,',
                Object.keys(dict).length, 'dictionary entries,',
                _frequency.size, 'ranked lemmas');
        }).catch(err => {
            console.error('Lexicon failed to load:', err);
            _verbIndex = _verbIndex || {};
            _wordIndex = _wordIndex || {};
            _dictionary = _dictionary || {};
            _frequency = _frequency || new Map();
        });

        return _loadPromise;
    }

    function normalise(word) {
        return String(word || '').toLowerCase().replace(/[.,!?¡¿;:"'()]/g, '').trim();
    }

    // "Imperfect, Indicative, 1st person plural" from a verb-index entry
    function describeVerb(a) {
        if (a.form) return FORM_LABELS[a.form] || a.form;
        const bits = [];
        if (a.tense) bits.push(TENSE_LABELS[a.tense] || a.tense);
        if (a.mood) bits.push(MOOD_LABELS[a.mood] || a.mood);
        if (a.polarity === 'negativo') bits.push('negative');
        const person = PERSON_LABELS[a.person + '-' + a.number];
        if (person) bits.push(person);
        return bits.join(', ');
    }

    // Cheap morphological description for nouns/adjectives. The word index
    // gives us lemma + part of speech but not number/gender, and deriving
    // them properly would need the full inflection tables; comparing the
    // surface form against its lemma covers the common regular cases and
    // stays silent when it isn't confident.
    function describeWord(form, lemma) {
        const isPlural = form.endsWith('s') && !lemma.endsWith('s');
        const isFeminine = /a$|as$/.test(form) && /o$/.test(lemma);
        if (isPlural && isFeminine) return 'feminine plural';
        if (isPlural) return 'plural';
        if (isFeminine) return 'feminine';
        return '';
    }

    /**
     * Look up a word, returning every reading we can find.
     *
     * Ordering is deliberate: a word that is itself a dictionary headword
     * comes first, then noun/adjective inflections, then verb forms. Many
     * Spanish words are genuinely ambiguous ("casas" is both "houses" and
     * "you marry"), and at A1/A2 the everyday-noun reading is far more
     * often the intended one — but every reading is returned so the UI can
     * offer the alternatives rather than silently choosing.
     */
    function lookup(word) {
        const key = normalise(word);
        if (!key) return { word: word, readings: [] };

        const readings = [];
        const seen = new Set();

        function add(lemma, pos, analysis) {
            const entry = _dictionary[lemma];
            const dedupeKey = lemma + '|' + (analysis || '');
            if (seen.has(dedupeKey)) return;
            seen.add(dedupeKey);
            readings.push({
                lemma: lemma,
                pos: (entry && entry.type) || POS_LABELS[pos] || pos || '',
                gender: entry && entry.gender,
                translation: entry ? entry.en : null,
                analysis: analysis || ''
            });
        }

        // the word is already a dictionary headword
        if (_dictionary[key]) add(key, null, '');
        // inflected noun / adjective / adverb
        (_wordIndex[key] || []).forEach(a => add(a.lemma, a.pos, describeWord(key, a.lemma)));
        // conjugated verb
        (_verbIndex[key] || []).forEach(a => add(a.lemma, 'verb', describeVerb(a)));

        // Rank the readings so the likeliest one leads. Proper nouns sink
        // to the bottom (Wiktionary carries many surnames and place names
        // that collide with ordinary vocabulary), then the more frequent
        // lemma wins — that is what separates "vez" (54th most common word
        // in Spanish) from the rare preposition also spelled "veces".
        readings.sort((a, b) =>
            (isProperNoun(a) - isProperNoun(b)) || (rankOf(a) - rankOf(b))
        );

        return { word: word, readings: readings };
    }

    // Longest multi-word expression containing the tapped word, if any.
    // "mucho gusto" means "nice to meet you" — translating the two words
    // separately ("much" + "taste") is actively misleading, so a phrase
    // match takes priority over the individual word.
    const MAX_PHRASE_WORDS = 4;

    function findPhrase(tokens, index) {
        if (!_dictionary || !tokens || index == null) return null;
        const clean = tokens.map(normalise);

        for (let size = MAX_PHRASE_WORDS; size >= 2; size--) {
            // every window of this size that still covers the tapped word
            for (let start = index - size + 1; start <= index; start++) {
                if (start < 0 || start + size > clean.length) continue;
                const parts = clean.slice(start, start + size);
                if (parts.some(p => !p)) continue;
                const phrase = parts.join(' ');
                const entry = _dictionary[phrase];
                if (entry) {
                    return {
                        phrase: tokens.slice(start, start + size).join(' '),
                        pos: entry.type || '',
                        translation: entry.en
                    };
                }
            }
        }
        return null;
    }

    function isProperNoun(reading) {
        return reading.pos === 'proper noun' ? 1 : 0;
    }

    // Unranked lemmas fall outside the top 20k, so they sort after
    // everything that has a rank rather than ahead of it.
    function rankOf(reading) {
        if (!_frequency) return Number.MAX_SAFE_INTEGER;
        const rank = _frequency.get(String(reading.lemma).toLowerCase());
        return rank === undefined ? Number.MAX_SAFE_INTEGER : rank;
    }

    function isLoaded() {
        return _dictionary !== null;
    }

    /** Raw dictionary entry for an exact lemma, or null if unavailable. */
    function define(lemma) {
        if (!_dictionary || !lemma) return null;
        return _dictionary[String(lemma).toLowerCase()] || null;
    }

    return {
        load: load, lookup: lookup, isLoaded: isLoaded,
        define: define, findPhrase: findPhrase
    };
})();
