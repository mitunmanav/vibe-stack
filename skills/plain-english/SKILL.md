---
name: plain-english
description: "Confused by technical terms, want to change a logged decision, or unsure what command to run next? Get a simple explanation and next step."
argument-hint: "[decision ID like D-01, or leave blank]"
disable-model-invocation: true
---

# Plain English

Rescue the user immediately using short, literal, everyday sentences with zero programmer terms.

## 1. Check what the user needs

1. Read `.vibe/WORDS.md` and `.vibe/DECISIONS.md` if present.
2. **If the user passed a decision ID (`$ARGUMENTS`, e.g. `D-02`) or asked to change a behind-the-scenes choice:**
   * Mark the old entry in `.vibe/DECISIONS.md` as `SUPERSEDED BY [D-XX]`.
   * Write the new `[D-XX]` entry with `Decided by: HUMAN OVERRULED`.
   * State in one plain sentence what will change on screen.
3. **If the user is confused by the last message:**
   * Rewrite the last message in 3 to 4 short, everyday sentences using only the everyday nouns in `.vibe/WORDS.md` and concrete real-world examples.
   * Show the most recent `[AGENT]` choice from `.vibe/DECISIONS.md` and ask: *"Did I assume something wrong here? Tell me and I will flip it."*
4. **Show where we are and what to type next:**
   * Read `FLOW-MAP.md` when recommending the next `/command` or explaining whether to keep chatting or type `/clear`.
