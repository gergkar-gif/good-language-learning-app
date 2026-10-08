// ============================================
// EXERCISE AUDIO — what an exercise says aloud once it's settled
// ============================================
// A learner should always hear the right target-language form, not only see
// it (ROADMAP 122). This module only decides *what text* to speak for an
// exercise; engine/lessons.js decides *when* (once the step is solved or
// revealed — never before, so audio can't give the answer away) and plays it
// through ParlourTTS.
//
// Pure functions, no DOM: scripts/audit-exercise-audio.js runs the same code
// over every exercise in Node so the output can be skimmed before shipping.
//
// Returning '' means "say nothing". That is the safe failure: silence is
// fine, an English gloss read in a Spanish voice is not. So text is only
// spoken when it can be positively identified as target language.

const ExerciseAudio = (function () {
    'use strict';

    // Words that only occur in English prompts and glosses. Kept free of
    // anything that is also a common Spanish or Hungarian word ("me", "no",
    // "he", "has", "is", "be", "a", "el") so the two scores below never count
    // one token for both sides.
    const ENGLISH = new Set(('the an to are was were of and in on at for with my your his her its ' +
        'it i you she we they do does did not this that have what which who how why ' +
        'mean means meaning word sentence correct will would can could should there their ' +
        'from by or but if than then them these those our us am been being very only because').split(' '));

    const TARGET = {
        es: {
            marks: /[áéíóúñü¿¡]/i,
            words: new Set(('el la los las un una unos unas de del al que y en es son está están me te se nos ' +
                'lo le les mi mis tu tus su sus por para con muy yo tú él ella ellos ellas hay ser estar soy ' +
                'eres somos tengo tiene quiero voy va vamos hace pero también cuando donde como porque ' +
                'este esta estos estas ese esa aquí allí ya sí').split(' '))
        },
        hu: {
            marks: /[áéíóöőúüű]/i,
            words: new Set(('az egy és nem van vagyok vagy vagyunk hogy meg ki fel ez azt ami mi én ő ' +
                'nagyon már még csak de ha akkor itt ott nincs kell lehet volt lesz igen szeretnék kérek ' +
                'köszönöm jó').split(' '))
        }
    };

    function family(lang) {
        const code = String(lang || (typeof Lang !== 'undefined' ? Lang.code() : 'es')).toLowerCase();
        return code.split('-')[0];
    }

    function tokens(text) {
        return String(text || '').toLowerCase().match(/[\p{L}']+/gu) || [];
    }

    // Quoted spans, in the order they appear: "«paciente»", "'konyha'",
    // "**grande**", "*acostarse*". Used both to find the target word an
    // English prompt is asking about, and to discount quoted words when
    // judging a sentence's language — "Because 'kedvéért' occupies the focus
    // slot" is English.
    const QUOTE = /\*\*?([^*]+)\*\*?|["“«„]([^"”»“]+)["”»“]|(?:^|[\s(])['‘]([^'’]+)['’](?=$|[\s.,;:?!)])/g;

    function quotedSpans(text) {
        const out = [];
        String(text || '').replace(QUOTE, (m, a, b, c) => { out.push((a || b || c).trim()); return m; });
        return out;
    }

    function score(text, lang) {
        const t = TARGET[family(lang)];
        let target = 0, english = 0;
        tokens(String(text || '').replace(QUOTE, ' ')).forEach(w => {
            if (t.words.has(w) || t.marks.test(w)) target++;
            if (ENGLISH.has(w)) english++;
        });
        return { target, english };
    }

    // Positive evidence only: more target-language signal (accented letters,
    // function words) than English signal. A tie is neither.
    function looksTarget(text, lang) {
        const s = score(text, lang);
        return s.target > s.english;
    }

    function looksEnglish(text, lang) {
        const s = score(text, lang);
        return s.english > s.target;
    }

    // Glosses, hints and markdown never belong in the audio: "[We need a
    // solution.]", "(solución)", "(iskola + from)", "**bold**".
    // Speech.sayable() also drops (...) at playback; doing it here too keeps
    // the audit output honest.
    function stripAsides(text) {
        return String(text || '')
            .replace(/\[[^\]]*\]/g, ' ')
            .replace(/\([^)]*\)/g, ' ')
            .replace(/\*+/g, '')
            .replace(/\s+([,.;:!?])/g, '$1')
            .replace(/\s+/g, ' ')
            .trim();
    }

    const BLANK = /_{2,}/g;

    // Drops an English instruction in front of the sentence itself:
    // "Complete the greeting: Buenos ___." -> "Buenos ___.". Only segments
    // that read as English are dropped, so a target-language "Nota: ..." stays.
    function dropLeadIn(text, lang) {
        const parts = String(text || '').split(/:\s+/);
        let i = 0;
        while (i < parts.length - 1 && looksEnglish(parts[i], lang) && !/_{2,}/.test(parts[i])) i++;
        return parts.slice(i).join(': ').replace(/\s+\/\s+/g, ' ');
    }

    // The sentence with its blank filled in. Fills a suffix blank in place
    // ("alkotmányunk_____" + "ban" -> "alkotmányunkban"). Two blanks with one
    // answer can't be completed, so those stay silent, and so does a
    // completed sentence that is still mostly English.
    function fillBlank(sentence, answer, lang) {
        const s = dropLeadIn(sentence, lang);
        const blanks = s.match(BLANK) || [];
        if (blanks.length !== 1 || !String(answer || '').trim()) return '';
        const full = stripAsides(s.replace(BLANK, String(answer).trim()).replace(/:\s*$/, '.'));
        return looksEnglish(full, lang) ? '' : full;
    }

    // Prompts whose options are target-language forms even when an option
    // on its own is a bare word with no telltale accent ("emelet", "olvas").
    const OPTIONS_ARE_TARGET = /\bwhich\b|choose|how do you say|c[oó]mo se dice|translate|complete|cu[aá]l|qu[eé] forma|melyik|v[aá]laszd/i;
    // Prompts asking what a target word means — the options are English.
    const OPTIONS_ARE_ENGLISH = /what does|what is|qu[eé] significa|mit jelent|meaning of|in english|en ingl[eé]s/i;

    // The target word an English-answer prompt asks about:
    // "¿Qué significa «paciente»?" -> "paciente".
    function askedWord(question, option, lang) {
        const word = stripAsides(quotedSpans(question)[0] || '');
        if (!word || looksEnglish(word, lang)) return '';
        return word.toLowerCase() === String(option).toLowerCase() ? '' : word;
    }

    // What to say once a choice exercise is settled, given the question and
    // the correct option's text (gloss already split off).
    function forChoice(question, option, lang) {
        const q = String(question || '');
        const opt = stripAsides(option);
        // A bare suffix ("-ban/-ben", "-emos") isn't a word: TTS reads it
        // badly or not at all.
        if (!opt || /^-/.test(opt)) return '';

        // A blank in the question: say the completed sentence. If the blank
        // sits inside a quote ("You answer: "__ de mi casa.""), only that
        // quote is completed. An English option never fills a blank.
        if ((q.match(BLANK) || []).length === 1 && !looksEnglish(opt, lang)) {
            const inner = quotedSpans(q).find(span => /_{2,}/.test(span));
            const full = fillBlank(inner || q, opt, lang);
            return full || opt;
        }

        if (looksEnglish(opt, lang)) return OPTIONS_ARE_ENGLISH.test(q) ? askedWord(q, opt, lang) : '';
        if (looksTarget(opt, lang)) return opt;
        if (OPTIONS_ARE_ENGLISH.test(q)) return askedWord(q, opt, lang);

        // No signal either way (a bare "emelet", "Buenas noches"): a one- or
        // two-word answer to a "which / choose" prompt, or to a question
        // asked in the target language, is a target-language form. Longer
        // unmarked options could be English sentences, so they stay silent.
        const short = tokens(opt).length <= 2;
        if (short && (OPTIONS_ARE_TARGET.test(q) || looksTarget(q, lang))) return opt;
        return '';
    }

    return { fillBlank, forChoice, looksTarget, looksEnglish, stripAsides, quotedSpans };
})();

if (typeof module !== 'undefined' && module.exports) module.exports = ExerciseAudio;
