# Learning From User Pushback (`LEARN-RULES.md`)

When the user tests a demo and says *"this isn't what I meant"*, follow these three steps:

1. **Flip the decision or step:** If an `[AGENT]` entry in `.vibe/DECISIONS.md` guessed wrong, mark it `SUPERSEDED` and write the user's choice as `[HUMAN OVERRULED]`.
2. **Prune and update `CLAUDE.md`:** If the mistake came from a recurring project preference (for example, *"Always show prices with tax included"*), propose a 1-line addition to `CLAUDE.md` - and check if any outdated or redundant line in `CLAUDE.md` can be deleted at the same time.
3. **Wait for `"yes"`** before editing `CLAUDE.md`.
