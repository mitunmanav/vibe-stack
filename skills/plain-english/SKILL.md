---
name: plain-english
description: "Lost, or the last message didn't make sense? Get it re-explained in everyday words, plus where you are and the one command to type next."
disable-model-invocation: true
---

# Plain English

The last message did not land, or the user does not know what to do next. Run the three steps in order.

## 1. Re-pitch

Say the last message again in three or four short sentences: the context the user was missing first, then the point. Write in Simplified Technical English. Use the words in `.vibe/WORDS.md` (if it exists), name things the user can see on screen, and give one concrete example from their own app. If the user typed something after the command, answer that first.

## 2. Check the assumption

Show the most recent `AGENT` entry from `.vibe/DECISIONS.md` that bears on the last message, in one plain line, and ask: *"Did I assume something wrong here? Tell me and I'll change it."* When no entry bears on it, skip this step.

## 3. Where you are, what to type next

Work out where the project stands from the project itself: whether `.vibe/` exists, which step files are `TODO` or `DONE`, and whether `git status` shows unsaved work from a step left half-built. Read `FLOW-MAP.md`, then tell the user in one sentence where they are and give the one command to type next, including whether to type `/clear` first.
