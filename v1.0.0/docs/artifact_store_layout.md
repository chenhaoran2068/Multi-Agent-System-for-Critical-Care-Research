# Artifact Store Layout - v1.0.0

This document defines the default on-disk layout for workflow runs.

The layout is intentionally simple.
A v1 system should be able to store all important objects, logs, and trace files without requiring a database just to understand one run.

## Root convention

All task runs should live under:

`outputs/{task_id}/`

## Recommended layout

```text
outputs/
  {task_id}/
    run_manifest.json
    artifacts/
      research_question/
      variable_mapping/
      analysis_plan/
      code_artifact/
      result_artifact/
      interpretation/
      trace_bundle/
      audit_summary/
      ideas_summary/
    logs/
      execution/
      validation/
    audit/
      decision_log.jsonl
      approval_log.jsonl
      state_transitions.jsonl
      release_decision.json
    branches/
      {branch_id}/
        branch_manifest.json
        artifacts/
        logs/
```

## Artifact object storage rule

Each formal object should be written as its own JSON file when practical.
Suggested naming pattern:

`{object_type}/{object_id}.json`

Examples:
- `artifacts/research_question/rq_001.json`
- `artifacts/analysis_plan/plan_001.json`
- `artifacts/result_artifact/result_003.json`
- `artifacts/trace_bundle/trace_001.json`

## Branch storage rule

If a branch exists, it should not overwrite the main branch artifacts silently.
Branch-specific outputs belong under:

`outputs/{task_id}/branches/{branch_id}/`

The main run may later reference branch outputs through aggregation metadata or the final trace bundle.

## Log storage rule

Separate execution logs from audit logs.

- execution logs explain runtime behavior
- audit logs explain governance and workflow decisions

Suggested execution log naming:
- `logs/execution/{run_id}.log`
- `logs/validation/{validation_report_id}.log`

## Immutability recommendation

Formal artifacts should be treated as versioned snapshots.
If an object changes materially, create a new versioned file rather than overwriting silently.

## Release bundle recommendation

A releasable task folder should be able to point to or contain:
- final `run_manifest.json`
- latest approved `research_question`
- latest approved `analysis_plan`
- code artifact index
- validated result artifacts
- final interpretation object
- trace bundle
- audit summary
- release decision record

## Forbidden layout behaviors

Do not:
- mix audit logs into execution log folders
- overwrite branch outputs without a history trail
- store final interpretation outside the artifact tree with no reference
- rely on temporary scratch files as the only record of a formal object

## v1 recommendation

Start file-system first.
If the project later grows into a service or database-backed registry, keep this folder layout as the canonical export shape so one run remains human-inspectable.
