---
name: connecting-services
description: "Plain, click-by-click guide through the outside-service steps only the user can take: accounts, dashboards, and secret keys. Use when the app needs a key, an account, or a dashboard setting the agent cannot reach."
user-invocable: false
---

# Connecting Services

Some steps only a person can take: making an account, clicking through a payment or email provider's dashboard, copying a secret key. This skill turns each one into a numbered **stage** the user follows by clicking and pasting, while you do everything else and check every stage yourself.

If you could do a step yourself (installing a package, writing a config file, running a command), do it. This skill is only for the wall a human has to pass.

## 1. Scope the stages

Read the app first, then ask: every key the code reads (`.env.example`, the config files, every place the code reads a setting) is a value some stage must produce. List the stages in the order they depend on each other, one service task each, and show the list to the user in plain words.

Done when every stage is named in order, and for each value you know (a) where the user gets it, (b) which line of `.env.local` it fills, and (c) whether it is secret.

## 2. Map each stage's clicks

For each stage, write the exact path a person follows: which page to open, what to click, where the value appears ("Developers -> API keys -> Reveal test key -> Copy"). Turn on the free tier, test mode, or a spending limit before anything that could bill, and mark that stage as a one-way door with a `⚠️ **Why this matters:**` line.

Where you do not know a service's current screens, say so and check its own documentation rather than invent buttons. Done when a stranger could follow every stage.

## 3. Write the guide and walk it together

Read `SETUP-GUIDE-FORMAT.md` and write `.vibe/service-setup-steps.md`. Open the first stage's page for the user if you can, and take the stages one at a time: after each, check it without printing the key, test the connection, and say the result in one plain sentence before the next.

Done when every key the app reads is filled in, and every stage ends in a check you ran.
