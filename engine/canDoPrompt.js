// ============================================
// CAN-DO PROMPT & SCAFFOLDING ENGINE
// ============================================
// Transforms CEFR Can-Do descriptors (meta-goals like "I can name all twelve months...")
// into active, natural, learner-ready communicative prompts with role, setting, and scaffolding cues.
// Universal for Spanish, Hungarian, and any Parlour language.

(function (root, factory) {
    const exp = factory();
    if (typeof define === 'function' && define.amd) {
        define([], () => exp);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = exp;
    }
    if (root) {
        root.CanDoPrompt = exp;
    }
    if (typeof global !== 'undefined') {
        global.CanDoPrompt = exp;
    }
})(typeof self !== 'undefined' ? self : (typeof window !== 'undefined' ? window : this), function () {
    'use strict';

    /**
     * Clean raw descriptor string: trim, remove leading "I can", "i can", "Can you", trailing punctuation.
     */
    function cleanRawText(text) {
        if (!text) return '';
        return String(text)
            .trim()
            .replace(/^I can\s+/i, '')
            .replace(/^Can you\s+/i, '')
            .replace(/\.+$/, '')
            .trim();
    }

    /**
     * Derives a crisp, human-readable card/prompt title without ugly mid-word truncation.
     */
    function extractCleanTitle(rawText) {
        const text = cleanRawText(rawText);
        if (!text) return 'Production Practice';

        // Known high-frequency topic patterns
        const lower = text.toLowerCase();
        if (lower.includes('café') || lower.includes('cafe')) return 'At the Café';
        if (lower.includes('twelve months') || lower.includes('12 months') || lower.includes('months')) return 'Months of the Year';
        if (lower.includes('days of the week') || lower.includes('days')) return 'Days of the Week';
        if (lower.includes('this week') || lower.includes('last week') || lower.includes('next week')) return 'Time: Weeks & Days';
        if (lower.includes('restaurant') || lower.includes('dining')) return 'At the Restaurant';
        if (lower.includes('directions') || lower.includes('way in town')) return 'Asking for Directions';
        if (lower.includes('daily routine') || lower.includes('routine')) return 'Daily Routine';
        if (lower.includes('greet') || lower.includes('hello')) return 'Greetings & Introductions';
        if (lower.includes('family')) return 'Family & Friends';
        if (lower.includes('count') || lower.includes('numbers')) return 'Numbers & Counting';
        if (lower.includes('weather')) return 'The Weather';
        if (lower.includes('hotel') || lower.includes('check-in')) return 'At the Hotel';
        if (lower.includes('shopping') || lower.includes('store') || lower.includes('market') || lower.includes('clothes')) return 'Shopping & Market';

        // If short enough, title-case the cleaned text
        if (text.length <= 32) {
            return text.charAt(0).toUpperCase() + text.slice(1);
        }

        // Extract head clause before connectors: "and say", "and ask", "in order to"
        const connectorMatch = text.match(/^(.*?\b(?:and say|and ask|and describe|in order to|when)\b)/i);
        if (connectorMatch && connectorMatch[1].length < 32) {
            const head = connectorMatch[1].replace(/\b(?:and say|and ask|and describe|in order to|when)\b.*$/i, '').trim();
            if (head.length > 5 && head.length <= 30) {
                return head.charAt(0).toUpperCase() + head.slice(1);
            }
        }

        // Clean cut on word boundary around 28-32 chars
        const words = text.split(/\s+/);
        let title = '';
        for (const w of words) {
            if ((title + ' ' + w).trim().length > 30) break;
            title = (title + ' ' + w).trim();
        }
        if (title.length >= 8) {
            return title.charAt(0).toUpperCase() + title.slice(1);
        }

        return 'Communicative Task';
    }

    /**
     * Formats a raw Can-Do descriptor into an active, scaffolded communicative task.
     *
     * @param {string} canDoText Raw statement (e.g. "I can name all twelve months and say which month something is in.")
     * @param {object} options
     *   - language: e.g. 'Hungarian', 'Spanish' (or Lang.name())
     *   - langCode: e.g. 'hu', 'es'
     *   - modality: 'oral' | 'written'
     *   - level: 'A1', 'A2', etc.
     * @returns {object} { type, title, scenario, prompt, cues, canDo }
     */
    function formatPrompt(canDoText, options) {
        const opts = options || {};
        const langName = opts.language || (typeof Lang !== 'undefined' ? Lang.name() : 'the target language');
        const langCode = (opts.langCode || (typeof Lang !== 'undefined' ? Lang.code() : 'es')).toLowerCase();
        const isOral = opts.modality !== 'written';
        const cleaned = cleanRawText(canDoText);
        const lower = (canDoText || '').toLowerCase();
        const title = extractCleanTitle(canDoText);

        // -------------------------------------------------------------
        // TYPOLOGY 1: ENUMERATION & INVENTORY (months, days, numbers, colors, lists)
        // -------------------------------------------------------------
        const isMonths = lower.includes('month');
        const isDays = lower.includes('day') && (lower.includes('week') || lower.includes('name'));
        const isNumbers = lower.includes('count') || lower.includes('number');

        if (isMonths) {
            const hasSayWhich = lower.includes('which month') || lower.includes('say which');
            const cues = (langCode === 'hu') ? [
                'Recite the months in order (január, február, március...)',
                hasSayWhich ? 'State when an event or your birthday is using -ban / -ben (e.g. "Októberben..." or "Decemberben...")' : 'Say your favorite month'
            ] : [
                'Recite the months in order (enero, febrero, marzo...)',
                hasSayWhich ? 'State when an event or your birthday is using "en" (e.g. "En octubre..." or "En diciembre...")' : 'Say your favorite month'
            ];

            return {
                type: 'enumeration',
                title: title,
                scenario: `Practicing the calendar and time expressions in ${langName}.`,
                prompt: hasSayWhich
                    ? `Say the months of the year in ${langName}, and then state which month your birthday (or an important event) is in.`
                    : `Name the months of the year in ${langName} in order.`,
                cues: cues,
                canDo: canDoText
            };
        }

        if (isDays) {
            const cues = (langCode === 'hu') ? [
                'Say the days of the week in order (hétfő, kedd...)',
                'Say which day you have an activity or day off (e.g. hétfőn, pénteken)'
            ] : [
                'Say the days of the week in order (lunes, martes...)',
                'Say which day you do an activity (e.g. los lunes, los viernes)'
            ];

            return {
                type: 'enumeration',
                title: title,
                scenario: `Practicing weekly schedules and days in ${langName}.`,
                prompt: `Say the days of the week in ${langName}, and state what day you study or work.`,
                cues: cues,
                canDo: canDoText
            };
        }

        if (isNumbers) {
            return {
                type: 'enumeration',
                title: title,
                scenario: `Practicing numbers in ${langName}.`,
                prompt: isOral
                    ? `Count out loud in ${langName}, or state numbers relevant to your everyday life (such as your age, address, or phone number).`
                    : `Write numbers in words in ${langName}, stating your age or simple quantities.`,
                cues: [
                    'Speak the numbers clearly and in correct order',
                    'Use them in a short sentence if possible'
                ],
                canDo: canDoText
            };
        }

        // -------------------------------------------------------------
        // TYPOLOGY 2: SITUATIONAL & TRANSACTIONAL (café, restaurant, shop, directions, ticket)
        // -------------------------------------------------------------
        const isCafe = lower.includes('café') || lower.includes('cafe') || lower.includes('coffee');
        const isRestaurant = lower.includes('restaurant') || lower.includes('meal') || lower.includes('order food') || lower.includes('table');
        const isDirections = lower.includes('direction') || lower.includes('way in town') || lower.includes('where');
        const isShopping = lower.includes('shop') || lower.includes('store') || lower.includes('market') || lower.includes('buy');

        if (isCafe) {
            const cues = (langCode === 'hu') ? [
                'Polite greeting (Jó napot / Szia)',
                'Order a drink or snack (e.g. "Kérek egy kávét és egy tejet")',
                'Conclude politely or ask for the bill ("Kérem a számlát" / "Köszönöm")'
            ] : [
                'Polite greeting (Hola / Buenas tardes)',
                'Order a drink or snack (e.g. "Un café con leche, por favor")',
                'Conclude politely or ask for the bill ("La cuenta, por favor" / "Muchas gracias")'
            ];

            return {
                type: 'transaction',
                title: title,
                scenario: `You are at a café in ${langName === 'Hungarian' ? 'Budapest' : langName === 'Spanish' ? 'Madrid' : 'town'}.`,
                prompt: isOral
                    ? `Order at the café: greet the server, ask politely for a drink and a pastry, and ask for the bill.`
                    : `Write a short interaction at the café: greet the server, order your drink, and ask for the bill.`,
                cues: cues,
                canDo: canDoText
            };
        }

        if (isRestaurant) {
            const cues = (langCode === 'hu') ? [
                'Greeting and ask for a table or menu',
                'Order food and drink politely ("Kérek egy...")',
                'Ask about the bill or thank the staff'
            ] : [
                'Greeting and request a table ("Una mesa para dos, por favor")',
                'Order food and drinks ("De primero queremos... y de segundo...")',
                'Ask for the bill ("La cuenta, por favor")'
            ];

            return {
                type: 'transaction',
                title: title,
                scenario: `You are dining at a restaurant.`,
                prompt: `Perform a dining interaction in ${langName}: greet the waiter, order your meal and drink, and ask for the check.`,
                cues: cues,
                canDo: canDoText
            };
        }

        if (isDirections) {
            const cues = (langCode === 'hu') ? [
                'Polite interruption (Elnézést / Bocsánat)',
                'Ask where a place is (e.g. "Hol van a pályaudvar?")',
                'Polite thank you (Köszönöm szépen)'
            ] : [
                'Polite opening (Disculpe / Perdón)',
                'Ask for directions (e.g. "¿Dónde está la estación de tren?")',
                'Thank the person (Muchas gracias)'
            ];

            return {
                type: 'transaction',
                title: title,
                scenario: `You are in town and need to find your way.`,
                prompt: `Ask someone on the street for directions to a station, hotel, or pharmacy politely, and thank them.`,
                cues: cues,
                canDo: canDoText
            };
        }

        if (isShopping) {
            return {
                type: 'transaction',
                title: title,
                scenario: `You are shopping in a local market or store.`,
                prompt: `Ask for an item you want to buy in ${langName}, ask about the price, and complete the purchase.`,
                cues: [
                    'Polite greeting & state what item you want',
                    'Ask how much it costs',
                    'Pay and say thank you'
                ],
                canDo: canDoText
            };
        }

        // -------------------------------------------------------------
        // TYPOLOGY 3: PERSONAL MONOLOGUE & DAILY LIFE
        // -------------------------------------------------------------
        const isRoutine = lower.includes('routine') || lower.includes('daily');
        const isFamily = lower.includes('family') || lower.includes('relative');
        const isHobbies = lower.includes('hobby') || lower.includes('free time') || lower.includes('weekend');
        const isHomeCity = lower.includes('where i live') || lower.includes('my house') || lower.includes('my town') || lower.includes('my city') || lower.includes('apartment');

        if (isRoutine) {
            return {
                type: 'monologue',
                title: title,
                scenario: `Describing your daily life to a friend in ${langName}.`,
                prompt: `Describe your typical morning or daily routine in ${langName} in 2–3 connected sentences.`,
                cues: [
                    'What time you wake up or get started',
                    'Key activities (breakfast, work, commute)',
                    'How your day finishes'
                ],
                canDo: canDoText
            };
        }

        if (isFamily) {
            return {
                type: 'monologue',
                title: title,
                scenario: `Talking about the people close to you.`,
                prompt: `Talk about your family or friends in ${langName}: mention 2–3 people, their names, and what they do.`,
                cues: [
                    'Introduce family members (brother, sister, parents...)',
                    'Share their names and a detail about each'
                ],
                canDo: canDoText
            };
        }

        if (isHobbies) {
            return {
                type: 'monologue',
                title: title,
                scenario: `Talking about your interests and leisure time.`,
                prompt: `Say what you like to do in your free time or on weekends in ${langName}.`,
                cues: [
                    'Mention 1–2 activities you enjoy',
                    'Say when or how often you do them'
                ],
                canDo: canDoText
            };
        }

        if (isHomeCity) {
            return {
                type: 'monologue',
                title: title,
                scenario: `Describing your surroundings.`,
                prompt: `Describe where you live (your home or town) in ${langName} in 2–3 sentences.`,
                cues: [
                    'State where you live',
                    'Describe 1–2 features (quiet, lively, small, big)'
                ],
                canDo: canDoText
            };
        }

        // -------------------------------------------------------------
        // TYPOLOGY 4: FUNCTIONAL & GRAMMATICAL (Fallback)
        // -------------------------------------------------------------
        let action = cleaned;
        if (/^say\b/i.test(action)) action = action.replace(/^say\b/i, 'Say');
        else if (/^ask\b/i.test(action)) action = action.replace(/^ask\b/i, 'Ask');
        else if (/^use\b/i.test(action)) action = action.replace(/^use\b/i, 'Use');
        else if (/^express\b/i.test(action)) action = action.replace(/^express\b/i, 'Express');
        else if (/^introduce\b/i.test(action)) action = action.replace(/^introduce\b/i, 'Introduce');
        else if (/^describe\b/i.test(action)) action = action.replace(/^describe\b/i, 'Describe');
        else if (/^talk\b/i.test(action)) action = action.replace(/^talk\b/i, 'Talk');
        else if (/^give\b/i.test(action)) action = action.replace(/^give\b/i, 'Give');
        else if (/^complete\b/i.test(action)) action = action.replace(/^complete\b/i, 'Complete');
        else action = action.charAt(0).toUpperCase() + action.slice(1);

        const parts = cleaned.split(/\band\s+/i);
        const cues = parts.length > 1 ? [
            parts[0].charAt(0).toUpperCase() + parts[0].slice(1),
            parts[1].charAt(0).toUpperCase() + parts[1].slice(1)
        ] : [
            'Express the idea clearly and naturally',
            `Use the structures and vocabulary you learned in ${langName}`
        ];

        return {
            type: 'functional',
            title: title,
            scenario: `Put your ${langName} skills into practice for this goal.`,
            prompt: isOral
                ? `In ${langName}, ${action.charAt(0).toLowerCase() + action.slice(1)}. Speak clearly and naturally.`
                : `In ${langName}, ${action.charAt(0).toLowerCase() + action.slice(1)}. Write clearly and naturally.`,
            cues: cues,
            canDo: canDoText
        };
    }

    return {
        cleanRawText,
        extractCleanTitle,
        formatPrompt
    };
});
