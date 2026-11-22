## What it does

`/undo` takes your app back to an earlier **Save Point**. Before it does, it tells you exactly which steps and repairs going back will remove, and waits for your yes.

Your plan, your wordbook, and your decisions are kept: only the app changes. And the undo can itself be undone, because it goes back by saving a new version, never by throwing anything away.

## When to reach for it

You start this by typing `/undo`; the agent won't run it on its own. Reach for it when a change isn't what you wanted, or the app is in a mess you'd rather not untangle. Name a Save Point if you know it: `/undo before step 02`.

If something is broken and you want to keep the work around it, [`/repair`](./repair.md) fixes it instead.

## Where Save Points come from

| Taken by | Before |
| :--- | :--- |
| `/start-project` | Anything at all (the very start) |
| `/build-step` | Each step |
| `/repair` | Each repair |
| `/tidy-up` | Each tidy-up |

## Common questions

**Will I lose my plan?**
No. Everything in `.vibe/` stays. Steps built after the Save Point are marked as not done, so `/build-step` can build them again.

**I undid the wrong thing.**
Type `/undo` again and pick the Save Point from just before the undo.

## It's working if

- You're told exactly what going back removes before you confirm.
- The app opens as it was at that Save Point.

## Where it fits

A **standalone safety net** you can use any time. After it, [`/build-step`](./build-step.md) tries the step again, or [`/ask-me`](./ask-me.md) rethinks it. For the full map, type [`/what-next`](./what-next.md).
