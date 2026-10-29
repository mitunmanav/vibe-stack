---
name: start-project
description: "One-time project setup: create your .vibe/ workspace, project wordbook, plain-English decision log, first save point, and agent instructions."
argument-hint: "[describe your project idea in a sentence]"
disable-model-invocation: true
---

# Start Project

Set up a new or existing folder once so every skill knows where plans, everyday words, decisions, and save points live.

## 1. Silent folder check

1. Check silently whether this folder is empty or already contains an app, whether `git` is initialized, and whether `.vibe/config.md` already exists.
2. If the folder already has code, spawn a background helper to figure out what the app does and how it starts locally.
3. If the folder is empty, pick the simplest, most reliable local web stack that runs with one command and requires zero paid cloud accounts to preview.

## 2. Confirm the plain-English summary (1 question)

Ask a single confirmation question (do not ask about issue trackers, linters, or frameworks):

```markdown
❓ **Q1** - **Project baseline**: Here is what we are setting up: "<2-sentence plain-English summary of the project and how it will run on your computer>". Does that match what you want?
➡️ Yes, set up the `.vibe/` workspace and create our first Save Point.
```

**Stop and wait for the user's confirmation.**

## 3. Initialize `.vibe/` and first Save Point

1. Run `git init` silently if this folder is not yet a git repository.
2. Read `WORKSPACE-TEMPLATE.md` when creating `.vibe/config.md`, `.vibe/WORDS.md`, `.vibe/DECISIONS.md`, `.vibe/specs/`, `.vibe/steps/`, `.vibe/previews/`, and the pointer block in `CLAUDE.md` (plus the `AGENTS.md` symlink).
3. Create an initial git commit and tag `restore/project-start` so `/undo` always has a clean starting point.
4. Tell the user: *"Workspace ready! Type `/ask-me` to shape your first feature."*
