---
name: clarifying
description: "Relentless plain-words interview that turns a rough app idea into a shared picture. Use when shaping an idea, settling an unclear request, or planning a change."
user-invocable: false
---

# Clarifying

Interview the user relentlessly until you both hold the same picture of what they want. Map the idea as a **design tree**: every decision opens the decisions that hang off it. This is conversation only; the app code waits until the plan is frozen.

## Before the first round

Read `.vibe/DECISIONS.md`. `USER` entries newer than the newest plan in `.vibe/specs/` are an interview left unfinished: say in a few plain bullets what is already settled, and carry on from there.

When the idea is too big for one chat (several kinds of people, several separate jobs), the first round asks which one thing must work first. Shape only that. Park each other part as one plain line in `.vibe/LATER.md`, and tell the user it waits there for a later `/ask-me`.

## Sort every open decision

Each open decision goes to exactly one place:

- **Technical two-way door**: how the app is built (file layout, where data is kept, libraries, test setup), and easy to change later without losing anyone's data or money. Decide it yourself with the simplest reliable option.
- **Taste question**: what people see, click, type, or experience. Ask the user. Read `QUESTION-GUIDE.md` when you word one.
- **One-way door**: costs money, exposes private information, needs an outside account, or deletes saved data. Ask the user, open with a `⚠️ **Why this matters:**` line stating the real-world result, and wait for an explicit yes.

When a question is easier to see than to describe (a screen layout, how something changes over time), call the Skill tool with "showing-options" and ask it as a clickable preview.

When only someone else can answer (a client, a partner, a friend), read `QUESTION-GUIDE.md` for the sheet to send them.

## Work the tree in rounds

The **frontier** is every taste question and one-way door whose prerequisites are settled: the ones you can ask now without guessing at answers you have not heard. Ask the whole frontier in one round, numbered, each with your recommended answer, worded so that "yes" accepts it:

```markdown
❓ **Q1** - **<short everyday title>**: <the question, with the choices if there are any>

➡️ <your recommended answer and a one-line reason>

---

❓ **Q2** - ...
```

A question that hangs on another question still open in this round belongs to a later round. Each reply reshapes the tree: settled answers push the frontier outward. Recompute it and ask the next round.

Finding facts is your work; decisions are the user's. When a question needs a fact from the project or the outside world (how the app stores things today, what a service costs, whether it has a free tier), start a helper in a fresh context window and let it find the answer. Keep asking while it works: only the questions downstream of its answer wait.

## Done when

The frontier is empty: every branch visited, nothing silently assumed. Summarise the agreed idea in a few plain bullets and ask the user to confirm it matches what they pictured. Act on nothing until they do; then tell them to type `/freeze-plan` in this same chat.
