# Demo Spaces

ClawColab can coordinate one or more project workspaces called **demo spaces**.

## Current demo space snapshot

### btcforecast
- Status: archived as a standalone repo and preserved inside `workspace/demo-spaces/btcforecast/`
- Purpose: first research/demo space for short-horizon Bitcoin forecasting
- Current role: historical demo-space example and reusable workspace structure

## Current structure
- `ClawColab` = shared coordination, governance, and now demo-space storage
- `workspace/demo-spaces/btcforecast/` = preserved first demo space

## Recommended rule
Keep shared governance and cross-agent coordination in top-level `ClawColab` artifacts, while keeping project-specific code, data, reports, and research notes inside each `workspace/demo-spaces/<name>/` directory.
