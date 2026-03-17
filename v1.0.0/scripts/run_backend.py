#!/usr/bin/env python3
"""Workflow skeleton runner for v1.0.0.

This script does not execute clinical analysis code yet.
It provides a machine-readable state-machine harness around the v1 workflow so the
project can move from documents to an executable orchestration skeleton.

Supported commands:
- init: create a task workspace and initial manifest from default_pipeline.json
- transition: validate and record a workflow state transition
- inspect: print allowed next states and current manifest summary
"""
from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AUDIT_EVENT_VERSION = "1.0.0"

ROOT = Path(__file__).resolve().parents[1]
PIPELINE_PATH = ROOT / "default_pipeline.json"
MANIFEST_TEMPLATE_PATH = ROOT / "run_manifest.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def pipeline() -> dict[str, Any]:
    return load_json(PIPELINE_PATH)


def transition_table(spec: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    table: dict[str, list[dict[str, Any]]] = {}
    for item in spec.get("transitions", []):
        table.setdefault(item["from"], []).append(item)
    return table


def allowed_next_states(spec: dict[str, Any], state: str) -> list[str]:
    table = transition_table(spec)
    return [item["to"] for item in table.get(state, [])]


def build_task_paths(spec: dict[str, Any], task_id: str) -> dict[str, str]:
    defaults = spec.get("defaults", {})
    return {
        "task_root": defaults.get("task_root", "outputs/{task_id}").format(task_id=task_id),
        "artifacts_root": defaults.get("artifacts_root", "outputs/{task_id}/artifacts").format(task_id=task_id),
        "audit_root": defaults.get("audit_root", "outputs/{task_id}/audit").format(task_id=task_id),
        "logs_root": defaults.get("logs_root", "outputs/{task_id}/logs").format(task_id=task_id),
    }


def load_manifest_template() -> dict[str, Any]:
    template = load_json(MANIFEST_TEMPLATE_PATH)
    return template


def append_jsonl(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")


def audit_log_path(manifest: dict[str, Any], key: str) -> Path:
    rel = manifest.get("audit_context", {}).get(key)
    if not rel:
        raise SystemExit(f"Missing audit path for {key} in manifest")
    return ROOT / rel


def write_state_transition_event(
    manifest: dict[str, Any],
    task_id: str,
    from_state: str,
    to_state: str,
    stage: str,
    actor: str,
    note: str,
    manifest_path: Path,
) -> None:
    event = {
        "transition_id": f"transition_{task_id}_{len(manifest.get('state_history', [])) + 1}",
        "event_version": AUDIT_EVENT_VERSION,
        "task_id": task_id,
        "timestamp": now_iso(),
        "from_state": from_state,
        "to_state": to_state,
        "stage": stage,
        "actor": actor,
        "note": note,
        "manifest_path": str(manifest_path),
    }
    append_jsonl(audit_log_path(manifest, "state_transition_log_path"), event)


def init_manifest(task_id: str, task_mode: str, title: str) -> dict[str, Any]:
    spec = pipeline()
    template = deepcopy(load_manifest_template())
    paths = build_task_paths(spec, task_id)
    template["manifest_version"] = spec.get("version", "1.0.0")
    template["task_id"] = task_id
    template["task_mode"] = task_mode
    template["study_title"] = title
    template["pipeline_id"] = spec.get("pipeline_id")
    template["pipeline_version"] = spec.get("version")
    template["current_state"] = "queued"
    template["state_history"] = [
        {
            "state": "queued",
            "entered_at": now_iso(),
            "actor": "system",
            "note": "Task initialized"
        }
    ]
    template["paths"] = paths
    template["audit_context"] = {
        "audit_status": "pending",
        "decision_log_path": f"outputs/{task_id}/audit/decision_log.jsonl",
        "approval_log_path": f"outputs/{task_id}/audit/approval_log.jsonl",
        "state_transition_log_path": f"outputs/{task_id}/audit/state_transitions.jsonl",
        "release_decision_path": f"outputs/{task_id}/audit/release_decision.json",
    }
    template["release_bundle_expected"] = spec.get("required_release_bundle", [])
    return template


def manifest_path_for(task_id: str) -> Path:
    spec = pipeline()
    task_root = build_task_paths(spec, task_id)["task_root"]
    return ROOT / task_root / "run_manifest.json"


def validate_task_mode(spec: dict[str, Any], task_mode: str) -> None:
    if task_mode not in spec.get("task_modes", {}):
        valid = ", ".join(sorted(spec.get("task_modes", {}).keys()))
        raise SystemExit(f"Unsupported task_mode '{task_mode}'. Valid modes: {valid}")


def cmd_init(args: argparse.Namespace) -> int:
    spec = pipeline()
    validate_task_mode(spec, args.task_mode)
    manifest = init_manifest(args.task_id, args.task_mode, args.title)
    manifest_path = manifest_path_for(args.task_id)

    for rel in manifest["paths"].values():
        (ROOT / rel).mkdir(parents=True, exist_ok=True)

    write_json(manifest_path, manifest)
    write_state_transition_event(
        manifest,
        args.task_id,
        "<init>",
        "queued",
        "init",
        "system",
        "Task manifest initialized",
        manifest_path,
    )
    print(f"Initialized task manifest: {manifest_path}")
    print(f"Current state: {manifest['current_state']}")
    print(f"Allowed next states: {', '.join(allowed_next_states(spec, manifest['current_state']))}")
    return 0


def load_existing_manifest(task_id: str) -> tuple[Path, dict[str, Any]]:
    path = manifest_path_for(task_id)
    if not path.exists():
        raise SystemExit(f"Task manifest not found: {path}")
    return path, load_json(path)


def cmd_inspect(args: argparse.Namespace) -> int:
    spec = pipeline()
    _, manifest = load_existing_manifest(args.task_id)
    state = manifest.get("current_state", "queued")
    print(json.dumps({
        "task_id": manifest.get("task_id"),
        "task_mode": manifest.get("task_mode"),
        "current_state": state,
        "allowed_next_states": allowed_next_states(spec, state),
        "paths": manifest.get("paths", {}),
    }, indent=2, ensure_ascii=True))
    return 0


def append_state_history(manifest: dict[str, Any], next_state: str, actor: str, note: str) -> None:
    manifest.setdefault("state_history", []).append({
        "state": next_state,
        "entered_at": now_iso(),
        "actor": actor,
        "note": note,
    })


def allowed_transition(spec: dict[str, Any], current: str, next_state: str) -> dict[str, Any] | None:
    for item in transition_table(spec).get(current, []):
        if item["to"] == next_state:
            return item
    return None


def cmd_transition(args: argparse.Namespace) -> int:
    spec = pipeline()
    path, manifest = load_existing_manifest(args.task_id)
    current = manifest.get("current_state", "queued")
    transition = allowed_transition(spec, current, args.next_state)
    if not transition:
        allowed = ", ".join(allowed_next_states(spec, current)) or "<none>"
        raise SystemExit(
            f"Illegal transition for task {args.task_id}: {current} -> {args.next_state}. Allowed: {allowed}"
        )

    manifest["current_state"] = args.next_state
    manifest["last_stage"] = transition.get("stage")
    manifest.setdefault("last_transition", {})
    manifest["last_transition"] = {
        "from": current,
        "to": args.next_state,
        "stage": transition.get("stage"),
        "recorded_at": now_iso(),
        "actor": args.actor,
        "note": args.note,
    }
    append_state_history(manifest, args.next_state, args.actor, args.note)
    write_json(path, manifest)
    write_state_transition_event(
        manifest,
        args.task_id,
        current,
        args.next_state,
        transition.get("stage", "unknown"),
        args.actor,
        args.note,
        path,
    )

    print(f"Transition recorded: {current} -> {args.next_state}")
    print(f"Manifest updated: {path}")
    next_allowed = allowed_next_states(spec, args.next_state)
    if next_allowed:
        print(f"Next allowed states: {', '.join(next_allowed)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--task-id", required=True)
    init_parser.add_argument("--task-mode", default="clinical_db_analysis")
    init_parser.add_argument("--title", required=True)
    init_parser.set_defaults(func=cmd_init)

    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument("--task-id", required=True)
    inspect_parser.set_defaults(func=cmd_inspect)

    transition_parser = subparsers.add_parser("transition")
    transition_parser.add_argument("--task-id", required=True)
    transition_parser.add_argument("--next-state", required=True)
    transition_parser.add_argument("--actor", default="system")
    transition_parser.add_argument("--note", default="")
    transition_parser.set_defaults(func=cmd_transition)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
