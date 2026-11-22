---
name: checking-behavior
description: "Red-green discipline for Automated Checks: one check watched failing, then the least code that passes it. Use when building a step, fixing a problem, or writing any check."
user-invocable: false
---

# Checking Behavior

The user cannot read code, so a passing check is the only proof they get that the app works. This skill is the reference that makes the red-green loop produce checks worth that trust. Every section applies on every cycle: consult them before and during the loop, not after.

Name checks with the words in `.vibe/WORDS.md`, so a check reads like a line from the plan: "an Owner can book a free slot".

## What a good check is

A good check proves behaviour through the app's public face and survives any rewrite of the code behind it. Read `CHECK-EXAMPLES.md` for good and bad examples, and `STAND-INS.md` before replacing anything with a stand-in.

## Seams: where checks go

A **seam** is the boundary you check through: the real page driven by a headless browser, the real form submission, the real saved data read back through the app. Checks live at seams the user would recognise, never inside private functions.

**Check only at agreed seams.** The step file lists the checks the user locked in at `/freeze-plan`. When a repair needs a new one, pick the highest seam that reaches the problem. Read `CHECK-TYPES.md` when you choose or describe a check, and give it its catches and misses lines.

## The traps

- **Coupled to the code**: it reaches into private functions, counts calls, or reads the database behind the app's back. The tell: it breaks when the code is tidied but nothing on screen changed.
- **Passes by construction**: its expected value is recomputed the way the code computes it, so it can never disagree with the code. Take expected values from outside the code: a literal from the plan, a worked example ("2 slots at $15 shows $30").
- **Blind to near misses**: its example cannot tell the rule from the likeliest wrong versions of it. For "round up to the cent", $90 split 7 ways is $12.86 either way; $10 split 3 ways tells them apart ($3.34 against $3.33).
- **Horizontal**: every check written first, then all the code. Bulk checks test the imagined shape of the app, not what people do. Work in **vertical slices**: one check, then the code for it, each one a tracer bullet that learns from the last.

## Rules of the loop

1. **Red.** Write one check and run it. It must fail because the behaviour is missing (not a typo, a crash in setup, or a wrong selector). Record the failure message.
2. **Green.** Write the least code that makes it pass. No code for checks you have not written yet.
3. Repeat, one seam and one check per cycle, until every check for the step is green. Then run the full check command once.

When the behaviour already exists and a check passes at once, force the red: break the code under test, confirm with `git diff` that the break really landed, watch the check fail, then undo the break.

Tidying waits until every check is green: it belongs to the review in `auditing-work`.

Done when every check listed for the step was seen red for the right reason and is now green, and the full check command passes.
