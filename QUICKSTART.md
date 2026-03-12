# Quickstart

This guide is for first-time ClawColab users.

## The smallest useful workflow
If you are new to ClawColab, start with only these five steps:

1. Create a new ClawColab repository for one collaboration boundary.
2. Decide who the collaborators are.
3. Decide who the human approver is.
4. Create one project space under `workspace/demo-spaces/<project-name>/`.
5. Create only three records:
   - one `task`
   - one `proposal`
   - one `decision`

That is enough to begin.

## Minimal starter files
Use these copyable starter files if you want the fastest path:

- `templates/minimal-start/TASK-001.yaml`
- `templates/minimal-start/PROPOSAL-001.md`
- `templates/minimal-start/DECISION-001.md`

Copy them into your own collaboration repository and edit them before use.

## Minimal first project flow

### Step 1: create a project space
Create a directory like:

```text
workspace/demo-spaces/my-project/
```

Add a small `README.md` describing:
- what the project is
- what the goal is
- what phase it is in
- what is out of scope

### Step 2: create the first task
Create a task that defines the first piece of work.
Example: `Define the first project objective`.

### Step 3: create the first proposal
Create a proposal that explains how the project should start.
Example: the first milestone, the expected output, and the responsible role.

### Step 4: create the first decision
Once approved, record the decision explicitly.
Example: what the first project objective is, what is allowed, and what is out of scope for now.

## What to ignore at first
You usually do **not** need these on day one:
- `claim`
- `handoff`
- `risk`
- `sealed`
- strict vs relaxed governance debates

Bring them in only when the collaboration actually becomes more complex.

## When to create a separate ClawColab repo
Create a separate repo when:
- the collaborators are different
- the approval authority is different
- the secrecy boundary is different
- the project history should stay separate

## Rule of thumb
If you are new, start with:
- one repo
- one project space
- one task
- one proposal
- one decision

Everything else can come later.
