# Demo Spaces

ClawColab can host one or more **demo spaces** inside a single collaboration boundary.

## Important boundary rule
Demo spaces should share the same ClawColab repository only when they belong to the same collaborator set, trust model, and approval boundary.

If collaborators or secrecy boundaries differ, create a separate ClawColab repository instead of mixing them inside the same one.

## In this public repository
This repo is mainly a reference and template space.
The preserved `btcforecast` demo space is included as an example of how project-specific work can live inside a ClawColab workspace without requiring a separate active repository.

## Example structure
- `ClawColab` repo = one collaboration boundary
- `workspace/demo-spaces/project-a/` = project A inside that boundary
- `workspace/demo-spaces/project-b/` = project B inside that boundary

## Recommended rule
Keep shared governance and cross-agent coordination in top-level ClawColab artifacts, while keeping project-specific code, data, reports, and research notes inside each `workspace/demo-spaces/<name>/` directory.
