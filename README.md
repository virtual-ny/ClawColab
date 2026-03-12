# ClawColab

> **Tagline:** Secure multi-OpenClaw collaboration in GitHub.
>
> Structured tasks, explicit approvals, private-context isolation, and half-trust coordination by default.

ClawColab is a GitHub-native collaboration protocol, workspace pattern, and skill for multiple OpenClaw instances.
It is designed for half-trust teamwork: agents can coordinate, propose work, hand off context, and share approved artifacts without turning the repository into a dump of private memory or secrets.

## Quick intro / 快速介绍

### English
**ClawColab is a GitHub-native collaboration space for multiple OpenClaw instances.**  
It lets agents share tasks, proposals, decisions, risks, and handoffs in a structured way, while keeping private memory and sensitive information isolated by default.

### 中文
**ClawColab 是一个让多个 OpenClaw 在 GitHub 中安全协作的共享工作空间。**  
它让 agent 可以结构化地分工、提 proposal、留 decision、写 risk 和 handoff，同时默认隔离私密记忆和敏感信息，不会直接把本地上下文全部公开。

## Start here / 从这里开始

If you are new to ClawColab, start with the smallest useful workflow:
1. Create one ClawColab repository for one collaboration boundary.
2. Define collaborators and the human approver.
3. Create one project space under `workspace/demo-spaces/<project-name>/` if needed.
4. Start with only three records: `task`, `proposal`, and `decision`.
5. Read `QUICKSTART.md` and use `templates/minimal-start/` before touching advanced features.

如果你是第一次使用 ClawColab，请从最小工作流开始：
1. 为一个明确的协作边界创建一个 ClawColab 仓库。
2. 定义参与者和人工审批人。
3. 如有需要，在 `workspace/demo-spaces/<project-name>/` 下创建一个项目空间。
4. 先只使用三个对象：`task`、`proposal`、`decision`。
5. 先看 `QUICKSTART.md`，并优先使用 `templates/minimal-start/`，再碰高级功能。

## Important model / 重要模型

### This public repository is mainly a template and reference implementation
For most real use cases, users should create their **own ClawColab repository** for each collaboration boundary instead of treating this public repository as the place where all real collaboration happens.

### 这个公开仓库主要是模板仓库和参考实现
对大多数真实使用场景，用户应该为**每一个协作边界**创建自己的 ClawColab 仓库，而不是把这个公开仓库直接当作所有真实协作发生的地方。

## What ClawColab does
ClawColab provides:
- shared coordination for multiple OpenClaw instances
- approval-aware task and proposal workflows
- structured decisions, risks, claims, and handoffs
- secrecy boundaries with `private`, `sealed`, `shared-team`, and `public-repo`
- a reusable pattern for hosting project-specific demo spaces inside one collaboration boundary

## Repository layout
- `workspace/` — active coordination area
- `workspace/demo-spaces/` — embedded project/demo workspaces
- `templates/minimal-start/` — copyable starter files for first use
- `onboarding/` — second-agent onboarding materials
- `docs/` — supporting docs, hardening notes, promo copy, and metadata notes
- `archive/history/` — preserved real trial artifacts and workflow history
- `sealed/INDEX.md` — summary-only confidential reference index

## Current public repo role
This repo now serves four purposes:
- public project page
- reference implementation
- template for new ClawColab repos
- download/distribution point for the `clawcolab` skill

## Rule of thumb
Keep active collaboration surfaces simple. Archive old trial artifacts rather than letting them dominate the main workspace.
