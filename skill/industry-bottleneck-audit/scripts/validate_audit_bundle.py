#!/usr/bin/env python3
"""Validate cross-reference and audit invariants for an audit-bundle JSON file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError:  # pragma: no cover - exercised only in an incomplete install
    Draft202012Validator = None
    SchemaError = Exception


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https?://")
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "audit-bundle.schema.json"
CURRENT_SCHEMA_VERSION = "1.0-draft.3"
LEGACY_SCHEMA_VERSIONS = {"1.0-draft", "1.0-draft.1", "1.0-draft.2"}
ROLE_SCHEMA_VERSIONS = {"1.0-draft.2", "1.0-draft.3"}
MODES = {"industry_first", "technology_first", "dynamic", "evidence_event"}
CLAIM_STATUS = {"anchored", "conditional", "speculative", "broken", "stale"}
PREDICTION_STATUS = {
    "registered",
    "not_due",
    "supported",
    "weakened",
    "falsified",
    "boundary_changed",
    "attribution_unresolved",
}
SCORE_KEYS = {"B_struct", "B_now", "P_joint", "P_own", "P_cycle", "P_now", "E"}
EMPTY_CUT_CLASSIFICATIONS = {"divergent_network", "non_cone_network", "unresolved"}


def _json_path(parts: Any) -> str:
    path = "$"
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"
    return path


@lru_cache(maxsize=1)
def _schema_validator() -> Any:
    if Draft202012Validator is None:
        return None
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _schema_errors(data: Any) -> list[str]:
    if Draft202012Validator is None:
        return [
            "schema: jsonschema is required for Full Audit validation; "
            "install skills/industry-bottleneck-audit/requirements.txt"
        ]
    try:
        validator = _schema_validator()
    except (OSError, json.JSONDecodeError, SchemaError) as exc:
        return [f"schema: unable to load a valid Draft 2020-12 schema: {exc}"]
    return [
        f"{_json_path(error.absolute_path)}: schema: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path))
    ]


def _required(obj: dict[str, Any], fields: list[str], path: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj:
            errors.append(f"{path}: missing required field '{field}'")


def _unique_ids(items: Any, key: str, path: str, errors: list[str]) -> set[str]:
    if not isinstance(items, list):
        errors.append(f"{path}: expected an array")
        return set()
    seen: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{path}[{index}]: expected an object")
            continue
        value = item.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}[{index}].{key}: expected a non-empty string")
            continue
        if value in seen:
            errors.append(f"{path}: duplicate {key} '{value}'")
        seen.add(value)
    return seen


def _check_refs(
    refs: Any,
    valid: set[str],
    path: str,
    errors: list[str],
    allow_empty: bool = True,
) -> None:
    if not isinstance(refs, list):
        errors.append(f"{path}: expected an array")
        return
    if not allow_empty and not refs:
        errors.append(f"{path}: must not be empty")
    for ref in refs:
        if not isinstance(ref, str) or not ref:
            errors.append(f"{path}: contains an invalid reference")
        elif ref not in valid:
            errors.append(f"{path}: unresolved reference '{ref}'")


def _check_date(value: Any, path: str, errors: list[str], nullable: bool = False) -> date | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        errors.append(f"{path}: expected YYYY-MM-DD")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{path}: invalid calendar date '{value}'")
        return None


def _check_score(value: Any, path: str, errors: list[str]) -> None:
    if value is None:
        return
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        # Match JSON Schema integer semantics: 2 and 2.0 are the same score.
        if not 0 <= value <= 5 or int(value) != value:
            errors.append(f"{path}: expected an integer from 0 to 5")
        return
    if not isinstance(value, dict):
        errors.append(f"{path}: expected an integer, tagged score, or null")
        return
    if not value.get("explanation", "").strip():
        errors.append(f"{path}.explanation: expected non-whitespace text")
    status = value.get("status")
    populated = {key for key in ("value", "lower", "upper") if key in value}
    if status == "point":
        if populated != {"value"}:
            errors.append(f"{path}: point score requires only 'value'")
    elif status == "range":
        if populated != {"lower", "upper"}:
            errors.append(f"{path}: range score requires only 'lower' and 'upper'")
        elif value["lower"] > value["upper"]:
            errors.append(f"{path}: range lower cannot exceed upper")
    elif status in {"unknown", "not_applicable"}:
        if populated:
            errors.append(f"{path}: {status} score cannot contain numeric fields")


def _hypothesis_ids(items: Any, errors: list[str]) -> tuple[set[str], set[tuple[str, int]]]:
    if not isinstance(items, list):
        errors.append("hypotheses: expected an array")
        return set(), set()
    ids: set[str] = set()
    versions: set[tuple[str, int]] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"hypotheses[{index}]: expected an object")
            continue
        hypothesis_id = item.get("hypothesis_id")
        version = item.get("version")
        if not isinstance(hypothesis_id, str) or not hypothesis_id:
            errors.append(f"hypotheses[{index}].hypothesis_id: expected a non-empty string")
            continue
        ids.add(hypothesis_id)
        if isinstance(version, int) and not isinstance(version, bool):
            key = (hypothesis_id, version)
            if key in versions:
                errors.append(f"hypotheses: duplicate hypothesis version '{hypothesis_id}' v{version}")
            versions.add(key)
    return ids, versions


def validate_bundle(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    schema_errors = _schema_errors(data)
    if schema_errors:
        return schema_errors, warnings

    top_fields = [
        "schema_version",
        "audit_id",
        "mode",
        "title",
        "case",
        "structure",
        "nodes",
        "edges",
        "claims",
        "sources",
        "rights",
        "companies",
        "hypotheses",
        "events",
        "snapshots",
        "predictions",
        "views",
    ]
    if data.get("schema_version") == CURRENT_SCHEMA_VERSION:
        top_fields.extend(["adoption_paths", "topology_transitions"])
    _required(data, top_fields, "root", errors)
    if data.get("schema_version") in LEGACY_SCHEMA_VERSIONS:
        warnings.append(
            f"schema_version: '{data['schema_version']}' is accepted for migration; "
            f"new bundles should use '{CURRENT_SCHEMA_VERSION}'"
        )
    if data.get("mode") not in MODES:
        errors.append(f"mode: expected one of {sorted(MODES)}")

    case = data.get("case", {})
    if not isinstance(case, dict):
        errors.append("case: expected an object")
        case = {}
    _required(case, ["Y", "Q", "Omega", "as_of", "evidence_cutoff", "exclusions"], "case", errors)
    for field in ("Y", "Q", "Omega"):
        if not isinstance(case.get(field), str) or not case.get(field, "").strip():
            errors.append(f"case.{field}: expected a non-empty string")
    case_as_of = _check_date(case.get("as_of"), "case.as_of", errors)
    case_cutoff = _check_date(case.get("evidence_cutoff"), "case.evidence_cutoff", errors)
    if case_as_of and case_cutoff and case_cutoff > case_as_of:
        errors.append("case.evidence_cutoff: cannot be later than case.as_of")
    if not isinstance(case.get("exclusions"), list):
        errors.append("case.exclusions: expected an array")

    node_ids = _unique_ids(data.get("nodes", []), "node_id", "nodes", errors)
    source_ids = _unique_ids(data.get("sources", []), "source_id", "sources", errors)
    claim_ids = _unique_ids(data.get("claims", []), "claim_id", "claims", errors)
    right_ids = _unique_ids(data.get("rights", []), "right_id", "rights", errors)
    hypothesis_ids, hypothesis_versions = _hypothesis_ids(data.get("hypotheses", []), errors)
    prediction_ids = _unique_ids(data.get("predictions", []), "prediction_id", "predictions", errors)
    scale_balance_ids = _unique_ids(
        data.get("scale_balances", []), "scale_balance_id", "scale_balances", errors
    )
    _unique_ids(data.get("adoption_paths", []), "adoption_path_id", "adoption_paths", errors)
    _unique_ids(
        data.get("topology_transitions", []),
        "transition_id",
        "topology_transitions",
        errors,
    )
    _unique_ids(data.get("edges", []), "edge_id", "edges", errors)
    _unique_ids(data.get("companies", []), "company_id", "companies", errors)
    event_ids = _unique_ids(data.get("events", []), "event_id", "events", errors)
    snapshot_ids = _unique_ids(data.get("snapshots", []), "snapshot_id", "snapshots", errors)

    if not node_ids:
        errors.append("nodes: at least one node is required")
    if not claim_ids:
        errors.append("claims: at least one claim is required")

    source_dates: dict[str, tuple[date | None, date | None]] = {}
    for index, source in enumerate(data.get("sources", [])):
        if not isinstance(source, dict):
            continue
        path = f"sources[{index}]"
        _required(
            source,
            ["source_id", "title", "url", "source_type", "published_at", "accessed_at", "primary", "limitations"],
            path,
            errors,
        )
        if not isinstance(source.get("url"), str) or not URL_RE.match(source.get("url", "")):
            errors.append(f"{path}.url: expected an http(s) URL")
        published_at = _check_date(source.get("published_at"), f"{path}.published_at", errors, nullable=True)
        accessed_at = _check_date(source.get("accessed_at"), f"{path}.accessed_at", errors)
        if published_at and accessed_at and published_at > accessed_at:
            errors.append(f"{path}.published_at: cannot be later than accessed_at")
        source_id = source.get("source_id")
        if isinstance(source_id, str):
            source_dates[source_id] = (published_at, accessed_at)
        if not isinstance(source.get("primary"), bool):
            errors.append(f"{path}.primary: expected a boolean")
        if not isinstance(source.get("limitations"), str) or not source.get("limitations", "").strip():
            errors.append(f"{path}.limitations: expected a non-empty string")

    if source_ids and not any(s.get("primary") is True for s in data.get("sources", []) if isinstance(s, dict)):
        warnings.append("sources: no primary source is marked")

    claims_by_id = {
        item["claim_id"]: item
        for item in data.get("claims", [])
        if isinstance(item, dict) and isinstance(item.get("claim_id"), str)
    }
    hypotheses_by_version = {
        (item["hypothesis_id"], item["version"]): item
        for item in data.get("hypotheses", [])
        if isinstance(item, dict)
        and isinstance(item.get("hypothesis_id"), str)
        and isinstance(item.get("version"), int)
    }
    snapshots_by_id = {
        item["snapshot_id"]: item
        for item in data.get("snapshots", [])
        if isinstance(item, dict) and isinstance(item.get("snapshot_id"), str)
    }

    legacy_null_scores = False
    for index, node in enumerate(data.get("nodes", [])):
        if not isinstance(node, dict):
            continue
        path = f"nodes[{index}]"
        _required(
            node,
            ["node_id", "label", "function", "owner", "qualification", "effective_width_basis", "substitutes", "scores", "evidence_ids", "unknowns"],
            path,
            errors,
        )
        _check_refs(node.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
        if data.get("schema_version") in ROLE_SCHEMA_VERSIONS:
            role = node.get("constraint_role")
            if not isinstance(role, dict):
                errors.append(f"{path}.constraint_role: required for {CURRENT_SCHEMA_VERSION}")
            else:
                for field in (
                    "gate_mechanism", "release_condition", "leverage_mechanism",
                    "activation_dependency", "observable",
                ):
                    if not isinstance(role.get(field), str) or not role.get(field, "").strip():
                        errors.append(f"{path}.constraint_role.{field}: expected a non-whitespace string")
        substitutes = node.get("substitutes", [])
        if isinstance(substitutes, list):
            for ref in substitutes:
                if ref not in node_ids:
                    errors.append(f"{path}.substitutes: unresolved node '{ref}'")
        else:
            errors.append(f"{path}.substitutes: expected an array")
        scores = node.get("scores", {})
        if not isinstance(scores, dict):
            errors.append(f"{path}.scores: expected an object")
        else:
            missing = SCORE_KEYS.difference(scores)
            for key in sorted(missing):
                errors.append(f"{path}.scores: missing '{key}'")
            for key, value in scores.items():
                if key in SCORE_KEYS:
                    legacy_null_scores = legacy_null_scores or value is None
                    _check_score(value, f"{path}.scores.{key}", errors)

    for index, edge in enumerate(data.get("edges", [])):
        if not isinstance(edge, dict):
            continue
        path = f"edges[{index}]"
        _required(
            edge,
            ["edge_id", "from", "to", "transmitted_object", "mechanism", "status", "lag", "counterforces", "evidence_ids", "falsifier"],
            path,
            errors,
        )
        for field in ("from", "to"):
            if edge.get(field) not in node_ids:
                errors.append(f"{path}.{field}: unresolved node '{edge.get(field)}'")
        _check_refs(edge.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
        if not isinstance(edge.get("counterforces"), list):
            errors.append(f"{path}.counterforces: expected an array")
        if not isinstance(edge.get("falsifier"), str) or not edge.get("falsifier", "").strip():
            errors.append(f"{path}.falsifier: expected a non-empty string")

    for index, claim in enumerate(data.get("claims", [])):
        if not isinstance(claim, dict):
            continue
        path = f"claims[{index}]"
        _required(
            claim,
            ["claim_id", "plain_claim", "technical_claim", "status", "epistemic_type", "evidence_ids", "unknowns", "falsifier", "review_trigger"],
            path,
            errors,
        )
        if claim.get("status") not in CLAIM_STATUS:
            errors.append(f"{path}.status: invalid claim status")
        evidence_ids = claim.get("evidence_ids")
        _check_refs(evidence_ids, source_ids, f"{path}.evidence_ids", errors)
        if claim.get("epistemic_type") in {"fact", "mixed"} and not evidence_ids:
            errors.append(f"{path}.evidence_ids: fact or mixed claims require evidence")
        for field in ("plain_claim", "technical_claim", "falsifier", "review_trigger"):
            if not isinstance(claim.get(field), str) or not claim.get(field, "").strip():
                errors.append(f"{path}.{field}: expected a non-empty string")
        hypothesis_id = claim.get("hypothesis_id")
        hypothesis_version = claim.get("hypothesis_version")
        if (hypothesis_id is None) != (hypothesis_version is None):
            errors.append(f"{path}: hypothesis_id and hypothesis_version must be filled together")
        elif hypothesis_id is not None and (hypothesis_id, hypothesis_version) not in hypothesis_versions:
            errors.append(
                f"{path}: unresolved hypothesis version '{hypothesis_id}' v{hypothesis_version}"
            )

    structure = data.get("structure", {})
    if not isinstance(structure, dict):
        errors.append("structure: expected an object")
        structure = {}
    _required(structure, ["classification", "minimum_cut", "alternatives", "largest_unknowns"], "structure", errors)
    classification = structure.get("classification")
    _check_refs(
        structure.get("minimum_cut"),
        node_ids,
        "structure.minimum_cut",
        errors,
        allow_empty=classification in EMPTY_CUT_CLASSIFICATIONS,
    )
    _check_refs(structure.get("alternatives"), node_ids, "structure.alternatives", errors)
    if not isinstance(structure.get("largest_unknowns"), list) or not structure.get("largest_unknowns"):
        errors.append("structure.largest_unknowns: at least one unknown is required")

    for index, right in enumerate(data.get("rights", [])):
        if not isinstance(right, dict):
            continue
        path = f"rights[{index}]"
        _required(right, ["right_id", "right_type", "actor", "scope", "evidence_ids", "confidence"], path, errors)
        _check_refs(right.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
    if not data.get("rights"):
        warnings.append("rights: no definition, validation, modification, responsibility, or feedback rights recorded")

    for index, path_record in enumerate(data.get("adoption_paths", [])):
        if not isinstance(path_record, dict):
            continue
        path = f"adoption_paths[{index}]"
        _check_refs(
            path_record.get("delegated_right_ids"), right_ids,
            f"{path}.delegated_right_ids", errors,
        )
        _check_refs(
            path_record.get("retained_right_ids"), right_ids,
            f"{path}.retained_right_ids", errors,
        )
        _check_refs(
            path_record.get("evidence_ids"), source_ids,
            f"{path}.evidence_ids", errors,
        )
        for field in (
            "initiating_actor", "old_function_holder", "required_context",
            "integration_burden", "observable", "falsifier",
        ):
            if not isinstance(path_record.get(field), str) or not path_record.get(field, "").strip():
                errors.append(f"{path}.{field}: expected a non-whitespace string")

    for index, transition in enumerate(data.get("topology_transitions", [])):
        if not isinstance(transition, dict):
            continue
        path = f"topology_transitions[{index}]"
        _check_refs(
            transition.get("affected_node_ids"),
            node_ids,
            f"{path}.affected_node_ids",
            errors,
        )
        _check_refs(
            transition.get("evidence_ids"),
            source_ids,
            f"{path}.evidence_ids",
            errors,
        )
        _check_refs(
            transition.get("claim_ids"),
            claim_ids,
            f"{path}.claim_ids",
            errors,
            allow_empty=False,
        )
        before_snapshot_id = transition.get("before_snapshot_id")
        after_snapshot_id = transition.get("after_snapshot_id")
        event_id = transition.get("event_id")
        if before_snapshot_id not in snapshot_ids:
            errors.append(f"{path}.before_snapshot_id: unresolved snapshot '{before_snapshot_id}'")
        if after_snapshot_id is not None and after_snapshot_id not in snapshot_ids:
            errors.append(f"{path}.after_snapshot_id: unresolved snapshot '{after_snapshot_id}'")
        if event_id is not None and event_id not in event_ids:
            errors.append(f"{path}.event_id: unresolved event '{event_id}'")
        transition_as_of = _check_date(transition.get("as_of"), f"{path}.as_of", errors)
        for field in (
            "event_anchor",
            "shared_interface_or_state",
            "viability_change",
            "falsifier",
            "review_trigger",
        ):
            if not isinstance(transition.get(field), str) or not transition.get(field, "").strip():
                errors.append(f"{path}.{field}: expected a non-whitespace string")
        observables = transition.get("observables")
        if not isinstance(observables, list) or not observables:
            errors.append(f"{path}.observables: at least one observable is required")
        elif any(not isinstance(item, str) or not item.strip() for item in observables):
            errors.append(f"{path}.observables: expected non-whitespace strings")
        if transition.get("status") == "observed" and not transition.get("evidence_ids"):
            errors.append(f"{path}.evidence_ids: observed transitions require evidence")
        if transition.get("status") == "observed" and not transition.get("affected_node_ids"):
            errors.append(f"{path}.affected_node_ids: observed transitions require affected nodes")
        if transition.get("status") == "observed" and after_snapshot_id is None:
            errors.append(f"{path}.after_snapshot_id: observed transitions require an after snapshot")
        if transition.get("status") == "no_change":
            if transition.get("from_classification") != transition.get("to_classification"):
                errors.append(f"{path}: no_change must retain the prior classification")
            if transition.get("transition_stage") != "none":
                errors.append(f"{path}: no_change must use transition_stage 'none'")
        if transition.get("transition_stage") == "convergence_candidate" and transition.get("status") in {
            "observed", "no_change",
        }:
            errors.append(f"{path}: a convergence candidate is not an observed or no-change transition")
        if transition.get("transition_stage") in {"observed_cluster", "qualified_cluster"} and transition.get("status") != "observed":
            errors.append(f"{path}: an observed or qualified cluster requires status 'observed'")

        if after_snapshot_id in snapshot_ids:
            after_snapshot = snapshots_by_id[after_snapshot_id]
            after_as_of = _check_date(after_snapshot.get("as_of"), f"{path}.after_snapshot.as_of", [])
            after_cutoff = _check_date(
                after_snapshot.get("evidence_cutoff"),
                f"{path}.after_snapshot.evidence_cutoff",
                [],
            )
            before_snapshot = snapshots_by_id.get(before_snapshot_id)
            before_as_of = (
                _check_date(before_snapshot.get("as_of"), f"{path}.before_snapshot.as_of", [])
                if before_snapshot is not None else None
            )
            before_cutoff = (
                _check_date(
                    before_snapshot.get("evidence_cutoff"),
                    f"{path}.before_snapshot.evidence_cutoff",
                    [],
                )
                if before_snapshot is not None else None
            )
            if before_snapshot_id == after_snapshot_id:
                errors.append(f"{path}: before and after snapshots must be distinct")
            if before_as_of and after_as_of and before_as_of > after_as_of:
                errors.append(f"{path}: before snapshot cannot be later than after snapshot")
            if before_cutoff and after_cutoff and before_cutoff > after_cutoff:
                errors.append(f"{path}: before snapshot cutoff cannot be later than after snapshot cutoff")
            if transition_as_of and before_as_of and transition_as_of < before_as_of:
                errors.append(f"{path}.as_of: cannot be earlier than the before snapshot")
            if transition_as_of and after_as_of and transition_as_of > after_as_of:
                errors.append(f"{path}.as_of: cannot be later than the after snapshot")

            transition_claim_ids = set(transition.get("claim_ids", []))
            snapshot_claim_ids = set(after_snapshot.get("claim_ids", []))
            omitted_claim_ids = transition_claim_ids.difference(snapshot_claim_ids)
            for claim_id in sorted(omitted_claim_ids):
                errors.append(
                    f"{path}.claim_ids: claim '{claim_id}' must be listed in after snapshot "
                    f"'{after_snapshot_id}'"
                )

            evidence_paths = {
                source_id: f"{transition['transition_id']} -> {source_id}"
                for source_id in transition.get("evidence_ids", [])
            }
            for claim_id in transition_claim_ids:
                claim = claims_by_id.get(claim_id)
                if claim is None:
                    continue
                for source_id in claim.get("evidence_ids", []):
                    evidence_paths.setdefault(
                        source_id,
                        f"{transition['transition_id']} -> {claim_id} -> {source_id}",
                    )
                hypothesis_key = (claim.get("hypothesis_id"), claim.get("hypothesis_version"))
                hypothesis = hypotheses_by_version.get(hypothesis_key)
                if hypothesis is not None:
                    for source_id in hypothesis.get("evidence_ids", []):
                        evidence_paths.setdefault(
                            source_id,
                            f"{transition['transition_id']} -> {claim_id} -> "
                            f"{hypothesis_key[0]} v{hypothesis_key[1]} -> {source_id}",
                        )
            for source_id, dependency in sorted(evidence_paths.items()):
                published_at = source_dates.get(source_id, (None, None))[0]
                if published_at and after_cutoff and published_at > after_cutoff:
                    errors.append(
                        f"{path}.evidence_ids: source '{source_id}' was published after "
                        f"after snapshot '{after_snapshot_id}' cutoff; dependency: {dependency}"
                    )
                elif published_at is None and source_id in source_dates:
                    warnings.append(
                        f"{path}.evidence_ids: source '{source_id}' has unknown publication date; "
                        f"cutoff consistency cannot be verified; dependency: {dependency}"
                    )

    for index, company in enumerate(data.get("companies", [])):
        if not isinstance(company, dict):
            continue
        path = f"companies[{index}]"
        _required(
            company,
            ["company_id", "name", "segment_department", "node_ids", "mapping_label", "right_ids", "commercial_lever", "customer_counterpower", "scores", "segment_materiality", "evidence_ids", "falsifier", "review_trigger"],
            path,
            errors,
        )
        _check_refs(company.get("node_ids"), node_ids, f"{path}.node_ids", errors, allow_empty=False)
        _check_refs(company.get("right_ids"), right_ids, f"{path}.right_ids", errors)
        _check_refs(company.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
        if company.get("mapping_label") not in {"strong_match", "partial_match", "coalition", "no_clean_match"}:
            errors.append(f"{path}.mapping_label: invalid company mapping label")
        scores = company.get("scores", {})
        company_score_keys = {"P_joint", "P_own", "P_cycle", "P_now"}
        if not isinstance(scores, dict):
            errors.append(f"{path}.scores: expected an object")
        else:
            for key in sorted(company_score_keys.difference(scores)):
                errors.append(f"{path}.scores: missing '{key}'")
            for key in company_score_keys.intersection(scores):
                legacy_null_scores = legacy_null_scores or scores[key] is None
                _check_score(scores[key], f"{path}.scores.{key}", errors)

    if legacy_null_scores:
        warnings.append(
            "scores: null is accepted only for legacy migration; use a tagged "
            "unknown or not_applicable score with an explanation in new bundles"
        )

    for index, hypothesis in enumerate(data.get("hypotheses", [])):
        if not isinstance(hypothesis, dict):
            continue
        path = f"hypotheses[{index}]"
        _required(
            hypothesis,
            ["hypothesis_id", "version", "boundary", "baseline_date", "mechanism", "status", "trigger_event", "expected_observable", "prediction_window", "falsifier", "escape_conditions", "successor_constraint", "rights_shift", "evidence_ids", "next_review_trigger"],
            path,
            errors,
        )
        _check_date(hypothesis.get("baseline_date"), f"{path}.baseline_date", errors)
        _check_refs(hypothesis.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
        if not isinstance(hypothesis.get("version"), int) or isinstance(hypothesis.get("version"), bool) or hypothesis.get("version", 0) < 1:
            errors.append(f"{path}.version: expected a positive integer")

    for index, event in enumerate(data.get("events", [])):
        if not isinstance(event, dict):
            continue
        path = f"events[{index}]"
        _required(
            event,
            ["event_id", "source_ids", "published_at", "effective_at", "observed_at", "prior_hypothesis_id", "prior_hypothesis_version", "direct_fact", "update_target", "update_relation", "revised_hypothesis_version", "observed_change_now", "expected_prediction_ids", "counterforces", "next_verification_at", "rebuild_required"],
            path,
            errors,
        )
        _check_refs(event.get("source_ids"), source_ids, f"{path}.source_ids", errors, allow_empty=False)
        _check_refs(event.get("expected_prediction_ids"), prediction_ids, f"{path}.expected_prediction_ids", errors)
        _check_date(event.get("published_at"), f"{path}.published_at", errors)
        _check_date(event.get("effective_at"), f"{path}.effective_at", errors, nullable=True)
        _check_date(event.get("observed_at"), f"{path}.observed_at", errors)
        _check_date(event.get("next_verification_at"), f"{path}.next_verification_at", errors, nullable=True)
        prior_key = (event.get("prior_hypothesis_id"), event.get("prior_hypothesis_version"))
        revised_key = (event.get("prior_hypothesis_id"), event.get("revised_hypothesis_version"))
        if prior_key not in hypothesis_versions:
            errors.append(
                f"{path}: unresolved prior hypothesis version '{prior_key[0]}' v{prior_key[1]}"
            )
        if revised_key not in hypothesis_versions:
            errors.append(
                f"{path}: unresolved revised hypothesis version '{revised_key[0]}' v{revised_key[1]}"
            )
        if event.get("update_relation") == "no_change":
            if event.get("revised_hypothesis_version") != event.get("prior_hypothesis_version"):
                errors.append(f"{path}: no_change must retain the prior hypothesis version")
        elif isinstance(event.get("revised_hypothesis_version"), int) and isinstance(
            event.get("prior_hypothesis_version"), int
        ):
            if event["revised_hypothesis_version"] <= event["prior_hypothesis_version"]:
                errors.append(f"{path}: a changed hypothesis must use a later version")

    # Use the exact version cited by a claim, never the latest hypothesis.
    for index, snapshot in enumerate(data.get("snapshots", [])):
        if not isinstance(snapshot, dict):
            continue
        path = f"snapshots[{index}]"
        _required(snapshot, ["snapshot_id", "as_of", "evidence_cutoff", "system_boundary", "node_ids", "claim_ids", "evidence_ids", "review_note"], path, errors)
        snapshot_as_of = _check_date(snapshot.get("as_of"), f"{path}.as_of", errors)
        snapshot_cutoff = _check_date(snapshot.get("evidence_cutoff"), f"{path}.evidence_cutoff", errors)
        if snapshot_as_of and snapshot_cutoff and snapshot_cutoff > snapshot_as_of:
            errors.append(f"{path}.evidence_cutoff: cannot be later than as_of")
        _check_refs(snapshot.get("node_ids"), node_ids, f"{path}.node_ids", errors, allow_empty=False)
        _check_refs(snapshot.get("claim_ids"), claim_ids, f"{path}.claim_ids", errors, allow_empty=False)
        _check_refs(snapshot.get("evidence_ids"), source_ids, f"{path}.evidence_ids", errors)
        snapshot_id = snapshot["snapshot_id"]
        evidence_paths = {
            source_id: f"{snapshot_id} -> {source_id}"
            for source_id in snapshot.get("evidence_ids", [])
        }
        listed_claims = set(snapshot.get("claim_ids", []))
        listed_nodes = set(snapshot.get("node_ids", []))
        for claim in data.get("claims", []):
            if isinstance(claim, dict) and claim.get("claim_id") in listed_claims:
                claim_id = claim["claim_id"]
                for source_id in claim.get("evidence_ids", []):
                    evidence_paths.setdefault(source_id, f"{snapshot_id} -> {claim_id} -> {source_id}")
                hypothesis_key = (claim.get("hypothesis_id"), claim.get("hypothesis_version"))
                hypothesis = hypotheses_by_version.get(hypothesis_key)
                if hypothesis is not None:
                    for source_id in hypothesis.get("evidence_ids", []):
                        evidence_paths.setdefault(
                            source_id,
                            f"{snapshot_id} -> {claim_id} -> "
                            f"{hypothesis_key[0]} v{hypothesis_key[1]} -> {source_id}",
                        )
        for node in data.get("nodes", []):
            if isinstance(node, dict) and node.get("node_id") in listed_nodes:
                for source_id in node.get("evidence_ids", []):
                    evidence_paths.setdefault(
                        source_id, f"{snapshot_id} -> {node['node_id']} -> {source_id}"
                    )
        if snapshot_cutoff:
            for source_id in sorted(evidence_paths):
                published_at = source_dates.get(source_id, (None, None))[0]
                if published_at and published_at > snapshot_cutoff:
                    errors.append(
                        f"{path}.evidence_ids: source '{source_id}' was published after the snapshot cutoff; "
                        f"dependency: {evidence_paths[source_id]}"
                    )
                elif published_at is None and source_id in source_dates:
                    warnings.append(
                        f"{path}.evidence_ids: source '{source_id}' has unknown publication date; "
                        f"cutoff consistency cannot be verified; dependency: {evidence_paths[source_id]}"
                    )
    if not data.get("snapshots"):
        errors.append("snapshots: at least one snapshot is required")

    for index, prediction in enumerate(data.get("predictions", [])):
        if not isinstance(prediction, dict):
            continue
        path = f"predictions[{index}]"
        _required(
            prediction,
            ["prediction_id", "claim_id", "expected_change", "horizon", "observable", "counterforce", "invalidating_result", "status"],
            path,
            errors,
        )
        if prediction.get("claim_id") not in claim_ids:
            errors.append(f"{path}.claim_id: unresolved claim '{prediction.get('claim_id')}'")
        if prediction.get("status") not in PREDICTION_STATUS:
            errors.append(f"{path}.status: invalid prediction status")
    if not data.get("predictions"):
        warnings.append("predictions: no dated causal response test is registered")

    for index, balance in enumerate(data.get("scale_balances", [])):
        if not isinstance(balance, dict):
            continue
        path = f"scale_balances[{index}]"
        if balance.get("node_id") not in node_ids:
            errors.append(f"{path}.node_id: unresolved node '{balance.get('node_id')}'")
        for field in ("before_snapshot_id", "after_snapshot_id"):
            ref = balance.get(field)
            if ref is not None and ref not in snapshot_ids:
                errors.append(f"{path}.{field}: unresolved snapshot '{ref}'")
        for field in (
            "qualified_volume", "unit_labor", "total_labor_or_headcount",
            "role_and_wage_mix", "organization_or_site_count", "unit_cost",
            "total_spend_or_revenue", "queue_or_service_level",
            "released_capacity_destination", "rebound_or_induced_demand",
        ):
            observation = balance.get(field, {})
            if isinstance(observation, dict):
                _check_refs(
                    observation.get("evidence_ids"), source_ids,
                    f"{path}.{field}.evidence_ids", errors,
                )
    if data.get("mode") in {"dynamic", "technology_first", "evidence_event"} and not scale_balance_ids:
        errors.append(
            "scale_balances: dynamic, technology-first, and evidence-event audits "
            "must record a scale balance; use explicit unknown observations when "
            "comparable output or labor data are unavailable"
        )

    views = data.get("views", {})
    if not isinstance(views, dict):
        errors.append("views: expected an object")
        views = {}
    _required(views, ["technical_claim_ids", "nontechnical_claim_ids", "low_impact_control"], "views", errors)
    _check_refs(views.get("technical_claim_ids"), claim_ids, "views.technical_claim_ids", errors, allow_empty=False)
    _check_refs(views.get("nontechnical_claim_ids"), claim_ids, "views.nontechnical_claim_ids", errors, allow_empty=False)
    if data.get("mode") == "technology_first" and not views.get("low_impact_control"):
        errors.append("views.low_impact_control: required for technology_first mode")

    return errors, warnings


def _self_test() -> int:
    valid = {
        "schema_version": CURRENT_SCHEMA_VERSION,
        "audit_id": "self-test",
        "mode": "industry_first",
        "title": "Self test",
        "case": {
            "Y": "qualified output",
            "Q": "transferred function",
            "Omega": "test boundary",
            "as_of": "2026-10-29",
            "evidence_cutoff": "2026-10-29",
            "exclusions": [],
        },
        "structure": {
            "classification": "unresolved",
            "minimum_cut": ["N1"],
            "alternatives": [],
            "largest_unknowns": ["unknown"],
        },
        "nodes": [
            {
                "node_id": "N1",
                "label": "Node",
                "function": "Function",
                "owner": "Actor",
                "qualification": "Acceptance",
                "effective_width_basis": "Qualified paths",
                "substitutes": [],
                "constraint_role": {
                    "gate_level": "unknown",
                    "gate_mechanism": "The test does not establish a pass or reject effect",
                    "release_condition": "Evidence identifies the release condition",
                    "leverage_level": "unknown",
                    "leverage_mechanism": "The test does not establish downstream amplification",
                    "activation_dependency": "Unknown complementary activation",
                    "observable": "Qualified flow changes after the node changes",
                },
                "scores": {key: None for key in SCORE_KEYS},
                "evidence_ids": ["S1"],
                "unknowns": [],
            }
        ],
        "edges": [],
        "claims": [
            {
                "claim_id": "C1",
                "plain_claim": "Plain claim",
                "technical_claim": "Technical claim",
                "status": "anchored",
                "epistemic_type": "fact",
                "evidence_ids": ["S1"],
                "unknowns": [],
                "falsifier": "Invalidating observation",
                "review_trigger": "Review event",
            }
        ],
        "sources": [
            {
                "source_id": "S1",
                "title": "Source",
                "url": "https://example.com/source",
                "source_type": "official",
                "published_at": "2026-10-29",
                "accessed_at": "2026-10-29",
                "primary": True,
                "limitations": "Self-test source",
            }
        ],
        "rights": [],
        "companies": [],
        "hypotheses": [],
        "events": [],
        "snapshots": [
            {
                "snapshot_id": "SN1",
                "as_of": "2026-10-29",
                "evidence_cutoff": "2026-10-29",
                "system_boundary": "test boundary",
                "node_ids": ["N1"],
                "claim_ids": ["C1"],
                "evidence_ids": ["S1"],
                "review_note": "Initial self-test snapshot",
            }
        ],
        "predictions": [],
        "adoption_paths": [],
        "topology_transitions": [],
        "views": {
            "technical_claim_ids": ["C1"],
            "nontechnical_claim_ids": ["C1"],
            "low_impact_control": None,
        },
    }
    errors, _ = validate_bundle(valid)
    if errors:
        print("SELF-TEST FAILED: valid fixture rejected", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    invalid = json.loads(json.dumps(valid))
    invalid["claims"][0]["evidence_ids"] = ["MISSING"]
    invalid_errors, _ = validate_bundle(invalid)
    if not any("unresolved reference 'MISSING'" in error for error in invalid_errors):
        print("SELF-TEST FAILED: unresolved source was not rejected", file=sys.stderr)
        return 1
    non_cone = json.loads(json.dumps(valid))
    non_cone["structure"]["classification"] = "non_cone_network"
    non_cone["structure"]["minimum_cut"] = []
    non_cone_errors, _ = validate_bundle(non_cone)
    if non_cone_errors:
        print("SELF-TEST FAILED: non-cone empty cut was rejected", file=sys.stderr)
        return 1
    bad_class = json.loads(json.dumps(valid))
    bad_class["structure"]["classification"] = "bananas"
    bad_class_errors, _ = validate_bundle(bad_class)
    if not bad_class_errors:
        print("SELF-TEST FAILED: unknown classification was accepted", file=sys.stderr)
        return 1
    print(
        "Self-test passed: schema, semantic references, and honest empty-cut outcomes behaved as expected."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Audit bundle JSON files")
    parser.add_argument("--self-test", action="store_true", help="Run built-in validation tests")
    args = parser.parse_args()

    if args.self_test:
        return _self_test()
    if not args.paths:
        parser.error("provide at least one bundle path or --self-test")

    failed = False
    for path in args.paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL {path}: {exc}")
            failed = True
            continue
        errors, warnings = validate_bundle(data)
        for warning in warnings:
            print(f"WARN {path}: {warning}")
        if errors:
            failed = True
            print(f"FAIL {path}: {len(errors)} error(s)")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}: {len(warnings)} warning(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
