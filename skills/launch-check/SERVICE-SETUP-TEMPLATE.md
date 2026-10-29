# Safe External Service Setup Guide (`SERVICE-SETUP-TEMPLATE.md`)

When the user needs to connect an outside service (payments, email, cloud database, or hosting), write `.vibe/service-setup-steps.md` following three strict safety laws:

1. **Never ask the user to paste a secret key into the AI chat window.** Instruct them to paste keys directly into `.env.local` (after verifying `.env.local` is listed in `.gitignore`).
2. **Idempotent stage checks:** For each service stage (e.g., *Stage 1: Create `.env.local` placeholder*, *Stage 2: Check key name exists without printing its secret value*, *Stage 3: Test connection*), provide a safe 1-line check command that checks whether the variable name is set (`[ -n "$KEY" ]`) without ever echoing the secret string.
3. **Plain-English dashboard clicks:** Tell the user the exact button names to click in the external dashboard and what free tier or spending limit to turn on first so they never get a surprise bill.
