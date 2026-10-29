# Microsoft 365 IT Operations & Automation Lab

**Portfolio status: reproducible offline lab + tenant-connected read-only export script.**
Designed for an IT Administrator / Digital Solutions application. No access to an employer tenant or production deployment is claimed.

## Demonstrable work

- A read-only Microsoft Graph PowerShell script that can export Entra user status, assigned license IDs and last recorded successful sign-in (subject to tenant authorization and licensing).
- A standard-library Python reporting pipeline that validates records, detects stale enabled accounts and disabled accounts retaining license assignments, and exports review records and a JSON summary.
- Eight isolated automated tests and a reproducible six-user **fictional** dataset.
- Power BI data model/measures and an implementable Power Automate review notification flow specification.

## Run locally

Prerequisites: Python 3.10+; no packages or cloud account required for offline demonstration.

```bash
python portfolio/it-operations-automation/audit.py --input portfolio/it-operations-automation/sample/users.csv --output-dir /tmp/m365-lab-output --as-of 2026-10-29 --inactive-days 90
python -m unittest discover -s portfolio/it-operations-automation/tests -v
```

Expected output: `user_review.csv` and `summary.json`. These are designed for import into Power BI or a governed workflow.

## Optional authorized tenant export

From PowerShell 7, install appropriate Microsoft Graph Authentication and Users modules, then run `scripts/export_m365_users.ps1` from this directory. This opens an interactive sign-in and requests delegated read scopes; it never changes user accounts. Access to `signInActivity` additionally depends on Microsoft Entra P1/P2 licensing, AuditLog.Read.All, and suitable directory role/consent. Missing sign-in evidence is flagged for verification, not declared proof a person never signed in.

**Security:** Real exports contain personal and organizational information. Save only to approved local/secured storage; NEVER commit tenant output. There are no tokens, credentials or access keys in this project.

## Honest scope

This lab demonstrates automation code, operational reporting, security-conscious data handling and understanding of Microsoft 365 reporting. It does **not** by itself demonstrate real-world administration of Exchange Online, Teams, SharePoint, OneDrive or Power Platform production environments. Those must be validated in an authorized tenant.

Sources: [Microsoft Graph user listing](https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0), [Power Automate ALM](https://learn.microsoft.com/en-us/power-platform/alm/overview-alm).
