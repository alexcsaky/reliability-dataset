# Reliability dataset, release v1

Built 2026-10-28 from the stored database. 31 subjects, 29754 claims, 0 verdict changes. Method versions: `0.1.0+4bff4432`, `0.1.0+ecd0c1d5`.

## What this is

For each subject (a public figure or organisation), a sample of what they have said in public was read, the checkable claims were checked against the public record, and each claim carries a verdict linked to its quote and its evidence. The score is the share of resolved claims that held up, per kind of claim (factual, promise, guidance, prediction) and overall, shrunk towards a fixed prior and shown with an 80% interval and a confidence level. Verdicts are made automatically and are not individually reviewed by a person. Two model judges from different model families judge each claim; `judges_disagree` marks the claims where they differed. How the method works: https://epistacklabs.com/methodology.

## Caveats

- Two model judges agreeing is consistency, not accuracy. Agreement with known outcomes and stability on re-runs are measured and published on the methodology page.
- No base-rate adjustment: a claim almost everyone got right counts the same as a bold one.
- No weighting by importance: a trivial claim counts as much as a central one.
- The sample is not the subject: the score describes the sampled documents and claims, chosen by the stated rules.
- Scores are shrunk towards a fixed prior of 50 worth 4 claims, because the database is too small for a reference-class average.
- Only subjects at medium or high confidence should be compared with each other; the interval columns say how wide the uncertainty is, and `n_resolved` how many claims a score rests on.
- `evidence_from_factcheck` counts evidence items from sites that publish verdicts themselves (fact-checkers, advertising regulators). Agreement with such a source is agreement with that source, not with the record.
- The sampling method per subject (which documents were read, and for X posts whether by date window or by model-chosen candidates) is recorded in the full records (`claims.jsonl`, coverage fields of the report).

## Scope

Public figures and organisations only, from their public professional output. Nothing about private life, family, health, home or location, and no inferred motives. Party-political claims are tagged `political` and left out of scores. Political candidates, serving politicians and officials in post are out of scope. Wording is neutral: a claim is "resolved false", never anything about honesty.

## Right of reply

A subject, or someone acting for them, can reply to any claim with a correction or counter-evidence. Use the `respond_url` on the subject's row (the request form; give the `claim_id` and a link to the evidence). Replies are recorded on the claim and corrections are published as verdict changes with the reason.

## Measured results (method `0.1.0+6d6bb9f2`, 2026-10-14)

Agreement with known outcomes on the measured sets, and stability on re-runs. Two judges agreeing is consistency, not accuracy.

- All claims: 93 of 104 the same verdict as the record, 104 in the right direction, 0 wrong, 0 unresolvable.
- Guidance (within the range or bound): 31 of 31 the same verdict as the record, 31 in the right direction, 0 wrong, 0 unresolvable.
- Guidance (above the range or bound): 24 of 29 the same verdict as the record, 29 in the right direction, 0 wrong, 0 unresolvable.
- Guidance (below the range or bound): 17 of 17 the same verdict as the record, 17 in the right direction, 0 wrong, 0 unresolvable.
- Promises: 21 of 27 the same verdict as the record, 27 in the right direction, 0 wrong, 0 unresolvable.
- Verdicts unchanged on a re-run: ? of ?.

## Files

- `subjects.csv`, `scores.csv`, `claims.csv.gz`, `changes.csv`: one table each; `datapackage.json` lists the columns.
- `claims.jsonl.gz`: every record in full, one JSON object per line.
- `infographics.html`: the release in charts, one self-contained page (`infographics.json` holds its figures).

## Licence

CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Quotes are short, attributed and linked to their source; no page text is included. Cite as: Reliability dataset v1, epistacklabs.com.
