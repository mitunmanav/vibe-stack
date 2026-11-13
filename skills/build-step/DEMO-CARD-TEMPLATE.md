# Demo Card Template (`DEMO-CARD-TEMPLATE.md`)

Write `.vibe/previews/demo-<NN>.html`: one self-contained page, readable on a phone, with four boxes in plain words. Fill every box from what actually happened in this run.

1. **New in Step <NN>:** two plain sentences on what the user can do now.
2. **Try It Yourself (30 Seconds):** the three actions from the step file, each as a tick box: `<what to click>` -> `<what you should see>`.
3. **What the agent already checked:** one line per Automated Check with its result (seen failing before the build, passing after), then one line per review axis from `auditing-work` saying what was found and fixed.
4. **Safety net:** "Not right? Type `/undo` to go back to how the app was before this step."
