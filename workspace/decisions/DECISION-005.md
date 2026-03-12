# DECISION-005

## Title
btcforecast first-demo reference price rule

## Status
approved

## Approved By
human-approver

## Based On
- TASK-007

## Scope
Define the reference-price rule used in the first offline btcforecast evaluation loop.

## Decision
Use the current bar close at time `t` as the reference price, and compare it with the close at `t + 5 minutes` to define the binary direction target.

## Rationale
This rule is simple, reproducible, and easy to align across labeling and evaluation scripts.

## Effective Reference
Approved in repository main branch.
