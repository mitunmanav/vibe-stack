---
name: start-project
description: "One-time setup: create your .vibe/ workspace, make sure the app can start and be checked automatically, and take your first Save Point."
argument-hint: "[describe your project idea in a sentence]"
disable-model-invocation: true
---

# Start Project

Set up a folder once, so every other command knows where the plan, the words, the decisions, and the Save Points live, and so the app can be started and checked from day one.

If `.vibe/config.md` already exists, the project is already set up: say so, tell the user to type `/plain-english` to see where they are, and stop.

## 1. Look before asking

Find out whether the folder is empty or already holds an app, and whether it is already a git repository.

- **Existing app:** start a helper in a fresh context window. Its job: find what the app does, the one command that starts it, and the one command that runs its checks (if any). Wait for its report; the summary in step 2 depends on it.
- **Empty folder:** choose the simplest reliable stack that runs on this computer with one command, needs no paid account, and can be checked by driving real pages in a headless browser. Prefer a stack with static types or a linter, and make that part of the check command, so slips are caught before the app runs. This is a technical two-way door: decide it yourself.

## 2. Confirm the summary

Ask one question:

```markdown
❓ **Q1** - **Getting started**: Here is what I'll set up: "<two plain sentences: what the app is for and how it will run on this computer>". Does that match what you want?
➡️ Yes, set it up and take the first Save Point.
```

Wait for a yes. The only thing to settle here is that summary; the idea itself is shaped later with `/ask-me`.

## 3. Make it startable and checkable

1. Run `git init` if needed. Before anything is committed, make sure `.gitignore` covers `.env` files, dependency folders, and build output, and that no file holding a key or password is about to be committed.
2. **Empty folder:** create the smallest app on the chosen stack that opens a page with the project's name, plus one Automated Check that opens that page in a headless browser and finds the name. **Existing app without checks:** add a headless browser check runner and one check that opens the home page.
3. Read `WORKSPACE-TEMPLATE.md` and create `.vibe/config.md`, `.vibe/DECISIONS.md` (with `D-01` for the stack), the pointer block, and the commit guardrail.

Done when the start command opens the app in the browser, the check command runs green, and a trial commit holding a made-up key is refused (then removed).

## 4. First Save Point

Commit everything ("Start project") and tag it `restore/project-start`. Tell the user: *"All set! Type `/ask-me` and describe the first thing you'd like the app to do."*
