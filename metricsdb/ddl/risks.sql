CREATE TABLE IF NOT EXISTS risks (
    risk_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES controller_runs(run_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    severity TEXT NOT NULL CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    likelihood TEXT NOT NULL CHECK (likelihood IN ('unlikely', 'possible', 'likely', 'almost_certain')),
    status TEXT NOT NULL CHECK (status IN ('open', 'mitigating', 'accepted', 'closed')),
    owner TEXT,
    mitigation TEXT NOT NULL DEFAULT ''
);