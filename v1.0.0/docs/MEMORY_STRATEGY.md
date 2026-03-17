# Memory Strategy - v1.0.0

This document defines the memory-layer strategy for the critical care research project.

The goal is to prevent two common failures:
- project-specific details polluting long-term assistant memory
- important cross-session decisions getting lost inside one long chat thread

## Two memory layers

### 1. Assistant-level memory

Location:
- `C:\Users\chr17\.openclaw\workspace\MEMORY.md`
- `C:\Users\chr17\.openclaw\workspace\memory\YYYY-MM-DD.md`

Purpose:
- store long-lived collaboration context between the human and the assistant
- store cross-project preferences, habits, environment facts, and recurring working rules
- preserve daily operational notes that may later be distilled into long-term memory

What belongs here:
- user workflow preferences
- review and approval preferences
- environment facts about OpenClaw / MedgeClaw / Windows setup
- recurring quality expectations such as conservative interpretation and audit-first behavior
- lessons learned that apply across multiple projects

What should not dominate here:
- detailed project-specific state for a single repository
- transient implementation notes that only matter for one project version
- long checklists that belong to a project workstream rather than global collaboration

### 2. Project-level memory

Location:
- `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0\memory\PROJECT_MEMORY.md`
- `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0\memory\SESSION_LOG.md`
- `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0\memory\DECISIONS.md`
- `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0\memory\OPEN_QUESTIONS.md`

Purpose:
- store the durable working memory for this project only
- preserve architecture choices, stage status, pending work, review findings, and unresolved questions
- support heavy long-horizon human-AI collaboration without bloating the assistant-level memory

What belongs here:
- current v1 scope boundaries
- phase completion status
- project-specific architecture and governance decisions
- review findings and revision candidates
- project-specific terminology, paths, and traceability conventions
- pending questions awaiting human approval

What should not go here:
- generic user preferences that apply outside this repo
- personal reminders unrelated to the project
- assistant-environment facts that belong to global memory

## Retrieval priority

When answering project questions, the preferred lookup order should be:

1. project-level memory in `v1.0.0\memory\`
2. assistant-level `MEMORY.md`
3. assistant-level daily notes in `workspace\memory\`

Reason:
- project context should win for this repository
- assistant memory should supply stable collaboration rules
- daily logs are supplemental, not primary truth

## File roles inside project memory

### `PROJECT_MEMORY.md`

Use for stable project facts that should survive many sessions.
Examples:
- product boundaries
- workflow architecture decisions
- what phases are complete
- what must happen before later phases can start

### `SESSION_LOG.md`

Use for rolling operational notes.
Examples:
- what was implemented today
- what was validated today
- what failed and why
- what changed since the last review

### `DECISIONS.md`

Use for explicit decision records.
Each entry should capture:
- date
- decision
- reason
- impact
- whether human approval was involved

### `OPEN_QUESTIONS.md`

Use for unresolved issues that should not be buried in chat history.
Examples:
- pending approval requests
- unresolved design forks
- unclear policy behaviors
- deferred implementation tradeoffs

## Write policy

### Write to assistant-level memory when:
- the fact is cross-project
- the fact reflects a stable working preference
- the fact is about the assistant environment rather than one repo

### Write to project-level memory when:
- the fact only matters to this project
- the fact tracks project progress or open work
- the fact describes a project-specific decision or unresolved issue

## Distillation policy

Do not copy everything into both layers.
Instead:
- keep detailed project context in project memory
- periodically distill only the cross-project lessons into assistant-level memory

## v1 recommendation

Treat project memory as the main continuity layer for this repository.
Treat assistant memory as the higher-level collaboration memory that spans many projects and sessions.
