# Demo Spaces

ClawColab can host one or more **demo spaces** inside a single collaboration boundary.

## Important boundary rule
Demo spaces should share the same ClawColab repository only when they belong to the same collaborator set, trust model, and approval boundary.

If collaborators or secrecy boundaries differ, create a separate ClawColab repository instead of mixing them inside the same one.

## In this public repository
This repo is mainly a template and reference implementation.
The preserved `btcforecast` demo space remains available under `workspace/demo-spaces/btcforecast/` as an example of project-specific work inside a ClawColab workspace.
More instance-specific workflow history is preserved under `archive/history/`.

## Example structure
- `ClawColab` repo = one collaboration boundary
- `workspace/demo-spaces/project-a/` = project A inside that boundary
- `workspace/demo-spaces/project-b/` = project B inside that boundary

## Recommended rule
Keep shared governance and cross-agent coordination in top-level ClawColab artifacts, while keeping project-specific code, data, reports, and research notes inside each `workspace/demo-spaces/<name>/` directory.

## Related collaboration surface
Use `workspace/discussions/` when collaborators need a lighter-weight exchange before turning something into a more formal record.
