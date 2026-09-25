// ============================================
// DECK BLAST GAME
// ============================================
// Fast-paced arcade vocabulary matching game inspired by Quizlet Blast,
// reimagined with Parlour's strict constructivist geometric aesthetic
// (faceted polyhedra targets, clean typography, zero emojis).
//
// Key Features:
// 1. Proactive Audio Preloading: All session vocabulary words are preloaded
//    into memory and IndexedDB via ParlourTTS.preload() the moment the lobby
//    opens, guaranteeing 0ms playback latency upon blasting a target.
// 2. Dual Modes:
//    - Time Attack: 60-second speed-run with combo multipliers (up to 5x).
//    - Survival: 3 shield charges; targets drift toward a danger threshold.
// 3. Language Direction Toggle:
//    - English prompt -> Match Target Language asteroid.
//    - Target Language prompt -> Match English asteroid.
// 4. HTML5 Canvas Physics:
//    - Smooth 60fps drifting and rotating faceted geometric polyhedra.
//    - Kinetic geometric shard particle explosions on impact.
//    - Screen shake and warning pulses on errors.
// 5. Personal Best Tracking:
//    - High scores persisted per deck, per mode, and per direction in localStorage.

const DeckBlast = (function () {
    'use strict';

    const TIME_LIMIT_SECONDS = 60;
    const SURVIVAL_SHIELDS = 3;
    const MAX_TARGETS_ON_SCREEN = 5;

    let _container = null;
    let _deckId = null;
    let _words0 = [];
    let _pool = [];
    let _exitLabel = null;
    let _onExit = null;
    let _onComplete = null;

    // Settings (persisted per session / user preference)
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
    let _lastFrameTime = 0;
    let _screenShake = 0;
    let _boundaryDangerFlash = 0;

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
    // AUDIO PRELOADING PIPELINE
    // ----------------------------------------
    function _preloadAudio() {
        if (typeof ParlourTTS === 'undefined' || typeof ParlourTTS.preload !== 'function') return;
        const lang = _langCode();
        _words0.forEach(w => {
            if (w && w.lemma) {
                ParlourTTS.preload({ text: w.lemma, language: lang, type: 'vocabulary' });
            }
        });
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
        _state = 'playing';

        _render();
        _setupCanvas();
        _advanceToNextTarget();
        _fillTargetField();

        _lastFrameTime = performance.now();
        if (_animId) cancelAnimationFrame(_animId);
        _animId = requestAnimationFrame(_loop);
    }

    function _advanceToNextTarget() {
        if (!_pool.length) {
            _pool = _shuffled(_words0);
        }
        _currentTargetWord = _pool.pop();

        // Update the prompt HUD element
        const promptWordEl = _container ? _container.querySelector('.dkb-prompt-word') : null;
        if (promptWordEl && _currentTargetWord) {
            const promptText = _direction === 'en-to-target'
                ? (_currentTargetWord.translation || '—')
                : _withArticle(_currentTargetWord.lemma);
            promptWordEl.textContent = promptText;
        }
    }

    // Ensure the current target word is among the active floating polyhedra
    function _fillTargetField() {
        if (!_currentTargetWord) return;

        const hasTarget = _activeTargets.some(t => t.word.uid === _currentTargetWord.uid);
        if (!hasTarget) {
            _activeTargets.push(_createTarget(_currentTargetWord, true));
        }

        while (_activeTargets.length < MAX_TARGETS_ON_SCREEN) {
            const available = _words0.filter(w =>
                w.uid !== _currentTargetWord.uid &&
                !_activeTargets.some(t => t.word.uid === w.uid)
            );
            if (!available.length) break;
            const distractor = available[Math.floor(Math.random() * available.length)];
            _activeTargets.push(_createTarget(distractor, false));
        }
    }

    // ----------------------------------------
    // GEOMETRIC TARGET GENERATOR
    // ----------------------------------------
    function _createTarget(word, isMatchTarget) {
        const radius = 48;
        const margin = radius + 20;

        let x, y, vx, vy;
        if (_mode === 'survival') {
            // Spawn at the top with downward velocity
            x = margin + Math.random() * (_canvasWidth - margin * 2);
            y = -radius - Math.random() * 60;
            vx = (Math.random() - 0.5) * 0.8;
            vy = 0.8 + Math.random() * 0.6; // downward drift
        } else {
            // Time attack: spawn anywhere on canvas and drift in random direction
            x = margin + Math.random() * (_canvasWidth - margin * 2);
            y = margin + Math.random() * (_canvasHeight - margin * 2);
            const speed = 1.0 + Math.random() * 0.6;
            const angle = Math.random() * Math.PI * 2;
            vx = Math.cos(angle) * speed;
            vy = Math.sin(angle) * speed;
        }

        // Generate faceted polygon geometry (7-8 sides with subtle irregularity)
        const sides = 7 + Math.floor(Math.random() * 2);
        const vertices = [];
        for (let i = 0; i < sides; i++) {
            const a = (i / sides) * Math.PI * 2;
            const r = radius * (0.85 + Math.random() * 0.3);
            vertices.push({ x: Math.cos(a) * r, y: Math.sin(a) * r });
        }

        const displayText = _direction === 'en-to-target'
            ? _withArticle(word.lemma)
            : (word.translation || '—');

        return {
            word,
            isMatchTarget,
            x,
            y,
            vx,
            vy,
            radius,
            vertices,
            rotation: Math.random() * Math.PI * 2,
            vRot: (Math.random() - 0.5) * 0.015,
            displayText,
            flashTime: 0,
            opacity: 1
        };
    }

    // ----------------------------------------
    // PARTICLES / SHATTER PHYSICS
    // ----------------------------------------
    function _spawnShatter(x, y, radius) {
        const count = 14;
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.random() - 0.5) * 0.5;
            const speed = 2.5 + Math.random() * 4.5;
            _shards.push({
                x,
                y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                rotation: Math.random() * Math.PI * 2,
                vRot: (Math.random() - 0.5) * 0.2,
                size: 7 + Math.random() * 9,
                life: 1.0,
                decay: 0.03 + Math.random() * 0.02
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
            if (dx * dx + dy * dy <= t.radius * t.radius * 1.1) {
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
            if (typeof Sound !== 'undefined' && typeof Sound.correct === 'function') {
                Sound.correct();
            }

            _activeTargets.splice(hitIndex, 1);
            _advanceToNextTarget();
            _fillTargetField();
            _updateHUD();
        } else {
            // Mistake
            target.flashTime = 250; // flash red/danger
            _screenShake = 12;
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
            // Matching target escaped across boundary
            _screenShake = 14;
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
        if (!_container) return;
        const scoreEl = _container.querySelector('.dkb-score-val');
        if (scoreEl) scoreEl.textContent = _score.toLocaleString();

        const comboEl = _container.querySelector('.dkb-combo-val');
        if (comboEl) {
            const mult = Math.min(5, 1 + Math.floor((_streak - 1) / 3));
            comboEl.textContent = `${mult}x`;
            comboEl.className = `dkb-combo-val ${mult > 1 ? 'is-active' : ''}`;
        }

        if (_mode === 'time-attack') {
            const timerEl = _container.querySelector('.dkb-timer-val');
            if (timerEl) timerEl.textContent = Math.max(0, _timeLeft).toFixed(1) + 's';
        } else {
            const shieldPips = _container.querySelectorAll('.dkb-shield-pip');
            shieldPips.forEach((pip, idx) => {
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

        // Timer handling for Time Attack
        if (_mode === 'time-attack') {
            _timeLeft -= dt / 1000;
            if (_timeLeft <= 0) {
                _timeLeft = 0;
                _gameOver();
                return;
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
        _updateHUD();

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
                // If it passes danger threshold line
                const dangerY = _canvasHeight - 32;
                if (t.y - t.radius >= dangerY) {
                    _activeTargets.splice(i, 1);
                    _targetEscaped(t);
                    continue;
                }
                // Bounce off left / right walls
                if (t.x - t.radius < 0) {
                    t.x = t.radius;
                    t.vx = Math.abs(t.vx);
                } else if (t.x + t.radius > _canvasWidth) {
                    t.x = _canvasWidth - t.radius;
                    t.vx = -Math.abs(t.vx);
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

        // Maintain target count
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

        // Apply screen shake
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

        // Constructivist palette fills & strokes
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

        _ctx.stroke(); // Final outer outline

        // Target label typography (counter-rotate text so it stays upright and legible!)
        _ctx.rotate(-target.rotation);
        _ctx.fillStyle = isWrongFlash ? '#B23A22' : '#102A47';
        _ctx.textAlign = 'center';
        _ctx.textBaseline = 'middle';

        // Auto-wrap / format long text
        const text = target.displayText;
        if (text.length > 13 && text.includes(' ')) {
            const parts = text.split(' ');
            const mid = Math.ceil(parts.length / 2);
            const line1 = parts.slice(0, mid).join(' ');
            const line2 = parts.slice(mid).join(' ');
            _ctx.font = '600 12px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            _ctx.fillText(line1, 0, -8);
            _ctx.fillText(line2, 0, 8);
        } else {
            const fontSize = text.length > 12 ? 12 : 14;
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

        // Triangular geometric shard
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
        _canvasWidth = Math.max(320, rect.width || 600);
        _canvasHeight = 420;

        _dpr = window.devicePixelRatio || 1;
        _canvas.width = _canvasWidth * _dpr;
        _canvas.height = _canvasHeight * _dpr;
        _canvas.style.height = _canvasHeight + 'px';

        _ctx = _canvas.getContext('2d');
        _ctx.scale(_dpr, _dpr);

        // Instant touch and click handling
        const handleDown = (e) => {
            e.preventDefault();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            _handleCanvasClick(clientX, clientY);
        };

        _canvas.addEventListener('pointerdown', handleDown);
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

        // Proactively begin audio preloading immediately so audio is ready
        _preloadAudio();
        _render();
    }

    function stop() {
        if (_animId) {
            cancelAnimationFrame(_animId);
            _animId = null;
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
