# Decision Rules

1. Evaluate mandatory gates before optional recommendations.
2. A failed mandatory gate yields `NO_GO` unless the gate is explicitly marked not applicable with evidence.
3. An unresolved critical risk yields `NO_GO`.
4. Missing or stale evidence for a mandatory gate yields `NOT_ASSESSABLE`.
5. Use `CONDITIONAL_GO` only when remaining risks are non-blocking, owned, and have tracked actions.
6. Record the rule, evidence identifiers, and rationale behind every final decision.
