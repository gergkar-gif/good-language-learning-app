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

    // Object/reflexive pronouns attach directly onto an infinitive, gerund
    // or affirmative command with no space — "conocerte" (conocer + te),
    // "dármelo" (dar + me + lo) — a fully productive construction, so it
    // can't be enumerated in the verb index the way finite conjugations
    // are (checked: none of these forms are in generated/indexes/verb-
    // index.json, confirmed against 102 real examples found across the
    // course's own reading content, "conocerte" among them). Longest
    // pronoun first so "selo" strips as one clitic pair, not "s" + "elo".
    const ENCLITIC_PRONOUNS = ['selo', 'sela', 'selos', 'selas',
        'nos', 'les', 'los', 'las', 'me', 'te', 'se', 'lo', 'la', 'le'];

    function stripAccents(text) {
        return text.normalize('NFD').replace(/[̀-ͯ]/g, '');
    }

    // Every way `word` could be an infinitive/gerund with one or two
    // enclitic pronouns stuck on the end, longest (most specific) match
    // first. A stem only counts if it still looks like a verb form once
    // the pronoun(s) are gone — checked accent-insensitively, since a
    // second pronoun can force a written accent onto the stem ("dar" ->
    // "dármelo") that a bare infinitive never carries. The stem itself is
    // returned accent-stripped too, since that written accent exists only
    // to preserve the pronunciation once the pronouns are attached — the
    // dictionary/verb-index key underneath is always the plain "dar".
    function encliticStems(word) {
        const stems = [];
        const looksLikeVerb = s => /(ar|er|ir|ando|iendo)$/.test(stripAccents(s));

        for (const p1 of ENCLITIC_PRONOUNS) {
            if (!word.endsWith(p1) || word.length - p1.length < 3) continue;
            const stem1 = word.slice(0, -p1.length);
            if (looksLikeVerb(stem1)) stems.push(stripAccents(stem1));

            for (const p2 of ENCLITIC_PRONOUNS) {
                if (!stem1.endsWith(p2) || stem1.length - p2.length < 3) continue;
                const stem2 = stem1.slice(0, -p2.length);
                if (looksLikeVerb(stem2)) stems.push(stripAccents(stem2));
            }
        }
        return stems;
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

        // Nothing direct — try peeling one or two attached pronouns off and
        // looking up what's left, itself either a conjugated form (gerunds,
        // commands — checked first) or, failing that, a bare dictionary
        // headword. Whichever finds it, not both: the infinitive form of
        // "conocer" is in *both* the dictionary and the verb index, and
        // without this the two would add the same reading twice.
        if (!readings.length) {
            for (const stem of encliticStems(key)) {
                const verbForms = _verbIndex[stem] || [];
                if (verbForms.length) {
                    verbForms.forEach(a => add(a.lemma, 'verb', describeVerb(a) + ' + pronoun'));
                } else if (_dictionary[stem]) {
                    add(stem, null, 'infinitive + pronoun');
                }
            }
        }

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

    const WORD_CHAR = /[a-zà-ÿñ]/i;

    // Where q sits inside en (already known to be a substring, at index
    // `at`): a whole word/gloss match beats one that merely starts a word,
    // which beats one buried mid-word — so searching "a" doesn't rank every
    // definition containing "a difficulty..." above an actual match. Tiers
    // are interleaved with the Spanish-side tiers in search() below: an
    // exact English word ("table" -> "mesa") should outrank a Spanish word
    // that merely happens to start with the same letters ("tablero"), which
    // is why this returns 1/3/5 rather than 2/3/4.
    function englishMatchTier(en, q, at) {
        const before = at === 0 ? '' : en[at - 1];
        const after = en[at + q.length] || '';
        const startsWord = at === 0 || !WORD_CHAR.test(before);
        const endsWord = !WORD_CHAR.test(after);
        if (startsWord && endsWord) return 1;
        if (startsWord) return 3;
        return 5;
    }

    /**
     * Free-text lookup across every headword and its translation, for
     * pickers that let a learner find a word rather than tap one (e.g.
     * building a My Deck) — in Spanish ("aeropuerto") or in English
     * ("airport"), since a learner reaches for whichever they know. Ranked
     * by how the query matched (exact lemma, lemma prefix, whole-word
     * translation match, translation prefix, lemma substring, translation
     * substring), then by frequency within each tier — proper nouns and
     * unranked lemmas sink to the bottom of theirs, same reasoning as
     * lookup()'s reading order.
     */
    function search(query, limit) {
        limit = limit || 20;
        const q = normalise(query);
        if (!_dictionary || !q) return [];

        const scored = [];
        for (const lemma in _dictionary) {
            const entry = _dictionary[lemma];

            // A word can match on both sides at once ("mesa" -> "table" is
            // an exact English match; a Spanish query might also happen to
            // prefix-match its own lemma) — take whichever side matched
            // better rather than picking one side and ignoring the other.
            let tier = Infinity;
            if (lemma === q) tier = 0;
            else if (lemma.indexOf(q) === 0) tier = 2;
            else if (lemma.indexOf(q) !== -1) tier = 4;

            const en = (entry.en || '').toLowerCase();
            const at = en.indexOf(q);
            if (at !== -1) tier = Math.min(tier, englishMatchTier(en, q, at));

            if (tier === Infinity) continue;
            scored.push({ lemma: lemma, tier: tier });
        }

        const rank = item => {
            const entry = _dictionary[item.lemma];
            const reading = { pos: entry && entry.type, lemma: item.lemma };
            return (isProperNoun(reading) * 1e9) + rankOf(reading);
        };
        scored.sort((a, b) => a.tier - b.tier || rank(a) - rank(b) || a.lemma.localeCompare(b.lemma));

        return scored.slice(0, limit).map(item => {
            const entry = _dictionary[item.lemma];
            return { lemma: item.lemma, translation: entry.en, pos: entry.type || '' };
        });
    }

    // "el" or "la" for a noun with a known simple gender, so a learner
    // collecting vocabulary gets the article for free rather than having to
    // learn "mesa" and its gender as two separate facts. Deliberately silent
    // for anything not plainly 'm' or 'f' (invariant nouns, "m; f", plurals,
    // etc.) — a wrong guess is worse than no article at all.
    function article(lemma) {
        const entry = define(lemma);
        if (!entry || entry.type !== 'noun') return null;
        if (entry.gender === 'm') return 'el';
        if (entry.gender === 'f') return 'la';
        return null;
    }

    // "gato" -> "el gato". The single place that formats a lemma with its
    // article, so every screen that lists Spanish words (Decks, Library) does
    // it the same way rather than each re-implementing the m/f check.
    function withArticle(lemma) {
        const a = article(lemma);
        return a ? a + ' ' + lemma : lemma;
    }

    // Rank of a lemma in the frequency list (0 = most common), or null if it
    // falls outside the top 20k or the list hasn't loaded. Used to estimate a
    // My Text's reading level — a coarse proxy, not a real CEFR assessment.
    function frequencyRank(lemma) {
        if (!_frequency) return null;
        const rank = _frequency.get(String(lemma || '').toLowerCase());
        return rank === undefined ? null : rank;
    }

    return {
        load: load, lookup: lookup, isLoaded: isLoaded, article: article,
        withArticle: withArticle, frequencyRank: frequencyRank,
        define: define, findPhrase: findPhrase, search: search
    };
})();
