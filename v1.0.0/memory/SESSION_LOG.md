# Session Log - v1.0.0

## 2026-03-17

- Confirmed the project needs a dedicated memory layer because the collaboration is long-running and context-heavy.
- Defined a two-layer memory strategy: assistant-level memory in `C:\Users\chr17\.openclaw\workspace\` and project-level memory in `v1.0.0\memory\`.
- Added `docs/MEMORY_STRATEGY.md` to formalize what belongs in each layer.
- Initialized project memory files: `PROJECT_MEMORY.md`, `SESSION_LOG.md`, `DECISIONS.md`, and `OPEN_QUESTIONS.md`.
- Identified that `memory_search` was failing because embeddings defaulted to OpenAI with an invalid path/key combination for embeddings.
- Began repair by explicitly configuring `agents.defaults.memorySearch` in `C:\Users\chr17\.openclaw\openclaw.json`.
- Found a separate OpenClaw-on-Windows issue: `openclaw gateway restart` failed due to `SIGUSR1` incompatibility.
