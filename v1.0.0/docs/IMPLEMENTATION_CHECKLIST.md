# Implementation Checklist - v1.0.0

This document is the execution baseline for the first build of the project.

The strategic long-term vision remains under `../Guideline/` and is intentionally preserved. This checklist only defines what must be completed to deliver a reliable, traceable, and focused first version.

## Guiding principle

Build a narrow and trustworthy system first.

Version `1.0.0` is not a full autonomous research laboratory. It is a focused critical care database research assistant that can turn a user question into a structured study plan, reproducible analysis, validated results, and constrained interpretation.

## Current build status

### Completed as backbone draft
- core product-boundary documents
- data-foundation relation and access policy documents
- SAP, agent contracts, approval matrix, and workflow overview
- machine-readable workflow backbone: `default_pipeline.json`
- implementation-facing state semantics: `workflow_state_machine.md`
- policy skeleton: `policy_engine_rules.yaml`
- structured handoff definition: `handoff_contracts.md`
- schemas and `schemas/pydantic_models.py`
- traceability, audit, artifact layout, success, acceptance, and review documents
- `run_manifest.json` template
- minimal `scripts/run_backend.py` skeleton for task init and state transition validation

### Completed for memory continuity
- project memory strategy in `docs/MEMORY_STRATEGY.md`
- project-level memory files under `memory/`
- assistant-level memory updated with retrieval priority rules

### Still pending before deeper implementation
- real policy evaluation in runtime
- handoff object emission and storage during runs
- audit stream append logic beyond manifest state history
- golden example / end-to-end walkthrough
- phase 3 skill reuse review and narrowing
- real execution integration and regression tests

## Phase 0 - Freeze product boundaries

### Must define
- domain boundary: emergency medicine, ICU, and critical care database research only
- data boundary: structured clinical databases only
- output boundary: study plan, analysis code, result tables/figures, and written interpretation only
- safety boundary: every conclusion must be traceable to data version, code version, parameters, logs, and decision records
- interaction boundary: the system may propose divergent ideas, but if they drift from the main objective, they must go to `ideas_summary` and not be deeply executed by default
- product boundary: this is a research analysis assistant, not a bedside clinical decision system and not an auto-paper factory

### Must deliver
- `product_scope.md`
- `DATABASE_ACCESS_POLICY.md`
- `approval_matrix.md`
- `success_criteria.md`
- `traceability_spec.md`
- `risk_register_v1.md`

### Key decisions
- single database first vs multi-database support
- observational analysis only vs prediction and limited causal workflows
- how conservative the default interpretation style should be

## Phase 1 - Freeze research question templates

### Must define
- supported question classes
  - descriptive studies
  - association studies
  - prediction tasks
  - time-to-event studies
  - longitudinal repeated-measure analyses
  - subgroup and sensitivity analyses
- minimum structured input fields
  - population
  - exposure/intervention
  - comparator
  - primary and secondary outcomes
  - time zero
  - inclusion and exclusion criteria
  - follow-up window
  - key confounders
- a common framing standard, preferably `PICO/PECO + estimand`
- explicit separation between exploratory and confirmatory work

### Must deliver
- `research_question_template.md`
- `analysis_templates.md`
- `estimand_catalog.md`
- `decision_tree.md`
- `use_cases_v1.md`

### Key decisions
- whether open-ended questions can enter execution directly
- whether time zero and follow-up windows must always be explicit
- whether causal inference enters v1 and, if so, with what limits

## Data foundation prerequisite

Before freezing the v1 analysis-layer contracts, treat `D:\\Database\\FRAMEWORK_v4_COMPLETE.md` as the upstream database engineering reference. See `DATA_FOUNDATION_RELATION.md` for the role split between the database foundation and the v1 research system.

## Phase 2 - Freeze data semantics and variable rules

### Must define
- a three-layer data model
  - raw
  - cleaned/interim
  - analytic
- a stable variable dictionary
  - source table
  - field name
  - unit
  - coding system
  - temporal meaning
  - missingness semantics
  - valid range
  - derivation rule
- stable clinical concept definitions
  - sepsis
  - AKI
  - ARDS
  - mechanical ventilation
  - vasopressor exposure
  - ICU mortality / hospital mortality / 28-day mortality
- stable time alignment rules
  - ICU admission time
  - first exposure time
  - baseline window
  - follow-up window

### Must deliver
- `data_inventory.md`
- `variable_dictionary.csv`
- `clinical_concept_definitions.md`
- `derived_variable_specs.md`
- `adataset_spec.md`

### Key decisions
- whether v1 only supports pre-certified variables
- where derived variables are computed: SQL vs Python/R
- whether cross-database harmonization is deferred in favor of single-database adaptation

## Phase 3 - Freeze cohort and study design rules

### Must define
- cohort entry logic
  - first ICU stay vs first admission vs first ED visit
  - repeated admissions
  - ICU readmission
  - adult vs pediatric scope
- study design grammar
  - baseline period
  - exposure assessment window
  - washout period if needed
  - follow-up period
- endpoint definitions and censoring rules
- a fixed bias checklist
  - selection bias
  - information bias
  - immortal time bias
  - label leakage
  - confounding
  - center effect
  - calendar-time effect

### Must deliver
- `cohort_definition.md`
- `cohort_builder_spec.md`
- `bias_checklist.md`
- `endpoint_definition_manual.md`
- `confounder_policy.md`

### Key decisions
- whether v1 starts with single-index, single-primary-endpoint designs only
- whether time-varying exposure/covariates are deferred
- whether advanced survival designs are in or out for v1

## Phase 4 - Freeze the statistical analysis plan discipline

