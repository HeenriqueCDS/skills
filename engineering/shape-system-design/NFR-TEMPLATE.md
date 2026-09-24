# `docs/non-functional-requirements.md` template

```markdown
# Non-functional requirements

<Opening paragraph: this doc states quality properties and the threat model behind them. Behaviour
lives in docs/spec.md. Mechanisms that are expensive to reverse live in docs/adr/. Routes, tables,
and modules live in later docs.>

<Whimsical link to the system context diagram, when one was drawn.>

## 1. Quality profile
One line per ISO/IEC 25010 characteristic: in scope (with the section that covers it) or out of
scope (with the reason). Functional suitability points at docs/spec.md.

## 2. Context and threat model
Load, jurisdictions, and a Mermaid system context diagram: actors, the system, external systems,
trust boundaries. Then a table: threat actor × data class → can read? (yes / no / accepted risk).

## 3. Data classification
| Class | Examples | Confidentiality | Integrity | Retention | Deletion | Logs | Backups |

## 4. Security requirements
ASVS version and target level. Per chapter: each requirement adopted, not applicable, or waived.
Scenarios for anything ASVS does not quantify.

## 5. Waivers and residual risk
Each waiver: the requirement, the accepted threat, the compensating control, the owner.

## 6. Privacy, retention, and erasure

## 7. Service levels
| Indicator | Objective | Window | Consequence ("no SLA" when none) |

## 8. Capacity and performance
Stated load, latency scenarios, and the numbers that reopen the design.

## 9. Cost ceiling
Monthly number at the stated load, and what it rules out.

## 10. Observability and redaction

## 11. Backup and recovery
RPO, RTO, restore drill.

## 12. Abuse limits

## 13. Portability and internationalisation

## 14. Constraints
Stakeholder-imposed products or standards, each linking its ADR.

## 15. Handoff
Answers that belong to later stages, grouped by stage.

## 16. Open points
```
