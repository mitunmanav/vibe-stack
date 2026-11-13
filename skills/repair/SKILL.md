---
name: repair
description: "Something broken or acting weird? Take a Save Point, make the problem happen on demand, find the real cause, fix it with a check that keeps it fixed, and clean up."
argument-hint: "[what went wrong or looks broken]"
disable-model-invocation: true
---

# Repair

Fix one problem without breaking the rest of the app. The whole skill rests on step 3: a **tight** loop that goes **red** on this exact problem. With one, the cause falls out; without one, every fix is a guess.

## 1. Redact, then take a Save Point

If the user pasted an error or log, replace every key, token, password, or personal detail with `<REDACTED>` before you quote any of it, and keep doing so in everything you show.

Commit any changes (`git add -A`, message "Save Point before repair") and tag the current commit `restore/repair-<YYYYMMDD-HHMM>`.

## 2. Restate the problem

Say back in one plain sentence what the user saw, not what you think caused it. If what they typed after the command is not enough to make the problem happen (which screen, what they clicked, what they expected, what happened instead), ask for exactly those in one round.

## 3. Build a loop that goes red

Find **one command** that drives the app to the problem and checks for the user's exact symptom. Try these in order:

1. A click-through or save-and-reload check against the real page.
2. A short script against the running app, or a replay of a captured request or saved data.
3. **Save Points as a time machine:** if the problem is new, copy the app at older `restore/*` tags into a scratch folder (`git worktree add`) and run the loop there. The first Save Point where it goes red brackets the change that caused it.
4. Only if the problem truly needs a human hand (a specific device, a drag gesture), read `MANUAL-CHECK-TEMPLATE.md`.

Make it tight: seconds, the same verdict every run, runnable without the user. For a problem that comes and goes, repeat the trigger until it shows up often enough to study.

If you cannot build a loop, stop and tell the user what you tried, then ask for one thing that would help: a screen recording, a screenshot of the message, or the exact steps on their device.

Done when you have run the command at least once, it fails showing the user's symptom (not a different, nearby failure), and you can name it. No loop, no theories.

## 4. Shrink it

Cut the scenario down one piece at a time (fewer items, fewer clicks, simpler data), rerunning after each cut. Done when removing anything left makes the loop pass.

## 5. Theories, one change at a time

Write three to five ranked theories. Each must predict something: "If <cause>, then <changing this> will make the problem go away." A theory with no prediction is a hunch; sharpen it or drop it.

Test them in rank order, changing one thing per run. Tag every temporary log line with one short random tag such as `[TRACE-k3f9]`, so cleanup is one search. Undo a failed attempt completely before the next one; `git diff` against the Save Point shows what to undo.

## 6. Fix with a check that stays

Call the Skill tool with "checking-behavior": turn the shrunk scenario into a lasting Automated Check at a seam that reaches the real problem (when the step 3 loop already is such a check, keep it as is), watch it fail, fix the cause, watch it pass. Add the check, in the step file's format, to the step that brought the problem in, so a rebuild after `/undo` builds it again. Then rerun the step 3 loop on the original, unshrunk scenario. If no seam can reach the problem, say so plainly in the summary instead of writing a check that cannot catch it.

## 7. Clean up and report

1. Search for the trace tag and remove every hit; delete any scratch copies from step 3 (`git worktree remove`).
2. Call the Skill tool with "auditing-work", naming the Save Point from step 1.
3. Commit with a message that states the cause that proved true.
4. Tell the user in one plain sentence what was wrong, then give two things to click to see it fixed.

Done when the original scenario passes, the new check is green, no trace tag remains, and the user has their two things to try.
