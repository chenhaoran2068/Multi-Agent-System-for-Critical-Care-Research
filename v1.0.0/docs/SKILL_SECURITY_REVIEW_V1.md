# Skill Security Review - v1.0.0

This document records the phase-3 skill reuse review for the critical care research project.

The review does not ask only whether a skill is useful.
For every candidate, it asks three questions at the same time:

1. Can it be used in v1?
2. Is it safe enough for v1?
3. If it is used, how should it be used to avoid network-security and workflow-governance risk?

## Review baseline

A skill is acceptable for v1 only if it does not break these backbone rules:
- stay inside critical care / ICU / emergency medicine database research scope
- do not bypass plan-before-code discipline
- do not bypass validation-before-interpretation discipline
- do not mutate protected data-foundation layers without approval
- do not create uncontrolled external side effects
- do not introduce avoidable network or supply-chain risk

## Decision labels

### `direct_reuse`

Can be used with minimal adaptation because the skill is narrow, low-risk, and aligned to v1.

### `wrap_and_narrow`

Potentially useful, but only through a project-native wrapper or strict policy constraints.
The original skill is too broad, too network-heavy, or too autonomous to import directly.

### `reference_only`

Its ideas, checklist logic, or structure are useful, but the skill itself should not be a live v1 dependency.

### `exclude_from_v1`

Do not bring this skill into v1.
The scope, execution surface, or network/security risk is too high.

## Summary outcome

### Direct reuse candidates
- `cjk-viz`
- `scientific-critical-thinking`
- `svg-ui-templates` (optional, non-core)

### Reuse only through wrapper / narrowing
- `paper-reproduce`
- `dashboard`
- `citation-management`
- `research-lookup`
- `literature-review`
- `scientific-writing`
- `markitdown`

### Reference only
- `biomed-dispatch`

### Exclude from v1 mainline
- `parallel-web`
- `feishu-rich-card`
- `generate-image`
- `scientific-schematics`
- `clinical-decision-support`
- `clinical-reports`
- `treatment-plans`
- `market-research-reports`
- `paper-2-web`
- `scientific-slides`
- `latex-posters`
- `pptx-posters`
- `research-grants`
- `hypothesis-generation`
- `venue-templates`
- `scholar-evaluation`
- document-conversion and presentation skills that require broad external I/O by default
- all omics / bioinformatics / drug-discovery / imaging style paths outside critical-care database research

## Detailed review

### 1. `cjk-viz`

**Can it be used?**
- Yes.
- It is directly relevant when the project produces Chinese labels in tables or figures.
- It fits the result-packaging layer and does not redefine the project scope.

**Is it safe?**
- Mostly yes.
- Main risk is local environment mutation through font installation if the full installation path is used.
- It does not inherently require network access, external APIs, or protected-database writes.

**How should it be used safely?**
- Reuse only the font-detection and rendering configuration path.
- Treat package installation instructions as manual or approval-gated, not autonomous.
- Do not allow the skill to install system packages automatically in v1.

**Decision**
- `direct_reuse`

### 2. `scientific-critical-thinking`

**Can it be used?**
- Yes.
- It aligns strongly with the reviewer and interpretation-boundary parts of the v1 system.
- It supports bias checks, method critique, and evidence-quality review.

**Is it safe?**
- Yes, with minor caveats.
- The core value is conceptual and checklist-oriented.
- The skill text sometimes suggests generating schematics, but that is optional and can be ignored.
- It does not require network access by itself.

**How should it be used safely?**
- Use its critique framework as a bounded reviewer skill under the Execution Validator Agent and Interpretation Agent.
- Strip or ignore its visual-generation suggestions.
- Keep it read-only and text-only in v1.

**Decision**
- `direct_reuse`

### 3. `svg-ui-templates`

**Can it be used?**
- Yes, but only as optional presentation support.
- It is useful for pipeline status and structured review panels.
- It is not a core analysis dependency.

**Is it safe?**
- Largely yes.
- It is local file generation, not inherently networked.
- The main risk is cosmetic distraction or over-investment in appearance before correctness.

**How should it be used safely?**
- Use only after core traceability and correctness artifacts exist.
- Keep it optional and internal-facing.
- Do not let it become a blocker for v1 execution.

**Decision**
- `direct_reuse` as optional presentation helper

### 4. `paper-reproduce`

**Can it be used?**
- Partly.
- Its staged methodology is highly relevant to observational-study reproduction and critical-care database analyses.
- However, it is broader than the v1 product and assumes a general paper-reproduction workflow.

