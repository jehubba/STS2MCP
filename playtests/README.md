# Character Playtests

This directory contains durable evidence from autonomous STS2 character and card balance tests.

## Files

- `TEMPLATE.md`: required structure for each run report.
- `runs/`: one immutable report per run. Create the directory when recording the first run.
- `../GUIDE.md`: repeated, high-confidence strategic lessons promoted from run reports.

Name reports `<character>-<run-id-or-date>.md`. Use the compendium `run_id` when available; otherwise use an ISO date plus a short distinguishing suffix. Never reuse a filename or overwrite evidence from an earlier run. A report is editable only while its outcome is `In progress` and becomes immutable when the run ends.

## Recording Cadence

- Before run start: call `get_playtest_metrics()` without version or report metadata so older unseen runs enter the ledger as `unknown` rather than receiving the new run's metadata.
- At run start: record versions, character, seed/run ID when available, ascension, starting deck, relic, and test questions.
- At every card reward: record the full offer, selection or skip, deck need, and decision hypothesis.
- After every combat: record encounter outcome, turns, HP change, observed card plays, resource constraints, and notable interactions.
- At elites, bosses, and act transitions: record a deck/relic checkpoint and current balance flags.
- At run end: complete the evidence table, confounders, recommendations, and next experiments, then call `get_playtest_metrics()` with the mod version, MCP version, and report path. Mark diagnostic or scripted runs with `development_test=true`.

Routine turn narration is intentionally omitted. The report should retain enough state to support or challenge balance conclusions without becoming a transcript.

## Evidence Rules

- `Observation` means directly visible in MCP state or action results.
- `Interpretation` explains what the observation may mean.
- `Recommendation` proposes a design or numerical change and must include confidence and tradeoffs.
- Give each reward, combat, and anomaly observation a stable ID (`E01`, `E02`, and so on), and cite those IDs from evaluations and recommendations.
- A `playable opportunity` is an observed draw where the card could legally be played and doing so could plausibly advance the turn's objective. Record `unknown` when state or causality is insufficient.
- Attribute exact card contribution only when before/after state makes causality unambiguous.
- Label each adverse outcome `balance`, `agent misplay`, `game variance`, `tooling`, `bug`, or `uncertain`.
- A single run normally supports only low-confidence balance conclusions.
- Upgrade comparisons require evidence from before and after the upgrade; otherwise record the missing comparison as a confounder.

## Aggregate Metrics

The MCP maintains an append-only JSONL ledger derived from the active profile's immutable `.run` files. Stable run IDs make ingestion idempotent, and an existing ledger record is never rewritten from a changed source file. The raw run file remains the source of truth for final deck, reward offers, selections, outcome, game build, character, and ascension; the Markdown report supplies qualitative evidence and interpretation.

Primary balance denominators include terminal, non-abandoned runs that are not marked as development/test. Reports must show sample sizes and Wilson 95% confidence intervals rather than rates alone. Compare game-build and mod-version cohorts instead of combining behavior changes into a lifetime average. Treat final-deck card win rate as correlation, not causal card strength; acquisition timing, starter status, deck archetype, and player policy remain confounders.
