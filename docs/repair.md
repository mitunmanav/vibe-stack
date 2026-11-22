## What it does

`/repair` fixes one problem without breaking the rest of the app. Before it changes anything, it takes a **Save Point**, then builds a quick, repeatable way to make the problem happen on demand: a loop that goes **red** on exactly what you saw. Only then does it look for the cause.

Guessing at fixes is how agents break three things while fixing one. With a loop that shows the problem, the cause falls out, and the same loop proves the fix worked.

## When to reach for it

You start this by typing `/repair` and what you saw: `/repair the Save button does nothing`. The agent won't run it on its own. Reach for it whenever something is broken, wrong, or slow. If you just don't like a change, [`/undo`](./undo.md) is quicker.

## How it works

1. **Make it happen on demand.** It drives the app to the problem with a check it can rerun in seconds. If the problem is new, it can try older Save Points to find which change brought it in.
2. **Shrink it.** It cuts the scenario down until every remaining piece matters.
3. **Theories, one at a time.** It shows you its ranked guesses in plain words (you may know something that reorders them), then tests each one by changing one thing.
4. **Fix it so it stays fixed.** It turns the problem into a lasting automated check, so the same problem can't quietly come back.

## Common questions

**It asked me for a screen recording. Why?**
Some problems only show up on one device or under a real hand. When it can't make the problem happen itself, it stops and asks for the one thing that would help, rather than guess.

**I pasted an error with a key in it.**
It replaces every key, password, and personal detail with `<REDACTED>` before quoting anything. Still, treat a key pasted into chat as exposed and get a new one.

## It's working if

- It makes the problem happen before it changes anything.
- It tells you in one sentence what was wrong, and gives you two things to click to see it fixed.

## Where it fits

An **on-ramp** to the main flow: reach for it any time, then carry on where you were. If repairs keep finding the same kind of slip, [`/look-back`](./look-back.md) turns it into a guardrail. For the full map, type [`/what-next`](./what-next.md).
