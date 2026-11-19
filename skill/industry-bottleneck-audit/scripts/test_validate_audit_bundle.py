#!/usr/bin/env python3
"""Regression tests for the audit bundle schema and semantic validator."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_audit_bundle import validate_bundle  # noqa: E402


class AuditBundleValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads((ROOT / "examples" / "minimal-audit-bundle.json").read_text(encoding="utf-8"))
        cls.non_cone = json.loads(
            (ROOT / "examples" / "minimal-non-cone-bundle.json").read_text(encoding="utf-8")
        )
        cls.unresolved = json.loads(
            (ROOT / "examples" / "minimal-unresolved-bundle.json").read_text(encoding="utf-8")
        )

    def errors(self, bundle: dict) -> list[str]:
        return validate_bundle(bundle)[0]

    def assert_error_contains(self, bundle: dict, fragment: str) -> None:
        errors = self.errors(bundle)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_fixtures(self) -> None:
        for bundle in (self.base, self.non_cone, self.unresolved):
            with self.subTest(audit_id=bundle["audit_id"]):
                self.assertEqual(self.errors(copy.deepcopy(bundle)), [])

    def test_draft3_requires_roles_adoption_paths_and_topology_transitions(self) -> None:
        missing_role = copy.deepcopy(self.base)
        del missing_role["nodes"][0]["constraint_role"]
        self.assert_error_contains(missing_role, "constraint_role")

        missing_paths = copy.deepcopy(self.base)
        del missing_paths["adoption_paths"]
        self.assert_error_contains(missing_paths, "adoption_paths")

        missing_transitions = copy.deepcopy(self.base)
        del missing_transitions["topology_transitions"]
        self.assert_error_contains(missing_transitions, "topology_transitions")

    def test_draft2_remains_migration_compatible(self) -> None:
        legacy = copy.deepcopy(self.base)
        legacy["schema_version"] = "1.0-draft.2"
        legacy.pop("topology_transitions")
        errors, warnings = validate_bundle(legacy)
        self.assertEqual(errors, [])
        self.assertTrue(any("accepted for migration" in warning for warning in warnings))

    def test_draft1_remains_migration_compatible(self) -> None:
        legacy = copy.deepcopy(self.base)
        legacy["schema_version"] = "1.0-draft.1"
        legacy.pop("adoption_paths")
        for node in legacy["nodes"]:
            node.pop("constraint_role")
        errors, warnings = validate_bundle(legacy)
        self.assertEqual(errors, [])
        self.assertTrue(any("accepted for migration" in warning for warning in warnings))

    def test_constraint_role_enum_is_enforced(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["nodes"][0]["constraint_role"]["gate_level"] = "absolute"
        self.assert_error_contains(bundle, "schema")

    def test_adoption_path_right_and_source_references(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["adoption_paths"] = [{
            "adoption_path_id": "AP1",
            "capability_scope": "task",
            "adoption_position": "beneath",
            "initiating_actor": "Qualified provider operator",
            "old_function_holder": "Human operator",
            "required_context": "Contract specification and operating state",
            "delegated_right_ids": [],
            "retained_right_ids": ["R1"],
            "jurisdiction_shift": "partial",
            "integration_burden": "Operator supervision and customer acceptance remain required",
            "evidence_ids": ["S1"],
            "observable": "Routine execution moves while customer acceptance remains human",
            "falsifier": "The system receives final acceptance authority or is not used in the workflow"
        }]
        self.assertEqual(self.errors(bundle), [])
        broken = copy.deepcopy(bundle)
        broken["adoption_paths"][0]["retained_right_ids"] = ["MISSING"]
        self.assert_error_contains(broken, "unresolved reference 'MISSING'")

    def test_topology_transition_references_and_observed_evidence(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["topology_transitions"] = [{
            "transition_id": "TT1",
            "as_of": "2026-10-29",
            "before_snapshot_id": "SNAP1",
            "after_snapshot_id": None,
            "event_id": None,
            "claim_ids": ["C1"],
            "from_classification": "divergent_network",
            "to_classification": "emergent_cluster_cone",
            "transition_stage": "convergence_candidate",
            "status": "conditional",
            "event_anchor": "A shared representation becomes reusable across implementations",
            "mechanisms": ["complement_activation", "interface_convergence"],
            "affected_node_ids": ["N1"],
            "shared_interface_or_state": "Reusable task representation and acceptance path",
            "viability_change": "Previously bespoke paths can share engineering work",
            "observables": ["Cross-path onboarding time falls"],
            "counterforces": ["Deployment-specific calibration remains bespoke"],
            "falsifier": "Transfer loss and qualification burden do not improve",
            "evidence_ids": [],
            "review_trigger": "Two independent deployments report comparable reuse"
        }]
        self.assertEqual(self.errors(bundle), [])

        broken_node = copy.deepcopy(bundle)
        broken_node["topology_transitions"][0]["affected_node_ids"] = ["MISSING"]
        self.assert_error_contains(broken_node, "unresolved reference 'MISSING'")

        observed_without_evidence = copy.deepcopy(bundle)
        observed_without_evidence["topology_transitions"][0]["status"] = "observed"
        observed_without_evidence["topology_transitions"][0]["transition_stage"] = "observed_cluster"
        observed_without_evidence["topology_transitions"][0]["after_snapshot_id"] = "SNAP1"
        self.assert_error_contains(observed_without_evidence, "observed transitions require evidence")

    def test_topology_transition_outcomes_are_distinct(self) -> None:
        candidate = copy.deepcopy(self.base)
        transition = {
            "transition_id": "TT1",
            "as_of": "2026-10-29",
            "before_snapshot_id": "SNAP1",
            "after_snapshot_id": None,
            "event_id": None,
            "claim_ids": ["C1"],
            "from_classification": "non_cone_network",
            "to_classification": "emergent_cluster_cone",
            "transition_stage": "convergence_candidate",
            "status": "conditional",
            "event_anchor": "A reusable interface may connect fragmented paths",
            "mechanisms": ["interface_convergence"],
            "affected_node_ids": ["N1"],
            "shared_interface_or_state": "Candidate shared interface",
            "viability_change": "Cross-path reuse becomes plausible",
            "observables": ["Two independent paths reuse the interface"],
            "counterforces": [],
            "falsifier": "Reuse remains bespoke",
            "evidence_ids": [],
            "review_trigger": "Independent deployment evidence"
        }
        candidate["topology_transitions"] = [transition]
        self.assertEqual(self.errors(candidate), [])

        no_change = copy.deepcopy(candidate)
        no_change["topology_transitions"][0].update(
            from_classification="non_cone_network",
            to_classification="non_cone_network",
            transition_stage="none",
            status="no_change",
        )
        self.assertEqual(self.errors(no_change), [])
        contradictory = copy.deepcopy(no_change)
        contradictory["topology_transitions"][0]["to_classification"] = "emergent_cluster_cone"
        self.assert_error_contains(contradictory, "no_change must retain")

        formed = copy.deepcopy(candidate)
        after_snapshot = copy.deepcopy(formed["snapshots"][0])
        after_snapshot["snapshot_id"] = "SNAP2"
        after_snapshot["review_note"] = "Same-day post-event state recorded separately"
        formed["snapshots"].append(after_snapshot)
        formed["topology_transitions"][0].update(
            transition_stage="qualified_cluster",
            status="observed",
            after_snapshot_id="SNAP2",
            evidence_ids=["S1"],
        )
        self.assertEqual(self.errors(formed), [])

    def test_topology_transition_snapshot_cutoff(self) -> None:
        bundle = self.with_future_source()
        after_snapshot = copy.deepcopy(bundle["snapshots"][0])
        after_snapshot["snapshot_id"] = "SNAP2"
        after_snapshot["review_note"] = "Post-event snapshot"
        bundle["snapshots"].append(after_snapshot)
        bundle["topology_transitions"] = [{
            "transition_id": "TT1",
            "as_of": "2026-10-29",
            "before_snapshot_id": "SNAP1",
            "after_snapshot_id": "SNAP2",
            "event_id": None,
            "claim_ids": ["C1"],
            "from_classification": "unresolved",
            "to_classification": "emergent_cluster_cone",
            "transition_stage": "observed_cluster",
            "status": "observed",
            "event_anchor": "Later evidence",
            "mechanisms": ["interface_convergence"],
            "affected_node_ids": ["N1"],
            "shared_interface_or_state": "Observed shared interface",
            "viability_change": "Paths now reuse one interface",
            "observables": ["Repeated independent adoption"],
            "counterforces": [],
            "falsifier": "No independent reuse",
            "evidence_ids": ["FUTURE"],
            "review_trigger": "Qualification evidence"
        }]
        self.assert_error_contains(bundle, "published after after snapshot")

    def test_topology_transition_traces_claim_and_hypothesis_evidence(self) -> None:
        bundle = self.with_future_source()
        later_claim = copy.deepcopy(bundle["claims"][0])
        later_claim.update(claim_id="C2", evidence_ids=["FUTURE"])
        bundle["claims"].append(later_claim)
        after_snapshot = copy.deepcopy(bundle["snapshots"][0])
        after_snapshot.update(snapshot_id="SNAP2", claim_ids=["C1"], review_note="Post-event snapshot")
        bundle["snapshots"].append(after_snapshot)
        bundle["topology_transitions"] = [{
            "transition_id": "TT1", "as_of": "2026-10-29",
            "before_snapshot_id": "SNAP1", "after_snapshot_id": "SNAP2",
            "event_id": None, "claim_ids": ["C2"],
            "from_classification": "unresolved", "to_classification": "conditional_cone",
            "transition_stage": "none", "status": "observed",
            "event_anchor": "Synthetic event", "mechanisms": ["qualification_change"],
            "affected_node_ids": ["N1"], "shared_interface_or_state": "No shared interface",
            "viability_change": "Qualification changed", "observables": ["Qualified flow changes"],
            "counterforces": [], "falsifier": "No qualification change", "evidence_ids": ["S1"],
            "review_trigger": "New qualification data"
        }]
        self.assert_error_contains(bundle, "must be listed in after snapshot")
        bundle["snapshots"][1]["claim_ids"].append("C2")
        self.assert_error_contains(bundle, "TT1 -> C2 -> FUTURE")

    def test_topology_transition_unknown_direct_date_warns(self) -> None:
        bundle = copy.deepcopy(self.base)
        unknown_source = copy.deepcopy(bundle["sources"][0])
        unknown_source.update(source_id="UNKNOWN_DATE", published_at=None)
        bundle["sources"].append(unknown_source)
        after_snapshot = copy.deepcopy(bundle["snapshots"][0])
        after_snapshot.update(snapshot_id="SNAP2", review_note="Post-event snapshot")
        bundle["snapshots"].append(after_snapshot)
        bundle["topology_transitions"] = [{
            "transition_id": "TT1", "as_of": "2026-10-29",
            "before_snapshot_id": "SNAP1", "after_snapshot_id": "SNAP2",
            "event_id": None, "claim_ids": ["C1"],
            "from_classification": "unresolved", "to_classification": "conditional_cone",
            "transition_stage": "none", "status": "observed",
            "event_anchor": "Synthetic event", "mechanisms": ["qualification_change"],
            "affected_node_ids": ["N1"], "shared_interface_or_state": "No shared interface",
            "viability_change": "Qualification changed", "observables": ["Qualified flow changes"],
            "counterforces": [], "falsifier": "No qualification change",
            "evidence_ids": ["UNKNOWN_DATE"], "review_trigger": "Source date verified"
        }]
        errors, warnings = validate_bundle(bundle)
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown publication date" in warning and "TT1" in warning for warning in warnings))

    def test_topology_transition_snapshot_order_and_invalid_dates(self) -> None:
        bundle = copy.deepcopy(self.base)
        before = copy.deepcopy(bundle["snapshots"][0])
        before.update(snapshot_id="LATE", as_of="2027-01-01", evidence_cutoff="2027-01-01")
        bundle["snapshots"].append(before)
        bundle["topology_transitions"] = [{
            "transition_id": "TT1", "as_of": "2026-10-29",
            "before_snapshot_id": "LATE", "after_snapshot_id": "SNAP1",
            "event_id": None, "claim_ids": ["C1"],
            "from_classification": "unresolved", "to_classification": "conditional_cone",
            "transition_stage": "none", "status": "observed",
            "event_anchor": "Synthetic event", "mechanisms": ["qualification_change"],
            "affected_node_ids": ["N1"], "shared_interface_or_state": "No shared interface",
            "viability_change": "Qualification changed", "observables": ["Qualified flow changes"],
            "counterforces": [], "falsifier": "No qualification change", "evidence_ids": ["S1"],
            "review_trigger": "New qualification data"
        }]
        self.assert_error_contains(bundle, "before snapshot cannot be later")

        same_snapshot = copy.deepcopy(bundle)
        same_snapshot["topology_transitions"][0].update(
            before_snapshot_id="SNAP1", after_snapshot_id="SNAP1"
        )
        self.assert_error_contains(same_snapshot, "must be distinct")

        invalid_date = copy.deepcopy(bundle)
        invalid_date["snapshots"][0]["as_of"] = "2026-02-30"
        self.assert_error_contains(invalid_date, "invalid calendar date")

    def test_unknown_classification_rejected(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["structure"]["classification"] = "bananas"
        self.assert_error_contains(bundle, "schema")

    def test_extra_property_rejected(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["garbage"] = True
        self.assert_error_contains(bundle, "Additional properties")

    def test_binding_class_requires_cut(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["structure"]["minimum_cut"] = []
        self.assert_error_contains(bundle, "must not be empty")

    def test_claim_hypothesis_reference_must_exist(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["claims"][0]["hypothesis_id"] = "NONEXISTENT"
        bundle["claims"][0]["hypothesis_version"] = 999
        self.assert_error_contains(bundle, "unresolved hypothesis version")

    def test_claim_hypothesis_pair_must_be_complete(self) -> None:
        bundle = copy.deepcopy(self.base)
        del bundle["claims"][0]["hypothesis_version"]
        self.assert_error_contains(bundle, "hypothesis_version")

    def test_event_versions_and_future_review_date(self) -> None:
        bundle = copy.deepcopy(self.base)
        revised = copy.deepcopy(bundle["hypotheses"][0])
        revised["version"] = 2
        revised["status"] = "supported"
        bundle["hypotheses"].append(revised)
        bundle["events"].append(
            {
                "event_id": "EV1",
                "source_ids": ["S1"],
                "published_at": "2026-10-20",
                "effective_at": None,
                "observed_at": "2026-10-29",
                "prior_hypothesis_id": "H1",
                "prior_hypothesis_version": 1,
                "direct_fact": "Synthetic update",
                "update_target": "H1 mechanism",
                "update_relation": "strengthens",
                "revised_hypothesis_version": 2,
                "observed_change_now": "Evidence strengthened without a boundary change",
                "expected_prediction_ids": ["P1"],
                "counterforces": [],
                "next_verification_at": "2027-04-30",
                "rebuild_required": False
            }
        )
        self.assertEqual(self.errors(bundle), [])
        broken = copy.deepcopy(bundle)
        broken["events"][0]["prior_hypothesis_version"] = 999
        self.assert_error_contains(broken, "unresolved prior hypothesis version")

    def test_no_change_retains_version(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["events"].append(
            {
                "event_id": "EV1",
                "source_ids": ["S1"],
                "published_at": "2026-10-20",
                "effective_at": None,
                "observed_at": "2026-10-29",
                "prior_hypothesis_id": "H1",
                "prior_hypothesis_version": 1,
                "direct_fact": "No structural change",
                "update_target": "H1 mechanism",
                "update_relation": "no_change",
                "revised_hypothesis_version": 1,
                "observed_change_now": "None",
                "expected_prediction_ids": [],
                "counterforces": [],
                "next_verification_at": None,
                "rebuild_required": False
            }
        )
        self.assertEqual(self.errors(bundle), [])

    def test_calendar_dates(self) -> None:
        valid = copy.deepcopy(self.base)
        valid["sources"][0]["published_at"] = "2024-02-29"
        self.assertEqual(self.errors(valid), [])
        invalid = copy.deepcopy(self.base)
        invalid["sources"][0]["published_at"] = "2025-02-29"
        self.assert_error_contains(invalid, "invalid calendar date")
        invalid_month = copy.deepcopy(self.base)
        invalid_month["sources"][0]["published_at"] = "2026-99-99"
        self.assert_error_contains(invalid_month, "invalid calendar date")

    def test_duplicate_reference_rejected(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["claims"][0]["evidence_ids"] = ["S1", "S1"]
        self.assert_error_contains(bundle, "non-unique elements")

    def test_changed_event_requires_a_revised_version(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["events"].append(
            {
                "event_id": "EV1",
                "source_ids": ["S1"],
                "published_at": "2026-10-20",
                "effective_at": None,
                "observed_at": "2026-10-29",
                "prior_hypothesis_id": "H1",
                "prior_hypothesis_version": 1,
                "direct_fact": "Synthetic change",
                "update_target": "H1 mechanism",
                "update_relation": "strengthens",
                "revised_hypothesis_version": None,
                "observed_change_now": "Evidence strengthened",
                "expected_prediction_ids": [],
                "counterforces": [],
                "next_verification_at": None,
                "rebuild_required": False,
            }
        )
        self.assert_error_contains(bundle, "revised_hypothesis_version")

    def test_snapshot_rejects_future_evidence_but_allows_late_access(self) -> None:
        future = copy.deepcopy(self.base)
        future["sources"][0]["published_at"] = "2099-01-01"
        future["sources"][0]["accessed_at"] = "2099-01-02"
        self.assert_error_contains(future, "published after the snapshot cutoff")
        late_access = copy.deepcopy(self.base)
        late_access["sources"][0]["accessed_at"] = "2027-01-01"
        self.assertEqual(self.errors(late_access), [])

    def test_source_cannot_be_published_after_access(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["sources"][0]["published_at"] = "2026-10-30"
        self.assert_error_contains(bundle, "cannot be later than accessed_at")

    def test_score_representation(self) -> None:
        tagged = copy.deepcopy(self.base)
        tagged["nodes"][0]["scores"]["B_struct"] = {
            "status": "range",
            "lower": 1,
            "upper": 2,
            "explanation": "Boundary-sensitive estimate"
        }
        self.assertEqual(self.errors(tagged), [])
        pseudo_precision = copy.deepcopy(self.base)
        pseudo_precision["nodes"][0]["scores"]["B_struct"] = 2.37
        self.assert_error_contains(pseudo_precision, "schema")
        reversed_range = copy.deepcopy(tagged)
        reversed_range["nodes"][0]["scores"]["B_struct"]["lower"] = 3
        self.assert_error_contains(reversed_range, "range lower cannot exceed upper")


    def with_future_source(self) -> dict:
        bundle = copy.deepcopy(self.base)
        source = copy.deepcopy(bundle["sources"][0])
        source.update(source_id="FUTURE", published_at="2027-01-01", accessed_at="2027-01-02")
        bundle["sources"].append(source)
        return bundle

    def test_future_prediction_without_evidence_is_allowed(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["hypotheses"][0].update(status="registered", evidence_ids=[], prediction_window="By 2027-01-01")
        bundle["claims"][0].update(status="speculative", epistemic_type="inference", evidence_ids=[])
        bundle["predictions"][0].update(status="not_due", horizon="By 2027-01-01")
        self.assertEqual(validate_bundle(bundle), ([], []))

    def test_attribution_unresolved_prediction_status_is_allowed(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["predictions"][0]["status"] = "attribution_unresolved"
        self.assertEqual(self.errors(bundle), [])

    def test_snapshot_rejects_indirect_future_hypothesis_evidence(self) -> None:
        bundle = self.with_future_source()
        bundle["hypotheses"][0]["evidence_ids"] = ["FUTURE"]
        self.assert_error_contains(bundle, "published after the snapshot cutoff")
        self.assert_error_contains(bundle, "SNAP1 -> C1 -> H1 v1 -> FUTURE")

    def test_unreferenced_future_source_is_allowed(self) -> None:
        self.assertEqual(validate_bundle(self.with_future_source()), ([], []))

    def test_new_hypothesis_version_does_not_rewrite_old_snapshot(self) -> None:
        bundle = self.with_future_source()
        revised = copy.deepcopy(bundle["hypotheses"][0])
        revised.update(version=2, evidence_ids=["FUTURE"], baseline_date="2027-01-02")
        # Newest first guards against implementations that index by ID alone.
        bundle["hypotheses"].insert(0, revised)
        bundle["events"].append({
            "event_id": "EV2", "source_ids": ["FUTURE"],
            "published_at": "2027-01-01", "effective_at": None, "observed_at": "2027-01-02",
            "prior_hypothesis_id": "H1", "prior_hypothesis_version": 1,
            "direct_fact": "Later synthetic verification", "update_target": "H1",
            "update_relation": "strengthens", "revised_hypothesis_version": 2,
            "observed_change_now": "New evidence", "expected_prediction_ids": ["P1"],
            "counterforces": [], "next_verification_at": None, "rebuild_required": False,
        })
        self.assertEqual(validate_bundle(bundle), ([], []))
        later_claim = copy.deepcopy(bundle["claims"][0])
        later_claim.update(claim_id="C2", hypothesis_version=2)
        bundle["claims"].append(later_claim)
        # A new claim is not automatically part of the sealed old snapshot.
        self.assertEqual(validate_bundle(bundle), ([], []))
        later_snapshot = copy.deepcopy(bundle["snapshots"][0])
        later_snapshot.update(snapshot_id="SNAP2", as_of="2027-01-02",
                              evidence_cutoff="2027-01-01", claim_ids=["C2"])
        bundle["snapshots"].append(later_snapshot)
        self.assertEqual(validate_bundle(bundle), ([], []))
        bundle["snapshots"][0]["claim_ids"].append("C2")
        self.assert_error_contains(bundle, "SNAP1 -> C2 -> H1 v2 -> FUTURE")

    def test_unknown_indirect_publication_date_warns(self) -> None:
        bundle = self.with_future_source()
        bundle["sources"][-1]["published_at"] = None
        bundle["hypotheses"][0]["evidence_ids"] = ["FUTURE"]
        errors, warnings = validate_bundle(bundle)
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown publication date" in warning and
                            "SNAP1 -> C1 -> H1 v1 -> FUTURE" in warning for warning in warnings))

    def test_indirect_evidence_on_cutoff_is_allowed(self) -> None:
        bundle = self.with_future_source()
        bundle["sources"][-1]["published_at"] = "2026-10-29"
        bundle["hypotheses"][0]["evidence_ids"] = ["FUTURE"]
        self.assertEqual(validate_bundle(bundle), ([], []))

    def test_scores_reject_whitespace_explanations(self) -> None:
        for collection, score in (("nodes", "B_struct"), ("companies", "P_own")):
            for status, numeric in (("point", {"value": 2}), ("range", {"lower": 1, "upper": 2}),
                                    ("unknown", {}), ("not_applicable", {})):
                with self.subTest(collection=collection, status=status):
                    bundle = copy.deepcopy(self.base)
                    bundle[collection][0]["scores"][score] = {
                        "status": status, "explanation": " \t\n", **numeric,
                    }
                    self.assert_error_contains(bundle, "non-whitespace")

    def test_integer_valued_scores_are_consistent(self) -> None:
        for score in (2.0, {"status": "point", "value": 2.0, "explanation": "Ordinal"},
                      {"status": "range", "lower": 1.0, "upper": 2.0, "explanation": "Interval"}):
            with self.subTest(score=score):
                bundle = copy.deepcopy(self.base)
                bundle["nodes"][0]["scores"]["B_struct"] = score
                self.assertEqual(self.errors(bundle), [])
        for score in (True, 2.37, {"status": "point", "value": 2.37, "explanation": "Invalid"}):
            with self.subTest(score=score):
                bundle = copy.deepcopy(self.base)
                bundle["nodes"][0]["scores"]["B_struct"] = score
                self.assert_error_contains(bundle, "schema")

    def test_dynamic_mode_requires_scale_balance(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["mode"] = "dynamic"
        self.assert_error_contains(bundle, "must record a scale balance")

    def test_scale_balance_references_and_unknowns(self) -> None:
        bundle = copy.deepcopy(self.base)
        bundle["mode"] = "dynamic"
        unknown = {
            "status": "unknown",
            "value": "Not publicly measured",
            "basis": "No comparable denominator located",
            "evidence_ids": [],
        }
        bundle["scale_balances"] = [{
            "scale_balance_id": "SB1",
            "node_id": "N1",
            "before_snapshot_id": "SNAP1",
            "after_snapshot_id": None,
            "boundary_and_unit": "Qualified output inside the frozen case",
            "qualified_volume": copy.deepcopy(unknown),
            "unit_labor": copy.deepcopy(unknown),
            "total_labor_or_headcount": copy.deepcopy(unknown),
            "role_and_wage_mix": copy.deepcopy(unknown),
            "organization_or_site_count": copy.deepcopy(unknown),
            "unit_cost": copy.deepcopy(unknown),
            "total_spend_or_revenue": copy.deepcopy(unknown),
            "queue_or_service_level": copy.deepcopy(unknown),
            "released_capacity_destination": copy.deepcopy(unknown),
            "rebound_or_induced_demand": copy.deepcopy(unknown),
            "classification": ["unresolved"],
            "comparability_notes": "Baseline only; later snapshot not yet due",
            "unknowns": ["Later comparable snapshot"],
        }]
        self.assertEqual(self.errors(bundle), [])
        broken = copy.deepcopy(bundle)
        broken["scale_balances"][0]["node_id"] = "MISSING"
        self.assert_error_contains(broken, "unresolved node")

if __name__ == "__main__":
    unittest.main()
