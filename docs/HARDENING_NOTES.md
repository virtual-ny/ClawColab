# Hardening Notes

This document summarizes the first hardening passes applied to the `clawcolab` skill after external review.

## Why this exists
ClawColab started as a strong collaboration protocol and governance model, but early feedback showed that some rules were still easier to misinterpret or bypass than intended.

The first hardening goal is to move from:
- good written norms

toward:
- safer default workflow
- stronger validation
- less ambiguity in day-to-day use

## Hardening pass 1
### Added
- classification checklist
- classification guide
- pre-share checks
- visibility-promotion decision template

### Effect
Before sharing proposals, decisions, handoffs, risks, or summaries, the intended workflow is now:
1. classify
2. scan
3. check approval
4. require decision record for visibility promotion
5. only then share

## Hardening pass 2
### Tightened defaults
- `proposal-approval` remains the default mode
- `claimable` is now treated as a narrow low-risk exception
- medium-risk task execution defaults to human approval
- visibility promotion requires a decision record

### Validator improvements
- task validation now checks `risk_level`
- claimable tasks must be explicitly low risk
- claimable + approval-required is rejected
- policy-touching outputs are rejected in ordinary task validation
- policy bundle validation now checks role/approval/promotion consistency more strictly

## Practical result
ClawColab is still not a full strong-enforcement system, but it now does more to push users and agents into a safer default operating path.
