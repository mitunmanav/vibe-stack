## What it does

`checking-behavior` holds the rules for the automated checks that prove your app works. Each check uses the app the way a person would (open a page, click, read the screen) and is watched **failing** before the feature exists, then **passing** once it's built. A check that has never failed might not be able to catch anything.

## When to reach for it

You never type this. [`/build-step`](./build-step.md), [`/repair`](./repair.md), [`/tidy-up`](./tidy-up.md), and [`/look-back`](./look-back.md) call it whenever they write a check.

## What makes a check worth trusting

- It goes through the real page, so it survives any rewrite of the code behind it.
- Its expected answer comes from your plan ("2 slots at $15 shows $30"), never from the code it's checking.
- Its example is picked so a slightly wrong rule would give a different answer.
- It only fakes what the project doesn't own: payment providers, email senders, the clock.

## It's working if

- Each Demo Card lists every check as seen failing before the build and passing after.
- Every check has a plain line on what it catches and what it misses.

## Where it fits

A **background skill** underneath every command that builds or fixes. Its partner is [auditing-work](./auditing-work.md), which reviews the result. For the full map, type [`/what-next`](./what-next.md).
