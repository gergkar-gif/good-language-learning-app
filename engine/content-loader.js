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
        return this.json(`content/${name}/manifest.json`);
    },

    async story(path) {
        return this.json(`content/stories/${path}`);
    },

    async lesson(id) {
        return this.json(`content/lessons/${id}.json`);
    },

    async verb(name) {
        return this.json(`imports/verbs/${name}.json`);
    },

    clearCache() {
        this.cache = {};
    }

};