# RISK-004

## Title
Second agent may over-assume authority during initial onboarding

## Severity
medium

## Affected Tasks
- TASK-011
- TASK-012
- TASK-013

## Description
A newly joined OpenClaw participant may assume broader permissions than intended if onboarding boundaries are not explicit.

## Potential Impact
- accidental policy edits
- implicit approval behavior
- over-sharing of shared-team or sealed context

## Mitigations
- use an explicit onboarding document
- keep the second agent in a non-approver role initially
- restrict first tasks to low-risk review or documentation work
- require human approval for any policy or visibility change

## Escalation Path
Escalate to Han before changing role authority, visibility rules, or policy files.
