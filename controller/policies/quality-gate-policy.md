# Quality Gate Policy

## Decisions

- `GO`: all mandatory gates pass and no unresolved critical risk remains.
- `CONDITIONAL_GO`: no blocking gate fails, but documented actions or accepted risks remain.
- `NO_GO`: a mandatory gate fails or an unresolved critical risk blocks release.
- `NOT_ASSESSABLE`: required evidence is missing, stale, or not trustworthy enough to decide.

## Minimum Evidence

Every decision must link to dated evidence, identify the evaluated scope, and report missing inputs. A missing measurement must never be treated as a passing result.

## Overrides

Any override must include the accountable approver, rationale, timestamp, and follow-up action in the evidence pack.