# Phase 3 Report - Skill Reuse and Security Review

## Phase goal

Phase 3 had three objectives:
1. inventory MedgeClaw skills that may be relevant to v1
2. decide which can be reused directly, which require narrowing, and which should be excluded
3. create only the truly necessary project-native wrapper skills

## Completed outputs

### Review and decision documents
- `docs/SKILL_SECURITY_REVIEW_V1.md`
- `docs/SKILL_WRAPPER_PLAN_V1.md`

### Project-native wrapper skill layer
- `skills/README.md`
- `skills/critical-care-review-helper/SKILL.md`
- `skills/critical-care-paper-repro-helper/SKILL.md`
- `skills/critical-care-writing-helper/SKILL.md`
- `skills/critical-care-doc-convert/SKILL.md`
- `skills/critical-care-local-dashboard/SKILL.md`

## Main conclusions

### Direct reuse is intentionally minimal

Only a small number of upstream skills are suitable for direct reuse in v1:
- `cjk-viz`
- `scientific-critical-thinking`
- optional `svg-ui-templates`

This is intentional.
The project benefits more from a small safe capability surface than from a large imported skill catalog.

### Wrapper-based reuse is the default safe pattern

Several upstream skills have useful logic but too much scope, network dependence, or execution authority to import directly.
Those are now treated as wrapper sources rather than live dependencies.

The selected wrapper targets are:
- `critical-care-review-helper`
- `critical-care-paper-repro-helper`
- `critical-care-writing-helper`
- `critical-care-doc-convert`
- `critical-care-local-dashboard`

### Broad networked and publishing-heavy skills are excluded

The phase-3 review explicitly excludes broad web-research, image-generation, publishing, and clinical-advice-adjacent skills from the v1 mainline.

That exclusion is not a rejection of their value in general.
It is a deliberate scope and security decision for this product version.

## Security and governance stance

Each selected wrapper was defined under these constraints:
- local-first where possible
- no silent network access
- no protected-database mutation
- no bypass of SAP approval
- no bypass of validation or audit requirements
- no publication-ready or clinical-advice-style output by default

This means phase 3 does not merely classify skills by usefulness.
It classifies them by usefulness, safety, and admissible integration style.

## Why these wrappers were created

### `critical-care-review-helper`

Created because the project needs a bounded quality/review layer and the upstream critique skill is conceptually useful and low-risk when kept local.

### `critical-care-paper-repro-helper`

Created because v1 needs disciplined variable validation and stepwise sample-attrition logic, but not a full paper-reproduction engine.

### `critical-care-writing-helper`

Created because v1 needs internal methods/summary/limitations drafting, but must avoid drifting into autonomous manuscript production.

### `critical-care-doc-convert`

Created because local document ingestion is useful, but the upstream converter's broader media and network features would add unnecessary risk.

### `critical-care-local-dashboard`

Created because a local preview layer can help usability, but it must remain optional and subordinate to formal artifacts.

## What phase 3 deliberately did not do

Phase 3 did not:
- implement full runtime behavior for the wrapper skills
- enable external API integrations for literature or citation search
- create prompt libraries or orchestration glue for each wrapper
- import broad upstream skills wholesale

Those would belong to later implementation work and should stay subordinate to the approved backbone.

## Phase-3 completion judgment

Phase 3 is complete as a design-and-governance phase.
It now has:
- a security-aware skill reuse review
- an explicit wrapper selection rule
- project-native wrapper skill skeletons for the selected targets
- a documented exclusion set for unsafe or scope-breaking skills

## Recommended next step after approval

After review approval, the next implementation phase should treat these wrapper skills as specification-level assets.
The next work should be:
1. connect the selected wrappers to agents and workflow stages
2. define minimal object contracts and audit behavior for wrapper invocation
3. add a first golden example that exercises only the approved wrapper surface

## Overall status after phase 3

The project now has:
- frozen scope and governance backbone
- schemas and workflow skeleton
- traceability and audit specifications
- memory-layer strategy
- skill reuse and security decision layer

This is a strong enough base to move into controlled implementation without importing unsafe breadth from the upstream ecosystem.
