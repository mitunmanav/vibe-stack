---
name: look-back
description: "Beta. After a step or repair that went badly, find what would have prevented it and offer changes so it doesn't happen again."
argument-hint: "[optional: what went badly]"
disable-model-invocation: true
---

# Look Back

A **retrospective** on the work just done. It improves the agent's **environment** (checks, guardrails, standards, standing instructions), never the app's features, so the next step starts from a better place.

If `.vibe/config.md` is missing, tell the user to type `/start-project` first, and stop.

## 1. Read what happened

Use primary sources. In the chat where the trouble happened, that is this conversation. In a fresh chat, read `git log` since the Save Point before the trouble, the step files, `SUPERSEDED` entries in `.vibe/DECISIONS.md`, and repair commit messages (each states a cause). If the user typed something after the command, start there.

List every point where work was redone, a check failed late, the user said "that's not what I meant", the agent searched a long time for something, or the agent could not see what went wrong.

## 2. Give each trouble one home

Building and reviewing are separate jobs. The builder carries the heaviest load (finding its way, writing code, chasing failures); the reviewer gets only a diff. So rules about how code is written belong with the reviewer, and the builder's standing instructions stay short.

- **A mechanical slip** (a fixed pattern a machine can spot): a deterministic **guardrail**. Add an Automated Check, a lint rule inside the check command, or a pattern in `.vibe/hooks/pre-commit`. Reach for this first: a guardrail holds on every run, and prose does not. A check command that skips the linter or type checker, or a guardrail that is silently broken, is itself the finding.
- **A wrong guess about what the user wanted**: a rule in the plan's "Rules That Always Hold", or a word settled through the Skill tool with "keeping-words".
- **A judgement call about how code is written** that review missed: one line in `.vibe/STANDARDS.md`, which only the reviewer reads. Create it the first time.
- **A fact the agent could not see** (server output, a browser error): a change that exposes it, such as the start command writing its output to a log file the agent can read.
- **A long search for the right file**: a one-line pointer in the project's agent instructions file (`AGENTS.md` or `CLAUDE.md`, whichever exists), naming where that thing lives.
- **How the agent works or talks with the user**: one line in that same file.

Every line you propose for the instructions file must change what the agent would do by default, and say the behaviour wanted rather than the one to avoid. While you are there, list any old line that no longer changes anything, to remove.

Done when every trouble has a proposed home, or is marked "no change would have prevented this".

## 3. Offer the changes

Present the proposals most severe first, as one round of numbered questions in plain words, each worded so "yes" accepts it. Say what trouble it prevents, not how it is built.

Apply only what the user accepts. For a new check, call the Skill tool with "checking-behavior" and write it red-green. Run the check command, then commit ("Look back: <what changed>").

Tell the user in one plain sentence what will now be caught earlier, and the command to type next.
