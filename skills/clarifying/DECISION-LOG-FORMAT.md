# Plain-English Decision Log Format (`DECISION-LOG-FORMAT.md`)

Append new entries to `.vibe/DECISIONS.md` using this exact 4-line structure. Date every entry (`YYYY-MM-DD`) and never delete past entries (mark overruled entries as `SUPERSEDED BY [D-XX]`).

```markdown
### [D-02] YYYY-MM-DD - <Short plain-English title>
* **Status:** ACTIVE | **Decided by:** AGENT (or HUMAN APPROVED - HIGH IMPACT)
* **What we chose:** <One plain sentence describing what the app does, zero code terms.>
* **Why:** <One plain sentence explaining how this keeps the app simple, fast, or safe.>
* **How to change this:** Type `/plain-english D-02` or tell the agent in chat.
```
