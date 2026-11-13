# Skill Invocation Rules

Every skill is one of two kinds:

* **User command** (`start-project`, `ask-me`, `freeze-plan`, `build-step`, `repair`, `launch-check`, `plain-english`, `undo`, and the beta commands `tidy-up`, `look-back`): runs only when the human types `/command-name`. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The description is a one-line summary for a person scanning the slash menu, with no trigger list.
* **Background skill** (`clarifying`, `showing-options`, `checking-behavior`, `auditing-work`): reached by the agent, or called by a user command. Set `user-invocable: false` in `SKILL.md` so the human's menu shows only the user commands, and leave the `policy` block out of `agents/openai.yaml` (implicit invocation is the default). The description is model-facing: what it is, then `Use when ...` with one trigger per real branch.

## Calling one skill from another

Write the call as an instruction to use the tool: `Call the Skill tool with "clarifying".` A bare mention of a skill name is easy for the model to read past. One skill per call; two skills means two calls.

Only background skills can be called this way. No skill can reach a user command. When the next step is a user command, tell the human in plain words which `/command` to type.
