// ============================================
// VOCABULARY DRILLER
// ============================================
// Per PARLOUR_VOCABULARY_DRILLER_SPEC.md: this driller does not duplicate
// My Decks/SRS (direct flashcard recall — "what does X mean?" with no
// context — belongs there). It trains recognising, inferring and
// retrieving vocabulary *in context*.
//
// No new content or exercise database. Everything is built at runtime from
// three things Parlour already has:
//   content/<lang>/decks/decks.json                  the curriculum word list
//   content/<lang>/indexes/translation-index.json    real sentences, per-course
//   engine/lexicon.js (word/verb index + dictionary)  surface form -> lemma
//
// _buildContextIndex() scans every sentence once, resolving each token to
// its lemma via Lexicon.lookup() — the same resolution the reader's word tap
// uses — so a sentence containing "agotadas" is correctly filed under the
// lemma "agotado". A sentence under 5 words is dropped as a context (the
// spec's "Yo quiero un ______" problem: too little to recover the answer
// from) — the one piece of automated quality control this needs, per the
// spec's own "conservative content selection, not an elaborate QC engine".
//
// Six exercise builders (see PARLOUR_VOCABULARY_DRILLER_SPEC.md's numbered
// list) each try to build one exercise for a word from its available
// contexts, returning null when the data doesn't support that type — a
// polysemy-style "same word, different context" exercise just doesn't exist
// for a word with only one sentence, same "some pools run smaller"
// precedent used elsewhere in this app. For each word in a session, one
// applicable type is picked at random, so a session is naturally a mix of
// all six rather than needing a type picker in the UI.
//
// Both exercise kinds (multiple-choice, fill-blank) are already renderable
// by GrammarRunner, so this module reuses it rather than writing a new one.

const VocabularyDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const MODE = { COUNT: 'count', TIMED: 'timed' };
    const COUNT_OPTIONS = [5, 10, 15, 20, 30];
    const TIMER_PRESETS = [1, 2, 3, 5];
    const DECOY_COUNT = 3;

    // A sentence shorter than this can't reliably support an inferable
    // answer — see the spec's own "Yo quiero un ______" counter-example.
    const MIN_CONTEXT_WORDS = 5;
    const WORD_RE = /\p{L}+/gu;

    let _phase = PHASE.SETTINGS;
    let _container = null;

    // Canonical CEFR ordering for the level picker — only levels the course
    // actually has lesson decks for are ever shown (see _load()), so this
    // never hardcodes a language's highest level and silently drops it as
    // new levels are added (found 2026-09-01: the picker only ever offered
    // "All levels"/A1/A2, hardcoded, so a course's B1 words — real content,
    // reachable only via "All levels" — had no dedicated filter option).
    const CEFR_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

    const TRACK = { CORE: 'core' };
    const TRACK_LABELS = { latam: 'Latin America', citizenship: 'Citizenship' };

    let _words = null;        // decks.json -> words { lemma: {en, pos} }
    let _wordLevels = null;   // lemma -> 'A1' | 'A2' | ... (from lesson decks)
    let _wordTracks = null;   // lemma -> Set(['core', ...])
    let _levelTracks = null;  // level -> Set(['core', ...])
    let _levels = null;       // distinct levels this course's lesson decks use, CEFR order
    let _pairs = null;        // translation-index.json -> pairs[]
    let _contextIndex = null; // lemma -> [{ sentence, english, form, inflected, track }]
    let _wordLessonIndex = null; // word-lesson-index.json's byLemma map — the Tier 2 cross-link

    let _mode = MODE.COUNT;
    let _level = 'all';
    let _track = TRACK.CORE;
    let _questionCount = 10;
    let _timerMinutes = 2;

    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;
    let _missed = []; // {lemma, translation, pos} for each distinct word missed this session

    let _timerInterval = null;
    let _endTime = 0;
    let _timeRemaining = 0;

    // ---- Helpers ----
    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _sample(list) {
        return list[Math.floor(Math.random() * list.length)];
    }

    function _formatTime(totalSeconds) {
        const m = Math.floor(totalSeconds / 60);
        const s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    let _loadedLang = null;

    // ---- Data loading (per language) ----
    async function _load() {
        if (_words && _pairs && _contextIndex && _loadedLang === Lang.code()) return;
        const [deckData, translationIndex, wordLessonIndex] = await Promise.all([
            Content.json(Lang.content('decks/decks.json')).catch(() => ({ words: {}, decks: [] })),
            Content.json(Lang.content('indexes/translation-index.json')).catch(() => ({ pairs: [] })),
            Content.json(Lang.content('indexes/word-lesson-index.json')).catch(() => ({ byLemma: {} })),
            Lexicon.load()
        ]);
        _words = deckData.words || {};
        _pairs = translationIndex.pairs || [];
        _wordLessonIndex = wordLessonIndex.byLemma || {};
        _wordLevels = {};
        _wordTracks = {};
        _levelTracks = {};
        const seenLevels = new Set();
        (deckData.decks || []).filter(d => d.kind === 'lesson').forEach(d => {
            const deckTrack = d.track || TRACK.CORE;
            if (d.level) {
                seenLevels.add(d.level);
                const normLvl = d.level.toUpperCase();
                if (!_levelTracks[normLvl]) _levelTracks[normLvl] = new Set();
                _levelTracks[normLvl].add(deckTrack);
            }
            (d.lemmas || []).forEach(lemma => {
                if (!(lemma in _wordLevels)) _wordLevels[lemma] = d.level;
                if (!_wordTracks[lemma]) _wordTracks[lemma] = new Set();
                _wordTracks[lemma].add(deckTrack);
            });
        });
        _levels = CEFR_ORDER.filter(l => seenLevels.has(l));
        _contextIndex = _buildContextIndex();
        _loadedLang = Lang.code();
    }

    if (typeof document !== 'undefined') {
        document.addEventListener('language-changed', () => {
            _words = null;
            _pairs = null;
            _contextIndex = null;
            _wordLevels = null;
            _wordTracks = null;
            _levelTracks = null;
            _levels = null;
            _track = TRACK.CORE;
            _loadedLang = null;
        });
    }

    function _secondTrack(level) {
        if (!_levelTracks) return null;
        if (level && level !== 'all') {
            const tracks = _levelTracks[level.toUpperCase()];
            if (tracks) {
                for (const t of tracks) {
                    if (t !== TRACK.CORE) return t;
                }
            }
            return null;
        }
        for (const lvl of Object.keys(_levelTracks)) {
            for (const t of _levelTracks[lvl]) {
                if (t !== TRACK.CORE) return t;
            }
        }
        return null;
    }

    function _trackLabel(track) {
        return TRACK_LABELS[track] || (track.charAt(0).toUpperCase() + track.slice(1));
    }

    // One pass over the sentence corpus, resolving every token to a lemma
    // the same way a tapped word in the Reader would be. Built once and
    // reused for every exercise type below, rather than re-scanning the
    // corpus per word (which would be O(words × sentences) instead of
    // O(sentences × words per sentence)).
    function _buildContextIndex() {
        const index = {};
        _pairs.forEach(pair => {
            const sentence = pair.spanish || pair.hungarian || pair.target || '';
            const tokens = sentence.match(WORD_RE) || [];
            if (tokens.length < MIN_CONTEXT_WORDS) return;

            const seenKeys = new Set();
            tokens.forEach(token => {
                const tokenLower = token.toLowerCase();
                const readings = (typeof Lexicon !== 'undefined' && typeof Lexicon.lookup === 'function')
                    ? Lexicon.lookup(token).readings
                    : [];
                const keysToIndex = new Set([tokenLower]);
                if (readings && readings.length) {
                    keysToIndex.add(readings[0].lemma.toLowerCase());
                }

                keysToIndex.forEach(key => {
                    if (seenKeys.has(key)) return;
                    seenKeys.add(key);

                    (index[key] || (index[key] = [])).push({
                        sentence: sentence,
                        english: pair.english || pair.translation || '',
                        form: token,
                        inflected: (readings && readings.length)
                            ? (tokenLower !== readings[0].lemma.toLowerCase())
                            : false,
                        track: pair.track || TRACK.CORE
                    });
                });
            });
        });
        return index;
    }

    // Content words only — nouns, verbs, adjectives, adverbs. Articles,
    // pronouns, prepositions and the like are real vocabulary too, but
    // "what does 'las' mean here?" against random decoys isn't a
    // meaningful inference question the way "what does 'agotado' mean
    // here?" is; every example in the spec is a content word. Filtering
    // here also keeps them out of the decoy pools below, since those draw
    // from the same word list.
    const CONTENT_POS = new Set(['noun', 'verb', 'adjective', 'adverb']);

    // A word whose first-taught lesson is on record but not yet completed
    // hasn't actually been reached in the learner's own progress, even
    // though it can sit earlier than other lessons they've already
    // finished — the driller used to sample level-wide regardless of
    // personal lesson progress, so a word taught in, say, lesson 120 could
    // turn up in a session for someone only up to lesson 70 (bug report
    // #151, 2026-09-16). word-lesson-index.json only covers vocabulary
    // explicitly listed in a lesson's own vocab list, so a lemma with no
    // entry there (met only in grammar examples or story content) is never
    // gated: there's no "not yet taught" evidence for it, so excluding it
    // would just shrink the pool for no real reason.
    function _isReached(lemma) {
        const lessonId = _wordLessonIndex[lemma];
        if (!lessonId) return true;
        return (typeof LearnerPath !== 'undefined') ? LearnerPath.isComplete(lessonId) : true;
    }

    function _wordList(level, track) {
        const activeTrack = track || _track || TRACK.CORE;
        const hasSecond = _secondTrack(level);
        return Object.keys(_words)
            .filter(lemma => CONTENT_POS.has(_words[lemma].pos))
            .filter(lemma => level === 'all' || _wordLevels[lemma] === level)
            .filter(lemma => {
                if (!hasSecond) return true;
                const tracks = _wordTracks && _wordTracks[lemma];
                if (!tracks || !tracks.size) return activeTrack === TRACK.CORE;
                return tracks.has(activeTrack);
            })
            .filter(_isReached)
            .map(lemma => ({ lemma, en: _words[lemma].en, pos: _words[lemma].pos }));
    }

    // Intelligent context occurrence resolver: resolves deck keys through a
    // multi-tier waterfall (direct token match, lowercase, slash-separated
    // gender pairs, article stripping, and Lexicon lemma analysis) so surface
    // forms ("soy", "alto / alta", "el gato") seamlessly match real sentences.
    function _getOccurrences(word, track) {
        if (!word || !_contextIndex) return [];
        const raw = (typeof word === 'string') ? word : word.lemma;
        if (!raw) return [];

        function _filterByTrack(matches) {
            if (!matches || !matches.length) return [];
            const activeTrack = track || _track || TRACK.CORE;
            if (activeTrack === TRACK.CORE) {
                return matches.filter(m => !m.track || m.track === TRACK.CORE);
            }
            const trackMatches = matches.filter(m => m.track === activeTrack);
            return trackMatches.length ? trackMatches : matches;
        }

        // 1. Direct match
        if (_contextIndex[raw] && _contextIndex[raw].length) return _filterByTrack(_contextIndex[raw]);

        // 2. Case-insensitive / lowercase match
        const lower = raw.toLowerCase();
        if (_contextIndex[lower] && _contextIndex[lower].length) return _filterByTrack(_contextIndex[lower]);

        // 3. Slash split (e.g. 'alto / alta' -> 'alto', 'alta')
        if (raw.includes('/')) {
            const parts = raw.split('/').map(s => s.trim().toLowerCase()).filter(Boolean);
            const combined = [];
            const seenSentences = new Set();
            for (const p of parts) {
                const subOcc = _contextIndex[p] || [];
                for (const item of subOcc) {
                    if (!seenSentences.has(item.sentence)) {
                        seenSentences.add(item.sentence);
                        combined.push(item);
                    }
                }
            }
            if (combined.length) return _filterByTrack(combined);
        }

        // 4. Article stripping (e.g. 'el perro' -> 'perro', 'la casa' -> 'casa')
        const noArt = lower.replace(/^(el|la|los|las|un|una)\s+/i, '').trim();
        if (noArt !== lower) {
            if (_contextIndex[noArt] && _contextIndex[noArt].length) return _filterByTrack(_contextIndex[noArt]);
            if (typeof Lexicon !== 'undefined' && typeof Lexicon.lookup === 'function') {
                const lk = Lexicon.lookup(noArt);
                if (lk && lk.readings && lk.readings.length) {
                    for (const r of lk.readings) {
                        const lem = r.lemma.toLowerCase();
                        if (_contextIndex[lem] && _contextIndex[lem].length) return _filterByTrack(_contextIndex[lem]);
                    }
                }
            }
        }

        // 5. Lexicon lemma lookup fallback (e.g. 'soy' -> 'ser', 'quiero' -> 'querer')
        if (typeof Lexicon !== 'undefined' && typeof Lexicon.lookup === 'function') {
            const lk = Lexicon.lookup(lower);
            if (lk && lk.readings && lk.readings.length) {
                for (const r of lk.readings) {
                    const lem = r.lemma.toLowerCase();
                    const lemmaOcc = _contextIndex[lem];
                    if (lemmaOcc && lemmaOcc.length) {
                        const exactFormMatches = lemmaOcc.filter(o => o.form.toLowerCase() === lower);
                        if (exactFormMatches.length) return _filterByTrack(exactFormMatches);
                        return _filterByTrack(lemmaOcc);
                    }
                }
            }
        }

        // 6. Hungarian infinitive fallback (e.g. 'hozni' -> stem 'hoz')
        if (lower.endsWith('ni')) {
            const stem = lower.slice(0, -2);
            if (_contextIndex[stem] && _contextIndex[stem].length) return _filterByTrack(_contextIndex[stem]);
        }

        return [];
    }

    function _hasContext(word, track) {
        return _getOccurrences(word, track).length > 0;
    }

    // Unicode-aware word boundaries so an accented form (día, agotadas) is
    // matched correctly — plain \b treats accented letters as non-word
    // characters and misses them.
    function _wordRegex(form) {
        const escaped = form.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp('(^|[^\\p{L}])(' + escaped + ')([^\\p{L}]|$)', 'iu');
    }

    function _blankSentence(sentence, form) {
        const m = sentence.match(_wordRegex(form));
        if (!m) return null;
        const start = m.index + m[1].length;
        return sentence.slice(0, start) + '_____' + sentence.slice(start + m[2].length);
    }

    // Translation decoys for a "what does this mean" question. `samePos`
    // narrows the pool to words of the same part of speech first — the
    // spec's "meaning discrimination" and "morphological inference" types
    // want decoys that are plausible, not just any random word, and sharing
    // a part of speech is a light, data-driven way to get that without
    // hand-curating distractor sets.
    function _pickTranslationDecoys(word, n, samePos) {
        let candidates = Object.keys(_words)
            .filter(l => CONTENT_POS.has(_words[l].pos) && l !== word.lemma && _words[l].en !== word.en);
        if (samePos) {
            const narrowed = candidates.filter(l => _words[l].pos === word.pos);
            if (narrowed.length >= n) candidates = narrowed;
        }
        return _shuffled(candidates).slice(0, n).map(l => _words[l].en);
    }

    // Same idea, but the decoys are Spanish words (for "which word fits the
    // blank" rather than "what does the word mean"). Excludes by spelling
    // against `form` (the correct answer as it actually appears in the
    // blanked sentence — often inflected), not just by lemma: a candidate
    // lemma can coincide with another word's inflected surface form (a
    // cross-POS homograph like "como", both the adverb "as/like" and a
    // conjugated form of "comer") — same "exclude by displayed value, not
    // key" fix _pickTranslationDecoys already applies via its `en` check.
    // Unguarded, that let a decoy render with the exact same text as the
    // correct option, so clicking either "como" gave a different result
    // for what looked like the identical answer.
    function _pickWordDecoys(word, form, n) {
        const formLower = form.toLowerCase();
        let candidates = Object.keys(_words)
            .filter(l => CONTENT_POS.has(_words[l].pos) && l !== word.lemma && l.toLowerCase() !== formLower);
        const narrowed = candidates.filter(l => _words[l].pos === word.pos);
        if (narrowed.length >= n) candidates = narrowed;
        return _shuffled(candidates).slice(0, n).map(l => {
            let clean = l;
            if (clean.includes('/')) {
                const parts = clean.split('/').map(p => p.trim());
                clean = parts.find(p => p.slice(-1) === formLower.slice(-1)) || parts[0];
            }
            clean = clean.replace(/^(el|la|los|las|un|una)\s+/i, '').trim();
            return clean;
        });
    }

    // Some corpus sentences carry no terminal punctuation (fragments pulled
    // from grammar exercises rather than full prose) — without this the
    // follow-up question runs straight into the sentence with nothing
    // between them.
    function _withStop(sentence) {
        const trimmed = sentence.trim();
        return /[.!?]$/.test(trimmed) ? trimmed : trimmed + '.';
    }

    function _meaningQuestion(sentence, form) {
        return `${_withStop(sentence)} What does "${form}" mean here?`;
    }

    // Shown after Check, alongside the revealed answer — GrammarRunner
    // already renders ex.explanation once an exercise is solved, so this is
    // the sentence's own translation-index English pair, not anything new.
    function _translationExplanation(match) {
        return `Translation: ${match.english}`;
    }

    // ================================================================
    //  EXERCISE BUILDERS — one per type in PARLOUR_VOCABULARY_DRILLER_SPEC.md
    //  Each returns a GrammarRunner-shaped exercise, or null if this word
    //  doesn't have the context data this type needs.
    // ================================================================

    // 1. Contextual inference — the defining exercise: a real sentence, the
    // target word in it, plain multiple-choice decoys.
    function _buildInference(word) {
        const matches = _getOccurrences(word);
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, false)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    // 2. Contextual recall — the sentence is blanked instead, with the
    // English meaning given as a hint; the learner types the Spanish word.
    // The expected answer is the exact form found in the sentence (an
    // inflected form if that's what appeared), not the bare dictionary
    // lemma — "agotadas" for a sentence that actually says "agotadas".
    function _buildRecall(word) {
        const matches = _getOccurrences(word);
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const blanked = _blankSentence(m.sentence, m.form);
        if (!blanked) return null;
        return {
            kind: 'fill-blank',
            sentence: `English: ${word.en}. ${blanked}`,
            answer: m.form,
            explanation: _translationExplanation(m)
        };
    }

    // 3. Meaning discrimination — same shape as inference, but decoys are
    // drawn from the same part of speech, so they're plausible rather than
    // obviously-wrong.
    function _buildDiscrimination(word) {
        const matches = _getOccurrences(word);
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, true)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    // 4. Same word, different context — the word as it appears in two
    // different real sentences at once. The dictionary here doesn't map
    // senses to specific sentences, so this doesn't force a "which sense"
    // split (that would risk marking a genuinely defensible answer wrong);
    // it tests recognising the same word holding its meaning across two
    // different settings, which is most valuable exactly for the
    // genuinely polysemous words the spec calls out.
    function _buildRepeat(word) {
        const matches = _getOccurrences(word);
        if (!matches || matches.length < 2) return null;
        const [a, b] = _shuffled(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, false)]);
        return {
            kind: 'multiple-choice',
            question: `Sentence 1: ${_withStop(a.sentence)} Sentence 2: ${_withStop(b.sentence)} `
                + `What does "${word.lemma}" mean in both?`,
            options,
            correct: options.indexOf(word.en),
            explanation: `Translation: ${a.english} / ${b.english}`
        };
    }

    // 5. Contextual choice — the sentence is blanked, but instead of typing
    // the learner picks the right Spanish word from same-part-of-speech
    // decoys (no English hint at all — the context alone has to carry it).
    function _buildChoice(word) {
        const matches = _getOccurrences(word);
        if (!matches || !matches.length) return null;
        const m = _sample(matches);
        const blanked = _blankSentence(m.sentence, m.form);
        if (!blanked) return null;
        const options = _shuffled([m.form, ..._pickWordDecoys(word, m.form, DECOY_COUNT)]);
        return {
            kind: 'multiple-choice',
            question: blanked,
            options,
            correct: options.indexOf(m.form),
            explanation: _translationExplanation(m)
        };
    }

    // 6. Morphological inference — the same shape as discrimination, but
    // restricted to a sentence where the word actually shows up inflected
    // ("agotadas", not "agotado") — the point is recognising the word
    // despite the grammatical change.
    function _buildMorphological(word) {
        const matches = _getOccurrences(word).filter(m => m.inflected);
        if (!matches.length) return null;
        const m = _sample(matches);
        const options = _shuffled([word.en, ..._pickTranslationDecoys(word, DECOY_COUNT, true)]);
        return {
            kind: 'multiple-choice',
            question: _meaningQuestion(m.sentence, m.form),
            options,
            correct: options.indexOf(word.en),
            explanation: _translationExplanation(m)
        };
    }

    // Direct recall fallback builders: used when a word lacks corpus sentences
    // or when non-content words are supplied for review.
    function _buildDirectDefinition(word) {
        if (!word.en) return null;
        let decoys = _pickTranslationDecoys(word, DECOY_COUNT, true);
        if (decoys.length < DECOY_COUNT) {
            decoys = _pickTranslationDecoys(word, DECOY_COUNT, false);
        }
        if (decoys.length === 0) return null;
        const options = _shuffled([word.en, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `What does "${word.lemma}" mean?`,
            options,
            correct: options.indexOf(word.en),
            explanation: `${word.lemma}${word.pos ? ' (' + word.pos + ')' : ''}: ${word.en}`
        };
    }

    function _buildReverseChoice(word) {
        if (!word.en) return null;
        const decoys = _pickWordDecoys(word, word.lemma, DECOY_COUNT);
        if (decoys.length === 0) return null;
        const options = _shuffled([word.lemma, ...decoys]);
        return {
            kind: 'multiple-choice',
            question: `Which word means "${word.en}"?`,
            options,
            correct: options.indexOf(word.lemma),
            explanation: `${word.lemma} = ${word.en}`
        };
    }

    function _buildReverseRecall(word) {
        if (!word.en) return null;
        const langName = typeof Lang !== 'undefined' ? Lang.name() : 'target language';
        const acceptable = [word.lemma];
        if (typeof Lexicon !== 'undefined' && typeof Lexicon.withArticle === 'function') {
            const art = Lexicon.withArticle(word.lemma);
            if (art && art !== word.lemma) acceptable.push(art);
        }
        return {
            kind: 'fill-blank',
            sentence: `Translate to ${langName}: "${word.en}" (_____)`,
            answer: word.lemma,
            acceptable,
            explanation: `${word.lemma} = ${word.en}`
        };
    }

    const BUILDERS = [_buildInference, _buildRecall, _buildDiscrimination, _buildRepeat, _buildChoice, _buildMorphological];

    // One random applicable type per word, so a session mixes all six
    // naturally instead of a fixed type dominating because it happens to
    // be tried first. If no sentence context exists for this word, falls back
    // to direct definition or recall builders so words are never dropped.
    function _buildExerciseFor(word) {
        let candidates = [];
        if (word.pos && CONTENT_POS.has(word.pos)) {
            candidates = BUILDERS.map(fn => fn(word)).filter(Boolean);
        }
        let exercise = null;
        if (candidates.length) {
            exercise = _sample(candidates);
        } else {
            const fallbacks = [
                _buildDirectDefinition(word),
                _buildReverseChoice(word),
                _buildReverseRecall(word)
            ].filter(Boolean);
            if (fallbacks.length) {
                exercise = _sample(fallbacks);
            }
        }
        if (!exercise) return null;
        exercise._word = word;
        return exercise;
    }

    function _buildPool(level, track) {
        return _wordList(level, track).map(_buildExerciseFor).filter(Boolean);
    }

    // A pool built directly from caller-supplied words (Decks' review
    // summary, when a session leaves some words shaky) rather than from
    // decks.json's curriculum table via _wordList() — a custom My Deck
    // word wouldn't be in that table at all, so this takes the
    // {lemma, translation, pos} shape Decks already hands around.
    // Words without corpus sentences gracefully fall back to direct recall.
    function _buildPoolFromWords(words) {
        return (words || [])
            .map(w => {
                const lemma = typeof w === 'string' ? w : (w.lemma || w.word);
                if (!lemma) return null;
                let en = (w && (w.translation || w.en)) || (_words && _words[lemma] && _words[lemma].en);
                let pos = (w && w.pos) || (_words && _words[lemma] && _words[lemma].pos);
                if (!en && typeof Lexicon !== 'undefined' && Lexicon.define) {
                    const def = Lexicon.define(lemma);
                    if (def) {
                        en = def.en || def.translation;
                        if (!pos) pos = def.type || def.pos;
                    }
                }
                return { lemma, en: en || lemma, pos: pos || 'noun' };
            })
            .filter(Boolean)
            .map(_buildExerciseFor)
            .filter(Boolean);
    }

    function _takeN(pool, n) {
        const out = [];
        while (out.length < n) out.push(..._shuffled(pool));
        return out.slice(0, n);
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    function _renderSettings() {
        const secondTrack = _secondTrack(_level);
        if (!secondTrack && _track !== TRACK.CORE) _track = TRACK.CORE;

        const available = _wordList(_level, _track).filter(w => _hasContext(w, _track)).length;

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Vocabulary Driller</h2>
                <p class="gd-hint">Recognise, infer and retrieve vocabulary from real ${Lang.name()} sentences —
                    not bare flashcards. Direct recall lives in My Decks.</p>
                <p class="gd-hint">${available} words with example sentences at this level.</p>

                <div class="vb-mode-switcher" role="tablist">
                    <button class="vb-mode-btn${_mode === MODE.COUNT ? ' active' : ''}"
                        data-mode="${MODE.COUNT}" role="tab" aria-selected="${_mode === MODE.COUNT}">By Count</button>
                    <button class="vb-mode-btn${_mode === MODE.TIMED ? ' active' : ''}"
                        data-mode="${MODE.TIMED}" role="tab" aria-selected="${_mode === MODE.TIMED}">Timed</button>
                </div>

                <div class="gd-setting">
                    <label for="vd-level">Level</label>
                    <select id="vd-level" class="vb-select">
                        <option value="all">All levels</option>
                        ${_levels.map(l => `<option value="${l}">${l}</option>`).join('')}
                    </select>
                </div>

                ${secondTrack ? `
                    <div class="gd-setting">
                        <label>Track</label>
                        <div class="vb-mode-switcher" role="tablist">
                            <button class="vb-mode-btn${_track === TRACK.CORE ? ' active' : ''}"
                                data-track="${TRACK.CORE}" role="tab" aria-selected="${_track === TRACK.CORE}">Core</button>
                            <button class="vb-mode-btn${_track === secondTrack ? ' active' : ''}"
                                data-track="${secondTrack}" role="tab" aria-selected="${_track === secondTrack}">${_trackLabel(secondTrack)}</button>
                        </div>
                    </div>
                ` : ''}

                ${_mode === MODE.COUNT ? `
                    <div class="gd-setting">
                        <label for="vd-count">Number of words</label>
                        <select id="vd-count" class="vb-select">
                            ${COUNT_OPTIONS.map(n => `
                                <option value="${n}"${n === _questionCount ? ' selected' : ''}>${n} words</option>
                            `).join('')}
                        </select>
                    </div>
                ` : `
                    <div class="gd-setting">
                        <label for="vd-timer">Timer</label>
                        <select id="vd-timer" class="vb-select">
                            ${TIMER_PRESETS.map(v => `
                                <option value="${v}"${v === _timerMinutes ? ' selected' : ''}>${v === 1 ? '1 minute' : v + ' minutes'}</option>
                            `).join('')}
                        </select>
                    </div>
                `}

                <button class="vbtn vbtn-primary vbtn-block" data-action="start">Start</button>
            </div>
        `;

        _container.querySelectorAll('[data-mode]').forEach(btn => {
            btn.addEventListener('click', () => { _mode = btn.dataset.mode; _renderSettings(); });
        });

        _container.querySelectorAll('[data-track]').forEach(btn => {
            btn.addEventListener('click', () => { _track = btn.dataset.track; _renderSettings(); });
        });

        const levelSelect = _container.querySelector('#vd-level');
        levelSelect.value = _level;
        levelSelect.addEventListener('change', e => {
            _level = e.target.value;
            if (!_secondTrack(_level)) _track = TRACK.CORE;
            _renderSettings();
        });

        const countSelect = _container.querySelector('#vd-count');
        if (countSelect) countSelect.addEventListener('change', e => { _questionCount = Number(e.target.value); });

        const timerSelect = _container.querySelector('#vd-timer');
        if (timerSelect) timerSelect.addEventListener('change', e => { _timerMinutes = Number(e.target.value); });

        _container.querySelector('[data-action="start"]').addEventListener('click', _startSession);
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    function _startSession() {
        let pool = _buildPool(_level, _track);
        if (!pool.length && _level !== 'all') {
            _level = 'all';
            pool = _buildPool('all', _track);
        }
        _seen = 0;
        _correct = 0;
        _missed = [];

        if (!pool.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">No words with example sentences at this level yet.</div>
                <button class="vbtn vbtn-secondary" data-action="change-settings">Change settings</button>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            return;
        }

        if (_mode === MODE.COUNT) {
            _queue = _takeN(pool, _questionCount);
        } else {
            _queue = _shuffled(pool);
            _timeRemaining = _timerMinutes * 60;
            _endTime = Date.now() + _timeRemaining * 1000;
            _timerInterval = setInterval(_tick, 250);
        }

        _queueIndex = 0;
        _phase = PHASE.SESSION;
        _renderSession();
    }

    // Entry point for a scoped session (Decks' review summary's "Practice
    // these words" link) — skips the level/count settings entirely and
    // just runs through the given words once, in Count mode so the
    // session has a real end rather than looping the same handful of
    // words on a timer.
    function _startSessionFromWords(words) {
        const pool = _buildPoolFromWords(words);
        _seen = 0;
        _correct = 0;
        _missed = [];

        if (!pool.length) {
            // This is a scoped request (Decks' "Practice these words", or a
            // Time-Based Session vocabulary item) — the caller isn't the
            // driller's own settings screen, so dropping the learner into
            // the generic level/count picker here would abandon whatever
            // they actually asked for with no way back to it. Offer a real
            // next step instead: mountNextAction already knows how to
            // return to a StudyPlan session in progress, or fall back to a
            // fresh recommendation otherwise — same mechanism a completed
            // session's results screen already uses.
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-empty">These words don't have example sentences yet, so there's nothing to build a context exercise from.</div>
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Practice other words instead</button>
                    <button class="vbtn vbtn-secondary" data-action="exit-workshop">Back to Workshop</button>
                </div>
            `;
            _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
            const exitBtn = _container.querySelector('[data-action="exit-workshop"]');
            if (exitBtn) exitBtn.addEventListener('click', () => { if (typeof Workshop !== 'undefined') Workshop.close(); });
            if (typeof RecommendationEngine !== 'undefined') RecommendationEngine.mountNextAction(_container);
            return;
        }

        _mode = MODE.COUNT;
        _queue = _shuffled(pool);
        _questionCount = _queue.length;
        _queueIndex = 0;
        _phase = PHASE.SESSION;
        _renderSession();
    }

    function _tick() {
        const remaining = Math.max(0, Math.ceil((_endTime - Date.now()) / 1000));
        _timeRemaining = remaining;
        const el = _container.querySelector('.vspeed-timer-display');
        if (el) el.textContent = _formatTime(remaining);
        if (remaining <= 0) _finishSession();
    }

    function _scoreLabel() {
        const base = `${_correct}/${_seen} correct`;
        return _mode === MODE.COUNT ? `${base} · Word ${_queueIndex + 1} of ${_queue.length}` : base;
    }

    function _progressPercent() {
        if (_mode === MODE.COUNT) {
            return Math.min(100, Math.round((_queueIndex / Math.max(1, _queue.length)) * 100));
        }
        const total = _timerMinutes * 60;
        const elapsed = Math.max(0, total - _timeRemaining);
        return Math.min(100, Math.round((elapsed / Math.max(1, total)) * 100));
    }

    function _renderSession() {
        const currentWord = _queue[_queueIndex]._word;

        // Tier 2 cross-link — same as the Reader popup and Decks' word-list
        // rows, just placed here instead of fighting GrammarRunner's own
        // append-don't-replace render lifecycle (its moreInfo/explanation
        // panels get inserted into the exercise container at several points
        // as an exercise is answered, so anything this module wants to add
        // reliably has to live outside that container, not inside it).
        // Shown up front rather than only after answering — it says where
        // a word was taught, never what it means, so it gives nothing away.
        const lessonId = currentWord && _wordLessonIndex ? _wordLessonIndex[currentWord.lemma] : null;
        const lessonInfo = lessonId && typeof lessonLabelFor === 'function' ? lessonLabelFor(lessonId) : null;

        _container.innerHTML = `
            <div class="driller-progress-track" aria-hidden="true">
                <div class="driller-progress-bar" style="width: ${_progressPercent()}%"></div>
            </div>
            <div class="gd-hud">
                <span class="gd-hud-score">${_scoreLabel()}</span>
                ${_mode === MODE.TIMED ? `<span class="vspeed-timer-display">${_formatTime(_timeRemaining)}</span>` : ''}
                <button class="gd-change-skill" data-action="change-settings">← Settings</button>
            </div>
            ${lessonInfo ? `
                <button class="dk-link-btn gd-word-lesson-link" data-open-lesson="${lessonId}">Taught in ${lessonInfo.label}</button>
            ` : ''}
            <div class="gd-exercise"></div>
        `;
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const lessonLinkBtn = _container.querySelector('[data-open-lesson]');
        if (lessonLinkBtn) {
            lessonLinkBtn.addEventListener('click', () => {
                if (typeof startLesson === 'function') startLesson(lessonLinkBtn.getAttribute('data-open-lesson'));
            });
        }

        const exerciseRoot = _container.querySelector('.gd-exercise');

        GrammarRunner.render(exerciseRoot, {
            exercise: _queue[_queueIndex],
            onResult: correct => {
                _seen++;
                if (correct) {
                    _correct++;
                } else if (currentWord && !_missed.some(w => w.lemma === currentWord.lemma)) {
                    _missed.push({ lemma: currentWord.lemma, translation: currentWord.en, pos: currentWord.pos });
                }
                const score = _container.querySelector('.gd-hud-score');
                if (score) score.textContent = _scoreLabel();
                const bar = _container.querySelector('.driller-progress-bar');
                if (bar) bar.style.width = _progressPercent() + '%';
            },
            onNext: _nextExercise
        });
    }

    function _nextExercise() {
        if (_mode === MODE.COUNT && _queueIndex + 1 >= _queue.length) {
            _finishSession();
            return;
        }

        _queueIndex++;
        if (_queueIndex >= _queue.length) {
            _queue = _shuffled(_queue);
            _queueIndex = 0;
        }
        _renderSession();
    }

    // ================================================================
    //  RENDERING — Results
    // ================================================================
    function _finishSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.RESULTS;
        _renderResults();
    }

    function _renderResults() {
        const accuracy = _seen ? Math.round((_correct / _seen) * 100) : 0;

        _container.innerHTML = `
            <div class="vspeed-results">
                <h3 class="vspeed-results-title">Session Results</h3>
                <div class="vspeed-results-grid">
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Correct</span>
                        <span class="vspeed-stat-value">${_correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Wrong</span>
                        <span class="vspeed-stat-value">${_seen - _correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Accuracy</span>
                        <span class="vspeed-stat-value">${accuracy}%</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Total</span>
                        <span class="vspeed-stat-value">${_seen}</span>
                    </div>
                </div>
                ${_missed.length ? `
                    <button class="vbtn vbtn-secondary vbtn-block" data-action="add-missed">
                        Add ${_missed.length} missed ${_missed.length === 1 ? 'word' : 'words'} to a deck
                    </button>
                ` : ''}
                <div class="vspeed-results-actions">
                    <button class="vbtn vbtn-primary" data-action="play-again">Practice Again</button>
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>
                    <button class="vbtn vbtn-secondary" data-action="exit-workshop">Back to Workshop</button>
                </div>
            </div>
        `;

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);
        const exitBtn = _container.querySelector('[data-action="exit-workshop"]');
        if (exitBtn) exitBtn.addEventListener('click', () => { if (typeof Workshop !== 'undefined') Workshop.close(); });

        const addMissedBtn = _container.querySelector('[data-action="add-missed"]');
        if (addMissedBtn) {
            addMissedBtn.addEventListener('click', () => {
                if (typeof Decks !== 'undefined') Decks.openBulkAddPicker(_missed);
            });
        }

        if (typeof RecommendationEngine !== 'undefined') RecommendationEngine.mountNextAction(_container);
    }

    function _abortSession() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    // `options.words`, when given, skips the settings screen and launches
    // straight into a session over exactly those words — used by Decks'
    // review summary. Same firstTime-style guard as GrammarDriller's own
    // `options.skill`: only takes effect from the settings phase, so a
    // driller resumed mid-session (e.g. navigating back to Workshop)
    // shows what was already in progress instead.
    async function render(root, options) {
        _container = root;

        if (options && (options.autoStart || options.words || options.count)) {
            if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
            _phase = PHASE.SETTINGS;
        }

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            if (options && options.words && options.words.length) {
                _startSessionFromWords(options.words);
            } else if (options && (options.autoStart || options.count)) {
                if (options.count) {
                    _questionCount = options.count;
                    _mode = MODE.COUNT;
                }
                if (options.level) _level = options.level;
                if (options.track) _track = options.track;

                const weakWords = (typeof LearnerModel !== 'undefined') ? LearnerModel.weakWords() : [];
                const weakPool = weakWords.length ? _buildPoolFromWords(weakWords.slice(0, _questionCount)) : [];

                if (weakPool.length) {
                    _seen = 0;
                    _correct = 0;
                    _missed = [];
                    _mode = MODE.COUNT;
                    _queue = _shuffled(weakPool);
                    _questionCount = _queue.length;
                    _queueIndex = 0;
                    _phase = PHASE.SESSION;
                    _renderSession();
                } else {
                    _startSession();
                }
            } else {
                if (options && options.track) _track = options.track;
                _renderSettings();
            }
        } else if (_phase === PHASE.SESSION) {
            _renderSession();
        } else {
            _renderResults();
        }
    }

    // Called when the learner leaves this driller mid-session via the main
    // nav rather than its own "change settings"/finish controls — without
    // this, a Timed-mode session's setInterval keeps ticking forever
    // against a container that's already been torn down. Idempotent: safe
    // to call even when no timer is running.
    function stop() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
    }

    return {
        render, stop,
        // Expose for unit testing and headless verification
        _buildPoolFromWords, _buildExerciseFor, _buildDirectDefinition, _buildReverseChoice, _buildReverseRecall,
        _getOccurrences, _hasContext, _buildContextIndex, _load, _secondTrack, _wordList
    };
})();

if (typeof window !== 'undefined') {
    window.VocabularyDriller = VocabularyDriller;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = VocabularyDriller;
}
