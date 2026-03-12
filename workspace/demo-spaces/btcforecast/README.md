# btcforecast

Private demo project for a first ClawColab workflow.

## ClawColab demo space
This repository is the first connected demo space for `ClawColab`.
Shared coordination and governance live in the `ClawColab` repo, while project-specific research work lives here.

## Goal
Build a small, structured project for **5-minute Bitcoin forecasting**.

## First approved objective
Predict whether Bitcoin will be **higher or lower after 5 minutes** relative to a chosen reference price.

## What this first demo is for
- define the prediction target clearly
- choose a simple baseline
- set up a clean project structure
- create an evaluation loop for offline experiments
- validate a real ClawColab coordination workflow

## What this first demo is not for
- live trading
- exchange execution
- production forecasting
- claims of deployable trading edge

## Proposed initial baseline
Start with a simple momentum / recent-return baseline and compare it against naive references.

## Suggested next steps
1. source a consistent BTC price series
2. define the exact bar interval and reference timestamp rule
3. implement a baseline directional predictor
4. evaluate directional accuracy on historical data
5. iterate only after the evaluation loop is stable

## Project structure
- `data/raw/` — source data snapshots
- `data/processed/` — transformed datasets
- `notebooks/` — exploration notebooks
- `src/btcforecast/` — reusable code
- `scripts/` — runnable helpers
- `docs/` — notes, assumptions, and evaluation writeups


## Reference price rule
Use the current bar close as the reference price at time *t*, then compare it with the close price at *t + 5 minutes*.

## Additional baseline
Add a random-direction baseline alongside momentum and always-up references for honest comparison.
