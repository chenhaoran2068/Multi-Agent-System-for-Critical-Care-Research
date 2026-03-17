# Decisions - v1.0.0

## 2026-03-17 - Memory layering

Decision:
- Use two distinct memory layers.

Why:
- Cross-project collaboration preferences and assistant-environment facts should not be mixed with project-specific implementation state.
- This project is long-running and document-heavy, so it needs its own persistent memory layer.

Impact:
- Assistant-level memory remains in `C:\Users\chr17\.openclaw\workspace\MEMORY.md` and `C:\Users\chr17\.openclaw\workspace\memory\`.
- Project-level memory is stored in `E:\chr\Multi-Agent-System-for-Critical-Care-Research\v1.0.0\memory\`.
- Retrieval for project work should prefer project memory first, then assistant memory.

Approval:
- Human-approved in chat on 2026-03-17.

## 2026-03-17 - V1 minimal loop, broader skills deferred to v2

Decision:
- `v1` should complete only the minimum trustworthy end-to-end workflow loop.
- broad web, publishing, image-generation, and clinical-advice-adjacent skills are deferred to `v2`.

Why:
- These capabilities increase scope, network exposure, packaging bias, and claim-risk before the local research backbone is fully proven.
- The first milestone is a small, stable, auditable research workflow, not a broad capability surface.

Impact:
- `v1` keeps a narrow, wrapper-based skill layer.
- excluded skill classes are not treated as useless, only version-deferred.
- future expansion should happen after the v1 workflow loop is accepted.

Approval:
- Human-approved in chat on 2026-03-17.
