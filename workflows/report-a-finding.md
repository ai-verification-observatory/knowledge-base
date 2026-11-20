# Report a finding

A finding is one result, with the evidence to check it. Negative and inconclusive results are findings too.

## Steps

1. **Commit the evidence in the project repository first**: code, command, results file or run log. A finding links to it by commit, not by branch.
2. **Copy [`templates/finding.md`](../templates/finding.md)** to `findings/YYYY-MM-DD-<slug>.md`. The date is the day of the run.
3. **Fill every section.** Claim, setup, result, residual, next. Pick the `strength` honestly: `timed` for a timing-based check, `sampled` for a statistical one, `measured` for a plain measurement with no adversary, `argued` for reasoning with no run behind it.
4. **Link it** from the project note's Findings list, from the track's What we know section if it changes the picture, and from [`index.md`](../index.md).
5. **Run `python3 scripts/check.py`** and open a pull request. Tag the maintainers of other projects on the same track.

## Reproducing someone else's finding

Run their command on your hardware. If the result holds within the stated spread, open a pull request that sets `status: reproduced` and adds your setup and handle under a `## Reproductions` section. If it does not hold, add the same section with your numbers and open an issue. Do not retract another team's finding yourself.

## Agents

An agent may draft a finding and open the pull request. A human on the project reviews and merges it.
