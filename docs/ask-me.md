## What it does

`/ask-me` takes a rough idea and keeps interviewing you until both of you hold the same picture of it. It asks in **rounds**: each round is every question that can be asked right now, numbered, each with a recommended answer (marked `➡️`). So "yes" is always a complete answer.

It only asks what you can actually answer: what people see, click, type, and pay for. The technical details (how the app is built, where things are stored) it decides itself, and writes down the ones you might want to change later.

## When to reach for it

You start this by typing `/ask-me`; the agent won't run it on its own. Reach for it whenever you have something new: a first idea, a new feature, a change to how something works. Vagueness is not a reason to wait, because the interview exists to remove it.

Run [`/start-project`](./start-project.md) first.

## Three kinds of question

| Kind | Example | What the agent does |
| :--- | :--- | :--- |
| How it's built | "Which database?" | Decides itself, and records it if you'd be surprised later |
| What people experience | "Can one owner book for several dogs at once?" | Asks you, with a recommendation |
| A **one-way door** | "Take real card payments now?" | Asks you, opens with `⚠️ Why this matters`, and waits for an explicit yes |

When a question is easier to see than describe, it opens clickable options in your browser instead.

## It's a conversation, not a form

You own the idea. The failure mode is answering "yes, yes, yes" to every question and ending up with a plan the agent wrote and you nodded at. Push back on a recommendation that doesn't fit. Say "I don't know" and mean it. Say when it's asking about something you don't care about.

Along the way it keeps a **wordbook** (`.vibe/WORDS.md`) of the words for your screens, people, and things, and points out when one word is doing two jobs. Those words then show up on the buttons and in every later message.

## Common questions

**It asked a lot of questions. Is something wrong?**
Usually the idea is big. If the questions are about things you can answer, it's working. If they're technical and you can't answer them, say so: those are the agent's to decide. For a very big idea, it asks which one part must work first and parks the rest in `.vibe/LATER.md`.

**I closed the chat halfway. Do I start over?**
No. Every answer is saved after each round. Type `/ask-me` again and it carries on from where you stopped.

**Someone else knows the answer, not me.**
Say so. It writes a short question sheet for that person in `.vibe/`, and you bring their answers back.

## It's working if

- Every question is about something you can see, click, or pay for.
- Later rounds clearly build on what you said earlier.
- You disagreed with at least one recommendation.
- It ends by summing up the idea and asking whether it matches what you pictured.

## Where it fits

A **step on the main flow**, right after [`/start-project`](./start-project.md). Type [`/freeze-plan`](./freeze-plan.md) next, in the **same chat**, because it writes down what you just agreed. For the full map, type [`/what-next`](./what-next.md).
