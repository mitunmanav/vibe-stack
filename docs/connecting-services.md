## What it does

`connecting-services` walks you through the steps only you can take with an outside service: making an account, clicking through a payment or email provider's dashboard, copying a secret key. It turns them into short numbered stages, tells you exactly which page to open and what to click, and checks each stage worked before the next.

You only click in the dashboard and paste keys into one file. The agent does everything else.

## When to reach for it

You never type this. The agent reaches for it the moment the app needs a key or account it can't get itself, usually during [`/build-step`](./build-step.md) or [`/launch-check`](./launch-check.md).

## Keys go in the file, never the chat

A key pasted into chat has to be treated as exposed and replaced. So every stage ends with you pasting into `.env.local`, a file that is never saved into the project's history, and the agent checking it's filled in without ever printing it.

Anything that could cost money starts in test mode or the free tier, and is marked as a **one-way door** before you switch it on.

## It's working if

- Each stage is one task, with the exact page and buttons named.
- After each stage, you're told in one sentence whether the connection works.

## Where it fits

A **background skill** for the walls only a person can pass. For the full map, type [`/what-next`](./what-next.md).
