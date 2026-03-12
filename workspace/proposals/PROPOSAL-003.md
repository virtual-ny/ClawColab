# PROPOSAL-003

## Title
Define the first btcforecast demo objective

## Status
pending_approval

## Visibility
shared-team

## Proposed By
Athena

## Scope
Define the initial forecasting task narrowly enough that the first ClawColab demo can focus on process, evaluation, and collaboration rather than system complexity.

## Proposed Actions
- predict Bitcoin direction over the next 5 minutes rather than exact price
- use a binary target: up or down from the current reference price after 5 minutes
- evaluate with simple accuracy plus a no-trade / uncertain option if needed later
- keep the first version offline and research-oriented, with no execution component

## Expected Outputs
- `workspace/decisions/DECISION-003.md`

## Risks
- exact price prediction may distract from the collaboration demo and be unnecessarily noisy
- unclear target definition will make evaluation meaningless

## Requested Owner or Role
- coordinator
- architect
- human-approver

## Approval Needed
Approve the first-demo objective definition for the btcforecast project.
