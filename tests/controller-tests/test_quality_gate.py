import unittest

from controller.quality_gate import decide_quality_gate


class QualityGateDecisionTests(unittest.TestCase):
    def test_empty_gate_results_are_not_assessable(self):
        self.assertEqual(decide_quality_gate({}), "NOT_ASSESSABLE")

    def test_missing_mandatory_evidence_is_not_assessable(self):
        self.assertEqual(
            decide_quality_gate({"security": "pass", "rollback": "missing"}),
            "NOT_ASSESSABLE",
        )

    def test_failed_mandatory_gate_is_no_go(self):
        self.assertEqual(
            decide_quality_gate({"security": "fail", "regression": "pass"}),
            "NO_GO",
        )

    def test_unresolved_critical_risk_is_no_go(self):
        self.assertEqual(
            decide_quality_gate({"security": "pass"}, unresolved_critical_risk=True),
            "NO_GO",
        )

    def test_conditional_gate_result_is_conditional_go(self):
        self.assertEqual(
            decide_quality_gate({"security": "pass", "performance": "conditional"}),
            "CONDITIONAL_GO",
        )

    def test_all_mandatory_gates_passing_is_go(self):
        self.assertEqual(
            decide_quality_gate({"security": "pass", "regression": "pass"}),
            "GO",
        )


if __name__ == "__main__":
    unittest.main()