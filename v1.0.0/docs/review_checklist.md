# Review Checklist - v1.0.0

Use this checklist before approving the backbone or any later run package.

## A. Scope and product boundary

- Is the task still clearly within critical care / ICU / emergency medicine database research?
- Does the workflow preserve the user's main research question rather than drifting into side ideas?
- Are any side ideas clearly labeled and kept subordinate?
- Does any writing-related branch stay within internal research support rather than silent manuscript autopilot?

## B. Workflow discipline

- Does the workflow require design before mapping, mapping before planning when applicable, and planning before code generation?
- Is there an explicit approval gate before code generation?
- Is validation required before interpretation?
- Is audit/trace completeness required before delivery?
- Are revision loops bounded rather than open-ended?

## C. Policy and approval coherence

- Do `docs/policy_engine_rules.yaml` and `docs/approval_matrix.md` express the same basic restrictions?
- Are protected data-foundation mutations blocked or approval-gated everywhere?
- Are non-default time-zero choices and major method switches approval-gated?
- Is causal language treated as restricted?

## D. Handoff and schema alignment

- Do handoff contracts reference the actual schema objects in `schemas/`?
- Can each major agent receive enough structured context without relying on hidden chat state?
- Is interpretation downstream of validation in both docs and machine flow?
- Is the trace bundle downstream of interpretation and upstream of release?

## E. Traceability and audit

- Does the minimum trace chain connect question, plan, code, run, result, validation, interpretation, and trace bundle?
- Does the artifact layout provide a clear place for formal objects, audit logs, and execution logs?
- Does `run_manifest.json` carry current state, object index, approval context, validation context, and audit paths?
- Are audit streams append-only and explicit enough for later review?

## F. Machine skeleton sanity

- Does `scripts/run_backend.py` load `default_pipeline.json` successfully?
- Can it initialize a task manifest and create the expected folder skeleton?
- Can it reject illegal state transitions?
- Do the allowed next states match the documented state machine?

## G. Release readiness

- Is a release impossible when validation fails?
- Is a release impossible when the trace bundle is incomplete?
- Are final outputs framed as internal review artifacts unless explicitly approved otherwise?
- Is there any place where the system could accidentally emit clinical-advice-style output?

## H. Issues to flag immediately

Flag for revision if you see any of the following:
- state names disagree across files
- a branch template exceeds product scope
- policy rules contradict approval rules
- a required trace artifact has no defined storage location
- a required release artifact is not listed in the pipeline or manifest

## Reviewer outcome

At the end of review, assign:
- `accept`
- `accept_with_minor_revisions`
- `major_revisions_required`
- `reject_for_v1`
