---
name: mt-platform-accounts
description: "Platform URLs and the identical-email requirement across Vercel, Feather (via LinkedIn), and Slack"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 245c96c2-20a4-4909-b2a6-fe539a64b62a
  modified: 2026-08-13T19:22:00.870Z
---

Interactive Preference Multi-Turn platforms:

- **Vercel / Data Annotation Platform** — https://annotation-platform-henna.vercel.app/ — claim
  tasks here first, submit here last.
- **Feather** — https://msft.feather-prod.azure.com/ — log in with **"Log In with LinkedIn"**;
  this is where prompts are written and responses chosen.
- **General onboarding** — https://annotation-hub.vercel.app/onboarding
- LinkedIn primary-email settings — https://www.linkedin.com/mypreferences/d/manage-email-addresses

Hard requirements: the LinkedIn **primary** email must match the email he was invited with, and
the Vercel, Feather, and Slack emails must all be identical. Slack is the only official
communication channel; payment questions go to `#all-trainer-hub` (spelled `#all-trainner-hub` in
one doc — verify in Slack).

Order is invariant: **always Vercel → Feather.** Claiming directly in Feather risks offboarding
and makes the task non-billable. See [[interactive-preference-multiturn]] and
[[mt-attempt-url-hidden-step]].
