# Skill Wrapper Plan - v1.0.0

This document converts the skill security review into a concrete phase-3 implementation plan.

The purpose is to decide which wrappers are worth creating now, which should remain future options, and which should stay excluded from v1.

## Selection rule

A wrapper should be created in v1 only if all of the following are true:
- it solves a real gap in the v1 workflow
- it improves discipline or reproducibility more than it expands scope
- it can be constrained to local-first or approval-aware behavior
- it maps cleanly to an existing v1 agent or workflow stage

## Wrapper priority tiers

### Tier 1 - Create now

These wrappers add direct value to the v1 backbone and can be kept narrow and safe.

1. `critical-care-review-helper`
2. `critical-care-paper-repro-helper`
3. `critical-care-writing-helper`
4. `critical-care-doc-convert`
5. `critical-care-local-dashboard`

### Tier 2 - Defer until later

Potentially useful, but not needed before the first end-to-end demo.

- literature support wrapper built from `research-lookup` and `literature-review`
- citation enrichment wrapper built from `citation-management`
- optional visual presentation wrapper built from `svg-ui-templates`

### Tier 3 - Explicitly excluded from v1 mainline

- broad dispatch wrappers
- broad web-research wrappers
- image generation wrappers
- clinical decision and treatment output wrappers
- publishing/presentation automation wrappers

## Why these five wrappers are enough for now

### `critical-care-review-helper`
- closes the reviewer-quality gap
- local and checklist-oriented
- aligns with validation and interpretation stages

### `critical-care-paper-repro-helper`
- borrows the most useful reproducibility logic from paper reproduction
- directly helps variable validation, sample filtering, and result comparison
- improves study discipline without forcing full reproduction workflow complexity

### `critical-care-writing-helper`
- provides bounded internal writing support
- turns approved plans and validated results into methods/summary/limitations drafts
- stays inside v1 output boundaries

### `critical-care-doc-convert`
- solves local document ingestion without introducing mandatory network dependencies
- useful for reading PDFs, protocols, and paper appendices

### `critical-care-local-dashboard`
- optional, not mandatory
- gives a local artifact preview path without changing the scientific core

## Mapping to agents

| Wrapper skill | Primary agent(s) |
| --- | --- |
| `critical-care-review-helper` | Execution Validator Agent, Interpretation Agent |
| `critical-care-paper-repro-helper` | Data Mapping Agent, Analysis Planning Agent, Code Generation Agent |
| `critical-care-writing-helper` | Analysis Planning Agent, Interpretation Agent, Audit / Trace Agent |
| `critical-care-doc-convert` | Study Design Agent, Data Mapping Agent |
| `critical-care-local-dashboard` | Orchestrator Agent |

## Phase-3 completion criterion

Phase 3 is considered complete when:
- the security review exists
- wrapper selection is explicit
- wrapper specs exist for each selected wrapper
- excluded skills are documented clearly
- no additional wrapper is created without justification

## Out-of-scope for phase 3

Phase 3 does not require:
- full runtime implementation of wrappers
- external API integration
- automatic package installation
- production-ready prompt libraries

Those belong to later implementation phases.
