---
name: launch-check
description: "Before you share or publish your app: check for exposed secret keys, private information anyone could see, and one-way doors, and get a plain guide for connecting outside accounts."
disable-model-invocation: true
---

# Launch Check

Before the app reaches other people, find anything that would leak a secret, expose someone's private information, or cost money or data in a way that cannot be taken back.

## 1. Review the whole build

Run the full check command from `.vibe/config.md`. Then call the Skill tool with "auditing-work", naming `restore/project-start` as the Save Point and every plan in `.vibe/specs/`.

## 2. Check what a single change cannot show

- **Secrets, now and in history.** Search every tracked file and the full git history (`git log -p`) for keys and tokens (for example `sk_live_`, `pk_live_`, `AIza`, `ghp_`, private key blocks, passwords in connection strings). A key that was ever committed counts as exposed once the project is shared, even if it was deleted later.
- **Private information.** Visit the app as a stranger and as a second user. Personal details (names, emails, phone numbers, addresses, health notes, payment details) must be reachable only by the people allowed to see them, and must not sit in folders the browser can load directly.
- **One-way doors.** List what launching this version would do that cannot be taken back: charging real cards, sending real emails, deleting or overwriting saved data, making private records public.

Done when each of the three has a result: clear, or the exact files, pages, or actions involved.

## 3. Report and gate

Write `.vibe/previews/launch-report.html`: one green or red badge each for **Secret keys protected**, **Private information locked down**, **All automated checks passing**, and **One-way doors** (none, or each one listed), each with one plain sentence. Open it if you can and print its path.

If any badge is red, stop with a `⚠️ **Why this matters:**` line in plain words and offer to fix it. A key found in history needs a new key from the service as well as the cleanup; say so plainly.

## 4. Outside accounts

If the app needs an outside service (payments, email, a hosted database, hosting, a domain), read `SERVICE-SETUP-TEMPLATE.md` and write `.vibe/service-setup-steps.md`.
