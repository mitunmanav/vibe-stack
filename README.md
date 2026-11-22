# Vibe Stack

[![Version](https://img.shields.io/badge/version-1.1.0-blue)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

Agent skills for people who don't read code, but still want to build real software.

Vibe coding is fun right up until it isn't. The agent builds something you didn't ask for, explains it in words you can't follow, breaks the thing that worked yesterday, and leaves a secret key where anyone can find it. You can't read the code, so you can't catch any of it.

These skills fix that by doing what good engineers do, and keeping all of it out of your way. You talk about what people see, click, and pay for. The agent makes the technical calls, writes them down in plain words, builds in small steps you can click through, and takes a Save Point before every change so nothing is ever lost.

They work in Claude Code, Codex, Copilot, Cursor, Gemini CLI, and more. They're small, and they're yours to adapt.

## Installation (30-second setup)

Pick one route per assistant. Installing through two routes gives you every command twice.

### 1. Get the skills

<details>
<summary><strong>Claude Code</strong></summary>

Type these into Claude Code, one at a time:

```text
/plugin marketplace add mitunmanav/vibe-stack
/plugin install vibe-stack@vibe-stack-catalog
```

</details>

<details>
<summary><strong>Any other assistant</strong> (Codex, Cursor, Copilot, Gemini CLI, OpenCode, and more)</summary>

```bash
npx skills@latest add mitunmanav/vibe-stack
```

To update later, run `npx skills@latest update`.

</details>

### 2. Run `/start-project`

Open your assistant in an empty folder (or an app you already have) and type:

```text
/start-project I want a simple booking page where dog owners can book a 30-minute grooming slot.
```

It will:

- Sum up your idea in two sentences and check it with you
- Set up a tiny app that starts and checks itself
- Take your first Save Point

### 3. Bam, you're ready to go.

Type `/ask-me` and describe the first thing you'd like the app to do. Whenever you're unsure what comes next, type `/what-next`.

## Why These Skills Exist

I built these to fix the ways coding agents fail people who can't read what they write.

### #1: The Agent Built The Wrong Thing

> "The most important single aspect of software development is to be clear about what you are trying to build."
>
> Bjarne Stroustrup

**The Problem**: You describe your idea, the agent nods, and an hour later you're looking at something you never asked for. The agent didn't understand you. Worse, it asked you a pile of technical questions you couldn't answer, so it guessed.

**The Fix** is an interview that only asks what you can actually answer: what people see, click, type, and pay for. Every question comes with a recommended answer (marked `➡️`), so "yes" is always enough. The agent decides the technical details itself.

- [`/ask-me`](./skills/ask-me/SKILL.md) interviews you, a round of questions at a time, until every branch of the idea is settled
- When a choice is easier to see than describe, it opens clickable options in your browser
- [`/freeze-plan`](./skills/freeze-plan/SKILL.md) then writes down what you agreed, without asking again

Use `/ask-me` every time you want something new. It's the one I'd never skip.

### #2: I Can't Understand A Word It Says

> "Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent."
>
> George Orwell, _Politics and the English Language_

**The Problem**: Agents talk like engineers. When you can't check what they're saying, every explanation is a leap of faith.

**The Fix** is a shared language. As you talk, the agent keeps a **wordbook** (`.vibe/WORDS.md`) of the words for your screens, your people, and your things, and uses them everywhere: in chat, on the buttons, in the code. Every choice it made for you goes in a **decision log** (`.vibe/DECISIONS.md`) in plain words, and you can change any of them by asking.

And when a message still doesn't land, type [`/plain-english`](./skills/plain-english/SKILL.md). The agent says it again, in your words, with an example from your own app.

### #3: It Worked Yesterday. Now It Doesn't.

> "A complex system that works is invariably found to have evolved from a simple system that worked."
>
> John Gall, _Systemantics_

**The Problem**: The agent changes ten things at once, something breaks, and you have no way back. Then it tells you everything works.

**The Fix** is small steps, real checks, and a way back from anything:

- [`/build-step`](./skills/build-step/SKILL.md) builds one **Playable Step** at a time: a thin slice that ends in something you can open and click. It writes an automated check, watches it fail, then builds until it passes. Two fresh helpers review the work. Then you get a **Demo Card** with three things to try.
- Before every change, the agent takes a **Save Point**. [`/undo`](./skills/undo/SKILL.md) takes you back to any of them, tells you exactly what going back removes, and can itself be undone.
- When something breaks, [`/repair`](./skills/repair/SKILL.md) makes the problem happen on demand before it touches anything, then fixes the real cause with a check that keeps it fixed.

### #4: It's Not Safe To Share

> "Trust, but verify."
>
> Russian proverb

**The Problem**: Secret keys end up in public files. One person's details show up for another. A paid service gets switched on before anyone noticed.

**The Fix**: [`/launch-check`](./skills/launch-check/SKILL.md) looks for exposed keys (including in the project's history), visits the app as a stranger to check private information stays private, and lists anything that can't be taken back. You get a page of green and red badges, not a wall of text. Anything that costs money or touches private data is a **one-way door**: the agent spells out what will happen in the real world and waits for your yes.

### Summary

None of this is new. It's what careful engineers have always done: understand before building, use shared words, take small steps, check everything, keep a way back. These skills just do it for you, in plain words. Enjoy.

## Reference

These split on one axis: who starts them. **Commands** run only when you type them; their job is to run the show. **Background skills** never show in your menu: the agent reaches for them when the moment fits, and the commands call them for you.

### Commands

The main flow, in order:

- **[start-project](./skills/start-project/SKILL.md)**: Run once per project: set up the `.vibe/` folder, an app that starts and checks itself, and your first Save Point.
- **[ask-me](./skills/ask-me/SKILL.md)**: A relentless, plain-English interview that turns a rough idea into a shared plan, and keeps your project's words and decisions as it goes.
- **[freeze-plan](./skills/freeze-plan/SKILL.md)**: Turn what you agreed into a plain-English plan and a short run of Playable Steps.
- **[build-step](./skills/build-step/SKILL.md)**: Build the next Playable Step behind a Save Point, prove it works, and open a Demo Card with three things to try.
- **[launch-check](./skills/launch-check/SKILL.md)**: Before you share your app: check for exposed keys, private information anyone could see, and anything that can't be taken back.

Any time:

- **[what-next](./skills/what-next/SKILL.md)**: See where your project is, and the one command to type next. Start here after a break.
- **[plain-english](./skills/plain-english/SKILL.md)**: That last message didn't make sense: say it again in everyday words.
- **[repair](./skills/repair/SKILL.md)**: Something broken? Make it happen on demand, find the real cause, and fix it with a check that keeps it fixed. Example: `/repair the Save button does nothing`.
- **[undo](./skills/undo/SKILL.md)**: Take your app back to a Save Point. Your plan and decisions are kept, and the undo can itself be undone.

Beta (newer, with less real-world use):

- **[tidy-up](./skills/tidy-up/SKILL.md)**: Tidy the code behind the scenes so the app stays easy to change, without changing anything you see.
- **[look-back](./skills/look-back/SKILL.md)**: After a step or repair that went badly, find what would have prevented it and offer changes so it doesn't happen again.

### Background skills

- **[clarifying](./skills/clarifying/SKILL.md)**: The interview behind `/ask-me`: rounds of questions, each with a recommended answer, until every branch is settled.
- **[keeping-words](./skills/keeping-words/SKILL.md)**: Keeps the wordbook and the decision log sharp as you talk.
- **[showing-options](./skills/showing-options/SKILL.md)**: Builds a throwaway clickable preview when a choice is easier to see than describe.
- **[checking-behavior](./skills/checking-behavior/SKILL.md)**: The rules for automated checks that prove the app works: watched failing first, then passing.
- **[auditing-work](./skills/auditing-work/SKILL.md)**: Two fresh helpers review every change: one for safety and code quality, one for "did it build what the plan asked for?".
- **[connecting-services](./skills/connecting-services/SKILL.md)**: A click-by-click guide through the outside-service steps only you can take, like copying a payment key.

Every command has a plain-words page in [`docs/`](./docs/): what it does, when to reach for it, and how to tell it's working.

**Pausing work:** close the chat any time. Everything that matters is saved in `.vibe/` and your Save Points. To pick up, open a new chat and type `/what-next`.

## Feedback

If a command doesn't behave as described, please [open an issue](https://github.com/mitunmanav/vibe-stack/issues/new/choose) with what you typed, what happened, and what you expected. You don't need to read code to file a good one. See [CONTRIBUTING.md](./CONTRIBUTING.md) and [SCOPE.md](./SCOPE.md). Release notes are in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](./LICENSE)
