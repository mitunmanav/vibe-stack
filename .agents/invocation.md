# Skill Invocation Rules

* **User commands** (`disable-model-invocation: true` in `SKILL.md`, `allow_implicit_invocation: false` in `agents/openai.yaml`): Only run when the human explicitly types `/command-name`.
* **Background capabilities** (`user-invocable: false` in `SKILL.md`, `allow_implicit_invocation: true` in `agents/openai.yaml`): Hidden from the human slash menu; loaded automatically by the agent or called from a user command via `Call the Skill tool with "<capability-name>"`.
* **Hard boundary:** No skill may ever call a user command via the `Skill` tool. When a user command is needed next, tell the human in plain English which `/command` to type.
