# Same Chat or Fresh Chat

A **phase** is one chunk of work: the interview, building one step, one repair. The **boundary** between two phases is the only place to choose; mid-phase there is nothing to decide, so keep going.

Work top to bottom. The first yes wins.

1. **Does the next command read this chat?** `/freeze-plan` reads the interview it follows; `/look-back` reads the trouble it looks back on. Then stay. The chat is the **primary source**: the reasons behind every answer, which no summary keeps whole.
2. **Is everything in this chat already saved somewhere?** Each `/build-step` works from its step file, and every answer from `/ask-me` is in `.vibe/DECISIONS.md`. Then `/clear`. It costs nothing and gives the next command a clean, sharp start.
3. **Has the chat grown long and still matters?** Long chats get worse: the agent forgets earlier details and answers less sharply. The signs a user can see are slow replies, repeated questions, and the agent forgetting something already settled. Then finish the current command, make sure its answers are written into `.vibe/`, and `/clear`.
4. **Otherwise, stay.**

The cost of a wrong `/clear` is one-way: clearing a chat that holds unsaved reasons loses the **why**, and reading the app back does not return it. That is why the first question rules out staying before anything else.

Tell the user the choice as one plain clause, for example: "Type `/clear` first, because the step file already holds everything the builder needs."
