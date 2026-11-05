# Reliability dataset

Reliability scores for public figures and organisations, with every claim, verdict and evidence link behind them,
built by the Reliability API (https://epistacklabs.com). A subject's public statements are sampled, the checkable
claims are checked against the public record, and each claim carries a verdict linked to its quote and its
evidence. The score is the share of resolved claims that held up, for each kind of claim (factual claims,
predictions, promises, company guidance), with an 80% interval and a confidence level. Predictions are scored on
their own. The overall row mixes kinds of claim in different proportions for different subjects; compare subjects
within one kind of claim, and only at medium or high confidence.

Verdicts are made automatically and are not individually reviewed by a person. Two model judges from different
model families judge each claim; `judges_disagree` marks where they differed. Two judges agreeing is consistency,
not accuracy. The method, its measured results and its caveats: https://epistacklabs.com/methodology.

## Releases

Each release is a folder (`v1/`, `v1.1/`, `v1.1.1/`, ...) with:

- `subjects.csv`: one row per subject, with the latest report and how to reply (`respond_url`).
- `scores.csv`: one row per subject and claim type (and overall): score, interval, resolved count, confidence.
- `claims.csv.gz`: one row per claim: quote, source, verdict, rationale, evidence links, whether the judges
  disagreed, how many evidence items are fact-checks.
- `claims.parquet` (from v1.1): the claims table as Parquet, the same columns and cells.
- `changes.csv`: verdict changes (old and new verdict, when, why, evidence added).
- `claims.jsonl.gz`: every record in full, one JSON object per line.
- `infographics.html`: the release in charts, one self-contained page; `infographics.json` holds its figures.
- `datapackage.json` (the columns) and `README.md` (what the release is, its method version, measured results,
  caveats, scope and licence).

`CHANGELOG.md` lists the releases and what changed between them. The latest is `v1.1.1`.

## Look a subject up

No key needed:

    curl "https://epistacklabs.com/v1/lookup?name=Jensen%20Huang"

Or read every claim in a browser at https://epistacklabs.com/explore.

## Scope and right of reply

Public figures and organisations only, from their public professional output; nothing about private life; no
inferred motives; neutral wording throughout. Politicians and officials are covered like anyone else, and
party-political claims are tagged `political` and scored like any other claim (from release v1.1; v1 left some
out of scores, as its README says). A subject, or someone acting for them, can reply to any claim with a correction
or counter-evidence, with the form at the foot of the claim's own page on https://epistacklabs.com (the
`respond_url` on their row explains how replies work).

## Licence

CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Quotes are short, attributed and linked to their
source; no page text is included. Cite as: Reliability dataset v1.1.1, epistacklabs.com, 2026.
