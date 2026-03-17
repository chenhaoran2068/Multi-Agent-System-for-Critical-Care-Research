# Agent Definitions - v1.0.0

This directory contains the first role files for the minimum multi-agent team used in v1.0.0.

The role design borrows the good parts of MedgeClaw's modular skill mindset:
- each role has a narrow mission
- each role has explicit inputs and outputs
- each role has forbidden actions
- roles compose into a governed workflow instead of collapsing into one all-powerful agent

## Included role files

- `orchestrator-agent.md`
- `study-design-agent.md`
- `data-mapping-agent.md`
- `analysis-planning-agent.md`
- `code-generation-agent.md`
- `execution-validator-agent.md`
- `interpretation-agent.md`
- `audit-trace-agent.md`

## Operating rule

These files should be read together with:
- `../docs/agent_contracts.md`
- `../docs/DATABASE_ACCESS_POLICY.md`
- `../docs/SAP.md`
- `../schemas/`
