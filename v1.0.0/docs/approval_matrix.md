# Approval Matrix - v1.0.0

This document defines how operational actions are classified in v1.0.0.

It is designed to support a disciplined but practical workflow.
The goal is not to freeze the system into uselessness.
The goal is to let the system move quickly inside the main research objective while forcing human oversight at the right boundaries.

## Approval levels

### `auto-allow`
The system may perform the action directly.

### `allow-with-log`
The system may perform the action directly, but it must record the action, inputs, and rationale in the trace or audit layer.

### `require-human-approval`
The system must stop and obtain explicit human approval before proceeding.

### `never-allow-in-v1`
The action is out of bounds for v1.0.0 and must not be performed.

## How to read this matrix

Each action includes:
- the action itself
- its default approval level
- upgrade conditions that make the action more restricted
- downgrade conditions that keep the action in its default lane

Not every action needs both upgrade and downgrade notes.

## 1. Data foundation access and inspection

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Read `index/` layer documents and machine-readable indexes | auto-allow | No upgrade under normal v1 use |
| Read `standardized/` layer outputs | auto-allow | No upgrade under normal v1 use |
| Read existing `studies/{study_id}/extracted_data/` datasets | auto-allow | No upgrade under normal v1 use |
| Read `formatted/` layer for trace or diagnosis | allow-with-log | Upgrade to `require-human-approval` if access would expose sensitive low-level content beyond the current study need |
| Read `split_cleaned/` layer for trace or diagnosis | allow-with-log | Upgrade to `require-human-approval` if inspection goes beyond variable traceability into broad exploratory mining |
| Read `raw/` layer | require-human-approval | No downgrade in v1; raw is treated as a protected layer |
| Scan whether a variable already exists in the current database foundation | auto-allow | No upgrade under normal v1 use |
| Check in which layer a variable first appears | allow-with-log | Downgrade to `auto-allow` only if this later becomes a fully automated metadata lookup rather than a deeper trace action |
| Check a variable's unit, time window, or derivation rule from existing indexes | auto-allow | No upgrade under normal v1 use |
| Generate a missing-variable report | auto-allow | No upgrade under normal v1 use |
| Generate a proposed insertion location for a missing variable | allow-with-log | Upgrade to `require-human-approval` if the proposal includes actual mutation steps rather than a recommendation |

## 2. Data foundation mutation and regeneration

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Add a new processing file for a new variable to an upstream layer | require-human-approval | No downgrade in v1 |
| Add a new dictionary entry in `index/` | require-human-approval | No downgrade in v1 |
| Add a new standard variable mapping in `standardized/` | require-human-approval | No downgrade in v1 |
| Add a new variable convention in `formatted/` | require-human-approval | No downgrade in v1 |
| Add a new split output in `split_cleaned/` | require-human-approval | No downgrade in v1 |
| Extract a currently missing variable from upstream source data | require-human-approval | No downgrade in v1 |
| Add unit-conversion rules for a new variable | require-human-approval | No downgrade in v1 |
| Add terminology-mapping rules for a new variable | require-human-approval | No downgrade in v1 |
| Add quality rules for a new variable | require-human-approval | No downgrade in v1 |
| Modify an existing variable definition | require-human-approval | No downgrade in v1 |
| Modify an existing derivation rule | require-human-approval | No downgrade in v1 |
| Modify an existing unit-conversion rule | require-human-approval | No downgrade in v1 |
| Modify existing variable explanation in index docs | require-human-approval | No downgrade in v1 |
| Backfill historical data for a newly added variable | require-human-approval | No downgrade in v1 |
| Re-run standardization pipeline | require-human-approval | Downgrade to `allow-with-log` only if later restricted to a previously approved no-content-change rebuild |
| Re-run index build | allow-with-log | Upgrade to `require-human-approval` if the rebuild follows unapproved upstream content changes |
| Re-run quality validation | allow-with-log | Downgrade to `auto-allow` only if later made part of a fixed automatic validation cycle |
| Re-run the full database preparation workflow | require-human-approval | No downgrade in v1 |

