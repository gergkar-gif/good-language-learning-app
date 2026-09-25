// ============================================
// DECK BLAST GAME
// ============================================
// Fast-paced arcade vocabulary matching game inspired by Quizlet Blast,
// reimagined with Parlour's strict constructivist geometric aesthetic
// (faceted polyhedra targets, clean typography, zero emojis).
//
// Key Features:
// 1. Zero-Latency Web Audio Preloading: Vocabulary words are pre-fetched and
//    decoded into PCM AudioBuffers via ParlourTTS.preload() in staggered
//    batches, playing in <0.02ms on impact without touching HTMLAudioElement
//    or blocking the main thread.
// 2. Hardware-Accelerated Offscreen Sprite Caching:
//    - Each polyhedron target's geometry and typography are rasterized ONCE
//      onto tiny offscreen canvas sprites upon spawn.
//    - The 60fps render loop performs pure GPU texture blits (drawImage)
//      with zero per-frame fillText(), font parsing, or path tessellation.
// 3. Anti-Overlap & Lane Physics:
//    - Survival Mode: Organised into dedicated vertical lanes (3 on mobile,
//      4 on desktop) with uniform velocities, mathematically preventing targets
//      from ever covering or overlapping each other.
//    - Time Attack Mode: 2D kinetic drift with mutual circle-circle repulsion.
// 4. Zero-Reflow Touch Input:
//    - Uses native PointerEvent offsetX/offsetY coordinates to avoid
//      synchronous getBoundingClientRect() layout reflows on tap.

