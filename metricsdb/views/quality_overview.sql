CREATE VIEW IF NOT EXISTS quality_overview AS
SELECT
    runs.run_id,
    runs.skill_id,
    runs.started_at,
    runs.completed_at,
    runs.status,
    runs.decision,
    runs.confidence,
    COUNT(DISTINCT risks.risk_id) AS risk_count,
    SUM(CASE WHEN risks.severity = 'critical' AND risks.status <> 'closed' THEN 1 ELSE 0 END) AS open_critical_risk_count,
    COUNT(DISTINCT actions.action_id) AS action_count,
    SUM(CASE WHEN actions.status IN ('open', 'in_progress', 'blocked') THEN 1 ELSE 0 END) AS outstanding_action_count
FROM controller_runs AS runs
LEFT JOIN risks ON risks.run_id = runs.run_id
LEFT JOIN actions ON actions.run_id = runs.run_id
GROUP BY runs.run_id;