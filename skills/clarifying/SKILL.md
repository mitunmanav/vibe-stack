---
name: clarifying
description: "Plain-words interview that turns a rough app idea into a shared picture, deciding technical details itself and asking only about what people see, do, and pay for. Use when shaping an idea, settling an unclear request, or planning a feature."
user-invocable: false
---

# Clarifying

Interview the user until you both hold the same picture of what they want. Map the idea as a **design tree**: each decision opens the decisions that hang off it. This is conversation only; the app code waits until the plan is frozen.

## Before the first round

Read `.vibe/DECISIONS.md`, and `.vibe/WORDS.md` if it exists. `USER` entries newer than the newest plan in `.vibe/specs/` are an interview that was left unfinished: say in a few plain bullets what is already settled, and carry on from there.

When the idea is too big for one chat to settle (several kinds of people, several separate jobs), the first round asks which one thing must work first. Shape only that. Write each parked part as one plain line in `.vibe/LATER.md`, and tell the user it is waiting there for a later `/ask-me`.

Looking up facts is your work, not the user's. When a question needs a fact from the project or the outside world (how the app stores things today, what a service costs, whether it has a free tier), start a helper in a fresh context window and have it look. Keep going while it works: only the questions that depend on its answer wait for it.

## Sort every open decision

Before any decision reaches the user or gets settled by you, call the Skill tool with "translating". It sorts the decision into a build choice (you settle and log it), a taste question (what people see, click, type, or experience), or a one-way door (money, private information, outside accounts, saved data, anything hard to undo), and it says how to word and log each one.

When only someone else can answer (a client, a partner, a friend), "translating" also has the sheet to send them.

## Work the tree in rounds

The **frontier** is every taste question and one-way door whose prerequisites are settled. Ask the whole frontier in one round, numbered, each with your recommended answer, worded so that "yes" accepts it:

```markdown
❓ **Q1** - **<short everyday title>**: <the question, with the choices if there are any>
➡️ <your recommended answer and a one-line reason>

---
```

A question that depends on another question still open in this round waits for a later round. Close each round with the line `Choices I made for you this round:` and the build choices you settled. After each reply, recompute the frontier, including any decisions a change has reopened, and ask the next round.

While the user answers:

- After each round, log every answer as "translating" describes, so closing the chat loses nothing.
- Test the edges with small stories from the user's own world ("Sam books the 3pm slot, then Priya tries to book it too. What should Priya see?"). Stories surface the rules a description skips.
- When the user uses a word that clashes with `.vibe/WORDS.md`, or one word for two things, point it out and ask which they mean.
- When a word for a screen, a person, or a thing is settled, write it into `.vibe/WORDS.md` right then, creating the file the first time, in the shape "translating" gives.

## Done when

The frontier is empty: every branch visited, nothing silently assumed. Summarise the agreed idea in a few plain bullets, ask the user to confirm it matches what they pictured, and tell them to type `/freeze-plan` in this same chat.
