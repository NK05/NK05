# Approved Vendor List and administration platform

**Focus:** Vendor onboarding · Evidence review · Permissions · Controlled public directory  
**Status:** Private client/platform development; implementation scope varies by module  
**Stack observed:** Django REST Framework, Python, Next.js, TypeScript, PostgreSQL

[← Back to profile](../README.md)

## The problem space

A vendor directory can look simple to visitors, but its administrative workflow must distinguish an application from a verified vendor and an internally approved vendor from one authorised for public display.

## My work

I have worked on the development of an Approved Vendor List (AVL) platform covering application capture, internal review, supporting evidence, approval decisions and controlled listing.

The underlying implementation separates administrative actions and permissions from the limited information intended for public viewing.

## Engineering focus

- Structured workflows rather than a single edit-and-publish switch
- Explicit review, activation and public listing boundaries
- Access control and protection of private supporting evidence
- A deliberately limited public-facing vendor representation

## What this demonstrates

**Workflow design → state transitions → permission boundaries → privacy-conscious publishing.**

This is a bounded account of software work, not proof of a production certification service, a live marketplace/payment system or independent security accreditation. Client identities, vendor information, private documents, commercial rules and code remain private.

Any future demonstration will use fictional companies and an approved scope.
