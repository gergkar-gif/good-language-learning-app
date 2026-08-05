const fs = require("fs");
const path = require("path");

const STORIES_DIR = path.join(__dirname, "..", "content", "stories");

const manifest = {
  generated: new Date().toISOString(),
  stories: []
};

// Find every subfolder inside content/stories
const folders = fs
  .readdirSync(STORIES_DIR, { withFileTypes: true })
  .filter(entry => entry.isDirectory())
  .map(entry => entry.name);

console.log(`Found ${folders.length} story folders.`);

for (const folder of folders) {

  const folderPath = path.join(STORIES_DIR, folder);

  const files = fs
    .readdirSync(folderPath)
    .filter(file => file.endsWith(".json"));

  console.log(`Scanning ${folder} (${files.length} files)...`);

  for (const file of files) {

    const filePath = path.join(folderPath, file);

    try {

      const story = JSON.parse(
        fs.readFileSync(filePath, "utf8")
      );

      manifest.stories.push({
        id: story.id,
        title: story.title,
        level: story.level,
        lesson: story.lesson,
        type: story.type || folder,
        source: folder,
        path: `${folder}/${file}`,
        estimatedMinutes: story.estimatedMinutes || null,
        characters: story.characters || [],
        location: story.location || null
      });

    } catch (err) {

      console.error(`❌ Failed to load ${folder}/${file}`);
      console.error(err.message);

    }

  }

}

// Sort by level, then lesson, then title
manifest.stories.sort((a, b) => {

  if (a.level !== b.level) {
    return a.level.localeCompare(b.level);
  }

  if ((a.lesson || 0) !== (b.lesson || 0)) {
    return (a.lesson || 0) - (b.lesson || 0);
  }

  return a.title.localeCompare(b.title);

});

// Write manifest
const manifestPath = path.join(STORIES_DIR, "manifest.json");

fs.writeFileSync(
  manifestPath,
  JSON.stringify(manifest, null, 2),
  "utf8"
);

console.log("");
console.log("=================================");
console.log(`✅ Manifest created successfully.`);
console.log(`📚 ${manifest.stories.length} stories indexed.`);
console.log(`📄 ${manifestPath}`);
console.log("=================================");