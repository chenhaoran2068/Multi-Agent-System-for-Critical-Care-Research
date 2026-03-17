# Cohort and Time Window Template

This document defines the study-level cohort and time-window contract for v1.0.0.

It is intentionally aligned with the upstream database framework in `D:\Database\FRAMEWORK_v4_COMPLETE.md`.

## Core default

Unless a study explicitly requires otherwise:
- default time zero is ICU admission time (`T0`)
- relative time is represented as `time_relative_minutes`
- study windows must be explicitly declared
- exposure, outcome, and covariates must be anchored to declared windows

## Purpose

This template prevents drift in:
- cohort entry definition
- repeated admission handling
- exposure timing
- outcome timing
- censoring
- baseline window logic

## Minimum study-level fields

Each study task must define:
- study identifier
- study question type
- target population
- cohort entry rule
- cohort exit rule
- time zero definition
- baseline window
- exposure assessment window
- outcome observation window
- censoring rule
- repeated admission handling rule
- ICU readmission handling rule
- primary endpoint definition
- secondary endpoint definitions if any

## Default time reference options

### Default option
- `T0_ICU_ADMISSION`
  - recommended default for most v1 studies
  - intended for ICU-centered observational studies

### Allowed exceptions
- `T0_HOSPITAL_ADMISSION`
  - for studies requiring pre-ICU continuity
- `T0_EXPOSURE_START`
  - for exposure-anchored designs when justified
- `T0_SEPSIS_ONSET`
  - for sepsis progression research when robustly defined

Any non-default time zero must be justified in the study plan.

## Core windows

### 1. Baseline window
Defines where baseline covariates may be collected.

Recommended default:
- `start_minutes = -60`
- `end_minutes = 60`

### 2. Exposure assessment window
Defines when exposure status is determined.

Examples:
- vasopressor exposure within first 6 hours: `0 to 360`
- mechanical ventilation in first 24 hours: `0 to 1440`

### 3. Outcome observation window
Defines when the endpoint is assessed.

Examples:
- ICU mortality: ICU stay
- hospital mortality: hospitalization episode
- 28-day mortality: `0 to 40320`

### 4. Follow-up end
Defines the latest valid observation point.

Can be:
- ICU discharge
- hospital discharge
- fixed day endpoint
- death
- administrative censoring

## Aggregation rules for repeated measurements

The study must explicitly choose one of the following when repeated measurements exist:
- `first`
- `last`
- `min`
- `max`
- `mean`
- `median`
- `slope`
- `any`
- `all`

If no aggregation is declared, the variable is not analysis-ready.

## Cohort entry template

Required elements:
- source population
- inclusion criteria
- exclusion criteria
- index event
- patient unit of analysis

### Unit of analysis must be one of:
- patient-level
- hospital-admission-level
- ICU-stay-level

For v1.0.0, ICU-stay-level should be the default unless a study explicitly requires a different unit.

## Repeated admission policy

The study must state one of the following:
- first eligible ICU stay only
- first hospital admission only
- all eligible ICU stays with clustering strategy declared
- all eligible admissions with patient-level correlation handling declared

For v1.0.0, the safest default is:
- first eligible ICU stay only

## ICU readmission policy

The study must explicitly state whether ICU readmission is:
- excluded
- merged into one hospitalization episode
- handled as a separate eligible event

If omitted, default to:
- exclude later ICU readmissions and keep the first eligible ICU stay only

## Censoring template

The study must define:
- censoring events
- administrative censoring date or rule
- transfer handling
- lost-to-follow-up handling if applicable

## Endpoint definition template

Each endpoint must include:
- endpoint name
- endpoint type
  - binary
  - time-to-event
  - continuous
  - count
- source variable or construction rule
- observation window
- competing event rule if relevant

## Bias-prevention checks

Every cohort/time definition should be checked for:
- immortal time bias risk
- post-baseline covariate leakage
- exposure-outcome overlap
- unclear index event definition
- mixed-level analysis units
- inconsistent repeated admission handling

## Template skeleton

```yaml
study_id: example_study_001
question_type: association
unit_of_analysis: icu_stay

time_zero:
  id: T0_ICU_ADMISSION
  justification: default critical care reference point

cohort_entry:
  source_population: adult ICU admissions
  inclusion_criteria:
    - age >= 18
    - suspected or confirmed sepsis
  exclusion_criteria:
    - ICU length of stay < 24h
  index_event: first eligible ICU admission

repeated_admission_policy:
  rule: first_eligible_icu_stay_only

icu_readmission_policy:
  rule: exclude_later_readmissions

baseline_window:
  start_minutes: -60
  end_minutes: 60

exposure_window:
  start_minutes: 0
  end_minutes: 360
  definition: vasopressor exposure in first 6 hours

outcome_window:
  start_minutes: 0
  end_minutes: 40320
  definition: death within 28 days after ICU admission

censoring:
  administrative_end: 28_days
  discharge_handling: follow until day 28 if death data are available

primary_endpoint:
  name: mortality_28d
  type: binary
  source: derived from death date and T0

secondary_endpoints:
  - name: icu_mortality
    type: binary
    source: ICU episode outcome
```

## v1.0.0 recommendation

For early implementation, prefer studies with:
- a single declared time zero
- a single primary endpoint
- fixed baseline and follow-up windows
- first eligible ICU stay only
- no time-varying causal complexity unless explicitly planned
