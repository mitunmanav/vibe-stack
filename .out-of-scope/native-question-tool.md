# Asking questions through a harness's pop-up question tool

Vibe Stack asks its questions as plain chat text, numbered, each with a recommended answer. Requests to route them through a harness's built-in question picker are out of scope.

## Why this is out of scope

The skills run in Claude Code, Codex, Copilot, Cursor, Gemini CLI, and more. Each has a different question tool, or none. Naming one means a harness-specific branch in every skill that asks anything, or a skill that only works properly in one place.

A picker also changes the questions. It pushes toward short multiple-choice options, when the most useful answer is often in the user's own words ("the top of B with the list from C", "only the groomer can cancel"). Plain text keeps that open, and "yes" still accepts the recommendation in one word.

If you prefer your harness's picker, say so in the instructions file your own assistant reads. That is a one-line personal preference, and the shared skills do not need to know about it.

## Prior requests

None yet.