**Is it safe?**
- Not fully safe as-is.
- It implies broad code execution, PDF generation, and potentially uncontrolled reproduction loops.
- It is operationally useful, but too open-ended if imported directly.

**How should it be used safely?**
- Reuse only its phased logic: explore variables first, validate mappings, compare sample attrition stepwise, and document deviations.
- Wrap it behind v1 agent contracts and approval rules.
- Remove any assumption that the full paper-reproduction workflow is allowed automatically.

**Decision**
- `wrap_and_narrow`

### 5. `dashboard`

**Can it be used?**
- Yes, but not as a mandatory default in early v1.
- It is useful for local progress visibility and artifact preview.

**Is it safe?**
- Mostly safe locally, but not risk-free.
- It runs a local server and increases surface area.
- The risk is not classic internet exposure by itself, but it does create a runtime service and UX dependency.

**How should it be used safely?**
- Use only as an internal localhost-only artifact viewer.
- Do not make it required for every v1 run before the core workflow stabilizes.
- Treat dashboard serving as optional and local-only.

**Decision**
- `wrap_and_narrow`

### 6. `citation-management`

**Can it be used?**
- Yes, in a bounded later-phase role.
- It is useful for citation verification, DOI completion, and bibliography hygiene.

**Is it safe?**
- Not fully safe if imported without constraints.
- It depends heavily on external web services such as Google Scholar, PubMed, CrossRef, DOI resolution, and possibly scraping-style access.
- That creates both network-dependency and data egress considerations.

**How should it be used safely?**
- Restrict it to metadata lookup on publication identifiers, never on private study data.
- Allow it only for final writing/report packaging, not core analysis execution.
- Prefer explicit, approval-aware lookup steps over automatic broad searches.

**Decision**
- `wrap_and_narrow`

### 7. `research-lookup`

**Can it be used?**
- Only in a narrow support role.
- It is useful for background literature and contextualization, not for the core v1 analysis path.

**Is it safe?**
- Not as-is.
- It is explicitly network-first and depends on Parallel API and Perplexity/OpenRouter.
- It encourages external API use and saved source harvesting.
- It should never see protected project data or intermediate clinical result objects by default.

**How should it be used safely?**
- Use only for public literature background, never for sending sensitive project content outward.
- Gate its use behind explicit user intent or approval when external research is needed.
- Keep it outside the mandatory mainline and outside sensitive data paths.

**Decision**
- `wrap_and_narrow`

### 8. `literature-review`

**Can it be used?**
- Only partially.
- Its review methodology is valuable, but its operational footprint is too large for v1 mainline.

**Is it safe?**
- Not as-is.
- It assumes multi-database search, heavy external data collection, PDF generation, and mandatory figure generation.
- This creates broad network dependence and unnecessary product expansion.

**How should it be used safely?**
- Borrow its structure and screening logic only.
- Do not import it as a live workflow dependency.
- If later needed, create a project-native mini-review wrapper limited to public literature context only.

**Decision**
- `wrap_and_narrow`

### 9. `scientific-writing`

**Can it be used?**
- Yes, but only for limited internal result packaging.
- It can help shape methods, limitations, and internal summaries.

**Is it safe?**
- Not as-is.
- It is oriented toward full manuscript production, uses research-lookup, and strongly pushes graphical abstracts and generated figures.
- That is too broad for the v1 product boundary.

**How should it be used safely?**
- Reuse only paragraph-style writing discipline and reporting-guideline awareness.
- Restrict outputs to internal result summaries, methods appendix drafts, and limitations notes.
- Do not permit autonomous manuscript-finalization behavior in v1.

**Decision**
- `wrap_and_narrow`

### 10. `markitdown`

**Can it be used?**
- Yes, in a very narrow ingestion role.
- It is useful for converting public PDFs or protocol documents into markdown for local inspection.

**Is it safe?**
- Mixed.
- The core converter is local and relatively safe, but the skill also supports OCR, audio transcription, YouTube URLs, plugin loading, and AI-enhanced image descriptions via external APIs.
- Those extra paths expand both supply-chain and network risk.

**How should it be used safely?**
- Allow only local file conversion for approved document types such as PDF and DOCX.
- Disable AI-enhanced image descriptions, plugin loading, YouTube ingestion, and any remote API augmentation.
- Treat it as a local utility, not a networked enrichment tool.

**Decision**
- `wrap_and_narrow`

### 11. `biomed-dispatch`

