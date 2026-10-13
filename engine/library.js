// ============================================
// LIBRARY
// ============================================
// The Library is where a learner reads whatever they want to read in
// their target language, per PARLOUR_LIBRARY_SPEC.md. Three sections share
// one reading view (engine/reader.js's #reader-content, via
// makeClickable/showWord — nothing here reimplements tap-to-define):
//
//   Parlour   — curated readings, engine/reader.js's existing manifest-driven
//               library. Read-only; this module never touches it beyond
//               reading Reader.stories and re-rendering it on return.
//   Saved     — story ids the learner has bookmarked out of Parlour. Stores
//               the id only, never a copy of the reading.
//   My Texts  — texts and books (.epub, .docx, .txt, .md, or pasted prose)
//               the learner brings in themselves. Fully owned here:
//               file import, automatic chaptering, IndexedDB chapter storage,
//               chapter table of contents, per-chapter reading view, and
//               persistent reading location (chapter + paragraph + scroll %).
//
// Library does not own SRS or vocabulary — reading a text, however
// unfamiliar, never adds anything to a deck by itself. That stays an
// explicit action (Add to deck, or the vocabulary-selection panel below),
// same principle as PARLOUR_DECKS_SPEC.md: the learner decides what's worth
// keeping.

const Library = (function () {
    'use strict';

    const PANES = { parlour: 'reader-library', saved: 'lib-saved', mytexts: 'lib-mytexts' };

    // Auto-chunking thresholds for unchaptered or very long chapters:
    // any chapter over CHUNK_TRIGGER_WORDS is split at paragraph boundaries
    // into ~CHUNK_TARGET_WORDS parts so DOM tokenization stays fast and
    // bookmarkable on mobile devices.
    const CHUNK_TRIGGER_WORDS = 3500;
    const CHUNK_TARGET_WORDS = 2500;
    const INLINE_TEXT_MAX_CHARS = 12000;

    let activeSection = 'parlour';
    let savedIds = [];          // story ids, resolved against Reader.stories at render time
    let myTexts = [];           // lightweight metadata in localStorage; heavy chapter bodies live in BookStore
    let textDraft = null;       // { id, title, author, sourceType, text, chapters, analysis, fileLabel } while editor is open
    let activeBookId = null;    // id of the multi-chapter book whose TOC is open in #lib-mytexts
    let activeReading = null;   // { id, chapterIndex } while #reader-content is displaying a My Text chapter

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
    }

    function withArticle(lemma) {
        return (typeof Lexicon !== 'undefined') ? Lexicon.withArticle(lemma) : lemma;
    }

    // ----------------------------------------
    // INDEXEDDB BOOK STORE (chapters + lemmas)
    // ----------------------------------------
    // Keeps multi-chapter book bodies and 5,000-word lemma arrays out of
    // localStorage's 5 MB quota and Cloud Sync snapshots. Each book's
    // localStorage entry stays ~1.5 KB (metadata, chapter titles, progress),
    // allowing 500+ full-length novels per device.
    const DB_NAME = 'parlour_library_db';
    const DB_VERSION = 1;
    const STORE_NAME = 'books';
    const memBookStore = new Map();
    let dbPromise = null;

    function bookStoreKey(textId) {
        const prefix = (typeof Lang !== 'undefined' && Lang.key) ? Lang.key('book') : 'es:book';
        return prefix + ':' + textId;
    }

    function openDb() {
        if (dbPromise) return dbPromise;
        if (typeof indexedDB === 'undefined' || !indexedDB) {
            dbPromise = Promise.resolve(null);
            return dbPromise;
        }
        dbPromise = new Promise(resolve => {
            try {
                const req = indexedDB.open(DB_NAME, DB_VERSION);
                req.onupgradeneeded = e => {
                    const db = e.target.result;
                    if (!db.objectStoreNames.contains(STORE_NAME)) {
                        db.createObjectStore(STORE_NAME, { keyPath: 'key' });
                    }
                };
                req.onsuccess = e => resolve(e.target.result);
                req.onerror = () => resolve(null);
            } catch (e) {
                resolve(null);
            }
        });
        return dbPromise;
    }

    async function saveBookPayload(textId, payload) {
        const key = bookStoreKey(textId);
        const record = {
            key: key,
            chapters: payload.chapters || [],
            lemmas: payload.lemmas || null,
            updated: Date.now()
        };
        memBookStore.set(key, record);
        const db = await openDb();
        if (!db) return;
        return new Promise(resolve => {
            try {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                tx.objectStore(STORE_NAME).put(record);
                tx.oncomplete = () => resolve();
                tx.onerror = () => resolve();
            } catch (e) {
                resolve();
            }
        });
    }

    async function loadBookPayload(textId) {
        const key = bookStoreKey(textId);
        if (memBookStore.has(key)) return memBookStore.get(key);
        const db = await openDb();
        if (!db) return null;
        return new Promise(resolve => {
            try {
                const tx = db.transaction(STORE_NAME, 'readonly');
                const req = tx.objectStore(STORE_NAME).get(key);
                req.onsuccess = () => {
                    if (req.result) memBookStore.set(key, req.result);
                    resolve(req.result || null);
                };
                req.onerror = () => resolve(null);
            } catch (e) {
                resolve(null);
            }
        });
    }

    async function deleteBookPayload(textId) {
        const key = bookStoreKey(textId);
        memBookStore.delete(key);
        const db = await openDb();
        if (!db) return;
        return new Promise(resolve => {
            try {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                tx.objectStore(STORE_NAME).delete(key);
                tx.oncomplete = () => resolve();
                tx.onerror = () => resolve();
            } catch (e) {
                resolve();
            }
        });
    }

    // Resolves the full chapter objects ([{ index, title, paragraphs, wordCount, estimatedMinutes }])
    // for a My Text item, falling back to inline t.text for legacy or short pasted texts.
    async function resolveBookChapters(t) {
        if (!t) return [];
        const payload = await loadBookPayload(t.id);
        if (payload && Array.isArray(payload.chapters) && payload.chapters.length) {
            return payload.chapters;
        }
        if (t.text) {
            const built = buildChaptersFromText(t.text, t.title);
            await saveBookPayload(t.id, {
                chapters: built,
                lemmas: (t.analysis && t.analysis.lemmas) || null
            });
            return built;
        }
        return [];
    }

    // ----------------------------------------
    // SAVED — bookmarks into the Parlour catalogue
    // ----------------------------------------
    const savedKey = () => Lang.key('savedReadings');

    function loadSaved() {
        try {
            savedIds = JSON.parse(localStorage.getItem(savedKey()) || '[]');
        } catch (error) {
            savedIds = [];
        }
    }

    function saveSaved() {
        localStorage.setItem(savedKey(), JSON.stringify(savedIds));
    }

    function isSaved(storyId) {
        return savedIds.includes(storyId);
    }

    // Returns the new saved state, so callers (the in-reading Save button)
    // can update their own label without a full re-render.
    function toggleSave(storyId) {
        if (!storyId) return false;
        const at = savedIds.indexOf(storyId);
        if (at === -1) { savedIds.push(storyId); } else { savedIds.splice(at, 1); }
        saveSaved();
        return at === -1;
    }

    async function renderSavedList() {
        const host = document.getElementById('lib-saved');
        if (!host) return;

        await Reader.ensureStories();
        const readIds = (typeof getReadStoryIds === 'function') ? getReadStoryIds() : [];
        const stories = savedIds
            .map(id => Reader.stories.find(s => s.id === id))
            .filter(Boolean);

        host.innerHTML = stories.length
            ? `<div class="story-grid">${stories.map(s => savedCardHtml(s, readIds.includes(s.id))).join('')}</div>`
            : '<p class="dk-empty">No saved readings yet. Open one from Parlour and tap Save.</p>';
    }

    function savedCardHtml(story, isRead) {
        const art = (typeof pathArt === 'function' && typeof coverArtIndexFor === 'function')
            ? pathArt(coverArtIndexFor(story.id), 'story-card-cover-icon')
            : '';
        const withinReach = !isRead && (typeof Reader !== 'undefined' && typeof Reader.isStoryWithinReach === 'function')
            ? Reader.isStoryWithinReach(story, [story.id].filter(() => isRead))
            : false;
        const comp = (typeof Reader !== 'undefined' && typeof Reader.getComprehension === 'function')
            ? Reader.getComprehension(story.id)
            : null;
        const compBadge = comp ? `<span class="story-card-comp-badge" title="Quiz: ${comp.correct}/${comp.total}">Quiz ${comp.correct}/${comp.total} ✓</span>` : '';

        return `
            <div class="story-card lt-saved-card">
                <button class="story-card-open" data-saved-open="${esc(story.id)}">
                    <div class="story-card-cover">
                        ${art}
                        ${isRead ? '<span class="story-card-read-badge" title="Read">✓</span>' : ''}
                    </div>
                    <div class="story-card-body">
                        <div class="story-card-title">${esc(story.title)}</div>
                        <div class="story-card-meta">
                            ${withinReach ? '<span class="story-card-reach-badge">Within Reach</span>' : ''}
                            ${compBadge}
                        </div>
                    </div>
                </button>
                <button class="lt-saved-remove" data-saved-remove="${esc(story.id)}">Remove from Saved</button>
            </div>
        `;
    }

    // ----------------------------------------
    // MY TEXTS — data & storage migration
    // ----------------------------------------
    const myTextsKey = () => Lang.key('myTexts');

    function compactAnalysis(a) {
        if (!a) return null;
        return {
            totalWords: a.totalWords || 0,
            estimatedMinutes: a.estimatedMinutes || 1,
            level: a.level || null,
            recognizedUnique: a.recognizedUnique || 0,
            unrecognizedUnique: a.unrecognizedUnique || 0,
            familiar: a.familiar || 0,
            notYetLearned: a.notYetLearned || 0,
            inDecks: a.inDecks || 0,
            due: a.due || 0,
            familiarPercent: a.familiarPercent || 0
        };
    }

    function compactChaptersMeta(chapters) {
        if (!Array.isArray(chapters)) return [];
        return chapters.map((ch, idx) => {
            const meta = {
                index: idx,
                title: ch.title || ('Part ' + (idx + 1)),
                wordCount: ch.wordCount || 0,
                estimatedMinutes: ch.estimatedMinutes || Math.max(1, Math.round((ch.wordCount || 0) / READING_WPM))
            };
            if (ch.subtitle) meta.subtitle = ch.subtitle;
            return meta;
        });
    }

    function loadMyTexts() {
        try {
            myTexts = JSON.parse(localStorage.getItem(myTextsKey()) || '[]');
        } catch (error) {
            myTexts = [];
        }
        // Migrate legacy entries that stored full lemmas arrays or unchaptered
        // long texts directly in localStorage.
        let migrated = false;
        myTexts.forEach(t => {
            if (!t.progress) {
                t.progress = { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: 0 };
            } else if (!Array.isArray(t.progress.readChapters)) {
                t.progress.readChapters = [];
            }
            if (!Array.isArray(t.chapters) && t.text) {
                const built = buildChaptersFromText(t.text, t.title);
                t.chapters = compactChaptersMeta(built);
                const lemmas = (t.analysis && t.analysis.lemmas) || null;
                saveBookPayload(t.id, { chapters: built, lemmas: lemmas });
                if (t.text.length > INLINE_TEXT_MAX_CHARS || built.length > 1) {
                    delete t.text;
                }
                migrated = true;
            }
            if (t.analysis && Array.isArray(t.analysis.lemmas)) {
                const lemmas = t.analysis.lemmas;
                t.analysis = compactAnalysis(t.analysis);
                loadBookPayload(t.id).then(existing => {
                    const chs = (existing && existing.chapters) || (t.text ? buildChaptersFromText(t.text, t.title) : []);
                    saveBookPayload(t.id, { chapters: chs, lemmas: lemmas });
                });
                migrated = true;
            }
        });
        if (migrated) saveMyTexts();
    }

    function saveMyTexts() {
        try {
            localStorage.setItem(myTextsKey(), JSON.stringify(myTexts));
        } catch (e) {
            if (typeof UI !== 'undefined' && UI.toast) {
                UI.toast('Browser storage is full. Try deleting unused texts.', 'error');
            }
        }
    }

    function genTextId() {
        return 'text-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
    }

    function listMyTexts() {
        return myTexts.slice().sort((a, b) => {
            const aTouch = (a.progress && a.progress.at) || new Date(a.modified || 0).getTime();
            const bTouch = (b.progress && b.progress.at) || new Date(b.modified || 0).getTime();
            return bTouch - aTouch;
        });
    }

    function getMyText(id) {
        return myTexts.find(t => t.id === id);
    }

    // ----------------------------------------
    // MY TEXTS — analysis
    // ----------------------------------------
    const WORD_RE = /[a-zA-ZáéíóúÁÉÍÓÚñÑüÜöÖőŐűŰ\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u024f]+/g;
    function tokenizeWords(text) {
        return (text || '').match(WORD_RE) || [];
    }

    const READING_WPM = 100;

    function estimateLevel(lemmas) {
        if (typeof Lexicon === 'undefined' || !Lexicon.frequencyRank) return null;
        const ranks = [];
        lemmas.forEach(lemma => {
            const r = Lexicon.frequencyRank(lemma);
            if (r !== null && r !== undefined) ranks.push(r);
        });
        if (ranks.length < 15) return null;
        ranks.sort((a, b) => a - b);
        const p80 = ranks[Math.min(ranks.length - 1, Math.floor(ranks.length * 0.8))];
        if (p80 < 600) return 'A1';
        if (p80 < 1500) return 'A2';
        if (p80 < 4000) return 'B1';
        if (p80 < 9000) return 'B2';
        return 'C1';
    }

    function analyseText(text) {
        const tokens = tokenizeWords(text);
        const totalWords = tokens.length;

        const seenSurface = new Set();
        const lemmaMap = new Map();
        let unrecognizedUnique = 0;

        tokens.forEach(tok => {
            const surface = tok.toLowerCase();
            if (seenSurface.has(surface)) return;
            seenSurface.add(surface);
            const readings = (typeof Lexicon !== 'undefined' && (!Lexicon.isLoaded || Lexicon.isLoaded()))
                ? Lexicon.lookup(tok).readings : [];
            if (readings.length) {
                const r = readings[0];
                const lemma = r.lemma.toLowerCase();
                if (!lemmaMap.has(lemma)) {
                    lemmaMap.set(lemma, { lemma: lemma, translation: Lexicon.shortGloss(r.translation), pos: r.pos });
                }
            } else {
                unrecognizedUnique++;
            }
        });

        const now = new Date();
        const deck = (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) ? srsDeck : [];
        const myDeckLemmas = (typeof Decks !== 'undefined' && Decks.allMyDeckLemmas)
            ? Decks.allMyDeckLemmas() : new Set();

        let familiarCount = 0, notYetLearnedCount = 0, inDecksCount = 0, dueCount = 0;
        const lemmas = [];
        lemmaMap.forEach(item => {
            const card = deck.find(c => ((typeof Lang !== 'undefined' && Lang.targetLemma) ? Lang.targetLemma(c) : c.spanish) === item.lemma);
            const familiar = !!(card && (card.reviews || 0) >= 1) ||
                (typeof isKnown === 'function' && isKnown(item.lemma));
            const isNew = !card;
            const due = !!(card && (!card.nextReview || new Date(card.nextReview) <= now));
            const inDeckList = myDeckLemmas.has(item.lemma);

            if (familiar) familiarCount++;
            if (isNew) notYetLearnedCount++;
            if (due) dueCount++;
            if (inDeckList) inDecksCount++;

            lemmas.push(Object.assign({}, item, { familiar, isNew, due, inDeck: inDeckList }));
        });

        const recognizedUnique = lemmaMap.size;

        return {
            totalWords: totalWords,
            estimatedMinutes: Math.max(1, Math.round(totalWords / READING_WPM)),
            level: estimateLevel(Array.from(lemmaMap.keys())),
            recognizedUnique: recognizedUnique,
            unrecognizedUnique: unrecognizedUnique,
            familiar: familiarCount,
            notYetLearned: notYetLearnedCount,
            inDecks: inDecksCount,
            due: dueCount,
            familiarPercent: recognizedUnique ? Math.round((familiarCount / recognizedUnique) * 100) : 0,
            lemmas: lemmas
        };
    }

    // ----------------------------------------
    // CHAPTER SPLITTING & AUTO-CHUNKING
    // ----------------------------------------
    function splitParagraphs(text) {
        return String(text || '').replace(/\r\n?/g, '\n').split(/\n\s*\n/).map(p => p.trim()).filter(Boolean);
    }

    const CHAPTER_HEADING_RE = /^(?:#{1,3}\s+(.+)|((?:chapter|capítulo|capitulo|fejezet|part|parte|rész|book|libro|könyv)\s+(?:\d+|[ivxlcdm]+|[a-záéíóúñüöőű]+)(?:\s*[:.\-—–]\s*.*)?)|([IVXLCDM]{1,7})\.?)$/i;

    function detectHeadingLine(para) {
        const lines = para.split('\n').map(l => l.trim()).filter(Boolean);
        if (!lines.length) return null;
        const first = lines[0];
        if (first.length > 90) return null;
        const m = first.match(CHAPTER_HEADING_RE);
        if (!m) return null;
        const title = (m[1] || m[2] || ('Chapter ' + m[3])).trim();
        const rest = lines.slice(1).join('\n').trim();
        return { title: title, remainder: rest };
    }

    function finalizeChapterList(rawChapters, fallbackTitle) {
        const result = [];
        const nonEmpty = (rawChapters || []).filter(ch => ch && Array.isArray(ch.paragraphs) && ch.paragraphs.length > 0);
        if (!nonEmpty.length) return [];

        nonEmpty.forEach((ch, idx) => {
            const baseTitle = (ch.title || '').trim() || (nonEmpty.length === 1 ? (fallbackTitle || 'Part 1') : ('Chapter ' + (idx + 1)));
            const subtitle = (ch.subtitle || '').trim();
            const paraWordCounts = ch.paragraphs.map(p => tokenizeWords(p).length);
            const totalChapterWords = paraWordCounts.reduce((a, b) => a + b, 0);

            // Auto-chunking: split chapters over CHUNK_TRIGGER_WORDS into ~CHUNK_TARGET_WORDS parts
            if (totalChapterWords > CHUNK_TRIGGER_WORDS && ch.paragraphs.length > 1) {
                const subChunks = [];
                let curParas = [];
                let curWords = 0;

                ch.paragraphs.forEach((p, pIdx) => {
                    const w = paraWordCounts[pIdx];
                    if (curWords >= CHUNK_TARGET_WORDS && curParas.length > 0) {
                        subChunks.push({ paragraphs: curParas, wordCount: curWords });
                        curParas = [];
                        curWords = 0;
                    }
                    curParas.push(p);
                    curWords += w;
                });
                if (curParas.length > 0) {
                    // Merge a tiny trailing remainder (< 500 words) into the previous chunk
                    if (subChunks.length > 0 && curWords < 500) {
                        const prev = subChunks[subChunks.length - 1];
                        prev.paragraphs = prev.paragraphs.concat(curParas);
                        prev.wordCount += curWords;
                    } else {
                        subChunks.push({ paragraphs: curParas, wordCount: curWords });
                    }
                }

                subChunks.forEach((sc, scIdx) => {
                    const partTitle = nonEmpty.length === 1
                        ? 'Part ' + (scIdx + 1)
                        : `${baseTitle} (${scIdx + 1}/${subChunks.length})`;
                    const entry = {
                        index: result.length,
                        title: partTitle,
                        paragraphs: sc.paragraphs,
                        wordCount: sc.wordCount,
                        estimatedMinutes: Math.max(1, Math.round(sc.wordCount / READING_WPM))
                    };
                    if (subtitle) entry.subtitle = subtitle;
                    result.push(entry);
                });
            } else {
                const entry = {
                    index: result.length,
                    title: baseTitle,
                    paragraphs: ch.paragraphs,
                    wordCount: totalChapterWords,
                    estimatedMinutes: Math.max(1, Math.round(totalChapterWords / READING_WPM))
                };
                if (subtitle) entry.subtitle = subtitle;
                result.push(entry);
            }
        });

        return result;
    }

    function buildChaptersFromText(text, fallbackTitle) {
        const rawParas = splitParagraphs(text);
        if (!rawParas.length) return [];

        const rawChapters = [];
        let current = { title: '', paragraphs: [] };

        rawParas.forEach(p => {
            const heading = detectHeadingLine(p);
            if (heading) {
                if (current.paragraphs.length > 0) {
                    rawChapters.push(current);
                }
                current = {
                    title: heading.title,
                    paragraphs: heading.remainder ? [heading.remainder] : []
                };
            } else {
                // Convert single newlines inside a paragraph to spaces unless dialogue lines
                const lines = p.split('\n').map(l => l.trim()).filter(Boolean);
                if (lines.length > 1 && lines.every(l => /^[-—–«"“]/.test(l))) {
                    lines.forEach(l => current.paragraphs.push(l));
                } else {
                    current.paragraphs.push(lines.join(' '));
                }
            }
        });
        if (current.paragraphs.length > 0) {
            rawChapters.push(current);
        }

        return finalizeChapterList(rawChapters, fallbackTitle);
    }

    // ----------------------------------------
    // CLIENT-SIDE ZIP / EPUB / DOCX PARSER
    // ----------------------------------------
    async function inflateRawBytes(compressedBytes) {
        if (typeof DecompressionStream !== 'undefined') {
            const ds = new DecompressionStream('deflate-raw');
            const writer = ds.writable.getWriter();
            writer.write(compressedBytes);
            writer.close();
            const reader = ds.readable.getReader();
            const chunks = [];
            let totalLen = 0;
            while (true) {
                const step = await reader.read();
                if (step.done) break;
                chunks.push(step.value);
                totalLen += step.value.byteLength;
            }
            const out = new Uint8Array(totalLen);
            let offset = 0;
            for (const c of chunks) {
                out.set(c, offset);
                offset += c.byteLength;
            }
            return out;
        }
        if (typeof require === 'function') {
            const zlib = require('zlib');
            return new Uint8Array(zlib.inflateRawSync(Buffer.from(compressedBytes)));
        }
        throw new Error('This browser does not support DecompressionStream for zipped files.');
    }

    async function unpackZip(arrayBuffer) {
        const bytes = new Uint8Array(arrayBuffer);
        const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);

        // Find End of Central Directory (0x06054b50) scanning backwards from the end
        let eocdOffset = -1;
        const minSearch = Math.max(0, bytes.length - 65557);
        for (let i = bytes.length - 22; i >= minSearch; i--) {
            if (view.getUint32(i, true) === 0x06054b50) {
                eocdOffset = i;
                break;
            }
        }
        if (eocdOffset === -1) {
            throw new Error('Invalid file archive (central directory not found).');
        }

        const totalEntries = view.getUint16(eocdOffset + 10, true);
        const cdOffset = view.getUint32(eocdOffset + 16, true);
        const decoder = new TextDecoder('utf-8');
        const entries = new Map();

        let ptr = cdOffset;
        for (let i = 0; i < totalEntries && ptr + 46 <= bytes.length; i++) {
            if (view.getUint32(ptr, true) !== 0x02014b50) break;
            const method = view.getUint16(ptr + 10, true);
            const compSize = view.getUint32(ptr + 20, true);
            const nameLen = view.getUint16(ptr + 28, true);
            const extraLen = view.getUint16(ptr + 30, true);
            const commentLen = view.getUint16(ptr + 32, true);
            const localHeaderOffset = view.getUint32(ptr + 42, true);

            const rawName = decoder.decode(bytes.subarray(ptr + 46, ptr + 46 + nameLen));
            const normName = rawName.replace(/\\/g, '/').replace(/^\/+/, '');

            entries.set(normName, {
                name: normName,
                method: method,
                compSize: compSize,
                localHeaderOffset: localHeaderOffset
            });

            ptr += 46 + nameLen + extraLen + commentLen;
        }

        async function getBytes(path) {
            const clean = String(path || '').replace(/\\/g, '/').replace(/^\/+/, '');
            let entry = entries.get(clean);
            if (!entry) {
                const lower = clean.toLowerCase();
                for (const [k, v] of entries.entries()) {
                    if (k.toLowerCase() === lower) { entry = v; break; }
                }
            }
            if (!entry) return null;

            const lh = entry.localHeaderOffset;
            if (lh + 30 > bytes.length || view.getUint32(lh, true) !== 0x04034b50) return null;
            const lhNameLen = view.getUint16(lh + 26, true);
            const lhExtraLen = view.getUint16(lh + 28, true);
            const dataStart = lh + 30 + lhNameLen + lhExtraLen;
            const slice = bytes.subarray(dataStart, dataStart + entry.compSize);

            if (entry.method === 0) return slice;
            if (entry.method === 8) return await inflateRawBytes(slice);
            throw new Error('Unsupported ZIP compression method: ' + entry.method);
        }

        async function getText(path) {
            const raw = await getBytes(path);
            if (!raw) return null;
            return decoder.decode(raw);
        }

        return { entries, getBytes, getText };
    }

    function resolveRelativeZipPath(baseDir, href) {
        if (!href) return '';
        const noHash = href.split('#')[0];
        let decoded = noHash;
        try { decoded = decodeURIComponent(noHash); } catch (e) {}
        const combined = (baseDir ? baseDir + '/' : '') + decoded;
        const parts = combined.split('/');
        const stack = [];
        for (const p of parts) {
            if (!p || p === '.') continue;
            if (p === '..') stack.pop();
            else stack.push(p);
        }
        return stack.join('/');
    }

    function decodeXmlEntities(str) {
        return String(str || '')
            .replace(/&nbsp;/gi, ' ')
            .replace(/&apos;/gi, "'")
            .replace(/&quot;/gi, '"')
            .replace(/&gt;/gi, '>')
            .replace(/&lt;/gi, '<')
            .replace(/&amp;/gi, '&')
            .replace(/&#(\d+);/g, (_, dec) => String.fromCharCode(parseInt(dec, 10)))
            .replace(/&#x([0-9a-fA-F]+);/g, (_, hex) => String.fromCharCode(parseInt(hex, 16)));
    }

    function parseXmlAttrs(attrString) {
        const attrs = {};
        const re = /([a-zA-Z0-9_:\-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g;
        let m;
        while ((m = re.exec(attrString || '')) !== null) {
            const key = m[1];
            const val = decodeXmlEntities(m[2] !== undefined ? m[2] : m[3]);
            attrs[key] = val;
            const localKey = key.includes(':') ? key.split(':').pop() : key;
            if (attrs[localKey] === undefined) attrs[localKey] = val;
        }
        return attrs;
    }

    function firstXmlTagText(xml, localTagName) {
        const re = new RegExp(`<(?:[a-zA-Z0-9_\\-]+:)?${localTagName}(?:\\s[^>]*)?>([\\s\\S]*?)<\\/(?:[a-zA-Z0-9_\\-]+:)?${localTagName}>`, 'i');
        const m = String(xml || '').match(re);
        return m ? decodeXmlEntities(m[1].replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim() : '';
    }

    const EPUB_BOILERPLATE_CLASS_RE = /(?:^|[\s_-])(?:cubierta|portada|cover|sinopsis|synopsis|info|creditos|credits|copyright|colophon|dedicatoria|dedication|exlibris|bloque_exlibris|tlogo|ttitulo|titlepage|title-page|halftitle|frontmatter|backmatter|autor|about-author)(?:$|[\s_-])/i;
    const EPUB_SUBTITLE_CLASS_RE = /(?:^|[\s_-])(?:subtit|subtitle|subtitulo|chap-sub|chapter-subtitle|ch-sub)(?:$|[\s_-])/i;
    const EPUB_BOILERPLATE_STEM_RE = /^(?:cubierta|portada|cover|titulo|title|titlepage|title[_-]page|halftitle|half[_-]title|info|creditos|credits|copyright|legal|colophon|sinopsis|synopsis|resumen|dedicatoria|dedication|epigrafe|epigraph|exlibris|agradecimientos|acknowledg(?:e)?ments|autor|author|biografia|bio|indice|toc|nav)$/i;
    const EPUB_GUIDE_BOILERPLATE_RE = /^(?:cover|title-page|titlepage|halftitlepage|copyright-page|colophon|dedication|epigraph|toc|acknowledg(?:e)?ments|bibliography|index|glossary|other\.(?:halftitlepage|credits|copyright|backmatter|frontmatter))$/i;

    function extractHtmlParagraphsAndTitle(xhtmlString) {
        const rawStr = String(xhtmlString || '');
        const isBoilerplateMarkup = /<(?:body|div|section)\b[^>]*(?:class|epub:type)\s*=\s*["'][^"']*(?:cubierta|portada|cover|sinopsis|synopsis|info|creditos|copyright|colophon|dedicatoria|dedication|bloque_exlibris|tlogo|ttitulo|titlepage|halftitle|frontmatter|autor|about-author)[^"']*["']/i.test(rawStr);

        if (typeof DOMParser !== 'undefined') {
            const doc = new DOMParser().parseFromString(rawStr, 'text/html');
            if (doc && doc.body) {
                const headTitleEl = doc.querySelector('head > title');
                const headTitle = headTitleEl ? headTitleEl.textContent.replace(/\s+/g, ' ').trim() : '';
                doc.querySelectorAll('script, style, svg, nav, head, noscript, iframe').forEach(el => el.remove());

                let detectedTitle = '';
                const headingEl = doc.querySelector('h1, h2, h3, [class*="title"], [class*="chapter"]');
                if (headingEl) {
                    const hText = (headingEl.textContent || headingEl.getAttribute('title') || '').replace(/\s+/g, ' ').trim();
                    if (hText && hText.length <= 120) detectedTitle = hText;
                }
                if (!detectedTitle && headTitle && headTitle.length <= 120 && !/^ignored$/i.test(headTitle)) {
                    detectedTitle = headTitle;
                }

                let detectedSubtitle = '';
                const paragraphs = [];
                const blocks = doc.querySelectorAll('p, h1, h2, h3, h4, h5, h6, blockquote, li');
                if (blocks.length > 0) {
                    blocks.forEach(el => {
                        if (el.tagName !== 'P' && el.querySelector('p')) return;
                        const txt = el.textContent.replace(/\s+/g, ' ').trim();
                        if (!txt) return;
                        if (paragraphs.length === 0 && !detectedSubtitle) {
                            if (el === headingEl || txt.toLowerCase() === (detectedTitle || '').toLowerCase()) return;
                            const cls = el.getAttribute('class') || '';
                            const isSubHeading = (EPUB_SUBTITLE_CLASS_RE.test(cls) || (headingEl && headingEl.tagName === 'H1' && (el.tagName === 'H2' || el.tagName === 'H3')));
                            if (isSubHeading && txt.length <= 160) {
                                detectedSubtitle = txt;
                                return;
                            }
                        }
                        paragraphs.push(txt);
                    });
                } else {
                    const raw = (doc.body.innerText || doc.body.textContent || '');
                    splitParagraphs(raw).forEach(p => {
                        const clean = p.replace(/\s+/g, ' ').trim();
                        if (clean && clean !== detectedTitle) paragraphs.push(clean);
                    });
                }
                return { title: detectedTitle, subtitle: detectedSubtitle, paragraphs: paragraphs, isBoilerplate: isBoilerplateMarkup };
            }
        }

        // Fallback HTML/XHTML extractor (also used in headless/Node test environments)
        const headTitleMatch = rawStr.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i);
        const headTitle = headTitleMatch ? decodeXmlEntities(headTitleMatch[1].replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim() : '';

        const cleaned = rawStr
            .replace(/<(script|style|svg|nav|head|noscript|iframe)\b[\s\S]*?<\/\1>/gi, '');
        let detectedTitle = '';
        let detectedTitleTag = '';
        const hMatch = cleaned.match(/<(h[1-3])\b([^>]*)>([\s\S]*?)<\/\1>/i);
        if (hMatch) {
            detectedTitleTag = hMatch[1].toUpperCase();
            const attrTitle = parseXmlAttrs(hMatch[2]).title || '';
            const hText = (decodeXmlEntities(hMatch[3].replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim()) || attrTitle.trim();
            if (hText && hText.length <= 120) detectedTitle = hText;
        }
        if (!detectedTitle && headTitle && headTitle.length <= 120 && !/^ignored$/i.test(headTitle)) {
            detectedTitle = headTitle;
        }

        let detectedSubtitle = '';
        const paragraphs = [];
        const blockRe = /<(p|h[1-6]|blockquote|li)\b([^>]*)>([\s\S]*?)<\/\1>/gi;
        let bm;
        while ((bm = blockRe.exec(cleaned)) !== null) {
            const tag = bm[1].toLowerCase();
            const attrs = parseXmlAttrs(bm[2] || '');
            const inner = bm[3];
            if (tag !== 'p' && /<p\b/i.test(inner)) continue;
            const txt = decodeXmlEntities(inner.replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
            if (!txt) continue;
            if (paragraphs.length === 0 && !detectedSubtitle) {
                if (txt.toLowerCase() === (detectedTitle || '').toLowerCase()) continue;
                const cls = attrs['class'] || '';
                const isSubHeading = (EPUB_SUBTITLE_CLASS_RE.test(cls) || (detectedTitleTag === 'H1' && (tag === 'h2' || tag === 'h3')));
                if (isSubHeading && txt.length <= 160) {
                    detectedSubtitle = txt;
                    continue;
                }
            }
            paragraphs.push(txt);
        }
        if (!paragraphs.length) {
            const bodyMatch = cleaned.match(/<body\b[^>]*>([\s\S]*?)<\/body>/i);
            const rawBody = decodeXmlEntities((bodyMatch ? bodyMatch[1] : cleaned).replace(/<br\s*\/?>/gi, '\n\n').replace(/<[^>]+>/g, ' '));
            splitParagraphs(rawBody).forEach(p => {
                const clean = p.replace(/\s+/g, ' ').trim();
                if (clean && clean !== detectedTitle) paragraphs.push(clean);
            });
        }
        return { title: detectedTitle, subtitle: detectedSubtitle, paragraphs: paragraphs, isBoilerplate: isBoilerplateMarkup };
    }

    async function parseEpub(arrayBuffer, fallbackTitle) {
        const zip = await unpackZip(arrayBuffer);
        const containerXml = await zip.getText('META-INF/container.xml');
        if (!containerXml) throw new Error('Invalid EPUB: missing META-INF/container.xml');

        const rfMatch = containerXml.match(/<rootfile\b([^>]*)\/?>/i);
        const opfPath = rfMatch && parseXmlAttrs(rfMatch[1])['full-path'];
        if (!opfPath) throw new Error('Invalid EPUB: could not locate OPF package.');

        const opfXml = await zip.getText(opfPath);
        if (!opfXml) throw new Error('Invalid EPUB: OPF file missing in archive.');

        const opfDir = opfPath.includes('/') ? opfPath.slice(0, opfPath.lastIndexOf('/')) : '';
        const bookTitle = firstXmlTagText(opfXml, 'title') || fallbackTitle || 'Untitled Book';
        const bookAuthor = firstXmlTagText(opfXml, 'creator') || '';

        const manifestById = new Map();
        let navHref = null;
        let ncxHref = null;

        const itemRe = /<(?:\w+:)?item\b([^>]*)\/?>/gi;
        let im;
        while ((im = itemRe.exec(opfXml)) !== null) {
            const attrs = parseXmlAttrs(im[1]);
            const id = attrs.id;
            const href = attrs.href;
            const mediaType = (attrs['media-type'] || '').toLowerCase();
            const props = (attrs.properties || '').toLowerCase();
            if (!id || !href) continue;
            const resolved = resolveRelativeZipPath(opfDir, href);
            manifestById.set(id, { href: resolved, mediaType: mediaType, properties: props });
            if (props.split(/\s+/).includes('nav')) navHref = resolved;
            if (mediaType.includes('dtbncx')) ncxHref = resolved;
        }

        // Collect OPF <guide> references that mark front/back-matter boilerplate (cover, title-page, copyright-page, etc.)
        const boilerplateGuideHrefs = new Set();
        const refRe = /<(?:\w+:)?reference\b([^>]*)\/?>/gi;
        let refm;
        while ((refm = refRe.exec(opfXml)) !== null) {
            const attrs = parseXmlAttrs(refm[1]);
            const rType = (attrs.type || '').trim();
            const rHref = attrs.href ? resolveRelativeZipPath(opfDir, attrs.href) : '';
            if (rHref && EPUB_GUIDE_BOILERPLATE_RE.test(rType)) {
                boilerplateGuideHrefs.add(rHref);
            }
        }

        // Map spine file path -> human-readable chapter title from TOC (EPUB 3 nav or EPUB 2 NCX)
        const tocTitlesByPath = new Map();
        if (navHref) {
            const navXml = await zip.getText(navHref);
            if (navXml) {
                const navDir = navHref.includes('/') ? navHref.slice(0, navHref.lastIndexOf('/')) : '';
                const aRe = /<a\b([^>]*)>([\s\S]*?)<\/a>/gi;
                let am;
                while ((am = aRe.exec(navXml)) !== null) {
                    const href = parseXmlAttrs(am[1]).href;
                    const label = decodeXmlEntities(am[2].replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
                    const target = resolveRelativeZipPath(navDir, href);
                    if (target && label && !tocTitlesByPath.has(target)) {
                        tocTitlesByPath.set(target, label);
                    }
                }
            }
        }
        if (tocTitlesByPath.size === 0 && ncxHref) {
            const ncxXml = await zip.getText(ncxHref);
            if (ncxXml) {
                const ncxDir = ncxHref.includes('/') ? ncxHref.slice(0, ncxHref.lastIndexOf('/')) : '';
                const navPtRe = /<(?:\w+:)?navPoint\b[^>]*>([\s\S]*?)<\/(?:\w+:)?navPoint>/gi;
                let pm;
                while ((pm = navPtRe.exec(ncxXml)) !== null) {
                    const block = pm[1];
                    const label = firstXmlTagText(block, 'text');
                    const contentMatch = block.match(/<(?:\w+:)?content\b([^>]*)\/?>/i);
                    const src = contentMatch && parseXmlAttrs(contentMatch[1]).src;
                    if (src && label) {
                        const target = resolveRelativeZipPath(ncxDir, src);
                        if (target && !tocTitlesByPath.has(target)) {
                            tocTitlesByPath.set(target, label);
                        }
                    }
                }
            }
        }

        const spineIds = [];
        const itemrefRe = /<(?:\w+:)?itemref\b([^>]*)\/?>/gi;
        let rm;
        while ((rm = itemrefRe.exec(opfXml)) !== null) {
            const attrs = parseXmlAttrs(rm[1]);
            if (attrs.idref && attrs.linear !== 'no') {
                spineIds.push(attrs.idref);
            }
        }

        const rawChapters = [];
        let seenNarrativeTocChapter = false;
        for (const idref of spineIds) {
            const item = manifestById.get(idref);
            if (!item) continue;
            if (item.href === navHref) continue;
            const xhtml = await zip.getText(item.href);
            if (!xhtml) continue;

            const extracted = extractHtmlParagraphsAndTitle(xhtml);
            if (!extracted.paragraphs.length) continue;

            const tocTitle = tocTitlesByPath.get(item.href);
            const chTitle = tocTitle || extracted.title || ('Chapter ' + (rawChapters.length + 1));
            const wordsInChapter = extracted.paragraphs.reduce((sum, p) => sum + tokenizeWords(p).length, 0);

            const fileStem = item.href.split('/').pop().replace(/\.[^.]+$/, '').toLowerCase();
            const isTitleRepeatStub = !!(tocTitle && tocTitle.toLowerCase() === bookTitle.toLowerCase() && wordsInChapter < 150);
            const isExplicitBoilerplate = boilerplateGuideHrefs.has(item.href) ||
                EPUB_BOILERPLATE_STEM_RE.test(fileStem) ||
                extracted.isBoilerplate ||
                isTitleRepeatStub;

            if (tocTitle && !isExplicitBoilerplate) {
                seenNarrativeTocChapter = true;
            }
            // Spine items at the front of the book that are omitted from a multi-entry TOC
            // (e.g. back-cover blurb/synopsis, copyright/errata log, dedication) are front-matter.
            const isUnlistedFrontMatter = !seenNarrativeTocChapter && tocTitlesByPath.size >= 2 && !tocTitle && wordsInChapter < 600;

            rawChapters.push({
                title: chTitle,
                subtitle: extracted.subtitle || '',
                paragraphs: extracted.paragraphs,
                _words: wordsInChapter,
                _isBoilerplate: isExplicitBoilerplate || isUnlistedFrontMatter
            });
        }

        // Filter out front/back-matter boilerplate (cover, synopsis, title page, copyright/credits,
        // dedication, author bio) and tiny stubs (< 15 words) when the book has real chapters.
        const narrativeChapters = rawChapters.filter(c => !c._isBoilerplate && c._words >= 15);
        const substantive = rawChapters.filter(c => c._words >= 15);
        const chosen = narrativeChapters.length > 0 ? narrativeChapters : (substantive.length > 0 ? substantive : rawChapters);
        const chapters = finalizeChapterList(chosen, bookTitle);

        if (!chapters.length) {
            throw new Error('No readable text chapters were found in this EPUB.');
        }

        return {
            title: bookTitle,
            author: bookAuthor,
            sourceType: 'epub',
            chapters: chapters
        };
    }

    async function parseDocx(arrayBuffer, fallbackTitle) {
        const zip = await unpackZip(arrayBuffer);
        const docXml = await zip.getText('word/document.xml');
        if (!docXml) throw new Error('Invalid DOCX: missing word/document.xml');

        let docTitle = fallbackTitle || 'Untitled Document';
        let docAuthor = '';
        const coreXml = await zip.getText('docProps/core.xml');
        if (coreXml) {
            const t = firstXmlTagText(coreXml, 'title');
            const c = firstXmlTagText(coreXml, 'creator');
            if (t) docTitle = t;
            if (c) docAuthor = c;
        }

        const rawChapters = [];
        let current = { title: '', paragraphs: [] };

        const pRe = /<(?:\w+:)?p(?:\s[^>]*)?>([\s\S]*?)<\/(?:\w+:)?p>/gi;
        let pm;
        while ((pm = pRe.exec(docXml)) !== null) {
            const pInner = pm[1];
            let isHeading = false;

            const styleMatch = pInner.match(/<(?:\w+:)?pStyle\b([^>]*)\/?>/i);
            if (styleMatch) {
                const val = parseXmlAttrs(styleMatch[1]).val || '';
                if (/^(Heading[123]|Title|Titulo|Título|Cabeza|Cim|Cím|[123])$/i.test(val)) {
                    isHeading = true;
                }
            }
            const outlineMatch = pInner.match(/<(?:\w+:)?outlineLvl\b([^>]*)\/?>/i);
            if (outlineMatch) {
                const lvl = parseXmlAttrs(outlineMatch[1]).val || '';
                if (lvl === '0' || lvl === '1') isHeading = true;
            }

            let paraText = '';
            const tokenRe = /<(?:\w+:)?(t|tab|br|cr)(?:\s[^>]*)?(?:\/>|>([\s\S]*?)<\/(?:\w+:)?\1>)/gi;
            let tm;
            while ((tm = tokenRe.exec(pInner)) !== null) {
                const kind = tm[1].toLowerCase();
                if (kind === 't') paraText += decodeXmlEntities(tm[2] || '');
                else if (kind === 'tab') paraText += ' ';
                else if (kind === 'br' || kind === 'cr') paraText += '\n';
            }
            paraText = paraText.replace(/[ \t]+/g, ' ').trim();
            if (!paraText) continue;

            if (isHeading && paraText.length <= 120) {
                if (current.paragraphs.length > 0) {
                    rawChapters.push(current);
                    current = { title: paraText, paragraphs: [] };
                } else if (!current.title) {
                    current.title = paraText;
                } else {
                    current.paragraphs.push(paraText);
                }
            } else {
                const inlineHeading = detectHeadingLine(paraText);
                if (inlineHeading) {
                    if (current.paragraphs.length > 0) rawChapters.push(current);
                    current = {
                        title: inlineHeading.title,
                        paragraphs: inlineHeading.remainder ? [inlineHeading.remainder] : []
                    };
                } else {
                    current.paragraphs.push(paraText);
                }
            }
        }

        if (current.paragraphs.length > 0) {
            rawChapters.push(current);
        }

        const chapters = finalizeChapterList(rawChapters, docTitle);
        if (!chapters.length) {
            throw new Error('No readable text found in this DOCX file.');
        }

        return {
            title: docTitle,
            author: docAuthor,
            sourceType: 'docx',
            chapters: chapters
        };
    }

    async function parseDocumentFile(file) {
        if (!file) throw new Error('No file selected.');
        const name = file.name || 'Document';
        const baseName = name.replace(/\.[^.]+$/, '').replace(/[_-]+/g, ' ').trim() || 'Imported Text';
        const ext = (name.split('.').pop() || '').toLowerCase();

        if (ext === 'epub') {
            const buf = await file.arrayBuffer();
            return await parseEpub(buf, baseName);
        }
        if (ext === 'docx') {
            const buf = await file.arrayBuffer();
            return await parseDocx(buf, baseName);
        }
        if (ext === 'doc') {
            throw new Error('Legacy binary .doc files are not supported. Please save as .docx, .epub, or .txt.');
        }
        // Plain text / Markdown (.txt, .md)
        const text = await file.text();
        const chapters = buildChaptersFromText(text, baseName);
        if (!chapters.length) {
            throw new Error('The selected file is empty.');
        }
        return {
            title: baseName,
            author: '',
            sourceType: ext === 'md' ? 'md' : 'txt',
            chapters: chapters
        };
    }

    // ----------------------------------------
    // MY TEXTS — editor (create / edit / import file)
    // ----------------------------------------
    function openAddText() {
        activeBookId = null;
        textDraft = {
            id: null,
            title: '',
            author: '',
            sourceType: 'paste',
            text: '',
            chapters: null,
            analysis: null,
            fileLabel: ''
        };
        if (typeof Lexicon !== 'undefined') Lexicon.load();
        renderMyTextsPane();
    }

    async function openEditText(id) {
        const t = getMyText(id);
        if (!t) return;
        activeBookId = null;
        if (typeof Lexicon !== 'undefined') Lexicon.load();
        const chapters = await resolveBookChapters(t);
        const payload = await loadBookPayload(t.id);
        const fullAnalysis = t.analysis
            ? Object.assign({}, t.analysis, { lemmas: (payload && payload.lemmas) || [] })
            : null;
        const isMultiFile = t.sourceType === 'epub' || t.sourceType === 'docx' || (chapters && chapters.length > 1);
        const joinedText = isMultiFile
            ? ''
            : (t.text || (chapters[0] ? chapters[0].paragraphs.join('\n\n') : ''));

        textDraft = {
            id: t.id,
            title: t.title,
            author: t.author || '',
            sourceType: t.sourceType || 'paste',
            text: joinedText,
            chapters: chapters,
            analysis: fullAnalysis,
            fileLabel: isMultiFile ? `${chapters.length} chapters (${(t.analysis && t.analysis.totalWords || 0).toLocaleString()} words)` : ''
        };
        renderMyTextsPane();
    }

    function closeTextEditor() {
        textDraft = null;
        renderMyTextsPane();
    }

    function draftPlainText(draft) {
        if (draft.chapters && draft.chapters.length) {
            return draft.chapters.map(c => (c.paragraphs || []).join('\n\n')).join('\n\n');
        }
        return draft.text || '';
    }

    async function handleFileUpload(file) {
        if (!file || !textDraft) return;
        const statusEl = document.getElementById('lt-import-status');
        if (statusEl) {
            statusEl.textContent = 'Reading ' + file.name + '…';
            statusEl.classList.remove('hidden');
        }
        try {
            if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) {
                await Lexicon.load();
            }
            const parsed = await parseDocumentFile(file);
            if (!textDraft) return;

            if (!textDraft.title.trim()) {
                textDraft.title = parsed.title;
            }
            textDraft.author = parsed.author || '';
            textDraft.sourceType = parsed.sourceType;
            textDraft.chapters = parsed.chapters;

            const combinedText = draftPlainText(textDraft);
            textDraft.analysis = analyseText(combinedText);
            textDraft.fileLabel = `${file.name} · ${parsed.chapters.length} ${parsed.chapters.length === 1 ? 'part' : 'chapters'} (${textDraft.analysis.totalWords.toLocaleString()} words)`;
            if (parsed.chapters.length === 1 && combinedText.length <= INLINE_TEXT_MAX_CHARS) {
                textDraft.text = combinedText;
            } else {
                textDraft.text = '';
            }
            renderMyTextsPane();
        } catch (err) {
            const msg = (err && err.message) ? err.message : 'Could not import file.';
            if (typeof UI !== 'undefined' && UI.toast) UI.toast(msg, 'error');
            else alert(msg);
            if (statusEl) statusEl.textContent = msg;
        }
    }

    async function runAnalysis() {
        if (!textDraft) return;
        const hasImportedChapters = Array.isArray(textDraft.chapters) && textDraft.chapters.length > 0 && !textDraft.text.trim();
        if (!hasImportedChapters && !textDraft.text.trim()) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Paste some text or import a file first.', 'warning');
            else alert('Paste some text or import a file first.');
            return;
        }
        if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) {
            const btn = document.querySelector('[data-text-analyse]');
            if (btn) { btn.disabled = true; btn.textContent = 'Analysing…'; }
            await Lexicon.load();
            if (!textDraft) return;
        }
        if (!hasImportedChapters) {
            textDraft.chapters = buildChaptersFromText(textDraft.text, textDraft.title);
        }
        textDraft.analysis = analyseText(draftPlainText(textDraft));
        renderMyTextsPane();
    }

    async function saveText(andRead) {
        const draft = textDraft;
        if (!draft) return;
        const title = (draft.title || '').trim();
        if (!title) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Give the text a title first.', 'warning');
            else alert('Give the text a title first.');
            return;
        }

        const hasImportedChapters = Array.isArray(draft.chapters) && draft.chapters.length > 0 && !draft.text.trim();
        if (!hasImportedChapters && !draft.text.trim()) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Paste some text or import a file first.', 'warning');
            else alert('Paste some text or import a file first.');
            return;
        }

        if (!hasImportedChapters) {
            draft.chapters = buildChaptersFromText(draft.text, title);
        } else if (draft.chapters.length === 1) {
            draft.chapters[0].title = title;
        }

        if (!draft.analysis) {
            if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) await Lexicon.load();
            if (textDraft !== draft) return;
            draft.analysis = analyseText(draftPlainText(draft));
        }

        const now = new Date().toISOString();
        let id = draft.id;
        const chaptersMeta = compactChaptersMeta(draft.chapters);
        const summaryAnalysis = compactAnalysis(draft.analysis);
        const inlineText = (draft.chapters.length === 1 && draft.text && draft.text.length <= INLINE_TEXT_MAX_CHARS)
            ? draft.text : undefined;

        if (id) {
            const t = getMyText(id);
            if (t) {
                t.title = title;
                t.author = draft.author || '';
                t.sourceType = draft.sourceType || 'paste';
                t.chapters = chaptersMeta;
                t.analysis = summaryAnalysis;
                t.modified = now;
                if (inlineText) t.text = inlineText;
                else delete t.text;
                if (!t.progress) {
                    t.progress = { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: 0 };
                } else if (t.progress.chapterIndex >= chaptersMeta.length) {
                    t.progress.chapterIndex = 0;
                    t.progress.pct = 0;
                    t.progress.paraIndex = 0;
                }
            }
        } else {
            id = genTextId();
            const entry = {
                id: id,
                title: title,
                author: draft.author || '',
                sourceType: draft.sourceType || 'paste',
                chapters: chaptersMeta,
                created: now,
                modified: now,
                analysis: summaryAnalysis,
                progress: { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: 0 }
            };
            if (inlineText) entry.text = inlineText;
            myTexts.push(entry);
        }

        await saveBookPayload(id, {
            chapters: draft.chapters,
            lemmas: (draft.analysis && draft.analysis.lemmas) || []
        });
        saveMyTexts();
        textDraft = null;

        if (andRead) {
            openMyTextOrChapters(id);
        } else {
            renderMyTextsPane();
        }
    }

    async function deleteText() {
        if (!textDraft || !textDraft.id) return;
        const id = textDraft.id;
        if (!confirm(`Delete "${textDraft.title}"? Words you've saved from it stay in your decks.`)) return;
        myTexts = myTexts.filter(t => t.id !== id);
        saveMyTexts();
        await deleteBookPayload(id);
        textDraft = null;
        if (activeBookId === id) activeBookId = null;
        renderMyTextsPane();
    }

    async function quickDeleteText(id) {
        const t = getMyText(id);
        if (!t) return;
        if (!confirm(`Delete "${t.title}"? Words you've saved from it stay in your decks.`)) return;
        myTexts = myTexts.filter(x => x.id !== id);
        saveMyTexts();
        await deleteBookPayload(id);
        if (activeBookId === id) activeBookId = null;
        renderMyTextsPane();
    }

    // ----------------------------------------
    // MY TEXTS — vocabulary selection ("Add selected words to deck")
    // ----------------------------------------
    function vocabPanelHtml(a) {
        const lemmas = (a && Array.isArray(a.lemmas)) ? a.lemmas : [];
        if (!lemmas.length) return '';

        const groups = [
            { key: 'familiar', label: 'Familiar', items: lemmas.filter(l => l.familiar) },
            { key: 'new', label: 'New', items: lemmas.filter(l => l.isNew) },
            { key: 'inDecks', label: 'In decks', items: lemmas.filter(l => l.inDeck) },
            { key: 'due', label: 'Due for review', items: lemmas.filter(l => l.due) }
        ];

        return `
            <div class="dk-group lt-vocab-group">
                <button class="dk-group-header" data-group-toggle="lt-vocab" aria-expanded="false">
                    <span>
                        <span class="dk-group-title">Inspect vocabulary</span>
                        <span class="dk-group-count">${lemmas.length}</span>
                    </span>
                    <span class="dk-group-arrow" id="dk-group-arrow-lt-vocab" aria-hidden="true">▶</span>
                </button>
                <div class="dk-group-body hidden" id="dk-group-body-lt-vocab">
                    ${groups.map(g => !g.items.length ? '' : `
                        <div class="lt-vocab-category">
                            <p class="lt-vocab-category-title">${esc(g.label)} (${g.items.length})</p>
                            <ul class="lt-vocab-list">
                                ${g.items.map(item => `
                                    <li>
                                        <label class="lt-vocab-item">
                                            <input type="checkbox" data-vocab-lemma="${esc(item.lemma)}"
                                                data-vocab-en="${esc(item.translation || '')}"
                                                data-vocab-pos="${esc(item.pos || '')}">
                                            <span class="lt-vocab-es">${esc(withArticle(item.lemma))}</span>
                                            <span class="lt-vocab-en">${esc(item.translation || '—')}</span>
                                        </label>
                                    </li>
                                `).join('')}
                            </ul>
                        </div>
                    `).join('')}
                    <div class="lt-vocab-actions">
                        <button class="dk-secondary" data-vocab-add-selected="1">Add selected words to deck</button>
                    </div>
                </div>
            </div>
        `;
    }

    function addSelectedVocabToDeck(host) {
        const checked = Array.from(host.querySelectorAll('[data-vocab-lemma]:checked'));
        if (!checked.length) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('Check a word first.', 'warning');
            else alert('Check a word first.');
            return;
        }
        const items = checked.map(el => ({
            lemma: el.getAttribute('data-vocab-lemma'),
            translation: el.getAttribute('data-vocab-en'),
            pos: el.getAttribute('data-vocab-pos')
        }));
        if (typeof Decks !== 'undefined') Decks.openBulkAddPicker(items);
    }

    // ----------------------------------------
    // MY TEXTS — render (Editor, Index, and Book Chapters View)
    // ----------------------------------------
    function textAnalysisHtml(a, chapterCount) {
        const chText = (chapterCount && chapterCount > 1) ? `${chapterCount} chapters · ` : '';
        return `
            <div class="lt-analysis">
                <p class="lt-analysis-headline">${a.level ? 'Estimated level: ' + esc(a.level) : 'Level: Unassessed'}</p>
                <p class="lt-analysis-line">${chText}${a.totalWords.toLocaleString()} words · ~${a.estimatedMinutes} min read</p>
                <p class="lt-analysis-coverage">${a.familiarPercent}% familiar</p>
                <ul class="lt-analysis-breakdown">
                    <li>${a.familiar} recognised words</li>
                    <li>${a.notYetLearned} words not yet learned</li>
                    <li>${a.inDecks} already in your decks</li>
                    <li>${a.due} due for review</li>
                </ul>
                ${vocabPanelHtml(a)}
            </div>
        `;
    }

    function removeDraftChapter(chIdx) {
        if (!textDraft || !Array.isArray(textDraft.chapters)) return;
        if (textDraft.chapters.length <= 1) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('A book must keep at least one chapter.', 'warning');
            return;
        }
        if (chIdx < 0 || chIdx >= textDraft.chapters.length) return;
        textDraft.chapters.splice(chIdx, 1);
        textDraft.chapters.forEach((c, idx) => { c.index = idx; });
        const combinedText = draftPlainText(textDraft);
        textDraft.analysis = analyseText(combinedText);
        textDraft.fileLabel = `${textDraft.chapters.length} ${textDraft.chapters.length === 1 ? 'part' : 'chapters'} (${textDraft.analysis.totalWords.toLocaleString()} words)`;
        renderMyTextsPane();
    }

    async function deleteBookChapter(textId, chIdx) {
        const t = getMyText(textId);
        if (!t) return;
        const chapters = await resolveBookChapters(t);
        if (chapters.length <= 1) {
            if (typeof UI !== 'undefined' && UI.toast) UI.toast('A book must keep at least one chapter.', 'warning');
            return;
        }
        if (chIdx < 0 || chIdx >= chapters.length) return;
        const removed = chapters.splice(chIdx, 1)[0];
        chapters.forEach((c, idx) => { c.index = idx; });

        const payload = await loadBookPayload(t.id);
        await saveBookPayload(t.id, {
            chapters: chapters,
            lemmas: (payload && payload.lemmas) || null
        });

        t.chapters = compactChaptersMeta(chapters);
        if (t.analysis) {
            const totalWords = chapters.reduce((sum, c) => sum + (c.wordCount || 0), 0);
            t.analysis.totalWords = totalWords;
            t.analysis.estimatedMinutes = Math.max(1, Math.round(totalWords / READING_WPM));
        }
        if (t.progress) {
            if (Array.isArray(t.progress.readChapters)) {
                t.progress.readChapters = t.progress.readChapters
                    .filter(idx => idx !== chIdx)
                    .map(idx => (idx > chIdx ? idx - 1 : idx));
            }
            if (typeof t.progress.chapterIndex === 'number') {
                if (chIdx < t.progress.chapterIndex) {
                    t.progress.chapterIndex = Math.max(0, t.progress.chapterIndex - 1);
                } else if (chIdx === t.progress.chapterIndex) {
                    t.progress.chapterIndex = Math.min(chapters.length - 1, t.progress.chapterIndex);
                    t.progress.pct = 0;
                    t.progress.paraIndex = 0;
                }
            }
        }
        t.modified = new Date().toISOString();
        saveMyTexts();
        if (typeof UI !== 'undefined' && UI.toast && removed) {
            UI.toast(`Removed "${removed.title}"`, 'info', 2000);
        }
        renderMyTextsPane();
    }

    function textEditorHtml() {
        const isNew = !textDraft.id;
        const a = textDraft.analysis;
        const chCount = Array.isArray(textDraft.chapters) ? textDraft.chapters.length : 0;
        const isImportedMulti = chCount > 1 || textDraft.sourceType === 'epub' || textDraft.sourceType === 'docx';

        return `
            <button class="dk-back" data-text-cancel="1">← My Texts</button>
            <div class="dk-editor">
                <h3 class="dk-editor-title">${isNew ? 'Add text or book' : 'Edit text'}</h3>

                <div class="lt-import-box">
                    <div class="lt-import-row">
                        <label class="dk-secondary lt-import-btn" for="lt-file-input">
                            Import file (.epub, .docx, .txt)
                        </label>
                        <input id="lt-file-input" type="file" accept=".epub,.docx,.txt,.md,application/epub+zip,application/vnd.openxmlformats-officedocument.wordprocessingml.document,text/plain,text/markdown" class="hidden">
                        <span class="lt-import-hint">Long texts are automatically split into chapters.</span>
                    </div>
                    <p id="lt-import-status" class="lt-import-status${textDraft.fileLabel ? '' : ' hidden'}">${esc(textDraft.fileLabel || '')}</p>
                </div>

                <label class="dk-editor-label" for="lt-text-title">Title</label>
                <input id="lt-text-title" class="dk-editor-input" type="text"
                    placeholder="e.g. Cien años de soledad" value="${esc(textDraft.title)}" maxlength="120">

                ${isImportedMulti ? `
                    <div class="lt-imported-summary">
                        <p class="lt-imported-summary-title">Loaded ${chCount} ${chCount === 1 ? 'chapter' : 'chapters'}${textDraft.author ? ' by ' + esc(textDraft.author) : ''}</p>
                        <ul class="lt-imported-chapter-preview">
                            ${textDraft.chapters.map((c, idx) => `
                                <li class="lt-imported-ch-item">
                                    <span class="lt-imported-ch-label">
                                        <strong>${idx + 1}.</strong> ${esc(c.title)}${c.subtitle ? ` <span class="lt-ch-preview-sub">— ${esc(c.subtitle)}</span>` : ''}
                                        <span class="lt-ch-preview-meta">(${c.wordCount.toLocaleString()} words)</span>
                                    </span>
                                    ${chCount > 1 ? `<button type="button" class="lt-ch-remove-btn" data-draft-remove-ch="${idx}" title="Remove chapter" aria-label="Remove ${esc(c.title)}">Remove</button>` : ''}
                                </li>
                            `).join('')}
                        </ul>
                        <button type="button" class="lt-card-action" data-text-clear-file="1">Switch to plain text paste</button>
                    </div>
                ` : `
                    <label class="dk-editor-label" for="lt-text-body">Or paste your text</label>
                    <textarea id="lt-text-body" class="dk-editor-input lt-text-area"
                        placeholder="Paste any ${Lang.name()} text here — an article, an essay, or a full book…">${esc(textDraft.text)}</textarea>

                    <div class="dk-actions lt-analyse-row">
                        <button class="dk-secondary" data-text-analyse="1">Analyse text</button>
                    </div>
                `}

                ${a ? textAnalysisHtml(a, chCount) : ''}

                <div class="dk-actions dk-editor-actions">
                    <button class="btn-primary" data-text-save="1">Save</button>
                    <button class="dk-secondary" data-text-save-read="1">Save &amp; read</button>
                    ${!isNew ? '<button class="dk-danger" data-text-delete="1">Delete text</button>' : ''}
                </div>
            </div>
        `;
    }

    function textProgressSummary(t) {
        const chs = Array.isArray(t.chapters) && t.chapters.length ? t.chapters : [{ index: 0, title: t.title }];
        const totalCh = chs.length;
        const p = t.progress || { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [] };
        const readSet = new Set(Array.isArray(p.readChapters) ? p.readChapters : []);
        const allRead = totalCh > 0 && readSet.size >= totalCh;
        const curIdx = Math.min(totalCh - 1, Math.max(0, p.chapterIndex || 0));
        const curPct = Math.round(p.pct || 0);
        const isStarted = !allRead && (readSet.size > 0 || curIdx > 0 || curPct >= 3 || (p.paraIndex || 0) > 0);

        if (allRead) {
            return { state: 'done', label: totalCh > 1 ? `All ${totalCh} chapters read ✓` : 'Read ✓', pct: 100 };
        }
        if (isStarted) {
            if (totalCh > 1) {
                const chLabel = `Ch. ${curIdx + 1} of ${totalCh}`;
                return {
                    state: 'now',
                    label: curPct > 0 ? `${chLabel} · ${curPct}%` : `${chLabel} (${readSet.size}/${totalCh} read)`,
                    pct: Math.round(((curIdx + (curPct / 100)) / totalCh) * 100),
                    chapterIndex: curIdx
                };
            }
            return { state: 'now', label: `${Math.max(1, curPct)}% read`, pct: Math.max(1, curPct), chapterIndex: 0 };
        }
        return { state: 'todo', label: '', pct: 0, chapterIndex: 0 };
    }

    function myTextCardHtml(t) {
        const a = t.analysis;
        const chCount = (Array.isArray(t.chapters) && t.chapters.length) ? t.chapters.length : 1;
        const chPart = chCount > 1 ? `${chCount} chapters · ` : '';
        const meta = a
            ? `${a.level || 'Unassessed'} · ${chPart}${a.totalWords.toLocaleString()} words · ~${a.estimatedMinutes} min`
            : 'Not analysed yet';
        const prog = textProgressSummary(t);
        const progBadge = prog.state === 'done'
            ? `<span class="lt-card-progress is-done">${esc(prog.label)}</span>`
            : (prog.state === 'now' ? `<span class="lt-card-progress is-now">${esc(prog.label)}</span>` : '');

        return `
            <div class="lt-card">
                <button class="lt-card-main" data-text-open="${esc(t.id)}">
                    <span class="lt-card-title">${esc(t.title)}${t.author ? ` <span class="lt-card-author">by ${esc(t.author)}</span>` : ''}</span>
                    <span class="lt-card-meta">${esc(meta)}</span>
                    <span class="lt-card-badges">
                        ${a ? `<span class="lt-card-coverage">${a.familiarPercent}% familiar</span>` : ''}
                        ${progBadge}
                    </span>
                </button>
                <div class="lt-card-actions">
                    <button class="lt-card-action" data-text-edit="${esc(t.id)}">Edit</button>
                    <button class="lt-card-action lt-card-action-danger" data-text-quick-delete="${esc(t.id)}">Delete</button>
                </div>
            </div>
        `;
    }

    function buildMyTextsContinueHtml(texts) {
        const inProgress = texts
            .map(t => ({ t, prog: textProgressSummary(t) }))
            .filter(x => x.prog.state === 'now')
            .slice(0, 3);
        if (!inProgress.length) return '';

        return `
            <div class="lib-continue lt-continue-block">
                <h3 class="lib-recs-heading">Continue Reading</h3>
                <div class="lib-continue-list">
                    ${inProgress.map(x => {
                        const chs = Array.isArray(x.t.chapters) && x.t.chapters.length ? x.t.chapters : [{ title: x.t.title }];
                        const chIdx = x.prog.chapterIndex || 0;
                        const chTitle = chs.length > 1 && chs[chIdx] ? chs[chIdx].title : '';
                        return `
                            <button type="button" class="lib-continue-item" data-text-resume="${esc(x.t.id)}" data-text-chapter="${chIdx}">
                                <span class="lib-continue-title">${esc(x.t.title)}</span>
                                <span class="lib-continue-meta">${esc(chTitle ? chTitle + ' · ' : '')}${esc(x.prog.label)}</span>
                                <span class="lib-continue-bar" aria-hidden="true"><span style="width:${x.prog.pct}%"></span></span>
                            </button>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    function myTextsIndexHtml() {
        const texts = listMyTexts();
        return `
            <div class="lt-index-head">
                <p class="dk-group-blurb">Bring in any ${Lang.name()} book (.epub, .docx, .txt) or paste text to read it chapter by chapter with full tap-to-translate.</p>
                <button class="btn-primary" data-text-add="1">+ Add text or book</button>
            </div>
            ${buildMyTextsContinueHtml(texts)}
            ${texts.length
                ? `<div class="lt-list">${texts.map(myTextCardHtml).join('')}</div>`
                : '<p class="dk-empty">No texts yet. Import an EPUB/DOCX or paste text to get started.</p>'}
        `;
    }

    function bookOverviewHtml(t) {
        const chs = Array.isArray(t.chapters) && t.chapters.length ? t.chapters : [{ index: 0, title: t.title, wordCount: (t.analysis && t.analysis.totalWords) || 0, estimatedMinutes: (t.analysis && t.analysis.estimatedMinutes) || 1 }];
        const a = t.analysis;
        const p = t.progress || { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [] };
        const readSet = new Set(Array.isArray(p.readChapters) ? p.readChapters : []);
        const activeIdx = Math.min(chs.length - 1, Math.max(0, p.chapterIndex || 0));
        const activeCh = chs[activeIdx] || chs[0];
        const activePct = Math.round(p.pct || 0);
        const hasStarted = readSet.size > 0 || activeIdx > 0 || activePct >= 3 || (p.paraIndex || 0) > 0;
        const allRead = readSet.size >= chs.length;

        const ctaLabel = allRead
            ? `Read again from Chapter 1 →`
            : (hasStarted
                ? `Continue — ${activeCh.title}${activePct > 0 ? ' (' + activePct + '%)' : ''} →`
                : `Start reading — ${chs[0].title} →`);
        const ctaChapter = allRead ? 0 : activeIdx;

        return `
            <div class="story-bar">
                <button type="button" class="story-action" data-book-back="1">&larr; My texts</button>
                <div class="lt-card-actions">
                    <button type="button" class="lt-card-action" data-text-edit="${esc(t.id)}">Edit</button>
                    <button type="button" class="lt-card-action lt-card-action-danger" data-text-quick-delete="${esc(t.id)}">Delete</button>
                </div>
            </div>
            <div class="lt-book-head">
                <h3 class="story-title">${esc(t.title)}</h3>
                ${t.author ? `<p class="lt-book-author">by ${esc(t.author)}</p>` : ''}
                <p class="lt-book-meta">
                    ${a ? `${esc(a.level || 'Unassessed')} · ${chs.length} chapters · ${a.totalWords.toLocaleString()} words · ${a.familiarPercent}% familiar` : `${chs.length} chapters`}
                    · ${readSet.size} / ${chs.length} read
                </p>
                <div class="lt-book-cta">
                    <button type="button" class="btn-primary" data-book-open-ch="${ctaChapter}">${esc(ctaLabel)}</button>
                </div>
            </div>
            <div class="lt-chapter-list" role="list">
                ${chs.map((ch, idx) => {
                    const isRead = readSet.has(idx);
                    const isCurrent = !allRead && hasStarted && idx === activeIdx;
                    const statusHtml = isCurrent && activePct > 0
                        ? `<span class="lt-ch-status is-now">${activePct}%</span>`
                        : (isRead
                            ? `<span class="lt-ch-status is-done">✓ Read</span>`
                            : (isCurrent ? `<span class="lt-ch-status is-now">Current</span>` : `<span class="lt-ch-status">→</span>`));
                    return `
                        <div class="lt-chapter-row-wrap${isCurrent ? ' is-current' : ''}${isRead ? ' is-read' : ''}" role="listitem">
                            <button type="button" class="lt-chapter-row${isCurrent ? ' is-current' : ''}${isRead ? ' is-read' : ''}" data-book-open-ch="${idx}">
                                <div class="lt-ch-main">
                                    <span class="lt-ch-num">${idx + 1}.</span>
                                    <div class="lt-ch-text">
                                        <span class="lt-ch-title">${esc(ch.title)}</span>
                                        ${ch.subtitle ? `<span class="lt-ch-subtitle">${esc(ch.subtitle)}</span>` : ''}
                                        <span class="lt-ch-meta">${(ch.wordCount || 0).toLocaleString()} words · ~${ch.estimatedMinutes || 1} min</span>
                                    </div>
                                </div>
                                ${statusHtml}
                            </button>
                            ${chs.length > 1 ? `<button type="button" class="lt-ch-delete-btn" data-book-delete-ch="${idx}" title="Remove this chapter from book" aria-label="Remove ${esc(ch.title)}">&times;</button>` : ''}
                        </div>
                    `;
                }).join('')}
            </div>
        `;
    }

    function openMyTextOrChapters(id) {
        const t = getMyText(id);
        if (!t) return;
        const chCount = (Array.isArray(t.chapters) && t.chapters.length) ? t.chapters.length : 1;
        if (chCount > 1) {
            activeBookId = id;
            renderMyTextsPane();
            window.scrollTo(0, 0);
        } else {
            openMyText(id, 0);
        }
    }

    function renderMyTextsPane() {
        const host = document.getElementById('lib-mytexts');
        if (!host) return;
        if (textDraft) {
            host.innerHTML = textEditorHtml();
        } else if (activeBookId) {
            const book = getMyText(activeBookId);
            if (book) {
                host.innerHTML = bookOverviewHtml(book);
            } else {
                activeBookId = null;
                host.innerHTML = myTextsIndexHtml();
            }
        } else {
            host.innerHTML = myTextsIndexHtml();
        }
        wireMyTextsPane(host);
    }

    function wireMyTextsPane(host) {
        host.querySelectorAll('[data-text-add]').forEach(el => { el.onclick = openAddText; });
        host.querySelectorAll('[data-text-open]').forEach(el => {
            el.onclick = function () { openMyTextOrChapters(el.getAttribute('data-text-open')); };
        });
        host.querySelectorAll('[data-text-resume]').forEach(el => {
            el.onclick = function () {
                const id = el.getAttribute('data-text-resume');
                const ch = parseInt(el.getAttribute('data-text-chapter') || '0', 10);
                openMyText(id, isNaN(ch) ? 0 : ch);
            };
        });
        host.querySelectorAll('[data-book-back]').forEach(el => {
            el.onclick = function () {
                activeBookId = null;
                renderMyTextsPane();
            };
        });
        host.querySelectorAll('[data-book-open-ch]').forEach(el => {
            el.onclick = function () {
                const ch = parseInt(el.getAttribute('data-book-open-ch') || '0', 10);
                if (activeBookId) openMyText(activeBookId, isNaN(ch) ? 0 : ch);
            };
        });
        host.querySelectorAll('[data-book-delete-ch]').forEach(el => {
            el.onclick = function (e) {
                if (e && e.stopPropagation) e.stopPropagation();
                const ch = parseInt(el.getAttribute('data-book-delete-ch') || '-1', 10);
                if (activeBookId && !isNaN(ch) && ch >= 0) return deleteBookChapter(activeBookId, ch);
            };
        });
        host.querySelectorAll('[data-draft-remove-ch]').forEach(el => {
            el.onclick = function () {
                const ch = parseInt(el.getAttribute('data-draft-remove-ch') || '-1', 10);
                if (!isNaN(ch) && ch >= 0) removeDraftChapter(ch);
            };
        });
        host.querySelectorAll('[data-text-edit]').forEach(el => {
            el.onclick = function () { openEditText(el.getAttribute('data-text-edit')); };
        });
        host.querySelectorAll('[data-text-quick-delete]').forEach(el => {
            el.onclick = function () { quickDeleteText(el.getAttribute('data-text-quick-delete')); };
        });

        const fileInput = document.getElementById('lt-file-input');
        if (fileInput) {
            fileInput.onchange = e => {
                const f = e.target.files && e.target.files[0];
                if (f) handleFileUpload(f);
            };
        }

        host.querySelectorAll('[data-text-clear-file]').forEach(el => {
            el.onclick = function () {
                if (!textDraft) return;
                textDraft.chapters = null;
                textDraft.sourceType = 'paste';
                textDraft.fileLabel = '';
                textDraft.analysis = null;
                renderMyTextsPane();
            };
        });

        const titleEl = document.getElementById('lt-text-title');
        const bodyEl = document.getElementById('lt-text-body');
        if (titleEl) titleEl.oninput = e => { if (textDraft) textDraft.title = e.target.value; };
        if (bodyEl) bodyEl.oninput = e => {
            if (!textDraft) return;
            textDraft.text = e.target.value;
            textDraft.chapters = null;
            textDraft.analysis = null;
        };

        host.querySelectorAll('[data-text-cancel]').forEach(el => { el.onclick = closeTextEditor; });
        host.querySelectorAll('[data-text-analyse]').forEach(el => { el.onclick = runAnalysis; });
        host.querySelectorAll('[data-text-save]').forEach(el => { el.onclick = () => saveText(false); });
        host.querySelectorAll('[data-text-save-read]').forEach(el => { el.onclick = () => saveText(true); });
        host.querySelectorAll('[data-text-delete]').forEach(el => { el.onclick = deleteText; });

        host.querySelectorAll('[data-group-toggle]').forEach(el => {
            el.onclick = function () {
                const key = el.getAttribute('data-group-toggle');
                const body = document.getElementById('dk-group-body-' + key);
                const arrow = document.getElementById('dk-group-arrow-' + key);
                if (!body) return;
                const nowOpen = body.classList.toggle('hidden') === false;
                el.setAttribute('aria-expanded', String(nowOpen));
                if (arrow) arrow.textContent = nowOpen ? '▼' : '▶';
            };
        });
        host.querySelectorAll('[data-vocab-add-selected]').forEach(el => {
            el.onclick = function () { addSelectedVocabToDeck(host); };
        });
    }

    // ----------------------------------------
    // MY TEXTS — per-chapter reading view & location persistence
    // ----------------------------------------
    function wireMyTextScrollProgress(textId, chapterIndex) {
        let saveTimer = null;
        const onScroll = () => {
            const bar = document.getElementById('story-scroll-bar');
            const storyBody = document.querySelector('#reader-content .story-body');
            if (!bar || !storyBody) return;
            const rect = storyBody.getBoundingClientRect();
            const total = rect.height;
            const scrolled = Math.max(0, -rect.top);
            const maxScroll = Math.max(1, total - window.innerHeight * 0.5);
            const pct = Math.min(100, Math.max(0, (scrolled / maxScroll) * 100));
            bar.style.width = pct + '%';

            // Find the top-most visible paragraph so restoring works even if
            // screen orientation or window width changes between sessions.
            let currentParaIdx = 0;
            const paras = storyBody.querySelectorAll('.story-paragraph[data-para-index]');
            for (let i = 0; i < paras.length; i++) {
                const pRect = paras[i].getBoundingClientRect();
                if (pRect.bottom > 80) {
                    currentParaIdx = parseInt(paras[i].getAttribute('data-para-index') || '0', 10);
                    break;
                }
            }

            // Keep floating audio player synced to the reader's scroll position while paused
            // so pressing Play starts from the currently visible paragraph.
            if (typeof StoryAudioPlayer !== 'undefined' && !StoryAudioPlayer.isPlaying &&
                StoryAudioPlayer.paragraphs && StoryAudioPlayer.paragraphs.length > 0) {
                const clampedIdx = Math.max(0, Math.min(StoryAudioPlayer.paragraphs.length - 1, currentParaIdx));
                if (StoryAudioPlayer.currentParaIndex !== clampedIdx) {
                    StoryAudioPlayer.currentParaIndex = clampedIdx;
                    if (typeof StoryAudioPlayer.updateProgressUI === 'function') {
                        StoryAudioPlayer.updateProgressUI();
                    }
                }
            }

            if (pct >= 2 || currentParaIdx > 0) {
                clearTimeout(saveTimer);
                saveTimer = setTimeout(() => {
                    const t = getMyText(textId);
                    if (!t) return;
                    if (!t.progress) t.progress = { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: 0 };
                    t.progress.chapterIndex = chapterIndex;
                    t.progress.pct = Math.min(99, Math.round(pct));
                    t.progress.paraIndex = currentParaIdx;
                    t.progress.at = Date.now();
                    saveMyTexts();
                }, 350);
            }
        };

        if (window._storyScrollListener && typeof window.removeEventListener === 'function') {
            window.removeEventListener('scroll', window._storyScrollListener);
        }
        window._storyScrollListener = onScroll;
        if (typeof window.addEventListener === 'function') {
            window.addEventListener('scroll', onScroll, { passive: true });
        }
        onScroll();
    }

    function restoreMyTextPosition(t, chapterIndex) {
        if (!t || !t.progress || t.progress.chapterIndex !== chapterIndex) {
            window.scrollTo(0, 0);
            return;
        }
        const savedPct = t.progress.pct || 0;
        const savedPara = t.progress.paraIndex || 0;
        if (savedPct < 3 && savedPara <= 0) {
            window.scrollTo(0, 0);
            return;
        }

        requestAnimationFrame(() => {
            const storyBody = document.querySelector('#reader-content .story-body');
            if (!storyBody) return;
            const targetPara = savedPara > 0
                ? storyBody.querySelector(`.story-paragraph[data-para-index="${savedPara}"]`)
                : null;
            if (targetPara) {
                const pRect = targetPara.getBoundingClientRect();
                window.scrollTo(0, Math.max(0, window.scrollY + pRect.top - 72));
            } else {
                const rect = storyBody.getBoundingClientRect();
                const maxScroll = Math.max(1, rect.height - window.innerHeight * 0.5);
                window.scrollTo(0, window.scrollY + rect.top + maxScroll * savedPct / 100);
            }
            if (typeof UI !== 'undefined' && UI.toast) {
                UI.toast('Picked up where you left off', 'info', 2000);
            }
        });
    }

    async function openMyText(id, requestedChapterIdx) {
        const t = getMyText(id);
        if (!t) return;

        const container = document.getElementById('reader-content');
        if (!container) return;

        // Stop any previous narration before loading the new chapter/text
        if (typeof StoryAudioPlayer !== 'undefined' && StoryAudioPlayer.teardown) {
            StoryAudioPlayer.teardown();
        }

        // Ensure dictionary/morphology is ready so word status colors and taps work immediately
        if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) {
            try { await Lexicon.load(); } catch (e) {}
        }

        const chapters = await resolveBookChapters(t);
        if (!chapters.length) return;

        const totalCh = chapters.length;
        const defaultCh = (t.progress && typeof t.progress.chapterIndex === 'number') ? t.progress.chapterIndex : 0;
        const chapterIndex = Math.min(totalCh - 1, Math.max(0, requestedChapterIdx !== undefined ? requestedChapterIdx : defaultCh));
        const chapter = chapters[chapterIndex];
        activeReading = { id: t.id, chapterIndex: chapterIndex };

        // Record which chapter the user has open if switching chapters
        if (!t.progress) {
            t.progress = { chapterIndex: chapterIndex, pct: 0, paraIndex: 0, readChapters: [], at: Date.now() };
            saveMyTexts();
        } else if (t.progress.chapterIndex !== chapterIndex) {
            t.progress.chapterIndex = chapterIndex;
            t.progress.pct = 0;
            t.progress.paraIndex = 0;
            t.progress.at = Date.now();
            saveMyTexts();
        }

        const level = t.analysis && t.analysis.level ? t.analysis.level : 'Unassessed';
        const isMulti = totalCh > 1;
        const isBookFormat = isMulti || t.sourceType === 'epub' || t.sourceType === 'docx';
        const backLabel = isMulti ? '&larr; Chapters' : '&larr; My texts';

        const chapterSelectHtml = isMulti ? `
            <select id="lt-reader-chapter-select" class="lt-chapter-select" aria-label="Jump to chapter">
                ${chapters.map((ch, idx) =>
                    `<option value="${idx}"${idx === chapterIndex ? ' selected' : ''}>Ch. ${idx + 1}/${totalCh}: ${esc(ch.title)}</option>`
                ).join('')}
            </select>
        ` : '';

        const paragraphs = chapter.paragraphs || [];
        let displaySubtitle = (chapter.subtitle || '').trim();
        let bodyStartIndex = 0;

        // Detect an inline chapter subtitle in paragraph 0 for books imported before
        // explicit subtitle extraction (e.g. "Pulverizo accidentalmente a mi profesora...")
        if (!displaySubtitle && isBookFormat && paragraphs.length >= 2 && !/\([2-9]\d*\/\d+\)$/.test(chapter.title || '')) {
            const p0 = (paragraphs[0] || '').trim();
            const p0Words = tokenizeWords(p0).length;
            if (p0.length > 0 && p0.length <= 100 && p0Words >= 2 && p0Words <= 16 &&
                !/[.?!…:;»”"]$/.test(p0) && !/^[-—–―«"“]/.test(p0)) {
                displaySubtitle = p0;
                bodyStartIndex = 1;
            }
        }

        const marksChecked = (typeof readerMarksOn === 'function' && readerMarksOn()) ? 'true' : 'false';

        let html = '<div class="story-bar">' +
            '<button type="button" class="story-action" data-mytext-back="1">' + backLabel + '</button>' +
            chapterSelectHtml +
        '</div>' +
        '<div class="story-header' + (isBookFormat ? ' lt-book-chapter-header' : '') + '">' +
            '<div class="story-header-left">' +
                (isMulti ? '<p class="lt-reading-eyebrow">' + esc(t.title) + (t.author ? ' · ' + esc(t.author) : '') + ' · Chapter ' + (chapterIndex + 1) + ' of ' + totalCh + '</p>' : '') +
                '<h3 class="story-title' + (isBookFormat ? ' lt-chapter-heading' : '') + '">' + esc(isMulti ? chapter.title : t.title) + '</h3>' +
                (displaySubtitle ? '<p class="lt-chapter-subtitle">' + Reader.makeClickable(displaySubtitle) + '</p>' : '') +
                '<span class="story-level-badge">' + esc(level) + '</span>' +
            '</div>' +
        '</div>' +
        '<div class="story-marks-row">' +
            '<span class="story-marks-label" id="story-marks-label">Mark words you\'re learning</span>' +
            '<button type="button" class="geo-toggle" id="story-marks-toggle" role="switch" aria-labelledby="story-marks-label" aria-checked="' + marksChecked + '">' +
                '<span class="geo-toggle-track"></span>' +
                '<span class="geo-toggle-shape geo-toggle-shape--off"></span>' +
                '<span class="geo-toggle-shape geo-toggle-shape--on"></span>' +
            '</button>' +
        '</div>' +
        '<div class="story-scroll-track" aria-hidden="true"><div class="story-scroll-bar" id="story-scroll-bar"></div></div>' +
        '<div class="story-body' + (isBookFormat ? ' lt-book-body' : '') + '">';

        let seenOpeningNarration = false;
        const playableParagraphs = [];
        for (let idx = bodyStartIndex; idx < paragraphs.length; idx++) {
            const p = (paragraphs[idx] || '').trim();
            if (!p) continue;
            if (/^(?:\*\s*\*\s*\*|\-{3,}|•\s*•\s*•|~{3,})$/.test(p)) {
                html += '<hr class="lt-scene-break" aria-hidden="true">';
                seenOpeningNarration = false;
                continue;
            }
            const isDialogue = /^[-—–―«"“]/.test(p);
            const isFirstNarration = isBookFormat && !seenOpeningNarration && !isDialogue;
            if (!isDialogue) seenOpeningNarration = true;

            const paraClasses = ['story-paragraph', isDialogue ? 'dialogue lt-book-dialogue' : 'narration'];
            if (isFirstNarration) paraClasses.push('lt-first-para');

            const playableIdx = playableParagraphs.length;
            playableParagraphs.push({
                text: p,
                type: isDialogue ? 'dialogue' : 'narration'
            });

            html += '<p class="' + paraClasses.join(' ') + '" data-para-index="' + playableIdx + '">' +
                Reader.makeClickable(p) +
            '</p>';
        }
        html += '</div>';

        // End of chapter navigation: advance directly to next chapter without a word review screen
        const hasNext = chapterIndex < totalCh - 1;
        const nextChapter = hasNext ? chapters[chapterIndex + 1] : null;
        html += '<div class="story-finish lt-chapter-finish">' +
            (hasNext
                ? `<p class="lt-next-ch-label">Up next: <strong>${esc(nextChapter.title)}${nextChapter.subtitle ? ' — ' + esc(nextChapter.subtitle) : ''}</strong></p>` +
                  `<div class="lt-finish-actions">` +
                      (chapterIndex > 0 ? `<button type="button" class="dk-secondary" data-mytext-prev-ch="1">&larr; Previous chapter</button>` : '') +
                      `<button type="button" class="btn-primary" data-mytext-next-ch="1">Next chapter &rarr;</button>` +
                  `</div>`
                : `<div class="lt-finish-actions">` +
                      (chapterIndex > 0 ? `<button type="button" class="dk-secondary" data-mytext-prev-ch="1">&larr; Previous chapter</button>` : '') +
                      `<button type="button" class="btn-primary" data-mytext-finish-book="1">Finish ${isMulti ? 'book' : 'reading'} ✓</button>` +
                  `</div>`) +
        '</div>';

        // Floating Substack-like audio player at the bottom of the reader
        const playIconHtml = (typeof Art !== 'undefined' && Art.icon) ? Art.icon('play') : '▶';
        html += '<div class="story-substack-player" id="story-substack-player" role="region" aria-label="Story narration">' +
            '<button type="button" class="ssp-play-btn" id="story-audio-play-btn" aria-label="Play story">' +
                '<span class="ssp-icon">' + playIconHtml + '</span>' +
            '</button>' +
            '<div class="ssp-track">' +
                '<div class="ssp-meta">' +
                    '<span class="ssp-label">Listen along</span>' +
                    '<span class="ssp-speaker-tag hidden" id="ssp-speaker-tag"></span>' +
                '</div>' +
                '<div class="ssp-scrubber-row">' +
                    '<span class="ssp-time" id="story-audio-time-cur">0:00</span>' +
                    '<input type="range" class="ssp-slider" id="story-audio-slider" min="0" max="100" value="0" aria-label="Narration position">' +
                    '<span class="ssp-time" id="story-audio-time-rem">-0:00</span>' +
                '</div>' +
            '</div>' +
            '<button type="button" class="ssp-speed-btn" id="story-audio-speed-btn" title="Playback speed">1×</button>' +
        '</div>';

        container.innerHTML = html;

        const backBtn = container.querySelector('[data-mytext-back]');
        if (backBtn) {
            backBtn.onclick = () => {
                if (isMulti) activeBookId = t.id;
                closeMyText();
            };
        }

        const chSelect = document.getElementById('lt-reader-chapter-select');
        if (chSelect) {
            chSelect.onchange = e => {
                const targetIdx = parseInt(e.target.value, 10);
                if (!isNaN(targetIdx)) openMyText(t.id, targetIdx);
            };
        }

        const marksToggle = document.getElementById('story-marks-toggle');
        if (marksToggle) {
            marksToggle.addEventListener('click', () => {
                const on = marksToggle.getAttribute('aria-checked') !== 'true';
                marksToggle.setAttribute('aria-checked', on ? 'true' : 'false');
                if (typeof setReaderMarks === 'function') setReaderMarks(on);
            });
        }

        const prevBtn = container.querySelector('[data-mytext-prev-ch]');
        if (prevBtn) {
            prevBtn.onclick = () => {
                if (chapterIndex > 0) return openMyText(t.id, chapterIndex - 1);
            };
        }

        const nextBtn = container.querySelector('[data-mytext-next-ch]');
        if (nextBtn) {
            nextBtn.onclick = () => {
                markChapterComplete(t, chapterIndex, chapterIndex + 1);
                return openMyText(t.id, chapterIndex + 1);
            };
        }

        const finishBtn = container.querySelector('[data-mytext-finish-book]');
        if (finishBtn) {
            finishBtn.onclick = () => {
                markChapterComplete(t, chapterIndex, null);
                if (isMulti) activeBookId = t.id;
                closeMyText();
            };
        }

        showReading();
        if (typeof StoryAudioPlayer !== 'undefined' && StoryAudioPlayer.init) {
            StoryAudioPlayer.init({
                id: t.id + '-ch-' + chapterIndex,
                title: isMulti ? chapter.title : t.title,
                paragraphs: playableParagraphs
            }, container);
            if (t.progress && t.progress.chapterIndex === chapterIndex && t.progress.paraIndex > 0 && playableParagraphs.length > 0) {
                StoryAudioPlayer.currentParaIndex = Math.min(playableParagraphs.length - 1, t.progress.paraIndex);
                if (typeof StoryAudioPlayer.updateProgressUI === 'function') {
                    StoryAudioPlayer.updateProgressUI();
                }
            }
        }
        if (typeof updateReaderWordColors === 'function') updateReaderWordColors();
        restoreMyTextPosition(t, chapterIndex);
        wireMyTextScrollProgress(t.id, chapterIndex);
    }

    function markChapterComplete(t, completedIdx, nextIdx) {
        if (!t) return;
        if (!t.progress) {
            t.progress = { chapterIndex: 0, pct: 0, paraIndex: 0, readChapters: [], at: Date.now() };
        }
        if (!Array.isArray(t.progress.readChapters)) t.progress.readChapters = [];
        const firstTime = !t.progress.readChapters.includes(completedIdx);
        if (firstTime) t.progress.readChapters.push(completedIdx);

        if (nextIdx !== null && nextIdx !== undefined) {
            t.progress.chapterIndex = nextIdx;
            t.progress.pct = 0;
            t.progress.paraIndex = 0;
        } else {
            t.progress.pct = 0;
            t.progress.paraIndex = 0;
        }
        t.progress.at = Date.now();
        saveMyTexts();

        if (typeof recordStoryCompleted === 'function') {
            recordStoryCompleted(firstTime);
        }
    }

    function closeMyText() {
        if (typeof StoryAudioPlayer !== 'undefined' && StoryAudioPlayer.teardown) {
            StoryAudioPlayer.teardown();
        }
        if (window._storyScrollListener && typeof window.removeEventListener === 'function') {
            window.removeEventListener('scroll', window._storyScrollListener);
            window._storyScrollListener = null;
        }
        activeReading = null;
        const container = document.getElementById('reader-content');
        if (container) {
            container.innerHTML = '';
            container.classList.add('hidden');
        }
        returnFromReading();
    }

    // ----------------------------------------
    // SECTION SWITCHING (Parlour / Saved / My Texts / reading)
    // ----------------------------------------
    function showSection(section) {
        if (typeof StoryAudioPlayer !== 'undefined' && StoryAudioPlayer.teardown) {
            StoryAudioPlayer.teardown();
        }
        activeSection = PANES[section] ? section : 'parlour';

        document.querySelectorAll('#lib-subnav [data-lib-tab]').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-lib-tab') === activeSection);
        });
        Object.keys(PANES).forEach(key => {
            const el = document.getElementById(PANES[key]);
            if (el) el.classList.toggle('hidden', key !== activeSection);
        });
        const content = document.getElementById('reader-content');
        if (content) content.classList.add('hidden');
        const subnav = document.getElementById('lib-subnav');
        if (subnav) subnav.classList.remove('hidden');

        if (activeSection === 'parlour' && typeof Reader !== 'undefined') {
            const el = document.getElementById('reader-library');
            if (el) Reader.buildLibraryUI(el);
        } else if (activeSection === 'saved') {
            renderSavedList();
        } else if (activeSection === 'mytexts') {
            renderMyTextsPane();
        }
    }

    function showReading() {
        const subnav = document.getElementById('lib-subnav');
        if (subnav) subnav.classList.add('hidden');
        Object.keys(PANES).forEach(key => {
            const el = document.getElementById(PANES[key]);
            if (el) el.classList.add('hidden');
        });
        const content = document.getElementById('reader-content');
        if (content) content.classList.remove('hidden');
    }

    function returnFromReading() {
        showSection(activeSection);
    }

    // ----------------------------------------
    // INIT
    // ----------------------------------------
    function init() {
        loadSaved();
        loadMyTexts();

        const subnav = document.getElementById('lib-subnav');
        if (subnav) {
            subnav.addEventListener('click', e => {
                const btn = e.target.closest('[data-lib-tab]');
                if (btn) {
                    activeBookId = null;
                    showSection(btn.getAttribute('data-lib-tab'));
                }
            });
        }

        const savedEl = document.getElementById('lib-saved');
        if (savedEl) {
            savedEl.addEventListener('click', e => {
                const openBtn = e.target.closest('[data-saved-open]');
                if (openBtn) { Reader.loadStory(openBtn.getAttribute('data-saved-open')); return; }
                const removeBtn = e.target.closest('[data-saved-remove]');
                if (removeBtn) { toggleSave(removeBtn.getAttribute('data-saved-remove')); renderSavedList(); }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    return {
        isSaved,
        toggleSave,
        showReading,
        returnFromReading,
        showSection,
        analyseText,
        openMyText,
        openMyTextOrChapters,
        buildChaptersFromText,
        parseDocumentFile,
        _parseEpub: parseEpub,
        _parseDocx: parseDocx
    };
})();
