---
name: showing-options
description: "Create a clickable browser preview in .vibe/previews/ showing visual layout options or an interactive screen-flow walkthrough. Use when a design, layout, or user-flow choice is easier to see and click than debate in text."
user-invocable: false
---

# Showing Options

Answer a visual style or user-flow question by opening a self-contained, double-clickable HTML file in `.vibe/previews/` so the human can choose by clicking rather than guessing from text descriptions. **Never switch git branches or strand the user's working files.**

## 1. Pick the preview type

1. State in one plain sentence the exact question this preview will settle.
2. Choose one branch:
   * **Visual Layout & Style Options:** Read `VISUAL-OPTIONS.md` when the user needs to compare 2 or 3 distinct look-and-feel directions for a screen.
   * **Interactive Step-by-Step Flow Simulator:** Read `FLOW-SIMULATOR.md` when the user needs to click through how an item (such as a booking, pass, or order) changes from start to finish.

## 2. Open and pause

1. Save the self-contained HTML file to `.vibe/previews/<slug>-options.html` (and try opening it in the default browser if available, while always printing the clickable file path).
2. **Gate:** Stop and ask one line:
   ```markdown
   ❓ **Q1** - **Pick your favorite preview**: I saved a clickable preview at `.vibe/previews/<slug>-options.html`. Does **Option A** feel closest to what you want, or should we mix parts of them?
   ➡️ Option A (cleanest layout and easiest to scan on both phone and desktop).
   ```
