// ============================================
// GRAMMAR DRILLER
// ============================================
// Rebuilt around the frozen skill registry (skills/<lang>.json) and
// LearnerModel (weakSkills / troubleSkills).
//
// Two focused modes:
//   1. Fix weak areas (default) — targeted practice on concepts the
//      learner has recently missed or is struggling with.
//   2. Practise a skill — deliberate drilling of any canonical grammar skill,
//      with progressive ordering (recognise -> manipulate -> produce),
//      rule reviews, and un-taught skills collapsed at the bottom.
//
// Both tabs are count-based (5, 10, 15, 20 questions). Timed mode is removed.

const GrammarDriller = (function () {
    'use strict';

    const PHASE = { SETTINGS: 1, SESSION: 2, RESULTS: 3 };
    const TAB = { WEAK: 'weak', SKILL: 'skill' };
    const COUNT_OPTIONS = [5, 10, 15, 20];
    const LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2'];

    let _phase = PHASE.SETTINGS;
    let _activeTab = TAB.WEAK;
    let _questionCount = 10;
    let _selectedSkill = null;
    let _container = null;

    let _registry = null; // content/<lang>/indexes/skill-registry.json
    let _index = null;    // content/<lang>/indexes/grammar-index.json -> { bySkill, titles }
    let _bank = null;     // content/<lang>/drills/grammar/a1-bank.json
    let _aliasMap = {};   // old-slug -> canonical-slug
    let _loadedLang = null;

    // Tab 1 state
    let _weakCandidates = [];
    let _checkedWeakSkills = new Set();
    let _isCleanState = false;

    // Tab 2 state
    let _searchQuery = '';

    // Session state
    let _queue = [];
    let _queueIndex = 0;
    let _seen = 0;
    let _correct = 0;
    let _missedDetails = [];
    let _skillStats = {}; // skillId -> { correct: 0, seen: 0, title: '', level: '', distractors: [] }
    let _outcomes = new Map(); // recycleId -> 'again' | 'good'

    // Active modal cleanup
    let _activeRuleModal = null;

    // ---- Helpers ----
    function _escapeHtml(text) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(text)
            : String(text == null ? '' : text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
    }

    function _escMd(value) {
        return _escapeHtml(value)
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
            .replace(/\*([^*]+)\*/g, '<em>$1</em>');
    }

    function _shuffled(list) {
        const copy = list.slice();
        for (let i = copy.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copy[i], copy[j]] = [copy[j], copy[i]];
        }
        return copy;
    }

    function _canonicalSkill(skillId) {
        if (!skillId) return skillId;
        const normalized = String(skillId).trim().replace(/_/g, '-');
        if (_aliasMap && _aliasMap[normalized]) return _aliasMap[normalized];
        return normalized;
    }

    function _formatFallbackTitle(skillId) {
        if (!skillId) return '';
        const text = skillId
            .replace(/-isn-t\b/g, " isn't")
            .replace(/-aren-t\b/g, " aren't")
            .replace(/-don-t\b/g, " don't")
            .replace(/-doesn-t\b/g, " doesn't")
            .replace(/-won-t\b/g, " won't")
            .replace(/-can-t\b/g, " can't")
            .replace(/-s-([a-z])/g, "'s $1")
            .replace(/-s\b/g, "'s");
        const minorWords = new Set(['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'vs', 'yet', 'with']);
        return text.split('-').map((w, i) => {
            const wLower = w.toLowerCase();
            if (i > 0 && minorWords.has(wLower)) return wLower;
            return w.charAt(0).toUpperCase() + w.slice(1);
        }).join(' ');
    }

    function _skillTitle(skillId) {
        const canonical = _canonicalSkill(skillId);
        const regSkill = _registry && _registry.skills && _registry.skills[canonical];
        const raw = (regSkill && regSkill.title)
            || (_index && _index.titles && _index.titles[canonical])
            || _formatFallbackTitle(canonical);
        return raw ? raw.charAt(0).toUpperCase() + raw.slice(1) : canonical;
    }

    function _skillInfo(skillId) {
        const canonical = _canonicalSkill(skillId);
        const reg = (_registry && _registry.skills && _registry.skills[canonical]) || {};
        return {
            id: canonical,
            title: _skillTitle(canonical),
            level: reg.level || 'A1',
            family: reg.family || 'grammar',
            taught_in: reg.taught_in || null,
            requires: reg.requires || []
        };
    }

    // ---- Data Loading ----
    async function _load() {
        if (_registry && _index && _loadedLang === Lang.code()) return;

        const [regData, indexData, bankData] = await Promise.all([
            Content.json(Lang.content('indexes/skill-registry.json')).catch(() => ({ skills: {} })),
            Content.json(Lang.content('indexes/grammar-index.json')).catch(() => ({ bySkill: {}, titles: {} })),
            Content.json(Lang.content('drills/grammar/a1-bank.json')).catch(() => ({ modules: [], items: [] }))
        ]);

        _registry = regData;
        _index = indexData;
        _bank = bankData;
        _loadedLang = Lang.code();

        _aliasMap = {};
        const skObj = (_registry && _registry.skills) || {};
        Object.keys(skObj).forEach(id => {
            const skill = skObj[id];
            if (skill && Array.isArray(skill.aliases)) {
                skill.aliases.forEach(al => { _aliasMap[al] = id; });
            }
        });
    }

    document.addEventListener('language-changed', () => {
        _registry = null;
        _index = null;
        _bank = null;
        _aliasMap = {};
        _loadedLang = null;
        _selectedSkill = null;
        _weakCandidates = [];
        _checkedWeakSkills.clear();
        _activeTab = TAB.WEAK;
        _closeRuleModal();
    });

    // ---- Reached & Taught Skills ----
    function _reachedOnly(entries) {
        const reached = (typeof LearnerPath !== 'undefined' && LearnerPath.reachedExerciseRefs)
            ? LearnerPath.reachedExerciseRefs() : null;
        if (!reached) return entries;
        const kept = entries.filter(e => reached.has(e.ref));
        return kept.length ? kept : entries;
    }

    const SUPPORTED_TYPES = new Set(['multiple-choice', 'fill-blank', 'fill-in-blank', 'dialogue-complete', 'error-correction']);

    function _lessonPoolSize(skillId) {
        const canonical = _canonicalSkill(skillId);
        const entries = (_index && _index.bySkill && (_index.bySkill[canonical] || _index.bySkill[skillId])) || [];
        const valid = entries.filter(e => !e.type || SUPPORTED_TYPES.has(e.type));
        const reached = _reachedOnly(valid);
        return reached ? reached.length : 0;
    }

    function _totalLessonPoolSize(skillId) {
        const canonical = _canonicalSkill(skillId);
        const entries = (_index && _index.bySkill && (_index.bySkill[canonical] || _index.bySkill[skillId])) || [];
        const valid = entries.filter(e => !e.type || SUPPORTED_TYPES.has(e.type));
        return valid.length;
    }

    function _bankPoolSize(skillId) {
        const canonical = _canonicalSkill(skillId);
        return ((_bank && _bank.items) || [])
            .filter(i => _canonicalSkill(i.module) === canonical)
            .length;
    }

    function _effectivePoolSize(skillId, isLearned) {
        const canonical = _canonicalSkill(skillId);
        const bankCount = _bankPoolSize(canonical);
        const lessonCount = _lessonPoolSize(canonical);
        const totalLesson = _totalLessonPoolSize(canonical);
        if (isLearned) {
            return lessonCount + bankCount;
        }
        return (lessonCount || totalLesson) + bankCount;
    }

    function _getLearnedSkillIds() {
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const completedLessonIds = Object.keys(progress).filter(id => progress[id]);
        const learned = new Set();

        const reached = (typeof LearnerPath !== 'undefined' && LearnerPath.reachedExerciseRefs)
            ? LearnerPath.reachedExerciseRefs() : null;

        if (_index && _index.bySkill) {
            Object.keys(_index.bySkill).forEach(skill => {
                const canonical = _canonicalSkill(skill);
                const entries = _index.bySkill[skill] || [];
                if (reached) {
                    if (entries.some(e => reached.has(e.ref))) learned.add(canonical);
                } else if (completedLessonIds.length) {
                    learned.add(canonical);
                }
            });
        }

        return learned;
    }

    function _competenceBadgeHtml(skillId, isLearned) {
        const canonical = _canonicalSkill(skillId);
        if (typeof DrillHistory !== 'undefined') {
            const cls = DrillHistory.classify('grammar:' + canonical);
            if (cls && cls.state === 'strong') {
                const icon = (typeof Art !== 'undefined') ? Art.icon('check') : '✓';
                return `<span class="gd-badge-status gd-status-practiced" title="Practiced">${icon} practiced</span>`;
            }
            if (cls && cls.state === 'weak') {
                const icon = (typeof Art !== 'undefined') ? Art.icon('alert') : '!';
                return `<span class="gd-badge-status gd-status-review" title="Needs review">${icon} needs review</span>`;
            }
            if (cls && cls.state === 'developing') {
                return '<span class="gd-badge-status gd-status-developing">developing</span>';
            }
        }

        if (typeof LearnerModel !== 'undefined' && LearnerModel.skillState) {
            // Synchronous fallback check if already in cache or simple state
            if (isLearned) return '<span class="gd-badge-new"><i>new</i></span>';
        }

        if (isLearned) {
            return '<span class="gd-badge-new"><i>new</i></span>';
        }
        return '<span class="gd-badge-status gd-status-untaught">not taught yet</span>';
    }

    // ---- Normalisation & Progression ----
    function _exerciseProgressionRank(kind) {
        switch (kind) {
            case 'multiple-choice':
            case 'dialogue-complete':
                return 1; // Recognise
            case 'fill-blank':
            case 'error-correction':
                return 2; // Produce / Retrieve
            default:
                return 3;
        }
    }

    function _normaliseBankItem(item, skillId) {
        const canonical = _canonicalSkill(skillId);
        return {
            kind: 'multiple-choice',
            question: item.prompt,
            options: item.options,
            correct: item.options.indexOf(item.answer),
            explanation: item.explanation,
            recycleId: 'bank:' + item.id,
            skillId: canonical,
            skillTitle: _skillTitle(canonical),
            distractor_skills: null
        };
    }

    function _normaliseLessonExercise(ex, skillId) {
        const canonical = _canonicalSkill(skillId);
        const title = _skillTitle(canonical);

        switch (ex.type) {
            case 'multiple-choice':
                return {
                    kind: 'multiple-choice',
                    question: ex.question,
                    options: ex.options,
                    correct: ex.correct,
                    explanation: ex.explanation,
                    distractor_skills: ex.distractor_skills || null,
                    skillId: canonical,
                    skillTitle: title
                };
            case 'dialogue-complete':
                return {
                    kind: 'dialogue-complete',
                    prompt: ex.prompt,
                    options: ex.options,
                    correct: ex.correct,
                    explanation: ex.explanation,
                    distractor_skills: ex.distractor_skills || null,
                    skillId: canonical,
                    skillTitle: title
                };
            case 'fill-blank':
                return {
                    kind: 'fill-blank',
                    sentence: ex.sentence,
                    hint: ex.hint,
                    answer: ex.answer || (ex.answers && ex.answers[0]),
                    acceptable: ex.answers || [ex.answer],
                    explanation: ex.explanation,
                    distractor_skills: ex.distractor_skills || null,
                    skillId: canonical,
                    skillTitle: title
                };
            case 'error-correction':
                return {
                    kind: 'error-correction',
                    sentence: ex.sentence,
                    solution: ex.solution,
                    explanation: ex.explanation,
                    distractor_skills: null,
                    skillId: canonical,
                    skillTitle: title
                };
            case 'fill-in-blank':
                return {
                    kind: 'multiple-choice',
                    question: ex.sentence,
                    options: ex.options,
                    correct: (ex.options || []).indexOf(ex.answer),
                    explanation: ex.explanation,
                    distractor_skills: ex.distractor_skills || null,
                    skillId: canonical,
                    skillTitle: title
                };
            case 'sentence-builder':
            case 'sentence-order':
            case 'matching':
            default:
                // Dropped: sentence-builder and sentence-order test word/tile ordering
                // rather than targeted grammar selection; matching converts vocab to MCQ.
                return null;
        }
    }

    async function _resolveLessonEntries(entries, skillId) {
        const canonical = _canonicalSkill(skillId);
        const refs = [...new Set(entries.map(e => e.ref))];
        const files = await Promise.all(refs.map(ref =>
            Content.json(Lang.content(ref)).catch(() => ({ exercises: [] }))
        ));
        const byRef = {};
        refs.forEach((ref, i) => { byRef[ref] = files[i]; });

        const resolved = [];
        const seenIds = new Set();
        for (const entry of entries) {
            if (seenIds.has(entry.id)) continue;
            const file = byRef[entry.ref];
            const ex = (file && file.exercises || []).find(e => e.id === entry.id);
            if (!ex) continue;
            const norm = _normaliseLessonExercise(ex, canonical);
            if (norm) {
                norm.recycleId = entry.id;
                resolved.push(norm);
                seenIds.add(entry.id);
            }
        }
        return resolved;
    }

    // Resolves all available exercises for a single skill, combining lesson exercises
    // and matching bank items, with progressive ordering (rank 1 -> 2 -> 3).
    async function _resolveSkillPool(skillId) {
        const canonical = _canonicalSkill(skillId);
        const rawEntries = (_index && _index.bySkill && (_index.bySkill[canonical] || _index.bySkill[skillId])) || [];
        const valid = rawEntries.filter(e => !e.type || SUPPORTED_TYPES.has(e.type));
        const entries = _reachedOnly(valid);

        const lessonItems = await _resolveLessonEntries(entries, canonical);

        // Opportunistic bank items matching this canonical slug
        const bankItems = ((_bank && _bank.items) || [])
            .filter(i => _canonicalSkill(i.module) === canonical)
            .map(i => _normaliseBankItem(i, canonical));

        const combined = lessonItems.concat(bankItems);

        // Sort into progression buckets: recognise (MCQ/dialogue) -> retrieve/produce (fill-blank/error-correction)
        const rank1 = [];
        const rank2 = [];

        combined.forEach(item => {
            const rank = _exerciseProgressionRank(item.kind);
            if (rank === 1) rank1.push(item);
            else rank2.push(item);
        });

        return [
            ..._shuffled(rank1),
            ..._shuffled(rank2)
        ];
    }

    // ---- Queue Builders ----
    async function _buildSkillQueue(skillId, count) {
        const pool = await _resolveSkillPool(skillId);
        if (!pool.length) return [];
        // Take unique items up to count — avoid repeating questions
        return pool.slice(0, count);
    }

    async function _buildWeakQueue(skillIds, totalCount) {
        if (!skillIds.length) return [];

        const schedule = (typeof loadRecycleSchedule === 'function') ? loadRecycleSchedule() : {};
        const poolsBySkill = {};

        // Resolve pool for each active skill
        for (const sid of skillIds) {
            poolsBySkill[sid] = await _resolveSkillPool(sid);
        }

        // Divide quota among skills (worst first)
        const baseQuota = Math.floor(totalCount / skillIds.length);
        let remainder = totalCount % skillIds.length;
        const quotas = {};
        skillIds.forEach((sid, idx) => {
            quotas[sid] = baseQuota + (idx < remainder ? 1 : 0);
        });

        // For each skill, select items prioritizing missed ones from recycle schedule
        const selectedBySkill = {};
        for (const sid of skillIds) {
            const pool = poolsBySkill[sid];
            const missedPriority = [];
            const freshOrGeneral = [];

            pool.forEach(item => {
                const card = schedule[item.recycleId];
                if (card && card.lapses > 0 && (card.reviews === 0 || card.ease < 2.3)) {
                    missedPriority.push(item);
                } else {
                    freshOrGeneral.push(item);
                }
            });

            // Missed questions first, followed by fresh questions, preserving rank order within
            const combinedSkillQueue = [...missedPriority, ...freshOrGeneral];
            selectedBySkill[sid] = combinedSkillQueue.slice(0, quotas[sid]);
        }

        // Interleave the questions across the skills so consecutive questions target different skills
        const interleaved = [];
        let added = true;
        let round = 0;
        while (added) {
            added = false;
            for (const sid of skillIds) {
                const list = selectedBySkill[sid];
                if (list && round < list.length) {
                    interleaved.push(list[round]);
                    added = true;
                }
            }
            round++;
        }

        return interleaved.slice(0, totalCount);
    }

    // ---- Tab 1: Load Weak Areas ----
    async function _loadWeakAreas() {
        const trouble = (typeof LearnerModel !== 'undefined' && LearnerModel.troubleSkills)
            ? await LearnerModel.troubleSkills() : [];
        const weak = (typeof LearnerModel !== 'undefined' && LearnerModel.weakSkills)
            ? await LearnerModel.weakSkills() : [];

        const seenSkills = new Set();
        const candidates = [];

        // Trouble skills first (recent unresolved misses)
        for (const t of trouble) {
            const sid = _canonicalSkill(t.skillId);
            if (seenSkills.has(sid)) continue;
            if (_effectivePoolSize(sid, true) > 0) {
                seenSkills.add(sid);
                const info = _skillInfo(sid);
                candidates.push({
                    skillId: sid,
                    title: info.title,
                    level: info.level,
                    family: info.family,
                    taught_in: info.taught_in,
                    reason: t.missed > 0 ? `${t.missed} recent ${t.missed === 1 ? 'miss' : 'misses'}` : (t.levelTest ? `Level test (${t.levelTest})` : 'Recent trouble'),
                    badgeType: 'trouble'
                });
            }
            if (candidates.length >= 4) break;
        }

        // Weak / developing skills next
        if (candidates.length < 4) {
            for (const w of weak) {
                const sid = _canonicalSkill(w.skillId);
                if (seenSkills.has(sid)) continue;
                if (_effectivePoolSize(sid, true) > 0) {
                    seenSkills.add(sid);
                    const info = _skillInfo(sid);
                    const isWeak = w.state === 'weak';
                    candidates.push({
                        skillId: sid,
                        title: info.title,
                        level: info.level,
                        family: info.family,
                        taught_in: info.taught_in,
                        reason: isWeak ? 'Needs review' : 'Developing',
                        badgeType: isWeak ? 'weak' : 'developing'
                    });
                }
                if (candidates.length >= 4) break;
            }
        }

        // If no trouble/weak spots detected, offer recently reached skills
        if (!candidates.length) {
            _isCleanState = true;
            const learnedIds = Array.from(_getLearnedSkillIds()).reverse();
            for (const sid of learnedIds) {
                if (_effectivePoolSize(sid, true) > 0) {
                    const info = _skillInfo(sid);
                    candidates.push({
                        skillId: sid,
                        title: info.title,
                        level: info.level,
                        family: info.family,
                        taught_in: info.taught_in,
                        reason: 'Recently studied',
                        badgeType: 'recent'
                    });
                }
                if (candidates.length >= 3) break;
            }
        } else {
            _isCleanState = false;
        }

        _weakCandidates = candidates;
        _checkedWeakSkills = new Set(candidates.map(c => c.skillId));
    }

    // ---- Catalogue Collection ----
    function _getCatalogue() {
        const skillsDict = (_registry && _registry.skills) || {};
        const learnedSet = _getLearnedSkillIds();

        // Include skills from registry with kind === 'grammar' and NOT retired, or fallback from index
        let skillIds = Object.keys(skillsDict).filter(id => skillsDict[id].kind === 'grammar' && !skillsDict[id].retired);
        if (!skillIds.length && _index && _index.bySkill) {
            skillIds = Object.keys(_index.bySkill);
        }

        const taught = [];
        const untaught = [];

        skillIds.forEach(id => {
            const canonical = _canonicalSkill(id);
            const totalSize = _totalLessonPoolSize(canonical) + _bankPoolSize(canonical);
            // Hide skills that have 0 exercises available in this course
            if (totalSize === 0) return;

            const info = _skillInfo(canonical);
            const isLearned = learnedSet.has(canonical);
            const poolSize = _effectivePoolSize(canonical, isLearned);

            const item = {
                id: canonical,
                title: info.title,
                level: info.level,
                family: info.family,
                taught_in: info.taught_in,
                poolSize: poolSize,
                totalSize: totalSize,
                isLearned: isLearned,
                badgeHtml: _competenceBadgeHtml(canonical, isLearned)
            };

            if (isLearned) taught.push(item);
            else untaught.push(item);
        });

        // Sort by level order then title
        const sortFn = (a, b) => {
            const la = LEVEL_ORDER.indexOf(a.level);
            const lb = LEVEL_ORDER.indexOf(b.level);
            if (la !== lb) return la - lb;
            return a.title.localeCompare(b.title);
        };

        taught.sort(sortFn);
        untaught.sort(sortFn);

        return { taught, untaught, all: [...taught, ...untaught] };
    }

    // ---- Rule Modal ----
    function _renderRuleSectionsFallback(sections) {
        if (!Array.isArray(sections)) return '';
        return sections.map(part => {
            if (part.type === 'text') {
                return `<p class="lsn-text">${_escMd(part.content || '')}</p>`;
            }
            if (part.type === 'tip') {
                return `<div class="lsn-tip"><strong>Tip</strong><p>${_escMd(part.content || '')}</p></div>`;
            }
            if (part.type === 'table') {
                const rows = (part.rows || []).map(r =>
                    `<tr>${r.map(cell => `<td>${_escapeHtml(cell)}</td>`).join('')}</tr>`
                ).join('');
                return `<table class="lsn-table"><tbody>${rows}</tbody></table>`;
            }
            if (part.type === 'examples') {
                const items = (part.items || []).map(it => `
                    <div class="lsn-example" style="margin-bottom:6px;">
                        <span class="lsn-example-target" style="font-style:italic;font-weight:600;">${_escapeHtml(it.spanish || it.target || it.hu || '')}</span>
                        <span class="lsn-example-en" style="color:var(--muted);margin-left:8px;">— ${_escapeHtml(it.english || it.en || '')}</span>
                    </div>
                `).join('');
                return `<div class="lsn-examples" style="margin:12px 0;">${items}</div>`;
            }
            return '';
        }).join('');
    }

    async function _openRuleModal(skillId) {
        _closeRuleModal();

        const info = _skillInfo(skillId);
        if (!info.taught_in) return;

        const level = (info.level || 'a1').toLowerCase();
        const ref = `grammar/${level}/${info.taught_in}.json`;

        let ruleData = null;
        try {
            ruleData = await Content.json(Lang.content(ref));
        } catch (e) {
            if (typeof Lang !== 'undefined' && Lang.code() === 'es-latam') {
                try {
                    ruleData = await Content.json('content/es-es/' + ref);
                } catch (e2) {
                    ruleData = null;
                }
            } else {
                ruleData = null;
            }
        }

        const overlay = document.createElement('div');
        overlay.className = 'gd-rule-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');

        let bodyHtml = '';
        if (ruleData && ruleData.sections) {
            if (typeof stepRenderers !== 'undefined' && stepRenderers.grammar) {
                bodyHtml = stepRenderers.grammar({ title: ruleData.title, parts: ruleData.sections });
            } else {
                bodyHtml = _renderRuleSectionsFallback(ruleData.sections);
            }
        } else {
            bodyHtml = `
                <div style="padding: 12px 0;">
                    <p class="lsn-text"><strong>${_escapeHtml(info.title)}</strong></p>
                    <p class="lsn-text text-muted" style="margin-top:6px;">Level ${info.level}</p>
                    <p class="lsn-text" style="margin-top:10px;">A standalone reference card is not yet authored for this topic. Practice exercises test this structure directly.</p>
                </div>
            `;
        }

        overlay.innerHTML = `
            <div class="gd-rule-modal">
                <div class="gd-rule-header">
                    <div>
                        <span class="hm-eyebrow" style="font-size:11px;font-weight:700;text-transform:uppercase;color:var(--muted);">${_escapeHtml(info.level)} Grammar Reference</span>
                        <h3>${_escapeHtml((ruleData && ruleData.title) || info.title)}</h3>
                    </div>
                    <button class="wp-close" data-close-rule="1" aria-label="Close">&times;</button>
                </div>
                <div class="gd-rule-body">
                    ${bodyHtml}
                </div>
                <div class="gd-rule-footer">
                    <button class="vbtn vbtn-primary" data-close-rule="1">Back to Practice</button>
                </div>
            </div>
        `;

        const closeModal = () => _closeRuleModal();
        overlay.querySelectorAll('[data-close-rule]').forEach(btn => btn.addEventListener('click', closeModal));
        overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });

        const onKeyDown = e => { if (e.key === 'Escape') closeModal(); };
        document.addEventListener('keydown', onKeyDown);

        _activeRuleModal = { overlay, onKeyDown };
        document.body.appendChild(overlay);
    }

    function _closeRuleModal() {
        if (_activeRuleModal) {
            document.removeEventListener('keydown', _activeRuleModal.onKeyDown);
            if (_activeRuleModal.overlay) {
                _activeRuleModal.overlay.remove();
            }
            _activeRuleModal = null;
        }
    }

    // ================================================================
    //  RENDERING — Settings
    // ================================================================
    async function _renderSettings() {
        _closeRuleModal();
        const catalogue = _getCatalogue();

        // Default selected skill for Tab 2
        if (!_selectedSkill || !catalogue.all.some(s => s.id === _selectedSkill)) {
            if (catalogue.taught.length) _selectedSkill = catalogue.taught[0].id;
            else if (catalogue.all.length) _selectedSkill = catalogue.all[0].id;
        }

        // Render Tab Switcher
        const switcherHtml = `
            <div class="gd-tab-switcher" role="tablist">
                <button class="gd-tab-btn${_activeTab === TAB.WEAK ? ' active' : ''}"
                    data-tab="${TAB.WEAK}" role="tab" aria-selected="${_activeTab === TAB.WEAK}">Fix weak areas</button>
                <button class="gd-tab-btn${_activeTab === TAB.SKILL ? ' active' : ''}"
                    data-tab="${TAB.SKILL}" role="tab" aria-selected="${_activeTab === TAB.SKILL}">Practise a skill</button>
            </div>
        `;

        // Render Question Count selector chips
        const countSelectorHtml = `
            <div class="gd-setting">
                <label>Number of questions</label>
                <div class="gd-count-chips">
                    ${COUNT_OPTIONS.map(n => `
                        <button type="button" class="gd-chip${n === _questionCount ? ' active' : ''}" data-count="${n}">${n}</button>
                    `).join('')}
                </div>
            </div>
        `;

        let tabContentHtml = '';

        if (_activeTab === TAB.WEAK) {
            // Tab 1: Fix weak areas
            if (_weakCandidates.length === 0) {
                tabContentHtml = `
                    <div class="gd-clean-state">
                        <div class="gd-clean-icon">${(typeof Art !== 'undefined') ? Art.icon('sparkles') : '✦'}</div>
                        <h3 class="gd-clean-title">No practice history yet!</h3>
                        <p class="gd-clean-desc">Complete lessons to track concepts you find challenging, or pick any grammar skill to practice directly.</p>
                        <div class="gd-clean-actions">
                            <button type="button" class="vbtn vbtn-primary" data-action="switch-to-skill-tab">Browse All Skills</button>
                        </div>
                    </div>
                `;
            } else if (_isCleanState && _weakCandidates.length > 0) {
                tabContentHtml = `
                    <div class="gd-clean-state">
                        <div class="gd-clean-icon">${(typeof Art !== 'undefined') ? Art.icon('check') : ''}</div>
                        <h3 class="gd-clean-title">No weak areas detected!</h3>
                        <p class="gd-clean-desc">Your grammar accuracy has been solid across completed lessons. Reinforce recently learned concepts or pick any skill to drill deliberately.</p>
                        <div class="gd-clean-actions">
                            <button type="button" class="vbtn vbtn-primary" data-action="start-recent">Reinforce Recent Topics</button>
                            <button type="button" class="vbtn vbtn-secondary" data-action="switch-to-skill-tab">Browse All Skills</button>
                        </div>
                    </div>
                `;
            } else {
                tabContentHtml = `
                    <div class="gd-focus-card">
                        <div class="gd-focus-header">
                            <h3 class="gd-focus-title">Focus Concepts</h3>
                            <span class="gd-focus-sub">${_checkedWeakSkills.size} of ${_weakCandidates.length} selected</span>
                        </div>
                        <div class="gd-weak-list">
                            ${_weakCandidates.map(c => `
                                <div class="gd-weak-item${_checkedWeakSkills.has(c.skillId) ? ' is-checked' : ''}">
                                    <div class="gd-weak-item-left">
                                        <input type="checkbox" id="weak-chk-${c.skillId}" class="gd-weak-checkbox"
                                            data-skill="${c.skillId}" ${_checkedWeakSkills.has(c.skillId) ? 'checked' : ''}>
                                        <label for="weak-chk-${c.skillId}" class="gd-weak-label">
                                            <span class="gd-weak-skill-title">${_escapeHtml(c.title)}</span>
                                            <span class="gd-weak-reason is-${c.badgeType}">${_escapeHtml(c.reason)}</span>
                                        </label>
                                    </div>
                                    ${c.taught_in ? `
                                        <button type="button" class="gd-rule-link-btn" data-rule-skill="${c.skillId}" title="Review rule">Review rule</button>
                                    ` : ''}
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    ${countSelectorHtml}
                    <button class="vbtn vbtn-primary vbtn-block" data-action="start-weak"
                        ${_checkedWeakSkills.size === 0 ? 'disabled style="opacity:0.5;"' : ''}>Start Practice</button>
                `;
            }
        } else {
            // Tab 2: Practise a skill
            const selectedInfo = catalogue.all.find(s => s.id === _selectedSkill) || catalogue.all[0];

            // Filter skills by search query
            const q = _searchQuery.toLowerCase().trim();
            const filterFn = s => !q || s.title.toLowerCase().includes(q) || s.family.toLowerCase().includes(q) || s.level.toLowerCase().includes(q);

            const filteredTaught = catalogue.taught.filter(filterFn);
            const filteredUntaught = catalogue.untaught.filter(filterFn);

            // Group taught skills by level
            const renderSkillGroup = (skills) => {
                const byLevel = {};
                skills.forEach(s => {
                    byLevel[s.level] = byLevel[s.level] || [];
                    byLevel[s.level].push(s);
                });

                return LEVEL_ORDER.map(lvl => {
                    const group = byLevel[lvl];
                    if (!group || !group.length) return '';
                    return `
                        <div class="gd-level-header">Level ${lvl}</div>
                        ${group.map(s => `
                            <button type="button" class="gd-skill-row${s.id === _selectedSkill ? ' is-selected' : ''}"
                                data-skill-id="${s.id}">
                                <div class="gd-skill-row-main">
                                    <span class="gd-skill-row-title">${_escapeHtml(s.title)}</span>
                                    <div class="gd-skill-row-meta">
                                        <span class="gd-exercise-count">${s.poolSize} ${s.poolSize === 1 ? 'exercise' : 'exercises'}</span>
                                    </div>
                                </div>
                                <div class="gd-skill-row-badges">
                                    ${s.badgeHtml}
                                </div>
                            </button>
                        `).join('')}
                    `;
                }).join('');
            };

            const isNewLearner = catalogue.taught.length === 0;
            const taughtListHtml = filteredTaught.length
                ? renderSkillGroup(filteredTaught)
                : (isNewLearner && !q ? '' : '<div class="gd-skill-empty">No matching taught skills.</div>');

            const untaughtListHtml = filteredUntaught.length
                ? renderSkillGroup(filteredUntaught)
                : '<div class="gd-skill-empty">No matching untaught skills.</div>';

            const untaughtOpen = q || isNewLearner;
            const untaughtTitle = isNewLearner
                ? `All skills (${catalogue.untaught.length} skills)`
                : `Not taught yet (${catalogue.untaught.length} skills)`;

            tabContentHtml = `
                <div class="gd-skill-browser-wrap">
                    <div class="gd-search-wrap">
                        <input type="search" id="gd-skill-search" class="gd-skill-filter"
                            placeholder="Search skills by name, concept, or level…" value="${_escapeHtml(_searchQuery)}" autocomplete="off" />
                    </div>

                    <div class="gd-skill-browser" id="gd-skill-browser">
                        ${taughtListHtml}

                        ${catalogue.untaught.length ? `
                            <details class="gd-untaught-section" ${untaughtOpen ? 'open' : ''}>
                                <summary class="gd-untaught-summary">${untaughtTitle}</summary>
                                <div class="gd-untaught-list" style="margin-top:8px;">
                                    ${untaughtListHtml}
                                </div>
                            </details>
                        ` : ''}
                    </div>
                </div>

                ${selectedInfo ? `
                    <div class="gd-selected-summary">
                        <div class="gd-selected-summary-left">
                            <div class="gd-selected-skill-name">${_escapeHtml(selectedInfo.title)}</div>
                            <div class="gd-selected-skill-info">
                                Level ${selectedInfo.level} · ${selectedInfo.poolSize} exercises available
                            </div>
                        </div>
                        ${selectedInfo.taught_in ? `
                            <button type="button" class="gd-rule-link-btn" data-rule-skill="${selectedInfo.id}">Review rule</button>
                        ` : ''}
                    </div>
                ` : ''}

                ${countSelectorHtml}
                <button class="vbtn vbtn-primary vbtn-block" data-action="start-skill"
                    ${!_selectedSkill ? 'disabled style="opacity:0.5;"' : ''}>Start Practice</button>
            `;
        }

        _container.innerHTML = `
            <div class="gd-settings">
                <h2 class="gd-title">Grammar Driller</h2>
                ${(typeof DrillInfo !== 'undefined') ? DrillInfo.buttonHtml('grammar') : ''}
                ${switcherHtml}
                <div class="gd-tab-panel">
                    ${tabContentHtml}
                </div>
            </div>
        `;

        if (typeof DrillInfo !== 'undefined') DrillInfo.attach(_container);

        // Attach Switcher Events
        _container.querySelectorAll('.gd-tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                _activeTab = btn.dataset.tab;
                _renderSettings();
            });
        });

        // Attach Count Chips Events
        _container.querySelectorAll('.gd-chip').forEach(btn => {
            btn.addEventListener('click', () => {
                _questionCount = Number(btn.dataset.count);
                _container.querySelectorAll('.gd-chip').forEach(b => b.classList.toggle('active', b === btn));
            });
        });

        // Attach Review Rule Modal Buttons
        _container.querySelectorAll('[data-rule-skill]').forEach(btn => {
            btn.addEventListener('click', e => {
                e.stopPropagation();
                _openRuleModal(btn.dataset.ruleSkill);
            });
        });

        // Tab 1 Events
        if (_activeTab === TAB.WEAK) {
            _container.querySelectorAll('.gd-weak-checkbox').forEach(chk => {
                chk.addEventListener('change', () => {
                    const sid = chk.dataset.skill;
                    if (chk.checked) _checkedWeakSkills.add(sid);
                    else _checkedWeakSkills.delete(sid);

                    const item = chk.closest('.gd-weak-item');
                    if (item) item.classList.toggle('is-checked', chk.checked);

                    const sub = _container.querySelector('.gd-focus-sub');
                    if (sub) sub.textContent = `${_checkedWeakSkills.size} of ${_weakCandidates.length} selected`;

                    const startBtn = _container.querySelector('[data-action="start-weak"]');
                    if (startBtn) {
                        startBtn.disabled = _checkedWeakSkills.size === 0;
                        startBtn.style.opacity = _checkedWeakSkills.size === 0 ? '0.5' : '1';
                    }
                });
            });

            const startWeakBtn = _container.querySelector('[data-action="start-weak"]');
            if (startWeakBtn) {
                startWeakBtn.addEventListener('click', () => {
                    if (_checkedWeakSkills.size > 0) _startSession();
                });
            }

            const startRecentBtn = _container.querySelector('[data-action="start-recent"]');
            if (startRecentBtn) {
                startRecentBtn.addEventListener('click', () => {
                    _checkedWeakSkills = new Set(_weakCandidates.map(c => c.skillId));
                    _startSession();
                });
            }

            const switchBtn = _container.querySelector('[data-action="switch-to-skill-tab"]');
            if (switchBtn) {
                switchBtn.addEventListener('click', () => {
                    _activeTab = TAB.SKILL;
                    _renderSettings();
                });
            }
        } else {
            // Tab 2 Events
            const searchInput = _container.querySelector('#gd-skill-search');
            if (searchInput) {
                searchInput.addEventListener('input', e => {
                    _searchQuery = e.target.value;
                    _renderSettings();
                    const nextInput = _container.querySelector('#gd-skill-search');
                    if (nextInput) {
                        nextInput.focus();
                        nextInput.setSelectionRange(nextInput.value.length, nextInput.value.length);
                    }
                });
            }

            _container.querySelectorAll('.gd-skill-row').forEach(row => {
                row.addEventListener('click', () => {
                    _selectedSkill = row.dataset.skillId;
                    _renderSettings();
                });
            });

            const startSkillBtn = _container.querySelector('[data-action="start-skill"]');
            if (startSkillBtn) {
                startSkillBtn.addEventListener('click', () => {
                    if (_selectedSkill) _startSession();
                });
            }
        }
    }

    // ================================================================
    //  RENDERING — Session
    // ================================================================
    async function _startSession() {
        _closeRuleModal();
        _container.innerHTML = `<div class="gd-loading">Building practice session…</div>`;

        let queue = [];
        if (_activeTab === TAB.WEAK) {
            const skillIds = Array.from(_checkedWeakSkills);
            queue = await _buildWeakQueue(skillIds, _questionCount);
        } else {
            queue = await _buildSkillQueue(_selectedSkill, _questionCount);
        }

        if (!queue.length) {
            _phase = PHASE.SETTINGS;
            _container.innerHTML = `
                <div class="gd-settings">
                    <div class="gd-clean-state">
                        <h3 class="gd-clean-title">No exercises available</h3>
                        <p class="gd-clean-desc">No interactive exercises were found for this selection yet.</p>
                        <button class="vbtn vbtn-primary" data-action="back-to-settings">Change Selection</button>
                    </div>
                </div>
            `;
            _container.querySelector('[data-action="back-to-settings"]').addEventListener('click', () => {
                _renderSettings();
            });
            return;
        }

        _queue = queue;
        _queueIndex = 0;
        _seen = 0;
        _correct = 0;
        _missedDetails = [];
        _skillStats = {};
        _outcomes = new Map();

        // Initialize skill stats for all skills in queue
        _queue.forEach(item => {
            if (!_skillStats[item.skillId]) {
                const info = _skillInfo(item.skillId);
                _skillStats[item.skillId] = {
                    title: item.skillTitle || info.title,
                    level: info.level,
                    taught_in: info.taught_in,
                    seen: 0,
                    correct: 0,
                    distractors: []
                };
            }
        });

        _phase = PHASE.SESSION;
        _renderSession();
    }

    function _progressPercent() {
        return Math.min(100, Math.round((_queueIndex / Math.max(1, _queue.length)) * 100));
    }

    function _renderSession() {
        _closeRuleModal();

        const currentItem = _queue[_queueIndex];
        const currentInfo = _skillInfo(currentItem.skillId);

        _container.innerHTML = `
            <div class="driller-progress-track" aria-hidden="true">
                <div class="driller-progress-bar" style="width: ${_progressPercent()}%"></div>
            </div>
            <div class="gd-hud">
                <span class="gd-hud-score">Question ${_queueIndex + 1} of ${_queue.length}</span>
                <button class="gd-change-skill" data-action="exit-session">← Exit</button>
            </div>
            <div class="gd-hud-subline">
                <span class="gd-hud-skill-tag">${_escapeHtml(currentItem.skillTitle || currentInfo.title)}</span>
                ${currentInfo.taught_in ? `
                    <button type="button" class="gd-hud-rule-btn" data-rule-skill="${currentItem.skillId}">Review rule</button>
                ` : ''}
            </div>
            <div class="gd-exercise"></div>
        `;

        _container.querySelector('[data-action="exit-session"]').addEventListener('click', _abortSession);

        const ruleBtn = _container.querySelector('.gd-hud-rule-btn');
        if (ruleBtn) {
            ruleBtn.addEventListener('click', () => _openRuleModal(currentItem.skillId));
        }

        const exerciseRoot = _container.querySelector('.gd-exercise');
        GrammarRunner.render(exerciseRoot, {
            exercise: currentItem,
            onResult: (correct, details) => {
                _seen++;
                const sid = currentItem.skillId;
                if (_skillStats[sid]) {
                    _skillStats[sid].seen++;
                    if (correct) _skillStats[sid].correct++;
                }

                _noteOutcome(currentItem, correct);

                if (correct) {
                    _correct++;
                } else {
                    let distractorTitle = null;
                    if (currentItem.distractor_skills && details && details.user && currentItem.options) {
                        const userIdx = currentItem.options.indexOf(details.user);
                        const distractorSlug = userIdx >= 0 ? currentItem.distractor_skills[String(userIdx)] : null;
                        if (distractorSlug) {
                            distractorTitle = _skillTitle(distractorSlug);
                            if (_skillStats[sid]) {
                                _skillStats[sid].distractors.push(distractorTitle);
                            }
                        }
                    }

                    _missedDetails.push({
                        question: (details && details.question) || 'Grammar question',
                        correct: (details && details.correct) || '',
                        user: (details && details.user) || '',
                        skillId: sid,
                        skillTitle: currentItem.skillTitle,
                        distractorTitle: distractorTitle
                    });
                }

                const score = _container.querySelector('.gd-hud-score');
                if (score) score.textContent = `Question ${_queueIndex + 1} of ${_queue.length}`;
                const bar = _container.querySelector('.driller-progress-bar');
                if (bar) bar.style.width = _progressPercent() + '%';
            },
            onNext: _nextExercise
        });
    }

    function _noteOutcome(exercise, correct) {
        if (!exercise || !exercise.recycleId) return;
        if (_outcomes.get(exercise.recycleId) === 'again') return;
        _outcomes.set(exercise.recycleId, correct ? 'good' : 'again');
    }

    function _creditRecycle() {
        if (!_outcomes.size || typeof Recycle === 'undefined' || !Recycle.credit) return;
        const results = [];
        _outcomes.forEach((rating, id) => results.push({ id, rating }));
        _outcomes = new Map();
        Recycle.credit(results);
    }

    function _nextExercise() {
        if (_queueIndex + 1 >= _queue.length) {
            _finishSession();
            return;
        }
        _queueIndex++;
        _renderSession();
    }

    function _abortSession() {
        _creditRecycle();
        _closeRuleModal();
        _phase = PHASE.SETTINGS;
        _renderSettings();
    }

    // ================================================================
    //  RENDERING — Results
    // ================================================================
    function _finishSession() {
        _creditRecycle();
        _closeRuleModal();

        // Record history per tested skill
        if (typeof DrillHistory !== 'undefined' && _seen > 0) {
            Object.keys(_skillStats).forEach(sid => {
                const s = _skillStats[sid];
                if (s.seen > 0) {
                    DrillHistory.record('grammar:' + sid, {
                        correct: s.correct,
                        wrong: s.seen - s.correct
                    });
                }
            });
        }

        _phase = PHASE.RESULTS;
        _renderResults();
    }

    function _renderResults() {
        const accuracy = _seen ? Math.round((_correct / _seen) * 100) : 0;
        const testedSkillIds = Object.keys(_skillStats);

        const skillBreakdownHtml = testedSkillIds.length ? `
            <div class="gd-skill-breakdown">
                <h4 class="gd-skill-breakdown-title">Performance by Skill</h4>
                <div class="gd-skill-breakdown-list">
                    ${testedSkillIds.map(sid => {
                        const stat = _skillStats[sid];
                        const pct = stat.seen ? Math.round((stat.correct / stat.seen) * 100) : 0;
                        const distractorNote = (stat.distractors && stat.distractors.length)
                            ? `<div class="gd-distractor-note">Tip: You selected a ${stat.distractors[0]} form on this skill.</div>`
                            : '';
                        return `
                            <div class="gd-skill-breakdown-card">
                                <div class="gd-skill-breakdown-left">
                                    <div class="gd-skill-breakdown-name">${_escapeHtml(stat.title)} <span style="font-size:11px;font-weight:700;color:var(--muted);">${stat.level}</span></div>
                                    <div class="gd-skill-breakdown-score">${stat.correct}/${stat.seen} correct (${pct}%)</div>
                                    ${distractorNote}
                                </div>
                                ${stat.taught_in ? `
                                    <button type="button" class="gd-rule-link-btn" data-rule-skill="${sid}">Review rule</button>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        ` : '';

        const missedRecapHtml = _missedDetails.length ? `
            <div class="gd-missed-recap">
                <h4 class="gd-missed-title">Review Missed Questions</h4>
                <div class="gd-missed-list">
                    ${_missedDetails.map(item => `
                        <div class="gd-missed-card">
                            <div class="gd-missed-q">
                                <span class="gd-family-tag" style="margin-right:6px;">${_escapeHtml(item.skillTitle)}</span>
                                ${_escapeHtml(item.question)}
                            </div>
                            <div class="gd-missed-answers">
                                ${item.user ? `<div class="gd-missed-user"><span class="gd-badge-wrong">Your answer:</span> ${_escapeHtml(item.user)}</div>` : ''}
                                <div class="gd-missed-correct"><span class="gd-badge-correct">Correct:</span> <strong>${_escapeHtml(item.correct)}</strong></div>
                                ${item.distractorTitle ? `<div style="font-size:12px;color:var(--ochre-text);margin-top:2px;">(Used a ${item.distractorTitle} form)</div>` : ''}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        ` : '';

        _container.innerHTML = `
            <div class="vspeed-results" style="max-width:540px;margin:0 auto;padding:16px;">
                <h3 class="vspeed-results-title">Session Complete</h3>
                <div class="vspeed-results-grid">
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Correct</span>
                        <span class="vspeed-stat-value">${_correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Wrong</span>
                        <span class="vspeed-stat-value">${_seen - _correct}</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Accuracy</span>
                        <span class="vspeed-stat-value">${accuracy}%</span>
                    </div>
                    <div class="vspeed-stat">
                        <span class="vspeed-stat-label">Total</span>
                        <span class="vspeed-stat-value">${_seen}</span>
                    </div>
                </div>

                ${skillBreakdownHtml}
                ${missedRecapHtml}

                <div class="vspeed-results-actions" style="margin-top:24px;">
                    <button class="vbtn vbtn-primary" data-action="play-again">Practice Again</button>
                    ${_activeTab === TAB.SKILL ? `
                        <button class="vbtn vbtn-secondary" data-action="go-to-weak">Fix Weak Areas</button>
                    ` : `
                        <button class="vbtn vbtn-secondary" data-action="browse-skills">Browse Skills</button>
                    `}
                    <button class="vbtn vbtn-secondary" data-action="change-settings">Settings</button>
                    <button class="vbtn vbtn-secondary" data-action="exit-workshop">Back to Workshop</button>
                </div>
            </div>
        `;

        _container.querySelectorAll('[data-rule-skill]').forEach(btn => {
            btn.addEventListener('click', () => _openRuleModal(btn.dataset.ruleSkill));
        });

        _container.querySelector('[data-action="play-again"]').addEventListener('click', _startSession);
        _container.querySelector('[data-action="change-settings"]').addEventListener('click', _abortSession);

        const weakBtn = _container.querySelector('[data-action="go-to-weak"]');
        if (weakBtn) {
            weakBtn.addEventListener('click', () => {
                _activeTab = TAB.WEAK;
                _abortSession();
            });
        }

        const browseBtn = _container.querySelector('[data-action="browse-skills"]');
        if (browseBtn) {
            browseBtn.addEventListener('click', () => {
                _activeTab = TAB.SKILL;
                _abortSession();
            });
        }

        const exitBtn = _container.querySelector('[data-action="exit-workshop"]');
        if (exitBtn) {
            exitBtn.addEventListener('click', () => {
                if (typeof Workshop !== 'undefined') Workshop.close();
            });
        }

        if (typeof RecommendationEngine !== 'undefined') {
            RecommendationEngine.mountNextAction(_container);
        }
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    async function render(root, options) {
        _container = root;

        if (options && (options.skill || options.autoStart)) {
            _phase = PHASE.SETTINGS;
        }

        if (_phase === PHASE.SETTINGS) {
            _container.innerHTML = `<div class="gd-loading">Loading…</div>`;
            await _load();
            await _loadWeakAreas();

            if (options && (options.skill || options.autoStart)) {
                if (options.skill) {
                    _activeTab = TAB.SKILL;
                    _selectedSkill = _canonicalSkill(options.skill);
                } else {
                    _activeTab = TAB.WEAK;
                    if (_weakCandidates.length) {
                        _checkedWeakSkills = new Set(_weakCandidates.map(c => c.skillId));
                    }
                }

                if (options.count) {
                    _questionCount = options.count;
                }

                await _startSession();
            } else {
                if (_weakCandidates.length === 0 && _getLearnedSkillIds().size === 0) {
                    _activeTab = TAB.SKILL;
                }
                await _renderSettings();
            }
        } else if (_phase === PHASE.SESSION) {
            _renderSession();
        } else {
            _renderResults();
        }
    }

    function stop() {
        _closeRuleModal();
        _creditRecycle();
        _phase = PHASE.SETTINGS;
    }

    return { render, stop };
})();
