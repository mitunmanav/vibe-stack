# Decision Log Entries (`DECISION-LOG-FORMAT.md`)

`.vibe/DECISIONS.md` holds every choice made for the project, whoever made it. New entries go at the bottom, numbered `D-NN`. Entries are never deleted.

## Shape

```markdown
### D-14 YYYY-MM-DD - <short plain title>
* **Status:** ACTIVE | **Decided by:** AGENT
* **What we chose:** <one plain sentence>
* **Why:** <one or two plain sentences>
* **What you will notice:** <the visible effect, or "nothing you can see">
* **Assumes:** <what must stay true for this to hold>
* **Risk if wrong:** <what would go wrong, in plain words>
* **Settled by:** <file, page, or check the agent relied on>
* **Depends on:** <D-NN, D-NN, or "nothing">
* **To change it:** say "change D-14" and what you want instead.
```

## Field rules

- `Decided by` is `AGENT` for a build choice, `USER` for a taste question, and `USER (one-way door)` for an approved one-way door. A one-way door entry adds `* **Approved:** <the user's words> on <date>`.
- `Status` is `ACTIVE`, `SUPERSEDED BY D-NN`, or `REOPENED`. When an entry is superseded, every entry that names it under `Depends on` becomes `REOPENED` until the next round settles it.
- Write the plain fields for the user. `Settled by` may name files and tools; it is for the next agent.
