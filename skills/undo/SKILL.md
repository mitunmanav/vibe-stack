---
name: undo
description: "Roll your project back to a working Save Point when a change goes wrong, or save a compact handoff note in .vibe/handoff.md before clearing chat."
argument-hint: "[save-point name, or 'handoff' before clearing chat]"
disable-model-invocation: true
---

# Undo and Handoff

Give the user a one-command safety net to either roll back broken changes to a working Save Point or pack up a clean handoff note before closing or clearing chat.

## 1. Decide whether to roll back or write a handoff note

* **Handoff branch:** If `$ARGUMENTS` mentions `handoff`, `pause`, or `clear` (or if the user says they are stopping for the day), read `HANDOFF-TEMPLATE.md` and write `.vibe/handoff.md`.
* **Rollback branch (default):** List the 3 most recent `restore/*` Save Point tags with their plain-English step names and timestamps, and ask:
  ```markdown
  ❓ **Q1** - **Roll back to Save Point**: Do you want to rewind your app files back to **`restore/<latest>`** (right before <step name>)?
  ➡️ Yes, restore my files to `restore/<latest>` (I will save a backup tag `backup/before-undo` first so nothing is lost forever).
  ```

## 2. Execute safely after confirmation

1. **Stop and wait for `"yes"` before resetting any files.**
2. Create a safety backup tag (`backup/before-undo-<timestamp>`) on the current state first, then reset the working tree cleanly to the chosen `restore/*` tag.
3. Confirm in one plain sentence that the app is back to the working Save Point and tell the user what command to run next.
