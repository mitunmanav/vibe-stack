---
name: build-step
description: "Take a Save Point, build one Playable Step red-green, have it reviewed, and open a Demo Card to click through."
argument-hint: "[step number, e.g. 01]"
disable-model-invocation: true
---

# Build Step

Build one Playable Step from `.vibe/steps/` and hand the user something they can click through in 30 seconds.

## 1. Find the step

Read `.vibe/config.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md`. If `.vibe/config.md` is missing, tell the user to type `/start-project`; if there are no step files, tell them to type `/freeze-plan`; then stop.

Build the step whose number the user typed after the command. If they typed none, build the lowest-numbered `TODO` step and name it in one line. Read that step file and its plan in `.vibe/specs/`.

## 2. Take a Save Point

Confirm `.gitignore` covers `.env` files, commit any changes (`git add -A`, message "Save Point before Step <NN>"), then tag the current commit `restore/<feature-slug>-<NN>`, moving the tag if it already exists. Done when `git status` is clean and the tag points at the new commit, so `/undo` can return here exactly.

## 3. Build it red-green

Call the Skill tool with "checking-behavior", and build the step through the checks listed in its step file. When the step needs a key from an outside service, read `../launch-check/SERVICE-SETUP-TEMPLATE.md` and walk the user through it before building that part.

Then start the app with the start command from `.vibe/config.md` and open the step's screen. Done when every check is green, the full check command passes, and the app starts and shows the screen with no errors in the browser console or the server output.

## 4. Review it

Call the Skill tool with "auditing-work", naming the Save Point from step 2 and this step file.

## 5. Hand over the Demo Card

Read `DEMO-CARD-TEMPLATE.md`, write `.vibe/previews/demo-<NN>.html`, open it in the browser if you can, and print its path. Show the three Try It Yourself actions in chat and ask:

```markdown
❓ **Q1** - **Try Step <NN>**: Click through the three things on the Demo Card. Does it work the way you pictured?
➡️ Yes, mark Step <NN> done. (Or tell me what feels off; `/undo` takes the app back to before this step.)
```

If the user says it is not what they meant, read `PUSHBACK.md` and follow it.

## 6. Close the step

On a yes, set the step file to `Status: DONE`, commit ("Step <NN>: <title>"), and tell the user: *"Step <NN> is done! Type `/clear`, then `/build-step` for the next one."* If it was the last step, suggest `/launch-check` instead.
