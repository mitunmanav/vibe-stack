---
name: auditing-work
description: "Audit recent changes using two fresh-memory helpers: Pass A (exposed secrets, file cleanliness, and fake-check detection) and Pass B (plan compliance against .vibe/specs/). Use when checking a completed build step, verifying a bug repair, or preparing to launch."
user-invocable: false
---

# Auditing Work

Never let the builder agent grade its own work in a cluttered memory window. Spawn **two isolated foreground helpers with fresh memory windows** to audit every change since the last Save Point (`git diff`).

## 1. Run the two isolated review passes

### Pass A - Safety, Cleanliness, and Check Honesty (Auto-Fixed Silently)
Spawn Helper A with the diff and instruct it to check four things:
1. **No exposed secrets or debug leftovers:** Zero hardcoded API keys/tokens, `.env` properly ignored, and zero lingering `[TRACE-` debug markers.
2. **No giant tangled files:** Keep each feature in its own clean folder and keep individual files under ~300 lines so future edits stay easy to delete or change.
3. **Code cleanliness:** Check for duplicated logic, dead code, or tangled functions.
4. **Honest automated check:** Verify the check written during `checking-behavior` actually tests the real feature and is not a fake always-green stub.
* **Rule for Pass A findings:** Do **not** lecture the human about code cleanliness. Fix Pass A code issues silently, re-run the automated check to confirm everything stays green (reverting the tidy-up if the check turns red), and only interrupt the human if a real secret/privacy risk requires their input.

### Pass B - Plan and Wordbook Compliance
Spawn Helper B with the diff, `.vibe/specs/<slug>.md`, `.vibe/steps/<slug>/<NN>.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md`:
1. Check every promised item in the step file: is it completely built, partially built, or missing?
2. Check that every button, label, and message on screen uses the exact everyday words from `.vibe/WORDS.md`.
3. Check that no unrequested extra features ("scope creep") were snuck in.

## 2. Report and learn from pushback

* Never merge Pass A and Pass B into one blended list.
* If the human says *"this isn't what I meant"* when trying the demo, read `LEARN-RULES.md` to update the plan and add a 1-line lesson to `CLAUDE.md`.
