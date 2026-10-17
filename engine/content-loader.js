// ============================================
// CONTENT LOADER
// ============================================

const Content = {

    cache: {},

    async json(path) {
        if (this.cache[path]) {
            return this.cache[path];
        }

        const response = await fetch(path);

        if (!response.ok) {
            throw new Error(`Failed to load ${path}`);
        }

        const data = await response.json();

        this.cache[path] = data;

        return data;
    },

    async manifest(name) {
        return this.json(Lang.content(`${name}/manifest.json`));
    },

    async story(path) {
        return this.json(Lang.content(`stories/${path}`));
    },

    async lesson(id) {
        return this.json(Lang.content(`lessons/${id}.json`));
    },

    async verb(name) {
        const lang = (typeof Lang !== 'undefined') ? Lang.code() : 'es';
        if (lang === 'fr' || (typeof lang === 'string' && lang.startsWith('fr-'))) {
            return this.json(`imports/verbs/fr/${name}.json`);
        }
        if (lang === 'it' || (typeof lang === 'string' && lang.startsWith('it-'))) {
            return this.json(`imports/verbs/it/${name}.json`);
        }
        return this.json(`imports/verbs/${name}.json`);
    },

    clearCache() {
        this.cache = {};
    }

};

if (typeof document !== 'undefined') {
    document.addEventListener('language-changed', () => {
        Content.clearCache();
    });
}