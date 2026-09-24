# Non-functional branches

One entry per branch of Part 2, in interview order: later answers are invalid if an earlier one changes. Each entry gives what to **decide** and the **default** to recommend for a small product (tens to a few thousand users). Defaults are recommendations, never assumptions.

## Making a requirement testable

"Secure" and "fast" are not requirements. Write each one as a **quality attribute scenario** with six parts: _source_, _stimulus_, _environment_, _artifact_, _response_, _response measure_ (a metric plus a threshold).

> An authenticated client (source) requests another owner's resource id (stimulus) in normal operation (environment) against the API (artifact). The API answers as if the id did not exist and reads none of that owner's data (response). The authorization test suite shows zero cross-owner reads (measure).

An OWASP ASVS requirement is already a testable "Verify that…" statement: cite its versioned id (`v5.0.0-6.3.3`) instead of writing a scenario for it. Target level and scope of review: ASVS chapters V2 (validation and business logic), V4 (API), V6 (authentication), V7 (sessions), V8 (authorization), V9 (self-contained tokens), V11 (cryptography), V12 (secure communication), V13 (configuration), V14 (data protection), V16 (logging and errors).

## 1. Context and threat actors

- **Decide:** users, expected load, jurisdictions, and who must fail to read the data: another user, whoever holds a database dump, a database admin, the app operator, a cloud admin.
- **Default:** protect against other users and a database-only compromise. Accept, in writing, that someone who can change and deploy the app can read everything.

## 2. Data classification (blocks every branch below)

- **Decide:** a class for every kind of data in the spec (credentials, session secrets, financial or health values, free text, identifiers, operational metadata), and per class its confidentiality, integrity, retention, deletion, log rule, and backup fate.
- **Default:** credentials and secrets never stored reversibly; the domain's sensitive values confidential; free-text labels stated explicitly as confidential or not, with the reason.

## 3. Tenancy and authorization

- **Decide:** the ownership unit from the spec, how every object access is checked, and what a foreign id returns.
- **Default:** every access is checked against the authenticated subject, identity comes only from the validated credential, and a foreign id is indistinguishable from a missing one. The same rule binds every channel (web, agents, jobs).

## 4. Authentication

- **Decide:** app-owned passwords or an identity provider; MFA or a written waiver; password policy; email verification; account recovery.
- **Default:** follow NIST SP 800-63B-4. Passwords of at least 15 characters when they are the only factor (8 when part of MFA), no composition rules, no forced rotation, a breached-password blocklist, a memory-hard salted hash. Throttle guessing without permanent lockout. Registration and recovery never reveal whether an email exists. ASVS Level 2 expects MFA: adopt it or waive it in writing.

## 5. Sessions and tokens

- **Decide:** token lifetimes, where each token lives in the client, rotation, revocation, and what logout and password change revoke.
- **Default:** a short-lived access token held in memory; a refresh token in an `HttpOnly`, `Secure`, `SameSite` cookie with a narrow path; rotation on every use; reuse detection that revokes the whole token family. State accepted residual risk (an access token outlives a password change until it expires).

## 6. Confidentiality at rest and in transit

- **Decide:** the protection layer per confidential class (disk, database, application-level field encryption, client-held keys), and TLS on every hop.
- **Default:** TLS everywhere, including to the database. Application-level authenticated encryption (AES-GCM) only for the classes a database dump must not reveal. Say in the same paragraph that the server can still decrypt, so this is not zero-knowledge.

## 7. Keys and secrets

- **Decide:** key hierarchy, who can unwrap, rotation, destruction, and where application secrets live.
- **Default:** one data key per owner, wrapped by a managed key that the workload can use and humans cannot. Rotate the wrapping key by re-wrapping, not re-encrypting data. Destroy the owner's data key on account deletion. Secrets in a secret store, never in git.

## 8. Privacy, retention, and erasure

- **Decide:** what account deletion removes and by when, backup retention, log retention, and legal holds (GDPR Art. 17 where it applies).
- **Default:** deletion removes the owner's data and destroys the data key in the same request; backups expire on a stated schedule (for example 30 days) and are unreadable once the key is gone. That promise also needs the wrapped key to be unrecoverable from the backup; record how, or record the gap as a residual risk.

## 9. Abuse and rate limits

- **Decide:** limits per channel (authentication, general API, agents), what the client receives when limited, and bot or enumeration defences.
- **Default:** a strict per-IP and per-account limit on authentication, a general per-user limit (about 60 requests per minute), a separate configurable agent limit.

## 10. Reliability, backup, and restore

- **Decide:** availability objective, recovery point, recovery time, and whether a restore has been rehearsed.
- **Default:** 99.9% monthly as an objective with no SLA; RPO 24 hours; RTO 4 hours; one restore drill before production.

## 11. Performance and capacity

- **Decide:** the load to design for, latency objectives per operation class, and the numbers that would reopen the design.
- **Default:** p95 under 500 ms for ordinary reads and writes at the stated load, measured over 28 days. Name the per-request volume that matters most (rows one owner's request must read), not only the user count.

## 12. Cost ceiling

- **Decide:** a monthly number at the stated load, and what it forbids.
- **Default:** a ceiling the owner would pay without thinking about it. Name the always-on resources it rules out (managed load balancers, NAT gateways, multi-zone databases).

## 13. Observability and redaction

- **Decide:** what is logged, correlation, metrics, alerts, and what must never appear in logs.
- **Default:** structured logs with a request id; never log passwords, tokens, keys, or confidential values; alert on objective burn, not on every error.

## 14. Portability and internationalisation

- **Decide:** vendor lock-in accepted or refused, time zones, currencies, languages, text encoding.
- **Default:** portable across managed hosts for the database; stable error codes that clients translate; UTF-8 everywhere.

## What does not belong

Routes, payloads, tables, indexes, frameworks, and cloud products. A cloud product enters only as a stakeholder **constraint** that links its ADR ("must use a customer-managed key"). The NFR states the property ("a database dump reveals no amounts"). The mechanism becomes an ADR when reversing it is expensive.

## Sources

ISO/IEC 25010 (quality model). SEI quality attribute scenarios (Bass, Clements, Kazman). OWASP ASVS 5.0 and the Password Storage, Session Management, Cryptographic Storage, and Key Management cheat sheets. NIST SP 800-63B-4 and SP 800-57 Part 1. Google SRE book, service level objectives. AWS Well-Architected pillars. GDPR Art. 17.
