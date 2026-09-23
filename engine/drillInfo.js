// ============================================
// DRILL INFO POPUP
// ============================================
// A small "About this drill" affordance for every Workshop driller's
// settings screen: what the exercise actually trains, why it can feel odd
// at first, and what getting better at it looks like — the thing a learner
// has no way to ask before committing to a session. One shared closeable
// bottom sheet (the same .wp-overlay/.wp-sheet/.wp-header/.wp-close
// component engine/guide.js's "How Parlour Works" modal and the Reader's
// word-tap popup already use — see styles/components.css), keyed by driller
// id so the copy lives in one place instead of duplicated across a dozen
// settings-screen templates.

const DrillInfo = (function () {
    'use strict';

    // Plain, second-person, sets expectations rather than describing UI.
    // Each entry: what this trains, why it might feel strange at first,
    // what "getting better" actually looks like — not a feature list.
    const COPY = {
        'hu-verb': {
            title: 'About the Verb Driller',
            body: [
                "This trains the ending, not the verb. You'll often be asked to conjugate a verb you don't recognise — that's on purpose. Once you know the pattern for a person (-ok/-asz/-ik...), you can build the right form for almost any verb, familiar or not.",
                "It can feel like guessing at first. With practice, your ear starts to catch what \"sounds right\" before you consciously work out the rule — that instinct is the actual goal, not memorising every verb."
            ]
        },
        'hu-suffix': {
            title: 'About the Suffix Driller',
            body: [
                "Hungarian builds meaning by stacking endings onto a word — plural, \"my/your/our\", and case (\"into\", \"from\", \"at\"...) — rather than using separate little words the way English does.",
                "This drills those endings directly, often on words you haven't met yet. The lemma and its meaning are always given; your job is just the ending. Case in particular can run ahead of what your lessons have covered — pick a narrower type below if you'd rather stay close to what you've been taught."
            ]
        },
        'hu-prefix': {
            title: 'About the Prefix Driller',
            body: [
                "Hungarian verbs often pair with a short prefix (meg-, el-, ki-, be-...) that shifts or sharpens their meaning — closer to English phrasal verbs (\"look up\" vs \"look into\") than to a grammar rule with a clean formula.",
                "There's no shortcut here but exposure: every pair drilled is a real, attested word, not a guess — the more you see, the more a prefix's \"flavor\" starts to feel familiar rather than arbitrary."
            ]
        },
        'hu-morphology': {
            title: 'About the Morphology Driller',
            body: [
                "Hungarian words can carry several endings stacked in a row — plural, then case, then more — and this drills pulling a long word apart (or building one up) piece by piece, the same breakdown the Reader's tap-to-translate popup already shows you.",
                "Reading a dense word by peeling off its endings one at a time is a real skill on its own, separate from knowing any single ending in isolation — this is where that skill gets built."
            ]
        },
        verbs: {
            title: 'About the Verb Driller',
            body: [
                "Table mode shows a full conjugation to study; Speed mode tests you against the clock on individual forms.",
                "The goal isn't memorising a giant list of endings — it's pattern recognition. The more forms you produce, the faster a conjugation starts to feel automatic instead of something you have to work out each time."
            ]
        },
        grammar: {
            title: 'About the Grammar Driller',
            body: [
                "This pulls questions from every grammar point your lessons have actually covered, weighted toward whatever you've been getting wrong — it's spaced review, not new material.",
                "If a question catches you out, that's the point: it means it's worth another pass before it's forgotten for good."
            ]
        },
        vocabulary: {
            title: 'About the Vocabulary Driller',
            body: [
                "Rather than bare flashcard recall, every question here tests a word inside a real sentence — you have to use the surrounding context to work out or confirm the meaning, the same way you'd meet it in actual reading.",
                "That makes it harder than a simple \"what does this mean\" quiz on purpose: recognising a word in context is the skill that actually transfers to reading and conversation."
            ]
        },
        translation: {
            title: 'About the Translation Driller',
            body: [
                "Short sentences, alternating direction — sometimes into the language you're learning, sometimes out of it — scaled to your current level.",
                "Translating on the clock forces you past careful, word-by-word thinking into faster, more automatic recall. Don't worry about a perfectly polished answer — the goal is speed and reasonable accuracy, not elegance."
            ]
        },
        listening: {
            title: 'About the Listening Driller',
            body: [
                "Short audio clips, decoded by ear alone — no text to lean on while you listen.",
                "This is deliberately uncomfortable at first: understanding a written sentence and understanding the same sentence spoken at natural speed are genuinely different skills. This one only gets built through repetition."
            ]
        },
        speaking: {
            title: 'About the Speaking Studio',
            body: [
                "Say sentences out loud rather than typing them — production, not recognition. You can shadow a native recording, respond to a prompt, or work through an open-ended scenario.",
                "Speaking a language and reading it use different mental muscles — this is the one place in the app dedicated to building the first."
            ]
        },
        writing: {
            title: 'About the Writing Studio',
            body: [
                "Open-ended composition, from single sentences up to short exchanges, graded against CEFR expectations for your level rather than a single fixed \"correct answer.\"",
                "This is where you get to be imprecise and find out what happens — the grading is there to catch real mistakes, not to demand a textbook-perfect response."
            ]
        }
    };

    function _escapeHtml(text) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(text)
            : String(text == null ? '' : text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
    }

    function close() {
        const existing = document.getElementById('drill-info-overlay');
        if (existing && existing.parentNode) existing.parentNode.removeChild(existing);
    }

    function open(id) {
        const entry = COPY[id];
        if (!entry) return;
        close();

        const overlay = document.createElement('div');
        overlay.id = 'drill-info-overlay';
        overlay.className = 'wp-overlay';
        overlay.innerHTML = `
            <div class="wp-sheet di-sheet" role="dialog" aria-modal="true" aria-labelledby="drill-info-title">
                <div class="wp-header">
                    <h2 id="drill-info-title" class="di-title">${_escapeHtml(entry.title)}</h2>
                    <button class="wp-close" data-drill-info-close="1" aria-label="Close">&times;</button>
                </div>
                <div class="di-body">
                    ${entry.body.map(p => `<p class="di-p">${_escapeHtml(p)}</p>`).join('')}
                </div>
            </div>
        `;
        document.body.appendChild(overlay);

        overlay.querySelectorAll('[data-drill-info-close]').forEach(btn => {
            btn.addEventListener('click', close);
        });
        overlay.addEventListener('click', e => {
            if (e.target === overlay) close();
        });

        function _onEsc(e) {
            if (e.key === 'Escape') {
                close();
                document.removeEventListener('keydown', _onEsc);
            }
        }
        document.addEventListener('keydown', _onEsc);
    }

    // A ready-to-drop "About this drill" link for a settings-screen title
    // row. Callers insert this HTML next to their own <h2 class="gd-title">
    // (or equivalent) and call attach(container) alongside their other
    // event wiring — same pattern every other data-action button in these
    // screens already follows. Returns '' for an id with no copy, so a
    // caller can splice it in unconditionally without an extra guard.
    function buttonHtml(id) {
        if (!COPY[id]) return '';
        return `<button type="button" class="di-info-btn" data-drill-info="${id}">ⓘ About this drill</button>`;
    }

    function attach(root) {
        if (!root) return;
        root.querySelectorAll('[data-drill-info]').forEach(btn => {
            btn.addEventListener('click', () => open(btn.getAttribute('data-drill-info')));
        });
    }

    return { open, close, buttonHtml, attach };
})();

if (typeof window !== 'undefined') {
    window.DrillInfo = DrillInfo;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DrillInfo;
}
