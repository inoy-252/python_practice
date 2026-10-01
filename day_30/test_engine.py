"""
day_30/test_engine.py - Automated Unit Test Suite for AI Engine.
Verifies decision boundaries, edge-cases, and score bounding.
"""

import sys
from pathlib import Path
import unittest

# Ensure Python looks inside day_30 for engine.py regardless of where the test is run from
sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine import predict_health_risk


class TestHealthAIEngine(unittest.TestCase):
    def test_healthy_young_patient(self):
        """Test ideal biomarkers produce Low Risk."""
        result = predict_health_risk(age=24, bmi=22.0, heart_rate=68)
        self.assertEqual(result["risk_level"], "Low Risk (Optimal)")
        self.assertLess(result["risk_score"], 30.0)
        self.assertGreaterEqual(result["confidence"], 90.0)

    def test_critical_bradycardia_emergency(self):
        """Test heart rate < 45 triggers severe emergency penalty."""
        result = predict_health_risk(age=30, bmi=22.0, heart_rate=25)
        self.assertGreaterEqual(result["risk_score"], 45.0)
        self.assertIn("Risk", result["risk_level"])

    def test_score_never_exceeds_100(self):
        """Test extreme biomarkers never breach the 100% ceiling."""
        result = predict_health_risk(age=75, bmi=42.0, heart_rate=120)
        self.assertLessEqual(result["risk_score"], 100.0)
        self.assertEqual(result["risk_level"], "High Risk (Action Recommended)")


if __name__ == "__main__":
    unittest.main()
