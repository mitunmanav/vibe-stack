# Contributing

Every issue is judged against the bar in [`SCOPE.md`](./SCOPE.md). Read it first.

## Where each request goes

| You have | Go to |
| :--- | :--- |
| A command that did the wrong thing | [Bug issue](https://github.com/mitunmanav/vibe-stack/issues/new?template=bug.yml) |
| A change to an existing command | [Idea or feedback issue](https://github.com/mitunmanav/vibe-stack/issues/new?template=idea.yml) |
| An idea for a new command | Read [`new-commands.md`](./.out-of-scope/new-commands.md) first, then an idea issue if it still clears the bar |

You do not need to read code to file a good issue. What you typed, what happened, and what you expected is all it takes.

## Issues written with AI

Your assistant is welcome to help, but you post the issue, so you own it:

- **One problem per issue.** Several things from one session are several issues, or none.
- **Short.** If it does not fit on one screen, cut it.
- **What happened first.** The steps that show the problem come before any analysis.
- **No pasted rewrites.** No full proposals or rewritten `SKILL.md` files. Describe the problem; the fix is ours to design.
- **Not your app's issues.** If your assistant files bugs in the app you are building here, it has the wrong repo.

## Changing the skills

Read [`CLAUDE.md`](./CLAUDE.md), then [`.agents/writing-skills.md`](./.agents/writing-skills.md). Run `npm run check` until it prints SUCCESS, and add a changeset (`npx changeset`) that names the failure the change fixes.
