// ============================================
// CEFR EXAM PRACTICE ENGINE (DELE B1 / ECL B1)
// ============================================
// Official CEFR exam preparation module for Workshop:
//   1. Targeted Task-by-Task practice (Entrenamiento por Tareas):
//      - Comprensión de lectura (Matching notices, deep article MCQs, gapped text, cloze)
//      - Comprensión auditiva (Authentic 2-pass protocol with 30s preview, multi-voice TTS, transcripts)
//      - Expresión e interacción escritas (Live word-counter, autosaved drafts, CEFR analytical rubric)
//      - Expresión e interacción orales (Audio visualizer, real-time STT streaming, oral evaluation)
//   2. Exam Strategy Guide & Discourse Connectors
//   3. Full 4-Skill Mock Exam Simulation (Phase 2)
//   4. Comprehensive Grade History & Score Matrix
//
// Strictly zero emojis across all UI chrome, tabs, badges, and exercises.

const CefrExam = (function () {
    'use strict';

    const EXTRA_UI_STRINGS = {
        'Escuchando con atención...': { pl: 'Słuchaj uważnie...', cs: 'Pozorně poslouchejte...', sk: 'Pozorne počúvajte...' },
        'Detener audio': { pl: 'Zatrzymaj nagranie', cs: 'Zastavit zvuk', sk: 'Zastaviť zvuk' },
        'Pausa entre audiciones': { pl: 'Przerwa między odtworzeniami', cs: 'Pauza mezi poslechy', sk: 'Prestávka medzi počúvaniami' },
        'Comenzar segunda audición': { pl: 'Rozpocznij drugie odtworzenie', cs: 'Spustit druhý poslech', sk: 'Spustiť druhé počúvanie' },
        'Audición completada': { pl: 'Odsłuch zakończony', cs: 'Poslech dokončen', sk: 'Počúvanie dokončené' },
        'Has escuchado los dos pases oficiales. Selecciona tus respuestas y comprueba la tarea.': {
            pl: 'Wysłuchałeś obu oficjalnych odtworzeń. Zaznacz odpowiedzi i sprawdź zadanie.',
            cs: 'Vyslechli jste oba oficiální poslechy. Vyberte odpovědi a zkontrolujte úlohu.',
            sk: 'Vypočuli ste si obe oficiálne prehrania. Vyberte odpovede a skontrolujte úlohu.'
        },
        'Repetir segundo pase': { pl: 'Powtórz drugi odsłuch', cs: 'Zopakovat druhý poslech', sk: 'Zopakovať druhé počúvanie' },
        'Pulsa reproducir cuando estés listo.': { pl: 'Naciśnij odtwórz, gdy będziesz gotowy.', cs: 'Stiskněte přehrát, až budete připraveni.', sk: 'Stlačte prehrať, keď budete pripravení.' },
        'Pulsa en cada pregunta para escuchar su mensaje correspondiente (hasta 2 pases por mensaje).': {
            pl: 'Kliknij każde pytanie, aby odsłuchać nagranie (do 2 odtworzeń na komunikat).',
            cs: 'Klikněte na jednotlivé položky a přehrajte si nahrávku (až 2 poslechy ke každé zprávě).',
            sk: 'Kliknite na každú otázku a vypočujte si nahrávku (až 2 prehrania ku každej správe).'
        },
        'Detectando voz — sigue hablando…': { pl: 'Wykrywanie mowy — mów dalej…', cs: 'Detekce hlasu — mluvte dál…', sk: 'Rozpoznávanie hlasu — hovorte ďalej…' },
        'No se pudo acceder al micrófono. Puedes redactar tu respuesta oral en el campo de texto.': {
            pl: 'Brak dostępu do mikrofonu. Możesz wpisać wypowiedź ustną w polu tekstowym.',
            cs: 'Nepodařilo se získat přístup k mikrofonu. Svou ústní odpověď můžete napsat do textového pole.',
            sk: 'Nepodarilo sa získať prístup k mikrofónu. Svoju ústnu odpoveď môžete napísať do textového poľa.'
        },
        'Detener grabación': { pl: 'Zatrzymaj nagrywanie', cs: 'Zastavit nahrávání', sk: 'Zastaviť nahrávanie' },
        'Grabando voz... Habla con naturalidad.': { pl: 'Nagrywanie głosu... Mów swobodnie.', cs: 'Nahrávání hlasu... Mluvte přirozeně.', sk: 'Nahrávanie hlasu... Hovorte prirodzene.' },
        'Iniciar grabación de voz': { pl: 'Rozpocznij nagrywanie głosu', cs: 'Spustit nahrávání hlasu', sk: 'Spustiť nahrávanie hlasu' },
        'Micrófono listo. Pulsa para comenzar tu producción oral.': {
            pl: 'Mikrofon gotowy. Naciśnij, aby rozpocząć wypowiedź ustną.',
            cs: 'Mikrofon připraven. Klikněte pro zahájení ústního projevu.',
            sk: 'Mikrofón pripravený. Kliknite na začatie ústneho prejavu.'
        },
        'Tareas oficiales': { pl: 'Zadania oficjalne', cs: 'Oficiální úlohy', sk: 'Oficiálne úlohy' },
        'Guía y estrategias': { pl: 'Przewodnik i strategie', cs: 'Průvodce a strategie', sk: 'Sprievodca a stratégie' },
        'Simulacro completo': { pl: 'Pełny egzamin próbny', cs: 'Celá cvičná zkouška', sk: 'Celá skúšobná skúška' },
        'Mis resultados': { pl: 'Moje wyniki', cs: 'Moje výsledky', sk: 'Moje výsledky' },
        'Comprensión de lectura': { pl: 'Rozumienie tekstów pisanych', cs: 'Čtení s porozuměním', sk: 'Čítanie s porozumením' },
        'Comprensión auditiva': { pl: 'Rozumienie ze słuchu', cs: 'Poslech s porozuměním', sk: 'Počúvanie s porozumením' },
        'Expresión escrita': { pl: 'Wypowiedź pisemna', cs: 'Psaní', sk: 'Písomný prejav' },
        'Expresión oral': { pl: 'Wypowiedź ustna', cs: 'Ústní část', sk: 'Ústny prejav' },
        'tareas': { pl: 'zadania', cs: 'úlohy', sk: 'úlohy' },
        'No hay tareas disponibles.': { pl: 'Brak dostępnych zadań.', cs: 'Nejsou k dispozici žádné úlohy.', sk: 'Nie sú k dispozícii žiadne úlohy.' },
        'Pendiente': { pl: 'Do wykonania', cs: 'Nesplněno', sk: 'Nevypracované' },
        'Comenzar práctica': { pl: 'Rozpocznij ćwiczenie', cs: 'Začít procvičovat', sk: 'Začať precvičovať' },
        'Volver a tareas': { pl: 'Wróć do zadań', cs: 'Zpět na úlohy', sk: 'Späť na úlohy' },
        '<span class="cefr-inline-gap-token">[ Hueco $1 ]</span>': {
            pl: '<span class="cefr-inline-gap-token">[ Luka $1 ]</span>',
            cs: '<span class="cefr-inline-gap-token">[ Mezera $1 ]</span>',
            sk: '<span class="cefr-inline-gap-token">[ Medzera $1 ]</span>'
        },
        'Texto de lectura': { pl: 'Tekst do czytania', cs: 'Čtený text', sk: 'Text na čítanie' },
        'Lee el texto con atención antes de responder': { pl: 'Przeczytaj uważnie tekst przed udzieleniem odpowiedzi', cs: 'Před odpovědí si text pozorně přečtěte', sk: 'Pred odpovedaním si text pozorne prečítajte' },
        'Preguntas de comprensión': { pl: 'Pytania sprawdzające', cs: 'Otázky k porozumění', sk: 'Otázky na porozumenie' },
        'Selecciona la opción correcta (A, B o C)': { pl: 'Wybierz właściwą odpowiedź (A, B lub C)', cs: 'Vyberte správnou možnost (A, B nebo C)', sk: 'Vyberte správnu možnosť (A, B alebo C)' },
        'Justificación': { pl: 'Uzasadnienie', cs: 'Odůvodnění', sk: 'Odôvodnenie' },
        'Texto principal': { pl: 'Tekst główny', cs: 'Hlavní text', sk: 'Hlavný text' },
        'Selecciona la oración correcta para cada posición': { pl: 'Wybierz właściwe zdanie w miejsce każdej luki', cs: 'Vyberte vhodnou větu pro každou mezeru', sk: 'Vyberte vhodnú vetu pre každú medzeru' },
        'Selecciona letra': { pl: 'Wybierz literę', cs: 'Vyberte písmeno', sk: 'Vyberte písmeno' },
        'Correcto': { pl: 'Poprawnie', cs: 'Správně', sk: 'Správne' },
        'Solución': { pl: 'Rozwiązanie', cs: 'Řešení', sk: 'Riešenie' },
        'Comprobar tarea': { pl: 'Sprawdź odpowiedzi', cs: 'Zkontrolovat úlohu', sk: 'Skontrolovať úlohu' },
        'Repetir tarea': { pl: 'Rozwiąż ponownie', cs: 'Zkusit znovu', sk: 'Skúsiť znova' },
        'Detener reproducción': { pl: 'Zatrzymaj odtwarzanie', cs: 'Zastavit přehrávání', sk: 'Zastaviť prehrávanie' },
        'Escuchar audio (Pase 1/2)': { pl: 'Odsłuchaj nagranie (1/2)', cs: 'Přehrát nahrávku (1/2)', sk: 'Prehrať nahrávku (1/2)' },
        'Transcripción': { pl: 'Transkrypcja', cs: 'Přepis nahrávky', sk: 'Prepis nahrávky' },
        'Transcripción completa de la audición': { pl: 'Pełny zapis nagrania', cs: 'Úplný přepis poslechu', sk: 'Úplný prepis nahrávky' },
        'Comprobar respuestas': { pl: 'Sprawdź odpowiedzi', cs: 'Zkontrolovat odpovědi', sk: 'Skontrolovať odpovede' },
        'Repetir audición': { pl: 'Odsłuchaj ponownie', cs: 'Přehrát znovu', sk: 'Prehrať znova' },
        'Elige opción de redacción': { pl: 'Wybierz temat wypowiedzi', cs: 'Vyberte téma zadání', sk: 'Vyberte tému zadania' },
        'Instrucciones de la tarea:': { pl: 'Polecenie do zadania:', cs: 'Zadání úlohy:', sk: 'Zadanie úlohy:' },
        'Palabras:': { pl: 'Liczba słów:', cs: 'Počet slov:', sk: 'Počet slov:' },
        'Borrador guardado automáticamente': { pl: 'Wersja robocza zapisana automatycznie', cs: 'Koncept automaticky uložen', sk: 'Koncept automaticky uložený' },
        'Escribe tu redacción aquí...': { pl: 'Napisz tutaj swoją wypowiedź...', cs: 'Sem napište svůj text...', sk: 'Sem napíšte svoj text...' },
        'Evaluar redacción (Rúbrica CEFR)': { pl: 'Oceń wypowiedź (kryteria CEFR)', cs: 'Vyhodnotit text (kritéria SERR)', sk: 'Vyhodnotiť text (kritériá SERR)' },
        'puntos': { pl: 'pkt', cs: 'bodů', sk: 'bodov' },
        'Párrafos y estructuración:': { pl: 'Akapity i kompozycja:', cs: 'Odstavce a struktura:', sk: 'Odseky a štruktúra:' },
        'Puntos guía y riqueza léxica:': { pl: 'Realizacja punktów i słownictwo:', cs: 'Naplnění zadání a slovní zásoba:', sk: 'Splnenie bodov a slovná zásoba:' },
        'Transcripción de tu respuesta (puedes revisarla o editarla antes de evaluar):': {
            pl: 'Transkrypcja Twojej wypowiedzi (możesz ją poprawić przed oceną):',
            cs: 'Přepis vaší odpovědi (před vyhodnocením jej můžete upravit):',
            sk: 'Prepis vašej odpovede (pred vyhodnotením ho môžete upraviť):'
        },
        'Tu voz se transcribirá aquí en tiempo real...': {
            pl: 'Twoja wypowiedź pojawi się tutaj lub możesz ją wpisać ręcznie...',
            cs: 'Váš hlas se zde přepíše v reálném čase...',
            sk: 'Váš hlas sa tu prepíše v reálnom čase...'
        },
        'Escucha tu grabación:': { pl: 'Odsłuchaj swoje nagranie:', cs: 'Poslechněte si svou nahrávku:', sk: 'Vypočujte si svoju nahrávku:' },
        'Evaluar expresión oral': { pl: 'Oceń wypowiedź ustną', cs: 'Vyhodnotit ústní projev', sk: 'Vyhodnotiť ústny prejav' },
        'Palabras producidas:': { pl: 'Wypowiedziane słowa:', cs: 'Počet pronesených slov:', sk: 'Počet vyslovených slov:' },
        'Conectores orales detectados:': { pl: 'Wykryte łączniki dyskursu:', cs: 'Zjištěné konektory:', sk: 'Zistené spojky:' },
        'Ninguno detectado': { pl: 'Nie wykryto', cs: 'Žádné nezjištěny', sk: 'Žiadne nezistené' },
        'Guía no disponible.': { pl: 'Przewodnik jest niedostępny.', cs: 'Průvodce není k dispozici.', sk: 'Sprievodca nie je k dispozícii.' },
        'Guía oficial del examen': { pl: 'Oficjalny przewodnik po egzaminie', cs: 'Oficiální průvodce zkouškou', sk: 'Oficiálny sprievodca skúškou' },
        'El examen oficial evalúa las cuatro destrezas divididas en dos bloques:': {
            pl: 'Egzamin oficjalny ocenia cztery sprawności podzielone na dwie części:',
            cs: 'Oficiální zkouška ověřuje čtyři řečové dovednosti rozdělené do dvou částí:',
            sk: 'Oficiálna skúška overuje štyri jazykové zručnosti rozdelené do dvoch častí:'
        },
        'Bloque 1: Destrezas escritas (50 pts)': { pl: 'Część 1: Sprawności pisemne (50 pkt)', cs: 'Část 1: Písemná zkouška (50 b.)', sk: 'Časť 1: Písomná časť (50 b.)' },
        'Bloque 2: Destrezas orales (50 pts)': { pl: 'Część 2: Sprawności ustne (50 pkt)', cs: 'Část 2: Ústní a poslechová část (50 b.)', sk: 'Časť 2: Ústna a posluchová časť (50 b.)' },
        'Apto: Mínimo 30 / 50 pts': { pl: 'Próg zaliczenia: 30 / 50 pkt', cs: 'Minimum ke složení: 30 / 50 b.', sk: 'Minimum na zloženie: 30 / 50 b.' },
        'Iniciar simulacro completo cronometrado': { pl: 'Rozpocznij pełny egzamin próbny', cs: 'Spustit celou cvičnou zkoušku', sk: 'Spustiť celú skúšobnú skúšku' },
        'APTO': { pl: 'ZALICZONY', cs: 'USPĚL', sk: 'USPEL' },
        'EN PROCESO': { pl: 'W TOKU', cs: 'PROBÍHÁ', sk: 'PREBIEHA' },
        'Lectura': { pl: 'Czytanie', cs: 'Čtení', sk: 'Čítanie' },
        'Audición': { pl: 'Słuchanie', cs: 'Poslech', sk: 'Počúvanie' },
        'Escritura': { pl: 'Pisanie', cs: 'Psaní', sk: 'Písanie' },
        'Oral': { pl: 'Mówienie', cs: 'Mluvení', sk: 'Rozprávanie' },
        'Tareas realizadas': { pl: 'Ukończone zadania', cs: 'Dokončené úlohy', sk: 'Dokončené úlohy' },
        'Puntuación media': { pl: 'Średni wynik', cs: 'Průměrné skóre', sk: 'Priemerné skóre' },
        'Calificación global': { pl: 'Ocena ogólna', cs: 'Celkové hodnocení', sk: 'Celkové hodnotenie' },
        'Registro detallado de tareas': { pl: 'Szczegółowy rejestr wyników', cs: 'Podrobný přehled výsledků', sk: 'Podrobný prehľad výsledkov' },
        "Aún no has completado ninguna tarea. Entrena en la pestaña 'Tareas oficiales'.": {
            pl: "Nie ukończyłeś jeszcze żadnego zadania. Ćwicz w zakładce 'Zadania oficjalne'.",
            cs: "Zatím jste nedokončili žádnou úlohu. Procvičujte v záložce 'Oficiální úlohy'.",
            sk: "Zatiaľ ste nedokončili žiadnu úlohu. Precvičujte na karte 'Oficiálne úlohy'."
        },
        'Destreza': { pl: 'Sprawność', cs: 'Dovednost', sk: 'Zručnosť' },
        'Tarea': { pl: 'Zadanie', cs: 'Úloha', sk: 'Úloha' },
        'Puntos': { pl: 'Punkty', cs: 'Body', sk: 'Body' },
        'Porcentaje': { pl: 'Wynik %', cs: 'Úspěšnost', sk: 'Úspešnosť' }
    };

    function createModule(config) {
        const _id = config.id;
        const _dataFile = config.dataFile;
        const _storageKey = `parlour_cefr_v1_${_id}`;
        const _lang = _id.startsWith('sk-') ? 'sk'
            : (_id.startsWith('cs-') ? 'cs'
            : (_id.startsWith('pl-') ? 'pl'
            : (_id.startsWith('fr-') ? 'fr'
            : (_id.startsWith('it-') ? 'it'
            : (_id.includes('hu') || _id.startsWith('ecl-') ? 'hu' : 'es')))));
        function _t(esStr, huStr, frStr, itStr, plStr, csStr, skStr) {
            if (_lang === 'hu') return huStr;
            if (_lang === 'fr') return frStr !== undefined ? frStr : esStr;
            if (_lang === 'it') return itStr !== undefined ? itStr : esStr;
            if (_lang === 'pl') return plStr !== undefined ? plStr : ((EXTRA_UI_STRINGS[esStr] && EXTRA_UI_STRINGS[esStr].pl) || esStr);
            if (_lang === 'cs') return csStr !== undefined ? csStr : ((EXTRA_UI_STRINGS[esStr] && EXTRA_UI_STRINGS[esStr].cs) || esStr);
            if (_lang === 'sk') return skStr !== undefined ? skStr : ((EXTRA_UI_STRINGS[esStr] && EXTRA_UI_STRINGS[esStr].sk) || esStr);
            return esStr;
        }

        let _data = null;
        let _container = null;

        let _state = {
            tab: 'tasks',           // 'tasks' | 'strategies' | 'mocks' | 'history'
            activeSkill: 'reading', // 'reading' | 'listening' | 'writing' | 'speaking'
            activeTareaId: null,

            // Reading state
            readingAnswers: {},     // itemId -> selectedValue
            readingSubmitted: false,

            // Listening state
            listeningAnswers: {},
            listeningSubmitted: false,
            listeningPreviewTimer: null,
            listeningPreviewCountdown: 30,
            listeningPass: 1,       // 1 or 2
            listeningPlaying: false,
            listeningActiveItemId: null,
            listeningItemPasses: {},
            listeningIntermission: false,
            listeningIntermissionCountdown: 15,
            listeningIntermissionTimer: null,
            listeningCurrentTurn: -1,
            listeningSpeed: 1.0,
            listeningTranscriptRevealed: false,

            // Writing state
            writingActiveOption: 'A',
            writingDraftText: '',
            writingResult: null,

            // Speaking state
            speakingPrepTimer: null,
            speakingPrepCountdown: 60,
            speakingIsRecording: false,
            speakingMediaRecorder: null,
            speakingAudioChunks: [],
            speakingAudioBlobUrl: null,
            speakingTranscriptText: '',
            speakingRecognition: null,
            speakingAudioContext: null,
            speakingAnalyser: null,
            speakingAnimFrame: null,
            speakingResult: null
        };

        function _esc(str) {
            if (typeof UI !== 'undefined' && UI.escape) return UI.escape(String(str || ''));
            const d = document.createElement('div');
            d.textContent = String(str || '');
            return d.innerHTML;
        }

        function _loadProgress() {
            try {
                return JSON.parse(localStorage.getItem(_storageKey) || '{}');
            } catch (e) {
                return {};
            }
        }

        function _saveTaskScore(skillId, tareaId, score, maxScore) {
            try {
                const prog = _loadProgress();
                prog.scores = prog.scores || {};
                prog.scores[skillId] = prog.scores[skillId] || {};
                const prev = prog.scores[skillId][tareaId];
                if (!prev || score >= prev.score) {
                    prog.scores[skillId][tareaId] = {
                        score: score,
                        maxScore: maxScore,
                        pct: Math.round((score / maxScore) * 100),
                        date: new Date().toISOString()
                    };
                }
                localStorage.setItem(_storageKey, JSON.stringify(prog));
            } catch (e) {}
            if (maxScore > 0 && typeof XP !== 'undefined' && typeof XP.award === 'function') {
                const earned = Math.max(10, Math.round((score / maxScore) * 25));
                XP.award(earned, 'exam-prep', 'CEFR Exam Prep');
            }
        }

        function _draftKey(tareaId) {
            return `parlour_cefr_draft_${_id}_${tareaId}`;
        }

        function _loadDraft(tareaId) {
            try {
                return localStorage.getItem(_draftKey(tareaId)) || '';
            } catch (e) {
                return '';
            }
        }

        function _saveDraft(tareaId, text) {
            try {
                localStorage.setItem(_draftKey(tareaId), text);
            } catch (e) {}
        }

        async function _loadData() {
            if (_data) return _data;
            try {
                let res = await fetch(Lang.content(_dataFile));
                const fallback = (typeof Lang.contentFallback === 'function') ? Lang.contentFallback() : null;
                if (!res.ok && fallback) {
                    res = await fetch('content/' + fallback + '/' + _dataFile);
                }
                _data = res.ok ? await res.json() : null;
            } catch (e) {
                _data = null;
            }
            return _data;
        }

        // ========================================
        // AUDIO & LISTENING RUNNER HELPERS
        // ========================================
        function _stopListeningTimers() {
            if (_state.listeningPreviewTimer) {
                clearInterval(_state.listeningPreviewTimer);
                _state.listeningPreviewTimer = null;
            }
            if (_state.listeningIntermissionTimer) {
                clearInterval(_state.listeningIntermissionTimer);
                _state.listeningIntermissionTimer = null;
            }
            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.stop) {
                ParlourTTS.stop();
            } else if (typeof window !== 'undefined' && window.speechSynthesis) {
                window.speechSynthesis.cancel();
            }
            _state.listeningPlaying = false;
            _state.listeningActiveItemId = null;
        }

        function _speakTurn(text, voiceGender, onEnded) {
            const langCode = typeof Lang !== 'undefined' ? Lang.code() : 'es';
            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
                ParlourTTS.speak({
                    text: text,
                    language: langCode,
                    type: 'listening',
                    gender: voiceGender,
                    speed: _state.listeningSpeed,
                    onEnded: () => {
                        if (typeof onEnded === 'function') onEnded();
                    }
                }).then(started => {
                    if (!started) {
                        _fallbackSpeak(text, langCode, onEnded);
                    }
                }).catch(() => {
                    _fallbackSpeak(text, langCode, onEnded);
                });
            } else {
                _fallbackSpeak(text, langCode, onEnded);
            }
        }

        function _fallbackSpeak(text, langCode, onEnded) {
            if (typeof Speech !== 'undefined' && Speech.speak) {
                Speech.speak(text, { rate: _state.listeningSpeed, onEnd: onEnded });
            } else if (typeof window !== 'undefined' && window.speechSynthesis) {
                const utter = new SpeechSynthesisUtterance(text);
                utter.lang = (typeof Lang !== 'undefined' && typeof Lang.sttLocale === 'function')
                    ? Lang.sttLocale(langCode) : langCode;
                utter.rate = _state.listeningSpeed;
                utter.onend = () => { if (typeof onEnded === 'function') onEnded(); };
                utter.onerror = () => { if (typeof onEnded === 'function') onEnded(); };
                window.speechSynthesis.speak(utter);
            } else {
                setTimeout(() => { if (typeof onEnded === 'function') onEnded(); }, 1500);
            }
        }

        function _playTurnSequence(turns, turnIndex, onComplete) {
            if (!_state.listeningPlaying || turnIndex >= turns.length) {
                _state.listeningPlaying = false;
                _state.listeningCurrentTurn = -1;
                if (typeof onComplete === 'function') onComplete();
                return;
            }

            _state.listeningCurrentTurn = turnIndex;
            _updateListeningConsole();

            const turn = turns[turnIndex];
            const text = turn.text;
            const voiceGender = turn.gender || (turnIndex % 2 === 0 ? 'female' : 'male');

            _speakTurn(text, voiceGender, () => {
                setTimeout(() => {
                    if (_state.listeningPlaying) {
                        _playTurnSequence(turns, turnIndex + 1, onComplete);
                    }
                }, 500);
            });
        }

        function _startAudioPass(passNum, turns) {
            _stopListeningTimers();
            _state.listeningPass = passNum;
            _state.listeningPlaying = true;
            _state.listeningIntermission = false;
            _updateListeningConsole();

            _playTurnSequence(turns, 0, () => {
                _state.listeningPlaying = false;
                _state.listeningCurrentTurn = -1;

                if (passNum === 1) {
                    _startListeningIntermission(turns);
                } else {
                    _updateListeningConsole();
                }
            });
        }

        function _startListeningIntermission(turns) {
            _state.listeningIntermission = true;
            _state.listeningIntermissionCountdown = 15;
            _updateListeningConsole();

            _state.listeningIntermissionTimer = setInterval(() => {
                _state.listeningIntermissionCountdown--;
                if (_state.listeningIntermissionCountdown <= 0) {
                    clearInterval(_state.listeningIntermissionTimer);
                    _state.listeningIntermissionTimer = null;
                    _state.listeningIntermission = false;
                    _startAudioPass(2, turns);
                } else {
                    _updateListeningConsole();
                }
            }, 1000);
        }

        function _updateListeningConsole() {
            const el = document.getElementById('cefr-audio-console');
            if (!el) return;
            const tarea = _getCurrentTarea();
            if (!tarea) return;

            // Case A: Continuous Audio Tarea (like Tarea 2 Interview)
            if (tarea.audio && tarea.audio.turns) {
                const turns = tarea.audio.turns;
                let statusText = '';
                let subText = '';
                let btnHtml = '';

                if (_state.listeningPlaying) {
                    const turn = turns[_state.listeningCurrentTurn];
                    statusText = _t(
                        `Pase ${_state.listeningPass} de 2: Reproduciendo audio`,
                        `${_state.listeningPass} / 2. meghallgatás: Hang lejátszása`,
                        `Écoute ${_state.listeningPass} sur 2 : Lecture en cours`,
                        `Ascolto ${_state.listeningPass} di 2: Riproduzione in corso`,
                        `Odtworzenie ${_state.listeningPass} z 2: Odtwarzanie nagrania`,
                        `Poslech ${_state.listeningPass} ze 2: Přehrávání zvuku`,
                        `Počúvanie ${_state.listeningPass} z 2: Prehrávanie zvuku`
                    );
                    subText = turn
                        ? _t(`Voz: ${turn.speaker}`, `Beszélő: ${turn.speaker}`, `Voix : ${turn.speaker}`, `Voce: ${turn.speaker}`, `Głos: ${turn.speaker}`, `Mluvčí: ${turn.speaker}`, `Hovoriaci: ${turn.speaker}`)
                        : _t('Escuchando con atención...', 'Figyelmes hallgatás...', 'Écoute attentive...', 'Ascolto attento...');
                    btnHtml = `
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-pause">${_t('Detener audio', 'Lejátszás szüneteltetése', 'Arrêter l\'audio', 'Ferma audio')}</button>
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    `;
                } else if (_state.listeningIntermission) {
                    statusText = _t('Pausa entre audiciones', 'Szünet a meghallgatások között', 'Pause entre les écoutes', 'Pausa tra gli ascolti');
                    subText = _t(
                        `La segunda audición comenzará en ${_state.listeningIntermissionCountdown} segundos. Revisa tus opciones.`,
                        `A második meghallgatás ${_state.listeningIntermissionCountdown} másodperc múlva kezdődik. Nézd át a válaszlehetőségeket.`,
                        `La deuxième écoute commencera dans ${_state.listeningIntermissionCountdown} secondes. Relisez vos options.`,
                        `Il secondo ascolto inizierà tra ${_state.listeningIntermissionCountdown} secondi. Rivedi le opzioni.`,
                        `Drugie odtworzenie rozpocznie się za ${_state.listeningIntermissionCountdown} s. Sprawdź opcje.`,
                        `Druhý poslech začne za ${_state.listeningIntermissionCountdown} s. Zkontrolujte své možnosti.`,
                        `Druhé počúvanie sa začne o ${_state.listeningIntermissionCountdown} s. Skontrolujte si možnosti.`
                    );
                    btnHtml = `
                        <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="skip-intermission">${_t('Comenzar segunda audición', 'Második meghallgatás indítása', 'Lancer la deuxième écoute', 'Avvia secondo ascolto')}</button>
                    `;
                } else if (_state.listeningPass === 2 && !_state.listeningPlaying) {
                    statusText = _t('Audición completada', 'Meghallgatás befejezve', 'Écoute terminée', 'Ascolto completato');
                    subText = _t(
                        'Has escuchado los dos pases oficiales. Selecciona tus respuestas y comprueba la tarea.',
                        'Mindkét hivatalos meghallgatás befejeződött. Jelöld be a válaszaidat és ellenőrizd a feladatot.',
                        'Vous avez entendu les deux écoutes officielles. Sélectionnez vos réponses et vérifiez l\'exercice.',
                        'Hai completato entrambi gli ascolti ufficiali. Seleziona le risposte e verifica la prova.'
                    );
                    btnHtml = `
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="replay-pass-2">${_t('Repetir segundo pase', 'Második meghallgatás ismétlése', 'Réécouter le second passage', 'Ripeti secondo ascolto')}</button>
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    `;
                } else {
                    statusText = _t(
                        `Pase ${_state.listeningPass} de 2 preparado`,
                        `${_state.listeningPass} / 2. meghallgatás készen áll`,
                        `Écoute ${_state.listeningPass} sur 2 prête`,
                        `Ascolto ${_state.listeningPass} di 2 pronto`,
                        `Odtworzenie ${_state.listeningPass} z 2 gotowe`,
                        `Poslech ${_state.listeningPass} ze 2 připraven`,
                        `Počúvanie ${_state.listeningPass} z 2 pripravené`
                    );
                    subText = _t('Pulsa reproducir cuando estés listo.', 'Kattints a lejátszásra, amikor készen állsz.', 'Appuyez sur lecture lorsque vous êtes prêt.', 'Premi riproduci quando sei pronto.');
                    btnHtml = `
                        <button type="button" class="btn btn-primary cefr-ctrl-btn" data-action="audio-play">${_t(`Reproducir pase ${_state.listeningPass}`, `${_state.listeningPass}. meghallgatás lejátszása`, `Écouter le passage ${_state.listeningPass}`, `Riproduci ascolto ${_state.listeningPass}`, `Odtwórz nagranie (${_state.listeningPass}/2)`, `Přehrát poslech ${_state.listeningPass}`, `Prehrať počúvanie ${_state.listeningPass}`)}</button>
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    `;
                }

                el.innerHTML = `
                    <div class="cefr-audio-status-wrap">
                        <span class="cefr-audio-status-label">${_esc(statusText)}</span>
                        <span class="cefr-audio-status-sub">${_esc(subText)}</span>
                    </div>
                    <div class="cefr-audio-controls">
                        ${btnHtml}
                    </div>
                `;

                const playBtn = el.querySelector('[data-action="audio-play"]');
                if (playBtn) playBtn.addEventListener('click', () => _startAudioPass(_state.listeningPass, turns));

                const pauseBtn = el.querySelector('[data-action="audio-pause"]');
                if (pauseBtn) pauseBtn.addEventListener('click', () => { _stopListeningTimers(); _updateListeningConsole(); });

                const skipBtn = el.querySelector('[data-action="skip-intermission"]');
                if (skipBtn) skipBtn.addEventListener('click', () => {
                    _stopListeningTimers();
                    _startAudioPass(2, turns);
                });

                const replayBtn = el.querySelector('[data-action="replay-pass-2"]');
                if (replayBtn) replayBtn.addEventListener('click', () => _startAudioPass(2, turns));

                const speedBtn = el.querySelector('[data-action="audio-speed"]');
                if (speedBtn) {
                    speedBtn.addEventListener('click', () => {
                        _state.listeningSpeed = (_state.listeningSpeed === 1.0) ? 0.85 : 1.0;
                        _updateListeningConsole();
                    });
                }
                return;
            }

            // Case B: Discrete Items Tarea (like Tarea 1 Short Messages)
            if (tarea.items && tarea.items.length > 0) {
                const isPlaying = _state.listeningPlaying;
                const activeItem = (tarea.items || []).find(it => it.id === _state.listeningActiveItemId);

                el.innerHTML = `
                    <div class="cefr-audio-status-wrap">
                        <span class="cefr-audio-status-label">${_t(`${tarea.items.length} avisos y mensajes breves`, `${tarea.items.length} rövid hanganyag`, `${tarea.items.length} annonces et messages courts`, `${tarea.items.length} annunci e brevi messaggi`, `${tarea.items.length} krótkie komunikaty`, `${tarea.items.length} krátká hlášení a zprávy`, `${tarea.items.length} krátke oznamy a správy`)}</span>
                        <span class="cefr-audio-status-sub">${isPlaying && activeItem ? _t(`Reproduciendo mensaje ${activeItem.num}...`, `${activeItem.num}. szöveg lejátszása...`, `Lecture du message ${activeItem.num}...`, `Riproduzione messaggio ${activeItem.num}...`, `Odtwarzanie komunikatu ${activeItem.num}...`, `Přehrávání zprávy ${activeItem.num}...`, `Prehrávanie správy ${activeItem.num}...`) : _t('Pulsa en cada pregunta para escuchar su mensaje correspondiente (hasta 2 pases por mensaje).', 'Kattints az egyes kérdések hangfájljára a meghallgatáshoz (legfeljebb 2 lejátszás kérdésenként).', 'Cliquez sur chaque question pour écouter le message correspondant (jusqu\'à 2 écoutes par message).', 'Clicca su ciascuna domanda per ascoltare il messaggio corrispondente (fino a 2 ascolti per messaggio).')}</span>
                    </div>
                    <div class="cefr-audio-controls">
                        ${isPlaying ? `
                            <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-pause">${_t('Detener audio', 'Leállítás', 'Arrêter l\'audio', 'Ferma audio')}</button>
                        ` : ''}
                        <button type="button" class="btn btn-secondary cefr-ctrl-btn" data-action="audio-speed">${_state.listeningSpeed}x</button>
                    </div>
                `;

                const pauseBtn = el.querySelector('[data-action="audio-pause"]');
                if (pauseBtn) pauseBtn.addEventListener('click', () => {
                    _stopListeningTimers();
                    render(_container);
                });

                const speedBtn = el.querySelector('[data-action="audio-speed"]');
                if (speedBtn) {
                    speedBtn.addEventListener('click', () => {
                        _state.listeningSpeed = (_state.listeningSpeed === 1.0) ? 0.85 : 1.0;
                        _updateListeningConsole();
                    });
                }
            }
        }

        // ========================================
        // SPEAKING RUNNER HELPERS (MIC & STT)
        // ========================================
        function _stopSpeakingStreams() {
            if (_state.speakingPrepTimer) {
                clearInterval(_state.speakingPrepTimer);
                _state.speakingPrepTimer = null;
            }
            if (typeof SpeechInput !== 'undefined') {
                if (typeof SpeechInput.cancelListening === 'function') SpeechInput.cancelListening();
                else SpeechInput.stopListening();
            }
            if (_state.speakingMediaRecorder && _state.speakingIsRecording) {
                try { _state.speakingMediaRecorder.stop(); } catch (e) {}
            }
            if (_state.speakingRecognition) {
                try { _state.speakingRecognition.stop(); } catch (e) {}
            }
            if (_state.speakingAudioContext) {
                try { _state.speakingAudioContext.close(); } catch (e) {}
                _state.speakingAudioContext = null;
            }
            if (_state.speakingAnimFrame) {
                cancelAnimationFrame(_state.speakingAnimFrame);
                _state.speakingAnimFrame = null;
            }
            _state.speakingIsRecording = false;
        }

        async function _startSpeakingRecording() {
            _state.speakingAudioChunks = [];
            _state.speakingTranscriptText = '';

            if (typeof SpeechInput !== 'undefined') {
                _state.speakingIsRecording = true;
                _updateSpeakingUI();
                const sttLang = (typeof Lang !== 'undefined' && typeof Lang.sttLocale === 'function')
                    ? Lang.sttLocale()
                    : ((typeof Lang !== 'undefined') ? Lang.code() : 'es-ES');
                SpeechInput.startListening({
                    preferRecording: true,
                    manualStop: true,
                    lang: sttLang,
                    onInterim: (text) => {
                        _state.speakingTranscriptText = text;
                        const transcriptBox = document.getElementById('cefr-speaking-transcript-input');
                        if (transcriptBox) transcriptBox.value = text;
                    },
                    onFinal: (text) => {
                        if (text) {
                            _state.speakingTranscriptText = text;
                            const transcriptBox = document.getElementById('cefr-speaking-transcript-input');
                            if (transcriptBox) transcriptBox.value = text;
                        }
                        _state.speakingIsRecording = false;
                        render(_container);
                    },
                    onAudioReady: (audioUrl) => {
                        _state.speakingAudioBlobUrl = audioUrl;
                        if (!_state.speakingIsRecording) {
                            render(_container);
                        }
                    },
                    onAudioLevel: (level, meta) => {
                        const statusEl = document.getElementById('cefr-mic-status-label');
                        if (statusEl && _state.speakingIsRecording && meta && meta.isHearingVoice) {
                            statusEl.textContent = _t(
                                'Detectando voz — sigue hablando…',
                                'Hang érzékelve — beszélj tovább…',
                                'Voix détectée — continuez à parler…',
                                'Voce rilevata — continua a parlare…'
                            );
                        }
                    },
                    onError: (err) => {
                        console.warn('Microphone error:', err);
                        _state.speakingIsRecording = false;
                        render(_container);
                        if (err === 'permission-denied' || err === 'service-not-allowed' || err === 'insecure-context' || err === 'device-busy') {
                            alert(_t(
                                'No se pudo acceder al micrófono. Puedes redactar tu respuesta oral en el campo de texto.',
                                'A mikrofonhoz való hozzáférés nem sikerült. A válaszodat a szövegmezőbe is megírhatod.',
                                'Impossible d\'accéder au microphone. Vous pouvez rédiger votre réponse orale dans le champ de texte.',
                                'Impossibile accedere al microfono. Puoi scrivere la tua risposta orale nel campo di testo.'
                            ));
                        }
                    }
                });
                return;
            }

            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                _state.speakingMediaRecorder = new MediaRecorder(stream);

                _state.speakingMediaRecorder.ondataavailable = (e) => {
                    if (e.data.size > 0) _state.speakingAudioChunks.push(e.data);
                };

                _state.speakingMediaRecorder.onstop = () => {
                    const blob = new Blob(_state.speakingAudioChunks, { type: _state.speakingMediaRecorder.mimeType || 'audio/webm' });
                    _state.speakingAudioBlobUrl = URL.createObjectURL(blob);
                    stream.getTracks().forEach(track => track.stop());
                    _renderActiveTarea();
                };

                _state.speakingMediaRecorder.start();
                _state.speakingIsRecording = true;
                _updateSpeakingUI();
            } catch (err) {
                console.warn('Microphone access unavailable or denied:', err);
                alert(_t(
                    'No se pudo acceder al micrófono. Puedes redactar tu respuesta oral en el campo de texto.',
                    'A mikrofonhoz való hozzáférés nem sikerült. A válaszodat a szövegmezőbe is megírhatod.',
                    'Impossible d\'accéder au microphone. Vous pouvez rédiger votre réponse orale dans le champ de texte.',
                    'Impossibile accedere al microfono. Puoi scrivere la tua risposta orale nel campo di testo.'
                ));
            }
        }

        function _stopSpeakingRecording() {
            if (typeof SpeechInput !== 'undefined') {
                _state.speakingIsRecording = false;
                SpeechInput.stopListening();
                _updateSpeakingUI();
                return;
            }
            if (_state.speakingMediaRecorder && _state.speakingIsRecording) {
                _state.speakingMediaRecorder.stop();
            }
            if (_state.speakingRecognition) {
                try { _state.speakingRecognition.stop(); } catch (e) {}
            }
            _state.speakingIsRecording = false;
            _updateSpeakingUI();
        }

        function _updateSpeakingUI() {
            const btn = document.getElementById('cefr-mic-toggle-btn');
            const statusEl = document.getElementById('cefr-mic-status-label');
            if (!btn || !statusEl) return;

            if (_state.speakingIsRecording) {
                btn.textContent = _t('Detener grabación', 'Felvétel leállítása', 'Arrêter l\'enregistrement', 'Ferma registrazione');
                btn.className = 'btn btn-secondary cefr-record-btn is-recording';
                statusEl.textContent = _t(
                    'Grabando voz... Habla con naturalidad.',
                    'Hangfelvétel folyamatban... Beszélj természetesen.',
                    'Enregistrement en cours... Parlez naturellement.',
                    'Registrazione in corso... Parla con naturalezza.'
                );
            } else {
                btn.textContent = _t('Iniciar grabación de voz', 'Hangfelvétel indítása', 'Démarrer l\'enregistrement vocal', 'Avvia registrazione vocale');
                btn.className = 'btn btn-primary cefr-record-btn';
                statusEl.textContent = _t(
                    'Micrófono listo. Pulsa para comenzar tu producción oral.',
                    'A mikrofon készen áll. Kattints a felvételhez.',
                    'Microphone prêt. Cliquez pour commencer votre production orale.',
                    'Microfono pronto. Clicca per iniziare la tua produzione orale.'
                );
            }
        }

        // ========================================
        // EVALUATION ENGINES
        // ========================================
        function _countWords(str) {
            if (!str || typeof str !== 'string') return 0;
            const m = str.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu);
            return m ? m.length : 0;
        }

        // Offline marking of writing and speaking goes through ProductionCheck
        // (engine/production-check.js): repeated words, text copied from the
        // task and English answers do not count, phrases match whole words,
        // and no criterion has a minimum score. Before 2026-11-25 every
        // criterion had a floor and phrases matched as substrings, so an
        // empty answer scored 11/25 and any recording 21/25.
        const _Check = (typeof ProductionCheck !== 'undefined')
            ? ProductionCheck
            : (typeof require === 'function' ? require('./production-check.js') : null);

        function _taskSources(tarea) {
            return [tarea.prompt, tarea.instructions, tarea.context, tarea.situation, tarea.text]
                .concat(Array.isArray(tarea.bulletPoints) ? tarea.bulletPoints : [])
                .filter(v => typeof v === 'string' && v);
        }

        function _evaluateWritingText(text, tarea) {
            const minWords = tarea.minWords || 100;
            const maxWords = tarea.maxWords || 130;
            const check = _Check.analyse(text, { minWords: minWords, targetKeywords: tarea.targetKeywords || [] },
                { modality: 'written', sourceTexts: _taskSources(tarea) });
            const wordCount = check.effectiveWords;
            const gate = !check.notTargetLanguage && wordCount >= minWords * 0.6;

            // Length score (up to 7 pts)
            let lengthScore = 0;
            if (check.notTargetLanguage) lengthScore = 0;
            else if (wordCount >= minWords) lengthScore = check.words > maxWords * 1.3 ? 5 : 7;
            else if (wordCount >= minWords * 0.7) lengthScore = 4;
            else if (wordCount >= minWords * 0.4) lengthScore = 2;

            // Connectors & cohesion (up to 6 pts)
            const isHu = _id.includes('hu');
            const isA1 = (_data && _data.level === 'A1') || _id.includes('a1');
            const isA2 = (_data && _data.level === 'A2') || _id.includes('a2');
            const isB2 = (_data && _data.level === 'B2') || _id.includes('b2');
            const levelCode = isA1 ? 'A1' : (isA2 ? 'A2' : (isB2 ? 'B2' : 'B1'));
            const langCode = _lang !== 'es' ? _lang : (typeof Lang !== 'undefined' ? Lang.code() : 'es');
            const profileConnectors = (typeof Lang !== 'undefined' && typeof Lang.discourseConnectors === 'function')
                ? Lang.discourseConnectors(levelCode, langCode)
                : [];
            let examConnectors = profileConnectors;
            if (!examConnectors || !examConnectors.length) {
                examConnectors = isHu ? (
                    isA1 ? [
                        'és', 'de', 'mert', 'is', 'szintén', 'vagy',
                        'szia', 'sziasztok', 'jó napot', 'köszönöm', 'nagyon köszönöm',
                        'üdvözlettel', 'szép napot', 'viszlát', 'ezért'
                    ] : (isA2 ? [
                        'és', 'de', 'mert', 'is', 'szintén', 'vagy', 'ezért',
                        'után', 'aztán', 'amikor', 'ha', 'szerintem', 'például',
                        'szia', 'sziasztok', 'kedves', 'köszönöm', 'nagyon köszönöm',
                        'üdvözlettel', 'remélem', 'viszlát'
                    ] : (isB2 ? [
                        'véleményem szerint', 'úgy vélem, hogy', 'meglátásom szerint', 'álláspontom szerint',
                        'egyrészt', 'másrészt', 'elsőként', 'mindazonáltal', 'ennek ellenére',
                        'jóllehet', 'ugyanakkor', 'viszont', 'továbbá', 'ráadásul',
                        'következésképpen', 'tekintettel arra, hogy', 'ebből fakadóan', 'ennek következtében',
                        'összességében', 'kétségkívül', 'határozottan', 'fontos hangsúlyozni'
                    ] : [
                        'véleményem szerint', 'úgy gondolom, hogy', 'szerintem', 'meglátásom szerint',
                        'egyrészt', 'másrészt', 'először is', 'továbbá', 'végül',
                        'azonban', 'ennek ellenére', 'bár', 'ugyanakkor', 'viszont',
                        'ezért', 'mivel', 'ennek következtében', 'így', 'tehát',
                        'nagyon köszönöm', 'üdvözlettel', 'remélem', 'fontos, hogy'
                    ]))
                ) : (
                    isA1 ? [
                        'y', 'pero', 'porque', 'también', 'además', 'o',
                        'hola', 'buenos días', 'gracias', 'muchas gracias',
                        'un saludo', 'un abrazo', 'hasta pronto', 'saludos', 'por eso'
                    ] : (isA2 ? [
                        'y', 'pero', 'porque', 'también', 'además', 'o', 'por eso',
                        'cuando', 'después', 'luego', 'entonces', 'primero',
                        'hola', 'buenos días', 'estimado', 'gracias', 'muchas gracias',
                        'un saludo', 'un abrazo', 'hasta pronto', 'saludos', 'si', 'aunque'
                    ] : (isB2 ? [
                        'en primer lugar', 'por una parte', 'por otra parte', 'en lo que respecta a',
                        'sin embargo', 'no obstante', 'a pesar de que', 'si bien', 'pese a',
                        'por consiguiente', 'en consecuencia', 'por lo tanto', 'de ahí que',
                        'desde mi punto de vista', 'en mi opinión', 'cabe destacar que', 'conviene señalar que',
                        'es imprescindible que', 'resulta fundamental que', 'en definitiva', 'en conclusión'
                    ] : [
                        'sin embargo', 'por lo tanto', 'en mi opinión', 'por un lado', 'por otro lado',
                        'en cuanto a', 'además', 'me encantaría', 'gracias por', 'un abrazo', 'aunque',
                        'de modo que', 'así que', 'dado que', 'es importante que', 'no creo que'
                    ]))
                );
            }
            const foundConnectors = _Check.matchPhrases(text, examConnectors);
            const cohesionScore = gate ? Math.min(6, foundConnectors.length * 2) : 0;

            // Sentences & paragraphs (up to 6 pts)
            const hasParagraphs = /\n\s*\S/.test(String(text || '').trim());
            const structScore = !gate ? 0
                : (check.sentences >= 3 ? (hasParagraphs ? 6 : 4) : (check.sentences >= 1 ? 2 : 0));

            // Keyword compliance (up to 6 pts). A task without target
            // phrases marks vocabulary range instead of handing out a floor.
            const targetKeywords = tarea.targetKeywords || [];
            const matchedKw = check.matchedKeywords;
            const kwScore = !gate ? 0
                : (targetKeywords.length
                    ? Math.min(6, matchedKw.length * 2)
                    : (check.distinctWords >= minWords * 0.6 ? 6 : (check.distinctWords >= minWords * 0.4 ? 3 : 0)));

            const totalScore = Math.min(25, lengthScore + cohesionScore + structScore + kwScore);

            return {
                totalScore: totalScore,
                maxScore: 25,
                wordCount: wordCount,
                minWords: minWords,
                maxWords: maxWords,
                foundConnectors: foundConnectors,
                matchedKeywords: matchedKw,
                criteria: {
                    adecuacion: lengthScore,
                    coherencia: cohesionScore,
                    estructura: structScore,
                    leves: kwScore
                }
            };
        }

        function _evaluateSpeakingText(text, tarea) {
            const hasAudio = !!_state.speakingAudioBlobUrl;
            const check = _Check.analyse(text, { minWords: 30, targetKeywords: tarea.targetKeywords || [] },
                { modality: 'oral', sourceTexts: _taskSources(tarea) });
            const wordCount = check.effectiveWords;
            const gate = !check.notTargetLanguage && wordCount >= 15;

            // Marked on the transcript only: a recording on its own proves
            // nothing was said in the language, so it earns no length points.
            let lengthScore = check.notTargetLanguage ? 0
                : (wordCount >= 60 ? 7 : (wordCount >= 30 ? 4 : (wordCount >= 15 ? 2 : 0)));
            const isHu = _id.includes('hu');
            const isA1 = (_data && _data.level === 'A1') || _id.includes('a1');
            const isA2 = (_data && _data.level === 'A2') || _id.includes('a2');
            const isB2 = (_data && _data.level === 'B2') || _id.includes('b2');
            const levelCode = isA1 ? 'A1' : (isA2 ? 'A2' : (isB2 ? 'B2' : 'B1'));
            const langCode = _lang !== 'es' ? _lang : (typeof Lang !== 'undefined' ? Lang.code() : 'es');
            const profileConnectors = (typeof Lang !== 'undefined' && typeof Lang.discourseConnectors === 'function')
                ? Lang.discourseConnectors(levelCode, langCode)
                : [];
            let speakingConnectors = profileConnectors;
            if (!speakingConnectors || !speakingConnectors.length) {
                speakingConnectors = isHu ? (
                    isA1 ? ['és', 'mert', 'is', 'de', 'szintén', 'szerintem']
                        : (isA2 ? ['és', 'mert', 'is', 'de', 'szintén', 'szerintem', 'ezért', 'például', 'aztán']
                        : (isB2 ? ['véleményem szerint', 'úgy vélem', 'meglátásom szerint', 'elsőként', 'például', 'ugyanakkor', 'mindazonáltal', 'ennek következtében', 'másrészt', 'egyrészt', 'összességében']
                        : ['véleményem szerint', 'szerintem', 'úgy gondolom', 'először is', 'például', 'ugyanakkor', 'azonban', 'ezért', 'másrészt', 'egyrészt'])))
                    : (isA1 ? ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo']
                        : (isA2 ? ['porque', 'también', 'y', 'pero', 'además', 'por ejemplo', 'por eso', 'después', 'entonces']
                        : (isB2 ? ['en primer lugar', 'por ejemplo', 'en mi opinión', 'desde mi perspectiva', 'además', 'por consiguiente', 'no obstante', 'sin embargo', 'en definitiva', 'cabe destacar']
                        : ['en primer lugar', 'por ejemplo', 'en mi opinión', 'además', 'por eso'])));
            }
            const foundConnectors = _Check.matchPhrases(text, speakingConnectors);
            const cohesionScore = gate ? Math.min(6, foundConnectors.length * 2) : 0;
            // Delivery: spoken (recorded) and long enough to judge.
            const deliveryScore = gate ? (hasAudio ? 6 : 3) : 0;
            // Range of vocabulary, in place of the former constant 6 points.
            const rangeScore = !gate ? 0 : (check.distinctWords >= 40 ? 6 : (check.distinctWords >= 20 ? 3 : 0));

            const totalScore = Math.min(25, lengthScore + cohesionScore + deliveryScore + rangeScore);

            return {
                totalScore: totalScore,
                maxScore: 25,
                wordCount: wordCount,
                hasAudio: hasAudio,
                foundConnectors: foundConnectors
            };
        }

        // ========================================
        // NAVIGATION & RENDER
        // ========================================
        function _getCurrentSkill() {
            if (!_data || !_data.skills) return null;
            return _data.skills[_state.activeSkill] || null;
        }

        function _getCurrentTarea() {
            const skill = _getCurrentSkill();
            if (!skill || !skill.tareas) return null;
            return skill.tareas.find(t => t.id === _state.activeTareaId) || null;
        }

        function _renderTabs() {
            const tabs = [
                { id: 'tasks', label: _t('Tareas oficiales', 'Hivatalos feladattípusok', 'Épreuves officielles', 'Prove ufficiali') },
                { id: 'strategies', label: _t('Guía y estrategias', 'Stratégiák és tanácsok', 'Guide et stratégies', 'Guida e strategie') },
                { id: 'mocks', label: _t('Simulacro completo', 'Teljes próbavizsga', 'Examen blanc complet', 'Simulazione completa') },
                { id: 'history', label: _t('Mis resultados', 'Eredmények', 'Mes résultats', 'I miei risultati') }
            ];

            return `
                <div class="hce-tabs cefr-tabs" role="tablist">
                    ${tabs.map(t => `
                        <button type="button" class="hce-tab ${_state.tab === t.id ? 'is-active' : ''}" data-cefr-tab="${t.id}" role="tab" aria-selected="${_state.tab === t.id}">
                            ${_esc(t.label)}
                        </button>
                    `).join('')}
                </div>
            `;
        }

        function _renderTasksTab() {
            const skillOrder = ['reading', 'listening', 'writing', 'speaking'];
            const skillLabels = {
                reading: _t('Comprensión de lectura', 'Olvasásértés', 'Compréhension des écrits', 'Comprensione della lettura'),
                listening: _t('Comprensión auditiva', 'Hallásértés', "Compréhension de l'oral", "Comprensione dell'ascolto"),
                writing: _t('Expresión escrita', 'Írásbeli kommunikáció', 'Production écrite', 'Produzione scritta'),
                speaking: _t('Expresión oral', 'Szóbeli kommunikáció', 'Production orale', 'Produzione orale')
            };

            const prog = _loadProgress().scores || {};

            return `
                <div class="cefr-skills-nav" role="tablist">
                    ${skillOrder.map(s => {
                        const skillData = _data.skills[s];
                        if (!skillData) return '';
                        const taskCount = (skillData.tareas || []).length;
                        return `
                            <button type="button" class="cefr-skill-chip ${_state.activeSkill === s ? 'is-active' : ''}" data-cefr-skill="${s}">
                                <span class="cefr-chip-title">${_esc(skillLabels[s] || skillData.name)}</span>
                                <span class="cefr-chip-count">${taskCount} ${_t('tareas', 'feladat', 'exercices', 'prove')}</span>
                            </button>
                        `;
                    }).join('')}
                </div>

                <div class="cefr-tasks-list">
                    ${_renderTareasCards(prog)}
                </div>
            `;
        }

        function _renderTareasCards(prog) {
            const skill = _getCurrentSkill();
            if (!skill || !skill.tareas) return `<p class="cefr-empty">${_t('No hay tareas disponibles.', 'Nincsenek elérhető feladatok.', 'Aucun exercice disponible.', 'Nessuna prova disponibile.')}</p>`;

            const skillProg = prog[_state.activeSkill] || {};

            return skill.tareas.map(t => {
                const recorded = skillProg[t.id];
                const badgeHtml = recorded
                    ? `<span class="cefr-status-pill is-completed">${recorded.pct}% (${recorded.score}/${recorded.maxScore})</span>`
                    : `<span class="cefr-status-pill is-pending">${_t('Pendiente', 'Nincs kitöltve', 'À faire', 'Da completare')}</span>`;

                return `
                    <div class="cefr-task-card" data-cefr-open-tarea="${_esc(t.id)}">
                        <div class="cefr-task-card-header">
                            <span class="cefr-task-pill">${_esc(t.title || _t(`Tarea ${t.tareaNum}`, `${t.tareaNum}. feladat`, `Exercice ${t.tareaNum}`, `Prova ${t.tareaNum}`, `Zadanie ${t.tareaNum}`, `Úloha ${t.tareaNum}`, `Úloha ${t.tareaNum}`))}</span>
                            ${badgeHtml}
                        </div>
                        <div class="cefr-task-card-body">
                            <p class="cefr-task-inst">${_esc(t.instructions || t.prompt || '')}</p>
                        </div>
                        <div class="cefr-task-card-footer">
                            <span class="cefr-task-meta">${_t('Comenzar práctica', 'Kattints a gyakorlás megkezdéséhez', "Commencer l'entraînement", 'Inizia la pratica')}</span>
                            <span class="cefr-task-arrow geo-triangle" aria-hidden="true"></span>
                        </div>
                    </div>
                `;
            }).join('');
        }

        // ========================================
        // TAREA RUNNER VIEWS
        // ========================================
        function _renderActiveTarea() {
            const tarea = _getCurrentTarea();
            if (!tarea) return '';

            let contentHtml = '';
            if (_state.activeSkill === 'reading') {
                contentHtml = _renderReadingTarea(tarea);
            } else if (_state.activeSkill === 'listening') {
                contentHtml = _renderListeningTarea(tarea);
            } else if (_state.activeSkill === 'writing') {
                contentHtml = _renderWritingTarea(tarea);
            } else if (_state.activeSkill === 'speaking') {
                contentHtml = _renderSpeakingTarea(tarea);
            }

            const backLabel = _t('Volver a tareas', 'Vissza a feladatokhoz', 'Retour aux épreuves', 'Torna alle prove');
            return `
                <div class="cefr-runner-container">
                    <div class="cefr-runner-topbar">
                        <button type="button" class="cefr-back-btn" data-action="back-to-tasks" aria-label="${backLabel}">
                            <svg class="art icon cefr-back-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
                            <span>${backLabel}</span>
                        </button>
                        <h3 class="cefr-runner-title">${_esc(tarea.title)}</h3>
                    </div>
                    ${contentHtml}
                </div>
            `;
        }

        function _formatGappedPassage(text) {
            const tokenHtml = _t(
                '<span class="cefr-inline-gap-token">[ Hueco $1 ]</span>',
                '<span class="cefr-inline-gap-token">[ $1. ]</span>',
                '<span class="cefr-inline-gap-token">[ Lacune $1 ]</span>',
                '<span class="cefr-inline-gap-token">[ Spazio $1 ]</span>'
            );
            return (text || '').split('\n\n').map(p => {
                const escaped = _esc(p);
                const withTokens = escaped.replace(/\[___(\d+)___\]/g, tokenHtml);
                return `<p class="cefr-passage-paragraph">${withTokens}</p>`;
            }).join('');
        }

        // 1. Reading Tarea View
        function _renderReadingTarea(tarea) {
            const isHu = _id.includes('hu');
            let stimulusTitle = '';
            let stimulusSubtitle = '';
            let stimulusHtml = '';
            let questionsTitle = '';
            let questionsSubtitle = '';
            let questionsHtml = '';

            if (tarea.type === 'matching-notices') {
                stimulusTitle = isHu ? 'Hirdetések (A-J)' : 'Tablón de anuncios (A-J)';
                stimulusSubtitle = isHu ? 'Olvasd el a 10 rövid hirdetést' : 'Lee los 10 avisos y anuncios breves';
                stimulusHtml = `
                    <div class="cefr-notices-editorial-grid">
                        ${(tarea.notices || []).map(n => `
                            <div class="cefr-notice-card" id="notice-${_esc(n.id)}">
                                <div class="cefr-notice-tag">[${_esc(n.letter)}] ${_esc(n.title)}</div>
                                <p class="cefr-notice-text">${_esc(n.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                questionsTitle = isHu ? 'Személyek és igények (1-6)' : 'Personas y necesidades (1-6)';
                questionsSubtitle = isHu ? 'Rendeld hozzá minden személyhez a megfelelő hirdetést' : 'Relaciona a cada persona con el anuncio adecuado';
                questionsHtml = `
                    <div class="cefr-matching-cards-list">
                        ${(tarea.people || []).map((p, idx) => {
                            const selected = _state.readingAnswers[p.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && selected === p.correctNoticeId;
                            const isWrong = isSubmitted && selected !== p.correctNoticeId;
                            const correctNotice = (tarea.notices || []).find(n => n.id === p.correctNoticeId);

                            return `
                                <div class="cefr-matching-row-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-matching-info">
                                        <span class="cefr-matching-idx">${idx + 1}</span>
                                        <div class="cefr-matching-text">
                                            <strong>${_esc(p.name)}:</strong> ${_esc(p.text)}
                                        </div>
                                    </div>
                                    <div class="cefr-matching-picker">
                                        <label class="cefr-select-label">${isHu ? 'Hozzárendelt hirdetés:' : 'Anuncio correspondiente:'}</label>
                                        <select class="cefr-select" data-match-qid="${_esc(p.id)}" ${isSubmitted ? 'disabled' : ''}>
                                            <option value="">-- ${isHu ? 'Válassz hirdetést' : 'Elige anuncio'} --</option>
                                            ${(tarea.notices || []).map(n => `
                                                <option value="${_esc(n.id)}" ${selected === n.id ? 'selected' : ''}>
                                                    [${_esc(n.letter)}] ${_esc(n.title)}
                                                </option>
                                            `).join('')}
                                        </select>
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-matching-feedback ${isCorrect ? 'is-correct' : 'is-wrong'}">
                                            ${isCorrect 
                                                ? `<span class="cefr-feedback-pass">${isHu ? 'Helyes' : 'Correcto'}: [${correctNotice ? _esc(correctNotice.letter) : ''}] ${correctNotice ? _esc(correctNotice.title) : ''}</span>`
                                                : `<span class="cefr-feedback-fail">${isHu ? 'Helyes megoldás' : 'Respuesta correcta'}: [${correctNotice ? _esc(correctNotice.letter) : ''}] ${correctNotice ? _esc(correctNotice.title) : ''}</span>`}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'reading-mc') {
                stimulusTitle = _t('Texto de lectura', 'Olvasandó szöveg', 'Texte de lecture', 'Testo di lettura');
                stimulusSubtitle = _t('Lee el texto con atención antes de responder', 'Olvasd el a cikket a kérdések megválaszolása előtt', 'Lisez attentivement le texte avant de répondre', 'Leggi attentamente il testo prima di rispondere');
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${(tarea.passage || '').split('\n\n').map(p => `<p class="cefr-passage-paragraph">${_esc(p)}</p>`).join('')}
                    </div>
                `;

                questionsTitle = _t('Preguntas de comprensión', 'Kérdések', 'Questions de compréhension', 'Domande di comprensione');
                questionsSubtitle = _t('Selecciona la opción correcta (A, B o C)', 'Válaszd ki a helyes opciót (A, B vagy C)', 'Sélectionnez la bonne réponse (A, B ou C)', "Seleziona l'opzione corretta (A, B o C)");
                questionsHtml = `
                    <div class="cefr-questions-stack">
                        ${(tarea.questions || []).map((q, qIdx) => {
                            const selectedOpt = _state.readingAnswers[q.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && selectedOpt === q.correct;
                            const isWrong = isSubmitted && selectedOpt !== q.correct && selectedOpt !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title"><span class="cefr-q-num">${qIdx + 1}.</span> ${_esc(q.question)}</div>
                                    <div class="cefr-options-list">
                                        ${(q.options || []).map((opt, optIdx) => {
                                            const optChecked = selectedOpt === optIdx;
                                            return `
                                                <button type="button" class="cefr-opt-btn ${optChecked ? 'is-selected' : ''} ${isSubmitted && optIdx === q.correct ? 'is-correct-target' : ''}" data-ans-qid="${_esc(q.id)}" data-ans-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                                    <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                                    <span class="cefr-opt-text">${_esc(opt)}</span>
                                                </button>
                                            `;
                                        }).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${_t('Justificación', 'Magyarázat', 'Explication', 'Spiegazione')}:</strong> ${_esc(q.explanation || '')}
                                            ${q.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(q.evidence)}"</em></div>` : ''}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'person-matching') {
                const numPeople = (tarea.people || []).length;
                const peopleLetters = numPeople ? tarea.people.map(p => p.letter) : ['A', 'B', 'C'];
                stimulusTitle = isHu ? 'Személyes vélemények' : 'Testimonios personales';
                stimulusSubtitle = isHu
                    ? `${numPeople} személy tapasztalatai (${peopleLetters.join(', ')})`
                    : `${numPeople} experiencias y puntos de vista (${peopleLetters.join(', ')})`;
                stimulusHtml = `
                    <div class="cefr-people-editorial-grid">
                        ${(tarea.people || []).map(p => `
                            <div class="cefr-person-card">
                                <div class="cefr-person-header">
                                    <span class="cefr-person-badge">[${_esc(p.letter)}]</span>
                                    <strong class="cefr-person-title">${_esc(p.name)}</strong>
                                </div>
                                <p class="cefr-person-quote">${_esc(p.text)}</p>
                            </div>
                        `).join('')}
                    </div>
                `;

                const numStatements = (tarea.statements || []).length;
                questionsTitle = isHu ? `Állítások (1-${numStatements})` : `Afirmaciones (1-${numStatements})`;
                questionsSubtitle = isHu
                    ? `Melyik személyre (${peopleLetters.join(', ')}) vonatkozik az állítás?`
                    : `¿A qué persona (${peopleLetters.join(', ')}) corresponde cada afirmación?`;
                questionsHtml = `
                    <div class="cefr-statements-stack">
                        ${(tarea.statements || []).map(s => {
                            const chosen = _state.readingAnswers[s.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === s.correctPerson;
                            const isWrong = isSubmitted && chosen !== s.correctPerson;

                            return `
                                <div class="cefr-statement-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-statement-text">${_esc(s.text)}</div>
                                    <div class="cefr-btn-trio">
                                        ${peopleLetters.map(letter => `
                                            <button type="button" class="cefr-opt-btn cefr-btn-compact ${chosen === letter ? 'is-selected' : ''}" data-stmt-qid="${_esc(s.id)}" data-stmt-letter="${letter}" ${isSubmitted ? 'disabled' : ''}>
                                                ${letter}
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(s.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'gapped-text') {
                const gapsCount = (tarea.gaps || []).length;
                const optLetterRange = (tarea.options && tarea.options.length)
                    ? `(${tarea.options[0].letter}–${tarea.options[tarea.options.length - 1].letter})`
                    : '';
                stimulusTitle = _t('Texto principal', 'Szöveg', 'Texte principal', 'Testo principale');
                stimulusSubtitle = _t(
                    `Observa la posición de los ${gapsCount || 6} fragmentos omitidos`,
                    'Figyeld meg a hiányzó mondatok helyét a szövegben',
                    "Observez l'emplacement des phrases manquantes dans le texte",
                    'Osserva la posizione delle frasi mancanti nel testo',
                    `Zwróć uwagę na miejsca ${gapsCount || 5} brakujących zdań w tekście`,
                    `Sledujte pozice ${gapsCount || 5} vynechaných vět v textu`,
                    `Sledujte pozície ${gapsCount || 5} chýbajúcich viet v texte`
                );
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${_formatGappedPassage(tarea.passage || '')}
                    </div>

                    <div class="cefr-gaps-options-pool-wrap">
                        <h5 class="cefr-gaps-pool-title">${_t(`Opciones de oraciones para los huecos ${optLetterRange}`, `Hiányzó mondatok ${optLetterRange}`, `Phrases proposées pour les lacunes ${optLetterRange}`, `Frasi disponibili per gli spazi ${optLetterRange}`, `Zdania do wyboru do luk ${optLetterRange}`, `Nabídka vět do mezer ${optLetterRange}`, `Ponuka viet do medzier ${optLetterRange}`).trim()}</h5>
                        <div class="cefr-gaps-options-pool">
                            ${(tarea.options || []).map(o => `
                                <div class="cefr-gap-pool-item">
                                    <span class="cefr-gap-badge">[${_esc(o.letter)}]</span>
                                    <span class="cefr-gap-desc">${_esc(o.text)}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;

                const gapNumRange = gapsCount ? `(1–${gapsCount})` : '';
                questionsTitle = _t(`Completar los huecos ${gapNumRange}`, `Hiányzó mondatok beillesztése ${gapNumRange}`, `Compléter les lacunes ${gapNumRange}`, `Completare gli spazi ${gapNumRange}`, `Uzupełnij luki ${gapNumRange}`, `Doplňte mezery ${gapNumRange}`, `Doplňte medzery ${gapNumRange}`).trim();
                questionsSubtitle = _t('Selecciona la oración correcta para cada posición', 'Válaszd ki a megfelelő mondatot az egyes helyekre', 'Choisissez la phrase appropriée pour chaque lacune', 'Seleziona la frase corretta per ogni spazio');
                questionsHtml = `
                    <div class="cefr-gaps-rows-stack">
                        ${(tarea.gaps || []).map(g => {
                            const chosen = _state.readingAnswers[g.id] || '';
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === g.correct;
                            const isWrong = isSubmitted && chosen !== g.correct;

                            return `
                                <div class="cefr-gap-row-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <span class="cefr-gap-row-label">${_t(`Hueco [___${g.num}___]:`, `[ ${g.num}. ]`, `Lacune ${g.num} :`, `Spazio ${g.num}:`, `Luka ${g.num}:`, `Mezera ${g.num}:`, `Medzera ${g.num}:`)}</span>
                                    <select class="cefr-select" data-gap-qid="${_esc(g.id)}" ${isSubmitted ? 'disabled' : ''}>
                                        <option value="">-- ${_t('Selecciona letra', 'Válassz megoldást', 'Choisir une lettre', 'Scegli lettera')} --</option>
                                        ${(tarea.options || []).map(o => `
                                            <option value="${_esc(o.letter)}" ${chosen === o.letter ? 'selected' : ''}>
                                                [${_esc(o.letter)}] ${_esc(o.text.substring(0, 60))}...
                                            </option>
                                        `).join('')}
                                    </select>
                                    ${isSubmitted ? `
                                        <div class="cefr-gap-feedback ${isCorrect ? 'is-correct' : 'is-wrong'}">
                                            ${isCorrect ? _t('Correcto', 'Helyes', 'Correct', 'Corretto') : `${_t('Solución', 'Megoldás', 'Solution', 'Soluzione')}: [${g.correct}]`}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            } else if (tarea.type === 'cloze-mc') {
                const itemsCount = (tarea.items || []).length;
                const itemNumRange = itemsCount ? `(1–${itemsCount})` : '';
                stimulusTitle = isHu ? 'Szöveg' : 'Texto con huecos gramaticales';
                stimulusSubtitle = isHu ? 'Olvasd el a szöveget és válaszd ki a helyes alakokat' : 'Lee el texto y completa los huecos con la opción correcta';
                stimulusHtml = `
                    <div class="cefr-passage-editorial-wrap">
                        ${_formatGappedPassage(tarea.passage || '')}
                    </div>
                `;

                questionsTitle = isHu ? `Nyelvtani és lexikai opciók ${itemNumRange}`.trim() : `Opciones de gramática y léxico ${itemNumRange}`.trim();
                questionsSubtitle = isHu ? 'Válaszd ki a helyes alakot az egyes helyekre' : 'Selecciona la forma correcta para cada hueco';
                questionsHtml = `
                    <div class="cefr-cloze-grid">
                        ${(tarea.items || []).map(item => {
                            const chosen = _state.readingAnswers[item.id];
                            const isSubmitted = _state.readingSubmitted;
                            const isCorrect = isSubmitted && chosen === item.correct;
                            const isWrong = isSubmitted && chosen !== item.correct && chosen !== undefined;

                            return `
                                <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                                    <div class="cefr-q-title">${isHu ? `[ ${item.num}. ]` : `Hueco [___${item.num}___]`}</div>
                                    <div class="cefr-options-list">
                                        ${(item.options || []).map((opt, optIdx) => `
                                            <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === item.correct ? 'is-correct-target' : ''}" data-cloze-qid="${_esc(item.id)}" data-cloze-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                                <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                                <span class="cefr-opt-text">${_esc(opt)}</span>
                                            </button>
                                        `).join('')}
                                    </div>
                                    ${isSubmitted ? `
                                        <div class="cefr-explanation-box">
                                            <strong>${isHu ? 'Magyarázat' : 'Justificación'}:</strong> ${_esc(item.explanation || '')}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                `;
            }

            return `
                <div class="cefr-reading-stack">
                    <div class="cefr-reading-stimulus-card">
                        <div class="cefr-stimulus-header">
                            <h4>${_esc(stimulusTitle)}</h4>
                            <span class="cefr-stimulus-sub">${_esc(stimulusSubtitle)}</span>
                        </div>
                        <div class="cefr-stimulus-body">
                            ${stimulusHtml}
                        </div>
                    </div>

                    <div class="cefr-reading-questions-block">
                        <div class="cefr-questions-header">
                            <h4>${_esc(questionsTitle)}</h4>
                            <span class="cefr-questions-sub">${_esc(questionsSubtitle)}</span>
                        </div>
                        <div class="cefr-questions-flow">
                            ${questionsHtml}
                        </div>

                        <div class="cefr-action-bar">
                            ${!_state.readingSubmitted ? `
                                <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-reading">
                                    ${_t('Comprobar tarea', 'Feladat ellenőrzése', 'Vérifier les réponses', 'Verifica le risposte')}
                                </button>
                            ` : `
                                <button type="button" class="btn btn-secondary cefr-reset-btn" data-action="reset-reading">
                                    ${_t('Repetir tarea', 'Újrapróbálás', 'Recommencer', 'Riprova')}
                                </button>
                            `}
                        </div>
                    </div>
                </div>
            `;
        }

        // 2. Listening Tarea View
        function _renderListeningTarea(tarea) {
            const isHu = _id.includes('hu');
            let questionsHtml = '';

            // Handle Discrete Items (Tarea 1: Avisos y mensajes breves)
            if (tarea.items && tarea.items.length > 0) {
                questionsHtml = tarea.items.map((item) => {
                    const chosen = _state.listeningAnswers[item.id];
                    const isSubmitted = _state.listeningSubmitted;
                    const isCorrect = isSubmitted && chosen === item.correct;
                    const isWrong = isSubmitted && chosen !== item.correct && chosen !== undefined;
                    const isThisPlaying = _state.listeningPlaying && _state.listeningActiveItemId === item.id;
                    const passes = _state.listeningItemPasses[item.id] || 0;

                    return `
                        <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                            <div class="cefr-item-topline">
                                <span class="cefr-q-num">${item.num}.</span>
                                <span class="cefr-item-situation">${_esc(item.situation || '')}</span>
                            </div>

                            <div class="cefr-item-audio-row">
                                <button type="button" class="cefr-item-play-btn ${isThisPlaying ? 'is-playing' : ''}" data-action="play-single-item" data-item-id="${_esc(item.id)}">
                                    <svg class="art icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                                        ${isThisPlaying ? '<rect x="6" y="6" width="12" height="12" fill="currentColor"/>' : '<polygon points="7 5 19 12 7 19 7 5" fill="currentColor"/>'}
                                    </svg>
                                    <span>${isThisPlaying ? _t('Detener reproducción', 'Leállítás', 'Arrêter', 'Ferma riproduzione') : (passes > 0 ? _t(`Repetir audio (${passes}/2 pases)`, `Újrahallgatás (${passes}/2)`, `Réécouter (${passes}/2)`, `Riascolta (${passes}/2)`, `Odsłuchaj ponownie (${passes}/2)`, `Přehrát znovu (${passes}/2)`, `Prehrať znova (${passes}/2)`) : _t('Escuchar audio (Pase 1/2)', 'Meghallgatás (1/2)', 'Écouter (1/2)', 'Ascolta audio (1/2)'))}</span>
                                </button>
                            </div>

                            <div class="cefr-q-title">${_esc(item.question)}</div>

                            <div class="cefr-options-list">
                                ${(item.options || []).map((opt, optIdx) => `
                                    <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === item.correct ? 'is-correct-target' : ''}" data-listen-qid="${_esc(item.id)}" data-listen-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                        <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                        <span class="cefr-opt-text">${_esc(opt)}</span>
                                    </button>
                                `).join('')}
                            </div>

                            ${isSubmitted ? `
                                <div class="cefr-explanation-box">
                                    <strong>${_t('Justificación', 'Magyarázat', 'Explication', 'Spiegazione')}:</strong> ${_esc(item.explanation || '')}
                                    ${item.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(item.evidence)}"</em></div>` : ''}
                                    ${(item.audio && item.audio.turns) ? `
                                        <div class="cefr-item-transcript">
                                            <strong>${_t('Transcripción', 'Szöveg', 'Transcription', 'Trascrizione')}:</strong>
                                            ${item.audio.turns.map(t => `<p><em>${_esc(t.speaker)}:</em> ${_esc(t.text)}</p>`).join('')}
                                        </div>
                                    ` : ''}
                                </div>
                            ` : ''}
                        </div>
                    `;
                }).join('');
            } else if (tarea.questions && tarea.questions.length > 0) {
                // Continuous Audio (Tarea 2: Entrevista)
                questionsHtml = tarea.questions.map((q, qIdx) => {
                    const chosen = _state.listeningAnswers[q.id];
                    const isSubmitted = _state.listeningSubmitted;
                    const isCorrect = isSubmitted && chosen === q.correct;
                    const isWrong = isSubmitted && chosen !== q.correct && chosen !== undefined;

                    return `
                        <div class="cefr-q-card ${isCorrect ? 'is-correct' : (isWrong ? 'is-wrong' : '')}">
                            <div class="cefr-q-title">${_esc(q.question)}</div>
                            <div class="cefr-options-list">
                                ${(q.options || []).map((opt, optIdx) => `
                                    <button type="button" class="cefr-opt-btn ${chosen === optIdx ? 'is-selected' : ''} ${isSubmitted && optIdx === q.correct ? 'is-correct-target' : ''}" data-listen-qid="${_esc(q.id)}" data-listen-idx="${optIdx}" ${isSubmitted ? 'disabled' : ''}>
                                        <span class="cefr-opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                                        <span class="cefr-opt-text">${_esc(opt)}</span>
                                    </button>
                                `).join('')}
                            </div>
                            ${isSubmitted ? `
                                <div class="cefr-explanation-box">
                                    <strong>${_t('Justificación', 'Magyarázat', 'Explication', 'Spiegazione')}:</strong> ${_esc(q.explanation || '')}
                                    ${q.evidence ? `<div class="cefr-evidence-quote"><em>"${_esc(q.evidence)}"</em></div>` : ''}
                                </div>
                            ` : ''}
                        </div>
                    `;
                }).join('');
            }

            return `
                <div class="cefr-listening-wrapper">
                    <div id="cefr-audio-console" class="cefr-audio-console">
                        <!-- Populated by _updateListeningConsole() -->
                    </div>

                    <div class="cefr-listening-questions">
                        ${questionsHtml}
                    </div>

                    ${_state.listeningSubmitted && tarea.audio && tarea.audio.turns ? `
                        <div class="cefr-transcript-section">
                            <div class="cefr-transcript-header">
                                <h4>${_t('Transcripción completa de la audición', 'Teljes hanganyag szövege', "Transcription complète de l'enregistrement", "Trascrizione completa dell'ascolto")}</h4>
                            </div>
                            <div class="cefr-transcript-turns">
                                ${tarea.audio.turns.map(t => `
                                    <div class="cefr-transcript-turn">
                                        <strong>${_esc(t.speaker)}:</strong> ${_esc(t.text)}
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : ''}

                    <div class="cefr-action-bar">
                        ${!_state.listeningSubmitted ? `
                            <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-listening">
                                ${_t('Comprobar respuestas', 'Válaszok ellenőrzése', 'Vérifier les réponses', 'Verifica le risposte')}
                            </button>
                        ` : `
                            <button type="button" class="btn btn-secondary cefr-reset-btn" data-action="reset-listening">
                                ${_t('Repetir audición', 'Újrahallgatás', "Recommencer l'écoute", "Ripeti l'ascolto")}
                            </button>
                        `}
                    </div>
                </div>
            `;
        }

        // 3. Writing Tarea View
        function _renderWritingTarea(tarea) {
            let activePrompt = tarea.prompt;
            let minWords = tarea.minWords || 100;
            let maxWords = tarea.maxWords || 120;

            let optionSwitcherHtml = '';
            if (tarea.options && tarea.options.length > 0) {
                const opt = tarea.options.find(o => o.optionLetter === _state.writingActiveOption) || tarea.options[0];
                activePrompt = opt.prompt;
                minWords = opt.minWords || 130;
                maxWords = opt.maxWords || 150;

                optionSwitcherHtml = `
                    <div class="cefr-option-switcher">
                        <span class="cefr-option-label">${_t('Elige opción de redacción', 'Válassz opciót', 'Choisissez un sujet', 'Scegli opzione')}:</span>
                        ${tarea.options.map(o => `
                            <button type="button" class="btn btn-secondary cefr-opt-toggle ${o.optionLetter === _state.writingActiveOption ? 'is-active' : ''}" data-writing-option="${_esc(o.optionLetter)}">
                                ${_esc(o.title)}
                            </button>
                        `).join('')}
                    </div>
                `;
            }

            const currentWords = _countWords(_state.writingDraftText);
            const isWordCountGood = currentWords >= minWords && currentWords <= maxWords;
            const lvlTag = (_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')));

            return `
                <div class="cefr-writing-wrapper">
                    ${optionSwitcherHtml}

                    <div class="cefr-writing-prompt-card">
                        <div class="cefr-prompt-title">${_t('Instrucciones de la tarea:', 'A feladat leírása:', 'Consignes de la tâche :', 'Istruzioni della prova:')}</div>
                        <div class="cefr-prompt-text">${_esc(activePrompt).split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}</div>
                    </div>

                    <div class="cefr-editor-container">
                        <div class="cefr-editor-toolbar">
                            <span class="cefr-word-counter ${isWordCountGood ? 'is-good' : (currentWords > maxWords ? 'is-over' : '')}">
                                ${_t('Palabras:', 'Szavak száma:', 'Mots :', 'Parole:')} <strong>${currentWords}</strong> / ${minWords}–${maxWords}
                            </span>
                            <span class="cefr-draft-status">${_t('Borrador guardado automáticamente', 'Piszkozat automatikusan mentve', 'Brouillon enregistré automatiquement', 'Bozza salvata automaticamente')}</span>
                        </div>
                        <textarea id="cefr-writing-textarea" class="cefr-textarea" placeholder="${_t('Escribe tu redacción aquí...', 'Írd ide a fogalmazásodat...', 'Rédigez votre texte ici...', 'Scrivi qui il tuo testo...')}" rows="12">${_esc(_state.writingDraftText)}</textarea>
                    </div>

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-writing">
                            ${_t('Evaluar redacción (Rúbrica CEFR)', 'Fogalmazás értékelése', 'Évaluer la production écrite', 'Valuta produzione scritta')}
                        </button>
                    </div>

                    ${_state.writingResult ? `
                        <div class="cefr-writing-results-card">
                            <div class="cefr-res-header">
                                <h4>${_t(`Informe de evaluación ${lvlTag}`, `${lvlTag} Értékelési jelentés`, `Rapport d'évaluation ${lvlTag}`, `Rapporto di valutazione ${lvlTag}`, `Raport oceny ${lvlTag}`, `Zpráva o hodnocení ${lvlTag}`, `Správa o hodnotení ${lvlTag}`)}</h4>
                                <span class="cefr-score-badge">${_state.writingResult.totalScore} / 25 ${_t('puntos', 'pont', 'points', 'punti')}</span>
                            </div>
                            <div class="cefr-rubric-breakdown">
                                <div class="cefr-rubric-item">
                                    <span>${_t(`Adecuación y extensión (${_state.writingResult.wordCount} palabras):`, `Tartalmi megfelelés és terjedelem (${_state.writingResult.wordCount} szó):`, `Respect de la consigne et longueur (${_state.writingResult.wordCount} mots) :`, `Adeguatezza e lunghezza (${_state.writingResult.wordCount} parole):`, `Zgodność z tematem i długość (${_state.writingResult.wordCount} słów):`, `Splnění zadání a rozsah (${_state.writingResult.wordCount} slov):`, `Splnenie zadania a rozsah (${_state.writingResult.wordCount} slov):`)}</span>
                                    <strong>${_state.writingResult.criteria.adecuacion} / 7 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${_t(`Coherencia y conectores (${_state.writingResult.foundConnectors.length} detectados):`, `Szövegösszefüggés és kötőszavak (${_state.writingResult.foundConnectors.length} észlelve):`, `Cohérence et connecteurs (${_state.writingResult.foundConnectors.length} détectés) :`, `Coerenza e connettivi (${_state.writingResult.foundConnectors.length} rilevati):`, `Spójność i łączniki (${_state.writingResult.foundConnectors.length} wykrytych):`, `Návaznost a konektory (${_state.writingResult.foundConnectors.length} zjištěno):`, `Súdržnosť a spojky (${_state.writingResult.foundConnectors.length} zistených):`)}</span>
                                    <strong>${_state.writingResult.criteria.coherencia} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${_t('Párrafos y estructuración:', 'Bekezdések és tagolás:', 'Paragraphes et structure :', 'Paragrafi e struttura:')}</span>
                                    <strong>${_state.writingResult.criteria.estructura} / 6 pts</strong>
                                </div>
                                <div class="cefr-rubric-item">
                                    <span>${_t('Puntos guía y riqueza léxica:', 'Irányítási szempontok és szókincs:', 'Points clés et richesse lexicale :', 'Punti guida e ricchezza lessicale:')}</span>
                                    <strong>${_state.writingResult.criteria.leves} / 6 pts</strong>
                                </div>
                            </div>
                            ${_state.writingResult.foundConnectors.length > 0 ? `
                                <div class="cefr-detected-connectors">
                                    <span>${_t(`Conectores ${lvlTag} empleados:`, `Használt ${lvlTag} kötőszavak:`, `Connecteurs ${lvlTag} utilisés :`, `Connettivi ${lvlTag} utilizzati:`, `Użyte łączniki ${lvlTag}:`, `Použité konektory ${lvlTag}:`, `Použité spojky ${lvlTag}:`)}</span>
                                    <em>${_esc(_state.writingResult.foundConnectors.join(', '))}</em>
                                </div>
                            ` : ''}
                        </div>
                    ` : ''}
                </div>
            `;
        }

        // 4. Speaking Tarea View
        function _renderSpeakingTarea(tarea) {
            const lvlTag = (_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'));
            return `
                <div class="cefr-speaking-wrapper">
                    <div class="cefr-speaking-prompt-card">
                        <div class="cefr-prompt-title">${_esc(tarea.title)}</div>
                        <div class="cefr-prompt-text">${_esc(tarea.prompt).split('\n\n').map(p => `<p>${_esc(p)}</p>`).join('')}</div>
                        ${tarea.bulletPoints ? `
                            <ul class="cefr-prompt-bullets">
                                ${tarea.bulletPoints.map(b => `<li>${_esc(b)}</li>`).join('')}
                            </ul>
                        ` : ''}
                    </div>

                    <div class="cefr-mic-console">
                        <div class="cefr-mic-status-wrap">
                            <span id="cefr-mic-status-label" class="cefr-mic-status-label">
                                ${_t('Micrófono listo. Pulsa para comenzar tu producción oral.', 'A mikrofon készen áll. Kattints a felvételhez.', 'Microphone prêt. Cliquez pour commencer votre production orale.', 'Microfono pronto. Premi per iniziare la produzione orale.')}
                            </span>
                        </div>
                        <div class="cefr-mic-controls">
                            <button type="button" id="cefr-mic-toggle-btn" class="btn btn-primary cefr-record-btn" data-action="toggle-mic">
                                ${_t('Iniciar grabación de voz', 'Hangfelvétel indítása', "Démarrer l'enregistrement", 'Avvia registrazione vocale')}
                            </button>
                        </div>
                    </div>

                    <div class="cefr-speaking-transcript-wrap">
                        <label for="cefr-speaking-transcript-input" class="cefr-transcript-label">
                            ${_t('Transcripción de tu respuesta (puedes revisarla o editarla antes de evaluar):', 'A válaszod leirata (átnézheted vagy szerkesztheted az értékelés előtt):', 'Transcription de votre réponse (modifiable avant évaluation) :', 'Trascrizione della tua risposta (modificabile prima della valutazione):')}
                        </label>
                        <textarea id="cefr-speaking-transcript-input" class="cefr-textarea cefr-transcript-textarea" rows="5" placeholder="${_t('Tu voz se transcribirá aquí en tiempo real...', 'A beszéded valós időben jelenik meg itt...', 'Votre voix sera transcrite ici...', 'La tua voce verrà trascritta qui...')}">${_esc(_state.speakingTranscriptText)}</textarea>
                    </div>

                    ${_state.speakingAudioBlobUrl ? `
                        <div class="cefr-playback-card">
                            <span>${_t('Escucha tu grabación:', 'Hallgasd vissza a felvételt:', 'Écoutez votre enregistrement :', 'Riascolta la tua registrazione:')}</span>
                            <audio controls src="${_state.speakingAudioBlobUrl}" class="cefr-audio-player"></audio>
                        </div>
                    ` : ''}

                    <div class="cefr-action-bar">
                        <button type="button" class="btn btn-primary cefr-submit-btn" data-action="submit-speaking">
                            ${_t('Evaluar expresión oral', 'Beszédkészség értékelése', 'Évaluer la production orale', 'Valuta produzione orale')}
                        </button>
                    </div>

                    ${_state.speakingResult ? `
                        <div class="cefr-speaking-results-card">
                            <div class="cefr-res-header">
                                <h4>${_t(`Informe oral ${lvlTag}`, `${lvlTag} Szóbeli értékelés`, `Évaluation orale ${lvlTag}`, `Valutazione orale ${lvlTag}`, `Ocena wypowiedzi ustnej ${lvlTag}`, `Hodnocení ústního projevu ${lvlTag}`, `Hodnotenie ústneho prejavu ${lvlTag}`)}</h4>
                                <span class="cefr-score-badge">${_state.speakingResult.totalScore} / 25 ${_t('puntos', 'pont', 'points', 'punti')}</span>
                            </div>
                            <p>${_t('Palabras producidas:', 'Kimondott szavak száma:', 'Mots prononcés :', 'Parole pronunciate:')} <strong>${_state.speakingResult.wordCount}</strong></p>
                            <p>${_t('Conectores orales detectados:', 'Észlelt beszédkötőszavak:', 'Connecteurs détectés :', 'Connettivi rilevati:')} <em>${_esc(_state.speakingResult.foundConnectors.join(', ') || _t('Ninguno detectado', 'Egyik sem észlelhető', 'Aucun détecté', 'Nessuno rilevato'))}</em></p>
                        </div>
                    ` : ''}
                </div>
            `;
        }

        // Strategies Tab
        function _renderStrategiesTab() {
            if (!_data || !_data.strategies) return `<p class="cefr-empty">${_t('Guía no disponible.', 'Nincsenek elérhető stratégiák.', 'Guide non disponible.', 'Guida non disponibile.')}</p>`;
            const s = _data.strategies;
            const lvlTag = (_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : 'B1'));

            return `
                <div class="cefr-strategies-wrapper">
                    <h3 class="cefr-sec-title">${_esc(s.title || _t('Guía oficial del examen', 'Hivatalos vizsgaútmutató', "Guide officiel de l'examen", "Guida ufficiale dell'esame"))}</h3>
                    
                    <div class="cefr-strat-grid">
                        ${(s.structure || []).map(item => `
                            <div class="cefr-strat-card">
                                <h4>${_esc(item.prueba)}</h4>
                                <p>${_esc(item.tip)}</p>
                            </div>
                        `).join('')}
                    </div>

                    <div class="cefr-connectors-section">
                        <h4>${_t(`Conectores y marcadores del discurso (Nivel ${lvlTag})`, `Kötőszavak és szövegösszekötők (${lvlTag} szint)`, `Connecteurs et articulateurs logiques (Niveau ${lvlTag})`, `Connettivi e segnali discorsivi (Livello ${lvlTag})`, `Łączniki i wyznaczniki dyskursu (Poziom ${lvlTag})`, `Konektory a spojovací výrazy (Úroveň ${lvlTag})`, `Spojky a spájacie výrazy (Úroveň ${lvlTag})`)}</h4>
                        <div class="cefr-connectors-grid">
                            ${(s.connectors || []).map(cat => `
                                <div class="cefr-connector-card">
                                    <div class="cefr-conn-cat">${_esc(cat.category)}</div>
                                    <ul class="cefr-conn-list">
                                        ${cat.examples.map(ex => `<li>${_esc(ex)}</li>`).join('')}
                                    </ul>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            `;
        }

        // Mocks Tab
        function _renderMocksTab() {
            const isHu = _id.includes('hu');
            const lvl = (_data && _data.level) || (_id.includes('a1') ? 'A1' : (_id.includes('a2') ? 'A2' : (_id.includes('b2') ? 'B2' : 'B1')));
            const title = (_data && _data.title) || _t(`Prueba DELE ${lvl}`, `ECL ${lvl} Nyelvvizsga`, `Épreuve DELF ${lvl}`, `Esame CILS ${lvl}`, `Certyfikat Polski ${lvl}`, `Zkouška CCE ${lvl}`, `Skúška ECL ${lvl}`);
            const rTime = (_data && _data.skills && _data.skills.reading && _data.skills.reading.officialTimeMinutes) || 45;
            const wTime = (_data && _data.skills && _data.skills.writing && _data.skills.writing.officialTimeMinutes) || 45;
            const lTime = (_data && _data.skills && _data.skills.listening && _data.skills.listening.officialTimeMinutes) || 30;
            const sTime = (_data && _data.skills && _data.skills.speaking && _data.skills.speaking.officialTimeMinutes) || 15;
            const rTasks = (_data && _data.skills && _data.skills.reading && _data.skills.reading.tareas && _data.skills.reading.tareas.length) || 2;
            const wTasks = (_data && _data.skills && _data.skills.writing && _data.skills.writing.tareas && _data.skills.writing.tareas.length) || 2;
            const lTasks = (_data && _data.skills && _data.skills.listening && _data.skills.listening.tareas && _data.skills.listening.tareas.length) || 2;
            const sTasks = (_data && _data.skills && _data.skills.speaking && _data.skills.speaking.tareas && _data.skills.speaking.tareas.length) || 2;

            if (isHu) {
                return `
                    <div class="cefr-mocks-wrapper">
                        <div class="cefr-mock-intro-card">
                            <h3>Hivatalos ${_esc(title)} komplex próbavizsga (4 készség)</h3>
                            <p>A nemzetközi ECL vizsga négy különálló készséget mér fel, két fő vizsgarészre bontva:</p>
                            <div class="cefr-blocks-spec">
                                <div class="cefr-spec-card">
                                    <strong>1. rész: Írásbeli vizsga (50 pont)</strong>
                                    <ul>
                                        <li>Olvasásértés (${rTime} perc · ${rTasks} feladat · 25 pont)</li>
                                        <li>Írásbeli kommunikáció (${wTime} perc · ${wTasks} feladat · 25 pont)</li>
                                    </ul>
                                    <span class="cefr-pass-pill">Megfelelt: Legalább 30 / 50 pont (60%)</span>
                                </div>
                                <div class="cefr-spec-card">
                                    <strong>2. rész: Szóbeli vizsga (50 pont)</strong>
                                    <ul>
                                        <li>Hallásértés (${lTime} perc · ${lTasks} feladat · 25 pont)</li>
                                        <li>Szóbeli kommunikáció (${sTime} perc · ${sTasks} feladat · 25 pont)</li>
                                    </ul>
                                    <span class="cefr-pass-pill">Megfelelt: Legalább 30 / 50 pont (60%)</span>
                                </div>
                            </div>
                            <div class="cefr-mock-cta-wrap">
                                <button type="button" class="btn btn-primary cefr-mock-btn" data-action="start-full-mock">
                                    Teljes időmérős próbavizsga indítása
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }
            return `
                <div class="cefr-mocks-wrapper">
                    <div class="cefr-mock-intro-card">
                        <h3>${_t(`Simulacro oficial ${_esc(title)} completo (4 Destrezas)`, '', `Examen blanc complet ${_esc(title)} (4 Compétences)`, `Simulazione ufficiale ${_esc(title)} completa (4 Abilità)`, `Pełny egzamin próbny ${_esc(title)} (4 Sprawności)`, `Kompletní cvičná zkouška ${_esc(title)} (4 Dovednosti)`, `Kompletná skúšobná skúška ${_esc(title)} (4 Zručnosti)`)}</h3>
                        <p>${_t('El examen oficial evalúa las cuatro destrezas divididas en dos bloques:', '', "L'examen officiel évalue les quatre compétences réparties en deux pôles :", "L'esame ufficiale valuta le quattro abilità linguistiche:")}</p>
                        <div class="cefr-blocks-spec">
                            <div class="cefr-spec-card">
                                <strong>${_t('Bloque 1: Destrezas escritas (50 pts)', '', 'Pôle 1 : Compétences écrites (50 pts)', 'Parte 1: Abilità scritte (50 pt)')}</strong>
                                <ul>
                                    <li>${_t(`Comprensión de lectura (${rTime} min · 25 pts)`, '', `Compréhension des écrits (${rTime} min · 25 pts)`, `Comprensione della lettura (${rTime} min · 25 pt)`, `Rozumienie tekstów pisanych (${rTime} min · 25 pkt)`, `Čtení s porozuměním (${rTime} min · 25 b.)`, `Čítanie s porozumením (${rTime} min · 25 b.)`)}</li>
                                    <li>${_t(`Expresión escrita (${wTime} min · 25 pts)`, '', `Production écrite (${wTime} min · 25 pts)`, `Produzione scritta (${wTime} min · 25 pt)`, `Wypowiedź pisemna (${wTime} min · 25 pkt)`, `Psaní (${wTime} min · 25 b.)`, `Písomný prejav (${wTime} min · 25 b.)`)}</li>
                                </ul>
                                <span class="cefr-pass-pill">${_t('Apto: Mínimo 30 / 50 pts', '', 'Seuil de réussite : 30 / 50 pts', 'Idoneo: Minimo 30 / 50 pt')}</span>
                            </div>
                            <div class="cefr-spec-card">
                                <strong>${_t('Bloque 2: Destrezas orales (50 pts)', '', 'Pôle 2 : Compétences orales (50 pts)', 'Parte 2: Abilità orali (50 pt)')}</strong>
                                <ul>
                                    <li>${_t(`Comprensión auditiva (${lTime} min · 25 pts)`, '', `Compréhension de l'oral (${lTime} min · 25 pts)`, `Comprensione dell'ascolto (${lTime} min · 25 pt)`, `Rozumienie ze słuchu (${lTime} min · 25 pkt)`, `Poslech s porozuměním (${lTime} min · 25 b.)`, `Počúvanie s porozumením (${lTime} min · 25 b.)`)}</li>
                                    <li>${_t(`Expresión oral (${sTime} min · 25 pts)`, '', `Production orale (${sTime} min · 25 pts)`, `Produzione orale (${sTime} min · 25 pt)`, `Wypowiedź ustna (${sTime} min · 25 pkt)`, `Ústní část (${sTime} min · 25 b.)`, `Ústny prejav (${sTime} min · 25 b.)`)}</li>
                                </ul>
                                <span class="cefr-pass-pill">${_t('Apto: Mínimo 30 / 50 pts', '', 'Seuil de réussite : 30 / 50 pts', 'Idoneo: Minimo 30 / 50 pt')}</span>
                            </div>
                        </div>
                        <div class="cefr-mock-cta-wrap">
                            <button type="button" class="btn btn-primary cefr-mock-btn" data-action="start-full-mock">
                                ${_t('Iniciar simulacro completo cronometrado', '', "Lancer l'examen blanc complet", 'Avvia simulazione completa')}
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        // History Tab
        function _renderHistoryTab() {
            const prog = _loadProgress();
            const scores = prog.scores || {};

            let totalAttempted = 0;
            let sumScore = 0;
            let sumMax = 0;

            const rows = [];
            ['reading', 'listening', 'writing', 'speaking'].forEach(sk => {
                const skScores = scores[sk] || {};
                Object.keys(skScores).forEach(tid => {
                    totalAttempted++;
                    const rec = skScores[tid];
                    sumScore += rec.score;
                    sumMax += rec.maxScore;
                    rows.push({ skill: sk, tareaId: tid, rec: rec });
                });
            });

            const overallPct = sumMax > 0 ? Math.round((sumScore / sumMax) * 100) : 0;
            const passLabel = _t('APTO', 'MEGFELELT', 'ADMIS', 'IDONEO');
            const inProgLabel = _t('EN PROCESO', 'FOLYAMATBAN', 'EN COURS', 'IN CORSO');

            const skillNames = {
                reading: _t('Lectura', 'Olvasásértés', 'Écrits', 'Lettura'),
                listening: _t('Audición', 'Hallásértés', 'Oral (écoute)', 'Ascolto'),
                writing: _t('Escritura', 'Írásbeli', 'Production écrite', 'Scrittura'),
                speaking: _t('Oral', 'Szóbeli', 'Production orale', 'Orale')
            };

            return `
                <div class="cefr-history-wrapper">
                    <div class="cefr-history-summary">
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${totalAttempted}</span>
                            <span class="cefr-sum-label">${_t('Tareas realizadas', 'Elvégzett feladatok', 'Exercices réalisés', 'Prove completate')}</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct}%</span>
                            <span class="cefr-sum-label">${_t('Puntuación media', 'Átlagos eredmény', 'Score moyen', 'Punteggio medio')}</span>
                        </div>
                        <div class="cefr-sum-metric">
                            <span class="cefr-sum-val">${overallPct >= 60 ? passLabel : (totalAttempted > 0 ? inProgLabel : '–')}</span>
                            <span class="cefr-sum-label">${_t('Calificación global', 'Összesített értékelés', 'Résultat global', 'Esito complessivo')}</span>
                        </div>
                    </div>

                    <div class="cefr-history-table-card">
                        <h4>${_t('Registro detallado de tareas', 'Részletes feladateredmények', 'Détail des résultats par exercice', 'Registro dettagliato delle prove')}</h4>
                        ${rows.length === 0 ? `
                            <p class="cefr-empty">${_t("Aún no has completado ninguna tarea. Entrena en la pestaña 'Tareas oficiales'.", "Még nem fejeztél be egyetlen feladatot sem. Gyakorolj a 'Hivatalos feladattípusok' fülön!", "Vous n'avez encore terminé aucun exercice. Entraînez-vous dans l'onglet « Épreuves officielles ».", "Non hai ancora completato nessuna prova. Esercitati nella scheda 'Prove ufficiali'.")}</p>
                        ` : `
                            <table class="cefr-table">
                                <thead>
                                    <tr>
                                        <th>${_t('Destreza', 'Készség', 'Compétence', 'Abilità')}</th>
                                        <th>${_t('Tarea', 'Feladat', 'Exercice', 'Prova')}</th>
                                        <th>${_t('Puntos', 'Pontszám', 'Points', 'Punti')}</th>
                                        <th>${_t('Porcentaje', 'Százalék', 'Pourcentage', 'Percentuale')}</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    ${rows.map(r => `
                                        <tr>
                                            <td><strong>${_esc(skillNames[r.skill] || r.skill)}</strong></td>
                                            <td>${_esc(r.tareaId)}</td>
                                            <td>${r.rec.score} / ${r.rec.maxScore}</td>
                                            <td><span class="cefr-pct-badge ${r.rec.pct >= 60 ? 'is-pass' : 'is-fail'}">${r.rec.pct}%</span></td>
                                        </tr>
                                    `).join('')}
                                </tbody>
                            </table>
                        `}
                    </div>
                </div>
            `;
        }

        // ========================================
        // EVENT ATTACHMENTS
        // ========================================
        function _attachEvents(root) {
            // Main tabs
            root.querySelectorAll('[data-cefr-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.tab = btn.dataset.cefrTab;
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            });

            // Skill chips
            root.querySelectorAll('[data-cefr-skill]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.activeSkill = btn.dataset.cefrSkill;
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            });

            // Open Tarea card
            root.querySelectorAll('[data-cefr-open-tarea]').forEach(card => {
                card.addEventListener('click', () => {
                    _state.activeTareaId = card.dataset.cefrOpenTarea;
                    _state.readingSubmitted = false;
                    _state.listeningSubmitted = false;
                    _state.listeningPass = 1;
                    _state.listeningActiveItemId = null;
                    _state.listeningItemPasses = {};
                    _state.writingResult = null;
                    _state.speakingResult = null;
                    _state.writingDraftText = _loadDraft(_state.activeTareaId);
                    render(_container);
                });
            });

            // Back button in runner
            const backBtn = root.querySelector('[data-action="back-to-tasks"]');
            if (backBtn) {
                backBtn.addEventListener('click', () => {
                    _state.activeTareaId = null;
                    _stopListeningTimers();
                    _stopSpeakingStreams();
                    render(_container);
                });
            }

            // Reading Events
            root.querySelectorAll('[data-match-qid]').forEach(sel => {
                sel.addEventListener('change', () => {
                    _state.readingAnswers[sel.dataset.matchQid] = sel.value;
                });
            });

            root.querySelectorAll('[data-ans-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.ansQid] = parseInt(btn.dataset.ansIdx, 10);
                    render(_container);
                });
            });

            root.querySelectorAll('[data-stmt-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.stmtQid] = btn.dataset.stmtLetter;
                    render(_container);
                });
            });

            root.querySelectorAll('[data-gap-qid]').forEach(sel => {
                sel.addEventListener('change', () => {
                    _state.readingAnswers[sel.dataset.gapQid] = sel.value;
                });
            });

            root.querySelectorAll('[data-cloze-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.readingAnswers[btn.dataset.clozeQid] = parseInt(btn.dataset.clozeIdx, 10);
                    render(_container);
                });
            });

            const submitReadingBtn = root.querySelector('[data-action="submit-reading"]');
            if (submitReadingBtn) {
                submitReadingBtn.addEventListener('click', () => {
                    _state.readingSubmitted = true;
                    // Calculate reading score
                    const tarea = _getCurrentTarea();
                    let correctCount = 0;
                    let totalItems = 0;

                    if (tarea.type === 'matching-notices') {
                        totalItems = (tarea.people || []).length;
                        tarea.people.forEach(p => {
                            if (_state.readingAnswers[p.id] === p.correctNoticeId) correctCount++;
                        });
                    } else if (tarea.type === 'reading-mc') {
                        totalItems = (tarea.questions || []).length;
                        tarea.questions.forEach(q => {
                            if (_state.readingAnswers[q.id] === q.correct) correctCount++;
                        });
                    } else if (tarea.type === 'person-matching') {
                        totalItems = (tarea.statements || []).length;
                        tarea.statements.forEach(s => {
                            if (_state.readingAnswers[s.id] === s.correctPerson) correctCount++;
                        });
                    } else if (tarea.type === 'gapped-text') {
                        totalItems = (tarea.gaps || []).length;
                        tarea.gaps.forEach(g => {
                            if (_state.readingAnswers[g.id] === g.correct) correctCount++;
                        });
                    } else if (tarea.type === 'cloze-mc') {
                        totalItems = (tarea.items || []).length;
                        tarea.items.forEach(item => {
                            if (_state.readingAnswers[item.id] === item.correct) correctCount++;
                        });
                    }

                    _saveTaskScore('reading', tarea.id, correctCount, totalItems);
                    render(_container);
                });
            }

            const resetReadingBtn = root.querySelector('[data-action="reset-reading"]');
            if (resetReadingBtn) {
                resetReadingBtn.addEventListener('click', () => {
                    _state.readingAnswers = {};
                    _state.readingSubmitted = false;
                    render(_container);
                });
            }

            // Listening Events
            root.querySelectorAll('[data-action="play-single-item"]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const itemId = btn.dataset.itemId;
                    if (_state.listeningActiveItemId === itemId && _state.listeningPlaying) {
                        _stopListeningTimers();
                        render(_container);
                        return;
                    }

                    const tarea = _getCurrentTarea();
                    const item = (tarea.items || []).find(it => it.id === itemId);
                    if (!item || !item.audio || !item.audio.turns) return;

                    _stopListeningTimers();
                    _state.listeningActiveItemId = itemId;
                    _state.listeningPlaying = true;
                    _state.listeningItemPasses[itemId] = (_state.listeningItemPasses[item.id] || 0) + 1;
                    render(_container);

                    _playTurnSequence(item.audio.turns, 0, () => {
                        _state.listeningPlaying = false;
                        _state.listeningActiveItemId = null;
                        render(_container);
                    });
                });
            });

            root.querySelectorAll('[data-listen-qid]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.listeningAnswers[btn.dataset.listenQid] = parseInt(btn.dataset.listenIdx, 10);
                    render(_container);
                });
            });

            const submitListenBtn = root.querySelector('[data-action="submit-listening"]');
            if (submitListenBtn) {
                submitListenBtn.addEventListener('click', () => {
                    _state.listeningSubmitted = true;
                    _stopListeningTimers();
                    const tarea = _getCurrentTarea();
                    const items = tarea.items || tarea.questions || [];
                    let correct = 0;
                    items.forEach(q => {
                        if (_state.listeningAnswers[q.id] === q.correct) correct++;
                    });
                    _saveTaskScore('listening', tarea.id, correct, items.length);
                    render(_container);
                });
            }

            const resetListenBtn = root.querySelector('[data-action="reset-listening"]');
            if (resetListenBtn) {
                resetListenBtn.addEventListener('click', () => {
                    _state.listeningAnswers = {};
                    _state.listeningSubmitted = false;
                    _state.listeningPass = 1;
                    _state.listeningActiveItemId = null;
                    _state.listeningItemPasses = {};
                    _stopListeningTimers();
                    render(_container);
                });
            }

            // Writing Events
            const textarea = root.querySelector('#cefr-writing-textarea');
            if (textarea) {
                textarea.addEventListener('input', (e) => {
                    _state.writingDraftText = e.target.value;
                    _saveDraft(_state.activeTareaId, e.target.value);
                    const counter = root.querySelector('.cefr-word-counter strong');
                    if (counter) counter.textContent = _countWords(e.target.value);
                });
            }

            root.querySelectorAll('[data-writing-option]').forEach(btn => {
                btn.addEventListener('click', () => {
                    _state.writingActiveOption = btn.dataset.writingOption;
                    render(_container);
                });
            });

            const submitWritingBtn = root.querySelector('[data-action="submit-writing"]');
            if (submitWritingBtn) {
                submitWritingBtn.addEventListener('click', () => {
                    const tarea = _getCurrentTarea();
                    _state.writingResult = _evaluateWritingText(_state.writingDraftText, tarea);
                    _saveTaskScore('writing', tarea.id, _state.writingResult.totalScore, 25);
                    render(_container);
                });
            }

            // Speaking Events
            const micBtn = root.querySelector('[data-action="toggle-mic"]');
            if (micBtn) {
                micBtn.addEventListener('click', () => {
                    if (_state.speakingIsRecording) {
                        _stopSpeakingRecording();
                    } else {
                        _startSpeakingRecording();
                    }
                });
            }

            const transcriptInput = root.querySelector('#cefr-speaking-transcript-input');
            if (transcriptInput) {
                transcriptInput.addEventListener('input', (e) => {
                    _state.speakingTranscriptText = e.target.value;
                });
            }

            const submitSpeakingBtn = root.querySelector('[data-action="submit-speaking"]');
            if (submitSpeakingBtn) {
                submitSpeakingBtn.addEventListener('click', () => {
                    const tarea = _getCurrentTarea();
                    _state.speakingResult = _evaluateSpeakingText(_state.speakingTranscriptText, tarea);
                    _saveTaskScore('speaking', tarea.id, _state.speakingResult.totalScore, 25);
                    render(_container);
                });
            }

            // Mock CTA
            const mockCta = root.querySelector('[data-action="start-full-mock"]');
            if (mockCta) {
                mockCta.addEventListener('click', () => {
                    // Open first reading task as preview for mock exam
                    _state.tab = 'tasks';
                    _state.activeSkill = 'reading';
                    const skill = _data.skills.reading;
                    if (skill && skill.tareas && skill.tareas.length > 0) {
                        _state.activeTareaId = skill.tareas[0].id;
                    }
                    render(_container);
                });
            }
        }

        async function render(container) {
            _container = container || _container;
            if (!_container) return;

            await _loadData();

            let mainContentHtml = '';
            if (_state.activeTareaId) {
                mainContentHtml = _renderActiveTarea();
            } else if (_state.tab === 'tasks') {
                mainContentHtml = _renderTasksTab();
            } else if (_state.tab === 'strategies') {
                mainContentHtml = _renderStrategiesTab();
            } else if (_state.tab === 'mocks') {
                mainContentHtml = _renderMocksTab();
            } else if (_state.tab === 'history') {
                mainContentHtml = _renderHistoryTab();
            }

            _container.innerHTML = `
                <div class="cefr-exam-hub" data-exam-id="${_esc(_id)}">
                    <div class="cefr-header">
                        <div class="cefr-header-left">
                            <h2 class="cefr-title">${_esc(_data ? _data.title : config.title)}</h2>
                            <p class="cefr-subtitle">${_esc(_data ? _data.subtitle : config.subtitle)}</p>
                        </div>
                    </div>

                    ${!_state.activeTareaId ? _renderTabs() : ''}

                    <div class="cefr-body">
                        ${mainContentHtml}
                    </div>
                </div>
            `;

            _attachEvents(_container);

            if (_state.activeTareaId && _state.activeSkill === 'listening') {
                _updateListeningConsole();
            }
        }

        function stop() {
            _stopListeningTimers();
            _stopSpeakingStreams();
        }

        return {
            id: _id,
            render: render,
            stop: stop,
            // For tests/test-cefr-exam-production.js: the offline markers.
            _testHooks: {
                writing: (text, tarea) => _evaluateWritingText(text, tarea),
                speaking: (text, tarea, audio) => {
                    _state.speakingAudioBlobUrl = audio || null;
                    return _evaluateSpeakingText(text, tarea);
                }
            }
        };
    }

    const DeleA1Exam = createModule({
        id: 'es-dele-a1-exam',
        dataFile: 'dele-a1-exam.json',
        title: 'Prueba DELE A1',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial A1'
    });

    const DeleA2Exam = createModule({
        id: 'es-dele-a2-exam',
        dataFile: 'dele-a2-exam.json',
        title: 'Prueba DELE A2',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial A2'
    });

    const DeleB1Exam = createModule({
        id: 'es-dele-b1-exam',
        dataFile: 'dele-b1-exam.json',
        title: 'Prueba DELE B1',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial B1'
    });

    const DeleB2Exam = createModule({
        id: 'es-dele-b2-exam',
        dataFile: 'dele-b2-exam.json',
        title: 'Prueba DELE B2',
        subtitle: 'Diplomas de Español como Lengua Extranjera · Modelo Oficial B2'
    });

    const EclA1Exam = createModule({
        id: 'hu-ecl-a1-exam',
        dataFile: 'ecl-a1-exam.json',
        title: 'ECL A1 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · A1 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclA2Exam = createModule({
        id: 'hu-ecl-a2-exam',
        dataFile: 'ecl-a2-exam.json',
        title: 'ECL A2 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · A2 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclB1Exam = createModule({
        id: 'hu-ecl-b1-exam',
        dataFile: 'ecl-b1-exam.json',
        title: 'ECL B1 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · B1 szintű komplex nyelvvizsga-felkészítő'
    });

    const EclB2Exam = createModule({
        id: 'hu-ecl-b2-exam',
        dataFile: 'ecl-b2-exam.json',
        title: 'ECL B2 Nyelvvizsga',
        subtitle: 'Európai Közös Referenciakeret (KER) · B2 szintű komplex nyelvvizsga-felkészítő'
    });

    const CilsB1Exam = createModule({
        id: 'it-cils-exam',
        dataFile: 'cils-b1-exam.json',
        title: 'Esame CILS Uno-B1',
        subtitle: 'Certificazione di Italiano come Lingua Straniera · Quadro Comune Europeo (QCER B1)'
    });

    const DelfB1Exam = createModule({
        id: 'fr-delf-exam',
        dataFile: 'delf-b1-exam.json',
        title: 'Épreuve DELF B1',
        subtitle: "Diplôme d'études en langue française · Cadre européen commun de référence (CECRL B1)"
    });

    const PlCertyfikatB1Exam = createModule({
        id: 'pl-certyfikat-b1-exam',
        dataFile: 'certyfikat-b1-exam.json',
        title: 'Egzamin Certyfikat Polski B1',
        subtitle: 'Państwowa Komisja do spraw Poświadczania Znajomości Języka Polskiego · Poziom B1 (CEFR)'
    });

    const CsCceB1Exam = createModule({
        id: 'cs-cce-b1-exam',
        dataFile: 'cce-b1-exam.json',
        title: 'Certifikovaná zkouška z češtiny pro cizince B1 (CCE-B1)',
        subtitle: 'Ústav jazykové a odborné přípravy Univerzity Karlovy · Úroveň B1 (CEFR)'
    });

    const SkEclB1Exam = createModule({
        id: 'sk-ecl-b1-exam',
        dataFile: 'ecl-b1-exam.json',
        title: 'Medzinárodná skúška ECL zo slovenského jazyka B1',
        subtitle: 'Európske konzorcium pre certifikáciu znalostí moderných jazykov · Úroveň B1 (CEFR)'
    });

    return {
        createModule: createModule,
        DeleA1Exam: DeleA1Exam,
        DeleA2Exam: DeleA2Exam,
        DeleB1Exam: DeleB1Exam,
        DeleB2Exam: DeleB2Exam,
        EclA1Exam: EclA1Exam,
        EclA2Exam: EclA2Exam,
        EclB1Exam: EclB1Exam,
        EclB2Exam: EclB2Exam,
        CilsB1Exam: CilsB1Exam,
        DelfB1Exam: DelfB1Exam,
        PlCertyfikatB1Exam: PlCertyfikatB1Exam,
        CsCceB1Exam: CsCceB1Exam,
        SkEclB1Exam: SkEclB1Exam
    };
})();

// Export globally and for CommonJS tests
if (typeof window !== 'undefined') {
    window.CefrExam = CefrExam;
    window.DeleA1Exam = CefrExam.DeleA1Exam;
    window.DeleA2Exam = CefrExam.DeleA2Exam;
    window.DeleB1Exam = CefrExam.DeleB1Exam;
    window.DeleB2Exam = CefrExam.DeleB2Exam;
    window.EclA1Exam = CefrExam.EclA1Exam;
    window.EclA2Exam = CefrExam.EclA2Exam;
    window.EclB1Exam = CefrExam.EclB1Exam;
    window.EclB2Exam = CefrExam.EclB2Exam;
    window.CilsB1Exam = CefrExam.CilsB1Exam;
    window.DelfB1Exam = CefrExam.DelfB1Exam;
    window.PlCertyfikatB1Exam = CefrExam.PlCertyfikatB1Exam;
    window.CsCceB1Exam = CefrExam.CsCceB1Exam;
    window.SkEclB1Exam = CefrExam.SkEclB1Exam;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CefrExam;
}
