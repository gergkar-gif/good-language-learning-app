// ============================================
// MUSIC STUDIO (Learn from Music)
// ============================================
// Workshop Studio for song lyrics reading, vocabulary inspection,
// and aural Cloze exercises.
//
// Tabs:
// 1. Easy: continuous stanzas with inline roll-down <select> blanks.
// 2. Hard: continuous stanzas with typed inline <input> blanks.
// 3. Understand the lyrics: full unredacted poetry with line translations,
//    inline grammatical/cultural notes, and tap-to-inspect Lexicon popups.

const MusicDriller = (function () {
    'use strict';

    let _container = null;
    let _songs = [];
    let _currentSongId = null;
    let _activeMode = 'easy'; // 'easy' | 'hard' | 'understand'
    let _showTranslations = false;
    let _activeWord = null;
    let _activeDefinition = null;
    let _activePos = null;

    // Built-in fallback songs in case of offline / test environments
    const _FALLBACK_SONGS = [
        {
            id: "bonito",
            title: "Bonito",
            artist: "Jarabe de Palo",
            youtubeId: "xxhET61yB1A",
            level: "A2",
            stanzas: [
                {
                    lines: [
                        {
                            text: "Bonito, todo me [parece] bonito",
                            english: "Beautiful, everything seems beautiful to me",
                            options: ["parece", "aparece", "merece", "carece"],
                            note: "parecer: In Spanish, 'parecer' operates like 'gustar' (me parece = 'it seems to me')."
                        },
                        {
                            text: "Bonita mañana",
                            english: "Beautiful morning"
                        },
                        {
                            text: "Bonito [lugar]",
                            english: "Beautiful place",
                            options: ["lugar", "hogar", "mar", "viajar"]
                        },
                        {
                            text: "Bonita la cama",
                            english: "Beautiful the bed"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Qué bien se [ve] el mar",
                            english: "How good the sea looks",
                            options: ["ve", "va", "da", "sé"]
                        },
                        {
                            text: "Bonito es el día",
                            english: "Beautiful is the day"
                        },
                        {
                            text: "Y [acaba] de empezar",
                            english: "And it has just begun",
                            options: ["acaba", "empieza", "trata", "deja"],
                            note: "acabar de + infinitive: Expresses having just done something ('acaba de empezar' = has just begun)."
                        },
                        {
                            text: "Bonita la vida",
                            english: "Beautiful life"
                        },
                        {
                            text: "Respira, respira, respira",
                            english: "Breathe, breathe, breathe"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "El teléfono suena, mi [pana] se queja",
                            english: "The phone is ringing, my pal complains",
                            options: ["pana", "cama", "semana", "mañana"],
                            note: "pana: Colloquial Latin American / Caribbean Spanish for 'buddy' or 'close pal'."
                        },
                        {
                            text: "La cosa va mal, la vida le [pesa]",
                            english: "Things are going badly, life weighs on him",
                            options: ["pesa", "pasa", "deja", "queda"]
                        },
                        {
                            text: "Que vivir así ya no le [interesa]",
                            english: "Living like this no longer interests him",
                            options: ["interesa", "importa", "molesta", "conviene"]
                        },
                        {
                            text: "Que seguir así no [vale] la pena",
                            english: "That continuing like this is not worth it",
                            options: ["vale", "sirve", "cuesta", "cuenta"],
                            note: "valer la pena: Idiomatic expression meaning 'to be worth the effort / trouble'."
                        },
                        {
                            text: "Se perdió el amor, se [acabó] la fiesta",
                            english: "Love was lost, the party is over",
                            options: ["acabó", "pasó", "quedó", "dejó"]
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Ya no anda el [motor] que empuja la tierra",
                            english: "The engine that pushes the earth no longer runs",
                            options: ["motor", "barco", "sol", "tren"]
                        },
                        {
                            text: "La vida es un [chiste] con triste final",
                            english: "Life is a joke with a sad ending",
                            options: ["chiste", "sueño", "cuento", "juego"]
                        },
                        {
                            text: "El futuro no existe, pero yo le [digo]",
                            english: "The future does not exist, but I tell him",
                            options: ["digo", "hago", "pido", "veo"]
                        },
                        {
                            text: "Bonito, todo me parece bonito",
                            english: "Beautiful, everything seems beautiful to me"
                        },
                        {
                            text: "Bonito, todo me parece bonito",
                            english: "Beautiful, everything seems beautiful to me"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Bonita la [paz], bonita la vida",
                            english: "Beautiful peace, beautiful life",
                            options: ["paz", "mar", "luz", "voz"]
                        },
                        {
                            text: "Bonito volver a [nacer] cada día",
                            english: "Beautiful to be born again every day",
                            options: ["nacer", "hacer", "tener", "crecer"],
                            note: "volver a + infinitive: Expresses doing an action again ('volver a nacer' = to be born anew)."
                        },
                        {
                            text: "Bonita la [verdad] cuando no suena a mentira",
                            english: "Beautiful truth when it doesn't sound like a lie",
                            options: ["verdad", "realidad", "palabra", "noticia"]
                        },
                        {
                            text: "Bonita la [amistad], bonita la risa",
                            english: "Beautiful friendship, beautiful laughter",
                            options: ["amistad", "verdad", "ciudad", "bondad"]
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Bonita la [gente] cuando hay calidad",
                            english: "Beautiful people when there is quality",
                            options: ["gente", "tarde", "noche", "fiesta"]
                        },
                        {
                            text: "Bonita la gente que no se [arrepiente]",
                            english: "Beautiful the people who don't regret",
                            options: ["arrepiente", "siente", "entiende", "detiene"],
                            note: "arrepentirse: Reflexive verb meaning 'to regret' (no se arrepiente = they don't regret)."
                        },
                        {
                            text: "Que gana y que [pierde], que habla y no miente",
                            english: "Who wins and who loses, who speaks and doesn't lie",
                            options: ["pierde", "puede", "quiere", "sabe"]
                        },
                        {
                            text: "Bonita la gente, por eso yo digo",
                            english: "Beautiful people, that's why I say"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Bonito, todo me parece bonito",
                            english: "Beautiful, everything seems beautiful to me"
                        },
                        {
                            text: "Qué bonito que te va cuando te va bonito",
                            english: "How nice it goes for you when it goes nicely",
                            note: "irle bonito: Impersonal expression for how things are turning out for someone (te va bonito = things are going nicely for you)."
                        },
                        {
                            text: "Qué bonito que te va cuando todo va bien",
                            english: "How nice it goes for you when everything goes well"
                        }
                    ]
                }
            ]
        },
        {
            id: "me-gustas-tu",
            title: "Me Gustas Tú",
            artist: "Manu Chao",
            youtubeId: "rs6Y4kZ8qtw",
            level: "A1",
            stanzas: [
                {
                    lines: [
                        {
                            text: "¿Qué horas son, mi [corazón]?",
                            english: "What time is it, my sweetheart?",
                            options: ["corazón", "canción", "razón", "ilusión"],
                            note: "¿qué horas son?: Plural colloquial idiom for 'what time is it?' common across Latin America (standard: ¿qué hora es?)."
                        },
                        {
                            text: "Te lo dije bien clarito",
                            english: "I told you very clearly",
                            note: "clarito: Diminutive of 'claro' (-ito suffix softening and adding affection/emphasis)."
                        },
                        {
                            text: "Permanece a la escucha",
                            english: "Stay tuned / keep listening",
                            note: "a la escucha: Radio broadcasting jargon meaning 'listening in / stay tuned'."
                        },
                        {
                            text: "Doce de la noche en La Habana, Cuba",
                            english: "Midnight in Havana, Cuba"
                        },
                        {
                            text: "Once de la noche en San Salvador, El Salvador",
                            english: "11 PM in San Salvador"
                        },
                        {
                            text: "Diez de la noche en Managua, Nicaragua",
                            english: "10 PM in Managua"
                        },
                        {
                            text: "Me gustas tú",
                            english: "I like you (You please me)"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Me [gustan] los aviones, me gustas tú",
                            english: "I like airplanes, I like you",
                            options: ["gustan", "gusta", "gusto", "gustas"],
                            note: "gustar agreement: 'Me gustan los aviones' (plural noun 'aviones' is grammatical subject) vs 'me gustas tú' (second-person singular subject)."
                        },
                        {
                            text: "Me gusta [viajar], me gustas tú",
                            english: "I like traveling, I like you",
                            options: ["viajar", "cantar", "bailar", "soñar"]
                        },
                        {
                            text: "Me gusta la [mañana], me gustas tú",
                            english: "I like the morning, I like you",
                            options: ["mañana", "noche", "tarde", "semana"]
                        },
                        {
                            text: "Me gusta el [viento], me gustas tú",
                            english: "I like the wind, I like you",
                            options: ["viento", "tiempo", "ciento", "momento"]
                        },
                        {
                            text: "Me gusta [soñar], me gustas tú",
                            english: "I like dreaming, I like you",
                            options: ["soñar", "amar", "dormir", "hablar"]
                        },
                        {
                            text: "Me gusta la mar, me gustas tú",
                            english: "I like the sea, I like you",
                            note: "la mar: Poetic feminine usage of 'el mar', traditional in seafaring folk and songs."
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "¿Qué voy a [hacer]? Je ne sais pas",
                            english: "What am I going to do? I don't know",
                            options: ["hacer", "decir", "tener", "poner"],
                            note: "Je ne sais pas: French for 'I don't know' (Manu Chao frequently blends Spanish, French, and English)."
                        },
                        {
                            text: "¿Qué voy a hacer? Je ne sais plus",
                            english: "What am I going to do? I don't know anymore",
                            note: "Je ne sais plus: French for 'I no longer know'."
                        },
                        {
                            text: "¿Qué voy a hacer? Je suis perdu",
                            english: "What am I going to do? I am lost",
                            note: "Je suis perdu: French for 'I am lost'."
                        },
                        {
                            text: "¿Qué horas son, mi corazón?",
                            english: "What time is it, my sweetheart?"
                        }
                    ]
                },
                {
                    lines: [
                        {
                            text: "Me gusta la [moto], me gustas tú",
                            english: "I like the motorcycle, I like you",
                            options: ["moto", "foto", "auto", "bici"],
                            note: "la moto: Feminine noun, colloquial short form of 'la motocicleta'."
                        },
                        {
                            text: "Me gusta [correr], me gustas tú",
                            english: "I like running, I like you",
                            options: ["correr", "comer", "beber", "leer"]
                        },
                        {
                            text: "Me gusta la [lluvia], me gustas tú",
                            english: "I like the rain, I like you",
                            options: ["lluvia", "nieve", "luz", "playa"]
                        },
                        {
                            text: "Me gusta [volver], me gustas tú",
                            english: "I like returning, I like you",
                            options: ["volver", "tener", "hacer", "poner"]
                        },
                        {
                            text: "Me gusta la [montaña], me gustas tú",
                            english: "I like the mountain, I like you",
                            options: ["montaña", "mañana", "campaña", "cabaña"]
                        },
                        {
                            text: "Me gusta la [noche], me gustas tú",
                            english: "I like the night, I like you",
                            options: ["noche", "tarde", "calle", "gente"]
                        }
                    ]
                }
            ]
        }
    ];

    async function _loadSongs() {
        let loaded = null;
        if (typeof Content !== 'undefined' && typeof Lang !== 'undefined' && Lang.content) {
            try {
                const data = await Content.json(Lang.content('songs.json'));
                if (data && Array.isArray(data.songs) && data.songs.length) {
                    loaded = data.songs;
                }
            } catch (e) {
                // fall through
            }
        }
        if (!loaded) {
            try {
                const lang = typeof Lang !== 'undefined' ? Lang.code() : 'es-es';
                const res = await fetch(`content/${lang}/songs.json`);
                if (res.ok) {
                    const data = await res.json();
                    if (data && Array.isArray(data.songs) && data.songs.length) {
                        loaded = data.songs;
                    }
                }
            } catch (e) {
                // fall through
            }
        }
        if (!loaded) {
            const currentLang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
            loaded = currentLang.startsWith('es') ? _FALLBACK_SONGS : [];
        }
        return loaded.slice().sort((a, b) => (a.title || '').localeCompare(b.title || '', undefined, { sensitivity: 'base' }));
    }

    function _normalize(str) {
        return String(str || '')
            .trim()
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/[¿¡,.]/g, '');
    }

    function _getCurrentSong() {
        return _songs.find(s => s.id === _currentSongId) || _songs[0];
    }

    function _renderBaseHtml() {
        if (!_songs || !_songs.length) {
            return `
                <div class="wk-music-root" style="padding-top: 16px;">
                    <div class="sp-setup-head">
                        <h3 style="margin-top:0;">No songs available</h3>
                        <p class="sp-setup-desc" style="color: var(--muted);">There are no song lyrics drills available for this language yet.</p>
                    </div>
                </div>
            `;
        }
        const current = _getCurrentSong();
        const optionsHtml = _songs.map(s => `
            <option value="${s.id}" ${s.id === current.id ? 'selected' : ''}>
                ${s.title} — ${s.artist} (${s.level || 'All'}${s.origin ? ' · ' + s.origin : ''})
            </option>
        `).join('');

        return `
            <div class="wk-music-root" style="padding-top: 8px;">
                <div class="sp-setup-head" style="margin-bottom: 14px;">
                    <p class="sp-setup-desc" style="margin: 0; color: var(--muted); font-size: 0.92rem;">
                        Poetic lyrics reading and aural Cloze with authentic music. Listen to the track, complete missing phrases, or inspect vocabulary with cultural and grammatical footnotes.
                    </p>
                </div>

                <div class="wk-music-shelf">
                    <div class="wk-music-cluster">
                        <label for="wk-music-song-picker" class="wk-music-shelf-label">Song:</label>
                        <select id="wk-music-song-picker" class="wk-music-song-select">
                            ${optionsHtml}
                        </select>
                    </div>

                    <div class="wk-music-cluster">
                        <button type="button" class="wk-music-btn ${_showTranslations ? 'is-active' : ''}" id="wk-music-toggle-trans">
                            ${_showTranslations ? 'Translations: On' : 'Translations: Off'}
                        </button>
                    </div>
                </div>

                <div class="wk-music-tabs">
                    <button type="button" class="wk-music-tab ${_activeMode === 'easy' ? 'is-active' : ''}" data-mode="easy">Easy</button>
                    <button type="button" class="wk-music-tab ${_activeMode === 'hard' ? 'is-active' : ''}" data-mode="hard">Hard</button>
                    <button type="button" class="wk-music-tab ${_activeMode === 'understand' ? 'is-active' : ''}" data-mode="understand">Understand the lyrics</button>
                </div>

                <div class="wk-music-grid">
                    <aside class="wk-music-player-col">
                        <div class="wk-music-video-wrap">
                            <iframe id="wk-music-yt-iframe"
                                    src="https://www.youtube.com/embed/${current.youtubeId}?enablejsapi=1&rel=0&modestbranding=1"
                                    allow="autoplay; encrypted-media"
                                    allowfullscreen></iframe>
                        </div>

                        <div style="margin: 6px 0 10px; display: flex; justify-content: flex-end;">
                            <a id="wk-music-yt-link" href="https://www.youtube.com/watch?v=${current.youtubeId}" target="_blank" rel="noopener noreferrer" class="wk-music-yt-link" style="display: inline-flex; align-items: center; gap: 4px; font-size: 0.8rem; color: var(--primary); text-decoration: none; opacity: 0.85;">
                                Open on YouTube ↗
                            </a>
                        </div>

                        <div class="wk-music-status-card">
                            <span id="wk-music-status-mode-label">Easy Mode</span>
                            <span class="wk-music-badge" id="wk-music-score-readout">0 answered</span>
                        </div>

                        <div class="wk-music-helper" id="wk-music-helper-text">
                            Play the song. Select the missing words from the roll-down choices as you hear them.
                        </div>
                    </aside>

                    <main class="wk-music-lyrics-col">
                        <div class="wk-music-lyrics-sheet" id="wk-music-lyrics-sheet">
                            <!-- Rendered by _renderSheet -->
                        </div>

                        <div class="wk-music-actions" id="wk-music-exercise-actions" style="display:flex;">
                            <button type="button" class="wk-music-btn is-active" id="wk-music-btn-check">Check All</button>
                            <button type="button" class="wk-music-btn" id="wk-music-btn-reveal">Reveal Answers</button>
                            <button type="button" class="wk-music-btn" id="wk-music-btn-reset">Reset</button>
                        </div>
                    </main>
                </div>

                <!-- Lexicon Popup -->
                <div class="wk-music-lexicon-pop" id="wk-music-lexicon-pop">
                    <div class="wk-music-pop-head">
                        <span class="wk-music-pop-lemma" id="wk-pop-lemma"></span>
                        <span class="wk-music-pop-pos" id="wk-pop-pos"></span>
                    </div>
                    <div class="wk-music-pop-def" id="wk-pop-def"></div>
                    <button type="button" class="wk-music-pop-btn" id="wk-pop-srs-btn">+ Add to Flashcards</button>
                </div>
            </div>
        `;
    }

    function _renderSheet() {
        const current = _getCurrentSong();
        const sheetEl = document.getElementById('wk-music-lyrics-sheet');
        if (!sheetEl) return;
        sheetEl.innerHTML = '';

        current.stanzas.forEach(stanza => {
            const stanzaEl = document.createElement('div');
            stanzaEl.className = 'wk-music-stanza';

            stanza.lines.forEach(line => {
                const lineEl = document.createElement('div');
                lineEl.className = 'wk-music-line';

                if (_activeMode === 'understand') {
                    // Full unredacted poetry, every word tappable for dictionary lookup
                    const cleanText = line.text.replace(/\[([^\]]+)\]/g, '$1');
                    if (typeof Reader !== 'undefined' && Reader.makeClickable) {
                        const verseSpan = document.createElement('span');
                        verseSpan.className = 'wk-music-line-verse';
                        verseSpan.innerHTML = Reader.makeClickable(cleanText);
                        lineEl.appendChild(verseSpan);
                    } else {
                        const words = cleanText.split(' ');
                        words.forEach((w, wIdx) => {
                            if (!w) return;
                            const span = document.createElement('span');
                            span.className = 'wk-music-word-tap word';
                            span.textContent = w;
                            const cleanWord = w.toLowerCase().replace(/[¿¡,.]/g, '');
                            span.addEventListener('click', (e) => _handleWordTap(cleanWord, e));
                            lineEl.appendChild(span);
                            if (wIdx < words.length - 1) {
                                lineEl.appendChild(document.createTextNode(' '));
                            }
                        });
                    }

                } else {
                    // Exercise Mode: Easy (Roll-down select) or Hard (Type-in input)
                    const parts = line.text.split(/(\[[^\]]+\])/);

                    parts.forEach(part => {
                        if (part.startsWith('[') && part.endsWith(']')) {
                            const targetWord = part.slice(1, -1);

                            if (_activeMode === 'easy') {
                                // Easy mode roll-down dropdown
                                const select = document.createElement('select');
                                select.className = 'wk-music-blank-select';
                                select.dataset.answer = targetWord;

                                const defOpt = document.createElement('option');
                                defOpt.value = '';
                                defOpt.textContent = '— choose —';
                                select.appendChild(defOpt);

                                const pool = line.options ? [...line.options] : [targetWord, 'otra', 'cosa', 'bien'];
                                pool.sort(() => Math.random() - 0.5);

                                pool.forEach(opt => {
                                    const optEl = document.createElement('option');
                                    optEl.value = opt;
                                    optEl.textContent = opt;
                                    select.appendChild(optEl);
                                });

                                select.addEventListener('change', () => {
                                    select.classList.remove('is-correct', 'is-wrong');
                                    _updateAnsweredCount();
                                });
                                lineEl.appendChild(select);

                            } else {
                                // Hard mode typed input
                                const input = document.createElement('input');
                                input.type = 'text';
                                input.className = 'wk-music-blank-input';
                                input.dataset.answer = targetWord;
                                input.placeholder = '____';
                                input.addEventListener('input', () => {
                                    input.classList.remove('is-correct', 'is-wrong');
                                    _updateAnsweredCount();
                                });
                                input.addEventListener('keydown', (e) => {
                                    if (e.key === 'Enter') _checkAnswers();
                                });
                                lineEl.appendChild(input);
                            }

                        } else {
                            // Non-blank words remain tappable for lexicon
                            if (typeof Reader !== 'undefined' && Reader.makeClickable) {
                                const partSpan = document.createElement('span');
                                partSpan.innerHTML = Reader.makeClickable(part);
                                lineEl.appendChild(partSpan);
                            } else {
                                const words = part.split(' ');
                                words.forEach((w, wIdx) => {
                                    if (!w) return;
                                    const span = document.createElement('span');
                                    span.className = 'wk-music-word-tap word';
                                    span.textContent = w;
                                    const cleanWord = w.toLowerCase().replace(/[¿¡,.]/g, '');
                                    span.addEventListener('click', (e) => _handleWordTap(cleanWord, e));
                                    lineEl.appendChild(span);
                                    if (wIdx < words.length - 1) {
                                        lineEl.appendChild(document.createTextNode(' '));
                                    }
                                });
                            }
                        }
                    });
                }

                // Bilingual Translation
                if (_showTranslations && line.english) {
                    const transEl = document.createElement('div');
                    transEl.className = 'wk-music-line-trans';
                    transEl.textContent = line.english;
                    lineEl.appendChild(transEl);
                }

                // Line Annotation Note (shown only in 'understand' mode directly below verse)
                if (_activeMode === 'understand' && line.note) {
                    const noteEl = document.createElement('div');
                    noteEl.className = 'wk-music-line-note';
                    noteEl.innerHTML = `<span class="wk-note-tag">Note</span> <span class="wk-note-body">${line.note}</span>`;
                    lineEl.appendChild(noteEl);
                }

                stanzaEl.appendChild(lineEl);
            });

            sheetEl.appendChild(stanzaEl);
        });

        if (_activeMode !== 'understand') {
            _updateAnsweredCount();
        }
    }

    function _switchMode(mode) {
        _activeMode = mode;
        const root = _container;
        if (!root) return;

        root.querySelectorAll('.wk-music-tab').forEach(t => {
            t.classList.toggle('is-active', t.dataset.mode === mode);
        });

        const actions = document.getElementById('wk-music-exercise-actions');
        const helper = document.getElementById('wk-music-helper-text');
        const label = document.getElementById('wk-music-status-mode-label');
        const score = document.getElementById('wk-music-score-readout');

        if (mode === 'easy') {
            if (actions) actions.style.display = 'flex';
            if (label) label.textContent = 'Easy Mode';
            if (helper) helper.textContent = 'Play the song. Select the missing words from the roll-down choices as you hear them.';
            _updateAnsweredCount();
        } else if (mode === 'hard') {
            if (actions) actions.style.display = 'flex';
            if (label) label.textContent = 'Hard Mode';
            if (helper) helper.textContent = 'Play the song. Type the missing words into the blanks as you hear them.';
            _updateAnsweredCount();
        } else {
            if (actions) actions.style.display = 'none';
            if (label) label.textContent = 'Understand the lyrics';
            if (score) score.textContent = 'Tap words to inspect';
            if (helper) helper.textContent = 'Read through full lyrics with translations and cultural notes. Tap any word to look up its definition.';
        }

        _renderSheet();
    }

    function _loadSong(songId) {
        _currentSongId = songId;
        const current = _getCurrentSong();
        const iframe = document.getElementById('wk-music-yt-iframe');
        if (iframe) {
            iframe.src = `https://www.youtube.com/embed/${current.youtubeId}?enablejsapi=1&rel=0&modestbranding=1`;
        }
        const ytLink = document.getElementById('wk-music-yt-link');
        if (ytLink) {
            ytLink.href = `https://www.youtube.com/watch?v=${current.youtubeId}`;
        }
        _renderSheet();
    }

    function _toggleTranslations() {
        _showTranslations = !_showTranslations;
        const btn = document.getElementById('wk-music-toggle-trans');
        if (btn) {
            btn.textContent = _showTranslations ? 'Translations: On' : 'Translations: Off';
            btn.classList.toggle('is-active', _showTranslations);
        }
        _renderSheet();
    }

    function _updateAnsweredCount() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        const filled = Array.from(blanks).filter(el => el.value && el.value.trim() !== '');
        const hasEvaluated = root.querySelector('.wk-music-blank-select.is-correct, .wk-music-blank-select.is-wrong, .wk-music-blank-input.is-correct, .wk-music-blank-input.is-wrong');
        const readout = document.getElementById('wk-music-score-readout');
        if (!hasEvaluated && readout) {
            readout.textContent = `${filled.length} of ${blanks.length} answered`;
        }
    }

    function _checkAnswers() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        let correctCount = 0;

        blanks.forEach(el => {
            const answer = el.dataset.answer;
            const userVal = el.value ? el.value.trim() : '';
            if (!userVal) {
                el.classList.remove('is-correct', 'is-wrong');
                return;
            }
            if (_normalize(userVal) === _normalize(answer)) {
                el.classList.add('is-correct');
                el.classList.remove('is-wrong');
                correctCount++;
            } else {
                el.classList.add('is-wrong');
                el.classList.remove('is-correct');
            }
        });

        const readout = document.getElementById('wk-music-score-readout');
        if (readout) {
            readout.textContent = `${correctCount} of ${blanks.length} correct`;
        }
        _showToast(`${correctCount} of ${blanks.length} correct`);
    }

    function _revealAnswers() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        blanks.forEach(el => {
            el.value = el.dataset.answer;
            el.classList.add('is-correct');
            el.classList.remove('is-wrong');
        });
        const readout = document.getElementById('wk-music-score-readout');
        if (readout) {
            readout.textContent = `${blanks.length} of ${blanks.length} correct`;
        }
    }

    function _resetExercises() {
        const root = _container;
        if (!root) return;
        const blanks = root.querySelectorAll('.wk-music-blank-select, .wk-music-blank-input');
        blanks.forEach(el => {
            el.value = '';
            el.classList.remove('is-correct', 'is-wrong');
        });
        _updateAnsweredCount();
    }

    // Lexicon & SRS
    async function _handleWordTap(cleanWord, event) {
        if (event && event.stopPropagation) event.stopPropagation();
        _activeWord = cleanWord;

        if (typeof showWord === 'function') {
            showWord(cleanWord, [cleanWord], 0, false, cleanWord);
            return;
        }
        if (typeof Reader !== 'undefined' && typeof Reader.showWord === 'function') {
            Reader.showWord(cleanWord, [cleanWord], 0, false, cleanWord);
            return;
        }

        let lemma = cleanWord;
        let pos = '';
        let def = 'No definition available';

        if (typeof Lexicon !== 'undefined' && typeof Lexicon.lookup === 'function') {
            try {
                if (typeof Lexicon.load === 'function') await Lexicon.load();
                const res = Lexicon.lookup(cleanWord);
                if (res && res.readings && res.readings.length > 0) {
                    const r = res.readings[0];
                    lemma = r.lemma || cleanWord;
                    pos = r.pos || '';
                    def = r.translation || 'Available in Lexicon';
                }
            } catch (e) {
                // Ignore lexicon resolution error
            }
        }

        _activeDefinition = def;
        _activePos = pos;
        _showLexiconPop(lemma, pos, def, (event && event.target) ? event.target : document.body);
    }

    function _showLexiconPop(lemma, pos, def, targetEl) {
        const pop = document.getElementById('wk-music-lexicon-pop');
        if (!pop) return;

        document.getElementById('wk-pop-lemma').textContent = lemma;
        document.getElementById('wk-pop-pos').textContent = pos;
        document.getElementById('wk-pop-def').textContent = def;

        const rect = targetEl.getBoundingClientRect();
        pop.style.left = `${Math.min(window.innerWidth - 260, Math.max(10, rect.left))}px`;
        pop.style.top = `${rect.bottom + window.scrollY + 6}px`;
        pop.style.display = 'block';
    }

    function _hideLexiconPop() {
        const pop = document.getElementById('wk-music-lexicon-pop');
        if (pop) pop.style.display = 'none';
    }

    function _addToFlashcards() {
        if (!_activeWord) return;
        const clean = _activeWord.toLowerCase();

        if (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) {
            const alreadyInDeck = srsDeck.some(w => {
                const targetLemma = (typeof Lang !== 'undefined' && Lang.targetLemma) ? Lang.targetLemma(w) : (w.spanish || w.target);
                return targetLemma === clean;
            });

            if (!alreadyInDeck) {
                if (typeof clearSrsLemmaReset === 'function') clearSrsLemmaReset(clean);
                const schedule = typeof newCardSchedule === 'function' ? newCardSchedule() : { interval: 1, ease: 2.5, reps: 0 };
                srsDeck.push(Object.assign({
                    target: clean,
                    spanish: clean,
                    english: _activeDefinition || clean,
                    type: _activePos || 'vocabulary',
                    source: 'music',
                    added: new Date().toISOString()
                }, schedule));

                if (typeof recordNewWord === 'function') recordNewWord();
                if (typeof saveDeck === 'function') saveDeck();
                if (typeof updateSRSCounter === 'function') updateSRSCounter();
                _showToast(`"${clean}" added to flashcards`);
            } else {
                _showToast(`"${clean}" is already in your deck`);
            }
        } else {
            _showToast(`"${clean}" saved`);
        }

        _hideLexiconPop();
    }

    function _showToast(msg) {
        if (typeof UI !== 'undefined' && typeof UI.toast === 'function') {
            UI.toast(msg);
            return;
        }
        let toastEl = document.getElementById('wk-music-toast');
        if (!toastEl) {
            toastEl = document.createElement('div');
            toastEl.id = 'wk-music-toast';
            toastEl.style.cssText = 'position:fixed;bottom:20px;right:20px;background:#102A47;color:#fff;padding:8px 14px;border-radius:2px;font-size:12px;z-index:3000;';
            document.body.appendChild(toastEl);
        }
        toastEl.textContent = msg;
        toastEl.style.display = 'block';
        setTimeout(() => { toastEl.style.display = 'none'; }, 2200);
    }

    function _attachEvents() {
        const root = _container;
        if (!root) return;

        // Song picker select
        const picker = root.querySelector('#wk-music-song-picker');
        if (picker) {
            picker.addEventListener('change', (e) => _loadSong(e.target.value));
        }

        // Translations toggle
        const toggleBtn = root.querySelector('#wk-music-toggle-trans');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', _toggleTranslations);
        }

        // Mode tabs
        root.querySelectorAll('.wk-music-tab').forEach(tab => {
            tab.addEventListener('click', () => _switchMode(tab.dataset.mode));
        });

        // Exercise actions
        const checkBtn = root.querySelector('#wk-music-btn-check');
        if (checkBtn) checkBtn.addEventListener('click', _checkAnswers);

        const revealBtn = root.querySelector('#wk-music-btn-reveal');
        if (revealBtn) revealBtn.addEventListener('click', _revealAnswers);

        const resetBtn = root.querySelector('#wk-music-btn-reset');
        if (resetBtn) resetBtn.addEventListener('click', _resetExercises);

        // SRS button in lexicon popup
        const srsBtn = root.querySelector('#wk-pop-srs-btn');
        if (srsBtn) srsBtn.addEventListener('click', _addToFlashcards);

        // Close lexicon popup on outside click
        document.addEventListener('click', (e) => {
            if (!e.target.closest('#wk-music-lexicon-pop') && !e.target.classList.contains('wk-music-word-tap')) {
                _hideLexiconPop();
            }
        });
    }

    // Public API
    async function render(container, options) {
        _container = container;
        _songs = await _loadSongs();
        if (!_currentSongId && _songs.length) {
            _currentSongId = _songs[0].id;
        }

        container.innerHTML = _renderBaseHtml();
        _attachEvents();
        _renderSheet();
    }

    function stop() {
        const iframe = document.getElementById('wk-music-yt-iframe');
        if (iframe) iframe.src = 'about:blank';
        _hideLexiconPop();
    }

    return {
        render: render,
        stop: stop
    };
})();

// Export globally for Parlour Workshop
if (typeof window !== 'undefined') {
    window.MusicDriller = MusicDriller;
}
