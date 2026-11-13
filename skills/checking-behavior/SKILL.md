---
name: checking-behavior
description: "Red-green discipline for proving a Playable Step or a repair works: one check, watched failing, then the least code that makes it pass. Use when building a step, fixing a bug, or writing any automated check."
user-invocable: false
---

# Checking Behavior

The user cannot read code, so a passing check is the only proof they get that the app works. Every check here must be able to fail for the right reason.

## Where checks go

Test at a **seam** the user would recognise: the real page driven by a headless browser, the real form submission, the real saved data read back through the app. A check at that height survives any rewrite of the code behind it and catches wiring the user would hit. Use the checks agreed in the step file; when a repair needs a new one, pick the highest seam that reaches the bug. Read `CHECK-TYPES.md` when you choose or describe a check.

A check earns its place when:

- **It tests behaviour, not structure.** It goes through the seam, never into private functions, call counts, or the database behind the app's back. It breaks when behaviour breaks and only then.
- **Its expected value comes from outside the code.** A literal from the plan or a worked example ("2 slots at $15 shows $30"), never a value recomputed the way the code computes it, which passes by construction.
- **Its example tells the rule apart from its near misses.** Pick inputs where the rule and the likeliest wrong versions of it give different answers. For "round up to the cent", $90 split 7 ways cannot tell rounding up from ordinary rounding ($12.86 either way); $10 split 3 ways can ($3.34 against $3.33).
- **It replaces only what the project does not own.** Stand in for payment providers, email senders, the clock, and randomness; run the app's own parts for real.

## The loop

Work in vertical slices, one behaviour at a time:

1. **Red.** Write one check and run it. It must fail, and fail because the behaviour is missing (not a typo, a crash in setup, or a wrong selector). Record the failure message.
2. **Green.** Write the least code that makes it pass. No code for checks you have not written yet.
3. Repeat until every check for the step is green, then run the project's full check command once.

If the behaviour already exists and the check passes at once, force the red by breaking the code under test, confirm with `git diff` that the break really landed, watch the check fail, then undo the break.

Tidying waits until every check is green; the review in `auditing-work` handles it.

Done when every check listed for the step was seen red for the right reason and is now green, and the full check command passes.
