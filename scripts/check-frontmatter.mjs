// Parses every SKILL.md's frontmatter with `yaml`, the parser the `skills`
// installer uses, so a skill that would be skipped on install fails here first.
import { readFileSync, readdirSync } from "node:fs";
import { join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { parseDocument } from "yaml";

const root = fileURLToPath(new URL("..", import.meta.url));
const failures = [];

for (const entry of readdirSync(join(root, "skills"), { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const file = join(root, "skills", entry.name, "SKILL.md");
  const where = relative(root, file);
  const match = readFileSync(file, "utf8").match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) {
    failures.push(`${where}: no frontmatter block`);
    continue;
  }
  const doc = parseDocument(match[1], { strict: true, uniqueKeys: true });
  if (doc.errors.length > 0) {
    failures.push(`${where}: ${doc.errors[0].message.split("\n")[0]}`);
    continue;
  }
  const data = doc.toJS();
  for (const key of ["name", "description"]) {
    if (typeof data?.[key] !== "string" || data[key].trim() === "") {
      failures.push(`${where}: missing \`${key}\``);
    }
  }
}

if (failures.length > 0) {
  console.error(failures.join("\n"));
  console.error(`\n${failures.length} SKILL.md frontmatter error(s). Quote any value containing ": ".`);
  process.exit(1);
}
console.log("All SKILL.md frontmatter parses.");
