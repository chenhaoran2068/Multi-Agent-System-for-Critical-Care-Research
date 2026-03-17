---
name: critical-care-writing-helper
description: Bounded internal-writing helper for critical care database research. Use when the system needs methods appendix drafts, internal summaries, or limitations notes based on approved plans and validated outputs only. Use for Analysis Planning Agent, Interpretation Agent, and Audit / Trace Agent tasks that must avoid autonomous manuscript production and publication-style claim inflation.
---

# Critical Care Writing Helper

Use this skill to package approved work into conservative internal writing outputs.

## Do this

1. Start only from approved plans and validated outputs.
2. Write in full paragraphs, not bullet fragments, when drafting internal narrative sections.
3. Keep language conservative and evidence-linked.
4. Distinguish clearly between findings, interpretation, and limitations.
5. Treat writing as packaging of completed work, not as an excuse to expand scope.

## Use it for

- methods appendix draft
- internal result summary
- limitations note
- interpretation-boundary check

## Expected outputs

Produce one or more of:
- `methods_appendix_draft`
- `internal_summary_draft`
- `limitations_note`
- `claim_boundary_check`

## Forbidden behavior

- Do not generate a full manuscript submission package automatically.
- Do not use stronger causal or clinical language than the approved boundary allows.
- Do not cite unvalidated outputs as findings.
- Do not turn exploratory side ideas into formal conclusions.
- Do not trigger external citation lookup automatically.

## Approval rule

- Internal drafting: `allow-with-log`
- Citation lookup or publication-oriented output: `require-human-approval`

## Agent alignment

Primary agents:
- Analysis Planning Agent
- Interpretation Agent
- Audit / Trace Agent
