## What it does

`/plain-english` makes the agent say its last message again for someone who doesn't read code: the bit of context you were missing first, then the point, in a few short everyday sentences. It uses your project's own words, points at things on your screen, and gives an example from your own app.

If the message rested on a choice the agent made for you, it tells you in one line, so you can change it.

## When to reach for it

You start this by typing `/plain-english`; the agent won't run it on its own. Reach for it the moment a message doesn't land, in the middle of any other command. Add the part that lost you if you know it: `/plain-english what's a seam?`

To find out what to type next instead, use [`/what-next`](./what-next.md).

## Common questions

**Can I use it in the middle of `/ask-me` or `/build-step`?**
Yes. That's the main place it's for. The other command carries on afterwards.

**It keeps happening. Can I stop the jargon at the source?**
Partly. The wordbook built during [`/ask-me`](./ask-me.md) gives the agent your words to use, which cuts most of it. If one kind of jargon keeps coming back, [`/look-back`](./look-back.md) can turn "talk to me like this" into a standing instruction.

## It's working if

- The second explanation is shorter and clearer than the first.
- It names something you can see on your screen.

## Where it fits

A **standalone you can use any time**, from inside any other command. For the full map, type [`/what-next`](./what-next.md).