## 3. Protected-layer red lines

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Delete files from `raw/` | never-allow-in-v1 | No downgrade |
| Delete files from `split_cleaned/` | never-allow-in-v1 | No downgrade |
| Delete files from `formatted/` | never-allow-in-v1 | No downgrade |
| Delete files from `standardized/` | never-allow-in-v1 | No downgrade |
| Delete files from `index/` | never-allow-in-v1 | No downgrade |
| Overwrite existing upstream files in place | never-allow-in-v1 | No downgrade |
| Silently replace historical data products | never-allow-in-v1 | No downgrade |
| Modify protected foundation content without version tracking | never-allow-in-v1 | No downgrade |

## 4. Research question and scope management

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Convert a user question into a structured research question | auto-allow | No upgrade under normal v1 use |
| Ask clarification questions when definitions are ambiguous | auto-allow | No upgrade under normal v1 use |
| Split a broad problem into a main question and side ideas | allow-with-log | Upgrade to `require-human-approval` if the split would materially change the main objective |
| Record side ideas in `ideas_summary` | allow-with-log | No upgrade under normal v1 use |
| Rephrase the study title without changing meaning | allow-with-log | Upgrade to `require-human-approval` if meaning, endpoint, or target population changes |
| Change the question class | require-human-approval | No downgrade in v1 |
| Change the primary research objective | require-human-approval | No downgrade in v1 |
| Replace the user's main question with a more convenient one | require-human-approval | Upgrade to `never-allow-in-v1` if done without explicit user awareness |
| Promote an exploratory idea into the main analysis path | require-human-approval | No downgrade in v1 |
| Discard the user's primary question and pursue a different one | never-allow-in-v1 | No downgrade |

## 5. Cohort, time, and endpoint design

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Use default `T0 = ICU admission` | auto-allow | No upgrade under normal v1 use |
| Use a non-default time zero | require-human-approval | No downgrade in v1 |
| Define baseline window within standard templates | allow-with-log | Upgrade to `require-human-approval` if the window materially changes cohort meaning |
| Define exposure window within standard templates | allow-with-log | Upgrade to `require-human-approval` if the window change alters the study question materially |
| Define follow-up window within standard templates | allow-with-log | Upgrade to `require-human-approval` if it materially changes endpoint meaning |
| Define censoring rules within standard templates | allow-with-log | Upgrade to `require-human-approval` if censoring becomes complex or strongly outcome-shaping |
| Set unit of analysis to default ICU-stay level | auto-allow | Upgrade to `allow-with-log` if justification text is required for audit completeness |
| Change to patient-level or all-ICU-stays analysis | require-human-approval | No downgrade in v1 |
| Modify inclusion criteria | require-human-approval | No downgrade in v1 |
| Modify exclusion criteria | require-human-approval | No downgrade in v1 |
| Modify repeated-admission policy | require-human-approval | No downgrade in v1 |
| Modify ICU-readmission policy | require-human-approval | No downgrade in v1 |
| Modify primary endpoint definition | require-human-approval | No downgrade in v1 |
| Modify outcome window | require-human-approval | No downgrade in v1 |
| Introduce competing-risk handling | require-human-approval | No downgrade in v1 |
| Introduce time-varying exposure or covariate logic | require-human-approval | No downgrade in v1 |

## 6. Variable mapping and analysis-dataset construction

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Select approved standard variables into an analysis dataset | allow-with-log | Downgrade to `auto-allow` only if later done by a fully deterministic extraction template |
| Define variable aggregation within approved templates | allow-with-log | Upgrade to `require-human-approval` if aggregation materially changes interpretation or departs from template norms |
| Generate an analysis-dataset extraction plan | allow-with-log | No upgrade under normal v1 use |
| Generate extraction manifest | auto-allow | No upgrade under normal v1 use |
| Generate codebook | auto-allow | No upgrade under normal v1 use |
| Use a proxy variable when the target variable is missing | require-human-approval | No downgrade in v1 |
| Treat a partial match as a formal mapped variable | require-human-approval | No downgrade in v1 |
| Change the analysis dataset unit of analysis | require-human-approval | No downgrade in v1 |
| Change field definitions in the analysis dataset contract | require-human-approval | No downgrade in v1 |
| Silently impute missing values during extraction | never-allow-in-v1 | No downgrade |
| Silently recode variables during extraction | never-allow-in-v1 | No downgrade |
| Silently trim outliers during extraction | never-allow-in-v1 | No downgrade |

