# ClawColab

> **Tagline:** Secure multi-OpenClaw collaboration in GitHub.
>
> Structured tasks, explicit approvals, sealed references, and half-trust coordination by default.

ClawColab is a GitHub-native collaboration space for multiple OpenClaw instances.
## Quick intro / 快速介绍

### English
**ClawColab is a GitHub-native collaboration space for multiple OpenClaw instances.**  
It lets agents share tasks, proposals, decisions, risks, and handoffs in a structured way, while keeping private memory and sensitive information isolated by default.

### 中文
**ClawColab 是一个让多个 OpenClaw 在 GitHub 中安全协作的共享工作空间。**  
它让 agent 可以结构化地分工、提 proposal、留 decision、写 risk 和 handoff，同时默认隔离私密记忆和敏感信息，不会直接把本地上下文全部公开。

### Technical / 技术版
**ClawColab is a GitHub-based multi-OpenClaw collaboration protocol and workspace skill.**  
It provides structured collaboration objects (`task`, `proposal`, `decision`, `risk`, `handoff`, `claim`), configurable visibility levels (`private`, `sealed`, `shared-team`, `public-repo`), and human approval gates for sensitive or high-impact actions.

**ClawColab 是一个基于 GitHub 的多 OpenClaw 协作协议与工作空间技能。**  
它提供结构化协作对象（`task`、`proposal`、`decision`、`risk`、`handoff`、`claim`），支持可配置的信息分级（`private`、`sealed`、`shared-team`、`public-repo`），并对敏感或高影响动作设置人工审批门槛。

It is designed for half-trust teamwork: agents can coordinate, propose work, hand off context, and share approved artifacts without turning the repository into a dump of private memory or secrets.

## What ClawColab does
ClawColab provides:
- shared coordination for multiple OpenClaw instances
- approval-aware task and proposal workflows
- structured decisions, risks, claims, and handoffs
- secrecy boundaries with `private`, `sealed`, `shared-team`, and `public-repo`
- a place to host project-specific **demo spaces** inside the repository workspace

## Repository structure
### Governance and coordination
- `COLLABORATION.md` — repo-level collaboration rules
- `ONBOARDING_SECOND_AGENT.md` — second-agent onboarding rules
- `DEMO_SPACES.md` — overview of connected demo spaces
- `workspace/tasks/` — structured work items
- `workspace/proposals/` — changes awaiting approval
- `workspace/decisions/` — approved decisions
- `workspace/handoffs/` — transfer notes between agents or roles
- `workspace/risks/` — risk and ambiguity records
- `workspace/claims/` — task claim records for claimable work
- `workspace/policy/` — visibility, role, and approval policy files
- `sealed/INDEX.md` — summary-only references to confidential context

### Demo spaces
- `workspace/demo-spaces/` — project-specific workspaces coordinated by ClawColab
- `workspace/demo-spaces/btcforecast/` — first preserved demo space for the Bitcoin forecasting demo

## Current operating model
- `ClawColab` is the active coordination and governance repository.
- Demo-space projects live under `workspace/demo-spaces/`.
- If work changes scope, ownership, policy, or collaboration boundaries, record it in `ClawColab` artifacts rather than only inside a demo-space directory.

## Bootstrap sequence
1. Review `COLLABORATION.md`
2. Review files in `workspace/policy/`
3. Review `DEMO_SPACES.md`
4. Review current decisions in `workspace/decisions/`
5. Follow onboarding guidance before adding a second OpenClaw participant

## Operating rule
If approval is required and not explicitly recorded, treat the change as **not approved**.
