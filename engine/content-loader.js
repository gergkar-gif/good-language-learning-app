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
        // Updated to include language prefix
        return this.json(`content/es/${name}/manifest.json`);
    },

    async story(path) {
        // Updated to include language prefix and story category
        return this.json(`content/es/stories/${path}`);
    },

    async lesson(id) {
        // Updated to include language prefix
        return this.json(`content/es/lessons/${id}.json`);
    },

    async verb(name) {
        // Path remains the same (imports/verbs/ is unchanged)
        return this.json(`imports/verbs/${name}.json`);
    },

    clearCache() {
        this.cache = {};
    }

};