**Can it be used?**
- Not directly.
- It is useful as an architectural reference for staged execution and dispatch patterns.
- But it is far broader than the v1 target.

**Is it safe?**
- No, not as a direct dependency.
- It is designed to dispatch broad biomedical tasks, spawn sessions, run dashboards, and execute heterogeneous scientific workflows.
- This is too much authority and too much scope for v1.

**How should it be used safely?**
- Use only as reference for dispatch structure and decomposition logic.
- Do not import its workflow directly into v1.

**Decision**
- `reference_only`

### 12. `parallel-web`

**Can it be used?**
- It can be useful in the abstract, but should not be part of v1 mainline.

**Is it safe?**
- Not safe enough for direct inclusion.
- It is explicitly the primary tool for all web operations, depends on external APIs, and encourages broad internet querying.
- This creates persistent network dependency and high risk of accidental project-context leakage.

**How should it be used safely?**
- Exclude it from v1 mainline.
- If ever needed later, use only behind explicit human-approved external research steps.

**Decision**
- `exclude_from_v1`

## Category exclusions

The following classes should be treated as out of scope or too risky for v1 unless later justified individually:

### Broad external-content and publishing skills
- `parallel-web`
- `paper-2-web`
- `scientific-slides`
- `latex-posters`
- `pptx-posters`
- `market-research-reports`

Reason:
- high externalization surface, presentation-first bias, and unnecessary scope expansion

### AI-generated image / schematic stack
- `generate-image`
- `scientific-schematics`
- `infographics`

Reason:
- not necessary for trustworthy v1 backbone, often network-backed, and can distract from traceable correctness

### Clinical output skills with claim-risk
- `clinical-decision-support`
- `clinical-reports`
- `treatment-plans`

Reason:
- too close to practice-guiding or clinical-advice-style output, which v1 explicitly avoids

### Broad research-expansion skills
- `hypothesis-generation`
- `research-grants`
- `scholar-evaluation`

Reason:
- encourage exploration and expansion rather than disciplined main-task execution

### Non-critical but still external-heavy writing helpers
- `venue-templates`

Reason:
- useful later, but not needed before the analysis and audit core is stable

## Recommended v1-native wrapper skills

Instead of importing broad MedgeClaw skills directly, v1 should introduce narrower wrappers around the useful parts.

### `critical-care-review-helper`
- source logic: `scientific-critical-thinking`
- role: bounded reviewer checklist for design, validation, and interpretation
- network: none
- approval level: `auto-allow` or `allow-with-log`

### `critical-care-writing-helper`
- source logic: `scientific-writing` + `citation-management`
- role: methods appendix, internal summary, limitations note
- network: disabled by default; citation lookup approval-gated
- approval level: `allow-with-log`

### `critical-care-paper-repro-helper`
- source logic: `paper-reproduce`
- role: variable validation, sample attrition checking, result-comparison structure
- network: none by default
- approval level: `allow-with-log`

### `critical-care-doc-convert`
- source logic: `markitdown`
- role: local PDF/DOCX to markdown conversion only
- network: forbidden
- plugin loading: forbidden
- approval level: `allow-with-log`

### `critical-care-local-dashboard`
- source logic: `dashboard`
- role: optional localhost artifact preview
- network: localhost only
- approval level: `allow-with-log`

## Recommended next implementation rule

Phase 3 should not import whole upstream skills blindly.
It should do this instead:

1. pick a narrow v1-native wrapper target
2. document what upstream skill logic is borrowed
3. explicitly remove or disable unsafe paths
4. map wrapper behavior to `approval_matrix.md` and `policy_engine_rules.yaml`
5. allow use only after the wrapper contract is frozen

## V1/V2 boundary decision

The project explicitly adopts this boundary:
- `v1` focuses on the smallest implementable end-to-end workflow loop
- broad web, publishing, image-generation, and clinical-advice-adjacent capabilities are deferred to `v2`

Reason:
- they are not useless, but they expand scope, increase network and supply-chain exposure, and pull the product away from the local, traceable, approval-aware research core that `v1` is supposed to freeze first

This means the current exclusions are version-bound, not permanent.
They are excluded from the `v1` mainline to protect the minimum trustworthy workflow, and may be reconsidered only after that backbone is proven stable.

## Bottom line

The project can and should reuse a small amount of MedgeClaw skill logic.
But for v1, safe reuse means:
- direct reuse only for narrow, local, low-side-effect helpers
- wrapper-based reuse for anything networked, broad, or execution-heavy
- exclusion for anything that expands scope, increases external attack surface, or weakens governance discipline
