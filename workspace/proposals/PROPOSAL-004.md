# PROPOSAL-004

## Title
Choose a simple first baseline for btcforecast

## Status
pending_approval

## Visibility
shared-team

## Proposed By
Athena

## Scope
Choose a baseline forecasting method that is simple enough for a first collaboration demo.

## Proposed Actions
- start with a naive momentum / recent-return baseline
- compare against a random baseline and an always-up baseline
- defer more complex models until the workflow and evaluation loop are stable

## Expected Outputs
- `workspace/decisions/DECISION-004.md`

## Risks
- jumping too quickly to complex models may hide workflow problems
- a weak baseline may still be useful if it makes evaluation honest and reproducible

## Requested Owner or Role
- architect
- researcher
- human-approver

## Approval Needed
Approve the baseline direction for the first btcforecast demo.
