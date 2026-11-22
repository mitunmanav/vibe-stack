# Scope

Vibe Stack is curated. Ideas are welcome, and each one is judged against the bar below. Issues are for tracking changes to the skills.

## The bar

A change, or an issue asking for one, stays open only if it clears **both** parts:

1. **Observed failure.** It fixes something that went wrong in a real session: a person who does not read code got confused, saw code jargon, lost work, or ended up with a broken app. Say what you typed, what the command did, and what you expected. "It would be nicer if" does not clear this part.
2. **No technical burden on the human.** It never asks the human to read source code, run a terminal command, configure an outside tool by hand, or settle a git conflict. And it does not match anything in [`.out-of-scope/`](./.out-of-scope/).

Size is irrelevant: a one-word fix and a rewrite face the same bar. Reactions and +1 comments do not count towards it.

## By kind

- **User commands and background skills**: the bar above.
- **New commands**: if the behaviour composes from the existing commands, it does not get a new one. See [`new-commands.md`](./.out-of-scope/new-commands.md).
- **Beta commands** (`/tidy-up`, `/look-back`): marked "Beta." in their description and the README, and promoted once a real person who does not read code has run them.

Every change is recorded in [`CHANGELOG.md`](./CHANGELOG.md) with the failure that caused it.

## Already decided

Each file in [`.out-of-scope/`](./.out-of-scope/) records one rejected idea and why. Read them before filing:

- [`native-question-tool.md`](./.out-of-scope/native-question-tool.md)
- [`new-commands.md`](./.out-of-scope/new-commands.md)
- [`no-auto-chaining-phases.md`](./.out-of-scope/no-auto-chaining-phases.md)
- [`no-code-jargon-in-gates.md`](./.out-of-scope/no-code-jargon-in-gates.md)
- [`no-parallel-worktrees.md`](./.out-of-scope/no-parallel-worktrees.md)
- [`no-question-caps.md`](./.out-of-scope/no-question-caps.md)

## Unclear issues

An issue that cannot be judged against the bar gets one round of questions and the `needs-info` label. With no reply in 14 days, it is closed. Rejections close as "not planned".
