# DECISION-011

## Title
btcforecast is the first ClawColab demo space

## Status
approved

## Approved By
human-approver

## Based On
- PROPOSAL-006

## Scope
Define how `btcforecast` should relate to `ClawColab`.

## Decision
Treat `btcforecast` as the first demo space under ClawColab, preserved directly inside `workspace/demo-spaces/btcforecast/`.

- `ClawColab` remains the shared coordination, policy, and multi-agent governance repository.
- `workspace/demo-spaces/btcforecast/` now holds the forecasting code, datasets, reports, notebooks, and research artifacts.
- Cross-agent coordination about `btcforecast` remains recorded in `ClawColab` through tasks, proposals, decisions, handoffs, and risks.

## Rationale
This keeps collaboration in one active repository while still separating governance artifacts from project-specific demo-space contents.

## Effective Reference
Approved in repository main branch.
