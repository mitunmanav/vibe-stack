# User commands and background skills

Every `SKILL.md` in this repo is a skill. The one axis that splits them is **invocation**: who can reach it.

* **User command** (`start-project`, `ask-me`, `freeze-plan`, `build-step`, `repair`, `launch-check`, `plain-english`, `what-next`, `undo`, and the beta commands `tidy-up`, `look-back`): runs only when the human types `/command-name`. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The description is **human-facing**: a one-line summary in plain words for a person scanning the slash menu, with no trigger list and no engineering words. A user command costs no context load, and spends cognitive load instead: the human has to remember it exists. That is why `/what-next` exists.
* **Background skill** (`clarifying`, `keeping-words`, `showing-options`, `checking-behavior`, `auditing-work`, `connecting-services`): reached by the agent, or called by a user command. Set `user-invocable: false` in `SKILL.md`, so the human's menu shows only the commands, and leave the `policy` block out of `agents/openai.yaml` (implicit invocation is the default). The description is **model-facing** and always loaded: what it is, then `Use when ...` with one trigger per real branch. The test for keeping a skill in the background: _could the agent usefully reach for this on its own, or does another skill need to call it?_

Each harness keeps a user command out of the agent's reach in its own way, so nothing but the human can fire it: no other skill can. Keep `SKILL.md` and `agents/openai.yaml` in step, so a skill is a user command in every harness or in none.

## Dependencies between them

Write a call as an instruction to use the tool: `Call the Skill tool with "clarifying".` A bare mention of a skill name is easy for the model to read past; naming the tool is what gets it fired. Leaving off the leading `/` keeps the call harness-neutral.

The Skill tool takes one skill per call. A step that needs two skills says so as two calls (`call the Skill tool with "clarifying", then call it again with "keeping-words"`), never one call with two names.

Only background skills can be called this way. When the next step is a user command, tell the human in plain words which `/command` to type. Router prose that names commands for the human to pick from (`what-next`, the README) is not a call, so it keeps `/command` names as labels.

Shared reference lives inside the background skill that owns it. Another skill reaches it by calling the Skill tool with that skill, never by a `../other-skill/FILE.md` path, which breaks once a harness copies skills into its own folders.

## Hard and soft dependencies on `/start-project`

A skill that cannot work without `.vibe/config.md` (it needs the start command, the check command, or the `.vibe/` folder to write into) opens with the one-line pointer: tell the user to type `/start-project` first, and stop. A skill that only reads `.vibe/` files to sharpen its words (`plain-english`, `what-next`) works without them and carries no pointer. [ADR 0003](./adr/0003-start-project-pointer-only-for-hard-dependencies.md) records why.

## Passive and active word work

Reading `.vibe/WORDS.md` to borrow its words is a one-line pointer any skill can carry. Only the active work (challenging a word, testing it with a story, writing the wordbook or a decision entry) calls the Skill tool with "keeping-words".
