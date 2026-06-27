# 📈 QuantTrade Framework

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> An institutional-grade, Python-based algorithmic trading engine designed for automated wealth generation simulation.

## 🚀 Overview
The **QuantTrade Framework** is a highly scalable, Object-Oriented trading bot built for quantitative analysis. It utilizes a **Dual Moving Average (SMA) Crossover Strategy** to identify market trends and execute simulated trades with a strict adherence to risk management protocols.

Unlike basic scripts, this architecture is designed to mimic real-world hedge fund execution environments, ensuring that capital preservation is prioritized alongside alpha generation.

## ✨ Premium Features
* **Advanced Risk Management:** Implements dynamic position sizing. By default, it risks a maximum of 2% of total capital per trade to prevent catastrophic drawdowns.
* **Algorithmic Signal Generation:** Utilizes short-term and long-term Simple Moving Averages to output highly accurate `BUY`, `SELL`, or `HOLD` signals.
* **Object-Oriented Architecture (OOP):** Modular design makes it easy to plug in new strategies, data sources, or execution APIs.
* **Institutional Data Simulation:** Features built-in Geometric Brownian Motion mathematics to simulate realistic market price action for backtesting without needing immediate API access.
* **Production-Ready Logging:** Replaces standard print statements with professional `logging` modules for real-time monitoring and debugging.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Data Analysis:** Pandas, NumPy
* **Architecture:** OOP, Type Hinting (`typing`)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/iftu8/quant-trading-engine.git](https://github.com/iftu8/quant-trading-engine.git)
   cd quant-trading-engine
Install required dependencies:
(It is recommended to use a virtual environment)
pip install pandas numpy
Run the wealth generation protocol:
python main.py
💻 Usage Example
​Upon execution, the bot initializes with a default portfolio of $1,000,000. It will fetch data, analyze the moving averages, and execute decisions autonomously:
2026-06-28 10:00:00 - [QUANT_BOT] - INFO - Initialized WealthGeneratorBot with $1,000,000.00
2026-06-28 10:00:01 - [QUANT_BOT] - INFO - Fetching real-time data for NASDAQ:NVDA...
2026-06-28 10:00:02 - [QUANT_BOT] - INFO - EXECUTED BUY: 133.45 shares @ $149.86. Capital left: $980,000.00
📬 Contact & Creator
​Developed and maintained by @iftu8.
​Email: iftuuu69@gmail.com
​GitHub: https://github.com/iftu8
​🤝 Contributing
​Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
​⚠️ Disclaimer
​For Educational Purposes Only.
This software is for simulation and educational purposes. It does not constitute financial advice. The creator is not responsible for any financial losses incurred if this code is connected to a live brokerage API. Always backtest strategies thoroughly before deploying real capital.
