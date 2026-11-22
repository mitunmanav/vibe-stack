## What it does

`clarifying` is the interview underneath [`/ask-me`](./ask-me.md). It maps your idea as a tree of decisions and asks in **rounds**: each round is every question whose earlier answers are already settled, so it never asks something that depends on an answer it hasn't heard yet. Every question carries a recommended answer, worded so "yes" accepts it.

It sorts each open decision before asking: technical details it decides itself, questions about what people experience it asks you, and **one-way doors** (money, private information, outside accounts, deleting data) it asks with a plain warning and waits for an explicit yes.

## When to reach for it

You never type this. `/ask-me` calls it for you, and the agent reaches for it on its own when a request is too unclear to build safely.

## Facts are the agent's job

When a question needs a fact (what a service costs, how the app stores something today), the agent looks it up with a helper instead of asking you. Only the questions that depend on that fact wait; the rest of the round goes ahead.

## It's working if

- Questions arrive in a few numbered rounds, not one at a time forever.
- Nothing you're asked needs technical knowledge.
- It ends by summing up and asking whether that matches what you pictured.

## Where it fits

A **background skill** behind `/ask-me`, working alongside [keeping-words](./keeping-words.md), which writes down the words and decisions as they settle. For the full map, type [`/what-next`](./what-next.md).
