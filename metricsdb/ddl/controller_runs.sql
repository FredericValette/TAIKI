CREATE TABLE IF NOT EXISTS controller_runs (
    run_id TEXT PRIMARY KEY,
    skill_id TEXT NOT NULL,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('completed', 'failed', 'not_assessable')),
    decision TEXT NOT NULL CHECK (decision IN ('GO', 'CONDITIONAL_GO', 'NO_GO', 'NOT_ASSESSABLE')),
    confidence REAL CHECK (confidence IS NULL OR confidence BETWEEN 0 AND 1),
    scope TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);