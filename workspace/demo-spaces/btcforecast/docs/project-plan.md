# Project Plan

## Objective
Build an offline first demo for 5-minute Bitcoin directional forecasting.

## Approved target
Binary target:
- `up` if price at t+5m > reference price at t
- `down` if price at t+5m <= reference price at t

## First baseline candidate
Use recent short-window return or momentum as a naive predictor.

## Initial evaluation ideas
- directional accuracy
- class balance
- comparison to always-up baseline
- comparison to random baseline

## Constraints
- no trading execution
- no live capital allocation
- no production claims
