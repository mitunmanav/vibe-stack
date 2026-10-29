# Decision 0001: Flat Skills Folder with Dual Plugin Manifests

* **Context:** Different coding agents discover skills differently. Claude Code reads `.claude-plugin/plugin.json` and scans `skills/<name>/SKILL.md`. OpenAI Codex reads `.codex-plugin/plugin.json` and `agents/openai.yaml`. Gemini CLI and VS Code Copilot require skills to sit one folder deep (`skills/<name>/SKILL.md`).
* **Decision:** Store all 12 skills flat under `skills/<name>/SKILL.md`, include `agents/openai.yaml` inside every skill folder, and ship both `.claude-plugin/` and `.codex-plugin/` manifests.
* **Consequences:** Every major agent discovers all 12 skills without nested-folder failures, while `user-invocable: false` hides background capabilities from the human slash menu.
