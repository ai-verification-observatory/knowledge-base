# Knowledge base

The shared memory of the [AI Verification Observatory](https://github.com/ai-verification-observatory): what each experiment found, including what did not work, written so that both people and coding agents can read it, cite it and add to it.

Every repository in the organisation runs its own experiment. This one holds what they learn. A finding from one proof of concept should be one link away from the next team that needs it.

## What is here

| Folder | One file per | Example |
|---|---|---|
| [`tracks/`](tracks) | research question, shared by several projects | [memory exhaustion](tracks/memory-exhaustion.md) |
| [`projects/`](projects) | repository or experiment in the organisation | [poc-memory-exhaustion](projects/poc-memory-exhaustion.md) |
| [`findings/`](findings) | result: positive, negative or inconclusive | none yet |
| [`sources/`](sources) | paper, post or code base we rely on | [SASH concept note](sources/sash-memory-exhaustion-note.md) |
| [`workflows/`](workflows) | way we work together | [report a finding](workflows/report-a-finding.md) |
| [`templates/`](templates) | note type, to copy | [finding](templates/finding.md) |

Start at [`index.md`](index.md). It lists every track, project and recent finding.

## Principles

- **One fact per file.** A finding is small enough to cite, link, dispute or retract on its own.
- **Negative results count.** "We tried X and it failed because Y" saves the next team a month. Record it like any other result.
- **Evidence or it is a hypothesis.** A finding links to the commit, command and run that produced it.
- **Several approaches per track.** A track with three competing projects is healthy. Findings are how they learn from each other.
- **Plain Markdown, typed by frontmatter.** No database, no special tool. GitHub renders it, agents parse it, `git log` is the history.

## Contribute

Open a pull request. [`workflows/report-a-finding.md`](workflows/report-a-finding.md) shows how, and [`AGENTS.md`](AGENTS.md) holds the rules every contributor, human or agent, follows. Run the check before you push:

```bash
python3 scripts/check.py
```

## Licence

Notes are licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Scripts are licensed under [Apache-2.0](LICENSE).
