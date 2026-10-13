// ==========================================================
// Unit & Integration Tests: Library Long Texts, EPUB/DOCX,
// Auto-Chunking, Chapter TOC, Single-Chapter Reader & Progress
// ==========================================================
const assert = require('assert');
const zlib = require('zlib');

// Minimal ZIP builder for testing real compressed .epub and .docx archives
function buildZipBuffer(files) {
    const localParts = [];
    const centralParts = [];
    let offset = 0;

    for (const f of files) {
        const nameBuf = Buffer.from(f.name, 'utf8');
        const rawBuf = Buffer.isBuffer(f.data) ? f.data : Buffer.from(f.data, 'utf8');
        const method = f.store ? 0 : 8;
        const compBuf = method === 8 ? zlib.deflateRawSync(rawBuf) : rawBuf;

        // Local file header (30 bytes + name)
        const lh = Buffer.alloc(30);
        lh.writeUInt32LE(0x04034b50, 0);
        lh.writeUInt16LE(20, 4);
        lh.writeUInt16LE(0, 6);
        lh.writeUInt16LE(method, 8);
        lh.writeUInt16LE(0, 10);
        lh.writeUInt16LE(0, 12);
        lh.writeUInt32LE(0, 14); // crc32 (unused by unpacker)
        lh.writeUInt32LE(compBuf.length, 18);
        lh.writeUInt32LE(rawBuf.length, 22);
        lh.writeUInt16LE(nameBuf.length, 26);
        lh.writeUInt16LE(0, 28);

        localParts.push(lh, nameBuf, compBuf);

        // Central directory header (46 bytes + name)
        const cd = Buffer.alloc(46);
        cd.writeUInt32LE(0x02014b50, 0);
        cd.writeUInt16LE(20, 4);
        cd.writeUInt16LE(20, 6);
        cd.writeUInt16LE(0, 8);
        cd.writeUInt16LE(method, 10);
        cd.writeUInt16LE(0, 12);
        cd.writeUInt16LE(0, 14);
        cd.writeUInt32LE(0, 16);
        cd.writeUInt32LE(compBuf.length, 20);
        cd.writeUInt32LE(rawBuf.length, 24);
        cd.writeUInt16LE(nameBuf.length, 28);
        cd.writeUInt16LE(0, 30);
        cd.writeUInt16LE(0, 32);
        cd.writeUInt16LE(0, 34);
        cd.writeUInt16LE(0, 36);
        cd.writeUInt32LE(0, 38);
        cd.writeUInt32LE(offset, 42);

        centralParts.push(cd, nameBuf);
        offset += lh.length + nameBuf.length + compBuf.length;
    }

    const cdStart = offset;
    const cdBuf = Buffer.concat(centralParts);
    const eocd = Buffer.alloc(22);
    eocd.writeUInt32LE(0x06054b50, 0);
    eocd.writeUInt16LE(0, 4);
    eocd.writeUInt16LE(0, 6);
    eocd.writeUInt16LE(files.length, 8);
    eocd.writeUInt16LE(files.length, 10);
    eocd.writeUInt32LE(cdBuf.length, 12);
    eocd.writeUInt32LE(cdStart, 16);
    eocd.writeUInt16LE(0, 20);

    const full = Buffer.concat([...localParts, cdBuf, eocd]);
    return full.buffer.slice(full.byteOffset, full.byteOffset + full.byteLength);
}

// Set up mock browser environment
global.window = global;
global.window.innerHeight = 800;
global.window.scrollY = 0;
global.window.scrollTo = (x, y) => { global.window.scrollY = y; };
global.requestAnimationFrame = (fn) => fn();
global.confirm = () => true;

const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: (k) => { delete mockStorage[k]; },
    clear: () => { Object.keys(mockStorage).forEach(k => delete mockStorage[k]); }
};

global.Lang = {
    code: () => 'es',
    name: () => 'Spanish',
    key: (k) => `es:${k}`,
    targetLemma: (c) => c.spanish
};

