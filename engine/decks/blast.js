// ============================================
// DECK BLAST GAME
// ============================================
// Fast-paced arcade vocabulary matching game inspired by Quizlet Blast,
// reimagined with Parlour's strict constructivist geometric aesthetic
// (faceted polyhedra targets, clean typography, zero emojis).
//
// Key Features:
// 1. Proactive Audio Preloading: Vocabulary words are preloaded in memory
//    and IndexedDB via ParlourTTS.preload() with smooth staggered batching,
//    guaranteeing 0ms playback latency upon blasting a target without choking
//    mobile networks.
// 2. Anti-Overlap & Lane Physics:
//    - Survival Mode: Organised into dedicated vertical lanes (3 on mobile,
//      4 on desktop) with uniform velocities, mathematically preventing targets
//      from ever covering or overlapping each other.
//    - Time Attack Mode: 2D kinetic drift with mutual circle-circle repulsion
//      so targets bounce cleanly off each other rather than passing through.
// 3. Mobile Performance Optimization:
//    - Capped devicePixelRatio (max 2) prevents multi-megapixel buffer lag.
//    - Cached DOM references eliminate layout thrashing in the 60fps loop.
//    - Decoupled audio calls prevent mobile media hardware pipeline freezes.
// 4. Dual Modes:
//    - Time Attack: 60-second speed-run with combo multipliers (up to 5x).
//    - Survival: 3 shield charges; targets drift toward a danger threshold.
// 5. Language Direction Toggle:
//    - English prompt -> Match Target Language asteroid.
//    - Target Language prompt -> Match English asteroid.

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
    let _currentTargetWord = null;
    let _activeTargets = [];
    let _shards = [];

    // Animation & timing
    let _animId = null;
    let _preloadTimer = null;
    let _lastFrameTime = 0;
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
    let _dpr = 1;

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

        // 1. Immediately preload the first 5 words
        const immediate = _words0.slice(0, 5);
        immediate.forEach(w => {
            if (w && w.lemma) {
                ParlourTTS.preload({ text: w.lemma, language: lang, type: 'vocabulary' });
            }
        });

        // 2. Stagger the rest in small intervals so mobile CPU/network isn't choked
        if (_preloadTimer) clearInterval(_preloadTimer);
        const remaining = _words0.slice(5);
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
            // Asynchronous dispatch prevents blocking the touch gesture or RAF animation
            setTimeout(() => {
                ParlourTTS.speak({ text: word.lemma, language: _langCode(), type: 'vocabulary' });
            }, 10);
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
    // SESSION INITIALIZATION
    // ----------------------------------------
    function _startSession() {
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
        _activeTargets = [];
        _shards = [];
        _screenShake = 0;
        _boundaryDangerFlash = 0;
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
                : _withArticle(_currentTargetWord.lemma);
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
        if (!_currentTargetWord) return;

        const maxTargets = _getMaxTargets();
        const totalLanes = _getLaneCount();

        // 1. Ensure the correct target word is on screen
        const hasTarget = _activeTargets.some(t => t.word.uid === _currentTargetWord.uid);
        if (!hasTarget) {
            const newTarget = _createTarget(_currentTargetWord, true);
            if (newTarget) _activeTargets.push(newTarget);
        }

        // 2. Fill empty slots with distractors
        let attempts = 0;
        while (_activeTargets.length < maxTargets && attempts < 10) {
            attempts++;
            const available = _words0.filter(w =>
                w.uid !== _currentTargetWord.uid &&
                !_activeTargets.some(t => t.word.uid === w.uid)
            );
            if (!available.length) break;

            const distractor = available[Math.floor(Math.random() * available.length)];
            const newTarget = _createTarget(distractor, false);
            if (newTarget) {
                _activeTargets.push(newTarget);
            } else {
                break; // No free lane available right now
            }
        }
    }

    function _createTarget(word, isMatchTarget) {
        // Responsive target radius: smaller on phone screens to prevent crowding
        const radius = _canvasWidth < 420 ? 39 : 46;
        const totalLanes = _getLaneCount();

        let x, y, vx, vy, lane = -1;

        if (_mode === 'survival') {
            // Find lanes with no target, or whose highest target is already well down the screen
            const laneOccupancy = new Array(totalLanes).fill(null);
            _activeTargets.forEach(t => {
                if (t.lane >= 0 && t.lane < totalLanes) {
                    if (laneOccupancy[t.lane] === null || t.y < laneOccupancy[t.lane]) {
                        laneOccupancy[t.lane] = t.y;
                    }
                }
            });

            // Candidates: lanes that are either empty or whose top asteroid is below y = 140
            const freeLanes = [];
            for (let l = 0; l < totalLanes; l++) {
                if (laneOccupancy[l] === null || laneOccupancy[l] > 140) {
                    freeLanes.push(l);
                }
            }

            if (!freeLanes.length) {
                return null; // All lanes occupied near the top; wait before spawning
            }

            lane = freeLanes[Math.floor(Math.random() * freeLanes.length)];
            x = _getLaneX(lane, totalLanes);
            y = -radius - 10;
            vx = 0; // Pure vertical drift in assigned lane eliminates horizontal collisions
            vy = 0.8 + Math.min(0.6, _totalBlasts * 0.015); // Uniform velocity prevents overtaking
        } else {
            // Time attack: spawn anywhere on canvas with clearance from existing targets
            const margin = radius + 15;
            let foundSpot = false;
            for (let a = 0; a < 15; a++) {
                const testX = margin + Math.random() * (_canvasWidth - margin * 2);
                const testY = margin + Math.random() * (_canvasHeight - margin * 2);
                const isClear = _activeTargets.every(t => Math.hypot(t.x - testX, t.y - testY) > (radius * 2 + 15));
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

        // Faceted polygon vertices (7-8 sided)
        const sides = 7 + Math.floor(Math.random() * 2);
        const vertices = [];
        for (let i = 0; i < sides; i++) {
            const a = (i / sides) * Math.PI * 2;
            const r = radius * (0.88 + Math.random() * 0.24);
            vertices.push({ x: Math.cos(a) * r, y: Math.sin(a) * r });
        }

        const displayText = _direction === 'en-to-target'
            ? _withArticle(word.lemma)
            : (word.translation || '—');

        return {
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
            flashTime: 0
        };
    }

    // ----------------------------------------
    // SHATTER PARTICLES (OPTIMIZED)
    // ----------------------------------------
    function _spawnShatter(x, y, radius) {
        const count = 8; // Optimized from 14 for smooth 60fps mobile execution
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.random() - 0.5) * 0.5;
            const speed = 2.5 + Math.random() * 3.5;
            _shards.push({
                x,
                y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                rotation: Math.random() * Math.PI * 2,
                vRot: (Math.random() - 0.5) * 0.2,
                size: 6 + Math.random() * 6,
                life: 1.0,
                decay: 0.04 + Math.random() * 0.02
            });
        }
    }

    // ----------------------------------------
    // HIT TESTING & GAMEPLAY LOGIC
    // ----------------------------------------
    function _handleCanvasClick(clientX, clientY) {
        if (_state !== 'playing' || !_canvas) return;

        const rect = _canvas.getBoundingClientRect();
        const scaleX = _canvasWidth / rect.width;
        const scaleY = _canvasHeight / rect.height;
        const cx = (clientX - rect.left) * scaleX;
        const cy = (clientY - rect.top) * scaleY;

        _totalAttempts++;

        let hitIndex = -1;
        for (let i = _activeTargets.length - 1; i >= 0; i--) {
            const t = _activeTargets[i];
            const dx = cx - t.x;
            const dy = cy - t.y;
            // Generous hit box for mobile fingers
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
            // Blast success!
            _totalBlasts++;
            _streak++;
            if (_streak > _maxStreak) _maxStreak = _streak;

            const comboMultiplier = Math.min(5, 1 + Math.floor((_streak - 1) / 3));
            _score += 100 * comboMultiplier;

            _spawnShatter(target.x, target.y, target.radius);
            _speakWord(target.word);

            _activeTargets.splice(hitIndex, 1);
            _advanceToNextTarget();
            _fillTargetField();
            _updateHUD();
        } else {
            // Mistake
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
            _domShieldPips.forEach((pip, idx) => {
                if (idx < _shields) {
                    pip.classList.add('is-active');
                } else {
                    pip.classList.remove('is-active');
                }
            });
        }
    }

    // ----------------------------------------
    // MAIN GAME LOOP (60 FPS CANVAS)
    // ----------------------------------------
    function _loop(timestamp) {
        if (_state !== 'playing') return;

        const dt = Math.min(64, timestamp - _lastFrameTime);
        _lastFrameTime = timestamp;

        // Timer handling (only update DOM when displayed value changes)
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

        // Screen shake decay
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

        // Update active targets
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
                // Time attack: bounce gently off all 4 edges
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

        // Anti-overlap circle repulsion for Time Attack mode
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
                        // Velocity exchange
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

        // Maintain field capacity
        _fillTargetField();

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
    // CANVAS RENDERING
    // ----------------------------------------
    function _drawCanvas() {
        if (!_ctx) return;

        _ctx.save();
        _ctx.clearRect(0, 0, _canvasWidth, _canvasHeight);

        // Screen shake
        if (_screenShake > 0) {
            const sx = (Math.random() - 0.5) * _screenShake;
            const sy = (Math.random() - 0.5) * _screenShake;
            _ctx.translate(sx, sy);
        }

        // Draw danger threshold line in survival mode
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

        // Draw floating targets
        for (let i = 0; i < _activeTargets.length; i++) {
            _drawTarget(_activeTargets[i]);
        }

        // Draw particle shards
        for (let i = 0; i < _shards.length; i++) {
            _drawShard(_shards[i]);
        }

        _ctx.restore();
    }

    function _drawTarget(target) {
        _ctx.save();
        _ctx.translate(target.x, target.y);
        _ctx.rotate(target.rotation);

        const isWrongFlash = target.flashTime > 0;

        // Outer polyhedral path
        _ctx.beginPath();
        const verts = target.vertices;
        _ctx.moveTo(verts[0].x, verts[0].y);
        for (let j = 1; j < verts.length; j++) {
            _ctx.lineTo(verts[j].x, verts[j].y);
        }
        _ctx.closePath();

        if (isWrongFlash) {
            _ctx.fillStyle = '#FAEDE9';
            _ctx.strokeStyle = '#B23A22';
            _ctx.lineWidth = 2.5;
        } else {
            _ctx.fillStyle = '#FFFFFF';
            _ctx.strokeStyle = '#102A47';
            _ctx.lineWidth = 2.0;
        }
        _ctx.fill();

        // Subtle internal geometric facet lines
        _ctx.beginPath();
        for (let k = 0; k < verts.length; k += 2) {
            _ctx.moveTo(0, 0);
            _ctx.lineTo(verts[k].x, verts[k].y);
        }
        _ctx.strokeStyle = isWrongFlash ? 'rgba(178, 58, 34, 0.25)' : 'rgba(16, 42, 71, 0.12)';
        _ctx.lineWidth = 1;
        _ctx.stroke();

        _ctx.stroke();

        // Target label (counter-rotate text to stay upright)
        _ctx.rotate(-target.rotation);
        _ctx.fillStyle = isWrongFlash ? '#B23A22' : '#102A47';
        _ctx.textAlign = 'center';
        _ctx.textBaseline = 'middle';

        const text = target.displayText;
        const isNarrow = _canvasWidth < 420;
        const maxSingleLen = isNarrow ? 10 : 12;

        if (text.length > maxSingleLen && text.includes(' ')) {
            const parts = text.split(' ');
            const mid = Math.ceil(parts.length / 2);
            const line1 = parts.slice(0, mid).join(' ');
            const line2 = parts.slice(mid).join(' ');
            _ctx.font = `600 ${isNarrow ? 11 : 12}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`;
            _ctx.fillText(line1, 0, -7);
            _ctx.fillText(line2, 0, 7);
        } else {
            const fontSize = (text.length > maxSingleLen || isNarrow) ? 12 : 14;
            _ctx.font = `600 ${fontSize}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`;
            _ctx.fillText(text, 0, 0);
        }

        _ctx.restore();
    }

    function _drawShard(shard) {
        _ctx.save();
        _ctx.translate(shard.x, shard.y);
        _ctx.rotate(shard.rotation);
        _ctx.globalAlpha = Math.max(0, shard.life);

        _ctx.beginPath();
        const s = shard.size;
        _ctx.moveTo(0, -s);
        _ctx.lineTo(s * 0.7, s * 0.7);
        _ctx.lineTo(-s * 0.7, s * 0.7);
        _ctx.closePath();

        _ctx.fillStyle = '#E94B16';
        _ctx.fill();
        _ctx.strokeStyle = '#102A47';
        _ctx.lineWidth = 1;
        _ctx.stroke();

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

        // Cap DPR to 2 on mobile to prevent GPU fill-rate hitching on 3x/4x screens
        _dpr = Math.min(2, window.devicePixelRatio || 1);
        _canvas.width = _canvasWidth * _dpr;
        _canvas.height = _canvasHeight * _dpr;
        _canvas.style.height = _canvasHeight + 'px';

        _ctx = _canvas.getContext('2d');
        _ctx.scale(_dpr, _dpr);

        // Clean pointerdown listener without 300ms tap delay
        const handleDown = (e) => {
            e.preventDefault();
            const clientX = e.clientX;
            const clientY = e.clientY;
            _handleCanvasClick(clientX, clientY);
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
                ? (_direction === 'en-to-target' ? (_currentTargetWord.translation || '—') : _withArticle(_currentTargetWord.lemma))
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
                                            <div class="gd-missed-q">${_escapeHtml(_withArticle(w.lemma))}</div>
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
        _words0 = rawWords.map((w, idx) => ({
            uid: idx,
            lemma: w.lemma || w.spanish,
            translation: w.translation || w.english || '—'
        }));

        if (options && options.mode) _mode = options.mode;
        if (options && options.direction) _direction = options.direction;
        _exitLabel = (options && options.exitLabel) || null;
        _onExit = (options && options.onExit) || function () {};
        _onComplete = (options && options.onComplete) || null;

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
