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
        // Path remains the same (imports/verbs/ is unchanged)
        return this.json(`imports/verbs/${name}.json`);
    },

    clearCache() {
        this.cache = {};
    }

};