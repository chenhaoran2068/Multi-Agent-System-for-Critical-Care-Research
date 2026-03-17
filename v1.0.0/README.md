# Multi-Agent System for Critical Care Research - v1.0.0

This folder contains the first implementation scope for the project.

The long-term vision remains in `../Guideline/` and is intentionally preserved without modification. This version only defines the minimum viable system that we can build, test, and iterate on step by step.

## Positioning

Version `1.0.0` is the first practical milestone for a focused critical care research assistant.

It is intentionally narrow:
- Domain boundary: emergency medicine, ICU, and critical care database research only
- Task boundary: structured clinical database analysis only
- Delivery boundary: study plan, analysis code, result tables/figures, and written interpretation
- Safety boundary: every conclusion must be traceable to data, code, and execution logs
- Interaction boundary: the system may propose adjacent ideas, but if they drift away from the main research objective, it only summarizes them in an organized report and does not execute deep follow-up analysis by default

## What v1.0.0 does

The system accepts a user research question and drives a controlled workflow:
1. Clarify the clinical research question
2. Convert it into a structured analysis specification
3. Select suitable statistical methods
4. Generate reproducible analysis code
5. Run the analysis and save logs
6. Return tables, figures, and an interpretable summary
7. Optionally list related but out-of-scope exploratory ideas as follow-up suggestions only

## What v1.0.0 does not do

This version does not aim to fully automate:
- autonomous topic discovery
- autonomous literature surveillance
- autonomous research portfolio expansion with full execution
- wet lab, instrument, or omics workflows
- full manuscript generation for top-tier journals as a default output
- unrestricted multi-agent debate loops

## Folder map

- `docs/` - scope, implementation checklist, architecture, workflow, state machine, policy rules, handoff contracts, traceability, audit, and review governance
- `agents/` - agent role definitions
- `schemas/` - structured task and result schemas
- `scripts/` - executable workflow skeleton and future orchestration glue
- `examples/` - example task inputs and outputs
- `outputs/` - reserved location for future run artifacts

## Workflow backbone

The first machine-readable backbone for v1 now exists.

Core files:
- `default_pipeline.json` - machine-readable pipeline order, state transitions, approval gate position, revision loop, and release bundle requirements
- `docs/workflow_state_machine.md` - human-readable explanation of the same workflow states and transitions
- `docs/policy_engine_rules.yaml` - guardrail and approval-rule skeleton aligned to `docs/approval_matrix.md`
- `docs/handoff_contracts.md` - structured handoff envelope between agents
- `run_manifest.json` - template for per-task run state, trace pointers, and audit paths
- `scripts/run_backend.py` - minimal backend skeleton that can initialize a task manifest and validate state transitions

Example usage:

```bash
python scripts/run_backend.py init \
  --task-id task_demo_001 \
  --task-mode clinical_db_analysis \
  --title "ICU vasopressor exposure and 28-day mortality"

python scripts/run_backend.py inspect --task-id task_demo_001
python scripts/run_backend.py transition --task-id task_demo_001 --next-state intake_ready --actor orchestrator-agent --note "Question intake completed"
```

## Versioning note

This project uses semantic versioning style labels.

For now:
- `v1.0.0` means the first concrete, user-facing implementation scope
- future compatible additions can move to `v1.1.0`
- breaking redesigns can move to `v2.0.0`

## Reference baseline

This version may selectively borrow proven ideas and safe reusable capabilities from MedgeClaw, especially around modular capability design, rule-first governance, disciplined output organization, and bounded skill reuse.

It should not inherit MedgeClaw's full all-discipline scope or heavyweight capability surface. See `docs/REFERENCE_STRATEGY.md` and `docs/SKILL_REUSE_STRATEGY.md`.

## System soul

The system's research temperament and non-negotiable working philosophy are defined in `SOUL.md`.

## Relationship to the long-term vision

The files under `../Guideline/` remain the strategic north star.

This `v1.0.0` folder is the execution layer for the first small, reliable step toward that larger vision.
