# Start a project

One repository per experiment. A second approach to a question that already has a project is a second repository, not a branch: competing approaches are the point.

## Steps

1. **Ask for a repository.** Open an issue in this repository, or ask an organisation owner. Say the question, the approach, and your GitHub handle.
2. **Name it** `poc-<topic>` for a proof of concept, `poc-<topic>-<approach>` when the topic already has one, and a plain name for a library or benchmark.
3. **Write the README before the code.** State the claim, the setting, the adversary, the mechanism, the success criterion and what is out of scope. [poc-memory-exhaustion](https://github.com/ai-verification-observatory/poc-memory-exhaustion) is a good model: open questions first, then a decisions log.
4. **Add `AGENTS.md`** with the project rules, and the knowledge-base section below so agents working in your repository read and write shared findings.
5. **Add a project note** here: copy [`templates/project.md`](../templates/project.md) to `projects/<repo>.md`, link it from its track and from [`index.md`](../index.md). If no track fits, add one from [`templates/track.md`](../templates/track.md).

## Knowledge-base section for your AGENTS.md

Paste this into the project's `AGENTS.md` and replace `<track>`:

```markdown
## Knowledge base

Shared findings live in https://github.com/ai-verification-observatory/knowledge-base.

- Before starting a task, read `index.md`, `tracks/<track>.md` and the findings that name this track there. Do not repeat an approach a finding already ruled out without saying what is different.
- When a run produces a result, positive or negative, draft a finding from `templates/finding.md` and open a pull request to the knowledge base, following its `AGENTS.md`. Link the commit and command that produced it.
```
