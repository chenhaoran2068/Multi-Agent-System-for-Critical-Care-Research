---
name: critical-care-doc-convert
description: Local document-to-markdown conversion helper for approved files such as PDF and DOCX. Use when the system needs to ingest local papers, appendices, or protocol documents into markdown for manual inspection. Use for Study Design Agent and Data Mapping Agent tasks that must stay local and must not use plugins, OCR add-ons, URLs, or AI-enhanced remote conversion paths.
---

# Critical Care Doc Convert

Use this skill to convert approved local documents into markdown for inspection.

## Do this

1. Accept only local files in approved formats.
2. Convert them into markdown for reading, not for decorative republishing.
3. Save converted output into the task artifact tree.
4. Preserve a note of the source file path and conversion time.

## Approved inputs in early v1

- PDF
- DOCX

## Expected outputs

Produce:
- converted markdown document
- source-file note
- conversion log entry

## Forbidden behavior

- Do not fetch remote URLs.
- Do not process YouTube or audio inputs.
- Do not enable AI-enhanced image descriptions.
- Do not enable plugin loading.
- Do not auto-install extra dependencies at runtime.
- Do not touch protected database files.

## Approval rule

- Local conversion of approved files: `allow-with-log`
- OCR, plugins, remote URLs, or external APIs: `require-human-approval`

## Agent alignment

Primary agents:
- Study Design Agent
- Data Mapping Agent
