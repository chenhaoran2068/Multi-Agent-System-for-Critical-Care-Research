# Success Criteria - v1.0.0

This document defines what it means for the v1 system to be considered functionally successful.

Success in v1 does not mean maximum automation.
Success means the system can reliably complete a narrow research workflow without losing methodological discipline or traceability.

## Primary success criteria

A task run is successful only if all of the following are true:

1. the main research question remains stable through the workflow
2. the workflow does not bypass the SAP discipline
3. execution outputs are validated before interpretation
4. the final interpretation is conservative and evidence-linked
5. the trace bundle is complete enough for internal expert review
6. any approval-required action is either explicitly approved or correctly blocked
7. side ideas remain subordinate unless explicitly promoted by a human

## Product-level success for v1

The v1 project is successful when it can repeatedly do the following:
- accept a bounded critical care research question
- convert it into a structured question object
- map required variables or clearly report missing variables
- generate an SAP-aligned analysis plan
- produce reproducible code and execution records
- generate tables, figures, and a conservative interpretation
- assemble a traceable release package for internal review

## Safety success criteria

The system should be considered safe enough for v1 only if it consistently avoids:
- silent scope drift
- silent protected-layer mutation
- code generation before plan approval
- interpretation before validation
- unsupported causal language
- release with incomplete traceability
- clinical-advice-style output

## Operational success criteria

A successful task should leave behind:
- `run_manifest.json`
- state transition history
- approval log when relevant
- code artifact metadata
- validated result artifacts
- interpretation object
- trace bundle
- audit summary

## Quality success criteria

The output package should be:
- understandable by a human researcher
- internally consistent
- conservative in wording
- replayable enough to inspect what happened
- explicit about uncertainty and limitations

## Non-goals masquerading as success

The following do not count as success by themselves:
- a fluent narrative with weak provenance
- a statistically complex method without clear justification
- lots of side analyses that overshadow the main question
- apparent autonomy that bypasses human approval boundaries
- attractive outputs that cannot be tied back to data and code

## v1 recommendation

Judge success by discipline and repeatability, not by how magical the system looks in a single demo.
