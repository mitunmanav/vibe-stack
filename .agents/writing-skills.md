# Writing and editing skills

Read this before you add, change, or review any `SKILL.md`, sidecar file, `CLAUDE.md`, or doc an agent reaches by a pointer. The packaging differs; the writing does not. Every rule here exists so that every run follows the **same path**: not the same output, the same process. The people Vibe Stack serves cannot read code, so they cannot catch a skill that drifts.

When the document is a skill, also read [invocation.md](./invocation.md) for the frontmatter and the user command or background skill choice.

## Two audiences, two vocabularies

Each sentence in this repo speaks to one of two readers:

- **The human** sees questions, Demo Cards, launch reports, `.vibe/` files, the README, the docs pages, and every user command's description. Write those in plain everyday words, using the project's wordbook.
- **The agent** reads the `SKILL.md` body and its sidecars. Write those with the strongest standard engineering word the model already knows: _red_, _green_, _vertical slice_, _tracer bullet_, _seam_, _one-way door_, _frontier_, _primary source_.

Keeping the agent's words technical is what lets the human's words stay plain. The translation happens at the moment of speaking to the human, never inside the skill.

## Context pointers

A **context pointer** is a line in the agent's context that names some material it has not loaded and says when to reach for it. A background skill's description is one; "Read `PUSHBACK.md` when the user says it is not what they meant" is another. The pointer's _wording_, not its target, decides when the agent reaches the material and how reliably. A must-have target behind a weak pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

A pointer does two jobs: say what the material is, and name each **branch** that should trigger it (a branch is a distinct case, so different runs take different paths). An always-loaded pointer costs on every turn, so prune it harder than any body:

- **Front-load the leading word.** The pointer is where it triggers.
- **One trigger per branch.** Three synonyms for one case are one branch written three times.
- **Cut what the body already says.**

## The two loads

Every line you add spends one of two budgets:

- **Context load**: always-loaded material (a background skill's description, a `CLAUDE.md` line) sits in the agent's window every turn, spending tokens and attention whether or not it fires.
- **Cognitive load**: the human is the index of the commands they must remember. Spend it only where human judgement matters. For this repo's users, it is the scarcer budget of the two, which is why there are few commands and one router.

## Information hierarchy

A document holds **steps** (what the agent does, in order) and **reference** (rules and facts consulted on demand). Each piece sits on a ladder, ranked by how soon the agent needs it:

1. **In-file step**: the primary tier.
2. **In-file reference**: consulted on demand. A flat set of peer rules is fine.
3. **Disclosed reference**: pushed to a sidecar in the same folder, reached by a pointer that names the condition ("Read `X.md` when ...").

**Progressive disclosure** is moving material down the ladder so the top stays legible. The cleanest test is branching: inline what every run needs, disclose what only some runs reach. Reference left inline buries the steps and makes attending to them a coin-flip.

**Co-location** is the within-file companion: keep a concept's definition, rules, and caveats under one heading, so reading one part brings its neighbours.

**Sprawl** is the failure: a document simply too long, even when every line is live. Attention thins across the excess. Cure it with the ladder, and by splitting.

## Steps end on a done-when

Every step ends on a **completion criterion** the agent can check. Two properties make it a lever:

- **Clarity.** "Done when the check is red for the reason the user described" can be checked; "once you understand the bug" invites **premature completion**, where attention slides to the steps still ahead. Sharpen the criterion first. Only if it stays fuzzy and you see the rush, hide the later steps by splitting the sequence across a real context boundary (a fresh chat or a helper).
- **Demand.** "Every line of What People See and Do accounted for" forces digging that "list what changed" does not. Demand drives **legwork** without a separate step telling the agent to dig, and it binds flat reference as well as steps ("every smell checked").

The strongest criteria are both checkable and exhaustive.

## When to split

Splitting spends one of the two loads, so split only when the cut earns it:

- **By sequence**: when the steps after the current one tempt the agent to rush it. `/ask-me` → `/freeze-plan` → `/build-step` is that cut.
- **By invocation**: split off a background skill only when the agent must reach it on its own, or more than one command must call it. It pays context load for its description, so the independent reach has to be worth it.

If the behaviour composes from existing skills, it does not get a new one.

## Leading words

A **leading word** is a compact concept already in the model's pretraining that the agent thinks with while it runs the document: _frontier_, _tracer bullet_, _tight_, _red_. Repeated as a token, never re-explained as a sentence, it anchors a whole region of known behaviour for one word. A home-made word recruits nothing and must be defined; reach for an existing word first.

Hunt for passages a leading word would collapse: a triad spelt out at three sites ("fast, steady, runnable alone" is _tight_), a fuzzy gate that could be a binary state (the loop goes _red_ on the problem, or it does not).

## Say the target, not the forbidden thing

Naming a banned behaviour puts it in front of the model and makes it more available, not less. Write the behaviour you want ("ask about what people see, click, and pay for"). Keep a "never" only for a hard guardrail with no positive phrasing (a key pasted into chat), and pair it with the positive action.

## No arbitrary numbers

A cap ("at most 3 questions", "2 to 4 steps") replaces judgement with a number that is wrong for half the projects. Give the real criterion: ask the whole **frontier**; size a step so it fits one fresh chat and ends in something the user can click.

## Facts are the agent's job; decisions are the human's

Look things up before asking. Start every helper in a **fresh context window** (some harnesses fork the conversation by default, which defeats the point), and do not block on it: only the questions that depend on its answer wait.

Every question carries a recommended answer, worded so "yes" accepts it. Technical choices that are easy to undo are the agent's own, recorded only when they would surprise the user later.

## Harness-neutral

Skills run in Claude Code, Codex, Copilot, Cursor, and Gemini CLI. Ask questions as plain chat text. Refer to what the user typed after the command in words, not with a harness placeholder. Name helpers and tools generically.

## Pruning

- **One home per meaning.** Changing a behaviour is a one-place edit. Duplication costs tokens and upkeep, and inflates the meaning's rank on the ladder.
- **The project is a source of truth.** A document that restates what git, the folder layout, or a `.vibe/` file shows in one look is a **cache** that will go stale. Cache only what the agent cannot find by looking: the unwritten convention, the reason behind a choice.
- **Relevance.** A line loses it by never bearing on the task, or by going stale. Without pruning, the default fate is **sediment**: stale layers that settle because adding feels safe and removing feels risky. Delete stale lines in the same change that makes them stale.
- **No-ops.** Test each sentence: does it change what the model would do by default? If not, delete the whole sentence. A word too weak to beat the default (_be thorough_) is a no-op too; the fix is a stronger word (_relentless_).
- After any change, update the router (`skills/what-next/`) if a command was added, renamed, or now fits the flow differently. A router that names a missing command, or misses a real one, misleads the user.

## Punctuation

No em-dashes or en-dashes. Rewrite the sentence with a comma, colon, period, or parentheses, whichever it actually wants; never swap the character for a hyphen.
