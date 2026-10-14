import sqlite3
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DDL_ORDER = (
    "controller_runs.sql",
    "processing_stages.sql",
    "run_metrics.sql",
    "evidence.sql",
    "risks.sql",
    "actions.sql",
)


class MetricsDbIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.database = sqlite3.connect(":memory:")
        self.database.execute("PRAGMA foreign_keys = ON")
        for filename in DDL_ORDER:
            script = ROOT / "metricsdb" / "ddl" / filename
            self.database.executescript(script.read_text(encoding="utf-8"))
        view = ROOT / "metricsdb" / "views" / "quality_overview.sql"
        self.database.executescript(view.read_text(encoding="utf-8"))

    def tearDown(self):
        self.database.close()

    def test_quality_overview_summarizes_run_risks_and_actions(self):
        self.database.execute(
            "INSERT INTO controller_runs (run_id, skill_id, started_at, status, decision) VALUES (?, ?, ?, ?, ?)",
            ("run-1", "release-readiness-dqa", "2026-10-14T09:00:00Z", "completed", "NO_GO"),
        )
        self.database.execute(
            "INSERT INTO risks (risk_id, run_id, title, severity, likelihood, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("risk-1", "run-1", "Critical exposure", "critical", "likely", "open"),
        )
        self.database.execute(
            "INSERT INTO actions (action_id, run_id, related_risk_id, title, priority, status) VALUES (?, ?, ?, ?, ?, ?)",
            ("action-1", "run-1", "risk-1", "Mitigate exposure", "critical", "in_progress"),
        )
        row = self.database.execute(
            "SELECT decision, risk_count, open_critical_risk_count, action_count, outstanding_action_count FROM quality_overview WHERE run_id = ?",
            ("run-1",),
        ).fetchone()
        self.assertEqual(row, ("NO_GO", 1, 1, 1, 1))

    def test_foreign_keys_reject_orphaned_evidence(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.database.execute(
                "INSERT INTO evidence (evidence_id, run_id, kind, source, observed_at, summary) VALUES (?, ?, ?, ?, ?, ?)",
                ("evidence-1", "missing-run", "document", "test", "2026-10-14T09:00:00Z", "orphan"),
            )

    def test_quality_overview_does_not_multiply_risk_or_action_counts(self):
        self.database.execute(
            "INSERT INTO controller_runs (run_id, skill_id, started_at, status, decision) VALUES (?, ?, ?, ?, ?)",
            ("run-2", "release-readiness-dqa", "2026-10-14T09:00:00Z", "completed", "NO_GO"),
        )
        self.database.executemany(
            "INSERT INTO risks (risk_id, run_id, title, severity, likelihood, status) VALUES (?, ?, ?, ?, ?, ?)",
            [
                ("risk-2", "run-2", "Critical A", "critical", "likely", "open"),
                ("risk-3", "run-2", "Critical B", "critical", "possible", "open"),
            ],
        )
        self.database.executemany(
            "INSERT INTO actions (action_id, run_id, title, priority, status) VALUES (?, ?, ?, ?, ?)",
            [
                ("action-2", "run-2", "Action A", "high", "open"),
                ("action-3", "run-2", "Action B", "medium", "in_progress"),
                ("action-4", "run-2", "Action C", "low", "done"),
            ],
        )
        row = self.database.execute(
            "SELECT risk_count, open_critical_risk_count, action_count, outstanding_action_count FROM quality_overview WHERE run_id = ?",
            ("run-2",),
        ).fetchone()
        self.assertEqual(row, (2, 2, 3, 2))


if __name__ == "__main__":
    unittest.main()