### Must define
- no formal code generation before an approved `SAP`
- primary, secondary, sensitivity, and subgroup analyses
- missing data handling strategy
- model diagnostics expectations
- multiple testing and exploratory labeling rules
- table shells and figure shells before execution

### Must deliver
- `SAP.md`
- `method_selection_tree.md`
- `analysis_order.md`
- `table_shells/`
- `figure_shells/`
- `validation_plan.md`

### Key decisions
- which methods are in v1 by default: descriptive + logistic/Cox may be enough
- whether agents can switch models autonomously
- which scenarios require manual approval before execution

## Phase 5 - Freeze agent contracts and orchestration

### Recommended v1 agent set
- `Coordinator / Orchestrator`
- `Study Design Agent`
- `Data Mapping Agent`
- `Analysis Planning Agent`
- `Code Generation Agent`
- `Execution Validator Agent`
- `Interpretation Agent`
- `Audit / Trace Agent`

### Must define
- strict sequencing
  - design before mapping
  - mapping before planning
  - planning before code generation
  - execution validation before interpretation
- divergent branches go to `ideas_summary` unless the user explicitly promotes them
- agent responsibilities, forbidden actions, and handoff contracts

### Must deliver
- `agent_contracts.md`
- `agent_registry.yaml`
- `workflow_state_machine.md`
- `handoff_contracts.md`
- `default_pipeline.json`

### Key decisions
- state machine first vs DAG first; v1 should prefer state machine
- free-form agent conversation vs structured handoff; v1 should prefer structured handoff
- where manual gates are required

## Phase 6 - Freeze schemas before prompts

### Must define
- every key object has a unique ID and version
- every interpretation block must cite at least one result object
- every result object must link back to code and run metadata
- hypothesis/speculation fields must be separate from fact fields

### Required schemas
- `ResearchQuestionSchema`
- `CohortDefinitionSchema`
- `VariableSpecSchema`
- `AnalysisPlanSchema`
- `CodeArtifactSchema`
- `ResultArtifactSchema`
- `InterpretationSchema`
- `TraceBundleSchema`
- `IdeaSummarySchema`

### Must deliver
- `schemas/` definitions
- `schema_examples/`
- `schema_validation_tests/`

### Key decisions
- schema implementation format; v1 should prefer Pydantic + JSON serialization
- structured interpretation skeleton plus text slots
- terminology mapping fields should exist even if full ontology support is deferred

## Phase 7 - Freeze guardrails

### Must define
- `Scope Guardrail`
- `Plan-First Guardrail`
- `Execution-First Guardrail`
- `Evidence Guardrail`
- `Traceability Guardrail`
- `Clinical Safety Guardrail`
- `Drift Guardrail`
- `Statistical Guardrail`

### Must deliver
- `guardrails.md`
- `policy_engine_rules.yaml`
- `failure_messages.md`
- `red_team_cases.md`

### Key decisions
- hard rules first, LLM classification second
- block vs degrade behavior
- non-overridable rules for traceability and clinical safety

## Phase 8 - Build the traceable execution backbone

### Must define
- minimum trace chain
  - `task_id`
  - `plan_id`
  - `dataset_version`
  - `code_version`
  - `run_id`
  - `artifact_id`
  - `decision_log_id`
- minimum logging requirements
  - agent input/output summary
  - schema validation result
  - state transition logs
  - execution environment
  - dependency versions
  - SQL/code hash
  - random seed
  - failure branch records
  - human intervention points

### Must deliver
- `audit_log_spec.md`
- `run_manifest.json`
- `artifact_store_layout.md`
- `traceability_matrix.md`
- `reproducibility_spec.md`

## Phase 9 - Ship a narrow end-to-end demo

### Recommended first demo scope
- single database only
- single primary analysis language only
- three example themes
  - ICU or hospital mortality
  - sepsis/infection-related cohort analysis
  - mechanical ventilation or vasopressor exposure outcome analysis
- three output classes
  - cohort flow / baseline table
  - main results table
  - one or two standard figures

### Must deliver
- `golden_cases/`
- `demo_runbook.md`
- `review_checklist.md`
- minimal trace browsing or report view

## Phase 10 - Acceptance and release gate

### Must pass
- workflow correctness
- traceability completeness
- research quality checks
- usability for expert review

### Minimum acceptance set
- one descriptive task end-to-end
- one regression task end-to-end
- one survival task end-to-end
- three consistent reruns
- at least one failure-case drill
- divergent ideas only summarized, not deeply executed

## Must-build-first set
- product scope
- research question template
- cohort/time window template
- variable dictionary and analytic dataset spec
- SAP template
- agent contracts
- schemas
- workflow state machine
- guardrails
- traceability and audit specifications

## Can-wait set
- multi-database harmonization
- deep literature coupling
- advanced causal inference suites
- complex survival families
- debate-heavy multi-agent systems
- manuscript automation
- full dashboard and permissions system

## Recommended build order
1. freeze the root documents
2. freeze schemas and workflow state machine
3. freeze agent contracts and guardrails
4. implement a single-database end-to-end demo
5. add audit review and trace browsing
6. expand task coverage only after the backbone is stable

## Root documents to write first
- `v1.0.0/docs/product_scope.md`
- `v1.0.0/docs/DATABASE_ACCESS_POLICY.md`
- `v1.0.0/docs/research_question_template.md`
- `v1.0.0/docs/cohort_time_window_template.md`
- `v1.0.0/docs/adataset_spec.md`
- `v1.0.0/docs/SAP.md`
- `v1.0.0/docs/agent_contracts.md`
