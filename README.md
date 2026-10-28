# Reliability dataset

Reliability scores for public figures and organisations, with every claim, verdict and evidence link behind them,
built by the Reliability API (https://epistacklabs.com). A subject's public statements are sampled, the checkable
claims are checked against the public record, and each claim carries a verdict linked to its quote and its
evidence. The score is the share of resolved claims that held up, per kind of claim and overall, with an 80%
interval and a confidence level.

Verdicts are made automatically and are not individually reviewed by a person. Two model judges from different
model families judge each claim; `judges_disagree` marks where they differed. Two judges agreeing is consistency,
not accuracy. The method, its measured results and its caveats: https://epistacklabs.com/methodology.

## Releases

Each release is a folder (`v1/`, ...) with:

- `subjects.csv`: one row per subject, with the latest report and how to reply (`respond_url`).
- `scores.csv`: one row per subject and claim type (and overall): score, interval, resolved count, confidence.
- `claims.csv.gz`: one row per claim: quote, source, verdict, rationale, evidence links, whether the judges
  disagreed, how many evidence items are fact-checks.
- `changes.csv`: verdict changes (old and new verdict, when, why, evidence added).
- `claims.jsonl.gz`: every record in full, one JSON object per line.
- `datapackage.json` (the columns) and `README.md` (what the release is, its method version, measured results,
  caveats, scope and licence).

`CHANGELOG.md` lists the releases. The latest is `v1` (28 October 2026): 31 public figures.

## Look a subject up

No key needed:

    curl "https://epistacklabs.com/v1/lookup?name=Jensen%20Huang"

## Scope and right of reply

Public figures and organisations only, from their public professional output; nothing about private life; no
inferred motives; party-political claims tagged and left out of scores; political candidates and officials in
post out of scope; neutral wording throughout. A subject can reply to any claim with a correction or
counter-evidence through the `respond_url` on their row.

## Licence

CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Quotes are short, attributed and linked to their
source; no page text is included. Cite as: Reliability dataset v1, epistacklabs.com, 2026.
