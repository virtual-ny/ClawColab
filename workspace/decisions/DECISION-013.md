# DECISION-013

## Title
Adopt a second-agent preflight checklist

## Status
approved

## Approved By
Han

## Based On
- TASK-016
- PROPOSAL-008

## Scope
Adopt a standard preflight routine for second-agent task execution in ClawColab.

## Decision
Use a second-agent preflight checklist before starting low-risk tasks. The checklist should at minimum require pulling the latest `main`, confirming the target task exists locally, reading task dependencies and inputs, checking expected outputs, avoiding unnecessary overwrites, and only marking tasks done when outputs match task intent.

## Rationale
This reduces preventable coordination mistakes during onboarding and makes second-agent participation more reliable.

## Effective Reference
Approved in repository main branch.
