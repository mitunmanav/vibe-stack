---
name: build-step
description: "Save an automatic restore point, build one playable step with fail-first verification and two-part quality checks, and open a live demo card."
argument-hint: "[step number, e.g. 01]"
disable-model-invocation: true
---

# Build Step

Build **one** playable step from `.vibe/steps/` safely from start to finish, then hand the user a working demo they can click and try in 30 seconds.

## 1. Locate the playable step

1. Read `.vibe/config.md`, `.vibe/WORDS.md`, `.vibe/DECISIONS.md`, and look up the requested step in `.vibe/steps/` (`$ARGUMENTS`).
2. **Gate:** If no step number was given and more than one `TODO` step exists, list the open steps in plain words and **stop to ask which one to build** (`➡️ Step <lowest TODO number>`).

## 2. Create automatic Save Point

Before editing a single file, commit any clean baseline state and create a git tag named `restore/<feature-slug>-<NN>` so `/undo` can return here instantly if anything goes wrong.

## 3. Build with `checking-behavior` and `auditing-work`

1. Run the `checking-behavior` skill: write the automated behavioral check for this step first, watch it fail (*Red*), and capture the failure reason before writing the feature code to make it pass (*Green*).
2. Run all project checks (`check command` in `.vibe/config.md`) and verify the app starts without console or server errors.
3. Run the `auditing-work` skill: spawn Helper A (Safety & Cleanliness) and Helper B (Plan Compliance) and resolve any findings before showing the user.

## 4. Open the Demo Card and wait for the human's verdict

1. Read `DEMO-CARD-TEMPLATE.md` and write `.vibe/previews/demo-<NN>.html` (opening it in the browser if supported).
2. **Hard Gate:** Present the 3-item **"Try It Yourself in 30 Seconds"** list in chat and ask:
   ```markdown
   ❓ **Q1** - **Try Step <NN>**: Does this step work the way you pictured when you click through it?
   ➡️ Yes, mark Step <NN> DONE (or tell me what feels off and we will adjust or `/undo`).
   ```
3. Once the user confirms `"yes"`, mark the step `Status: DONE` in `.vibe/steps/<feature-slug>/<NN>-<step-slug>.md`, commit the finished step, and advise: *"Step <NN> complete! Type `/clear` and then `/build-step <next>`."*
