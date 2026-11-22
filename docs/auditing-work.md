## What it does

`auditing-work` reviews every change before you see it. The agent that built something is the worst judge of it, so two fresh helpers, each starting with a clean slate, review the change from two sides that are kept apart:

| Side | The question |
| :--- | :--- |
| Safety & Standards | Is any secret key or private information exposed? Are there leftovers, checks that can't fail, or messy code? |
| Plan | Is everything in the plan built, nothing extra added, and every word on screen the one from your wordbook? |

The agent fixes what they find, and only asks you about a finding that needs your decision.

## When to reach for it

You never type this. [`/build-step`](./build-step.md), [`/repair`](./repair.md), [`/tidy-up`](./tidy-up.md), and [`/launch-check`](./launch-check.md) call it for you.

## Why two sides

A change can pass one and fail the other. Neat, careful code can build the wrong thing; the exactly-right feature can leak a key. Reviewing them apart stops one from hiding the other.

## It's working if

- The Demo Card has one plain line per side: what was found, and what was fixed.

## Where it fits

A **background skill** at the end of every build, repair, and tidy-up, after [checking-behavior](./checking-behavior.md) has proved the change works. For the full map, type [`/what-next`](./what-next.md).
