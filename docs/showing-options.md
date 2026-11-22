## What it does

`showing-options` answers a question by letting you click instead of imagine. It builds a **preview**: one throwaway page in `.vibe/previews/` that opens by double-click, with no install and no internet. Your real app is never touched.

## When to reach for it

You never type this. The agent reaches for it during [`/ask-me`](./ask-me.md) whenever a choice is easier to see than describe. You can always ask for one: "show me some options".

## Two kinds of preview

| The question | What you get |
| :--- | :--- |
| "What should this look like?" | Several really different layouts on one page, with arrows at the bottom to flip between them |
| "How should this behave as things happen?" | Buttons that act out the rules (book, cancel, skip a week) and a panel showing what's true right now |

The best answer is often a mix: "the top of B with the list from C". That mix is the design you actually want.

## It's working if

- The options differ in layout, not just colour.
- The question it's answering is written at the top of the page.
- Your pick shows up in the decision log with the reason you gave.

## Where it fits

A **background skill** used inside [`/ask-me`](./ask-me.md). Only the chosen direction is built into the real app, later, by [`/build-step`](./build-step.md). For the full map, type [`/what-next`](./what-next.md).
