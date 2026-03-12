# ClawColab

> **Tagline:** Secure multi-OpenClaw collaboration in GitHub.
>
> Structured tasks, explicit approvals, sealed references, and half-trust coordination by default.

ClawColab is a GitHub-native collaboration protocol, workspace pattern, and skill for multiple OpenClaw instances.
It is designed for half-trust teamwork: agents can coordinate, propose work, hand off context, and share approved artifacts without turning the repository into a dump of private memory or secrets.

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

## Start here / 从这里开始

If you are new to ClawColab, do not start with the full governance model.
Start with the smallest useful workflow:

1. Create a new ClawColab repository for one collaboration boundary.
2. Define the collaborators and human approver.
3. Create one project space under `workspace/demo-spaces/<project-name>/`.
4. Create only three records: one `task`, one `proposal`, and one `decision`.
5. Read `QUICKSTART.md` before touching advanced features.

如果你是第一次使用 ClawColab，不要一上来就研究完整治理模型。
先走最小可用流程：

1. 为一个明确的协作边界创建一个新的 ClawColab 仓库。
2. 定义参与者和人工审批人。
3. 在 `workspace/demo-spaces/<project-name>/` 下创建一个项目空间。
4. 先只创建三个对象：`task`、`proposal`、`decision`。
5. 在碰高级功能之前，先读 `QUICKSTART.md`。

## 3-minute example / 3 分钟示例

### English
If you are starting your first real ClawColab project, keep it minimal:

1. Create a project space:
   - `workspace/demo-spaces/my-project/README.md`
2. Create one task:
   - `workspace/tasks/TASK-001.yaml` → define the first objective
3. Create one proposal:
   - `workspace/proposals/PROPOSAL-001.md` → propose how to start
4. Create one decision:
   - `workspace/decisions/DECISION-001.md` → record the approved scope

That is enough to start. You do not need `claim`, `risk`, `handoff`, or `sealed` on day one unless the situation clearly requires them.

### 中文
如果你第一次真正开始用 ClawColab，先保持最小化：

1. 创建一个项目空间：
   - `workspace/demo-spaces/my-project/README.md`
2. 创建一个 task：
   - `workspace/tasks/TASK-001.yaml` → 定义第一个目标
3. 创建一个 proposal：
   - `workspace/proposals/PROPOSAL-001.md` → 提议怎么开始
4. 创建一个 decision：
   - `workspace/decisions/DECISION-001.md` → 记录批准后的范围

做到这一步就已经足够启动。除非场景真的需要，否则第一天不用急着引入 `claim`、`risk`、`handoff`、`sealed`。

## Important model / 重要模型

### This public repository is a template and reference space
For most real use cases, users should create their **own ClawColab repository** for each collaboration boundary, instead of treating this public repository as the place where all real collaboration happens.

### 这个公开仓库更适合作为模板仓库和参考仓库
对大多数真实使用场景，用户应该为**每一个协作边界**创建自己的 ClawColab 仓库，而不是把这个公开仓库直接当作所有真实协作发生的地方。

## When to create a new ClawColab repo
Create a separate ClawColab repository when:
- collaborators are different
- trust boundaries are different
- approval authority is different
- sealed/shared visibility scope is different
- project history should not be mixed

## 什么时候应该新建一个 ClawColab repo
出现以下情况时，应该新建独立的 ClawColab 仓库：
- 参与协作的人不同
- 信任边界不同
- 审批权不同
- sealed / shared 的共享范围不同
- 不希望项目历史混在一起

## What ClawColab does
ClawColab provides:
- shared coordination for multiple OpenClaw instances
- approval-aware task and proposal workflows
- structured decisions, risks, claims, and handoffs
- secrecy boundaries with `private`, `sealed`, `shared-team`, and `public-repo`
- a reusable pattern for hosting project-specific **demo spaces** inside a ClawColab workspace

## Repository structure
### Governance and coordination
- `COLLABORATION.md` — repo-level collaboration rules
- `ONBOARDING_SECOND_AGENT.md` — second-agent onboarding rules
- `DEMO_SPACES.md` — overview of demo-space structure
- `workspace/tasks/` — structured work items
- `workspace/proposals/` — changes awaiting approval
- `workspace/decisions/` — approved decisions
- `workspace/handoffs/` — transfer notes between agents or roles
- `workspace/risks/` — risk and ambiguity records
- `workspace/claims/` — task claim records for claimable work
- `workspace/policy/` — visibility, role, and approval policy files
- `sealed/INDEX.md` — summary-only references to confidential context

### Demo spaces
- `workspace/demo-spaces/` — example layout for project-specific workspaces inside one collaboration boundary
- `workspace/demo-spaces/btcforecast/` — preserved example demo space

## How to start your first real project
1. Create a new repository from this ClawColab pattern.
2. Define the collaborators and approval roles for that repository.
3. Add your first project inside `workspace/demo-spaces/<project-name>/` if needed.
4. Create the first task, proposal, and decision records.
5. Keep future projects with different people or different secrecy boundaries in separate ClawColab repositories.

## Current operating model of this public repo
- This repository is primarily a public project, template, and reference implementation.
- It demonstrates how a ClawColab workspace can be structured.
- Real collaboration should usually happen in separate derived ClawColab repositories.

## Operating rule
If approval is required and not explicitly recorded, treat the change as **not approved**.
