CREATE TABLE IF NOT EXISTS processing_stages (
    stage_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES controller_runs(run_id) ON DELETE CASCADE,
    stage_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('running', 'completed', 'failed', 'skipped')),
    started_at TEXT NOT NULL,
    completed_at TEXT,
    records_processed INTEGER NOT NULL DEFAULT 0 CHECK (records_processed >= 0),
    error_message TEXT,
    UNIQUE (run_id, stage_name)
);