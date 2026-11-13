# Maintaining Vibe Stack

Vibe Stack is a set of skills for people who cannot read code. Every change is judged against [SCOPE.md](./SCOPE.md). The words this repo uses for its own ideas (Playable Step, Save Point, Demo Card, one-way door) are defined in [WORDS.md](./WORDS.md).

- Before you add, change, or review a skill, read [.agents/writing-skills.md](./.agents/writing-skills.md). It holds the writing rules, including the split between plain words for the human and engineering words for the agent.
- Skills live one level deep, `skills/<name>/SKILL.md`, so every harness finds them. [ADR 0001](./.agents/adr/0001-dual-manifest-plugin-packaging.md) records why.
- Each skill is a user command or a background skill. The flags, and the rule that no skill calls a user command, live in [.agents/invocation.md](./.agents/invocation.md).
- Every skill that starts a helper says to start it in a fresh context window.
- Install wording is copied from [.agents/install-block.md](./.agents/install-block.md) and nowhere else. Run `claude plugin validate .` after touching a manifest.
- When a user command is added, renamed, removed, or fits the flow differently, update the README and the router in `skills/plain-english/FLOW-MAP.md` in the same change.
- No em-dashes or en-dashes anywhere. Rewrite the sentence with a comma, colon, period, or parentheses; never swap in a hyphen.
- Run `python3 scripts/validate-plugin.py` after every edit. Done when it prints SUCCESS.
