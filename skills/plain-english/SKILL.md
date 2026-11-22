---
name: plain-english
description: "Stop. That last message didn't make sense: say it again in everyday words."
argument-hint: "[optional: the part that lost you]"
disable-model-invocation: true
---

Hold on, I'm lost. I don't read code, so say that again for me: start with the bit of context I'm missing, then the point, in three or four short everyday sentences. Use the words from `.vibe/WORDS.md` if it exists, point at things I can see on my screen, and give me one example from my own app. If I typed something after the command, answer that first.

If you assumed something on my behalf that bears on this (an `AGENT` entry in `.vibe/DECISIONS.md`), tell me in one plain line so I can change it.
