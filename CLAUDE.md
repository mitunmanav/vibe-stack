# Maintaining Vibe Stack

Vibe Stack is a set of skills for people who cannot read code. Every change is judged against [SCOPE.md](./SCOPE.md). The words this repo uses for its own ideas (Playable Step, Save Point, Demo Card, one-way door) are defined in [WORDS.md](./WORDS.md).

- Before you add, change, or review a skill or a steering file, read [.agents/writing-skills.md](./.agents/writing-skills.md). It holds the writing rules, including the split between plain words for the human and engineering words for the agent.
- Skills live one level deep, `skills/<name>/SKILL.md`, and both plugin manifests list every skill folder by name. [ADR 0001](./.agents/adr/0001-flat-skills-two-manifests.md) records why.
- Each skill is a user command or a background skill. The flags, the rule that no skill calls a user command, and how one skill calls another live in [.agents/invocation.md](./.agents/invocation.md).
- Every skill that starts a helper says to start it in a fresh context window. Some harnesses fork the chat by default, and a fork inherits exactly the context the helper was meant to escape.
- Every skill has a plain-words docs page at `docs/<name>.md`. When a skill is added, renamed, or changes behaviour, create or re-sync its page following [.agents/writing-docs.md](./.agents/writing-docs.md).
- [`what-next`](./skills/what-next/SKILL.md) is the router over every user command. When a command is added, renamed, removed, or fits the flow differently, update its `SKILL.md` and `FLOW-MAP.md` and the README in the same change: a router that names a missing command, or misses a real one, misleads the user.
- Install wording is copied from [.agents/install-block.md](./.agents/install-block.md) and nowhere else. Run `claude plugin validate .` after touching a manifest.
- Every user-facing change gets a changeset (`npx changeset`) naming the failure that caused it. The Release workflow turns them into `CHANGELOG.md` and the version bump.
- No em-dashes or en-dashes anywhere. Rewrite the sentence with a comma, colon, period, or parentheses; never swap in a hyphen.
- Run `npm run check` after every edit. Done when it prints SUCCESS.
- To try the skills locally, run `scripts/link-skills.sh`. Each entry is a symlink into this repo, so edits show up at once; re-run it after adding, removing, or renaming a skill.
