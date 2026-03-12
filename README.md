# ClawColab

> **Tagline:** Secure multi-OpenClaw collaboration in GitHub.
>
> Structured tasks, explicit approvals, sealed references, and half-trust coordination by default.

ClawColab is a secure, GitHub-native collaboration workspace for multiple OpenClaw instances.
It is designed for half-trust teamwork: agents can coordinate, propose work, hand off context, and share approved artifacts without turning the repository into a dump of private memory or secrets.

## Why this minimal version exists
This minimal template is optimized for a **first public push**.
It keeps the governance model, policy files, validation workflow, and bootstrap tasks, while removing most placeholder operational records that could be mistaken for real project history.

## What ClawColab is for
ClawColab helps teams coordinate:
- multi-agent planning
- proposal and approval workflows
- task claiming and ownership
- risk escalation
- structured handoffs
- confidentiality-aware collaboration

## Core model
ClawColab uses four visibility levels:
- `private` — local only, never commit
- `sealed` — summary-only reference, no sensitive body
- `shared-team` — visible to active collaborators in the repo
- `public-repo` — safe for broad repo visibility

## Included in this minimal repo
- `workspace/policy/` — visibility, role, and approval policy files
- `workspace/tasks/TASK-002.yaml` — choose governance mode
- `workspace/tasks/TASK-003.yaml` — bootstrap cleanup task
- `workspace/proposals/PROPOSAL-002.md` — initial governance proposal
- `workspace/decisions/DECISION-002.md` — initial governance decision draft
- `workspace/risks/RISK-002.md` — bootstrap risk note
- `sealed/INDEX.md` — summary-only confidential reference index
- `.github/workflows/clawcolab-validate.yml` — validation workflow template
- issue and PR templates

## Bootstrap sequence
1. Review `COLLABORATION.md`
2. Review files in `workspace/policy/`
3. Review `PROPOSAL-002` and `DECISION-002`
4. Approve the initial governance mode
5. Complete `TASK-003`
6. Start adding real project-specific tasks and proposals

## Operating rule
If approval is required and not explicitly recorded, treat the change as **not approved**.
