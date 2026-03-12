# First Push Checklist

## Goal
Publish a clean first version of ClawColab without placeholder noise or misleading fake history.

## Include in the first public push
- [ ] `README.md`
- [ ] `COLLABORATION.md`
- [ ] `.gitignore`
- [ ] `.github/workflows/clawcolab-validate.yml`
- [ ] `.github/pull_request_template.md`
- [ ] `.github/ISSUE_TEMPLATE/`
- [ ] `workspace/policy/visibility-policy.yaml`
- [ ] `workspace/policy/role-policy.yaml`
- [ ] `workspace/policy/approval-policy.yaml`
- [ ] `workspace/tasks/TASK-002.yaml`
- [ ] `workspace/tasks/TASK-003.yaml`
- [ ] `workspace/proposals/PROPOSAL-002.md`
- [ ] `workspace/decisions/DECISION-002.md`
- [ ] `workspace/risks/RISK-002.md`
- [ ] `sealed/INDEX.md`

## Leave out of the first public push
- [ ] old scaffold placeholders that look like fake historical work
- [ ] private notes or local memory exports
- [ ] any secrets, tokens, credentials, or environment-specific values
- [ ] sample handoffs or claims unless they reflect real current use

## Before pushing
- [ ] confirm strict mode is still the desired starting posture
- [ ] confirm policy files match your real collaboration expectations
- [ ] confirm workflow paths match the repo layout
- [ ] confirm `sealed/INDEX.md` contains summaries only
- [ ] confirm no fake approvals are present

## Good second push candidates
- [ ] first real task set
- [ ] first real project proposal
- [ ] first repo-specific decision after team review
- [ ] first real claim or handoff once collaboration begins
