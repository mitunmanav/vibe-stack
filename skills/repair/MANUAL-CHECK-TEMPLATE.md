# One-Click Human Reproduction Guide (`MANUAL-CHECK-TEMPLATE.md`)

Use this only when a visual or browser-specific bug cannot be triggered by a headless script alone:

1. Add `[TRACE-repair]` logging around the suspected screen action.
2. Start the local app and ask the user one simple line:
   ```markdown
   ❓ **Q1** - **Click once to capture the bug**: Please click the <button name> once in your browser and reply `done` so I can read the trace log.
   ➡️ Done (I clicked it once).
   ```
3. As soon as the trace confirms the root cause, write an automated check for that cause and strip all `[TRACE-repair]` lines before finishing.
