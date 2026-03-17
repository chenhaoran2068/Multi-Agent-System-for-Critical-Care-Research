---
name: critical-care-paper-repro-helper
description: Narrow reproducibility helper for critical care observational studies. Use when the system needs disciplined variable validation, stepwise sample attrition tracking, deviation logging, or structured result comparison under an approved study question and SAP. Use for Data Mapping Agent, Analysis Planning Agent, and Code Generation Agent tasks that must stay local and approval-aware.
---

# Critical Care Paper Repro Helper

Use this skill to import the discipline of staged paper reproduction without importing a full reproduction engine.

## Do this

1. Validate variables before modeling.
2. Track sample inclusion and exclusion step by step.
3. Record where observed counts or outputs differ from expectations.
4. Keep deviation notes explicit instead of silently smoothing mismatches away.
5. Prefer phased execution over monolithic analysis runs.

## Use it for

- variable validation checklists
- sample attrition logs
- cohort filtering sanity checks
- result comparison notes
- reproducibility comments for audit packages

## Expected outputs

Produce one or more of:
- variable validation checklist
- sample attrition log
- deviation note
- reproducibility note for trace or audit

## Forbidden behavior

- Do not trigger a full paper-reproduction workflow automatically.
- Do not rewrite the approved study question to match a paper template.
- Do not treat partial or uncertain mappings as fully valid without labeling uncertainty.
- Do not introduce new upstream variables without approval.
- Do not bypass `SAP.md` or the approval matrix.

## Approval rule

- Normal use: `allow-with-log`
- Any change to cohort logic, endpoint definition, or variable foundation: `require-human-approval`

## Agent alignment

Primary agents:
- Data Mapping Agent
- Analysis Planning Agent
- Code Generation Agent
