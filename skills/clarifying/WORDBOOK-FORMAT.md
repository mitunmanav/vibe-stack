# Project Wordbook Format (`WORDBOOK-FORMAT.md`)

Create or update `.vibe/WORDS.md` only after the user has confirmed at least one round of questions (lazy creation). Keep descriptions 100% free of code or database terms in the first three columns.

```markdown
# Project Wordbook (`.vibe/WORDS.md`)

## Everyday Words We Use

| Everyday Word | What It Means in Plain Words | Rules It Always Follows | Agent Code Mapping (Agent Only) |
| :--- | :--- | :--- | :--- |
| **<Term>** | <Plain definition> | <Real-world constraint> | `<internal file or model path>` |

## Words We Avoid (Retired Synonyms)

* **<Old or confusing word>:** Always say **<Term>** instead.
```
