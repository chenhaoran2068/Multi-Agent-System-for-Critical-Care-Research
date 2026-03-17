# MVP Scope - v1.0.0

## Core principle

Keep the vision large, but keep the first build narrow.

## Accepted boundaries

### Domain boundary
Only emergency medicine, ICU, and critical care database research.

### Task boundary
Only structured clinical database analysis.

### Delivery boundary
The system outputs:
- study design and analysis plan
- reproducible analysis code
- result tables and figures
- written interpretation tied to actual outputs

### Safety boundary
Every conclusion must be traceable to:
- source dataset or derived analytic dataset
- variable definitions
- analysis code
- model output
- execution logs

### Interaction boundary
The system is allowed to diverge and propose related ideas.

However, if a proposed direction drifts away from the main research objective:
- it should be summarized clearly in a follow-up section
- it should not be executed into full analysis results by default
- it should remain subordinate to the user's primary task unless the user explicitly promotes it

## Primary success criteria

A successful v1.0.0 run should be able to:
1. receive a clinical research question
2. turn it into a structured analysis specification
3. choose a justified method
4. generate runnable code
5. produce tables, figures, and interpretable results
6. preserve a traceable evidence chain

## Explicit non-goals for v1.0.0

- autonomous end-to-end literature exploration
- self-directed research portfolio expansion with full execution
- pathophysiology deep-dive as a required stage
- automatic manuscript submission-grade writing pipeline
- unrestricted multi-agent autonomy
- multi-omics or device/instrument integration
