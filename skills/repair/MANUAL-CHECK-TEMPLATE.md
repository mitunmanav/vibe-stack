# One-Click Help From the User (`MANUAL-CHECK-TEMPLATE.md`)

The last resort, for a problem that only shows up under a real person's hand. Keep the user's part to one action per round.

1. Add temporary log lines with this repair's trace tag around the suspected action, writing to a place you can read afterwards (the server output, or a log file).
2. Start the app, then ask:
   ```markdown
   ❓ **Q1** - **Make it happen once**: Please open <exact page>, click <exact button> once, and reply `done`.
   ➡️ Done.
   ```
3. Read the log. Repeat with a different single action only if the log has not yet shown the cause.
4. Once the cause is clear, return to step 6 of `repair`. The trace lines are removed in step 7.
