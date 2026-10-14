from collections.abc import Mapping


_KNOWN_GATE_RESULTS = {"pass", "fail", "conditional", "missing", "stale", "not_assessable"}


def decide_quality_gate(
    mandatory_gate_results: Mapping[str, str],
    unresolved_critical_risk: bool = False,
) -> str:
    """Return the auditable release decision for mandatory gate results."""
    if not mandatory_gate_results:
        return "NOT_ASSESSABLE"

    results = tuple(mandatory_gate_results.values())
    if unresolved_critical_risk or "fail" in results:
        return "NO_GO"

    if any(result not in _KNOWN_GATE_RESULTS for result in results):
        return "NOT_ASSESSABLE"

    if any(result in {"missing", "stale", "not_assessable"} for result in results):
        return "NOT_ASSESSABLE"

    if "conditional" in results:
        return "CONDITIONAL_GO"

    return "GO"