# Power BI reporting model: user-access inventory

**Status:** model specification and DAX examples. The CSV pipeline is runnable; no .pbix file or published Power BI service report is claimed.

Import the output `user_review.csv` as table **UserReview** in Power BI Desktop.
Set `account_enabled` to True/False, `assigned_license_count` and `days_since_sign_in` to whole number. The output deliberately includes no MFA claims.

## Measures

```dax
Users = COUNTROWS(UserReview)

Enabled Users =
CALCULATE(COUNTROWS(UserReview), UserReview[account_enabled] = TRUE())

Users Requiring Review =
CALCULATE(COUNTROWS(UserReview), UserReview[review_status] = "review")

Review Rate =
DIVIDE([Users Requiring Review], [Users], 0)

License Assignments =
SUM(UserReview[assigned_license_count])
```

Suggested visuals: KPI cards for user count/review count, segmented bar for review reason, table for users requiring review, and filter for account enabled. This is **license assignment counts, not license seat utilisation**.

Use organization-approved storage and apply row-level security where relevant. Do not publish actual employee UPNs or access findings to a public workspace.

## Reproducibility

The synthetic dataset uses `example.invalid` email domains. No credentials, customer records, tenant exports, or actual security incidents are included.