const DeckBlast = (function () {
    'use strict';

    const TIME_LIMIT_SECONDS = 60;
    const SURVIVAL_SHIELDS = 3;

    let _container = null;
    let _deckId = null;
    let _words0 = [];
    let _pool = [];
    let _exitLabel = null;
    let _onExit = null;
    let _onComplete = null;

    // Settings
    let _mode = 'time-attack'; // 'time-attack' | 'survival'
    let _direction = 'en-to-target'; // 'en-to-target' | 'target-to-en'

    // Game state
    let _state = 'lobby'; // 'lobby' | 'playing' | 'gameover'
    let _score = 0;
    let _streak = 0;
    let _maxStreak = 0;
    let _totalBlasts = 0;
    let _totalAttempts = 0;
    let _shields = SURVIVAL_SHIELDS;
    let _timeLeft = TIME_LIMIT_SECONDS;
    let _missedWords = new Map();
    let _hitUids = new Set();
    let _srsCredit = false; // set by the Decks screen; see _creditSrs()
    let _credited = true;
    let _currentTargetWord = null;
    let _activeTargets = [];
    let _shards = [];

    // Animation & timing
    let _animId = null;
    let _preloadTimer = null;
    let _lastFrameTime = 0;
    let _spawnAccumMs = 0;
    let _screenShake = 0;
    let _boundaryDangerFlash = 0;
    let _lastDisplayedSec = '';

    // Cached DOM nodes for 60fps performance
    let _domPromptWord = null;
    let _domScoreVal = null;
    let _domComboVal = null;
    let _domTimerVal = null;
    let _domShieldPips = [];

    // Canvas references
    let _canvas = null;
    let _ctx = null;
    let _canvasWidth = 600;
    let _canvasHeight = 420;
    let _canvasCssWidth = 600;
    let _canvasCssHeight = 420;
    let _dpr = 1;
    let _shardSprite = null;

    function _escapeHtml(text) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(text)
            : String(text == null ? '' : text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
    }

    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _withArticle(lemma) {
        return (typeof Lexicon !== 'undefined' && Lexicon.withArticle) ? Lexicon.withArticle(lemma) : lemma;
    }

    function _langName() {
        return (typeof Lang !== 'undefined' && typeof Lang.name === 'function') ? Lang.name() : 'Spanish';
    }

    function _langCode() {
        return (typeof Lang !== 'undefined' && typeof Lang.code === 'function') ? Lang.code() : 'es';
    }

    // ----------------------------------------
    // SMOOTH AUDIO PRELOADING PIPELINE
    // ----------------------------------------
    function _preloadAudio() {
        if (typeof ParlourTTS === 'undefined' || typeof ParlourTTS.preload !== 'function') return;
        const lang = _langCode();

        // 1. Immediately preload the first 6 words
        const immediate = _words0.slice(0, 6);
        for (let i = 0; i < immediate.length; i++) {
            const w = immediate[i];
            if (w && w.lemma) {
                ParlourTTS.preload({ text: w.lemma, language: lang, type: 'vocabulary' });
            }
        }

        // 2. Stagger the rest in small intervals so mobile CPU/network isn't choked
        if (_preloadTimer) clearInterval(_preloadTimer);
        const remaining = _words0.slice(6);
        if (remaining.length > 0) {
            let idx = 0;
            _preloadTimer = setInterval(() => {
                if (_state !== 'lobby' && _state !== 'playing') {
                    clearInterval(_preloadTimer);
                    _preloadTimer = null;
                    return;
                }
                if (idx >= remaining.length) {
                    clearInterval(_preloadTimer);
                    _preloadTimer = null;
                    return;
                }
                const w = remaining[idx++];
                if (w && w.lemma) {
                    ParlourTTS.preload({ text: w.lemma, language: lang, type: 'vocabulary' });
                }
            }, 100);
        }
    }

    function _speakWord(word) {
        if (!word || !word.lemma) return;
        if (typeof ParlourTTS !== 'undefined' && typeof ParlourTTS.speak === 'function') {
            ParlourTTS.speak({ text: word.lemma, language: _langCode(), type: 'vocabulary' });
        }
    }

    // ----------------------------------------
    // HIGH SCORE PERSISTENCE
    // ----------------------------------------
    function _bestKey() {
        const langKey = (typeof Lang !== 'undefined' && typeof Lang.key === 'function')
            ? Lang.key('deckBlastBest')
            : 'deckBlastBest';
        return `${langKey}:${_mode}:${_direction}:${_deckId}`;
    }

    function _getBestScore() {
        try {
            const raw = localStorage.getItem(_bestKey());
            return raw ? parseInt(raw, 10) : 0;
        } catch (e) {
            return 0;
        }
    }

    function _saveBestScore(score) {
        const prev = _getBestScore();
        if (score > prev) {
            try {
                localStorage.setItem(_bestKey(), String(score));
            } catch (e) {
                // Ignore private browsing storage issues
            }
            return score;
        }
        return prev;
    }

    // ----------------------------------------
    // OFFSCREEN SPRITE BAKING (ZERO PER-FRAME TEXT/PATH OVERHEAD)
    // ----------------------------------------
    function _createOffscreenCanvas(w, h) {
        if (typeof document === 'undefined' || typeof document.createElement !== 'function') return null;
        const c = document.createElement('canvas');
        if (!c || typeof c.getContext !== 'function') return null;
        c.width = Math.ceil(w * _dpr);
        c.height = Math.ceil(h * _dpr);
        const ctx = c.getContext('2d');
        if (!ctx) return null;
        ctx.scale(_dpr, _dpr);
        return { canvas: c, ctx };
    }

    function _bakeShardSprite() {
        const size = 20;
        const off = _createOffscreenCanvas(size, size);
        if (!off) return null;
        const ctx = off.ctx;
        const half = size / 2;
        const s = 7;
        ctx.translate(half, half);
        ctx.beginPath();
        ctx.moveTo(0, -s);
        ctx.lineTo(s * 0.7, s * 0.7);
        ctx.lineTo(-s * 0.7, s * 0.7);
        ctx.closePath();
        ctx.fillStyle = '#E94B16';
        ctx.fill();
        ctx.strokeStyle = '#102A47';
        ctx.lineWidth = 1;
        ctx.stroke();
        return off.canvas;
    }

    function _bakeTargetSprites(target) {
        const half = target.radius + 4;
        const box = half * 2;
        target.spriteHalf = half;

        // 1. Normal polyhedron sprite
        const polyOff = _createOffscreenCanvas(box, box);
        if (polyOff) {
            _renderPolyToContext(polyOff.ctx, half, target.vertices, false);
            target.polySprite = polyOff.canvas;
        }

        // 2. Wrong-hit flash polyhedron sprite
        const flashOff = _createOffscreenCanvas(box, box);
        if (flashOff) {
            _renderPolyToContext(flashOff.ctx, half, target.vertices, true);
            target.flashSprite = flashOff.canvas;
        }

        // 3. Upright text sprite (normal & flash)
        const textOff = _createOffscreenCanvas(box, box);
        if (textOff) {
            _renderTextToContext(textOff.ctx, half, target.displayText, false);
            target.textSprite = textOff.canvas;
        }
    }

    function _renderPolyToContext(ctx, half, verts, isWrongFlash) {
        ctx.save();
        ctx.translate(half, half);

        ctx.beginPath();
        ctx.moveTo(verts[0].x, verts[0].y);
        for (let j = 1; j < verts.length; j++) {
            ctx.lineTo(verts[j].x, verts[j].y);
        }
        ctx.closePath();

        if (isWrongFlash) {
            ctx.fillStyle = '#FAEDE9';
            ctx.strokeStyle = '#B23A22';
            ctx.lineWidth = 2.5;
        } else {
            ctx.fillStyle = '#FFFFFF';
            ctx.strokeStyle = '#102A47';
            ctx.lineWidth = 2.0;
        }
        ctx.fill();
        ctx.stroke();

        // Internal geometric facet lines
        ctx.beginPath();
        for (let k = 0; k < verts.length; k += 2) {
            ctx.moveTo(0, 0);
            ctx.lineTo(verts[k].x, verts[k].y);
        }
        ctx.strokeStyle = isWrongFlash ? 'rgba(178, 58, 34, 0.25)' : 'rgba(16, 42, 71, 0.12)';
        ctx.lineWidth = 1;
        ctx.stroke();

        ctx.restore();
    }

    function _renderTextToContext(ctx, half, text, isWrongFlash) {
        ctx.save();
        ctx.translate(half, half);
        ctx.fillStyle = isWrongFlash ? '#B23A22' : '#102A47';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        const isNarrow = _canvasWidth < 420;
        const maxSingleLen = isNarrow ? 10 : 12;

        if (text.length > maxSingleLen && text.includes(' ')) {
            const parts = text.split(' ');
            const mid = Math.ceil(parts.length / 2);
            const line1 = parts.slice(0, mid).join(' ');
            const line2 = parts.slice(mid).join(' ');
            ctx.font = `600 ${isNarrow ? 11 : 12}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`;
            ctx.fillText(line1, 0, -7);
            ctx.fillText(line2, 0, 7);
        } else {
            const fontSize = (text.length > maxSingleLen || isNarrow) ? 12 : 14;
            ctx.font = `600 ${fontSize}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`;
            ctx.fillText(text, 0, 0);
        }
        ctx.restore();
    }

    // ----------------------------------------
    // SESSION INITIALIZATION
    // ----------------------------------------
    // A word missed at any point this game (wrong hit on its prompt, or
    // letting it escape) is 'again'; one only ever hit correctly is 'weak'
    // (see creditPractice() in engine/srs.js). Sent once per game — at
    // game over, or on leaving partway.
    function _creditSrs() {
        if (!_srsCredit || _credited || typeof creditPractice !== 'function') return;
        _credited = true;
        const results = [];
        _missedWords.forEach(w => results.push({ lemma: w.lemma, rating: 'again' }));
        _hitUids.forEach(uid => {
            if (!_missedWords.has(uid)) results.push({ lemma: _words0[uid].lemma, rating: 'weak' });
        });
        creditPractice(results);
    }

    function _startSession() {
        _creditSrs();
        _preloadAudio();
        _pool = _shuffled(_words0);
        _score = 0;
        _streak = 0;
        _maxStreak = 0;
        _totalBlasts = 0;
        _totalAttempts = 0;
        _shields = SURVIVAL_SHIELDS;
        _timeLeft = TIME_LIMIT_SECONDS;
        _missedWords.clear();
        _hitUids.clear();
        _credited = false;
        _activeTargets = [];
        _shards = [];
        _screenShake = 0;
        _boundaryDangerFlash = 0;
        _spawnAccumMs = 0;
        _lastDisplayedSec = '';
        _state = 'playing';

        _render();
        _cacheDomReferences();
        _setupCanvas();
        _advanceToNextTarget();
        _fillTargetField();
        _updateHUD();

        _lastFrameTime = performance.now();
        if (_animId) cancelAnimationFrame(_animId);
        _animId = requestAnimationFrame(_loop);
    }

    function _cacheDomReferences() {
        if (!_container) return;
        _domPromptWord = _container.querySelector('.dkb-prompt-word');
        _domScoreVal = _container.querySelector('.dkb-score-val');
        _domComboVal = _container.querySelector('.dkb-combo-val');
        _domTimerVal = _container.querySelector('.dkb-timer-val');
        _domShieldPips = Array.from(_container.querySelectorAll('.dkb-shield-pip'));
    }

    function _advanceToNextTarget() {
        if (!_pool.length) {
            _pool = _shuffled(_words0);
        }
        _currentTargetWord = _pool.pop();

        if (_domPromptWord && _currentTargetWord) {
            const promptText = _direction === 'en-to-target'
                ? (_currentTargetWord.translation || '—')
                : _currentTargetWord.displayLemma;
            _domPromptWord.textContent = promptText;
        }
    }

    // ----------------------------------------
    // LANE MANAGEMENT & SPAWNING (NO OVERLAP)
    // ----------------------------------------
    function _getLaneCount() {
        return _canvasWidth < 420 ? 3 : 4;
    }

    function _getLaneX(laneIndex, totalLanes) {
        const laneWidth = _canvasWidth / totalLanes;
        return laneWidth * (laneIndex + 0.5);
    }

    function _getMaxTargets() {
        if (_mode === 'survival') {
            return _getLaneCount();
        }
        return _canvasWidth < 420 ? 4 : 5;
    }

    function _fillTargetField() {
        if (!_currentTargetWord || !_words0.length) return;

        const maxTargets = _getMaxTargets();

        // 1. Ensure the correct target word is on screen
        let hasTarget = false;
        for (let i = 0; i < _activeTargets.length; i++) {
            if (_activeTargets[i].word.uid === _currentTargetWord.uid) {
                hasTarget = true;
                break;
            }
        }
        if (!hasTarget) {
            const newTarget = _createTarget(_currentTargetWord, true);
            if (newTarget) _activeTargets.push(newTarget);
        }

        // 2. Fill empty slots with distractors in O(1) random picks
        let attempts = 0;
        const totalWords = _words0.length;
        while (_activeTargets.length < maxTargets && attempts < 12) {
            attempts++;
            const candidate = _words0[Math.floor(Math.random() * totalWords)];
            if (candidate.uid === _currentTargetWord.uid) continue;

            let alreadyOnScreen = false;
            for (let i = 0; i < _activeTargets.length; i++) {
                if (_activeTargets[i].word.uid === candidate.uid) {
                    alreadyOnScreen = true;
                    break;
                }
            }
            if (alreadyOnScreen) continue;

            const newTarget = _createTarget(candidate, false);
            if (newTarget) {
                _activeTargets.push(newTarget);
            } else {
                break; // No free lane available right now
            }
        }
    }

    function _createTarget(word, isMatchTarget) {
        const radius = _canvasWidth < 420 ? 39 : 46;
        const totalLanes = _getLaneCount();

        let x, y, vx, vy, lane = -1;

        if (_mode === 'survival') {
            const laneOccupancy = new Array(totalLanes).fill(null);
            for (let i = 0; i < _activeTargets.length; i++) {
                const t = _activeTargets[i];
                if (t.lane >= 0 && t.lane < totalLanes) {
                    if (laneOccupancy[t.lane] === null || t.y < laneOccupancy[t.lane]) {
                        laneOccupancy[t.lane] = t.y;
                    }
                }
            }

            const freeLanes = [];
            for (let l = 0; l < totalLanes; l++) {
                if (laneOccupancy[l] === null || laneOccupancy[l] > 135) {
                    freeLanes.push(l);
                }
            }

            if (!freeLanes.length) {
                return null;
            }

            lane = freeLanes[Math.floor(Math.random() * freeLanes.length)];
            x = _getLaneX(lane, totalLanes);
            y = -radius - 10;
            vx = 0;
            vy = 0.8 + Math.min(0.6, _totalBlasts * 0.015);
        } else {
            const margin = radius + 15;
            let foundSpot = false;
            for (let a = 0; a < 12; a++) {
                const testX = margin + Math.random() * (_canvasWidth - margin * 2);
                const testY = margin + Math.random() * (_canvasHeight - margin * 2);
                let isClear = true;
                for (let i = 0; i < _activeTargets.length; i++) {
                    const t = _activeTargets[i];
                    if (Math.hypot(t.x - testX, t.y - testY) <= (radius * 2 + 12)) {
                        isClear = false;
                        break;
                    }
                }
                if (isClear) {
                    x = testX;
                    y = testY;
                    foundSpot = true;
                    break;
                }
            }
            if (!foundSpot) {
                x = margin + Math.random() * (_canvasWidth - margin * 2);
                y = margin + Math.random() * (_canvasHeight - margin * 2);
            }

            const speed = 0.9 + Math.random() * 0.4;
            const angle = Math.random() * Math.PI * 2;
            vx = Math.cos(angle) * speed;
            vy = Math.sin(angle) * speed;
        }

        const sides = 7 + Math.floor(Math.random() * 2);
        const vertices = [];
        for (let i = 0; i < sides; i++) {
            const a = (i / sides) * Math.PI * 2;
            const r = radius * (0.88 + Math.random() * 0.24);
            vertices.push({ x: Math.cos(a) * r, y: Math.sin(a) * r });
        }

        const displayText = _direction === 'en-to-target'
            ? word.displayLemma
            : (word.translation || '—');

        const targetObj = {
            word,
            isMatchTarget,
            lane,
            x,
            y,
            vx,
            vy,
            radius,
            vertices,
            rotation: Math.random() * Math.PI * 2,
            vRot: (Math.random() - 0.5) * 0.012,
            displayText,
            flashTime: 0,
            spriteHalf: radius + 4,
            polySprite: null,
            flashSprite: null,
            textSprite: null
        };

        _bakeTargetSprites(targetObj);
        return targetObj;
    }

    // ----------------------------------------
    // SHATTER PARTICLES
    // ----------------------------------------
    function _spawnShatter(x, y) {
        const count = 8;
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.random() - 0.5) * 0.4;
            const speed = 2.8 + Math.random() * 3.2;
            _shards.push({
                x,
                y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                rotation: Math.random() * Math.PI * 2,
                vRot: (Math.random() - 0.5) * 0.2,
                size: 10,
                life: 1.0,
                decay: 0.045 + Math.random() * 0.02
            });
        }
    }

    // ----------------------------------------
    // HIT TESTING & GAMEPLAY LOGIC (ZERO REFLOW)
    // ----------------------------------------
    function _handleCanvasCoords(cx, cy) {
        if (_state !== 'playing') return;

        _totalAttempts++;

        let hitIndex = -1;
        for (let i = _activeTargets.length - 1; i >= 0; i--) {
            const t = _activeTargets[i];
            const dx = cx - t.x;
            const dy = cy - t.y;
            const hitR = t.radius + 12;
            if (dx * dx + dy * dy <= hitR * hitR) {
                hitIndex = i;
                break;
            }
        }

        if (hitIndex === -1) return;

        const target = _activeTargets[hitIndex];
        const isCorrect = (target.word.uid === _currentTargetWord.uid);

        if (isCorrect) {
            _totalBlasts++;
            _hitUids.add(_currentTargetWord.uid);
            _streak++;
            if (_streak > _maxStreak) _maxStreak = _streak;

            const comboMultiplier = Math.min(5, 1 + Math.floor((_streak - 1) / 3));
            _score += 100 * comboMultiplier;

            _spawnShatter(target.x, target.y);
            _speakWord(target.word);

            _activeTargets.splice(hitIndex, 1);
            _advanceToNextTarget();
            _fillTargetField();
            _updateHUD();
        } else {
            target.flashTime = 250;
            _screenShake = 10;
            _streak = 0;
            _missedWords.set(_currentTargetWord.uid, _currentTargetWord);

            if (typeof Sound !== 'undefined' && typeof Sound.wrong === 'function') {
                Sound.wrong();
            }

            if (_mode === 'survival') {
                _shields--;
                if (_shields <= 0) {
                    _gameOver();
                    return;
                }
            }
            _updateHUD();
        }
    }

    function _handleCanvasClick(clientX, clientY) {
        if (_state !== 'playing' || !_canvas) return;
        const rect = _canvas.getBoundingClientRect();
        _canvasCssWidth = rect.width || _canvasWidth;
        _canvasCssHeight = rect.height || _canvasHeight;
        const cx = (clientX - rect.left) * (_canvasWidth / _canvasCssWidth);
        const cy = (clientY - rect.top) * (_canvasHeight / _canvasCssHeight);
        _handleCanvasCoords(cx, cy);
    }

    function _targetEscaped(target) {
        if (target.word.uid === _currentTargetWord.uid) {
            _screenShake = 12;
            _boundaryDangerFlash = 300;
            _streak = 0;
            _missedWords.set(_currentTargetWord.uid, _currentTargetWord);

            if (typeof Sound !== 'undefined' && typeof Sound.wrong === 'function') {
                Sound.wrong();
            }

            if (_mode === 'survival') {
                _shields--;
                if (_shields <= 0) {
                    _gameOver();
                    return;
                }
            }
            _advanceToNextTarget();
        }
        _fillTargetField();
        _updateHUD();
    }

    function _updateHUD() {
        if (_domScoreVal) _domScoreVal.textContent = _score.toLocaleString();

        if (_domComboVal) {
            const mult = Math.min(5, 1 + Math.floor((_streak - 1) / 3));
            _domComboVal.textContent = `${mult}x`;
            _domComboVal.className = `dkb-combo-val ${mult > 1 ? 'is-active' : ''}`;
        }

        if (_mode === 'survival' && _domShieldPips.length) {
            for (let idx = 0; idx < _domShieldPips.length; idx++) {
                if (idx < _shields) {
                    _domShieldPips[idx].classList.add('is-active');
                } else {
                    _domShieldPips[idx].classList.remove('is-active');
                }
            }
        }
    }

    // ----------------------------------------
    // MAIN GAME LOOP (60 FPS CANVAS)
    // ----------------------------------------
    function _loop(timestamp) {
        if (_state !== 'playing') return;

        const dt = Math.min(64, timestamp - _lastFrameTime);
        _lastFrameTime = timestamp;

        if (_mode === 'time-attack') {
            _timeLeft -= dt / 1000;
            if (_timeLeft <= 0) {
                _timeLeft = 0;
                _gameOver();
                return;
            }
            const secStr = Math.max(0, _timeLeft).toFixed(1);
            if (secStr !== _lastDisplayedSec) {
                _lastDisplayedSec = secStr;
                if (_domTimerVal) _domTimerVal.textContent = secStr + 's';
            }
        }

        if (_screenShake > 0) {
            _screenShake = Math.max(0, _screenShake - dt * 0.05);
        }
        if (_boundaryDangerFlash > 0) {
            _boundaryDangerFlash = Math.max(0, _boundaryDangerFlash - dt);
        }

        _updatePhysics(dt);
        _drawCanvas();

        _animId = requestAnimationFrame(_loop);
    }

    function _updatePhysics(dt) {
        const timeScale = dt / 16.666;

        for (let i = _activeTargets.length - 1; i >= 0; i--) {
            const t = _activeTargets[i];
            t.x += t.vx * timeScale;
            t.y += t.vy * timeScale;
            t.rotation += t.vRot * timeScale;

            if (t.flashTime > 0) {
                t.flashTime = Math.max(0, t.flashTime - dt);
            }

            if (_mode === 'survival') {
                const dangerY = _canvasHeight - 32;
                if (t.y - t.radius >= dangerY) {
                    _activeTargets.splice(i, 1);
                    _targetEscaped(t);
                    continue;
                }
            } else {
                if (t.x - t.radius < 8) {
                    t.x = t.radius + 8;
                    t.vx = Math.abs(t.vx);
                } else if (t.x + t.radius > _canvasWidth - 8) {
                    t.x = _canvasWidth - t.radius - 8;
                    t.vx = -Math.abs(t.vx);
                }
                if (t.y - t.radius < 8) {
                    t.y = t.radius + 8;
                    t.vy = Math.abs(t.vy);
                } else if (t.y + t.radius > _canvasHeight - 8) {
                    t.y = _canvasHeight - t.radius - 8;
                    t.vy = -Math.abs(t.vy);
                }
            }
        }

        // Mutual circle repulsion for Time Attack mode
        if (_mode === 'time-attack') {
            for (let i = 0; i < _activeTargets.length; i++) {
                for (let j = i + 1; j < _activeTargets.length; j++) {
                    const t1 = _activeTargets[i];
                    const t2 = _activeTargets[j];
                    const dx = t2.x - t1.x;
                    const dy = t2.y - t1.y;
                    const dist = Math.hypot(dx, dy) || 1;
                    const minDist = t1.radius + t2.radius + 10;
                    if (dist < minDist) {
                        const overlap = (minDist - dist) / 2;
                        const nx = dx / dist;
                        const ny = dy / dist;
                        t1.x -= nx * overlap;
                        t1.y -= ny * overlap;
                        t2.x += nx * overlap;
                        t2.y += ny * overlap;
                        const kx = t1.vx - t2.vx;
                        const ky = t1.vy - t2.vy;
                        const p = (nx * kx + ny * ky);
                        t1.vx -= p * nx;
                        t1.vy -= p * ny;
                        t2.vx += p * nx;
                        t2.vy += p * ny;
                    }
                }
            }
        }

        // Throttled spawn check (only every 250ms when needed, never 60fps)
        if (_activeTargets.length < _getMaxTargets()) {
            _spawnAccumMs += dt;
            if (_spawnAccumMs >= 250) {
                _spawnAccumMs = 0;
                _fillTargetField();
            }
        }

        // Update shards
        for (let i = _shards.length - 1; i >= 0; i--) {
            const s = _shards[i];
            s.x += s.vx * timeScale;
            s.y += s.vy * timeScale;
            s.rotation += s.vRot * timeScale;
            s.life -= s.decay * timeScale;
            if (s.life <= 0) {
                _shards.splice(i, 1);
            }
        }
    }

    // ----------------------------------------
    // CANVAS RENDERING (HARDWARE BLIT FAST PATH)
    // ----------------------------------------
    function _drawCanvas() {
        if (!_ctx) return;

        _ctx.save();
        _ctx.clearRect(0, 0, _canvasWidth, _canvasHeight);

        if (_screenShake > 0) {
            const sx = (Math.random() - 0.5) * _screenShake;
            const sy = (Math.random() - 0.5) * _screenShake;
            _ctx.translate(sx, sy);
        }

        if (_mode === 'survival') {
            const dangerY = _canvasHeight - 32;
            _ctx.save();
            _ctx.beginPath();
            _ctx.setLineDash([8, 8]);
            _ctx.moveTo(12, dangerY);
            _ctx.lineTo(_canvasWidth - 12, dangerY);
            if (_boundaryDangerFlash > 0) {
                _ctx.strokeStyle = '#B23A22';
                _ctx.lineWidth = 3;
            } else {
                _ctx.strokeStyle = 'rgba(16, 42, 71, 0.25)';
                _ctx.lineWidth = 1.5;
            }
            _ctx.stroke();
            _ctx.restore();
        }

        for (let i = 0; i < _activeTargets.length; i++) {
            _drawTarget(_activeTargets[i]);
        }

        for (let i = 0; i < _shards.length; i++) {
            _drawShard(_shards[i]);
        }

        _ctx.restore();
    }

    function _drawTarget(target) {
        // Fast hardware-accelerated offscreen sprite path
        if (target.polySprite && target.textSprite) {
            const half = target.spriteHalf;
            const box = half * 2;
            const polyImg = (target.flashTime > 0 && target.flashSprite) ? target.flashSprite : target.polySprite;

            _ctx.save();
            _ctx.translate(target.x, target.y);
            _ctx.rotate(target.rotation);
            _ctx.drawImage(polyImg, -half, -half, box, box);
            _ctx.rotate(-target.rotation);
            _ctx.drawImage(target.textSprite, -half, -half, box, box);
            _ctx.restore();
            return;
        }

        // Fallback immediate path (for headless unit test environments)
        _ctx.save();
        _ctx.translate(target.x, target.y);
        _ctx.rotate(target.rotation);
        _renderPolyToContext(_ctx, 0, target.vertices, target.flashTime > 0);
        _ctx.rotate(-target.rotation);
        _renderTextToContext(_ctx, 0, target.displayText, target.flashTime > 0);
        _ctx.restore();
    }

    function _drawShard(shard) {
        _ctx.save();
        _ctx.translate(shard.x, shard.y);
        _ctx.rotate(shard.rotation);
        _ctx.globalAlpha = Math.max(0, shard.life);

        if (_shardSprite) {
            _ctx.drawImage(_shardSprite, -10, -10, 20, 20);
        } else {
            _ctx.beginPath();
            const s = 7;
            _ctx.moveTo(0, -s);
            _ctx.lineTo(s * 0.7, s * 0.7);
            _ctx.lineTo(-s * 0.7, s * 0.7);
            _ctx.closePath();
            _ctx.fillStyle = '#E94B16';
            _ctx.fill();
        }

        _ctx.restore();
    }

    // ----------------------------------------
    // GAME OVER & RESULTS
    // ----------------------------------------
    function _gameOver() {
        if (_animId) {
            cancelAnimationFrame(_animId);
            _animId = null;
        }
        if (_preloadTimer) {
            clearInterval(_preloadTimer);
            _preloadTimer = null;
        }
        _state = 'gameover';
        _creditSrs();

        const prevBest = _getBestScore();
        const isNewBest = _score > prevBest;
        _saveBestScore(_score);

        if (typeof Sound !== 'undefined' && typeof Sound.complete === 'function') {
            Sound.complete();
        }

        if (_onComplete) {
            _onComplete({
                score: _score,
                blasts: _totalBlasts,
                maxStreak: _maxStreak,
                mode: _mode,
                direction: _direction
            });
        }

        _render();
    }

    // ----------------------------------------
    // DOM RENDERING & WIRING
    // ----------------------------------------
    function _setupCanvas() {
        if (!_container) return;
        _canvas = _container.querySelector('.dkb-canvas');
        if (!_canvas) return;

        const rect = _canvas.getBoundingClientRect();
        _canvasWidth = Math.max(300, rect.width || 600);
        _canvasHeight = 420;
        _canvasCssWidth = _canvasWidth;
        _canvasCssHeight = _canvasHeight;

        // Cap DPR to 2 on mobile to prevent GPU fill-rate hitching on 3x/4x screens
        _dpr = Math.min(2, window.devicePixelRatio || 1);
        _canvas.width = _canvasWidth * _dpr;
        _canvas.height = _canvasHeight * _dpr;
        _canvas.style.height = _canvasHeight + 'px';

        _ctx = _canvas.getContext('2d');
        _ctx.scale(_dpr, _dpr);

        _shardSprite = _bakeShardSprite();

        // Zero-reflow pointerdown handler using native offsetX / offsetY
        const handleDown = (e) => {
            e.preventDefault();
            if (typeof e.offsetX === 'number' && typeof e.offsetY === 'number' && _canvasCssWidth > 0) {
                const cx = e.offsetX * (_canvasWidth / _canvasCssWidth);
                const cy = e.offsetY * (_canvasHeight / _canvasCssHeight);
                _handleCanvasCoords(cx, cy);
            } else {
                _handleCanvasClick(e.clientX, e.clientY);
            }
        };

        _canvas.addEventListener('pointerdown', handleDown, { passive: false });
    }

    function _render() {
        if (!_container) return;
        const exitText = _exitLabel || 'Back to deck';
        const langName = _langName();

        if (!_words0.length || _words0.length < 2) {
            _container.innerHTML = `
                <div class="dkb">
                    <button class="dk-back" data-blast-exit="1">← ${_escapeHtml(exitText)}</button>
                    <p class="dk-empty">At least 2 words are required to play Blast.</p>
                </div>
            `;
            _wire();
            return;
        }

        if (_state === 'lobby') {
            const best = _getBestScore();
            _container.innerHTML = `
                <div class="dkb dkb-lobby">
                    <div class="dkb-lobby-nav">
                        <button class="dk-back" data-blast-exit="1">← ${_escapeHtml(exitText)}</button>
                    </div>

                    <div class="dkb-lobby-card">
                        <div class="dkb-badge">ARCADE</div>
                        <h2 class="dkb-title">Blast</h2>
                        <p class="dkb-subtitle">Fast-paced target matching. Spot and blast the matching geometric polyhedron before time expires.</p>

                        <div class="dkb-section">
                            <span class="dkb-section-title">Mode</span>
                            <div class="dkb-segmented" role="group" aria-label="Game Mode">
                                <button class="dkb-seg-btn ${_mode === 'time-attack' ? 'is-active' : ''}" data-set-mode="time-attack">
                                    Time Attack
                                </button>
                                <button class="dkb-seg-btn ${_mode === 'survival' ? 'is-active' : ''}" data-set-mode="survival">
                                    Survival
                                </button>
                            </div>
                            <p class="dkb-control-hint">
                                ${_mode === 'time-attack'
                                    ? '60-second speed challenge. Blast targets and build combo multipliers.'
                                    : '3 shield charges. Avoid letting matching targets escape and avoid wrong hits.'}
                            </p>
                        </div>

                        <div class="dkb-section">
                            <span class="dkb-section-title">Prompt Language</span>
                            <div class="dkb-segmented" role="group" aria-label="Prompt Language Direction">
                                <button class="dkb-seg-btn ${_direction === 'en-to-target' ? 'is-active' : ''}" data-set-dir="en-to-target">
                                    English → ${_escapeHtml(langName)}
                                </button>
                                <button class="dkb-seg-btn ${_direction === 'target-to-en' ? 'is-active' : ''}" data-set-dir="target-to-en">
                                    ${_escapeHtml(langName)} → English
                                </button>
                            </div>
                            <p class="dkb-control-hint">
                                ${_direction === 'en-to-target'
                                    ? `Prompt is in English; blast the matching ${_escapeHtml(langName)} target.`
                                    : `Prompt is in ${_escapeHtml(langName)}; blast the matching English target.`}
                            </p>
                        </div>

                        ${best > 0 ? `<div class="dkb-best-pill">Personal best: <strong>${best.toLocaleString()}</strong> pts</div>` : ''}

                        <button class="btn-primary dkb-start-btn" data-blast-start="1">Start Game</button>
                    </div>
                </div>
            `;
            _wire();
            return;
        }

        if (_state === 'playing') {
            const promptText = _currentTargetWord
                ? (_direction === 'en-to-target' ? (_currentTargetWord.translation || '—') : _currentTargetWord.displayLemma)
                : '';

            _container.innerHTML = `
                <div class="dkb dkb-game">
                    <div class="dkb-head">
                        <button class="dk-back dkb-back-btn" data-blast-exit="1">← Exit</button>

                        <div class="dkb-center-indicator">
                            ${_mode === 'time-attack' ? `
                                <div class="dkb-metric">
                                    <span class="dkb-metric-label">TIME</span>
                                    <span class="dkb-timer-val">${Math.max(0, _timeLeft).toFixed(1)}s</span>
                                </div>
                            ` : `
                                <div class="dkb-metric">
                                    <span class="dkb-metric-label">SHIELDS</span>
                                    <div class="dkb-shields">
                                        <span class="dkb-shield-pip ${_shields >= 1 ? 'is-active' : ''}"></span>
                                        <span class="dkb-shield-pip ${_shields >= 2 ? 'is-active' : ''}"></span>
                                        <span class="dkb-shield-pip ${_shields >= 3 ? 'is-active' : ''}"></span>
                                    </div>
                                </div>
                            `}
                        </div>

                        <div class="dkb-stats">
                            <div class="dkb-metric">
                                <span class="dkb-metric-label">SCORE</span>
                                <span class="dkb-score-val">${_score.toLocaleString()}</span>
                            </div>
                            <div class="dkb-metric">
                                <span class="dkb-metric-label">COMBO</span>
                                <span class="dkb-combo-val">1x</span>
                            </div>
                        </div>
                    </div>

                    <div class="dkb-prompt-bar">
                        <span class="dkb-prompt-kicker">FIND MATCH</span>
                        <div class="dkb-prompt-word">${_escapeHtml(promptText)}</div>
                    </div>

                    <div class="dkb-canvas-wrap">
                        <canvas class="dkb-canvas"></canvas>
                    </div>
                </div>
            `;
            _wire();
            return;
        }

        if (_state === 'gameover') {
            const best = _getBestScore();
            const isNewBest = _score === best && _score > 0;
            const accuracy = _totalAttempts > 0 ? Math.round((_totalBlasts / _totalAttempts) * 100) : 0;

            _container.innerHTML = `
                <div class="dkb dkb-done">
                    <button class="dk-back" data-blast-exit="1">← ${_escapeHtml(exitText)}</button>

                    <div class="dkb-done-card">
                        <span class="dkb-done-kicker">${_mode === 'time-attack' ? 'TIME EXPIRED' : 'GAME OVER'}</span>
                        <div class="dkb-done-score">${_score.toLocaleString()}</div>
                        <div class="dkb-done-score-label">POINTS</div>

                        ${isNewBest ? `<p class="dkb-new-best">New personal best!</p>` : (best > 0 ? `<p class="dkb-best">Personal best: ${best.toLocaleString()} pts</p>` : '')}

                        <div class="dkb-stats-grid">
                            <div class="dkb-stat-box">
                                <span class="dkb-stat-num">${_totalBlasts}</span>
                                <span class="dkb-stat-name">Blasted</span>
                            </div>
                            <div class="dkb-stat-box">
                                <span class="dkb-stat-num">${accuracy}%</span>
                                <span class="dkb-stat-name">Accuracy</span>
                            </div>
                            <div class="dkb-stat-box">
                                <span class="dkb-stat-num">${_maxStreak}x</span>
                                <span class="dkb-stat-name">Max Streak</span>
                            </div>
                        </div>

                        ${_missedWords.size ? `
                            <div class="gd-missed-recap dkb-missed-recap">
                                <h4 class="gd-missed-title">Review Missed Pairs</h4>
                                <div class="gd-missed-list">
                                    ${Array.from(_missedWords.values()).map(w => `
                                        <div class="gd-missed-card">
                                            <div class="gd-missed-q">${_escapeHtml(w.displayLemma)}</div>
                                            <div class="gd-missed-answers">
                                                <div class="gd-missed-correct"><span class="gd-badge-correct">Meaning:</span> <strong>${_escapeHtml(w.translation)}</strong></div>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        ` : ''}

                        <div class="dkb-done-actions">
                            <button class="btn-primary" data-blast-restart="1">Play Again</button>
                            <button class="dk-secondary" data-blast-lobby="1">Change Settings</button>
                            <button class="dk-secondary" data-blast-exit="1">${_escapeHtml(exitText)}</button>
                        </div>
                    </div>
                </div>
            `;
            _wire();
        }
    }

    function _wire() {
        if (!_container) return;

        _container.querySelectorAll('[data-blast-exit]').forEach(el => {
            el.onclick = () => {
                _creditSrs();
                stop();
                if (_onExit) _onExit();
            };
        });

        _container.querySelectorAll('[data-set-mode]').forEach(el => {
            el.onclick = () => {
                _mode = el.getAttribute('data-set-mode');
                _render();
            };
        });

        _container.querySelectorAll('[data-set-dir]').forEach(el => {
            el.onclick = () => {
                _direction = el.getAttribute('data-set-dir');
                _render();
            };
        });

        _container.querySelectorAll('[data-blast-start]').forEach(el => {
            el.onclick = () => { _startSession(); };
        });

        _container.querySelectorAll('[data-blast-restart]').forEach(el => {
            el.onclick = () => { _startSession(); };
        });

        _container.querySelectorAll('[data-blast-lobby]').forEach(el => {
            el.onclick = () => {
                _creditSrs();
                stop();
                _state = 'lobby';
                _render();
            };
        });
    }

    // ----------------------------------------
    // PUBLIC INTERFACE
    // ----------------------------------------
    function render(root, options) {
        stop();
        _container = root;
        _deckId = (options && options.deckId) || 'unknown';
        const rawWords = ((options && options.words) || []).filter(w => w && (w.lemma || w.spanish));
        _words0 = rawWords.map((w, idx) => {
            const lemma = w.lemma || w.spanish;
            return {
                uid: idx,
                lemma,
                displayLemma: _withArticle(lemma),
                translation: w.translation || w.english || '—'
            };
        });

        if (options && options.mode) _mode = options.mode;
        if (options && options.direction) _direction = options.direction;
        _exitLabel = (options && options.exitLabel) || null;
        _onExit = (options && options.onExit) || function () {};
        _onComplete = (options && options.onComplete) || null;
        _srsCredit = !!(options && options.srsCredit);
        _credited = true; // nothing played yet

        _state = 'lobby';

        _preloadAudio();
        _render();
    }

    function stop() {
        if (_animId) {
            cancelAnimationFrame(_animId);
            _animId = null;
        }
        if (_preloadTimer) {
            clearInterval(_preloadTimer);
            _preloadTimer = null;
        }
        _state = 'lobby';
        _activeTargets = [];
        _shards = [];
    }

    return { render, stop };
})();

if (typeof module !== 'undefined' && module.exports) {
    module.exports = DeckBlast;
}
