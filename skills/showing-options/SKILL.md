---
name: showing-options
description: "Throwaway clickable preview that settles one question words cannot: how a screen should look, or how something should behave over time. Use when a layout, style, or flow choice is easier to see than describe."
user-invocable: false
---

# Showing Options

A preview is **throwaway code that answers one question**: the user clicks instead of imagining. The question decides the shape.

## Pick a branch

Name the question in one plain sentence. It goes at the top of the preview, where the user sees it, so the answer can be checked against it later. Then pick:

- **"What should this look like?"** Read `VISUAL-OPTIONS.md` and build `.vibe/previews/<slug>-options.html`: several structurally different options, switchable from one bar.
- **"How should this behave as things happen?"** (a booking, an invite, an order moving from start to finish) Read `FLOW-SIMULATOR.md` and build `.vibe/previews/<slug>-flow.html`: buttons that drive the rules, and a panel showing what is true now.

The two branches make very different files, so getting this wrong wastes the preview. When the question could be either, ask which the user is unsure about: the look, or what happens.

## Rules for both

1. **Throwaway, and lives beside the app.** One self-contained HTML file in `.vibe/previews/`, never inside the app, so the real app is untouched.
2. **Opens by double-click.** No install, no server, no internet.
3. **Real surroundings.** When the screen already exists, copy its real header, wording, and sample content into the preview: an option judged in a vacuum always looks fine.
4. **Surface the state.** On every option switch or button press, show what changed.
5. **Skip the polish.** No checks, no saving, no handling of cases the question does not ask about.

Done when the file opens by double-click and the question sits at its top.

## Hand it over and ask

Open the file in the browser if you can, and always print its path. Then ask one question, recommending the option that best fits what the user has said so far:

```markdown
❓ **Q1** - **Pick a direction**: I saved a clickable preview at `.vibe/previews/<file>`. Does **<recommended option>** feel closest to what you want? Mixing parts ("the top of B with the list from C") is a great answer too.

➡️ <recommended option>, because <one plain reason tied to what the user said>.
```

The best answers are often a mix: that mix is the design they actually want.

## Capture the answer

Call the Skill tool with "keeping-words" and record the pick as a `Decided by: USER` entry naming the question, the pick, the reason, and the preview file. The preview stays in `.vibe/previews/` as the record of what was compared. Only the chosen direction is built into the real app, later, by `/build-step`, and rebuilt properly there rather than copied from the preview.
