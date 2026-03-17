# Skill Reuse Strategy

This document defines how v1.0.0 should reuse capabilities from MedgeClaw.

## Principle

Reuse proven and safe capability modules when they genuinely fit the v1 objective.
Do not hand-build everything from scratch if a safe and appropriate MedgeClaw capability already solves the problem.

At the same time, do not import broad or unsafe capabilities just because they exist.

## Reuse decision rule

A MedgeClaw skill is a good candidate for reuse only if all of the following are true:
- it supports emergency / ICU / critical care database research work directly or indirectly
- it does not push the system outside the v1 scope
- it does not weaken the protected-database policy
- it does not create uncontrolled external side effects
- it can be used as a bounded tool, not as an uncontrolled autonomous workflow

## Reuse categories

### Likely reusable with minimal adaptation
- literature and evidence lookup support, if used as optional support rather than autonomous exploration
- scientific critical thinking / review support
- structured writing or reporting helpers for result packaging
- visualization helpers for figures and result presentation
- citation support for later-stage research outputs

### Reusable only with strong boundary control
- paper reproduction style workflows
- broad scientific writing workflows
- dashboard/reporting presentation workflows
- document conversion utilities

These may be useful, but they must not redefine the v1 product into a literature-first or manuscript-first system.

### Usually not reusable in the v1 mainline
- broad biomed dispatch flows
- omics / wet-lab / instrument / drug discovery skills
- anything that assumes unrestricted autonomous scientific exploration
- anything that mutates external systems or datasets without approval

## Preferred reuse pattern

When reusing from MedgeClaw, prefer one of these patterns:
- reference the skill as a bounded optional helper
- borrow its structure or checklist logic into a project-native skill
- wrap it behind the v1 agent contracts and approval rules

Do not let an imported skill bypass:
- product scope
- database access policy
- SAP discipline
- traceability requirements

## Current practical stance

Before building project-native skills from scratch, first check whether MedgeClaw already contains a safe equivalent or partial equivalent.

If yes:
- reuse it directly when the fit is narrow and safe
- otherwise adapt its logic into a narrower v1-specific skill

If no:
- create a project-native skill only for the missing core capability

## Bottom line

v1 should be pragmatic.
It should stand on MedgeClaw's shoulders when that improves safety, speed, and discipline.
It should not inherit unnecessary weight or scope just to avoid writing a small amount of project-specific glue.
