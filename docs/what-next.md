## What it does

`/what-next` tells you where your project stands and the **one** command to type next, including whether to type `/clear` first. It works that out from the project itself (the plan, which steps are done, anything left half-built), not from your memory.

You don't have to remember every command. This is the one to remember.

## When to reach for it

You start this by typing `/what-next`; the agent won't run it on its own. Reach for it any time you're unsure, and always when you come back after a break. Add what you're trying to do after the command if you know it: `/what-next I want to add a price list`.

If a message didn't make sense, type [`/plain-english`](./plain-english.md) instead.

## The map it reads

| You want to | Type |
| :--- | :--- |
| Set up a new project | `/start-project` |
| Shape an idea or a change | `/ask-me` |
| Write down what you agreed | `/freeze-plan` (same chat) |
| Build the next piece | `/build-step` (fresh chat) |
| Fix something broken | `/repair` |
| Go back to before a change | `/undo` |
| Check before sharing | `/launch-check` |

## Same chat or fresh chat

Some commands need the chat that came before them: `/freeze-plan` reads your interview, `/look-back` reads what went wrong. Others work best fresh, because everything they need is already saved in `.vibe/`. `/what-next` tells you which, every time.

## Common questions

**Where did "where am I" go from `/plain-english`?**
It moved here in 1.1.0. `/plain-english` now only re-explains the last message; `/what-next` is where you ask what to do.

## It's working if

- You get exactly one command to type.
- It says whether to type `/clear` first, and why.

## Where it fits

A **standalone you can use any time**. It's the map over every other command, so each docs page points back here.
