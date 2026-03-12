# Data Source Notes

## Preferred source
Massive / Polygon remains the preferred primary market-data source for production-like market research when a valid local API key is available.

## Current first-demo fallback
For this single-user demo, recent 1-minute BTC-USD candles were fetched from Coinbase's public candles endpoint as a no-key fallback.

## Why fallback was used
- `MASSIVE_API_KEY` was not available in the current shell environment
- Binance public klines returned HTTP 451 from this environment

## Current dataset
- file: `data/raw/coinbase/btcusd_1m_coinbase_recent.csv`
- symbol: BTC-USD
- interval: 1 minute
- source: Coinbase public candles endpoint
