## What it does

`/look-back` (beta) runs a short **retrospective** after something went badly. It reads what happened, then proposes changes so the same trouble can't happen again. It changes the agent's surroundings (its checks, guardrails, and standing instructions), never your app's features.

Each proposal is a question you can answer "yes" to, most serious first. Nothing is changed without your yes.

## When to reach for it

You start this by typing `/look-back`; the agent won't run it on its own. Reach for it after a step or repair that went badly, **in the same chat**, so it can read what happened. Say what bothered you after the command if you like: `/look-back it built the wrong page twice`.

## Where each lesson goes

| The trouble | What it proposes |
| :--- | :--- |
| A slip a machine could spot | An automated check or guardrail that catches it every time |
| It guessed wrong about what you wanted | A rule in the plan, or a word in the wordbook |
| The code review missed something | A line for the reviewer to enforce |
| It couldn't see what went wrong | A change that lets it see (for example, keeping the app's messages in a log) |
| How it talks with you | One standing instruction |

## It's working if

- Every proposal says what trouble it prevents, in plain words.
- It ends by telling you what will now be caught earlier.

## Where it fits

**Upkeep**, run after trouble. It often follows [`/repair`](./repair.md) or a step you sent back from [`/build-step`](./build-step.md). For the full map, type [`/what-next`](./what-next.md).
