"""
Test Suite: Quantitative Metrics Validation
Purpose: Verifies the integrity of Sharpe Ratio and Maximum Drawdown calculations.
Copyright: (c) 2026 Castle Trade LLC. Quantitative Research Infrastructure.
"""

import unittest
import numpy as np
import pandas as pd
from typing import List

class TestQuantitativeMetrics(unittest.TestCase):
    """
    Unit tests ensuring the mathematical accuracy of institutional risk-adjusted 
    performance metrics.
    """

    def setUp(self) -> None:
        """Initializes high-fidelity synthetic return series for testing."""
        # 1% daily return over 10 days
        self.returns: pd.Series = pd.Series([0.01] * 10)
        self.prices: pd.Series = pd.Series([100 * (1.01**i) for i in range(11)])

    def test_sharpe_ratio_calculation(self) -> None:
        """Validates annualized Sharpe Ratio logic under constant returns."""
        annual_factor: float = np.sqrt(252)
        mean_return: float = self.returns.mean()
        std_return: float = self.returns.std()
        
        # In a constant return scenario, std is 0; handle edge cases for robustness
        sharpe: float = (mean_return / std_return * annual_factor) if std_return != 0 else 0.0
        
        self.assertIsInstance(sharpe, float)
        self.assertEqual(sharpe, 0.0) # Correct for zero variance

    def test_drawdown_integrity(self) -> None:
        """Ensures the Maximum Drawdown algorithm correctly identifies equity peaks."""
        declining_prices: pd.Series = pd.Series([100, 110, 90, 80, 105])
        rolling_max: pd.Series = declining_prices.cummax()
        drawdowns: pd.Series = (declining_prices - rolling_max) / rolling_max
        max_dd: float = float(drawdowns.min())
        
        # Expected max drawdown from 110 to 80 is approx -27.27%
        self.assertLess(max_dd, -0.27)
        self.assertGreater(max_dd, -0.28)

if __name__ == "__main__":
    unittest.main()
