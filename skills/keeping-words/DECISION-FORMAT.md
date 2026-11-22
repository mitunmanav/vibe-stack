# Decision Log Format

`.vibe/DECISIONS.md` holds the choices made for this project that the user might want to change, in plain words. It explains its own format, so every later entry takes the same shape.

When the file does not exist yet, create it with this header:

<decision-log-template>

```markdown
# Decision Log

Choices made for this project that you might want to change. To change one, say so in chat, for example "change D-02 so it works on phones too".

<!-- Agents: add each entry at the bottom in the same shape as the entries above it. Never delete an entry. -->
```

</decision-log-template>

Then add each entry at the bottom, numbered one past the highest `D-NN` in the file:

<decision-entry-template>

```markdown
### D-NN YYYY-MM-DD - <short plain title>
* **Status:** ACTIVE | **Decided by:** AGENT or USER
* **What we chose:** <one plain sentence, e.g. "Runs on your computer as a small website; no accounts or payments needed to try it.">
* **Why:** <one plain sentence: how this keeps the app simple, safe, free, or easy to change>
```

</decision-entry-template>

An entry can be those three lines and nothing more. Its value is in recording _that_ a choice was made and _why_, in words the user can check.

Add one line, `* **Preview:** <path in .vibe/previews/>`, when a clickable preview settled the choice.

## Changing an earlier choice

1. Set the old entry's status to `SUPERSEDED BY D-NN`.
2. Add the new choice as its own entry with `Decided by: USER`.
3. Tell the user in one plain sentence what will change on screen.
