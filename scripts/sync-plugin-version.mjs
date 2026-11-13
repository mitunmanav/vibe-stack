import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const pkg = JSON.parse(fs.readFileSync(path.join(root, "package.json"), "utf8"));
const targets = [
  path.join(root, ".claude-plugin", "plugin.json"),
  path.join(root, ".codex-plugin", "plugin.json")
];

const checkOnly = process.argv.includes("--check");
for (const target of targets) {
  if (!fs.existsSync(target)) continue;
  const data = JSON.parse(fs.readFileSync(target, "utf8"));
  if (checkOnly) {
    if (data.version !== pkg.version) {
      console.error(`Version mismatch in ${target}: ${data.version} != ${pkg.version}`);
      process.exit(1);
    }
  } else {
    data.version = pkg.version;
    fs.writeFileSync(target, JSON.stringify(data, null, 2) + "\n");
  }
}
console.log(checkOnly ? "All plugin versions match." : `Synced plugin versions to ${pkg.version}.`);
