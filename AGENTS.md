# Instructions for Agents Maintaining Vibe Stack

1. **Audience rule:** Every message, question, and document shown to the human must be written in plain everyday English. Never ask a user to read source code, database schemas, or test files.
2. **Flat skill layout:** All skills live one level deep at `skills/<skill-name>/SKILL.md` so Claude Code, OpenAI Codex, GitHub Copilot, Gemini CLI, Cursor, and `npx skills` discover them automatically.
3. **Invocation rule:** User commands (`start-project`, `ask-me`, `freeze-plan`, `build-step`, `repair`, `launch-check`, `plain-english`, `undo`) set `disable-model-invocation: true` in `SKILL.md` and `allow_implicit_invocation: false` in `agents/openai.yaml`. Background capabilities (`clarifying`, `showing-options`, `checking-behavior`, `auditing-work`) set `user-invocable: false`. A skill must never invoke a user command via the `Skill` tool.
4. **Punctuation rule:** Never use em-dashes or en-dashes in any file in this repository. Use colons, parentheses, or spaced hyphens (` - `) instead.
5. **Validation gate:** Run `python3 scripts/validate-plugin.py` after any edit and ensure all checks pass.
