# AGENTS.md

Rules for coding agents and humans who read or write this knowledge base. `CLAUDE.md` imports this file.

## Reading

1. Read [`index.md`](index.md) first. It maps tracks, projects and recent findings.
2. Before you start work on a track, read its file in `tracks/` and every finding that names it: `grep -l "^track: <slug>" findings/*.md`.
3. Treat a finding's `status` as its weight. `reported` means one team saw it once. `reproduced` means someone else got the same result. `retracted` means do not build on it.

## Writing

1. **Copy a template** from `templates/`. Keep its frontmatter keys and section headings.
2. **One fact per file.** Two results are two findings, even from the same run.
3. **File names are IDs.** Lowercase, hyphens, no spaces. Findings are named `YYYY-MM-DD-<slug>.md`. Never rename a file once merged: other notes and repositories link to it.
4. **Link with relative Markdown links**, such as `[memory exhaustion](../tracks/memory-exhaustion.md)`. They render on GitHub and resolve for agents. No wiki links.
5. **Frontmatter values are plain.** One `key: value` per line. Lists are `[a, b]`. No nesting, no multi-line values. `scripts/check.py` parses nothing else.
6. **Update [`index.md`](index.md)** in the same pull request when you add a track, project or finding.
7. **Retract, do not delete.** A finding that turns out wrong gets `status: retracted` and a line saying why. The record of the mistake is useful.
8. **Run `python3 scripts/check.py`** before you push. CI runs the same check.

## Note types

A note's type is its folder. Required frontmatter keys below; `scripts/check.py` enforces them.

| Type | Keys | Allowed values |
|---|---|---|
| `track` | `title`, `question`, `status` | status: `open`, `paused`, `closed` |
| `project` | `title`, `track`, `repo`, `maintainers`, `status`, `started` | status: `scaffold`, `active`, `paused`, `done`, `archived` |
| `finding` | `title`, `track`, `project`, `result`, `strength`, `status`, `evidence`, `date`, `authors` | result: `positive`, `negative`, `inconclusive`; strength: `cryptographic`, `hardware-attested`, `sampled`, `timed`, `measured`, `argued`; status: `reported`, `reproduced`, `retracted` |
| `source` | `title`, `url`, `kind`, `tracks` | kind: `paper`, `post`, `code`, `talk`, `dataset` |

`track` and `project` values name a file in `tracks/` or `projects/`, without `.md`.

## Language

The same rules as the rest of the organisation.

- A finding states what was shown, under which assumption, and what a dishonest party can still do. Say bound, attested, sampled or timed. Never "secure" or "proves" without saying what and under which assumption.
- Numbers carry units, conditions and spread: hardware, versions, sample size. No single best run.
- Simulated or emulated results say so in the title.
- No secrets, hostnames, IP addresses, usernames or serial numbers. No personal data beyond GitHub handles.
- Plain, dense, active voice, short sentences.

## Layout

| Path | What |
|---|---|
| `index.md` | entry point: every track, project and recent finding |
| `tracks/` | research questions |
| `projects/` | repositories and experiments |
| `findings/` | results, one per file |
| `sources/` | external references |
| `workflows/` | how the organisation works |
| `templates/` | one per note type |
| `scripts/check.py` | frontmatter and link check, standard library only |
