#!/usr/bin/env python3
"""Create a v0.12-derived audit bundle without rewriting the historical source file."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


SCORE_KEYS = {"B_struct", "B_now", "P_joint", "P_own", "P_cycle", "P_now", "E"}
SOURCE_TYPE_MAP = {
    "research_lab": "company",
    "product_demo": "company",
    "vendor_support": "company",
    "vendor_case": "company",
    "manufacturer": "company",
    "issuer_release": "company",
    "issuer_filing": "company",
    "standards_body": "official",
}
VALID_CLASSIFICATIONS = {
    "direct_cone", "feedback_cone", "institutional_cone", "emergent_cluster_cone",
    "conditional_cone", "cyclical_narrowness", "hidden_cone", "divergent_network",
    "non_cone_network", "unresolved",
}


def unknown_score() -> dict[str, Any]:
    return {
        "status": "unknown",
        "explanation": "Historical bundle did not establish this ordinal score.",
    }


def unknown_observation() -> dict[str, Any]:
    return {
        "status": "unknown",
        "value": "Not measured in the historical evaluation",
        "basis": "Migration preserves the original evidence boundary and does not invent a denominator",
        "evidence_ids": [],
    }


def default_role() -> dict[str, Any]:
    return {
        "gate_level": "unknown",
        "gate_mechanism": "Historical evaluation did not separately encode the pass or reject mechanism",
        "release_condition": "Requires a new bounded audit rather than migration-time inference",
        "leverage_level": "unknown",
        "leverage_mechanism": "Historical evaluation did not separately encode downstream amplification",
        "activation_dependency": "Unknown in the preserved historical evidence set",
        "observable": "Qualified flow response after a bounded change in this node",
    }


def migrate(data: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(data)
    result["schema_version"] = "1.0-draft.3"
    result.setdefault("adoption_paths", [])
    result.setdefault("topology_transitions", [])

    structure = result.get("structure", {})
    classification = structure.get("classification")
    if classification not in VALID_CLASSIFICATIONS:
        original = str(classification)
        structure["classification"] = (
            "non_cone_network" if original.startswith("non_cone_network") else "unresolved"
        )
        structure.setdefault("largest_unknowns", []).append(
            f"Migrated composite classification preserved verbatim: {original}"
        )

    for source in result.get("sources", []):
        source_type = source.get("source_type")
        if source_type not in {"official", "regulatory", "company", "paper", "market_data", "industry", "media", "other"}:
            source["source_type"] = SOURCE_TYPE_MAP.get(source_type, "other")
            limitation = source.get("limitations", "")
            source["limitations"] = (
                f"{limitation} Migrated source_type from '{source_type}'."
            ).strip()

    for node in result.get("nodes", []):
        node.setdefault("constraint_role", default_role())
        for key in SCORE_KEYS:
            if node.get("scores", {}).get(key) is None:
                node["scores"][key] = unknown_score()
    for company in result.get("companies", []):
        for key in ("P_joint", "P_own", "P_cycle", "P_now"):
            if company.get("scores", {}).get(key) is None:
                company["scores"][key] = unknown_score()

    if result.get("mode") in {"dynamic", "technology_first", "evidence_event"} and not result.get("scale_balances"):
        snapshot_ids = [item.get("snapshot_id") for item in result.get("snapshots", [])]
        node_ids = [item.get("node_id") for item in result.get("nodes", [])]
        observation_fields = (
            "qualified_volume", "unit_labor", "total_labor_or_headcount", "role_and_wage_mix",
            "organization_or_site_count", "unit_cost", "total_spend_or_revenue",
            "queue_or_service_level", "released_capacity_destination", "rebound_or_induced_demand",
        )
        balance = {
            "scale_balance_id": "SB-MIGRATION-1",
            "node_id": node_ids[0],
            "before_snapshot_id": snapshot_ids[-1],
            "after_snapshot_id": None,
            "boundary_and_unit": "Historical evaluation boundary; comparable scale denominator was not recorded",
            "classification": ["unresolved"],
            "comparability_notes": "Added as explicit unknowns during v0.12 migration; no historical scale conclusion was inferred",
            "unknowns": ["Comparable before/after output, labor, cost, and queue data"],
        }
        for field in observation_fields:
            balance[field] = unknown_observation()
        result["scale_balances"] = [balance]

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.target.resolve():
        parser.error("target must differ from the preserved source")
    if args.target.exists():
        parser.error("target already exists; migration never overwrites an artifact")
    data = json.loads(args.source.read_text(encoding="utf-8"))
    migrated = migrate(data)
    args.target.parent.mkdir(parents=True, exist_ok=True)
    args.target.write_text(json.dumps(migrated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
