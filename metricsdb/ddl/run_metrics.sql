CREATE TABLE IF NOT EXISTS run_metrics (
    metric_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES controller_runs(run_id) ON DELETE CASCADE,
    stage_id TEXT REFERENCES processing_stages(stage_id) ON DELETE SET NULL,
    metric_name TEXT NOT NULL,
    metric_value REAL NOT NULL,
    unit TEXT NOT NULL DEFAULT '',
    threshold_value REAL,
    outcome TEXT CHECK (outcome IS NULL OR outcome IN ('pass', 'fail', 'not_assessable')),
    observed_at TEXT NOT NULL,
    UNIQUE (run_id, metric_name, observed_at)
);