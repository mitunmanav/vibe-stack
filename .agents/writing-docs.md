# Writing docs pages

Every skill has a human-facing **docs page** at `docs/<skill-name>.md`. The page is not the skill and not a copy of `SKILL.md`. It is written for the person using Vibe Stack, who does not read code, so it uses plain everyday words throughout.

Most skills here are user commands: the agent will never fire them on its own, so the person is the index that has to remember they exist and when to type them. That memory is **cognitive load**, and the page exists to relieve it: orient one reader around one command, so they can hold it in their head, know when to reach for it, and see where it sits. Together the pages are a spread-out router; each is one node, and `/what-next` is the whole map.

Act whenever a skill is added, renamed, or changes behaviour: create or re-sync its page in the same change. A rename moves the file too. A removed skill keeps its page, opened with a blockquote (`> **Removed in 1.2.0.** Use /other instead.`), so old links keep working.

There is no H1: the file name is the title.

## Page structure

Fill the template below, in its order. The **fixed frame** (`## What it does`, `## When to reach for it`, `## Where it fits`) appears on every page. `## Before you start` and the free-form middle carry only what this skill needs; delete the rest.

Four sections make a page worth reading: `What it does`, `When to reach for it`, `Common questions`, and `It's working if`. A page with neither of the last two is unfinished, not finished-and-short.

A page carries no install commands. Those live in the README, copied from [install-block.md](./install-block.md).

<page-template>

## What it does

One or two plain paragraphs. Lead with the command's one-sentence job, then the **defining constraint**: the single fact that makes it behave differently from what a person would expect (for `/freeze-plan`: it does not ask you everything again, it writes down what you already agreed). Write it as a plain sentence, never as a labelled aside like "The key thing:".

## When to reach for it

Two beats:

- **Who starts it.** A user command: "You start this by typing `/<name>`; the agent won't run it on its own." A background skill: "You never type this. The agent reaches for it when ..., and some commands call it for you."
- **The moment.** "Reach for this when ...". Where it is easy to confuse with a sibling, add the other half: "for X instead, type `/sibling`."

## Before you start

Optional. Only when something must already be in place: `/start-project` has run, a plan is saved, a step is built. Omit the heading otherwise.

## <free-form middle>

One to three short sections in the command's own words that make it click: the loop it runs, what it leaves behind, the one mistake it prevents. Surface its **leading idea** (a Save Point, a Playable Step, a loop that goes red, the frontier of questions) so the reader learns the word they will later think with.

## Common questions

Real questions, each in bold with the answer beneath it. An observed question beats an invented one, so hunt first: this repo's issues (`gh issue list --repo mitunmanav/vibe-stack --search "<name>" --state all`) and `CHANGELOG.md` (anything renamed or changed raises "where did it go?"). Where the hunt comes up thin, carry only the questions a reader would plainly ask, and keep the count honest: one or two beats six padded ones. Say the unflattering thing where it is true. Omit the heading if nothing is worth answering.

## It's working if

A few bullets the reader can check on their own screen, without opening `SKILL.md`. "A Demo Card opens and all three things work" passes; "the step file has a Status line" does not.

## Where it fits

Always present. One or two sentences:

- **Role**: a step on the main flow (`/ask-me → /freeze-plan → /build-step → /launch-check`), a run-once setup (`/start-project`), upkeep (`/tidy-up`), or an any-time standalone (`/plain-english`, `/undo`).
- **Neighbours**: the one or two commands that matter, each with a because-clause.
- **The map**: point to `/what-next`, so the page never redraws the whole flow.

</page-template>

## Conventions

- Explain the **why**, not the steps. A person choosing a command does not need the runbook.
- Plain words only. Where an idea needs a name, use the repo's own word from [WORDS.md](../WORDS.md) (Save Point, Playable Step, Demo Card, one-way door) and explain it once.
- **Branches go in a table or a list**, never a paragraph: the reader is scanning for the one row that matches them.
- Links are relative: `[/undo](./undo.md)`.
- Keep the page itself low-load. Spare headings and restated links are the clutter it argues against.

## Done when

- The page exists at `docs/<name>.md`, and no stale page survives a rename.
- `## What it does` states the defining constraint as a plain sentence.
- `## When to reach for it` says who starts it and the moment to reach for it.
- `## Where it fits` names the role and points to `/what-next`.
- The middle surfaces the leading idea.
- `## Common questions` is sized to what the hunt found.
- Every `## It's working if` bullet is checkable on the reader's own screen.
- Every multi-way branch is a table or a list, and the sections appear in the template's order.
