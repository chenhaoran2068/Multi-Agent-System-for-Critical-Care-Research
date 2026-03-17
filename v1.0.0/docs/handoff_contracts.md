# Handoff Contracts - v1.0.0

This document defines how agents pass work to each other.
The goal is to prevent role drift, missing context, and hidden state.

A handoff is not free-form chat.
A handoff is a structured object package with explicit provenance.

## Global contract

Every handoff must include these fields:

- `handoff_id`
- `task_id`
- `source_agent`
- `target_agent`
- `state_before`
- `requested_next_state`
- `object_refs`
- `approval_status`
- `trace_refs`
- `created_at`
- `version`

## Required handoff envelope

```json
{
  "handoff_id": "handoff_001",
  "task_id": "task_001",
  "source_agent": "study-design-agent",
  "target_agent": "data-mapping-agent",
  "state_before": "design_ready",
  "requested_next_state": "mapping_ready",
  "object_refs": [
    {
      "object_type": "research_question",
      "object_id": "rq_001",
      "object_version": "1.0.0",
      "path": "outputs/task_001/artifacts/research_question.json"
    }
  ],
  "approval_status": "allow-with-log",
  "trace_refs": {
    "question_id": "rq_001",
    "decision_log_ids": ["decision_001"]
  },
  "created_at": "2026-03-17T10:30:00+09:00",
  "version": "1.0.0"
}
```

## Object-level requirements

### 1. Orchestrator -> Study Design Agent

Minimum payload:
- normalized user request
- task mode
- current state
- any existing human clarifications
- scope notes

Required object refs:
- none yet, unless task resume is happening

Expected output from next agent:
- `research_question`

### 2. Study Design Agent -> Data Mapping Agent

Minimum payload:
- approved or review-ready `research_question`
- time-zero definition
- cohort framing assumptions
- ambiguity list

Required object refs:
- `research_question`

Expected output from next agent:
- `variable_mapping`

### 3. Study Design Agent -> Analysis Planning Agent

Used only for `research_writing_support` or when mapping is already frozen upstream.

Required object refs:
- `research_question`
- optional validated `result_artifact` refs when writing support starts from finished outputs

Expected output from next agent:
- `analysis_plan`

### 4. Data Mapping Agent -> Analysis Planning Agent

Minimum payload:
- `research_question`
- `variable_mapping`
- missing-variable notes
- source-trace notes

Required object refs:
- `research_question`
- `variable_mapping`

Expected output from next agent:
- `analysis_plan`

### 5. Analysis Planning Agent -> Orchestrator

Purpose:
- submit the plan for approval evaluation

Required object refs:
- `analysis_plan`
- `research_question`
- `variable_mapping` when relevant

Expected output from next agent:
- `approval_record`

### 6. Orchestrator -> Code Generation Agent

May occur only after approval gate passes.

Required object refs:
- `research_question`
- `analysis_plan`
- `variable_mapping` when relevant
- `approval_record`

Expected output from next agent:
- `code_artifact`

### 7. Code Generation Agent -> Execution Validator Agent

Minimum payload:
- `code_artifact`
- `run_manifest`
- execution logs
- `result_artifact` refs

Required object refs:
- `code_artifact`
- `run_manifest`
- one or more `result_artifact`

Expected output from next agent:
- `validation_report`

### 8. Execution Validator Agent -> Interpretation Agent

May occur only when validation passed.

Required object refs:
- `validation_report`
- validated `result_artifact`
- `analysis_plan`

Expected output from next agent:
- `interpretation`

### 9. Interpretation Agent -> Audit / Trace Agent

Required object refs:
- `interpretation`
- `validation_report`
- `result_artifact`
- `code_artifact`
- `analysis_plan`
- `research_question`

Expected output from next agent:
- `trace_bundle`
- `audit_summary`

### 10. Audit / Trace Agent -> Orchestrator

Required object refs:
- `trace_bundle`
- `audit_summary`
- release bundle manifest

Expected output from next agent:
- delivery package or revision request

## Approval field semantics

Allowed values:
- `auto-allow`
- `allow-with-log`
- `require-human-approval`
- `approved`
- `denied`
- `never-allow-in-v1`

Rules:
- `require-human-approval` means the receiving agent must not execute the requested next stage
- `approved` means a human approval record is present
- `denied` and `never-allow-in-v1` should route to `blocked_by_policy` or `failed`

## Trace reference minimums

Every handoff must preserve enough information to reconstruct:
- which upstream objects existed
- which approvals applied
- which workflow state the system believed it was in
- why the handoff happened

At minimum, `trace_refs` should carry:
- `question_id` when available
- `plan_id` when available
- `run_id` when available
- `decision_log_ids`
- `approval_ids` when available

## Forbidden handoff patterns

Do not allow:
- downstream agent execution on plain-text intent without schema object refs
- interpretation handoff without validation report
- code generation handoff without approval status
- audit handoff without result and code references
- handoffs that change the requested next state without recording why

## Resume behavior

A resumed run must reconstruct the last valid handoff envelope before continuing.
If the last valid handoff cannot be reconstructed, the system should stop and request human review rather than guessing the missing state.

## v1 recommendation

Prefer slightly verbose handoff objects over clever implicit context.
In this system, explicit provenance is a feature, not bureaucracy.
