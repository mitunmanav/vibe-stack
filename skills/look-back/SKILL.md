---
name: look-back
description: "Beta. After a step or repair that went badly, find what would have prevented the trouble and offer changes so it does not happen again."
argument-hint: "[optional: what went badly]"
disable-model-invocation: true
---

# Look Back

A retrospective on the work just done. It changes the agent's **environment** (checks, guardrails, standing instructions), never the app's features, so the next step starts from a better place.

If `.vibe/config.md` is missing, tell the user to type `/start-project` first, and stop.

## 1. Read what happened

Use primary sources. In the chat where the trouble happened, that is this conversation. In a fresh chat, read `git log` since the Save Point before the trouble, the step files, entries marked `SUPERSEDED` in `.vibe/DECISIONS.md`, and repair commit messages (each states a cause). If the user typed something after the command, start there.

List every point where work was redone, a check failed late, the user said "that's not what I meant", or the agent searched a long time for something.

## 2. Give each trouble one home

- **A mechanical slip** (a fixed pattern a machine can spot): a deterministic guardrail. Add an Automated Check, a lint rule inside the check command, or a pattern in `.vibe/hooks/pre-commit`. Reach for this first; a guardrail holds on every run and prose does not.
- **A wrong guess about what the user wanted**: a rule in the plan's "Rules That Always Hold", or a word in `.vibe/WORDS.md`.
- **A judgement call about how code is written** that review missed: one line in `.vibe/STANDARDS.md`, which the review reads. Create the file the first time.
- **A fact the agent could not see** (server output, a browser error): a change that exposes it, such as the start command writing its output to a log file.
- **How the agent works or talks with the user**: one line in the project's agent instructions file (`AGENTS.md` or `CLAUDE.md`, whichever exists). Check whether an old line there can go at the same time.

Done when every trouble has a proposed home, or is marked "no change would have prevented this".

## 3. Offer the changes

Present the proposals most severe first, as one round of numbered questions in plain words, each worded so "yes" accepts it. Say what trouble it prevents, not how it is built.

Apply only what the user accepts. For a new check, call the Skill tool with "checking-behavior" and write it red-green. Run the check command, then commit ("Look back: <what changed>").

Tell the user in one plain sentence what will now be caught earlier, and the command to type next.
