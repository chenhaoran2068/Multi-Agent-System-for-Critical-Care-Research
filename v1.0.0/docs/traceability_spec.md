# Traceability Specification - v1.0.0

This document defines the minimum evidence chain required for every formal output in v1.0.0.

The goal is simple:
no important conclusion should exist without a reconstructable path back to the question, plan, code, execution, and validation context that produced it.

## Core principle

Traceability is not an optional reporting feature.
It is a release condition.

If the system cannot show where a claim came from, that claim is not ready to leave the workflow.

## Minimum trace chain

Every completed task must be able to connect these identifiers:

- `task_id`
- `question_id`
- `mapping_id` when applicable
- `plan_id`
- `approval_id`
- `code_artifact_id`
- `run_id`
- `result_artifact_id`
- `validation_report_id`
- `interpretation_id`
- `trace_bundle_id`
- `decision_log_id`

## Required object relationships

### Research question layer

A `research_question` object must link to:
- `task_id`
- study title
- question class
- time-zero definition
- version

### Variable mapping layer

A `variable_mapping` object must link to:
- `question_id`
- source-layer trace
- missing-variable notes
- version

### Analysis plan layer

An `analysis_plan` object must link to:
- `question_id`
- `mapping_id` when relevant
- approval status or approval reference
- interpretation boundary
- version

### Code layer

A `code_artifact` object must link to:
- `plan_id`
- declared language and entrypoint
- generated file list
- dependencies
- code hash when possible

### Execution layer

A `run_manifest` must link to:
- `task_id`
- `plan_id`
- execution environment summary
- input datasets
- random seed or deterministic note
- output artifact list
- log paths
- run timestamps

### Result layer

Every `result_artifact` must link to:
- `run_id`
- `plan_id`
- `source_code_artifact_id`
- dataset version when known
- validation status

### Interpretation layer

Every interpretation claim must link to:
- one or more `result_artifact_id`
- interpretation type: fact, statistical_result, interpretation, or hypothesis
- confidence or limitation note when needed

### Audit layer

A `trace_bundle` must link the whole chain together.
It should be possible to reconstruct a release decision from the trace bundle without guessing hidden context.

## Required trace checks before release

The release gate should confirm:
- every formal claim links to validated result artifacts
- every result artifact links to a code artifact and run context
- every code artifact links to an approved plan
- every plan links to a research question
- every required approval node is present when triggered
- no terminal output depends on unversioned upstream state

## Trace completeness levels

### Level 0 - insufficient

Missing one or more of:
- plan linkage
- run linkage
- result linkage
- validation linkage
- claim linkage

This level is not releasable.

### Level 1 - minimally sufficient

The full object chain exists, but some secondary metadata may be sparse.
This is the minimum v1 release level.

### Level 2 - audit-strong

The full chain exists and includes:
- decision rationale
- approval notes
- code hash
- environment metadata
- rerun history
- branch history when applicable

This is the preferred internal quality standard.

## Branch traceability

If the system uses multiple branches, each branch must retain:
- `branch_id`
- parent `task_id`
- parent `plan_id`
- branch-specific code and result artifact IDs
- merge notes for any aggregation step

No branch output may be silently merged into the main result package without a record.

## Human intervention traceability

When a human decision changes workflow behavior, record:
- who approved
- what was approved
- why approval was needed
- what workflow state was active
- what downstream actions became allowed

## Required trace files in a task run

At minimum, each run folder should be able to contain or reference:
- `run_manifest.json`
- `audit/decision_log.jsonl`
- `audit/approval_log.jsonl`
- `audit/state_transitions.jsonl`
- `artifacts/` object files or indexes
- `logs/` execution logs
- `audit/trace_bundle.json`

## Failure policy

If trace data is partially missing:
- stop release
- route to `revision_required` if repairable
- route to `failed` if the missing chain cannot be reconstructed safely

## v1 recommendation

Prefer explicit IDs and explicit links everywhere.
A slightly verbose trace chain is much cheaper than arguing later about where a result came from.
