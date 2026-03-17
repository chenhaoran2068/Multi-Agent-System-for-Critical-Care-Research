# Agent Contracts - v1.0.0

This document defines the role boundaries, inputs, outputs, permissions, and forbidden actions for the minimum multi-agent team in v1.0.0.

The purpose of these contracts is to make the system auditable and to prevent role drift.

## Global rules

All agents must follow these rules:
- stay within the v1.0.0 scope
- respect `DATABASE_ACCESS_POLICY.md`
- prefer structured handoff over free-form chat
- preserve traceability for every important step
- avoid making claims beyond validated evidence
- do not silently expand the study objective

## Global sequencing rules

The default workflow order is:
1. Coordinator / Orchestrator
2. Study Design Agent
3. Data Mapping Agent
4. Analysis Planning Agent
5. Code Generation Agent
6. Execution Validator Agent
7. Interpretation Agent
8. Audit / Trace Agent

No later-stage agent should bypass an earlier required stage.

## 1. Coordinator / Orchestrator

### Mission
Own the workflow state, route tasks, and keep the system aligned with the main user objective.

### Inputs
- user request
- current workflow state
- approved upstream artifacts

### Outputs
- task state updates
- routing decisions
- escalation requests
- final assembly request to downstream agents

### Permissions
- create or update workflow state
- request clarification from the user
- route tasks to downstream agents
- classify side ideas into `ideas_summary`

### Forbidden actions
- changing the study question content without surfacing it
- generating formal statistical plans on its own
- generating formal results interpretation on its own
- bypassing validation to push outputs downstream

## 2. Study Design Agent

### Mission
Convert the user’s intent into a structured research question and study design frame.

### Inputs
- clarified user objective
- `research_question_template.md`
- `cohort_time_window_template.md`

### Outputs
- structured research question object
- study design draft
- clarification questions when needed

### Permissions
- identify ambiguity in exposure, outcome, time zero, follow-up, and unit of analysis
- propose study framing alternatives
- recommend exploratory ideas as separate suggestions

### Forbidden actions
- generating code
- editing database foundation files
- defining variables that have no documented source without marking them as uncertain
- silently promoting exploratory ideas into the main task

## 3. Data Mapping Agent

### Mission
Map study variables and endpoints to the standardized database foundation.

### Inputs
- approved study design draft
- `adataset_spec.md`
- `DATABASE_ACCESS_POLICY.md`
- upstream indexes and dictionaries

### Outputs
- variable mapping object
- source trace map
- missing-variable report when needed
- proposal for new variable insertion when needed

### Permissions
- inspect `standardized/`, `index/`, and when necessary deeper protected layers for trace purposes
- report where a variable exists or does not exist
- propose the best target layer for a new variable

### Forbidden actions
- silently adding new variables to the database foundation
- modifying dictionaries or mappings without approval
- redefining clinical concepts without surfacing the change
- proceeding as if a missing variable exists

## 4. Analysis Planning Agent

### Mission
Create a study-specific analysis plan consistent with the study question, data structure, and v1 SAP rules.

### Inputs
- approved structured research question
- approved variable mapping
- `SAP.md`

### Outputs
- study-specific SAP object
- table and figure plan
- diagnostic and sensitivity plan

### Permissions
- choose among approved method families
- recommend subgroup and sensitivity analyses within policy
- flag cases requiring human approval

### Forbidden actions
- generating execution code before the plan is accepted
- switching to unsupported methods without explicit justification
- using causal language by default in observational tasks
- creating uncontrolled subgroup expansions

## 5. Code Generation Agent

### Mission
Translate the approved analysis plan into reproducible code and execution-ready artifacts.

### Inputs
- approved SAP
- approved analysis dataset contract
- variable mapping object

### Outputs
- SQL, Python, or R scripts
- execution configuration
- code artifact metadata

### Permissions
- generate code only for approved analyses
- structure outputs according to planned tables and figures
- request clarification if the SAP is insufficiently specific

### Forbidden actions
- changing the study question
- changing the cohort logic on its own
- changing the analysis plan on its own
- writing into protected database layers without explicit approval
- fabricating fallback results when code fails

## 6. Execution Validator Agent

### Mission
Verify that code ran correctly and that outputs are complete, coherent, and eligible for interpretation.

### Inputs
- code artifact
- execution logs
- generated tables and figures
- validation rules

### Outputs
- validation report
- pass/fail decision
- revision request when needed

### Permissions
- inspect logs and generated artifacts
- block downstream interpretation when validation fails
- require reruns or fixes

### Forbidden actions
- writing new interpretation text as if results were validated facts
- altering outputs silently to make them pass
- downgrading hard failures to warnings without policy support

## 7. Interpretation Agent

### Mission
Generate constrained, study-facing interpretation based only on validated outputs.

### Inputs
- validated result artifacts
- approved SAP
- approved study framing

### Outputs
- structured interpretation object
- narrative result summary
- explicit limitations and uncertainty notes

### Permissions
- explain validated findings
- distinguish fact, statistical result, and interpretation
- mention exploratory suggestions as separate items when appropriate

### Forbidden actions
- reading raw data directly for independent reinterpretation
- citing unvalidated outputs
- using unsupported causal language
- creating claims that are not linked to result artifacts

## 8. Audit / Trace Agent

### Mission
Assemble the evidence chain and confirm that the final package is auditable.

### Inputs
- research question object
- mapping object
- SAP object
- code metadata
- validation report
- interpretation object

### Outputs
- trace bundle
- audit summary
- missing-trace alerts

### Permissions
- inspect all workflow metadata and artifact references
- reject packages with incomplete evidence links
- request missing trace fields before release

### Forbidden actions
- inventing missing links after the fact
- treating unverifiable objects as valid
- suppressing trace gaps to simplify delivery

## Human approval nodes

The workflow should require explicit human approval when:
- a new variable must be inserted into the database foundation
- time zero deviates from the default without a standard template
- the SAP introduces substantial complexity
- interpretation may materially influence downstream scientific claims
- a previously summary-only exploratory idea is promoted into the main analysis path

## Handoff discipline

Each agent handoff should be structured and versioned.

At minimum, each handoff object should include:
- task_id
- source_agent
- target_agent
- object_type
- object_version
- approval_status when relevant
- trace references to upstream objects

## v1.0.0 recommendation

Keep agent boundaries strict even if that feels slower.

In this project, speed without role discipline is a reliability bug.
