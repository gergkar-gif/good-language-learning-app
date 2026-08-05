// ============================================
// CONTENT LOADER — Renders Learn & Drills from JSON
// ============================================

const ContentLoader = {
    async init() {
        await this.loadLessons();
        await this.loadDrills();
    },

    async loadLessons() {
        const container = document.getElementById('learn');
        if (!container) return;

        try {
            const data = await this.loadJSON('content/lessons/manifest.json');
            const html = this.renderLearnTab(data.levels || []);
            // Replace everything after the section title
            const title = container.querySelector('h2.section-title');
            const subtitle = container.querySelector('p');
            container.innerHTML = '';
            if (title) container.appendChild(title);
            if (subtitle) container.appendChild(subtitle);
            container.insertAdjacentHTML('beforeend', html);
        } catch (e) {
            console.error('ContentLoader: failed to load lessons', e);
        }
    },

    renderLearnTab(levels) {
        return levels.map(level => this.renderLevel(level)).join('');
    },

    renderLevel(level) {
        const arrow = level.comingSoon ? '▶' : '▼';
        const display = level.comingSoon ? 'none' : 'block';
        const opacity = level.comingSoon ? 'opacity: 0.6;' : '';

        let html = '<div class="level-section" style="margin-bottom: 20px;">' +
            '<div onclick="toggleLevel(\'' + level.id + '\')" ' +
            'style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; background: ' + level.color + '; color: white; border-radius: 12px; cursor: pointer;">' +
                '<div>' +
                    '<h3 style="font-size: 18px; margin: 0;">' + this.escapeHtml(level.name) + ' (' + level.id.toUpperCase() + ')</h3>' +
                    '<p style="font-size: 13px; margin: 4px 0 0 0; opacity: 0.9;">' + this.escapeHtml(level.subtitle) + '</p>' +
                '</div>' +
                '<span id="' + level.id + '-arrow" style="font-size: 20px;">' + arrow + '</span>' +
            '</div>' +
            '<div id="' + level.id + '-lessons" style="display: ' + display + ';">';

        level.lessons.forEach(lesson => {
            const clickAttr = level.comingSoon ? '' : ' onclick="startLesson(\'' + lesson.id + '\')"';
            const cursor = level.comingSoon ? '' : 'cursor: pointer;';
            html += '<div class="card"' + clickAttr + ' style="' + cursor + opacity + '">' +
                '<h3>' + this.escapeHtml(lesson.emoji) + ' ' + this.escapeHtml(lesson.title) + '</h3>' +
                '<p>' + this.escapeHtml(lesson.description) + '</p>' +
                '<span class="level-badge">' + level.id.toUpperCase() + '</span>' +
            '</div>';
        });

        html += '</div></div>';
        return html;
    },

    async loadDrills() {
        const select = document.getElementById('tense-select');
        if (!select) return;

        try {
            const data = await this.loadJSON('content/drills/tenses.json');
            select.innerHTML = this.renderTenseOptions(data.groups || []);
        } catch (e) {
            console.error('ContentLoader: failed to load tenses', e);
        }
    },

    renderTenseOptions(groups) {
        return groups.map(group => {
            let html = '<optgroup label="' + this.escapeHtml(group.label) + '">';
            group.options.forEach(opt => {
                const selected = opt.value === 'indicativo.presente' ? ' selected' : '';
                html += '<option value="' + this.escapeHtml(opt.value) + '"' + selected + '>' +
                    this.escapeHtml(opt.label) + '</option>';
            });
            html += '</optgroup>';
            return html;
        }).join('');
    },

    async loadJSON(url) {
        const res = await fetch(url);
        if (!res.ok) throw new Error('HTTP ' + res.status + ': ' + url);
        return res.json();
    },

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
};

// Auto-init
(function() {
    function start() {
        if (window.ContentLoader) ContentLoader.init();
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
})();