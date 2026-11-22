## What it does

`/launch-check` looks for anything that would hurt you once other people use the app: a secret key anyone could find, one person's details visible to another, or an action that can't be taken back. It looks at the whole app, and at the project's full history, because a key that was ever saved counts as exposed even if it was deleted later.

You get a page with four green or red badges, not a wall of text.

## When to reach for it

You start this by typing `/launch-check`; the agent won't run it on its own. Reach for it before the app reaches anyone else: before you share a link, publish it, or connect real payments or email.

## The four badges

| Badge | What it checks |
| :--- | :--- |
| Secret keys protected | No key in any file, now or in the project's history |
| Private information locked down | Visiting as a stranger and as a second person shows only what they're allowed to see |
| All automated checks passing | Every check from every step still passes |
| One-way doors | Anything launching would do that can't be taken back: charging cards, sending emails, deleting data |

A red badge stops the launch with a plain `⚠️ Why this matters` line and an offer to fix it.

## Common questions

**A key was found in the history. Is deleting it enough?**
No. Once a key has been saved anywhere it could be shared, treat it as exposed: get a new key from the service and replace the old one. The agent walks you through both.

**I need live payments or real email to launch.**
The agent writes a click-by-click guide for connecting them, and checks each stage as you go. You only click in the service's dashboard and paste keys into one file, never into chat.

## It's working if

- You see a page of four badges.
- Every red badge comes with one plain sentence on what would happen in the real world.

## Where it fits

The **last step on the main flow**, after every [`/build-step`](./build-step.md) is done. If a badge is red because something is broken, [`/repair`](./repair.md) fixes it. For the full map, type [`/what-next`](./what-next.md).
