---
name: critical-care-review-helper
description: Bounded review helper for critical care database research. Use when the system needs to review an approved analysis plan, validated result artifacts, a validation report, or an interpretation draft for bias, overclaiming, evidence weakness, or release-readiness. Use for Execution Validator Agent and Interpretation Agent tasks that must remain local-first and text-only.
---

# Critical Care Review Helper

Use this skill to review whether a study package is scientifically cautious enough to move forward.

## Do this

1. Read the available formal objects first:
   - `analysis_plan`
   - `validation_report`
   - validated `result_artifact`
   - `interpretation`
2. Check whether the interpretation stays inside the approved plan and validated outputs.
3. Flag overclaiming, causal overreach, unacknowledged uncertainty, weak subgroup logic, and missing limitation statements.
4. Return reviewer notes as structured findings, not vague impressions.
5. If the evidence chain is incomplete, recommend `revise` or `block`, not soft approval.

## Focus areas

- bias and confounding concerns
- mismatch between plan and reported result
- unsupported causal language
- missing limitations
- weak evidence strength
- release-readiness of the current package

## Expected outputs

Produce one or more of:
- reviewer notes
- risk flags
- interpretation-boundary comments
- release recommendation: `pass`, `revise`, or `block`

## Forbidden behavior

- Do not rewrite the main research question.
- Do not reinterpret raw data outside validated artifacts.
- Do not introduce external literature claims as if they were validated project findings.
- Do not suggest treatment decisions or clinical advice.
- Do not bypass validation to approve interpretation.

## Approval rule

- Normal use: `allow-with-log`
- If stronger claim language or major reinterpretation is requested: escalate to `require-human-approval`

## Agent alignment

Primary agents:
- Execution Validator Agent
- Interpretation Agent
