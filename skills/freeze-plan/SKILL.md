---
name: freeze-plan
description: "Turn what we agreed in this chat into a plain-English plan and a short run of Playable Steps, without asking you everything again."
argument-hint: "[optional feature name]"
disable-model-invocation: true
---

# Freeze Plan

Turn what this conversation already settled into a plan and a run of Playable Steps. This is synthesis of the decisions on the table: the interview is over, so do not run it again.

If `.vibe/config.md` is missing, tell the user in plain words to type `/start-project` first, and stop.

## 1. Draft the plan and the steps

Read `.vibe/config.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md`, and look at the app as it is today. Use the wordbook's words throughout.

Slice the feature into **Playable Steps**: tracer bullets, each cutting a thin but complete path through every layer the feature touches.

<slicing-rules>

- Each step ends in something the user can open and click. A step that only lays groundwork is a horizontal slice; fold it into the first step that uses it.
- Step 01 is the thinnest path that works end to end. Later steps thicken it.
- Each step builds only on the steps before it, so the run goes straight from 01 down.
- Each step fits one fresh chat.
- Make the change easy, then make the easy change: if the existing app needs tidying first, that tidy-up is part of Step 01, and Step 01 still ends in something clickable.

</slicing-rules>

For each step, choose its **Automated Checks** at the highest seam that shows the behaviour (a real page clicked by a headless browser beats a single function), using as few seams as will do. Give each check a worked example whose numbers come out differently if the rule were slightly wrong, and one plain line on what it catches and what it misses, so the user sees why their own click-through still matters.

Slicing often turns up a choice the chat never settled (what shows before anything is picked, what happens on an empty list). Sort each one the way `clarifying` does: decide a technical two-way door yourself; put a taste question or one-way door in the same round as the lock-in question below.

## 2. Show the draft and wait

Show in chat:

1. **Playable Steps:** `Step 01`, `Step 02`, ... each with one sentence on what the user can see and click once it is built.
2. **How we will check it works:** the checks for each step, with their catches and misses lines.
3. **Choices I made for you:** every `AGENT` entry in `.vibe/DECISIONS.md` that touches this feature, one line each, so the user can flip any of them.

Then ask any open questions from slicing, numbered from Q1, and finish the round with:

```markdown
❓ **Q<N>** - **Lock in this plan**: Do these steps feel the right size, and do the checks match what you want built?

➡️ Yes, save the plan so we can start on Step 01. (Or tell me a step is too big, too small, or in the wrong order.)
```

Adjust and show it again until the user says yes. Write nothing before the yes.

## 3. Write the files

1. Read `PLAN-TEMPLATE.md` and write `.vibe/specs/<feature-slug>.md`.
2. Read `STEP-TEMPLATE.md` and write one file per step at `.vibe/steps/<feature-slug>/<NN>-<step-slug>.md`.
3. List the saved files and tell the user: *"Plan locked! Type `/clear` to give the next chat a fresh start, then type `/build-step`."*

Done when every agreed step has its own file with status `TODO`, and every rule from the conversation appears in the plan.