global.Lexicon = {
    isLoaded: () => true,
    load: async () => {},
    withArticle: (w) => w,
    shortGloss: (g) => g,
    frequencyRank: () => 500,
    lookup: (w) => ({
        readings: [{ lemma: w.toLowerCase(), translation: 'gloss-' + w.toLowerCase(), pos: 'noun' }]
    })
};

global.Reader = {
    stories: [],
    ensureStories: async () => [],
    makeClickable: (text) => text.replace(/([a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+)/g, '<span class="word" data-word="$1">$1</span>')
};

let completedStoryCalls = 0;
global.recordStoryCompleted = () => { completedStoryCalls++; };
global.updateReaderWordColors = () => {};

// Minimal DOM mock for #lib-mytexts, #reader-content, #lib-subnav
const elementsById = {};
function makeEl(id) {
    return {
        id: id,
        _html: '',
        _nodes: [],
        style: {},
        textContent: '',
        value: '',
        disabled: false,
        get innerHTML() { return this._html; },
        set innerHTML(v) {
            this._html = String(v || '');
            this._nodes = [];
            const tagRe = /<([a-zA-Z0-9]+)\b([^>]*)>/g;
            let m;
            while ((m = tagRe.exec(this._html)) !== null) {
                const attrs = {};
                const attrRe = /([a-zA-Z0-9\-]+)="([^"]*)"/g;
                let am;
                while ((am = attrRe.exec(m[2])) !== null) {
                    attrs[am[1]] = am[2];
                }
                const node = {
                    tagName: m[1].toUpperCase(),
                    _attrs: attrs,
                    style: {},
                    value: '',
                    disabled: false,
                    onclick: null,
                    onchange: null,
                    oninput: null,
                    getAttribute(k) { return this._attrs[k] !== undefined ? this._attrs[k] : null; },
                    setAttribute(k, val) { this._attrs[k] = String(val); },
                    addEventListener(ev, fn) { if (ev === 'click') this.onclick = fn; }
                };
                if (attrs.id) elementsById[attrs.id] = node;
                this._nodes.push(node);
            }
        },
        classList: {
            _set: new Set(),
            add(c) { this._set.add(c); },
            remove(c) { this._set.delete(c); },
            toggle(c, force) {
                if (force === undefined) force = !this._set.has(c);
                if (force) this._set.add(c); else this._set.delete(c);
                return !this._set.has(c);
            },
            contains(c) { return this._set.has(c); }
        },
        setAttribute() {},
        getAttribute() { return null; },
        addEventListener() {},
        querySelector(sel) {
            return this.querySelectorAll(sel)[0] || null;
        },
        querySelectorAll(sel) {
            const attrMatch = sel.match(/^\[([a-zA-Z0-9\-]+)(?:="([^"]+)")?\]$/);
            if (!attrMatch) return [];
            const attr = attrMatch[1];
            const expectedVal = attrMatch[2];
            return this._nodes.filter(n => {
                if (n._attrs[attr] === undefined) return false;
                return expectedVal === undefined || n._attrs[attr] === expectedVal;
            });
        }
    };
}

['reader-library', 'lib-saved', 'lib-mytexts', 'reader-content', 'lib-subnav', 'lt-text-title', 'lt-text-body', 'lt-reader-chapter-select', 'story-marks-toggle', 'story-scroll-bar'].forEach(id => {
    elementsById[id] = makeEl(id);
});

global.document = {
    readyState: 'complete',
    getElementById: (id) => elementsById[id] || null,
    querySelector: (sel) => {
        if (sel === '#reader-content .story-body') {
            return {
                getBoundingClientRect: () => ({ top: -100, height: 1200 }),
                querySelectorAll: () => [{
                    getBoundingClientRect: () => ({ top: 90, bottom: 130 }),
                    getAttribute: () => '2'
                }],
                querySelector: () => ({
                    getBoundingClientRect: () => ({ top: 150, bottom: 190 })
                })
            };
        }
        return null;
    },
    querySelectorAll: () => [],
    addEventListener: () => {}
};

const Library = require('../../engine/library.js') || global.Library;
const Lib = global.Library || eval(require('fs').readFileSync(require.resolve('../../engine/library.js'), 'utf8') + '; Library;');

