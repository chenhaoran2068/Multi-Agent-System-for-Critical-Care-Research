# Database Access Policy

This document defines what the v1.0.0 system may read, may propose, and may not change in the upstream database foundation.

## Core rule

The upstream database foundation is read-first and protected-by-default.

The v1.0.0 research system may consume it for research tasks, but must not mutate protected layers without explicit human approval.

## Layer policy

The upstream framework defines these layers:
- `raw/`
- `split_cleaned/`
- `formatted/`
- `standardized/`
- `index/`
- `studies/`

### Read policy

#### Default readable layers
- `standardized/`
- `index/`
- `studies/{study_id}/extracted_data/`

#### Conditionally inspectable layers
- `split_cleaned/`
- `formatted/`
- `raw/`

These deeper layers may be inspected when needed to:
- trace a variable origin
- diagnose missing variables
- verify derivation logic
- determine whether a proposed new variable is technically extractable

Inspection does not imply write permission.

## Write policy

### Forbidden by default
- deleting files in any upstream layer
- modifying existing files in any upstream layer
- overwriting indexes, dictionaries, or processed tables
- appending new variables into protected layers
- changing derivation logic or unit mappings in place

### Allowed only with explicit human approval
- creating a new variable extraction output
- adding new variable metadata to a dictionary or index
- adding new processed files into an appropriate layer
- revising an existing mapping rule
- revising an existing derivation definition

## Missing-variable workflow

If a study requires a variable that is not currently available in the protected database foundation, the system should follow this workflow:

1. detect and declare the variable as missing
2. search the existing indexed and standardized layers
3. if still missing, inspect deeper layers to see whether the raw source likely exists
4. produce a structured proposal containing:
   - variable name
   - clinical meaning
   - likely source file or field
   - proposed target layer
   - proposed standard variable name
   - unit and coding expectations
   - derivation or extraction logic
   - risks or ambiguities
5. stop and wait for human approval
6. only after approval, execute extraction/addition work

## Human approval triggers

Explicit approval is required for:
- any new variable insertion
- any new processed file creation inside the upstream foundation
- any update to a data dictionary or index
- any change to an existing variable definition
- any backfill affecting previously processed data

## Agent policy

### Agents that may inspect protected layers when necessary
- Data Mapping Agent
- Audit / Trace Agent
- Extraction logic owned by the approved data-processing workflow

### Agents that should not directly use protected low-level layers for analysis
- Interpretation Agent
- final report generation logic
- user-facing summary generation

## Logging requirement

Every inspection or proposed mutation involving protected layers should be logged with:
- task_id
- requesting agent
- reason for inspection
- accessed layer
- requested change
- approval status
- execution status

## Bottom line

The system may learn from the database foundation and inspect it carefully.
It may propose new variables and improved mappings.
But it must not silently change the foundation.
Protected layers remain human-governed.
