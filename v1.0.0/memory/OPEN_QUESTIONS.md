# Open Questions - v1.0.0

## Active

1. Should project memory be wired into OpenClaw semantic retrieval directly, or should the first pass remain manual/file-based until local-first indexing is fully stable?
2. For local-first memory retrieval, should the system prefer a true local embedding backend, or use the existing proxy endpoint as a temporary fallback while keeping project memory files local?
3. Should the project eventually maintain per-phase memory files in addition to the current four-file structure?

## Resolved

- The project needs its own dedicated memory layer separate from assistant-level memory.
