# Flat skills folder, two plugin manifests

Coding agents find skills in different ways. Claude Code reads `.claude-plugin/plugin.json`; Codex reads `.codex-plugin/plugin.json` and each skill's `agents/openai.yaml`; Gemini CLI and Copilot only find skills that sit one folder deep. So every skill lives flat at `skills/<name>/SKILL.md`, carries its own `agents/openai.yaml`, and both manifests list every skill folder by name.

We considered grouping skills into folders by kind (commands, background skills, beta), the way larger skill sets do. It would make the repo easier to scan, but it breaks discovery on the harnesses that look one level deep, and the set is small enough to scan flat. Beta commands ship with the rest, marked "Beta." in their description and the README, because the people who need them most are the ones least able to install a second route.

Both manifests list skills explicitly rather than pointing at `./skills`, so adding a folder never ships a skill by accident. `scripts/validate-plugin.py` fails when a manifest and the folder disagree.
