---
name: auditing-work
description: "Two-axis review of everything changed since a Save Point, by two fresh helpers: Safety & Standards, and Plan. Use when a step is built, a repair is done, or the app is about to launch."
user-invocable: false
---

# Auditing Work

The agent that built a change is the worst judge of it: its window is full of the reasons the code looks right. Review the change from two fresh windows, along two **axes** kept apart:

- **Safety & Standards**: is the change safe, and is it written the way this project writes code?
- **Plan**: does the change build exactly what the plan and the step asked for?

## 1. Pin the fixed point

The caller names the Save Point to review from (a step's `restore/...` tag, a repair's tag, or `restore/project-start` for the whole app). Stage everything so new files are included (`git add -A`), then capture the diff command once: `git diff --staged <save-point>`.

Done when the tag resolves and the diff is not empty. A bad tag or an empty diff stops here, not inside two helpers; say so in one plain line.

## 2. Gather what each helper needs

- **Standards**: `.vibe/STANDARDS.md` if it exists (the project's own rules, written by `/look-back`), plus the smell baseline in `SMELLS.md`, pasted in full: the helper has no other way to see it. A project rule always overrides the baseline.
- **Plan**: the plan in `.vibe/specs/`, the step file if the caller named one, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md`. With no plan (a repair, a tidy-up), the Plan helper checks only that nothing on screen changed beyond what the caller intended.

## 3. Run both helpers

Start both together, in the foreground, each in a fresh context window, and use the reports they return.

**Safety & Standards brief.** Give it the diff command, the standards material, and this brief: report every place the change

- puts a secret key or token in a tracked file or in code sent to the browser, or leaves a `.env` file outside `.gitignore`;
- shows one person's private information to anyone else;
- leaves debug leftovers (`[TRACE-` lines, stray console output, commented-out code);
- carries a check that cannot fail: one that tests a stand-in instead of the app, or recomputes its own expected value;
- breaks a rule in `.vibe/STANDARDS.md` (cite the rule);
- shows a smell from the baseline (name it and quote the lines).

Mark each finding **must fix** (secrets, privacy, a check that cannot fail, a broken project rule) or **judgement call** (every smell, always). Skip anything the check command already enforces. Under 400 words.

**Plan brief.** Give it the diff command, the plan material, and this brief: for every line of the plan's "What People See and Do" (and every item in the step file, if given), say whether it is built, partly built, or missing; list anything built that the plan did not ask for; list every label, button, or message on screen that uses a different word from `.vibe/WORDS.md`. Quote the plan line for each finding. Under 400 words.

## 4. Act on the reports

Keep the two reports separate. Never merge them or rank one axis's findings against the other's.

- Fix every **must fix** yourself. Fix a judgement call when the fix is small and every check stays green; leave it with a one-line reason otherwise. Rerun the checks after each fix, and undo any fix that turns one red.
- Build anything missing or partial, remove anything built that was not asked for, and fix every wording mismatch.
- Tell the user about a finding only when fixing it needs their decision (a one-way door).

Done when every must-fix and every missing item is resolved and every check is green. Give the caller one plain line per axis: what was found, and what was fixed.

## Why two axes

A change can pass one axis and fail the other. Code that follows every standard can build the wrong thing; code that builds exactly the right thing can leak a key. Reporting them apart stops one from hiding the other.
