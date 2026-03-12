# DECISION-002

## Title
Initial governance mode

## Status
proposed

## Approved By
TBD

## Based On
- PROPOSAL-002

## Scope
Define the initial governance posture for this repository before broader multi-agent collaboration begins.

## Decision
Start this repository in **strict governance mode**.

Strict mode means:
- all visibility promotion requires human approval
- all policy changes require human approval
- high-risk execution requires human approval and security review
- claimable mode is limited to low-risk work
- unresolved claim conflicts block autonomous execution
- default branch content is treated as approved shared state only after explicit approval records exist

## Rationale
This repository is intended for half-trust collaboration across multiple OpenClaw instances and may involve more than one human operator.
Starting in strict mode reduces accidental over-sharing, ambiguous authority, and premature autonomous execution while the team is still establishing norms.

Strict mode is the safest default because it:
- protects secrecy boundaries early
- forces explicit approval habits
- makes audit trails clearer
- limits damage from misclassification or role confusion

## Revisit Conditions
This decision may be revisited after the team demonstrates:
- consistent use of visibility labels
- clean approval records
- low conflict rates in task claiming
- no recurring leakage or policy violations over multiple collaboration cycles

## Effective Reference
Effective upon human approval and merge to the default branch.
