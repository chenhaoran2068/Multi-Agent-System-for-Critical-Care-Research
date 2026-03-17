# Project Memory - Multi-Agent System for Critical Care Research v1.0.0

## Project identity

- Project root: `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0`
- Positioning: a focused critical care database research assistant, not a full autonomous research laboratory
- Long-term vision stays in `../Guideline/`
- Upstream data foundation reference: `D:\Database\FRAMEWORK_v4_COMPLETE.md`

## Current scope boundaries

- Domain: emergency medicine, ICU, and critical care database research only
- Task type: structured clinical database analysis only
- Output type: structured question, analysis plan, reproducible code, validated results, conservative interpretation
- Guardrails: plan before code, validation before interpretation, trace before release, human approval for material escalation
- Version boundary: `v1` targets the minimum trustworthy end-to-end workflow loop; broad web, publishing, image-generation, and clinical-advice-adjacent capabilities are deferred to `v2`

## Current implementation status

Completed:
- v1 positioning and scope documents
- architecture, workflow, approval matrix, agent contracts, SAP, data-foundation relation
- schemas and pydantic models
- default pipeline machine skeleton
- workflow state machine documentation
- policy engine rule skeleton
- handoff contracts
- traceability and audit specifications
- run manifest template
- artifact store layout
- success, acceptance, and review documents
- README and README_ZH entrypoints for the workflow backbone
- minimal executable `scripts/run_backend.py` that can initialize and validate state transitions

Phase 3 status:
- phase 3 skill reuse review is complete at the design level
- security-aware review document: `docs/SKILL_SECURITY_REVIEW_V1.md`
- wrapper selection and prioritization document: `docs/SKILL_WRAPPER_PLAN_V1.md`
- phase-end summary document: `docs/PHASE3_REPORT.md`
- direct-reuse candidates are narrow and local-first: `cjk-viz`, `scientific-critical-thinking`, and optional `svg-ui-templates`
- project-native wrapper skill skeletons now exist under `skills/`:
  - `critical-care-review-helper`
  - `critical-care-paper-repro-helper`
  - `critical-care-writing-helper`
  - `critical-care-doc-convert`
  - `critical-care-local-dashboard`
- broad web, publishing, image-generation, and clinical-advice-adjacent skills are excluded from v1 mainline unless revisited later

Not started yet:
- runtime wiring of wrapper skills into agents and workflow stages
- examples / golden path demo
- runtime orchestration glue beyond the skeleton
- real execution integration and regression tests

## Current sequencing rule

- Finish memory strategy and memory-layer repair first
- Then resume project work from the existing plan
- Phase 3 skill work must not begin until the human reviews and approves the phase-2 report and revision list
