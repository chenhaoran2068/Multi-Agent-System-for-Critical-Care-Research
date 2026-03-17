# Acceptance Criteria - v1.0.0

This document defines the minimum gate for approving the v1 backbone before deeper implementation or skill expansion.

## Acceptance principle

The goal is not to prove the final system is complete.
The goal is to prove the v1 backbone is coherent enough that implementation will not rest on contradictory rules.

## Backbone acceptance criteria

The documentation and machine skeleton pass the v1 gate only if:

1. `README.md` and `README_ZH.md` clearly position v1 scope and point to the workflow backbone files
2. `default_pipeline.json` and `docs/workflow_state_machine.md` agree on the core states and transitions
3. `docs/policy_engine_rules.yaml` aligns with `docs/approval_matrix.md`
4. `docs/handoff_contracts.md` aligns with `docs/agent_contracts.md` and existing schemas
5. `run_manifest.json` can support the minimum trace chain defined in `docs/traceability_spec.md`
6. `scripts/run_backend.py` can at least initialize and validate state transitions against the pipeline
7. release requirements explicitly require validation and trace completeness before delivery

## Phase-2 acceptance criteria

The second phase is accepted only if the repository contains and aligns:
- `docs/traceability_spec.md`
- `docs/audit_log_spec.md`
- `run_manifest.json`
- `docs/artifact_store_layout.md`
- `docs/success_criteria.md`
- `docs/acceptance_criteria_v1.md`
- `docs/review_checklist.md`

## Internal consistency checks

The backbone should fail acceptance if any of the following occur:
- a document allows interpretation before validation
- a document allows code generation before SAP approval
- a machine file defines states that the docs do not explain
- an audit or trace spec does not have a place in the proposed artifact layout
- a writing branch silently exceeds the product scope into full autonomous manuscript production

## Implementation readiness criteria

The project is ready to move into implementation only when:
- state machine is stable enough to code against
- approval and policy boundaries are explicit
- agent handoffs are structured
- trace and audit files have clear destinations
- review criteria are concrete enough for self-check and human review

## What does not block acceptance yet

The following can still be missing after this gate:
- full runtime orchestration
- real database connectors
- full prompt library
- complete tests
- production packaging
- skill integration work

## Reviewer decision options

Use one of these outcomes:
- `accept`
- `accept_with_minor_revisions`
- `major_revisions_required`
- `reject_for_v1`

## v1 recommendation

Be strict at this gate.
A weak backbone becomes expensive later because every later component has to guess which rule set actually matters.
