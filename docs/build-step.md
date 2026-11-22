## What it does

`/build-step` builds one Playable Step and hands you something to click through in 30 seconds. Before it changes anything, it takes a **Save Point**. It writes an automated check for the step and watches it **fail** first, then builds until it passes, which proves the check can actually catch a broken app. Two fresh helpers review the work. Then it opens a **Demo Card**: what's new, and three things to try.

It builds exactly one step, then stops and waits for you.

## When to reach for it

You start this by typing `/build-step`; the agent won't run it on its own. Reach for it once for each step in the plan, in a **fresh chat** each time (type `/clear` first). With no number, it builds the next step that isn't done; `/build-step 03` builds step 3.

## Before you start

A saved plan from [`/freeze-plan`](./freeze-plan.md).

## Why the check fails first

A check that has never failed might not be able to. Watching it fail on the missing feature, then pass once the feature is built, is the only way to know it is really looking. You can't read the code, so a check you can trust is your proof the app works.

The checks catch broken buttons, things that don't save, and private items shown to the wrong person. They can't judge whether it feels right. That's what your three clicks on the Demo Card are for.

## Common questions

**It's not what I meant. Now what?**
Say so on the Demo Card question. The agent asks what you expected, writes the lesson down where it'll be read next time, and rebuilds. Or type `/undo` to put the app back to just before this step.

**Why clear the chat between steps?**
Long chats make the agent less sharp. Each step file holds everything the builder needs, so a fresh chat loses nothing and keeps step five as careful as step one.

## It's working if

- A Demo Card opens with three things to try, and all three work.
- It tells you which step it's building before it starts.
- It ends by telling you to type `/clear`, then `/build-step`.

## Where it fits

A **step on the main flow**, repeated once per Playable Step. When every step is done, type [`/launch-check`](./launch-check.md). If something breaks along the way, [`/repair`](./repair.md); if you don't like a step, [`/undo`](./undo.md). For the full map, type [`/what-next`](./what-next.md).
