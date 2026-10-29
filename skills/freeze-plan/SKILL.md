---
name: freeze-plan
description: "Turn our agreed conversation into a jargon-free feature plan in .vibe/specs/ and slice it into ordered, playable steps in .vibe/steps/."
argument-hint: "[optional feature name]"
disable-model-invocation: true
---

# Freeze Plan

Turn the decisions already reached in this conversation into a plain-English feature plan and a short list of playable steps. **Ask no new questions; summarize only decisions already settled.**

## 1. Check workspace and vocabulary

1. Read `.vibe/config.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md` passively inline (do not call `clarifying`). If `.vibe/config.md` is missing, stop and tell the user in plain words to run `/start-project` first.
2. Identify the 2 to 4 **Playable Steps** needed to build this feature so that **every single step ends with something visible the user can click and try in their browser** (never create code-only steps like "set up database tables" or "build backend routes").

## 2. Gate on playable steps and behind-the-scenes recap

Present a short preview in chat before writing the files:
1. **Playable Steps List:** Numbered list (`Step 01`, `Step 02`, ...) stating in one sentence what the user will be able to see and click after each step finishes.
2. **How We Will Check It Works:** 2 to 4 plain-English checks the agent will test automatically.
3. **Decisions I Made For You (Bucket 1 Recap):** List any `[AGENT]` choices from `.vibe/DECISIONS.md` in one bullet each so the user can spot any assumption they want to flip.
4. **Hard Gate:** Ask:
   ```markdown
   ❓ **Q1** - **Lock in this plan**: Do these playable steps and checks match what you want to build?
   ➡️ Yes, save the plan and steps to `.vibe/` so we can start building Step 01.
   ```
   **Stop and wait for confirmation before writing files.**

## 3. Write files and advise `/clear`

1. Read `PLAN-TEMPLATE.md` when writing `.vibe/specs/<feature-slug>.md`.
2. Read `STEP-TEMPLATE.md` when writing `.vibe/steps/<feature-slug>/<NN>-<step-slug>.md`.
3. Print the saved file paths and tell the user: *"Plan locked! Type `/clear` to refresh chat memory, then type `/build-step 01`."*
