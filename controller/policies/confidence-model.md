# Confidence Model

Confidence is a value from `0` to `1` describing how strongly the available evidence supports a finding. It is not a probability of release success.

Assess confidence from evidence quality, recency, coverage of the requested scope, and independent corroboration. Record material limitations with the finding. Missing or contradictory evidence lowers confidence; it must not be silently averaged away.

The controller must return `NOT_ASSESSABLE` when evidence is insufficient to support a defensible gate decision, regardless of the numeric confidence value.