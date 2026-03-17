---
name: critical-care-local-dashboard
description: Optional localhost-only dashboard helper for internal task progress and artifact preview. Use when the Orchestrator Agent needs a local visual view of task state, outputs, or progress, but only after formal workflow artifacts exist. Do not use as a substitute for run manifests, audit logs, or trace bundles.
---

# Critical Care Local Dashboard

Use this skill only as an optional local convenience layer.

## Do this

1. Build dashboard state from formal workflow artifacts.
2. Keep the service localhost-only.
3. Treat dashboard output as a view, not as the source of truth.
4. Keep dashboard creation optional and non-blocking.

## Use it for

- local task progress view
- artifact preview
- step summary browsing
- internal-only workflow visibility

## Expected outputs

Produce one or more of:
- local dashboard directory
- localhost URL
- dashboard state derived from formal artifacts

## Forbidden behavior

- Do not replace `run_manifest.json`, audit logs, or trace bundle.
- Do not expose a non-local service by default.
- Do not publish outputs externally.
- Do not block valid scientific release if the dashboard is absent or broken.

## Approval rule

- Localhost-only dashboard creation: `allow-with-log`
- Any non-local exposure or sharing: `require-human-approval`

## Agent alignment

Primary agent:
- Orchestrator Agent