## 7. SAP and methodological planning

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Generate a study-specific SAP | allow-with-log | No upgrade under normal v1 use |
| Choose among approved default method families | allow-with-log | Upgrade to `require-human-approval` if the chosen family changes the study class materially |
| Set primary analysis method within the study class | allow-with-log | Upgrade to `require-human-approval` if the change materially redefines the question or endpoint |
| Set secondary analyses | allow-with-log | Upgrade to `require-human-approval` if the analysis count or complexity expands substantially |
| Add subgroup analysis | allow-with-log | Upgrade to `require-human-approval` if subgroup analysis is result-driven, not predeclared, unusually numerous, or materially shifts the study narrative |
| Add sensitivity analysis | allow-with-log | Upgrade to `require-human-approval` if it materially rewrites the main question, introduces major methodological complexity, or requires new database-foundation changes |
| Modify missing-data strategy | require-human-approval | No downgrade in v1 |
| Modify covariate set | require-human-approval | No downgrade in v1 |
| Introduce data-driven variable selection | require-human-approval | No downgrade in v1 |
| Reframe an association study as prediction | require-human-approval | No downgrade in v1 |
| Reframe an association study as causal analysis | require-human-approval | No downgrade in v1 |
| Switch between major method families in a way that changes endpoint interpretation | require-human-approval | No downgrade in v1 |
| Modify multiplicity policy | require-human-approval | No downgrade in v1 |
| Modify interpretation boundary | require-human-approval | No downgrade in v1 |
| Proceed to code generation without SAP approval | never-allow-in-v1 | No downgrade |

## 8. Code generation and execution

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Generate SQL/Python/R code from an approved plan | allow-with-log | Downgrade to `auto-allow` only if later restricted to deterministic, fully template-driven generation |
| Generate dependency files and execution entrypoints | allow-with-log | No upgrade under normal v1 use |
| Execute approved code | allow-with-log | Upgrade to `require-human-approval` if execution would mutate protected upstream layers |
| Re-run failed tasks | allow-with-log | Upgrade to `require-human-approval` if rerun implies a methodological downgrade or altered data contract |
| Auto-downgrade methods after failure and rerun | require-human-approval | No downgrade in v1 |
| Modify code to fix implementation bugs without changing plan | allow-with-log | Upgrade to `require-human-approval` if the bug fix changes the plan logic |
| Modify code to reflect a changed SAP | require-human-approval | No downgrade in v1 |
| Run queries that read protected layers but do not write them | allow-with-log | Upgrade to `require-human-approval` when touching `raw/` |
| Run a process that writes new files into the upstream foundation | require-human-approval | No downgrade in v1 |
| Execute protected-layer mutations without explicit human approval | never-allow-in-v1 | No downgrade |
| Fabricate placeholder results after execution failure | never-allow-in-v1 | No downgrade |

## 9. Validation and quality control

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Check execution success | auto-allow | No upgrade under normal v1 use |
| Check whether expected tables and figures were produced | auto-allow | No upgrade under normal v1 use |
| Check validation status fields | auto-allow | No upgrade under normal v1 use |
| Check sample-size consistency | auto-allow | No upgrade under normal v1 use |
| Check endpoint completeness | auto-allow | No upgrade under normal v1 use |
| Check consistency between outputs and planned shells | auto-allow | No upgrade under normal v1 use |
| Downgrade a hard fail to a warning | require-human-approval | No downgrade in v1 |
| Upgrade a warning to a hard fail | allow-with-log | Downgrade to `auto-allow` only if later governed by fixed QC thresholds |
| Block interpretation because of validation problems | auto-allow | No upgrade under normal v1 use |
| Request rerun or correction | allow-with-log | No upgrade under normal v1 use |

## 10. Interpretation and scientific expression

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Generate interpretation from validated results | allow-with-log | No upgrade under normal v1 use |
| Distinguish fact, statistical result, interpretation, and hypothesis | auto-allow | No upgrade under normal v1 use |
| Add limitations and uncertainty statements | auto-allow | No upgrade under normal v1 use |
| Record exploratory findings in side notes | allow-with-log | No upgrade under normal v1 use |
| Use association language for observational findings | auto-allow | No upgrade under normal v1 use |
| Use prediction-performance language for prediction tasks | auto-allow | No upgrade under normal v1 use |
| Use causal language | require-human-approval | No downgrade in v1 |
| Add mild research-facing clinical significance commentary | allow-with-log | Upgrade to `require-human-approval` if wording could reasonably be read as practice-guiding rather than research-facing |
| Suggest changing treatment strategy | never-allow-in-v1 | No downgrade |
| Cite unvalidated outputs as findings | never-allow-in-v1 | No downgrade |
| Cite outputs that lack artifact IDs as findings | never-allow-in-v1 | No downgrade |
| Omit limitations while presenting formal conclusions | never-allow-in-v1 | No downgrade |

