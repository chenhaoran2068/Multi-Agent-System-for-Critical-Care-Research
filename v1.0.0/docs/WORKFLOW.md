# Workflow - v1.0.0

This file is the high-level workflow overview.

For the authoritative state-by-state machine definition, transition rules, and terminal-state behavior, see `docs/workflow_state_machine.md`.
Use this file for the conceptual flow and `docs/workflow_state_machine.md` for implementation-facing semantics.

## Main workflow

1. User question intake
2. Clinical framing
3. Structured specification generation
4. Method selection
5. Code generation and execution
6. Reviewer check
7. Result delivery
8. Optional exploratory suggestions summary

## Decision rule for divergence

If the system identifies promising directions outside the main objective, it must classify them as one of the following:
- near-scope extension
- future analysis candidate
- out-of-scope idea

Only near-scope extensions may be recommended inline.
All others should be summarized at the end without deep execution.

## Human control points

Human confirmation should be requested when:
- the cohort definition materially changes
- the primary outcome changes
- a major method switch is required
- an exploratory branch is about to become a full analysis task

## Required traceability package

Each completed task should preserve:
- original question
- structured task spec
- analysis plan
- generated code
- execution logs
- result summary
- review notes
