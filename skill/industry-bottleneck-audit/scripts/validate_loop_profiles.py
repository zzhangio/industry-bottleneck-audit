#!/usr/bin/env python3
"""Validate LCI profiles in a CSV and recompute their display indices."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


PROFILE_FIELDS = (("local_profile", "local_lci"), ("parent_profile", "parent_lci"))


def parse_profile(raw: str) -> list[int] | None:
    value = raw.strip()
    if not value or value.upper() in {"NA", "N/A"}:
        return None
    scores = [int(part) for part in value.split("/")]
    if len(scores) != 8 or any(score < 1 or score > 5 for score in scores):
        raise ValueError(f"expected eight slash-separated scores from 1 to 5, got {raw!r}")
    return scores


def loop_index(scores: list[int]) -> int:
    return round(100 * math.exp(sum(math.log(score / 5) for score in scores) / 8))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    with args.csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"case_id", *(field for pair in PROFILE_FIELDS for field in pair)}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"missing columns: {', '.join(sorted(missing))}")

        rows = list(reader)

    for line_no, row in enumerate(rows, start=2):
        case_id = row.get("case_id") or f"line-{line_no}"
        for profile_field, index_field in PROFILE_FIELDS:
            try:
                scores = parse_profile(row.get(profile_field, ""))
            except (ValueError, TypeError) as exc:
                errors.append(f"{case_id} {profile_field}: {exc}")
                continue
            expected_raw = (row.get(index_field) or "").strip()
            if scores is None:
                if expected_raw and expected_raw.upper() not in {"NA", "N/A"}:
                    errors.append(f"{case_id} {index_field}: expected blank/NA for missing profile")
                continue
            calculated = loop_index(scores)
            if expected_raw != str(calculated):
                errors.append(
                    f"{case_id} {index_field}: stored {expected_raw!r}, calculated {calculated}"
                )

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(rows)} loop-profile rows validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