## 11. Audit, traceability, and release integrity

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Generate trace bundle | allow-with-log | No upgrade under normal v1 use |
| Link result artifacts to code artifacts | auto-allow | No upgrade under normal v1 use |
| Link interpretation claims to result artifact IDs | auto-allow | No upgrade under normal v1 use |
| Record decision logs | auto-allow | No upgrade under normal v1 use |
| Record approval nodes | auto-allow | No upgrade under normal v1 use |
| Block release when trace is incomplete | auto-allow | No upgrade under normal v1 use |
| Mark outputs as releasable despite missing trace | never-allow-in-v1 | No downgrade |
| Backfill trace links after the fact without provenance | never-allow-in-v1 | No downgrade |
| Modify historical audit records | never-allow-in-v1 | No downgrade |

## 12. Output packaging and publication-oriented wording

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Generate internal research summary | allow-with-log | No upgrade under normal v1 use |
| Generate formal result bundle for internal review | allow-with-log | No upgrade under normal v1 use |
| Generate manuscript-ready wording draft | allow-with-log | Upgrade to `require-human-approval` when marking wording as final or ready for external use |
| Output to internal researcher review | allow-with-log | No upgrade under normal v1 use |
| Output publication-oriented result description for external-style use | require-human-approval | Downgrade to `allow-with-log` only when clearly marked draft-for-review |
| Output wording likely to be mistaken for clinical advice | never-allow-in-v1 | No downgrade |
| Release final conclusions before audit pass | never-allow-in-v1 | No downgrade |
| Use exaggerated language for exploratory findings | never-allow-in-v1 | No downgrade |

## 13. Divergence and branch governance

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Propose future research directions | allow-with-log | No upgrade under normal v1 use |
| Propose subgroup candidates | allow-with-log | No upgrade under normal v1 use |
| Propose alternate endpoint candidates | allow-with-log | No upgrade under normal v1 use |
| Propose new variable needs | allow-with-log | No upgrade under normal v1 use |
| Record these items in `ideas_summary` | allow-with-log | No upgrade under normal v1 use |
| Run multiple analysis strategies that still serve the same original research objective | allow-with-log | Upgrade to `require-human-approval` if the strategy count becomes operationally excessive or effectively changes the study question |
| Promote a summary-only branch into a formal execution branch | require-human-approval | No downgrade in v1 |
| Deepen multiple side branches that drift away from the original objective | require-human-approval | Upgrade to `never-allow-in-v1` if the drift would effectively hijack the main task |
| Delay the main task because side branches are more interesting | never-allow-in-v1 | No downgrade |

## 14. System governance and self-modifying configuration

| Action | Default level | Upgrade conditions / Downgrade conditions |
|---|---|---|
| Add a new agent role | require-human-approval | No downgrade in v1 |
| Modify agent role boundaries | require-human-approval | No downgrade in v1 |
| Modify workflow state machine | require-human-approval | No downgrade in v1 |
| Modify default pipeline configuration | require-human-approval | No downgrade in v1 |
| Modify policy engine rules | require-human-approval | No downgrade in v1 |
| Modify the approval matrix itself | require-human-approval | No downgrade in v1 |
| Loosen protected-database rules | require-human-approval | No downgrade in v1 |
| Loosen interpretation guardrails | require-human-approval | No downgrade in v1 |
| Disable traceability requirements | never-allow-in-v1 | No downgrade |
| Disable validation gate | never-allow-in-v1 | No downgrade |

## Summary principle

The overall logic of v1.0.0 is:
- move fast inside the declared main study objective
- log anything that materially shapes interpretation or traceability
- require human approval whenever the system wants to mutate the protected data foundation, rewrite the study's scientific identity, or materially strengthen claims
- never allow silent foundation mutation, silent methodological drift, fabricated outputs, missing traceability, or clinical-advice-style conclusions
