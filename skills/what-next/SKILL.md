---
name: what-next
description: "Not sure which command to type? See where your project is, and the one command to type next."
argument-hint: "[optional: what you are trying to do]"
disable-model-invocation: true
---

# What Next

Nobody remembers every command, so the user asks. Answer with where they are and the **one** command to type next, including whether to type `/clear` first.

Before stating what a command does, or telling the user a step can be skipped, read that command's `SKILL.md`: the summaries below are for orientation only.

## 1. Read where the project stands

Work it out from the project itself, never from the user's memory: whether `.vibe/` exists, which step files are `TODO` or `DONE`, whether `git status` shows unsaved work from a step left half-built, and what this chat has already done. If the user typed something after the command, that is what they are trying to do; route that.

## 2. Find their place on the map

A **flow** is a path through the commands. Most work travels one **main flow**, a few **on-ramps** join it, and the rest is upkeep or standalone.

**The main flow: idea → app you can share.**

1. **`/start-project`** once per project: the precondition for everything else.
2. **`/ask-me`** shapes the idea by interview, deciding the technical details itself. Clickable previews happen inside it when a choice is easier to see than describe.
3. **`/freeze-plan`** turns the agreed idea into a plan and a run of Playable Steps. It reads the interview, so it runs in the **same** chat.
4. **`/build-step`** once per step, each in a **fresh** chat (`/clear` first): the step file carries everything the builder needs.
5. **`/launch-check`** before the app reaches anyone else.

**On-ramps.**

- **Something is broken or acting weird** → **`/repair <what you saw>`**. It makes the problem happen on demand before touching anything, then fixes it with a check that keeps it fixed.
- **The last change is not what you wanted** → **`/undo`**. It shows exactly what going back removes, and the undo can itself be undone.
- **A new idea, or a change to a finished plan** → back to **`/ask-me`**. Parked ideas wait in `.vibe/LATER.md`.

**Upkeep (beta).**

- **`/look-back`** after a step or repair that went badly, in the same chat, so it can read what happened. It changes the checks and guardrails, never the app.
- **`/tidy-up`** once several steps are built, so the app stays easy to change. Nothing on screen changes.

**Standalone.**

- **`/plain-english`** the moment a message does not land. It re-explains in everyday words, from inside any other command.
- **`/what-next`** (this one), any time, and always after a break.

Read `FLOW-MAP.md` for the exact row that matches the project's state.

## 3. Fresh chat or same chat

The gap between two commands is the only place to decide whether to keep this chat or start fresh. Read `NEW-CHAT.md` whenever the answer is not plain from the flow map.

## 4. Answer

Tell the user in one plain sentence where they are, then the one command to type next, and whether to type `/clear` first. Done when they have exactly one command to type.
