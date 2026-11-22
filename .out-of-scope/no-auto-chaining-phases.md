# Chaining commands together automatically

Vibe Stack does not run `/ask-me`, `/freeze-plan`, and `/build-step` back to back on its own. Each one starts only when the human types it. Requests for an "autopilot" mode, or for one command to run the next, are out of scope.

## Why this is out of scope

The gap between two commands is where the human decides. After `/ask-me`, they confirm the summary matches what they pictured. After `/freeze-plan`, they lock in the steps. After each `/build-step`, they click through a Demo Card. Skip those gaps and the agent builds features nobody approved, in a chat so long it has stopped reasoning sharply.

The gaps are also where the chat gets cleared. Each `/build-step` starts fresh from its step file, which is what keeps step five as sharp as step one. Chaining would run the whole build in one ever-longer chat.

A user command cannot call another user command in any harness, so this is also how the skills are built, not just a preference. `/what-next` is the answer to "what do I type now?".

## Prior requests

None yet.
