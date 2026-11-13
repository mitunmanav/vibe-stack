# When the User Says "That's Not What I Meant" (`PUSHBACK.md`)

1. Ask one round of plain questions until you can say what they expected, in their words. Show any `AGENT` entry in `.vibe/DECISIONS.md` that may have caused the gap.
2. Put the lesson where it will be read next time, in its one right home:
   * A silent choice that guessed wrong: mark it `SUPERSEDED BY D-NN` in `.vibe/DECISIONS.md` and add the user's choice with `Decided by: USER`.
   * A rule about the product ("prices always include tax"): add it to the plan's "Rules That Always Hold" and to the rules column of `.vibe/WORDS.md`.
   * A slip an Automated Check could have caught: add that check to the step file and write it red-green.
   * A preference about how the agent works or talks with them: propose one line for the project's agent instructions file (`AGENTS.md` or `CLAUDE.md`, whichever exists), checking whether an old line there can go at the same time, and add it only after their yes.
3. Rebuild the step from step 3 of `build-step`, or take them back with `/undo` if they prefer to start the step over.
