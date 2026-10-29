"""Deterministic tests; no credentials or tenant are required."""
from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit import audit_inventory, load_inventory, parse_sign_in


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 10, 29)
        self.user = {
            "user_id": "demo-01", "display_name": "Demo User",
            "user_principal_name": "demo@example.invalid",
            "account_enabled": "true",
            "last_successful_sign_in": "2026-10-20T09:00:00Z",
            "assigned_licenses": "SKU-A",
        }

    def test_recent_sign_in_needs_no_review(self):
        report, summary = audit_inventory([self.user], self.today)
        self.assertEqual(report[0]["review_status"], "monitor")
        self.assertEqual(summary["users_for_review"], 0)

    def test_inactive_enabled_account_needs_review(self):
        user = dict(self.user, last_successful_sign_in="2026-01-02T00:00:00Z")
        report, _ = audit_inventory([user], self.today)
        self.assertIn("inactivity", report[0]["review_reason"])

    def test_disabled_account_with_license_needs_review(self):
        user = dict(self.user, account_enabled="false")
        report, _ = audit_inventory([user], self.today)
        self.assertIn("retains license", report[0]["review_reason"])

    def test_no_signin_is_not_called_never_signed_in(self):
        user = dict(self.user, last_successful_sign_in="")
        report, _ = audit_inventory([user], self.today)
        self.assertIn("data coverage", report[0]["review_reason"])

    def test_duplicate_ids_rejected(self):
        with self.assertRaises(ValueError):
            audit_inventory([self.user, self.user], self.today)

    def test_invalid_boolean_rejected(self):
        user = dict(self.user, account_enabled="sometimes")
        with self.assertRaises(ValueError):
            audit_inventory([user], self.today)

    def test_timestamp_requires_timezone(self):
        with self.assertRaises(ValueError):
            parse_sign_in("2026-10-20T09:00:00")

    def test_sample_inventory_schema(self):
        rows = load_inventory(Path(__file__).resolve().parents[1] / "sample" / "users.csv")
        report, summary = audit_inventory(rows, self.today)
        self.assertEqual(len(report), 6)
        self.assertEqual(summary["total_users"], 6)


if __name__ == "__main__":
    unittest.main()
