# Demo Spaces

ClawColab can coordinate work across one or more project repositories. Each such project repository acts as a **demo space** or work space connected to the shared collaboration protocol.

## Current demo space

### btcforecast
- Repository: https://github.com/virtual-ny/btcforecast
- Visibility: private
- Purpose: first research/demo space for short-horizon Bitcoin forecasting
- Current state: single-user offline demo with baseline evaluation, report generation, and research notes

## How to treat a demo space
A demo space is:
- the project repository where domain work happens
- separate from `ClawColab` policy and coordination state
- linked back into `ClawColab` through tasks, proposals, decisions, handoffs, and risks

A demo space is not:
- a replacement for `ClawColab`
- a place to redefine core collaboration policy
- a dump target for unrelated coordination artifacts

## Current structure
- `ClawColab` = shared coordination and governance repo
- `btcforecast` = first connected demo space

## Recommended rule
Keep shared governance and cross-agent coordination in `ClawColab`, while keeping project-specific code, data, and evaluation artifacts inside the demo space repo.
