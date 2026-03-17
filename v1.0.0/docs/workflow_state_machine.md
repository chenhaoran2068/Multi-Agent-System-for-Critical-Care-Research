# Workflow State Machine - v1.0.0

This document is the human-readable companion to `../default_pipeline.json`.

The system uses a state machine first, not a free-form agent conversation model.
That choice is intentional.
It keeps the research workflow auditable, makes approval points explicit, and prevents downstream agents from skipping upstream discipline.

## Design goal

The v1 workflow should be able to answer one narrow question well:

Can the system turn a bounded critical care database research question into a traceable, reproducible, conservatively interpreted result package without silently drifting, fabricating, or bypassing human control?

## Core states

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `queued` | Task exists but has not yet been normalized | `intake_ready`, `failed` |
| `intake_ready` | User request has been clarified enough to start formal design | `design_ready`, `failed` |
| `design_ready` | Structured research question is ready | `mapping_ready`, `plan_ready`, `failed` |
| `mapping_ready` | Variable mapping is complete for clinical database analysis mode | `plan_ready`, `failed` |
| `plan_ready` | Analysis plan exists and is ready for approval review | `approval_pending`, `failed` |
| `approval_pending` | Workflow is waiting on approval policy evaluation or explicit human review | `approved_for_codegen`, `blocked_by_policy`, `failed` |
| `approved_for_codegen` | Code generation is permitted under policy | `code_ready`, `failed` |
| `code_ready` | Execution package exists but has not run yet | `execution_running`, `failed` |
| `execution_running` | Execution is in progress | `execution_ready`, `failed` |
| `execution_ready` | Execution outputs exist and are ready for validator review | `validation_ready`, `failed` |
| `validation_ready` | Validator has the execution package and may pass or request revision | `interpretation_ready`, `revision_required`, `failed` |
| `interpretation_ready` | Interpretation may proceed because validation passed | `audit_ready`, `failed` |
| `audit_ready` | Final traceability assembly is underway | `completed`, `revision_required`, `failed` |
| `revision_required` | A bounded repair loop is required before release | `code_ready`, `failed` |
| `blocked_by_policy` | A policy rule prevents autonomous continuation | terminal unless a human explicitly resolves it |
| `completed` | Release bundle is ready for human review or internal use | terminal |
| `failed` | Fatal stop condition or unrecoverable inconsistency | terminal |

## Why `design_ready` can branch two ways

The system supports two narrow v1 task modes:

1. `clinical_db_analysis`
2. `research_writing_support`

For clinical database analysis, the path is:

`design_ready -> mapping_ready -> plan_ready`

For bounded writing support, the path may be:

`design_ready -> plan_ready`

That shortcut exists because a writing support task may operate on already validated result artifacts rather than raw variable mapping work.
Even then, it is still constrained by the same interpretation and audit rules.

## Transition rules by stage

### 1. `queued -> intake_ready`

The orchestrator confirms that the task is within v1 scope and creates a stable task record.

Minimum conditions:
- research intent is recognizable
- domain is critical care / ICU / emergency medicine
- task is a database research task rather than bedside clinical decision support
- no obvious policy red line is already triggered

### 2. `intake_ready -> design_ready`

The Study Design Agent converts the request into a structured research question.

Minimum outputs:
- research question object
- explicit population, exposure, outcome, time zero, and follow-up framing
- ambiguity notes if anything still needs approval or clarification

### 3. `design_ready -> mapping_ready`

This transition is required for `clinical_db_analysis`.

The Data Mapping Agent must:
- identify source variables
- document missing or partial mappings
- avoid pretending a missing variable exists
- keep the database foundation read-only unless separately approved

### 4. `mapping_ready -> plan_ready`

The Analysis Planning Agent writes a study-specific SAP-aligned plan.

Minimum outputs:
- primary analysis method
- endpoint definitions
- subgroup and sensitivity boundaries
- missing-data strategy
- output shells or output expectations
- interpretation boundary

### 5. `plan_ready -> approval_pending`

