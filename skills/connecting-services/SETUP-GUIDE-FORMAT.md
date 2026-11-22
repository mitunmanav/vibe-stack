# Setup Guide Format

`.vibe/service-setup-steps.md` is numbered stages, one service task per stage. The user only clicks in dashboards and pastes into one file; you do everything else.

## Before the first stage

Make sure `.gitignore` covers `.env.local`, then create `.env.local` with one empty line per key the app needs (`STRIPE_SECRET_KEY=`).

<setup-guide-template>

```markdown
# Connecting <service names>

You'll click through <N> short stages. Each one ends with me checking it worked.

## Stage 1 of <N>: <plain task, e.g. "Get your Stripe test key">

1. Open <exact page URL>.
2. Click <button> -> <button> -> <button>.
3. Copy the value labelled **<label>**.
4. Open `.env.local`, paste it after `STRIPE_SECRET_KEY=`, and save.
5. Reply `done`.

⚠️ **Why this matters:** <only on a stage that could cost money or expose data>
```

</setup-guide-template>

## Rules

- **Paste into the file, never into chat.** A key pasted into chat has to be treated as exposed and replaced. If one arrives in chat anyway, say so plainly and walk the user through making a new one.
- **Check without looking.** Confirm a key is filled in without printing it (for example `grep -c '^STRIPE_SECRET_KEY=.' .env.local`), then test the connection.
- **One task per stage**, so nothing the user needs scrolls out of view.
