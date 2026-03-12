# Data Spec

## Minimal first-demo requirement
A timestamped Bitcoin price series with enough resolution to evaluate 5-minute directional moves.

## Acceptable first-pass forms
- 1-minute OHLCV bars
- tick data resampled to 1-minute bars
- exchange export or market data API snapshots

## Required fields
- timestamp
- open
- high
- low
- close
- volume (preferred but optional for the earliest baseline)

## Notes
Keep the first dataset simple and reproducible.
