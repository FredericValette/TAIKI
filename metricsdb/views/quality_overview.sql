CREATE VIEW IF NOT EXISTS quality_overview AS
SELECT
    runs.run_id,
    runs.skill_id,
    runs.started_at,
    runs.completed_at,
    runs.status,
    runs.decision,
    runs.confidence,
    (SELECT COUNT(*) FROM risks WHERE risks.run_id = runs.run_id) AS risk_count,
    (SELECT COUNT(*) FROM risks WHERE risks.run_id = runs.run_id AND risks.severity = 'critical' AND risks.status <> 'closed') AS open_critical_risk_count,
    (SELECT COUNT(*) FROM actions WHERE actions.run_id = runs.run_id) AS action_count,
    (SELECT COUNT(*) FROM actions WHERE actions.run_id = runs.run_id AND actions.status IN ('open', 'in_progress', 'blocked')) AS outstanding_action_count
FROM controller_runs AS runs
