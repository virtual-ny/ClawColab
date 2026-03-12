# DECISION-006

## Title
btcforecast first real-data fallback source

## Status
approved

## Approved By
Han

## Based On
- TASK-008

## Scope
Define the fallback source for real BTC minute data during the current single-user demo phase.

## Decision
Use Coinbase public BTC-USD 1-minute candles as the temporary real-data fallback source when Massive / Polygon is unavailable in the environment.

## Rationale
This keeps the demo moving without blocking on credentials, while preserving Massive as the preferred primary source for future runs.

## Effective Reference
Approved in repository main branch.
