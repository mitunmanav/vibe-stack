# Writing and editing skills

Read this before you add, change, or review any `SKILL.md` or sidecar file. Every rule here exists so the agent follows the **same path** on every run, for a user who cannot read code and so cannot catch a skill that drifts.

## Two audiences, two vocabularies

Each sentence in this repo speaks to one of two readers:

- **The human** sees questions, demo cards, launch reports, `.vibe/` documents, and the README. Write those in plain everyday words, using the project's wordbook.
- **The agent** reads the `SKILL.md` body and its sidecars. Write those with the strongest standard engineering word the model already knows: _red_, _green_, _vertical slice_, _tracer bullet_, _seam_, _one-way door_, _frontier_, _primary source_. A pretrained word pulls a whole region of known behaviour into the run for one token; a home-made word has to be defined and still pulls nothing.

Keeping the agent's words technical is what lets the human's words stay plain. The translation happens at the moment of speaking to the human, never inside the skill.

## Invocation

See [invocation.md](./invocation.md). In short: the user commands carry no always-loaded description, so they cost no context; the four background skills carry a model-facing description and cost context on every turn, so their descriptions stay short.

A description is a pointer. Front-load the leading word, give one trigger per real branch, and cut anything the body already says.

## Where each piece of text lives

- **Steps** the agent always performs sit in `SKILL.md`, in order.
- **Reference** only some runs need (a template, a format, one branch of a choice) moves to a sidecar file in the same folder, reached by a pointer that names the condition: "Read `X.md` when ...".
- One meaning has one home. If two skills need the same rule, it lives in the background skill that owns it, and the others call the Skill tool with that skill's name.
- The project itself is a source of truth. Do not copy into a document what the agent can read from git, the folder layout, or a `.vibe/` file in one step.

## Steps end on a done-when

Every step ends on a condition the agent can check: "Done when the check is red for the reason the user described", not "once you understand the bug". A vague end invites the agent to rush to the next step. Sharpen the condition first; split the skill only when sharpening is not enough.

Make the condition demanding where thoroughness matters ("every item in the step file is built") so the agent does the digging without a separate step telling it to.

## Say the target, not the forbidden thing

Naming a banned behaviour puts it in front of the model. Write the behaviour you want ("ask about what people see, click, and pay for"), not a list of words to avoid. Keep a "never" only for a hard guardrail with no positive phrasing (a secret pasted into chat, a destructive git command), and pair it with the positive action.

No "tempting shortcut" tables. They spend tokens rehearsing the shortcut.

## No arbitrary numbers

A cap ("at most 3 questions", "2 to 4 steps", "files under 300 lines") replaces judgement with a number that is wrong for half the projects. Give the real criterion instead: ask the **frontier** (every question whose prerequisites are settled); size a step so it fits one fresh context window and ends in something the user can click.

## Facts are the agent's job; decisions are the human's

Look things up before asking. Start every helper in a **fresh context window** (some harnesses fork the conversation by default, which defeats the point), and do not block on it: only the questions that depend on its answer wait.

Every question carries a recommended answer, worded so that "yes" accepts it. Technical choices that are easy to undo are the agent's own decision, recorded only when they would surprise the user later.

## Harness-neutral

Skills run in Claude Code, Codex, Copilot, Cursor, and Gemini CLI. Ask questions as plain chat text. Refer to what the user typed after the command in words ("what the user typed after the command"), not with a harness-specific placeholder. Name subagents and tools generically.

## Prune

- Hunt no-ops: a sentence the model would obey without being told changes nothing. Delete the whole sentence.
- Delete stale lines in the same change that makes them stale.
- After any change, update the router (`plain-english/FLOW-MAP.md`) if a command was added, renamed, or now fits the flow differently. A router that names a missing command, or misses a real one, misleads the user.

## Punctuation

No em-dashes or en-dashes. Rewrite the sentence with a comma, colon, period, or parentheses, whichever it actually wants; do not swap the character for a hyphen.
