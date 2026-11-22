# When the User Says "That's Not What I Meant"

1. Ask one round of plain questions until you can say what they expected, in their words. Show any `AGENT` entry in `.vibe/DECISIONS.md` that may have caused the gap.
2. Put the lesson in its one right home:
   * **A silent choice that guessed wrong**: call the Skill tool with "keeping-words" and supersede it with the user's choice.
   * **A rule about the product** ("prices always include tax"): add it to the plan's "Rules That Always Hold".
   * **A word that meant something else to them**: call the Skill tool with "keeping-words" and settle the word in `.vibe/WORDS.md`.
   * **A slip an Automated Check could have caught**: add that check to the step file and write it red-green.
   * **A preference about how the agent works or talks with them**: tell them `/look-back` can turn it into a standing instruction.
3. Rebuild the step from step 3 of `build-step`, or take them back with `/undo` if they would rather start the step over.
