# Analysis Dataset Specification

This document defines what an analysis-ready dataset must look like for the v1.0.0 research system.

It does not replace the upstream database engineering framework in `D:\Database\FRAMEWORK_v4_COMPLETE.md`.
Instead, it defines the downstream contract for the datasets that may enter the research-agent workflow.

## Purpose

The purpose of the analysis dataset specification is to ensure that:
- every study task uses a stable and auditable dataset contract
- agents do not analyze raw data directly
- variable meaning, timing, and derivation are explicit
- outputs can be reproduced from the same extraction definition

## Relationship to the upstream framework

The upstream framework standardizes data into layered resources such as:
- `raw/`
- `split_cleaned/`
- `formatted/`
- `standardized/`
- `index/`
- `studies/{study_id}/`

For v1.0.0, the preferred path is:
- use `standardized/` and `index/` to locate and validate variables
- materialize study-specific extracted datasets under `studies/{study_id}/extracted_data/`
- analyze only the materialized analysis dataset plus its codebook and quality report

## Definition of an analysis-ready dataset

An analysis-ready dataset is a study-specific table that has already resolved:
- unit harmonization
- variable naming
- cohort inclusion
- endpoint construction
- time-window aggregation
- derivation rules
- missingness representation
- dataset versioning

It should be possible to hand the dataset to a statistician or analysis agent without re-deciding what the variables mean.

## Minimum required companion artifacts

Each analysis dataset must be accompanied by:
- `analysis_dataset.csv` or equivalent tabular file
- `codebook.md`
- `quality_report.md` or machine-readable equivalent
- extraction parameters or manifest
- dataset version identifier
- study identifier
- trace links to the source standardization/index layer

## Core dataset grain

Every analysis dataset must explicitly declare its unit of analysis.

Allowed units:
- patient-level
- hospital-admission-level
- ICU-stay-level

For v1.0.0, ICU-stay-level should be the default unless the study plan justifies another choice.

## Mandatory metadata fields

Each dataset must define these metadata fields, either as columns or in a companion manifest:
- `study_id`
- `dataset_id`
- `dataset_version`
- `unit_of_analysis`
- `time_zero_definition`
- `source_database_id`
- `source_data_version`
- `extraction_timestamp`
- `cohort_definition_version`
- `analysis_plan_version` if already frozen

## Mandatory identifier fields

At least the relevant identifiers must exist:
- `patient_id`
- `hospital_admission_id` when applicable
- `icu_stay_id` when applicable

De-identified IDs are preferred for exported analysis datasets.

## Mandatory temporal fields

At minimum, the dataset must preserve:
- `t0_time`
- `time_zero_type`

Optional but strongly recommended:
- `followup_end_time`
- `outcome_time`
- key exposure timestamps

If the dataset is already aggregated to one row per analysis unit, the detailed measurement timestamps may live in upstream layers, but the aggregation window must still be documented.

## Variable classes in the analysis dataset

Each included analysis variable should belong to one of these classes:
- identifier
- cohort flag
- exposure
- comparator
- primary outcome
- secondary outcome
- baseline covariate
- stratification variable
- sensitivity-analysis variable
- quality or missingness indicator
- derived variable

## Required variable-level metadata

Every analysis variable must have metadata covering:
- variable name
- clinical meaning
- variable class
- source location
- source variable or source rule
- unit
- coding system if categorical
- allowed values or range
- derivation method
- time window used
- aggregation method
- missingness meaning

## Recommended one-row-per-unit structure

For most v1.0.0 studies, the preferred form is one row per analysis unit with study-specific derived columns.

Example columns:
- `patient_id`
- `icu_stay_id`
- `age`
- `sex`
- `sepsis_flag`
- `sofa_max_24h`
- `lactate_max_24h`
- `platelet_min_24h`
- `vasopressor_6h_flag`
- `mechanical_ventilation_24h_flag`
- `mortality_28d`
- `icu_mortality`
- `followup_days`

## Variable derivation rules

No derived variable should appear without a documented rule.

Examples:
- `sofa_max_24h` = maximum SOFA score from 0 to 1440 minutes
- `lactate_max_24h` = maximum lactate value from 0 to 1440 minutes
- `age` = age at time zero
- `mortality_28d` = death within 28 days after T0

## Missingness rules

Missingness must never be implicit.

The dataset or codebook must define:
- whether missing means not measured, not recorded, not applicable, or failed extraction
- whether missing indicators are added as explicit columns
- whether imputation occurs before or after dataset materialization

For v1.0.0, default preference is:
- materialize raw missingness explicitly
- do not silently impute inside dataset extraction
- let imputation policy be controlled by the SAP

## Quality requirements before release to analysis agents

Before an analysis dataset is considered eligible for downstream analysis, it must pass at least:
- identifier integrity check
- duplicate row check at the declared unit of analysis
- range and validity checks for key variables
- endpoint completeness check
- time-window consistency check
- extraction log completeness check

## Required companion codebook structure

The codebook should include, for each variable:
- name
- label
- type
- unit
- class
- source
- derivation
- time window
- aggregation
- missing rate
- notes

## Example extraction bundle

```text
studies/example_study_001/
  study_plan.json
  extracted_data/
    analysis_dataset.csv
    codebook.md
    quality_report.md
    extraction_manifest.json
```

## Example manifest fields

```json
{
  "study_id": "example_study_001",
  "dataset_id": "example_study_001_adataset",
  "dataset_version": "1.0.0",
  "unit_of_analysis": "icu_stay",
  "time_zero_definition": "T0_ICU_ADMISSION",
  "source_database_id": "sepsis_icu_001",
  "source_data_version": "1.0",
  "cohort_definition_version": "1.0.0",
  "generated_at": "2026-03-16T22:00:00+09:00"
}
```

## Agent usage policy

### May read directly
- Data Mapping Agent
- Analysis Planning Agent
- Code Generation Agent
- Execution Validator Agent

### Should read only validated derived outputs
- Interpretation Agent
- Audit / Trace Agent

### Should not analyze raw layers directly
- Interpretation Agent
- final report generation logic

## v1.0.0 recommendation

In early implementation, keep the analysis dataset contract simple:
- one row per ICU stay
- fixed time zero
- explicit endpoint columns
- explicit derived covariates
- companion codebook and extraction manifest every time

That is enough to support a stable first-generation research workflow.
