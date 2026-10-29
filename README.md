# Vibe Stack: Build Real Software Using Plain Everyday Words

**Vibe Stack** is a toolkit for AI coding assistants (like Claude Code, OpenAI Codex, GitHub Copilot in VS Code, Cursor, and Gemini CLI) designed from the ground up for **non-technical creators**.

You describe what you want in plain words. The AI handles the technical decisions behind the scenes, shows you clickable visual options in your web browser, builds your project one playable step at a time, and creates automatic save points so you never get stuck with a broken app.

## What Problem Does This Solve?

When you use an AI coding tool without Vibe Stack, four frustrating things happen:
1. **The AI guesses wrong or asks you programmer riddles:** It either starts building before it understands your idea, or asks you confusing questions about "databases", "frameworks", and "APIs".
2. **You get walls of technical jargon:** The AI explains its work in programmer language you cannot verify.
3. **The "Death Loop" breaks your working app:** You ask for one small tweak, the AI breaks three other screens, and you have no easy way to undo it.
4. **Hidden safety and cost traps:** The AI accidentally leaves secret keys in public files or connects paid cloud services before you have even tried a free version on your computer.

Vibe Stack fixes all four by putting a **Translator Layer** between you and the AI:
* **The AI decides the code details silently** and writes what it chose in a plain-English log (`.vibe/DECISIONS.md`) that you can overrule anytime.
* **You only answer everyday questions** about what people see, click, and experience - and every question comes with a recommended default (`➡️`) so you can simply reply `"yes"`.
* **You judge clickable results, never code:** After every step, the AI opens a **Demo Card** in your browser with a 30-second "Try It Yourself" checklist.

## 30-Second Install (Pick Your Tool)

### Option 1: Claude Code
Run these two commands inside Claude Code:
```text
/plugin marketplace add ./vibe-stack
/plugin install vibe-stack@vibe-stack-catalog
```

### Option 2: Universal Installer (Works with Claude Code, Codex, Cursor, Copilot, OpenCode)
In your terminal, run:
```bash
npx skills add ./vibe-stack
```

### Option 3: OpenAI Codex / GitHub Copilot (VS Code) / Gemini CLI
Copy or link the `skills/` folder into your project or home folder:
```bash
# For OpenAI Codex or Gemini CLI (in your project folder):
mkdir -p .agents/skills && cp -r ./vibe-stack/skills/* .agents/skills/

# For VS Code / GitHub Copilot (in your project folder):
mkdir -p .github/skills && cp -r ./vibe-stack/skills/* .github/skills/
```

## Your First 5-Minute Walkthrough (Exact Words to Type)

Open your AI assistant inside an empty folder (or an existing project folder) and follow these 5 simple steps:

### Step 1: Set up your project folder (once per project)
Type:
```text
/start-project I want a simple booking page where dog owners can book a 30-minute grooming slot.
```
*What happens:* The AI checks your folder, summarizes your idea in two plain sentences, and asks if that summary is right (`➡️ Yes`). Reply `yes`, and it creates your `.vibe/` workspace and first Save Point.

### Step 2: Shape your idea in plain English
Type:
```text
/ask-me
```
*What happens:* The AI asks you 1 to 3 short, everyday questions at a time (for example, whether bookings are for one dog at a time, or what info an owner must type). Every question has a recommended answer (`➡️`) so you can just reply `yes` or tell it what you prefer. If a screen layout needs choosing, it automatically opens clickable visual options in your browser!

### Step 3: Freeze your plan into playable steps
When you and the AI agree on the idea, type:
```text
/freeze-plan
```
*What happens:* The AI turns your conversation into a short, jargon-free plan and breaks it into 2 to 4 **Playable Steps** (where each step ends with something real you can click and try). Reply `yes` to lock it in, then type `/clear` to give the AI a fresh, fast memory window.

### Step 4: Build one playable step at a time
Type:
```text
/build-step 01
```
*What happens:* The AI automatically saves a **Save Point**, writes an automated self-test first, builds Step 01, checks its own work with two separate quality helpers, and opens a **Demo Card** in your browser showing 3 things to click and try. Repeat `/clear` and `/build-step 02` for the next step!

### Step 5: Check safety before sharing with the world
When your app is working the way you want, type:
```text
/launch-check
```
*What happens:* The AI scans your project to make sure no secret keys or private data are exposed, warns you in plain English about any irreversible changes, and gives you a simple step-by-step guide if you need to connect an outside account.

## What to Type When You Get Stuck or Change Your Mind

You only ever need three rescue commands:

| When This Happens | Exact Command to Type | What the AI Does |
| :--- | :--- | :--- |
| **The AI used confusing jargon, or you aren't sure what command to run next** | `/plain-english` | Re-explains the last message in simple everyday words, shows any recent choices the AI made behind the scenes so you can change them, and tells you the exact next command to type. |
| **Something looks broken or a button stopped working** | `/repair the Save button does nothing when I click it` | Saves a safety snapshot, reproduces the problem without guessing random fixes, repairs the root cause, and cleans up after itself. |
| **You hate the last change and want to go back to when it worked (or want to pause for the day)** | `/undo` | Lets you roll your app back to your last working Save Point in one step, or saves a compact handoff note so you can close your laptop and pick up tomorrow. |

## All 8 Commands at a Glance

* **`/start-project`** - Set up your `.vibe/` folder, project wordbook, and first Save Point.
* **`/ask-me`** - Clarify your idea through short, plain-English questions with `"yes"` defaults and clickable browser previews.
* **`/freeze-plan`** - Lock your agreed idea into a jargon-free plan and bite-sized Playable Steps.
* **`/build-step`** - Save a restore point, build and self-test one Playable Step, and open a live Demo Card to try.
* **`/repair`** - Fix a broken screen or behavior scientifically without breaking the rest of your app.
* **`/launch-check`** - Check for exposed secret keys, privacy risks, and irreversible changes before launching.
* **`/plain-english`** - Translate jargon, overrule a behind-the-scenes AI decision, or see what command to run next.
* **`/undo`** - Roll back to a working Save Point, or save a handoff note before clearing chat.
