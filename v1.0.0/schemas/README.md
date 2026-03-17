# Schemas - v1.0.0

This directory stores the first structured object contracts for the v1.0.0 workflow.

## Design goals

These schemas are intended to:
- connect agents through structured handoff objects
- make workflow state auditable
- separate facts from proposals and interpretation
- enforce trace links between question, data, plan, code, results, and claims

## Included schema files

- `research_question.schema.json`
- `variable_mapping.schema.json`
- `analysis_plan.schema.json`
- `code_artifact.schema.json`
- `result_artifact.schema.json`
- `interpretation.schema.json`
- `trace_bundle.schema.json`
- `idea_summary.schema.json`
- `pydantic_models.py`

## Notes

- These are v1.0.0 skeletons, not final production schemas
- IDs and versions are required throughout
- Interpretation objects must cite result artifact IDs
- Trace bundles should be able to connect every formal conclusion back to plan, code, run, and data version
