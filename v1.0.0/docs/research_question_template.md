# Research Question Template

This document defines how user intent is converted into a structured research question for v1.0.0.

## Purpose

The template exists to prevent vague questions from entering the analysis workflow.

A research task is not ready until the study question is structured clearly enough to determine:
- who is being studied
- what exposure or comparison is being evaluated
- what outcome is being measured
- when the study clock starts
- what follow-up window applies
- what major confounders must be considered

## Supported question classes in v1.0.0

- descriptive
- association
- prediction
- time-to-event
- longitudinal repeated-measure
- subgroup analysis
- sensitivity analysis

## Required fields

Every research question must define:
- study title or short label
- question class
- clinical context
- target population
- exposure or predictor
- comparator if relevant
- primary outcome
- secondary outcomes if relevant
- time zero
- baseline window
- follow-up window
- inclusion criteria
- exclusion criteria
- key confounders or adjustment intent
- primary estimand or main effect target

## Recommended framing standard

Use `PICO/PECO + estimand` whenever possible.

### Population
Who is being studied?

### Exposure / Intervention
What factor, treatment, state, or predictor is under evaluation?

### Comparator
What is the reference group or baseline condition?

### Outcome
What endpoint is being measured?

### Estimand
What exact quantity is the study trying to estimate?

## Clarification rule

If any of the following are unclear, the workflow should stop and ask for clarification before planning analysis:
- exposure definition
- outcome definition
- time zero
- follow-up window
- unit of analysis
- whether the task is exploratory or confirmatory

## Exploratory extension policy

The system may propose adjacent research ideas.

However:
- they must be kept separate from the primary task
- they should be stored as structured suggestions
- they must not replace the user’s main question
- they must not be executed deeply unless explicitly promoted by the user

## Template skeleton

```yaml
study_id: draft_study_001
study_title: Early vasopressor exposure and 28-day mortality in adult septic ICU patients
question_class: association
clinical_context: septic shock / critical care hemodynamic support

population:
  description: adult ICU patients with sepsis
  inclusion_criteria:
    - age >= 18
    - sepsis criteria met
  exclusion_criteria:
    - ICU stay < 24h

exposure:
  name: early_vasopressor_exposure
  definition: any vasopressor use within first 6 hours after ICU admission

comparator:
  name: no_early_vasopressor_exposure

primary_outcome:
  name: mortality_28d
  definition: death within 28 days after ICU admission

secondary_outcomes:
  - icu_mortality
  - hospital_mortality

time_zero: T0_ICU_ADMISSION
baseline_window:
  start_minutes: -60
  end_minutes: 60
followup_window:
  start_minutes: 0
  end_minutes: 40320

key_confounders:
  - age
  - sex
  - sofa_score
  - lactate
  - mechanical_ventilation

estimand:
  target: association between early vasopressor exposure and 28-day mortality
  scale: odds_ratio_or_hazard_ratio_to_be_defined_in_SAP

study_mode: confirmatory
```

## v1.0.0 recommendation

Prefer questions that are:
- anchored to a single clear time zero
- based on a single primary outcome
- grounded in available structured variables
- feasible within one analysis dataset contract
