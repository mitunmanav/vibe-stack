## What it does

`/freeze-plan` turns what you agreed in `/ask-me` into a short written plan and a run of **Playable Steps**. It does not interview you again: it writes down what is already settled, and only asks about the few gaps that slicing the work turns up.

A Playable Step is a thin slice of the app that ends in something you can open and click. Step 01 is the thinnest version that works from start to finish; each later step thickens it.

## When to reach for it

You start this by typing `/freeze-plan`; the agent won't run it on its own. Reach for it right after `/ask-me` ends, in the **same chat**, because it reads the conversation you just had. Clearing first throws away the reasons behind your answers.

## Before you start

A finished `/ask-me` in this chat.

## What you'll see before anything is saved

1. **The steps**, each with one sentence on what you'll be able to click.
2. **How each step is checked**, with a plain line on what the check catches and what your own click-through still has to judge.
3. **Choices made for you**, one line each, so you can flip any of them.

Nothing is written until you say yes. Tell it a step is too big, too small, or in the wrong order, and it redraws the run.

## Common questions

**Why not build everything at once?**
Because a small thing that works grows into a big thing that works, and a big thing built all at once rarely does. Each step ends in something you can try, so a wrong turn shows up after one step, not ten.

## It's working if

- Every step ends in something you can open and click.
- It didn't ask you again about things you already answered.
- Every rule you mentioned in the interview shows up in the plan.

## Where it fits

A **step on the main flow**, between [`/ask-me`](./ask-me.md) (which it reads) and [`/build-step`](./build-step.md) (which works from the step files it writes). It ends by telling you to type `/clear`, then `/build-step`. For the full map, type [`/what-next`](./what-next.md).
