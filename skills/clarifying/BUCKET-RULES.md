# Three-Bucket Filter and Question Rules (`BUCKET-RULES.md`)

## Banned Programmer Words in Human Questions

Never use these words in chat with the user: `schema`, `table`, `foreign key`, `boolean`, `nullable`, `endpoint`, `API`, `route`, `component`, `state machine`, `hook`, `props`, `mock`, `test seam`, `adapter`, `worktree`, `branch`, `commit`, `migration`, `RLS`, `OAuth`, `JWT`, `env var`, `localStorage`, `SQLite`, `Postgres`, `JSON`, `CSV`, `DOM`, `regex`.

## How to Translate Technical Questions into Everyday Choices

1. **Instead of asking about data models:** Ask a concrete story question (*"Can one person book spots for several friends at once, or just one spot per person?"*).
2. **Instead of asking about storage engines (`localStorage` vs `SQLite` vs cloud DB):** Never name storage technologies in chat; ask whether the tool is used on *"this computer only"* versus *"across multiple phones and computers"*.
3. **Instead of asking about authentication protocols:** Ask a Bucket 3 consequence question (*"Should we start with a simple passcode on your computer for free, or set up Google sign-in right away?"*).
4. **Instead of asking about third-party APIs:** Warn if it costs money (`⚠️ **Why this matters:**`) and recommend a free simulated preview mode first (`➡️`).
5. **External person questions:** If the user says they need to ask a client, partner, or friend before answering, ask only who that person is and what answers are needed back, then write a plain-English `.vibe/questions-for-<name>.md` sheet where `"I don't know"` is welcomed.
