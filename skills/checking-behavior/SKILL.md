---
name: checking-behavior
description: "Reference discipline for automated fail-first verification: watching a behavioral check fail before writing feature code, building one playable step at a time, and skipping mid-loop cleanup. Use when building a step or repairing a bug."
user-invocable: false
---

# Checking Behavior

Prove every playable step or bug repair actually works by running an automated check that tests real user-visible behavior. **Never ask the human to act as your manual tester for broken basics.**

## 1. Where checks must sit

Test the app through the same doorway the user uses (clicking the real page in a headless browser, calling the real form handler, or running the real feature workflow). Read `CHECK-TYPES.md` when choosing the check type and recording what it catches and misses.

## 2. Three bad checks to avoid

* **Fake ("always-green") check:** A check that only verifies a file exists or tests a fake stub instead of the real behavior.
* **Fragile internal check:** A check tied to internal variable names that breaks when code is tidied even though the screen still works.
* **Layer-only check:** Testing database helpers in isolation while the button on screen is not even wired up.

## 3. Rules of the verification loop

1. **Fail first (Red before Green):** Write the automated check for the current playable step and run it **before** writing the feature code. Record the exact failure message so you have proof the check catches missing behavior.
2. **One playable step at a time:** Write only the code needed to make this step's check pass and its screen work.
3. **No mid-loop gold-plating:** Do not reorganize unrelated files while getting the step working; leave code tidying for `auditing-work` after all checks for the step are green.

## Red flags (never rationalize these)

| Tempting Shortcut | Required Action Instead |
| :--- | :--- |
| "I'll write the feature code first and add a quick test after." | Write and run the failing check first, or temporarily comment out the new logic to witness and record the red failure. |
| "A mock test is faster than testing the real page." | Test the real page or storage boundary so wiring bugs are caught. |
