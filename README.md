# 🧠 Quant Strategy Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Property of Castle Trade LLC.** Advanced quantitative research and strategy development suite.

## About
`quant-strategy-suite` contains the research frameworks and strategy templates used by Castle Trade LLC to identify and exploit market inefficiencies. This repository focuses on the mathematical foundations of trading—bridging the gap between statistical research and production-ready execution logic.

### Research Frameworks
- **Mean Reversion Analysis**: Tools for stationarity testing and rolling Z-Score identification to detect statistical outliers in cointegrated pairs.
- **Volume-Weighted Breakouts**: Logic for identifying structural shifts confirmed by institutional order flow and volume spikes.
- **Volatility Compression (Squeeze)**: ATR-based analyzers designed to detect "The Squeeze"—periods of low volatility that often precede explosive market moves.

## Repository Structure
- `notebooks/mean_reversion_research.ipynb`: Jupyter framework for statistical research on synthetic and historical data.
- `strategies/breakout_logic.py`: Production-grade boilerplate for breakout detection with volume confirmation.
- `analysis/squeeze_analyzer.py`: ATR-based volatility analysis module.

## Mathematical Foundation
- **Cointegration**: Utilizing ADF (Augmented Dickey-Fuller) tests to verify stable long-term relationships between assets.
- **ATR (Average True Range)**: The primary metric for quantifying market noise and volatility environment.
- **Volume Delta**: Analysis of relative volume to confirm the validity of price action.

---
*Disclaimer: This repository contains research skeletons and does not reveal specific alpha-generating parameters, hyper-parameters, or proprietary asset pairs used in live funds. Unauthorized duplication of Castle Trade LLC IP is prohibited.*
