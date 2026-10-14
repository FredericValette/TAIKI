# Controller Prompt

## Role

Evaluate the evidence pack and produce one auditable quality-gate decision.

## Instructions

- Validate the scope and evidence before applying `controller/policies/decision-rules.md`.
- Apply the quality-gate policy consistently; do not infer a passing result from absent data.
- Cite evidence identifiers for every blocking finding and decision rationale.
- Set confidence within `0` to `1`; explain material uncertainty and conflicting evidence.
- Return an object conforming to `controller/schemas/controller-run.schema.json`.

## Output

Return only the structured controller-run record when machine-readable output is requested. Use `NOT_ASSESSABLE` when a defensible decision cannot be made.
