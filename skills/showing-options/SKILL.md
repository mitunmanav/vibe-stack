---
name: showing-options
description: "Throwaway clickable preview in .vibe/previews/ that settles one question words cannot: how a screen should look, or how something should behave over time. Use when a layout, style, or flow choice is easier to see and click than to describe."
user-invocable: false
---

# Showing Options

A preview is **throwaway** code that answers one question by letting the user click instead of imagine. It is a single self-contained HTML file in `.vibe/previews/` that opens by double-click: it lives beside the app, never inside it, so the user's real app is untouched.

## 1. Name the question and pick the branch

Write the question this preview settles in one plain sentence. It goes at the top of the preview, where the user sees it. Then pick the branch by the question:

- **"What should this look like?"** Read `VISUAL-OPTIONS.md` and build `.vibe/previews/<slug>-options.html`.
- **"How should this behave as things happen?"** (a booking, an invite, an order moving from start to finish) Read `FLOW-SIMULATOR.md` and build `.vibe/previews/<slug>-flow.html`.

If the screen already exists in the app, copy its real header, wording, and sample content into the preview so each option is judged in its real surroundings.

Done when the file opens by double-click with no install, no server, and no internet.

## 2. Hand it over and ask

Open the file in the browser if you can, and always print its path. Then ask one question, recommending the option that best fits what the user has said so far:

```markdown
❓ **Q1** - **Pick a direction**: I saved a clickable preview at `.vibe/previews/<file>`. Does **<recommended option>** feel closest to what you want? Mixing parts ("the top of B with the list from C") is a great answer too.
➡️ <recommended option>, because <one plain reason tied to what the user said>.
```

## 3. Record the answer

When the user picks, add a `.vibe/DECISIONS.md` entry with `Decided by: USER` that names the question, the pick, and the reason, and link the preview file in it. The preview stays in `.vibe/previews/` as the record of what was compared; only the chosen direction is built into the real app, later, by `/build-step`.
