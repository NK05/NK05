"""Read-only, dependency-free audit of Microsoft 365-style user inventory exports.

All supplied sample records are fictional. This module NEVER connects to a tenant.
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date, datetime
from pathlib import Path

REQUIRED = (
    "user_id", "display_name", "user_principal_name",
    "account_enabled", "last_successful_sign_in", "assigned_licenses",
)
REPORT_FIELDS = (
    "user_id", "display_name", "user_principal_name", "account_enabled",
    "last_successful_sign_in", "days_since_sign_in",
    "assigned_license_count", "review_status", "review_reason",
)


def parse_sign_in(value: str) -> date | None:
    if not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"Invalid sign-in timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError("Sign-in timestamps must include a timezone.")
    return parsed.date()


def load_inventory(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not set(REQUIRED).issubset(reader.fieldnames):
            raise ValueError("Missing required columns: " + ", ".join(REQUIRED))
        rows = list(reader)
    return rows


def audit_inventory(
    users: list[dict[str, str]], as_of: date, inactive_days: int = 90
) -> tuple[list[dict[str, object]], dict[str, int | str]]:
    if inactive_days < 1:
        raise ValueError("inactive_days must be positive")
    seen: set[str] = set()
    report: list[dict[str, object]] = []
    for user in users:
        uid = user["user_id"].strip()
        if not uid or uid in seen:
            raise ValueError("Missing or duplicate user ID")
        seen.add(uid)
        enabled_text = user["account_enabled"].strip().lower()
        if enabled_text not in ("true", "false"):
            raise ValueError(f"Invalid account_enabled for {uid}")
        enabled = enabled_text == "true"
        last = parse_sign_in(user["last_successful_sign_in"])
        if last is not None and last > as_of:
            raise ValueError(f"Future sign-in date for {uid}")
        licenses = [x.strip() for x in user["assigned_licenses"].split(";") if x.strip()]
        days = (as_of - last).days if last is not None else None

        # Review flags are indicators, not findings of a security breach.
        if not enabled and licenses:
            status, reason = "review", "Disabled account retains license assignment"
        elif enabled and last is None:
            status, reason = "review", "No successful sign-in recorded; verify data coverage"
        elif enabled and days is not None and days >= inactive_days:
            status, reason = "review", "Enabled account exceeds inactivity threshold"
        else:
            status, reason = "monitor", "No threshold-based review flag"

        report.append({
            "user_id": uid,
            "display_name": user["display_name"].strip(),
            "user_principal_name": user["user_principal_name"].strip(),
            "account_enabled": enabled,
            "last_successful_sign_in": user["last_successful_sign_in"].strip(),
            "days_since_sign_in": days if days is not None else "",
            "assigned_license_count": len(licenses),
            "review_status": status,
            "review_reason": reason,
        })
    summary: dict[str, int | str] = {
        "as_of": as_of.isoformat(),
        "total_users": len(report),
        "enabled_users": sum(row["account_enabled"] is True for row in report),
        "disabled_users": sum(row["account_enabled"] is False for row in report),
        "users_for_review": sum(row["review_status"] == "review" for row in report),
        "assigned_license_instances": sum(int(row["assigned_license_count"]) for row in report),
        "inactive_threshold_days": inactive_days,
    }
    return report, summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Microsoft 365 inventory triage")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--as-of", type=date.fromisoformat, required=True)
    parser.add_argument("--inactive-days", type=int, default=90)
    args = parser.parse_args()
    report, summary = audit_inventory(
        load_inventory(args.input), args.as_of, args.inactive_days
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / "user_review.csv").open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.DictWriter(stream, fieldnames=REPORT_FIELDS)
        writer.writeheader()
        writer.writerows(report)
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
