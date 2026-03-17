# Data Foundation Relation

This document defines the relationship between the database standardization framework and the v1.0.0 multi-agent research system.

## Positioning

The file `D:\Database\FRAMEWORK_v4_COMPLETE.md` is treated as the upstream data engineering and database standardization framework.

The folder `v1.0.0/` defines the downstream research analysis execution layer.

They are not competing designs.
They are upstream and downstream parts of the same future system.

## Division of responsibility

### Upstream: database foundation framework
The upstream framework defines how raw ICU clinical databases should be transformed into a standardized, indexed, quality-controlled, and AI-readable data foundation.

Its responsibilities include:
- layered storage design
- raw data protection
- splitting and cleaning rules
- wide/long transformation
- variable and unit standardization
- machine-readable and human-readable indexing
- quality validation rules
- database versioning and incremental update logic
- study-plan-driven extraction capability at the database engineering level

### Downstream: v1.0.0 research system
The v1.0.0 system defines how a focused critical care research assistant consumes the standardized data foundation to perform structured research tasks.

Its responsibilities include:
- turning user questions into structured research questions
- defining cohorts and time windows for a study task
- selecting analysis plans
- generating analysis code
- validating execution and outputs
- producing constrained interpretations
- preserving a traceable audit chain across the research workflow

## Shared assumptions inherited from the upstream framework

The v1.0.0 system should inherit these default assumptions unless explicitly overridden:
- ICU admission time is the default time zero (`T0`)
- relative time should use `time_relative_minutes`
- raw data are read-only
- processed data should follow a layered architecture
- variable definitions should come from a maintained dictionary and standardization layer
- quality reports and processing logs are first-class artifacts
- index documents should be both human-readable and machine-readable when possible

## Layer usage policy for v1.0.0

The upstream framework contains six layers. The v1.0.0 system should not treat all layers equally. The detailed read/write boundary is defined in `DATABASE_ACCESS_POLICY.md`.

### Preferred layers for v1.0.0 agents
- `standardized/`
- `index/`
- `studies/{study_id}/extracted_data/`

### Restricted layers
- `raw/` should not be used directly by analysis or interpretation agents
- `split_cleaned/` and `formatted/` may be used by data-mapping or extraction logic when necessary, but should not be the default user-facing analysis layer

## Data handoff philosophy

The upstream framework answers:
- what the database has been transformed into
- how variables were standardized
- what quality checks were applied
- where a variable can be found

The v1.0.0 system answers:
- what study-specific cohort should be built
- what time windows should be used
- what analysis-ready dataset should be materialized
- what methods should be applied
- what conclusions are justified

## What v1.0.0 should not duplicate

The v1.0.0 docs should not re-implement the full database engineering framework.

They should not duplicate in full:
- raw file handling rules
- wide/long conversion mechanics
- full database directory engineering
- full incremental update strategy
- all standardization layer internals

Instead, v1.0.0 should reference the upstream framework and only define the parts needed for the research analysis workflow.

## What v1.0.0 must define on top

The v1.0.0 layer must still define:
- study-facing cohort and time-window templates
- analysis dataset contracts
- SAP constraints
- agent contracts
- schema objects for traceable research tasks
- workflow guardrails
- result interpretation restrictions

## Practical contract

In implementation terms:
- `FRAMEWORK_v4_COMPLETE.md` is the data factory specification
- `v1.0.0/docs/cohort_time_window_template.md` is the study-level time and cohort contract
- `v1.0.0/docs/adataset_spec.md` is the analysis-ready dataset contract

## Bottom line

The upstream database framework gives this project a strong foundation.

The correct move is not to rebuild that foundation inside v1.0.0.
The correct move is to explicitly plug the research-agent system into it.
