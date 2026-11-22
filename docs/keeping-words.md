## What it does

`keeping-words` keeps your project's shared language sharp. As you talk, it writes the words for your screens, people, and things into a **wordbook** (`.vibe/WORDS.md`), points out when one word is doing two jobs, and tests rules with small stories from your own world ("Sam books 3pm, then Priya tries to book it too. What should Priya see?").

It also keeps the **decision log** (`.vibe/DECISIONS.md`): every answer you give, plus only those choices the agent made that would surprise you later and take real work to change.

## When to reach for it

You never type this. [`/ask-me`](./ask-me.md) calls it alongside the interview, and other commands call it when a choice changes or a word needs settling.

## Why shared words matter

When you, the screens, and the agent all say **Booking** for the same thing, messages get shorter, buttons get clearer, and the code is named the same way, so later changes land in the right place. Most of the jargon in an agent's replies disappears once it has your words to use.

## Common questions

**Can I change a decision later?**
Yes. Say so in chat ("change D-02 so it works on phones too"). The old entry is marked as replaced, never deleted, and you're told what will change on screen.

## It's working if

- It catches you using two words for one thing, and asks which you mean.
- The words in chat match the words on the buttons.

## Where it fits

A **background skill** that runs underneath [`/ask-me`](./ask-me.md), next to [clarifying](./clarifying.md). For the full map, type [`/what-next`](./what-next.md).
