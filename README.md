# Quant Strategy Suite | Quantitative Research

The Quant Strategy Suite is a modular framework for advanced market analysis, signal generation, and statistical validation of systematic trading strategies.

## Mathematical Core Logic

The suite is built upon multi-regime mathematical frameworks to exploit market structural inefficiencies.

### Mean Reversion
Utilizes statistical arbitrage patterns based on the cointegration of asset pairs. The engine identifies temporary price dislocations from a high-probability rolling mean, enabling entries at statistically significant Z-Score thresholds.

### Momentum & Volume Analysis
Incorporates institutional volume profiles and volatility-adjusted momentum indicators (ATR-based) to identify high-conviction trend expansions and liquidity-driven breakouts.

## Backtesting Methodology (Anti-Overfitting)

To ensure institutional robustness and avoid the pitfalls of curve-fitting, the following protocols are strictly enforced:

1. **Walk-Forward Analysis (WFA)**: Continuous validation of strategy parameters on out-of-sample data.
2. **Monte Carlo Sensitivity**: Stress-testing signal performance against synthetic market noise.
3. **Slippage & Impact Modeling**: Realistic execution simulation including variable commissions and liquidity exhaustion.
4. **Data Hygiene**: Rigorous cleaning of survivorship bias and look-ahead bias from history datasets.

## Technical Components
- **Volatility Engine**: High-performance implementations of ATR and Institutional Squeeze logic.
- **Validation Notebooks**: Standardized documentation for research reproducibility.
- **Sample Dataset**: High-fidelity market data slices for initial parameter calibration.

---
**Technical Note**: This repository serves as a research workbench. Execution alpha and proprietary parameter sets are restricted.

(c) 2026 Castle Trade LLC. Proprietary and Confidential.
