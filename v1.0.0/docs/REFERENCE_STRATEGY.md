# Reference Strategy - MedgeClaw to v1.0.0

This document explains how the project should stand on the shoulders of MedgeClaw without inheriting unnecessary scope or complexity.

## Core principle

Borrow architecture, governance, and reusable discipline.
Do not copy full breadth, full weight, or unrelated domain capability.

## What to borrow from MedgeClaw

### 1. Rule-first project governance
Borrow the pattern of defining project rules explicitly through core documents before expanding capabilities.

Useful inspiration:
- `MEDGECLAW.md`
- `CLAUDE.md`
- workspace-level boundary and behavior files

How to adapt:
- create strict v1 project rule files for scope, safety, traceability, and delivery constraints
- treat these files as system contracts, not optional notes

### 2. Modular capability organization
Borrow the idea of splitting capabilities into bounded modules rather than putting everything into one giant agent.

Useful inspiration:
- `skills/`
- `scientific-skills/`
- `scientific-writer/skills/`

How to adapt:
- use `agents/` plus `schemas/` plus rule docs as the v1 equivalent of bounded capabilities
- keep agent responsibilities narrow and auditable
- prefer composable modules over one omniscient workflow

### 3. Output discipline and directory structure
Borrow the idea that outputs belong in clearly defined folders with role-specific meaning.

Useful inspiration:
- `data/`
- `outputs/`
- `writing_outputs/`

How to adapt:
- maintain explicit separation between raw, interim, analytic, outputs, logs, and qc artifacts
- define naming and storage conventions before execution logic grows complex

### 4. Skill-driven execution mindset
Borrow the mindset that specialized tasks should be guided by explicit instructions and best practices.

Useful inspiration:
- specialized `SKILL.md` files
- domain-specific execution guidance

How to adapt:
- translate this into explicit agent contracts, workflow constraints, SAP templates, and schema-driven handoffs
- for v1, discipline beats generality

### 5. Reporting awareness
Borrow the idea that results are not complete until they are clearly packaged for human review.

Useful inspiration:
- `dashboard`
- `svg-ui-templates`
- `feishu-rich-card`

How to adapt:
- ensure v1 result delivery includes readable tables, figures, and trace links
- do not prioritize a fancy UI, but do prioritize understandable artifact presentation

### 6. Separation of strategic vision and execution layer
Borrow the idea that high-level identity and day-to-day execution can be separated cleanly.

How to adapt:
- preserve `Guideline/` as the north-star vision layer
- use `v1.0.0/` as the execution layer for the first practical milestone

## What not to borrow directly

### 1. Full-domain breadth
Do not import the full all-discipline scientific scope.

Reason:
- v1 needs focus on emergency medicine, ICU, and critical care database research only

### 2. Heavy academic writing stack as a blocker
Do not make full manuscript generation a prerequisite for v1.

Reason:
- the first milestone is trustworthy analysis, not publication automation

### 3. Omics, imaging, instrumentation, and wet-lab paths
Do not pull in bioinformatics, device integration, or unstructured modality workflows into the v1 mainline.

Reason:
- these are valuable later, but harmful to early scope control

### 4. Overweight capability catalogs
Do not mirror the full scale of MedgeClaw's capability inventory.

Reason:
- a broad catalog is useful in a mature platform, but distracting in an MVP

### 5. Appearance-first delivery
Do not over-invest in polished presentation before traceable correctness is stable.

Reason:
- the first competitive advantage is research credibility, not cosmetics

## Recommended reference mapping

### MedgeClaw layer -> v1.0.0 layer
- `Guiding project rules` -> `docs/product_scope.md`, `docs/traceability_spec.md`, `docs/SAP.md`
- `Skill modularity` -> `agents/`, `schemas/`, `agent_contracts.md`
- `Output discipline` -> `outputs/`, future `logs/`, `qc/`, and artifact conventions
- `Scientific best-practice guidance` -> templates, checklists, validation plans, guardrails
- `Report packaging mindset` -> baseline report layouts and trace-aware result bundles

## Practical rule for this project

When borrowing from MedgeClaw, always ask:
1. Does this increase traceable end-to-end analysis quality?
2. Does this help scope control and auditability?
3. Is this necessary for emergency/ICU/critical care database research v1?

If the answer is not mostly yes, defer it.

## Bottom line

This project should inherit MedgeClaw's strengths in:
- modular organization
- explicit operating rules
- disciplined outputs
- reusable specialist guidance

It should not inherit MedgeClaw's full size, broad scientific breadth, or heavyweight feature surface.

The correct move is to borrow the skeleton, not the entire body.
