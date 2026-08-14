# memory/ — saved Claude Code auto-memory for this project

These are the memory files Claude Code wrote while working this project on the first laptop.
They are kept in the repo so the context travels; Claude Code does not read them from here.

To make them active on a new machine, copy the `.md` files (this README excluded) into
`~/.claude/projects/<slugified-repo-path>/memory/`. Finding that path and the copy commands:
[../SETUP.md](../SETUP.md) step 4.

Skipping it costs nothing critical — `CLAUDE.md` and `PROJECT_KNOWLEDGE.md` carry the same facts.
The memory files just make them recallable without a read.

## Index

| File | What it records |
|---|---|
| `MEMORY.md` | the index Claude Code loads each session |
| `interactive-preference-multiturn.md` | what the project is and where the reconciled manual lives |
| `mt-turn-count-conflict.md` | the stale single-turn text; 10 is a hard floor, padding is removal |
| `mt-attempt-url-hidden-step.md` | the billing-critical step that exists only inside a flowchart image |
| `mt-never-ai-write-prompts.md` | superseded 2026-08-14 — AI drafting now allowed if humanized |
| `mt-prompt-drafting-checklist.md` | check the doc's style rules, then run the humanizer, every turn |
| `mt-platform-accounts.md` | Vercel / Feather / LinkedIn URLs and the identical-email requirement |
| `mt-legacy-system-stale-and-off-limits.md` | why `Interactive_contri_inst/` is reference-only |

## Caveats

- Several entries contain **absolute paths from the original laptop**
  (`c:\Users\Suraj\Downloads\project_interactive_linkedin\…`). Read them as pointers to
  repo-relative files, not as working paths.
- Entries are **timestamped snapshots of what was true when written**. Where one disagrees with
  `PROJECT_KNOWLEDGE.md` or `system/rules/`, those win — they are maintained; these are a log.
