---
name: ask-me
description: "Turn a rough idea into a clear, shared plan through rounds of plain-English questions, where replying 'yes' accepts the recommended answer."
argument-hint: "[what you want to build or change]"
disable-model-invocation: true
---

If `.vibe/config.md` is missing, tell the user to type `/start-project` first, and stop.

Otherwise, call the Skill tool with "clarifying", taking whatever the user typed after the command as the idea to shape.
