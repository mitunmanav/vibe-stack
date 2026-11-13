# Scope and Quality Bar for Vibe Stack

Every change to Vibe Stack must clear both parts of this bar:

1. **Observed failure.** It fixes something that went wrong in a real session: a non-technical user got confused, saw code jargon, lost work, or ended up with a broken app. "It would be nicer if" does not clear this part.
2. **No technical burden on the human.** It never asks the human to read source code, run a command, configure an external tool, or settle a git conflict.

If the behaviour can be composed from the existing commands, it does not get a new one.

A new command starts as **beta**: marked so in its description and the README, and promoted only after a real non-technical user has run it. Every change is recorded in [`CHANGELOG.md`](./CHANGELOG.md) with the failure that caused it.

## Already decided

Each file in [`.out-of-scope/`](./.out-of-scope/) records one rejected idea and why:

- [`no-auto-chaining-phases.md`](./.out-of-scope/no-auto-chaining-phases.md)
- [`no-code-jargon-in-gates.md`](./.out-of-scope/no-code-jargon-in-gates.md)
- [`no-parallel-worktrees.md`](./.out-of-scope/no-parallel-worktrees.md)
- [`no-question-caps.md`](./.out-of-scope/no-question-caps.md)
