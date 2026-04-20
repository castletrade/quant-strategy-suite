# Mathematical Validation Standards | Castle Trade LLC
## Quantitative Research Division | Institutional Protocol

This document outlines the rigorous mathematical and statistical criteria required for strategy validation at Castle Trade LLC.

### 1. Statistical Significance (p-Value Thresholds)
Every mean-reversion signal must be validated via the Augmented Dickey-Fuller (ADF) test for stationarity.
- **Minimum Criteria**: p-value < 0.01 for institutional conviction.
- **Sample Integrity**: Minimum lookback periods of 500 data points to minimize variance noise.

### 2. Risk-Adjusted Performance (Sharpe & Sortino)
Raw returns are secondary to risk-adjusted stability.
- **Institutional Sharpe**: Target ratio > 2.0 (annualized).
- **Sortino Ratio**: Focus on downside deviation to ensure resilience against tail-end risks.

### 3. Cointegration Methodology
Strategy entry logic based on asset pairs must pass Engle-Granger two-step cointegration tests.
- **Residue Stationarity**: The spread must demonstrate mean-reverting properties with a defined half-life.

### 4. Backtesting Integrity Protocols
- **Slippage Modeling**: Minimum slippage padding of 1.5 basis points per transaction side.
- **Anti-Overfitting**: Mandatory Walk-Forward Analysis (WFA) with 70/30 In-Sample/Out-of-Sample split.
- **Monte Carlo Simulation**: Strategy must survive 5,000 iterations of synthetic market shuffling with < 5% risk of ruin.

---
**Technical Note**: All research must adhere to these standards before being considered for Alpha Engine integration.

(c) 2026 Castle Trade LLC. Proprietary Research Standards.
