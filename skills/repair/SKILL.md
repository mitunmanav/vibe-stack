---
name: repair
description: "Something broken or acting weird? Save a restore point, reproduce the problem scientifically without guessing, fix the root cause, and clean up."
argument-hint: "[what went wrong or looks broken]"
disable-model-invocation: true
---

# Repair

Fix broken behavior without entering a guessing spiral ("death loop") that breaks the rest of the user's app. **Never guess a code fix before you have reproduced the failure.**

## 1. Save Point and plain-English translation

1. Strip or mask any secret keys if the user pasted an error log.
2. Create an automatic Save Point tag `restore/pre-repair-<timestamp>` before touching any file.
3. Inspect the browser console, server logs, or error trace directly, and explain to the user in **one plain-English sentence** what went wrong on screen.

## 2. Reproduce first (No reproduction, no code edits)

1. Build an automated check that triggers the exact broken behavior and watch it fail (*Red*).
2. If the bug only happens through a visual human action that cannot be triggered automatically yet, read `MANUAL-CHECK-TEMPLATE.md` to set up a 1-click reproduction check with the user. **Do not move to Step 3 until the failure is reproduced.**

## 3. Test 3 plain theories with temporary trace markers

1. Write down 3 ranked theories for why the bug happens and what evidence will prove each theory right or wrong.
2. If needed, add temporary log lines tagged with `[TRACE-repair]` to observe what happens when the reproduction check runs.

## 4. Fix, verify, and clean every trace marker

1. Run the `checking-behavior` skill: fix the root cause so the reproduction check turns *Green*, and verify all existing checks still pass.
2. Remove every `[TRACE-repair]` marker and verify with `git diff` that only the clean fix and regression check remain.
3. Run the `auditing-work` skill, then show the user a 2-step **"Try It Yourself"** check in chat to confirm the bug is gone.

## Red flags (never rationalize these)

| Tempting Shortcut | Required Action Instead |
| :--- | :--- |
| "I think I see the typo, I'll just edit the file without reproducing it." | Reproduce the failure with a failing check first so you know for sure the fix worked. |
| "Fix #1 didn't work, let me try Fix #2 on top of Fix #1." | Revert the failed guess back to `restore/pre-repair` before testing the next theory. |
