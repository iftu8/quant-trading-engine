import numpy as np
import pandas as pd
import logging
from typing import Literal

# Premium Logging Format for Institutional Feel
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - [APEX_QUANT_ENGINE] - %(levelname)s - %(message)s'
)

class ApexQuantEngine:
    """
    An Institutional-Grade Algorithmic Trading Engine.
    Features: Multi-factor analysis (SMA, RSI, MACD) and Dynamic Risk Management.
    """
    def __init__(self, initial_capital: float, risk_per_trade: float = 0.02):
        self.capital = initial_capital
        self.risk_per_trade = risk_per_trade # Strict 2% risk limit
        self.positions = 0.0
        self.entry_price = 0.0
        logging.info(f"Initialized ApexQuant Engine with ${self.capital:,.2f}")

    def fetch_market_data(self, ticker: str) -> pd.DataFrame:
        """Simulates high-frequency institutional market data."""
        logging.info(f"Fetching high-frequency data for {ticker}...")
        dates = pd.date_range(start="2023-01-01", periods=150)
        prices = np.random.lognormal(mean=0.005, sigma=0.02, size=150).cumprod() * 250
        return pd.DataFrame({'Close': prices}, index=dates)

    def add_technical_indicators(self, data: pd.DataFrame) -> pd.DataFrame:
        """Injects institutional indicators: SMA, RSI, and MACD."""
        logging.info("Injecting Multi-Factor Technical Indicators...")
        
        # 1. Simple Moving Averages
        data['SMA_10'] = data['Close'].rolling(window=10).mean()
        data['SMA_30'] = data['Close'].rolling(window=30).mean()
        
        # 2. RSI (Relative Strength Index)
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))

        # 3. MACD (Moving Average Convergence Divergence)
        exp1 = data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = exp1 - exp2
        data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
        
        return data.dropna()

    def analyze_strategy(self, data: pd.DataFrame) -> Literal["BUY_SIGNAL", "SELL_SIGNAL", "HOLD"]:
        """Multi-Factor Alpha Generation Logic."""
        current = data.iloc[-1]
        
        # BUY LOGIC: Short > Long trend AND Not Overbought (RSI < 70) AND MACD is Bullish
        if (current['SMA_10'] > current['SMA_30']) and (current['RSI'] < 70) and (current['MACD'] > current['Signal_Line']):
            return "BUY_SIGNAL"
            
        # SELL LOGIC: Short < Long trend OR Overbought (RSI > 80) OR MACD is Bearish
        elif (current['SMA_10'] < current['SMA_30']) or (current['RSI'] > 80) or (current['MACD'] < current['Signal_Line']):
            return "SELL_SIGNAL"
            
        return "HOLD"

    def execute_trade(self, signal: str, current_price: float):
        """Executes trades with Stop-Loss and Take-Profit logic."""
        # 1. Check Stop-Loss and Take-Profit first
        if self.positions > 0:
            profit_pct = (current_price - self.entry_price) / self.entry_price
            if profit_pct <= -0.05: # 5% Stop Loss
                logging.warning(f"STOP-LOSS TRIGGERED! Down {profit_pct*100:.2f}%. Liquidating to protect capital.")
                signal = "SELL_SIGNAL"
            elif profit_pct >= 0.15: # 15% Take Profit
                logging.info(f"TAKE-PROFIT TRIGGERED! Up {profit_pct*100:.2f}%. Securing gains.")
                signal = "SELL_SIGNAL"

        # 2. Execute based on final signal
        if signal == "BUY_SIGNAL" and self.capital > 0:
            trade_amount = self.capital * self.risk_per_trade
            shares_to_buy = trade_amount / current_price
            
            self.capital -= trade_amount
            self.positions += shares_to_buy
            self.entry_price = current_price
            logging.info(f"EXECUTED BUY: {shares_to_buy:.2f} shares @ ${current_price:.2f}. Capital: ${self.capital:,.2f}")
        
        elif signal == "SELL_SIGNAL" and self.positions > 0:
            profit = self.positions * current_price
            self.capital += profit
            logging.info(f"EXECUTED SELL: Liquidated {self.positions:.2f} shares @ ${current_price:.2f}. New Capital: ${self.capital:,.2f}")
            self.positions = 0.0
            self.entry_price = 0.0
        else:
            logging.info("Market parameters neutral. Holding current positions.")

# ==========================================
# 🚀 INITIALIZE APEX ALPHA ENGINE
# ==========================================
if __name__ == "__main__":
    # Start with a Premium $5 Million Portfolio
    engine = ApexQuantEngine(initial_capital=5000000.00) 
    
    ticker = "NASDAQ:NVDA"
    
    # Process Data
    market_data = engine.fetch_market_data(ticker)
    analyzed_data = engine.add_technical_indicators(market_data)
    
    # Get latest data and execute
    latest_price = analyzed_data['Close'].iloc[-1]
    trading_signal = engine.analyze_strategy(analyzed_data)
    
    engine.execute_trade(trading_signal, latest_price)
