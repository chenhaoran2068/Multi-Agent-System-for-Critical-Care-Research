# Product Scope - v1.0.0

This document defines the hard boundaries of v1.0.0.

## Product identity

v1.0.0 is a focused multi-agent research assistant for emergency medicine, ICU, and critical care database analysis.

It is not:
- a general medical AI platform
- a bedside clinical decision system
- a full autonomous paper-generation system
- a wet-lab, omics, imaging, or device-analysis platform

## In-scope

### Domain scope
- emergency medicine research
- ICU research
- critical care research
- retrospective and structured clinical database studies

### Data scope
- structured clinical databases only
- demographics, diagnoses, procedures, medications, laboratory tests, vital signs, respiratory support, hemodynamics, outcomes, and time-stamped event data
- standardized and indexed database layers prepared through the upstream database framework

### Output scope
- structured research question
- cohort and time-window definition
- analysis dataset extraction contract
- statistical analysis plan
- reproducible code
- result tables and figures
- constrained written interpretation
- traceable audit bundle

### Exploration scope
- the system may propose related ideas, subgroup ideas, alternative outcomes, and sensitivity-analysis candidates
- if they drift away from the main research objective, they must be summarized only
- they must not be deeply executed unless explicitly approved and promoted by the user

## Out-of-scope

- patient-specific treatment advice
- real-time bedside decision support
- unrestricted autonomous literature exploration as a default behavior
- unrestricted autonomous topic expansion
- non-structured source modalities such as raw notes, free text, images, waveforms, audio, and omics for v1 mainline
- uncontrolled direct database mutation by analysis agents

## Database handling boundary

The upstream database is treated as a protected data foundation.

### Allowed default behavior
- read database framework documents
- read indexed metadata and variable dictionaries
- read standardized and study-level extracted datasets
- inspect where a variable currently exists in the database foundation
- report missing variables or unsupported mappings
- propose where a new variable should be inserted in the framework

### Forbidden default behavior
- delete files from the database foundation
- modify existing files in the database foundation
- overwrite existing mappings, dictionaries, or processed datasets without explicit human approval
- silently add a new variable to any layer
- silently backfill or regenerate database layers after discovering a missing variable

## Missing-variable policy

If a needed variable is not currently available in the existing database foundation, the system may:
- identify that the variable is missing
- inspect upstream layers to determine whether the raw signal or source field appears to exist
- recommend the most appropriate target layer for insertion or mapping
- generate a proposed extraction or standardization plan

However, the system must not:
- extract and add the new variable into the database foundation automatically
- modify any protected layer without explicit human approval

Human approval is required before:
- extracting a new variable from an upstream source
- adding new variable metadata to a dictionary or index
- adding new processed files to a standardized layer
- changing an existing variable definition or derivation rule

## Safety boundary

Every formal conclusion must be traceable to:
- source database and version
- study-level extraction definition
- code version
- execution run
- result artifact
- audit record

## Build philosophy

v1.0.0 should be narrow, disciplined, and auditable first.
Breadth comes later.
