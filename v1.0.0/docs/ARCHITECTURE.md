# Architecture - v1.0.0

## Design stance

The first version should behave more like a disciplined research analysis team than a fully autonomous laboratory.

## Minimal agent set

### 1. Orchestrator Agent
Responsibilities:
- receive the user request
- keep the task aligned with the main research objective
- coordinate downstream agents
- stop uncontrolled scope expansion
- separate primary analysis from exploratory suggestions

Outputs:
- task state
- routing decisions
- final assembled response package

### 2. Clinical Framing Agent
Responsibilities:
- convert the clinical question into a research question
- define exposure, outcome, cohort, time window, and key covariates
- identify ambiguities that require clarification

Outputs:
- structured question specification
- inclusion and exclusion assumptions
- variable requirement list

### 3. Methodology Agent
Responsibilities:
- propose the statistical strategy
- define primary and secondary analyses
- define subgroup and sensitivity analyses when justified
- explain why the method matches the study design

Outputs:
- analysis plan
- method rationale
- model checklist

### 4. Analysis Agent
Responsibilities:
- generate reproducible code
- run the analysis pipeline
- produce tables, figures, and logs
- preserve execution traceability

Outputs:
- scripts
- execution logs
- result artifacts
- machine-readable result summary

### 5. Reviewer Agent
Responsibilities:
- challenge variable definitions, model fit, and interpretation
- identify overclaiming and obvious bias risks
- decide whether the result package is safe to present

Outputs:
- review notes
- risk flags
- revision requests or release approval

## Optional exploratory branch

The system may emit an exploration note section with:
- adjacent hypotheses
- useful subgroup ideas
- follow-up analyses worth considering later

This branch is summary-only unless the user explicitly requests promotion into the main workflow.
