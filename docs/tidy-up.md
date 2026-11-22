## What it does

`/tidy-up` (beta) keeps your app easy to change. It looks at the parts of the code that keep changing, finds the mess that builds up across steps, and tidies it behind the scenes. Nothing you see changes, and every automated check must pass before and after.

Each step is reviewed on its own, so mess that spreads across several steps goes unseen. This is the one place that looks at the whole app.

## When to reach for it

You start this by typing `/tidy-up`; the agent won't run it on its own. Reach for it once several steps are built, or when changes start taking longer than they used to. Type an area after the command to point it there: `/tidy-up the booking page`.

## Before you start

Every check must be passing. If one isn't, it tells you to type [`/repair`](./repair.md) first: tidying needs a green start to prove it broke nothing.

## Common questions

**Will it change how my app looks or works?**
No. Anything that would change what people see or what's saved is a new idea, so it lists those for you to take to [`/ask-me`](./ask-me.md) instead.

## It's working if

- It tells you every check passed before and after.
- Nothing on screen changed.
- The next change you ask for goes faster.

## Where it fits

**Upkeep**, run every few steps. It takes a Save Point first, so [`/undo`](./undo.md) takes the whole tidy-up back. For the full map, type [`/what-next`](./what-next.md).
