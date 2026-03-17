# Project Skills - v1.0.0

This directory stores project-native wrapper skills for the critical care research system.

These are not broad imports of upstream MedgeClaw skills.
They are narrow, security-aware wrappers created only where v1 genuinely benefits from reuse.

## Design rule

Every skill in this directory must answer three questions clearly:
- Can it be used in v1?
- Is it safe enough for v1?
- If used, how must it be constrained to avoid network, execution, and governance risk?

## Current phase-3 stance

The project does not import upstream skills wholesale.
It only creates wrappers around the parts that are both useful and governable.

Current wrapper targets:
- `critical-care-review-helper`
- `critical-care-paper-repro-helper`
- `critical-care-writing-helper`
- `critical-care-doc-convert`
- `critical-care-local-dashboard`

## Relationship to upstream skills

Each wrapper should document:
- the upstream skill(s) it borrows from
- what is retained
- what is explicitly disabled
- what approval level applies

See `docs/SKILL_SECURITY_REVIEW_V1.md` for the security review and `docs/SKILL_WRAPPER_PLAN_V1.md` for wrapper selection and rationale.
