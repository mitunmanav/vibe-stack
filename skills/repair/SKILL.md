---
name: repair
description: "Something broken or acting weird? Make it happen on demand, find the real cause, and fix it with a check that keeps it fixed."
argument-hint: "[what went wrong or looks broken]"
disable-model-invocation: true
---

# Repair

A discipline for fixing one problem without breaking the rest of the app. Skip a phase only with a reason you state.

## 1. Redact, then take a Save Point

If the user pasted an error or log, replace every key, token, password, or personal detail with `<REDACTED>` before you quote any of it, and keep doing so in everything you show. Build loops that read keys from the environment, so they never appear in what you show.

Commit any changes (`git add -A`, message "Save Point before repair") and tag the current commit `restore/repair-<YYYYMMDD-HHMM>`.

Say back in one plain sentence what the user saw, not what you think caused it. If what they typed after the command is not enough to make the problem happen (which screen, what they clicked, what they expected, what happened instead), ask for exactly those in one round.

## 2. Build a loop that goes red

**This is the skill.** With a **tight** loop that goes **red** on this exact problem, the cause falls out; without one, every fix is a guess. Spend most of your effort here. Be creative, and refuse to give up. Try, roughly in this order:

1. A click-through or save-and-reload check against the real page.
2. A short script against the running app, or a replay of a captured request or saved data.
3. Many random inputs, when the problem is "sometimes the number is wrong".
4. **Save Points as a time machine**, when the problem is new: copy the app at older `restore/*` tags into a scratch folder (`git worktree add`) and run the loop there. The first Save Point where it goes red brackets the change that caused it.
5. Only when the problem truly needs a human hand (a specific phone, a drag gesture), read `MANUAL-CHECK-TEMPLATE.md`.

Then tighten it: faster (skip unrelated setup), sharper (check the exact symptom, not "did not crash"), steadier (fix the clock, the random seed, the test data). For a problem that comes and goes, raise how often it shows up (repeat the trigger, run copies side by side) until it fails often enough to study.

If you cannot build a loop, stop and say so. List what you tried, then ask for one thing that would help: a screen recording, a screenshot of the message, or the exact steps on their device.

Done when you can name **one command** that you have already run, and it is:

- [ ] **Red on this problem**: it fails showing the user's exact symptom, not a different failure nearby.
- [ ] **Steady**: the same verdict every run (or, for a problem that comes and goes, a high and steady rate).
- [ ] **Fast**: seconds, not minutes.
- [ ] **Runnable without the user.**

Theories wait for this command. Reading code to guess the cause before it exists is the exact failure this skill prevents.

## 3. Shrink it

Cut the scenario down one piece at a time (fewer items, fewer clicks, simpler data), rerunning after each cut. Done when every piece left is load-bearing: removing any one makes the loop pass.

## 4. Theories, one change at a time

Write three to five ranked theories before testing any. Each must predict something: "If <cause>, then <changing this> will make the problem go away." A theory with no prediction is a hunch; sharpen it or drop it.

Show the ranked list to the user in plain words: they often know something that reorders it ("it started after I changed the price"). Carry on with your ranking while they read.

Test in rank order, changing one thing per run. Tag every temporary log line with one short random tag such as `[TRACE-k3f9]`, so cleanup is one search. Undo a failed attempt completely before the next; `git diff` against the Save Point shows what to undo.

For a **slow** problem, logs mislead: time it first (a timing script, the browser's performance panel), then compare Save Points. Measure, then fix.

## 5. Fix with a check that stays

Call the Skill tool with "checking-behavior": turn the shrunk scenario into a lasting Automated Check at a seam that reaches the real problem (when the step 2 loop already is such a check, keep it), watch it fail, fix the cause, watch it pass. Add the check, in the step file's format, to the step that brought the problem in, so a rebuild after `/undo` builds it again. Then rerun the step 2 loop on the original, unshrunk scenario.

If no seam can reach the problem, that is itself the finding: say so plainly in the summary rather than write a check that cannot catch it, and suggest `/tidy-up`.

## 6. Clean up and report

- [ ] The original scenario no longer fails (rerun the step 2 loop).
- [ ] The new check is green, or the missing seam is stated.
- [ ] No trace tag remains (search for it) and no scratch copy remains (`git worktree remove`).
- [ ] Call the Skill tool with "auditing-work", naming the Save Point from step 1.
- [ ] Commit with a message stating the cause that proved true, so the next repair learns from it.

Tell the user in one plain sentence what was wrong, then give two things to click to see it fixed.
