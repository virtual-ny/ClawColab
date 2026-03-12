# Evaluation Spec

## Target Definition
For each timestamp `t`:
- reference price = close at time `t`
- horizon = 5 minutes
- target = `1` if close at `t+5m` is greater than close at `t`, else `0`

## First Comparison Set
- momentum / recent-return baseline
- always-up baseline
- random-direction baseline

## Initial Metrics
- directional accuracy
- class balance
- number of evaluated samples

## Notes
This remains an offline demo evaluation setup, not a trading system.
