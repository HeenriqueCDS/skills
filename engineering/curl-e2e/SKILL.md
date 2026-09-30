---
name: curl-e2e
description: Probe a running HTTP API with curl and print each case in a terminal table. Use when the user wants a curl check of a route, or the side effect that route produced.
---

# Probe

A **probe** is one curl against the running app, plus the side effect that proves it. The side effect is whatever this project records: a stored record, a sent message, a queued job, a file, a log line, or an error body. The probe checks the running app, which unit tests do not start. It reads this repo's contract and start command, sends the requests, and reports through the `scripts/table.py` next to this file.

## 1. Name the cases

Read the route from the contract this repo already has: `docs/api-contract.md`, an OpenAPI document, or the route definition. Take the method, path, success status, and the error the contract names. Each case is one request and the evidence that passes it. A value the case creates (an address, a name, an idempotency key) is unique to that case, so the evidence is this case's record.

Done when: every case is one line, and that line names the request and the evidence.

## 2. Raise the stack

Read how this repo starts: the README, the task runner, or the compose file. Start the local development stack that serves the route. Run a setup step (install, migrate, seed) only when that documentation lists it before the app can serve traffic. When the repo documents an example env file and the real one is absent, copy the example.

When this repo's app is already listening and its health check passes, reuse it. When a port the stack needs is held by a leftover process this repo started, stop that leftover and start again. When an unrelated process holds the port, leave it. The health check is the one this repo documents. When it documents none, the app is up once its port accepts connections. Keep the app log.

Done when: either the health check passes and the app log is captured, or a blocked port is named and every case is already a `fail` row.

## 3. Send the probe

Send the cases in the order from step 1. Use the headers, body, and auth the contract names. Record the status code, the body length in bytes, and the content type. A success with no body has length 0.

**Side effect.** When the case writes a side effect, read it through the interface this repo already exposes: a query, a mailbox API, a queue, a file, or a log line. Compare the stored value to the contract (a status field, a hash prefix, a recipient, a subject). Quote from the log only the method, the path, and the status. A password, token, session, or connection string stays out of the log quote and out of the table.

A failed case stays a failed row. Continue with the remaining cases.

Done when: every case from step 1 has a status and its evidence, and any log quote is method, path, and status only.

## 4. Stop what this probe started

Stop the app process this probe started. Leave a process that was already running, and leave dependency services running.

Done when: every process this probe started is stopped, and anything it found already running is still up.

## 5. Report

From the directory that contains this `SKILL.md`, render the report with `scripts/table.py`. One TSV row per case, six fields separated by tabs:

`case`, `request`, `result`, `status`, `bytes`, `evidence`

- `request` is the method and path, such as `POST /users`.
- `result` is `pass` or `fail`.
- `status` is the HTTP status code, or `-` when the request was not sent.
- `bytes` is the body length, or `-` when the request was not sent.
- `evidence` is one short ASCII line: a non-secret proof (a hash prefix, a field value, an error code) or the reason the request was not sent.

```bash
python3 scripts/table.py --footer "App port free. Dependencies left running." <<'EOF'
register new user	POST /users	pass	201	0	record stored
duplicate email	POST /users	fail	409	96	error code email_taken
EOF
```

That command prints:

```
┌───────────────────┬─────────────┬────────┬────────┬───────┬────────────────────────┐
│ Case              │ Request     │ Result │ Status │ Bytes │ Evidence               │
├───────────────────┼─────────────┼────────┼────────┼───────┼────────────────────────┤
│ register new user │ POST /users │ pass   │    201 │     0 │ record stored          │
│ duplicate email   │ POST /users │ fail   │    409 │    96 │ error code email_taken │
└───────────────────┴─────────────┴────────┴────────┴───────┴────────────────────────┘

App port free. Dependencies left running.
```

Show the script's stdout in one fenced block, unchanged. The footer states whether the app port is free and whether dependency services are still up. When the user asked to read a message, print its text under that block.

Done when: the fenced block is the script's stdout, with one data row per case from step 1, and the footer states the app port and the dependency services.
