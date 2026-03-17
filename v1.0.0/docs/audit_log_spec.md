# Audit Log Specification - v1.0.0

This document defines the minimum audit logging requirements for a task run.

The audit log is not the same as raw execution logs.
Execution logs explain what the code did.
Audit logs explain what the system decided, when it decided it, and why that decision was allowed.

## Goals

The audit layer should make it possible to answer these questions:
- what question was the system actually trying to answer
- what plan was approved
- what state transitions happened
- what approvals were required
- what code and execution run produced the final results
- why the final package was considered releasable or blocked

## Required audit streams

### 1. `decision_log.jsonl`

Captures workflow-shaping decisions.

Minimum fields per line:
- `decision_log_id`
- `task_id`
- `timestamp`
- `actor`
- `state`
- `decision_type`
- `summary`
- `reason`
- `object_refs`
- `policy_refs`

### 2. `approval_log.jsonl`

Captures explicit approval-related events.

Minimum fields per line:
- `approval_id`
- `task_id`
- `timestamp`
- `requested_action`
- `approval_level`
- `decision`
- `approver`
- `scope`
- `rationale`
- `object_refs`

### 3. `state_transitions.jsonl`

Captures every state-machine transition.

Minimum fields per line:
- `transition_id`
- `task_id`
- `timestamp`
- `from_state`
- `to_state`
- `stage`
- `actor`
- `note`
- `manifest_path`

### 4. `release_decision.json`

One per task release attempt.

Minimum fields:
- `task_id`
- `timestamp`
- `audit_status`
- `trace_bundle_id`
- `release_decision`
- `blocking_issues`
- `release_scope`

## Recommended optional audit streams

- `branch_events.jsonl`
- `validation_findings.jsonl`
- `rerun_log.jsonl`
- `artifact_index.jsonl`

## Event type recommendations

### Decision types
- `scope_classification`
- `question_clarification`
- `mapping_resolution`
- `method_selection`
- `approval_required`
- `approval_bypass_denied`
- `revision_requested`
- `release_blocked`
- `release_allowed`

### Approval decisions
- `auto-allow`
- `allow-with-log`
- `require-human-approval`
- `approved`
- `denied`
- `never-allow-in-v1`

## Write policy

Audit events should be append-only.
Do not rewrite historical audit entries in place.
If correction is needed, append a new event that references the earlier event.

## Minimum retention policy for v1

Keep audit records for every completed, blocked, or failed task run.
The system should not discard them just because the main output was unsatisfactory.
Failed runs are part of the evidence chain.

## Example `state_transitions.jsonl` entry

```json
{
  "transition_id": "transition_003",
  "task_id": "task_001",
  "timestamp": "2026-03-17T02:10:00Z",
  "from_state": "plan_ready",
  "to_state": "approval_pending",
  "stage": "approval_gate",
  "actor": "orchestrator-agent",
  "note": "Plan submitted for approval evaluation.",
  "manifest_path": "outputs/task_001/run_manifest.json"
}
```

## Example `approval_log.jsonl` entry

```json
{
  "approval_id": "approval_004",
  "task_id": "task_001",
  "timestamp": "2026-03-17T02:12:00Z",
  "requested_action": "use non-default time zero",
  "approval_level": "require-human-approval",
  "decision": "approved",
  "approver": "human_reviewer",
  "scope": "study_design",
  "rationale": "Custom time zero is necessary for exposure alignment.",
  "object_refs": ["rq_001", "plan_001"]
}
```

## Blocking conditions

The audit layer should block release if:
- required state transitions are missing
- approval-required actions lack approval entries
- interpretation exists without validation evidence
- release decision exists without a trace bundle reference

## v1 recommendation

Keep the audit format boring and explicit.
The system will benefit more from clean append-only logs than from clever but hard-to-read provenance graphs.
