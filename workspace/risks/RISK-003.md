# RISK-003

## Title
Demo may be mistaken for trading-grade forecasting

## Severity
high

## Affected Tasks
- TASK-004
- TASK-005
- TASK-006

## Description
A short-horizon Bitcoin forecasting demo can be misread as a production-ready trading system even when the real goal is workflow validation and basic research coordination.

## Potential Impact
- overconfidence in early model results
- premature automation pressure
- confusion between research metrics and deployable edge

## Mitigations
- keep the first demo explicitly offline and non-executional
- use simple baselines first
- document that the main goal is collaboration workflow plus evaluation discipline
- require explicit human approval before expanding scope toward live decision-making

## Escalation Path
Escalate to the human approver before any step that moves from demo evaluation toward real trading use.
