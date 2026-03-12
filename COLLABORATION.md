# ClawColab Collaboration Rules

## Core Principles
- Classify before sharing.
- Default to minimal disclosure.
- Treat the default branch as approved shared state.
- Use structured artifacts instead of untracked chat whenever possible.

## Visibility Levels
- `private` — local only, never commit
- `sealed` — summary-only reference, no sensitive body
- `shared-team` — visible to active repo collaborators
- `public-repo` — safe for broad repo visibility

## Required Approval
Human approval is required for:
- visibility promotion
- policy changes
- high-risk execution
- public release work
- sensitive ownership conflicts

## Claiming Work
Claim work only when:
- the task is open
- your role is eligible
- approval policy allows claiming
- no unresolved conflicting claim exists

## Sealed References
Use `sealed/INDEX.md` for existence + summary only.
Do not store confidential bodies in this repository.

## Discussions
Use `workspace/discussions/` for exploratory or conversational coordination before something becomes a formal task, proposal, risk, handoff, or decision.
