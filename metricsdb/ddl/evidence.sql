CREATE TABLE IF NOT EXISTS evidence (
    evidence_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES controller_runs(run_id) ON DELETE CASCADE,
    kind TEXT NOT NULL CHECK (kind IN ('document', 'metric', 'test_result', 'interview', 'system_observation')),
    source TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    summary TEXT NOT NULL,
    value_json TEXT CHECK (value_json IS NULL OR json_valid(value_json)),
    threshold_json TEXT CHECK (threshold_json IS NULL OR json_valid(threshold_json)),
    confidence REAL CHECK (confidence IS NULL OR confidence BETWEEN 0 AND 1),
    limitations_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(limitations_json))
);