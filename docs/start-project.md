## What it does

`/start-project` sets up a folder once so every other command knows where things live. It creates a small `.vibe/` folder for your plan, your words, and your decisions, makes sure the app can start and check itself with one command each, and takes your first **Save Point**.

It does not shape your idea. It only checks a two-sentence summary with you, then gets out of the way. Shaping the idea is the job of [`/ask-me`](./ask-me.md).

## When to reach for it

You start this by typing `/start-project`; the agent won't run it on its own. Reach for it once per project, before anything else: in an empty folder, or in a folder that already holds an app. Add a sentence about your idea after the command if you like.

If the project is already set up, it says so and points you to [`/what-next`](./what-next.md).

## What it leaves behind

| Thing | What it's for |
| :--- | :--- |
| A tiny working app | Opens a page with your project's name, so there's something real from minute one |
| One automated check | Proves the app starts, so every later check has a place to live |
| `.vibe/config.md` | The one command that starts the app, and the one that checks it |
| `.vibe/DECISIONS.md` | The first choice made for you (how the app runs), in plain words |
| A commit guardrail | Stops a secret key from ever being saved into the project's history |
| The first Save Point | The very start, which [`/undo`](./undo.md) can always return to |

## Common questions

**Do I need to pick a programming language or set anything up first?**
No. In an empty folder, the agent picks the simplest reliable setup that runs on your computer for free, and writes down why. You can ask to change it later.

**Can I use it on an app I already have?**
Yes. It looks at the app first, finds how it starts, and adds a check if there isn't one. It doesn't rebuild what you have.

## It's working if

- It asks you exactly one question: whether its two-sentence summary matches your idea.
- The app opens in your browser at the end.
- It tells you to type `/ask-me` next.

## Where it fits

A **run-once setup**, the precondition for the whole main flow. Next comes [`/ask-me`](./ask-me.md), because the idea is shaped there. For the full map, type [`/what-next`](./what-next.md).
