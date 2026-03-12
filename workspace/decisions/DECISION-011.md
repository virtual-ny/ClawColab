# DECISION-011

## Title
btcforecast is the first ClawColab demo space

## Status
approved

## Approved By
Han

## Based On
- PROPOSAL-006

## Scope
Define how `btcforecast` should relate to `ClawColab`.

## Decision
Treat `btcforecast` as the first connected demo space under ClawColab.

- `ClawColab` remains the shared coordination, policy, and multi-agent governance repository.
- `btcforecast` remains the project repository where forecasting code, datasets, reports, and research artifacts live.
- Cross-agent coordination about `btcforecast` should be recorded in `ClawColab` through tasks, proposals, decisions, handoffs, and risks.

## Rationale
This keeps repo responsibilities clean: one repo for collaboration protocol and one repo for domain-specific demo work.

## Effective Reference
Approved in repository main branch.
