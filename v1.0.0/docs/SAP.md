# Statistical Analysis Plan (SAP) - v1.0.0

This document defines the minimum statistical analysis discipline for the v1.0.0 research system.

The purpose of the SAP is not to maximize methodological sophistication.
The purpose is to make the workflow stable, auditable, and resistant to uncontrolled analysis drift.

## Core rule

No formal analysis code should be generated for a study until a study-specific SAP has been created and approved at the required level.

## Purpose

The SAP exists to prevent:
- post-hoc model switching
- hidden p-hacking
- uncontrolled subgroup explosion
- silent changes to outcome definitions
- unclear missing-data handling
- interpretation that outruns the analysis actually performed

## Scope of v1.0.0 SAP

The v1.0.0 SAP should support a focused set of study types:
- descriptive studies
- association studies
- prediction tasks
- time-to-event studies
- longitudinal repeated-measure analyses in limited form
- subgroup and sensitivity analyses when predeclared

## Mandatory SAP sections

Every study-specific SAP must include:
- study identifier
- linked research question identifier
- question class
- study objective
- unit of analysis
- time zero definition
- cohort definition reference
- primary endpoint
- secondary endpoints if any
- exposure definition or predictor set
- covariate strategy
- primary analysis method
- secondary analysis methods if any
- subgroup analysis plan
- sensitivity analysis plan
- missing-data strategy
- model diagnostics plan
- multiplicity handling statement
- output table and figure plan
- interpretation boundary statement

## Recommended default method families for v1.0.0

### Descriptive studies
- counts and proportions
- mean and standard deviation when appropriate
- median and IQR when skewed
- standardized mean difference for group balance summaries when relevant

### Association studies
- logistic regression
- linear regression
- Cox proportional hazards model when time-to-event is justified
- Poisson or negative binomial only when explicitly justified

### Prediction tasks
- start narrow
- only include prediction workflows if:
  - train/validation strategy is explicit
  - metrics are predeclared
  - interpretation does not drift into causal language

### Time-to-event studies
- Kaplan-Meier curves
- log-rank comparison when appropriate
- Cox model if assumptions and censoring plan are explicit

### Longitudinal repeated-measure analyses
- limited and explicit only
- use mixed models or repeated-measure summaries only when data structure is clearly defined
- do not allow free-form longitudinal modeling in early v1 use

## Endpoint discipline

Each endpoint must be declared before analysis with:
- endpoint name
- endpoint type
- construction rule
- observation window
- competing-event note if applicable

The primary endpoint must be singular unless a study explicitly justifies co-primary endpoints.

For v1.0.0, a single primary endpoint is strongly preferred.

## Exposure and predictor discipline

The SAP must explicitly state:
- exposure definition
- exposure assessment window
- comparator definition when relevant
- whether variables are baseline-only or include post-baseline information

Post-baseline covariates should not enter primary adjustment casually.
If used, the SAP must justify the choice and its causal implications.

## Covariate strategy

The SAP must describe:
- mandatory adjustment variables
- clinically essential confounders
- prohibited variables
- handling of collinearity or redundancy
- whether any data-driven selection is allowed

### Default v1.0.0 recommendation
- use a clinically justified fixed covariate set where possible
- avoid unconstrained stepwise variable fishing
- treat mediators and post-outcome variables as prohibited in standard adjustment sets

## Missing-data strategy

The SAP must declare one of the following for each important variable class:
- complete-case analysis
- missing-indicator strategy
- multiple imputation
- variable-specific exclusion from model

If missingness handling differs between primary and sensitivity analyses, both must be stated explicitly.

### Default v1.0.0 recommendation
- do not hide missingness inside extraction
- define missingness strategy in SAP, not ad hoc in code generation

## Subgroup analysis policy

Subgroup analyses are allowed only when:
- predeclared in SAP
- clinically or methodologically justified
- clearly labeled as subgroup analyses

The SAP must define:
- subgroup variable
- subgroup categories
- whether interaction testing is planned
- interpretation limitations

### Default v1.0.0 recommendation
- keep subgroup analyses few
- avoid automatic subgroup proliferation

## Sensitivity analysis policy

The SAP should define the minimum sensitivity checks needed for credibility.

Examples:
- alternative exposure definition
- alternative endpoint definition
- alternative missing-data handling
- alternative covariate adjustment set
- restricted cohort analysis

Sensitivity analyses must be clearly separated from the primary analysis.

## Multiplicity statement

The SAP must state how multiplicity is treated.

At minimum it should declare one of:
- no formal adjustment, results interpreted cautiously
- formal adjustment applied to a defined family of tests
- exploratory results clearly marked as exploratory

For v1.0.0, explicit caution labeling is often more realistic than overcomplicated adjustment schemes.

## Model diagnostics

Each primary model family must include minimal diagnostic checks.

### Logistic regression
- convergence check
- sparse-cell warning check
- coefficient stability review
- separation risk note

### Cox model
- convergence check
- event-count sufficiency review
- proportional-hazards check or explicit limitation note

### Linear regression
- residual distribution review
- influential point review when relevant
- collinearity check

### Prediction models
- train/validation split or resampling strategy
- discrimination metric
- calibration metric when possible
- leakage review

## Table and figure plan

Before execution, the SAP should name the planned outputs.

Minimum examples:
- Table 1: baseline characteristics
- main model results table
- subgroup table if predeclared
- sensitivity analysis table
- one or two core figures such as KM curve or forest plot

## Interpretation boundary statement

Every SAP must include a statement that defines what claims are allowed.

Examples:
- observational association only
- prediction performance only
- no causal language unless specifically justified and approved
- exploratory outputs must not be framed as confirmatory findings

## Human approval gates

Manual approval is strongly recommended before execution when:
- the cohort definition is complex
- time zero is not ICU admission
- missing-data handling materially affects interpretation
- a prediction task is proposed
- any causal language is contemplated
- subgroup or sensitivity branches multiply beyond the default template

## Study-specific SAP template

```yaml
study_id: example_study_001
research_question_id: rq_example_001
question_class: association
study_objective: evaluate the association between early vasopressor exposure and 28-day mortality

unit_of_analysis: icu_stay
time_zero: T0_ICU_ADMISSION
cohort_definition_version: 1.0.0

primary_endpoint:
  name: mortality_28d
  type: binary
  window: 0_to_40320_minutes

secondary_endpoints:
  - icu_mortality
  - hospital_mortality

exposure:
  name: early_vasopressor_exposure
  window: 0_to_360_minutes

covariates:
  mandatory:
    - age
    - sex
    - sofa_score_max_24h
    - lactate_max_24h
  prohibited:
    - post_outcome_variables

primary_analysis:
  method: logistic_regression
  estimand_scale: odds_ratio

secondary_analyses:
  - method: cox_model
    condition: only_if_time_to_event_data_are_complete

subgroup_analyses:
  - variable: septic_shock_flag
    interaction_test: true

sensitivity_analyses:
  - alternative_exposure_window: 0_to_1440_minutes
  - complete_case_only

missing_data:
  primary_strategy: complete_case
  sensitivity_strategy: missing_indicator

model_diagnostics:
  - convergence_check
  - sparse_cell_review
  - collinearity_review

multiplicity:
  policy: exploratory_results_labeled_explicitly

outputs:
  tables:
    - table1_baseline
    - main_model_table
    - sensitivity_table
  figures:
    - forest_plot

interpretation_boundary:
  allowed: association_language_only
  forbidden: causal_claims
```

## v1.0.0 recommendation

Prefer simple, transparent SAPs over ambitious, unstable ones.

A smaller method set with strong traceability is better than a broad method catalog with weak discipline.
