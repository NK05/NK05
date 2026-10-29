# Power Automate workflow: IT access-review notifications

**Status: implementable design, not an imported or executed cloud flow.**
A Microsoft 365/Power Platform development tenant and appropriate permissions are required before stating practical Power Automate deployment experience.

## Business problem

Operational reports are often delivered but never actioned. Route flagged accounts to an accountable reviewer without automatically changing permissions or licenses.

## Proposed flow (SharePoint list -> Power Automate -> Teams/Outlook)

1. Create a SharePoint list **ITAccessReviews** with fields: `ReviewKey` (unique ID), `UserId`, `Reason`, `Status` (Open / Investigating / Resolved / Exception), `Owner`, `DueDate`, `LastNotified`.
2. With explicit administrator approval, import only **review** rows from `user_review.csv` into the list; use `ReviewKey` to deduplicate daily imports. Keep UPN and other identifiable fields out of broad notification messages.
3. Cloud flow trigger: **When an item is created or modified** (SharePoint).
4. Condition: only notify on `Status = Open` with an assigned owner. Guard against repeated notifications by checking `LastNotified` and item version/notification state.
5. Send a targeted Teams message or Outlook email to the owner containing the item link and reason category, not raw export contents.
6. Update `LastNotified` only after the delivery action succeeds; record error branch and alert administrator on repeated failures.
7. Scheduled secondary flow: escalate overdue unresolved reviews to the designated manager, respecting working calendars and notification limits.
8. Resolve only after a human-reviewed outcome; never disable accounts, reset passwords, or revoke access automatically.

## Acceptance checks

- New flagged record with owner produces one notification.
- Updating an unrelated item field does not flood the owner.
- Missing owner routes to a controlled exception queue.
- Connector failure preserves record for later retry.
- Re-processing the same `ReviewKey` does not create duplicates.
- Reviewer access is scoped to least privilege.
- All notifications avoid employee details beyond an approved minimum.

## Deployment evidence still needed

An authenticated development tenant, actual screenshots or export of a solution-managed cloud flow, successful test-run history, and a recorded owner-approved demo. An untested blueprint is not proof of production Power Platform administration.

Microsoft ALM guidance: https://learn.microsoft.com/en-us/power-platform/alm/overview-alm
