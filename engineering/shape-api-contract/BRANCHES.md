# API contract branches

One entry per branch, in interview order. Each gives what to **decide** and the **default** to recommend. Defaults are recommendations, never assumptions. When the NFR doc already settles a branch (token transport, rate limits), cite it instead of asking.

## 1. Clients and transports

- **Decide:** who calls (first-party web app, mobile, third parties, AI agents), over what (REST, GraphQL, gRPC, MCP), and whether one resource model serves them all.
- **Default:** REST with JSON over HTTPS for apps; MCP as a second facade over the same operations when agents call. Hypermedia formats (JSON:API, HAL) only when a generic client really exists.

## 2. Auth transport

- **Decide:** how each client proves identity, where tokens travel, whether the web app and API share a site, and the `401` challenge.
- **Default:** bearer access token in the `Authorization` header; the browser's refresh token only in an `HttpOnly`, `Secure`, `SameSite` cookie scoped to the refresh path, rotated on use (OAuth 2.0 Security BCP, RFC 9700). Every `401` carries `WWW-Authenticate` (RFC 9110). Confirm the sites match, because a `SameSite=Strict` cookie is not sent on cross-site requests. For MCP, the spec's OAuth-based authorization, or deferred with the v1 behaviour stated.

## 3. Resource model

- **Decide:** the nouns, their nesting under the ownership unit, and which computed figures are read-only views.
- **Default:** resource-oriented design (Google AIP-121): plural nouns, nested under the owner resource, one schema per resource used by every method. Computed figures are GET views, never stored resources.

## 4. Field behaviour

- **Decide:** for each field, whether it is required, optional, immutable, or output-only (AIP-203); what omission and `null` mean on update; what unknown fields do.
- **Default:** partial update where omission means unchanged; `null` clears only where the spec defines clearing; unknown fields are refused. Small related objects (a name beside an id) are embedded on read, not expanded on demand.

## 5. Standard methods

- **Decide:** status codes and bodies for get, list, create, update, delete.
- **Default:** create returns `201` with the resource and `Location`; update returns `200` with the full resource; delete returns `204`. The server assigns ids. A DELETE carries no body (RFC 9110 gives it no semantics), so password-confirmed deletes are a POST.

## 6. Custom actions

- **Decide:** operations a standard method would misdescribe: bulk changes, state transitions with side effects, generating many items at once.
- **Default:** `POST` on a verb sub-path (AIP-136), all-or-nothing. Partial success (`207`) only when the user asked for it.

## 7. Lists: filters, sort, pagination

- **Decide:** required and optional filters, the sort order, and pagination or a maximum.
- **Default:** a stable documented sort. Cursor pagination with an opaque token for anything that can grow, because adding pagination later breaks existing clients (AIP-158). A list that stays unpaginated states a hard maximum size.

## 8. Errors

- **Decide:** the error body, how clients identify a problem, validation detail, and non-disclosure.
- **Default:** RFC 9457 problem details (`application/problem+json`) with a stable identifier per problem: a `type` URI, or a `code` extension when `type` stays `about:blank` (say which one clients branch on). Validation errors list each field as a JSON Pointer. `detail` is human text, never parsed. A resource owned by someone else returns `404`, never `403`. Catalogue `400`, `401`, `403`, `404`, `409`, `415`, `422`, `429`, and `500`.

## 9. Idempotency and concurrency

- **Decide:** protection against double-submits on non-idempotent POSTs, and against lost updates.
- **Default:** an `Idempotency-Key` header on creating POSTs (IETF draft, Stripe behaviour): scoped to user, method, and path; stored with a published request fingerprint for 24 hours; a replay returns the stored status and body; the same key with a different body is refused; a concurrent duplicate gets `409`; validation failures are not stored. Concurrency is last-write-wins in v1, stated as accepted, or `ETag` with `If-Match`.

## 10. Versioning and change

- **Decide:** the versioning scheme and what counts as breaking.
- **Default:** a major version in the path (`/api/v1`), additive changes only within it. Breaking means: a removed or retyped field, a changed default sort or page size, a changed error identifier. `Deprecation` and `Sunset` headers when a successor ships.

## 11. Formats: ids, casing, money, dates

- **Decide:** id format, JSON casing, money representation, calendar dates versus instants, time zones.
- **Default:** UUID strings; camelCase. Money as a decimal string (`"1200.50"`) or integer minor units, never a JSON number, because JavaScript parses numbers as binary floating point. The currency appears once per response when it is uniform. Calendar dates as `YYYY-MM-DD` with no zone; instants as ISO 8601 UTC; zones as IANA names.

## 12. Limits, CORS, and headers

- **Decide:** rate-limit responses, allowed origins and headers, request size limits.
- **Default:** `429` with `Retry-After`; CORS allows the web origin with credentials and the custom headers in use (`Authorization`, `Idempotency-Key`). Numeric limits come from the NFR doc or go to **Open points**.

## 13. Agent tools

- **Decide:** which operations agents can reach, tool granularity, input and output schemas, and how errors surface.
- **Default:** about one tool per use case, grouped by a `kind` parameter where resources share a shape; each tool carries `readOnlyHint`, `destructiveHint`, and `idempotentHint`, and maps problem details to a tool error. Account, credential, and destructive settings operations stay off the agent surface. The agent never passes an owner id; the server resolves it from the credential.

## 14. Machine-readable description

- **Decide:** whether an OpenAPI 3.1 description ships with the contract, and which is authoritative.
- **Default:** prose only at this stage. The prose is the decision record. An OpenAPI file is generated during implementation and checked against this doc.

## Sources

Google AIP (121, 130–136, 158, 193, 203). Microsoft REST API Guidelines. Zalando RESTful API Guidelines. RFC 9110 (HTTP semantics). RFC 9457 (problem details). RFC 9700 (OAuth 2.0 Security BCP). IETF `Idempotency-Key` header draft. Stripe API reference (idempotency, versioning). OpenAPI 3.1. Model Context Protocol specification (tools, authorization).
