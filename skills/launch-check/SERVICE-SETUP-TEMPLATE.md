# Outside Service Setup Guide (`SERVICE-SETUP-TEMPLATE.md`)

Write `.vibe/service-setup-steps.md` as numbered stages, one service task per stage, in the order they depend on each other. The user only clicks in dashboards and pastes into one file; you do everything else.

1. **Prepare the key file yourself.** Make sure `.gitignore` covers `.env.local`, then create `.env.local` with one empty line per key the app needs (`STRIPE_SECRET_KEY=`).
2. **Dashboard clicks, exactly.** For each key, give the page to open and the buttons to click, in order ("Developers -> API keys -> Reveal test key -> Copy"). Turn on the free tier, test mode, or a spending limit before anything that could bill. Where you do not know the service's current screens, say so and check its documentation rather than guess at buttons.
3. **Paste into the file, never into chat.** Tell the user to open `.env.local`, paste each key after its `=`, and save. A key pasted into chat has to be treated as exposed and replaced.
4. **Check without looking.** After each stage, confirm the key is filled in without printing it (for example `grep -c '^STRIPE_SECRET_KEY=.' .env.local`), then test the connection and report the result in one plain sentence.

Done when every key the app reads has a stage, and every stage ends in a check you ran.
