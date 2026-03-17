# Skill Design Rules - v1.0.0

This document captures the design rules used for project-native skills in v1.

It is derived from the `skill-creator` guidance and adapted to the critical care research system.

## Why this document exists

The project does not want broad, vague, or unsafe skills.
It wants small, auditable, role-aligned skills that fit the v1 workflow.

## Core skill principles for this project

### 1. Narrow scope beats broad capability

A v1 skill should solve one bounded problem.
If a skill appears to handle an entire product surface, it is too large for v1.

### 2. Local-first by default

A v1 skill should prefer local files, local reasoning, and local artifacts.
Any network behavior must be explicit and approval-aware.

### 3. Workflow obedience is mandatory

A skill must not bypass:
- plan before code
- validation before interpretation
- trace before release
- protected-data restrictions
- human approval for material escalation

### 4. Description must carry trigger logic

The YAML `description` is not just a summary.
It should clearly say:
- what the skill does
- when it should be used
- what kinds of tasks should trigger it

### 5. SKILL.md should be concise and imperative

The body should tell the agent what to do.
It should not turn into a long essay or architecture memo.
If detailed design rationale is needed, store it in project docs, not inside the skill.

### 6. Prefer wrappers over imports

When borrowing from upstream MedgeClaw skills:
- keep only the useful core logic
- remove broad autonomy
- remove unsafe network defaults
- remove nonessential visual or publishing expectations

### 7. Every skill must state forbidden behavior

A v1 skill should say not only what it does, but what it must not do.
This is especially important for:
- network access
- protected data access
- interpretation drift
- publication-style output
- clinical-advice-like output

### 8. Agent alignment matters

Each skill should map cleanly to one or more existing project agents.
If a skill does not have a natural agent home, it probably should not exist yet.

## Required elements for project-native skills

Every v1 skill should make clear:
- purpose
- trigger conditions
- required inputs or upstream objects
- expected outputs
- safe-use constraints
- forbidden actions
- approval mapping
- agent alignment

## What v1 skills should avoid

Do not put these into the v1 skill layer by default:
- broad web search workflows
- mandatory external APIs
- autonomous manuscript production
- mandatory figure generation
- clinical advice or treatment suggestion logic
- broad dispatch engines
- hidden package installation behavior

## Preferred skill shape

For this project, the preferred skill shape is:
- one concise `SKILL.md`
- optional small `references/` files only when truly needed
- no bloated support docs inside the skill folder
- no extra README files inside each skill

## Bottom line

A good v1 skill is:
- narrow
- local-first
- approval-aware
- trace-friendly
- aligned to one workflow role
- explicit about its limits
