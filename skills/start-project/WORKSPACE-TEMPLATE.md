# Workspace Initialization Templates (`WORKSPACE-TEMPLATE.md`)

1. **`.vibe/config.md`:**
   ```markdown
   # Project Workspace Configuration
   * **Project summary:** <2-sentence plain summary>
   * **Start command:** `<command to run app locally>`
   * **Check command:** `<command to run automated checks>`
   * **Plans & steps:** `.vibe/specs/` and `.vibe/steps/`
   * **Wordbook & decisions:** `.vibe/WORDS.md` and `.vibe/DECISIONS.md`
   * **Browser previews:** `.vibe/previews/`
   ```
2. **`CLAUDE.md` pointer block (and symlink `AGENTS.md -> CLAUDE.md`):**
   ```markdown
   ## Vibe Stack Workspace
   Before starting any task, read `.vibe/config.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md` (and `.vibe/handoff.md` if present).
   Use plain everyday English with the user. Never ask the human to read source code, database schemas, or test files.
   ```
3. Seed `.vibe/WORDS.md` with the initial everyday nouns from the user's description, and record `[D-01]` (the local tech stack choice and why) in `.vibe/DECISIONS.md`.
