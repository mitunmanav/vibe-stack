---
name: launch-check
description: "Run a pre-flight safety audit for exposed secret keys, private data leaks, and irreversible changes, and walk through outside account setup."
disable-model-invocation: true
---

# Launch Check

Audit the entire project for hidden safety, privacy, and cost risks before the user shares or publishes their app, and guide any external account connections without ever exposing secret keys in chat.

## 1. Run deterministic safety and cleanliness scans

1. Run the `auditing-work` skill across the full project.
2. Run four mandatory pre-flight checks:
   * **Secret Key Scan:** Search all tracked files for hardcoded API keys, tokens (`sk_`, `pk_live_`, `AIza`, `ghp_`, `Bearer`), or `.env` files missing from `.gitignore`.
   * **Private Data & Access Rules Check:** Verify that personal records (names, emails, phone numbers, medical/allergy notes, addresses, or payment details) are never stored in publicly served browser folders (`public/`, `dist/`, static client files) and that database access rules block uninvited visitors from reading or editing private rows.
   * **Debug Leftover Scan:** Confirm zero `[TRACE-` markers or broken console errors exist.
   * **One-Way Choice Audit:** Classify whether launching this version involves any **Irreversible Choice** (deleting saved user data, charging real credit cards, or publishing private records) versus a **Reversible Choice** (safe to undo anytime).

## 2. Generate the Pre-Flight Safety Card and Service Guide

1. Save a readable summary report to `.vibe/previews/launch-report.html` showing Green/Red badges in plain English for: **1. Secret Keys Protected**, **2. Private Data Locked Down**, **3. All Automated Checks Passing**, and **4. Undo Difficulty (Reversible vs. Irreversible)**.
2. If the app needs outside accounts or secret keys configured (like Stripe, Supabase, email sending, or a custom domain), read `SERVICE-SETUP-TEMPLATE.md` and generate `.vibe/service-setup-steps.md`.
3. **Hard Gate:** If any secret key is exposed, any private data is unlocked, or any Irreversible Choice is detected, **stop with a `⚠️ Why this matters` warning** and offer to fix the safety gap before the user launches.
