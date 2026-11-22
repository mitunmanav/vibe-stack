---
name: ask-me
description: "A relentless, plain-English interview that turns a rough idea into a shared plan, and keeps your project's words and decisions as it goes."
argument-hint: "[what you want to build or change]"
disable-model-invocation: true
---

If `.vibe/config.md` is missing, tell the user to type `/start-project` first, and stop.

Otherwise, call the Skill tool with "clarifying", then call it again with "keeping-words", taking whatever the user typed after the command as the idea to shape.