This is the first formal governance gate.
The orchestrator evaluates the planned actions against `docs/approval_matrix.md` and `docs/policy_engine_rules.yaml`.

This transition always happens before code generation.

### 6. `approval_pending -> approved_for_codegen`

Autonomous continuation is allowed only when the action set is compatible with:
- `auto-allow`
- `allow-with-log`
- a recorded explicit approval outcome

If any required action is `require-human-approval` and no approval exists yet, the system must not continue.

### 7. `approval_pending -> blocked_by_policy`

Use this state when:
- a human approval is required and still missing
- a `never-allow-in-v1` action is detected
- the plan would mutate the protected data foundation
- the plan would use disallowed claim language or bypass traceability rules

### 8. `approved_for_codegen -> code_ready`

The Code Generation Agent produces the execution package.

Minimum outputs:
- code artifact object
- execution entrypoint
- declared dependencies
- planned output list

### 9. `code_ready -> execution_running -> execution_ready`

Execution may begin only after code exists and approval conditions are satisfied.

Execution outputs must include:
- run manifest
- raw logs
- produced result artifacts
- failure notes when any sub-step fails

The run may not fabricate placeholder results.

### 10. `execution_ready -> validation_ready`

The Execution Validator Agent receives the run package.
It checks:
- did the code run
- were expected outputs produced
- do counts and basic consistency checks pass
- are result artifacts fit for interpretation

### 11. `validation_ready -> interpretation_ready`

This transition is allowed only when validation passes.
Interpretation must never start from failed or incomplete outputs.

### 12. `validation_ready -> revision_required`

Use this path when the issue is bounded and repairable, such as:
- missing output file
- naming mismatch
- failed figure export
- code bug that does not change the approved plan
- missing validation field or run metadata

This is not a license for open-ended iteration.
The default pipeline allows one bounded revision loop.

### 13. `interpretation_ready -> audit_ready`

The Interpretation Agent writes a conservative study-facing interpretation.
The Audit / Trace Agent then assembles the evidence chain.

Interpretation claims must cite result artifact IDs.

### 14. `audit_ready -> completed`

Release is allowed only when the trace bundle is complete.
The minimum release bundle is defined in `../default_pipeline.json`.

### 15. `audit_ready -> revision_required`

This transition exists because traceability gaps are release blockers.
Examples:
- interpretation exists but lacks result links
- result artifacts exist but do not point to code artifacts
- approval node is missing for a method change
- run manifest is incomplete

## Terminal states

### `completed`

The package is ready for human review or internal use.
This does not mean the system has scientific sovereignty.
It means the package cleared the v1 workflow.

### `blocked_by_policy`

A non-terminal workflow problem could still be resolved by a human, but autonomous progress must stop.
Typical reasons:
- new variable insertion request
- non-default time zero
- causal wording request
- direct raw-layer access
- unsupported methodological escalation

### `failed`

Use `failed` for fatal stops such as:
- impossible or contradictory question framing
- repeated unrecoverable execution failure
- corrupted outputs
- revision loop exhausted
- unrecoverable trace break

## Revision policy

`revision_required` is a repair node, not a shadow workflow.

Allowed:
- bug fix without changing study meaning
- rerun after technical failure
- restore missing metadata
- regenerate a broken figure

Not allowed without new approval:
- changing the cohort
- changing the endpoint
- changing the main method family
- changing the interpretation boundary

## Writing support branch policy

The writing-oriented branch templates in `../default_pipeline.json` are deliberately narrow.
They may generate:
- internal summary drafts
- methods appendix drafts
- limitations notes

They may not autonomously generate:
- final manuscript submission packages
- external publication claims
- stronger conclusions than the validated result package supports

## State-machine-first advantages

This design gives v1 four practical benefits:
- easier audit of who did what and when
- explicit policy choke points
- bounded revision loops
- cleaner handoffs between structured schema objects

## Relationship to implementation

`scripts/run_backend.py` should treat this document and `../default_pipeline.json` as the source of truth for allowed transitions.
If implementation behavior differs from these files, the implementation is wrong and should be corrected rather than silently redefining the workflow.