async function runTests() {
    console.log('1. Testing explicit chapter splitting on plain text...');
    const sampleWithHeadings = [
        'Capítulo 1: El comienzo\nHabía una vez un pequeño pueblo en las montañas donde todos se conocían.',
        'La vida era tranquila y el río corría limpio durante todo el año.',
        'Capítulo 2: El viaje\nUna mañana de otoño, Carlos preparó su maleta y salió hacia la estación.',
        'El tren llegó puntual entre la niebla de la mañana.'
    ].join('\n\n');

    const chs1 = Lib.buildChaptersFromText(sampleWithHeadings, 'Mi Novela');
    assert.strictEqual(chs1.length, 2, 'Should split into 2 chapters');
    assert.strictEqual(chs1[0].title, 'Capítulo 1: El comienzo');
    assert.strictEqual(chs1[0].paragraphs.length, 2);
    assert.strictEqual(chs1[1].title, 'Capítulo 2: El viaje');
    assert.strictEqual(chs1[1].paragraphs.length, 2);
    console.log('   ✓ Explicit chapter headings split cleanly.');

    console.log('2. Testing auto-chunking of unchaptered long texts (>3,500 words)...');
    const hundredWordPara = Array.from({ length: 100 }, (_, i) => 'palabra' + (i + 1)).join(' ') + '.';
    const fortyTwoParas = Array.from({ length: 42 }, () => hundredWordPara).join('\n\n'); // 4,200 words
    const chsAuto = Lib.buildChaptersFromText(fortyTwoParas, 'Ensayo Largo');
    assert.strictEqual(chsAuto.length, 2, '4,200-word unchaptered text should auto-chunk into 2 parts');
    assert.strictEqual(chsAuto[0].title, 'Part 1');
    assert.strictEqual(chsAuto[1].title, 'Part 2');
    assert.strictEqual(chsAuto[0].wordCount, 2500);
    assert.strictEqual(chsAuto[1].wordCount, 1700);
    console.log('   ✓ Unchaptered long text auto-chunked into Part 1 (2,500 words) and Part 2 (1,700 words).');

    console.log('3. Testing client-side EPUB parser (compressed ZIP archive)...');
    const epubBuffer = buildZipBuffer([
        {
            name: 'mimetype',
            data: 'application/epub+zip',
            store: true
        },
        {
            name: 'META-INF/container.xml',
            data: `<?xml version="1.0"?>
                <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
                    <rootfiles>
                        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
                    </rootfiles>
                </container>`
        },
        {
            name: 'OEBPS/content.opf',
            data: `<?xml version="1.0" encoding="utf-8"?>
                <package xmlns="http://www.idpf.org/2007/opf" version="2.0">
                    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
                        <dc:title>Don Quijote de la Mancha</dc:title>
                        <dc:creator>Miguel de Cervantes</dc:creator>
                    </metadata>
                    <manifest>
                        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
                        <item id="cover" href="Text/cover.xhtml" media-type="application/xhtml+xml"/>
                        <item id="ch1" href="Text/cap1.xhtml" media-type="application/xhtml+xml"/>
                        <item id="ch2" href="Text/cap2.xhtml" media-type="application/xhtml+xml"/>
                    </manifest>
                    <spine toc="ncx">
                        <itemref idref="cover"/>
                        <itemref idref="ch1"/>
                        <itemref idref="ch2"/>
                    </spine>
                </package>`
        },
        {
            name: 'OEBPS/toc.ncx',
            data: `<?xml version="1.0" encoding="utf-8"?>
                <ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
                    <navMap>
                        <navPoint id="nav1" playOrder="1">
                            <navLabel><text>Capítulo Primero</text></navLabel>
                            <content src="Text/cap1.xhtml"/>
                        </navPoint>
                        <navPoint id="nav2" playOrder="2">
                            <navLabel><text>Capítulo Segundo</text></navLabel>
                            <content src="Text/cap2.xhtml#top"/>
                        </navPoint>
                    </navMap>
                </ncx>`
        },
        {
            name: 'OEBPS/Text/cover.xhtml',
            data: `<html><body><p>Portada</p></body></html>` // < 15 words front-matter stub, should be skipped
        },
        {
            name: 'OEBPS/Text/cap1.xhtml',
            data: `<html><head><title>Ignored</title><style>body{color:red}</style></head><body>
                <h1>Capítulo Primero</h1>
                <p>En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero.</p>
                <p>Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte.</p>
            </body></html>`
        },
        {
            name: 'OEBPS/Text/cap2.xhtml',
            data: `<html><body>
                <h2>Capítulo Segundo</h2>
                <p>Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento, apretándole a ello la falta que él pensaba que hacía en el mundo su tardanza.</p>
            </body></html>`
        }
    ]);

    const parsedEpub = await Lib._parseEpub(epubBuffer, 'quijote');
    assert.strictEqual(parsedEpub.title, 'Don Quijote de la Mancha');
    assert.strictEqual(parsedEpub.author, 'Miguel de Cervantes');
    assert.strictEqual(parsedEpub.chapters.length, 2, 'Front-matter cover stub (<15 words) should be filtered out, leaving 2 chapters');
    assert.strictEqual(parsedEpub.chapters[0].title, 'Capítulo Primero');
    assert.strictEqual(parsedEpub.chapters[0].paragraphs.length, 2);
    assert(parsedEpub.chapters[0].paragraphs[0].includes('En un lugar de la Mancha'));
    assert.strictEqual(parsedEpub.chapters[1].title, 'Capítulo Segundo');
    assert.strictEqual(parsedEpub.chapters[1].paragraphs.length, 1);
    console.log('   ✓ EPUB parsed title, author, NCX TOC chapter titles, and paragraphs accurately.');

    console.log('4. Testing client-side DOCX parser (compressed ZIP archive)...');
    const docxBuffer = buildZipBuffer([
        {
            name: 'docProps/core.xml',
            data: `<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">
                <dc:title>Crónica de Viaje</dc:title>
                <dc:creator>Elena Gómez</dc:creator>
            </cp:coreProperties>`
        },
        {
            name: 'word/document.xml',
            data: `<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
                <w:body>
                    <w:p>
                        <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
                        <w:r><w:t>Primera Parte: Madrid</w:t></w:r>
                    </w:p>
                    <w:p>
                        <w:r><w:t>Llegamos a la estación de Atocha temprano por la mañana y tomamos un café caliente.</w:t></w:r>
                    </w:p>
                    <w:p>
                        <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
                        <w:r><w:t>Segunda Parte: Sevilla</w:t></w:r>
                    </w:p>
                    <w:p>
                        <w:r><w:t>El río Guadalquivir brillaba bajo el sol de la tarde mientras caminábamos por Triana.</w:t></w:r>
                    </w:p>
                </w:body>
            </w:document>`
        }
    ]);

    const parsedDocx = await Lib._parseDocx(docxBuffer, 'viaje');
    assert.strictEqual(parsedDocx.title, 'Crónica de Viaje');
    assert.strictEqual(parsedDocx.author, 'Elena Gómez');
    assert.strictEqual(parsedDocx.chapters.length, 2);
    assert.strictEqual(parsedDocx.chapters[0].title, 'Primera Parte: Madrid');
    assert(parsedDocx.chapters[0].paragraphs[0].includes('estación de Atocha'));
    assert.strictEqual(parsedDocx.chapters[1].title, 'Segunda Parte: Sevilla');
    assert(parsedDocx.chapters[1].paragraphs[0].includes('Guadalquivir'));
    console.log('   ✓ DOCX parsed core metadata, Heading1 chapter splits, and paragraph runs accurately.');

    console.log('5. Testing end-to-end Book Import, Storage Compactness, Chapter View, Next Chapter, & Tap-to-Translate...');
    Lib.showSection('mytexts');
    const host = elementsById['lib-mytexts'];
    const addBtn = host.querySelector('[data-text-add]');
    assert(addBtn && addBtn.onclick, 'Should render + Add text or book button');
    addBtn.onclick();

    // Simulate importing the EPUB file via parseDocumentFile
    const fakeFile = {
        name: 'quijote.epub',
        arrayBuffer: async () => epubBuffer
    };
    const fileDoc = await Lib.parseDocumentFile(fakeFile);
    assert.strictEqual(fileDoc.chapters.length, 2);

    // Populate editor draft and save & read
    elementsById['lt-text-title'].value = sampleWithHeadings;
    // Trigger paste of multi-chapter text and save
    const bodyInput = host.querySelector('[data-text-save-read]');
    // Set draft via simulated input:
    // Let's re-wire with simulated title and body
    const savedRawBefore = localStorage.getItem('es:myTexts');
    assert.strictEqual(savedRawBefore, null);

    // Seed a multi-chapter book in localStorage and open it
    const bookId = 'text-test-book-1';
    localStorage.setItem('es:myTexts', JSON.stringify([{
        id: bookId,
        title: 'Don Quijote',
        author: 'Cervantes',
        sourceType: 'epub',
        text: sampleWithHeadings,
        created: new Date().toISOString(),
        modified: new Date().toISOString(),
        analysis: Lib.analyseText(sampleWithHeadings)
    }]));

    // Reload Library myTexts (triggers migration that strips lemmas from localStorage and builds chapters)
    const Lib2 = eval(require('fs').readFileSync(require.resolve('../../engine/library.js'), 'utf8') + '; Library;');
    const storedAfterMigration = JSON.parse(localStorage.getItem('es:myTexts'));
    assert.strictEqual(storedAfterMigration.length, 1);
    assert.strictEqual(storedAfterMigration[0].chapters.length, 2, 'Should migrate multi-chapter text into chapters metadata');
    assert.strictEqual(storedAfterMigration[0].analysis.lemmas, undefined, 'Should strip heavy lemmas array from localStorage so 500+ books fit');
    assert.strictEqual(storedAfterMigration[0].text, undefined, 'Multi-chapter book text should live in BookStore, not localStorage');

    // Open book -> should open Chapter Table of Contents first
    Lib2.openMyTextOrChapters(bookId);
    assert(host.innerHTML.includes('Capítulo 1: El comienzo'), 'TOC view should list Chapter 1');
    assert(host.innerHTML.includes('Capítulo 2: El viaje'), 'TOC view should list Chapter 2');
    assert(host.innerHTML.includes('Start reading — Capítulo 1: El comienzo'), 'TOC view should show Start reading CTA');

    // Open Chapter 1 (index 0)
    await Lib2.openMyText(bookId, 0);
    const readerEl = elementsById['reader-content'];
    assert(readerEl.innerHTML.includes('Capítulo 1: El comienzo'), 'Reader should render Chapter 1 title');
    assert(!readerEl.innerHTML.includes('data-word="tren"'), 'Reader should NOT render Chapter 2 paragraphs while in Chapter 1');
    assert(readerEl.innerHTML.includes('<span class="word" data-word="pueblo">pueblo</span>'), 'Reader should wrap words in .word spans for tap-to-translate');
    assert(readerEl.innerHTML.includes('data-para-index="0"'), 'Reader should include data-para-index for paragraph-accurate bookmarking');
    assert(readerEl.innerHTML.includes('Next chapter &rarr;'), 'Chapter 1 footer should show Next chapter button without word review');

    // Click "Next chapter ->" button
    const nextBtn = readerEl.querySelector('[data-mytext-next-ch]');
    assert(nextBtn && nextBtn.onclick, 'Next chapter button should be wired');
    const prevCompleted = completedStoryCalls;
    await nextBtn.onclick();

    assert.strictEqual(completedStoryCalls, prevCompleted + 1, 'Finishing a chapter should credit reading activity');
    assert(readerEl.innerHTML.includes('Capítulo 2: El viaje'), 'Clicking Next chapter should immediately open Chapter 2');
    assert(readerEl.innerHTML.includes('<span class="word" data-word="tren">tren</span>'), 'Chapter 2 body should be rendered with clickable word spans');
    assert(readerEl.innerHTML.includes('Finish book ✓'), 'Final chapter should show Finish book button');

    const storedProgress = JSON.parse(localStorage.getItem('es:myTexts'))[0].progress;
    assert(storedProgress.readChapters.includes(0), 'Chapter 1 (index 0) should be marked read');
    assert.strictEqual(storedProgress.chapterIndex, 1, 'Saved location should now be on Chapter 2 (index 1)');

    console.log('   ✓ End-to-end TOC, single-chapter rendering, tap-to-translate spans, Next Chapter flow, and progress persistence verified.');

    console.log('6. Testing EPUB front-matter filtering, chapter subtitles, book formatting, and manual chapter removal...');
    const riordanStyleEpub = buildZipBuffer([
        { name: 'mimetype', data: 'application/epub+zip', store: true },
        {
            name: 'META-INF/container.xml',
            data: `<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>`
        },
        {
            name: 'OEBPS/content.opf',
            data: `<?xml version="1.0" encoding="utf-8"?>
                <package xmlns="http://www.idpf.org/2007/opf" version="2.0">
                    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
                        <dc:title>El ladrón del rayo</dc:title>
                        <dc:creator>Rick Riordan</dc:creator>
                    </metadata>
                    <manifest>
                        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
                        <item id="cubierta.xhtml" href="Text/cubierta.xhtml" media-type="application/xhtml+xml"/>
                        <item id="sinopsis.xhtml" href="Text/sinopsis.xhtml" media-type="application/xhtml+xml"/>
                        <item id="titulo.xhtml" href="Text/titulo.xhtml" media-type="application/xhtml+xml"/>
                        <item id="info.xhtml" href="Text/info.xhtml" media-type="application/xhtml+xml"/>
                        <item id="cap1" href="Text/Capitulo_01.xhtml" media-type="application/xhtml+xml"/>
                        <item id="cap2" href="Text/Capitulo_02.xhtml" media-type="application/xhtml+xml"/>
                    </manifest>
                    <spine toc="ncx">
                        <itemref idref="cubierta.xhtml"/>
                        <itemref idref="sinopsis.xhtml"/>
                        <itemref idref="titulo.xhtml"/>
                        <itemref idref="info.xhtml"/>
                        <itemref idref="cap1"/>
                        <itemref idref="cap2"/>
                    </spine>
                    <guide>
                        <reference type="cover" title="Portada" href="Text/cubierta.xhtml"/>
                        <reference type="title-page" title="Página de título" href="Text/titulo.xhtml"/>
                        <reference type="copyright-page" title="Créditos" href="Text/info.xhtml"/>
                    </guide>
                </package>`
        },
        {
            name: 'OEBPS/toc.ncx',
            data: `<?xml version="1.0" encoding="utf-8"?>
                <ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
                    <navMap>
                        <navPoint id="n1" playOrder="1"><navLabel><text>Cubierta</text></navLabel><content src="Text/cubierta.xhtml"/></navPoint>
                        <navPoint id="n2" playOrder="2"><navLabel><text>El ladrón del rayo</text></navLabel><content src="Text/titulo.xhtml"/></navPoint>
                        <navPoint id="n3" playOrder="3"><navLabel><text>Capítulo 1</text></navLabel><content src="Text/Capitulo_01.xhtml"/></navPoint>
                        <navPoint id="n4" playOrder="4"><navLabel><text>Capítulo 2</text></navLabel><content src="Text/Capitulo_02.xhtml"/></navPoint>
                    </navMap>
                </ncx>`
        },
        { name: 'OEBPS/Text/cubierta.xhtml', data: `<html><body class="sinmargen"><div class="cubierta"></div></body></html>` },
        {
            name: 'OEBPS/Text/sinopsis.xhtml',
            data: `<html><head><title>Sinopsis</title></head><body><div class="sinopsis"><p>¿Qué pasaría si un día descubrieras que, en realidad, eres hijo de un dios griego que debe cumplir una misión secreta? Pues eso es lo que le sucede a Percy Jackson.</p></div></body></html>`
        },
        {
            name: 'OEBPS/Text/titulo.xhtml',
            data: `<html><head><title>Título</title></head><body><p class="tautor">Rick Riordan</p><h1 class="ttitulo">El ladrón del rayo</h1><p class="tserie">Percy Jackson y los dioses del Olimpo - 1</p><p class="trevision">ePub r1.9 Titivillus 30.05.2019</p></body></html>`
        },
        {
            name: 'OEBPS/Text/info.xhtml',
            data: `<html><head><title>Créditos</title></head><body><div class="info"><p>Título original: The Lightning Thief Rick Riordan 2006 Traducción Libertad Aguilera Ballester Editor digital Titivillus Corrección de erratas r1.2 r1.3 r1.4</p></div></body></html>`
        },
        {
            name: 'OEBPS/Text/Capitulo_01.xhtml',
            data: `<html><body><h1 title="Capítulo 1">C<small>APÍTULO</small> 1</h1><p class="subtit">Pulverizo accidentalmente a mi profesora de introducción al álgebra</p><p class="asangre">Mira, yo no quería ser mestizo. Si estás leyendo esto porque crees que podrías estar en la misma situación, cierra el libro inmediatamente.</p><p>—Hola, Percy —dijo Grover mientras subíamos al autobús escolar amarillo.</p></body></html>`
        },
        {
            name: 'OEBPS/Text/Capitulo_02.xhtml',
            data: `<html><body><h1 title="Capítulo 2">C<small>APÍTULO</small> 2</h1><p class="subtit">Tres ancianas tejen los calcetines de la muerte</p><p class="asangre">Estaba acostumbrado a tener experiencias raras de vez en cuando, pero solían acabarse pronto y nadie me creía jamás en el colegio.</p></body></html>`
        }
    ]);

    const parsedRiordan = await Lib2._parseEpub(riordanStyleEpub, 'El ladrón del rayo');
    assert.strictEqual(parsedRiordan.chapters.length, 2, 'Should automatically filter out sinopsis, titulo, and info front-matter pages');
    assert.strictEqual(parsedRiordan.chapters[0].title, 'Capítulo 1');
    assert.strictEqual(parsedRiordan.chapters[0].subtitle, 'Pulverizo accidentalmente a mi profesora de introducción al álgebra');
    assert(parsedRiordan.chapters[0].paragraphs[0].startsWith('Mira, yo no quería ser mestizo'), 'Subtitle should be extracted into chapter.subtitle, not left as paragraph 0');

    // Verify centered book chapter header, subtitle, first-para and dialogue formatting in reader
    await Lib2.openMyText(bookId, 0);
    assert(readerEl.innerHTML.includes('lt-book-chapter-header'), 'Book reader should use centered lt-book-chapter-header');
    assert(readerEl.innerHTML.includes('lt-chapter-heading'), 'Book reader should style chapter title with lt-chapter-heading');
    assert(readerEl.innerHTML.includes('lt-book-body'), 'Book reader should style prose container with lt-book-body');
    assert(readerEl.innerHTML.includes('lt-first-para'), 'First narrative paragraph should receive lt-first-para class');

    // Verify manual chapter deletion from Book Overview TOC
    Lib2.openMyTextOrChapters(bookId);
    const deleteChBtns = host.querySelectorAll('[data-book-delete-ch]');
    assert.strictEqual(deleteChBtns.length, 2, 'TOC should render remove button on each chapter when >1 chapters exist');
    await deleteChBtns[0].onclick({});
    const remainingBook = JSON.parse(localStorage.getItem('es:myTexts'))[0];
    assert.strictEqual(remainingBook.chapters.length, 1, 'Deleting chapter 0 should leave 1 chapter');
    assert.strictEqual(remainingBook.chapters[0].title, 'Capítulo 2: El viaje');
    assert.strictEqual(remainingBook.progress.chapterIndex, 0, 'Reading progress chapterIndex should shift down when an earlier chapter is removed');
    console.log('   ✓ Front-matter filtering, chapter subtitles, book typography classes, and manual chapter removal verified.');

    console.log('\nAll Library book & chapter tests passed!');
}

runTests().catch(err => {
    console.error(err);
    process.exit(1);
});
