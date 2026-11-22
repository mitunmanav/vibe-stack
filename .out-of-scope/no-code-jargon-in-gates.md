# Asking the human technical questions

Vibe Stack never asks the user about database tables, API endpoints, components, test doubles, or code smells. Requests for an "advanced mode" that surfaces those questions are out of scope.

## Why this is out of scope

The people Vibe Stack serves cannot answer a technical question well, and a question they cannot answer is worse than no question: they guess, and the guess becomes a decision. Every technical question has an everyday one under it (who can see this, what happens when two people click at once, will this be used on phones), and that is the one the agent asks.

Technical choices that are easy to undo are the agent's own. The ones that would surprise the user later go in `.vibe/DECISIONS.md` in plain words, where the user can change any of them by asking. The choices that really are the user's (money, private information, outside accounts, deleting data) are asked as one-way doors, with the real-world result spelt out.

People who do read code and want to steer the technical choices are better served by an engineering skill set.

## Prior requests

None yet.
